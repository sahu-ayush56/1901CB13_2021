import os.path
def output_by_subject(dataset):
    parentdir="output_by_subject"
    if os.path.exists(parentdir)==False:
        os.mkdir(parentdir) 
    newfiletopline = ""    
    for lines in dataset:
        lineindata = ""
        sub = ""    
        lineindata = lines[0]+","+ lines[1]+","+ lines[3]+"," + lines[8]
        if lines[0] == "rollno":
            newfiletopline = lineindata
        else:
            sub = lines[3]
            checkingfile=os.path.join(parentdir,sub+".csv")
            if os.path.isfile(checkingfile) is True:
                with open(checkingfile,"a") as appending:
                    appending.write(lineindata)
            else:
                with open(checkingfile,"w") as writing:
                    writing.write(newfiletopline)
                    writing.write(lineindata)

    return

def output_individual_roll(dataset):
    parentdir="output_individual_roll"
    if os.path.exists(parentdir)==False:
        os.mkdir(parentdir) 
    newfiletopline = ""    
    for lines in dataset:
        lineindata = ""
        rollno = ""    
        lineindata = lines[0]+","+ lines[1]+","+ lines[3]+"," + lines[8]
        if lines[0] == "rollno":
            newfiletopline = lineindata
        else:
            rollno = lines[0]
            
            checkingfile=os.path.join(parentdir,rollno+".csv")
            if os.path.isfile(checkingfile) is True:
                with open(checkingfile,"a") as appending:
                    appending.write(lineindata)
            else:
                with open(checkingfile,"w") as writing:
                    writing.write(newfiletopline)
                    writing.write(lineindata)

    return

f = open("regtable_old.csv", "r")
dataset = [line.split(',') for line in f]

output_by_subject(dataset)
output_individual_roll(dataset)
