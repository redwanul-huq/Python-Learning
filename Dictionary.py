#python3 dict_theory.py 


# """
# Dictionary is a built-in data structure in Python that is used to store data in
# key-value pairs. Dictionaries are ordered, mutable (changeable), and do not allow
# duplicate keys. The values can be of any data type.
# """

# student = {
#     "name": "Alice",
#     "age": 20,
#     "grade": "A"
# }

# different_types_dict = {
#     "integer": 1,
#     "string": "Hello",
#     "float": 3.14,
#     "list": [1, 2, 3],
#     "tuple": (4, 5),
#     "dictionary": {"city": "Dhaka"}
# }

# """
# Features of Dictionaries:
# 1. Ordered: Dictionaries maintain the order of insertion (Python 3.7+).
# 2. Mutable: You can add, update, or remove key-value pairs.
# 3. Unique Keys: Duplicate keys are not allowed. If a duplicate key is added,
#    the last value overwrites the previous one.
# 4. Key-Value Pairs: Each item consists of a key and its corresponding value.
# """

# # Accessing Dictionary Items

# # Access a value using its key

# print(student["name"])  # Output: Alice

# # Access a value using get()

# print(student.get("age"))  # Output: 20

# # Access a nested dictionary

# person = {
#     "name": "Bob",
#     "address": {
#         "city": "Dhaka",
#         "country": "Bangladesh"
#     }
# }

# print(person["address"]["city"])  # Output: Dhaka

# # Adding Items to a Dictionary

# student["department"] = "CSE"

# print(student)
# # Output:
# # {'name': 'Alice', 'age': 20, 'grade': 'A', 'department': 'CSE'}

# # Updating Existing Items

# student["grade"] = "A+"

# print(student)

# # Updating Multiple Items

# student.update({
#     "age": 21,
#     "semester": 5
# })

# print(student)

# # Input a Dictionary from the User

# # Use a Loop

# user_dict = {}

# n = int(input("Enter the number of key-value pairs: "))

# for i in range(n):
#     key = input(f"Enter key {i + 1}: ")
#     value = input(f"Enter value for '{key}': ")
#     user_dict[key] = value

# print("The dictionary you entered is:")
# print(user_dict)

# # Changing Dictionary Items

# student["name"] = "John"

# print(student)

# # Removing Items from a Dictionary

# # Remove a specific key using pop()

# student.pop("semester")

# print(student)

# # Remove the last inserted key-value pair

# student.popitem()

# print(student)

# # Remove a key using del

# del student["department"]

# print(student)

# # Remove all items

# student.clear()

# print(student)  # Output: {}

# # Dictionary Methods

# employee = {
#     "id": 101,
#     "name": "Rahim",
#     "salary": 50000
# }

# # keys()

# print(employee.keys())
# # Output: dict_keys(['id', 'name', 'salary'])

# # values()

# print(employee.values())
# # Output: dict_values([101, 'Rahim', 50000])

# # items()

# print(employee.items())
# # Output:
# # dict_items([('id', 101), ('name', 'Rahim'), ('salary', 50000)])

# # Copying a Dictionary

# employee_copy = employee.copy()

# print(employee_copy)

# # Checking if a Key Exists

# print("name" in employee)      # Output: True
# print("address" in employee)   # Output: False

# # Duplicate Keys

# duplicate_dict = {
#     "name": "Alice",
#     "name": "Bob"
# }

# print(duplicate_dict)
# # Output:
# # {'name': 'Bob'}
# # The second value overwrites the first one.





#Dictionary Project: Contact Program

dict_Contact = {}
while True:                         #Keep running this block of code forever till the user chooses exit.
    print("\n========== PHONE CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    print("6. View Contact Names")
    print("7. View Phone Numbers")
    print("8. Total Contacts")
    print("9. Backup Contacts")
    print("10. Clear All Contacts")
    print("11. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:

        name = input("Enter Name : ").title()
        phone = input("Enter phone number : ")
        dict_Contact.update({name:phone})

        print("contact added successfully!!")

    elif choice == 2:
        if len(dict_Contact) == 0:
            print("No contact added!")
        else:
            for name,phone in dict_Contact.items(): 
                    print(f"Name:  {name}")
                    print(f"phone Number : {phone}\n")
            
    
    elif choice == 3:
        if len(dict_Contact) == 0:
            print("No contact added!")
            continue                   #Takes to while(true)
        name = input("Enter contact name : ").title()
        if name in dict_Contact.keys():
            print(f"Phone Number : {dict_Contact.get(name)}")
        else:
             print("Invalid contact Name!")
    elif choice == 4:
        if len(dict_Contact) == 0:
            print("No contact added!")
            continue
        name = input("Enter contact name : ").title()
        if name in dict_Contact.keys():
            New_phone = input("Enter new phone number : ")
            dict_Contact[name] = New_phone
        else:
            print("Invalid Contact name!")
    elif choice == 5:
        if len(dict_Contact) == 0:
            print("No contact added!")
            continue
        name = input("Enter the name you want to delete: ").title()
        if name in dict_Contact.keys():
            del dict_Contact[name]
            print("contact deleted successfully")
        else:
            print("Invalid Contact name!")
    elif choice == 6:
        if len(dict_Contact) == 0:
            print("No contact added!")
        else:
            print("========> Contact Names <=========")
            for name in dict_Contact.keys():
                print(name)
    elif choice  == 7:
        if len(dict_Contact) == 0:
            print("No contact added!")
            continue
        else:
            print("========> Contact Numbers <=========")
            for phone in dict_Contact.values():
                print(phone)
    elif choice == 8:
        #i = 0
        if len(dict_Contact) == 0:
            print("No contact added!") 
        else:
            #for name in dict_Contact.keys():
                #i = i+1
            print(f"Total contacts : {len(dict_Contact)}")  
    elif choice == 9:
        dict_Contact_copy = dict_Contact.copy()
        if len(dict_Contact_copy) == 0:
            print("No back up!") 
        else:
            print("Back up compleated")
            for name,phone in dict_Contact_copy.items():
                print(f"Name:  {name}")
                print(f"\nphone Number : {phone}")
    elif choice == 10:
        if len(dict_Contact) == 0:
            print("No contact added!") 
            continue
        dict_Contact.clear()
        print("All contact cleared")    
    elif choice == 11:
         break

    