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

#334388962.athing td.title span.titleline a > td:nth-child(3) > span > a
# page = requests.get('https://news.ycombinator.com/')
# page_text = page.text
# tree = html.fromstring(page_text)
# print(tree)
# first_article_text = tree.xpath('html/body/center/table/tbody/tr[3]/td/table/tbody/tr[1]/td[3]/span/a')
# print(first_article_text)

#\33 4388369 > td:nth-child(3) > span > a

# /html/body/center/table/tbody/tr[3]/td/table/tbody/tr[1]/td[3]/span/a

