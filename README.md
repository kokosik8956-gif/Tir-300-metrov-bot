# Telegram FAQ Bot

Простой Telegram-бот на Python с использованием `pyTelegramBotAPI`.

## Что умеет бот

- Отвечает на команду `/start`
- Показывает кнопки с часто задаваемыми вопросами
- Отправляет ответы по нажатию на кнопку
- Показывает кнопку `Назад к вопросам`
- Отправляет образец электронного сертификата картинкой

## Структура проекта

- `main.py` - основной файл бота
- `config.py` - загрузка токена из `.env`
- `.env` - хранение токена `BOT_TOKEN`
- `requirements.txt` - зависимости проекта
- `assets/certificate_sample.png` - образец сертификата

## Установка

Установите зависимости:

```powershell
& "C:\Users\User\AppData\Local\Programs\Python\Python314\python.exe" -m pip install -r requirements.txt
```

## Настройка

Укажите токен бота в файле `.env`:

```env
BOT_TOKEN=ВАШ_ТОКЕН_БОТА
```

## Запуск

Запуск бота:

```powershell
cd "d:\Чат-бот в тг"
& "C:\Users\User\AppData\Local\Programs\Python\Python314\python.exe" main.py
```

## Примечание

Если Telegram сообщает об ошибке `409 Conflict`, значит этот же бот уже запущен где-то еще с тем же токеном. Нужно остановить другой экземпляр бота или перевыпустить токен через `@BotFather`.
