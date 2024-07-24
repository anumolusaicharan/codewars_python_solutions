#Link --> https://www.codewars.com/kata/54a91a4883a7de5d7800009c/python
#Instructions
#Your job is to write a function which increments a string, to create a new string.

#If the string already ends with a number, the number should be incremented by 1.
#If the string does not end with a number. the number 1 should be appended to the new string.

#Examples:
#foo -> foo1
#foobar23 -> foobar24
#foo0042 -> foo0043
#foo9 -> foo10
#foo099 -> foo100

def increment_string(strng):
    digit = ('0','1','2','3','4','5','6','7','8','9')
    if strng.endswith(digit):
        last_num = int(strng[-1])
        if last_num == 9:
            return increment_string(strng[:-1]) + '0'
        else:
            strng = strng[:-1] + str(last_num+1)
    else:
        strng = strng + '1'
    return strng
