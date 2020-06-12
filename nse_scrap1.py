import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def webscrap():

    try:
        symbol="NIFTY"
        url="https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol="+symbol
        # print(url)
        headers={"User-Agent": "Mozilla/5.0"}
        page=requests.get(url,headers=headers)
        soup=BeautifulSoup(page.content,'lxml')
        # print(soup.title.text)
    except Exception as e:
        print("connection error",e)

    try:
        nse_table = soup.find("table",attrs={'id':'octable'})
        # nse_heading =nse_table.tbody.find_all("tr")
        # print(nse_table)

        calls_headers=[]
        puts_headers=[]
        for th,j in zip(nse_table.find_all("th"),range(26)):
            if(j<=14):
                calls_headers.append(th.text.replace('\n',' ').strip())
            else:
                puts_headers.append(th.text.replace('\n',' ').strip())

        # print(calls_headers)
        del calls_headers[0:4]
        del puts_headers[-1]
        # print(calls_headers)
        # print(puts_headers)
        calls_data=[]
        puts_data=[]
        tbody =nse_table.find_all("tr")
        trs=tbody[2:]
        # print(len(trs))
        for tr in trs[:-1]:
            c_row={}
            p_row={}

            tds=tr.find_all("td")
        # print(tds)

            for td,th in zip(tds[1:12],calls_headers):
                c_row[th] = re.sub(",|\n","",td.text).strip()
            calls_data.append(c_row)
            
            for td,th in zip(tds[12:25],puts_headers):
                p_row[th] = re.sub(",|\n","",td.text).strip() 
            puts_data.append(p_row)

    except:
        print("error")

    try:
        first_df = pd.DataFrame(calls_data)
        sec_df = pd.DataFrame(puts_data)
        final_df=pd.concat([first_df,sec_df],axis=1)

        final_df.to_csv("nse_data1.csv",index=False)

        # first_df.to_csv("nse_data1.csv")
        # sec_df.to_csv("nse_data2.csv")
        print("successful")
    except:
        print('excel error')

    
#webscrap()
