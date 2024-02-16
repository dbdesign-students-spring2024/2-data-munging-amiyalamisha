# Place code below to do the munging part of this assignment.
def main():
    data = open('data/NASA_data.txt', 'r')   # open nasa data in read mode

    all_data = data.readlines()     # list of all the lines on the txt

    cleanData = open('data/clean_data.csv', 'w')
    wroteHeading = False

    # go through list of lines and write cleaned ones onto csv file
    for lines in all_data:
        if (lines[0] == "Y") and (wroteHeading == False):           # makes sure there is only 1 heading
            cleanData.write(','.join(lines.split()))
            wroteHeading = True
        if (lines[0] == "1") or (lines[0] == "2"):
            convertedData = convertTemp(lines)
            # iterates through converted data string and adds spaces in between
            cleanData.write('\n' + ','.join(map(str, convertedData)))

    cleanData.close()

#Divide by 100 to get changes in degrees Celsius (deg-C).
#Multiply that result by 1.8(=9/5) to get changes in degrees Fahrenheit (deg-F).
def convertTemp(dataString):
    cleanValues = []
    values = dataString.split()

    for value in values:
        # deleting the missing values
        if (value == '***') or (value == '****'):
            #value = "  "
            #print(missingValues(values, value))
            cleaned = format(missingValues(values, value), ".1f")
            cleanValues.append(cleaned)
        elif (float(value) < 1000):           # checking for years so not to delete
            cleaned = format((float(value) / 100) * 1.8, ".1f")
            cleanValues.append(cleaned)
        else:
            cleanValues.append(value)
    
    return cleanValues

def missingValues(line, val):
    firstAvg = 0
    sum = 0
    valueList = line
    valueList.reverse()
    
    count = 0
    for v in valueList:
        if(count > 0):
            # for --> val == '****'
            sum += float(v)
            if (count > 3):
                firstAvg = sum / 3
        
        if (val == '****'):
            return firstAvg
        elif (val == '***'):
            secondAvg = (firstAvg + sum) / 4
            return secondAvg

        count += 1
        


main()