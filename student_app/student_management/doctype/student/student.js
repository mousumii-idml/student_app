frappe.ui.form.on("Student", {
    refresh(frm) {

        frm.add_custom_button("Get Assignment Details", function () {

            frappe.call({
                method: "student_app.student_management.doctype.student.student.get_assignment_details",
                args: {
                    student: frm.doc.name
                },
                callback: function (r) {

                    if (r.message) {

                        frappe.msgprint({
                            title: "Assignment Details",
                            message:
                                "<b>Course:</b> " + r.message.course +
                                "<br><b>Semester:</b> " + r.message.semester +
                                "<br><b>Assignment Details:</b> " +
                                r.message.assignment_details
                        });

                    } else {

                        frappe.msgprint("No Assignment Found");

                    }
                }
            });

        });

    }
});