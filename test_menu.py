start = True
def exit():
    print(f"\n\t Thank you for viewing this program {name}. Have a pleasant day and good luck!")
    

while start:
    name = input("\n\t Good day! Welcome to Mei's Program. Please state your name: ")
    print(f"\n\t Hello {name}, I will now show you the contents of this program.")
    option = input("\n\t A - Activities, B - Code Challenges, C - Surprise, D - Exit \n\t Your decision: ")
    if option.lower() == "a":
        program_list = ["Choose an Activity", 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        choose = input(f"\n\t Please{program_list} that you want to view: ")

    elif option.lower() == "b":
        program_list2 = ["Choose a Code Challenge", 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    elif option.lower() == "c":
        print("k")
    elif option.lower() == "d":
        exit()
        break
    else:
        print("Please choose from the given.")
        continue
# if choose == 1 or 2:
#     print()
# #print statements
# print("=" *90, "\n\t The Escape Sequence \n") #explain
# print("\\n - means next line  \t \\t - means space tab  \t \\b - for back space  \t \\r - for carriage return")

# # print("=" *90, "\n\t The Arithmetic Operators \n") import activity4
# # ----------------------------------------v^v^v^v^v^v^v^v^v^v^v-------------------------------------------
# print("=" *90, "\n\t The Assignment Operators \n") #show receipt of a calculated value like grocery"
# # print("=" *90, "\n\t The Relational Operators \n") math problem heredity
# print("=" *90, "\n\t The Logical Operators \n") and, or, not  binary system
# print("=" *90, "\n\t Conditional Statements \n") BMI
# print("=" *90, "\n\t Looping Statements \n") explain
# print("=" *90, "\n\t For Loop \n") nachos/excel table
# print("=" *90, "\n\t While Loop \n") jeepney fare
# print("=" *90, "\n\t Function \n") library
# print("=" *90, "\n\t Function with Return Statement \n")
# print("=" *90, "\n\t Documentation Strings \n") explain the concept of program/subjects
# print("=" *90, "\n\t Creation of Modules \n") explain then import activity17
# print("=" *90, "\n\t List Creation \n") subjects 1st sem



