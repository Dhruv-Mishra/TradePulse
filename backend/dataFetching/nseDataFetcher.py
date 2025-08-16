import requests
import pandas as pd
from io import StringIO

def fetchFromSite(startDate:str,endDate:str,type:str="bulk_deals"):
    # URL to fetch the CSV
    url = f"https://www.nseindia.com/api/historicalOR/bulk-block-short-deals?optionType={type}&from={startDate}&to={endDate}csv=true"

    # Set headers to mimic a browser (NSE blocks bots without headers)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept": "text/csv",
        "Referer": "https://www.nseindia.com/"
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check if response is successful
    if response.status_code == 200:
        # Parse JSON directly
        data = response.json()
        
        # Extract the "data" list and convert to DataFrame
        df = pd.DataFrame(data.get("data", []))
        print(df.columns)
    else:
        print("Failed to fetch data. Status code:", response.status_code)

def fetchFromCSV(filename):
    df = pd.read_csv(filename)
    print(df.head)

fetchFromSite("9-08-2025","16-08-2025")