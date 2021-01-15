# PresentproofpiidnegotiaterequestpresentationProposePresentation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**comment** | **str** | Comment is a field that provides some human readable information about the proposed presentation. TODO: Should follow DIDComm conventions for l10n. [Issue #1300] | [optional] 
**formats** | [**list[Format]**](Format.md) | Formats contains an entry for each proposal~attach array entry, including an optional value of the attachment @id (if attachments are present) and the verifiable presentation format and version of the attachment. | [optional] 
**proposalattach** | [**list[Attachment]**](Attachment.md) | FilterAttach is an array of attachments that further define the presentation request being proposed. This might be used to clarify which formats or format versions are wanted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


