"""
A menu to interact with the job search program
"""


import os


PROJECT_DIR = '/Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/'


# --------------------------------------------------------------------
# Defining Main Menu
def main_menu():
    """
    The main menu function that takes user input
    """
    print("1. Scrape Indeed")
    print("2. Quit")

    while True:
        try:
            selection = int(input("Enter choice: "))
            if selection == 1:

                os.system("python " + PROJECT_DIR +
                          "src/2_python/2_pull_indeed.py")

                main_menu()

                break
            elif selection == 2:
                break
            else:

                print("Invalid choice. Enter 1-2")
                main_menu()

        except ValueError:
            print("Invalid choice. Enter 1-2")


# --------------------------------------------------------------------
# Running Main Program

if __name__ == "__main__":
    main_menu()
