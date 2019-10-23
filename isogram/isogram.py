def is_isogram(str):
    #Uses list method count; returns count of how many times obj occurs in list
    #ToDo: Add ignore multiple - and space
    word = input("Enter a word \n")
    realWord = list(word)
    for char in realWord : #convert  to list 
        #counts = realWord.count(char)
        if  realWord.count(char) > 1:
            print(word +" != isogram") #responds to each letter, prints #chars
        else:
            print(word +" = isogram")

is_isogram(str)
