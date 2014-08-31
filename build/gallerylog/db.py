#import gallerylog.crypto
from pysqlcipher import dbapi2
import os.path

# db = DB("filename.db", "secretKey")
# if not db.successful():
#   ERRR
# db.closeDBFile()

class DB:
    def __init__(self, filename, key):
        self.filename = filename
        self.key = key
        self.openDBFile()

    def openDBFile(self):
        fileExists = os.path.isfile(self.filename)
        self.connection = dbapi2.connect(self.filename)
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA KEY = '" + self.key + "';")
        if not fileExists:
            self.cursor.execute("CREATE TABLE testvalid(nothing);")
            self.cursor.execute("CREATE TABLE log(name NOT NULL, personType NOT NULL, direction NOT NULL, time INTEGER NOT NULL, room integer);")
            self.cursor.execute("CREATE TABLE status(name NOT NULL, personType NOT NULL, isHere NOT NULL DEFAULT 'f', currentRoom integer);")

    def successful(self):
        try:
            self.cursor.execute("SELECT * FROM testvalid;")
            self.cursor.execute("SELECT * FROM log;")
            self.cursor.execute("SELECT * FROM status;")
            return True
        except:
            return False

    def closeDBFile(self):
        self.connection.commit()
        self.connection.close()

    def getCurrentRoomForPerson(self, name, personType):
        self.cursor.execute("SELECT currentRoom FROM status WHERE name LIKE ? AND personType LIKE ?", (name, personType))
        ret = self.cursor.fetchone()
        if ret != None:
            ret = ret[0]
        return ret

    def isPersonNew(self, name, personType):
        self.cursor.execute("SELECT count(*) FROM status WHERE name LIKE ? AND personType LIKE ?", (name, personType))
        value = self.cursor.fetchone()[0]
        if value == 0:
            return True
        else:
            return False

    def isPersonInGallery(self, name, personType):
        self.cursor.execute("SELECT isHere FROM status WHERE name LIKE ? AND personType LIKE ?", (name, personType))
        ret = self.cursor.fetchone()
        if ret != None:
            ret = ret[0]
        return ret == "t"

    # for logread -T

    def getTotalTime(self, name, personType):
        self.cursor.execute("SELECT time FROM log WHERE room IS NULL AND direction LIKE 'A' AND personType LIKE ? AND name LIKE ? ORDER BY time ASC;", (personType, name))
        val = self.cursor.fetchone()
        self.cursor.execute("SELECT time FROM log WHERE room IS NULL AND direction LIKE 'D' AND personType LIKE ? AND name LIKE ? ORDER BY time ASC;", (personType, name))
        val2 = self.cursor.fetchone()
        if val:
            if val2:
                return val2[0] - val[0]
            else:
                return self.lastLoggedTime() - val[0]
        else:
            return None

    # for logread -R

    def getRoomsForPerson(self, name, personType):
        self.cursor.execute("SELECT room FROM log WHERE room IS NOT NULL AND direction LIKE 'A' AND personType LIKE ? AND name LIKE ? ORDER BY time ASC;", (personType, name))
        val = self.cursor.fetchall()
        val = map(lambda x: x[0], val)
        return val

    # for logappend

    def addLogEntry(self, name, personType, direction, time, room=None):
        self.cursor.execute("INSERT INTO log(name, personType, direction, time, room) VALUES (?, ?, ?, ?, ?);",
                            (name, personType, direction, time, room))
        if self.isPersonNew(name, personType):
            self.cursor.execute("INSERT INTO status(name, personType, currentRoom, isHere) VALUES (?, ?, ?, 't');",
                                (name, personType, room))
        else:
            if direction == "A":
                if room == None:
                    self.cursor.execute("UPDATE status SET isHere = 't' WHERE name LIKE ? AND personType LIKE ?;",
                                        (name, personType))
                else:
                    self.cursor.execute("UPDATE status SET currentRoom = ? WHERE name LIKE ? AND personType LIKE ?;",
                                        (room, name, personType))
            else: # departure
                if room == None:
                    self.cursor.execute("UPDATE status SET isHere = 'f' WHERE name LIKE ? AND personType LIKE ?;",
                                        (name, personType))
                else:
                    self.cursor.execute("UPDATE status SET currentRoom = NULL WHERE name LIKE ? AND personType LIKE ?;",
                                        (name, personType))
        return None

    # for logappend input verifications

    def lastLoggedTime(self):
        self.cursor.execute("SELECT MAX(time) FROM log;")
        v = self.cursor.fetchone()[0]
        if v == None:
            v = -1
        return v

    # for logread -S

    def getPeopleByRoom(self):
        self.cursor.execute("SELECT currentRoom, name FROM status WHERE currentRoom IS NOT NULL ORDER BY name ASC;")
        ret = dict()
        myl = self.cursor.fetchall()
        for row in myl:
            if not row[0] in ret.keys():
                ret[row[0]] = []
            ret[row[0]].append(row[1])
        return ret

    def getPeopleHereByType(self, personType):
        self.cursor.execute("SELECT name FROM status WHERE personType LIKE ? AND isHere = 't' ORDER BY name ASC;", (personType))
        val = self.cursor.fetchall()
        val = map(lambda x: x[0], val)
        return val

    # for additional functionality

    def getLogByPerson(self, name, personType):
        self.cursor.execute("SELECT time, direction, room FROM log WHERE personType LIKE ? AND name LIKE ? ORDER BY time ASC;", (personType, name))
        val = self.cursor.fetchall()
        return val

