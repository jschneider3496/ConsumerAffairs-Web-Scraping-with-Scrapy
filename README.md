# ConsumerAffairs-Web-Scraping-with-Scrapy

### What this is
- Using Python's Scrapy framework, this program allows for the gathering and storing of reviews from https://www.consumeraffairs.com/ to  .csv format. 

### How to use
1. Preparation
- Go to https://www.consumeraffairs.com/
- Find a company such as Uber: https://www.consumeraffairs.com/travel/uber.html
- Find how many pages of reviews there are: As of 11/9/2019, last page is https://www.consumeraffairs.com/travel/uber.html?page=57#sort=top_reviews&filter=none
2. Reorganizing sitejapper_bs.py code
- replace range(1, 58) with desired range
- replace ''https://www.consumeraffairs.com/travel/uber.html?page='' with desired company
3. Execution
- Run sitejapper_bs.py!

### Example .csv
[![Image from Gyazo](https://i.gyazo.com/1325830faed24ce9f3eae04bd6b3c260.png)](https://gyazo.com/1325830faed24ce9f3eae04bd6b3c260)
