from Vocabulary import *
import MainMenu as MM

#create an array for the words we have create flashcards for
known_english_words = []
known_foreign_words = []

#create a flashcard deck
flashcards = []

#This function will ask the user to create a sentence
def user_make_sentence():
    #set the current english noun to the index we are currently on (will always be the length of the known english words)
    current_english_noun = list(nouns.keys())[len(known_english_words)].upper()
    current_foreign_noun = list(nouns.values())[len(known_foreign_words)].upper()

    #ask the user to type a sentence with the current noun
    print(f"\nMake a sentence with the word {current_english_noun}")
    user_sentence = input()
    
    #check that the user_sentence contains the key word in english
    sentence_error_check(user_sentence, current_english_noun)

    #add the english key word to the known english words list.
    known_english_words.append(current_english_noun)
    
    #add the foreign value to the known foreign words list.
    known_foreign_words.append(current_foreign_noun)

    #replace the english key with the foreign language value.
    modified_sentence = replace_word(user_sentence, current_english_noun, current_foreign_noun)

    #add this modified sentence to the flashcard deck.
    create_flashcard(modified_sentence)

    #ask the user to make another sentence
    create_next()

#add the new sentence to the flashcard deck
def create_flashcard(sentence):
    flashcards.append(sentence)
    print(f"\nA new flashcard has been created!")
    print(f"Known Words: {len(known_foreign_words)}")
    print(f"\n{flashcards[len(known_foreign_words) - 1]}")

#this function will check to see if the user entered a sentence that contained the key word
def sentence_error_check(user_sentence, word):
    #create a temp sentence that is the user sentence in all upper to perform a check
    temp_sentence = user_sentence.upper()

    #call a function to split this temp sentence into an array. breaks the sentence up.
    broken_sentence = sentence_into_array(temp_sentence)

    #this while loop will check if the current noun is in the broken sentence array
    while word not in broken_sentence:
        #if it's not, the user is prompted and the user make sentence function is called again.
        print(f"\nThe sentence you entered did not include the key word '{word}'\n") 
        user_make_sentence()

#this function will take our sentence and break each word into an array index. It returns the array
def sentence_into_array(sentence):
    #create an array from the sentence sparated by a space
    array_from_sentence = sentence.split(" ")
    
    return array_from_sentence

#this function will join a sentence that has been broken into an array
def join_sentence(broken_sentence):
    joined_sentence = " ".join(broken_sentence)
    return joined_sentence

#this function will replace an english key word with a foreign value
def replace_word(sentence, original_word, replacement_word):
    #store the sentence as an array
    broken_sentence = sentence_into_array(sentence)
    
    #iterate through each word in the array
    for i in range(len(broken_sentence)):
        #if the word in the array equal the current english word
        if broken_sentence[i].upper() == original_word.upper():
            #replace the word in the array.
            broken_sentence[i] = broken_sentence[i].upper()
            broken_sentence[i] = replacement_word.upper()
    
    sentence = join_sentence(broken_sentence)
    
    return sentence

#this function will ask the user to create another flashcard
def create_next():
    print(f"\nWould you like to create another card?\n1. Yes\n2. No")
    user_selction = int(input())

    if user_selction == 1:
        user_make_sentence()
    elif user_selction ==2:
        MM.menu()
    else:
        print(f"invalid input. Please select 1 for 'Yes' or 2 for 'No'.")
        create_next()

def sentence_compare(broken_sentence, known_english_word, known_foreign_word, sentence):
    for word in range(len(broken_sentence)):
        for known in range(len(known_english_words)):
            if known_english_words[known] == broken_sentence[word]:
                print(known_english_words[known])
                print(known_foreign_words[known])
                #for knownf in range(len(known_foreign_words)):
                #known_english_word = knownf.upper()
                #the known_foreign_word is incorrect. need to call the current foreign word.
                sentence = replace_word(sentence, known_english_words[known], known_foreign_words[known])
                #print(broken_sentence)
    return sentence