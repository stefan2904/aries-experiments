# SendNewMessageArgs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**await_reply** | [**AwaitReply**](AwaitReply.md) |  | [optional] 
**connection_id** | **str** | Connection ID of the message destination This parameter takes precedence over all the other destination parameters. | [optional] 
**message_body** | **object** | Message body of the message | [optional] 
**service_endpoint** | [**ServiceEndpointDestinationParams**](ServiceEndpointDestinationParams.md) |  | [optional] 
**their_did** | **str** | DID of the destination. This parameter takes precedence over &#x60;ServiceEndpoint&#x60; destination parameter. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


