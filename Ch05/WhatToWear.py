# What to wear

def whatToWear(temperature):
    if temperature > 90:
        clothes = 'swim suit'
    elif temperature > 70:	
        clothes = 'shorts'
    elif temperature > 50:
        clothes = 'long pants'
    else:
        clothes = 'thermal underwear and long pants'

    return 'Put on ' + clothes

print whatToWear(100)
print whatToWear(40)
print whatToWear(71)

