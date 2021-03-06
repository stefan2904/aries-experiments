# coding: utf-8

"""
    (Aries Agent REST Server) of VC4SM University.

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DidExchangeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def accept_invitation(self, id, **kwargs):  # noqa: E501
        """Accept a stored connection invitation....  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.accept_invitation(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Connection ID (required)
        :param str public: Optional Public DID to be used for this request
        :param str router_connections: Optional specifies router connections (comma-separated values)
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.accept_invitation_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.accept_invitation_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def accept_invitation_with_http_info(self, id, **kwargs):  # noqa: E501
        """Accept a stored connection invitation....  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.accept_invitation_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Connection ID (required)
        :param str public: Optional Public DID to be used for this request
        :param str router_connections: Optional specifies router connections (comma-separated values)
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'public', 'router_connections']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method accept_invitation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `accept_invitation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'public' in params:
            query_params.append(('public', params['public']))  # noqa: E501
        if 'router_connections' in params:
            query_params.append(('router_connections', params['router_connections']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/connections/{id}/accept-invitation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2006',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def accept_request(self, id, **kwargs):  # noqa: E501
        """Accepts a stored connection request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.accept_request(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Connection ID (required)
        :param str public: Optional Public DID to be used for this invitation request
        :param str router_connections: Optional specifies router connections (comma-separated values)
        :return: ExchangeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.accept_request_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.accept_request_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def accept_request_with_http_info(self, id, **kwargs):  # noqa: E501
        """Accepts a stored connection request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.accept_request_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Connection ID (required)
        :param str public: Optional Public DID to be used for this invitation request
        :param str router_connections: Optional specifies router connections (comma-separated values)
        :return: ExchangeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'public', 'router_connections']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method accept_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `accept_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'public' in params:
            query_params.append(('public', params['public']))  # noqa: E501
        if 'router_connections' in params:
            query_params.append(('router_connections', params['router_connections']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/connections/{id}/accept-request', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExchangeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_connection(self, request, **kwargs):  # noqa: E501
        """Saves the connection record.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_connection(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateConnectionRequest request: Params for creating a connection. (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_connection_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_connection_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def create_connection_with_http_info(self, request, **kwargs):  # noqa: E501
        """Saves the connection record.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_connection_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateConnectionRequest request: Params for creating a connection. (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_connection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `create_connection`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/connections/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_invitation(self, **kwargs):  # noqa: E501
        """Creates a new connection invitation....  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_invitation(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alias: The Alias to be used in invitation to be created
        :param str public: Optional public DID to be used in invitation
        :param str router_connection_id: Optional specifies router connection id
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_invitation_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_invitation_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_invitation_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a new connection invitation....  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_invitation_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alias: The Alias to be used in invitation to be created
        :param str public: Optional public DID to be used in invitation
        :param str router_connection_id: Optional specifies router connection id
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alias', 'public', 'router_connection_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_invitation" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'alias' in params:
            query_params.append(('alias', params['alias']))  # noqa: E501
        if 'public' in params:
            query_params.append(('public', params['public']))  # noqa: E501
        if 'router_connection_id' in params:
            query_params.append(('router_connection_id', params['router_connection_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/connections/create-invitation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_connection(self, id, **kwargs):  # noqa: E501
        """Fetch a single connection record.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connection(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the connection to get (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_connection_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_connection_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_connection_with_http_info(self, id, **kwargs):  # noqa: E501
        """Fetch a single connection record.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connection_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the connection to get (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_connection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_connection`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/connections/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def implicit_invitation(self, **kwargs):  # noqa: E501
        """Create implicit invitation using inviter DID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.implicit_invitation(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str their_did: InviterDID
        :param str their_label: Optional inviter label
        :param str my_did: Optional invitee did
        :param str my_label: Optional invitee label
        :param str router_connections: Optional specifies router connections (comma-separated values)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.implicit_invitation_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.implicit_invitation_with_http_info(**kwargs)  # noqa: E501
            return data

    def implicit_invitation_with_http_info(self, **kwargs):  # noqa: E501
        """Create implicit invitation using inviter DID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.implicit_invitation_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str their_did: InviterDID
        :param str their_label: Optional inviter label
        :param str my_did: Optional invitee did
        :param str my_label: Optional invitee label
        :param str router_connections: Optional specifies router connections (comma-separated values)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['their_did', 'their_label', 'my_did', 'my_label', 'router_connections']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method implicit_invitation" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'their_did' in params:
            query_params.append(('their_did', params['their_did']))  # noqa: E501
        if 'their_label' in params:
            query_params.append(('their_label', params['their_label']))  # noqa: E501
        if 'my_did' in params:
            query_params.append(('my_did', params['my_did']))  # noqa: E501
        if 'my_label' in params:
            query_params.append(('my_label', params['my_label']))  # noqa: E501
        if 'router_connections' in params:
            query_params.append(('router_connections', params['router_connections']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/connections/create-implicit-invitation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_connections(self, **kwargs):  # noqa: E501
        """query agent to agent connections.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_connections(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alias: Alias of connection invitation
        :param str initiator: Initiator is Connection invitation initiator
        :param str invitation_key: Invitation key
        :param str invitation_id: Invitation ID
        :param str parent_thread_id: Parent threadID
        :param str my_did: MyDID is DID of the agent
        :param str state: State of the connection invitation
        :param str their_did: TheirDID is other party's DID
        :param str their_role: TheirRole is other party's role
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_connections_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.query_connections_with_http_info(**kwargs)  # noqa: E501
            return data

    def query_connections_with_http_info(self, **kwargs):  # noqa: E501
        """query agent to agent connections.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_connections_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alias: Alias of connection invitation
        :param str initiator: Initiator is Connection invitation initiator
        :param str invitation_key: Invitation key
        :param str invitation_id: Invitation ID
        :param str parent_thread_id: Parent threadID
        :param str my_did: MyDID is DID of the agent
        :param str state: State of the connection invitation
        :param str their_did: TheirDID is other party's DID
        :param str their_role: TheirRole is other party's role
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alias', 'initiator', 'invitation_key', 'invitation_id', 'parent_thread_id', 'my_did', 'state', 'their_did', 'their_role']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_connections" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'alias' in params:
            query_params.append(('alias', params['alias']))  # noqa: E501
        if 'initiator' in params:
            query_params.append(('initiator', params['initiator']))  # noqa: E501
        if 'invitation_key' in params:
            query_params.append(('invitation_key', params['invitation_key']))  # noqa: E501
        if 'invitation_id' in params:
            query_params.append(('invitation_id', params['invitation_id']))  # noqa: E501
        if 'parent_thread_id' in params:
            query_params.append(('parent_thread_id', params['parent_thread_id']))  # noqa: E501
        if 'my_did' in params:
            query_params.append(('my_did', params['my_did']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'their_did' in params:
            query_params.append(('their_did', params['their_did']))  # noqa: E501
        if 'their_role' in params:
            query_params.append(('their_role', params['their_role']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/connections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def receive_invitation(self, invitation, **kwargs):  # noqa: E501
        """Receive a new connection invitation....  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.receive_invitation(invitation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Invitation invitation: The Invitation Request to receive (required)
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.receive_invitation_with_http_info(invitation, **kwargs)  # noqa: E501
        else:
            (data) = self.receive_invitation_with_http_info(invitation, **kwargs)  # noqa: E501
            return data

    def receive_invitation_with_http_info(self, invitation, **kwargs):  # noqa: E501
        """Receive a new connection invitation....  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.receive_invitation_with_http_info(invitation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Invitation invitation: The Invitation Request to receive (required)
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invitation']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method receive_invitation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invitation' is set
        if ('invitation' not in params or
                params['invitation'] is None):
            raise ValueError("Missing the required parameter `invitation` when calling `receive_invitation`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'invitation' in params:
            body_params = params['invitation']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/connections/receive-invitation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_connection(self, id, **kwargs):  # noqa: E501
        """Removes given connection record.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_connection(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the connection record to remove (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_connection_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_connection_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_connection_with_http_info(self, id, **kwargs):  # noqa: E501
        """Removes given connection record.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_connection_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the connection record to remove (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_connection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_connection`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/connections/{id}/remove', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
