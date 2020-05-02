errors = []
linenum = 0
substr = "TCPNEENAHFM"

with open('c:\\temp\ApptOutreach_20190813.txt', 'rt') as myfile:
    for line in myfile:
        linenum +=1
        if line.find(substr)  != -1:
            errors.append("Line " + str(linenum) + ": " + line.rstrip('\n'))

for err in errors:
    print(err)


myfile = open('c:\\temp\ApptOutreach_new.txt', 'w')
for line in errors:

    myfile.writelines(line+'\n')

myfile.close()




