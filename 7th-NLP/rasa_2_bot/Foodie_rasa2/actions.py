from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib, ssl
from email.message import EmailMessage


class Utility:

	def get_soundex(self, token):

		token = token.upper()
		soundex = 'A'
		# first letter of input is always the first letter of soundex\n",
		#soundex += token[0]
		dictionary = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6", "AEIOUHWY":"."}
	
		for char in token[1:]:
			for key in dictionary.keys():
				if char in key:
					code = dictionary[key]
					if code != '.':
						if code != soundex[-1]:
							soundex += code 
	
		# trim or pad to make soundex a 4-character code\n",
		soundex = soundex[:4].ljust(4, "0")
		return soundex


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		

			
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget').strip()
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		lowerLimit = 0
		upperLimit = 0
		rests = {}
		counter = 0

		if (budget) == 'less than 300':
			lowerLimit = 0
			upperLimit = 300
		
		if (budget) == '300 to 700':
			lowerLimit = 300
			upperLimit = 700
			
		if (budget) == 'more than 700':
			lowerLimit = 700
			upperLimit = 100000
		
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 1000)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				if ((restaurant['restaurant']['average_cost_for_two']) > lowerLimit) and ((restaurant['restaurant']['average_cost_for_two']) < upperLimit):
					counter +=1 
					if counter > 5:
						break
					response= restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+str(restaurant['restaurant']['user_rating']['aggregate_rating'])
					rests[response] = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
			rests = sorted(rests,key=rests.get,reverse=True)
			response = ''
			for msg in rests:
				response=response+ msg +"\n"
		
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

class ValidateLocation(Action):
	def name(self):
		return 'validate_location'

	def run(self, dispatcher, tracker, doomain):
		t1_t2_cities = ["Ahmedabad","Bangalore","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune","Agra","Ajmer","Aligarh","Allahabad","Amravati","Amritsar","Asansol","Aurangabad",
						"Bareilly","Belgaum","Bhavnagar","Bhiwandi","Bhopal","Bhubaneswar","Bikaner","Bokaro Steel City","Chandigarh","Coimbatore","Cuttack","Dehradun",
						"Dhanbad","Durg-Bhilai Nagar","Durgapur","Erode","Faridabad","Firozabad","Ghaziabad","Gorakhpur","Gulbarga","Guntur","Gurgaon","Guwahati",
						"Gwalior","Hubli-Dharwad","Indore","Jabalpur","Jaipur","Jalandhar","Jammu","Jamnagar","Jamshedpur","Jhansi","Jodhpur","Kannur","Kanpur","Kakinada","Kochi","Kottayam","Kolhapur","Kollam","Kota","Kozhikode","Kurnool","Lucknow","Ludhiana",
						"Madurai","Malappuram","Mathura","Goa","Mangalore","Meerut","Moradabad","Mysore","Nagpur","Nanded","Nashik","Nellore","Noida","Palakkad","Patna","Pondicherry","Raipur","Rajkot",
						"Rajahmundry","Ranchi","Rourkela","Salem","Sangli","Siliguri","Solapur","Srinagar","Sultanpur","Surat","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tirunelveli","Tiruppur",
						"Ujjain","Vijayapura","Vadodara","Varanasi","Vasai-Virar City","Vijayawada","Visakhapatnam","Warangal"]

		t1_t2_cities_list = [x.lower() for x in t1_t2_cities]
		loc = tracker.get_slot('location')
		city = str(loc)
		util = Utility()
		for c in t1_t2_cities_list:
			c_list =  util.get_soundex(c)
			city2 = util.get_soundex(city)

			if city2 == c_list:
				city = c
				break

		if(city.lower() in t1_t2_cities_list):
			return [SlotSet('check_loc',True)]
		else:
			return [SlotSet('check_loc',False)]
			
class SendEmail(Action):
	def name(self):
		return 'send_email'

	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget').strip()
		email = tracker.get_slot('email').strip()
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		lowerLimit = 0
		upperLimit = 0
		rests = {}
		counter = 0

		if (budget) == 'less than 300':
			lowerLimit = 0
			upperLimit = 300
		
		if (budget) == '300 to 700':
			lowerLimit = 300
			upperLimit = 700
			
		if (budget) == 'more than 700':
			lowerLimit = 700
			upperLimit = 100000
		
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 1000)
		d = json.loads(results)
		response=""

		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				if ((restaurant['restaurant']['average_cost_for_two']) > lowerLimit) and ((restaurant['restaurant']['average_cost_for_two']) < upperLimit):
					counter +=1 
					if counter > 10:
						break
					response= restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+str(restaurant['restaurant']['user_rating']['aggregate_rating'])+" for budget of -"+str(restaurant['restaurant']['average_cost_for_two'])
					rests[response] = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
			rests = sorted(rests,key=rests.get,reverse=True)
			response = 'Hello folk, \n\n\nPlease find details of Top 10 restaurant in '+loc+"\n\n\n"
			for msg in rests:
				response=response+ msg +"\n"
		
		
		msg = EmailMessage()
		msg.set_content(response)
		msg["Subject"] = "Top 10 "+cuisine+" restaurants in "+loc
		msg["From"] = "amarparsekar@gmail.com"
		msg["To"] = email

		context=ssl.create_default_context()

		with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
			smtp.starttls(context=context)
			smtp.login('amarparsekar@gmail.com', 'AnythingButN@t1_1')
			smtp.send_message(msg)
