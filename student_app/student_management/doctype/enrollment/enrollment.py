import frappe
from frappe.model.document import Document

class Enrollment(Document):
    pass


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_courses(doctype, txt, searchfield, start, page_len, filters):

    return frappe.db.sql("""
        SELECT
            name
        FROM `tabCourse`
        WHERE seats_available > 0
        AND name LIKE %(txt)s
        LIMIT %(start)s, %(page_len)s
    """, {
        "txt": "%" + txt + "%",
        "start": start,
        "page_len": page_len
    })