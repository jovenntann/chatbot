from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker 
from rasa_sdk.executor import CollectingDispatcher

# SET SLOTS =========================================================================================
from rasa_sdk.events import SlotSet

# API REQUESTS ======================================================================================
import requests
import json
import requests
import time

# MINI DATABASE ======================================================================================
images = {
  "thorough_cleaning":"https://images.summitmedia-digital.com/spotph/images/2017/07/31/CleaningServices_10.jpg",
  "house_cleaning":"https://images.summitmedia-digital.com/spotph/images/2017/07/31/CleaningServices_10.jpg",
  "carpet_cleaning":"https://images.summitmedia-digital.com/spotph/images/2017/07/31/CleaningServices_10.jpg",
  "upholstery_cleaning":"https://images.summitmedia-digital.com/spotph/images/2017/07/31/CleaningServices_10.jpg",

  "aircon_cleaning":"https://www.81aircon.com/wp-content/uploads/2016/11/repair.jpg",
  "aircon_repair":"https://www.81aircon.com/wp-content/uploads/2016/11/repair.jpg",
  "aircon_installation":"https://www.81aircon.com/wp-content/uploads/2016/11/repair.jpg",

  "lighting_installation_repair":"http://midtowncitygreens.org/wp-content/uploads/2019/06/cropped-midtowncitygreens-header.jpg",
  "breaker_installation_repair":"http://midtowncitygreens.org/wp-content/uploads/2019/06/cropped-midtowncitygreens-header.jpg",
  "water_heater_installation_repair":"http://midtowncitygreens.org/wp-content/uploads/2019/06/cropped-midtowncitygreens-header.jpg",

  "laundry_services":"https://media3.s-nbcnews.com/i/newscms/2016_32/1149295/laundry-stock-today-160808-tease_8816217b49c15bf3fc07bbcd6558c2db.jpg",
  "plumbing_services":"http://www.phdmechanicalnj.com/wp-content/uploads/2016/05/phd-mechanical-Kitchen-Plumbing-Services.jpg",
  "home_renovation":"https://img-aws.ehowcdn.com/600x600p/s3-us-west-1.amazonaws.com/contentlab.studiod/getty/94dbf74690e34394bd9da6624ba75e3a.jpg",
  
  "web_development": "https://careerfoundry.com/en/blog/uploads/web_dev_pillar_page.jpg",
  "mobile_development":"https://miro.medium.com/max/2560/1*Ec7MJdsUiuVUMkeTw_6y_g.jpeg",
  "marketing_services":"https://www.evolvedigitas.com/blog/wp-content/uploads/2018/05/digital-marketing.jpg",
  "graphic_design":"https://www.shillingtoneducation.com/content-blog/uploads/2019/01/IMG_4022-copy.jpg",
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
		
		r = requests.get('https://graph.facebook.com/{}?fields=first_name,last_name,profile_pic&access_token={}'.format(sender_id, "EAAFfYX0Yvt0BAEL6S4RQu8ZA5UJLRQ9bshQVLT6tFfaBQMuuwnddrimBR4VQ4I9HzsFjJA8B1ugzPr6ut4MK5X8CsNgqTqbwj3ZAVXP0B7JjLlSuqpNjMAfT7Dsn34VVtvLe3GcU62esDjSeErTybmY7Kx3n7uvUTZCJ7TZBMZAZAgLOgukkvVZBQA7IKzY2L8ZD")).json()
		first_name = r['first_name']
		last_name = r['last_name']
		
		return [SlotSet('first_name', first_name), SlotSet('last_name', last_name)]

class ActionTyping(Action):
    def name(self):
        return 'action_typing'

    def run(self, dispatcher, tracker, domain):

        most_recent_state = tracker.current_state()
        sender_id = most_recent_state['sender_id']

        headers = {'Content-Type': 'application/json',}
        data = """
            {
                "recipient":{
                "id":" """ + sender_id + """ ",
                },
                "sender_action":"typing_on"
            }
        """
        requests.post('https://graph.facebook.com/v4.0/me/messages?access_token=EAAFfYX0Yvt0BAEL6S4RQu8ZA5UJLRQ9bshQVLT6tFfaBQMuuwnddrimBR4VQ4I9HzsFjJA8B1ugzPr6ut4MK5X8CsNgqTqbwj3ZAVXP0B7JjLlSuqpNjMAfT7Dsn34VVtvLe3GcU62esDjSeErTybmY7Kx3n7uvUTZCJ7TZBMZAZAgLOgukkvVZBQA7IKzY2L8ZD', headers=headers, data=data)
        
        time.sleep(1)

        return None
        
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
        first_name = tracker.get_slot('first_name')
        location = tracker.get_slot('location')
        time = tracker.get_slot('time')
        phone_number = tracker.get_slot('phone_number')

        # NOTE: IF TIME IS EMPTY UTTER_ASK_WHEN
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
                        "subtitle":"Category: Home - Location: " + location,
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

            text_message = f"Hi {first_name}! You have requested for {specialty} in {location}. \n\nFor more details please visit https://m.me/servicereferralhub"
            # requests.post(url = f'http://sms.servicereferralhub.com:1401/send?username=foo&password=bar&to={phone_number}&content={text_message}') 
            dispatcher.utter_message(f"Note: You will earn a Rebate for every successful booking from this platform and it will automatically added in your Service Referral Hub - Wallet. ")
            dispatcher.utter_message(f'You have requested for {specialty} in {location} at {time} and your contact number is {phone_number}. Please Tap on "Confirm" to confirm you request.')
    
        else:
            message = {"text": "Sorry I didn't get the Provider you want. What type of Service do you need? (Aircon Installaton, House Cleaning, Electrical Repair, etc.)"}

        dispatcher.utter_custom_json(message)
        return []


class ActionAskHomeServices(Action):

    def name(self) -> Text:
        return "action_ask_home_services"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        most_recent_state = tracker.current_state()
        sender_id = most_recent_state['sender_id']

        message = {
                    "attachment": {
                        "type": "template",
                        "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                            "title": "Cleaning Services",
                            "image_url": "https://images.summitmedia-digital.com/spotph/images/2017/07/31/CleaningServices_10.jpg",
                            "subtitle": "Hire our cleaning experts",
                            "buttons": [
                                {
                                "type": "web_url",
                                "url": "https://www.servicereferralhub.com/messenger/cleaning-services/" + sender_id,
                                "title": "Cleaning Services",
                                "webview_height_ratio": "full",
                                "messenger_extensions": True,
                                "fallback_url": "https://www.servicereferralhub.com/messenger/cleaning-services/" + sender_id
                                }
                            ]
                            },
                            {
                            "title": "Interior Design",
                            "image_url": "https://www.arch2o.com/wp-content/uploads/2018/09/Arch2O-InteriorDesigner-9-1.jpg",
                            "subtitle": "Interior Design Experts",
                            "buttons": [
                                {
                                "type": "web_url",
                                "url": "https://www.servicereferralhub.com/messenger/interior-designer/" + sender_id,
                                "title": "Interior Designer",
                                "webview_height_ratio": "full",
                                "messenger_extensions": True,
                                "fallback_url": "https://www.servicereferralhub.com/messenger/interior-designer/" + sender_id
                                }
                            ]
                            },
                            {
                            "title": "Electrical Services",
                            "image_url": "http://midtowncitygreens.org/wp-content/uploads/2019/06/cropped-midtowncitygreens-header.jpg",
                            "subtitle": "Electrical Installation, Maintenance & Troubleshooting",
                            "buttons": [
                                {
                                "type": "web_url",
                                "url": "https://www.servicereferralhub.com/messenger/electrical-services/" + sender_id,
                                "title": "Electrical Services",
                                "webview_height_ratio": "full",
                                "messenger_extensions": True,
                                "fallback_url": "https://www.servicereferralhub.com/messenger/electrical-services/" + sender_id
                                }
                            ]
                            },
                            {
                            "title": "Plumbing Services",
                            "image_url": "http://www.phdmechanicalnj.com/wp-content/uploads/2016/05/phd-mechanical-Kitchen-Plumbing-Services.jpg",
                            "subtitle": "Plumbing Services",
                            "buttons": [
                                {
                                "type": "web_url",
                                "url": "https://www.servicereferralhub.com/messenger/plumbing-services/" + sender_id,
                                "title": "Plumbing Services",
                                "webview_height_ratio": "full",
                                "messenger_extensions": True,
                                "fallback_url": "https://www.servicereferralhub.com/messenger/plumbing-services/" + sender_id
                                }
                            ]
                            },
                            {
                            "title": "Aircon Services",
                            "image_url": "https://www.81aircon.com/wp-content/uploads/2016/11/repair.jpg",
                            "subtitle": "Aircon Installation, Cleaning & Repair",
                            "buttons": [
                                {
                                "type": "web_url",
                                "url": "https://www.servicereferralhub.com/messenger/aircon-services/" + sender_id,
                                "title": "Aircon Services",
                                "webview_height_ratio": "full",
                                "messenger_extensions": True,
                                "fallback_url": "https://www.servicereferralhub.com/messenger/aircon-services/" + sender_id
                                }
                            ]
                            },
                            {
                            "title": "Home Renovation",
                            "image_url": "https://img-aws.ehowcdn.com/600x600p/s3-us-west-1.amazonaws.com/contentlab.studiod/getty/94dbf74690e34394bd9da6624ba75e3a.jpg",
                            "subtitle": "Home Renovation & Improvements",
                            "buttons": [
                                {
                                "type": "web_url",
                                "url": "https://www.servicereferralhub.com/messenger/home-renovation/" + sender_id,
                                "title": "Home Renovation",
                                "webview_height_ratio": "full",
                                "messenger_extensions": True,
                                "fallback_url": "https://www.servicereferralhub.com/messenger/home-renovation/" + sender_id
                                }
                            ]
                            },
                            {
                            "title": "Laundry & Dry Cleaning",
                            "image_url": "https://media3.s-nbcnews.com/i/newscms/2016_32/1149295/laundry-stock-today-160808-tease_8816217b49c15bf3fc07bbcd6558c2db.jpg",
                            "subtitle": "Dry Cleaning to Wash & Fold Services",
                            "buttons": [
                                {
                                "type": "web_url",
                                "url": "https://www.servicereferralhub.com/messenger/laundry-services/" + sender_id,
                                "title": "Laundry Services",
                                "webview_height_ratio": "full",
                                "messenger_extensions": True,
                                "fallback_url": "https://www.servicereferralhub.com/messenger/laundry-services/" + sender_id
                                }
                            ]
                            }
                        ]
                        }
                    }
                   }

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
