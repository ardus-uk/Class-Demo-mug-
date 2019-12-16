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
        self.size=size
        self.decoration="\'" + decoration + "\'"
        # Mugs have no content at the start
        self.state=0
        self.clean=True
        self.content='nothing'
        
    def fill(self,quantity,content='tea'):
        # quantity is the amount in ml put in the mug.
        ''' fill adds to your mug a quantity in ml of the beverage specified
        '''
        self.content=content
        
        if quantity > (self.size - self.state):
            self.state = self.size
            print('Oh dear! Some of that '+ self.content + ' overflowed!')
            
        else:
            self.state = quantity
            
        self.clean = False                
        
    def empty(self):

        # Pour away the contents
        ''' empty the mug
        '''
        self.state=0
        
    def sip(self,sip_size=30):
        # Take a sip of the drink, default is 30ml
        ''' Take a sip of your beverage; a standard sip is 30ml
            If you have drunk it all you will get an appropriate warning.
        '''
        if self.state==0:
            report_string ='Your mug is already empty!'
        elif sip_size >= self.state:
            self.state = 0
            report_string ='Oh dear.  All your ' + self.content + ' has gone, so you were short-changed!'
        else:
            self.state = self.state - sip_size
            report_string = 'Mmm, tasty sip, that!'
        print(report_string)
    
    def wash(self):
        ''' wash uses the built-in "empty" function and sets "clean" back to True.
        '''
        self.empty()
        self.clean=True
        
    def whatsleft(self):
        # Returns a string commenting on the current state of the mug
        ''' Tells you about the contents of your mug.
        '''
        if self.state==0:
            state_s = 'is empty.'
        elif self.state==self.size:
            state_s = 'is full of ' + self.content + '.'
        else:
            state_s = 'has ' + str(self.state) + 'ml of ' + self.content + ' left.'
        
        return('The ' + self.decoration + ' mug ' + state_s)
    
if __name__ == '__main__':
    
    print('Class mug test')
    #'Create an object of class mug - mymug, holds a maximun of 450ml and has a picture of a blue bird'
    mymug=Mug(450,'Blue Bird')
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
    
