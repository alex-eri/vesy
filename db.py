from typing import Union
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord, QSqlTableModel
import logging
from PySide6.QtCore import Qt, Slot, QFile, QDir

import datetime


class JournalModel(QSqlTableModel):

    def __init__(self, parent=None):
        super(JournalModel, self).__init__(parent)

        self.connect_database()
        self.create_table('journal')
        self.setTable('journal')
        self.setSort(0, Qt.SortOrder.AscendingOrder)
        self.setQuery(
            "SELECT time, plate, direction, weight, load FROM journal")
        self.setHeaderData(3, Qt.Orientation.Horizontal, "ТС")
        self.setHeaderData(0, Qt.Orientation.Horizontal, "Время")
        self.setHeaderData(1, Qt.Orientation.Horizontal, "Направление")
        self.setHeaderData(2, Qt.Orientation.Horizontal, "Вес")
        self.setHeaderData(2, Qt.Orientation.Horizontal, "Груз")
        self.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)

        self.select()
        logging.debug("Table was loaded successfully.")

    def connect_database(self):
        database = QSqlDatabase.database()
        if not database.isValid():
            database = QSqlDatabase.addDatabase("QSQLITE")
            if not database.isValid():
                logging.error("Cannot add database")

        write_dir = QDir("")
        if not write_dir.mkpath("."):
            logging.error("Failed to create writable directory")

        # Ensure that we have a writable location on all devices.
        abs_path = write_dir.absolutePath()
        filename = f"{abs_path}/journal.sqlite3"

        # When using the SQLite driver, open() will create the SQLite
        # database if it doesn't exist.
        database.setDatabaseName(filename)
        if not database.open():
            logging.error("Cannot open database")

        return database

    def create_table(self, name):
        if name in QSqlDatabase.database().tables():
            return
        if name == "journal":
            query = QSqlQuery()
            if not query.exec_(
                """
                CREATE TABLE journal (
                    id INTEGER PRIMARY KEY ASC ,
                    time DATETIME default CURRENT_TIMESTAMP,
                    direction TEXT,
                    weight REAL,
                    plate TEXT,
                    load TEXT,
                    shots TEXT
                    )
                """
            ):
                logging.error("Failed to create database")

    def insert(self, plate, weigth, direction, load_type, shots):
        r = self.record()
        r.setValue('direction', direction)
        r.setValue('plate', plate)
        r.setValue('weight', float(weigth))
        r.setValue('time', datetime.datetime.now(
        ).isoformat(timespec='seconds', sep=' '))

        if not self.insertRecord(-1, r):
            logging.error(f"Insert Failed: {self.lastError().text()}")

        if not self.submitAll():
            logging.error(f"submit Failed: {self.lastError().text()}")
            logging.error(self.query)
        else:
            self.database().commit()
        self.select()
