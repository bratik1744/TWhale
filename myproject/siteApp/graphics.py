# import numpy as np
# import pandas as pd
# import apimoex
# from views import get_ell
# import matplotlib.pyplot as plt
# import mplfinance as mpf

# import requests

# def get_candles_data(ticker: str, interval: str, start_date=None, end_date=None) -> pd.DataFrame:
#     with requests.Session() as session:
#         data = apimoex.get_market_candles(session, security=ticker, interval=intervals[interval], start=start_date, end=end_date)
#     df = pd.DataFrame(data)
#     return df

# intervals = {'1m': 1, '10m': 10, '1h': 60, '1d': 24, '1w': 7, '1_month': 31, '1_quater': 4}
# elements = list(get_ell('data\\tickers.csv')[0].keys())
# for element in elements:
#     ticker_name = element
#     ticker = get_candles_data(ticker_name, '1d', '2024-06-11', '2024-07-11')

#     ticker['begin'] = pd.to_datetime(ticker['begin'])
#     ticker.set_index('begin', inplace=True)

#     my_style = mpf.make_mpf_style(
#         base_mpf_style='charles',
#         marketcolors=mpf.make_marketcolors(
#             up='#00FF7F',     # softer green for up candles
#             down='#FF6347',    # softer red for down candles
#             wick={'up': '#00FF7F', 'down': '#FF6347'},   # wicks matching candle colors
#             edge={'up': '#00FF7F', 'down': '#FF6347'},   # edges matching candle colors
#             volume='in'),  # in color for volume bars
#         facecolor='#131F2B',  # background color
#         edgecolor='white',
#         gridcolor='gray',
#         gridstyle='--',
#         figcolor='#131F2B',  # figure background color
#         rc={'axes.labelcolor': '#fec501', 'ytick.color': '#fec501', 'xtick.color': '#fec501', 'axes.titlecolor': '#fec501'}  # colors for labels and title
#     )

#     fig, ax = mpf.plot(ticker, type='candle', style=my_style, ylabel='Цена', volume=False, returnfig=True)
#     ax[0].set_title(f'График изменения цены акции {ticker_name}', color='#fec501')
#     plt.show()



import os
import sys


# Добавляем корневую директорию проекта в sys.path
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Инициализируем Django
# django.setup()
# import django
import numpy as np
import pandas as pd
import apimoex
# from views import get_ell  # Absolute import
import matplotlib.pyplot as plt
import mplfinance as mpf
import requests



def get_candles_data(ticker: str, interval: str, start_date=None, end_date=None) -> pd.DataFrame:
    with requests.Session() as session:
        data = apimoex.get_market_candles(session, security=ticker, interval=intervals[interval], start=start_date, end=end_date)
    df = pd.DataFrame(data)
    return df

intervals = {'1m': 1, '10m': 10, '1h': 60, '1d': 24, '1w': 7, '1_month': 31, '1_quater': 4}

# Create a directory for charts if it doesn't exist
# def grafs_dict(path):
#     os.makedirs('charts', exist_ok=True)


#     # Initialize dictionary to store chart file paths
#     chart_files = {}

#     # Fetch elements from the CSV file
#     elements = list(get_ell('data\\tickers.csv')[0].keys())

    # for element in elements:
ticker_name = "GAZP"
ticker = get_candles_data(ticker_name, '1d', '2024-04-12', '2024-07-12')
ticker['begin'] = pd.to_datetime(ticker['begin'])
ticker.set_index('begin', inplace=True)

my_style = mpf.make_mpf_style(
            base_mpf_style='charles',
            marketcolors=mpf.make_marketcolors(
                up='#00FF7F',     # softer green for up candles
                down='#FF6347',    # softer red for down candles
                wick={'up': '#00FF7F', 'down': '#FF6347'},   # wicks matching candle colors
                edge={'up': '#00FF7F', 'down': '#FF6347'},   # edges matching candle colors
                volume='in'),  # in color for volume bars
            facecolor='#131F2B',  # background color
            edgecolor='white',
            gridcolor='gray',
            gridstyle='--',
            figcolor='#131F2B',  # figure background color
            rc={'axes.labelcolor': '#fec501', 'ytick.color': '#fec501', 'xtick.color': '#fec501', 'axes.titlecolor': '#fec501'}  # colors for labels and title
        )

fig, ax = mpf.plot(ticker, type='candle', style=my_style, ylabel='Цена', volume=False, returnfig=True)
ax[0].set_title(f'График изменения цены акции {ticker_name}', color='#fec501')
        
        # Save the plot to a file
        # file_path = f'charts/{ticker_name}_candlestick_chart.png'
        # fig.savefig(file_path)
plt.show(fig)

        # Add the file path to the dictionary
    #     chart_files[ticker_name] = file_path
        
    # return chart_files