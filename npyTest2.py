import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#fig, ax = plt.subplots()
#
# x = np.array([[0, 0, 255], [255, 255, 0], [0, 255, 0]])
# #def update(img, x):
# for obj in np.nditer(x):
#     print obj
# updateIn=33
#
# print 77
#
#a = np.arange(256).reshape(16,16)
a = np.zeros((16,16))
c=0
while 1:
    # for i,obj in enumerate(np.nditer(a, op_flags=['readwrite'])):
    #    # print obj
    #     if c == 255:
    #         c=0
    #     if i == 255:
    #         xx=i+c
    #         xx1=xx+1
    #         #obj[xx] = 255
    #         #obj[xx1] = 0
    #         obj[...] = 666
    #         obj[...] = 666

    print a
    print "########################################################################################################################"
    for index, cc in np.ndenumerate(a):
       # print index[0]
        if c == 15:
            c=0
        if index[1] == c:
            #a[(1,0)]=66
            # try:
            #     a[(index[0]+c,index[1]+c)]=666
            #
            #     a[(index[0] + c-1, index[1] + c-1)] = 0
            # except:
            #     pass
            try:
                a[(index[0] + 1, index[1] + 1)] = 255

                #a[(index[0], index[1])] = 0
            except:
                pass
       # a[index]=77
        #print(index, cc)
    c += 1
   # print "kokot"
#img = ax.imshow(x, interpolation='nearest')
#anime = animation.FuncAnimation(fig, update, fargs=(img, x), frames=33, interval=updateIn)
#plt.show()