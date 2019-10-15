import numpy
import time

data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')

max_inflammation_0 = numpy.max(data, axis=0)[0]
max_inflammation_20 = numpy.max(data, axis=0)[20]

if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print('Suspicious looking maxima!')
elif numpy.sum(numpy.min(data, axis=0)) == 0:
    print('Minima add up to zero!')
else:
    print('Seems OK!')

print('----time----')
print(time.ctime())
print('----ANOTHER TEST----')
print(data[0:4, 0:10])
print('--------')