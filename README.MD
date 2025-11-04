## telegram-feedback-bot

<a href="https://github.com/z0xca/telegram-feedback-bot/pkgs/container/telegram-feedback-bot"><img alt="telegram-feedback-bot" src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"></a>

Simple Telegram feedback bot based on [aiogram](https://github.com/aiogram/aiogram) and [sulguk](https://github.com/Tishka17/sulguk).

Use this bot to communicate with users without sharing your personal contact details.

> For example: you are an administrator of a Telegram group

## Available commands

| Command |    Description    |
|:-------:|:-----------------:|
|  /help  | Show help message |

### Usage

Messages with of a supported type *(TEXT, ANIMATION, AUDIO, DOCUMENT, PHOTO, VIDEO, VOICE)* will be forwarded to the **admin group** or **admin chat** depending on the destination set via the `chat_id` variable in [`config.yaml`](config.yaml) in which you can also customize the bot's responses.

### Deploy

Copy [`docker-compose.yaml`](docker-compose.yaml) and [`config.yaml`](config.yaml), then run:

```bash
docker compose up -d
```