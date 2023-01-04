print("menu")
print("1)kitkat : 1aed")
print("2)snicker : 2aed")
print("3)m&ms : 3aed")
print("4)chips : 1aed")
print("5)juice : 2aed")
print("6)ice tea : 5aed")
print("7)water : 1aed")
print("8)pepsi : 3aed")
print("9)mountain dew : 3aed")
print("10)redbull : 4 aed")
money=int(input("enter money:"))
number=input("enter number of the item")
if number=='1':
  print("you bought kitkat")
  money=money-1
elif number=='2':
  print("you bought snicker")
  money=money-2
elif number=='3':
  print("you bought m&ms")
  money=money-3  
elif number=='4':
  print("you bought chips")
  money=money-1
elif number=='5':
  print("you bought juice")
  money=money-2
elif number=='6':
  print("you bought ice tea")
  money=money-5
elif number=='7':
  print("you bought water")
  money=money-1
elif number=='8':
  print("you bought pepsi")
  money=money-3
elif number=='9':
  print("you bought mountain dew")
  money=money-3
elif number=='10':
  print("you bought redbull")
  money=money-4
print("your change:",money)