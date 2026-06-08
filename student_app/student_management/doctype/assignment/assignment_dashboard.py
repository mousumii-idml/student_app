from frappe import _

def get_data(data=None):
    return {
        "fieldname": "reference_name",
        "transactions": [
            {
                "label": _("Connections"),
                "items": ["ToDo"]
            }
        ]
    }