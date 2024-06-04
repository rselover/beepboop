import plotly.express as px

def agsf_dollar_hist(df):
    return px.histogram(df, x='$/AGSF', 
                        title='Distribution of $/AGSF',
                        range_x=[0, 1500])

def dollar_per_acre_hist(df):
    return px.histogram(df, x='$/Acre', 
                        title='Distribution of Land Value per Acre',
                        range_x=[0, 2500000])