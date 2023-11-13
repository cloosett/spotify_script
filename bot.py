import datetime
import os
import threading
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, SessionNotCreatedException
from selenium.webdriver.common.by import By
import random
import string
import concurrent.futures
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import zipfile
import telebot
from telebot import types
from datetime import datetime
from moviepy.editor import *
import speech_recognition as sr
import wget
import multiprocessing


TOKEN = 'your token'


bot = telebot.TeleBot(TOKEN)


# МЕНЮ СТАРТ
@bot.message_handler(commands=['start'])
def send_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton("Авторегер✅")
    item2 = types.KeyboardButton("Инвайтер💪")
    item3 = types.KeyboardButton("Чекер👀")
    item4 = types.KeyboardButton("Профиль👨‍💻")
    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Оберите опцию:", reply_markup=markup)
############################


# МЕНЮ Назад🔙
@bot.message_handler(func=lambda message: message.text == "Назад🔙")
def return_menu_nazad(message):
    global otmena_register
    global otmena_invite
    global otmena_cheker
    otmena_register = True
    otmena_invite = True
    otmena_cheker = True
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton("Авторегер✅")
    item2 = types.KeyboardButton("Инвайтер💪")
    item3 = types.KeyboardButton("Чекер👀")
    item4 = types.KeyboardButton("Профиль👨‍💻")
    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Оберите опцию:", reply_markup=markup)


##################################################
# МЕНЮ ПРОФИЛЯ
@bot.message_handler(func=lambda message: message.text == "Профиль👨‍💻")
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Настройка прокси🚨")
    btn3 = types.KeyboardButton("Выгрузить файл valid_register")
    markup.row(btn1,btn3)
    btn4 = types.KeyboardButton("Выгрузить файл silki")
    btn6 = types.KeyboardButton("Выключить messages ERROR")
    markup.row(btn4,btn6)
    btn7 = types.KeyboardButton("Назад🔙")
    markup.row(btn7)

    bot.send_message(message.chat.id, "Оберите опцию:", reply_markup=markup)
######################################

@bot.message_handler(func=lambda message: message.text == "Отмена🆘")
def return_menu(message):
    global otmena_register
    global otmena_invite
    global otmena_cheker
    otmena_register = True
    otmena_invite = True
    otmena_cheker = True

    try:
        path_to_valid_register_now = 'valid_register_now.txt'
        with open(path_to_valid_register_now, 'rb') as document_file:
            bot.send_document(message.chat.id, document_file)
        os.remove(path_to_valid_register_now)
    except Exception as e:
        try:
            path_to_valid_invited_now = 'invited_account_now.txt'
            with open(path_to_valid_invited_now, 'rb') as document_file:
                bot.send_document(message.chat.id, document_file)
            os.remove(path_to_valid_invited_now)
        except Exception as e:
            try:
                path_to_checkedfile = 'checked_accounts_now.txt'
                with open(path_to_checkedfile, 'rb') as document_file:
                    bot.send_document(message.chat.id, document_file)
                os.remove(path_to_checkedfile)
            except Exception as e:
                bot.send_message(message.chat.id, 'Всі файли пусті або не можуть бути відправлені')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton("Авторегер✅")
    item2 = types.KeyboardButton("Инвайтер💪")
    item3 = types.KeyboardButton("Чекер👀")
    item4 = types.KeyboardButton("Профиль👨‍💻")
    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Операция окончена, ожидайте проходит последный цикл.", reply_markup=markup)

##########################################################

# Настройка прокси🚨
@bot.message_handler(func=lambda message: message.text == "Настройка прокси🚨")
def add_proxy(message):
    bot.send_message(message.chat.id, "Введите прокси в формате: user:password:host:port")
    bot.register_next_step_handler(message, process_proxy)
def process_proxy(message):
    if message.text == 'Назад🔙':
        return_menu_nazad(message)
    else:
        save_proxy(message)

def save_proxy(message):
    proxy_data = message.text
    with open('proxy.txt', 'w', encoding='utf-8') as proxy_file:
        proxy_file.write(proxy_data + '\n')
    bot.send_message(message.chat.id, "Прокси успешно добавлены!")
######################################



# Общая статистика🤔
@bot.message_handler(func=lambda message: message.text == "Общая статистика🤔")
def total_statics(message):
    file_path = "total_statistic.txt"

    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('Данные авторег: VALID:0 ; INVALID:0\n')
            file.write('Данные Инвайтера: VALID:0 ; INVALID:0\n')
            file.write('Данные Чекера: VALID:0 ; INVALID:0')
    else:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            bot.send_message(message.chat.id, file_content)

