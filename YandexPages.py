import time
from BaseClass import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class YandexLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.XPATH, '//*[@class="input__control input__input mini-suggest__input"]')
    LOCATOR_SUGGEST = (By.XPATH, '//ul[@class="mini-suggest__popup-content"]')
    LOCATOR_SEARCH_RESULT = (By.XPATH, '//*[@class= "Link Link_theme_outer Path-Item link path__item link organic__greenurl"]')
    LOCATOR_YANDEX_IMAGES = (By.XPATH, '//*[@class="services-new__icon services-new__icon_images"]')
    LOCATOR_IMAGES_CATEGORIES = (By.XPATH, '//div[@class="PopularRequestList-Item PopularRequestList-Item_pos_0"]')
    LOCATOR_TEXT_SEARCH = (By.XPATH,
                           '//li[@class="mini-suggest__item mini-suggest__item_type_fulltext mini-suggest__item_arrow_yes mini-suggest__item_with-button"]')
    LOCATOR_FIRST_IMAGE = (By.XPATH,
                           '//*[@class="serp-item serp-item_type_search serp-item_group_search serp-item_pos_0 serp-item_scale_yes justifier__item i-bem justifier__item_first serp-item_loaded serp-item_js_inited"]')
    LOCATOR_ALL_IMAGES = (By.XPATH, '//*[@class="serp-item__preview"]')
    LOCATOR_OPEN_IMAGE = (By.XPATH, '//*[@class="MMImage-Origin"]')
    LOCATOR_SWITCH_RIGHT_BUTTON = (By.XPATH,
                                   '//*[@class="CircleButton CircleButton_type_next CircleButton_type MediaViewer-Button MediaViewer-Button_hovered MediaViewer_theme_fiji-Button MediaViewer-ButtonNext MediaViewer_theme_fiji-ButtonNext"]')
    LOCATOR_SWITCH_LEFT_BUTTON = (By.XPATH,
                                  '//*[@class="CircleButton CircleButton_type_prev CircleButton_type MediaViewer-Button MediaViewer_theme_fiji-Button MediaViewer-ButtonPrev MediaViewer_theme_fiji-ButtonPrev"]')


class SearchHelper(BasePage):
    def search_field(self, text):
        search_field = self.find_element(YandexLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(text)
        return search_field

    def check_suggest(self):
        time.sleep(1)
        suggest = self.find_element(YandexLocators.LOCATOR_SUGGEST)
        return suggest

    def submit(self):
        enter = self.search_field(text='')
        enter.submit()
        return enter

    def check_site(self, site):
        site_search = self.find_element(YandexLocators.LOCATOR_SEARCH_RESULT).get_attribute('href')
        assert site == site_search

    def check_images_button(self):
        check_images = self.find_element(YandexLocators.LOCATOR_YANDEX_IMAGES).click()
        return check_images

    def refresh(self):
        refresh = self.driver.refresh()
        return refresh

    def switch_window(self):
        switch = self.driver.switch_to.window(self.driver.window_handles[1])
        return switch

    def check_current_url(self):
        check_current_url = self.driver.current_url
        assert check_current_url == 'https://yandex.ru/images/?utm_source=main_stripe_big'

    def open_yandex_images_categories(self):
        images_categories = self.find_element(YandexLocators.LOCATOR_IMAGES_CATEGORIES).click()
        return images_categories

    def save_name_categories(self):
        name_categories = self.find_element(YandexLocators.LOCATOR_IMAGES_CATEGORIES).get_attribute(
            'data-grid-text')
        return name_categories

    def check_text_search_field(self, name_categories):
        text = self.find_element(YandexLocators.LOCATOR_TEXT_SEARCH).get_attribute('data-text')
        assert text == name_categories

    def open_first_image(self):
        im = self.find_element(YandexLocators.LOCATOR_ALL_IMAGES)
        img = ActionChains(self.driver).move_to_element(im)
        img.perform()
        image = self.find_element(YandexLocators.LOCATOR_FIRST_IMAGE)
        image.click()

    def test_check_open_image(self):
        image = self.find_element(YandexLocators.LOCATOR_OPEN_IMAGE)
        return image

    def save_src_first_image(self):
        first_src = self.find_element(YandexLocators.LOCATOR_OPEN_IMAGE).get_attribute('src')
        return first_src

    def switch_to_right_image(self):
        im = self.find_element(YandexLocators.LOCATOR_OPEN_IMAGE)
        img = ActionChains(self.driver).move_to_element(im)
        img.perform()
        time.sleep(1)
        button = self.find_element(YandexLocators.LOCATOR_SWITCH_RIGHT_BUTTON)
        time.sleep(1)
        button.click()


    def check_switch_image(self, down_src):
        actual_src = self.find_element(YandexLocators.LOCATOR_OPEN_IMAGE).get_attribute('src')
        assert actual_src != down_src
        return actual_src

    def switch_to_left_image(self):
        im = self.find_element(YandexLocators.LOCATOR_OPEN_IMAGE)
        img = ActionChains(self.driver).move_to_element(im)
        img.perform()
        time.sleep(1)
        button = self.find_element(YandexLocators.LOCATOR_SWITCH_LEFT_BUTTON)
        button.click()
        time.sleep(2.5)


    def check_to_switch_first_image(self, down_src):
        actual_src = self.find_element(YandexLocators.LOCATOR_OPEN_IMAGE).get_attribute('src')
        time.sleep(1)
        assert actual_src == down_src




