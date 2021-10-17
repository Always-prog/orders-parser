from os import environ as env
from os import urandom

import google.cloud.dialogflow_v2 as dialogflow
from google.oauth2 import service_account

"""

Library for extracting exact addresses, cities, states, postcodes, and your custom values from a string.

"""


class DialogFlowAPI:
    def __init__(self, project_id: str, session_id: str = None, language_code: str = "en",
                 creds_path: str = env.get("GOOGLE_APPLICATION_CREDENTIALS")):
        if not session_id:
            session_id = urandom(24).hex() + "_session_id"
        self.SESSION_ID = session_id
        self.CREDENTIALS = service_account.Credentials.from_service_account_file(creds_path)
        self.SERVICE_AGENTS = dialogflow.services.agents.AgentsClient(credentials=self.CREDENTIALS)
        self.INTENTS_CLIENT = dialogflow.IntentsClient(credentials=self.CREDENTIALS)
        self.LANG_CODE = language_code
        self.PROJECT_ID = project_id

    def extract(self, text: str = None):

        cs = dialogflow.SessionsClient(credentials=self.CREDENTIALS)
        sess = cs.session_path(project=self.PROJECT_ID, session=self.SESSION_ID)
        if text:
            text_input = dialogflow.TextInput(text=text, language_code=self.LANG_CODE)
            query_input = dialogflow.QueryInput(text=text_input)
            response = cs.detect_intent(
                request={"session": sess, "query_input": query_input})
            return response._pb.query_result.parameters.fields
        else:
            raise ValueError("You need to set text or speech")
