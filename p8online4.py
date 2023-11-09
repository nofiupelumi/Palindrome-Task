# '''
# Dictionaries: They are key-value pairs, unordered, mutable
# '''
# ​
# x = {
#     'name': 'adebola',
#     'club': 'barca',
#     'language': 'python',
#     'age': 22
# }
# ​
# # get item in a dict
# #print(x['name'])
# #print(x.get('name'))
# ​
# # add item to a dict
# x['item'] = 'ball'
# #print(x)
# x.update({'married': False})
# #print(x)
# x.setdefault('food','garri')
# #print(x)
# x._setitem_('drink','water')
# #print(x)
# ​
# # update item in a dict
# x.update({'married': True})
# x['club'] = 'Chelsea'
# #print(x)
# ​
# # delete item in a dict
# del x['item']
# x.pop('club')
# x.popitem()
# #print(x)
# ​
# # food = x.pop('food')
# # print(food)
# # print(x)
# ​
# # for key, value in x.items():
# #     if key != 'age':
# #         print(key, value)
# ​
# # list comprehension
# #print([(key, value) for key, value in x.items() if key != 'age'])
# ​
# print()
# #print(x.items())
# ​
# # for value in x.values():
# #     print('mtd 1 =>', value)
# ​
# # print()
# # print('mtd 2 =>', [value for value in x.values()])
# ​
# '''
# .items() -> returns the key-value pairs in a dict
# .keys() -> returns the keys in a dict
# .values() -> returns the values in a dict
# '''
# ​
# lists of fruits
#fruits =  ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
# for index, fruit in enumerate(fruits):
#       print(index,fruit)
# # ​
# # redo this using list comprehension
#print([(index, fruit) for index, fruit in enumerate(fruits)])
# ​
# # use list comprehension to print the fruits that start with 'a'
# # print('list comp =>',[fruit for fruit in fruits if 'a' in fruit])
# ​
#for fruit in fruits:
#     if 'a' in fruit:
#         print(fruit)
# ​
# ​
# # # check if a key exists in a dict
# # if 'name' in x:
# #     print('name exists in x')
# ​
# # # name exists - chiamaka
# # # name exist in x - semande, miriam
 
# # print('name' in x)
# # # adebola - chiamaka
# # # name - miriam, semande
# # #
# ​
# # # redo line 81 & 82 using list comprehension
# # #print([name for name in x.item()])
# # print(['name exists in x' if 'name' for key in x.keys() if key == 'name'])
# # #print(for key in x, key, value.items[] if key = name)
# # #print(['name exists in x' if 'name' in x])
# ​
# '''
# Mini-Project: Contact Management System
# Do well to improve on the code as a group.
# '''
# import time
# ​
# # initialize a contact db 
# contacts = {}
# ​
# # while True:
# #     print("\n**Welcome To my Contact Management System App**\n")
# #     print("1. Add Contact")
# #     print("2. Update Contact")
# #     print("3. Delete Contact")
# #     print("4. View Contacts")
# #     print("5. Quit\n")
# ​
# #     # get user choice
# #     user_choice = int(input("Enter a number to perform an operation: "))
# ​
# #     if user_choice == 5:
# #         print("Sad to see you leave. Thanks and Goodbye!!!")
# #         break
# #     elif user_choice == 1:
# #         name = input("Enter contact name: ")
# #         phone_num = input("Enter phone number: ")
# #         # pair the value with the key
# #         contacts[name] = phone_num
# #     elif user_choice == 2:
# #         name = input("Enter contact name to update: ")
# #         # check if name exist before performing update 
# #         if name in contacts:
# #             new_phone_num = input("Enter new phone number: ")
# #             # update new phone number with the name
# #             contacts[name] = new_phone_num
# #             time.sleep(5)
# #             print(f'{name} contact has been updated successfully!!!')
# #         else:
# #             print('Oops! That name doesn\'t exist!!!')
# #     elif user_choice == 3:
# #         # check if name exist before performing delete operation
# #         name = input("Enter contact name to delete: ")
# #         if name in contacts:
# #             # delete key from dict
# #             del contacts[name]
# #         else:
# #             print('Oops! Contact not found!!!')
# #     elif user_choice == 4:
# #         print("Displaying contacts ...\n")
# #         # delay for about 5 seconds
# #         time.sleep(5)
# #         for name, phone_num in contacts.items():
# #             print(f'{name} -> {phone_num}')
# #     else:
# #         print('Invalid Input!!! Please, make sure you enter a number between 1 - 5. Thanks')
# # Nested Dicts

# s​tudents = {
#     'student1':{
#         'name':'Semande',
#         'gender':"female",
#         "strengths":{
#             "lists":80,
#             "sets":70,
#             "variables":95
#         }
#     },
#     'student2':{
#         'name':'Gideon',
#         'gender':"male",
#         "strengths":{
#             "lists":70,
#             "sets":75,
#             "variables":97
#         }
#     },
#     'student3':{
#         'name':'Bima',
#         'gender':"male",
#         "strengths":{
#             "lists":67,
#             "sets":88,
#             "variables":99
#         }
#     }
# }


# print(students['student2']['strengths'])

# x = [1,2,3]
# y = x
# x.append(4)
# x = x + [5]
# print(y)
