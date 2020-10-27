class Duck:
    def __init__(self,**kwargs):
        self.attributes=kwargs

    def speak(self):
        print(self.attributes.get('Speak',None))
    def walk(self):
        print(self.attributes.get('Walk',None))

    @property
    def color(self):
        return self.attributes.get('color')

    @color.setter
    def color(self,a):
        self.attributes['color']=a
        print('In the color 2 function and setting the color attributes',a)

    @color.deleter
    def color(self):
        del self.attributes['color']
        print('In the color 3 function and deleting the color attributes')

def main():
    donald = Duck()
    donald.color='blue'
    print(donald.color)
    donald.color='red'
    print(donald.color)
    del donald.color

if __name__ == '__main__':
    main();

    # he sure doesn't quack
    #he fly sometimes and shit over human's head
