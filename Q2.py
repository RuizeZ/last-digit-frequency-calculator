'''
RuizeZ
4/10/2020

Calculate the frequency of the last digit of the stock price, and do an empirical study to find out what the last and most freuemt digit is
'''
import random
from collections import Counter
stockprice_list = []
lastdigit_list = []
stock = 1000
#Randomly generate stock prices
for i in range(stock):
    stockprice = random.randrange(0,500)
    lastdigit = stockprice % 10
    stockprice_list.append(stockprice)
    lastdigit_list.append(lastdigit)
digit_count = dict(Counter(lastdigit_list))
print("stockprice:",stockprice_list)
print("digit_count:",digit_count)

#Calculate the frequency of each last digit
for i in digit_count: 
    print( "% s 's frequency is: % s" % (i, digit_count[i]/stock), end ="\n")

#Find the last digit that appears the most
most = max(digit_count.values())
most_list = []
for i in digit_count:
    if digit_count[i] == most:
        most_list.append(i)
print("The most frequent digit is:", *most_list)

#Find the last digit that appears the least
least = min(digit_count.values())
least_list = []
for i in digit_count:
    if digit_count[i] == least:
        least_list.append(i)
print("The least frequent digit is:", *least_list)



