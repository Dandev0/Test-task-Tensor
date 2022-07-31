import pytest
from YandexPages import SearchHelper


@pytest.mark.usefixtures('driver')
class TestYandex():
    def test_yandex_search(self, driver):
        yandex_main_page = SearchHelper(driver)
        yandex_main_page.go_to_site()

    def test_search_field(self, driver):
        yandex_main_page = SearchHelper(driver)
        yandex_main_page.search_field(text='Тензор')

    def test_suggest(self, driver):
        yandex_main_page = SearchHelper(driver)
        yandex_main_page.check_suggest()

    def test_search(self, driver):
        yandex_main_page = SearchHelper(driver)
        yandex_main_page.submit()
        yandex_main_page.check_site(site='https://tensor.ru/')


@pytest.mark.usefixtures('driver')
class TestYandexImage():
    def test_yandex_image(self, driver):
        yandex = SearchHelper(driver)
        yandex.go_to_site()

    def test_yandex_image_button(self, driver):
        yandex = SearchHelper(driver)
        yandex.check_images_button()

    def test_url(self, driver):
        yandex = SearchHelper(driver)
        yandex.switch_window()
        yandex.check_current_url()

    def test_categories_in_search_field(self, driver):
        yandex = SearchHelper(driver)
        name_categories = str(yandex.save_name_categories()).lower()
        yandex.open_yandex_images_categories()
        yandex.check_text_search_field(name_categories)

    def test_open_image(self, driver):
        yandex = SearchHelper(driver)
        yandex.open_first_image()
        yandex.test_check_open_image()

    def test_switch_image_next(self, driver):
        yandex = SearchHelper(driver)
        down_src = str(yandex.save_src_first_image())
        yandex.switch_to_right_image()
        yandex.check_switch_image(down_src)

    def test_switch_image_down(self, driver):
        yandex = SearchHelper(driver)
        yandex.switch_to_left_image()
        yandex.check_to_switch_first_image(yandex.save_src_first_image())


if __name__ == '__main__':
    TestYandex(SearchHelper), TestYandexImage(SearchHelper)
