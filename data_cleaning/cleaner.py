import csv

typeDict = {}
typeCount = 0

subTypeDict = {}
subTypeCount = 0

sourceDict = {}
sourceCount = 0

neighbourhoodDict = {}
neighbourhoodCount = 0

geoLocationDict = {}
geoLocationCount = 0

outputRowHeadings = ['month', 'date', 'hours', 'minutes', 'type', 'subType', 'source', 'neighbourhood', 'lat', 'lng']

zerolat = 0
with open("dataset_2.csv", "r") as csvfile:
    with open("dataset_2_cleaned.csv", "w") as outputFile:

        output = {}
        writer = csv.DictWriter(outputFile, fieldnames=outputRowHeadings)
        writer.writeheader()

        lines = csv.reader(csvfile)
        count = 0
        paramCount = 0
        for line in lines:
            paramCount = paramCount + len(line)
            if len(line) is not 14:
                print line

            # Date
            output['month'] = line[1][0:2]
            output['date'] = line[1][3:5]

            # Time

            splits = str(line[1]).split(" ")  # 0 is date, 1 is time, 2 optionally AM/PM
            timesplits = splits[1].split(":")
            hours = int(timesplits[0])
            output['minutes'] = int(timesplits[1])

            if len(splits) == 3 and splits[2] == 'PM':
                hours += 12

            output['hours'] = hours

            count = count + 1

            # Type
            type = -1
            if line[7] in typeDict:
                type = typeDict[line[7]]
            else:
                typeCount += 1
                typeDict[line[7]] = typeCount
                type = typeCount
            output['type'] = type

            # SubType
            subType = -1
            if line[8] in subTypeDict:
                subType = subTypeDict[line[8]]
            else:
                subTypeCount += 1
                subTypeDict[line[8]] = subTypeCount
                subType = subTypeCount
            output['subType'] = subType

            # Source
            source = -1
            if line[9] in sourceDict:
                source = sourceDict[line[9]]
            else:
                sourceCount += 1
                sourceDict[line[9]] = sourceCount
                source = sourceCount
            output['source'] = source

            # Neighbourhood
            neighbourhood = -1
            if line[11] in neighbourhoodDict:
                neighbourhood = neighbourhoodDict[line[11]]
            else:
                neighbourhoodCount += 1
                neighbourhoodDict[line[11]] = neighbourhoodCount
                neighbourhood = neighbourhoodCount
            output['neighbourhood'] = neighbourhood

            # GeoLocation
            geoSplits = str(line[13][1:-1]).split(",")

            lat = -1
            lng = -1

            if len(geoSplits) == 2:
                lat = geoSplits[0]
                lng = geoSplits[1]
            output['lat'] = lat
            output['lng'] = lng

            if lat == -1:
                zerolat += 1

            if output is not None:
                writer.writerow(output)

        print "Sample Record", line
        print count
        print paramCount

        print typeDict
        print len(typeDict)

        print subTypeDict
        print len(subTypeDict)

        print sourceDict
        print len(sourceDict)

        print neighbourhoodDict
        print len(neighbourhoodDict)

        print "---->", zerolat

        with open("type.csv", "w") as subTypeCsv:
            for row in typeDict:
                subTypeCsv.write(row + ", " + str(typeDict[row]) + "\n")
            subTypeCsv.close()

        with open("subtype.csv", "w") as subTypeCsv:
            for row in subTypeDict:
                subTypeCsv.write(row + ", " + str(subTypeDict[row]) + "\n")
            subTypeCsv.close()

        with open("source.csv", "w") as sourceCsv:
            for row in sourceDict:
                sourceCsv.write(row + ", " + str(sourceDict[row]) + "\n")
            subTypeCsv.close()

        with open("neighbourhood.csv", "w") as neighbourhoodCsv:
            for row in neighbourhoodDict:
                neighbourhoodCsv.write(row + ", " + str(neighbourhoodDict[row]) + "\n")
            neighbourhoodCsv.close()

    outputFile.close()
csvfile.close()