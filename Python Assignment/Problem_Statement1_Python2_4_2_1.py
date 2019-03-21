from pip._vendor.distlib.compat import raw_input

def map_length_of_words(input_string):
     list_of_words = list(input_string.split())
     list_of_length_of_words = list()

     for counter in range(0,len(list_of_words)):
          list_of_length_of_words.append(len(list_of_words[counter]))

     return list_of_length_of_words

input_string = raw_input('Please enter the string to be split to a list ? ')
print(map_length_of_words(input_string))
