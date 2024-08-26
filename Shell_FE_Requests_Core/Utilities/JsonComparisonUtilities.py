import json
import re
import jsonpath
import requests
from nested_lookup import nested_lookup
from deepdiff import DeepDiff
from Shell_FE_Requests_Core.Utilities.LoggingUtilities import LoggingUtilities


class JsonComparisonUtils:
    keys = []
    values = []
    log_obj = LoggingUtilities()
    log = log_obj.logger()

    @staticmethod
    def ordered(obj):
        """
        Ordered is a method which will take a json data as a parameter and verify dict , list
        and sort the data based on dict and list instance and return sorted json data
        :Args:
            -obj : json data file
        :Returns:
            Sorted json object
        """
        if isinstance(obj, dict):
            return sorted((key, JsonComparisonUtils.ordered(value)) for key, value in obj.items())
        if isinstance(obj, list):
            return sorted(JsonComparisonUtils.ordered(x) for x in obj)
        else:
            return obj

    @staticmethod
    def response_isequal(res1, res2):
        """
        It's a method used to compare 2 json data files,
        :Args:
            file1_data : Json data file 1
            file2_data : Json data file 2
        :Returns:
            boolean
        """

        JsonComparisonUtils.log.info("Comparing response values")
        if isinstance(res1, requests.models.Response) and isinstance(res2, requests.models.Response):
            json1_data = json.loads(res1.text)
            json2_data = json.loads(res2.text)
            return JsonComparisonUtils.ordered(json1_data) == JsonComparisonUtils.ordered(json2_data)
        elif isinstance(res1, (dict, list,str)) and isinstance(res2, requests.models.Response):
            json2_data = json.loads(res2.text)
            return JsonComparisonUtils.ordered(res1) == JsonComparisonUtils.ordered(json2_data)
        elif isinstance(res1, requests.models.Response) and isinstance(res2, (dict, list, str)):
            json1_data = json.loads(res1.text)
            return JsonComparisonUtils.ordered(json1_data) == JsonComparisonUtils.ordered(res2)
        elif isinstance(res1, (dict, list, str)) and isinstance(res2, (dict, list, str)):
            return JsonComparisonUtils.ordered(res1) == JsonComparisonUtils.ordered(res2)
        else:
            return False

    @staticmethod
    def search_values_in_response_with_key(json_obj, user_key):
        """
        This is the method to search the particular value based on the user provided key
        :Args:
            json_obj : Json Data
            user_ey : Key to search in the json data
        :Returns:
            List of values matched to user key
        """
        if isinstance(json_obj, requests.models.Response):

            data = json.loads(json_obj.text)
            JsonComparisonUtils.log.info("Following are the values matched with key  ' {} ' ".format(user_key))
            JsonComparisonUtils.log.info(nested_lookup(user_key, data)[0])
            return nested_lookup(user_key, data)
        else:
            data = json.loads(json_obj)
            JsonComparisonUtils.log.info("Following are the values matched with key  ' {} ' ".format(user_key))
            JsonComparisonUtils.log.info(nested_lookup(user_key, data)[0])
            return nested_lookup(user_key, data)

    @staticmethod
    def get_node_value(res, key):
        """
        This method can be used to get a value for a particular key from json response.

        :Args:
            res: api response data
            key: Key item to search in the response data
        :Returns:
            List of Values for key provided
        """
        if isinstance(res, requests.models.Response):
            value = jsonpath.jsonpath(res.json(), key)
            JsonComparisonUtils.log.info(f"Node value: '{value}' for jsonpath : '{key}'")
            return value[0]
        else:
            value = jsonpath.jsonpath(res, key)
            JsonComparisonUtils.log.info(f"Node value: '{value}' for jsonpath : '{key}'")
            return value[0]

    @staticmethod
    def find_difference(res1, res2):
        """
        find_difference: Find Difference of dictionaries, iterables, strings and other objects. It will recursively look for
        all the changes but it will not ignore the order of the nodes.

        :Args:
            res1: api response data 1
            res2: api response data 2
        :Returns:
            The difference data in the form of dictionary
        """
        json1_data = json.loads(res1.text)
        json2_data = json.loads(res2.text)

        if len(json1_data) != len(json2_data):

            for js1, js2 in zip(JsonComparisonUtils.ordered(json1_data), JsonComparisonUtils.ordered(json2_data)):
                if js1[0] != js2[0]:
                    # keys.append((js1[0], js2[0]))
                    JsonComparisonUtils.keys.append((js1[0], js2[0]))
                if js1[1] != js2[1]:
                    # values.append((js1[1], js2[1]))
                    JsonComparisonUtils.values.append((js1[1], js2[1]))
        return JsonComparisonUtils.keys, JsonComparisonUtils.values

    @staticmethod
    def deep_difference(res1, res2):
        """
        DeepDiff: Deep Difference of dictionaries, iterables, strings and other objects. It will recursively look for
        all the changes.

        :Args:
            res1: api response data 1
            res2: api response data 2
        :Returns:
            The difference data in the form of dictionary
        """
        json1_data = json.loads(res1.text)
        json2_data = json.loads(res2.text)
        deep_diff = DeepDiff(json1_data, json2_data, ignore_order=True)
        JsonComparisonUtils.log.info(f"Difference between the responses: {deep_diff} ")
        return deep_diff

    @staticmethod
    def is_value_present_in_res(value, res):
        """
        is_value_present_in_res: Which will search a user provided value in the response data

        :Args:
            value: Value to be searched
            res2: api response data 2
        :Returns:
            Boolean
        """
        res_str = res.text
        JsonComparisonUtils.log.info("Searching a {} value in {} res".format(value, res_str))
        pattern = r'(^|[^\w]){}([^\w]|$)'.format(value)
        pattern = re.compile(pattern, re.IGNORECASE)
        matches = re.search(pattern, res_str)
        return bool(matches)

    @staticmethod
    def compare_node_values(node_result1, node_result2):
        """
        compare_node_values: Which will compare two node values return true id both the node valued are same else returns false

        :Args:
            node_result1: Actual node data
            node_result2: expected node data
        :Returns:
            Boolean
        """
        JsonComparisonUtils.log.info(f"Comparing 2 node results {node_result1} and {node_result2}")
        return node_result1.sort() == node_result2.sort()

