import frappe

def execute():
    frappe.db.sql("""
        UPDATE `tabCourse`
        SET course_name = 'C Foundation'
        WHERE course_name = 'Bcd'
    """)

    frappe.db.commit()