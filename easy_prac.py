even = []
odd_sum = 0
while True:
    ask = eval(input("\n\t Enter a number: "))
    if ask == 0:
        break
    elif ask % 2 == 0:
        even.append(ask)
    else:
        odd_sum += ask
print(f"\n\t Sum of odd numbers: {odd_sum}")
print(f"\n\t Even numbers: {even} \n")