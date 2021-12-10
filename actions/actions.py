# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

#To link API with RASA

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from musicAPI import MusicAPI


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_music_API"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        artist=tracker.latest_message['text'] #the artist name the user enter
        data=MusicAPI(artist) #what is found in API

        dispatcher.utter_template("utter_info", tracker, artist=data['strArtist'], biography=data['strBiographyEN']) #what is written

        return []