from bs4 import BeautifulSoup
import requests
import re
class HDRezka():
    @staticmethod
    def get_parsed_page( url, headers = {}, params = None):
            headers = {
                "referer": "https://www.yandex.ru",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
            return BeautifulSoup(requests.get(url, headers = headers, params = params, timeout=(3.05, 27)).text, "lxml")
    
    
    
    def search (self, keyword):
        
        params = {
            "do":"search",
            "subaction":"search",
            "q":keyword
        }
        page = self.get_parsed_page(self.url, params = params)
        links = page.find_all("a")
        links = [el.get("href") for el in links]
        if "search" in links[-1]: links.pop(-1)
        result = {}
        for i in range(len(links)):
            current_page = self.get_parsed_page(links[i])
            main_block = current_page.find("div", {"class", "b-content__main"})
            
            film_name = main_block.find("div", {"class", "b-post__title"}).text
            film_img = main_block.find("img").get("src")
            tds = main_block.find_all("td")
            film_year = tds[7].text
            film_zhanr = tds[13].text
            film_country = tds[9].text
            film_director = tds[11].text
            film_actors = tds[24].text.replace("В ролях актеры:","")
            film_description = main_block.find("div", {"class", "b-post__description_text"}).text
            full_info = {"film_img":film_img,"film_year":film_year,"film_zhanr":film_zhanr, "film_name":film_name,
                            "film_country":film_country,"film_director":film_director,"film_actors":film_actors,"film_description":film_description}
            result[i] = full_info
        return result
    def __init__(self,keyword, link = "http://rezkance.com/engine/ajax/search.php"):
        self.url = link
        self.keyword  = keyword
        
        self.search_results = self.search(self.keyword)
    
#rezka = HDRezka("http://rezkance.com/engine/ajax/search.php")
#print(rezka.search("гарри поттер"))

    
#full_info = {"film_img":film_img,"film_year":film_year,"film_zhanr":film_zhanr, "film_name":film_name,
#                      "film_country":film_country,"film_director":film_director,"film_actors":film_actors,"film_description":film_description}