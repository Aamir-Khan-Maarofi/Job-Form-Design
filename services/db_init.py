import sqlite3
from sqlite3 import Error
from banner import banner

def connectDB():
    return sqlite3.connect("./jobs.db")


def createDailyJobsTable():
    cursor = connectDB()
    cursor.execute('''CREATE TABLE DAILY_JOBS
        (
            ID                  INTEGER PRIMARY KEY AUTOINCREMENT ,
            JOB_CREATION_TIME   TIMESTAMP                 NOT NULL,
            COMPANY             TEXT                      NOT NULL,
            NAME                TEXT                      NOT NULL,
            BILLING_DETAILS     MEDIUMTEXT                NOT NULL, 
            JOB_PRIORITY        TEXT                      NOT NULL,
            TYPE_OF_TRIP        TEXT                      NOT NULL,
            CLIETN_DETAILS      MEDIUMTEXT                NOT NULL,
            PICkUP_DATE         DATE                      NOT NULL,
            PICKUP_TIME         TIME                      NOT NULL,
            RETURN_TIME         TIME                              ,
            DESTINATION_DETAILS MEDIUMTEXT                NOT NULL,
            NOTES               MEDIUMTEXT                        , 
            START_DATE          DATE                      NOT NULL,
            END_DATE            DATE                      NOT NULL
        ); '''
                   )

    print("[INFO] : DAILY_JOBS TABLE CREATED...")


def createNormalJobsTable():
    cursor = connectDB()
    cursor.execute('''CREATE TABLE NORMAL_JOBS
        (
            ID                      INTEGER PRIMARY KEY AUTOINCREMENT   ,
            JOB_CREATION_TIME       TIMESTAMP                   NOT NULL,
            COMPANY                 TEXT                        NOT NULL,
            NAME                    TEXT                        NOT NULL,
            BILLING_DETAILS         MEDIUMTEXT                  NOT NULL, 
            JOB_PRIORITY            TEXT                        NOT NULL,
            TYPE_OF_TRIP            TEXT                        NOT NULL,
            CLIETN_DETAILS          MEDIUMTEXT                  NOT NULL,
            PICkUP_DATE             DATE                        NOT NULL,
            PICKUP_TIME             TIME                        NOT NULL,
            RETURN_TIME             TIME                                ,
            DESTINATION_DETAILS     MEDIUMTEXT                  NOT NULL,
            NOTES                   MEDIUMTEXT                          , 
            JOB_TYPE                TEXT                        NOT NULL,
            MEET_AND_GREET          TEXT                                ,
            FLIGHT_DETAILS          MEDIUMTEXT                          ,
            SPECIAL_REQUIREMENTS    MEDIUMTEXT                          
        ); '''
                   )

    print("[INFO] : NORMAL_JOBS TABLE CREATED")


if __name__ == "__main__":
    banner()
    try:
        print("[INFO] : CREATING DAILY JOBS TABLE")
        createDailyJobsTable()
        print("[INFO] : CREATING NORMAL JOBS TABLE")
        createNormalJobsTable()

        print("[INFO] : ALL SET FOR NEXT OPERATIONS")
    except Error as e:
        print(e)