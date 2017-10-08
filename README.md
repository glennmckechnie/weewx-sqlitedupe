# weewx-sqlitedupe
Duplicate weewx archive records and store them in a seperate database - currently in SQLite format.

Early days yet. 

Works for me, may need tweaking to suit your schema set-up.

1. wget -O weewx-sqlitedupe.zip https://github.com/glennmckechnie/weewx-sqlitedupe/archive/master.zip

2. wee_extension --install weewx-sqlitedupe.zip

3. /etc/init.d/weewx restart

details in weewx.conf 
<pre>
    [Databases]
        [[sqlitedupe_sqlite]]
            database = /var/lib/sqlitedupe.sdb
</pre>
