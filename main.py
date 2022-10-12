import fnmatch
import os
import pandas as pd

# folder path
dir_path = r'C:\Done'
count = len(fnmatch.filter(os.listdir(dir_path), '*.*'))

# prints the folders count
print('File Count:', count)

#list all the folders in the present folder
entries = os.listdir(dir_path)
folder_count = 0
final_df =pd.DataFrame()

# reads the particular csv files present inside the folder
while folder_count < count:
    folder_name = entries[folder_count]
    final_df.loc[folder_count+1, 1] = folder_name
    path_totalcount = dir_path+"\\"+folder_name+"\\final.csv"
    print(path_totalcount)
    df =pd.read_csv(path_totalcount)
    total_cards = len(df. index)
    final_df.loc[folder_count + 1, 2] = total_cards
    path_cleantoutput_count = dir_path + "\\" + folder_name + "\\final.csv_CleanOutput.csv"
    print(path_totalcount)
    df1 = pd.read_csv(path_cleantoutput_count)
    cleanoutputcards = len(df1.index)
    final_df.loc[folder_count + 1, 3] = cleanoutputcards
    folder_count=folder_count+1
# write the folders and csv files row counts in a csv file
final_df.to_csv("./count.csv",index=False,header=None)
