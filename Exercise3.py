#Ivan Roussev A01287751


from os import linesep
from typing import Container


new_words = open('new_words.txt', 'r')


def content_read(new_words):
    list_of_lists = []

    while True:
        line = new_words.readline().strip()
        if line == '':
            break
        for x in line:
            stripped_line = x.strip()
            line_list = stripped_line.split()
            list_of_lists.append(line_list)
    return list_of_lists

def user_input_letter():
    user_input = input('Enter a letter from a-z or A-Z:   ')
    new_input = user_input.lower()

    attemps = 0
    while new_input.isalpha() == False:
        print('Re prompt a letter')
        attemps += 1
        user_input = input('Enter a letter from a-z or A-Z:   ')

        if new_input == new_input.isalpha(): 
            break        
    return new_input

def validator(new_input):
    while new_input == new_input.isalpha():
        print('This is a valid letter')
        return True


def word_counter(letter, content_list):
    count = 0
    for word in content_list:
        if word[0] == letter:
            count += 1
    print(f'File new_words contains {count} words that contain the letter {letter}')

def has_punctuation(list_word: list):
    punctuation_char = ['$', "'",'-','.','#']
    count = 0
    for words in list_word:
        if punctuation_char in words:
            count += 1
            print(words)

def wordChecker(file_list):
    wordinput = input('Enter a Name: ')
    count = 0
    for words in file_list:
        if wordinput in words:
            count += 1
            print(words)
        print(f'There are {count} words that contain the name bob')





def main():
    word_counter(user_input_letter(), content_read(new_words))
    has_punctuation(content_read(new_words))
    wordChecker(content_read(new_words))

if __name__ == '__main__':
    main()






