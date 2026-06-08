import frappe
from frappe.model.mapper import get_mapped_doc


@frappe.whitelist()
def make_todo(target_doc=None):

    source_name = frappe.flags.args.source_name

    def set_values(source, target):
        _set_hardCoded_values("Assignment", source, target)

    target_doc = get_mapped_doc(
        "Assignment",
        source_name,
        {
            "Assignment": {
                "doctype": "ToDo",
                "field_map": {
                    "name": "reference_name"
                }
            }
        },
        target_doc,
        set_values,
    )

    return target_doc


def _set_hardCoded_values(referenceType, source, target):

    target.reference_type = referenceType
    target.reference_name = source.name

    if hasattr(source, "assignment_details"):
        target.description = source.assignment_details

    target.assigned_by = frappe.session.user

    if hasattr(source, "allocated_to"):
        target.allocated_to = source.allocated_to

    if hasattr(source, "priority"):
        target.priority = source.priority

    if hasattr(source, "status"):
        target.status = source.status