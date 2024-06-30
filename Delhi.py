import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
url = "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U05.htm"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
all_tables = soup.find_all('table')
print(f"Number of tables found: {len(all_tables)}")
if all_tables:
    table = all_tables[0]
    print("Table attributes:", table.attrs)
    print("\nFirst few rows of the table:")
    for row in table.find_all('tr'):  
        print([cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])])
    html_string = StringIO(str(table))
    try:
        df_list = pd.read_html(html_string)
        if df_list:
            df = df_list[0]
            print("\nTable contents :")
            print(df.head().to_string(index=False))
        else:
            print("No tables found by pandas")
    except Exception as e:
        print(f"Error parsing table with pandas: {e}")
else:
    print("No tables found in the HTML")