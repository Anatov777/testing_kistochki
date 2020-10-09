from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def fx_driver():
       fx_driver = webdriver.Firefox(firefox_binary=r'C:\Program Files\Mozilla Firefox\firefox.exe')
       yield fx_driver
       fx_driver.close()

class TestShares:
       def checkSalesContent(self, driver, element):
              if (WebDriverWait(driver, 0.5, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'Sales__Content')))): element += 1
              return element

       def checkLinks(self, driver, base_link, card, selector):
              base_link.click()
              WebDriverWait(driver, 0.5, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector))).click()
              card = self.checkSalesContent(driver, card)
              return card

       def test_links(self, fx_driver):
              fx_driver.get('https://kistochki.ru/akcii')
              card = 0
              WebDriverWait(fx_driver, 0.5, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#__layout > div > div > div.PageScroll.Sales__Scroll > div > div:nth-child(1) > div.CardPopular__Picture'))).click()
              card = self.checkSalesContent(fx_driver, card)
              shares_link = WebDriverWait(fx_driver, 0.5, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#__layout > div > div > div.SidebarFixed.Info__Aside.vue-sticky-el.top-sticky > div:nth-child(3) > nav > ul > li:nth-child(1) > a')))
              card = self.checkLinks(fx_driver, shares_link, card, '#__layout > div > div > div.PageScroll.Sales__Scroll > div > div:nth-child(2) > div.CardPopular__Center > a')
              card = self.checkLinks(fx_driver, shares_link, card, '#__layout > div > div > div.PageScroll.Sales__Scroll > div > div:nth-child(3) > div.CardPopular__Btn > div > a')
              card = self.checkLinks(fx_driver, shares_link, card, '#__layout > div > div > div.PageScroll.Sales__Scroll > div > div:nth-child(4) > div.CardPopular__Picture')
              card = self.checkLinks(fx_driver, shares_link, card, '#__layout > div > div > div.PageScroll.Sales__Scroll > div > div:nth-child(5) > div.CardPopular__Center > a')
              card = self.checkLinks(fx_driver, shares_link, card, '#__layout > div > div > div.PageScroll.Sales__Scroll > div > div:nth-child(6) > div.CardPopular__Btn > div > a')
              WebDriverWait(fx_driver, 0.5, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#__layout > div > div > div.SidebarFixed.Info__Aside.vue-sticky-el.top-sticky > div:nth-child(3) > nav > ul > li:nth-child(2) > a'))).click()
              card = self.checkSalesContent(fx_driver, card)
              WebDriverWait(fx_driver, 0.5, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#__layout > div > div > div.SidebarFixed.Info__Aside.vue-sticky-el.top-sticky > div:nth-child(3) > nav > ul > li:nth-child(3) > a'))).click()
              card = self.checkSalesContent(fx_driver, card)
              assert card == 8