if __name__ == "__main__":
   import os

   logfile = "testlogdb"
   keytoken= "token"

   # delete it and start over each time
   if os.path.isfile(logfile):
       os.unlink(logfile)

   # NOTE: this DB is called db.DB outside this file
   sql = DB(logfile, keytoken)
   if not sql.successful():
       print ("invalid database or token")
       sys.exit(-1)

   def p():
       print "================================"
       print "Is here: " + str(sql.isPersonInGallery("Ryan", "E"))
       print "Current Room: " + str(sql.getCurrentRoomForPerson("Ryan", "E"))
       print "Last logged: " + str(sql.lastLoggedTime())
       print
       print "Status: " + str(sql.getPeopleByRoom())
       print "================================"
       print

   def q():
       print "================================"
       print "Employees: " + str(sql.getPeopleHereByType("E"))
       print "Guests: " + str(sql.getPeopleHereByType("G"))
       print "================================"
       print

   def s():
       print "================================"
       print "Bob log: " + str(sql.getRoomsForPerson("Bob", "E"))
       print "Joe log: " + str(sql.getRoomsForPerson("Joe", "G"))
       print "Ryan log: " + str(sql.getRoomsForPerson("Ryan", "E"))
       print
       print "Joe full log:"
       print str(sql.getLogByPerson("Joe", "G"))
       print "================================"
       print

   q()
   p()

   print "Into the gallery"
   sql.addLogEntry("Ryan", "E", "A", 52)
   p()

   print "Into room 101"
   sql.addLogEntry("Ryan", "E", "A", 55, 101)
   p()

   print "Bob and Joe appear"
   sql.addLogEntry("Bob", "E", "A", 70)
   sql.addLogEntry("Joe", "G", "A", 71)
   p()
   q()

   print "Out of room 101"
   sql.addLogEntry("Ryan", "E", "D", 95, 101)
   p()

   print "Out of this place"
   sql.addLogEntry("Ryan", "E", "D", 152)
   sql.addLogEntry("Ryan", "E", "A", 160, 123)
   sql.addLogEntry("Ryan", "E", "D", 161, 123)
   sql.addLogEntry("Ryan", "E", "A", 162, 123)
   sql.addLogEntry("Ryan", "E", "D", 163, 123)
   sql.addLogEntry("Ryan", "E", "A", 164, 101)
   sql.addLogEntry("Ryan", "E", "D", 165, 101)
   sql.addLogEntry("Joe", "G", "A", 166, 101)
   sql.addLogEntry("Mary", "E", "A", 170)
   sql.addLogEntry("Sally", "E", "A", 171)
   sql.addLogEntry("Ben", "E", "A", 172)
   sql.addLogEntry("Sally", "E", "A", 173, 144)
   sql.addLogEntry("Ben", "E", "A", 174, 144)
   p()
   q()
   s()
   print sql.isPersonNew("Jack", "E")
   print sql.isPersonNew("Ben", "E")
   # Ben= 2, Ryan= 100
   print sql.getTotalTime("Ben", "E")
   print sql.getTotalTime("Ryan", "E")
   print sql.getTotalTime("Jack", "E")

   # always gracefully close the DB after it is open!
   sql.closeDBFile()
