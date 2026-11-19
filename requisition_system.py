#Assessment 2



print("Welcome to Purchase Requisition System")
print("Assessment 2 - Software Development Project")

class Requisition:

    next_id = 10001
    all_requisitions = []

    def __init__(self, date, staff_id, staff_name):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name

        self.requisition_id = Requisition.next_id
        Requisition.next_id += 1

        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

        Requisition.all_requisitions.append(self)

    
    def add_requisition(self, items):
        self.items = items
        self.total = 0

        for item_name, price in items:
            self.total += price

        return self.total


    
    def check_approval(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = "APR-" + str(self.requisition_id)
        else:
            self.status = "Pending"

        return self.status



    def manager_approval(self, decision):
        if self.status == "Pending":
            if decision == "Approve":
                self.status = "Approved"
                self.approval_reference = "APR-" + str(self.requisition_id)
            elif decision == "Reject":
                self.status = "Rejected"

        return self.status


    def display_requisition(self):
        print("---------------------------")
        print("Requisition ID:", self.requisition_id)
        print("Date:", self.date)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total Cost: $", self.total)
        print("Status:", self.status)
        print("Approval Reference:", self.approval_reference)
        print("---------------------------")


    @classmethod
    def display_statistics(cls):
        total = len(cls.all_requisitions)
        approved = 0
        pending = 0
        rejected = 0

        for requisition in cls.all_requisitions:
            if requisition.status == "Approved":
                approved += 1
            elif requisition.status == "Pending":
                pending += 1
            elif requisition.status == "Rejected":
                rejected += 1

        print("\nREQUISITION STATISTICS")
        print("Total Requisitions:", total)
        print("Approved:", approved)
        print("Pending:", pending)
        print("Rejected:", rejected)


request1 = Requisition("19/11/2026", "FN19", "John")
request2 = Requisition("19/11/2026", "FN20", "Emma")

print("First Requisition ID:", request1.requisition_id)
print("Second Requisition ID:", request2.requisition_id)


print("Total Requisitions:", len(Requisition.all_requisitions))


items1 = [
    ("Laptop", 1200),
    ("Mouse", 50),
    ("Keyboard", 100)
]

request1.add_requisition(items1)

print("Purchase Items:", request1.items)
print("Total Cost: $", request1.total)

request1.check_approval()

print("Requisition Status:", request1.status)


items2 = [
    ("Mouse", 50),
    ("Keyboard", 100)
]

request2.add_requisition(items2)
request2.check_approval()

print("Second Requisition Total: $", request2.total)
print("Second Requisition Status:", request2.status)


request3 = Requisition("19/11/2026", "FN21", "Alex")

items3 = [
    ("Office Chair", 300),
    ("Desk Lamp", 200)
]

request3.add_requisition(items3)
request3.check_approval()

print("Third Requisition ID:", request3.requisition_id)
print("Third Requisition Total: $", request3.total)
print("Third Requisition Status:", request3.status)

print("Before Manager Approval:", request1.status)

request1.manager_approval("Approve")

print("After Manager Approval:", request1.status)


print("Before Manager Rejection:", request3.status)

request3.manager_approval("Reject")

print("After Manager Rejection:", request3.status)

print("\nALL REQUISITIONS")

for requisition in Requisition.all_requisitions:
    requisition.display_requisition()

Requisition.display_statistics()

print("\nMANAGER APPROVAL REFERENCE TEST")
print("Request 1 Approval Reference:", request1.approval_reference)


print("\nAPPROVAL REFERENCE TEST")
print("Request 2 Approval Reference:", request2.approval_reference)


print("\nREQUISITION 4")

request4 = Requisition("19/11/2026", "FN22", "Sam")

items4 = [("Office Supplies", 499)]

request4.add_requisition(items4)
request4.check_approval()


request4.display_requisition()

print("\nASSERTION TEST")

assert request4.total == 499
assert request4.status == "Approved"
assert request4.approval_reference == "APR-10004"

print("All assertion tests passed!")

print("\nAPPROVAL DECISION TESTS")

assert request1.status == "Approved"
assert request2.status == "Approved"
assert request3.status == "Rejected"

assert request1.approval_reference == "APR-10001"
assert request2.approval_reference == "APR-10002"
assert request3.approval_reference == "Not available"

print("All approval decision tests passed!")

print("\nFINAL REQUISITION STATISTICS")
Requisition.display_statistics()

print("\nFIFTH REQUISITION TEST")

request5 = Requisition("19/11/2026", "FN23", "David")

items5 = [("Printer", 350), ("Paper", 50)]

request5.add_requisition(items5)
request5.check_approval()

request5.display_requisition()

print("\nUPDATED STATISTICS")
Requisition.display_statistics()


