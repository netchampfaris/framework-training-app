# Copyright (c) 2022, Frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Article(WebsiteGenerator):
	def get_title(self):
		return self.name

	def get_test(self):
		return 'asdf'

	@frappe.whitelist()
	def set_isbn(self):
		self.isbn = frappe.generate_hash('Article', 10)


@frappe.whitelist()
def get_isbn():
	return frappe.generate_hash('Article', 10)
