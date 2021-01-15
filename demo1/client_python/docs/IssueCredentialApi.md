# swagger_client.IssueCredentialApi

All URIs are relative to *https://localhost:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issue_credential_accept_credential**](IssueCredentialApi.md#issue_credential_accept_credential) | **POST** /issuecredential/{piid}/accept-credential | Accepts a credential.
[**issue_credential_accept_offer**](IssueCredentialApi.md#issue_credential_accept_offer) | **POST** /issuecredential/{piid}/accept-offer | Accepts an offer.
[**issue_credential_accept_problem_report**](IssueCredentialApi.md#issue_credential_accept_problem_report) | **POST** /issuecredential/{piid}/accept-problem-report | Accepts a problem report.
[**issue_credential_accept_proposal**](IssueCredentialApi.md#issue_credential_accept_proposal) | **POST** /issuecredential/{piid}/accept-proposal | Accepts a proposal.
[**issue_credential_accept_request**](IssueCredentialApi.md#issue_credential_accept_request) | **POST** /issuecredential/{piid}/accept-request | Accepts a request.
[**issue_credential_actions**](IssueCredentialApi.md#issue_credential_actions) | **GET** /issuecredential/actions | Returns pending actions that have not yet to be executed or cancelled.
[**issue_credential_decline_credential**](IssueCredentialApi.md#issue_credential_decline_credential) | **POST** /issuecredential/{piid}/decline-credential | Declines a credential.
[**issue_credential_decline_offer**](IssueCredentialApi.md#issue_credential_decline_offer) | **POST** /issuecredential/{piid}/decline-offer | Declines an offer.
[**issue_credential_decline_proposal**](IssueCredentialApi.md#issue_credential_decline_proposal) | **POST** /issuecredential/{piid}/decline-proposal | Declines a proposal.
[**issue_credential_decline_request**](IssueCredentialApi.md#issue_credential_decline_request) | **POST** /issuecredential/{piid}/decline-request | Declines a request.
[**issue_credential_negotiate_proposal**](IssueCredentialApi.md#issue_credential_negotiate_proposal) | **POST** /issuecredential/{piid}/negotiate-proposal | Is used when the Holder wants to negotiate about an offer he received.
[**issue_credential_send_offer**](IssueCredentialApi.md#issue_credential_send_offer) | **POST** /issuecredential/send-offer | Sends an offer.
[**issue_credential_send_proposal**](IssueCredentialApi.md#issue_credential_send_proposal) | **POST** /issuecredential/send-proposal | Sends a proposal.
[**issue_credential_send_request**](IssueCredentialApi.md#issue_credential_send_request) | **POST** /issuecredential/send-request | Sends a request.


# **issue_credential_accept_credential**
> object issue_credential_accept_credential(piid, body=body)

Accepts a credential.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialApi()
piid = 'piid_example' # str | Protocol instance ID
body = swagger_client.Body9() # Body9 |  (optional)

try:
    # Accepts a credential.
    api_response = api_instance.issue_credential_accept_credential(piid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialApi->issue_credential_accept_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **body** | [**Body9**](Body9.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_accept_offer**
> object issue_credential_accept_offer(piid)

Accepts an offer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialApi()
piid = 'piid_example' # str | Protocol instance ID

try:
    # Accepts an offer.
    api_response = api_instance.issue_credential_accept_offer(piid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialApi->issue_credential_accept_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_accept_problem_report**
> object issue_credential_accept_problem_report(piid)

Accepts a problem report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialApi()
piid = 'piid_example' # str | Protocol instance ID

try:
    # Accepts a problem report.
    api_response = api_instance.issue_credential_accept_problem_report(piid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialApi->issue_credential_accept_problem_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_accept_proposal**
> object issue_credential_accept_proposal(piid, body=body)

Accepts a proposal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialApi()
piid = 'piid_example' # str | Protocol instance ID
body = swagger_client.Body10() # Body10 |  (optional)

try:
    # Accepts a proposal.
    api_response = api_instance.issue_credential_accept_proposal(piid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialApi->issue_credential_accept_proposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **body** | [**Body10**](Body10.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_accept_request**
> object issue_credential_accept_request(piid, body=body)

Accepts a request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialApi()
piid = 'piid_example' # str | Protocol instance ID
body = swagger_client.Body11() # Body11 |  (optional)

try:
    # Accepts a request.
    api_response = api_instance.issue_credential_accept_request(piid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialApi->issue_credential_accept_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **body** | [**Body11**](Body11.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_actions**
> InlineResponse2007 issue_credential_actions()

Returns pending actions that have not yet to be executed or cancelled.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialApi()

try:
    # Returns pending actions that have not yet to be executed or cancelled.
    api_response = api_instance.issue_credential_actions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialApi->issue_credential_actions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_decline_credential**
> object issue_credential_decline_credential(piid, reason=reason)

Declines a credential.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialApi()
piid = 'piid_example' # str | Protocol instance ID
reason = 'reason_example' # str | Reason is an explanation of why it was declined (optional)

try:
    # Declines a credential.
    api_response = api_instance.issue_credential_decline_credential(piid, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialApi->issue_credential_decline_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **reason** | **str**| Reason is an explanation of why it was declined | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_decline_offer**
> object issue_credential_decline_offer(piid, reason=reason)

Declines an offer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialApi()
piid = 'piid_example' # str | Protocol instance ID
reason = 'reason_example' # str | Reason is an explanation of why it was declined (optional)

try:
    # Declines an offer.
    api_response = api_instance.issue_credential_decline_offer(piid, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialApi->issue_credential_decline_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **reason** | **str**| Reason is an explanation of why it was declined | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_decline_proposal**
> object issue_credential_decline_proposal(piid, reason=reason)

Declines a proposal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialApi()
piid = 'piid_example' # str | Protocol instance ID
reason = 'reason_example' # str | Reason is an explanation of why it was declined (optional)

try:
    # Declines a proposal.
    api_response = api_instance.issue_credential_decline_proposal(piid, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialApi->issue_credential_decline_proposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **reason** | **str**| Reason is an explanation of why it was declined | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_decline_request**
> object issue_credential_decline_request(piid, reason=reason)

Declines a request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialApi()
piid = 'piid_example' # str | Protocol instance ID
reason = 'reason_example' # str | Reason is an explanation of why it was declined (optional)

try:
    # Declines a request.
    api_response = api_instance.issue_credential_decline_request(piid, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialApi->issue_credential_decline_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **reason** | **str**| Reason is an explanation of why it was declined | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_negotiate_proposal**
> object issue_credential_negotiate_proposal(piid, body=body)

Is used when the Holder wants to negotiate about an offer he received.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialApi()
piid = 'piid_example' # str | Protocol instance ID
body = swagger_client.Body12() # Body12 |  (optional)

try:
    # Is used when the Holder wants to negotiate about an offer he received.
    api_response = api_instance.issue_credential_negotiate_proposal(piid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialApi->issue_credential_negotiate_proposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **body** | [**Body12**](Body12.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_send_offer**
> InlineResponse2008 issue_credential_send_offer(body=body)

Sends an offer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialApi()
body = swagger_client.Body6() # Body6 |  (optional)

try:
    # Sends an offer.
    api_response = api_instance.issue_credential_send_offer(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialApi->issue_credential_send_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body6**](Body6.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_send_proposal**
> InlineResponse2008 issue_credential_send_proposal(body=body)

Sends a proposal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialApi()
body = swagger_client.Body7() # Body7 |  (optional)

try:
    # Sends a proposal.
    api_response = api_instance.issue_credential_send_proposal(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialApi->issue_credential_send_proposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body7**](Body7.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_credential_send_request**
> InlineResponse2008 issue_credential_send_request(body=body)

Sends a request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssueCredentialApi()
body = swagger_client.Body8() # Body8 |  (optional)

try:
    # Sends a request.
    api_response = api_instance.issue_credential_send_request(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssueCredentialApi->issue_credential_send_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body8**](Body8.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

