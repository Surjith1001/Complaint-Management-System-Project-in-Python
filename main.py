class ComplaintManagementSystem:
    def __init__(self):
        self.complaints = {}

    def submit_complaint(self, title, content):
        complaint_id = len(self.complaints) + 1
        complaint = {"title": title, "content": content, "status": "Open"}
        self.complaints[complaint_id] = complaint
        return complaint_id

    def view_complaints(self):
        if not self.complaints:
            print("No complaints available.")
        else:
            for complaint_id, complaint in self.complaints.items():
                print(f"Complaint ID: {complaint_id}")
                print(f"Title: {complaint['title']}")
                print(f"Content: {complaint['content']}")
                print(f"Status: {complaint['status']}")
                print("-" * 20)

    def resolve_complaint(self, complaint_id):
        if complaint_id in self.complaints:
            self.complaints[complaint_id]["status"] = "Resolved"
            print(f"Complaint {complaint_id} has been resolved.")
        else:
            print("Complaint not found.")

# Example Usage
if __name__ == "__main__":
    cms = ComplaintManagementSystem()

    while True:
        print("\nComplaint Management System")
        print("1. Submit a Complaint")
        print("2. View Complaints")
        print("3. Resolve a Complaint")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            title = input("Enter the complaint title: ")
            content = input("Enter the complaint content: ")
            complaint_id = cms.submit_complaint(title, content)
            print(f"Complaint submitted successfully. Complaint ID: {complaint_id}")

        elif choice == "2":
            cms.view_complaints()

        elif choice == "3":
            complaint_id = int(input("Enter the complaint ID to resolve: "))
            cms.resolve_complaint(complaint_id)

        elif choice == "4":
            print("Exiting the Complaint Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

