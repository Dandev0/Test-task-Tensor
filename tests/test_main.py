import pytest
from YandexPages import SearchHelper

@pytest.fixture
def yandex(driver):
    yandex = SearchHelper(driver)
    return yandex


@pytest.mark.usefixtures('driver')
class TestYandex:
    def test_yandex_page(self, yandex):
        yandex.go_to_site()

    def test_search_field(self, yandex):
        yandex.search_field(text='Тензор')

    def test_suggest(self, yandex):
        yandex.check_suggest()

    def test_search(self, yandex):
        yandex.submit()
        yandex.check_site(site='https://tensor.ru/')


@pytest.mark.usefixtures('driver')
class TestYandexImage:
    def test_yandex_image(self, yandex):
        yandex.go_to_site()

    def test_yandex_image_button(self, yandex):
        yandex.check_images_button()

    def test_url(self, yandex):
        yandex.switch_window()
        yandex.check_current_url()

    def test_categories_in_search_field(self, yandex):
        name_categories = str(yandex.save_name_categories()).lower()
        yandex.open_yandex_images_categories()
        yandex.check_text_search_field(name_categories)

    def test_open_image(self, yandex):
        yandex.open_first_image()
        yandex.test_check_open_image()

    def test_switch_image_next(self, yandex):
        down_src = str(yandex.save_src_first_image())
        yandex.switch_to_right_image()
        yandex.check_switch_image(down_src)

    def test_switch_image_down(self, yandex):
        yandex.switch_to_left_image()
        yandex.check_to_switch_first_image(yandex.save_src_first_image())
