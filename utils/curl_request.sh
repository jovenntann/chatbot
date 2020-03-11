curl -X POST -H "Content-Type: application/json" -d '{
  "messaging_type": "RESPONSE",
  "recipient": {
    "id": "2233033630067075"
  },
  "message": {
    "text": "You've earn ₱20.00 for your service request id *123456*"
  }
}' "https://graph.facebook.com/v4.0/me/messages?access_token=EAAFfYX0Yvt0BACRjOtnoj5QeqraZC6Xyop3eFr9evN2OBFyx0AtAylWtE0oYnnzL1Dq1M9ZAUMzuZAz2GVdqrh6EJickiTSAlBTbOofZCdPKIrL2lbNkS3Any6mOy4aR0JWY1ZCu4yZBaLtCieBlnjWmaT5hMjZAdbdDZAPwnurrUG66TqyK7lM9"




curl -X POST -H "Content-Type: application/json" -d '{
  "messaging_type": "RESPONSE",
  "recipient": {
    "id": "2233033630067075"
  },"message": {
    "type":"phone_number",
    "title":"Call",
    "payload":"+639062131607"
  }
}' "https://graph.facebook.com/v4.0/me/messages?access_token=EAAFfYX0Yvt0BACRjOtnoj5QeqraZC6Xyop3eFr9evN2OBFyx0AtAylWtE0oYnnzL1Dq1M9ZAUMzuZAz2GVdqrh6EJickiTSAlBTbOofZCdPKIrL2lbNkS3Any6mOy4aR0JWY1ZCu4yZBaLtCieBlnjWmaT5hMjZAdbdDZAPwnurrUG66TqyK7lM9"



curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id": "2233033630067075"
  },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"button",
        "text":"Need further assistance? Talk to a representative",
        "buttons":[
          {
            "type":"phone_number",
            "title":"Call Representative",
            "payload":"+639062131607"
          }
        ]
      }
    }
  }
}' "https://graph.facebook.com/me/messages?access_token=EAAFfYX0Yvt0BACRjOtnoj5QeqraZC6Xyop3eFr9evN2OBFyx0AtAylWtE0oYnnzL1Dq1M9ZAUMzuZAz2GVdqrh6EJickiTSAlBTbOofZCdPKIrL2lbNkS3Any6mOy4aR0JWY1ZCu4yZBaLtCieBlnjWmaT5hMjZAdbdDZAPwnurrUG66TqyK7lM9"

# Converted to:

utter_call_representative:
- custom: 
    attachment:
      type: template
      payload:
        template_type: button
        text: Need further assistance? Talk to a representative
        buttons:
        - type: phone_number
          title: Call Representative
          payload: "+639062131607"





curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id": "2233033630067075"
  },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[
          {
            "title":"Breaking News: Record Thunderstorms",
            "subtitle":"The local area is due for record thunderstorms over the weekend.",
            "image_url":"https://thechangreport.com/img/lightning.png",
            "buttons": [
              {
                "type": "element_share",
                "share_contents": { 
                  "attachment": {
                    "type": "template",
                    "payload": {
                      "template_type": "generic",
                      "elements": [
                        {
                          "title": "I took the hat quiz",
                          "subtitle": "My result: Fez",
                          "image_url": "https://bot.peters-hats.com/img/hats/fez.jpg",
                          "default_action": {
                            "type": "web_url",
                            "url": "http://m.me/petershats?ref=invited_by_24601"
                          },
                          "buttons": [
                            {
                              "type": "web_url",
                              "url": "http://m.me/petershats?ref=invited_by_24601", 
                              "title": "Take Quiz"
                            }
                          ]
                        }
                      ]
                    }
                  }
                }
              }
            ]
          }
        ]
      }
    }
  }
}' "https://graph.facebook.com/me/messages?access_token=EAAFfYX0Yvt0BACRjOtnoj5QeqraZC6Xyop3eFr9evN2OBFyx0AtAylWtE0oYnnzL1Dq1M9ZAUMzuZAz2GVdqrh6EJickiTSAlBTbOofZCdPKIrL2lbNkS3Any6mOy4aR0JWY1ZCu4yZBaLtCieBlnjWmaT5hMjZAdbdDZAPwnurrUG66TqyK7lM9"






"https://graph.facebook.com/2233033630067075?fields=first_name,last_name,profile_pic&access_token=EAAFfYX0Yvt0BACRjOtnoj5QeqraZC6Xyop3eFr9evN2OBFyx0AtAylWtE0oYnnzL1Dq1M9ZAUMzuZAz2GVdqrh6EJickiTSAlBTbOofZCdPKIrL2lbNkS3Any6mOy4aR0JWY1ZCu4yZBaLtCieBlnjWmaT5hMjZAdbdDZAPwnurrUG66TqyK7lM9"



