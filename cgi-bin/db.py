import sqlite3

conn = sqlite3.connect("pragsale.db")
c = conn.cursor()

def createTables():
    c.execute("Create Table If Not Exists Tbl_Attribute(ID integer PRIMARY Key, name Text, description Text)")
    conn.commit()

    c.execute("Create Table If Not Exists Tbl_Requirement(ID integer PRIMARY Key, name Text, description Text)")
    conn.commit()

    c.execute("Create Table If Not Exists Tbl_AttReq(ID integer PRIMARY Key, attID integer, reqID integer, priorprob real, ER real)")
    conn.commit()

    c.execute("Create Table If Not Exists Tbl_Flat(ID integer PRIMARY Key, title Text, address Text, description Text)")
    conn.commit()

def addNewRec(tablename, inputs):
    if bool(inputs):
        fields = ""
        vals = ""
        for key, val in inputs.items():
            fields += key + ","
            vals += "'" + val + "',"

        if fields.find(',') != -1:
            fields = fields.rstrip(',')

        if vals.find(',') != -1:
            vals = vals.rstrip(',')

        c.execute("Insert Into " + tablename +"(" + fields + ") Values(" + vals + ")")
        conn.commit()


def getList(tablename):
    c.execute("SELECT * FROM " + tablename)
    for row in c.fetchall():
        print(row)
        print "<br>"