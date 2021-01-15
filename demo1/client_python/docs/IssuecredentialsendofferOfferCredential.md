# IssuecredentialsendofferOfferCredential

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**comment** | **str** | Comment is an optional field that provides human readable information about this Credential Offer, so the offer can be evaluated by human judgment. TODO: Should follow DIDComm conventions for l10n. [Issue #1300]. | [optional] 
**credential_preview** | [**PreviewCredential**](PreviewCredential.md) |  | [optional] 
**formats** | [**list[Format]**](Format.md) | Formats contains an entry for each offers~attach array entry, providing the the value of the attachment @id and the verifiable credential format and version of the attachment. | [optional] 
**offersattach** | [**list[Attachment]**](Attachment.md) | OffersAttach is a slice of attachments that further define the credential being offered. This might be used to clarify which formats or format versions will be issued. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


