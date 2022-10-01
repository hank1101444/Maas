from cmath import nan
from itertools import count
from time import strptime
import pandas as pd
from datetime import datetime

# dateformat='%Y-%m-%d  %H:%M:%S.%f'

# df = pd.read_csv("yoxi_2021H1.csv")

# time_range=[[0,8],[8,12],[12,16],[16,24]]
# ReadData=[{}]*len(time_range)
# r,c=df.shape
# for row in range(1,r):
#     strtime=df.at[row,"yoxi_3"]
#     if(strtime=="0") : continue
#     timeObj=strptime(strtime,dateformat)
#     hour = timeObj.tm_hour
#     LocationsList=str(df.at[row,"yoxi_5"][7:-1]).split(' ')
#     PricesList=str(df.at[row,"yoxi_15"]).split('-')

#     if(PricesList[0] == "0" or PricesList[0] =="nan"): continue
#     if(PricesList[1]=="" and PricesList[0]=="500") :
#         PricesList[0]="501"
#         PricesList[1]="48763"
   
#     locations=(float(LocationsList[0]),float(LocationsList[1]))
#     prices=(int(PricesList[0]),int(PricesList[1]))

#     for i in range(0,len(ReadData)):
#         if( time_range[i][0] <= hour< time_range[i][1]):
#             ReadData[i][locations]=prices
#             break

Simpleinput1=[
{(121.618130,25.054810):(1,100)
,(121.618158,25.054836):(101,150)
,(121.618140,25.054820):(151,200)
,(121.618135,25.054817):(201,250)
,(121.618180,25.054840):(251,300)
,(121.618170,25.054838):(301,400)
,(121.618165,25.054750):(401,500)
,(121.618012,25.054700):(501,48763)},

{(121.618130,25.054810):(1,100)
,(121.618158,25.054836):(101,150)
,(121.618140,25.054820):(151,200)
,(121.618135,25.054817):(201,250)
,(121.618180,25.054840):(251,300)
,(121.618170,25.054838):(301,400)
,(121.618165,25.054750):(401,500)
,(121.618012,25.054700):(501,48763)},

{(121.618130,25.054810):(1,100)
,(121.618158,25.054836):(101,150)
,(121.618140,25.054820):(151,200)
,(121.618135,25.054817):(201,250)
,(121.618180,25.054840):(251,300)
,(121.618170,25.054838):(301,400)
,(121.618165,25.054750):(401,500)
,(121.618012,25.054700):(501,48763)},

{(121.618130,25.054810):(1,100)
,(121.618158,25.054836):(101,150)
,(121.618140,25.054820):(151,200)
,(121.618135,25.054817):(201,250)
,(121.618180,25.054840):(251,300)
,(121.618170,25.054838):(301,400)
,(121.618165,25.054750):(401,500)
,(121.618012,25.054700):(501,48763)}]

