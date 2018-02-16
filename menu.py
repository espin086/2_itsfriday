import os
import sys

project_dir = '/Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/'


#--------------------------------------------------------------------
#Defining Main Menu
def mainMenu():
	print("1. Scrape Indeed")
	print("2. Do something bad")
	print("3. Quit")
	
	while True:
		try:
			selection = int(input("Enter choice: "))
			if selection ==   1:
				
				os.system("python " + project_dir + "1_src/2_python/2_pull_indeed.py" )
				
				mainMenu()
				
				break
			elif selection == 2:
				
				#calling function
				#bad()
				
				#calling python program
				#os.system("python mypy.py")
				
				#caling a shell script
				#os.system("sh test.sh")
				
				break
			elif selection == 3:
				
				break 
			else:
				
				print("Invalid choice. Enter 1-3")
				mainMenu()
		
		except ValueError:
			print("Invalid choice. Enter 1-3")
	exit

#--------------------------------------------------------------------
#Defining functions that go into menu:

def good():
	print("Good")
	anykey = input("Any Key to Main Menu: ")
	mainMenu()

def bad():
	print("Bad")
	anykey = input("Any Key to Main Menu: ")
	mainMenu()

#--------------------------------------------------------------------
#Running Main Program

mainMenu()

