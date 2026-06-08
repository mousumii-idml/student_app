// Copyright (c) 2026, Mousumi and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Enrollment", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Enrollment", {
    refresh(frm) {

        frm.set_query("course", function() {
            return {
                filters: {
                    available_seats: [">", 0]
                }
            };
        });

    }
});