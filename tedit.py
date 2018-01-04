fr = open('data/data_lr.csv','r')
fw = open('data/lr.csv', 'a')

for line in fr:
    tokens = line.split(",")
    fw.write(str(float(tokens[0].strip())/10)+','+str(float(tokens[1].strip())/10)+'\n')

