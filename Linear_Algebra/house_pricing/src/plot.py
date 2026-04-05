import matplotlib.pyplot as plt
import os
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

def main():
    x, y = createRandomPoints(100)
    print(len(x))
    
    plot(x,y)

    projectPath = os.getcwd()
    plotImagePath = os.path.join(projectPath, "data", "plot.png")
    plt.savefig(plotImagePath)

if __name__ == "__main__":
    main()

