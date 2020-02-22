from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker 
from rasa_sdk.executor import CollectingDispatcher

# SET SLOTS
from rasa_sdk.events import SlotSet
# API REQUESTS
import requests
import json
import requests
import time
import mysql.connector

# MINI DATABASE 
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

def checkifProviderRegistered(sender_id):
    conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='servicereferralhub')
    cursor = conn.cursor()
    sql = f"SELECT * FROM srhubapp_messengerprovider WHERE sender_id = '{sender_id}';" 
    cursor.execute(sql)
    result = cursor.fetchall()
    message = {}

    if result:
            message = {
                "text": "Welcome back! Select an option below.",
                "quick_replies":[
                    {
                    "content_type":"text",
                    "title":"🙋‍♀️ Show Requests",
                    "payload":"View Requests",
                    },{
                    "content_type":"text",
                    "title":"👨🏻‍💻 My Profile",
                    "payload":"Profile",
                    }]
            }
    else:
            message = {
                    "attachment": {
                        "type": "template",
                        "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                            "title": "Sign-up",
                            "image_url": "https://www.tune.com/wp-content/themes/tune.com/img/pages/our-platform-mobile.png",
                            "subtitle": "Become one of our Trusted Service Provider",
                            "buttons": [
                                {
                                "type": "web_url",
                                "url": "https://www.servicereferralhub.com/messenger/provider/signup/" + sender_id,
                                "title": "Sign-up",
                                "webview_height_ratio": "full",
                                "messenger_extensions": True,
                                "fallback_url": "https://www.servicereferralhub.com/messenger/provider/signup/" + sender_id
                                }]
                            }
                        ]
                        }
                    }
            }

    return message

def getCategories(sender_id):
    conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='servicereferralhub')
    cursor = conn.cursor()
    sql = "SELECT id,name,description,picture,url,main_id FROM srhubapp_messengercategory;" 
    cursor.execute(sql)
    result = cursor.fetchall()
    elements = []

    for row in result:
        data = {
                    "title": row[1],
                    "image_url": row[3],
                    "subtitle": row[2],
                    "buttons": [
                        {
                        "type": "web_url",
                        "url": "https://www.servicereferralhub.com/messenger/list/" + row[4] + "/" + sender_id,
                        "title": row[1],
                        "webview_height_ratio": "full",
                        "messenger_extensions": True,
                        "fallback_url": "https://www.servicereferralhub.com/messenger/list/" + row[4] + "/" + sender_id,
                        }
                    ]
                }
        elements.append(data)

    return elements

def getCategoryDetails(category):
    conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='servicereferralhub')
    cursor = conn.cursor()
    sql = f"SELECT title,picture FROM srhubapp_messengerform WHERE category = '{category}' LIMIT 1;" 
    cursor.execute(sql)
    result = cursor.fetchall()
    
    details = {}

    for row in result:
        details['title'] = row[0]
        details['picture'] = row[1]
    
    return details

def getRequest(provider_id):
    conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='servicereferralhub')
    cursor = conn.cursor()
    sql = "SELECT id,sender_id,name,address,category FROM srhubapp_messengerrequest ORDER BY id desc LIMIT 10;" 
    cursor.execute(sql)
    result = cursor.fetchall()
    elements = []

    for row in result:
        category_details = getCategoryDetails(row[4])
        title = category_details['title']
        picture = category_details['picture']
        data = {
                    "title": f"{row[2]} - {title}",
                    "image_url": picture,
                    "subtitle": row[3],
                    "buttons": [
                        {
                        "type": "web_url",
                        "url": "https://www.servicereferralhub.com/messenger/request/" + str(row[0]) + "/" + provider_id,
                        "title": "View Details",
                        "webview_height_ratio": "full",
                        "messenger_extensions": True,
                        "fallback_url": "https://www.servicereferralhub.com/messenger/request/" + str(row[0]) + "/" + provider_id,
                        }
                    ]
                }
        elements.append(data)

    return elements


class MyFallbackAction(Action):

    def name(self) -> Text:
        return "my_fallback_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,   
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = {
            "text": "Sorry I didn't get that. Can you rephrase that?",
            "quick_replies":[
            {
                "content_type":"text",
                "title":"🔍 Hire Provider",
                "payload":"Hire Provider",
            },
            {
                "content_type":"text",
                "title":"📣 Referrals",
                "payload":"Referrals",
            },
            {
                "content_type":"text",
                "title":"👷Provider",
                "payload":"Provider",
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

        specialty = tracker.get_slot('specialty')
        first_name = tracker.get_slot('first_name')
        location = tracker.get_slot('location')
        time = tracker.get_slot('time')
        phone_number = tracker.get_slot('phone_number')

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


class ActionAskHomeServices(Action):

    def name(self) -> Text:
        return "action_ask_home_services"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        most_recent_state = tracker.current_state()
        sender_id = most_recent_state['sender_id']

        elements = getCategories(sender_id)
        message = {
                    "attachment": {
                        "type": "template",
                        "payload": {
                        "template_type": "generic",
                        "elements": elements,
                        }
                    }
                   }
        dispatcher.utter_custom_json(message)
        return []


class ActionVerifyProvider(Action):

    def name(self) -> Text:
        return "action_verify_provider"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        most_recent_state = tracker.current_state()
        sender_id = most_recent_state['sender_id']

        message = checkifProviderRegistered(sender_id)

        dispatcher.utter_custom_json(message)
        return []

class ActionShowRequests(Action):

    def name(self) -> Text:
        return "action_show_requests"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        most_recent_state = tracker.current_state()
        sender_id = most_recent_state['sender_id']

        elements = getRequest(sender_id)
        message = {
                    "attachment": {
                        "type": "template",
                        "payload": {
                        "template_type": "generic",
                        "elements": elements,
                        }
                    }
                }
        dispatcher.utter_custom_json(message)
        return []
