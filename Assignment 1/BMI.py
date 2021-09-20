print('BMI Calculater')
while(1):
    weight = float(input('Enter your Weight in Kilograms: '))
    height = float(input('Enter your height in meters: '))
    BMI = (weight) / ((height) * (height))
    print('Your BMI is :' + str(BMI))
    usrInput = input('Do you want to restart?? y/n: ')
    if (usrInput == 'n'):
        break
print('Thank you for using BMI calculater')