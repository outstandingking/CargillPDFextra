from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view

from . import constants
from .models import PdfExtraModel

from .extra import Extra
from rest_framework.response import Response


@api_view(['POST'])
def vat_pdf_extra(request):
    data = request.data

    type = data.get('type', None)

    try:
        type = constants.area_mapping[type]

    except:
        return Response(data={'error': 'type 不在mapping列表里'}, status=status.HTTP_400_BAD_REQUEST)

    format = data.get('format', None)

    if format is None:
        return Response(data={'error': 'format 不可为空。可选VAT，VAT1，VAT2'}, status=status.HTTP_400_BAD_REQUEST)

    file = data.get('file', None)
    # 兼容PDF和pdf
    file.name = file.name.lower()
    if '.excel' in file.name or '.xls' in file.name:
        file_type = 'excel'
    if '.pdf' or '.PDF' in file.name:
        file_type = 'pdf'

    try:
        pdfExtra = PdfExtraModel.objects.create(type=type, format=format, file=data.get('file'))
        remove_columns = []
        remove_rows = []
        entity_pair_setting = constants.vat_entity_map
  
        if format == 'VAT':
            extraE = Extra(pdfExtra.file.url.encode('gbk').decode('gbk'), pdfExtra.file.name, [1,],
                           entity_pair_setting, file_type, type, company_name_column_index=None,
                           sheetNamelist=None, company_name=None)
        if file_type == 'pdf':
                data = extraE.extra_raw_data_from_VAT_PDF()
        if file_type == 'excel':
                data = extraE.extra_raw_data_from_VAT_excel()

        pdfExtra.result = data
        pdfExtra.save()

        if format =='VAT1':
            extraE = Extra(pdfExtra.file.url.encode('gbk').decode('gbk'), pdfExtra.file.name, remove_columns,
                           entity_pair_setting, 'PDF', type, company_name_column_index=None,
                           sheetNamelist=None, company_name=None)

            data = extraE.extra_raw_data_from_VAT1_PDF()
            pdfExtra.result = data
            pdfExtra.save()

        if format =='VAT2':

            extraE = Extra(pdfExtra.file.url.encode('gbk').decode('gbk'), pdfExtra.file.name, [],
                           entity_pair_setting, 'PDF', type, company_name_column_index=None,
                           sheetNamelist=None, company_name=None)

            data = extraE.extra_raw_data_from_VAT2_PDF()
            pdfExtra.result = data
            pdfExtra.save()



    except Exception as e:
        print(e)
        return Response(data={'error': '解析失败'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(data=data)

