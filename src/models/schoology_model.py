from requests_oauthlib import OAuth1
import requests
from datetime import date
from config.config import KEY, SECRET, USER_ID, API_BASE_URL

class SchoologyModel:
    @staticmethod
    def make_api_request(endpoint, params=None):
        url = f"{API_BASE_URL}{USER_ID}/{endpoint}"
        response = requests.get(url, auth=OAuth1(KEY, SECRET, "", ""), params=params)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_sections():
        sections = SchoologyModel.make_api_request("sections")["section"]
        return [[section["course_title"], section["id"]] for section in sections]


    @staticmethod
    def get_grades(sections):
        temp = []

        for name, section_id in sections:
            section_grade = SchoologyModel.make_api_request("grades", {"section_id": section_id})
            section = section_grade.get("section", [])

            if section:
                temp.append([name, section[-1]["final_grade"][-1]["grade"]])

        return temp
