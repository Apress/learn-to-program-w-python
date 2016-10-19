# Examples of  a list of dicts, and of a dict of lists


carsList = [\
    {'make':'Toyota', 'model':'Prius', 'year': 2006, 'color':'gold', 'doors':4, 'leather':False, 'license': 'ABC123', 'mileage': 777777},\
    {'make':'Honda', 'model':'Civic', 'year': 2010, 'color':'red', 'doors':2, 'leather':False, 'license': 'DEF444', 'mileage': 54321},\
    {'make':'Ford', 'model':'Fusion', 'year': 2012, 'color':'blue', 'doors':4, 'leather':True, 'license': 'GHI999', 'mileage': 24680},\
    {'make':'Chevy', 'model':'Volt', 'year': 2015, 'color':'black', 'doors':4, 'leather':False, 'license': 'JKL444', 'mileage': 7890}\
    ]


for carDict in carsList:
    if (carDict['doors'] == 4) and (carDict['mileage'] < 50000):
        print carDict['make'], carDict['model'], carDict['license']

    

personalDataDict = {
    'Joe': {'height':73, 'weight': 200, 'sex':'M', 'age':35, 'allergies':['tree pollen', 'carrots', 'onions']},\
    'Sally':{'height':58, 'weight': 100, 'sex':'F', 'age':32, 'allergies':['bee stings']},\
    'John': {'height':36, 'weight': 75, 'sex':'M', 'age':8, 'allergies':['peanuts']},\
    'Mary': {'height':35, 'weight': 60, 'sex':'F', 'age':7, 'allergies':[]}\
    }



joesData = personalDataDict['Joe']
joesAllergies = joesData['allergies']
print joesAllergies

marysData = personalDataDict['Mary']
marysAllergies = marysData['allergies']
print marysAllergies


for personName in personalDataDict:
    onePersonDict = personalDataDict[personName]
    allergyList = onePersonDict['allergies']
    if allergyList == []:
        print personName, 'is not allergic to anything'
    else:
        print personName, 'is allergic to the following:'
        for allergy in allergyList:
            print '    ', allergy
    
