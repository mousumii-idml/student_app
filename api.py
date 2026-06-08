import frappe


@frappe.whitelist()
def get_latest_assignment(student):

    assignment = frappe.get_all(
        "Assignment",
        filters={
            "student": student
        },
        fields=[
            "course",
            "semester",
            "assignment_details"
        ],
        order_by="creation desc",
        limit=1
    )

    if assignment:
        return assignment[0]

    return None