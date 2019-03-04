from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen(input("Enter URL: "))
soup = BeautifulSoup(page, "html.parser")

spans = soup('span')

numbers = []

for span in spans:
    numbers.append(int(span.string))

print(sum(numbers))
