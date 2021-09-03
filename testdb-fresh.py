#!/usr/bin/python3

import pymysql

# 打开数据库连接
connection = pymysql.connect(host='10.251.76.11', port=3306, user='usercenter_test', password='usercenter_test123',
                             database='yh_srm_odercenter_fresh_test', cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
sql = "INSERT INTO yh_srm_odercenter_fresh_test.fresh_shoppingcart (user_id,shop_code,product_code,product_name," \
      "product_barcode,purchase_price,purchase_count,supplier_code,supplier_name,dc_code,dc_name,logistics_mode," \
      "project_area,unit,spec,pack_count,purchase_group,purchase_group_name,purchase_org,purchase_org_name," \
      "realtime_inventory_count,in_transport_count,dms,status,selected,updated_time,created_time,created_by," \
      "updated_by,replenish_id,origin_type,normal_business) VALUES (1000001058388,'9010','114','冰小肚','2300034000006'," \
      "26.80,1.00,'QGC00029','哈根达斯店1334','W003','福州生鲜DC',1,'17','KG','*',0.00,%s,'家禽课',%s,'永辉福建大区采购组织',0.00," \
      "0.00,0.16,1,1,'2021-08-18 16:55:13.0','2021-08-18 16:55:13.0','sys','sys',0,0,0); "


def test(k1):
    i = 1
    j = 1
    while i < 10:
        group = 'H0' + str(i)
        # group = "H02"
        # print(group)
        while j < 10:
            org = "P00" + str(j)
            # org = "P001"
            # print(org)
            cursor.execute(sql, (group, org))
            connection.commit()
            j = j + 1
        i = i + 1
        # print(i)
        j = 1
    return k1


k = 1
while k < 100:
    print(test(k))
    k = k + 1

# sql = "SELECT x.purchase_org ,x.purchase_group FROM yh_srm_odercenter_fresh_test.fresh_shoppingcart x;"
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
