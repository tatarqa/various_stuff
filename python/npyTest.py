import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


N = 100
R=N-1
grid = np.random.choice([0,255], N*N, p=[0.2, 0.8]).reshape(N, N)
updateIn = 33
def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            if i==R and j==R:
                try:
                    newGrid[0:1, 0:j] = 255
                except:
                    continue
            if newGrid[i-1, j] == 255:
                try:
                    newGrid[i, j] = 0
                    newGrid[i+1, j] = 255
                except:
                    continue
            try:
                if grid[i-1,j]==0 and grid[i+1,j]==0:
                    newGrid[i:i+2, j:j+2] = 255
            except:
                continue
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
anime = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),frames=33,interval=updateIn)
plt.show()
