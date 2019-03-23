class Ledger:

    order_no = []
    content_recieved = []
    rate_content = []
    empty_recieved = []
    rate_empty = []
    debit = []
    empty_returned = []
    wrong_bottle = []
    cash_pay = []
    credit = []
    CandE = []
    empty_only = []

    def __init__(self, index, order_no, content_recieved, rate_content, empty_recieved, rate_empty, debit, empty_returned, wrong_bottle, cash_pay, credit, CandE, empty_only):
        self.index = index
        self.order_no = order_no
        self.content_recieved = content_recieved
        self.rate_content = rate_content
        self.empty_recieved = empty_recieved
        self.rate_empty = rate_empty
        self.debit = debit
        self.empty_returned = empty_returned
        self.wrong_bottle = wrong_bottle
        self.cash_pay = cash_pay
        self.credit = credit
        self.CandE = CandE
        self.empty_only = empty_only

    def genesis_input(self):

        self.index = 0
        self.order_no = int(input("Enter Order No: "))
        self.content_recieved = int(input("Enter No of Content Recieved: "))
        self.rate_content = int(input("Enter Rate Content: "))
        self.empty_recieved = int(input("Enter Empty Recieved: "))
        self.rate_empty = int(input("Enter rate empty: "))
        self.empty_returned = int(input("Enter empty returned: "))
        self.wrong_bottle = int(input("Enter Wrong Bottle no: "))
        self.cash_pay = int(input("Enter cash amount payed: "))
        self.debit = int((self.content_recieved * self.rate_content) +
                         (self.empty_recieved * self.rate_empty))
        self.credit = int((self.empty_returned * self.rate_empty) +
                          ((self.wrong_bottle * self.rate_empty * 0.5) + self.cash_pay))
        self.CandE = int(self.credit - self.debit)
        self.empty_only = int(self.empty_returned - self.empty_recieved)
        return Ledger(self.index, self.order_no, self.content_recieved, self.rate_content, self.empty_recieved, self.rate_empty, self.empty_returned,
                      self.wrong_bottle, self.cash_pay, self.debit, self.credit, self.CandE, self.empty_only)

def next_block(last_block):
    this_index = last_block.index + 1
    this_order_no = int(input("Enter Order No: "))
    this_content_recieved = int(input("Enter No of Content Recieved: "))
    this_rate_content = int(input("Enter Rate Content: "))
    this_empty_recieved = int(input("Enter Empty Recieved: "))
    this_rate_empty = int(input("Enter rate empty: "))
    this_empty_returned = int(input("Enter empty returned: "))
    this_wrong_bottle = int(input("Enter Wrong Bottle no: "))
    this_cash_pay = int(input("Enter cash amount payed: "))
    this_debit = int((this_content_recieved * this_rate_content) +
                     (this_empty_recieved * this_rate_empty))
    this_credit = int((this_empty_returned * this_rate_empty) +
                      (this_wrong_bottle * this_rate_empty * 0.5) + this_cash_pay)
    this_CandE = int(last_block.CandE + (this_credit - this_debit))
    this_empty_only = int(last_block.empty_only + this_empty_returned - this_empty_recieved)

    return Ledger(this_index, this_order_no, this_content_recieved, this_rate_content, this_empty_recieved, this_rate_empty, this_empty_returned,
                  this_wrong_bottle, this_cash_pay, this_debit, this_credit, this_CandE, this_empty_only)


print(Ledger.content_recieved)
