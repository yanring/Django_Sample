from django.test import TestCase,Client
from models import User
class SomeTest(TestCase):
    def setUp(self):
        User.objects.create(username='yanzijie',password="123456")
        pass

    def testUser(self):
        '''test'''
        u = User.objects.get(username='yanzijie')
        self.assertEqual(u.password, '123456')

    # def testLogin(self):
        c = Client()
        re = c.post('/login/', {'username': 'yanzijie', 'password': '123456'})
        print(re.content)

        self.assertEqual(re.status_code, 302)

    def testUser2(self):
        '''test'''
        u = User.objects.get(username='yanzijie')
        self.assertEqual(u.password, '1234567')

    def testLogin1(self):
        c = Client()
        re = c.post('/login/', {'username': 'yanzijie', 'password': '123456'})
        #print(re.content)
        self.assertEqual(re.status_code, 302)
    def testLogin2(self):
        c = Client()
        re = c.post('/login/', {'username': 'yanzijie2', 'password': '123456'})
        #print(re.content)
        self.assertEqual(re.status_code, 302)
    def testViewArticle(self):
        c = Client()
        re = c.post('/1')
        print(re)
        print(re.content)
        #print(type(c.get('/regist')))
        self.assertEqual(re.status_code, 301)
