def acronym(n):
    new_n = n.split()
    a = ""    # like this we have created acronym of the number for the follwoing by creating a empty string and getting stored it in the form of the and upper value
    for i in new_n:
        a += str(i[0]).upper()
    return a

while True:
   
   print("choose 1) acronym or 2) exit")
   try :
    
    choose = int(input("enter a your choice:"))
   
    if choose == 1 :
            name = input("enter a name that u want the acroynm of:")
            print(acronym(name))
   
    elif choose == 2 :
      break
    
    else:
        print("please re-enter either choice 1 or 2 ")

   except ValueError:
       print("Invalid input. Please enter a valid integer.")
