from datetime import datetime

def batch_record():
    """Returns the batch record a.k.a. the first row for the payment file.
    
    Includes the following data: record code, entry date,
    hour of data, code of the sending bank group, reference payment 
    code of the invoicer, and currency code for EUR. Filled with 
    67 spaces, full length 90 digits.
    """
    # Create a timestamp with entry date yymmdd and hour of data hhmm
    creationtime = datetime.now().strftime('%Y%m%d%H%M')[2:]
    record = '0' + creationtime + '99' + '123456789' + '1' + 67 * ' '
    return record

print(batch_record())
print('Lenght:', len(batch_record()))

