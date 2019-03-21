from pip._vendor.distlib.compat import raw_input


subjects_of_sentence = raw_input('Please enter  a set of words to define the subject words ? ')
""" The first set of words includes ["American","Indians"] """
verbs_of_sentence = raw_input('Please enter  a set of words to define the verb words ? ')
""" The second set of words includes ["play","watch"] """
objects_of_sentence = raw_input('Please enter  a set of words to define the object words of sentence ? ')
""" The third set of words include ["Baseball","Cricket"] """

list1 = list(subjects_of_sentence.split())
list2 = list(verbs_of_sentence.split())
list3 = list(objects_of_sentence.split())
separator = " "

for subject_index in range(0,len(list1)):
     for verb_index in range(0,len(list2)):
          for object_index in range(0,len(list3)):
               print(list1[subject_index]+ separator + list2[verb_index]+ separator +list3[object_index])

