# Copyright (c) 2022, Frappe and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestLibrarySystem(FrappeTestCase):
	def test_article_creation(self):
		article = frappe.get_doc(
			doctype='Article',
			name='Book 1',
			author='Test Author'
		).insert()

		self.assertEqual(article.name, 'Book 1')


