frappe.ui.form.on("Assignment", {
    setup(frm) {
        frm.make_methods = {
            ToDo: () => {
                frappe.model.open_mapped_doc({
                    method: "student_app.student_management.api.connections.make_todo.make_todo",
                    args: {
                        referenceType: "Assignment",
                        source_name: frm.doc.name
                    }
                });
            }
        };
    }
});