from typing import Optional

from pydantic import Field
from pydantic import SecretStr
from pydantic_settings import BaseSettings


class BotConfig(BaseSettings):
    """
    Bot config
    """

    token: SecretStr


class Messages(BaseSettings):
    notify_user_about_success_deliver: Optional[str] = Field(
        default="✅ Please wait for response."
    )
    help_message: str = Field(
        default="""
     <h1>
      👋 Hello!
      </h1>
      <p>
          I can redirect to recipient <b>text, audios, voice messages, images, files</b> to recipient.
      </p>

      <p>
       Just send your message and wait for a response! 
      </p>
    """
    )
    notify_admin_about_success_answer: Optional[str] = Field(default="✅ Answered.")


class Errors(BaseSettings):
    unsupported_type: str = Field(
        default="❌ Unsupported message type.<br/>Please check <b>/help</b> command."
    )
    too_long_message_text: str = Field(default="❌ Too long message text.")
    too_long_message_caption: str = Field(default="❌ Too long message caption.")
    copy_message: str = Field(default="❌ Error during copying")
    extract_user_id: str = Field(default="❌ Error during extract_id")
    chat_not_found: str = Field(
        default="❌ Chat not found. Make sure you have added the bot to the admin group"
    )


class Config(BaseSettings):
    """
    All in one config
    """

    bot: BotConfig
    chat_id: int
    messages: Messages = Messages()
    errors: Errors = Errors()


__all__ = ["BotConfig", "Config"]
