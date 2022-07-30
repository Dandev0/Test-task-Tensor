import time
from YandexPages import SearchHelper

def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.search(text='тензор')
    time.sleep(1)
    yandex_main_page.check_suggest()
    yandex_main_page.submit()
    time.sleep(1)
    yandex_main_page.check_site(site='https://tensor.ru/')



if __name__=='__main__':
    test_yandex_search()
