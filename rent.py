import reading

class rent():

    #constructor
    def __init__(self,name):
        self.name = name        

    #function to initialize the costume, number and price
    def ask(self,costume,num,price):
        self.costume = costume
        self.num = num
        self.price = price
    
    #function to write the header
    def invoice_rent(self):
        file_name = 'Rent_'+self.name+'.txt'
        rent = open(file_name,'w')

        rent.write('\n')
        rent.write('______________________________Costume Rent House______________________________\n\n\n')
        rent.write('__________________________SundarHaraincha-10, Morang__________________________\n\n')
        rent.write('Pa No: 606456123________________________________________Date: '+str(reading.getDate())+'\n\n')
        rent.write('Name: '+self.name+'______________________________________Rent Invoice'+'\n\n')
        rent.write('S.N   Costume(Brand)                                  Quantity          Price  \n')
        
    #function for rent
    def renting(self):

        file = open("costume1.txt","r")
        lines = file.readlines()

        #making a 2d list
        rows = []
        for line in lines:
            list2 = [word.strip() for word in line.split(',')]
            rows.append(list2)

        file.close()

        #initialize the variables
        total_price = 0
        file_name = 'Rent_'+self.name+'.txt'
        rent = open(file_name,'a')
        count = 1 
        
        another = "Y"
        
            
        while another.upper() == 'Y':
            try:
                index = True
                while index: 
                    choice = int(input("The S.N. of the costume you want to Rent: "))
                    #if costume selected is less than 1 or greater than length of the list
                    if choice < 1 or choice > 8:
                        print("Sorry we dont have the costume right now.")
                        index = True 

                    #if costume selected is greater than 0 or smaller than or equal to length of the list
                    else:               
                        try:
                            if choice == 1:
                                print('1  Cop Costume Set,              Cartmax,         $15,   '+rows[0][3])
                            if choice == 2:
                                print('2  Formal Suite (Black Premium), Megaplex,        $14.5, '+rows[1][3])
                            if choice == 3:
                                print('3  Fairy Costume Full Set,       DollarSmart,     $18,   '+rows[2][3])
                            if choice == 4:
                                print('4  Shirt Pant,                   Jouie vutton,    $30,   '+rows[3][3])
                            if choice == 5:
                                print('5  Doura Suruwal,                CG,              $12,   '+rows[4][3])
                            if choice == 6:
                                print('6  Kurtha Suruwal,               Nike,            $8,    '+rows[5][3])
                            if choice == 7:
                                print('7  Vest Half-pant,               Fashion,         $10,   '+rows[6][3])
                            if choice == 8:
                                print('8  Jama,                         Kardon,          $5,    '+rows[7][3])
                            
                            print('')
                            print("We have",rows[choice-1][3],"stock available.")

                            try_again = True                    
                            while try_again:

                                #ask user how many???
                                num = int(input("How many do you want???? : "))
                                if num < 1:
                                    print("Rent can't be zero or less than zero")
                                    print('')
                                    try_again = True     
                                elif num <= int(rows[choice-1][3]):

                                    #update the stock in list
                                    new_stock = int(rows[choice-1][3])-num
                                    rows[choice-1][3] = str(new_stock)

                                    #call ask function to initialize parameters
                                    self.ask(rows[choice-1][0],num,float(rows[choice-1][2].strip('$'))*num)
                                    costum = self.costume+"("+rows[choice-1][1]+")"

                                    #append the costumes in the invoice
                                    rent.write(str(count)+' '*(6-len(str(count)))+costum+' '*(48-len(costum)) +str(self.num)+' '*(18-len(str(self.num)))+'$'+str(self.price)+'\n')
                                        
                                    count = count + 1
                                    try_again = False
                                else:
                                    print("Don't have that much. Sorry!!")
                                    print('')
                                    try_again = True
                            another = input('Do you want to try renting again?? Y/N :')
                            total_price += self.price
                            index = False
                        except IndexError:
                            print('')
                            print("We will update the list soon.")
            except ValueError:
                print('')
                print("Please Enter the number.")
        else:

            #write the footer for the invoice
            rent.write('\n\n\n\n')
            rent.write('_______________________________________________total price : $'+str(total_price)+'\n\n\n')
            rent.write('Please! Return in 5 days else 5 percentage fine will be added.\n\n')
            rent.write('________________________Time:'+str(reading.getTime())+'______________________________')
            print('')
            print("Collect your invoice Thank you!!!!!!!!!!!")

            #update the costume1.txt file
            file = open('costume1.txt','w')
            for i in range(len(rows)):
                file.write(str(rows[i][0])+', '+str(rows[i][1])+', '+str(rows[i][2])+', '+str(rows[i][3])+'\n')

            file.close()