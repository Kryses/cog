# Create your tests here.
from assets.models import AssetType, Asset
from cog.base_classes.test_classes import UserProjectBaseClass
from notes.models import Note
from pipelines.models import Pipeline, Status


class TestAssetModel(UserProjectBaseClass):
    def setUp(self):
        super(TestAssetModel, self).setUp()
        self.asset_type = AssetType.objects.get_or_create(name='test type', project=self.project)
        self.note_names = ['Note 1', 'Note 2', 'Note 3']
        self.notes = []
        for note in self.note_names:
            self.notes.append(Note.objects.get_or_create(name=note, text='test')[0])

        self.pipeline = Pipeline.objects.get_or_create(name='Pipeline')[0]
        self.status = Status.objects.get_or_create(name='Ready')[0]
        self.asset = Asset.objects.get_or_create(name='test asset', asset_type=self.asset_type[0], status=self.status)[
            0]
        self.asset.notes.add(*self.notes)
        self.asset.pipeline = self.pipeline
        self.asset.save()

    def test_name(self):
        asset = Asset.objects.get(name=self.asset.name)
        self.assertEquals(asset.name, self.asset.name)

    def test_notes(self):
        asset = Asset.objects.get(name=self.asset.name)
        notes = asset.notes.values_list('name', flat=True)
        for i in self.note_names:
            self.assertIn(i, notes)

    def test_pipelines(self):
        asset = Asset.objects.get(name=self.asset.name)
        self.assertEquals(asset.pipeline.name, self.pipeline.name)

    def test_status(self):
        asset = Asset.objects.get(name=self.asset.name)
        self.assertEquals(asset.status.name, self.status.name)
