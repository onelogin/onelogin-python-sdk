# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import StrictInt, StrictStr

from typing import List, Optional

from onelogin.models.auth_claim import AuthClaim
from onelogin.models.auth_id import AuthId
from onelogin.models.token_claim import TokenClaim

from onelogin.api_client import ApiClient
from onelogin.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class APIAuthClaimsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_auth_claim(self, api_auth_id : StrictStr, content_type : Optional[StrictStr] = None, auth_claim : Optional[AuthClaim] = None, **kwargs) -> int:  # noqa: E501
        """Create Api Auth Server Claim  # noqa: E501

        Create Authorization Claim  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_auth_claim(api_auth_id, content_type, auth_claim, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param content_type:
        :type content_type: str
        :param auth_claim:
        :type auth_claim: AuthClaim
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: int
        """
        kwargs['_return_http_data_only'] = True
        return self.create_auth_claim_with_http_info(api_auth_id, content_type, auth_claim, **kwargs)  # noqa: E501

    @validate_arguments
    def create_auth_claim_with_http_info(self, api_auth_id : StrictStr, content_type : Optional[StrictStr] = None, auth_claim : Optional[AuthClaim] = None, **kwargs):  # noqa: E501
        """Create Api Auth Server Claim  # noqa: E501

        Create Authorization Claim  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_auth_claim_with_http_info(api_auth_id, content_type, auth_claim, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param content_type:
        :type content_type: str
        :param auth_claim:
        :type auth_claim: AuthClaim
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(int, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'api_auth_id',
            'content_type',
            'auth_claim'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_auth_claim" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['api_auth_id']:
            _path_params['api_auth_id'] = _params['api_auth_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['content_type']:
            _header_params['Content-Type'] = _params['content_type']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['auth_claim']:
            _body_params = _params['auth_claim']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "int",
            '401': "AltErr",
            '404': "AltErr",
            '422': "AltErr",
        }

        return self.api_client.call_api(
            '/api/2/api_authorizations/{api_auth_id}/claims', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_auth_claim(self, api_auth_id : StrictStr, claim_id : StrictInt, content_type : Optional[StrictStr] = None, **kwargs) -> None:  # noqa: E501
        """Delete Api Auth Server Claim  # noqa: E501

        Delete Authorization Claim  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_auth_claim(api_auth_id, claim_id, content_type, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param claim_id: (required)
        :type claim_id: int
        :param content_type:
        :type content_type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_auth_claim_with_http_info(api_auth_id, claim_id, content_type, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_auth_claim_with_http_info(self, api_auth_id : StrictStr, claim_id : StrictInt, content_type : Optional[StrictStr] = None, **kwargs):  # noqa: E501
        """Delete Api Auth Server Claim  # noqa: E501

        Delete Authorization Claim  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_auth_claim_with_http_info(api_auth_id, claim_id, content_type, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param claim_id: (required)
        :type claim_id: int
        :param content_type:
        :type content_type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'api_auth_id',
            'claim_id',
            'content_type'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_auth_claim" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['api_auth_id']:
            _path_params['api_auth_id'] = _params['api_auth_id']

        if _params['claim_id']:
            _path_params['claim_id'] = _params['claim_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['content_type']:
            _header_params['Content-Type'] = _params['content_type']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/2/api_authorizations/{api_auth_id}/claims/{claim_id}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_authclaims(self, api_auth_id : StrictStr, content_type : Optional[StrictStr] = None, **kwargs) -> List[TokenClaim]:  # noqa: E501
        """Get Api Auth Server claims  # noqa: E501

        Get Authorization claims  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_authclaims(api_auth_id, content_type, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param content_type:
        :type content_type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[TokenClaim]
        """
        kwargs['_return_http_data_only'] = True
        return self.get_authclaims_with_http_info(api_auth_id, content_type, **kwargs)  # noqa: E501

    @validate_arguments
    def get_authclaims_with_http_info(self, api_auth_id : StrictStr, content_type : Optional[StrictStr] = None, **kwargs):  # noqa: E501
        """Get Api Auth Server claims  # noqa: E501

        Get Authorization claims  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_authclaims_with_http_info(api_auth_id, content_type, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param content_type:
        :type content_type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[TokenClaim], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'api_auth_id',
            'content_type'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_authclaims" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['api_auth_id']:
            _path_params['api_auth_id'] = _params['api_auth_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['content_type']:
            _header_params['Content-Type'] = _params['content_type']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "List[TokenClaim]",
            '401': "AltErr",
            '404': "AltErr",
        }

        return self.api_client.call_api(
            '/api/2/api_authorizations/{api_auth_id}/claims', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def update_claim(self, api_auth_id : StrictStr, claim_id : StrictInt, content_type : Optional[StrictStr] = None, auth_claim : Optional[AuthClaim] = None, **kwargs) -> AuthId:  # noqa: E501
        """Update Api Auth Server Claim  # noqa: E501

        Update Authorization Server Claim  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_claim(api_auth_id, claim_id, content_type, auth_claim, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param claim_id: (required)
        :type claim_id: int
        :param content_type:
        :type content_type: str
        :param auth_claim:
        :type auth_claim: AuthClaim
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AuthId
        """
        kwargs['_return_http_data_only'] = True
        return self.update_claim_with_http_info(api_auth_id, claim_id, content_type, auth_claim, **kwargs)  # noqa: E501

    @validate_arguments
    def update_claim_with_http_info(self, api_auth_id : StrictStr, claim_id : StrictInt, content_type : Optional[StrictStr] = None, auth_claim : Optional[AuthClaim] = None, **kwargs):  # noqa: E501
        """Update Api Auth Server Claim  # noqa: E501

        Update Authorization Server Claim  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_claim_with_http_info(api_auth_id, claim_id, content_type, auth_claim, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param claim_id: (required)
        :type claim_id: int
        :param content_type:
        :type content_type: str
        :param auth_claim:
        :type auth_claim: AuthClaim
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AuthId, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'api_auth_id',
            'claim_id',
            'content_type',
            'auth_claim'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_claim" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['api_auth_id']:
            _path_params['api_auth_id'] = _params['api_auth_id']

        if _params['claim_id']:
            _path_params['claim_id'] = _params['claim_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['content_type']:
            _header_params['Content-Type'] = _params['content_type']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['auth_claim']:
            _body_params = _params['auth_claim']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "AuthId",
            '401': "AltErr",
            '404': "AltErr",
            '422': "AltErr",
        }

        return self.api_client.call_api(
            '/api/2/api_authorizations/{api_auth_id}/claims/{claim_id}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
