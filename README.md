## Build a Real-Time Shipment Tracking Tool using a Telegram Bot 🚚
*Design a Telegram Bot that will interact with truck drivers to track your shipments and provide real-time visibility of your transportation performance*

### Medium Article
In this [Medium Article](https://towardsdatascience.com/build-a-real-time-shipment-tracking-tool-using-a-telegram-bot-beb6ab29fca3), we will implement a simple, cheap and easy-to-implement solution to track your shipments that
- Does not require additional IT development for your carriers
- Easily integrates into the current transportation processes
- Reduces admin workload for your logistics team
- Does not impact drivers’ productivity
- Does not require additional equipment
- Provides visibility, real-time tracking and transparency

### How does it work?
Scenario
Your shipment has been unloaded in your store. DRIVER wants to send delivery confirmation before leaving for his next destination.\
#### Step 1: DRIVER opens telegram and starts a discussion with BOT 
![This is an image](https://miro.medium.com/max/315/1*qnBHC99rd8J1Q5xmommMew.png) 
#### Step2: DRIVER shares it’s GPS Location (= Store Location) 
![This is an image](https://miro.medium.com/max/315/1*c1XgJWH7EH-Lcg5YPQiTWA.png)
#### Step 3: DRIVER shares a delivery number 
![This is an image](https://miro.medium.com/max/315/1*Vb3et27oNAnje5sSWgdh0w.png) 
#### Step 4: DRIVER shares a picture of the shipment 
![This is an image](https://miro.medium.com/max/315/1*7r7RHIWykG3zklrSl2DxPQ.png) 
#### Step 5: Your logistics teams receive a shipment confirmation
![This is an image](https://miro.medium.com/max/315/1*V1oEQcRAPxcgCPYN5ywZZA.png) 


## Code
This repository code is ready to be deployed on Heroku:
##### 1. Copy Github repository in your local folder and create a local python environment
##### 2. Download libraries listed in requirements.txt
```
  pip3 install -r requirements.txt
```
#### 1. Create your bot with another bot :)
@ BotFather is a Telegram bot that will help you create your own bot \
Search @ BotFather on Telegram and send him ‘/start’ \
Answer ‘/newbot’ message and follow instructions to set up a name and a username \
Your bot is now ready, with an API token created — please keep a copy of this token! 

![This is an image](https://miro.medium.com/max/875/1*FcjfAGjjYuQ_GG8s9dWQQg.png) 

#### 2. Take your token and Telegram API keys
```
TOKEN: shared by @ BotFather when you created your bot
APP_NAME: address of your Heroku application (see steps below)
```

#### 3. Deploy the code on the cloud
Heroku is a cloud-based service where you can host your web application; the free formula of hosting provides enough resources to run your app.
```
Procfile
requirements.txt
```

#### 4. Test it :)

## About me 🤓
Senior Supply Chain Engineer with an international experience working on Logistics and Transportation operations. \
Have a look at my portfolio: [Data Science for Supply Chain Portfolio](https://samirsaci.com) \
Data Science for Warehousing📦, Transportation 🚚 and Demand Forecasting 📈 

