import frappe

def execute():
    print("PatchRunning")

    courses = [
        {"course_name": "Java", "duration": 3},
        {"course_name": "Python", "duration": 2},
        {"course_name": "SQL", "duration": 1},
        {"course_name": "React", "duration": 4},
        {"course_name": "AWS", "duration": 2}
    ]

    for c in courses:
        doc = frappe.get_doc({
            "doctype": "Course",
            "course_name": c["course_name"],
            "duration": c["duration"],
            "fees": 1000,
            "available_seats": 10
        })

        doc.insert(ignore_permissions=True)

    frappe.db.commit()