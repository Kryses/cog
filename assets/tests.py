from django.test import TestCase

# Create your tests here.
from assets.models import AssetType
from cog.base_classes.test_classes import UserProjectBaseClass


class TestAssetModel(UserProjectBaseClass):
    def setUp(self):
        super(TestAssetModel, self).setUp()

    def test_name(self):
        self.assertTrue(False)

    def test_notes(self):
        self.assertTrue(False)

    def test_pipelines(self):
        self.assertTrue(False)

    def test_status(self):
        self.assertTrue(False)