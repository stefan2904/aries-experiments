# swagger_client.KmsApi

All URIs are relative to *https://localhost:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_key_set**](KmsApi.md#create_key_set) | **POST** /kms/keyset | Create key set.
[**import_key**](KmsApi.md#import_key) | **POST** /kms/import | Import key.


# **create_key_set**
> create_key_set()

Create key set.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KmsApi()

try:
    # Create key set.
    api_instance.create_key_set()
except ApiException as e:
    print("Exception when calling KmsApi->create_key_set: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_key**
> GenericErrorBody import_key()

Import key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KmsApi()

try:
    # Import key.
    api_response = api_instance.import_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KmsApi->import_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GenericErrorBody**](GenericErrorBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

