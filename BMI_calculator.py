def bmi_checker(w,h):
    bm = w/(h*h)
    print("your BMI:",bm)
    if bm > 0:
        if bm < 18.5:
            return "You are not Healthy,Kindly look after your health"
        elif 18.5 <= bm <= 24.9:
            return "You are Healthy , Be assure"
        else:
            return 'You are overweight'
    else:
        return 'Error: pls give us a valid W & H'
    
if __name__ == '__main__':
    print("Welcome to BMI Calculator")
    print()
    while True:
        weight = int(input("enter your weight in KG: "))
        height = float(input('enter your height in "M":'))

        print(bmi_checker(weight,height))

        name = int(input('''
1)Continue
2)Exit
select 1 or 2 : '''))
        
        if name == 2:
            print("Thank You for using our Application")
            break
