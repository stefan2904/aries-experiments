# swagger_client.MediatorApi

All URIs are relative to *https://localhost:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_pickup_request**](MediatorApi.md#batch_pickup_request) | **POST** /mediator/batchpickup | BatchPickup dispatches pending messages for given connection.
[**connections_request**](MediatorApi.md#connections_request) | **GET** /mediator/connections | Retrieves the router&#x60;s connections.
[**reconnect_all**](MediatorApi.md#reconnect_all) | **GET** /mediator/reconnect-all | Re-establishes network connections for all mediator connections.
[**reconnect_route_request**](MediatorApi.md#reconnect_route_request) | **POST** /mediator/reconnect | Reconnect the agent with the router to re-establish lost connection.
[**register_route_request**](MediatorApi.md#register_route_request) | **POST** /mediator/register | Registers the agent with the router.
[**status_request**](MediatorApi.md#status_request) | **POST** /mediator/status | Status returns details about pending messages for given connection.
[**unregister_router**](MediatorApi.md#unregister_router) | **DELETE** /mediator/unregister | Unregisters the agent with the router.


# **batch_pickup_request**
> BatchPickupResponse batch_pickup_request(params=params)

BatchPickup dispatches pending messages for given connection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediatorApi()
params = swagger_client.BatchPickupRequest() # BatchPickupRequest | Params for dispatching pending messages for given connection.. (optional)

try:
    # BatchPickup dispatches pending messages for given connection.
    api_response = api_instance.batch_pickup_request(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediatorApi->batch_pickup_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**BatchPickupRequest**](BatchPickupRequest.md)| Params for dispatching pending messages for given connection.. | [optional] 

### Return type

[**BatchPickupResponse**](BatchPickupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connections_request**
> ConnectionsResponse connections_request()

Retrieves the router`s connections.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediatorApi()

try:
    # Retrieves the router`s connections.
    api_response = api_instance.connections_request()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediatorApi->connections_request: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConnectionsResponse**](ConnectionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconnect_all**
> GenericErrorBody reconnect_all()

Re-establishes network connections for all mediator connections.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediatorApi()

try:
    # Re-establishes network connections for all mediator connections.
    api_response = api_instance.reconnect_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediatorApi->reconnect_all: %s\n" % e)
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

# **reconnect_route_request**
> GenericErrorBody reconnect_route_request(params=params)

Reconnect the agent with the router to re-establish lost connection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediatorApi()
params = swagger_client.RegisterRoute() # RegisterRoute | Params for reconnecting the router (optional)

try:
    # Reconnect the agent with the router to re-establish lost connection.
    api_response = api_instance.reconnect_route_request(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediatorApi->reconnect_route_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**RegisterRoute**](RegisterRoute.md)| Params for reconnecting the router | [optional] 

### Return type

[**GenericErrorBody**](GenericErrorBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_route_request**
> object register_route_request(params=params)

Registers the agent with the router.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediatorApi()
params = swagger_client.RegisterRoute() # RegisterRoute | Params for registering the route (optional)

try:
    # Registers the agent with the router.
    api_response = api_instance.register_route_request(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediatorApi->register_route_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**RegisterRoute**](RegisterRoute.md)| Params for registering the route | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_request**
> StatusResponse status_request(params=params)

Status returns details about pending messages for given connection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediatorApi()
params = swagger_client.StatusRequest() # StatusRequest | Params for getting details of pending messages for given connection. (optional)

try:
    # Status returns details about pending messages for given connection.
    api_response = api_instance.status_request(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediatorApi->status_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**StatusRequest**](StatusRequest.md)| Params for getting details of pending messages for given connection. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_router**
> object unregister_router(params=params)

Unregisters the agent with the router.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediatorApi()
params = swagger_client.RegisterRoute() # RegisterRoute | Params for unregister the router (optional)

try:
    # Unregisters the agent with the router.
    api_response = api_instance.unregister_router(params=params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediatorApi->unregister_router: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**RegisterRoute**](RegisterRoute.md)| Params for unregister the router | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

