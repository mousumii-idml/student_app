import frappe
from frappe.model.document import Document


class Assignment(Document):

    def validate(self):
        enrollment = frappe.db.exists(
            "Enrollment",
            {
                "student": self.student,
                "course": self.course,
                "semester": self.semester
            }
        )

        if not enrollment:
            frappe.throw(
                "Selected student is not enrolled in the selected course and semester"
            )

    def on_update(self):
        if self.status == "Completed":

            # Direct call for testing
            update_student_grade(
                self.name,
                self.student
            )


@frappe.whitelist()
def update_student_grade(assignment, student):

    grade = "A"

    frappe.db.set_value(
        "Student",
        student,
        "grade",
        grade
    )

    frappe.db.commit()