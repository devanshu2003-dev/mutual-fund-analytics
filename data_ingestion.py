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
print("\n Investor Transaction \n")
investor_transc = ingest_data("D:\\Bluestock\\mutual-fund-analytics\\data\\raw\\investor_transactions.csv")
print(investor_transc.head(5))
print(investor_transc.dtypes)

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

# DAY 2 DATA CLEANING + SQL DATABASE DESIGN
# fund_master.csv = fund_master
# aum_by_fund_house.csv = aum_history
# monthly_sip_inflows.csv = monthly_sip_inflows
# category_inflows.csv = category_inflows
# industry_folio_count.csv = industry_folio_counts
# portfolio_holdings.csv = portfolio_holdings
# benchmark_indices.csv = benchmark_indices

# nav_history.csv = nav_history
# investor_transactions.csv = investor_transc
# scheme_performance.csv = scheme_performance 
print("Missing values :\n",fund_master.isnull().sum())
print("\n")
print("Duplicate values ",fund_master.duplicated().sum())

def analyse(dataframe):
    print("\nMissing values :\n",dataframe.isnull().sum())
    print("\n Duplicate values : \n", dataframe.duplicated().sum())
    return None
print("\nfundmaster")
f1 = analyse(fund_master)
print("\n aum history")
f2 = analyse(aum_history)
print("\n monthly sip flow")
f3 = analyse(monthly_sip_inflows)
print("\n category inflow")
f4 = analyse(category_inflows)
print("\n industry folio count")
f5 = analyse(industry_folio_counts)
print("\n portfolio holdings")
f6 = analyse(portfolio_holdings)
print(" \n benchmark indices")
f7 = analyse(benchmark_indices)


print("\n from the above analysis we got monthly sip has 12 missing values")

# handling missing values in monthly_sip_inflows
print(
    monthly_sip_inflows['yoy_growth_pct']
)
monthly_sip_inflows[monthly_sip_inflows['yoy_growth_pct'].isnull()] # give the corresponding row data of nan values

print("since the yoy growth of 2021 is not give so growth cannot be calculated and nothing can be done here")

def convert_datatype(dataframe,column):
    dataframe[column] = pd.to_datetime(dataframe[column], format= 'mixed')
    return dataframe
convert_datatype(aum_history,'date')   # passing the column name in string
convert_datatype(portfolio_holdings, 'portfolio_date')
portfolio_holdings['portfolio_date'].dtypes
convert_datatype(benchmark_indices, 'date' )
benchmark_indices['date'].dtypes
df_list = (
    "fund_master",
    "aum_history",
    "monthly_sip_inflows",
    "category_inflows",
    "industry_folio_counts",
    "portfolio_holdings",
    "benchmark_indices",
)

def check_datatype(df_name):
    
    if df_name in globals():
        df_object = globals()[df_name]
        print(f"\n Datatypes of {df_name} :")
        print(df_object.dtypes)
    else:
        print(f"\n Error: Variable '{df_name}' does not exist.")

# 2. Run the loop
for df in df_list:
    check_datatype(df)

# nav_history analysing
print("\n nav history")
f8 = analyse(nav_history)
print("\n scheme performance")
f10 = analyse(scheme_performance)
print("\n investor transaction")
f9 = analyse(investor_transc)

print("from the output we can see there is no NAN and duplicate values in the above")
nav_history.info()
nav_history.dtypes
nav_history['date'] = pd.to_datetime(nav_history['date'] , format = 'mixed' , errors = 'coerce')
nav_history['date'].isnull().sum()
nav_history = nav_history.sort_values(['amfi_code', 'date'])
nav_history

# scheme performance analysing

scheme_performance.info()

scheme_performance.dtypes
# this code was written for experiment on duplicate database scheme, not to spoil the original database
# scheme = scheme_performance
# print(scheme)
# scheme.iloc[:,5:8] = scheme.iloc[:, 5:8].apply(pd.to_numeric , errors= 'coerce')
# scheme.dtypes
scheme_performance.iloc[:,5:8] = scheme_performance.iloc[:, 5:8].apply(pd.to_numeric , errors= 'coerce')
scheme_performance.dtypes
scheme_performance['sharpe_ratio']
negative_ratio = scheme_performance[scheme_performance['sharpe_ratio']< 0]
print("\n scheme with negative sharpe ratio", negative_ratio)
print("\n from the output we got there is no negative sharpe ratio")
scheme_performance['expense_ratio_pct']
exp_ratio = scheme_performance[(scheme_performance['expense_ratio_pct'] > 2.5) | (scheme_performance['expense_ratio_pct'] < 0.1)]
exp_ratio

print("from the output we got all the expense ratio of scheme are between 0.1 to 2.5 ")

# investor transaction analysing
investor_transc.info()
investor_transc.dtypes
investor_transc['transaction_date'] = pd.to_datetime(investor_transc['transaction_date'], format = 'mixed' )
investor_transc['transaction_date'].dtypes
investor_transc.dtypes
investor_transc['transaction_type'].value_counts()
investor_transc['transaction_type'].unique()
print("\n Validation Result:transaction_type column contains only three standardized values: SIP, Lumpsum, Redemption hence, no cleaning required.")
amount_lessthan_zero = investor_transc[investor_transc['amount_inr']<0]
print("\n invalid transaction" , amount_lessthan_zero)
print("\n every transaction is valid")
print("\n KYC status values ",investor_transc['kyc_status'].unique())
print("\n", investor_transc['kyc_status'].value_counts())
print(investor_transc.columns.tolist())



"""
amfi_code               int64
fund_house             object
scheme_name            object
category               object
sub_category           object
plan                   object
launch_date            object
benchmark              object
expense_ratio_pct     float64
exit_load_pct         float64
min_sip_amount          int64
min_lumpsum_amount      int64
fund_manager           object
risk_category          object
sebi_category_code     object   """

# Save all cleaned datasets to data/processed/

fund_master.to_csv(
    "data/processed/clean_fund_master.csv",
    index=False
)

aum_history.to_csv(
    "data/processed/clean_aum_by_fund_house.csv",
    index=False
)

monthly_sip_inflows.to_csv(
    "data/processed/clean_monthly_sip_inflows.csv",
    index=False
)

category_inflows.to_csv(
    "data/processed/clean_category_inflows.csv",
    index=False
)

industry_folio_counts.to_csv(
    "data/processed/clean_industry_folio_count.csv",
    index=False
)

portfolio_holdings.to_csv(
    "data/processed/clean_portfolio_holdings.csv",
    index=False
)

benchmark_indices.to_csv(
    "data/processed/clean_benchmark_indices.csv",
    index=False
)

nav_history.to_csv(
    "data/processed/clean_nav.csv",
    index=False
)

investor_transc.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

scheme_performance.to_csv(
    "data/processed/clean_scheme_performance.csv",
    index=False
)

print("All 10 cleaned datasets saved successfully!")









