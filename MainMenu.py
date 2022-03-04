from SentenceHandler import *
from FlashcardHandler import *

def menu():
    #ask the user to select an option from the menu and set the input to a varaible.
    print(f"\nMain Menu\nLet's learn some Spanish!\n1.Create flashcards\n2.Review Flashcards\n3.List of known words\n4.Display Flashcards\n5.Quit")
    menu_selection = int(input())

    #If the user input equals 
    if menu_selection == 1:
        #call the function to create a sentence
        user_make_sentence()

    #if the user input equals 2.
    elif menu_selection == 2:
        #call the review flashcard function
        review_flashcards()
        menu()
    
    #if the user input equals 3
    elif menu_selection == 3:
        #call the function to list known words
        print(known_foreign_words)
        menu()

    #if the user input equals 4
    elif menu_selection == 4:
        print(flashcards)
        menu()
    
    #if the user input equals 5 
    elif menu_selection == 5:
        #say goodbye
        print("Goodbye")
    
    #if the user does not enter an accepted value
    else:
        #prompt to select a valid input
        "Invalid input. Please select an option from the menu 1-4."
        
        #call back to the menu
        menu()