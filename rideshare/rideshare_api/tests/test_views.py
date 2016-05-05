from django.contrib.auth.models import User
from rideshare_profile.models import Profile, Route
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from django.contrib.gis.geos import GEOSGeometry


class TestEndpoints(APITestCase):
    """Test request and response of endpoints."""

    def setUp(self):
        """Setup."""
        self.client = APIClient()
        self.profile = Profile()
        self.user = User.objects.create_user(username='foo', password='foobared')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.profile.user = self.user
        self.profile.carbrand = 'Audi'
        self.profile.carseat = 1
        self.profile.petsallowed = True
        self.profile.save()
        self.route = Route()
        self.route.user = self.profile
        self.route.start_point = GEOSGeometry('POINT(2 3)', srid=4326)
        self.route.save()

    def tearDown(self):
        """Teardown."""
        User.objects.all().delete()
        Profile.objects.all().delete()
        Route.objects.all().delete()

    # def test_post_user(self):
    #     """Test that when a user is added it is in the database."""

    def test_get_user(self):
        """Test that a user returned when a get request is performed."""
        response = self.client.get('/users/{}/'.format(self.user.id))
        self.assertEqual(response.data[0]['username'], 'foo')

    def test_post_user(self):
        """Test that a user is created when a post request is performed."""
        post = self.client.post('/users/', {'username': 'joe',
                                            'password': 'i love beer'})
        self.assertEquals(post.data['username'], 'joe')
        self.assertEquals(post.data['password'], 'i love beer')

    def test_get_route(self):
        """Test that you can get a route."""
        response = self.client.get('/routes/{}/'.format(self.route.id))
        self.assertEqual(response.data['start_point'],
                         u'SRID=4326;POINT (2.0000000000000000 3.0000000000000000)')

    def test_get_route_no_route_exists(self):
        """Test that you can get a route."""
        response = self.client.get('/routes/500/')
        self.assertEqual(response.data, {u'detail': u'Not found.'})

    def test_get_profile(self):
        """Test that you can get a profile."""
        response = self.client.get('/profiles/{}/'.format(self.profile.id))
        self.assertEqual(response.data['carbrand'], 'Audi')

    # def test_add_route(self):
    #     """Test that a post to /routes/add/ adds a route to the database."""

    def test_query_get_exact_point(self):
        """Test query on same point returns point."""
        response = self.client.get('/query/', {'lat': '2',
                                               'lng': '3'})
        self.assertEqual(response.data[0]['start_point'], u'SRID=4326;POINT (2.0000000000000000 3.0000000000000000)')

    def test_query_get_near_point(self):
        """Test query on nearby coordinates returns nearest."""
        response = self.client.get('/query/', {'lat': '2.0000000000000001',
                                               'lng': '3.0000000000000002'})
        self.assertEqual(response.data[0]['start_point'], u'SRID=4326;POINT (2.0000000000000000 3.0000000000000000)')

    def test_query_two_routes_return(self):
        """Test query with multiple returns."""
        profile1 = Profile()
        user1 = User.objects.create_user(username='billy', password='truckstop')
        user1.save()
        self.client.force_authenticate(user=user1)
        profile1.user = user1
        profile1.carbrand = 'Audi'
        profile1.carseat = 1
        profile1.petsallowed = True
        profile1.save()
        route1 = Route()
        route1.user = profile1
        route1.start_point = GEOSGeometry('POINT(2.0000000000000009 3.0000000000000009)', srid=4326)
        route1.save()
        response = self.client.get('/query/', {'lat': '2.0000000000000001',
                                               'lng': '3.0000000000000002'})
        self.assertEqual(response.data[0]['start_point'], u'SRID=4326;POINT (2.0000000000000000 3.0000000000000000)')
        self.assertEqual(response.data[1]['start_point'], u'SRID=4326;POINT (2.0000000000000009 3.0000000000000009)')
