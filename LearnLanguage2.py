#from distutils import command
#from ast import pattern
from turtle import clear
from MainMenu import *
#import subprocess
import os
import re
import time
#import navigator as np
 
 
special_directory = '/specialproject/logdz/setup.exe'
#function that gets the special project.
def url():
    url = "https://github.com/mshoy/specialproject.git"
    return url
 
#use git clone to clone the repository.
def clone_repository(url):
    os.system(f"git clone {url}")
 
#take the output from the dir command and put it in a txt
def dir_to_txt():
    dir_name = os.system('dir >> dir_name.txt')
    dir_as_var = dir_to_variable("dir_name.txt")
    return dir_as_var
 
#read the txt and put the text as a variable   
def dir_to_variable(dir_as_txt):
    with open(dir_as_txt, "r") as directory:
         dir_as_var = directory.read()
    #print(dir_as_var)
 
    if 'specialproject' not in dir_as_var:
        #clone the repository
        clone_repository(git_url)
    
    return dir_as_var
 
#define a pattern that we want to match.
def dir_pattern():
    pattern = re.compile(r'(\\\w+)+')
    return pattern
 
#takes the directory as a match 
def search_for_pattern(text):
    match_object = dir_regex.search(text)
    return match_object
 
#get the github repository
git_url = url()
 
#clone the repository
#clone_repository(git_url)
 
#sleep for a bit to allow for everything to process.
time.sleep(3)
 
#save the directory to a text document. and create a variable
working_dir = dir_to_txt()
 
#match the directory address with the current working directory.
dir_regex = dir_pattern()
 
#search working_dir for our regex pattern
match_object = search_for_pattern(working_dir)
match_object = match_object.group()
match_object = match_object.replace("\\", "/")
 
# dirname = os.path.dirname()
 
 
filename = 'C:/' + match_object + special_directory
print(filename)
 
 
os.startfile(filename)
 
time.sleep(7)
# #start the main menu function
menu()
 
