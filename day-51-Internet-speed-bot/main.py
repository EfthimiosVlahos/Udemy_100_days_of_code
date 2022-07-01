from selenium import webdriver
from bot import InternetSpeedTwitterBot

twit_bot=InternetSpeedTwitterBot()
twit_bot.get_internet_speed()
twit_bot.tweet_at_provider()


