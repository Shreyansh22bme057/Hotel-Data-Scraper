import requests 
from bs4 import BeautifulSoup
import lxml
import csv
import time

url_text = 'https://www.booking.com/searchresults.en-gb.html?ss=Mumbai&ssne=New+Delhi&ssne_untouched=New+Delhi&label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4AueF3b0GwAIB0gIkMjFkYTVhYTMtZWM5ZC00ZmYyLTkzMDktZjUxN2IxMzVjZTdk2AIF4AIB&sid=e926d54c76bc20f9416c4f573131702a&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-2092174&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=bb7575c39e5206d2&ac_meta=GhBiYjc1NzVjMzllNTIwNmQyIAAoATICZW46Bk11bWJhaUAASgBQAA%3D%3D&checkin=2025-04-01&checkout=2025-04-02&group_adults=2&no_rooms=1&group_children=0&flex_window=1'



def web_scrapper(web_url, file_name):

    print("Thank you sharing the url and file name!\n⏳\nReading the content!")
   
    header1 = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

 


    response = requests.get(url_text, headers=header1)
    print(response.status_code)

    if response.status_code == 200:
        print("Connected to the website successfully!")
        html_content = response.text

        soup = BeautifulSoup(html_content, 'lxml')
#       print(soup.prettify())

        hotel_divs = soup.find_all('div', role="listitem")
            
        with open(f'{file_name}.csv', 'w', encoding='utf-8') as file_csv:
            writer = csv.writer(file_csv)

            writer.writerow(['Hotel Name', 'Location', 'Reach', 'Score', 'Rating', 'Review', 'Link'])

        for hotel in hotel_divs:
            hotel_name = hotel.find('div', class_= "b87c397a13 a3e0b4ffd1").text.strip()
            hotel_name if hotel_name else "NA"
    
            location = hotel.find('span', class_="d823fbbeed f9b3563dd4").text.strip()
            location if location else "NA"

            reach = hotel.find('span', class_= "a297f43545").text.strip()
            if reach:
                reach
            else:
                "NA"

            score = hotel.find('div', class_="bc946a29db").text.strip()
            score if score else "NA"
            
            rating = hotel.find('div', class_="aa225776f2 ca9d921c46 e951e75167").text
            rating if rating else "NA"
                
            review = hotel.find('div', class_="fff1944c52 fb14de7f14 eaa8455879").text.strip()
            review if review else 'NA'
                
            link = hotel.find('a', href=True).get('href')
            link if link else 'NA'
        
            #print(hotel_name)
          #  print(location)
           # print(reach)
           # print(score)
          #  print(rating)
          #  print(review)
          #  print(link)


    else:
        print(f"Connection failed! {response.status_code}")



if __name__ == "__main__":

    url= input("Please enter the url! :")
    file_name= input("Please give the file name! :")  # To avoid overwhelming the server with requests

    web_scrapper(url, file_name)