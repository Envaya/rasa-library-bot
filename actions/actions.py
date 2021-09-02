# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


import requests
import json

import datetime as dt

from typing import Text, List, Any, Dict

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time = dt.datetime.now()
        day = time.day
        hour = time.hour
        minutes = time.minute
        switcher = {
            1: "Januar",
            2: "Februar",
            3: "März",
            4: "April",
            5: "Mai",
            6: "Juni",
            7: "Juli",
            8: "August",
            9: "September",
            10: "Oktober",
            11: "November",
            12: "Dezember",
        }
        month = switcher.get(time.month, "Undefiniert")
        dispatcher.utter_message("Es ist {} Uhr {}. {}. {}".format(hour, minutes, day, month))
        return []


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        request = requests.get("https://witzapi.de/api/joke")
        response = request.json()
        dispatcher.utter_message(response[0]["text"])  # send the message back to the user
        return []

# class ValidateLibraryRegistrationForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_library_registration_form"
#
#     @staticmethod
#     def cuisine_db() -> List[Text]:
#         """Database of supported cuisines"""
#
#         return ["caribbean", "chinese", "french"]
#
#     def validate_is_student(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate cuisine value."""
#
#         if slot_value:
#             return {"is_student": True}
#
#         if slot_value.lower() in self.cuisine_db():
#             # validation succeeded, set the value of the "cuisine" slot to value
#             return {"cuisine": slot_value}
#         else:
#             # validation failed, set this slot to None so that the
#             # user will be asked for the slot again
#             return {"cuisine": None}
