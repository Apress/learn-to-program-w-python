def calculateAverage(param1, param2, param3, param4):
    total = param1 + param2 + param3 + param4
    # Divide by a floating point value to ensure we get the proper potentially fractional answer
    average = total / 4.0   
    print 'Average value is:', average

calculateAverage(2, 3, 4, 5)
calculateAverage(-3, 5.2, 15, 1000.8)
calculateAverage(1.4, -2.5, 14.3, 200.5)
