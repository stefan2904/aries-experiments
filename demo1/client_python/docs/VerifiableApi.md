# swagger_client.VerifiableApi

All URIs are relative to *https://localhost:8082*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_presentation_req**](VerifiableApi.md#generate_presentation_req) | **POST** /verifiable/presentation/generate | Generates the verifiable presentation from a verifiable credential.
[**get_credential_by_name_req**](VerifiableApi.md#get_credential_by_name_req) | **GET** /verifiable/credential/name/{name} | Retrieves the verifiable credential by name.
[**get_credential_req**](VerifiableApi.md#get_credential_req) | **GET** /verifiable/credential/{id} | Retrieves the verifiable credential.
[**get_credentials**](VerifiableApi.md#get_credentials) | **GET** /verifiable/credentials | Retrieves the verifiable credentials.
[**get_presentation_req**](VerifiableApi.md#get_presentation_req) | **GET** /verifiable/presentation/{id} | Retrieves the verifiable presentation.
[**remove_credential_by_name_req**](VerifiableApi.md#remove_credential_by_name_req) | **POST** /verifiable/credential/remove/name/{name} | Removes a verifiable credential by name.
[**remove_presentation_by_name_req**](VerifiableApi.md#remove_presentation_by_name_req) | **POST** /verifiable/presentation/remove/name/{name} | Removes a verifiable presentation by name.
[**save_credential_req**](VerifiableApi.md#save_credential_req) | **POST** /verifiable/credential | Saves the verifiable credential.
[**save_presentation_req**](VerifiableApi.md#save_presentation_req) | **POST** /verifiable/presentation | Saves the verifiable presentation.
[**sign_credential_req**](VerifiableApi.md#sign_credential_req) | **POST** /verifiable/signcredential | Signs given credential.
[**validate_credential_req**](VerifiableApi.md#validate_credential_req) | **POST** /verifiable/credential/validate | Validates the verifiable credential.


# **generate_presentation_req**
> generate_presentation_req(params=params)

Generates the verifiable presentation from a verifiable credential.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifiableApi()
params = swagger_client.PresentationRequest() # PresentationRequest | Params for generating the verifiable presentation (pass the vc document as a raw JSON) (optional)

try:
    # Generates the verifiable presentation from a verifiable credential.
    api_instance.generate_presentation_req(params=params)
except ApiException as e:
    print("Exception when calling VerifiableApi->generate_presentation_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**PresentationRequest**](PresentationRequest.md)| Params for generating the verifiable presentation (pass the vc document as a raw JSON) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credential_by_name_req**
> get_credential_by_name_req(name)

Retrieves the verifiable credential by name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifiableApi()
name = 'name_example' # str | VC Name

try:
    # Retrieves the verifiable credential by name.
    api_instance.get_credential_by_name_req(name)
except ApiException as e:
    print("Exception when calling VerifiableApi->get_credential_by_name_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| VC Name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credential_req**
> get_credential_req(id)

Retrieves the verifiable credential.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifiableApi()
id = 'id_example' # str | VC ID - pass base64 version of the ID

try:
    # Retrieves the verifiable credential.
    api_instance.get_credential_req(id)
except ApiException as e:
    print("Exception when calling VerifiableApi->get_credential_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| VC ID - pass base64 version of the ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credentials**
> list[Record] get_credentials()

Retrieves the verifiable credentials.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifiableApi()

try:
    # Retrieves the verifiable credentials.
    api_response = api_instance.get_credentials()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerifiableApi->get_credentials: %s\n" % e)
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

# **get_presentation_req**
> get_presentation_req(id)

Retrieves the verifiable presentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifiableApi()
id = 'id_example' # str | VP ID - pass base64 version of the ID

try:
    # Retrieves the verifiable presentation.
    api_instance.get_presentation_req(id)
except ApiException as e:
    print("Exception when calling VerifiableApi->get_presentation_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| VP ID - pass base64 version of the ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_credential_by_name_req**
> EmptyRes remove_credential_by_name_req(name)

Removes a verifiable credential by name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifiableApi()
name = 'name_example' # str | VC Name

try:
    # Removes a verifiable credential by name.
    api_response = api_instance.remove_credential_by_name_req(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerifiableApi->remove_credential_by_name_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| VC Name | 

### Return type

[**EmptyRes**](EmptyRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_presentation_by_name_req**
> EmptyRes remove_presentation_by_name_req(name)

Removes a verifiable presentation by name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifiableApi()
name = 'name_example' # str | VC Name

try:
    # Removes a verifiable presentation by name.
    api_response = api_instance.remove_presentation_by_name_req(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerifiableApi->remove_presentation_by_name_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| VC Name | 

### Return type

[**EmptyRes**](EmptyRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_credential_req**
> save_credential_req(params=params)

Saves the verifiable credential.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifiableApi()
params = swagger_client.CredentialExt() # CredentialExt | Params for saving the verifiable credential (pass the vc document as a string) (optional)

try:
    # Saves the verifiable credential.
    api_instance.save_credential_req(params=params)
except ApiException as e:
    print("Exception when calling VerifiableApi->save_credential_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**CredentialExt**](CredentialExt.md)| Params for saving the verifiable credential (pass the vc document as a string) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_presentation_req**
> save_presentation_req(params=params)

Saves the verifiable presentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifiableApi()
params = swagger_client.PresentationExt() # PresentationExt | Params for saving the verifiable presentation (optional)

try:
    # Saves the verifiable presentation.
    api_instance.save_presentation_req(params=params)
except ApiException as e:
    print("Exception when calling VerifiableApi->save_presentation_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**PresentationExt**](PresentationExt.md)| Params for saving the verifiable presentation | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_credential_req**
> sign_credential_req(params=params)

Signs given credential.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifiableApi()
params = swagger_client.SignCredentialRequest() # SignCredentialRequest | Params for signing a credential (optional)

try:
    # Signs given credential.
    api_instance.sign_credential_req(params=params)
except ApiException as e:
    print("Exception when calling VerifiableApi->sign_credential_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**SignCredentialRequest**](SignCredentialRequest.md)| Params for signing a credential | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_credential_req**
> validate_credential_req(params=params)

Validates the verifiable credential.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifiableApi()
params = swagger_client.Credential() # Credential | Params for validating the verifiable credential (pass the vc document as a string) (optional)

try:
    # Validates the verifiable credential.
    api_instance.validate_credential_req(params=params)
except ApiException as e:
    print("Exception when calling VerifiableApi->validate_credential_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**Credential**](Credential.md)| Params for validating the verifiable credential (pass the vc document as a string) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

