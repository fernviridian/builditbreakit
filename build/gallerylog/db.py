import gallerylog.crypto
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
        return None # or an integer!

    def isPersonInGallery(self, name, personType):
        return False # or True

    # for logread -R

    def getRoomsForPerson(self, name, personType):
        return () # or a list of Room numbers

    # for logappend

    def addLogEntry(self, name, direction, personType, time, room=None):
        return None

    # for logappend input verifications

    def lastLoggedTime(self):
        return -1 # or the most recent time

    # for logread -S

    def getPeopleByRoom(self):
        return dict() # mapping room numbers to list of people

    def getPeopleByType(self, personType):
        return () # list of people of that type in the gallery

    # for logread input sanitization

    def isValidRoom():
        return False # or True

    # for additional functionality

    def getLogByPerson():
        return False
