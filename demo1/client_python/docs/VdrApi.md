# swagger_client.VdrApi

All URIs are relative to *https://localhost:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_did_records**](VdrApi.md#get_did_records) | **GET** /vdr/did/records | 
[**get_did_req**](VdrApi.md#get_did_req) | **GET** /vdr/did/{id} | Gets did document with the friendly name.
[**resolve_did_req**](VdrApi.md#resolve_did_req) | **GET** /vdr/did/resolve/{id} | 
[**save_did_req**](VdrApi.md#save_did_req) | **POST** /vdr/did | Saves a did document with the friendly name.


# **get_did_records**
> list[Record] get_did_records()



Retrieves the did records

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VdrApi()

try:
    api_response = api_instance.get_did_records()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdrApi->get_did_records: %s\n" % e)
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

# **get_did_req**
> get_did_req(id)

Gets did document with the friendly name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VdrApi()
id = 'id_example' # str | DID ID - pass the did

try:
    # Gets did document with the friendly name.
    api_instance.get_did_req(id)
except ApiException as e:
    print("Exception when calling VdrApi->get_did_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DID ID - pass the did | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_did_req**
> resolve_did_req(id)



Resolve did

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VdrApi()
id = 'id_example' # str | DID ID - pass the did

try:
    api_instance.resolve_did_req(id)
except ApiException as e:
    print("Exception when calling VdrApi->resolve_did_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| DID ID - pass the did | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_did_req**
> GenericErrorBody save_did_req(params=params)

Saves a did document with the friendly name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VdrApi()
params = swagger_client.DIDArgs() # DIDArgs | Params for saving the did document (pass the did document as json raw message) (optional)

try:
    # Saves a did document with the friendly name.
    api_response = api_instance.save_did_req(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VdrApi->save_did_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**DIDArgs**](DIDArgs.md)| Params for saving the did document (pass the did document as json raw message) | [optional] 

### Return type

[**GenericErrorBody**](GenericErrorBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

