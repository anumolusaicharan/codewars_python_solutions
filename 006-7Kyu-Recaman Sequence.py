#Link --> https://www.codewars.com/kata/5c3f31c2460e9b4020780aa2

#Instructions:
#Return the nth term of the Recamán's sequence.

# a(0) = 0;

#        a(n-1) - n, if this value is positive and not yet in the sequence
#      /
# a(n) <
#      \
#        a(n-1) + n, otherwise

# input range: 0 – 30 000

def recaman(n):
    seq = [0,1]
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2,n+1):
            
            if (seq[i-1] - i) > 0 and (seq[i-1]-i) not in seq:
                seq.append(seq[i-1]-i)
            else:
                seq.append(seq[i-1]+i)
        return seq[n]

       
