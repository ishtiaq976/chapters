# 8-1. Message: Write a function called display_message() that prints one sen-
# tence telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.

def display_message():
    print("I am learning about functions in this chapter.")

display_message()


# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.


def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.


def make_shirt(size, message):
    print(f"The shirt size is {size} and it will say '{message}'.")

make_shirt("M", "Code More")
make_shirt(message="Hello World", size="L")



# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.


def make_shirt(size="L", message="I love Python"):
    print(f"The shirt size is {size} and it will say '{message}'.")

make_shirt()
make_shirt(size="M")
make_shirt(size="S", message="Debug Everything")



# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.


def describe_city(city, country="USA"):
    print(f"{city} is in {country}.")

describe_city("New York")
describe_city("Los Angeles")
describe_city("Tokyo", country="Japan")



# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.

# 8-6
def city_country(city, country):
    return f"{city}, {country}"

print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France"))
print(city_country("Tokyo", "Japan"))


# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.


# 8-7
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

print(make_album("Adele", "30"))
print(make_album("Drake", "Scorpion"))
print(make_album("Coldplay", "Parachutes", songs=10))




# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.


# 8-8
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

while True:
    print("\nEnter artist and album title (or type 'q' to quit):")
    artist = input("Artist: ")
    if artist.lower() == 'q':
        break
    title = input("Album Title: ")
    if title.lower() == 'q':
        break

    album_info = make_album(artist, title)
    print(album_info)



# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.

# 8-9
def show_messages(messages):
    for message in messages:
        print(message)

messages = ["Hello!", "How are you?", "See you soon."]
show_messages(messages)


# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.


# 8-10
def send_messages(messages, sent_messages):
    while messages:
        msg = messages.pop(0)
        print(msg)
        sent_messages.append(msg)

messages = ["Hello!", "How are you?", "See you soon."]
sent_messages = []
send_messages(messages, sent_messages)
print("Original messages:", messages)
print("Sent messages:", sent_messages)


# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.

# 8-11
messages = ["Hello!", "How are you?", "See you soon."]
sent_messages = []
send_messages(messages[:], sent_messages)
print("Original messages:", messages)
print("Sent messages:", sent_messages)


# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sand-
# wich that’s being ordered. Call the function three times, using a different num-
# ber of arguments each time.

# 8-12
def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print()

make_sandwich("turkey", "lettuce", "tomato")
make_sandwich("ham", "cheese")
make_sandwich("peanut butter", "jelly", "banana", "honey")
# 8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("John", "Doe", location="New York", field="Web Development", hobby="Reading")
print(user_profile)

# 8-14.

# main.py

# message_module.py
def display_message():
    print("I am learning about functions and imports in Python.")


# Method 1: import module_name
import message_module
message_module.display_message()

# Method 2: from module_name import function_name
from message_module import display_message
display_message()

# Method 3: from module_name import function_name as fn
from message_module import display_message as dm
dm()

# Method 4: import module_name as mn
import message_module as mm
mm.display_message()

# Method 5: from module_name import *
from message_module import *
display_message()