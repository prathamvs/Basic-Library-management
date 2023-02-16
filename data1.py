import sqlite3

def DataBase():
    con = sqlite3.connect('data1.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data1(id INTEGER PRIMARY KEY AUTOINCREMENT ,Bookname TEXT,Author TEXT,Year TEXT,Isbm TEXT)")
    con.commit()
    con.close()
    
def Add(Bookname,Author,Year,Isbm):
    con = sqlite3.connect('data1.db')
    cur = con.cursor()
    cur.execute("INSERT INTO data1 VALUES(NULL,?,?,?,?)",(Bookname,Author,Year,Isbm))
    con.commit()
    con.close()
    
def View():
    con = sqlite3.connect('data1.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM data1")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def Delete(id):
    con = sqlite3.connect('data1.db')
    cur = con.cursor()
    cur.execute("DELETE FROM data1 WHERE id =? ",(id,))
    con.commit()
    con.close()
    
    
def SearchData(Bookname="",Author="",Year="",Isbm=""):
    con = sqlite3.connect('data1.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM data1 where Bookname=? OR Author=? OR Year=? OR Isbm=?",(Bookname,Author,Year,Isbm))
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows    
    
    

def Update():
    con = sqlite3.connect('data1.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM data1")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows
        
    
DataBase()   