from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker 
from rasa_sdk.executor import CollectingDispatcher

# SET SLOTS =========================================================================================
from rasa_sdk.events import SlotSet

# API REQUESTS ======================================================================================
import requests
import json

# MINI DATABASE ======================================================================================
images = {
  "electrical services": "https://www.kingstonelectrician.ca/wp-content/uploads/2018/06/electrician-2.jpg",
  "cleaning serivces": "https://cdn.shortpixel.ai/client/q_glossy,ret_img/https://nancyshousekeepingservice.com/wp-content/uploads/2019/04/Goleta-House-Cleaning.png",
  "web developer": "https://careerfoundry.com/en/blog/uploads/web_dev_pillar_page.jpg",
  "aircon services": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAtheT1xgis2pPWB5nYJLbMgOjZ-zLNredzu5E2BLAJINg-KajMQ",
  "interior designer": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJLoAIGlFI5rqf50-DH0qA6cV9uVYwAXjxef4T-W9ixXOu1QWM",
  "moving services":"https://www.rd.com/wp-content/uploads/2016/09/01-guarantee-lies-moving-companies-tell-AndreyPopov.jpg"
}

class MyFallbackAction(Action):

    def name(self) -> Text:
        return "my_fallback_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,   
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = {
            "text": "I'm Sorry, Can you rephrase that?",
            "quick_replies":[
            {
                "content_type":"text",
                "title":"About Us",
                "payload":"About Us",
            },
            {
                "content_type":"text",
                "title":"Talk to Human",
                "payload":"Talk to Human",
            }]
        }

        dispatcher.utter_custom_json(message)

        return []

class ActionName(Action):
	def name(self):
		return 'action_name'
		
	def run(self, dispatcher, tracker, domain):
		import requests
		most_recent_state = tracker.current_state()
		sender_id = most_recent_state['sender_id']
		
		r = requests.get('https://graph.facebook.com/{}?fields=first_name,last_name,profile_pic&access_token={}'.format(sender_id, "EAAFfYX0Yvt0BAJrZAFFkEaUYZCADKGjhZAZCgH2NZBW79ZAYFIuw6EWvhOluYeCjWsYRc921qumO9ZBNNe49ZB32MCOm6sCzTWU3qZBRHDY36mCRNKZBpPXBsFsJAkyx1p2jZALP63ZBMLYwloT3gRsrgRFrQeogZCiOygzfTRA5ZAlUqP1TEu4FRQ9iIiTjSAOMU0cScZD")).json()
		first_name = r['first_name']
		last_name = r['last_name']
		
		return [SlotSet('first_name', first_name), SlotSet('last_name', last_name)]
        
class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = {
            "text": "Hi there! I'm Service Referral Hub - AI Assistant, How can I help you?",
            "quick_replies":[
            {
                "content_type":"text",
                "title":"Book a Service",
                "payload":"Book a Service",
            },{
                "content_type":"text",
                "title":"Be an Agent",
                "payload":"Be an Agent",
            },{
                "content_type":"text",
                "title":"Be a Provider",
                "payload":"Be a Provider",
            }
            ]
        }

        dispatcher.utter_custom_json(message)
        return []

class ActionSearchProvider(Action):
    def name(self) -> Text:
        return "action_search_provider"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # ---------------------------------------------------------------
        # GET SLOTS FROM TRACKER
        # ---------------------------------------------------------------
        # main_category = tracker.get_slot('main_category')
        specialty = tracker.get_slot('specialty')
        service_category = tracker.get_slot('service_category')
        location = tracker.get_slot('location')
        time = tracker.get_slot('time')
        phone_number = tracker.get_slot('phone_number')

        # ---------------------------------------------------------------
        # API REQUEST
        # ---------------------------------------------------------------
        # url = f"https://api.betterdoctor.com/2016-03-01/doctors?specialty_uid=dentist&location=37.773%2C-122.413%2C100&user_location=37.773%2C-122.413&skip=0&limit=10&user_key=3c4164ab5182e76b1e8b2055f496257c"
        # response_json = requests.request("GET", url)
        # response_json = response_json.json()
        # provider_name = response_json['data'][0]['profile']['bio']

        # ---------------------------------------------------------------
        # UTTER MESSAGE
        # ---------------------------------------------------------------
        # dispatcher.utter_message(f"Here is What I Found, {provider_name}")

        # IF TIME IS EMPTY UTTER_ASK_WHEN

        if specialty:
            image = images.get(specialty.lower(), 'https://www.sonypictures.com/sites/default/files/styles/max_560x840/public/chameleon/title-movie/DP_4169338_TC_1400x2100_DP_4169339_SEARCHING_2000x3000_EST_1.jpg') 

            message = {
                "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"generic",
                    "elements":[{
                        "title":specialty,
                        "image_url":image,
                        "subtitle":"Category: Home",
                        "default_action": {
                        "type": "web_url",
                        "url": "https://www.servicereferralhub.com/",
                        "webview_height_ratio": "tall",
                        },
                        "buttons":[
                        {
                            "type":"postback",
                            "title":"Confirm",
                            "payload":"Confirm"
                            # "type":"web_url",
                            # "url":"https://www.servicereferralhub.com/",
                            # "title":"Confirm"
                        }]      
                    }]
                }
                }
            }

            dispatcher.utter_message(f"Note: You will earn a Rebate for every successful booking from this platform and it will automatically added in your Service Referral Hub - Wallet. ")
            dispatcher.utter_message(f'You have requested for {specialty} in {location} at {time} and your contact number is {phone_number}. Please Tap on "Confirm" to confirm you request.')
    
        else:
            message = {"text": "Sorry I didn't get the Provider you want. What type of Service do you need? (Aircon Installaton, House Cleaning, Electrical Repair, etc.)"}

        dispatcher.utter_custom_json(message)
        return []












