# spotify_script
EN:
The script that registers accounts in Spotify, invites to the family, and at the end checks if everything is OK, this is all done in the Telegram bot, and successful accounts are stored in the valid_register.txt file. More in README.

UA:
Скрипт який реєструє аккаунти в спотіфай, запрошує в сім'ю , і вкінці провіряє чи все гаразд, це все зроблено в телеграм боті, і  успішні аккаунти зберігаються в файлі valid_register.txt.


    Авторегер,инвайтер,чекер
Це Telegram бот, який дозволяє автоматизувати процес реєстрації,запрошення в сім'ю, і провірку аккаунтів на Spotify. Бот використовує багатопотоковий підхід для швидкої та ефективної обробки багатьох акаунтів одночасно.

    Використання
Запуск бота: Після запуску бота виберіть любу опцію для розпочатку процесу автоматичної реєстрації.

    Рекомендації
Спочатку рекомендується створити аккаунти, після створення вони добавлять в файл "valid_register.txt", після чого аккаунти будуть братись з цього файлу, і ви зможете їх запрошувати в сім'ю , або провіряти.
Введення кількості аккаунтів: Оберіть кількість аккаунтів, які ви хочете зареєструвати. Бот розпочне автоматичний процес реєстрації для вказаної кількості облікових записів.

    Статистика та результат: 
Після завершення процесу реєстрації, бот надішле статистику успішно зареєстрованих та невалідних акаунтів. Також, ви отримаєте файли зі списками успішно зареєстрованих акаунтів (valid_register.txt та valid_register_now.txt).

    Перевірка помилок: 
Бот виведе повідомлення про будь-які помилки або невалідні акаунти.

    Файли:
valid_register.txt - Файл, де зберігаються успішно зареєстровані аккаунти. 
notvalid_register.txt - Файл, де зберігаються не зареєстровані аккаунти , через якусь помилку.
silki.txt - Файл, де зберігаються силки для запрошення в сім'ю.
proxy.txt - Файл, де зберігаються проксі. Проксі зберігати в форматі (username:password:ip:port)

    Важливо
Проксі: Переконайтеся, що у вас є файли proxy.txt, background.js, та manifest.json для використання проксі.
Третя сторона: Будьте обачні та дотримуйтеся умов користування ресурсу, на якому ви реєструєтеся. Автоматизована реєстрація може супроводжуватися ризиками.

    Вимоги
Python: Бот написаний на Python, тому переконайтеся, що ви маєте його встановленого.
Залежності: Встановіть всі необхідні залежності, використовуючи pip install -r requirements.txt.

    Внесок
Якщо ви хочете внести свій внесок або вдосконалити бота, відкрийте новий Pull Request або напишіть мені в телеграм @kiiirookie. Будьте вільні вносити зміни та вдосконалювати бота.


Важливо: Використання даного бота може порушувати правила використання певного ресурсу. Будьте обачні та дотримуйтеся умов користування, щоб уникнути можливих проблем.
