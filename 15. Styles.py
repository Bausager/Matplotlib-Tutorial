import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates
from matplotlib import style

style.use('fast')
print(plt.style.available) #Deffient styles in matplot.
print(plt.__file__) #The dirotory for the style files (you can modify it.(Back it up when updating))


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    

def graph_data(stock):
    
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          # %Y = full year. 2015
                                                          # %y = partial year 15
                                                          # %m = number month
                                                          # %d = number day
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          # 12-06-2014
                                                          # %m-%d-%Y
                                                          converters={0: bytespdate2num('%Y-%m-%d')})

    ax1.plot_date(date, closep,'-', label='Price')
    
    ax1.fill_between(date, closep, closep[0], where=(closep > closep[0]), facecolor='g', alpha=0.5) #alpha makes it see-though
    ax1.fill_between(date, closep, closep[0], where=(closep < closep[0]), facecolor='r', alpha=0.5)
   # ax1.grid(True,
    #         color='g',
     #        linestyle='-',
      #       linewidth=0.5)
    #ax1.axhline(closep[0], color='k', linewidth=5)
    
#    ax1.xaxis.label.set_color('c')
#    ax1.yaxis.label.set_color('r')
    
    #ax1.set_yticks([0,200,400,600])
    #ax1.tick_params(axis='x', color='r')
    
    
    #ax1.spines['left'].set_color('c')
    #ax1.spines['right'].set_visible(False)
    #ax1.spines['top'].set_visible(False)
    
    #ax1.spines['left'].set_linewidth(5)
    
    
    #for label in ax1.xaxis.get_ticklabels():
        #label.set_rotation(45)
        
        

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('STOCK')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data('ebay')