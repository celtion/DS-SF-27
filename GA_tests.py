n = 75
i = 2
#uses 2 while loops.
while i * i < n: #outer loop states while i * i isn't great than n, add 1 to i #after the inner loop runs
    while n%i == 0: #while i divides evenly into n, replace n with n divided by i
        n = n / i
    i = i + 1
print n
# for n = 20 and i=2, n is replaced by 10, then again by 5.
#because 2 doesn't evely divide into 5, the loop stops with n=5 and the
# outer loop finishes, producing i+1=3
#finally, b/c 3 squared is greater than 5, the outer loop no long TRUE
