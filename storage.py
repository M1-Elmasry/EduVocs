#!/usr/bin/env python3
"""module represents the Storage class"""

import os
import sqlite3
import translate

class Storage:
    """
    Storage class for managing vocabulary and sentence records.

    This class facilitates the storage, retrieval, and management of vocabulary and sentence records.
    It includes methods for saving, loading, flipping the state of records between "learning" and "knowing",
    deleting records, and editing the translation of specific records.
    """
    db_dir = os.getenv("HOME")
    db_name = "vocabs"
    __all_records = {}

    def __init__(self):
        """
        Initialize the Storage class.

        Initializes the Storage class by creating a connection to an SQLite database
        and defining the table structure for storing records.
        """

        self.__con = sqlite3.connect(f"{Storage.db_dir}/{Storage.db_name}.db")
        self.__cur = self.__con.cursor()
        self.__cur.execute(
            """CREATE TABLE IF NOT EXISTS vocabs(
        voc_or_sent VARCHAR(256) NOT NULL UNIQUE,
        translation VARCHAR(265) NOT NULL,
        source_lang VARCHAR(20) NOT NULL,
        target_lang VARCHAR(20) NOT NULL,
        state VARCHAR(1) NOT NULL
        );"""
        )

    def save_record(self, voc_or_sent, source_lang, target_lang):
        """
        Save a new record to the database.

        This method saves a new vocabulary or sentence record to the database. The record includes the original
        vocabulary or sentence, its translation, source language, target language, state, and a timestamp.

        Args:
            voc_or_sent (str): The original vocabulary or sentence to be saved.
            source_lang (str): The source language of the vocabulary or sentence.
            target_lang (str): The target language for translation.

        Raises:
            sqlite3.IntegrityError: If the vocabulary or sentence already exists in the database.
        """
        translation = translate.translate(voc_or_sent, source_lang, target_lang)

        try:
            self.__cur.execute(
                f"""INSERT INTO vocabs(voc_or_sent, translation, source_lang, target_lang, state) 
            VALUES
            ('{voc_or_sent}', '{translation}', '{source_lang}', '{target_lang}', 'L')"""
            )
        except sqlite3.IntegrityError:
            print(
                "Error: this vocabulary or sentence already exists check learning or knowing vocabs"
            )
            exit()

        self.__con.commit()
        return self.load_records()

    def load_records(self):
        """
        Load all records from the database.

        This method loads all records from the database, categorizing
        them as "learning" or "knowing" based on their state.

        Returns:
            dict: A dictionary containing two lists of records
            categorized as "learning" and "knowing."

        """
        result = self.__cur.execute(
            """SELECT * FROM vocabs WHERE state = 'L'"""
        )
        all_learning = result.fetchall()

        result = self.__cur.execute(
            """SELECT * FROM vocabs WHERE state = 'K'"""
        )
        all_knowing = result.fetchall()
        Storage.__all_records = {"learning": all_learning, "knowing": all_knowing}
        return Storage.__all_records

    def flip_record(self, voc_or_sent):
        """
        Flip the state of the record from learning to knowing.

        This method changes the state of a specific record from "learning" to "knowing."
        It is used to manage the transition of records as they are learned.

        Args:
            voc_or_sent (str): The vocabulary or sentence whose state needs to be flipped.

        """
        self.__cur.execute(
            f"""UPDATE vocabs SET state = 'K' WHERE voc_or_sent = '{voc_or_sent}'"""
        )
        return self.load_records()

    def delete_record(self, voc_or_sent):
        """
        Delete a record from the database.
        This method deletes a specific record from the database.

        Args:
            voc_or_sent (str): The vocabulary or sentence to be deleted.
        """
        self.__cur.execute(
            f"""DELETE FROM vocabs WHERE voc_or_sent = '{voc_or_sent}'"""
        )
        return self.load_records()

    def edit_record_translation(self, voc_or_sent, new_translation):
        """
        Edit the translation of a specific record.

        This method allows you to edit the translation of a specific record in the database.

        Args:
            voc_or_sent (str): The vocabulary or sentence to be edited.
            new_translation (str): The updated translation.
        """
        self.__cur.execute(
            f"""UPDATE vocabs SET translation = '{new_translation}' WHERE voc_or_sent = '{voc_or_sent}'"""
        )
        return self.load_records()
