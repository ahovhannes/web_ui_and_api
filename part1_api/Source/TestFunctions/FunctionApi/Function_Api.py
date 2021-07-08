#
# Author: Hovhannes Atoyan (hovhannes.atoyan@gmail.com)
#
# Collection of API functions
#

import json
import requests
from requests.exceptions import HTTPError

class bddApi:

    def do_api_call(self, apiCallType, host, headers, data={}, cert={}, files={}):
        """
        Doing API call

        Args:
            apiCallType : The API method, e.g. GET, POST, PUT
            host        : The URL to send data to
            headers     : Headers for the request
            data        : The data to be sent along
            cert        : The certificate file

        Returns:
            The server response as a dictionary
        """
        if apiCallType == 'get':
            resp = requests.get(host, headers=headers, cert=cert)
        elif apiCallType == 'post':
            resp = requests.post(host, headers=headers, json=data, cert=cert, files=files)
        elif apiCallType == 'delete':
            resp = requests.delete(host, headers=headers, data=data, cert=cert)
            
        elif apiCallType == 'put':
            resp = requests.put(host, headers=headers, data=data, cert=cert)
        else:
            print("\n*****ERROR: Wrong API call type...")
            return {"status": 400, "MSG": "ERROR: Wrong API call type "+str(apiCallType)}
        return resp

    def api_get_from_index_aspx(self, host, headers, data):
        """
        Get API call for index.aspx
        
        Args:
            host    : The URL to send data to
            headers : Headers for the request
            data    : The data to be sent along

        Returns:
            The server response as a dictionary
        """
        try:
            resp = self.do_api_call("get", host, headers, data)
            # If the response was successful, no Exception will be raised
            resp.raise_for_status()
        except HTTPError as http_err:
            print(f'\n*****ERROR: HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'\n*****ERROR: Other error occurred: {err}')
            print("\n*****ERROR: An exception occurred... Check Your Network Connection...\n")
        else:
            return resp.json()


    # --------------- API Calls With Certificate ---------------

    def do_api_call_wit_certificate(self, apiCallType, host, headers, data, files={}):
        """
        Doing API call with Certificate

        Args:
            apiCallType : The API method, e.g. GET, POST, PUT
            host        : The URL to send data to
            headers     : Headers for the request
            data        : The data to be sent along

        Returns:
            The server response as a dictionary
        """
        cert_dir = "TestFunctions/FunctionApi/CE-cert/"
        cert = cert_dir+"cecertificate.pem"
        resp = self.do_api_call(apiCallType, host, headers, data, cert=cert, files=files)
        return resp

    def api_get_ce(self, host, headers):
        """
        Get API calls for Blaklists, Phrases, Creatives
        
        Args:
            host    : The URL to get data from
            headers : Headers for the request

        Returns:
            The server response as a dictionary
        """
        data={}
        try:
            resp = self.do_api_call_wit_certificate("get", host, headers, data)
            # If the response was successful, no Exception will be raised
            resp.raise_for_status()
        except HTTPError as http_err:
            print(f'\n*****ERROR: HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'\n*****ERROR: Other error occurred: {err}')
        else:
            return resp.json()

    def api_post_ce(self, host, headers, data):
        """
        POST API calls for Blaklists, Phrases, Creatives
        
        Args:
            host    : The URL to get data from
            headers : Headers for the request
            data    : The data to be sent along

        Returns:
            The server response as a dictionary
        """
        try:
            resp = self.do_api_call_wit_certificate("post", host, headers, data)
            # If the response was successful, no Exception will be raised
            resp.raise_for_status()
        except HTTPError as http_err:
            print(f'\n*****ERROR: HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'\n*****ERROR: Other error occurred: {err}')
        else:
            return resp.text

    def api_post_file_ce(self, host, headers, data, files):
        """
        POST API calls for Creatives
        
        Args:
            host    : The URL to get data from
            headers : Headers for the request
            data    : The data to be sent along
            files   : Dictionary with the key 'file' and with the value containing opened image-file. Example: {'file': open(MY_IMAGE_FILE, 'rb')}

        Returns:
            The server response is <Response [200]> when file were successfully uploaded
        """
        resp = self.do_api_call_wit_certificate("post", host, headers, data, files)
        return resp


    def api_delete_ce(self, host, headers, data):
        """
        DELETE API calls for Creatives
        
        Args:
            host    : The URL to get data from
            headers : Headers for the request
            data    : The data to be sent along

        Returns:
            The server response is <Response [200]> when creative were successfully deleted
        """
        
        resp = self.do_api_call_wit_certificate("delete", host, headers, data)
        return resp
