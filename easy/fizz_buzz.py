import sys

a = []
b = []
n = []

input = open(sys.argv[1], 'r')

for line in input:
    # get a, b, n
    l = line.split(' ')
    a.append(int(l[0]))
    b.append(int(l[1]))
    n.append(int(l[2]))

input.close()

for i in xrange(2):
    for j in xrange(1, n[i]+1):
        if j % a[i] == 0 and j % b[i] == 0:
            sys.stdout.write('FB')
        elif j % a[i] == 0:
            sys.stdout.write('F')
        elif j % b[i] == 0:
            sys.stdout.write('B')
        else:
            sys.stdout.write(str(j))
        if j != n[i]:
            sys.stdout.write(' ')
    if i == 0:
        sys.stdout.write('\n')