"https://graph.facebook.com/v4.0/me/messenger_profile?access_token=EAAFfYX0Yvt0BAJrZAFFkEaUYZCADKGjhZAZCgH2NZBW79ZAYFIuw6EWvhOluYeCjWsYRc921qumO9ZBNNe49ZB32MCOm6sCzTWU3qZBRHDY36mCRNKZBpPXBsFsJAkyx1p2jZALP63ZBMLYwloT3gRsrgRFrQeogZCiOygzfTRA5ZAlUqP1TEu4FRQ9iIiTjSAOMU0cScZD"



## Set Menu Button ## 

curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
      "id": "2233033630067075"},
  "persistent_menu": [
    {
        "locale": "default",
        "composer_input_disabled": false,
        "call_to_actions": [
              {
                "type": "postback",
                "title": "🔍 Hire Provider",
                "payload": "Hire Provider"
            },
            {
                "type": "postback",
                "title": "📣 Referrals",
                "payload": "Referrals"
            },
            {
              "type": "postback",
              "title": "👷Provider",
              "payload": "Provider"
            }
        ]
    }
]
}' "https://graph.facebook.com/v4.0/me/messenger_profile?access_token=EAAFfYX0Yvt0BAEL6S4RQu8ZA5UJLRQ9bshQVLT6tFfaBQMuuwnddrimBR4VQ4I9HzsFjJA8B1ugzPr6ut4MK5X8CsNgqTqbwj3ZAVXP0B7JjLlSuqpNjMAfT7Dsn34VVtvLe3GcU62esDjSeErTybmY7Kx3n7uvUTZCJ7TZBMZAZAgLOgukkvVZBQA7IKzY2L8ZD"

## LIST VIEW

curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id":"2233033630067075"
  },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[
           {
            "title":"Agent",
            "image_url":"https://www.business.com/images/content/5ca/3daf75a215e8a458b9a90/1500-0-",
            "subtitle":"Become our agent and start to earning",
            "default_action": {
              "type": "web_url",
              "url": "https://petersfancybrownhats.com/view?item=103",
              "webview_height_ratio": "tall",
            },
            "buttons":[
              {
                "type":"postback",
                "title":"Be an Agent",
                "payload":"Be an Agent"
              }              
            ]      
          },
          {
            "title":"Provider",
            "image_url":"https://5.imimg.com/data5/IN/FQ/GLADMIN-33773374/carpentry-500x500.jpg",
            "subtitle":"Provide any kind of service and want to boost your sales",
            "default_action": {
              "type": "web_url",
              "url": "https://petersfancybrownhats.com/view?item=103",
              "webview_height_ratio": "tall",
            },
            "buttons":[{
                "type":"postback",
                "title":"Be a Provider",
                "payload":"Be a Provider"
              }              
            ]      
          }
        ]
      }
    }
  }
}' "https://graph.facebook.com/v2.6/me/messages?access_token=EAAFfYX0Yvt0BAJrZAFFkEaUYZCADKGjhZAZCgH2NZBW79ZAYFIuw6EWvhOluYeCjWsYRc921qumO9ZBNNe49ZB32MCOm6sCzTWU3qZBRHDY36mCRNKZBpPXBsFsJAkyx1p2jZALP63ZBMLYwloT3gRsrgRFrQeogZCiOygzfTRA5ZAlUqP1TEu4FRQ9iIiTjSAOMU0cScZD"




curl -X POST -H "Content-Type: application/json" -d '{
  "message":{
    "attachment":{
      "type":"image", 
      "payload":{
        "is_reusable": true,
        "url":"https://cdn.dribbble.com/users/220043/screenshots/6288970/dttr_loaderricerca_ac_ver1.gif"
      }
    }
  }
}' "https://graph.facebook.com/v5.0/me/message_attachments?access_token=EAAFfYX0Yvt0BAEL6S4RQu8ZA5UJLRQ9bshQVLT6tFfaBQMuuwnddrimBR4VQ4I9HzsFjJA8B1ugzPr6ut4MK5X8CsNgqTqbwj3ZAVXP0B7JjLlSuqpNjMAfT7Dsn34VVtvLe3GcU62esDjSeErTybmY7Kx3n7uvUTZCJ7TZBMZAZAgLOgukkvVZBQA7IKzY2L8ZD"
  





curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id":"2233033630067075"
  },
  "messaging_type": "RESPONSE",
  "message":{
    "text": "Pick a color:",
    "quick_replies":[
      {
        "content_type":"text",
        "title":"Red",
        "payload":"Red",
      },{
        "content_type":"text",
        "title":"Green",
        "payload":"Green",
      }
    ]
  }
}' "https://graph.facebook.com/v5.0/me/messages?access_token=EAAFfYX0Yvt0BAEL6S4RQu8ZA5UJLRQ9bshQVLT6tFfaBQMuuwnddrimBR4VQ4I9HzsFjJA8B1ugzPr6ut4MK5X8CsNgqTqbwj3ZAVXP0B7JjLlSuqpNjMAfT7Dsn34VVtvLe3GcU62esDjSeErTybmY7Kx3n7uvUTZCJ7TZBMZAZAgLOgukkvVZBQA7IKzY2L8ZD"