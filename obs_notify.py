CONFIG_PATH = "$SCRIPT/obsNativeNotifier/config.toml"


from notifypy import Notify
import tomllib
from inspect import getsourcefile
from os.path import abspath, dirname
import obspython as S
import logging




def script_path() -> str:
    return dirname(abspath(getsourcefile(lambda:0)))

def replace_dollar_strings(string: str, action: str = "no_action") -> str:
    path = script_path()

    string = string.replace("$ACTION", action)
    string = string.replace("$SCRIPT", script_path())
    return string


with open(replace_dollar_strings(CONFIG_PATH), "rb") as rb:
    config = tomllib.load(rb)

logging.basicConfig(
    level=getattr(logging, config["logs"]["level"]),
    format="%(asctime)s %(levelname)s: %(message)s",
    filename=replace_dollar_strings(config["logs"]["file"]),
)


def script_description():
    "Notifies a user via native OS pop-up when selected actions are performed"


notification = Notify(
    default_notification_title="NOT SPECIFIED",
    default_application_name="NOT SPECIFIED",
    default_notification_message="NOT SPECIFIED",
)


def on_event(event):
    for encoded, plain_text in config["notification"]["actions"][0].items():
        if event == getattr(S, encoded):
            notification.title = replace_dollar_strings(
            config["notification"]["title"], str(plain_text)
            )
            notification.message = replace_dollar_strings(
                config["notification"]["text"], str(plain_text)
            )
            notification.icon = replace_dollar_strings(config["notification"]["image"])
            notification.audio = replace_dollar_strings(config["notification"]["sound"])
            notification.application_name = replace_dollar_strings(
                config["notification"]["appName"], str(plain_text)
            )
            notification.send()
            logging.info(f"Notification sent: title={notification.title} msg={notification.message}")
            


def script_load(settings):
    S.obs_frontend_add_event_callback(on_event)