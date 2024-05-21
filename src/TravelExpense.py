from src.Expense import Expense
class TravelExpense(Expense):
    def print_name(self):
        print(self.tittel)
    def get_sum(self):
        return self.totalsum

    def set_status(self,status):
        self.status = status
