# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 14:12:00 2022

@author: aleks
"""
#TODO
#1) Logistic regression for shot in the end probability
#2) Implement xG
#3) OLS xG~coordinates.

#chain - either one team two contacts or ball out of play 
#importing necessary libraries 
import pandas as pd
import numpy as np
import json
# plotting
import matplotlib.pyplot as plt
#opening data
import os
import pathlib
import warnings 
#used for plots
from mplsoccer import Pitch
from scipy.stats import binned_statistic_2d

pd.options.mode.chained_assignment = None
warnings.filterwarnings('ignore')

df = pd.DataFrame()
for i in range(13):
    file_name = 'events_England_' + str(i+1) + '.json'
    path = os.path.join(str(pathlib.Path().resolve().parents[0]), 'data', 'Wyscout', file_name)
    with open(path) as f:
        data = json.load(f)
    df = pd.concat([df, pd.DataFrame(data)])

see = df.iloc[:1000]

#probably need to drop "others on the ball event" - nope



#potential +0s
# foul by another team
# won duel by the same team
# pass by the same team
# lost duel by the other team

#potential +1s
# other team wins duel/neutral duel
# inaccurate pass
# pass by the other team 

# potential +2s
# ball out of the field - unsuccessful pass with one of the coordinates 
# shot 
# faul by the same team as over possesion chain

#if inaccurate pass + pass by other team -> start counting possesion by the pass by other team. 
#chain = 0, sprawdzamy wszystkie warunki eventu - ify, jeli którys spelnia to dodajemy k=k+1
# najpierw dochodzi do dwóch, dodajemy +1 do chaina, df.at[i, chain] = chain
next_actions = see.shift(-1, fill_value=0)
