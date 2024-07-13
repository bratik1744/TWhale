# myapp/management/commands/load_tickers.py
import csv
import os
from django.core.management.base import BaseCommand
from django.contrib.staticfiles import finders
from models import Ticker
import pandas as pd

class Command(BaseCommand):
    help = 'Load tickers from CSV file'

    def handle(self, *args, **kwargs):
        # Найдите путь к файлу CSV в директории static/data вашего приложения
        csv_path = finders.find('data/tickers.csv')

        if csv_path:
            with open(csv_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                ticker_descriptions = []
                ticker_names = []
                ticker_sectors = []
                for line in lines:
                    splited = line.split(';')
                    ticker_name = splited[0]
                    sector = splited[1]
                    description = ';'.join(splited[2:])
                    ticker_names.append(ticker_name)
                    ticker_sectors.append(sector)
                    ticker_descriptions.append(description)
                                                        #  sector=sector,
                                                        #  description=description

            print(len(ticker_names), len(ticker_sectors), len(ticker_descriptions))


            values = zip(ticker_sectors, ticker_descriptions)

            info = {}
            info_sec = {}
            info_des = {}
            for key, value in zip(ticker_names, values):
                info[key] = value
    
            for key, value in zip(ticker_names, ticker_sectors):
                info_sec[key] = value
    
            for key, value in zip(ticker_names, ticker_descriptions):
                info_des[key] = value
            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
            print(info_sec)
            for i in ticker_names:
                Ticker.objects.create(
                        name=i,
                        description=info_des[i],
                        sector=info_sec[i],
                )
        else:
            self.stdout.write(self.style.ERROR('CSV file not found'))