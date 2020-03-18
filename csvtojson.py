# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:13:26 2020

@author: 18moh
"""

import pandas as pd

key='virus'

c=open('key_'+key+'.csv','r',encoding='utf-8')

f=c.read()

l=[['keyword|&id|&tweet|&date|&location|&retweets|&likes']]

for i in range(len(f)-3):
    if(f[i:i+len(key)+2]==key+'|&'):
        j=i
        while(f[j+1:j+1+len(key)+2]!=key+'|&'):
            j+=1
            if(j>=len(f)):
                break
        l.append([f[i:j]])

for i in range(len(l)):
    n=l[i][0].split('|&')
    l[i]=n
    
d=pd.DataFrame(l[1:], columns=l[0])

print(d.head())

d.to_json('key_'+key+'.json',orient='records')

        
        
        
    
    

