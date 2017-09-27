FINAL_SUM = 1000
def check():


    for x in range(1,FINAL_SUM):
        for y in range(1,FINAL_SUM):
            for z in range(1,FINAL_SUM):
                if x**2+y**2==z**2:
                    if y+x+z==FINAL_SUM:
                        yield x,y,z
for nr in check():
    print nr