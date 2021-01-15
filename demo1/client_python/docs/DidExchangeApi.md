# swagger_client.DidExchangeApi

All URIs are relative to *https://localhost:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_invitation**](DidExchangeApi.md#accept_invitation) | **POST** /connections/{id}/accept-invitation | Accept a stored connection invitation....
[**accept_request**](DidExchangeApi.md#accept_request) | **POST** /connections/{id}/accept-request | Accepts a stored connection request.
[**create_connection**](DidExchangeApi.md#create_connection) | **POST** /connections/create | Saves the connection record.
[**create_invitation**](DidExchangeApi.md#create_invitation) | **POST** /connections/create-invitation | Creates a new connection invitation....
[**get_connection**](DidExchangeApi.md#get_connection) | **GET** /connections/{id} | Fetch a single connection record.
[**implicit_invitation**](DidExchangeApi.md#implicit_invitation) | **POST** /connections/create-implicit-invitation | Create implicit invitation using inviter DID.
[**query_connections**](DidExchangeApi.md#query_connections) | **GET** /connections | query agent to agent connections.
[**receive_invitation**](DidExchangeApi.md#receive_invitation) | **POST** /connections/receive-invitation | Receive a new connection invitation....
[**remove_connection**](DidExchangeApi.md#remove_connection) | **POST** /connections/{id}/remove | Removes given connection record.


# **accept_invitation**
> InlineResponse2006 accept_invitation(id, public=public, router_connections=router_connections)

Accept a stored connection invitation....

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DidExchangeApi()
id = 'id_example' # str | Connection ID
public = 'public_example' # str | Optional Public DID to be used for this request (optional)
router_connections = 'router_connections_example' # str | Optional specifies router connections (comma-separated values) (optional)

try:
    # Accept a stored connection invitation....
    api_response = api_instance.accept_invitation(id, public=public, router_connections=router_connections)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidExchangeApi->accept_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Connection ID | 
 **public** | **str**| Optional Public DID to be used for this request | [optional] 
 **router_connections** | **str**| Optional specifies router connections (comma-separated values) | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accept_request**
> ExchangeResponse accept_request(id, public=public, router_connections=router_connections)

Accepts a stored connection request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DidExchangeApi()
id = 'id_example' # str | Connection ID
public = 'public_example' # str | Optional Public DID to be used for this invitation request (optional)
router_connections = 'router_connections_example' # str | Optional specifies router connections (comma-separated values) (optional)

try:
    # Accepts a stored connection request.
    api_response = api_instance.accept_request(id, public=public, router_connections=router_connections)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidExchangeApi->accept_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Connection ID | 
 **public** | **str**| Optional Public DID to be used for this invitation request | [optional] 
 **router_connections** | **str**| Optional specifies router connections (comma-separated values) | [optional] 

### Return type

[**ExchangeResponse**](ExchangeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connection**
> InlineResponse2001 create_connection(request)

Saves the connection record.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DidExchangeApi()
request = swagger_client.CreateConnectionRequest() # CreateConnectionRequest | Params for creating a connection.

try:
    # Saves the connection record.
    api_response = api_instance.create_connection(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidExchangeApi->create_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateConnectionRequest**](CreateConnectionRequest.md)| Params for creating a connection. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invitation**
> InlineResponse2003 create_invitation(alias=alias, public=public, router_connection_id=router_connection_id)

Creates a new connection invitation....

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DidExchangeApi()
alias = 'alias_example' # str | The Alias to be used in invitation to be created (optional)
public = 'public_example' # str | Optional public DID to be used in invitation (optional)
router_connection_id = 'router_connection_id_example' # str | Optional specifies router connection id (optional)

try:
    # Creates a new connection invitation....
    api_response = api_instance.create_invitation(alias=alias, public=public, router_connection_id=router_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidExchangeApi->create_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| The Alias to be used in invitation to be created | [optional] 
 **public** | **str**| Optional public DID to be used in invitation | [optional] 
 **router_connection_id** | **str**| Optional specifies router connection id | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection**
> InlineResponse2005 get_connection(id)

Fetch a single connection record.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DidExchangeApi()
id = 'id_example' # str | The ID of the connection to get

try:
    # Fetch a single connection record.
    api_response = api_instance.get_connection(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidExchangeApi->get_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the connection to get | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **implicit_invitation**
> InlineResponse2002 implicit_invitation(their_did=their_did, their_label=their_label, my_did=my_did, my_label=my_label, router_connections=router_connections)

Create implicit invitation using inviter DID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DidExchangeApi()
their_did = 'their_did_example' # str | InviterDID (optional)
their_label = 'their_label_example' # str | Optional inviter label (optional)
my_did = 'my_did_example' # str | Optional invitee did (optional)
my_label = 'my_label_example' # str | Optional invitee label (optional)
router_connections = 'router_connections_example' # str | Optional specifies router connections (comma-separated values) (optional)

try:
    # Create implicit invitation using inviter DID.
    api_response = api_instance.implicit_invitation(their_did=their_did, their_label=their_label, my_did=my_did, my_label=my_label, router_connections=router_connections)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidExchangeApi->implicit_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **their_did** | **str**| InviterDID | [optional] 
 **their_label** | **str**| Optional inviter label | [optional] 
 **my_did** | **str**| Optional invitee did | [optional] 
 **my_label** | **str**| Optional invitee label | [optional] 
 **router_connections** | **str**| Optional specifies router connections (comma-separated values) | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_connections**
> InlineResponse200 query_connections(alias=alias, initiator=initiator, invitation_key=invitation_key, invitation_id=invitation_id, parent_thread_id=parent_thread_id, my_did=my_did, state=state, their_did=their_did, their_role=their_role)

query agent to agent connections.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DidExchangeApi()
alias = 'alias_example' # str | Alias of connection invitation (optional)
initiator = 'initiator_example' # str | Initiator is Connection invitation initiator (optional)
invitation_key = 'invitation_key_example' # str | Invitation key (optional)
invitation_id = 'invitation_id_example' # str | Invitation ID (optional)
parent_thread_id = 'parent_thread_id_example' # str | Parent threadID (optional)
my_did = 'my_did_example' # str | MyDID is DID of the agent (optional)
state = 'state_example' # str | State of the connection invitation (optional)
their_did = 'their_did_example' # str | TheirDID is other party's DID (optional)
their_role = 'their_role_example' # str | TheirRole is other party's role (optional)

try:
    # query agent to agent connections.
    api_response = api_instance.query_connections(alias=alias, initiator=initiator, invitation_key=invitation_key, invitation_id=invitation_id, parent_thread_id=parent_thread_id, my_did=my_did, state=state, their_did=their_did, their_role=their_role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidExchangeApi->query_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| Alias of connection invitation | [optional] 
 **initiator** | **str**| Initiator is Connection invitation initiator | [optional] 
 **invitation_key** | **str**| Invitation key | [optional] 
 **invitation_id** | **str**| Invitation ID | [optional] 
 **parent_thread_id** | **str**| Parent threadID | [optional] 
 **my_did** | **str**| MyDID is DID of the agent | [optional] 
 **state** | **str**| State of the connection invitation | [optional] 
 **their_did** | **str**| TheirDID is other party&#39;s DID | [optional] 
 **their_role** | **str**| TheirRole is other party&#39;s role | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive_invitation**
> InlineResponse2004 receive_invitation(invitation)

Receive a new connection invitation....

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DidExchangeApi()
invitation = swagger_client.Invitation() # Invitation | The Invitation Request to receive

try:
    # Receive a new connection invitation....
    api_response = api_instance.receive_invitation(invitation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidExchangeApi->receive_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation** | [**Invitation**](Invitation.md)| The Invitation Request to receive | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_connection**
> object remove_connection(id)

Removes given connection record.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DidExchangeApi()
id = 'id_example' # str | The ID of the connection record to remove

try:
    # Removes given connection record.
    api_response = api_instance.remove_connection(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DidExchangeApi->remove_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the connection record to remove | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

