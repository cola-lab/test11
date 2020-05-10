# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:21:49 2020

@author: 89437
"""

import pickle
import datetime
import numpy as np
import pandas as pd
file_GSD = open(r'dic_Vis_GSD.pkl','rb')
content  = pickle.load(file_GSD)

year = 2018
begin = datetime.datetime(year,1,1,0,0)
end = datetime.datetime(year,12,31,23,59)
d = begin
delta = datetime.timedelta(hours=1)

Ttt = []
while d <= end:
    #print(d.strftime("%Y-%m-%d %H:%M"))
    Ttt.append(d)
    d += delta

times = list(content.keys())
value_gsd = list(content.values())

x = len(Ttt)

values = np.full(len(Ttt),np.nan)
worker_vis = zip(Ttt,values)
dic_vis = dict(worker_vis)

for i in range(len(times)):
    dic_vis[times[i]] = content[times[i]]

def fill_nan(dic,Ttt):
    value_list = list(dic.values())
    for i in range(len(Ttt)):
        if pd.isnull(value_list[i]):
            num = i+1
            while pd.isnull(value_list[num]):
                num = num + 1
            fp = [value_list[i-1],value_list[num]]
            xp = [1,num-i+2]
            value_list[i] = np.interp(2,xp,fp)
            dic[Ttt[i]] = value_list[i]
            #print('pre:',value_list[i],dic[Ttt[i]])

fill_nan(dic_vis,Ttt)

#test
#test111