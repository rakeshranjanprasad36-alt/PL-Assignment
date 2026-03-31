class Human:
    def __init__(self, n, a):
        self.n = n
        self.a = a

    def show_basic(self):
        print(f"Name: {self.n}, Age: {self.a}")


class Worker(Human):
    def __init__(self, n, a, emp_id, pay):
        super().__init__(n, a)
        self.emp_id = emp_id
        self.pay = pay

    def show_job(self):
        print(f"Employee ID: {self.emp_id}, Salary: ${self.pay:.2f}")


class Supervisor(Worker):
    def __init__(self, n, a, emp_id, pay, dept):
        super().__init__(n, a, emp_id, pay)
        self.dept = dept

    def show_all(self):
        self.show_basic()
        self.show_job()
        print(f"Department: {self.dept}")


mgr = Supervisor("Alice Johnson", 40, "MGR102", 85000, "IT")

print("Manager Information")
mgr.show_all()