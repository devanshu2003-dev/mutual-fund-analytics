import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"
response = requests.get(url)
data = response.json()
nav_df = pd.DataFrame(data['data'])
print(nav_df.head(100))

nav_df.to_csv("D:\\Bluestock\\mutual-fund-analytics\\data\\raw\\hdfc_top_100_direct.csv", index =False)
print("\n CSV file saved \n")

print("\n Now for the next five funds \n")
funds = {
    "Sbi_Bluechip" : 119551 ,
    "ICICI Bluechip" : 120503 ,
    "Nippon_Large_Cap" : 118632 ,
    "Axis Bluechip" : 119092 ,
    "Kotak Bluechip" : 120841 
}
for fund_name , fund in funds.items():
    url = f"https://api.mfapi.in/mf/{fund}"
    response  = requests.get(url)
    data_fund = response.json()
    fund_df = pd.DataFrame(data_fund["data"])
    fund_df.to_csv(f"D:\\Bluestock\\mutual-fund-analytics\\data\\raw\\{fund_name}.csv" , index = False)

print("\n File saved successfully for the funds \n")
