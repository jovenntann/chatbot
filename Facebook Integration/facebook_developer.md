https://developers.facebook.com/


Invividual Verification:
```
https://developers.facebook.com/settings/developer/indie-verification/
```

RASA: https://rasa.com/docs/rasa/user-guide/connectors/facebook-messenger/

APP Credentials:
```
App ID: 386347291950813
App Secret: 2bf02a7bebc94123708dbbc66bd479b4
Display Name: ServiceReferralHub
Contact Email: jovenntann@gmail.com
Privacy Policy URL: 
Terms of Service URL: 
```


> update credentials.yml
```python
facebook:
  verify: "rasa-bot" # Webhook Verification
  secret: "2bf02a7bebc94123708dbbc66bd479b4" # App Secret
  page-access-token:  "EAAFfYX0Yvt0BACRjOtnoj5QeqraZC6Xyop3eFr9evN2OBFyx0AtAylWtE0oYnnzL1Dq1M9ZAUMzuZAz2GVdqrh6EJickiTSAlBTbOofZCdPKIrL2lbNkS3Any6mOy4aR0JWY1ZCu4yZBaLtCieBlnjWmaT5hMjZAdbdDZAPwnurrUG66TqyK7lM9" # Generate FB Page access token
```

> Edit Page Subscriptions: 

Subscription Fields: *messages* and *messaging_postbacks* and messaging_referrals

> Format a Text

https://www.facebook.com/help/147348452522644?helpref=related
