# Copyright (c) 2022, Frappe and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	# columns = [df1, df2]
	# result = [{'df1': 'val1', 'df2': 'val2'}, ...]
	# message = 'Hello World'
	# chart = {
	# 	"data": {
	# 		"labels": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
	# 		"datasets": [
	# 			{"name": "Some Data", "values": [25, 40, 30, 35, 8]},
	# 			{"name": "Another Set", "values": [25, 50, -10, 15, 18]},
	# 		],
	# 	}
	# }

	# data = columns, result, message, chart, report_summary

	# return data

	chart = {
		"type": "bar",
		"data": {
			"labels": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
			"datasets": [
				{"name": "Some Data", "values": [25, 40, 30, 35, 8]},
				{"name": "Another Set", "values": [25, 50, -10, 15, 18]},
			],
		}
	}

	profit = 20

	report_summary = [
			{"value": 1200, "label": 'Income', "datatype": "Currency", "currency": 'INR'},
			{"type": "separator", "value": "-"},
			{"value": 300, "label": 'Expense', "datatype": "Currency", "currency": 'INR'},
			{"type": "separator", "value": "=", "color": "blue"},
			{"value": 1200 - 300, "indicator": "Green" if profit > 0 else "Red", "label": 'Profit/Loss',"datatype": "Currency","currency": 'INR'},
	]

	columns = [
		{'fieldtype': 'Data', 'label': 'Book Name', 'fieldname': 'book_name', 'width': 100},
		{'fieldtype': 'Data', 'label': 'Author', 'fieldname': 'author', 'width': 100},
		{'fieldtype': 'Int', 'label': 'Age', 'fieldname': 'age', 'width': 100},
	]

	result = [
		{'book_name': 'Book 1', 'author': 'Author 1', 'age': 6},
		{'book_name': 'Book 2', 'author': 'Author 2', 'age': 10},
		{'book_name': 'Book 3', 'author': 'Author 3', 'age': 12},
	]

	return columns, result, "Report generated 3 minutes ago", chart, report_summary
