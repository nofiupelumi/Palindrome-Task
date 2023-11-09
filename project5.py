#create a todo list
todo_list =[]
while True:
    print('\n***WELCOME TO MY TODO APP***\n')
    #display the todo list
    print('Here are your uncompleted task(s):\n')
    for index, value in enumerate(todo_list, start=1):
        print(f'{index}.{value}')
        #get user  choice
    choice = input('\n What do  you want to do ?(add, complete, edit, delete,quit): ').lower()
        #check for user choice and perform necessary operation 
    if choice =='quit':
            print('Thank you for using my todo app. Goodbye!')
            break
    elif choice=='add':
                task = str(input ('Enter a task: ')).lower()
            #add user task to the list
                todo_list.append(task)
    elif choice=='complete':
        index = int(input('Enter the index of the task you want to complete: '))
            #check  if  index is valid 
        if index>len(todo_list):
            print('Invalid index please enter a valid  index:')
            #check for -ve or  O index
        elif index<=0:
            print('Invalid index! please enter a valid  index')
            #check  for valid index and  complete task
        elif 1<=index<=len(todo_list):
            todo_list.pop(index-1)  
        else:
            print ('Invalid choice! Please enter a valid choice ') 
    elif choice=='edit':
        user_index=int(input('Enter the index of the task you want to edit:'))
        new_value=input('Enter the new value:')
        if 1<=user_index<=len(todo_list):
            todo_list[user_index-1]=new_value
            print('Task has been edited successfully.')
        else:
            print ('Invalid choice! Please enter a valid choice ') 
    elif choice =='delete':
            your_index=int(input('Enter the index of the task you want to delete:'))               
            if 1<=your_index<=len(todo_list):
                deleted_task=todo_list.pop(your_index-1) 
                print(f'Task "{deleted_task}" has been deleted.')
            else:
                print ('Invalid choice! Please enter a valid choice ') 
    else:
         print ('Invalid choice! Please enter a valid choice ') 
              
                                
 