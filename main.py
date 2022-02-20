import shutil
import string
import time
from tqdm import tqdm

lowercase_alphabets = list(string.ascii_lowercase) # Storing list of alphabets in a variable
uppercase_alphabets = list(string.ascii_uppercase) # Storing list of alphabets in a variable

#----------------------------Function to decrypt our Caesar Cipher text using Brute Force----------------------------
def decrypt(encoded_string):
    possibilities = [] # Empty list to store all the decoded strings 

    for key in range(1,26): # We chose such range because key can only be from 1 to 25
        decoded_letter_list = [] # Empty list to store all decoded letters

        for character in encoded_string:

            if character.islower():
                if lowercase_alphabets.index(character)-key >= 0:
                    decoded_letter_list.append(lowercase_alphabets[lowercase_alphabets.index(character)-key])
                else:
                    decoded_letter_list.append(lowercase_alphabets[lowercase_alphabets.index(character)-key+26])
                
            elif character.isupper():
                if uppercase_alphabets.index(character)-key >= 0:
                    decoded_letter_list.append(uppercase_alphabets[uppercase_alphabets.index(character)-key])
                else:
                    decoded_letter_list.append(uppercase_alphabets[uppercase_alphabets.index(character)-key+26])

            else:
                decoded_letter_list.append(character)

        possibilities.append(''.join(decoded_letter_list))

    return possibilities # Return all decoded string possibilities in the form of a list

#----------------------------This is the main function, this is just to enhance command-line experience----------------------------
def main():
    ascii_logo = ('''

░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░  ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝  ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║  ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

██████╗░███████╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗███████╗██████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║░░██║█████╗░░██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░░██████╔╝
██║░░██║██╔══╝░░██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗
██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░███████╗██║░░██║
╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
    ''')
    for line in ascii_logo.split('\n'): # This is just to print the ascii_art in the center of the command line window
        print(line.center(shutil.get_terminal_size().columns))

    encoded_string = input("Enter your encoded string: ")
    decoded_strings = decrypt(encoded_string) # Saving our function result in a variable for readability

    for i in tqdm(range (100),desc="Fetching…",ascii=False, ncols=75): # This displays the progress bar
        time.sleep(0.02)
    print("\nKEYS    DECODED_STRINGS")
    for key in range (1 , len(decoded_strings)+1): # Prints our decoded strings
        print(f'{key}       {decoded_strings[key-1]}')

if __name__ == "__main__":
    main()