## RASA GUIDE  

#### Starting the Servers:
```bash
rasa run --credentials credentials.yml
rasa run actions
./ngrok http 5005
stack exec duckling-example-exe

# Monitor Webhook Logs
http://localhost:4040 
```


#

#### Linux command Installation:
```
export PATH=/root/anaconda3/condabin:$PATH
```

> Requirements: Python 3.6 

#### reate Anaconda Env
```
conda create --name BotDev python=3.6
```

#### Install Rasa X
``` 
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
```

#### Initialize RASA Project
```
rasa init
```

#### To fixed some error on runtime
```
conda install matplotlib 
```


RASA Commands
```bash
rasa shell # RASA Testing in CLI
rasa shell nlu # Test NLU Training Data
rasa interactive # Create Stories via Interactive thru CLI
rasa train # Train RASA (NLU,Core,Etc.)
rasa visualize # Generate Visualize Flow from Trained Data
rasa run actions # Run Actions Service

rasa run --enable-api # Run Code and Enable API
rasa run --enable-api --cors "*" --debug # Debugging Verbose


# Get Conversation Tracker Data (GET)
curl http://localhost:5005/conversations/default/tracker | python -mjson.tool
curl http://localhost:5005/conversations/joventan/tracker | python -mjson.tool

# Predict (POST)
curl -X POST http://localhost:5005/conversations/default/predict | python -mjson.tool

# Rest API | Send Message
curl -X POST http://localhost:5005/webhooks/rest/webhook -d '{"sender": "joventan", "message": "hello"}' -H "Content-type: application/json" | python -mjson.tool

```


#### Issues and Fixed:

```python
RuntimeError: Python is not installed as a framework.
The Mac OS X backend will not be able to function correctly if Python is not installed 
as a framework. See the Python documentation for more information on installing Python 
as a framework on Mac OS X. Please either reinstall Python as a framework,
or try one of the other backends.

# Solution to Fix:
conda install matplotlib 
```

#### rasa run --credentials credentials.yml
> https://38f3d100.ngrok.io/webhooks/facebook/webhook


#### Messenger Templates:
> https://developers.facebook.com/docs/messenger-platform/reference/template/button  


## Duckling
#### Duckling Installation Guide: 
>https://github.com/facebook/duckling#quickstart

```python
# MAC OS
curl -sSL https://get.haskellstack.org/ | sh

# Install Brew
brew install pcre

# Install Duckling
# Download Duckling Git Repo
https://github.com/facebook/duckling.git
cd duckling-master
stack build
# Run Inside Duckling Master Folder
stack exec duckling-example-exe

# Stack has been installed to:
/usr/local/bin/stack
```

#### Linux Duckling Installation:
```bash
wget -qO- https://get.haskellstack.org/ | sh
wget https://github.com/facebook/duckling/archive/master.zip
# cd to extracted directory
stack build
stack build -j1 # 1 mwc-random SHA # Avoid error with Out of memory
# Run Inside Duckling Master Folder
stack exec duckling-example-exe
stack exec duckling-example-exe -- -p 9000 # run in port 9000
```


#### Edit: config.yml
```
language: "en"

pipeline:
- name: "nlp_spacy"
- name: "tokenizer_spacy"
- name: "intent_entity_featurizer_regex"
- name: "intent_featurizer_spacy"
- name: "ner_crf"
- name: "ner_synonyms"
- name: "intent_classifier_sklearn"
- name: "ner_duckling_http"
  url: "http://127.0.0.1:8000"
  dimensions: ["time"] 
```


```python
/Users/joventan/anaconda/envs/BotDev/lib/python3.6/site-packages/rasa/core/channels/facebook.py

# Add This Line

        try:
            referrer_id = self.last_message.get("postback", {}).get("referral","").get("ref","")
            # if referred_id is not None:
            text = "REFERRED " + str(referrer_id)
        except:
            print("TRY CATCH TRIGERRED")

# Edit before this line
out_channel = MessengerBot(self.client)
user_msg = UserMessage(text, out_channel, sender_id, input_channel=self.name())


```

DOCKER
```python
https://docs.docker.com/install/linux/docker-ce/centos/
https://hub.docker.com/r/ramtin/duckling/

# REMOVE DOCKER:
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine

# INSTALL DOCKER UTILS:
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2

sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

# INSTALL DOCKER:
sudo yum install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo docker run hello-world

# RUN FB DUCKER
docker run -d -p 8000:8000 ramtin/duckling
curl -XPOST http://localhost:8000/parse --data 'text=tomorrow at eight'

# CHECK DOCKER STATUS
service docker status
```


EDIT DUCKLING EXTRACTOR TO WORK WITH DUCKLING VIA DOCKET
```python
/root/anaconda3/envs/BotDev/lib/python3.6/site-packages/rasa/nlu/extractors/duckling_http_extractor.py

def extract_value(match):
    print(match)
    # DIM TIME
    if match["dim"] == "time":
        match = json.loads(match["value"])
        if match['type'] == "interval":
            value = match['from']['value']
            # value = {
            #     match['from']['value'],
            #     match['to']['value']
            # }
        else:
            value = match["value"]
    else:
        value = None

    # if match["value"].get("type") == "interval":
    #    value = {
    #        "to": match["value"].get("to", {}).get("value"),
    #        "from": match["value"].get("from", {}).get("value"),
    #    }
    # else:
    #    value = match["value"].get("value")

    # value = match["value"]

    return value
```
   