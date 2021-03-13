![FANG](https://static.seekingalpha.com/uploads/2018/1/7/48200183-15153603846257193_origin.jpg)

# FANG Stocks Prediction and Quantitative Trading using Sentiment Analysis

> This project aims to investigate the prediction power of public sentiment on FANG, i.e Facebook, Amazon, Netflix and Google, extracted from [Economics Subreddit](https://www.reddit.com/r/Economics/) and [New York times](https://www.nytimes.com) by comparing the prediction accuracy of different machine learning methods. 

##### We conclude that simpler models, such as linear regression and random forest better predict `(63.16% accuracy)` on stock return's growth trend using sentiment, largely due to high correlations between sentiment effects and stock prices.

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

> RESULT:

> ASSUMPTION:

> DATA:

> MODEL:

---
## Table of Contents

- [Abstract](#abstract)
- [Data Source](#dataSource)
- [Exploratory Data Analysis](#exploratoryDataAnalysis)
- [Benchmark](#benchmark)
- [Sentiment Analysis](#sentimentanalysis)
- [Trading Strategy](#tradingstrategy)
- [Conclusion](#conclusion)
- [Team](#team)

---

## Data Source
Sorted New York Times Data
![nytimes_data](https://github.com/danielle707/stock_sentiment_analysis_using_social_media/blob/master/src/media/nytimes_data.png)
Stock Price from Nov 26th 2018 to Nov 11th 2019:

Emotional Analysis with `NRC emotion lexicon`: counting 8 emotions and 2 sentiments
```python
def return_emotions(stock_df):
count = 0
columns = ['anticipation', 'sadness', 'joy', 'negative', 'trust', 'positive', 'surprise', 'disgust', 'anger', 'fear']
emotions = pd.concat([pd.DataFrame(emotion_analyzer(i), columns=columns) 
for i in stock_df['lead_paragraph']], ignore_index=True)
return emotions
```
---
New York Times Headline Daily Sentiment Daily
![nytimes_fb_sent](https://github.com/danielle707/stock_sentiment_analysis_using_social_media/blob/master/src/media/nytimes_fb_sent.png)

## Exploratory Daily Sentiment Data Analysis
Daily Sentiemnt 


## Contributors


| <a href="https://github.com/danielle707" target="_blank">**Danielle (zw2631)**</a> | <a href="https://github.com/cuengjobjob" target="_blank">**Mary Shao**</a> |
| :---: |:---:|
| [![Danielle](https://avatars0.githubusercontent.com/u/36138460?s=400&u=99ec29ff9741db96c1115b7d4322ae4a089d9f6f&v=4&s=200)](https://www.linkedin.com/in/zhidanwang/)    | [![Mary](https://avatars0.githubusercontent.com/u/58192127?s=460&v=4?&s=200)](https://www.linkedin.com/in/menglin-mary-shao-86b909158/)

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)
