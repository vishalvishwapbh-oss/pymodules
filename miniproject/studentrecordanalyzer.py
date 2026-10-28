name=input("enter the name : ")
income=float(input("enter the monthly income: "))
food=float(input("enter the monthly food expense: "))
travel=float(input("enter the monthly tarvel charge: "))
study=float(input("enter the study material expense: "))
mobile=float(input("enter the mobile recharge expense: "))
other=float(input("enter the other expense: "))
texp=(food+travel+study+mobile+other)
available_balance=income-texp
if texp>0:
    foodprcent=(food/texp)*100
    travelprcent=(travel/texp)*100    
    studyprcent=(food/texp)*100
    mobileprcent=(food/texp)*100
    otherprcent=(food/texp)*100
else:
    foodprcent=0
    travelprcent=0
    studyprcent=0
    mobileprcent=0
    otherprcent=0
if income>0:
    savings_rate=available_balance/income*100
else:
    savings_rate=0
print("\n----- MONTHLY BUDGET REPORT -----")
print("Student:", name)
print(f"Monthly income: Rs. {income}")
print(f"Food: Rs. {food} ({foodprcent}%)")
print(f"Travel: Rs. {travel} ({travelprcent}%)")
print(f"Study materials: Rs. {study} ({studyprcent}%)")
print(f"Mobile/Internet: Rs. {mobile} ({mobileprcent}%)")
print(f"Other: Rs. {other} ({otherprcent}%)")
print(f"Total expenses: Rs. {texp}")
print(f"Remaining balance: Rs. {available_balance}")
print(f"Savings rate: {savings_rate}%")