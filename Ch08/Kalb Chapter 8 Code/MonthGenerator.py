# Given a month number, find the three letter abbreviation for that month

months = 'JanFebMarAprMayJunJulAugSepOctNovDec'

monthNumber = raw_input('Enter a month number (1-12): ')
monthNumber = int(monthNumber)

startIndex = (monthNumber - 1) * 3
endIndex = startIndex + 3

# Generate the appropriate slice
monthAbbrev = months[startIndex :  endIndex]
print monthAbbrev
