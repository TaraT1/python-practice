def distance(strand_a, strand_b):
    '''
    compare 2 strings with equal length [len(string)]
        -iteration and indexing '''
    if len(strand_a) == len(strand_b): 
        #val of chars in a & b; iterate over string, compare at index
        for char in strand_a:
            if char in strand_a == char in strand_b:
                char = i++

    else: 
        print("Problem: the strands have unequal lengths")
        return False 
        

    '''Consider sequences: set vs list vs tuple (csv, unique, dupes)
    
    find & index (str, beg=0, end=len(string)) 
    https://www.tutorialspoint.com/python/python_strings.htm

    hammering distance = count the # of differences
    '''
    pass
