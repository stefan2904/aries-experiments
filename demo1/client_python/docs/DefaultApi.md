# swagger_client.DefaultApi

All URIs are relative to *https://localhost:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verifiable**](DefaultApi.md#verifiable) | **GET** /verifiable/presentations | Retrieves the verifiable credentials.


# **verifiable**
> list[Record] verifiable()

Retrieves the verifiable credentials.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Retrieves the verifiable credentials.
    api_response = api_instance.verifiable()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->verifiable: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Record]**](Record.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

