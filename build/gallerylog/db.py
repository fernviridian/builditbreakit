import gallerylog.crypto
from pysqlcipher import dbapi2

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
        # TODO: check if file exists, create tables if not
        self.connection = dbapi2.connect(self.filename)
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA KEY = '" + self.key + "';")

    def successful(self):
        # TODO: have a table for verifying connectivity
        return True

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

    def addLogEntry(self, name, direction, personType, time):
        return None

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
