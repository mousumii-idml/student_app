import frappe
from frappe.utils import add_years, nowdate

def execute():
    one_year_ago = add_years(nowdate(), -1)

    enrollments = frappe.get_all(
        "Enrollment",
        filters={
            "enrollment_date": [">=", one_year_ago]
        },
        fields=["student"]
    )

    for e in enrollments:
        frappe.db.set_value(
            "Student",
            e.student,
            "status",
            "Active"
        )

    frappe.db.commit()