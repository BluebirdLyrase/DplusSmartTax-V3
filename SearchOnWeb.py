from PIL import Image
import os
import time
import pyautogui
import pandas as pd
from datetime import datetime
resultFound = []
resultNotFound = []
# print(Search)

# prep dir
dataFromDatabase = pd.read_csv('input/SearchOnWebData.csv',header=None,names=['colA'])
index = 1
dt_stringDir = datetime.now().strftime("%d-%m-%Y%H%M%S")
ScreenshotDir = 'screenshot/'+dt_stringDir
outputDir = 'output/'+dt_stringDir
ssFoundDir = ScreenshotDir+'/found'
ssNotFoundDir = ScreenshotDir+'/notfound'
os.mkdir(ScreenshotDir)
os.mkdir(ssFoundDir)
os.mkdir(ssNotFoundDir)
os.mkdir(outputDir)

for dataDB in dataFromDatabase['colA'] : 
    Search = pyautogui.locateOnScreen('input/Search.png', confidence=0.9)
    while Search is None :
        print('cannot find search button')
        time.sleep(1)
        Search = pyautogui.locateOnScreen('input/Search.png', confidence=0.9)
    lenght = dataFromDatabase['colA'].count()
    msg = 'progress ' + str(index) + '/'+ str(lenght)

    # write data
    pyautogui.moveTo(Search[0], Search[1]-50)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(dataDB)

    # search press
    pyautogui.moveTo(Search[0], Search[1])
    pyautogui.click()

    # waiting for website
    PreNoData = pyautogui.locateOnScreen('input/NoData.png', confidence=0.9)
    refButton = pyautogui.locateOnScreen('input/refButton.png', confidence=0.9)
    while refButton is None and PreNoData is None:
        print('waiting for website')
        time.sleep(0.01)
        PreNoData = pyautogui.locateOnScreen('input/NoData.png', confidence=0.9)
        refButton = pyautogui.locateOnScreen('input/refButton.png', confidence=0.9)
        # print(PreNoData)
        # print(refButton)

    # image process and write Data
    index = index + 1
    NoData = pyautogui.locateOnScreen('input/NoData.png', confidence=0.9)
    if NoData is None :
        resultFound.append(dataDB)
        print(dataDB,' is found ',msg)
        ss = pyautogui.screenshot(ssFoundDir+'/'+dataDB+'.png')
    else :
        print(dataDB,' is not found ',msg)
        resultNotFound.append(dataDB)
        ss = pyautogui.screenshot(ssNotFoundDir+'/'+dataDB+'.png')

resultFoundDF = pd.DataFrame(resultFound)
resultNotFoundDF = pd.DataFrame(resultNotFound)    

dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print('finished at ',dt_string)

resultFoundDF.to_csv(outputDir+'/Found'+dt_stringDir+'.csv', index=False,header=None)
resultNotFoundDF.to_csv(outputDir+'/NotFound'+dt_stringDir+'.csv', index=False,header=None)
print('All Data : ',dataFromDatabase['colA'].count())
print('Data found : ',resultFoundDF.count())
print('Data not found :',resultNotFoundDF.count())