import pymssql
import psycopg2
from psycopg2 import sql
from datetime import datetime

class CollectData():

    def __init__(self):
        # self.start_date = "2015-12-22"
        # self.end_date = "2021-01-11"       
        self.start_date = "{0}-{1}-{2}".format(datetime.now().year, datetime.now().month, datetime.now().day) 
        self.end_date = "{0}-{1}-{2}".format(datetime.now().year, datetime.now().month, datetime.now().day)
        self.malls = {'Мебельный базар': {'SQL_Server': 'CRONOS', 'id': 11},
             'Сормовские зори': {'SQL_Server': 'LIBRA', 'id': 12},
             'ЦУМ': {'SQL_Server': 'PERSEUS', 'id': 13},
             'ТЦ Муравей': {'SQL_Server': 'ANDROMEDA', 'id': 10},
             'ТРК Небо': {'SQL_Server': '10.0.92.55', 'id': 9},
             'ТРЦ Нора': {'SQL_Server': '10.0.77.158', 'id': 14},
             'ТРЦ Горки': {'SQL_Server': '10.0.81.13', 'id': 15}}
        self.sql_request = """
declare @start date, @end date
Set @start='{1}'
Set @end='{2}'
SELECT * FROM [dbo].[collect_data] (
   @start
  ,@end
  ,{0}) ORDER BY [date]
"""


# ON CONFLICT (date) DO UPDATE SET real_in = EXCLUDED.real_in, real_out = EXCLUDED.real_out

    def __insert_into_portal(self, values):
        conn_pg = psycopg2.connect(dbname='rent_db', user='django', password='djangoDB#4563', host='localhost')
        with conn_pg.cursor() as cursor_pg:
            conn_pg.autocommit = True
            insert = sql.SQL("INSERT INTO api_visitorsflow (date, real_in, real_out, mall_id) VALUES {} ON CONFLICT (mall_id, date) DO UPDATE SET real_in = EXCLUDED.real_in, real_out = EXCLUDED.real_out").format(
                sql.SQL(',').join(map(sql.Literal, values))
            )
            cursor_pg.execute(insert)

    def __collect_mb(self, username, password, db_name):
        server = self.malls['Мебельный базар']['SQL_Server']
        mall_id = self.malls['Мебельный базар']['id']
        conn_mssql = pymssql.connect('{0}\SQLEXPRESS'.format(server), username, password, db_name)
        cursor_mssql = conn_mssql.cursor()
        print('Мебельный базар: Сбор данных!')
        cursor_mssql.execute(self.sql_request.format(mall_id, self.start_date, self.end_date))
        values = []
        for i in cursor_mssql.fetchall():
            values.append(i)
        print('Мебельный базар: Импорт данных в портал!')
        self.__insert_into_portal(values)
        print('Мебельный базар: ОК!')

    def __collect_sz(self, username, password, db_name):
        server = self.malls['Сормовские зори']['SQL_Server']
        mall_id = self.malls['Сормовские зори']['id']
        conn_mssql = pymssql.connect('{0}\SQLEXPRESS'.format(server), username, password, db_name)
        cursor_mssql = conn_mssql.cursor()
        print('Сормовские зори: Сбор данных!')
        cursor_mssql.execute(self.sql_request.format(mall_id, self.start_date, self.end_date))
        values = []
        for i in cursor_mssql.fetchall():
            values.append(i)
        print('Сормовские зори: Импорт данных в портал!')
        self.__insert_into_portal(values)
        print('Сормовские зори: ОК!')

    def __collect_tsum(self, username, password, db_name):
        server = self.malls['ЦУМ']['SQL_Server']
        mall_id = self.malls['ЦУМ']['id']
        conn_mssql = pymssql.connect('{0}\SQLEXPRESS'.format(server), username, password, db_name)
        cursor_mssql = conn_mssql.cursor()
        print('ЦУМ: Сбор данных!')
        cursor_mssql.execute(self.sql_request.format(mall_id, self.start_date, self.end_date))
        values = []
        for i in cursor_mssql.fetchall():
            values.append(i)
        print('ЦУМ: Импорт данных в портал!')
        self.__insert_into_portal(values)
        print('ЦУМ: ОК!')

    def __collect_ml(self, username, password, db_name):
        server = self.malls['ТЦ Муравей']['SQL_Server']
        mall_id = self.malls['ТЦ Муравей']['id']
        conn_mssql = pymssql.connect('{0}\SQLEXPRESS'.format(server), username, password, db_name)
        cursor_mssql = conn_mssql.cursor()
        print('ТЦ Муравей: Сбор данных!')
        cursor_mssql.execute(self.sql_request.format(mall_id, self.start_date, self.end_date))
        values = []
        for i in cursor_mssql.fetchall():
            values.append(i)
        print('ТЦ Муравей: Импорт дыннх в портал!')
        self.__insert_into_portal(values)
        print('ТЦ Муравей: ОК!')

    def __collect_nebo(self, username, password, db_name):
        server = self.malls['ТРК Небо']['SQL_Server']
        mall_id = self.malls['ТРК Небо']['id']
        conn_mssql = pymssql.connect('{0}\SQLEXPRESS'.format(server), username, password, db_name)
        cursor_mssql = conn_mssql.cursor()
        print('ТРК Небо: Сбор данных!')
        cursor_mssql.execute(self.sql_request.format(mall_id, self.start_date, self.end_date))
        values = []
        for i in cursor_mssql.fetchall():
            values.append(i)
        print('ТРК Небо: Импорт данных в портал!')
        self.__insert_into_portal(values)
        print('ТРК Небо: ОК!')

    def __collect_gorky(self, username, password, db_name):
        server = self.malls['ТРЦ Горки']['SQL_Server']
        mall_id = self.malls['ТРЦ Горки']['id']
        conn_mssql = pymssql.connect('{0}\ANTIVOR'.format(server), username, password, db_name)
        cursor_mssql = conn_mssql.cursor()
        print('ТРЦ Горки: Сбор данных!')
        cursor_mssql.execute(self.sql_request.format(mall_id, self.start_date, self.end_date))
        values = []
        for i in cursor_mssql.fetchall():
            values.append(i)
        print('ТРЦ Горки: Импорт данных в портал!')
        self.__insert_into_portal(values)
        print('ТРЦ Горки: ОК!')

    def __collect_nora(self, username, password, db_name):
        server = self.malls['ТРЦ Нора']['SQL_Server']
        mall_id = self.malls['ТРЦ Нора']['id']
        conn_mssql = pymssql.connect('{0}\SQLEXPRESS'.format(server), username, password, db_name)
        cursor_mssql = conn_mssql.cursor()
        print('ТРЦ Нора: Сбор данных!')
        cursor_mssql.execute(self.sql_request.format(mall_id, self.start_date, self.end_date))
        values = []
        for i in cursor_mssql.fetchall():
            values.append(i)
        print('ТРЦ Нора: Импорт данных в портал!')
        self.__insert_into_portal(values)
        print('ТРЦ Нора: ОК!')

    def start(self):
        self.__collect_mb('rstat_conn', 'adMG#7924', 'RetailStat')
        self.__collect_sz('rstat_conn', 'adMG#7924', 'RStat')
        self.__collect_tsum('rstat_conn', 'adMG#7924', 'RStat')
        self.__collect_ml('rstat_conn', 'adMG#7924', 'RStat')
        self.__collect_nebo('rstat_conn', 'adMG#7924', 'RetailStat')
        self.__collect_gorky('rstat_conn', 'adMG#7924', '_Antivor')
        self.__collect_nora('rstat_conn', 'adMG#7924', 'RetailStat')

CollectData().start()

