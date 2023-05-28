from reading import costume
from rent import rent
from returning import returning

print("*****************************************************************************")
print('                           Costume Rent House                                ')
print('                          Welcome to the shop (::                            ')
print("*****************************************************************************")
print("*****************************************************************************")



doAgain = 'Y'
while doAgain == 'Y':
    try:
        print()
        print('''Press 1 to see the Costumes
Press 2 to Rent Costumes
Press 3 to Return Costumes
Press 4 to Exit''')
        print()
        press = int(input('Press (1-4) : '))  #integers to display, rent, return and exit
    
        if press == 1:
            costume()
        elif press == 2:
            FName_rent = input("First Name Please : ")
            LName_rent = input("Last Name Please : ")
            a = rent(FName_rent+'_'+LName_rent)
            a.invoice_rent()
            a.renting()
        elif press == 3:
            first_return = input("First Name Please : ")
            last_return = input("Last Name Please : ")
            b = returning(first_return+'_'+last_return)
            b.invoice_return()
            b.remit()
        elif press == 4:
            print("*****************************************************************************")
            print("           Thank you for the visit hope to see you again soon                ")
            print("*****************************************************************************")
            break
        else:               #if integer is given except 1-4
            print()
            print('Do not have the choices')
    except ValueError:          #if the string value is given instead of integer
        print('')
        print("Please Enter the number from (1-4).")