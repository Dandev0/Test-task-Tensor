from BaseApp import BasePage
from selenium.webdriver.common.by import By


class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.XPATH, '//*[@class="input__control input__input mini-suggest__input"]')
    LOCATOR_SUGGEST = (By.XPATH, '//*[@class="mini-suggest__item mini-suggest__item_type_fulltext"]')
    LOCATOR_SEARCH_RESULT = (By.XPATH, '//*[@id="search-result"]/li[1]/div/div[1]/div[2]/div[1]/a')


class SearchHelper(BasePage):
    def search(self, text):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(text)
        return search_field

    def check_suggest(self):
        suggest = self.find_element(YandexSeacrhLocators.LOCATOR_SUGGEST)
        return suggest

    def submit(self):
        enter = self.search(text='')
        enter.submit()
        return enter

    def check_site(self, site):
        site_search = self.find_element(YandexSeacrhLocators.LOCATOR_SEARCH_RESULT)
        assert site != site_search
        print(site_search)













    # def click_on_the_search_button(self):
    #     return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON,time=3).click()
    #
    # def check_navigation_bar(self):
    #     all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR,time=3)
    #     nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
    #     return nav_bar_menu