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
    pragm = {"orderUdf":
     {"OrderLines":
          [{
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
            "OL_HEIGHT":17.0,
            "OL_HEIGHT_UOM":"米",
            "UNIT_WEIGHT":19.0,
            "UNIT_WEIGHT_UOM":"千克",
            "UNIT_VOLUME":21.0,
            "UNIT_VOLUME_UOM":"立方米",
            "UNIT_NET_WEIGHT":23.0,
            "UNIT_NET_WEIGHT_UOM":"千克",
            "PACKAGE_REMARK":"服装",
            "OL_UDF1":"",
            "OL_UDF2":"",
            "OL_UDF3":"",
            "OL_UDF4":"",
            "OL_UDF5":"",
            "OL_UDF6":"",
            "OL_UDF7":"",
            "OL_UDF8":"",
            "OL_UDF9":"",
            "OL_UDF10":""}],
      "ORDER_GID":"noll.test180731002",
      "ORDER_ID":"test180731002",
      "C_ORDER_NO":"123456",
      "ORDER_RELEASE_TYPE_PSC":"",
      "RELEASE_FROM_TYPE_PSC":"客户单",
      "EARLY_PICKUP_DATE":"",
      "LATE_PICKUP_DATE":"2018-07-31 16:00",
      "EARLY_DELIVERY_DATE":"",
      "LATE_DELIVERY_DATE":"2018-08-02 16:00",
      "PLAN_SP_GID":"",
      "PLAN_SP_ID":"",
      "PLAN_TM_GID":"公路零担",
      "PLAN_TM_ID":"公路零担",
      "CUSTOMER_GID":"",
      "CUSTOMER_ID":"LNSCS",
      "CUSTOMER_NAME":"雷诺斯测试",
      "BU_GID":"",
      "BU_ID":"LNSCS",
      "BU_NAME":"雷诺斯测试",
      "INCO_TERM_PSC":"",
      "DISPATCH_TYPE":"",
      "SERVICE_LEVEL_PSC":"",
      "PAY_METHOD":"",
      "FEATURE_SC":"",
      "NEGOTIATED_PRICE":"否",
      "IS_URGENCY":"是",
      "ORDER_INFO_REMARK":"123456",
      "DELIVERY":"654321",
      "OMS_ID":"",
      "WH_ID":"",
      "CARRIER_BY":"",
      "SRC_LOCATION_GID":"",
      "SRC_LOCATION_ID":"上海诺尔/SHNE",
      "SRC_ENABLED":"否",
      "SRC_LOCATION_NAME":"上海诺尔/SHNE",
      "SRC_CONTACT_NAME":"",
      "SRC_CONTACT_PHONE":"021-31156688",
      "SRC_COUNTRY_CODE_ID":"CHN",
      "SRC_CITY":"上海市",
      "SRC_PROVINCE":"上海市",
      "DEST_LOCATION_GID":"",
      "DEST_LOCATION_ID":"广州测试中转仓",
      "DEST_ENABLED":"否",
      "DEST_LOCATION_NAME":"广州爱马仕调拨中转仓",
      "DEST_CONTACT_NAME":"",
      "DEST_CONTACT_PHONE":"",
      "DEST_COUNTRY_CODE_ID":"",
      "DEST_CITY":"广州市",
      "DEST_PROVINCE":"广东省",
      "CREATED_BY":"nolladmin",
      "DOMAIN_NAME":"test",
      "EXT_WAYBII_NO":"987654321",
      "ITEM_VALUE":98.0,
      },
 "token": token_value}
    r = requests.post(api_url,params=pragm)
    print(r.text)


print(postOrder())