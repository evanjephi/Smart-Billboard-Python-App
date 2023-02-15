import pyodbc
import os

"""check_tds_protocol_version
Queries the SQL Server to determine the actual TDS protocol version in use.
"""


def tds_version(cnxn):
    """
    Get the TDS protocol version from the SQL Server system view.
    :param cnxn: a currently open pyodbc.Connection
    :return: the active TDS protocol version as string
    """
    protocol_versions = {
        67239936: '4.2',  # b'\x04\x02\x00\x00'
        117440512: '7.0',  # b'\x07\x00\x00\x00'
        1895825409: '7.1',  # b'q\x00\x00\x01'
        1913192450: '7.2',  # b'r\t\x00\x02'
        1930100739: '7.3',  # b's\x0b\x00\x03'
        1946157060: '7.4',  # b't\x00\x00\x04'
    }
    sql = "SELECT protocol_version FROM sys.dm_exec_connections WHERE session_id=@@SPID"
    crsr = cnxn.cursor()
    result = crsr.execute(sql).fetchval()
    return protocol_versions.get(result, 'unknown ({})'.format(result))


if __name__ == '__main__':
    cnxn_str = (
        'Driver=FreeTDS;'
        'Server=192.168.1.144;'
        'Port=49242;'
        'TDS_Version=7.3;'
        'UID={};PWD={}'
        ).format(os.environ['myUID'], os.environ['myPWD'])
    cnxn = pyodbc.connect(cnxn_str)
    print('ODBC driver: "{}", version {}'.format(
        cnxn.getinfo(pyodbc.SQL_DRIVER_NAME),
        cnxn.getinfo(pyodbc.SQL_DRIVER_VER)))
    print('Actual TDS protocol version in use: {}'.format(tds_version(cnxn)))
    """
    Sample output:
    
        ODBC driver: "libtdsodbc.so", version 0.91
        Actual TDS protocol version in use: 4.2
    
    Note that although we asked for version 7.3 we wound up using version 4.2 
    because FreeTDS 0.91 is too old.
    """
    cnxn.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
