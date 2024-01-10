##IMPORTS
import sys

##DEFINITIONS 
def display_menu(): #Displays menu
  print(f'\nWhat can I help you with today {user_name}?')
  print('1. Placeholder 1')
  print('2. Placeholder 2')
  print('3. Placeholder 3')
  print('4. More Options')
  print('5. Exit \n')

def menu_selection(): #Process user menu selection
  user_choice = int(input('Please enter a number from the menu: '))
  if user_choice == 1:
    placeholder_1()
  elif user_choice == 2:
    placeholder_2()
  elif user_choice == 3:
    placeholder_3()
  elif user_choice == 4:
    more_options()
  elif user_choice == 5:
    print(f'See you later {user_name}, and thank you for using Chatbot!')
    sys.exit()
  else:
    print('Invalid input, try again')
    menu_selection()


##MENU DEFINITIONS
def placeholder_1():
  print('Placeholder 1')

def placeholder_2():
  print('Placeholder 2')

def placeholder_3():
  print('Placeholder 3')

def more_options():
  print('More Options') #add more options to menu

##MAIN
print('Hello I\'m Chatbot, and I\'ll be your personal assistant!')

user_name = input('What\'s your name? ')
user_age = int(input(f'How old are you {user_name}? '))

print('\nChabot collects information to enhance experience' 
' and give personalized recommendations. You can choose to allow or deny this.')

print('Do you want to allow Chatbot to collect the following information?')
print(f'Name: {user_name}, Age: {user_age}')

collection_permission = input('1:Yes \n2:No \n')

while collection_permission != '1' and collection_permission != '2':
  print('Plese enter a valid number')
  collection_permission = input('1:Yes \n2:No \n')
if collection_permission == '1':
  print('Thank you for allowing Chabot to collect your information')
elif collection_permission == '2':
  print('Alright, you will continue as \'guest\' and will not '
          'recive personalized recommendations. You can always change this later.')
  user_name = 'guest'
  user_age = None

print('-------------------------------------------------')
display_menu()
menu_selection()

##RESOURCES

#About Null: https://favtutor.com/blogs/null-python

#About Exit Function: https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/#:~:text=The%20exit()%20function%20in,the%20program%20at%20any%20point
