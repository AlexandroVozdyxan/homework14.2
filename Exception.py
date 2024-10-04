import Group, Student

class FullGroupError(Exception):
    def __init__(self, text="Group is full."):
        self.text = text
        super().__init__(self.text)
# try:
#     group = Group("ФИТ")
#     students = [Student("gender","age", "first_name", "last_name", "record_book") for i in range(12)]
#
#     raise FullGroupError("Group is full.")
# except FullGroupError as fge:
#     print(f"Group error: {fge}")