#!/usr/bin/python
#coding:UTF-8
import requests, json
from datetime import datetime,timedelta
import csv
import sys
import pandas as pd
from matplotlib import pyplot
import time
import numpy as np
from datetime import datetime as dt

def kddiapi():
    now=datetime.now()
    before=now+timedelta(minutes=-20)
    url = "http://logger.m2m-cloud-std.kddi.ne.jp/v1.0/data/regular"
    method = "POST"
    obj = {
        "terminals" :
           [ {
        "terminal_id" : "410",
        "no" : [2,3,4,5,6,7,8,9,14]
            }],
       "from" : "{0:%Y%m%d%H%M%S}".format(before),
        "to" : "{0:%Y%m%d%H%M%S}".format(now)
    }
    json_data = json.dumps(obj).encode("utf-8")
    headers = {"Host":"logger.m2m-cloud-std.kddi.ne.jp",
              "Authorization":"Bearer W2DEAhjNvxlvwVlM-sIYmsyHYsfrCHgPi" ,
    "Content-Type" : "application/json",
    "Accept":"text/csv"}

    r = requests.post(url=url, data=json_data, headers=headers)
    f=open('kddidata.txt','w')
    f.write(r.text)
    f.close()


def transcsv():
    df= pd.read_csv('kddidata.txt')
    df.to_csv("kddidata.csv")


