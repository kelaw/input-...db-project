from blockchain1 import Block
from testing2 import open_transactions, participants, blockchain
from input_file import users
import functools


class User(Block):
    def __init__(self, balance):
        self.user_name = input('Enter the sender of the transaction: ')
        self.balance = balance

        User.no_of_instances += 1

    @staticmethod
    def get_transaction_val():
        """ Returns the input of the user as a float(new transaction)"""
        tx_sender = users()
        tx_recipient = input('Enter the recipient of the transaction: ')
        tx_amount = float(input('Your transaction amount please: '))
        return tx_recipient, tx_sender, tx_amount

    def get_balance(self, participant):
        self.balance = 0
        tx_sender = [[trx['amount'] for trx in block.data if trx['sender'] == participant] for block in blockchain]
        open_trx_sender = [trx['amount'] for trx in open_transactions if trx['sender'] == participant]
        tx_sender.append(open_trx_sender)
        amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)

        tx_recipient = [[trx['amount'] for trx in block.data if trx['recipient'] == participant] for block in
                        blockchain]
        amount_received = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)

        calc1 = amount_received - amount_sent
        self.balance += calc1
        return self.balance

    def verify_trx(self, transaction):
        sender_balance = self.balance
        return sender_balance >= transaction['amount']

    def add_transaction(self, recipient, sender=None, amount=None):
        verify_trx = User.verify_trx
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        if verify_trx(self, transaction):
            open_transactions.append(transaction)
            participants.add(self.user_name)
            participants.add(recipient)
            return True
        return False
