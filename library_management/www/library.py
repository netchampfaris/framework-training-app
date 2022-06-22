# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe


def get_context(context):
	# frappe.session.user -> Guest
	# frappe.session.user -> faris@erpnext.com
	context.articles = frappe.db.get_all('Article', '*', filters={'owner': frappe.session.user})
