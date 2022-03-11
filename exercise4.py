#Ivan Roussev A01287751


num_word = { '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0, '10' : 0, 
'11' : 0, '12' : 0, '13' : 0, '14' : 0, '15' : 0, '16' : 0, '17' : 0, '18' : 0, '19' : 0, '20' : 0, 
'21' : 0, '22' : 0, '23' : 0,'24' : 0}

def word_length():
    new_words = open('new_words.txt', 'r')
    for line in new_words:
        length_word = len(line) - 1
        num_word[str(length_word)] += 1
                     
    

def main():
    word_length()
    for length, count in num_word.items():
        print(f" length of word is {length} : amount of words with that num of letters {count} ")





if __name__ == '__main__':
    main()