###########################################################################################################################



@bot.message_handler(func=lambda message: message.text == "Выгрузить файл valid_register")
def file_register(message):
    path_to_valid_register = 'valid_register.txt'
    with open(path_to_valid_register, 'rb') as document_file:
        bot.send_document(message.chat.id, document_file)
    os.remove('valid_register.txt')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад🔙')
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Ваш файл valid_register, был успешно выгружен', reply_markup=markup)




@bot.message_handler(func=lambda message: message.text == "Выгрузить файл silki")
def file_register(message):
    path_to_valid_silki = 'silki.txt'
    with open(path_to_valid_silki, 'rb') as document_file:
        bot.send_document(message.chat.id, document_file)
    os.remove('silki.txt')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад🔙')
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Ваш файл silki, был успешно выгружен', reply_markup=markup)
###################################################################################



######################################################################################


@bot.message_handler(func=lambda message: message.text == "Выключить messages ERROR")
def off_error(message):
    global message_errors_off
    message_errors_off = True
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад🔙')
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Сообщение успешно выключены', reply_markup=markup)


###########################################################################################






# Авторегер✅
@bot.message_handler(func=lambda message: message.text == "Авторегер✅")
def option_selected(message):
    valid_register_now_file_path = 'valid_register_now.txt'


    if os.path.exists(valid_register_now_file_path):
        os.remove(valid_register_now_file_path)


    with open(valid_register_now_file_path, 'a', encoding='utf-8') as file:
        pass
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Назад🔙")
    markup.add(button1)
    bot.send_message(message.chat.id, "Количество аккаунтов:", reply_markup=markup)
    bot.register_next_step_handler(message, process_option)


def process_option(message):
    if message.text == 'Назад🔙':
        return_menu_nazad(message)
    else:
        option_one(message)

