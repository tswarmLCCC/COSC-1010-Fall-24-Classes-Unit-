def main():
    firstname = get_first_name()
    lastname = get_last_name()
    print(f"Hello {firstname} {lastname}!")
    

def get_first_name():
    inputval = input("What is your first name? ")
    return inputval

def get_last_name():
    inputval = input("What is your first name? ")
    return inputval

#firstname = get_first_name()
#lastname = get_last_name()

if __name__ == "__main__":
    main()


'''Moving forward!'''

def main():
    firstname = get_name()
    lastname = get_name("What is your last name? ")
    print(f"Hello {firstname} {lastname}!")
    

def get_name(namePrompt = "What is your first name? "):
    inputval = input(namePrompt)
    return inputval


firstname = get_first_name()

if __name__ == "__main__":
    main()


'''Touples'''
def main():
    fullname = get_full_name()
    #print(f"Hello {firstname} {lastname}!")
    print(f"Hello {fullname}") # well that's interesting!
    print(f"Hello {fullname[0]} {fullname[1]}")
    

def get_name(namePrompt = "What is your first name? "):
    inputval = input(namePrompt)
    return inputval

def get_full_name():
    firstname = get_name("What is your first name? ")
    lastname = get_name("Cool prompt for the last name: ")
    return (firstname, lastname)

#firstname = get_first_name()

if __name__ == "__main__":
    main()
