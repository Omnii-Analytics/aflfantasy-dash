import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.footywire.com/afl/footy/ft_match_statistics?mid=10933"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')

# Fetch all tables within #match-statistics-team1-row
tables = soup.select("#match-statistics-team1-row table")

data = []  # to store rows of data

# Assuming the table you are interested in is the second one:
if len(tables) > 1:
    target_table = tables[2] # Adjust this index if necessary
    for row in target_table.find_all('tr'):
        values = [td.get_text(strip=True) for td in row.find_all('td')]
        data.append(values)
else:
    print("Target table not found.")

# Convert list of lists to DataFrame
df = pd.DataFrame(data[1:], columns=data[0])
print(df)
print(df.iloc[:, 0])

