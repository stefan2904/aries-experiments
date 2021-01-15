# AttachmentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base64** | **str** | Base64 encoded data, when representing arbitrary content inline instead of via links. Optional. | [optional] 
**json** | **object** | JSON is a directly embedded JSON data, when representing content inline instead of via links, and when the content is natively conveyable as JSON. Optional. | [optional] 
**links** | **list[str]** | Links is a list of zero or more locations at which the content may be fetched. | [optional] 
**sha256** | **str** | Sha256 is a hash of the content. Optional. Used as an integrity check if content is inlined. if content is only referenced, then including this field makes the content tamper-evident. This may be redundant, if the content is stored in an inherently immutable container like content-addressable storage. This may also be undesirable, if dynamic content at a specified link is beneficial. Including a hash without including a way to fetch the content via link is a form of proof of existence. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


