import base64
import json
import requests, os
from Shell_FE_Selenium_Core.Utilities.FileUtilities import FileUtilities


class TestResultUpdate:
    input_file = FileUtilities.read_json_file_as_dictionary("/AzureCredentials/AzureCredentials.json")
    organization_url = input_file['Organization_url']
    project_name = input_file['Project_name']
    test_plan_id = input_file['Test_Plan_Id']
    test_suite_ids = input_file['Test_Suite_Id']
    api_version = input_file['api_version']
    pat_token = base64.b64encode(bytes(f":{os.environ.get('AZURE_PAT_TOKEN')}", "utf-8")).decode("ascii")

    # @staticmethod
    # def get_test_suit_ids():
    #     return
    @staticmethod
    def get_test_case_id(suite_id, file_name):
        test_points = {}
        test_case_ids = FileUtilities.read_json_file_as_dictionary(file_name)
        for data in test_case_ids:
            for key, value in data.items():
                test_id = key
                test_points[TestResultUpdate.get_test_points(suite_id, test_id)] = value
        return test_points

    @staticmethod
    def get_test_points(suite_id, test_case_id):
        end_point = f'{TestResultUpdate.organization_url}/{TestResultUpdate.project_name}/_apis/test/plans/{TestResultUpdate.test_plan_id}/Suites/{suite_id}/points?api-version={TestResultUpdate.api_version}'
        headers = {

            'Authorization': f"Basic {TestResultUpdate.pat_token}",
        }
        response = requests.get(end_point, headers=headers)
        if response.status_code == 200:
            test_cases = response.json()['value']
            for test_points in test_cases:
                # print(
                #     f'Test point Id : {test_points["id"]}, Test case id :{test_points["testCase"]["id"]}, Test '
                #     f'case name: {test_points["testCase"]["name"]}')
                if test_points["testCase"]["id"] == test_case_id:
                    test_point_value = test_points["id"]
                    return test_point_value
                else:
                    print("value not matched")

        else:
            print(f'Request failed with status code {response.status_code}')

    @staticmethod
    def update_test_result(suite_id, test_point_id, test_status):
        print(suite_id, test_point_id, test_status)
        end_point = f'{TestResultUpdate.organization_url}/{TestResultUpdate.project_name}/_apis/test/plans/{TestResultUpdate.test_plan_id}/Suites/{suite_id}/points/{test_point_id}?api-version={TestResultUpdate.api_version}'
        headers = {
            'Authorization': f"Basic {TestResultUpdate.pat_token}",
            'Content-Type': 'application/json'
        }
        params = {
            'outcome': test_status
        }
        print(end_point)

        response = requests.patch(end_point, headers=headers, data=json.dumps(params))
        # print(response.text)
        if response.status_code == 200:
            test_status = response.json()['value']
            for test_case_status in test_status:
                print(
                    f'Test Case status: {test_case_status["outcome"]}')

        else:
            print(f'Request failed with status code {response.status_code}')

    @staticmethod
    def test_plan_result_update(file_name):
        for suite_id in TestResultUpdate.test_suite_ids:
            test_point_values = TestResultUpdate.get_test_case_id(suite_id, file_name)
            for key, value in test_point_values.items():
                test_point_id = key
                test_case_result = value
                print("Test point id", test_point_id)
                TestResultUpdate.update_test_result(suite_id, test_point_id, test_case_result)
