def calculateAverage(param1, param2, param3, param4):
    total = param1 + param2 + param3 + param4
    average = total / 4.0   #floating point divide
    return average

yardsOnRun1 = 4
yardsOnRun2 = 6.5
yardsOnRun3 = 2.5
yardsOnRun4 = -2

averageYardsPerRun = calculateAverage(yardsOnRun1, yardsOnRun2, yardsOnRun3, yardsOnRun4)
print 'Averge yards per run is:', averageYardsPerRun

yardsOnPass1 = 0
yardsOnPass2 = 25.5
yardsOnPass3 = 0
yardsOnPass4 = 12

averageYardsPerPass = calculateAverage(yardsOnPass1, yardsOnPass2, yardsOnPass3, yardsOnPass4)
print 'Averge yards per pass is:', averageYardsPerPass

