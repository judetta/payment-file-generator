# Payment file generator

Tool to easily create incoming reference payment files.

### Background

Working in application management for ledger and invoicing services one very often needs to create incoming reference payment files for application testing purposes. The idea of this tool is to reduce manual work when creating those files, and make the creation of files easier and quicker.

### Specs

The specification for the file is described in details in 
[Incoming reference payments | Service Description/version 2.1](https://www.finanssiala.fi/wp-content/uploads/2021/03/Incoming_reference_payments_v2_1.pdf).

On the pages of [Finance Finland (FFI)](https://www.finanssiala.fi/en/topics/digital-services-and-payments/payment-services-in-finland/#/) you can find lot of other information about payment systems in Finland along with all the technical descriptions.

### How to use this tool?

You'll need the receiving account number and the reference number(s) and amount(s) for payment(s) you want to include in the file.

Currently the Python script works; run the script, enter as many payment references and amounts you want, and when you do not want to add more, just hit enter. The file will be created into a folder _paymentfiles_ under whereever you are running the script.

Web UI with html and javascript will (maybe) follow later.