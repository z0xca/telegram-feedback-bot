# telegram-feedback-bot

<p>

<a href="https://github.com/z0xca/telegram-feedback-bot/pkgs/container/telegram-feedback-bot"><img alt="telegram-feedback-bot" src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"></a>
</p>


Simple telegram-feedback bot based on [aiogram](https://github.com/aiogram/aiogram) and [sulguk](https://github.com/Tishka17/sulguk).

Use this bot for communicate with users in case you do not want to provide your personal contacts. 

> For example: you are administrator of telegram group or technical support provider.

## Available commands

| Command |    Description    |
|:-------:|:-----------------:|
|  /help  | Show help message |

## Usage

Messages with an **available content type** *(TEXT, ANIMATION, AUDIO, DOCUMENT, PHOTO, VIDEO, VOICE)* will be transferred to **admin group** or **admin chat**.

*(See variable `chat_id` from [config.yaml](deploy/docker/example.config.yaml#L6))*

If the transfer is successful, the requesting party will be notified.

**Admin** can **answer** to message **by reply**. The answer will be sent to the person who asked.

The user will receive the reply as a **reply** to the original message. If the message does not exist, the user will receive a response with a **separate message**.

If the transfer is successful, the administrator will be notified.

You can [customize the bot's responses](deploy/docker/example.config.yaml#12), or use default values.

## Deploy

Just copy [docker-compose.yml](deploy/docker/example.docker-compose.yml) and fill in [config.yaml](deploy/docker/example.config.yaml).

Run container:

`docker compose up -d`