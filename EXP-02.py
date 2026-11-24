def wrap(func):
    def wrapper(*args):
        print("\n--- REPORT ---")
        func(*args)
        print("----------------")
    return wrapper


class Report:
    template = "Simple"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def change_template(cls, t):
        cls.template = t

    def __str__(self):
        return f"{self.title}: {self.content}"

    @wrap
    def show(self):
        print("Template:", Report.template)
        print(self)


while True:
    print("\n1. Create Report\n2. Change Template\n3. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        t = input("Title: ")
        c = input("Content: ")
        r = Report(t, c)
        r.show()

    elif ch == 2:
        Report.change_template(input("New Template: "))

    elif ch == 3:
        break