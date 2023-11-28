# Complaint-Management-System-Project-in-Python

The ComplaintManagementSystem class is defined to encapsulate the functionality of the complaint management system.

The __init__ method initializes the system by creating an empty dictionary (self.complaints) to store complaints. Each complaint is associated with a unique identifier.

The submit_complaint method allows users to submit a complaint. It takes a title and content as input, generates a unique complaint ID, and creates a dictionary representing the complaint. The complaint is then added to the self.complaints dictionary, and the complaint ID is returned.

The view_complaints method displays all the complaints stored in the system. It checks if there are any complaints, and if there are, it iterates through the dictionary and prints details such as the complaint ID, title, content, and status.

The resolve_complaint method allows users to mark a complaint as resolved. It takes a complaint ID as input, checks if the ID exists in the system, and if so, updates the status of the corresponding complaint to "Resolved."

The if __name__ == "__main__": block initializes an instance of the ComplaintManagementSystem and provides a simple console-based user interface for users to interact with the system. The user can submit complaints, view existing complaints, resolve complaints, or exit the system.
