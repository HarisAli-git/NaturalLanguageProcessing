
def getWordsList(filename):
    
    l1 = []
    l2 = []
    #opening the StopWords.txt file 
    file1 = open("StopWords.txt", 'r')
    #this will copy each word in the list one by one
    for e in file1:
        l1.append(e)
    
    #removing \n
    for e in list(l1):
        k = l1.index(e)
        if len(e) >= 2:
            l1[k] = e[0:-1]
    #print(l1)
    
    #l1 has StopWords list[]

    # a file named filename, will be opened with the reading mode.
    file = open(filename, 'r')
    for each in file:
    #firstly, removing Alphanumeric data and converting to lower case
        each = each.lower()
        each = each.split(" ")
        for x in list(each):
            if x == '.' or x == '(' or x == ')' or x == '"' or x == ',' or x == '?':
                each.remove(x)
            for i in range(len(x)):    
                if x[i] >= str(0) and x[i] <= str(9):
                    each.remove(x)
                    break
        #Now removing Special characters from in between the words
        for x in list(each):
            ix = (each.index(x))
            x2 = ""
            for i in range(len(x)):    
                    if x[i] >= 'a' and x[i] <= 'z':
                        x2 = x2 + x[i]
            each[ix] = x2
        
        #Now removing empty blanks
        for x in list(each):
            if x == '':
                each.remove(x)
        
        #now removing StopWords
        for x in list(each):
            for jk in list(l1):
                if x == jk:
                    each.remove(x)
                    break
        
        #finally copying the list into new list
        l2.append(each)
    #l2 holds modified data from the file
    
    return l2

def printWord(my_list):
    from collections import Counter
    total_count = 0
    
    for each in my_list:
        for x in list(each):
            total_count += 1
    
    my_dict = {
        "Word": 0
    }
     
    
    for each in my_list:
        for x in each:
            if x in my_dict.keys():
                my_dict[x] = my_dict[x] + 1
            else:
                my_dict[x] = 1
    
    #now Counting Dictionary elements
    count = Counter(my_dict)
    
    #picking up highest 100 values
    top100 = count.most_common(100)    
    
    print("Now printing the 100 Top values!\n")
    print("Word:  Count:  Probability: ")
    
    for h in top100:
        print(h[0], "  ", h[1], "  ", h[1]/total_count, "\n")

l = []
l1 = []

i = 1

while i < 5:
    l = getWordsList("data" + str(i) + ".txt")
    l1.extend(l)
    i +=1
printWord(l1)
