#  write a program to add, update, delete Contacts from Contact Book here we can add phoen number and e-mail 

# here i use the strip() function to get clean input and also user can get good experience after giving some as the want 
#  without having worry to type case sensitive words


contact_list={"Gorav Thakur":9058674106,}

def add_in_contact_list():
    while True: 
        print("type 1 to quit: ")
        print("type 2 to add detials: ")
        a=input("type here: ").strip()
        if(a=="1"):
            return
        elif(a=="2"):
            key=input("Enter the name: ").strip()
            print("TYPE: ")
            print("1: to add phone number: ")
            print("2: to add email: ")
            print("3: to add both: ")
            print("4: to quit: ")
            int_or_str=(input("type here: ")).strip()
            if(int_or_str=="1"):
                value=int(input("enter the contact number: "))
                contact_list.update({key:value})
                print("Contact number is added successfully: ")
            elif(int_or_str=="2"):
                value=input("enter the contact e-mail: ")
                contact_list.update({key:value})
                print("Contact e-mail is added successfully: ")
            elif(int_or_str=="3"):
                value=input("enter the contact number and e-mail: ")
                contact_list.update({key:value})
                print("Contact number and e-mail are added successfully: ")
            elif(int_or_str=="4"):
                print("existed successfully from adding contacts to contact list: ")
                return

            else:
                print("INVALID INPUT, please try again: ")

def delete_from_contact_list():
    key=input("Enter the name: ").strip()
    if key in contact_list:
        del contact_list[key]
        print("Contact detials are deleted successfully: ")
    else:
        print(f"{key} does not exist in contact list")

def serach_in_contact_list():
    key=input("enter the name: ").strip()
    for item in contact_list:
        if(item.lower()==key.lower()):
            contact_detials = contact_list[item]
            print(f"contact detials of {key} is {contact_detials}")
            return
        else:
            print(f"there no one with {key} name in contact list ")

while True:
    print("TYPE: ")
    print("1: for adding contact detials: ")
    print("2: for viewing contact detials: ")
    print("3: for deleting contact detials: ")
    print("q: To exit: ")
    entery=(input("type here: ")).strip()
    if(entery=="q"):
        print("You are safely exited ")
        break
    elif(entery=="1"):
        add_in_contact_list()
    elif(entery=="3"):
        delete_from_contact_list()
    elif(entery=="2"):
        serach_in_contact_list()
    else:
        print("INVALIED ENTERY, please enter again: ")
