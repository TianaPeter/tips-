#If the bill was $150.00, split between 5 people, with 12% tip. 
print("welcome to tips calculator!")
bill=input("what was the total bill?\n")
tips = input("how much tips will you love to give? 10, 12, or 15?\n")
spilt=input("how many people to spilt the bill?\n")
eachper=(float(bill)/int(spilt))/100*(100+int(tips))
roun=round(eachper,2)
final="{:.2f}".format(roun)
print(f"each person should pay ${final} dollars")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
