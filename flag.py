#Shape of the Philippine flag
print("="*100, "\n\n\t Philippine flag \n\n\t Red: valor and bravery. \n\t",
      "White: purity and innocence. \n\t Blue: vigilance, perseverance, and justice. \n")
for a in range(-1,6):
    for b in range(-1, a+1):
        print("-", end=" ")
    for c in range(5, a, -1):
        print("*", end=" ")
    for d in range(4, a, -1):
        print("*", end=" ")
    
    print()
for f in range(-1, 6):
    for g in range(-1, 6):
        print("-", end =" ")
    print()
