#------------------------------------------------------------------------------
# clob.py (Section 7.1)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright 2017, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

import cx_Oracle

con = cx_Oracle.connect("pythonhol", "welcome", "localhost/orclpdb")
cur = con.cursor()

print("Inserting data...")
cur.execute("truncate table testclobs")
longString = ""
for i in range(5):
    char = chr(ord('A') + i)
    longString += char * 250
    cur.execute("insert into testclobs values (:1, :2)",
                   (i + 1, "String data " + longString + ' End of string'))
con.commit()

print("Querying data...")
cur.prepare("select * from testclobs where id = :id")
cur.execute(None, {'id': 1})
(id, clob) = cur.fetchone()
print("CLOB length:", clob.size())
clobdata = clob.read()
print("CLOB data:", clobdata)
