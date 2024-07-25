#Link --> https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

#Instructions
# Implement the function unique_in_order which takes as argument a sequence 
# and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

#For example:
#unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
#unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence):
    output = []
    if len(sequence) == 0:
        return list(sequence)
    else:
        output.append(sequence[0])
        for i in range(1,len(sequence)):
            if sequence[i] != sequence[i-1]:
                output.append(sequence[i])
        return output

