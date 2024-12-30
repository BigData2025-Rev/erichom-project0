newSet = {(1,2), (1,3)}

print(newSet)
if (1,2) in newSet:
    print("FOUND")

newTuple = (1,2)

if newTuple in newSet:
    print("tuple found.")

newTuple = (1,4)

if newTuple not in newSet:
    print("tuple not found.")

def returnTypes():
    if newTuple not in newSet:
        if newTuple in newSet:
            return 'nope'
        
print(returnTypes())

print(type((1,2)))