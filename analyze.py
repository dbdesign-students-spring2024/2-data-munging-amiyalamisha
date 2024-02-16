import csv

def main():
    #cleanData = open('data/clean_data.csv', 'r')
    with open('data/clean_data.csv', mode='r') as cleanData:
        csvReader = csv.DictReader(cleanData)
        
        print("Temperature anomaly averages for the decades: ")

        for row in csvReader:
            if (int(row["Year"]) % 10 == 0): 
                print(decade(row, int(row["Year"]), csvReader))

def decade(dataLine, year, csvRead):
    decadeAvg = dataLine
    
    count = 0
    for row2 in csvRead:
        if (int(row2["Year"]) > year):
            decadeAvg["Jan"] = float(decadeAvg["Jan"]) + float(row2["Jan"])
            decadeAvg["Feb"] = float(decadeAvg["Feb"]) + float(row2["Feb"])
            decadeAvg["Mar"] = float(decadeAvg["Mar"]) + float(row2["Mar"])
            decadeAvg["Apr"] = float(decadeAvg["Apr"]) + float(row2["Apr"])
            decadeAvg["May"] = float(decadeAvg["May"]) + float(row2["May"])
            decadeAvg["Jun"] = float(decadeAvg["Jun"]) + float(row2["Jun"])
            decadeAvg["Jul"] = float(decadeAvg["Jul"]) + float(row2["Jul"])
            decadeAvg["Aug"] = float(decadeAvg["Aug"]) + float(row2["Aug"])
            decadeAvg["Sep"] = float(decadeAvg["Sep"]) + float(row2["Sep"])
            decadeAvg["Oct"] = float(decadeAvg["Oct"]) + float(row2["Oct"])
            decadeAvg["Nov"] = float(decadeAvg["Nov"]) + float(row2["Nov"])
            decadeAvg["Dec"] = float(decadeAvg["Dec"]) + float(row2["Dec"])

            decadeAvg["J-D"] = float(decadeAvg["J-D"]) + float(row2["J-D"])
            decadeAvg["D-N"] = float(decadeAvg["D-N"]) + float(row2["D-N"])
            decadeAvg["DJF"] = float(decadeAvg["DJF"]) + float(row2["DJF"])
            decadeAvg["MAM"] = float(decadeAvg["MAM"]) + float(row2["MAM"])
            decadeAvg["JJA"] = float(decadeAvg["JJA"]) + float(row2["JJA"])
            decadeAvg["SON"] = float(decadeAvg["SON"]) + float(row2["SON"])
            
            # loops 7 times bc i already went through a couple lines of data before this loop
            if (count > 7): 
                decadeAvg["Jan"] /= 10
                decadeAvg["Feb"] /= 10
                decadeAvg["Mar"] /= 10
                decadeAvg["Apr"] /= 10
                decadeAvg["May"] /= 10
                decadeAvg["Jun"] /= 10
                decadeAvg["Jul"] /= 10
                decadeAvg["Aug"] /= 10
                decadeAvg["Sep"] /= 10
                decadeAvg["Oct"] /= 10
                decadeAvg["Nov"] /= 10
                decadeAvg["Dec"] /= 10

                decadeAvg["J-D"] /= 10
                decadeAvg["D-N"] /= 10
                decadeAvg["DJF"] /= 10
                decadeAvg["MAM"] /= 10
                decadeAvg["JJA"] /= 10
                decadeAvg["SON"] /= 10
                
                for avg in decadeAvg:
                    if (float(decadeAvg[avg]) < 1000):
                        decadeAvg[avg] = format(float(decadeAvg[avg]), ".1f")
                return decadeAvg
            count += 1


main()