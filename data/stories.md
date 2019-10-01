# Testing
* testing
  - utter_provider

# Referred
* referred{"referrer":"ABCD1234"}
  - slot{"referrer":"ABCD1234"}
  - action_name
  - slot{"first_name":"Jovenn"}
  - slot{"last_name":"Tan"}
  - utter_getstarted
  - utter_getstarted_options

# Get Started
* get_started
  - action_name
  - slot{"first_name":"Jovenn"}
  - slot{"last_name":"Tan"}
  - utter_getstarted
  - utter_getstarted_options

# Talk to Human
* talktohuman
  - utter_transfer_to_agent

# About Us
* aboutus
  - utter_aboutus
  
## Greet
* greet
  - action_name
  - slot{"first_name":"Jovenn"}
  - slot{"last_name":"Tan"}
  - utter_greet

## welcome
* thankyou
  - utter_welcome

## goodbye
* goodbye
  - utter_goodbye

<!--HOME: MAIN CATEGORY ========================================================================================================================================-->

<!--HOME: CLEANING SERVICES ====================================================-->
## Home - Cleaning Services - house_cleaning
* provider_lookup
    - utter_how_it_work
    - utter_ask_main_category
* provider_home{"main_category": "home"}
    - slot{"main_category": "home"}
    - utter_ask_home_services
* provider_cleaning_services{"service_category": "cleaning_services"}
    - slot{"service_category": "cleaning_services"}
    - utter_ask_cleaning_services
* inform_specialty{"specialty": "house_cleaning"}
    - slot{"specialty": "house_cleaning"}
    - utter_ask_location
* inform{"location": "Pasig"}
    - slot{"location": "pasig"}
    - utter_ask_number
