bankdata=[["157380","ron",56000],
           ["285379","itachi",68000],
           ["572981","sasuke",19000],
           ["681093","madara",89000]
           ]

def balanceEnquiry():
    for i in bankdata:
        if i[0]==id:
            print(i[2])

def cashwithdrawl():
    for u in bankdata:
        if u[0]==id:
            print(u)

def deposit():
    for t in bankdata:
        if t[0]==id:
            print(t)                        

id=input("enter your id") 
print("press 1 for balance enquiry")
print("press 2 for cash withdrawl")
print("press 3 for deposit")

choice=int (input("enter your choice"))

if choice==1:
    balanceEnquiry()

elif choice==2:
    cashwithdrawl()

else :
    deposit()        