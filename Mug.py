#!/usr/bin/python3

# Script name: Mug.py

# Mark Bradley
# 12/12/19
# Peter Normington
# 16/12/2019

# demo of a class representing a commom tea mug

class Mug:
    ''' Class to describe the common Mug.
        size: capacity in ml.
        decoration: colour picture etc.
        state: how many ml are in the mug at the moment.
        clean: True if the mug is in a pristine state
        content: what sort of stuff is in the mug'''
    
    def __init__(self,size=350,decoration='plain white'):
        # Initalize an instance of mug
        '''This builds a clean, empty mug with a default size and decoration unless new values are supplied.
        '''
        self.__size=size
        self.__decoration="\'" + decoration + "\'"
        # Mugs have no content at the start
        self.__state=0
        self.__clean=True
        self.__content='nothing'
        
    def fill(self,quantity,content='tea'):
        # quantity is the amount in ml put in the mug.
        ''' fill adds to your mug a quantity in ml of the beverage specified
        '''
        self.__content=content
        
        if quantity > (self.__size - self.__state):
            self.__state = self.__size
            print('Oh dear! Some of that '+ self.__content + ' overflowed!')
            
        else:
            self.__state = quantity
            
        self.__clean = False                
        
    def empty(self):

        # Pour away the contents
        ''' empty the mug
        '''
        self.__state=0
        
    def sip(self,sip_size=30):
        # Take a sip of the drink, default is 30ml
        ''' Take a sip of your beverage; a standard sip is 30ml
            If you have drunk it all you will get an appropriate warning.
        '''
        if self.__state==0:
            report_string ='Your mug is already empty!'
        elif sip_size >= self.__state:
            self.__state = 0
            report_string ='Oh dear.  All your ' + self.__content + ' has gone, so you were short-changed!'
        else:
            self.__state = self.__state - sip_size
            report_string = 'Mmm, tasty sip, that!'
        print(report_string)
    
    def wash(self):
        ''' wash uses the built-in "empty" function and sets "clean" back to True.
        '''
        self.empty()
        self.__clean=True
        
    def whatsleft(self):
        # Returns a string commenting on the current state of the mug
        ''' Tells you about the contents of your mug.
        '''
        if self.__state==0:
            state_s = 'is empty.'
        elif self.__state==self.__size:
            state_s = 'is full of ' + self.__content + '.'
        else:
            state_s = 'has ' + str(self.__state) + 'ml of ' + self.__content + ' left.'
        
        return('The ' + self.__decoration + ' mug ' + state_s)
    
if __name__ == '__main__':
    
    print('Class mug test')
    #'Create an object of class mug - mymug, holds a maximun of 450ml and has a picture of a blue bird'
    mymug=Mug(450,'Blue Bird')
    #'Create an object of class mug - petersmug, holds a maximun of 350ml and has a slogan printed on it'
    petersmug = Mug(350,"We're with Greta!")
    # Fill the mymug with 400ml of coffee
    mymug.fill(400,'coffee')
    # Check mymug
    print(mymug.whatsleft())
    # Have a sip from my mug - default sip size is 30ml
    mymug.sip()
    print(mymug.whatsleft())
    # Have a big sip
    mymug.sip(500)
    print(mymug.whatsleft())
    mymug.sip(50)

    petersmug.fill(600,'ginger ale')
    print(petersmug.whatsleft())
    print(mymug.whatsleft())
    
