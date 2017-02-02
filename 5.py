import csv
from datetime import date as d, datetime as dt

path = 'd:\gm.csv.csv'
file = open(path, newline = '')
reader = csv.reader(file)

header = next(reader)   # the first line is the header

data = []

for row in reader:
    # row = [date, open, high, low, close, volume, adj. close]
    date = dt.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1]) # open is  a builtin function
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])

# compute the daily returns
    
returns_path = 'd:/gm.csv.csv'
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
    todays_row = data[i]
    today_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterday_price = yesterdays_row[-1]

    daily_returns = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([todays_date, daily_returns])
   
    
