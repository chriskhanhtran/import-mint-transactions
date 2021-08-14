# Run## Overview
Simulates bulk manual transaction adds to mint.com. Mint manual transactions are submitted as "cash transactions" which
will mean it shows in your cash / all accounts transaction list. You cannot submit manual transactions against credit
cards or other integrated bank accounts (even in Mint's UI this is not possible and ends up as cash transction).
## Instructions
1. Prepare your data to import using import.csv as an example
2. Edit import.py and replace the variables set to XXXXX's to values in your browser during a live Mint session
  - account is mtaccount and approximately 8 digits
  - tag1 is in form of tagXXXXXXX
  - tag2 is in form of tagXXXXXXX
  - tag3 is in form of tagXXXXXXX
  - cookie will be an apprimately 2000 character string
  - referrer is likely always 'https://mint.intuit.com/transaction.event'
  - token is approximately 50 characters
3. If you have custom categories, they need to go along others in function category_id_switch()

## Reference
https://nathanielkam.com/import-transactions-to-mint-using-python/