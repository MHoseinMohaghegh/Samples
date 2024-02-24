# Importing the pyshortener module for URL shortening
import pyshorteners

# Function to shorten a given URL
def shortener(url):
    # Creating an instance of the Shortener class from pyshorteners
    s = pyshorteners.Shortener() 
    
    # Using the tinyurl service to shorten the given URL and printing the result
    print(s.tinyurl.short(url))

# Infinite loop for user input
while True:
    # Prompting the user to enter a URL, and providing instructions to exit by typing '0'
    url = input('Please enter a url (for exit, type 0): ')
    
    # Checking if the user wants to exit the program
    if url == '0':
        break
    else:
        # Calling the shortener function to shorten and print the URL
        shortener(url)

