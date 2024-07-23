#Link --> https://www.codewars.com/kata/57a06b07cf1fa58b2b000252

#Write a function, isItLetter or is_it_letter or IsItLetter, which tells us if a given character is a letter or not.

def is_it_letter(s):
    return True if s.isalpha() else False

#Learn:
# text.isalpha() --> Checks if all characters in the text are Alphabets.
# text.isdigit() --> Checks if all characters in the text are Digits.
# text.isalnum() --> Checks if all characters in the string are alphanumeric (letters or numbers).
# text.islower() --> Checks if all characters in the text are Lower case or not.
# text.isupper() --> Checks if all characters in the text are Upper case or not.
