import os
import requests
from configparser import ConfigParser
from Shell_FE_Requests_Core.Utilities.LoggingUtilities import LoggingUtilities


class RequestsBase:
    """RequestsBase class contains methods for reading values from INI file and performing basic HTTP actions."""
    # region Class Variable Declarations
    config = None
    base_uri = None
    endpoint_url = None
    response = None
    request = None
    current_working_directory = os.path.dirname(os.getcwd())
    configfile = current_working_directory + '/Shell_FE_Behave_Tests/behave.ini'
    log = LoggingUtilities().logger()

    # endregion

    @staticmethod
    def read_config():
        """Reads behave.ini file present in Shell_FE_Behave_Tests folder.

        Returns:
                An instance of ConfigParser.
        """
        try:
            configuration = ConfigParser()
            configuration.read(RequestsBase.configfile)
            RequestsBase.config = configuration
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def initialize_values():
        """Assigns respective values to class variables from behave.ini file."""
        try:
            RequestsBase.read_config()
            environment = RequestsBase.config['api']['environment']
            # region Base Uri initialization
            if environment == "dev":
                RequestsBase.base_uri = RequestsBase.config['api']['dev_baseuri']
            elif environment == "qa":
                RequestsBase.base_uri = RequestsBase.config['api']['qa_baseuri']
            elif environment == "stage":
                RequestsBase.base_uri = RequestsBase.config['api']['stage_baseuri']
            elif environment == "prod":
                RequestsBase.base_uri = RequestsBase.config['api']['prod_baseuri']
            else:
                RequestsBase.log.error(
                    "Invalid environment name provided in INI file. Environment: {0}.".format(environment))
            # endregion
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def set_endpoint(base_uri=None, path_params=None):
        """Builds the Endpoint by appending the BaseUri along with the resource passed as arguments to this method.
        The value would be saved into the 'endpoint_url' variable available in RequestsBase."""
        try:
            if base_uri is None:
                if path_params is not None:
                    RequestsBase.endpoint_url = RequestsBase.base_uri + path_params
                    RequestsBase.log.info("The end point url is: " + RequestsBase.endpoint_url)
                else:
                    RequestsBase.endpoint_url = RequestsBase.base_uri
                    RequestsBase.log.info(
                        "The end point url is: " + RequestsBase.endpoint_url + ". No path parameters were passed.")
            else:
                if path_params is not None:
                    RequestsBase.endpoint_url = base_uri + path_params
                    RequestsBase.log.info("The end point url is: " + RequestsBase.endpoint_url)
                else:
                    RequestsBase.endpoint_url = base_uri
                    RequestsBase.log.info(
                        "The end point url is: " + RequestsBase.endpoint_url + ". No path parameters were passed.")
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def get_request(url=None, query_params=None, **opts):
        """Makes a GET request to the URI.

        :Args:
            - url - It has a default parameter of None. If the user doesn't pass an endpoint url then the value
        from endpoint_url in RequestsBase would be used else the user provided url value would be used.
            - query_params - It has a default parameter of None. User can pass a dictionary or list of tuples into this
            parameter which will be assigned as query parameters to the endpoint url.
            - **opts - This is a placeholder for keyword arguments where the user can pass any valid arguments to the
            GET request viz. data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream,
            verify,cert or json. Please refer to the official documentation of Python Requests to learn more about these
            parameters and the type of value to send.
        """
        try:
            if url is None:
                RequestsBase.response = requests.get(RequestsBase.endpoint_url, params=query_params, **opts)
                RequestsBase.log.info(
                    "The GET request has been passed with the url: " + RequestsBase.response.request.url)
            else:
                RequestsBase.response = requests.get(url, params=query_params, **opts)
                RequestsBase.log.info(
                        "The GET request has been passed with the url: " + RequestsBase.response.request.url)
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def put_request(url=None, body_data=None, **opts):
        """Makes a PUT request to the URI.

        :Args:
            - url - It has a default parameter of None. If the user doesn't pass an endpoint url then the value
            from endpoint_url in RequestsBase would be used else the user provided url value would be used.
            - body_data - It has a default parameter of None. User can pass a dictionary or list of tuples into this
            parameter which will be passed as the Request payload / body.
            - **opts - This is a placeholder for keyword arguments where the user can pass any valid arguments to the
            PUT request viz. data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream,
            verify,cert or json. Please refer to the official documentation of Python Requests to learn more about these
            parameters and the type of value to send.
        """
        try:
            if url is None:
                RequestsBase.response = requests.put(RequestsBase.endpoint_url, data=body_data, **opts)
                RequestsBase.log.info(
                    "The PUT request has been passed with the url: " + RequestsBase.response.request.url)
            else:
                RequestsBase.response = requests.put(url, data=body_data, **opts)
                RequestsBase.log.info(
                    "The PUT request has been passed with the url: " + RequestsBase.response.request.url)
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def post_request(url=None, body_data=None, body_json=None, **opts):
        """Makes a POST request to the URI.

        :Args:
            - url - It has a default parameter of None. If the user doesn't pass an endpoint url then the value
            from endpoint_url in RequestsBase would be used else the user provided url value would be used.
            - body_data - It has a default parameter of None. User can pass a dictionary or list of tuples into this
            parameter which will be passed as the Request payload / body.
            - body_json - It has a default parameter of None. User can pass a json data into this parameter which will
            be passed as the Request payload / body.
            - **opts - This is a placeholder for keyword arguments where the user can pass any valid arguments to the
            POST request viz. data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream,
            verify,cert or json. Please refer to the official documentation of Python Requests to learn more about these
            parameters and the type of value to send.
        """
        try:
            if url is None:
                RequestsBase.response = requests.post(RequestsBase.endpoint_url, data=body_data, json=body_json, **opts)
                RequestsBase.log.info(
                    "The POST request has been passed with the url: " + RequestsBase.response.request.url)
            else:
                RequestsBase.response = requests.post(url, data=body_data, json=body_json, **opts)
                RequestsBase.log.info(
                    "The POST request has been passed with the url not None: " + RequestsBase.response.request.url)
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def delete_request(url=None, **opts):
        """Makes a DELETE request.

        :Args:
            - url - It has a default parameter of None. If the user doesn't pass an endpoint url then the value
            from endpoint_url in RequestsBase would be used else the user provided url value would be used.
            - **opts - This is a placeholder for keyword arguments where the user can pass any valid arguments to the
            DELETE request viz. data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream,
            verify,cert or json. Please refer to the official documentation of Python Requests to learn more about these
            parameters and the type of value to send.
        """
        try:
            if url is None:
                RequestsBase.response = requests.delete(RequestsBase.endpoint_url, **opts)
                RequestsBase.log.info(
                    "The DELETE request has been passed with the url: " + RequestsBase.response.request.url)
            else:
                RequestsBase.response = requests.delete(url, **opts)
                RequestsBase.log.info(
                    "The DELETE request has been passed with the url: " + RequestsBase.response.request.url)
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def patch_request(url=None, body_data=None, **opts):
        """Makes a PATCH request to the URI.

        :Args:
            - url - It has a default parameter of None. If the user doesn't pass an endpoint url then the value
            from endpoint_url in RequestsBase would be used else the user provided url value would be used.
            - body_data - It has a default parameter of None. User can pass a dictionary or list of tuples into this
            parameter which will be passed as the Request payload / body.
            - **opts - This is a placeholder for keyword arguments where the user can pass any valid arguments to the
            PATCH request viz. data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream,
            verify,cert or json. Please refer to the official documentation of Python Requests to learn more about these
            parameters and the type of value to send.
        """
        try:
            if url is None:
                RequestsBase.response = requests.patch(RequestsBase.endpoint_url, data=body_data, **opts)
                RequestsBase.log.info(
                    "The PATCH request has been passed with the url: " + RequestsBase.response.request.url)
            else:
                RequestsBase.response = requests.patch(url, data=body_data, **opts)
                RequestsBase.log.info(
                    "The PATCH request has been passed with the url: " + RequestsBase.response.request.url)
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def request_url(response=None):
        """Returns the complete request url. The user needs to provide a valid Response object as a parameter. If no
        parameter is passed then the Request Url of the Response object available in RequestsBase class would be
        returned."""
        try:
            if response is None:
                return RequestsBase.response.request.url
            else:
                return response.request.url
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def request_header(response=None):
        """Returns the header passed in the request. The user needs to provide a valid Response object as a parameter.
        If no parameter is passed then the request headers of the Response object available in RequestsBase class would
        be returned."""
        try:
            if response is None:
                return RequestsBase.response.request.headers
            else:
                return response.request.headers
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def response_status_code(response=None):
        """Returns the status code of the response. The user needs to provide a valid Response object as a parameter.
        If no parameter is passed then the status code of the Response object available in RequestsBase class would
        be returned."""
        try:
            if response is None:
                return RequestsBase.response.status_code
            else:
                return response.status_code
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def response_headers(response=None):
        """Returns the headers of the response. The user needs to provide a valid Response object as a parameter.
        If no parameter is passed then the status code of the Response object available in RequestsBase class would
        be returned."""
        try:
            if response is None:
                return RequestsBase.response.headers
            else:
                return response.headers
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def response_cookies(response=None):
        """Returns the cookies of the response. The user needs to provide a valid Response object as a parameter.
        If no parameter is passed then the status code of the Response object available in RequestsBase class would
        be returned."""
        try:
            if response is None:
                return RequestsBase.response.cookies
            else:
                return response.cookies
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def response_body_as_dictionary(response=None):
        """Returns the body of the response as a Python dictionary object. The user needs to provide a valid Response
        object as a parameter. If no parameter is passed then the status code of the Response object available in
        RequestsBase class would be returned."""
        try:
            if response is None:
                return RequestsBase.response.json()
            else:
                return response.json()
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def response_body_as_string(response=None):
        """Returns the body of the response as a String object. The user needs to provide a valid Response object as a
        parameter. If no parameter is passed then the status code of the Response object available in RequestsBase class
        would be returned."""
        try:
            if response is None:
                return RequestsBase.response.text
            else:
                return response.text
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def response_body_as_bytes(response=None):
        """Returns the body of the response as Bytes. The user needs to provide a valid Response object as a parameter.
        If no parameter is passed then the status code of the Response object available in RequestsBase class would
        be returned."""
        try:
            if response is None:
                return RequestsBase.response.content
            else:
                return response.content
        except Exception as err:
            RequestsBase.log.error(err)

    @staticmethod
    def get_access_token(url='', data='', verify=False, allow_redirects=False):
        """
        Return the access token as a response for the url
        :param url: Provide the url for which access token needs to capture
        :param data: User can pass a dictionary into this parameter which will be passed as the Request payload / body.
        :param verify: True or False
        :param allow_redirects: True or False
        :return: access token or False
        """
        try:
            RequestsBase.post_request(url=url, body_data=data, verify=verify, allow_redirects=allow_redirects)
            access_token_response = RequestsBase.response
            RequestsBase.log.info(access_token_response)
            return access_token_response
        except Exception as err:
            RequestsBase.log.error(err)
            return False

    @staticmethod
    def get_response_time():
        RequestsBase.log.info(f"The total time elapsed to get the response is {RequestsBase.response.elapsed.total_seconds()} Seconds")
        return RequestsBase.response.elapsed.total_seconds()

