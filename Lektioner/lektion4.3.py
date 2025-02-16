import random
with open('slumptal.txt','w',encoding='utf-8') as mathFile:
    for fileRun in range(10):
        slump_tal = random.randint(1,50)
        mathFile.write(str(slump_tal)+'\n')