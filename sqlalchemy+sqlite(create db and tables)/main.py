import os

from models.database import DATABASE_NAME
import create_database as db_creator


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()


