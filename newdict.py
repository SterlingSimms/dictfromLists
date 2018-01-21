name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def liststoDict(list1, list2):
    if len(list2) > len(list1):
        newList = zip(list2, list1)
    else: 
        newList = zip(list1, list2)
    newDict = dict(newList)
    print newDict  
liststoDict(name, favorite_animal)