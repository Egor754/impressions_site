import random
import string
from unittest import TestCase

from myapp.forms import CreateMemoryForm


class RenewBookFormTest(TestCase):

    def test_create_form_date_field_label(self):
        form = CreateMemoryForm()
        self.assertTrue(form.fields['title'].label == 'Название')
        self.assertTrue(form.fields['description'].label == 'Описание')

    def test_create_form_date(self):
        form_data = {
            'title': ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 200))),
            'description': ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 500))),
            'latitude': 423.4234,
            'longitude': 123.1233,
        }
        form = CreateMemoryForm(data=form_data)
        self.assertTrue(form.is_valid())
