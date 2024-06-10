from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_nearest_place(query, latitude, longitude):

    driver = webdriver.Chrome()

    map_url = f"https://www.google.com/maps/search/{query}/@{latitude},{longitude},15z"

    driver.get(map_url)

    time.sleep(5)

    place_elements = driver.find_elements_by_xpath("//div[@class='section-result-details-container']")

    if not place_elements:
        return "Nenhum local encontrado próximo a você."

    places_info = []
    for place_element in place_elements:
        place_name = place_element.find_element_by_xpath(".//h3[@class='section-result-title']").text.strip()
        place_address = place_element.find_element_by_xpath(".//span[@class='section-result-location']").text.strip()
        aria_label = get_aria_label(driver, place_element)
        places_info.append(f"O lugar mais próximo encontrado é '{place_name}' localizado em '{place_address}' - Aria label: '{aria_label}'.")

    driver.quit()

    return "\n".join(places_info)

def get_aria_label(driver, element):
    return element.get_attribute("aria-label")

if __name__ == "__main__":
    latitude = -21.332407  
    longitude = -46.368329 
    print(get_nearest_place("Pizzaria", latitude, longitude))
