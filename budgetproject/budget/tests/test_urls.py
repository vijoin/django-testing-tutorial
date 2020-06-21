from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import project_list, ProjectCreateView, project_detail


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse('list')
        self.assertEqual(resolve(url).func, project_list)

    def test_create_url_resolves(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func.view_class, ProjectCreateView)

    def test_detail_url_resolves(self):
        url = reverse('detail', args=['project1'])
        self.assertEqual(resolve(url).func, project_detail)
