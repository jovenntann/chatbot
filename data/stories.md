# Referred
* referred{"referrer":"ABCD1234"}
  - slot{"referrer":"ABCD1234"}
  - action_name
  - slot{"first_name":"Jovenn"}
  - slot{"last_name":"Tan"}
  - utter_getstarted

# Get Started
* get_started
  - action_name
  - slot{"first_name":"Jovenn"}
  - slot{"last_name":"Tan"}
  - utter_getstarted

# Talk to Human
* talktohuman
  - action_typing
  - utter_transfer_to_agent

## Greet
* greet
  - action_name
  - slot{"first_name":"Jovenn"}
  - slot{"last_name":"Tan"}
  - action_typing
  - utter_greet

## welcome
* thankyou
  - action_typing
  - utter_welcome

## goodbye
* goodbye
  - action_typing
  - utter_goodbye

## Home Category
* provider_lookup
    - action_ask_home_services

<!-- This should be the flow once I added other services
## Home Category
* provider_lookup
    - utter_ask_main_category
* provider_home{"main_category": "home"}
    - slot{"main_category": "home"}
    - action_ask_home_services -->

