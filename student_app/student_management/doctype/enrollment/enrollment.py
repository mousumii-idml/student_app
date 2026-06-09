import frappe
from frappe.model.document import Document

class Enrollment(Document):

    def on_submit(self):
        course = frappe.get_doc("Course", self.course)

        course.available_seats = course.available_seats - 1

        course.save()

        frappe.msgprint("Enrollment Submitted")

    def on_cancel(self):
        course = frappe.get_doc("Course", self.course)

        course.available_seats = course.available_seats + 1

        course.save()

        frappe.msgprint("Enrollment Cancelled")

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_courses(doctype, txt, searchfield, start, page_len, filters):

    return frappe.db.sql("""
        SELECT
            name
        FROM `tabCourse`
        WHERE available_seats > 0
        AND name LIKE %(txt)s
        LIMIT %(start)s, %(page_len)s
    """, {
        "txt": "%" + txt + "%",
        "start": start,
        "page_len": page_len
    })