# Python Application Manager Telegram Bot
This bot allows you to create applications and delete them from the database. Each application contains information entered or filled out by the user.

Bot available [here](https://t.me/application_manager_tg_bot), or type @application_manager_tg_bot in the search field.

# Project Structure
* package bot contains:
  * db package:
    * package models with application.py
    * connection.py, database.py to connect and work with the database
  * modules package:
    * handlers package, where event handlers are stored, responsible for the functioning and interaction of the bot with the user
    * keyboard package, where are the classes responsible for creating inline and reply keyboard markup
    * states.py that stores the states of finite machine
  * config.py, bot configuration
* .env.example - environment variables example
* env_loading.py is used to load environment variables
* main.py starts the bot
* requirements.txt contains all dependencies needed to run the program.
```
.
├───bot
│   ├───db
│   │   ├───models
│   │   │   ├───__init__.py
│   │   │   └───application.py
│   │   ├───__init__.py
│   │   ├───connection.py
│   │   └───database.py
│   ├───modules
│   │   ├───handlers
│   │   │   ├───__init__.py
│   │   │   ├───callback_data_vars.py
│   │   │   ├───callback_handlers.py
│   │   │   └───message_handlers.py
│   │   ├───keyboard
│   │   │   ├───__init__.py
│   │   │   ├───inline_keyboard_creator.py
│   │   │   └───reply_keyboard_creator.py
│   │   ├───__init__.py
│   │   └───states.py
│   ├───__init__.py
│   └───config.py
├───.env.example
├───.gitignore
├───LICENSE
├───README.md
├───env_loading.py
├───main.py
└───requirements.txt
```
