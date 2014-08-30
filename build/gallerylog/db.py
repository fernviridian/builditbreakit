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

    def isPersonInGallery(self, name, personType):
        self.cursor.execute("SELECT isHere FROM status WHERE name LIKE ? AND personType LIKE ?", (name, personType))
        ret = self.cursor.fetchone()
        if ret != None:
            ret = ret[0]
        return ret == "t"

    # for logread -R

    # TODO: implement
    def getRoomsForPerson(self, name, personType):
        return () # or a list of Room numbers

    # for logappend

    def addLogEntry(self, name, personType, direction, time, room=None):
        self.cursor.execute("INSERT INTO log(name, personType, direction, time, room) VALUES (?, ?, ?, ?, ?);",
                            (name, personType, direction, time, room))
        self.cursor.execute("SELECT count(*) FROM status WHERE name LIKE ? AND personType LIKE ?", (name, personType))
        value = self.cursor.fetchone()[0]
        if value == 0:
            self.cursor.execute("INSERT INTO status(name, personType, currentRoom, isHere) VALUES (?, ?, ?, 't');",
                                (name, personType, room))
        else:
            if direction == "a":
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

    # TODO: test
    def lastLoggedTime(self):
        self.cursor.execute("SELECT MAX(time) FROM log;")
        v = self.cursor.fetchone()[0]
        if v == None:
            v = -1
        return v

    # for logread -S

    # TODO: implement
    def getPeopleByRoom(self):
        return dict() # mapping room numbers to list of people

    # TODO: implement (sort)
    def getPeopleByType(self, personType):
        return () # list of people of that type in the gallery

    # for additional functionality

    # TODO: implement
    def getLogByPerson(self):
        return False

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
       print "================================"
       print

   p()

   print "Into the gallery"
   sql.addLogEntry("Ryan", "E", "a", 52)
   p()

   print "Into room 101"
   sql.addLogEntry("Ryan", "E", "a", 55, 101)
   p()

   print "Out of room 101"
   sql.addLogEntry("Ryan", "E", "d", 95, 101)
   p()

   print "Out of this place"
   sql.addLogEntry("Ryan", "E", "d", 152)
   p()

   # always gracefully close the DB after it is open!
   sql.closeDBFile()
