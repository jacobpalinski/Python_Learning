class Budget:
    
    def __init__(self):
        self.food=[]
        self.clothing=[]
        self.entertainment=[]
    
    def breakdown_by_percentage(self):
        food_total = sum([sum(list(item.values())) for item in self.food])
        clothing_total = sum([sum(list(item.values())) for item in self.clothing])
        entertainment_total = sum([sum(list(item.values())) for item in self.entertainment])

        total_expenditure= food_total + clothing_total + entertainment_total

        return print(f'Food : {(food_total/total_expenditure)*100}%', f'Clothing : {(clothing_total/total_expenditure)*100}%', f'Entertainment: {(entertainment_total/total_expenditure)*100}%',sep='\n')
     
class Food:
    
    def __init__(self,item,amount):
        self.item=item
        self.amount=amount

    def add_to_budget(self,Budget):
        Budget.food.append({self.item : self.amount})

    def remove_from_budget(self,Budget):
        for item in Budget.food:
            if self.item in item:
                Budget.food.remove(item)


class Clothing(Food):
    
    def add_to_budget(self,Budget):
        Budget.clothing.append({self.item : self.amount})
    
    def remove_from_budget(self,Budget):
        for item in Budget.clothing:
            if self.item in item:
                Budget.clothing.remove(item)

class Entertainment(Food):
    
    def add_to_budget(self,Budget):
        Budget.entertainment.append({self.item:self.amount})
    
    def remove_from_budget(self,Budget):
        for item in Budget.entertainment:
            if self.item in item:
                Budget.entertainment.remove(item)
            

budget=Budget()
apple=Food('Apple',3.20)
apple.add_to_budget(budget)
jeans=Clothing('Levis Jeans',85)
jeans.add_to_budget(budget)
movie=Entertainment('Heat',15)
movie.add_to_budget(budget)
budget.breakdown_by_percentage()
movie.remove_from_budget(budget)
budget.breakdown_by_percentage()












