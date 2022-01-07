import datetime
import random

basePrice = 5

class Product:
    def __init__(self, designation, quality, dueDate):
        self.designation = designation
        self.quality = quality
        self.dueDate = dueDate
        self.price = basePrice + (quality*0.1)
    
    def throwAway(self, date):
        throw = False;
        if("cheese" in self.designation):
            if((self.dueDate - date).days <= 0 or self.quality <= 30):
                throw = True
        else:
            if(self.quality < 0):
                throw = True
        
        return(throw)

    def qualityChange(self, date):
        if("cheese" in self.designation):
            self.quality-=1
            self.price = basePrice + (self.quality*0.1)
        else:
            if(self.quality < 50):
                overDueDate = (date - self.dueDate).days
                if(overDueDate >= 10 and overDueDate % 10 == 0):
                    self.quality+=1





if __name__=='__main__':

    products = []

    simulateDays = int(input("How many days would you like to simulate: "))

    startDate = datetime.date(2022,1,7)
    date = startDate
    products.append(Product("cheese1", 20, startDate + datetime.timedelta(days=random.randint(50,100))))
    products.append(Product("wine1", -1, startDate + datetime.timedelta(days=20)))
    products.append(Product("cheese2", 50, startDate + datetime.timedelta(days=random.randint(50,100))))
    products.append(Product("wine2", 49, startDate + datetime.timedelta(days=10)))
    products.append(Product("cheese3", 31, startDate + datetime.timedelta(days=random.randint(50,100))))
    products.append(Product("wine3", 1, startDate + datetime.timedelta(days=1)))

    
    
    for i in range (simulateDays):
        throw = []
        for j in range (len(products)):
            products[j].qualityChange(date)
            if(products[j].throwAway(startDate) == True):
                print(products[j].designation + " had to be thrown away. Its quality was: ", products[j].quality, " and it's due date was ", products[j].dueDate)
                print(" ")
                throw.append(products[j])
            else:
                print("Designation: " + products[j].designation)
                print("Price: ", products[j].price)
                print("Quality: ", products[j].quality)
                print(" ")
        for prod in throw:
            products.remove(prod)    
        date = date+ datetime.timedelta(days=1)
        
