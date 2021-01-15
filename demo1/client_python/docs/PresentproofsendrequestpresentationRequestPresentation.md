# PresentproofsendrequestpresentationRequestPresentation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**comment** | **str** | Comment is a field that provides some human readable information about the proposed presentation. TODO: Should follow DIDComm conventions for l10n. [Issue #1300] | [optional] 
**formats** | [**list[Format]**](Format.md) | Formats contains an entry for each request_presentations~attach array entry, providing the the value of the attachment @id and the verifiable presentation request format and version of the attachment. | [optional] 
**request_presentationsattach** | [**list[Attachment]**](Attachment.md) | RequestPresentationsAttach is an array of attachments containing the acceptable verifiable presentation requests. | [optional] 
**will_confirm** | **bool** | WillConfirm is a field that defaults to \&quot;false\&quot; to indicate that the verifier will or will not send a post-presentation confirmation ack message. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


