import os
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

env_path = Path(".") / ".env"

load_dotenv(dotenv_path=env_path)

app = App(token=os.environ.get("SLACK_BOT_TOKEN"), name="BroKOLee Bot")


@app.event("app_home_opened")
def say_hw(message, say):
    say(f"hello world ")


@app.event("message")
def handle_message(ack, body, say):
    event = body["event"]
    user_id = event["user"]
    channel_id = event["channel"]
    text = event["text"]

    ack()

    if "hello" in text.lower():
        say(f"Hi <@{user_id}>! How can I help you?")


def main():
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()


if __name__ == "__main__":
    main()
