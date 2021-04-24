from datetime import datetime

def create_batch_record():
    """Returns the batch record, i.e. the first row for the payment file."""
    creationtime = datetime.now().strftime('%Y%m%d%H%M')[2:]
    record = ('0'  # Record code
                + creationtime  # Entry date & hour of data
                + '99'  # Code of the sending bank group
                + '123456789'  # Reference payment code of the invoicer
                + '1'  # Currecy code
                + 67 * ' '  # Filling spaces
                )
    return record


def create_transaction_records():
    """Returns the transaction records, i.e. the rows with individual payments."""
    records = []
    while True:
        account = input('Enter account number: ')
        if len(account) != 14 or not account.isnumeric():
            print('Account number is not correct.')
            continue
        break
    while True:
        reference = input('Enter reference number: ')
        if len(reference) == 0:  # Stop adding records
            break
        elif len(reference) > 20:
            print('Reference number is too long.')
            continue
        reference = reference.zfill(20)
        amount = input(
        'Enter payment amount with comma and two decimals: ').replace(',','')
        if len(amount) > 10:
            print('Amount is too large.')
            continue
        amount = amount.zfill(10)
        date = datetime.now().strftime('%Y%m%d')[2:]
        record = ('3'  # Record code
                    + account  # Invoicer’s account number
                    + 2 * date  # Entry & payment date
                    + 16 * '1'  # Filing code
                    + reference  # Reference number
                    + 'TESTPAYMENTS'  # Payer name
                    + '1'  # Currency code
                    + 'A'  # Source of name
                    + amount
                    + '0  '  # Correction code + extra spaces
                    )
        records.append(record)
    return records


def create_summary_record(transaction_records):
    """Returns the sum-up record with payment total number and amount."""
    number_of_transactions = str(len(transactions)).zfill(6)
    sum_of_payments = 0
    for t in transactions:
        amount = int(t[77:87])
        sum_of_payments += amount
    sum_of_payments = str(sum_of_payments).zfill(11)
    record = ('9'  # Record code
                + number_of_transactions  # Number of reference trans.
                + sum_of_payments  # Amount of reference trans.
                + 72 * '0'
                )
    return record


batch = create_batch_record()
transactions = create_transaction_records()
summary = create_summary_record(transactions)

filename = 'payments_' + datetime.now().strftime('%Y%m%d%H%M%S')[2:] + '.txt'
with open(filename, 'x') as f:
    print(batch, file=f)
    for t in transactions:
        print(t, file=f)
    print(summary, file=f)
