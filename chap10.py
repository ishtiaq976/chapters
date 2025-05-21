# 10-1. Learning Python: Open a blank file in your text editor and write a few
# lines summarizing what you’ve learned about Python so far. Start each line
# with the phrase In Python you can. . . . Save the file as learning_python.txt in
# the same directory as your exercises from this chapter. Write a program that
# reads the file and prints what you wrote three times. Print the contents once by
# reading in the entire file, once by looping over the file object, and once by stor-
# ing the lines in a list and then working with them outside the with block.


filename = "learning_python.txt"

# Read the entire file
with open(filename) as file:
    contents = file.read()
print("=== Read entire file ===")
print(f'Content is {contents}')

# Loop over the file object
print("\n=== Loop over file object ===")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

# Store lines in a list and work outside the with block
print("\n=== Read lines into a list ===")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())



# 10-2. Learning C: You can use the replace() method to replace any word in a
# string with a different word. Here’s a quick example showing how to replace
# 'dog' with 'cat' in a sentence:
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# Read in each line from the file you just created, learning_python.txt, and
# replace the word Python with the name of another language, such as C. Print
# each modified line to the screen.

filename = "learning_python.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

print("\n=== Replacing 'Python' with 'C' ===")
for line in lines:
    print(line.replace("Python", "C").strip())



# 10-3. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt. 


name = input("What is your name? ")
with open("guest.txt", "w") as file:
    file.write(name)

# 10-4. Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.


print("Enter 'q' to quit.")
while True:
    name = input("What is your name? ")
    if name.lower() == 'q':
        break
    print(f"Hello, {name}!")
    with open("guest_book.txt", "a") as file:
        file.write(f"{name} visited.\n")


# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters

print("Enter 'q' to quit.")
while True:
    reason = input("Why do you like programming? ")
    if reason.lower() == 'q':
        break
    with open("programming_poll.txt", "a") as file:
        print(file.read())
        file.write(f"{reason}\n")

# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a ValueError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.

first = input("Enter the first number: ")
second = input("Enter the second number: ")

try:
    result = int(first) + int(second)
except ValueError:
    print("❌ You need to enter valid numbers.")
else:
    print(f"✅ The sum is: {result}")


#  10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.


name = True

while name:
    first = input("Enter the first number: ")
    second = input("Enter the second number: ")

    try:
        result = int(first) + int(second)
    except ValueError:
        print("Please enter valid numbers.")
    else:
        print(f"The sum is: {result}")



# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
# names of cats in the first file and three names of dogs in the second file. Write
# a program that tries to read these files and print the contents of the file to the
# screen. Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing. Move one of the files to a dif-
# ferent location on your system, and make sure the code in the except block
# executes properly.


filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Cannot find the file: {filename}")
    else:
        print(f"\nContents of {filename}:")
        print(contents)


# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.


filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\nContents of {filename}:")
        print(contents)



# 10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org/ )
# and find a few texts you’d like to analyze. Download the text files for these
# works, or copy the raw text from your browser into a text file on your
# computer.
# You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the number
# of times 'row' appears in a string:
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# 3
# >>> line.lower().count('row')
# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for, regardless of how it’s
# formatted.
# Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text. This will be
# an approximation because it will also count words such as 'then' and 'there'.
# Try counting 'the ', with a space in the string, and see how much lower your
# count is.


filename = 'your_gutenberg_file.txt'

try:
    with open(filename, encoding='utf-8') as file:
        contents = file.read().lower()
except FileNotFoundError:
    print("File not found.")
else:
    the_count = contents.count('the')
    the_space_count = contents.count('the ')
    print(f"'the' count: {the_count}")
    print(f"'the ' count: {the_space_count}")
