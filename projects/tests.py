# Create your tests here.
from cog.base_classes.test_classes import UserProjectBaseClass


class TestProject(UserProjectBaseClass):
    """Tests for the project model."""
    def test_users(self):
        self.assertEquals(self.project.users.get(username='test'), self.user)