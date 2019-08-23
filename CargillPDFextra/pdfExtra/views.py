import os

from rest_framework import status
from rest_framework.decorators import api_view

from . import utils
from . import constants
from .models import PdfExtraModel

from .extra import Extra
from rest_framework.response import Response
import time
import traceback
import requests

@api_view(['POST'])
def vat_pdf_extra(request):
    data = request.data

    type = data.get('type', None)

    type_object = utils.return_type_standard(type)

    type = type_object.get('type_value')
    type_standard = type_object.get('type_standard')

    format = data.get('format', None)

    if format is None:
        return Response(data={'error': 'format 不可为空。可选VAT，VAT1，VAT2'}, status=status.HTTP_400_BAD_REQUEST)

    file = data.get('file', None)
    # 兼容PDF和pdf
    file.name = file.name.lower()
    if '.excel' in file.name or '.xls' in file.name:
        file_type = 'excel'
    if '.pdf'in file.name or '.PDF' in file.name:
        file_type = 'pdf'

    try:
        pdfExtra = PdfExtraModel.objects.create(type=type, format=format, file=file)
        remove_columns = []
        remove_rows = []
        entity_pair_setting = constants.vat_entity_map
        pdf_source_path =pdfExtra.file.url.encode('gbk').decode('gbk')

        if format == 'VAT':
            extraE = Extra(pdf_source_path, pdfExtra.file.name, [1,],
                           entity_pair_setting, file_type, type, company_name_column_index=None,
                           sheetNamelist=None, company_name=None)
        if file_type == 'pdf':
            if type_standard == 'xfaPDF' :
                pdf_ab_source_path = os.getcwd() + '/'+pdf_source_path

                target_pdf = pdf_source_path.replace('.pdf','_format.pdf')
                target_ab_pdf_path = os.getcwd() + '/'+target_pdf
                lience_key = 'itextkey.xml'
                url = 'http://127.0.0.1:8005/readxfa'
                data = {'source_pdf': pdf_ab_source_path, 'target_pdf':target_ab_pdf_path,"lienceKey":lience_key}
                e_r = requests.post(url, data)
                if e_r.status_code is status.HTTP_200_OK:
                    extraE.filePath = target_pdf
                    extraE.filename = extraE.filename.replace(".pdf","_format.pdf")
                    extraE.remove_columns = []
                else:
                    Response(data={'error': '解析失败,xfapdf转换失败'}, status=status.HTTP_400_BAD_REQUEST)
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
        traceback.print_exc()
        return Response(data={'error': '解析失败'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(data=data)

