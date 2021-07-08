import pandas as pd
dataFromWeb = pd.read_csv('input/DataFromWeb.csv',header=None,names=['colA'])
# print(dataFromWeb)
dataFromDatabase = pd.read_csv('input/DataFromDatabase.csv',header=None,names=['colA'])
# print(dataFromDatabase)
print("dataFromWeb count : ",dataFromWeb.count())
print("dataFromDatabase count : ",dataFromDatabase.count())
result = []
isInTable = False
currentData = ''
for dataWeb in dataFromWeb['colA'] : 
    for dataDB in dataFromDatabase['colA'] : 
        currentData = dataWeb
        if isInTable!=True :
            if dataWeb == dataDB :
                isInTable = True
        else :
            continue
     
    if isInTable!=True :
        print(currentData,' is not in Database')
        result.append(currentData)
    isInTable = False

resultDF = pd.DataFrame(result)   
resultDF.to_csv('output/DatabaseComparatorResult.csv', index=False,header=None)