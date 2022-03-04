from SentenceHandler import *

def review_flashcards():
    for card in range(len(flashcards)):
        sentence = update_card(flashcards[card], known_english_words[card], known_foreign_words[card])
        #print(f'the current known english word: {known_english_words[card]}')
        print(f'\nWhat is {known_foreign_words[card]}')
        input('Press enter to show the answer...')
        print(f'\n{sentence}')

def update_card(sentence, known_english_word, known_foreign_word):
    broken_sentence = sentence_into_array(sentence.upper())
    sentence = sentence_compare(broken_sentence, known_english_word, known_foreign_word, sentence)
    #print(new_sentence)

    return sentence