
def longestWord(input_string):
     max_length_word = 0
     list_of_words = list(input_string.split())

     for counter in range(0,len(list_of_words)):
        if (max_length_word < len(list_of_words[counter])):
            longest_word = list_of_words[counter]
            max_length_word = len(list_of_words[counter])

     return longest_word

input_string = input('Please enter the string to be split to a list ? ')
print("The longest word in the sentence is \n")
print(longestWord(input_string))



