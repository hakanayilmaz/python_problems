from bs4 import BeautifulSoup
import sys
import requests

"""
This code takes some input(float) from user and returns the top IMDB movies that has a higher rating.

"""

myURL = 'https://www.imdb.com/chart/top'

headers  = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

page = requests.get(myURL,headers=headers)
content = page.content
soup = BeautifulSoup(content,'html.parser')

titles= soup.find_all("td",{"class":"titleColumn"}) #keep all title names in this list
ratings = soup.find_all("td",{"class":"ratingColumn imdbRating"}) # keep all ratings here

puan = float(input("Enter a rating..:")) # User inoput for the rating of the movie
for title,rating in zip(titles,ratings): 
    
    title = title.text
    title = title.strip()
    title = title.replace("\n" , "")
    rating = rating.text
    rating = rating.strip()
    rating = rating.replace("\n","")

    if float(rating) > puan:
            print("Title :{} - rating: {} ".format(title,rating))
           # print("ilk 3 karakteri title in {}".format(title[0:3]))
