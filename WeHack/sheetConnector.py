import gspread
import pandas as pd
sa = gspread.service_account()
sh = sa.open("WeHack")
wks = sh.worksheet("BaseSheet")
df = pd.DataFrame({'a':['astronaut', 'ant'], 'b':['bingo', 'bee'], 'c':['candy', 'cake']})
df_values = df.values.tolist()
sh.values_append('BaseSheet', {'valueInputOption': 'RAW'}, {'values': df_values})