# ------------------------------------------------------------------------------------------------
# DUCKLING EXTRACT
# ------------------------------------------------------------------------------------------------
# class ActionStoreEntityExtractor(Action):

#     def name(self):
#         return "action_store_entity_extractor"

#     def run(self, dispatcher, tracker, domain):

#         print("action_store_entity_extractor")

#         time = tracker.get_slot('time')
#         print(f"I've got {time}")

#         extracted_time = next(tracker.get_latest_entity_values("entity_name"), None) 
#         extracted_time = tracker.latest_message['entities'][0]['value']
#         extracted_time = tracker.latest_message['entities']

#         print(f"Time entity is {extracted_time}")
        
#         return [SlotSet('grain','rice')]

# ------------------------------------------------------------------------------------------------
# IMAGE REPLY 
# ------------------------------------------------------------------------------------------------
# img = "https://image.shutterstock.com/image-vector/welcome-letters-banner-on-blue-260nw-1189574716.jpg"
# message = {
#     "attachment": {
#         "type": "image",
#         "payload": {
#             "url": img,
#             "is_reusable": False
#         }
#     }
# }

# ------------------------------------------------------------------------------------------------
# BUTTON WITH LINK
# ------------------------------------------------------------------------------------------------
# message = {
#     "attachment":{
#     "type":"template",
#     "payload":{
#         "template_type":"button",
#         "text":"What do you want to do next?",
#         "buttons":[
#             {
#                 "type":"web_url",
#                 "url":"https://www.messenger.com",
#                 "title":"Visit Messenger"
#             },
#             {
#                 "type":"web_url",
#                 "url":"https://www.messenger.com",
#                 "title":"Visit Website"
#             }
#         ]
#     }
#     }
# }

# ------------------------------------------------------------------------------------------------
# QUICK REPLY 
# ------------------------------------------------------------------------------------------------
# message = {
#     "text": "Please select your next action",
#     "quick_replies":[
#     {
#         "content_type":"text",
#         "title":"Book",
#         "payload":"Book",
#     },{
#         "content_type":"text",
#         "title":"Next",
#         "payload":"Next",
#     }
#     ]
# }

# ------------------------------------------------------------------------------------------------
# RECEIPT TEMPLATE
# ------------------------------------------------------------------------------------------------
# message = {
#     "attachment":{
#     "type":"template",
#     "payload":{
#         "template_type":"receipt",
#         "recipient_name":"Stephane Crozatier",
#         "order_number":"12345678902",
#         "currency":"PHP",
#         "payment_method":"Visa 2345",        
#         "order_url":"http://petersapparel.parseapp.com/order?order_id=123456",
#         "timestamp":"1428444852",         
#         "address":{
#         "street_1":"Marikina City",
#         "city":"Marikina City",
#         "postal_code":"94025",
#         "state":"CA",
#         "country":"US"
#         },
#         "summary":{
#         "subtotal":75.00,
#         "shipping_cost":4.95,
#         "total_tax":6.19,
#         "total_cost":56.14
#         },
#         "adjustments":[
#         {
#             "name":"New Customer Discount",
#             "amount":20
#         },
#         {
#             "name":"$10 Off Coupon",
#             "amount":10
#         }
#         ],
#         "elements":[
#         {
#             "title":"Interior Designer",
#             "subtitle":"Category: Home Renovation Services",
#             "quantity":1,
#             "price":5000,
#             "currency":"PHP",
#             "image_url":"http://www.hamstech.com/blog/wp-content/uploads/2017/03/interior-designing-600x410.jpg"
#         },
#         {
#             "title":"Classic Gray T-Shirt",
#             "subtitle":"100% Soft and Luxurious Cotton",
#             "quantity":1,
#             "price":25,
#             "currency":"USD",
#             "image_url":"http://petersapparel.parseapp.com/img/grayshirt.png"
#         }
#         ]
#     }
#     }
# }

# ------------------------------------------------------------------------------------------------
# BASIC
# ------------------------------------------------------------------------------------------------
# class ActionAskSpecialty(Action):

#     def name(self) -> Text:
#         return "action_ask_specialty"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         message = {
#             "text": "What Service do you need?",
#             "quick_replies":[
#             {
#                 "content_type":"text",
#                 "title":"Electrical Services",
#                 "payload":"Electrical Services",
#             },{
#                 "content_type":"text",
#                 "title":"Interior Designer",
#                 "payload":"Interior Designer",
#             },{
#                 "content_type":"text",
#                 "title":"Web Developer",
#                 "payload":"Web Developer",
#             }
#             ]
#         }

#         dispatcher.utter_custom_json(message)
#         return []