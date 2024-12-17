def cc1():
    print("\n\t\t\t\t\t\t\t\t\t\t     \b\b *")
    print("\t\t\t\t\t\t\t\t\t\t    \b\b ***")
    print("\t\t\t\t\t\t\t\t\t\t  *****")
    print("\t\t\t\t\t\t\t\t\t\t ******* \n\t\t\t\t\t\t\t\t\t\t  *****")
    print("\t\t\t\t\t\t\t\t\t\t   *** \n\t\t\t\t\t\t\t\t\t\t     \b*")

def cc2():
    name = input("Please type your name --> ")
    print("\n\t\t\t\t\t\t\t\t\t\t * \n\t\t\t\t\t\t\t\t\t       * * *")
    print("\t\t\t\t\t\t\t\t\t     * * * * * \n\t\t\t\t\t\t\t\t\t   \b\b  * * * * * * * ")
    print("\t\t\t\t\t\t\t\t         * * * * * * * * * \n\t\t\t\t\t\t\t\t       *      " + name + "      *")
    print("\t\t\t\t\t\t\t\t\t * * * * * * * * * \n\t\t\t\t\t\t\t\t\t     \b\b* * * * * * *")
    print("\t\t\t\t\t\t\t\t\t     * * * * * \n\t\t\t\t\t\t\t\t\t       * * * \n\t\t\t\t\t\t\t\t\t\t *") 

def cc3():
    full_name = input("\n\n\t\t\t\t\t Bio-Data \n\n\t Please type your Name: ")
    gender = input("\t Please type your Gender: ")
    age = input("\t Please type your Age: ")
    BDate = input("\t Please type your Date of Birth: ")
    Brgy = input("\t Please type your Barangay name: ")
    ProvAd = input("\t Please type your Provincial Name: ")
    print("\n\t\t\t\t FAMILY DETAILS")
    Fn = input("\t Father's name: ")
    Mn = input("\t Mother's name: ")
    print("\n\t\t\t\t CONTACT DETAILS ")
    ConDe = input("\t Contact No.: ")
    ConD = input("\t E-mail Address: ")
    print("\n\n\n\n\t\t\t\t Hi, I am" , full_name, gender , "and I am" , age , "years old. I was born on" , 
          BDate , " I live in", Brgy, ProvAd, ". \n My father is" , Fn , "and my mother is" , Mn, 
          ".  You can contact me with my cellphone number," , ConDe , "and an e-mail of \n\t" , ConD,"." )
    
