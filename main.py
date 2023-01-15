from bs4 import BeautifulSoup
# import lxml

with open("website.html", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

section_heading = soup.select(".heading")
print(section_heading)

profile_pic = soup.select("#profile-pic")
print(profile_pic)