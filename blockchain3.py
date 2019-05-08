from blockchain1 import Block
from blockchain2 import User
from testing2 import blockchain, open_transactions, miner_reward, participants
from input_file import input_choice
import datetime as date


user = User(balance=None)


def clear_block():
    open_transactions.clear()


def add_value(trx_amounts):
    blockchain.append(trx_amounts)


def mine_block(recipient=user.user_name, amount=miner_reward):
    data = []
    reward_trx = {
        'sender': 'MINING',
        'recipient': recipient,
        'amount': amount
    }

    for transaction in open_transactions:
        data.append(transaction)
    data.append(reward_trx)
    return data


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
    global lag1
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


def participants_balance():
    for x in participants:
        print('balance of {} is: {}'.format(x, user.get_balance(x)))


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
            tx_data = user.get_transaction_val()
            recipient, sender, amount = tx_data
            if user.add_transaction(recipient, sender=user.user_name, amount=amount):
                print('Added trx')
            else:
                print('Trx failed')
            print(open_transactions)
        elif user_choice == '2':
            if len(blockchain) < 1:
                blockchain.append(create_genesis_block())
                last_bloc = blockchain[0]
                clear_block()
                if True:
                    user.get_balance(user.user_name)
                    print('Balance of {} is: {:5.2f}'.format(user.user_name, user.get_balance(user.user_name)))
            else:
                trx_amounts = next_block(last_bloc)
                add_value(trx_amounts)
                last_bloc = trx_amounts
                clear_block()

                if True:
                    user.get_balance(user.user_name)
                    print('Balance of {} is: {:5.2f}'.format(user.user_name, user.get_balance(user.user_name)))

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
            participants_balance()
        elif user_choice == '7':
            break
        else:
            print('invalid choice, please a value from the list')


#       if not confirm_block_in_blockchain():
#           break


main()