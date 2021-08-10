"""

This script scrapes the web for a list of top 100 movies.

This script requires that 'requests', 'bs4' be installed within the Python
environment you are running this script in.

"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
movies_html = response.text
soup = BeautifulSoup(movies_html, 'html.parser')
print(soup.prettify())

# titles_list = soup.select('div div h3')
img_elements_list = soup.find_all(name='img', class_='jsx-952983560 loading')

titles_list = [title.get('alt') for title in img_elements_list[::-1]]


# for title in img_elements_list[::-1]:
#     titles_list.append(title.get('alt'))

# Here we are manipulating the list a little bit because I had to use a round about way to get the titles, which loaded more
# images and titles than I wanted

with open('./movies.txt', 'w') as file:
    for i in range(len(titles_list)-12):
        file.write(f'{i+1}) {titles_list[i]}\n')