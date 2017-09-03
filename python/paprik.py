import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


N = 100
R=N-1
ON = 255
OFF = 0
vals = [ON, OFF]
grid = np.array([])
grid = np.zeros(N*N).reshape(N, N)

def addGlider(i, j, grid,N):
    glider = np.random.choice(vals, R*R, p=[0.2, 0.8]).reshape(R, R)
    grid[i:i+N, j:j+N] = glider

updateIn = 33
addGlider(1, 1, grid, N)
def update(frameNum, img, grid, N):
    c=0
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            if i==R and j==R:
                try:
                    newGrid[0:1, 0:j] = ON
                    print 666
                except:
                    continue
            if newGrid[i-1, j] == ON:
                try:
                    newGrid[i, j] = OFF
                    newGrid[i+1, j] = ON
                except:
                    continue
            try:
                if grid[i-1,j]==OFF and grid[i+1,j]==OFF:
                    newGrid[i:i+2, j:j+2] = ON
            except:
                continue


    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,



# set up the animation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
anime = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),frames=33,interval=updateIn)
# number of frames?
# set the output file
#if args.movfile:
#    anime.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()






# print grid
# c=0
# for y in np.nditer(grid, op_flags=['readwrite']):
#     #y += 3
#     #y *= 0
#     c+=1
#     y[...] = c
#
# print grid
#addGlider(1, 1, grid)