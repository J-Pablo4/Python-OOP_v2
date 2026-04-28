class Bird:
    def fly(self):
        return "Bird is flying"
    
class Penguin(Bird):
    
    def fly(self):
        return "Penguins can't fly, but they can swim"
    
def let_fly(bird):
    print(bird.fly())

sparrow = Bird()
penguin = Penguin()
let_fly(sparrow)
let_fly(penguin)