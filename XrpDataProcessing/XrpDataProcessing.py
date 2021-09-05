import numpy as np
import pandas as pd
import urllib.request
import json
from XrpDataDownloading import XrpDataDownloader

xrpDataDownloader = XrpDataDownloader()
validatorsDF = xrpDataDownloader.downloadValidatorsDF()
print(validatorsDF)

print (xrpDataDownloader.downloadValidatorJSON(validatorsDF['validation_public_key'][0]))

xrpDataDownloader.downloadValidatorsManifest(validatorsDF['validation_public_key'][0])

#
#url = 'https://data.ripple.com/v2/network/validators'#
#
#with urllib.request.urlopen(url) as urlresponse: 
#    dataJsonObject = json.loads(urlresponse.read())#
#
#dfValidators0 = pd.json_normalize(dataJsonObject['validators'])
#print(dfValidators0`)#
#
#dfValidators = pd.DataFrame(dataJsonObject['validators'], columns=['validation_public_key', 'domain', 'chain', 'current_index', 'agreement_1h', 'agreement_24h', 'partial', 'unl'])
#print(dfValidators)
#
#dfValidationPublicKeys = dfValidators['validation_public_key']
#dfValidationAgreement_1h = dfValidators['agreement_1h']
#dfValidationAgreement_24h = dfValidators['agreement_24h']
#
#dfValidatorsIndex = dfValidators.index
#dfValidatorsColumns = dfValidators.columns
#
#print(dfValidators.describe())
#
#print('Loaded some data...')
#
#print('Columns: ')
#print(dfValidatorsColumns)#
#
#print('Index: ')
#print(dfValidatorsIndex)
#