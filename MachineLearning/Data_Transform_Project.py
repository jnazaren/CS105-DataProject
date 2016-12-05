#CS105 Project Program to Transform Data
import csv

outfile = open("Earthquakes_data_formatted.csv", "w")
outfile2=open("Hour & Total Deaths.csv", "w")
outfile3=open("Focal Depth & Total Deaths.csv", "w")
outfile4=open("Magnitude & Total Deaths.csv", "w")
outfile5=open("Hour & Total Damage.csv", "w")
outfile6=open("Focal Depth & Total Damage.csv", "w")
outfile7=open("Magnitude & Total Damage.csv", "w")
outfile8=open("Hour, Focal Depth, & Total Deaths.csv", "w")
outfile9=open("Hour, Focal Depth, & Total Damage.csv", "w")
outfile10=open("Hour, Magnitude, & Total Deaths.csv", "w")
outfile11=open("Hour, Magnitude, & Total Damage.csv", "w")
outfile12=open("Focal Depth, Magnitude, & Total Deaths.csv", "w")
outfile13=open("Focal Depth, Magnitude, & Total Damage.csv", "w")

#Pairing each variable with Total Deaths
with open("SignificantEarthquakes.csv", "r") as f:
    header = ("Year", "Hour", "Focal Depth", "Magnitude", "Total Deaths", "Total Damage in Millions")
    print(','.join(header), file=outfile)
    next(f)
    for line in f:
        line = line[:-1]
        variables = line.split(',')
        variables_used = variables[2], variables[5], variables[8], variables[9], variables[35], variables[41]
        transformed = ','.join(variables_used)

        if variables[35] == "" or variables[41] == "":
            continue
        elif int(variables[2]) > 1960:
            print(transformed, file=outfile)
            
with open("SignificantEarthquakes.csv", "r") as f:
    print("Hour", ',', "Total Deaths", file=outfile2)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_5_35 = (variables[5], variables[35])
        transformed = ','.join(variables_5_35)
        
        if variables[35] == "":
            continue
        if variables[5] == "":
            continue
        else:
            if int(variables[2]) > 1960:
                print(transformed, file=outfile2)


with open("SignificantEarthquakes.csv", "r") as f:
    print("Focal Depth", ',', "Total Deaths", file=outfile3)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_8_35 = (variables[8], variables[35])
        transformed = ','.join(variables_8_35)
        
        if variables[35] == "":
            continue
        if variables[8] == "":
            continue
        elif int(variables[2]) > 1960:
            print(transformed, file=outfile3)
            
with open("SignificantEarthquakes.csv", "r") as f:
    print("Magnitude", ',', "Total Deaths", file=outfile4)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_9_35 = (variables[9], variables[35])
        transformed = ','.join(variables_9_35)
        
        if variables[9] == "":
            continue
        if variables[35] == "":
            continue
        elif int(variables[2]) > 1960:
            print(transformed, file=outfile4)

#Pairing Variables with Total Damage

with open("SignificantEarthquakes.csv", "r") as f:
    print("Hour", ',', "Total Damage", file=outfile5)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_5_41 = (variables[5], variables[41])
        transformed = ','.join(variables_5_41)
        
        if variables[5] == "":
            continue
        if variables[41] == "":
            continue
        elif int(variables[2]) > 1960:
            print(transformed, file=outfile5)

with open("SignificantEarthquakes.csv", "r") as f:
    print("Hour", ',', "Total Damage", file=outfile6)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_6_41 = (variables[6], variables[41])
        transformed = ','.join(variables_6_41)
        
        if variables[5] == "":
            continue
        if variables[41] == "":
            continue
        elif int(variables[2]) > 1960:
            print(transformed, file=outfile5)


with open("SignificantEarthquakes.csv", "r") as f:
    print("Focal Depth", ',', "Total Damage", file=outfile6)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_8_41 = (variables[8], variables[41])
        transformed = ','.join(variables_8_41)
        
        if variables[8] == "":
            continue
        if variables[41] == "":
            continue
        elif int(variables[2]) > 1960:
            print(transformed, file=outfile6) 


with open("SignificantEarthquakes.csv", "r") as f:
    print("Magnitude", ',', "Total Damage", file=outfile6)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_9_41 = (variables[9], variables[41])
        transformed = ','.join(variables_9_41)
        
        if variables[9] == "":
            continue
        if variables[41] == "":
            continue
        elif int(variables[2]) > 1960:
            print(transformed, file=outfile7) 

#Creating two input variables

with open("SignificantEarthquakes.csv", "r") as f:
    print("Hour", ',', "Focal Depth", "," "Total Deaths", file=outfile8)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_5_8_35 = (variables[5], variables[8], variables[35])
        transformed = ','.join(variables_5_8_35)
        
        if variables[5] == "":
            continue
        if variables[8] == "":
            continue
        if variables[35] == "":
            continue
        elif int(variables[2]) > 1960:
            print(transformed, file=outfile8)

with open("SignificantEarthquakes.csv", "r") as f:
    print("Hour", ',', "Focal Depth", "," "Total Damage", file=outfile9)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_5_8_41 = (variables[5], variables[8], variables[41])
        transformed = ','.join(variables_5_8_41)
        
        if variables[5] == "":
            continue
        if variables[8] == "":
            continue
        if variables[41] == "":
            continue
        elif int(variables[2]) > 1960:
            print(transformed, file=outfile9)

with open("SignificantEarthquakes.csv", "r") as f:
    print("Hour", ',', "Magnitdue", "," "Total Deaths", file=outfile10)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_5_9_35 = (variables[9], variables[35])
        transformed = ','.join(variables_5_9_35)
        
        if variables[5] == "":
            continue
        if variables[9] == "":
            continue
        if variables[35] == "":
            continue
        elif int(variables[2]) > 1960:
            print(transformed, file=outfile10)

with open("SignificantEarthquakes.csv", "r") as f:
    print("Hour", ',', "Magnitude", "," "Total Damage", file=outfile11)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_5_9_41 = (variables[5], variables[9], variables[41])
        transformed = ','.join(variables_5_9_41)
        
        if variables[5] == "":
            continue
        if variables[9] == "":
            continue
        if variables[41] == "":
            continue
        elif int(variables[2]) > 1960:
            print(transformed, file=outfile11)

with open("SignificantEarthquakes.csv", "r") as f:
    print("Focal Depth", ',', "Magnitdue", "," "Total Deaths", file=outfile12)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_8_9_35 = (variables[8], variables[9], variables[35])
        transformed = ','.join(variables_8_9_35)
        
        if variables[8] == "":
            continue
        if variables[9] == "":
            continue
        if variables[35] == "":
            continue
        elif int(variables[2]) > 1960:
            print(transformed, file=outfile12)
               
with open("SignificantEarthquakes.csv", "r") as f:
    print("Focal Depth", ',', "Magnitdue", "," "Total Damage", file=outfile13)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_8_9_41 = (variables[8], variables[9], variables[41])
        transformed = ','.join(variables_8_9_41)
        
        if variables[8] == "":
            continue
        if variables[9] == "":
            continue
        if variables[41] == "":
            continue
        elif int(variables[2]) > 1960:
            print(transformed, file=outfile13)

outfile.close()
outfile2.close()
outfile3.close()
outfile4.close()
outfile5.close()
outfile6.close()
outfile7.close()
outfile8.close()
outfile9.close()
outfile10.close()
outfile11.close()
outfile12.close()
outfile13.close()              
f.close()