* inform{"phone_number": "09062131607"}
    - slot{"phone_number": "09062131607"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

## Cleaning Services : cleaning_services
* provider_cleaning_services{"service_category": "cleaning_services"}
    - slot{"service_category": "cleaning_services"}
    - utter_ask_cleaning_services
* inform_specialty{"specialty": "house_cleaning"}
    - slot{"specialty": "house_cleaning"}
    - utter_ask_location
* inform{"location": "Pasig"}
    - slot{"location": "pasig"}
    - utter_ask_number
* inform{"phone_number": "09062131607"}
    - slot{"phone_number": "09062131607"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

## carpet_cleaning
* inform_specialty{"specialty": "carpet_cleaning"}
    - slot{"specialty": "carpet_cleaning"}
    - utter_ask_location
* inform{"location": "Pasig"}
    - slot{"location": "pasig"}
    - utter_ask_number
* inform{"phone_number": "09062131607"}
    - slot{"phone_number": "09062131607"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

<!--HOME: AIRCON SERVICES ====================================================-->
## Home - Aircon Services - aircon_cleaning
* provider_lookup
    - utter_how_it_work
    - utter_ask_main_category
* provider_home{"main_category": "home"}
    - slot{"main_category": "home"}
    - utter_ask_home_services
* provider_aircon_services{"service_category": "aircon_services"}
    - slot{"service_category": "aircon_services"}
    - utter_ask_aircon_services
* inform_specialty{"specialty": "aircon_cleaning"}
    - slot{"specialty": "aircon_cleaning"}
    - utter_ask_location
* inform{"location": "pasay"}
    - slot{"location": "pasay"}
    - utter_ask_number
* inform{"phone_number": "09997441234"}
    - slot{"phone_number": "09997441234"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

## Aircon Services - aircon_cleaning
* provider_aircon_services{"service_category": "aircon_services"}
    - slot{"service_category": "aircon_services"}
    - utter_ask_aircon_services
* inform_specialty{"specialty": "aircon_cleaning"}
    - slot{"specialty": "aircon_cleaning"}
    - utter_ask_location
* inform{"location": "pasay"}
    - slot{"location": "pasay"}
    - utter_ask_number
* inform{"phone_number": "09997441234"}
    - slot{"phone_number": "09997441234"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

## aircon_cleaning
* inform_specialty{"specialty": "aircon_cleaning"}
    - slot{"specialty": "aircon_cleaning"}
    - utter_ask_location
* inform{"location": "pasay"}
    - slot{"location": "pasay"}
    - utter_ask_number
* inform{"phone_number": "09997441234"}
    - slot{"phone_number": "09997441234"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

<!--HOME: ELECTRICAL SERVICES ====================================================-->
## Service Category - Home - Aircon Services - aircon_cleaning
* provider_lookup
    - utter_how_it_work
    - utter_ask_main_category
* provider_home{"main_category": "home"}
    - slot{"main_category": "home"}
    - utter_ask_home_services
* provider_aircon_services{"service_category": "aircon_services"}
    - slot{"service_category": "aircon_services"}
    - utter_ask_aircon_services
* inform_specialty{"specialty": "aircon_cleaning"}
    - slot{"specialty": "aircon_cleaning"}
    - utter_ask_location
* inform{"location": "marikina"}
    - slot{"location": "marikina"}
    - utter_ask_number
* inform{"phone_number": "09062131607"}
    - slot{"phone_number": "09062131607"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

## Electrical Services - lighting_installation_repair
* provider_electrical_services{"service_category": "electrical_services"}
    - slot{"service_category": "electrical_services"}
    - utter_ask_electrical_services
* inform_specialty{"specialty": "lighting_installation_repair"}
    - slot{"specialty": "lighting_installation_repair"}
    - utter_ask_location
* inform{"location": "pasay"}
    - slot{"location": "pasay"}
    - utter_ask_number
* inform{"phone_number": "09239108311"}
    - slot{"phone_number": "09239108311"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

## lighting_installation_repair
* inform_specialty{"specialty": "lighting_installation_repair"}
    - slot{"specialty": "lighting_installation_repair"}
    - utter_ask_location
* inform{"location": "pasay"}
    - slot{"location": "pasay"}
    - utter_ask_number
* inform{"phone_number": "09239108311"}
    - slot{"phone_number": "09239108311"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

<!--TECHONOLOGY: MAIN CATEGORY ========================================================================================================================================-->
## Technology - web_development
* provider_lookup
    - utter_how_it_work
    - utter_ask_main_category
* provider_technology{"main_category": "technology"}
    - slot{"main_category": "technology"}
    - utter_ask_technology_services
* inform_specialty{"specialty": "web_development"}
    - slot{"specialty": "web_development"}
    - utter_ask_location
* inform{"location": "marikina"}
    - slot{"location": "marikina"}
    - utter_ask_number
* inform{"phone_number": "09062131607"}
    - slot{"phone_number": "09062131607"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

## web_development
* inform_specialty{"specialty": "web_development"}
    - slot{"specialty": "web_development"}
    - utter_ask_location
* inform{"location": "marikina"}
    - slot{"location": "marikina"}
    - utter_ask_number
* inform{"phone_number": "09062131607"}
    - slot{"phone_number": "09062131607"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

## check balance to cashout
* check_balance
    - utter_balance
* cashout
    - utter_cashout_method

## cashout
* cashout
    - utter_cashout_method

## Become an Agent
* be_an_agent
    - utter_getstarted_agent

<!-- PROVIDER REGISTRATION ========================================================================================================================================-->
## Become a Provider
* be_a_provider
    - utter_getstarted_provider
    - utter_ask_main_category
* provider_home{"main_category": "home"}
    - slot{"main_category": "home"}
    - utter_ask_home_services
* provider_aircon_services{"service_category": "aircon_services"}
    - slot{"service_category": "aircon_services"}
    - utter_ask_email
* inform{"email":"jovenntann@gmail.com"}
    - slot{"email":"jovenntann@gmail.com"}
    - utter_ask_number
* inform{"phone_number": "09062131607"}
    - slot{"phone_number": "09062131607"}
    - utter_process_completed
* whatis_wallet
    - utter_whatis_provider_wallet

## Become a Provider - No Email
* be_a_provider
    - utter_getstarted_provider
    - utter_ask_main_category
* provider_technology{"main_category": "technology"}
    - slot{"main_category": "technology"}
    - utter_ask_technology_services
* inform_specialty{"specialty": "web_development"}
    - slot{"specialty": "web_development"}
    - utter_ask_email
* deny
    - utter_ask_number
* inform{"phone_number": "09106850351"}
    - slot{"phone_number": "09106850351"}
    - utter_process_completed
* whatis_wallet
    - utter_whatis_provider_wallet

<!-- 
## Provider Lookup 00
* inform{"specialty": "interior designer","location":"makati"}
    - slot{"specialty": "interior designer"}
    - slot{"location": "makati"}
    - utter_ask_number
* inform{"phone_number": "09062131607"}
    - slot{"phone_number": "09062131607"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

## interactive_story_02
* greet
  - action_name
  - slot{"first_name":"Jovenn"}
  - slot{"last_name":"Tan"}
  - utter_greet
* provider_lookup
    - utter_how_it_work
    - utter_ask_service_category
* inform{"specialty": "electrical services"}
    - slot{"specialty": "electrical services"}
    - utter_ask_location
* inform{"location": "quezon city"}
    - slot{"location": "quezon city"}
    - utter_ask_number
* inform{"phone_number": "09062131607"}
    - slot{"phone_number": "09062131607"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

## interactive_story_03
* greet
  - action_name
  - slot{"first_name":"Jovenn"}
  - slot{"last_name":"Tan"}
  - utter_greet
* inform{"location": "quezon city"}
    - slot{"location": "quezon city"}
    - utter_ask_service_category
* inform{"specialty": "electrical services"}
    - slot{"specialty": "electrical services"}
    - utter_ask_number
* inform{"phone_number": "09062131607"}
    - slot{"phone_number": "09062131607"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

## interactive_story_04
* greet
  - action_name
  - slot{"first_name":"Jovenn"}
  - slot{"last_name":"Tan"}
  - utter_greet
* inform{"location": "pasay"}
    - slot{"location": "pasay"}
    - utter_ask_service_category
* inform{"specialty": "interior designer"}
    - slot{"specialty": "interior designer"}
    - utter_ask_number
* inform{"phone_number": "09239108311"}
    - slot{"phone_number": "09239108311"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

## interactive_story_05
* greet
  - action_name
  - slot{"first_name":"Jovenn"}
  - slot{"last_name":"Tan"}
  - utter_greet
* inform{"location": "malabon"}
    - slot{"location": "malabon"}
    - utter_ask_service_category
* inform{"specialty": "web developer"}
    - slot{"specialty": "web developer"}
    - utter_ask_number
* inform{"phone_number": "09106850351"}
    - slot{"phone_number": "09106850351"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

## interactive_story_05
* greet
  - action_name
  - slot{"first_name":"Jovenn"}
  - slot{"last_name":"Tan"}
  - utter_greet
* inform{"location": "pasig"}
    - slot{"location": "pasig"}
    - utter_ask_service_category
* inform{"specialty": "interior designer"}
    - slot{"specialty": "interior designer"}
    - utter_ask_number
* inform{"phone_number": "09106850351"}
    - slot{"phone_number": "09106850351"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider -->
<!-- 
## service request
* inform{"specialty": "electrical services"}
    - slot{"specialty": "electrical services"}
    - utter_ask_location
* inform{"location": "quezon city"}
    - slot{"location": "quezon city"}
    - utter_ask_number
* inform{"phone_number": "09062131607"}
    - slot{"phone_number": "09062131607"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider -->
<!-- 
## service request - no remarks
* inform{"specialty": "electrical services"}
    - slot{"specialty": "electrical services"}
    - utter_ask_location
* inform{"location": "quezon city"}
    - slot{"location": "quezon city"}
    - utter_ask_number
* inform{"phone_number": "09062131607"}
    - slot{"phone_number": "09062131607"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* deny
    - action_search_provider

## service request - insert specialty
* inform{"specialty": "electrical services"}
    - slot{"specialty": "electrical services"}
    - utter_ask_location
* inform{"location": "quezon city"}
    - slot{"location": "quezon city"}
    - utter_ask_number
* inform{"phone_number": "09062131607"}
    - slot{"phone_number": "09062131607"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* deny
    - action_search_provider
* inform{"specialty": "electrical services"}
    - slot{"specialty": "electrical services"}
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider

## service request
* inform{"specialty": "electrical services"}
    - slot{"specialty": "electrical services"}
    - utter_ask_location
* inform{"location": "quezon city"}
    - slot{"location": "quezon city"}
    - utter_ask_number
* inform{"phone_number": "09062131607"}
    - slot{"phone_number": "09062131607"}
    - utter_ask_when
* dates
    - utter_ask_remarks
* provider_lookup_remarks
    - action_search_provider
* inform{"specialty": "interior designer"}
    - slot{"specialty": "interior designer"}
    - action_search_provider
* affirm
    - utter_please_wait
    - utter_provider -->
