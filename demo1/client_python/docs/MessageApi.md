# swagger_client.MessageApi

All URIs are relative to *https://localhost:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_msg_svc**](MessageApi.md#register_msg_svc) | **POST** /message/register-service | 
[**send_new_message**](MessageApi.md#send_new_message) | **POST** /message/send | 
[**send_reply_message**](MessageApi.md#send_reply_message) | **POST** /message/reply | 
[**services**](MessageApi.md#services) | **GET** /message/services | 
[**unregister_msg_svc**](MessageApi.md#unregister_msg_svc) | **POST** /message/unregister-service | 


# **register_msg_svc**
> GenericErrorBody register_msg_svc(params=params)



registers new message service to message handler registrar

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageApi()
params = swagger_client.RegisterMsgSvcArgs() # RegisterMsgSvcArgs | Params for registering message service (optional)

try:
    api_response = api_instance.register_msg_svc(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->register_msg_svc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**RegisterMsgSvcArgs**](RegisterMsgSvcArgs.md)| Params for registering message service | [optional] 

### Return type

[**GenericErrorBody**](GenericErrorBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_new_message**
> send_new_message(params=params)



sends new message to destination provided

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageApi()
params = swagger_client.SendNewMessageArgs() # SendNewMessageArgs | Params for sending new message (optional)

try:
    api_instance.send_new_message(params=params)
except ApiException as e:
    print("Exception when calling MessageApi->send_new_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**SendNewMessageArgs**](SendNewMessageArgs.md)| Params for sending new message | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_reply_message**
> send_reply_message(params=params)



sends reply to existing message

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessageApi()
params = swagger_client.SendReplyMessageArgs() # SendReplyMessageArgs | Params for sending message reply (optional)

try:
    api_instance.send_reply_message(params=params)
except ApiException as e:
    print("Exception when calling MessageApi->send_reply_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**SendReplyMessageArgs**](SendReplyMessageArgs.md)| Params for sending message reply | [optional] 

### Return type

void (empty response body)

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
api_instance = swagger_client.MessageApi()

try:
    api_instance.services()
except ApiException as e:
    print("Exception when calling MessageApi->services: %s\n" % e)
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
api_instance = swagger_client.MessageApi()
params = swagger_client.UnregisterMsgSvcArgs() # UnregisterMsgSvcArgs | Params for unregistering a message service (optional)

try:
    api_response = api_instance.unregister_msg_svc(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->unregister_msg_svc: %s\n" % e)
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

