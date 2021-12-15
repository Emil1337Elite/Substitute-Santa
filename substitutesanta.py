#Emil Ahrnstedt Öster
#Inf20
#2021-12-14
#Substitiute santa

import os.path

def list_c():
    n = input("What would you like your file to be called? ")
    cn = input("What is the child called? ")
    i = []
    i.append(input("What items would you like to add to the list? ").lower())
    while True:
        a = input("Forget to add something? ").lower()
        if a == "yes" or a == "y":
            i.append(input("What did you forget to add? \n"))
        elif a == "no" or "n":
            break
    file_exists = os.path.exists(f"{n}.txt")
    if file_exists:
        print("A file with this name already exits. Please choose another name. \n")
    else:
        with open(f"{n}.txt", "a", encoding="utf-8") as f:
            f.write(cn+"\n")
            f.writelines(i)

def list_r():
    n = input("What is the name of your wishlist? ")
    with open(f"{n}.txt", "r", encoding="utf-8") as f:
        print(f.readline())
        print("Wishlist")
        for i in f:
            print(i.strip())

def list_n():
    a = input("Would you like to add names or read the naughty list.").lower()
    i = []
    i.append(input("What names do yo want to add? "))
    if a == "add" or a == "add names":
        while True:
            with open("kolbarn.txt", "a", encoding="utf-8"):
                a = input("Do you want to add another name? ").lower()
                if a == "yes" or a == "y":
                    i.append(input("What did you forget to add? \n"))
                elif a == "no" or "n":
                    break
    elif a == "read":
        with open("kolbarn.txt", "r", encoding="utf-8") as f:
            f.readline()
            for i in f:
                print(i.strip())

print("""Santa has gotten sick and needs help with his work so he can take time off an recover in time for Christmas. 
You have been tasked with creating and reading the wish lists of children.""")
def main():
    while True:
        print("Would you like to create or read a list? ")
        print("Type 'c' to create a new file, type 'r' to read a file or type 'n' to read the naughty list.")
        a = input()
        if a == "c":
            list_c()
        elif a == "r":
            list_r()
        elif a == "n":
            list_n()
        else:
            print("Input not recognised.")

if __name__ == "__main__": 
    main()