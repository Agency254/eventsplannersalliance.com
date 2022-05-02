from django.contrib.auth.models import User
from django.test import TestCase

from epa_frontend.models import Profile


class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='karanu', first_name='Newton', last_name='Kiragu', password='karanu')

    def testFirstNameLabel(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 30)

    def test_object_name_is_first_name_space_last_name(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.first_name} {user.last_name}'
        self.assertEqual(str(user.get_full_name()), expected_object_name)


class ProfileTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='karanu', first_name='Newton', last_name='Kiragu', password='karanu')
        Profile.objects.create(user=User.objects.get(), email='karanunewton4@gmail.com', bio='some catchy bio', country_code='KE')

    def test_profile_is_linked_to_user(self):
        user = User.objects.get(id=1)
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.user.id, user.id)

    def test_profile_has_username(self):
        pass
