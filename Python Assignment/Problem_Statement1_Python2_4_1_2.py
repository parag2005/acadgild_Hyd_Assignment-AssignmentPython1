from pip._vendor.distlib.compat import raw_input


def filter_long_words(input_string,words_longer_than_n):
     list_of_words = list(input_string.split())
     list_of_words_longerThan_n = list()

     for counter in range(0,len(list_of_words)):
        if (words_longer_than_n < len(list_of_words[counter])):
            list_of_words_longerThan_n.append(list_of_words[counter])

     return list_of_words_longerThan_n

input_string = raw_input('Please enter the string to be split to a list ? ')
n = int(raw_input('Enter an integer length of words ? '))
print(filter_long_words(input_string,n))
