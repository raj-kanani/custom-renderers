import response as response
from rest_framework import renderers
from .serializers import *


class CustomRenderers(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # response = 'hello india !!!!'
        # import pdb
        # pdb.set_trace()
        return response({'msg':'heeellleldelded'})
        # return super().render(data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)


# from django.utils.encoding import smart_unicode

#
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
