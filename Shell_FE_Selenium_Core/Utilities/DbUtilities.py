import os
import mysql.connector
import pyodbc
import pandas as pd
from configparser import ConfigParser
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase


class DbUtilities:
    configuration = None
    db_connection = None
    sql_connection = None
    current_working_directory = os.path.dirname(os.getcwd())
    excel_report = current_working_directory + "\\Shell_FE_Behave_Tests\\TestResults\\"

    # region MYSQL Integration
    @staticmethod
    def create_mysql_connection():
        """This  is used to create the connection for the database"""
        DbUtilities.configuration = SeleniumBase.read_config()
        DbUtilities.db_connection = mysql.connector.connect(
            host=DbUtilities.configuration['database']['host'],
            user=DbUtilities.configuration['database']['user'],
            password=DbUtilities.configuration['database']['password'],
            database=DbUtilities.configuration['database']['database']
        )
        return DbUtilities.db_connection

    @staticmethod
    def fetchalldata(dbquery):
        """This is used to fetch all the data from the table
           :args:
                -dbquery- MYSQL query to fetch the data
           Returns : It will return the data in the dictionary format
        """
        dbcursor = DbUtilities.db_connection.cursor()
        dbcursor.execute(dbquery)
        dbdata = dbcursor.fetchall()
        return dbdata

    @staticmethod
    def fetchone(dbquery):
        """This is used to fetch the first row of the table
        :args:
              -dbquery- MYSQL query to fetch the data
         Returns : It will return the data in the dictionary format
        """
        dbcursor = DbUtilities.db_connection.cursor()
        dbcursor.execute(dbquery)
        dbdata = dbcursor.fetchone()
        return dbdata

    @staticmethod
    def closeconnection():
        """This is used to close MYSQL server connection"""
        DbUtilities.db_connection.close()

    # endregion

    # region SQL Integration
    @staticmethod
    def create_sql_connection():
        """This method is used to create the connection from the database"""
        DbUtilities.configuration = SeleniumBase.read_config()
        DbUtilities.sql_connection = pyodbc.connect(
            Driver=DbUtilities.configuration['database']['driver'],
            Server=DbUtilities.configuration['database']['SQL_Server'],
            Database=DbUtilities.configuration['database']['SQL_database'],
            Trusted_Connection=DbUtilities.configuration['database']['Trusted_Connection'],
            UID=DbUtilities.configuration['database']['sql_server_Username'],
            PWD=DbUtilities.configuration['database']['sql_server_Password'],
            AUTHENTICATION=DbUtilities.configuration['database']['authentication_type']
        )
        return DbUtilities.sql_connection

    @staticmethod
    def execute_sql_command(sql_query):
        """This helps to execute the sql query
           :args:
                - sql_query : SQL query needs to perform
        """

        sql_cursor = DbUtilities.sql_connection.cursor()
        sql_values = sql_cursor.execute(sql_query)
        return sql_values

    @staticmethod
    def close_sql_connection():
        """This will close the sql connection"""
        DbUtilities.sql_connection.close()

    @staticmethod
    def get_drivers():
        """This will help you find the drivers available in the system"""
        driver_list = pyodbc.drivers()
        return driver_list

    @staticmethod
    def export_datas_to_excel(sql_query, file_name):
        """This will export the datas to excel directly
           :args:
               - sql_query : SQL query to fetch the data
               - file_name : name of the file to be stored
        """
        df = pd.read_sql(sql=sql_query, con=DbUtilities.sql_connection)
        df.to_excel(DbUtilities.excel_report + file_name + ".xlsx")
    # endregion
