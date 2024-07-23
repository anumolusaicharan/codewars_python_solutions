#Instructions
# Link --> https://www.codewars.com/kata/5a9e86705ee396d6be000091

#Given an array with exactly 5 strings "a", "b" or "c" (chars in Java, characters in Fortran), check if the array contains three and two of the same values.

#Examples
#["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
#["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
#["a", "a", "a", "a", "a"] ==> false // 5x "a"


def check_three_and_two(array):

    count_a = array.count('a')
    count_b = array.count('b')
    count_c = array.count('c')
    
    if (count_a==3 or count_b==3 or count_c == 3) and (count_a == 2 or count_b==2 or count_c==2):
        return True
    else:
        return False

#Learn : The count() method is used to count the occurence of a element in a list,Tuples,Strings
