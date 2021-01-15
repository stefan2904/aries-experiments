# Attachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is a JSON-LD construct that uniquely identifies attached content within the scope of a given message. Recommended on appended attachment descriptors. Possible but generally unused on embedded attachment descriptors. Never required if no references to the attachment exist; if omitted, then there is no way to refer to the attachment later in the thread, in error messages, and so forth. Because @id is used to compose URIs, it is recommended that this name be brief and avoid spaces and other characters that require URI escaping. | [optional] 
**byte_count** | **int** | ByteCount is an optional, and mostly relevant when content is included by reference instead of by value. Lets the receiver guess how expensive it will be, in time, bandwidth, and storage, to fully fetch the attachment. | [optional] 
**data** | [**AttachmentData**](AttachmentData.md) |  | [optional] 
**description** | **str** | Description is an optional human-readable description of the content. | [optional] 
**filename** | **str** | FileName is a hint about the name that might be used if this attachment is persisted as a file. It is not required, and need not be unique. If this field is present and mime-type is not, the extension on the filename may be used to infer a MIME type. | [optional] 
**lastmod_time** | **datetime** | LastModTime is a hint about when the content in this attachment was last modified. | [optional] 
**mime_type** | **str** | MimeType describes the MIME type of the attached content. Optional but recommended. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


