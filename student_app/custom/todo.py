import frappe
from frappe.desk.doctype.todo.todo import ToDo

class CustomToDo(ToDo):

    def on_update(self):
        frappe.msgprint("ToDo Updated")