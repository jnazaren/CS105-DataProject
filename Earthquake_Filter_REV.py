#CS105 Project Program to Transform Data From Large Database
#The program opens a downloaded file of the database (SignificantEarthquakes_rev.csv) and uses this to create our dataset.
#From this file, individual files in which our input variables are paired with our output variables are created.

import csv

outfile=open("Earthquakes_data_formatted.csv", "w")
outfile2=open("Focal Depth & Total Deaths.csv", "w")
outfile3=open("Magnitude & Total Deaths.csv", "w")
outfile4=open("Focal Depth & Total Damage.csv", "w")
outfile5=open("Magnitude & Total Damage.csv", "w")


#Creating the full "relational table" with all selected attributes

with open("SignificantEarthquakes_rev.csv", "r") as f:
    header = ("Year", "Focal Depth", "Magnitude", "Total Deaths", "Total Damage in Millions", "Latitude", "Longitude", "Total Damage Description", "Total Deaths Description")
    print(','.join(header), file=outfile)
    next(f)
    for line in f:
        line = line[:-1]
        variables = line.split(',')
        variables_used = variables[2], variables[8], variables[9], variables[-12], variables[-6], variables[19], variables[20], variables[-5], variables[-11]
        transformed = ','.join(variables_used)

        if variables[-12] == "" or variables[-6] == "":
            continue
        if variables[19] == "" or variables[20] == "":
            continue
        if variables[-11] == "" or variables[-7] == "":
            continue
        elif int(variables[2]) > 1960:
            print(transformed, file=outfile)

#Pairing Focal Depth and Magnitude with Total Deaths
            
with open("SignificantEarthquakes_rev.csv", "r") as f:
    print("Focal Depth", ',', "Total Deaths", file=outfile2)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_f_td = (variables[8], variables[-12])
        transformed = ','.join(variables_f_td)
        
        if variables[8] == "":
            continue
        if variables[-12] == "":
            continue
        else:
            print(transformed, file=outfile2)
            
with open("SignificantEarthquakes.csv", "r") as f:
    print("Magnitude", ',', "Total Deaths", file=outfile3)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_m_td = (variables[9], variables[-12])
        transformed = ','.join(variables_m_td)
        
        if variables[9] == "":
            continue
        if variables[-12] == "":
            continue
        else:
            print(transformed, file=outfile3)

#Pairing Focal Depth and Magnitude with Total Damage
            
with open("SignificantEarthquakes.csv", "r") as f:
    print("Focal Depth", ',', "Total Damage", file=outfile4)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_f_dam = (variables[8], variables[-6])
        transformed = ','.join(variables_f_dam)
        
        if variables[8] == "":
            continue
        if variables[-6] == "":
            continue
        else:
            print(transformed, file=outfile4) 


with open("SignificantEarthquakes.csv", "r") as f:
    print("Magnitude", ',', "Total Damage", file=outfile5)
    next(f)
    for line in f:
        line=line[:-1]
        variables = line.split(',')
        variables_m_dam = (variables[9], variables[-6])
        transformed = ','.join(variables_m_dam)
        
        if variables[9] == "":
            continue
        if variables[-6] == "":
            continue
        else:
            print(transformed, file=outfile5)

outfile.close()
outfile2.close()
outfile3.close()
outfile4.close()
outfile5.close()
f.close()
