#!/usr/bin/env python3
import os

select_year = input("Please input year : ")
if select_year:select_year=int(select_year)
comd = 'ls backup/SET-100/'
res=os.popen(comd).read().split("\n")
count=1
for r in res:
    try:
        print("r-----",r)
        stock=open('%s/backup/SET-100/%s'%(os.getcwd(),r),'r').read()
        row_stocks = stock.split("\n")
        new_stock=open('%s/stockdata/%s'%(os.getcwd(),r),'w')
        for index, f in enumerate(row_stocks):
            date,open_s,high,low,close=f.split(",")
            if index==0:
                new_stock.write(f+'\n')
            else:
                if int(date[0:4]) >=select_year:
                    new_stock.write(f+'\n')
    except Exception as e:
        print("EROR ",e)
    count+=1
    new_stock.close()
