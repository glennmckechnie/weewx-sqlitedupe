# $Id: install.py 1319 2015-05-10 08:27:43Z mwall $
# (was the) installer for csvwriter
# Copyright 2015 Matthew Wall
#
# sqlitedupe.py
# based on the csv, pmon and cmon extensions by mwall
# Copyright 2017 Glenn McKechnie
# glenn.mckechnie@gmail.com

from setup import ExtensionInstaller

def loader():
    return SQLiteDupeInstaller()

class SQLiteDupeInstaller(ExtensionInstaller):
    def __init__(self):
        super(SQLiteDupeInstaller, self).__init__(
            version="0.1",
            name='sqlitedupe',
            description='Duplicate weewx archive records and store them in'
                        'a seperate database - currently in SQLite format.',
            author="Glenn McKechnie",
            author_email="glennmckechnie@gmail.com",
            process_services='user.sqlitedupe.SQLiteDupe',
            config={
                'SQLiteDupe': {
                    'data_binding': 'sqlitedupe_binding'},
                'DataBindings': {
                    'sqlitedupe_binding': {
                        'database': 'sqlitedupe_sqlite',
                        'table_name': 'archive',
                        'manager': 'weewx.manager.DaySummaryManager',
                        'schema': 'user.sqlitedupe.schema'}},
                'Databases': {
                    'sqlitedupe_sqlite': {
                        'database_name': 'sqlitedupe.sdb',
                        'driver': 'weedb.sqlite'}},
                   },
            files=[('bin/user',
                    ['bin/user/sqlitedupe.py'
                    ])
                  ]
            )
