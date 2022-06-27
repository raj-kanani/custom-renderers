import json
import response as response
from rest_framework import renderers
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer, BaseRenderer
from .serializers import *
from django.utils.encoding import smart_text
import json
from rest_framework.views import exception_handler


# class CustomRenderer(JSONRenderer):
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         status_code = renderer_context['response'].status_code
#         response = {
#             # "status": "success",
#             "code": 400,
#             "data": data,
#             "message": 'success'
#             # 'error': False,
#             # 'message': 'Success',
#             # 'data': data
#         }
#
#         if not str(status_code).startswith('2'):
#             response["status"] = "error"
#             response["data"] = None
#             try:
#                 response["message"] = data["detail"]
#             except KeyError:
#                 response["data"] = data
#
#         return super(CustomRenderer, self).render(response, accepted_media_type, renderer_context)


class CustomRenderer1(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        # charset = 'utf-8'
        # import pdb
        # pdb.set_trace()
        # if status_code == 200:
        #     # status_code = {
        #     #     'code': status_code,
        #     #     'message': renderer_context['response'].status_text,
        #     #     'data': data,
        #     #     }
        #     status_code = {"message": "success", "errors": [], "data": data, "status": "success"}
        #     print('new status code.............')
        # else:
        #     print('hello testing purpose ')
        # return super().render(data, accepted_media_type=accepted_media_type,
        #                       renderer_context=renderer_context)

        if 'ErrorDetail' in str(data):
            # response = json.dumps({'errors': data})
            response = {
                'code': 400,
                'message': 'failed',
            }
        elif status_code == 200:
            print(status_code, 'my status 200 success')
            response = {
                'code': status_code,
                'message': 'success',
                'data': data,
            }
        elif status_code == 300:
            print(status_code, '300 - data found ')
            response = {
                'code': 300,
                'message': 'data found',
                'data': data,
            }
        else:
            print('500 internet server error')
            response = {
                'code': 500,
                'message': 'Internet server error',
            }
        return super().render(data, accepted_media_type=accepted_media_type,
                              renderer_context=renderer_context)


class CustomRenderers(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors': data})

        else:
            response = json.dumps({'data': data})
        return response


class CustomJSONRenderer12(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # reformat the response
        response_data = {"message": "success", "errors": [], "data": data, "status": "success"}
        # call super to render the response
        response = super(CustomJSONRenderer12, self).render(
            response_data, accepted_media_type, renderer_context
        )
        return response


# class CustomRenderer(JSONRenderer):
#
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         status_code = renderer_context['response'].status_code
#         print(renderer_context['response'], 'fdecdecdecdecde')
#         response = {
#             # 'code': status_code,
#             'code': 400,
#             # 'message': renderer_context['response'].status_text,
#             'message': 'failed to  data pass',
#             'data': data,
#             # "data": {
#             #     "non_field_errors": [
#             #        'failed error '
#             #     ]
#             # }
#         }
#         renderer_context['response'].status_code = 400
#         return super(CustomRenderer, self).render(response, accepted_media_type, renderer_context)


# class CustomRenderer(JSONRenderer):
#
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         status_code = renderer_context['response'].status_code
#         response = {
#             "status": "success",
#             "code": status_code,
#             "data": data,
#             "message": None
#         }
#         if not str(status_code).startswith('2'):
#             response["status"] = "error"
#             response["data"] = None
#             try:
#                 response["message"] = data["detail"]
#             except KeyError:
#                 response["data"] = data
#
#         return super(CustomRenderer, self).render(response, accepted_media_type, renderer_context)

#
# class CustomJSONRenderers1(JSONRenderer):
#     def render(self, data,accepted_media_type=None, renderer_context=None):
#         # data = {'data': data, 'message': 'created', 'status': 201}
#         # data_status = 'unknown'
#         data_status = renderer_context['response'].status_code
#         print(dir(response), 'gjfnngngngngesnfengregergrerb')
#         if renderer_context.status_code // 100 == 2:
#             data_status = 'success'
#             print(data_status,'success')
#         elif renderer_context.status_code // 100 == 4:
#             data_status = 'failure'
#             response.data.setdefault('data_status', data_status)
#             return response
#         return super(CustomJSONRenderers1, self).render(data, accepted_media_type, renderer_context)


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


class JSONRenderers(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Render `data` into JSON, returning a bytestring.
        """
        response = renderer_context.get('response')
        if response and 200 <= response.status_code <= 299 and 'status_code' not in response.data:
            response.data = Errors.success(response.data)
