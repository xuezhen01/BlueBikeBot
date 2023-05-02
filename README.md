# BlueBikeBot
**Done by: Matteo Sta. Maria and Xue Zhen Ng**

---

## 1. Overview

This project focuses on building a Telegram Bot for users to find out real-time data of Blue Bikes.

## 2. The Big Idea: 

The Main idea of this project would be to enable users to find out bike availabilities via the telegram bot - User raises a question about bluebikes, e.g. whether there are bikes available for rent at a specific station.

Instructions: 
1. Run app.py (5000)
2. ensure ngrok is installed, run ngrok on http 5000
3. Copy the link given from running ngrok on a separate terminal
4. Here is the link to run on your browser: https://api.telegram.org/bot<Your Bot Token>/setWebhook?url=<URL that you got from Ngrok>
5. Run the link on the browser with API key and NGROK link included 
6. Test the bot! 

## 3. Learning Objectives

For this project, we both aim to be able to integrate more features with functionalities into the project, and to ensure good communication and teamwork is obtained. 

Individual goals:

xz - I want to be able to build a telegram bot successfully, as i have never done so before and feel that it would give me good exposure. I also want to be able to better organise code structure to ensure neatness and good coding habits. 

matteo - I would want to look into learning how to use the Telegram API and utilizing the user's location in order to find the nearest BlueBikes. In addition, I want to familiarize myself more with flask and designing a web app.

## 4. Implementation Plan: 

First, we have sourced for an API provided by bluebikes, this API is able to share with us the station names and IDs, number of available bikes, number of bikes to be returned and many more. 

Next, we want to be read up on the implementation of a telegram bot, and how a bot can read and respond to queries from the user to provide accurate replies. Following this, we will find out how we can integrate using a map into telegram bot. 

To add more fun features, we also would like to explore using telegram features such as sending current location to the bot, and then intepreting the location details to return the nearest bike station, rather than having the user manually type the zipcode or location address. 

## 5. Project Schedule: 

- Week 1: read up on telegram bot, how to access the bluebike api, how to structure the API calling (as more than 1 api will need to be called), define what functionalities the telegram bot should be able to carry out. 
- Week 2: create flask file and other files (html, functions), build the basic requirements of a telegram bot. Create necessary functions to call and extract data given from bluebike's api.
- Week 3: utilise mapbox to enable user's input to get the nearest bluebike location to the user's input. code out the responses from a bot, cover corner cases as well (when location does not exist, or when location is out of bounds (where bluebike does not provide services & other error messages)
- Week 4: continue week 3's functionalities 
- Week 5: improve code functionality and tidy up any unnecessary features, add more special featuers from telegram, such as using location services to send user's current location. Or add some cool responses to random questions submitted by user. 
- Week 6: testing for the website, to ensure that the functionalities are working. 

## 6. Collaboration Plan

To collaborate for this project, we plan on having a mix of in-person meetings and asynchronous work. During our first in-person meeting, we will outline the various functions we need to complete and delegate tasks accordingly. We might consider experimenting with a scrum structure where several days a week, we update each other on what we are doing, what progress we made, and what next steps we have. Since it is just a 2 person project, it will be really easy to find meeting times and communicate effectively through text messaging.

## 7. Risks and Limitations

One significant threat to the project's success is Telegram bot not being able to return the expected asnwers, such as the nearest bike not being able to be found. API call failing, because we will need to access different api to link the data together, example API 1 only provides station ID, but to get the exact station name, we will need to call API 2 and match the station ID to obtain the station name. 

## Additional Course Content

What topics do you believe will be beneficial to your project?

