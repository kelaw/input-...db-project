import hashlib as hasher
from input_file import input_choice
import datetime as date


class Block:
    no_of_instances = 0

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash

        Block.no_of_instances += 1

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + str(self.timestamp) +
                    str(self.data) + str(self.previous_hash)).encode("utf-8"))
        return sha.hexdigest()


blockchain = []
open_transactions = []
participants = {'>'}
miner_reward = 1
owner = input('Enter the sender of the transaction: ')


def get_transaction_val():
    """ Returns the input of the user as a float(new transaction)"""
    tx_sender = owner
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_recipient, tx_sender, tx_amount


def add_transaction(recipient, sender=None, amount=None):
    transactions = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transactions)
    participants.add(sender)
    participants.add(recipient)


def clear_block():
    open_transactions.clear()


def add_value(trx_amounts):
    blockchain.append(trx_amounts)


def mine_block():
    data = []
    reward_trx = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': miner_reward
    }

    for transaction in open_transactions:
        data.append(transaction)
    data.append(reward_trx)
    return data


def get_balance(participant):
    tx_sender = [[trx['amount'] for trx in block.data if trx['sender'] == participant] for block in blockchain]
    amount_sent = 0

    for tx in tx_sender:
        for x in range(len(tx)):
            if len(tx) > 0:
                amount_sent += tx[x]

    tx_recipient = [[trx['amount'] for trx in block.data if trx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        for x in range(len(tx)):
            if len(tx) > 0:
                amount_received += tx[x]

    return amount_sent, amount_received


def user_balance():
    balance = 0
    balance_trx = get_balance(owner)
    amount_sent, amount_received = balance_trx
    calc1 = amount_received - amount_sent
    balance += calc1

    return balance, amount_sent


# def verify_balance(transaction):
#     sender_balance = user_balance()
#     return sender_balance >= transaction['amount']


def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    data = mine_block()
    
    return Block(0, date.datetime.now(), data, "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = mine_block()
    this_hash = last_block.hash_block()
    print(this_data)
    return Block(this_index, this_timestamp, this_data, this_hash)


def confirm_block_in_blockchain():
    if len(blockchain) > 1:
        lag = Block.hash_block(blockchain[-1])
        for block in blockchain:
            lag1 = block.hash_block()
        print(lag + '\t' + lag1)
        if lag != lag1:
            print('invalid blockchain')
            return False
        else:
            print('its legit')
    else:
        print('blockchain will cont')
    return True


def get_last_blockchain_val():
    """ Returns last value of the current blockchain """
    latest_block = blockchain[-1]
    if not blockchain:
        print('Nothing in blockchain')
    else:
        print("Index: {}".format(latest_block.index))
        print("Time stamp: {}".format(latest_block.timestamp))
        print("Data: {}".format(latest_block.data))
        print("Previous Hash: {}".format(latest_block.previous_hash))
        print("Hash: {}".format(latest_block.hash_block()))


def print_blockchain():

    for block in blockchain:
        dicts = {
            'index': block.index,
            'Time stamp': block.timestamp,
            'Data': block.data,
            'Previous Hash': block.previous_hash,
            'Hash': block.hash_block()
        }

        print('Current value in blockchain after ' + str(block.index) + ' transactions')
        for key in dicts.keys():
            print(key, ': ', dicts[key])
            print('\t')


def main():
    while True:

        print('''Please choose: 
                 1: Add a new transaction
                 2: Mine a block to Blockchain
                 3: Show blockchain
                 4: Confirm Block
                 5: Show last value in blockchain
                 6: List participants
                 7: Quit''')
        global last_bloc
        user_choice = input_choice()

        if user_choice == '1':
            tx_data = get_transaction_val()
            recipient, sender, amount = tx_data
            add_transaction(recipient, sender=sender, amount=amount)
            print(open_transactions)
        elif user_choice == '2':
            if len(blockchain) < 1:
                blockchain.append(create_genesis_block())
                last_bloc = blockchain[0]
                clear_block()
                if True:
                    user_balance()
                    print(sender + ' Balance/Total amount sent per block is: ' + str(user_balance()))
            else:
                trx_amounts = next_block(last_bloc)
                add_value(trx_amounts)
                last_bloc = trx_amounts
                clear_block()

                if True:
                    user_balance()
                    print(sender + 'Balance/Total amount sent per block is: ' + str(user_balance()))

        elif user_choice == '3':
            if not blockchain:
                print('there is nothing in the blockchain')
            else:
                print_blockchain()
        elif user_choice == '4':
            if not confirm_block_in_blockchain():
                print('invalid')
                break
            else:
                print('valid block')
        elif user_choice == '5':
            get_last_blockchain_val()
        elif user_choice == '6':
            print("These are the participants of the blockchain : {} ".format(participants))
        elif user_choice == '7':
            break
        else:
            print('invalid choice, please a value from the list')
        if not confirm_block_in_blockchain():
            break


main()



