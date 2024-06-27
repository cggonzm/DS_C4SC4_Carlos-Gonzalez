from vega_datasets import data as vega_data
import pandas as pd
import streamlit as st

movie_df = pd.read_json(vega_data.movies.url)

def extract_year(value):
    return pd.to_datetime(value, format='%b %d %Y').year

movie_df["Year"] = movie_df["Release_Date"].apply(extract_year)

movie_2000 = movie_df[movie_df["Year"] == 2000]

alt.Chart(movie_2000).mark_point(filled=True).encode(
    alt.X('Production_Budget'),
    alt.Y('Worldwide_Gross'),
    alt.Size('US_Gross'),
    alt.Color('Major_Genre'),
    alt.OpacityValue(0.7)
)
