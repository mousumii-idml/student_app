frappe.ui.form.on("Enrollment", {
    refresh(frm) {

        frm.set_query("course", function () {
            return {
                query: "enrollment_system.enrollment_system.doctype.course.course.get_available_courses"
            };
        });

    }
});