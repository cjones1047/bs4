from bs4 import BeautifulSoup
import requests
import re

# with open("website.html", "r") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# section_heading = soup.select(".heading")
# print(section_heading)
#
# profile_pic = soup.select("#profile-pic")
# print(profile_pic)

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

first_titleline_element = soup.find(class_="titleline")
first_article_string = first_titleline_element.next_element.string
print(first_article_string)

first_article_score_element = soup.find(class_="score")
first_article_score_string = first_article_score_element.string
first_article_score_num = float(re.findall(r"[-+]?\d*\.?\d+|[-+]?\d+", first_article_score_string)[0])
print(first_article_score_num)

first_article_link = first_titleline_element.next_element.get("href")
print(first_article_link)

print('-' * 20)

sa_stock_ideas_response = requests.get("https://seekingalpha.com/stock-ideas")
sa_stock_ideas = sa_stock_ideas_response.text
all_tickers_mentioned_soup = BeautifulSoup(sa_stock_ideas, "html.parser")
all_tickers_mentioned = all_tickers_mentioned_soup.find_all(class_='qE-ji')
print(f"Length of tickers list: {len(all_tickers_mentioned)}")
all_tickers_mentioned_set = {ticker.string for ticker in all_tickers_mentioned}
print(f"Length of tickers set: {len(all_tickers_mentioned_set)}")
print(all_tickers_mentioned_set)
searched_ticker = 'TSLA'
if searched_ticker in all_tickers_mentioned_set:
    print(f"{searched_ticker} is in set.")
else:
    print(f"{searched_ticker} is NOT in set")

searched_stock_page_response = requests.get(f"https://seekingalpha.com/symbol/{searched_ticker}")
searched_stock_page = searched_stock_page_response.text
searched_stock_page_soup = BeautifulSoup(searched_stock_page, "html.parser")
searched_stock_page_price = searched_stock_page_soup.find(class_="qv-Qf aw-g1 aw-hi aw-hn")
searched_stock_page_price_text = searched_stock_page_price.text
print(searched_stock_page_price_text)
searched_stock_price_string = re.search(r"[-+]?\d*\.?\d+|[-+]?\d+", searched_stock_page_price_text).group(0)
print(f"{type(searched_stock_price_string)} {searched_stock_price_string}")
searched_stock_price_float = float(searched_stock_price_string)
print(f"{type(searched_stock_price_float)} {searched_stock_price_float}")
