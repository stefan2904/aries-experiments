# swagger_client.OutofbandApi

All URIs are relative to *https://localhost:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**outofband_accept_invitation**](OutofbandApi.md#outofband_accept_invitation) | **POST** /outofband/accept-invitation | Accepts an invitation.
[**outofband_accept_request**](OutofbandApi.md#outofband_accept_request) | **POST** /outofband/accept-request | Accepts a request.
[**outofband_action_continue**](OutofbandApi.md#outofband_action_continue) | **POST** /outofband/{piid}/action-continue | Allows continuing with the protocol after an action event was triggered.
[**outofband_action_stop**](OutofbandApi.md#outofband_action_stop) | **POST** /outofband/{piid}/action-stop | Stops the protocol after an action event was triggered.
[**outofband_actions**](OutofbandApi.md#outofband_actions) | **GET** /outofband/actions | Returns pending actions that have not yet to be executed or cancelled.
[**outofband_create_invitation**](OutofbandApi.md#outofband_create_invitation) | **POST** /outofband/create-invitation | Creates an invitation.
[**outofband_create_request**](OutofbandApi.md#outofband_create_request) | **POST** /outofband/create-request | Creates a request.


# **outofband_accept_invitation**
> InlineResponse2009 outofband_accept_invitation(body=body)

Accepts an invitation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutofbandApi()
body = swagger_client.Body13() # Body13 |  (optional)

try:
    # Accepts an invitation.
    api_response = api_instance.outofband_accept_invitation(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutofbandApi->outofband_accept_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body13**](Body13.md)|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outofband_accept_request**
> InlineResponse2009 outofband_accept_request(body=body)

Accepts a request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutofbandApi()
body = swagger_client.Body14() # Body14 |  (optional)

try:
    # Accepts a request.
    api_response = api_instance.outofband_accept_request(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutofbandApi->outofband_accept_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body14**](Body14.md)|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outofband_action_continue**
> object outofband_action_continue(piid, label=label, router_connections=router_connections)

Allows continuing with the protocol after an action event was triggered.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutofbandApi()
piid = 'piid_example' # str | Protocol instance ID
label = 'label_example' # str |  (optional)
router_connections = 'router_connections_example' # str |  (optional)

try:
    # Allows continuing with the protocol after an action event was triggered.
    api_response = api_instance.outofband_action_continue(piid, label=label, router_connections=router_connections)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutofbandApi->outofband_action_continue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **label** | **str**|  | [optional] 
 **router_connections** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outofband_action_stop**
> object outofband_action_stop(piid, reason=reason)

Stops the protocol after an action event was triggered.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutofbandApi()
piid = 'piid_example' # str | Protocol instance ID
reason = 'reason_example' # str |  (optional)

try:
    # Stops the protocol after an action event was triggered.
    api_response = api_instance.outofband_action_stop(piid, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutofbandApi->outofband_action_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **reason** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outofband_actions**
> InlineResponse20010 outofband_actions()

Returns pending actions that have not yet to be executed or cancelled.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutofbandApi()

try:
    # Returns pending actions that have not yet to be executed or cancelled.
    api_response = api_instance.outofband_actions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutofbandApi->outofband_actions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outofband_create_invitation**
> InlineResponse20011 outofband_create_invitation(body=body)

Creates an invitation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutofbandApi()
body = swagger_client.Body15() # Body15 |  (optional)

try:
    # Creates an invitation.
    api_response = api_instance.outofband_create_invitation(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutofbandApi->outofband_create_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body15**](Body15.md)|  | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outofband_create_request**
> InlineResponse20012 outofband_create_request(body=body)

Creates a request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutofbandApi()
body = swagger_client.Body16() # Body16 |  (optional)

try:
    # Creates a request.
    api_response = api_instance.outofband_create_request(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutofbandApi->outofband_create_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body16**](Body16.md)|  | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

