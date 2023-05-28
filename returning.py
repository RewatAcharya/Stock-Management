import datetime
import reading

class returning():
    #constructor for the class
    def __init__(self,name):
        self.name = name
    
    #asking for stock and date of the rent
    def ask_return(self,date_rent,stock):
        self.date = date_rent
        self.stock = stock

    #function to calculate fine
    def fine(self,principal,time,rate):
        fine = (principal*time*rate)/100
        return fine

    #function to write the header of return invoice
    def invoice_return(self):
        file_name = 'Return_'+self.name+'.txt'
        rent = open(file_name,'w')

        rent.write('\n')
        rent.write('______________________________Costume Rent House______________________________\n\n\n')
        rent.write('__________________________SundarHaraincha-10, Morang__________________________\n\n')
        rent.write('Pa No: 606456123________________________________________Date: '+str(reading.getDate())+'\n\n')
        rent.write('Name: '+self.name+'______________________________________Return Invoice'+'\n\n')
        rent.write('S.N   Costume(Brand)                                  Quantity          Price  \n')

    #function for return
    def remit(self):

        file = open("costume1.txt","r")
        lines = file.readlines()

        #making a 2d list
        rows = []
        for line in lines:
            list2 = [word.strip() for word in line.split(',')]
            rows.append(list2)

        file.close()

        #initializing variables
        new_fine = 0
        total = 0
        grand_total = 0
        file_name = 'Return_'+self.name+'.txt'
        rent = open(file_name,'a')
        count = 1
        another = "Y"
        
        while another.upper() == 'Y':             
            print('')
            try:
                index = True
                while index: 
                    choice = int(input("The S.N. of the costume you want to Return: "))
                    if choice < 1 or choice > 8:            #if costume selected is less than 1 or greater than length of the list
                        print("Sorry we dont have the costume right now.")
                        index = True
                    else:                                   #if costume selected is greater than 1 or smaller or equals than length of the list
                        try:  
                            available = int(rows[choice-1][3])
                    
                            stocked = int(input('How many costumes were Rented??: '))
                            stock = stocked + available

                            #update the stock in the list
                            rows[choice-1][3] = str(stock)
                            date_rent = int(input('Enter the day you took costume: '))

                            total = total + (float(rows[choice-1][2].strip('$'))*int(stocked))

            
                            self.ask_return(date_rent,stocked)

                             #if the day is smaller than today's date for a month
                            if self.date + 5 < int(datetime.datetime.now().day) :  
                                fine = self.fine(float(rows[choice-1][2].strip('$'))*self.stock,int(datetime.datetime.now().day)-(self.date+5),0.05)
                            
                             #if the day is greater than today's date for a month
                            elif self.date > int(datetime.datetime.now().day) :
                                fine = self.fine(float(rows[choice-1][2].strip('$'))*self.stock,((int(datetime.datetime.now().day)-self.date)+30)-5,0.05)
                            
                            #if the day is not more than 5 days
                            else:
                                fine = 0
                            new_fine += fine
                            costum = rows[choice-1][0]+"("+rows[choice-1][1]+")"

                            #appending the returned costume in the invoice
                            rent.write(str(count)+' '*(6-len(str(count)))+costum+' '*(48-len(costum))+str(self.stock)+' '*(18-len(str(self.stock)))+'$'+str(float(rows[choice-1][2].strip('$'))*self.stock)+'\n')
                            count = count + 1
                            
                            index = False
                            another = input('Do you have another costume to return???: Y/N : ')
                        except IndexError:
                            print("Sorry We do not have that S.N.")
            except ValueError:
                print("Try Again (: ")
        else:

            # write the footer in the invoice 
            grand_total = total + new_fine
            rent.write('\n\n\n\n')
            rent.write('___________________________________________Total: $'+str(total)+'\n')
            rent.write('___________________________________________Fine: $'+str(new_fine)+'\n')
            rent.write('___________________________________________Grand Total: $'+str(grand_total)+'\n\n')

            rent.write('-------------------------------Bye Bye------------------------------------\n')
            rent.write('________________________Time:'+str(reading.getTime())+'______________________________')
            print()
            print("Collect invoice....")

            #update the stock file (costume1.txt)
            file = open('costume1.txt','w')
            for i in range(len(rows)):
                file.write(str(rows[i][0])+', '+str(rows[i][1])+', '+str(rows[i][2])+', '+rows[i][3]+'\n')
            
            file.close()