TAX_RATE = .09  # 9 percent tax
COST_PER_SMALL_WIDGET = 5.00
COST_PER_LARGE_WIDGET = 8.00

def calculateCost(nSmallWidgets, nLargeWidgets):
    subTotal = (nSmallWidgets * COST_PER_SMALL_WIDGET) + (nLargeWidgets * COST_PER_LARGE_WIDGET)
    taxAmount = subTotal * TAX_RATE
    totalCost = subTotal + taxAmount
    return totalCost

total1 = calculateCost(4, 3)
print taxAmount
print 'Total for first order is', total1
total2 = calculateCost(12, 15)
print 'Total for second order is', total2
