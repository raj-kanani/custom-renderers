import json
import response as response
from rest_framework import renderers
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from .serializers import *
from django.utils.encoding import smart_text
import json
from rest_framework.views import exception_handler


class CustomRenderers(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        charset = 'utf-8'
        # import pdb
        # pdb.set_trace()
        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors': data})
        else:
            response = json.dumps({'data': data})
        return super().render(data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)


class CustomRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        print(renderer_context['response'],'fdecdecdecdecde')
        response = {
            'code': status_code,
            # 'code': 400,
            'message': renderer_context['response'].status_text,
            # 'message': 'successfully data pass',
            'data': data,
        }
        renderer_context['response'].status_code = 400

        return super(CustomRenderer, self).render(response, accepted_media_type, renderer_context)


class CustomJSONRenderers1(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        data = {'data': data, 'message': 'created', 'status': 201}
        data = {'data': data, 'message': 'ok', 'status': 200}
        data = {'data': data, 'message': 'accepted', 'status': 202}

        return super(CustomJSONRenderers1, self).render(data, accepted_media_type, renderer_context)


def custom_exception(exc, context):
    handlers = {
        'ValidationError': handle_generic_error,
        'Http404': handle_generic_error,
        'PermissionDenied': handle_generic_error,
        'NotAuthenticated': handle_authentication_error,
    }
    response = exception_handler(exc, context)
    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response


def handle_authentication_error(exc, context, response):
    response.data = {
        'error': 'please login'

    }
    return response


def handle_generic_error(exc, context, response):
    return response

#########################################################################
# class CustomRenderers(renderers.BaseRenderer):
#     media_type = 'text/plain'
#     format = 'txt'
#
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         raise NotImplementedError('Renderer class testing purpose')
#


###############################################################
# from django.utils.encoding import smart_unicode
# class TsvRenderer(renderers.BaseRenderer):
#     media_type = 'text/tab-separated-values'
#     format = 'tsv'
#
#     def render(self, data, media_type=None, renderer_context=None):
#
#         # TSV format:
#         # Column Names first row
#         # Tab separated per row
#         # Using Fields defined in the ImageSerializer to create fields and add values
#
#         tabbedData = ''
#
#         # Column names
#         first = True
#         for columnName in StudentSerializer.Meta.fields:
#             if first == True:
#                 tabbedData = '%s' % (columnName)
#                 first = False
#             else:
#                 tabbedData = '%s\t%s' % (tabbedData, columnName)
#
#         tabbedData = '%s\n' % tabbedData
#
#         # Column values
#         first = True
#         # for lineItem in data:
#         #     for columnName in StudentSerializer.Meta.fields:
#         #         if first == True:
#         #             tabbedData = '%s%s' % (tabbedData, lineItem[columnName])
#         #             first = False
#         #         else:
#         #             tabbedData = '%s\t%s' % (tabbedData, lineItem[columnName])
#
#             # tabbedData = '%s\n' % tabbedData
#             # first = True
#
#         return tabbedData


##################################################
# class PlainTextRenderer(renderers.BaseRenderer):
#     media_type = 'text/plain'
#     format = 'txt'
#
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         return smart_text(data, encoding=self.charset)

#######################################################
# class CustomJSONRenderer(JSONRenderer):
#
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         # call super, as we really just want to mess with the data returned
#         json_str = super(CustomJSONRenderer, self).render(data, accepted_media_type, renderer_context)
#         root_element = 'contact'
#
#         # wrap the json string in the desired root element
#         ret = '{%s: %s}' % (root_element, json_str)
#
#         return ret

from rest_framework.renderers import BaseRenderer
from rest_framework.utils import json


class ApiRenderer(BaseRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_dict = {
            'status': 'failure',
            'data': {},
            'message': '',
        }
        if data.get('data'):
            response_dict['data'] = data.get('data')
        if data.get('status'):
            response_dict['status'] = data.get('status')
        if data.get('message'):
            response_dict['message'] = data.get('message')
        data = response_dict
        return json.dumps(data)