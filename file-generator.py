from datetime import datetime

def batch_record():
    """Returns the batch record, i.e. the first row for the payment file.
    
    Includes the following data: record code, entry date,
    hour of data, code of the sending bank group, reference payment 
    code of the invoicer, and currency code for EUR. Filled with 
    67 spaces, full length 90 digits.
    """
    # Create a timestamp with entry date yymmdd and hour of data hhmm
    creationtime = datetime.now().strftime('%Y%m%d%H%M')[2:]
    # Craft the record string
    record = '0' + creationtime + '99' + '123456789' + '1' + 67 * ' '
    return record

#additional checks
#print(batch_record())
#print('Lenght:', len(batch_record()))


def transaction_records():
    """Returns the transaction records, i.e. the rows with individual payments."""
    records = []
    account = input('Enter account number: ')
    if len(account) == 14 and account.isnumeric():
        while True:
            reference = input('Enter reference number: ')
            if len(reference) == 0:
                break
            elif len(reference) <= 20:
                reference = reference.zfill(20)
                amount = input(
                'Enter payment amount with comma and two decimals: ').replace(',','')
                if len(amount) <= 10:
                    amount = amount.zfill(10)
                    date = datetime.now().strftime('%Y%m%d')[2:]
                    record = ('3' # Record code
                                + account 
                                + 2 * date # Entry & payment date
                                + 16 * '1' # Filing code
                                + reference
                                + 'TESTPAYMENTS' # Payer name
                                + '1' # Currency code
                                + 'A' # Source of name
                                + amount
                                + '0  ' # Correction code + extra spaces
                                )
                    records.append(record)
                else:
                    print('Amount is too large.')
            else:
                print('Reference number is too long.')
    else:
        print('Account number is not correct.')
    return records

#additional checks
records = transaction_records()
for r in records:
    print(r)
    print(len(r))


def summary_record():
    """Returns the sum-up record with payment total number and amount."""
    pass