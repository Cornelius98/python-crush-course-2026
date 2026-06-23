bank_accounts = [
    "111",
    "222",
    "333", #premium account - no promo SMSs
    "444",
    "555"
]

for account in bank_accounts:
    if account == "333":
        print("Premium account skipped - ", account)  #Exempt premium account
        continue
    else:
        print("Promo SMSs sent to account:", account)
