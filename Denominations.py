print("\n\t Creating denomination of your given number. \n", "-"*100)
amount = eval(input("\n\t Enter an amount: "))
print("\n\t -------------------------------------------")

thou = amount // 1000
thou_sukli = amount % 1000

hun5 = thou_sukli // 500
hun5_s = thou_sukli % 500

hun2 = hun5_s // 200
hun2_s = hun5_s % 200

hun1 = hun2_s // 100
hun1_s = hun2_s % 100

fifty = hun1_s // 50
fifty_s = hun1_s % 50

twenty = fifty_s // 20
twenty_s = fifty_s % 20

ten = twenty_s // 10
ten_s = twenty_s % 10

five = ten_s // 5
five_s = ten_s % 5

one = five_s // 1


print("\n\t", thou, "- 1000 \n\t", hun5, "- 500 \n\t", hun2, "- 200 \n\t", hun1, "- 100 \n\t", fifty, "- 50 \n\t", twenty, "- 20 \n\t", ten, "- 10 \n\t", five, "- 5 \n\t", one, "- 1 \t")