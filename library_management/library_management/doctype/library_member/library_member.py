# Copyright (c) 2022, Frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LibraryMember(Document):
	def before_save(self):
		self.full_name = self.first_name + " " + (self.last_name or '')
		self.compute_age()

	def compute_age(self):
		if self.date_of_birth:
			self.age = frappe.utils.date_diff(frappe.utils.today(), self.date_of_birth) / 365
