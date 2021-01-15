# swagger_client.HttpOverDidcommApi

All URIs are relative to *https://localhost:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_http_msg_svc**](HttpOverDidcommApi.md#register_http_msg_svc) | **POST** /http-over-didcomm/register | 
[**services**](HttpOverDidcommApi.md#services) | **GET** /message/services | 
[**unregister_msg_svc**](HttpOverDidcommApi.md#unregister_msg_svc) | **POST** /message/unregister-service | 


# **register_http_msg_svc**
> GenericErrorBody register_http_msg_svc(params=params)



registers new http over didcomm service to message handler registrar

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HttpOverDidcommApi()
params = swagger_client.RegisterHTTPMsgSvcArgs() # RegisterHTTPMsgSvcArgs | Params for registering http over did comm message service. (optional)

try:
    api_response = api_instance.register_http_msg_svc(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HttpOverDidcommApi->register_http_msg_svc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**RegisterHTTPMsgSvcArgs**](RegisterHTTPMsgSvcArgs.md)| Params for registering http over did comm message service. | [optional] 

### Return type

[**GenericErrorBody**](GenericErrorBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services**
> services()



returns list of registered service names

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HttpOverDidcommApi()

try:
    api_instance.services()
except ApiException as e:
    print("Exception when calling HttpOverDidcommApi->services: %s\n" % e)
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

# **unregister_msg_svc**
> GenericErrorBody unregister_msg_svc(params=params)



unregisters given message service handler registrar

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HttpOverDidcommApi()
params = swagger_client.UnregisterMsgSvcArgs() # UnregisterMsgSvcArgs | Params for unregistering a message service (optional)

try:
    api_response = api_instance.unregister_msg_svc(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HttpOverDidcommApi->unregister_msg_svc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**UnregisterMsgSvcArgs**](UnregisterMsgSvcArgs.md)| Params for unregistering a message service | [optional] 

### Return type

[**GenericErrorBody**](GenericErrorBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

