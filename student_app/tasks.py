import frappe

def update_attendance_count():

    attendance_list = frappe.get_all(
        "Student Attendance",
        fields=["name"]
    )

    for attendance in attendance_list:

        doc = frappe.get_doc(
            "Student Attendance",
            attendance.name
        )

        for row in doc.attendance_details:

            if row.attendance_status == "Present":

                current_count = frappe.db.get_value(
                    "Student",
                    row.student,
                    "attendance_count"
                ) or 0

                frappe.db.set_value(
                    "Student",
                    row.student,
                    "attendance_count",
                    current_count + 1
                )

    frappe.db.commit()