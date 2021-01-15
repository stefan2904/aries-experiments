# PresentationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge** | **str** | Challenge is a random or pseudo-random value option authentication | [optional] 
**created** | **datetime** | Created date of the proof. If omitted current system time will be used. | [optional] 
**did** | **str** |  | [optional] 
**domain** | **str** | Domain is operational domain of a digital proof. | [optional] 
**presentation** | **object** |  | [optional] 
**signature_type** | **str** | SignatureType signature type used for signing | [optional] 
**skip_verify** | **bool** | SkipVerify can be used to skip verification of &#x60;VerifiableCredentials&#x60; provided. | [optional] 
**verifiable_credential** | **list[object]** |  | [optional] 
**verification_method** | **str** | VerificationMethod is the URI of the verificationMethod used for the proof. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


