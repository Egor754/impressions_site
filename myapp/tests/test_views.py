import random
import string

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from myapp.models import Memories


class ListViewTest(TestCase):

    def setUp(self):
        test_user1 = get_user_model().objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        value = 30
        for book_copy in range(value):
            Memories.objects.create(
                title=''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 200))),
                description=''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 500))),
                latitude=423.4234,
                longitude=123.1233,
                owner=test_user1
            )

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('main'))
        self.assertRedirects(resp, '/login/?next=/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('main'))
        self.assertEqual(str(resp.context['user']), 'testuser1')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')

    def test_only_borrowed_books_in_list(self):
        self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('main'))
        self.assertEqual(str(resp.context['user']), 'testuser1')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('memories' in resp.context)
        for memory in resp.context['memories']:
            self.assertEqual(resp.context['user'], memory.owner)


class CreateViewTest(TestCase):
    def setUp(self):
        test_user1 = get_user_model().objects.create_user(username='testuser1', password='12345')
        test_user1.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('create'))
        self.assertRedirects(resp, '/login/?next=/create/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('create'))
        self.assertEqual(str(resp.context['user']), 'testuser1')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'create_memory.html')
