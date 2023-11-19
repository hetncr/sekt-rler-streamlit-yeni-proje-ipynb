#%%writefile deneme.py
# Import the necessary modules
import requests
from bs4 import BeautifulSoup
import streamlit as st

# Web scraping code to get the sector name
url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/Temel-Degerler-Ve-Oranlar.aspx?"
response = requests.get(url)
temeldegerler = BeautifulSoup(response.text, "html.parser")

# Find the table with the desired data
table = temeldegerler.find("tbody", id="temelTBody_Ozet")

# Create an empty dictionary to store the stock name and sector name pairs
hisse_sektor = {}

# Iterate over the rows in the table
for row in table.find_all("tr"):
    # Get the cells in the row
    cells = row.find_all("td")
    # Get the stock name
    hisse = cells[0].find("a").text
    # Get the sector name
    sektor = cells[2].text
    # Add the pair to the dictionary
    hisse_sektor[hisse] = sektor

# Create an input box to enter the stock name
hisse_input = st.text_input("Hisse Adı:")

# Check if the input is not empty
if hisse_input:
    # Check if the input is in the dictionary
    if hisse_input in hisse_sektor:
        # Get the sector name from the dictionary
        sektor_output = hisse_sektor[hisse_input]
        # Display the sector name
        st.write("Sektör Alanı:", sektor_output)
    else:
        # Display an error message
        st.write("Hisse bulunamadı.")
