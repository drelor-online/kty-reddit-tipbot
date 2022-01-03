from datetime import datetime
from web3 import Web3
import json
import config

from shared import (
    CURRENCY,
    CONTRACT;
    ACCOUNT,
    PRIVATEKEY,
    LOGGER,
)

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))

main_address= ACCOUNT
contract_address = CONTRACT #be sure to use a BSC Address in uppercase format like this 0x9F0818B... 

abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeSub","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeDiv","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeMul","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeAdd","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Approval","type":"event"}]')

contract = web3.eth.contract(address=contract_address, abi=abi)


me = '0x5977987.....'  #send from this address
main_address= "0x9F....."   #to this address

send = 1000
amount = web3.toWei(send, 'ether')
print(amount)

nonce = web3.eth.getTransactionCount(me)
print(nonce)

token_tx = contract.functions.transfer(main_address, amount).buildTransaction({
    'chainId':56, 'gas': 100000,'gasPrice': web3.toWei('10','gwei'), 'nonce':nonce
})
sign_txn = web3.eth.account.signTransaction(token_tx, private_key=YOURPRIVATEKEY)
web3.eth.sendRawTransaction(sign_txn.rawTransaction)
print(f"Transaction has been sent to {main_address}")
server = Server(horizon_url=DEFAULT_URL)

# Get a workable fee to prevent a transaction from getting stuck.
def get_fee():
    try:
        fee_stats = server.fee_stats().call()
        base_fee = int(fee_stats["last_ledger_base_fee"])
        ledger_capacity_usage = float(str(fee_stats["ledger_capacity_usage"]))
        higher_fee = int(fee_stats["fee_charged"]["p70"])        
        if (ledger_capacity_usage >= 0.9): # Ledger almost fully used
            return higher_fee 
        else:
            return base_fee
    except SdkError:
        return DEFAULT_FEE 

# Check if an account is open.
def is_account_open(account):
    try:
        accounts = server.accounts().account_id(account).call()
        return True
    except SdkError:
        pass
    return False

# Check if an account is open.
def account_has_trustline(account, asset_name, asset_issuer):    
    try:
        asset = Asset(asset_name, asset_issuer)
        accounts = server.accounts().account_id(account).for_asset(asset).call()
        return True
    except SdkError:
        pass
    return False

# Get balances of XLM and assets in the main account.
def get_balances(account):
    balances = {}
    try:
        accounts = server.accounts().account_id(account).call()
        for balance in accounts["balances"]:
            if balance["asset_type"] == "native":
                balances["xlm"] = to_stroop(balance["balance"])    
            else:
                balances[balance["asset_code"].lower()] = to_stroop(balance["balance"])
    except SdkError:
        LOGGER.exception("Cannot get balances")
    return balances


# Check if a transaction is successful.
def is_transaction_successful(transaction_hash):
    try:
        payments = server.payments().for_transaction(transaction_hash).call()        
        transaction_successful = True
        for payment in payments["_embedded"]["records"]:
            transaction_successful &= payment["transaction_successful"]
        return transaction_successful
    except SdkError:
        LOGGER.exception("Cannot get transaction state for %s" % transaction_hash)
    return False


# Get transaction amount.
def get_transaction_payments(transaction_hash):
    payments = []
    try:
        payments_call_result = server.payments().for_transaction(transaction_hash).call()        
        # Assume only one payment per transaction.
        for payment in payments_call_result["_embedded"]["records"]:
            if "asset_code" in payment:
                asset = payment["asset_code"].lower()
            else:
                asset = "xlm"
            if not "amount" in payment:
                continue
            payments.append({"from": payment["from"], "to": payment["to"], "asset": asset, "amount": to_stroop(str(payment["amount"]))})
    except SdkError:
        LOGGER.exception("Cannot get transaction state for %s" % transaction_hash)
    return payments


# Get the most recent incoming transactions.
def get_incoming_transactions():
    transactions = []
    try:
        transactions_call_result = server.transactions().for_account(account_id=ACCOUNT).include_failed(False).order(desc=True).limit(200).call()
        for transaction in transactions_call_result["_embedded"]["records"]:
            if transaction["source_account"] == ACCOUNT: 
                continue
            date = datetime.strptime(transaction["created_at"][:19], "%Y-%m-%dT%H:%M:%S")
            transactions.append({"hash" : transaction["hash"], "date" : date, "source_account": transaction["source_account"], "memo": transaction.get('memo', None)})
    except SdkError:
        LOGGER.exception("Cannot get incoming transactions")
    return transactions


def get_sequence_number():
    try:
        account = server.accounts().account_id(ACCOUNT).call()
        return int(account['sequence'])       
    except SdkError:
        LOGGER.exception("Cannot get sequence number")


def send_payment(destination_account, amount, memo, fee):
# Send a payment to an account.
    try:
        source_keypair = Keypair.from_secret(SECRET)
        source_account = server.load_account(source_keypair.public_key)
        #root_account = Account(account_id = source_keypair.public_key, sequence=1)
        transaction = (
            TransactionBuilder(
                source_account = source_account,
                network_passphrase = Network.PUBLIC_NETWORK_PASSPHRASE,
                base_fee = fee,
            )
            .add_text_memo(memo)
            .append_payment_op(
                destination = destination_account,
                amount = str(from_stroop(amount)),
                #asset_code = CURRENCY,
                #asset_issuer = CURRENCY_ISSUER
                asset = Asset(CURRENCY, CURRENCY_ISSUER)
            )
            .set_timeout(20)
            .build()
        )
        transaction.sign(source_keypair)
        response = server.submit_transaction(transaction)
        return response["successful"]
    except SdkError:
        LOGGER.exception("Cannot send transaction")
    return False    
