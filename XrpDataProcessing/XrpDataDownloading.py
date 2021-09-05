import numpy as np
import pandas as pd
import urllib.request
import json

class XrpDataDownloader: 

    ALL_VALIDATORS_API = '/network/validators'
    VALIDATOR_API = '/network/validators/{}'
    VALIDATOR_MANIFEST_API = '/network/validators/{}/manifests'

    API_SUCCESS_STRING = 'success'

    xrpAPIBase = None

    def __init__(self, xrpAPIBase = 'https://data.ripple.com/v2'): 
        self.xrpAPIBase = xrpAPIBase

    def __downloadJSONFrom(self, url): 
        with urllib.request.urlopen(url) as urlResponse: 
            return json.loads(urlResponse.read())

    def downloadAllValidatorsDF(self): 
        validatorsJSON = self.__downloadJSONFrom(self.xrpAPIBase + self.ALL_VALIDATORS_API)
        if validatorsJSON['result'] == self.API_SUCCESS_STRING: 
            return pd.json_normalize(validatorsJSON['validators'])

    def downloadValidatorJSON(self, validation_public_key): 
        return self.__downloadJSONFrom(self.xrpAPIBase + self.VALIDATOR_API.form(validation_public_key))

    def downloadValidatorsManifestJSON(self, validation_public_key): 
        return self.__downloadJSONFrom(self.xrpAPIBase + self.VALIDATOR_MANIFEST_API.format(validation_public_key))
