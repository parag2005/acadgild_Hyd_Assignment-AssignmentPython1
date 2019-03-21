from pip._vendor.distlib.compat import raw_input

def evaluate_vowel(input_string):
     if (len(input_string) is 1):
          enter_character = input_string
          if enter_character == 'a' or enter_character == 'e' or enter_character == 'i' or enter_character == 'o' or enter_character == 'u':
               return True
          else:
               return False
     else:
          print('The length of the entered string is greater than 1\n')
          return None

input_string = raw_input('Please enter  a character to evaluate whether it is a vowel ? ')
print("The character entered is a vowel", evaluate_vowel(input_string))
