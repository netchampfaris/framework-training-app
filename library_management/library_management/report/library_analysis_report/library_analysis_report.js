// Copyright (c) 2022, Frappe and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Library Analysis Report"] = {
	get_datatable_options(options) {
		options.hooks.columnTotal = (columnValues, cell) => {
			console.log(columnValues, cell)
			// return aggregated value
		}
		return options;
	},
	formatter: function(value, row, column, data, default_formatter) {
		if (column.fieldname === 'age') {
			if (value > 6) {
				return `<span class="text-success">${value}</span>`
			}
			return `<span class="text-danger">${value}</span>`
		}
		return value
	},
};