def cc4():
    num1 = eval(input("\n\t Enter the first number: "))
    num2 = eval(input("\t Enter the second number: "))
    print("\n\t", num1, "+", num2, "is", num1 + num2, "\b. \n\t", num1, "-", num2, "is", num1 - num2, "\b.")
    print("\t", num1, "*", num2, "is", num1 * num2, "\b. \n\t", num1, "/", num2, "is", num1 / num2, "\b.")
    print("\t", num1, "exponent by", num2, "is", num1 ** num2, "\b.\n\t", num1, "%", num2, "is", num1 % num2, "\b.")
    print("\t", num1, "//", num2, "is", num1 // num2, "\b.")

def cc5():
    print("\n\t Fahrenheit to Celsius Converter Program")
    print("\n\t =====================================================")

    fahrenheit = eval(input("\n\t Enter temperature in Fahrenheit: "))
    celsius = ((fahrenheit - 32) * 5) /9
    print("\n\t", fahrenheit, "degrees Fahrenheit converted to celsius is", celsius, "degrees")
    print(f"\t {fahrenheit} degrees Fahrenheit converted to celsius is {round(celsius, 2)} degrees")

def cc6():
    #Program that will accept Prelim, Midterm, Semi-final, Final, Quiz, and Project
    pre = eval(input("\n\t Enter your Prelim Grade: "))
    mid = eval(input("\n\t Enter your Midterm Grade: "))
    semi = eval(input("\n\t Enter your Semi-final Grade: "))
    final= eval(input("\n\t Enter your Final Grade: "))
    quiz = eval(input("\n\t Enter your Quiz Grade: "))
    project = eval(input("\n\t Enter your Project Grade: "))

    if (pre >= 65 and pre <= 100) and (mid >= 65 and mid <= 100) and (semi >= 65 and semi <= 100) and (final >= 65 and final <= 100) and (quiz >= 65 and quiz <= 100) and (project >= 65 and project <= 100):
        fgrade = (pre * 0.15) + (mid * 0.15) + (semi * 0.15) + (final * 0.15) + (quiz * 0.25) + (project * 0.15)
        #nested condition
        if fgrade >= 75 :
            print("\n\t Congratulations! You passed the course.")
        else:
            print("\n\t Sorry, you failed the course. Better luck next time.")
        print("\n\t Your grade is", fgrade)

    else:
        print("\n\t Invalid grade number.")
def cc7():
    isFood = input("\t Hi dear shopper! Are you going to buy some grocery (yes / no): ")    #Sell and give discount
    if isFood.lower() == "yes":
        print("\n\t Which of these food did you buy? \n\t Pastry - 56.00  Meat - 230.25   Rice - 130.65",
              "\t Pasta - 147.00  Cooking oil - 35.60   Ketchup - 54.89   Mayonnaise \n\t Vgetable - 54  Carrot - 25")

        price1 = eval(input("\n\t Enter your shopping cart's food price (maximum of 3): "))
        if price1 <= 230.26:
            price2 = eval(input("\n\t Enter your shopping cart's food price: "))
            price3 = eval(input("\n\t Enter your shopping cart's food price: "))
            print("\n\t Tax = 12.3% ")	
            tot = price1 + price2 + price3
            tot2 = round(tot  * 0.123, 2)
            amt = tot2 + tot
            print("\n\t Your total amount is", amt ,"\b. ")             # The Discount for senior is 5.2%
            pay = input("\n\t Cash or card: ")
            if pay.lower() == "cash":
                payment = eval(input("\n\t How much will you pay? "))
                total = round(payment - amt, 2)
                Age = eval(input("\n\t By the way, how old are you: "))
                if Age >= 60:
                    dis = amt * 0.052
                    discount = amt - dis
                    change = round(payment - discount, 2)
                    print(f"\n\t Your change is {change} \b. Thanks for shopping.")
                else:
                    print(f"\n\t Your change is {total} \b. Thanks")
            elif pay.lower() == "card":
                Age = eval(input("\n\t By the way, how old are you: "))
                if Age >= 60:
                    dis = amt * 0.052
                    discount = amt - dis
                    print(f"\n\t Your card will be reduced with a total of {discount}. Thanksss")
                else:
                    print(f"\n\t Your card will be reduced with a total of {amt}. \n\t Thanks for shopping!")
            else:
                print("\n\t You did not state your way of payment. Try again.")
        else:
            print("\n\t The amount you entered is beyond the limit. \n\t Try again. ") 
    else:
        print("\n\t Hmmm... Well, thank you for coming by. Until next time. ")
def cc8():
    sum = 0
    for i in range(1,11):
        num = eval(input(f"\n\t  Enter a number {i}: "))
        sum += num
    print(f"\n\t  The sum of all the numbers you entered is {sum}.")

def cc9():
    print("\n======================================= \n")
    for x in range(10):
        for y in range(2*x):
            print(" ", end = "")
        for z in range(10-x):
            print(" *", end = "")
        print()

def cc10():
    #not a sharp diamond
    print("\n\n")      #arrow up
    for x in range(1,6):
        for y in range(6, x, -1):
            print(" ", end =" ")
        for z in range(1, x+1):
            print("*", end =" ")
        for a in range(1, x+1):
            print("*", end =" ")
        print()

    for x in range(1,6):      #arrow down
        for y in range(1, x+1):
            print(" ", end =" ")
        for z in range(6, x, -1):
            print("*", end =" ")
        for a in range(6, x, -1):
            print("*", end =" ")
        print()
    print("\n\n")

def cc11():
    # sharp diamond
    print("\n\n")       #arrow up
    for x in range(1,5):
        for y in range(5, x, -1):
            print(" ", end =" ")
        for z in range(1, x-1):
            print("*", end =" ")
        for a in range(1, x):
            print("*", end =" ")
        print()

    for x in range(1,5):       #arrow down
        for y in range(1, x):
            print(" ", end =" ")
        for z in range(4, x, -1):
            print("*", end =" ")
        for a in range(5, x, -1):
            print("*", end =" ")
        print()
    print("\n\n")

def cc12():
    # make an arrow pointing upward
    print("\n\n")
    for x in range(1,5):
        for y in range(5, x, -1):
            print(" ", end =" ")
        for z in range(1, x+1):
            print("*", end =" ")
        for a in range(1, x+1):
            print("*", end =" ")
        print()

    for x in range(1,5):
        for y in range(5, 4, -1):
            print(" ", end = "\t")
        for z in range(5, 4, -1):
            print("* *", end = " ")
        print()
    print("\n\n")

def cc13():
    # sharp diamond but with numbers
    print("\n\n")           #arrow up
    for x in range(1,6):
        for y in range(6, x, -1):
            print(" ", end =" ")
        for z in range(x, 0,-1):
            print(z, end =" ")
        for a in range(2, x+1):
            print(a, end =" ")
        print()

    for b in range(4, 0, -1):       #arrow down
        for c in range(6, b,-1):
            print(" ", end =" ")
        for d in range(b, 0,-1):
            print(d, end =" ")
        for e in range(2, b+1):
            print(e, end =" ")
        print()
    print("\n\n")

def cc14():
    import os 
    print("\n\n\t Ooohh...")     #continue to ask a number then provide the sum 
    name = input("\t Hi dear user! What's your name? ")
    isGo = True
    sum = 0
    while isGo == True:
        num = eval(input("\n\t Enter a number -> "))
        sum += num 
        if (num <= 10 and num >= 0) :
            if num == 0:
                print("\n\t Yey! The loop has been terminated.")
                con = input("\n\t Would you still like to continue giving numbers(yes/no):")
                if con.lower() == "no":
                    os.system("cls")
                    print(f"\n\t Dear {name}, the number you entered has a total of {sum}.")
                    print("\n\t Program stopped.","."*100)
                    break
                    isGo == False 
                else:
                    os.system("cls")
                    print("\n\t So you want more ^o^?")
                    continue
            else:
                continue
        else:
            print(f"\n\t You typed an invalid number, {name}. TRY AGAIN.")
            print("."*128)
            continue
            
def cc15():
    import os          #PACKAGE # HYBRID LOOP
    num = 0
    while True:
        ask = input("\n\t Do you want to CREATE a triangle (yes/no): ")
        if ask.lower() == "yes":
            os.system('cls')
            num += 1
            for x in range(1,5):
                for y in range(1,num + 1):
                    for z in range(1,x+1):
                        print("*", end=" ")
                    for a in range(5, x, -1):
                        print(" ", end=" ")
                print()
            continue
        else:
            os.system('cls')
            print("\n\t You entered an invalid answer. TRY AGAIN.", "."*100)
            continue
        
def cc16():
    go = True         # make a Banking account that can deposit and withdraw 
    bal = 5000    # breakdown a Filipino denomination that will only be terminated if the user choose to stop it
    initial_dep = 2000
    def greet():
        print("\n\t\t\t\t\t\t Plumeria Bank \n\t Good day!")
        print("\n\t SELECT TRANSACTION   \n\n\t 1 - Check Balance   \t\t\t\t 2 - Deposit Cash")
        print("\t 3 - Withdraw Cash   \t\t\t\t 4 - Pay Bills \n\t 5 - Create an Account \t\t\t\t 6 - Exit \n")

    def exit():
        print("\nThank you for using our bank. The system will now close. \n","_"*120)
    def bal_amt():
        print(f"\nYour current balance is {bal}.")
    def in_dep():
        print(f"\nYour initial deposit is {initial_dep}.")
    def receipt2():
        rec = input("\n Do you need to print a receipt? ")
        if rec.lower() == "yes":
            print("="*120)
            print(f"\n\t\t\t\t\t\t Plumeria Bank \n\t TRANSACTION \n\t Cash Withdrawal \n\n\t AMOUNT: {amt} \n\t Balance: {bal} \n", "="*120)
        elif rec.lower() == "no":
            exit()
        else:
            print("You've entered an invalid answer.")
    def receipt1():
        rec = input("\nDo you need to print a receipt? ")
        if rec.lower() == "yes":
            print("="*120)
            print(f"\n\t\t\t\t\t\t Plumeria Bank \n\t TRANSACTION \n\t Cash Deposit \n\n\t AMOUNT: {dep} \n\t Balance: {bal} \n\t Initial deposit: {initial_dep} \n", "="*120)
        elif rec.lower() == "no":
            exit()
        else:
            print("You've entered an invalid answer.")
    def mon():
        print("\n\t PHP 1,000 \t PHP 2,000 \t PHP 5,000 \t PHP 10,000 \t Other amount")
    def nm():
        name = input("\n Enter your name: ")
        pin = input("\n Enter your pin number: ")
    def denomi1():
        ans1 = dep_2 // 1000 
        num1 = dep_2 % 1000
        ans2 = num1 // 500
        num2 = num1 % 500
        ans3 = num2 // 200
        num3 = num2 % 200
        ans4 = num3 // 100
        num4 = num3 % 100
        ans5 = num4 // 50
        num5 = num4 % 50
        ans6 = num5 // 20
        num6 = num5 % 20
        ans7 = num6 // 10
        num7 = num6 % 10
        ans8 = num7 // 5
        num8 = num7 % 5
        ans9 = num8 // 1
        print(f"\n\t Current Balance: \n\t 1000 - {ans1} \n\t 500 - {ans2} \n\t 200 - {ans3} \n\t 100 - {ans4}")
        print(f"\t 50 - {ans5} \n\t 20 - {ans6} \n\t 10 - {ans7} \n\t 5 - {ans8} \n\t 1 - {ans9}")
        receipt1()
        exit()
    def denomi2():
        ans1 = amt_2 // 1000 
        num1 = amt_2 % 1000
        ans2 = num1 // 500
        num2 = num1 % 500
        ans3 = num2 // 200
        num3 = num2 % 200
        ans4 = num3 // 100
        num4 = num3 % 100
        ans5 = num4 // 50
        num5 = num4 % 50
        ans6 = num5 // 20
        num6 = num5 % 20
        ans7 = num6 // 10
        num7 = num6 % 10
        ans8 = num7 // 5
        num8 = num7 % 5
        ans9 = num8 // 1
        print(f"\n\t Current Balance: \n\t 1000 - {ans1} \n\t 500 - {ans2} \n\t 200 - {ans3} \n\t 100 - {ans4}")
        print(f"\t 50 - {ans5} \n\t 20 - {ans6} \n\t 10 - {ans7} \n\t 5 - {ans8} \n\t 1 - {ans9}")
        receipt2()
        exit()


    while go:
        greet()
        choose = input("Please select an option: ")
        if choose == "1":
            nm()
            bal_amt()
            exit()
            continue
        elif choose == "2":
            nm()
            in_dep()
            mon()
            dep = int(input("\nPlease select the amount that you want to deposit: "))
            dep_2 = dep + bal 
            print(f"Your current balance is {dep_2}")
            denomi1()
        elif choose == "3":
            nm()
            in_dep()
            mon()
            amt = int(input("Select an amount that you want to withdraw: "))
            if amt <= 4500:
                amt_2 = bal - amt
                print(f"Your remaining cash is now {amt_2}.")
                denomi2()
            else:
                print(f"Your current balance is only {bal}. Try again")
                continue
        elif choose.lower() == "4":
            nm()
            print("\n\n\n\t Sorry, this program is still under observation. Please try our other options... \n", "."*120)
            exit()
            continue
        elif choose == "5":
            acc = input("Enter your name: ")
            pn = input("Enter a pin: ")
            print("Account created.")
            exit()
            continue
        elif choose == "6":
            exit()
            break
        else:
            continue
