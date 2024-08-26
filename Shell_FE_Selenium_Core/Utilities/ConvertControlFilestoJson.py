import json
import os
from selenium.webdriver.common.by import By


class controls_json_creation:
    file_name = ""
    controls_json_file_path = ""

    @staticmethod
    def creating_json_file(input_control_file_name, control_library_path):
        controls_json_creation.file_name = "".join(input_control_file_name.split('.', 1)[0] + ".json")
        current_working_directory = os.getcwd()
        test_data = current_working_directory + control_library_path
        controls_file_name = test_data + input_control_file_name
        files_list = os.listdir(test_data)
        controls_json_creation.controls_json_file_path = current_working_directory + "/TestData/Controls/" + controls_json_creation.file_name

        if input_control_file_name in files_list:

            with open(controls_file_name, "r") as f:
                data = f.readlines()

            with open(controls_json_creation.controls_json_file_path, "w") as json_file:
                controls: dict = {}
                for i in range(len(data)):
                    by_locator_names = ['By.XPATH', 'By.ID', 'By.NAME', 'By.CSS_SELECTOR', 'By.CLASS_NAME', 'By.ACCESSIBILITY_ID','By.LINK_TEXT', 'By.PARTIAL_LINK_TEXT', 'By.TAG_NAME']
                    if any(locator_type in data[i] for locator_type in by_locator_names):

                        locator_names = ['XPATH', 'ID', 'NAME', 'CSS_SELECTOR', 'CLASS_NAME', 'ACCESSIBILITY_ID', 'LINK_TEXT', 'PARTIAL_LINK_TEXT', 'TAG_NAME']
                        if any(ele in data[i].strip() for ele in locator_names):
                            locator_name_valid = data[i].split('=', 1)[1].split('.')[1].split(",")[0].lower()
                            # locator_data = data[i].split('=', 1)[1].split('.', 1)[1].split(',', 1)[
                            #     1].strip()
                            # locator_value = locator_data[1:-1]
                            original_data = data[i].split('=', 1)[1].replace("\n", "")
                            tuple_data = eval(original_data)
                            locator_name, locator_value = tuple_data
                            controls[(data[i].split('=', 1)[0]).strip()] = {"reference_name":"", "locator_name": locator_name_valid, "locator_value": locator_value}
                        else:
                            locator_data = data[i].split('=', 1)[1].replace(')', '').strip()
                            locator_value = locator_data[1:-1]
                            controls[data[i].split('=', 1)[0].strip()] = {"reference_name": "", "locator_name": "NA",
                                                                      "locator_value": locator_value}

                    else:
                        no_locator = ['"', "'"]
                        if any(ele in data[i].strip() for ele in no_locator):
                            if "=" in data[i].strip() and "self" not in data[i].strip():
                                original_data = data[i].split('=', 1)[1].replace("\n", "")[1:-1]
                                # locator_data = data[i].split('=', 1)[1].replace(')', '').strip()
                                locator_value = original_data[1:]
                                controls[data[i].split('=', 1)[0].strip()] = {"reference_name": "", "locator_name": "NA",
                                                                          "locator_value": locator_value}
                json.dump(controls, json_file, indent=2)

        else:
            pass
        try:
            with open(controls_json_creation.controls_json_file_path, 'r') as f:
                data = f.read()
                # data = data.replace('\\"', "")
            with open(controls_json_creation.controls_json_file_path, 'w') as f:
                f.write(data)
        except Exception as e:
            pass
