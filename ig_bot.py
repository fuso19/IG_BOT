from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get('https://instagram.com')
        time.sleep(3)

        username = bot.find_element_by_xpath('//input[@name="username"]')
        password = bot.find_element_by_xpath('//input[@name="password"]')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        bot.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(4)

        # click Not Now Button
        bot.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()

    def like_photos(self, hashtag):
        bot = self.bot
        bot.get(
            'https://www.instagram.com/explore/tags/{hashtag}/'.format(hashtag=hashtag))

        time.sleep(5)

        # scroll da pagina
        for i in range(2):
            bot.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(3)

        hrefs = bot.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        print(pic_hrefs)
        print(type(pic_hrefs))
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            print(pic_href)
            if (pic_href.find('https://www.instagram.com/p/') != -1):
                bot.get(pic_href)
                time.sleep(3)
                try:
                    bot.find_element_by_class_name(
                        '//button[@class="wpO6b "').click()
                    time.sleep(20)
                    print('Like aplicado')
                except Exception:
                    time.sleep(5)
            else:
                print("Nâo é link de foto")

    def start_following(self, hashtag):
        bot = self.bot
        bot.get(
            'https://www.instagram.com/explore/tags/{hashtag}'.format(hashtag=hashtag))

        time.sleep(5)


coursew = InstaBot('galeria.brindel', 'Celia123!')
coursew.login()
coursew.like_photos('quadrossala')
'''
saladeestardecorada
decoracaodecasa
decoracao
'''
