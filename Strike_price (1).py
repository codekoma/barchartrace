from nse_scrap1 import webscrap
from pymongo import MongoClient
import pandas as pd
import time

def max_strike():
    connection = MongoClient('localhost', 27017)
    oi_collec = f"oi_collec"
    try:
        oi_db = connection['MAX_OI']
        oi_db[oi_collec].drop()
        # print('status Collec Deleted')
    except Exception as e:
        print('error',e)

    try:
        webscrap()

        data=pd.read_csv("nse_data1.csv")
        data=data.replace('-',"0")

        data[['OI','OI.1']]=data[['OI','OI.1']].apply(pd.to_numeric)

        #============Calls=========================
        max_oi=data.nlargest(5,['OI'])
        df=pd.DataFrame(max_oi[['OI','Strike Price']])
        call_oi,call_oi_sp=df["OI"],df["Strike Price"]
        # print(call_oi)
        #=============Puts=====================
        max_oi1=data.nlargest(5,['OI.1'])
        f=pd.DataFrame(max_oi1[['OI.1','Strike Price']])
        put_oi,put_oi_sp=f["OI.1"],f["Strike Price"]
        a=0
        for i,j in zip(call_oi,call_oi_sp):
            color=["red","yellow","green","blue","violet"]
            post={"id":j,"label":j,"value":i,"color":color[a]}
            a+=1
            save(post)
    
    except Exception as e:
        print(e)

    
def save(post):
    try:
        client = MongoClient()
        db = client['MAX_OI']
        collec = f"oi_collec"
        db.create_collection(collec)
        # print(f"Created New Collection '{collec}'")
        db[collec].insert_one(post)
        
    except:
        db[collec].insert_one(post)

while True:
    max_strike()
    time.sleep(300)