def tojson():
    df =pd.read_csv('kddidata.csv',header=None,skiprows=1)
    data=[]
    time=[]
    time_i=[]
    humidity=[]
    temperature=[]
    brightness=[]
    ultraviolet=[]
    atmopressure=[]
    volume=[]
    discomfort=[]
    heatstrokerisk=[]
    co2=[]
    for i in range(len(df)):
        data.append('value')
        time.append(df.iloc[i,3])
        humidity.append(df.iloc[i,4])
        temperature.append(df.iloc[i,5])
        brightness.append(df.iloc[i,6])
        ultraviolet.append(df.iloc[i,7])
        atmopressure.append(df.iloc[i,8])
        volume.append(df.iloc[i,9])
        discomfort.append(df.iloc[i,10])
        heatstrokerisk.append(df.iloc[i,11])
        co2.append(df.iloc[i,12])

    # df2 = pd.DataFrame({'time':time,'humidity': humidity, 'temperature':temperature,'brightness':brightness,'ultraviolet':ultraviolet,'atmopressure':atmopressure,'volume':volume,'discomfort':discomfort,'heatstrokerisk':heatstrokerisk,'co2':co2},index=data)
    # print(df2)
    # path='./tojson.json'
    # df2.to_json(path,orient='records')
    
    for i in(reversed(co2)):
        if i == i:
            nowco2=i
            break

    for i in range(len(df))[::-1]:
        if temperature[i]==temperature[i]:
            nownum=i
            break
        
    nowtime=time[nownum]
    nowhumidity=humidity[nownum]
    nowtemperature=temperature[nownum]
    nowbrightness=brightness[nownum]
    nowultraviolet=ultraviolet[nownum]
    nowatmopressure=atmopressure[nownum]
    nowvolume=volume[nownum]
    nowdiscomfort=discomfort[nownum]
    nowheatstrokerisk=heatstrokerisk[nownum]
    nowco=nowco2

    #date draw
    for i in time:
        time_i.append(dt.strptime(i,'%Y/%m/%d %H:%M:%S'))

    time_j=[]
    for i in time_i:
        time_j.append('{}:{}'.format(i.hour,i.minute))
    


    def make_patch_spines_invisible(ax):
        ax.set_frame_on(True)
        ax.patch.set_visible(False)
        for sp in ax.spines.values():
            sp.set_visible(False)

    fig,host=pyplot.subplots(figsize=(20,10))
    fig.subplots_adjust(right=0.5)
    par1=host.twinx()
    par2=host.twinx()
    par3=host.twinx()
    par4=host.twinx()
    par5=host.twinx()
    par6=host.twinx()
    par7=host.twinx()
    par8=host.twinx()

    # Offset the right spine of par2.  The ticks and label have already been
    # placed on the right by twinx above.
    par2.spines["right"].set_position(("axes", 1.1))
    make_patch_spines_invisible(par2)
    par2.spines["right"].set_visible(True)
    #
    par3.spines["right"].set_position(("axes", 1.2))
    make_patch_spines_invisible(par3)
    par3.spines["right"].set_visible(True)
    #
    par4.spines["right"].set_position(("axes", 1.3))
    make_patch_spines_invisible(par4)
    par4.spines["right"].set_visible(True)
    #
    par5.spines["right"].set_position(("axes", 1.5))
    make_patch_spines_invisible(par5)
    par5.spines["right"].set_visible(True)
    #
    par6.spines["right"].set_position(("axes", 1.7))
    make_patch_spines_invisible(par6)
    par6.spines["right"].set_visible(True)
    #
    par7.spines["right"].set_position(("axes", 1.9))
    make_patch_spines_invisible(par7)
    par7.spines["right"].set_visible(True)
    #
    par8.spines["right"].set_position(("axes",2))
    make_patch_spines_invisible(par8)
    par8.spines["right"].set_visible(True)
    #
    p1, = host.plot(time_j,volume,'darkgreen',  label="volume")
    p2, = par1.plot(time_j,temperature,'pink', label="Temperature",antialiased="True")
    p3, = par2.plot(time_j,humidity, 'b',label="humidity",antialiased="True")
    p4, = par3.plot(time_j,brightness, 'y',label="brightness",antialiased="True")
    p5, = par4.plot(time_j,ultraviolet, 'violet',label="ultraviolet",antialiased="True")
    p6, = par5.plot(time_j,atmopressure, 'grey',label="atmopressure",antialiased="True")
    p7, = par6.plot(time_j,discomfort, 'peru',label="discomfort",antialiased="True")
    p8, = par7.plot(time_j,heatstrokerisk, 'r',label="heatstrokerisk",antialiased="True")
    p9, = par8.plot(time_j,co2, 'lightgreen',label="co2",antialiased="True")

    host.set_xlabel("time")
    host.set_ylabel("volume")
    par1.set_ylabel("Temperature")
    par2.set_ylabel("humidity")
    par3.set_ylabel("brightness")
    par4.set_ylabel("ultraviolet")
    par5.set_ylabel("atmopressure")
    par6.set_ylabel("discomfort")
    par7.set_ylabel("heatstrokerisk")
    par8.set_ylabel("co2")

    tkw = dict(size=4, width=1.5)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
    par3.tick_params(axis='y', colors=p4.get_color(), **tkw)
    par4.tick_params(axis='y', colors=p5.get_color(), **tkw)
    par5.tick_params(axis='y', colors=p6.get_color(), **tkw)
    par6.tick_params(axis='y', colors=p7.get_color(), **tkw)
    par7.tick_params(axis='y', colors=p8.get_color(), **tkw)
    par8.tick_params(axis='y', colors=p9.get_color(), **tkw)
    host.tick_params(axis='x',labelsize=8,**tkw)

    pyplot.savefig('kddifigure.png')

    return nowtime,nowhumidity,nowtemperature,nowbrightness,nowultraviolet,nowatmopressure,nowvolume,nowdiscomfort,nowheatstrokerisk,nowco

    

   

        
def tophp():
    # f=open('tojson.json')
    # data=f.read()
    # f.close()
    # r = requests.post("http://192.168.10.179/sensorAPI.php", data=data)
    # print(r)
    result=tojson()
    data=[{"time":result[0],
          "humidity":result[1],
          "temperature":result[2],
          "brightness":result[3],
          "ultraviolet":result[4],
          "atmopressure":result[5],
          "volume":result[6],
          "discomfort":result[7],
           "heatstrokerisk":result[8],
            "co2":result[9]}]
    r = requests.post("http://192.168.20.42/sensorAPI.php", data=json.dumps(data))
    print(r)

def pic():
    url='http://192.168.20.61/pic.php'
    files={'image':("photo.png",open('kddifigure.png','rb'),"image/png")}
    r=requests.post(url,files=files)
    print(r)



    
if __name__=='__main__':
    interval=700
    while True:
        kddiapi()
        transcsv()
        tojson()
        tophp()
        #pic()
        time.sleep(interval)












    
