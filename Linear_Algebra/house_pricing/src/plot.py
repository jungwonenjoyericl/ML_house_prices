import matplotlib.pyplot as plt
from random import randint

def plot(X : list[int], Y : list[int]):

    plt.scatter(X,Y)
    plt.show()

def createRandomPoints(n : int) -> int:
    xCoordList : list[int] = [] 
    yCoordList : list[int] = []

    for i in range(n):
        xCoordList.append(randint(1,100))
        yCoordList.append(randint(1,100))
    return xCoordList, yCoordList

x, y = createRandomPoints(100)
print(len(x))

plot(x,y)



