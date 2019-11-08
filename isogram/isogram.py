def is_isogram(str):
    
    #User inputs word. Function lower cases input 
    #and determines if word is isogram.
    str = input("Enter a word \n")
    str = str.lower()
    for char in str: 
        #iterates over each character for repetition; 
        #if more than 1, not isogram
        if  str.count(char) > 1: 
            print(str +" != isogram")
            return False #return prevents multiple instances from printing
        else: 
            print(str +" = isogram")         
            return True #return prevents multiple instances from printing
    

is_isogram(str)
