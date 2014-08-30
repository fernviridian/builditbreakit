import gallerylog.crypto
from pysqlcipher import dbapi2

# db = DB("filename.db", "secretKey")
# if not db.successful():
#   ERRR
# db.closeDBFile()

class DB:
    def __init__(filename, key):
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

    def closeDBFile():
        self.connection.commit()
        self.connection.close()

    # for logread -R

    def getRoomsForPerson():
        return False

    # for logappend

    def addLogEntry():
        return False

    # for logread -S

    def getPeopleByRoom():
        return False

    def getPeopleByType():
        return False

    # for additional functionality

    def getLogByPerson():
        return False
