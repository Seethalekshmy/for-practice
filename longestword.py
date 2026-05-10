# question: to print the longest word and its size from a given input sentence
# input: sentence
# output : longest word and its size 
# ALGORITHM 
# get the input sentence
# clean the sentence from punctuations 
# break the sentence to words 
# calculate the length of each word 
# print the output

sentence = input("enter the sentence : ")

clean_sentence = ""
for ch in sentence:
    if ch.isalpha() or ch == " ":#is.alpha() true only when its a character else false
        clean_sentence+=ch

words = clean_sentence.split()#splits the sentence to words

longest_word = " "
max_len = 0
for word in words:
    if len(word) > max_len:
        longest_word = word
        max_len = len(word)

print("longest word : " ,longest_word )
print("length : " ,max_len )
