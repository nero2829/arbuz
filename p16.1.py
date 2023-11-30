import csv
import requests
from bs4 import BeautifulSoup
def read1(file_path, delimiter='\t'):
    data=[]
    with open(file_path,'r') as file:
        reader=csv.reader(file, delimiter=delimiter)
        for row in reader:
            data.append(row)
    return data
def poshsliv(page, words):
    poshsliv=[]
    for word in words:
        elements=page.find_all(string=lambda text: word.lower() in str(text).lower())
        if elements:
            poshsliv.append((word, elements))
    return poshsliv
if __name__ == "__main__":
    filepath=r"D:\dteu\vkn\2023.11\16 pt\silka16.txt"
    data=read1(filepath)
    pages=[]
    for row in data:
        url=row[0]
        response=requests.get(url)
        if response.status_code == 200:
            soup=BeautifulSoup(response.text,'html.parser')
            pages.append(soup)
        else:
            print(f"Failed to fetch {url}")
    x = input("Enter the first word to search: ")
    y = input("Enter the second word to search: ")
    z = input("Enter the third word to search: ")
    h = input("Enter the fourth word to search: ")
    k = input("Enter the fifth word to search: ")
for i, page in enumerate(pages):
        print(f"\nSearching in page {i + 1} ({data[i][0]}):")
        results = poshsliv(page, [x, y, z, h, k])
        if results:
            for word, elements in results:
                print(f"Word '{word}' found: {len(elements)}")
        else:
            print("No words found.")
