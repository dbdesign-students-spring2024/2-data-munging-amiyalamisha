#import csv

# Place code below to do the munging part of this assignment.
def main():
    data = open('data/NASA_data.txt', 'r')   # open nasa data in read mode

    all_data = data.readlines()     # list of all the lines on the txt

    cleanData = open('data/clean_data.csv', 'w')
    wroteHeading = False

    # go through list of lines and write cleaned ones onto csv file
    for lines in all_data:
        if (lines[0] == "Y") and (wroteHeading == False):           # makes sure there is only 1 heading
            cleanData.write(lines)
            wroteHeading = True
        if (lines[0] == "1") or (lines[0] == "2"):
            convertedData = convertTemp(lines)
            #for value in convertedData:
            cleanData.write('  '.join(map(str, convertedData)) + '\n')
            #cleanData.write(lines)

    cleanData.close()

#Divide by 100 to get changes in degrees Celsius (deg-C).
#Multiply that result by 1.8(=9/5) to get changes in degrees Fahrenheit (deg-F).
def convertTemp(dataString):
    cleanValues = []
    # THIS WHOLE THING DOESNT WORK JUST DELETE THE DATA LOL
    values = dataString.split()

    for value in values:
        # deleting the missing values
        if (value == '***') or (value == '****'):
            value = "  "
        elif (float(value) < 1000):           # checking for years so not to delete
            cleaned = round((float(value) / 100) * 1.8, 1)
            cleanValues.append(cleaned)
        else:
            cleanValues.append(value)
    
    return cleanValues

main()