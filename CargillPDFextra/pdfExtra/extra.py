# -*- coding: utf-8 -*-
import sys


import datetime

import subprocess

import pandas as pd
import xlrd

import os
import json

from .constants import *
import numpy as np



class Extra(object):
    file = None
    remove_columns = []
    entity_pair_setting = {}
    company_name_column_index = []
    sheetName = []
    filePath = ''
    file_type = ''
    company_name = ''
    format_type = ''




    def __init__(cls, filePath, filename, remove_columns, entity_pair_setting, file_type, type=None,company_name_column_index=None,
                 sheetNamelist=None, company_name=None):
        cls.remove_columns = remove_columns
        cls.entity_pair_setting = entity_pair_setting
        cls.company_name_column_index = company_name_column_index
        cls.remove_columns = remove_columns
        cls.sheetName = sheetNamelist
        cls.filePath = filePath
        cls.file_type = file_type
        cls.company_name = company_name
        cls.type = type
        cls.filename = filename




    def format(cls, value, index):
        if '-' in value:
            return 0
        else:
            if index >= 2:
                value = value.replace(',', '')
                try:
                    value = float(value)
                except:
                    value = 0
                return value
            else:
                return value

    def check_is_entity(self, row_values, index):
        try:
            if self.format_type == 'VAT':
                if (row_values[index] is not None and \
                    not isinstance(row_values[index], float)) and \
                        (row_values[index] is not None and len(row_values[index]) is not 0):
                    # if row_values[index] not in self.remove_columns:
                        try:
                            row_values[index] = row_values[index].replace(' ',"").replace('　',"")
                            float(str(row_values[index + 1]).replace(',', ''))
                            return True
                        except:
                            row_values[index + 1] = 0
                            return True
            if (row_values[index] is not None and \
                not isinstance(row_values[index], float)) and \
                    (row_values[index] is not None and len(row_values[index]) is not 0):
                if row_values[index] not in self.remove_columns:
                    if type(row_values[index + 1]) is float:
                        return True
                    elif isinstance(float(row_values[index + 1].replace(',', '')), float):
                        try:
                            float(row_values[index + 1].replace(',', ''))
                            return True
                        except ValueError:
                            return False

            else:
                return False
        except:
            return False




    def filter_unexpect_str(cls, str, unexpect_str_list):
        for i in range(len(unexpect_str_list)):
            str = str.replace(unexpect_str_list[i], "")
        return str

    def format_value(self, value):
        if type(value) is float:
            if str(value) != 'nan':
                return str(value)
        try:
            value = str(float(value.replace(",", "")))
            return value
        except:
            return '0.0'

    def get_sheet_name(cls, sheet):
        unexpect_str_list = 'abcdefghijklmnopqrst1234567890()ABCDEFGHIJKLMOPQRSTUVWXYZ:'
        if cls.company_name_column_index is not None and len(cls.company_name_column_index) > 0:
            return cls.filter_unexpect_str(
                sheet.row_values(cls.company_name_column_index[0])[cls.company_name_column_index[1]], unexpect_str_list)
        else:
            cls.filter_unexpect_str(sheet.name, unexpect_str_list)

    def delete_remove_columns(cls, row_values):
        new_list = [j for i, j in enumerate(row_values) if i not in cls.remove_columns]
        return new_list

    def extra_raw_data_from_VAT1(cls):
        fp = open("VAT1extraScript.sh", "r+")
        infos = fp.readlines()
        fp.seek(0, 0)
        newscriptFile = 'VAT1extraScript' + '_' + 'temp' + '.sh'
        fp2 = open(newscriptFile, "w")
        for line in infos:
            line_new = line.replace('$filename', cls.filePath)
            fp2.write(line_new)
        fp.close()
        fp2.close()
        subprocess.check_call('sh ' + newscriptFile, shell=True)
        extra_raw_data = []
        all_entitys = []
        sheet_entity_json = {}
        with open("temp/VAT1_extra_result.json") as f:
            data = json.load(f)
            print(data)
            for index, value in enumerate(data):
                s = ''
                for i, v in enumerate(value['data']):
                    for i in range(len(v)):
                        s = s + ' ' + ''.join(v[i]['text'])
                extra_raw_data.append(cls.format(s, index))

        sheet_entity_json['sheetName'] = cls.company_name
        sheet_entity_json['fileExtraResult'] = []

        entity_json_month_7 = {
            "file_type": cls.file_type,
            "entityIdentity": {
                "entity_key": "即征即退服务、不动产和无形资产(销售额)",
                "entity_value": "即征即退服务、不动产和无形资产(销售额)",
                "file_type": cls.file_type
            },
            "value": cls.format_value(extra_raw_data[0]),
            "value_type": "this_month"
        }

        entity_json_month_14 = {
            "file_type": cls.file_type,
            "entityIdentity": {
                "entity_key": "即征即退货物及加工修理修配劳务(销售额)",
                "entity_value": "即征即退货物及加工修理修配劳务(销售额)",
                "file_type": cls.file_type
            },
            "value": cls.format_value(extra_raw_data[1]),
            "value_type": "this_month"
        }

        entity_json_month_18 = {
            "file_type": cls.file_type,
            "entityIdentity": {
                "entity_key": "货物及加工修理修配劳务(销售额)",
                "entity_value": "货物及加工修理修配劳务(销售额)",
                "file_type": cls.file_type
            },
            "value": cls.format_value(extra_raw_data[2]),
            "value_type": "this_month"
        }

        sheet_entity_json['fileExtraResult'].append(entity_json_month_7)
        sheet_entity_json['fileExtraResult'].append(entity_json_month_14)
        sheet_entity_json['fileExtraResult'].append(entity_json_month_18)
        all_entitys.append(sheet_entity_json)
        return all_entitys

    def extra_raw_data_from_VAT2(cls):
        fp = open("VAT2extraScript.sh", "r+")
        infos = fp.readlines()
        fp.seek(0, 0)
        newscriptFile = 'VAT2extraScript' + '_' + 'temp' + '.sh'
        fp2 = open(newscriptFile, "w")
        for line in infos:
            line_new = line.replace('$filename', cls.filePath)
            fp2.write(line_new)
        fp.close()
        fp2.close()
        subprocess.check_call('sh ' + newscriptFile, shell=True)
        extra_raw_data = []
        all_entitys = []
        sheet_entity_json = {}
        with open("temp/VAT2_exta_result.json") as f:
            data = json.load(f)
            print(data)
            for index, value in enumerate(data):
                s = ''
                for i, v in enumerate(value['data']):
                    for i in range(len(v)):
                        s = s + ' ' + ''.join(v[i]['text'])
                extra_raw_data.append(cls.format(s, index))

        sheet_entity_json['sheetName'] = cls.company_name
        sheet_entity_json['fileExtraResult'] = []



        entity_json_month_2 = {
            "file_type": cls.file_type,
            "entityIdentity": {
                "entity_key": "本期国内进项",
                "entity_value": "本期国内进项",
                "file_type": cls.file_type
            },
            "value": cls.format_value(extra_raw_data[0]),
            "value_type": "this_month"
        }

        entity_json_month_5 = {
            "file_type": cls.file_type,
            "entityIdentity": {
                "entity_key": "本期海关进口进项",
                "entity_value": "本期海关进口进项",
                "file_type": cls.file_type
            },
            "value": cls.format_value(extra_raw_data[1]),
            "value_type": "this_month"
        }

        entity_json_month_14 = {
            "file_type": cls.file_type,
            "entityIdentity": {
                "entity_key": "本期实际进项转出额",
                "entity_value": "本期实际进项转出额",
                "file_type": cls.file_type
            },
            "value": cls.format_value(extra_raw_data[2]),
            "value_type": "this_month"
        }

        sheet_entity_json['fileExtraResult'].append(entity_json_month_2)
        sheet_entity_json['fileExtraResult'].append(entity_json_month_5)
        sheet_entity_json['fileExtraResult'].append(entity_json_month_14)
        all_entitys.append(sheet_entity_json)

        return all_entitys

    def extra_raw_data_from_excel(cls):
        all_entitys = []
        remove_columns = cls.remove_columns
        data = xlrd.open_workbook(cls.filePath)

        if cls.sheetName is not None and len(cls.sheetName) > 0:
            sheet = data.sheet_by_name(cls.sheetName[0])
            sheet_entity_json = {}
            sheet_name = cls.get_sheet_name(sheet)
            sheet_entity_json['sheetName'] = sheet_name
            sheet_entity_json['fileExtraResult'] = []
            nrows = sheet.nrows
            nclos = sheet.ncols
            for i in range(nrows):
                row_values = sheet.row_values(i)
                row_values = cls.delete_remove_columns(row_values)
                if cls.check_is_entity(row_values, 0):
                    """
                    若表单数列的值不为空而且不为数值，那么就把它当做EntityIdentity
                    """
                    entity_json_month = {
                        "file_type": cls.file_type,
                        "entityIdentity": {
                            "entity_key": row_values[0].replace(" ", ""),
                            "entity_value": row_values[0].replace(" ", ""),
                            "file_type": cls.file_type

                        },
                        "value": row_values[1],
                        "value_type": 'this_month',
                    }

                    entity_json_year = {
                        "file_type": cls.file_type,
                        "entityIdentity": {
                            "entity_key": row_values[0].replace(" ", ""),
                            "entity_value": row_values[0].replace(" ", ""),
                            "file_type": cls.file_type

                        },
                        "value": row_values[2],
                        "value_type": 'this_year',
                    }


                    sheet_entity_json['fileExtraResult'].append(entity_json_month)
                    sheet_entity_json['fileExtraResult'].append(entity_json_year)
                if cls.check_is_entity(row_values, 3):
                    entity_json_month = {
                        "file_type": cls.file_type,
                        "entityIdentity": {
                            "entity_key": row_values[3].replace(" ", ""),
                            "entity_value": row_values[3].replace(" ", ""),
                            "file_type": cls.file_type

                        },
                        "value": row_values[4],
                        "value_type": 'this_month'
                    }
                    entity_json_year = {
                        "file_type": cls.file_type,
                        "entityIdentity": {
                            "entity_key": row_values[3].replace(" ", ""),
                            "entity_value": row_values[3].replace(" ", ""),
                            "file_type": cls.file_type

                        },
                        "value": row_values[5],
                        "value_type": 'this_year'
                    }

                    sheet_entity_json['fileExtraResult'].append(entity_json_month)
                    sheet_entity_json['fileExtraResult'].append(entity_json_year)

            all_entitys.append(sheet_entity_json)

        else:
            for sheet in data.sheets():
                sheet_entity_json = {}
                sheet_name = cls.get_sheet_name(sheet)
                sheet_entity_json['sheetName'] = sheet_name
                sheet_entity_json['fileExtraResult'] = []
                cls.delete_remove_columns(sheet)
                nrows = sheet.nrows
                nclos = sheet.ncols
                for i in range(nrows):
                    print(sheet.row_values(i))
                    if cls.check_is_entity(sheet.row_values(i), 0):
                        """
                        若表单数列的值不为空而且不为数值，那么就把它当做EntityIdentity
                        """
                        entity_json = {}
                        entity_json = {
                            "entityIdentity": {
                                "entity_key": sheet.row_values(i)[0].replace(" ", ""),
                                "entity_value": sheet.row_values(i)[0].replace(" ", ""),
                                "file_type": cls.file_type
                            },
                            "value": round(sheet.row_values(i)[1].replace(",", ""), 2),
                            "value_type": 'this_year',
                        }
                        sheet_entity_json['fileExtraResult'].append(entity_json)
                    if cls.check_is_entity(sheet.row_values(i), 2):
                        entity_json = {}
                        entity_json = {
                            "file_type": cls.file_type,
                            "entityIdentity": {
                                "entity_key": sheet.row_values(i)[2].replace(" ", ""),
                                "entity_value": sheet.row_values(i)[2].replace(" ", ""),
                                "file_type": cls.file_type

                            },
                            "value": round(sheet.row_values(i)[1].replace(",", ""), 2),
                            "value_type": 'this_month'
                        }
                        sheet_entity_json['fileExtraResult'].append(entity_json)
                all_entitys.append(sheet_entity_json)

        return all_entitys


    def extra_raw_data_from_VAT_PDF(cls):
        cls.format_type = 'VAT'

        sheet_entity_json = {}
        pwd = os.path.dirname(__file__)
        remove_columns = cls.remove_columns
        fp = open(pwd + '/script/' + cls.type + "_VATextraScript.sh", "r+")
        infos = fp.readlines()
        fp.seek(0, 0)
        filename = cls.filename.split('.')[0]

        newscriptFile = 'temp/script/' + cls.type + '_VATextraScript' + '_' + filename + '.sh'
        fp2 = open(newscriptFile, "w", encoding='utf-8')
        time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        csv_path = cls.type + '_' + filename + '_' + str(time) + '.csv'
        for line in infos:
            line_new = line.replace('$filePath', 'media/' + filename + '.pdf').replace('$pageNo', "1")
            line_new = line_new.replace('$csv_path', csv_path)
            fp2.write(line_new)
        fp.close()
        fp2.close()
        subprocess.check_call('sh ' + newscriptFile, shell=True)
        df = pd.read_csv("temp/" + csv_path, encoding='gbk',header=None)
        column_name_list = list(df.columns.values.tolist())
        print (column_name_list)
        df = df.rename(columns={
            column_name_list[0]: 'column0',
            column_name_list[1]: 'column1',
            column_name_list[2]: 'column2',
            column_name_list[3]: 'column3',
            column_name_list[4]: 'column4',
            column_name_list[5]: 'column5'
        })
        # df.loc[-1] = [column_name_list[0], column_name_list[1], column_name_list[2],
        #               column_name_list[3], column_name_list[4], column_name_list[5]
        #               ]
        # df.index = df.index + 1
        # df = df.sort_index()
        for i in cls.remove_columns:
            df.drop(df.columns[i], axis=1, inplace=True)
        sheet_entity_json['fileExtraResult'] = []
        for index, row in df.iterrows():
            row_values = row
            print(row_values)
            if cls.check_is_entity(row_values, 0):
                entity_json_month = {}
                e_value = str(row_values[0].replace(" ", "").replace("\r", ""))
                entity_key = cls.entity_pair_setting.get(e_value, e_value)

                entity_json_month = {
                    "item_type": "normal",
                    "key": entity_key,
                    "value": cls.format_value(row_values[1]),
                    "value_type": "this_month",

                }

                entity_json_year = {
                    "item_type": "normal",
                    "key": entity_key,
                    "value": cls.format_value(row_values[2]),
                    "value_type": "this_year"
                }

                entity_timely_json_month = {}

                entity_timely_json_month = {
                    "item_type": "timely",
                    "key": entity_key,
                    "value": cls.format_value(row_values[3]),
                    "value_type": "this_month",

                }

                entity_timely_json_year = {}

                entity_timely_json_year = {

                    "item_type": "timely",
                    "key": entity_key,
                    "value": cls.format_value(row_values[4]),
                    "value_type": "this_year",

                }

                sheet_entity_json['fileExtraResult'].append(entity_json_month)
                sheet_entity_json['fileExtraResult'].append(entity_json_year)
                sheet_entity_json['fileExtraResult'].append(entity_timely_json_month)
                sheet_entity_json['fileExtraResult'].append(entity_timely_json_year)

        return sheet_entity_json


    def extra_raw_data_from_VAT_excel(cls):
        cls.format_type = 'VAT'

        sheet_entity_json = {}
        pwd = os.path.dirname(__file__)
        with open(pwd + '/script/' + cls.type + "_VATextraScript.json") as f:
            json_data = json.load(f)
        start_row = json_data['start_row']
        end_row = json_data['end_row']
        remove_columns = json_data['remove_column']
        cls.remove_columns = remove_columns


        df = pd.read_excel("media/" +cls.filename, encoding='gbk')
        df = df.loc[int(start_row):int(end_row)]

        column_name_list = list(df.columns.values.tolist())
        df = df.rename(columns={
            column_name_list[0]: 'column0',
            column_name_list[1]: 'column1',
            column_name_list[2]: 'column2',
            column_name_list[3]: 'column3',
            column_name_list[4]: 'column4',
            column_name_list[5]: 'column5',
            column_name_list[6]: 'column6'
        })
        # df.loc[-1] = [column_name_list[0], column_name_list[1], column_name_list[2],
        #               column_name_list[3], column_name_list[4], column_name_list[5], column_name_list[6]
        #               ]
        # df.index = df.index + 1
        # df = df.sort_index()
        for i in cls.remove_columns:
            df.drop(df.columns[i], axis=1, inplace=True)
        sheet_entity_json['fileExtraResult'] = []
        for index, row in df.iterrows():
            row_values = row
            print(row_values)
            if cls.check_is_entity(row_values, 0):
                entity_json_month = {}
                e_value = str(row_values[0].replace(" ", "").replace("\r", ""))
                entity_key = cls.entity_pair_setting.get(e_value, e_value)

                entity_json_month = {
                    "item_type": "normal",
                    "key": entity_key,
                    "value": cls.format_value(row_values[1]),
                    "value_type": "this_month",

                }

                entity_json_year = {
                    "item_type": "normal",
                    "key": entity_key,
                    "value": cls.format_value(row_values[2]),
                    "value_type": "this_year"
                }

                entity_timely_json_month = {}

                entity_timely_json_month = {
                    "item_type": "timely",
                    "key": entity_key,
                    "value": cls.format_value(row_values[3]),
                    "value_type": "this_month",

                }

                entity_timely_json_year = {}

                entity_timely_json_year = {

                    "item_type": "timely",
                    "key": entity_key,
                    "value": cls.format_value(row_values[4]),
                    "value_type": "this_year",

                }

                sheet_entity_json['fileExtraResult'].append(entity_json_month)
                sheet_entity_json['fileExtraResult'].append(entity_json_year)
                sheet_entity_json['fileExtraResult'].append(entity_timely_json_month)
                sheet_entity_json['fileExtraResult'].append(entity_timely_json_year)

        return sheet_entity_json

    def extra_raw_data_from_VAT1_PDF(cls):
        cls.format_type = 'VAT1'

        try:
            sheet_entity_json = {}
            pwd = os.path.dirname(__file__)
            remove_columns = cls.remove_columns
            fp = open(pwd + '/script/' + cls.type + "_VAT1extraScript.sh", "r+")
            infos = fp.readlines()
            fp.seek(0, 0)
            filename = cls.filename.split('.')[0]

            newscriptFile = 'temp/script/' + cls.type + '_VAT1extraScript' + '_' + filename + '.sh'
            fp2 = open(newscriptFile, "w", encoding='utf-8')
            time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            csv_path = cls.type + '_' + filename + '_' + str(time) + '.csv'
            for line in infos:
                line_new = line.replace('$filePath', 'media/' + filename + '.pdf').replace('$pageNo', "1")
                line_new = line_new.replace('$csv_path', csv_path)
                fp2.write(line_new)
            fp.close()
            fp2.close()
            subprocess.check_call('sh ' + newscriptFile, shell=True)
            df = pd.read_csv("temp/" + csv_path)
            column_name_list = list(df.columns.values.tolist())
            df = df.rename(columns={
                column_name_list[0]: 'column0',
                column_name_list[1]: 'column1',
                column_name_list[2]: 'column2',
                column_name_list[3]: 'column3',
                column_name_list[4]: 'column4',
                column_name_list[5]: 'column5',
                column_name_list[6]: 'column6',
                column_name_list[7]: 'column7',
                column_name_list[8]: 'column8',
                column_name_list[9]: 'column9',
                column_name_list[10]: 'column10',
                column_name_list[11]: 'column11',
                column_name_list[12]: 'column12',
                column_name_list[13]: 'column13',
            })
            df.loc[-1] = [column_name_list[0], column_name_list[1], column_name_list[2],
                          column_name_list[3], column_name_list[4], column_name_list[5],
                          column_name_list[6], column_name_list[7], column_name_list[8],
                          column_name_list[9], column_name_list[10], column_name_list[11],
                          column_name_list[12], column_name_list[13]

                          ]
            df.index = df.index + 1
            df = df.sort_index()
            df = df.replace(np.nan,0)
            for i in cls.remove_columns:
                df.drop(df.columns[i], axis=1, inplace=True)
            sheet_entity_json['fileExtraResult'] = []
            for index, row in df.iterrows():
                row_values = row
                for r_i,r in enumerate(row):

                    print ("r_i")
                    print(r_i)
                    print("r")
                    print(r)


                    print(r)
                    entity_json = {}
                    try:
                        if (r is not None and \
                                not isinstance(r, float)) and \
                                (r is not None and len(r) is not 0):
                            try:
                                r = float(r.replace(',', ''))
                            except:
                                r = 0
                        else:
                            try:
                                r = float(r)
                            except:
                                r= 0
                    except:
                        r=0

                    e_value = str(r)
                    if int((e_value).split('.')[0]) == 0:
                        e_value = str(0)

                    entity_json= {
                            "item_type":VAT1_entity_column_row_mapping[r_i],
                            "key": VAT1_entity_column_mapping[cls.type][index],
                            "value": cls.format_value(e_value),

                    }


                    print(entity_json)
                    sheet_entity_json['fileExtraResult'].append(entity_json)
        except Exception as  e:
            print (e)



        return sheet_entity_json


    def extra_raw_data_from_VAT2_PDF(cls):
        cls.format_type = 'VAT2'
        try:
            sheet_entity_json = {}
            pwd = os.path.dirname(__file__)
            fp = open(pwd + '/script/' + cls.type + "_VAT2extraScript.sh", "r+")
            infos = fp.readlines()
            fp.seek(0, 0)
            filename = cls.filename.split('.')[0]

            newscriptFile = 'temp/script/' + cls.type + '_VA2extraScript' + '_' + filename + '.sh'
            fp2 = open(newscriptFile, "w", encoding='utf-8')
            time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            csv_path = cls.type + '_' + filename + '_' + str(time) + '.csv'
            csv_path_1= cls.type + '_' + filename + '_' + str(time) + '1.csv'
            csv_path_2 =  cls.type + '_' + filename + '_' + str(time) + '2.csv'
            csv_path_3 =  cls.type + '_' + filename + '_' + str(time) + '3.csv'


            for line in infos:
                line_new = line.replace('$filePath', 'media/' + filename + '.pdf').replace('$pageNo', "1")
                line_new = line_new.replace('$csv_path_1', csv_path_1)
                line_new = line_new.replace('$csv_path_2', csv_path_2)
                line_new = line_new.replace('$csv_path_3', csv_path_3)
                line_new = line_new.replace('$csv_path', csv_path)
                fp2.write(line_new)
            fp.close()
            fp2.close()
            subprocess.check_call('sh ' + newscriptFile, shell=True)
            df = pd.read_csv("temp/" + csv_path)
            df1 = pd.read_csv("temp/" + csv_path_1)
            df2 = pd.read_csv("temp/" + csv_path_2)
            df3 = pd.read_csv("temp/" + csv_path_3)
            column_name_list = list(df.columns.values.tolist())
            df = df.rename(columns={
                column_name_list[0]: 'column0',
                column_name_list[1]: 'column1',
                column_name_list[2]: 'column2'
            })
            df.loc[-1] = [column_name_list[0], column_name_list[1], column_name_list[2]
                          ]
            df.index = df.index + 1
            df = df.sort_index()

            sheet_entity_json['fileExtraResult'] = []
            row_index = 0
            try:
                for index, row in df.iterrows():
                    row_values = row[0]
                    for r_i, r in enumerate(row):
                        print("index")
                        print(index)

                        print("e_i")
                        print(r_i)
                        print(VAT2_entity_column_row_mapping[r_i])
                        print(VAT2_entity_column_mapping[index])

                        print(r)
                        entity_json = {}
                        try:
                            if (r is not None and \
                                not isinstance(r, float)) and \
                                    (r is not None and len(r) is not 0):
                                try:
                                    r = float(r.replace(',', ''))
                                except:
                                    r = 0
                            else:
                                try:
                                    r = float(r)
                                except:
                                    r = 0
                        except:
                            r = 0

                        e_value = str(r)
                        if int((e_value).split('.')[0])== 0:
                            e_value = str(0)

                        entity_json = {
                            "item_type": VAT2_entity_column_row_mapping[r_i],
                            "key": VAT2_entity_column_mapping[index],
                            "value": cls.format_value(e_value),

                        }

                        print(entity_json)
                        sheet_entity_json['fileExtraResult'].append(entity_json)
            except Exception as  e:
                print(e)

            ##2


            column_name_list_1 = list(df1.columns.values.tolist())

            df1 = df.rename(columns={
                column_name_list_1[0]: 'column0'
            })
            df1.loc[-1] = [column_name_list_1[0],]
            df1.index = df1.index + 1
            df1 = df.sort_index()

            try:
                for index, row in df.iterrows():
                    row_values = row[0]
                    for r_i, r in enumerate(row):
                        print("index")
                        print(index)

                        print("e_i")
                        print(r_i)
                        print(VAT2_entity_column_row_mapping_1[r_i])
                        print(VAT2_entity_column_mapping_1[3])

                        print(r)
                        entity_json = {}
                        try:
                            if (r is not None and \
                                not isinstance(r, float)) and \
                                    (r is not None and len(r) is not 0):
                                try:
                                    r = float(r.replace(',', ''))
                                except:
                                    r = 0
                            else:
                                try:
                                    r = float(r)
                                except:
                                    r = 0
                        except:
                            r = 0

                        e_value = str(r)
                        if int((e_value).split('.')[0]) == 0:
                            e_value = str(0)

                        entity_json = {
                            "item_type": VAT2_entity_column_row_mapping_1[r_i],
                            "key": VAT2_entity_column_mapping_1[3],
                            "value": cls.format_value(e_value),

                        }

                        print(entity_json)
                        sheet_entity_json['fileExtraResult'].append(entity_json)
            except Exception as  e:
                print(e)

            column_name_list_2 = list(df2.columns.values.tolist())
            df2 = df2.rename(columns={
                column_name_list[0]: 'column0',
                column_name_list[1]: 'column1',
                column_name_list[2]: 'column2'
            })
            df2.loc[-1] = [column_name_list[0], column_name_list[1], column_name_list[2]
                          ]
            df2.index = df2.index + 1
            df2 = df2.sort_index()
            try:
                for index, row in df.iterrows():
                    row_values = row[0]
                    for r_i, r in enumerate(row):
                        print("index")
                        print(index)

                        print("e_i")
                        print(r_i)
                        print(VAT2_entity_column_row_mapping_2[r_i])
                        print(VAT2_entity_column_mapping_2[3+index])

                        print(r)
                        entity_json = {}
                        try:
                            if (r is not None and \
                                not isinstance(r, float)) and \
                                    (r is not None and len(r) is not 0):
                                try:
                                    r = float(r.replace(',', ''))
                                except:
                                    r = 0
                            else:
                                try:
                                    r = float(r)
                                except:
                                    r = 0
                        except:
                            r = 0

                        e_value = str(r)
                        if int((e_value).split('.')[0]) == 0:
                            e_value = str(0)

                        entity_json = {
                            "item_type": VAT2_entity_column_row_mapping_2[r_i],
                            "key": VAT2_entity_column_mapping_2[3+index],
                            "value": cls.format_value(e_value),

                        }

                        print(entity_json)
                        sheet_entity_json['fileExtraResult'].append(entity_json)
            except Exception as  e:
                print(e)



            column_name_list_3 = list(df3.columns.values.tolist())
            df3 = df3.rename(columns={
                column_name_list[0]: 'column0',
                column_name_list[1]: 'column1',
                column_name_list[2]: 'column2'
            })
            df3.loc[-1] = [column_name_list[0], column_name_list[1], column_name_list[2]
                           ]
            df3.index = df3.index + 1
            df3 = df3.sort_index()


            sheet_entity_json['fileExtraResult'] = []
            row_index = 0
            for index, row in df.iterrows():
                row_values = row[0]
                for r_i, r in enumerate(row):
                    print("index")
                    print(index)

                    print("e_i")
                    print(r_i)
                    print(VAT1_entity_column_row_mapping_3[r_i])
                    print(VAT1_entity_column_mapping_3[6+index])

                    print(r)
                    entity_json = {}
                    try:
                        if (r is not None and \
                            not isinstance(r, float)) and \
                                (r is not None and len(r) is not 0):
                            try:
                                r = float(r.replace(',', ''))
                            except:
                                r = 0
                        else:
                            try:
                                r = float(r)
                            except:
                                r = 0
                    except:
                        r = 0

                    e_value = str(r)
                    if int((e_value).split('.')[0]) == 0:
                        e_value = str(0)

                    entity_json = {
                        "item_type": VAT1_entity_column_row_mapping_3[r_i],
                        "key": VAT1_entity_column_mapping_3[6+index],
                        "value": cls.format_value(e_value),

                    }

                    print(entity_json)
                    sheet_entity_json['fileExtraResult'].append(entity_json)
        except Exception as  e:
            print(e)

        return sheet_entity_json


