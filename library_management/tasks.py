# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe


def monthly():
    # pdf_content =
    frappe.sendmail('customeremail', attachments=[
        {
            'fcontent': pdf_content,
            'fname': 'report.pdf',
        }
    ])
