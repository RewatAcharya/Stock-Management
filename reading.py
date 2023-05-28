import datetime


def costume():
    file = open("costume1.txt","r")
    lines = file.readlines()

    #making a 2d list
    rows = []
    for line in lines:
        list2 = [word.strip() for word in line.split(',')]
        rows.append(list2)
    
    file.close()

    #show the details of the list
    print('1  Cop Costume Set,              Cartmax,         $15,   '+rows[0][3])
    print('2  Formal Suite (Black Premium), Megaplex,        $14.5, '+rows[1][3])
    print('3  Fairy Costume Full Set,       DollarSmart,     $18,   '+rows[2][3])
    print('4  Shirt Pant,                   Jouie vutton,    $30,   '+rows[3][3])
    print('5  Doura Suruwal,                CG,              $12,   '+rows[4][3])
    print('6  Kurtha Suruwal,               Nike,            $8,    '+rows[5][3])
    print('7  Vest Half-pant,               Fashion,         $10,   '+rows[6][3])
    print('8  Jama,                         Kardon,          $5,    '+rows[7][3])


#get today's date 
def getDate():
    return str(datetime.datetime.now().year)+'/'+str(datetime.datetime.now().month)+'/'+str(datetime.datetime.now().day)

#get now time (:
def getTime():
    return str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)+':'+str(datetime.datetime.now().second)
