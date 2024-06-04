import plotly.express as px

def agsf_dollar_hist(df):
    return px.histogram(df, x='$/AGSF', title='Distribution of $/AGSF')

def dollar_per_acre_hist(df):
    return px.histogram(df, x='$/Acre', title='Distribution of Total Value per Acre')