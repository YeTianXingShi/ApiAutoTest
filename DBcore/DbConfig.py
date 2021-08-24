import pymysql


class DbConfig:
    host = '10.251.77.27'
    port = 3306
    user = 'ceshi_admin'
    password = 'N7fNO98CNOiBu9gb@Wi9'
    database = 'yh_test_tool'

    def __init__(self):
        connection = pymysql.connect(host=self.host,
                                     port=self.port,
                                     user=self.user,
                                     password=self.password,
                                     database=self.database,
                                     cursorclass=pymysql.cursors.DictCursor
                                     )
        self.connection = connection

    def get_connect(self):
        return self.connection

    def close_connect(self):
        self.connection.close()
        return 'success'
