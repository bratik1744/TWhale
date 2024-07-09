import os
import sys
import json
import requests
import datetime
from tqdm import tqdm

import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

main_href = 'https://smart-lab.ru'

def make_href_for_date(date: str) -> str:
    """
        date in a format: 'yyyy-mm-dd'
    """
    return f'https://smart-lab.ru/news/date/{date}/'


def get_news_hrefs_and_title_for_specific_date(date: str):
    """
        date in a format: 'yyyy-mm-dd'
    """

    href = make_href_for_date(date)

    driver = webdriver.Safari()
    # browser.get(main_href)

    hrefs, titles = [], []

    try:
        # Открываем сайт
        driver.get(href)
        
        # Ждем, пока страница полностью загрузится
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

        # Получаем исходный код страницы
        page_source = driver.page_source

        # print(page_source)

        
        soup = BeautifulSoup(page_source, 'html.parser')

        inside_blocks = soup.find_all('div', class_='inside')

        # Проход по всем найденным блокам и извлечение ссылок и заголовков
        for block in inside_blocks:
            a_tag = block.find('a')
            if a_tag:
                href = a_tag['href']
                title = a_tag['title']
                hrefs.append(main_href + href)
                titles.append(title)

        return hrefs, titles

    finally:
        # Закрываем браузер
        driver.quit()


def collect_hrefs(start_date: str, end_date: str) -> str:
    """
        Arguments:
            start_date, str - a date to start from, in a format 'yyyy-mm-dd'
            end_date, str - a date to end at, in a format 'yyy-mm-dd'

        Returns:
            csv_path, str - a path to csv file data saved at
    """

    dates = pd.date_range(start=start_date, end=end_date)

    dates_list = []

    for date in tqdm(dates):

        _hrefs, _titles = get_news_hrefs_and_title_for_specific_date(date.date())

        hrefs += _hrefs
        titles += _titles
        dates_list += [date.date()]*len(_hrefs)

    df = pd.DataFrame({'date': dates_list,
                       'title': titles,
                       'href': hrefs})
    
    # print(df)
    
    df.to_csv('./news_smart_lab_hrefs.csv')
    
    return './news_smart_lab_hrefs.csv'


if __name__ == '__main__':

    hrefs, titles = [], []
    
    start_date = '2022-05-01'
    # end_date = '2022-05-10'
    end_date = '2024-07-02'

    dates = pd.date_range(start=start_date, end=end_date)

    df_path = collect_hrefs(start_date, end_date)
    