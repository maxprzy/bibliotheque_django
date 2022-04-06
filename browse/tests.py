from django.test import TestCase

# Create your tests here.

class testFail(TestCase):
    def testFail(self):
        response = self.client.get('/browse')
        self.assertContains(response, 'Raté')

