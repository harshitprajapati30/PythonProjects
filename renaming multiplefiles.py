import os
os.chdir('E:\Test')
list = os.listdir('E:\Test')
print(list)
i=7
for file in os.listdir():
    src = file
    dst = 'Screenshot' + str(i) + '.png'
    os.rename(src, dst)
    i += 1
    print(i)
print("Done")