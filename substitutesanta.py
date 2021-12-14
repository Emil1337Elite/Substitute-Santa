#Emil Ahrnstedt Öster
#Inf20
#2021-12-14
#Substitiute santa

def list_c():
    n = input("What would you like your file to be called? ")
    cn = input("What is the child called? ")
    i = []
    i.append(input("What items would you like to add to the list? ").lower())
    while True:
        a = input("Forget to add something? ").lower()
        if a == "yes" or a == "y":
            input("What did you forget to add? \n")
        elif a == "no" or "n":
            break

    with open(f"{n}.txt", "a", encoding="utf-8") as f:
        f.write(cn+"\n")
        f.writelines(i)

print("""Santa has gotten sick and needs help with his work so he can take time off an recover in time for Christmas. 
You have been tasked with creating and reading the wish lists of children.""")
def main():
    while True:
        print("Would you like to create or read a list? ")
        print("Type 'c' to create a new file, type 'r' to read a file.")
        a = input
        if a == "c":

if __name__ == "__main__":
    main()