def option_one(message):
    global count_valid_register
    global count_invalid_register
    count_valid_register = 0
    count_invalid_register = 0
    global otmena_register
    otmena_register = False




    with open('proxy.txt', 'r') as proxy_file:
        proxy_lines = proxy_file.readlines()

    with open('background.js', 'r') as background_file:
        background_js = background_file.read()

    with open('manifest.json', 'r') as manifest_file:
        manifest_json = manifest_file.read()

    def generate_password(length=20):
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def generate_email(username_length=18, domain="gmail.com"):
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))
        email = f"{username}@{domain}"
        return email

    def generate_username(length=15):
        characters = string.ascii_letters + string.digits
        username = ''.join(random.choice(characters) for _ in range(length))
        return username

    def register_spotify(account_number, proxy_line):
        current_time = int(time.time())
        audio_file_name = f'audio_{current_time}.mp3'
        global count_valid_register
        global count_invalid_register
        global otmena_register
        global message_errors_off

        if otmena_register:
            return

        url = 'https://www.spotify.com/tr-tr/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F'

        options = webdriver.ChromeOptions()

        PROXY_USER, PROXY_PASS, PROXY_HOST, PROXY_PORT = proxy_line.strip().split(':')


        plugin_file = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(plugin_file, 'w') as zp:
            zp.writestr('manifest.json', manifest_json)
            zp.writestr('background.js', background_js % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS))

        options.add_extension(plugin_file)
        # options.add_argument("--headless")
        options.add_argument(f'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36')
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        # ФУНКЦИИ
        def register_logins():

            time.sleep(1)
            email_input1 = driver.find_element(By.XPATH, '//*[@id="username"]')
            email_input1.send_keys(random_email)
            time.sleep(2)
            next_button_emails = driver.find_element(By.XPATH, '//*[@id="__next"]/main/main/section/div/div/form/button/span[1]')
            next_button_emails.click()
            time.sleep(2)
            password_input = driver.find_element(By.XPATH, '//*[@id="new-password"]')
            password_input.send_keys(random_password)

            time.sleep(2)
            next_button_password = driver.find_element(By.XPATH,
                                                       '//*[@id="__next"]/main/main/section/div/div/section/form/div[2]/button/span[1]')
            next_button_password.click()
            time.sleep(2)
            username_input = driver.find_element(By.XPATH, '//*[@id="displayName"]')
            username_input.send_keys(random_username)

            # Input birthday, choice stat
            day_input = driver.find_element(By.XPATH, '//*[@id="day"]')
            day_input.send_keys("15")
            time.sleep(1)
            month_option = driver.find_element(By.XPATH, '//*[@id="month"]/option[2]')
            month_option.click()
            time.sleep(1)

            year_input = driver.find_element(By.XPATH, '//*[@id="year"]')
            year_input.send_keys("1999")
            time.sleep(1)
            stat_checkbox = driver.find_element(By.XPATH,
                                                '//*[@id="__next"]/main/main/section/div/div/section/form/div[1]/section/div[3]/fieldset/div/div/div[1]/label/span[2]')
            stat_checkbox.click()

            time.sleep(1)
            submit_button1 = driver.find_element(By.XPATH,
                                                 '//*[@id="__next"]/main/main/section/div/div/section/form/div[2]/button/span[1]')
            submit_button1.click()
            time.sleep(2)
            submit_button2 = driver.find_element(By.XPATH,
                                                 '//*[@id="__next"]/main/main/section/div/div/section/form/div[2]/button/span[1]')
            submit_button2.click()
            time.sleep(15)







        try:
            random_email = generate_email()
            random_password = generate_password()
            random_username = generate_username()
            try:
                try:
                    close_cookie = driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')
                    close_cookie.click()
                except Exception as e:
                    register_logins()
            except Exception as e:
                try:
                    close_cookie2 = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
                    close_cookie2.click()
                except Exception as e:
                    register_logins()
            if driver.current_url == 'https://open.spotify.com/':
                registrationesa_data = f"{random_email}:{random_password}\n"
                with open('valid_register_now.txt', 'a', encoding='utf-8') as file:
                    file.write(registrationesa_data)

                with open('valid_register.txt', 'a', encoding='utf-8') as file:
                    file.write(registrationesa_data)
                bot.send_message(message.chat.id, f'[CREATED] {random_email}:{random_password}')
                count_valid_register += 1
                driver.quit()
            else:
                captcha_iframe = driver.find_element(By.XPATH,
                                                     '//*[@id="encore-web-main-content"]/div/div/div/div/div/div/div[1]/div/div/div/iframe')
                driver.switch_to.frame(captcha_iframe)
                captcha_checkbox = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')
                captcha_checkbox.click()
                time.sleep(3)
                driver.switch_to.default_content()
                try:
                    submit_captchas = driver.find_element(By.XPATH,
                                                          '//*[@id="encore-web-main-content"]/div/div/div/div/div/div/button/span[1]')
                    submit_captchas.click()
                    time.sleep(5)
                    if driver.current_url == 'https://open.spotify.com/':
                        bot.send_message(message.chat.id, f'[CREATED] {random_email}:{random_password}')
                        registration_data = f"{random_email}:{random_password}\n"

                        with open('valid_register_now.txt', 'a', encoding='utf-8') as file:
                            file.write(registration_data)

                        # Enter in Valid Data
                        with open('valid_register.txt', 'a', encoding='utf-8') as file:
                            file.write(registration_data)
                        count_valid_register += 1
                        time.sleep(1)
                        driver.quit()
                    else:
                        random_email = generate_email()
                        random_password = generate_password()
                        registration_data = f"{random_email}:{random_password}\n"
                        with open('notvalid_register.txt', 'a', encoding='utf-8') as file:
                            file.write(registration_data)

                except Exception as e:
                    captcha_iframe_audio = driver.find_element(By.XPATH,
                                                               '/html/body/div[2]/div[4]/iframe')
                    driver.switch_to.frame(captcha_iframe_audio)
                    captcha_audio = driver.find_element(By.XPATH, '//*[@id="recaptcha-audio-button"]').click()
                    time.sleep(3)
                    captcha_download_audio = driver.find_element(By.XPATH, '//*[@id="rc-audio"]/div[7]/a').click()
                    time.sleep(2)
                    driver.switch_to.window(driver.window_handles[1])
                    time.sleep(1)
                    url = driver.current_url
                    wget.download(url, audio_file_name)
                    time.sleep(2)

                    mp3_audio_file = audio_file_name
                    audio = AudioFileClip(mp3_audio_file)

                    wav_audio_file = "audio.wav"
                    audio.write_audiofile(wav_audio_file)
                    time.sleep(2)

                    recognizer = sr.Recognizer()

                    audio_file = "audio.wav"
                    with sr.AudioFile(audio_file) as source:

                        audio = recognizer.listen(source)

                        try:
                            text = recognizer.recognize_google(audio, language="en-US")
                            time.sleep(2)
                            driver.switch_to.window(driver.window_handles[0])
                            driver.switch_to.frame(captcha_iframe_audio)
                            time.sleep(1)
                            input_audio = driver.find_element(By.XPATH, '//*[@id="audio-response"]').send_keys(text)
                            time.sleep(3)
                            submit_captchas_audio = driver.find_element(By.XPATH,
                                                                        '//*[@id="recaptcha-verify-button"]').click()
                            driver.switch_to.default_content()
                            submit_captchas_audio_finall = driver.find_element(By.XPATH,
                                                                               '//*[@id="encore-web-main-content"]/div/div/div/div/div/div/button/span[1]').click()
                            time.sleep(5)
                            if driver.current_url == 'https://open.spotify.com/':
                                bot.send_message(message.chat.id, f'[CREATED] {random_email}:{random_password}')
                                registration_data = f"{random_email}:{random_password}\n"

                                with open('valid_register_now.txt', 'a', encoding='utf-8') as file:
                                    file.write(registration_data)

                                # Enter in Valid Data
                                with open('valid_register.txt', 'a', encoding='utf-8') as file:
                                    file.write(registration_data)
                                count_valid_register += 1
                                time.sleep(1)
                                driver.quit()
                            os.remove(audio_file_name)
                        except sr.UnknownValueError:
                            bot.send_message(message.chat.id,
                                'Невозможно розпознать')
                            os.remove(audio_file_name)

                        except sr.RequestError as e:
                            bot.send_message(message.chat.id,
                                "Ошибка запиту к серверу Google Web Speech API; {0}".format(e))
                            os.remove(audio_file_name)
            driver.quit()

        except Exception as e:
            if not message_errors_off:
                random_email = generate_email()
                random_password = generate_password()
                registration_data = f"{random_email}:{random_password}\n"
                count_invalid_register += 1
                with open('notvalid_register.txt', 'a', encoding='utf-8') as file:
                    file.write(registration_data)
                bot.send_message(message.chat.id,
                                 f'[ERROR] {random_email}:{random_password} | {e}')
                os.remove(audio_file_name)
            else:
                random_email = generate_email()
                random_password = generate_password()
                registration_data = f"{random_email}:{random_password}\n"
                with open('notvalid_register.txt', 'a', encoding='utf-8') as file:
                    file.write(registration_data)
                os.remove(audio_file_name)

    num_accounts = int(message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Отмена🆘")
    button2 = types.KeyboardButton("Назад🔙")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, 'Работа авторегера началась✅', reply_markup=markup)
    num_threads = 2
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for account_number in range(1, num_accounts + 1):
            current_proxy_line = proxy_lines[account_number - 1]
            executor.submit(register_spotify, account_number, current_proxy_line)

    path_to_valid_register = 'valid_register.txt'
    path_to_valid_register_now = 'valid_register_now.txt'


    # Отправляем документ
    with open(path_to_valid_register, 'rb') as document_file:
        bot.send_document(message.chat.id, document_file)

    with open(path_to_valid_register_now, 'rb') as document_file:
        bot.send_document(message.chat.id, document_file)
    os.remove(path_to_valid_register_now)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Назад🔙")
    markup.add(button1)
    bot.send_message(message.chat.id, 'Регистрация закончилась🔴', reply_markup=markup)
    bot.send_message(message.chat.id, f'Statistic: VALID:{count_valid_register}; INVALID:{count_invalid_register}')

