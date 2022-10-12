import csv
from datetime import datetime
from matplotlib import pyplot as plt
#==================================================
#filename = 'Projects\DataImport\CSV\sitka_weather_2018_full.csv'
filename = 'Projects\DataImport\CSV\sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) # store values as list
    header_row = next(reader) #returns the next line in the file
    #print(header_row) # now we have file header only
    #-----------------------------------------------------------------
    #print("==================PRINT HEADER ===========================")
    # We use enumerate() on the list to get the index of each item, 
    # as well as the value. Thus we print column names
    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)
    #----------------------------------------------------------------
    #print("==================PRINT HIGHS ===========================")
    dates, highs, lows = [], [], []
    # Loop through the remaining rows in the file, 'cause we've read Header 
    # already and reader object continues from where it left off
    # Also it's a good idea to always use Error Handling
    for row in reader:
        try:
            # strptime not only converts to DATE but also format it as YYYY-MMM-DD
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[5]) # the 6th column = TMAX
            low = int(row[6])  # the 7th column = TMIN                        
        except ValueError: # this type of error occur if any data is missing
            # Sometimes you’ll use continue to skip over some data or use 
            # remove() or del to eliminate some data after it’s been extracted
            print(current_date, 'missing data')    
        else:
            dates.append(current_date)
            highs.append(high) # append the data from index 5, 
            lows.append(low)
        #print(current_date)
    #------------------------------------------------------------------
    
#======================================================================   
# Plot data.
# We store chart object in variable only to refer to it in function autofmt_xdate
fig = plt.figure(dpi=128, figsize=(10, 6)) 
'''
The alpha argument at controls a color's transparency. An alpha value 
of 0 is completely transparent, and 1 (the default) is completely opaque. 
By setting alpha to 0.5 we make the red and blue plot lines appear lighter.
Also we pass fill_between() the list dates for the x-values and then the
two y-value series highs and lows. The facecolor argument determines the
color of the shaded region, and we give it a low alpha value of 0.1 so the
filled region connects the two data series without distracting from the
information they represent. 
'''
# Pass two linked lists of dates and highs to plot() and set color
plt.plot(dates, highs, c='red',  alpha=0.5) # MAX temperature. 
plt.plot(dates, lows,  c='blue', alpha=0.5) # MIN temperature
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=15)
fig.autofmt_xdate() # draw the date labels diagonally to prevent them from overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.show()
