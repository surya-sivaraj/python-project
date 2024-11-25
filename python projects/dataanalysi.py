import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.downloader.download('vader_lexicon')

file = 'C:/Users/surya/Downloads/FSI-2023-DOWNLOAD.xlsx'
xl = pd.ExcelFile(file)  # read the file
dfs = xl.parse(xl.sheet_names[0])  # parsing the first sheet
#dfs = list(dfs['Timeline'])  # remove the blank space
print(dfs)
sid=SentimentIntensityAnalyzer()
str1="UTC+05:30"
for data in dfs:
    a=data.find(str1)
    if(a==-1): #doesnot found
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])

