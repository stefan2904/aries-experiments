# swagger_client.PresentProofApi

All URIs are relative to *https://localhost:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**present_proof_accept_presentation**](PresentProofApi.md#present_proof_accept_presentation) | **POST** /presentproof/{piid}/accept-presentation | Accepts a presentation.
[**present_proof_accept_problem_report**](PresentProofApi.md#present_proof_accept_problem_report) | **POST** /presentproof/{piid}/accept-problem-report | Accepts a problem report.
[**present_proof_accept_propose_presentation**](PresentProofApi.md#present_proof_accept_propose_presentation) | **POST** /presentproof/{piid}/accept-propose-presentation | Accepts a propose presentation.
[**present_proof_accept_request_presentation**](PresentProofApi.md#present_proof_accept_request_presentation) | **POST** /presentproof/{piid}/accept-request-presentation | Accepts a request presentation.
[**present_proof_actions**](PresentProofApi.md#present_proof_actions) | **GET** /presentproof/actions | Returns pending actions that have not yet to be executed or cancelled.
[**present_proof_decline_presentation**](PresentProofApi.md#present_proof_decline_presentation) | **POST** /presentproof/{piid}/decline-presentation | Declines a presentation.
[**present_proof_decline_propose_presentation**](PresentProofApi.md#present_proof_decline_propose_presentation) | **POST** /presentproof/{piid}/decline-propose-presentation | Declines a propose presentation.
[**present_proof_decline_request_presentation**](PresentProofApi.md#present_proof_decline_request_presentation) | **POST** /presentproof/{piid}/decline-request-presentation | Declines a request presentation.
[**present_proof_negotiate_request_presentation**](PresentProofApi.md#present_proof_negotiate_request_presentation) | **POST** /presentproof/{piid}/negotiate-request-presentation | Is used by the Prover to counter a presentation request they received with a proposal.
[**present_proof_send_propose_presentation**](PresentProofApi.md#present_proof_send_propose_presentation) | **POST** /presentproof/send-propose-presentation | Sends a propose presentation.
[**present_proof_send_request_presentation**](PresentProofApi.md#present_proof_send_request_presentation) | **POST** /presentproof/send-request-presentation | Sends a request presentation.


# **present_proof_accept_presentation**
> object present_proof_accept_presentation(piid, body=body)

Accepts a presentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
piid = 'piid_example' # str | Protocol instance ID
body = swagger_client.Body19() # Body19 |  (optional)

try:
    # Accepts a presentation.
    api_response = api_instance.present_proof_accept_presentation(piid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_accept_presentation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **body** | [**Body19**](Body19.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_accept_problem_report**
> object present_proof_accept_problem_report(piid)

Accepts a problem report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
piid = 'piid_example' # str | Protocol instance ID

try:
    # Accepts a problem report.
    api_response = api_instance.present_proof_accept_problem_report(piid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_accept_problem_report: %s\n" % e)
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

# **present_proof_accept_propose_presentation**
> object present_proof_accept_propose_presentation(piid, body=body)

Accepts a propose presentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
piid = 'piid_example' # str | Protocol instance ID
body = swagger_client.Body20() # Body20 |  (optional)

try:
    # Accepts a propose presentation.
    api_response = api_instance.present_proof_accept_propose_presentation(piid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_accept_propose_presentation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **body** | [**Body20**](Body20.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_accept_request_presentation**
> object present_proof_accept_request_presentation(piid, body=body)

Accepts a request presentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
piid = 'piid_example' # str | Protocol instance ID
body = swagger_client.Body21() # Body21 |  (optional)

try:
    # Accepts a request presentation.
    api_response = api_instance.present_proof_accept_request_presentation(piid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_accept_request_presentation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **body** | [**Body21**](Body21.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_actions**
> InlineResponse2007 present_proof_actions()

Returns pending actions that have not yet to be executed or cancelled.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()

try:
    # Returns pending actions that have not yet to be executed or cancelled.
    api_response = api_instance.present_proof_actions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_actions: %s\n" % e)
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

# **present_proof_decline_presentation**
> object present_proof_decline_presentation(piid, reason=reason)

Declines a presentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
piid = 'piid_example' # str | Protocol instance ID
reason = 'reason_example' # str | Reason is an explanation of why it was declined (optional)

try:
    # Declines a presentation.
    api_response = api_instance.present_proof_decline_presentation(piid, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_decline_presentation: %s\n" % e)
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

# **present_proof_decline_propose_presentation**
> object present_proof_decline_propose_presentation(piid, reason=reason)

Declines a propose presentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
piid = 'piid_example' # str | Protocol instance ID
reason = 'reason_example' # str | Reason is an explanation of why it was declined (optional)

try:
    # Declines a propose presentation.
    api_response = api_instance.present_proof_decline_propose_presentation(piid, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_decline_propose_presentation: %s\n" % e)
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

# **present_proof_decline_request_presentation**
> object present_proof_decline_request_presentation(piid, reason=reason)

Declines a request presentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
piid = 'piid_example' # str | Protocol instance ID
reason = 'reason_example' # str | Reason is an explanation of why it was declined (optional)

try:
    # Declines a request presentation.
    api_response = api_instance.present_proof_decline_request_presentation(piid, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_decline_request_presentation: %s\n" % e)
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

# **present_proof_negotiate_request_presentation**
> object present_proof_negotiate_request_presentation(piid, body=body)

Is used by the Prover to counter a presentation request they received with a proposal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
piid = 'piid_example' # str | Protocol instance ID
body = swagger_client.Body22() # Body22 |  (optional)

try:
    # Is used by the Prover to counter a presentation request they received with a proposal.
    api_response = api_instance.present_proof_negotiate_request_presentation(piid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_negotiate_request_presentation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **piid** | **str**| Protocol instance ID | 
 **body** | [**Body22**](Body22.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_send_propose_presentation**
> InlineResponse2008 present_proof_send_propose_presentation(body=body)

Sends a propose presentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
body = swagger_client.Body17() # Body17 |  (optional)

try:
    # Sends a propose presentation.
    api_response = api_instance.present_proof_send_propose_presentation(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_send_propose_presentation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body17**](Body17.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **present_proof_send_request_presentation**
> InlineResponse2008 present_proof_send_request_presentation(body=body)

Sends a request presentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresentProofApi()
body = swagger_client.Body18() # Body18 |  (optional)

try:
    # Sends a request presentation.
    api_response = api_instance.present_proof_send_request_presentation(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresentProofApi->present_proof_send_request_presentation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body18**](Body18.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

