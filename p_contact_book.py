import json

with open('j_contact_book.json', 'r') as file:
    contact_book = json.load(file)
# print(contact_book)

# To add a contact
def cont_add():
    headline = """
            --:: To add a new contact info ::--
    """
    print(headline)
    ui_name = str(input("Enter the contact person name: ")).lower()
    ui_email = str(input("Enter the contact person email: ")).lower()
    ui_ph = int(input("Enter the contact person phone number: "))
    contact_book[ui_name] = [ui_email, ui_ph]
    if ui_name in contact_book:
        cont_edit()
    else:
        print("----:::: The contact person's info added successfully ::::----")

# To view a contact  
def cont_view():
    headline = """
            --:: Below is all the contact info of your contact book ::--
    """
    print(headline)
    for k, v in contact_book.items():
        print(f"{k}~ email:{v[0]}, phone number:{v[1]}")

# To edit a contact
def cont_edit():
    heading = """
            Enter '1' to edit the name
            Enter '2' to edit the email address
            Enter '3' to edit the phone number
    
    """
    print(heading)
    ui_for_edit_cont = int(input("Enter a number to edit the contact: "))
    ui_name = str(input("Enter the contact person name you want to edit: ")).lower()
    if ui_for_edit_cont == 1:
        ui_new_name = str(input(f"Enter the name you want to replace with the present contact ({ui_name}): "))
        contact_book[ui_new_name] = contact_book.pop(ui_name)
        print("----:::: Your updated name and the info is below ::::----")
        print(f"{ui_new_name}~ email:{contact_book[ui_new_name][0]}, Phone Number:{contact_book[ui_new_name][1]}")
        
    elif ui_for_edit_cont == 2:
        ui_new_email = str(input(f"Enter the email you want to replace with the present email ({contact_book[ui_name][0]}): "))
        contact_book[ui_name][0] = ui_new_email
        print("----:::: Your updated email and the info is below ::::----")
        print(f"{ui_name}~ email:{contact_book[ui_name][0]}, Phone Number:{contact_book[ui_name][1]}")
        
    elif ui_for_edit_cont == 3:
        ui_new_ph = str(input(f"Enter the phone number you want to replace with the present phone number ({contact_book[ui_name][1]}): "))
        contact_book[ui_name][1] = ui_new_email
        print("----:::: Your updated phone number and the info is below ::::----")
        print(f"{ui_name}~ email:{contact_book[ui_name][0]}, Phone Number:{contact_book[ui_name][1]}")

# To view all contact
def cont_viewall():
    headline = """
            --:: Below is all the contact info of your contact book ::--
    """
    print(headline)
    for k, v in contact_book.items():
        print(f"{k}~ email:{v[0]}, phone number:{v[1]}")

# To delete a contact
def cont_delete():
    headline = """
            --:: Delete a contact person info ::--
    """
    print(headline)
    ui_name = str(input("Enter the contact person name you want to delete: ")).lower()
    if ui_name in contact_book:
        del contact_book[ui_name]
        print("----:::: The contact person's info successfully deleted ::::----")
    else:
        print("The name you entered is not in your contact book.....")

main_menu = """
        ---::: What you want to do :::---
            Enter '1' to add a contact
            Enter '2' to view a contact
            Enter '3' to edit a contact
            Enter '4' to view all contacts
            Enter '5' to delete a contact
            Enter '6' to save and exit the app

"""

while True:
    print(main_menu)
    ui = int(input("Enter a number: "))
    if ui == 1:
        cont_add()
    elif ui == 2:
        cont_view()
    elif ui == 3:
        cont_edit()
    elif ui == 4:
        cont_viewall()
    elif ui == 5:
        cont_delete()
    elif ui == 6:
        break
    else:
        print("Enter a vaid number")

with open('j_contact_book.json', 'w') as file:
    json.dump(contact_book, file)