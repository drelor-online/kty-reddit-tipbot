from datetime import datetime
from web3 import Web3
import json
import config

bsc = https://bsc-dataseed.binance.org/
web3 = Web3(Web3.HTTPProvider(bsc))

tipbot_address= 0xC54F3F8Cb42dCe075ff40800Cb00F555df993ab1
contract_address = 0x86296279C147bd40cBe5b353F83cea9e9cC9b7bB 

abi = json.loads('[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint256","name":"_decimals","type":"uint256"},{"internalType":"uint256","name":"_supply","type":"uint256"},{"internalType":"uint256","name":"_txFee","type":"uint256"},{"internalType":"uint256","name":"_burnFee","type":"uint256"},{"internalType":"uint256","name":"_charityFee","type":"uint256"},{"internalType":"address","name":"_FeeAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"FeeAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_BURN_FEE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_CHARITY_FEE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_TAX_FEE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tAmount","type":"uint256"}],"name":"deliver","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"excludeAccount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"includeAccount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isExcluded","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tAmount","type":"uint256"},{"internalType":"bool","name":"deductTransferFee","type":"bool"}],"name":"reflectionFromToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"setAsCharityAccount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rAmount","type":"uint256"}],"name":"tokenFromReflection","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalBurn","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalCharity","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalFees","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_txFee","type":"uint256"},{"internalType":"uint256","name":"_burnFee","type":"uint256"},{"internalType":"uint256","name":"_charityFee","type":"uint256"}],"name":"updateFee","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

contract = web3.eth.contract(address=contract_address, abi=abi)


#me = '0x5977987.....'  #send from this address
#main_address= "0x9F....."   #to this address

#send = 1000
#amount = web3.toWei(send, 'ether')
#print(amount)

#nonce = web3.eth.getTransactionCount(me)
#print(nonce)

#token_tx = contract.functions.transfer(main_address, amount).buildTransaction({
#    'chainId':56, 'gas': 100000,'gasPrice': web3.toWei('10','gwei'), 'nonce':nonce
#})
#sign_txn = web3.eth.account.signTransaction(token_tx, private_key=YOURPRIVATEKEY)
#web3.eth.sendRawTransaction(sign_txn.rawTransaction)
#print(f"Transaction has been sent to {main_address}")


# Check if an account is open.
#def is_account_open(account):
#    try:
#        accounts = server.accounts().account_id(account).call()
#        return True
#    except SdkError:
#        pass
#    return False

# Get balances of BNB and assets in the main account.
def get_balances(account):
    balances = web3.eth.get_balance(account)
    return balances


# Check if a transaction is successful.
#def is_transaction_successful(transaction_hash):
#    try:
#        payments = server.payments().for_transaction(transaction_hash).call()        
#        transaction_successful = True
#        for payment in payments["_embedded"]["records"]:
#            transaction_successful &= payment["transaction_successful"]
#        return transaction_successful
#    except SdkError:
#        LOGGER.exception("Cannot get transaction state for %s" % transaction_hash)
#    return False


# Get transaction amount.
#def get_transaction_payments(transaction_hash):
#    payments = []
#    try:
#        payments_call_result = server.payments().for_transaction(transaction_hash).call()        
        # Assume only one payment per transaction.
#        for payment in payments_call_result["_embedded"]["records"]:
#            if "asset_code" in payment:
#                asset = payment["asset_code"].lower()
#            else:
#                asset = "xlm"
#            if not "amount" in payment:
#                continue
#            payments.append({"from": payment["from"], "to": payment["to"], "asset": asset, "amount": to_stroop(str(payment["amount"]))})
#    except SdkError:
#        LOGGER.exception("Cannot get transaction state for %s" % transaction_hash)
#    return payments


# Get the most recent incoming transactions.
#def get_incoming_transactions():
#    transactions = []
#    try:
#        transactions_call_result = server.transactions().for_account(account_id=ACCOUNT).include_failed(False).order(desc=True).limit(200).call()
#        for transaction in transactions_call_result["_embedded"]["records"]:
#            if transaction["source_account"] == ACCOUNT: 
#                continue
#            date = datetime.strptime(transaction["created_at"][:19], "%Y-%m-%dT%H:%M:%S")
#            transactions.append({"hash" : transaction["hash"], "date" : date, "source_account": transaction["source_account"], "memo": transaction.get('memo', None)})
#    except SdkError:
#        LOGGER.exception("Cannot get incoming transactions")
#    return transactions


#def get_sequence_number():
#    try:
#        account = server.accounts().account_id(ACCOUNT).call()
#        return int(account['sequence'])       
#    except SdkError:
#        LOGGER.exception("Cannot get sequence number")


#def send_payment(destination_account, amount, memo, fee):
# Send a payment to an account.
#    try:
#        source_keypair = Keypair.from_secret(SECRET)
#        source_account = server.load_account(source_keypair.public_key)
#        #root_account = Account(account_id = source_keypair.public_key, sequence=1)
#        transaction = (
#            TransactionBuilder(
#                source_account = source_account,
#                network_passphrase = Network.PUBLIC_NETWORK_PASSPHRASE,
#                base_fee = fee,
#            )
#            .add_text_memo(memo)
#            .append_payment_op(
#                destination = destination_account,
#                amount = str(from_stroop(amount)),
#                #asset_code = CURRENCY,
#                #asset_issuer = CURRENCY_ISSUER
#                asset = Asset(CURRENCY, CURRENCY_ISSUER)
#            )
#            .set_timeout(20)
#            .build()
#        )
#        transaction.sign(source_keypair)
#        response = server.submit_transaction(transaction)
#        return response["successful"]
#    except SdkError:
#        LOGGER.exception("Cannot send transaction")
#    return False    
