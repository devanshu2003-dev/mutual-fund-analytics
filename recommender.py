import pandas as pd
import numpy as np

funds = pd.read_csv("D:\\Bluestock\\mutual-fund-analytics\\reports\\sharpe_values.csv")

funds['risk_grade'] = np.where(
    funds['annual_volatility'] < 0.12,
    'Low',
    np.where(
        funds['annual_volatility'] < 0.18,
        'Moderate',
        'High'
    )
)

def recommend_funds(risk_appetite):

    return (
        funds[funds['risk_grade'] == risk_appetite]
        .sort_values('sharpe_ratio', ascending=False)
        [['amfi_code',
          'sharpe_ratio',
          'annual_return',
          'annual_volatility']]
        .head(3)
    )

risk = input("Enter Risk Appetite (Low/Moderate/High): ")

print(recommend_funds(risk))