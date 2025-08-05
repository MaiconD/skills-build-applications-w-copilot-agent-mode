from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_data
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populates the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        for collection_name, data in test_data.items():
            collection = db[collection_name]
            collection.insert_many(data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
