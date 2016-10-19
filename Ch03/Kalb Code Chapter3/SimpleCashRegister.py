# -*- coding: utf-8 -*-
# Simple cash register

cost = raw_input('Please enter the cost of the item: ')
cost = float(cost)
cash = raw_input('Please enter the cash given: ')
cash = float(cash)
change = cash - cost
print 'Your item costs', cost, 'and you gave me', cash, 'dollars. Your change is', change
