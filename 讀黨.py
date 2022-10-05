from cmath import nan
from time import strptime
from cv2 import imread, waitKey
import pandas as pd
from datetime import datetime
import cv2
dateformat='%Y-%m-%d  %H:%M:%S.%f'

df = pd.read_csv("yoxi_2021H1.csv")
PriceRangeToID={(1,100):0,(101,150):1,(151,200):2,(201,250):3,(251,300):4,(301,400):5,(401,500):6,(501,48763):7}
TimeRange=[] #<- 想要改成更多段在這裡改即可 如 [[0,4],[4,8],[8,12],[12,16],[16,24]]
temp=0
for i in range(0,12):
    TimeRange.append([temp,temp+2])
    temp+=2

ReadData=[]
for i in TimeRange:
    ReadData.append({})
r,c=df.shape
for row in range(1,r):
    strtime=df.at[row,"yoxi_3"]
    if(strtime=="0") : continue
    timeObj=strptime(strtime,dateformat)
    hour = timeObj.tm_hour
    LocationsList=str(df.at[row,"yoxi_5"][7:-1]).split(' ')
    PricesList=str(df.at[row,"yoxi_15"]).split('-')

    if(PricesList[0] == "0" or PricesList[0] =="nan"): continue
    if(PricesList[1]=="" and PricesList[0]=="500") :
        PricesList[0]="501"
        PricesList[1]="48763"
   
    locations=(float(LocationsList[0]),float(LocationsList[1]))
    prices=PriceRangeToID[int(PricesList[0]),int(PricesList[1])]

    for i in range(0,len(ReadData)):
        if( TimeRange[i][0] <= hour< TimeRange[i][1]):
            ReadData[i][locations]=prices
            break
path="data"
ID=0
for dic in ReadData:
    f = open(f"data{ID}.txt", 'w')
    for key in dic:
        f.write(f"{key[0]},{key[1]},{dic[key]}\n")
    ID+=1
    f.close






Simpleinput1=[
{(121.618130,25.054810):0
,(121.618158,25.054836):1
,(121.618140,25.054820):2
,(121.618135,25.054817):3
,(121.618180,25.054840):4
,(121.618170,25.054838):5
,(121.618165,25.054750):6
,(121.618012,25.054700):7},

{(121.618130,25.054810):0
,(121.618158,25.054836):1
,(121.618140,25.054820):2
,(121.618135,25.054817):3
,(121.618180,25.054840):4
,(121.618170,25.054838):5
,(121.618165,25.054750):6
,(121.618012,25.054700):7},

{(121.618130,25.054810):0
,(121.618158,25.054836):1
,(121.618140,25.054820):2
,(121.618135,25.054817):3
,(121.618180,25.054840):4
,(121.618170,25.054838):5
,(121.618165,25.054750):6
,(121.618012,25.054700):7},

{(121.618130,25.054810):0
,(121.618158,25.054836):1
,(121.618140,25.054820):2
,(121.618135,25.054817):3
,(121.618180,25.054840):4
,(121.618170,25.054838):5
,(121.618165,25.054750):6
,(121.618012,25.054700):7}]

