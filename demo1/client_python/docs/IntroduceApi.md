# swagger_client.IntroduceApi

All URIs are relative to *https://localhost:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**introduce_accept_problem_report**](IntroduceApi.md#introduce_accept_problem_report) | **POST** /introduce/{piid}/accept-problem-report | Accepts a problem report.
[**introduce_accept_proposal**](IntroduceApi.md#introduce_accept_proposal) | **POST** /introduce/{piid}/accept-proposal | Accepts a proposal.
[**introduce_accept_proposal_with_oob_request**](IntroduceApi.md#introduce_accept_proposal_with_oob_request) | **POST** /introduce/{piid}/accept-proposal-with-oob-request | Accepts a proposal with OOBRequest.
[**introduce_accept_request_with_public_oob_request**](IntroduceApi.md#introduce_accept_request_with_public_oob_request) | **POST** /introduce/{piid}/accept-request-with-public-oob-request | Accept a request with public OOBRequest.
[**introduce_accept_request_with_recipients**](IntroduceApi.md#introduce_accept_request_with_recipients) | **POST** /introduce/{piid}/accept-request-with-recipients | Accept a request with recipients.
[**introduce_actions**](IntroduceApi.md#introduce_actions) | **GET** /introduce/actions | Returns pending actions that have not yet to be executed or cancelled.
[**introduce_decline_proposal**](IntroduceApi.md#introduce_decline_proposal) | **POST** /introduce/{piid}/decline-proposal | Declines a proposal.
[**introduce_decline_request**](IntroduceApi.md#introduce_decline_request) | **POST** /introduce/{piid}/decline-request | Declines a request.
[**introduce_send_proposal**](IntroduceApi.md#introduce_send_proposal) | **POST** /introduce/send-proposal | Sends a proposal.
[**introduce_send_proposal_with_oob_request**](IntroduceApi.md#introduce_send_proposal_with_oob_request) | **POST** /introduce/send-proposal-with-oob-request | Sends a proposal with OOBRequest.
[**introduce_send_request**](IntroduceApi.md#introduce_send_request) | **POST** /introduce/send-request | Sends a request.


# **introduce_accept_problem_report**
> object introduce_accept_problem_report(piid)

Accepts a problem report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntroduceApi()
piid = 'piid_example' # str | Protocol instance ID

try:
    # Accepts a problem report.
    api_response = api_instance.introduce_accept_problem_report(piid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntroduceApi->introduce_accept_problem_report: %s\n" % e)
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

# **introduce_accept_proposal**
> object introduce_accept_proposal(piid)

Accepts a proposal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntroduceApi()
piid = 'piid_example' # str | Protocol instance ID

try:
    # Accepts a proposal.
    api_response = api_instance.introduce_accept_proposal(piid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntroduceApi->introduce_accept_proposal: %s\n" % e)
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

# **introduce_accept_proposal_with_oob_request**
> object introduce_accept_proposal_with_oob_request(piid, body=body)

Accepts a proposal with OOBRequest.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntroduceApi()
piid = 'piid_example' # str | Protocol instance ID
body = swagger_client.Body3() # Body3 |  (optional)

try:
    # Accepts a proposal with OOBRequest.
    api_response = api_instance.introduce_accept_proposal_with_oob_request(piid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntroduceApi->introduce_accept_proposal_with_oob_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **body** | [**Body3**](Body3.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **introduce_accept_request_with_public_oob_request**
> object introduce_accept_request_with_public_oob_request(piid, body=body)

Accept a request with public OOBRequest.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntroduceApi()
piid = 'piid_example' # str | Protocol instance ID
body = swagger_client.Body4() # Body4 |  (optional)

try:
    # Accept a request with public OOBRequest.
    api_response = api_instance.introduce_accept_request_with_public_oob_request(piid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntroduceApi->introduce_accept_request_with_public_oob_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **body** | [**Body4**](Body4.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **introduce_accept_request_with_recipients**
> object introduce_accept_request_with_recipients(piid, body=body)

Accept a request with recipients.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntroduceApi()
piid = 'piid_example' # str | Protocol instance ID
body = swagger_client.Body5() # Body5 |  (optional)

try:
    # Accept a request with recipients.
    api_response = api_instance.introduce_accept_request_with_recipients(piid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntroduceApi->introduce_accept_request_with_recipients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **body** | [**Body5**](Body5.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **introduce_actions**
> InlineResponse2007 introduce_actions()

Returns pending actions that have not yet to be executed or cancelled.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntroduceApi()

try:
    # Returns pending actions that have not yet to be executed or cancelled.
    api_response = api_instance.introduce_actions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntroduceApi->introduce_actions: %s\n" % e)
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

# **introduce_decline_proposal**
> object introduce_decline_proposal(piid, reason=reason)

Declines a proposal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntroduceApi()
piid = 'piid_example' # str | Protocol instance ID
reason = 'reason_example' # str | Reason is an explanation of why it was declined (optional)

try:
    # Declines a proposal.
    api_response = api_instance.introduce_decline_proposal(piid, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntroduceApi->introduce_decline_proposal: %s\n" % e)
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

# **introduce_decline_request**
> object introduce_decline_request(piid, reason=reason)

Declines a request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntroduceApi()
piid = 'piid_example' # str | Protocol instance ID
reason = 'reason_example' # str | Reason is an explanation of why it was declined (optional)

try:
    # Declines a request.
    api_response = api_instance.introduce_decline_request(piid, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntroduceApi->introduce_decline_request: %s\n" % e)
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

# **introduce_send_proposal**
> InlineResponse2008 introduce_send_proposal(body=body)

Sends a proposal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntroduceApi()
body = swagger_client.Body() # Body |  (optional)

try:
    # Sends a proposal.
    api_response = api_instance.introduce_send_proposal(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntroduceApi->introduce_send_proposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **introduce_send_proposal_with_oob_request**
> InlineResponse2008 introduce_send_proposal_with_oob_request(body=body)

Sends a proposal with OOBRequest.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntroduceApi()
body = swagger_client.Body1() # Body1 |  (optional)

try:
    # Sends a proposal with OOBRequest.
    api_response = api_instance.introduce_send_proposal_with_oob_request(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntroduceApi->introduce_send_proposal_with_oob_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **introduce_send_request**
> InlineResponse2008 introduce_send_request(body=body)

Sends a request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntroduceApi()
body = swagger_client.Body2() # Body2 |  (optional)

try:
    # Sends a request.
    api_response = api_instance.introduce_send_request(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntroduceApi->introduce_send_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

