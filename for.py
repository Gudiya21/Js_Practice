# i=0
# while True:
#     print(i)
#     i+=1

# for _ in iter(int, 1): 
    # pass
# print(_) 

# a= [1]
# for x in a:
#     a.append(x + 1)
#     print(x)

# temp = "5 degrees"
# cel = 0
# fahr = float(temp)
# cel = (fahr - 32.0) * 5.0 / 9.0
# print(cel)


# smallest = None
# print("Before:", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         break
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)

# word = "bananana"
# i = word.find("na")
# print(i)

# words = 'His e-mail is q-lar@freecodecamp.org'
# pieces = words.split()
# parts = pieces[3].split('-')
# n = parts[1]
# print(n)

# counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(counts.get('kris', 0))

# counts={'a':1,'b':2,'c':3}
# lst = []
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
# lst = sorted(lst, reverse=True)
# print(lst)


# print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )


# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\\S+@\\S+', s)
# print(lst)


# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
# mysock.close()

# import urllib.request
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

# class PartyAnimal:
#     x = 0
#     def party(self):
#         self.x = self.x + 2
#         print(self.x)

# an = PartyAnimal()
# an.party()
# an.party()


# class PartyAnimal:
#     x = 0
#     name = ''
#     def __init__(self, nam):
#         self.name = nam
#         print(self.name,'constructed')
#     def party(self):
#         self.x = self.x + 1
#         print(self.name,'party count',self.x)

# q = PartyAnimal('Quincy')
# m = PartyAnimal('Miya')

# q.party()
# m.party()
# q.party()

# a="banana"
# for i in a:
#     print(i)

# b=5
# c="gudia"*b
# print(c)

# class Category:
#   def __init__(self, category): 
#         self.ledger =[]
#         self.amount=0
#         self.category = category 


#   def check_funds(self,amount):
#     if self.amount< amount:
#       return False
#     else:
#       return True


#   def deposit(self,amount, description=""):
#     self.ledger.append({"amount":amount,"description":description})
#     self.amount += amount


#   def withdraw(self,amount,description=""):
#     if self.check_funds(amount) ==True:
#       self.amount -=amount
#       self.ledger.append({"amount":-amount,"description":description})
#       return True
#     else:
#       return False

#   # return balanace of budget 
#   def get_balance(self):
#     return self.amount

#   def __str__(self):
#     result=""
#     result+="*************Food*************"+"\n"
#     for transaction in self.ledger:
#       amount=0
#       description=""
#       for key,value in transaction.items():
#           if key=="amount":
#             amount = value
#           elif key=="description":
#             description=value
#       if len(description)>23:
#         description=description[:23]
#       amount = str(format(float(amount),'.2f'))
#       if len(amount)>7:
#         amount= amount[:7] 
#       result+= description + str(amount).rjust(30-len(description))+"\n"
#     result+="Total: "+str(format(float(self.amount),'.2f'))
#     return result



#   def transfer(self,amount,category):
#     if self.check_funds(amount)==True:
#       self.amount-=amount
#       self.ledger.append({"amount": -amount,"description":"Transfer to "+category.category})
#       category.ledger.append({"amount": amount,"description": "Transfer from "+self.category})
#       return True
#     else:
#       return False


# def create_spend_chart(categories):
#     return "------karu akaur ----"


# import datetime
# import dateutil.relativedelta

# # current time
# date_and_time = datetime.datetime.now()
# date_only = date.today()
# time_only = datetime.datetime.now().time()

# # calculate date and time
# result = date_and_time - datetime.timedelta(hours=26, minutes=25, seconds=10)

# # calculate dates: years (-/+)
# result = date_only - dateutil.relativedelta.relativedelta(years=10)

# # months
# result = date_only - dateutil.relativedelta.relativedelta(months=10)

# # days
# result = date_only - dateutil.relativedelta.relativedelta(days=10)

# # calculate time 
# result = date_and_time - datetime.timedelta(hours=26, minutes=25, seconds=10)
# result.time()

# import prob_calculator
# from unittest import main

# hat = prob_calculator.Hat(blue=4, red=2, green=6)
# probability = prob_calculator.experiment(
#     hat=hat,
#     expected_balls={"blue": 2,
#                     "red": 1},
#     num_balls_drawn=4,
#     num_experiments=3000)
# print("Probability:", probability)

# # Run unit tests automatically
# main(module='test_module', exit=False)




# def switch_demo(argument):
#     switcher = {
#         1: "January",
#         2: "February",
#         3: "March",
#         4: "April",
#         5: "May",
#         6: "June",
#         7: "July",
#         8: "August",
#         9: "September",
#         10: "October",
#         11: "November",
#         12: "December"
#     }
#     print switcher.get(argument, "Invalid month")



# def f(x):
#     match x:
#         case 'a':
#             return 1
#         case 'b':
#             return 2

# def methodA(self, arg1, arg2):

# ClassA.methodA(ObjectA, arg1, arg2)

# x = a or b
# print(x)



# print(3.2*(10**(-12)))

# for x in range(0.5, 5.5, 0.5):
#   print(x)

# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append(2, "Scott")
# print(sampleList)


# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki")
# print(sampleSet)


# def calculate (num1, num2=4):
#   res = num1 * num2
#   print(res)

# calculate(5, 6)


# var = "James" * 2  * 4
# print(var)

# for i in range(1, 5):
#     print(i)
# else:
#     print("this is else block statement" )

# x = 36 / 4 * (3 +  2) * 4 + 2
# print(x)

# var= "James Bond"
# print(var[2::-1])

# print(type([]) is list)

# x = 75
# def myfunc():
#     x = x + 1
#     print(x)

# myfunc()
# print(x)

# print(type(0xFF))

# aTuple = (1, 'Jhon', 1+3j)
# print(type(aTuple[2:3]))


# print(type(range(5)))

# print(2%6)

# a = 4
# b = 11
# print(a | b)
# print(a >> 2)


# x = 10
# y = 50
# if x ** 2 > 100 and y < 100:
#     print(x, y)

# print(-18 // 4)

# print('%x, %X' % (15, 15))
