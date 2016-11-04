#MEAN result = 55.1009090909
#data1 =[49,66,24,98,27,56,93,68,78,22,25.11]
#def mean(data):
  #return sum (data1)/len (data1)
#print mean(data1)

#MEDIAN result = 2
#data1 = [1,2,5,10,-20]
#def median(data):
#    sdata = sorted(data)
#    index = (len(data)-1)/2
#    return sdata[index]
#print median(data1)

#MODE result = 5
#data1 = [1,2,5,10,-20,5,5]
#def mode(data):
    #modecnt=0
    #for i in range(len(data)):
    #    icount = data.count(data[i])
    #if icount > modecnt:
    #    mode =data [i]
    #    modecnt = icount
    #return mode
#print mode(data1)

#Complete the variance function to make it return the variance of a list of numbers
# Result is 62.572884
data2=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]
def mean(data):
    return sum(data)/len(data)

def variance(data):
    #Insert your code here
    mu = mean(data)
    ndata = []
    for i in range(len(data)):
        ndata.append((data[i] - mu)**2)
    sigma2 = mean(ndata)
    return sigma2
print variance(data2)

# or
data2=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]
def mean(data):
    return sum(data)/len(data)

def variance(data):
    mu=mean(data)
    return mean([(x-mu)**2 for x in data])
print variance (data2)

#Complete the stddev function to make it return the standard deviation
#of a list of numbers
#result is 7.91030239624
from math import sqrt

data3=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]

def mean(data):
    return sum(data)/len(data)
def variance(data):
    mu=mean(data)
    return mean([(x-mu)**2 for x in data])
def stddev(data):
    #Insert your code here
    return sqrt(variance(data))
print stddev(data3)
