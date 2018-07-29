#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

import requests


def token():        # 获取客户token
    api_url = "http://app.360scm.com/SCM.TMS7.WebApi/Oauth/GetTokenByCustomer"
    apikey = "XfZ+9AIpwYX3RwKISXxpjZCjq8KbfnpvfEZNLq7YCIoT4DuBhumf7+FTBEGCadnmYT8YYJnyDBGy5bnM98UG8VWZhSgGHXVeu7XH38vmiWr4JNvPSqpJPm9vJlnipy14fkqMSKyaQzm48PNGSlE1jLggKfWXlzNapcixCqY4C35l1Zn9IMfGChlxCT2c74pno4PYK0tlXIaxZAnfaZAxyxEqxId7CeQnYCLXBTneKBU="
    apikey_eo = {"apikey":apikey}
    r = requests.get(api_url,params=apikey_eo)
    token_value = r.json()["token"]
    return token_value


def postOrder():
    api_url = "https://app.360scm.com/SCM.TMS7.WebApi/Customer/SaveOrderInfo"
    token_value = token()
    print(token_value)
    pragm = {"Order":
                 {"OrderLines":
                      [{"OrderLineItems":
                            [{"ITEM_ID":"",
                              "ITEM_NAME":""}],
                        "ERP_ORDER_LINE":"",
                        "ORL_COUNT":4.0,
                        "PACKAGE_COUNT":5.0,
                        "PACKAGE_COUNT_UOM":"箱",
                        "WEIGHT":7.0,
                        "WEIGHT_DIS_UOM":"千克",
                        "NET_WEIGHT":9.0,
                        "NET_WEIGHT_DIS_UOM":"千克",
                        "VOLUME":11.0,
                        "VOLUME_UOM":"立方米",
                        "OL_LENGTH":13.0,
                        "OL_LENGTH_UOM":"米",
                        "OL_WIDTH":15.0,
                        "OL_WIDTH_UOM":"米",
                        "OL_HEIGHT": 17.0,
                        "OL_HEIGHT_UOM":"米",
                        "UNIT_WEIGHT":19.0,
                        "UNIT_WEIGHT_UOM": "千克",
                        "UNIT_VOLUME": 21.0,
                        "UNIT_VOLUME_UOM": "立方米",
                        "UNIT_NET_WEIGHT": 23.0,
                        "UNIT_NET_WEIGHT_UOM": "千克",
                        "PACKAGE_REMARK": "服装",
                        "OL_UDF1":"1",
                        "OL_UDF2":"2",
                        "OL_UDF3":"3",
                        "OL_UDF4":"4",
                        "OL_UDF5":"5",
                        "OL_UDF6":"6",
                        "OL_UDF7":"7",
                        "OL_UDF8":"8",
                        "OL_UDF9":"9",
                        "OL_UDF10":"10"}],
                  "ORDER_ID":"test180723001",
                  "C_ORDER_NO":"test123456789",
                  "ORDER_RELEASE_TYPE_PSC":"普通单",
                  "RELEASE_FROM_TYPE_PSC":"api",
                  "EARLY_PICKUP_DATE":"2018-07-23T11:08:25.7875555+08:00",
                  "LATE_PICKUP_DATE":"2018-07-23T11:08:25.7875555+08:00",
                  "EARLY_DELIVERY_DATE":"2018-07-25T11:08:25.8031806+08:00",
                  "LATE_DELIVERY_DATE":"2018-07-25T11:08:25.8031806+08:00",
                  "PLAN_SP_ID":"",
                  "PLAN_TM_ID":"空运",
                  "BU_ID":"LNSCS",
                  "INCO_TERM_PSC":"",
                  "DISPATCH_TYPE":"",
                  "SERVICE_LEVEL_PSC":"",
                  "PAY_METHOD":"",
                  "FEATURE_SC":"",
                  "NEGOTIATED_PRICE":"否",
                  "IS_URGENCY":"否",
                  "ORDER_INFO_REMARK":"测试123456789",
                  "DELIVERY":"测试987654321",
                  "SRC_LOCATION_NAME":"tset/lns",
                  "SRC_CONTACT_NAME":"测试",
                  "SRC_CONTACT_PHONE":"13917898717",
                  "SRC_ZONE1":"",
                  "SRC_ZONE2":"",
                  "SRC_ADDRESS":"上海市松江区九亭镇九泾路1501号",
                  "SRC_PERIOD":"",
                  "SRC_FLOOR":40.0,
                  "SRC_EMAIL":"20",
                  "SRC_REMARK":"",
                  "DEST_LOCATION_NAME":"test2/lns",
                  "DEST_CONTACT_NAME":"tdg",
                  "DEST_CONTACT_PHONE":"12358465848",
                  "DEST_ZONE1":"",
                  "DEST_ZONE2":"",
                  "DEST_ADDRESS":"广顺路33号D南200室",
                  "DEST_PERIOD":"",
                  "DEST_FLOOR":61.0,
                  "DEST_EMAIL":"",
                  "DEST_REMARK":"",
                  "UDF1":"",
                  "UDF2":"",
                  "UDF3":"",
                  "UDF4":"",
                  "UDF5":"",
                  "UDF6":"",
                  "UDF7":"",
                  "UDF8":"",
                  "UDF9":"",
                  "UDF10":"",
                  "DOMAIN_NAME":"test",
                  "SERVICE_TYPE":"",
                  "SALESMAN_DEPT":"",
                  "SALESMAN_NAME":"",
                  "SALESMAN_CONTACT":"",
                  "INSURED_AMOUNT":80.0,
                  "SALESMAN_EMAIL":"",
                  "CUSTOMS_DECLARE_NO":"",
                  "CUSTOMS_DECLARE_PLACE":"",
                  "INVOICE_NO":"",
                  "TRADE_FORM_SC":""},
             "token": token_value
             }
    r = requests.post(api_url,params=pragm)
    print(r)
    return r


print(postOrder())