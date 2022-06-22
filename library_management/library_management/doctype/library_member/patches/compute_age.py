# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe


def execute():
	for member in frappe.db.get_all('Library Member', pluck='name'):
		doc = frappe.get_doc('Library Member', member)
		doc.compute_age()
		doc.save()
