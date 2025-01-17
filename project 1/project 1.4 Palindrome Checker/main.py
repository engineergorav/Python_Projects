# Palindrome Checker 
# in this word can be reads the same forwards and backwards

def Palindrome_Checker(word_1):
    if (word_1 == word_1[::-1]):
        print(f"The {worde} is a Palindrome word: ")
    else:
        print(f"The {worde} is not a Palindrome word: ")

while True:
    print("")
    print("Chose anyone of the following: ")
    print("1 : to write a word: ")
    print("2 : to exit the Palindrome Checker")
    option=input("type here: ")
    if(option=="1"):
        worde=input("Enter your word: ").strip()
        word_1=worde.lower()
        Palindrome_Checker(word_1)
    elif(option == "2"): 
        print("You have successfully exited the Palindrome Checker! ")
        print("revisit soon: ")
        exit()
    else:
        print("This option is not in the list")
        print("please chose the option again")
        print()

    
