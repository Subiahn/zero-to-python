from budget import FamilyBudgetApp

app = FamilyBudgetApp("김철수")
app.add_income(50000, "알바비")
app.add_income(30000, "용돈")
app.add_expense(12000, "점심")
app.add_expense(3500, "커피")
app.owner_show()
app.show_all()