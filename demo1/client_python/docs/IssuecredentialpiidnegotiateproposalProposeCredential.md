# IssuecredentialpiidnegotiateproposalProposeCredential

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**comment** | **str** | Comment is an optional field that provides human readable information about this Credential Offer, so the offer can be evaluated by human judgment. TODO: Should follow DIDComm conventions for l10n. [Issue #1300] | [optional] 
**credential_proposal** | [**PreviewCredential**](PreviewCredential.md) |  | [optional] 
**filterattach** | [**list[Attachment]**](Attachment.md) | FilterAttach is an array of attachments that further define the credential being proposed. This might be used to clarify which formats or format versions are wanted. | [optional] 
**formats** | [**list[Format]**](Format.md) | Formats contains an entry for each filter~attach array entry, providing the the value of the attachment @id and the verifiable credential format and version of the attachment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


