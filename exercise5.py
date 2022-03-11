#Ivan Roussev A01287751

from os import write


file_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def content_read(random_file):
    content_list = []
    with open(random_file) as new_file:
        for word in new_file:
            if len(word) == 4:
                content_list.append(word.rstrip('\n').lower())
            else:
                continue
        content_list.sort()
    
        return content_list

 

def list_items(item__list, letter):
    content_list = []
    for word in item__list:
        if word[0] == letter:
            content_list.append(word)
    return content_list

def new_Txt_File(letter, item__list):
    New_txt = open(f'{letter}_file.txt', 'w')
    for word in item__list:
        New_txt.write(word)
    word_count = len(item__list)
    print(f'{new_Txt_File} was created -------  {word_count} words were found in file')
    New_txt.close()


def letter_file(list):
    for char in file_names:
        new_Txt_File(char, list_items(list, char))











def main():
    file = 'new_words.txt'
    new_file = content_read(file)
    letter_file(new_file)
    






if __name__ == '__main__':
    main()

