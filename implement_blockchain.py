import datetime as date
from input_file import input_choice, input_value0, input_value1, input_value2, input_value3, input_value4, \
    input_value5, input_value6, input_value7
import hashlib as hasher


class Ledger:
    no_of_instances = 0

    def __init__(self, index, timestamp, order_no, content_received, rate_content, empty_received, rate_empty, debit,
                 empty_returned, wrong_bottle, cash_pay, credit, cash_n_carry, empty_only, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.order_no = order_no
        self.content_received = content_received
        self.rate_content = rate_content
        self.empty_received = empty_received
        self.rate_empty = rate_empty
        self.debit = debit
        self.empty_returned = empty_returned
        self.wrong_bottle = wrong_bottle
        self.cash_pay = cash_pay
        self.credit = credit
        self.cash_n_carry = cash_n_carry
        self.empty_only = empty_only
        self.previous_hash = previous_hash
        Ledger.no_of_instances += 1

        print('this is ' + str(Ledger.no_of_instances) + ' instance')

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + str(self.timestamp) +
                    str(self.order_no) + str(self.content_received) + str(self.rate_content) + str(self.empty_received)
                    + str(self.rate_empty) + str(self.debit) + str(self.empty_returned) + str(self.wrong_bottle)
                    + str(self.cash_pay) + str(self.credit) + str(self.cash_n_carry) + str(self.empty_only)
                    + str(self.previous_hash)).encode("utf-8"))
        return sha.hexdigest()


def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    index = 0
    gen_order_no = input_value0()
    gen_content_received = input_value1()
    gen_rate_content = input_value2()
    gen_empty_received = input_value3()
    gen_rate_empty = input_value4()
    gen_debit = (gen_content_received * gen_rate_content) + (gen_empty_received * gen_rate_empty)
    gen_empty_returned = input_value5()
    gen_wrong_bottle = input_value6()
    gen_cash_pay = input_value7()
    gen_credit = (gen_empty_returned * gen_rate_empty) + ((gen_wrong_bottle * gen_rate_empty * 0.5) + gen_cash_pay)
    gen_cash_n_carry = gen_credit - gen_debit
    gen_empty_only = gen_empty_returned - gen_empty_received
    print('Empty only 1: ' + str(gen_empty_only))

    return Ledger(index, date.datetime.now(), gen_order_no, gen_content_received, gen_rate_content, gen_empty_received,
                  gen_rate_empty, gen_debit, gen_empty_returned, gen_wrong_bottle, gen_cash_pay, gen_credit,
                  gen_cash_n_carry, gen_empty_only, "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_order_no = input_value0()
    this_content_received = input_value1()
    this_rate_content = input_value2()
    this_empty_received = input_value3()
    this_rate_empty = input_value4()
    this_debit = (this_content_received * this_rate_content) + (this_empty_received * this_rate_empty)
    this_empty_returned = input_value5()
    this_wrong_bottle = input_value6()
    this_cash_pay = input_value7()
    this_credit = (this_empty_returned * this_rate_empty) + (
                (this_wrong_bottle * this_rate_empty * 0.5) + this_cash_pay)
    this_cash_n_carry = last_block.cash_n_carry + (this_credit - this_debit)
    this_empty_only = last_block.empty_only + (this_empty_returned - this_empty_received)
    this_hash = last_block.previous_hash
    print('Empty only last block: ' + str(last_block.empty_only))
    print('Empty only 2: ' + str(this_empty_only))

    return Ledger(this_index, date.datetime.now(), this_order_no, this_content_received, this_rate_content,
                  this_empty_received, this_rate_empty, this_debit, this_empty_returned, this_wrong_bottle,
                  this_cash_pay, this_credit, this_cash_n_carry, this_empty_only, this_hash)


blockchain = []


def add_value(trx_amounts):
    blockchain.append(trx_amounts)


def print_blockchain():
    for block in blockchain:
        dicts = {'index': block.index, 'Empty Received': block.empty_received, 'Empty Returned': block.empty_returned,
                 'Empty Only': block.empty_only}
        counter = 1
        print('Current value in blockchain after ' + str(counter) + ' transactions')
        print(dicts)
        counter += 1


def get_last_blockchain_val():
    """ Returns last value of the current blockchain """

    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def confirm_block_in_blockchain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
        if block.previous_hash == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
        break
    return is_valid


def main():
    while True:

        print('''Please choose: 
                 1: Add a new transaction
                 2: Show blockchain
                 3: Confirm Block
                 4: Show last value in blockchain
                 5: Quit''')
        global last_bloc

        user_choice = input_choice()

        if user_choice == '1':
            if len(blockchain) < 1:
                blockchain.append(create_genesis_block())
                last_bloc = blockchain[0]
            else:
                trx_amounts = next_block(last_bloc)
                add_value(trx_amounts)
                last_bloc = trx_amounts
        elif user_choice == '2':
            print_blockchain()

        elif user_choice == '3':
            continue
        elif user_choice == '4':
            get_last_blockchain_val()
        elif user_choice == '5':
            break
        else:
            print('invalid choice, please a value from the list')


main()



