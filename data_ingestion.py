import pandas as pd

""" File loading function """
def ingest_data(file_path):
    """First loading the csv file and then converting it to dataframe """

    try:
        df = pd.read_csv(file_path)
        print("File loaded successfully : ",{file_path})
        print("Shape of the data :", df.shape)
        return df
    except Exception as e:
        print(f"Error on loading file", {file_path})
        print(e)

        return None
print("\n Funds : \n")    
fund_master = ingest_data("D:\\Bluestock\\mutual-fund-analytics\\data\\raw\\fund_master.csv")    
print(fund_master.head(5))
print(fund_master.dtypes)
#------------------------------
print("\n NAV history data:\n")
nav_history = ingest_data("D:\\Bluestock\\mutual-fund-analytics\\data\\raw\\nav_history.csv")
print(nav_history.head(5))
print(nav_history.dtypes)
#------------------------------
print("\n Asset under management (AUM) :\n")
aum_history = ingest_data("D:\\Bluestock\\mutual-fund-analytics\\data\\raw\\aum_by_fund_house.csv")
print(aum_history.head(5))
print(aum_history.dtypes)
#------------------------------
print("\n Monthly sip inflows : \n")
monthly_sip_inflows = ingest_data("D:\\Bluestock\\mutual-fund-analytics\\data\\raw\\monthly_sip_inflows.csv")
print(monthly_sip_inflows.head(5))
print(monthly_sip_inflows.dtypes)
#-------------------------------
print("\n Category inflows : \n")
category_inflows = ingest_data("D:\\Bluestock\\mutual-fund-analytics\\data\\raw\\category_inflows.csv")
print(category_inflows.head(5))
print(category_inflows.dtypes)
#-------------------------------
print("\n Industry folio counts : \n")
industry_folio_counts = ingest_data("D:\\Bluestock\\mutual-fund-analytics\\data\\raw\\industry_folio_count.csv")
print(industry_folio_counts.head(5))
print(industry_folio_counts.dtypes)
#-------------------------------
print("\n Scheme performance : \n")
scheme_performance = ingest_data("D:\\Bluestock\\mutual-fund-analytics\\data\\raw\\scheme_performance.csv")
print(scheme_performance.head(5))
print(scheme_performance.dtypes)
#-------------------------------
print("\n Portfolio holdings : \n")
portfolio_holdings = ingest_data("D:\\Bluestock\\mutual-fund-analytics\\data\\raw\\portfolio_holdings.csv")
print(portfolio_holdings.head(5))
print(portfolio_holdings.dtypes)
#-------------------------------
print("\n Indices Benchmark: \n")
benchmark_indices = ingest_data("D:\\Bluestock\\mutual-fund-analytics\\data\\raw\\benchmark_indices.csv")
print(benchmark_indices.head(5))
print(benchmark_indices.dtypes)


# Understanding and analysing the fund master
print(fund_master)
cols = fund_master.columns
print(cols)
# printing fund house, categories, sub-categories, risk grades
print(" \n printing fund house, categories, sub-categories, risk grades :\n ")
print("\n unique funds:\n" , fund_master['fund_house'].unique())
print("\n unique categories:\n" , fund_master['category'].unique())
print("\n unique sub-categories:\n" , fund_master['sub_category'].unique())
print("\n unique risk grades:\n" , fund_master['risk_category'].unique())

print("nav_history columns: \n", nav_history.columns.tolist())

code_exist = pd.merge(fund_master[['amfi_code']], nav_history[['amfi_code']].drop_duplicates(), on  = 'amfi_code', how = 'left', indicator = True)

missing_codes = code_exist[code_exist['_merge'] == 'left_only']

print("Missing amfi codes in nav_history: \n", missing_codes['amfi_code'].tolist())

with open("reports/data_quality_report.txt", "w") as file:

    file.write("DATA QUALITY SUMMARY\n")
    file.write("-" * 40 + "\n")

    file.write(f"Fund Master Codes: {len(fund_master)}\n")
    file.write(f"NAV History Codes: {len(nav_history)}\n")
    file.write(f"Missing Codes: {len(missing_codes)}\n")

    if len(missing_codes) == 0:
        file.write("All AMFI codes validated successfully.\n")
    else:
        file.write(f"Missing Codes: {missing_codes}\n")