################################################################################################################






# Инвайтер💪

@bot.message_handler(func=lambda message: message.text == "Инвайтер💪")
def account_validfile(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Назад🔙")
    markup.add(button1)
    bot.send_message(message.chat.id, 'Загрузите файл valid_register.txt', reply_markup=markup)
    bot.register_next_step_handler(message, process_option_inviter)

def process_option_inviter(message):
    if message.text == 'Назад🔙':
        return_menu_nazad(message)
    else:
        handle_valid_file(message)

def handle_valid_file(message):
    if message.content_type == 'document':
        file_info = message.document
        file_name = file_info.file_name

        if file_name != "valid_register.txt":
            bot.send_message(message.chat.id, "Название файла должно быть valid_register.txt!")
            return

        file_id = file_info.file_id
        file = bot.get_file(file_id)
        downloaded_file = bot.download_file(file.file_path)
        new_file_name = "valid_register.txt"

        with open(new_file_name, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.send_message(message.chat.id, 'Файл добавлен✅')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Назад🔙")
        markup.add(button1)
        bot.send_message(message.chat.id, 'Загрузите файл silki.txt', reply_markup=markup)
        bot.register_next_step_handler(message, process_option_inviter1)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, отправьте файл valid_register.txt!")

def process_option_inviter1(message):
    if message.text == 'Назад🔙':
        return_menu_nazad(message)
    else:
        handle_silki_file(message)

def handle_silki_file(message):
    if message.content_type == 'document':
        file_info = message.document
        file_name = file_info.file_name

        if file_name != "silki.txt":
            bot.send_message(message.chat.id, "Название файла должно быть silki.txt!")
            return

        file_id = file_info.file_id
        file = bot.get_file(file_id)
        downloaded_file = bot.download_file(file.file_path)
        new_file_name = "silki.txt"

        with open(new_file_name, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.send_message(message.chat.id, 'Файл добавлен✅')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Назад🔙")
        markup.add(button1)
        bot.send_message(message.chat.id, "Кол-во аккаунтов инвайтнуть:", reply_markup=markup)
        bot.register_next_step_handler(message, process_option_inviter2)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, отправьте файл silki.txt!")

def process_option_inviter2(message):
    if message.text == 'Назад🔙':
        return_menu_nazad(message)
    else:
        option_two(message)

def option_two(message):
    with open('invited_account_now.txt', 'a') as file:
        pass
    global count_valid
    global count_invalid
    global otmena_invite
    otmena_invite = False
    count_valid = 0
    count_invalid = 0

    with open('background.js', 'r') as background_file:
        background_js = background_file.read()


    with open('manifest.json', 'r') as manifest_file:
        manifest_json = manifest_file.read()



    def invite(account_number, proxy_lines, silka, data_list, email, password):
        current_time = time.time()
        audio_file_name = f'audio.{current_time}'
        url = 'https://accounts.spotify.com/uk/login?continue=https%3A%2F%2Fwww.spotify.com%2Faccount%2Foverview%2F&_locale=tr-TR'
        with open('invited_account_now.txt', 'a') as file:
            pass
        global count_valid
        global count_invalid
        global otmena_invite

        if otmena_invite:
            return
        options = webdriver.ChromeOptions()
        PROXY_USER, PROXY_PASS, PROXY_HOST, PROXY_PORT = proxy_lines.strip().split(':')


        plugin_file = 'proxy_auth_plugin.zip'
        with zipfile.ZipFile(plugin_file, 'w') as zp:
            zp.writestr('manifest.json', manifest_json)
            zp.writestr('background.js', background_js % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS))

        options.add_extension(plugin_file)
        ua = UserAgent()
        user_agent = ua.random
        options.add_argument("--disable-gpu")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument(f'user-agent={user_agent}')
        driver = webdriver.Chrome(options=options)
        driver.get(url)



        # # ФУНКЦИИ
        def cookie():
            try:
                close_cookie = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
                close_cookie.click()
            except Exception as e:
                close_cookie2 = driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')
                close_cookie2.click()




        def confirm_family(cookie):
            driver.get(silka)
            time.sleep(8)

            silka_button = driver.find_element(By.XPATH,
                                               '//*[@id="__next"]/main/div/section[1]/div/header/a/span[1]').click()
            time.sleep(4)
            confirmurl_button = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/a[1]/span[1]').click()
            time.sleep(8)
            cookie()
            input_emailing = driver.find_element(By.XPATH, '//*[@id="address"]')
            input_emailing.send_keys('hurma mah.36.cad.c blk.kandilli sit.no.46 D.17 KONYAALTI ANTALYA TURKEY')
            confirm_adrressa = driver.find_element(By.XPATH, '//*[@id="__next"]/form/main/div/fieldset/div/button/span[1]')
            confirm_adrressa.click()
            time.sleep(4)
            finall = driver.find_element(By.XPATH, '//*[@id="confirm-address-dialog"]/footer/button[2]/span[1]')
            finall.click()
            time.sleep(10)



        def login():
            wait = WebDriverWait(driver, 10)
            email_input = wait.until(EC.presence_of_element_located((By.ID, 'login-username')))
            email_input.clear()
            email_input.send_keys(email)

            password_input = wait.until(EC.presence_of_element_located((By.ID, 'login-password')))
            password_input.send_keys(password)

            login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]/span[1]')))
            login_button.click()
            time.sleep(14)

        check_url_login = 'https://www.spotify.com/tr-tr/account/overview/?flow_ctx=5233ae06-5569-442b-ae9e-00cc045dcf4f%3A1697849122'
        split_url = check_url_login.split('?')
        ready_url = split_url[0]



        login()
        try:
            captcha_iframe = driver.find_element(By.XPATH,
                                                 '//*[@id="encore-web-main-content"]/div/div/div/div/div/div/div[1]/div/div/div/iframe')
            driver.switch_to.frame(captcha_iframe)
            captcha_checkbox = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')
            captcha_checkbox.click()
            time.sleep(6)
            driver.switch_to.default_content()
            try:
                submit_captchas = driver.find_element(By.XPATH,
                                                      '//*[@id="encore-web-main-content"]/div/div/div/div/div/div/button/span[1]')
                submit_captchas.click()
                time.sleep(10)
                try:
                    confirm_family(cookie)
                    inviter_data = f"{email}:{password}\n"

                    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                    filename = f"invited_{current_datetime}.txt"
                    count_valid += 1

                    valid_folder = "valid"

                    file_path = os.path.join(valid_folder, filename)
                    with open('invited_account_now.txt', 'a', encoding='utf-8') as files:
                        files.write(inviter_data)

                    with open(file_path, 'a', encoding='utf-8') as file:
                        file.write(inviter_data)
                    bot.send_message(message.chat.id, f'[INVITED] {email}:{password}')
                    driver.delete_all_cookies()
                except Exception as e:
                    invitere_novalid_data = f"{email}:{password}\n"

                    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                    filename = f"noinvited_{current_datetime}.txt"
                    count_invalid += 1

                    valid_folder = "no_valid"

                    file_path = os.path.join(valid_folder, filename)
                    # Enter in Invalid Data

                    with open(file_path, 'a', encoding='utf-8') as file:
                        file.write(invitere_novalid_data)
                    bot.send_message(message.chat.id, f'[ERROR] {email}:{password} | Error inviter')
                    driver.delete_all_cookies()

            except Exception as e:
                captcha_iframe_audio = driver.find_element(By.XPATH,
                                                           '/html/body/div[2]/div[4]/iframe')
                driver.switch_to.frame(captcha_iframe_audio)
                captcha_audio = driver.find_element(By.XPATH, '//*[@id="recaptcha-audio-button"]').click()
                time.sleep(5)
                captcha_download_audio = driver.find_element(By.XPATH, '//*[@id="rc-audio"]/div[7]/a').click()
                time.sleep(4)
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(2)
                url = driver.current_url
                wget.download(url, audio_file_name)
                time.sleep(4)

                mp3_audio_file = audio_file_name
                audio = AudioFileClip(mp3_audio_file)

                wav_audio_file = "audio.wav"
                audio.write_audiofile(wav_audio_file)
                time.sleep(4)

                recognizer = sr.Recognizer()

                audio_file = "audio.wav"
                with sr.AudioFile(audio_file) as source:

                    audio = recognizer.listen(source)

                    try:
                        text = recognizer.recognize_google(audio, language="en-US")
                        time.sleep(4)
                        driver.switch_to.window(driver.window_handles[0])
                        driver.switch_to.frame(captcha_iframe_audio)
                        time.sleep(2)
                        input_audio = driver.find_element(By.XPATH, '//*[@id="audio-response"]').send_keys(text)
                        time.sleep(6)
                        submit_captchas_audio = driver.find_element(By.XPATH,
                                                                    '//*[@id="recaptcha-verify-button"]').click()
                        driver.switch_to.default_content()
                        submit_captchas_audio_finall = driver.find_element(By.XPATH,
                                                                           '//*[@id="encore-web-main-content"]/div/div/div/div/div/div/button/span[1]').click()
                        time.sleep(10)
                        os.remove(audio_file_name)
                        try:
                            confirm_family(cookie)
                            inviter_data = f"{email}:{password}\n"

                            current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                            filename = f"invited_{current_datetime}.txt"
                            count_valid += 1

                            valid_folder = "valid"

                            file_path = os.path.join(valid_folder, filename)
                            with open('invited_account_now.txt', 'a', encoding='utf-8') as files:
                                files.write(inviter_data)

                            with open(file_path, 'a', encoding='utf-8') as file:
                                file.write(inviter_data)
                            bot.send_message(message.chat.id, f'[INVITED] {email}:{password}')
                            driver.delete_all_cookies()
                        except Exception as e:
                            invitere_novalid_data = f"{email}:{password}\n"

                            current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                            filename = f"noinvited_{current_datetime}.txt"
                            count_invalid += 1

                            valid_folder = "no_valid"

                            file_path = os.path.join(valid_folder, filename)
                            # Enter in Invalid Data

                            with open(file_path, 'a', encoding='utf-8') as file:
                                file.write(invitere_novalid_data)
                            bot.send_message(message.chat.id, f'[ERROR] {email}:{password} | Error inviter')
                            driver.delete_all_cookies()

                    except sr.RequestError as e:
                        bot.send_message(message.chat.id,
                                         "Ошибка запиту к серверу Google Web Speech API; {0}".format(e))
                        os.remove(audio_file_name)
        except Exception as e:
            if ready_url in driver.current_url:
                try:
                    confirm_family(cookie)
                    inviter_data = f"{email}:{password}\n"

                    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                    filename = f"invited_{current_datetime}.txt"
                    count_valid += 1

                    valid_folder = "valid"

                    file_path = os.path.join(valid_folder, filename)
                    with open('invited_account_now.txt', 'a', encoding='utf-8') as files:
                        files.write(inviter_data)

                    with open(file_path, 'a', encoding='utf-8') as file:
                        file.write(inviter_data)
                    bot.send_message(message.chat.id, f'[INVITED] {email}:{password}')
                    driver.delete_all_cookies()
                except Exception as e:
                    invitere_novalid_data = f"{email}:{password}\n"

                    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                    filename = f"noinvited_{current_datetime}.txt"
                    count_invalid += 1

                    valid_folder = "no_valid"

                    file_path = os.path.join(valid_folder, filename)
                    # Enter in Invalid Data

                    with open(file_path, 'a', encoding='utf-8') as file:
                        file.write(invitere_novalid_data)
                    bot.send_message(message.chat.id, f'[ERROR] {email}:{password} | Error inviter')
                    driver.delete_all_cookies()
            else:
                invitere_novalid_data = f"{email}:{password}\n"

                current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                filename = f"noinvited_{current_datetime}.txt"
                count_invalid += 1

                valid_folder = "no_valid"

                file_path = os.path.join(valid_folder, filename)
                # Enter in Invalid Data

                with open(file_path, 'a', encoding='utf-8') as file:
                    file.write(invitere_novalid_data)
                bot.send_message(message.chat.id, f'[ERROR] {email}:{password} | Invalid account')
                driver.delete_all_cookies()



    with open('valid_register.txt', 'r', encoding='utf-8') as file:
        data_list = [line.strip().split(':', 1) for line in file.readlines()]

    with open('silki.txt', 'r', encoding='utf-8') as file:
        silka_list = file.readlines()


    with open('proxy.txt', 'r') as proxy_file:
        proxy_lines = proxy_file.readlines()

    num_accounts = int(message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Отмена🆘")
    button2 = types.KeyboardButton("Назад🔙")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, 'Работа инвайтера началась✅', reply_markup=markup)
    num_threads = 2

    # Create a ThreadPoolExecutor with a maximum of num_threads threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for account_number in range(1, num_accounts + 1):
            if account_number <= len(data_list) and account_number <= len(silka_list) and account_number <= len(
                    proxy_lines):
                email, password = data_list[account_number - 1]
                silka = silka_list[account_number - 1].strip()
                current_proxy_line = proxy_lines[account_number - 1]  # Get the proxy for the current account


                executor.submit(invite, account_number, current_proxy_line, silka, data_list, email, password)


    bot.send_message(message.chat.id,f'Statistic: VALID:{count_valid}; INVALID:{count_invalid}')
    path_to_invitedfile = 'invited_account_now.txt'
    # Отправляем документ
    with open(path_to_invitedfile, 'rb') as document_file:
        bot.send_document(message.chat.id, document_file)
    os.remove('invited_account_now.txt')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Назад🔙")
    markup.add(button1)
    bot.send_message(message.chat.id, 'Инвайтер закончил свою работу🔴', reply_markup=markup)
#########################################################################################












# Чекер👀
@bot.message_handler(func=lambda message: message.text == "Чекер👀")
def option_three(message):
    with open('checked_accounts_now.txt', 'a', encoding='utf-8') as files:
        pass
    global count_valid
    global count_invalid
    global otmena_cheker
    otmena_cheker = False
    count_valid = 0
    count_invalid = 0



    with open('proxy.txt', 'r') as proxy_file:
        proxy_lines = proxy_file.readlines()

    with open('background.js', 'r') as background_file:
        background_js = background_file.read()

    with open('manifest.json', 'r') as manifest_file:
        manifest_json = manifest_file.read()

    MAX_THREADS = 2
    COMBO_PATH = 'valid_register.txt'

    url = 'https://accounts.spotify.com/tr/login'



    def check_account(account, proxy_line):
        global count_valid
        global count_invalid
        global otmena_cheker

        if otmena_cheker:
            return
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        PROXY_USER, PROXY_PASS, PROXY_HOST, PROXY_PORT = proxy_line.strip().split(':')

        plugin_file = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(plugin_file, 'w') as zp:
            zp.writestr('manifest.json', manifest_json)
            zp.writestr('background.js', background_js % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS))

        options.add_extension(plugin_file)

        driver = webdriver.Chrome(options=options)
        driver.get(url)
        driver.implicitly_wait(30)
        email, password = account.split(':')

        try:
            driver.find_element(By.CSS_SELECTOR, '#login-username').send_keys(email)
            driver.find_element(By.CSS_SELECTOR, '#login-password').send_keys(password)
            driver.find_element(By.CSS_SELECTOR, '#login-button').click()

            time.sleep(10)
            if driver.current_url == "https://accounts.spotify.com/tr/status":
                driver.find_element(By.XPATH, '//*[@id="account-settings-link"]/span[1]/span').click()
                driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button').click()
                driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div[2]/div/div[1]/div').click()
                time.sleep(5)
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                check_podpiska = soup.find('span',class_='Type__TypeElement-sc-goli3j-0 gyivyS sc-5bfc67eb-3 kEVIue').text
                srok = soup.find('b', class_='recurring-date')
                if srok is not None:
                    cheker_data = f"{email}:{password}\n"
                    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M")
                    filename = f"cheked_{current_datetime}.txt"
                    count_valid += 1
                    valid_folder = "valid"
                    file_path = os.path.join(valid_folder, filename)


                    with open('checked_accounts_now.txt', 'a', encoding='utf-8') as files:
                        files.write(cheker_data)

                    with open(file_path, 'a', encoding='utf-8') as file:
                        file.write(cheker_data)


                    srok_text = srok.text
                    bot.send_message(message.chat.id, f'[VALID] {email}:{password} | {check_podpiska} | {srok_text}')
                elif check_podpiska in ['Spotify Free', 'Ücretsiz Spotify']:
                    chekereseq_data = f"{email}:{password}\n"
                    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M")
                    filename = f"cheked_{current_datetime}.txt"
                    valid_folder = "valid"
                    file_path = os.path.join(valid_folder, filename)

                    with open('checked_accounts_now.txt', 'a', encoding='utf-8') as files:
                        files.write(chekereseq_data)


                    with open(file_path, 'a', encoding='utf-8') as file:
                        file.write(chekereseq_data)


                    count_valid += 1
                    bot.send_message(message.chat.id, f'[NO PREMIUM] {email}:{password}')
                else:
                    chekere_data = f"{email}:{password}\n"
                    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M")
                    filename = f"cheked_{current_datetime}.txt"
                    valid_folder = "valid"
                    count_valid += 1
                    file_path = os.path.join(valid_folder, filename)


                    with open('checked_accounts_now.txt', 'a', encoding='utf-8') as files:
                        files.write(chekere_data)


                    with open(file_path, 'a', encoding='utf-8') as file:
                        file.write(chekere_data)



                    bot.send_message(message.chat.id, f'[VALID] {email}:{password} | {check_podpiska} ')
            else:
                bot.send_message(message.chat.id, '[INVALID] Невірні дані')
        except Exception as e:
            cheker_novalides_data = f"{email}:{password}\n"
            current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M")
            filename = f"nocheked_{current_datetime}.txt"
            valid_folder = "no_valid"
            count_invalid += 1
            file_path = os.path.join(valid_folder, filename)
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(cheker_novalides_data)
            bot.send_message(message.chat.id, f'[INVALID] {email}:{password} | {e}')
        finally:
            driver.quit()

    with open(COMBO_PATH, 'r') as file:
        accounts = file.read().split('\n')
        accounts = [account for account in accounts if account.strip()]

    if not accounts:
        bot.send_message(message.chat.id, 'Немає аккаунтів для перевірки. Програма завершує роботу.')
        return

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Отмена🆘")
    button2 = types.KeyboardButton("Назад🔙")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, 'Чекер начал свою работу🟢', reply_markup=markup)


    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        processed_accounts = set()
        for current_proxy_line in proxy_lines:
            for account in accounts:
                if account not in processed_accounts:
                    executor.submit(check_account, account, current_proxy_line)
                    processed_accounts.add(account)


    path_to_checkedfile = 'checked_accounts_now.txt'

    with open(path_to_checkedfile, 'rb') as document_file:
        bot.send_document(message.chat.id, document_file)
    os.remove('checked_accounts_now.txt')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Назад🔙")
    markup.add(button1)
    bot.send_message(message.chat.id, 'Чекер окончил свою работу🔴', reply_markup=markup)
    bot.send_message(message.chat.id, f'STATICTIC: VALID:{count_valid}, INVALID: {count_invalid}')
######################################################################################################################################


bot.polling(none_stop=True)
