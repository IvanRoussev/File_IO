#Ivan Roussev A01287751

from os import name, read
import string


new_words = open('new_words.txt', 'r')


def content_read(new_Words):
    content = new_Words.read()
    content_list = content.split("\n")
    word_count = len(content_list)
    print(f'There are {word_count} words in the list')
    return content_list

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





def main():
    word_counter(user_input_letter(), content_read(new_words))



if __name__ == '__main__':
    main()





