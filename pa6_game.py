
# Connor Aalto 11/30/22
#PA6 Test


from graphics import *
from buttonClass import *


class Drawing:
    #counter for number of class instances
    counter = 0
    def __init__(self, title, difficulty):
        self.title = title
        #counts how many objects of this class there are to be used to display images
        type(self).counter += 1
        self.difficulty = difficulty
        
    def display(self, gwin):

        imgTitle = Text(Point(600, 200*self.counter - 75), self.title)
        imgTitle.setSize(30)
        img = Image(Point(400, 100*self.counter), ('images/' + self.title + '.gif'))
        hitButton = Button(gwin, Point(300, 100*self.counter), 50, 50, "Select")
        hitButton.activate()

        img.draw(gwin)
        imgTitle.draw(gwin)


def main():
    win = GraphWin("Drawing Window", 600, 600)

    text = Text(Point(400, 50), "Select the drawing you want to recreate")
    text.setSize(40)
    text.draw(win)
    
    rabbit = Drawing('box', 'easy')
    rabbit.display(win)
    
    car = Drawing('arrow', 'medium')
    car.display(win)

    car = Drawing('pyramids', 'hard')
    car.display(win)
    
    stuff = input("ad")

main()
