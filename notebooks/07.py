from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.dba.dk/')
browser.implicitly_wait(3)
search_field = browser.find_element(By.ID, "searchField")
search_field.send_keys('Møller')
search_field.submit()

browser.find_element(By.CLASS_NAME, "no-koebenhavn-og-omegn").click()

browser.implicitly_wait(3)

#browser.find_element(By.XPATH, "//button[contains(text(), 'KUN NØDVENDIGE')]")[0].click() # <-- Kan ikke finde den her, både med class og XPATH, så kan ikke lukke den hvis det blokerer at jeg tykker på "Oprettet"
#browser.implicitly_wait(3)
browser.find_elements(By.XPATH, "//h4[contains(text(), 'Oprettet')]")[0].click() # <-- kan ikke få lov til at trykke på den her, så kan ikke trykke på "Seneste 24 timer"

browser.implicitly_wait(3)
browser.find_elements(By.XPATH, "//span[contains(text(), 'Seneste 24 timer')]")[0].click()

browser.implicitly_wait(3)
print(browser.page_source)

# Har arbejdet meget med browser automation og web scraping før så det undrer mig meget at jeg ikke kan få det her til at virke :/