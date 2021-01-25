## user story_1
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"check_loc": false}
	- utter_nooperation
    - utter_goodbye

## user story_2
* restaurant_search{"location": "sldkajfsdlkj", "budget": "less than 300"}
    - slot{"budget": "less than 300"}
    - slot{"location": "sldkajfsdlkj"}
    - validate_location
    - slot{"check_loc": false}
    - utter_nooperation
    - utter_goodbye


## user story_3
* restaurant_search{"cuisine": "italian", "location": "adslkj", "budget": " 300 to 700"}
    - slot{"budget": " 300 to 700"}
    - slot{"cuisine": "italian"}
    - slot{"location": "adslkj"}
    - validate_location
    - slot{"check_loc": false}
    - utter_nooperation
    - utter_goodbye

## user story_4
* restaurant_search{"cuisine": "italian", "location": "lkjadf", "budget": " 300 to 700"}
    - slot{"budget": " 300 to 700"}
    - slot{"cuisine": "italian"}
    - slot{"location": "lkjadf"}
    - validate_location
    - slot{"check_loc": false}
    - utter_nooperation
    - utter_goodbye

## user story_5
* restaurant_search{"cuisine": "Italian", "location": "lkjadsf"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "lkjadsf"}
    - validate_location
    - slot{"check_loc": false}
    - utter_nooperation
    - utter_goodbye

## user story_6
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Mumbai", "budget": "less than 300"}
    - slot{"budget": "less than 300"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"check_loc": true}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email
* affirm
    - utter_email
* restaurant_search{"email": "amar@gmail.com"}
    - slot{"email": "amar@gmail.com"}
    - send_email
    - utter_goodbye

## user story_7
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai", "budget": "less than 300"}
    - slot{"budget": "less than 300"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"check_loc": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email
* affirm
    - utter_email
* restaurant_search{"email": "amar@gmail.com"}
    - slot{"email": "amar@gmail.com"}
    - send_email
    - utter_goodbye

## user story_8
* restaurant_search{"location": "Mumbai", "budget": "less than 300"}
    - slot{"budget": "less than 300"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"check_loc": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email
* affirm
    - utter_email
* restaurant_search{"email": "amarparsekar@gmail.com"}
    - slot{"email": "amarparsekar@gmail.com"}
    - send_email
    - utter_goodbye

## user story_9
* restaurant_search{"cuisine": "south indian", "location": "chennai", "budget": " 300 to 700"}
    - slot{"budget": " 300 to 700"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "chennai"}
    - validate_location
    - slot{"check_loc": true}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_email
* negation
    - utter_goodbye

## user story_10
* restaurant_search{"cuisine": "chinese", "location": "Nashik", "budget": " 300 to 700"}
    - slot{"budget": " 300 to 700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Nashik"}
    - validate_location
    - slot{"check_loc": true}
    - action_search_restaurants
    - slot{"location": "Nashik"}
    - utter_ask_email
* negation
    - utter_goodbye

## user story_11
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - validate_location
    - slot{"check_loc": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - utter_ask_email
* affirm
    - utter_email
* restaurant_search{"email": "amarparsekar@gmail.com"}
    - slot{"email": "amarparsekar@gmail.com"}
    - send_email
    - utter_goodbye
	
## user story_12
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - validate_location
    - slot{"check_loc": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email
* negation
    - utter_goodbye
	
## user story_13
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"check_loc": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email
* negation
    - utter_goodbye
	
## user story_14
* greet
    - utter_greet
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - validate_location
    - slot{"check_loc": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - utter_ask_email
* affirm
    - utter_email
* restaurant_search{"email": "amarparsekar@gmail.com"}
    - slot{"email": "amarparsekar@gmail.com"}
    - send_email
    - utter_goodbye


## user story_15
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - validate_location
    - slot{"check_loc": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "less than 300"}
    - slot{"budget": "less than 300"}
    - action_search_restaurants
    - slot{"location": "Jaipur"}
    - utter_ask_email
* affirm
    - utter_email
* restaurant_search{"email": "amarparsekar@gmail.com"}
    - slot{"email": "amarparsekar@gmail.com"}
    - send_email
    - utter_goodbye

## user story_16
* restaurant_search{"cuisine": "chinese", "Location": null}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Luckhnow"}
    - slot{"location": "Luckhnow"}
    - validate_location
    - slot{"check_loc": true}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_search_restaurants
    - slot{"location": "Luckhnow"}
    - utter_ask_email
* negation
    - utter_goodbye

## user story_17
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"check_loc": true}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email
* affirm
    - utter_email
* restaurant_search{"email": "amarparsekar@gmail.com"}
    - slot{"email": "amarparsekar@gmail.com"}
    - send_email
    - utter_goodbye
	
## user story_18
* restaurant_search{"cuisine": "chinese", "Location": null}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Bokaro Steel City"}
    - slot{"location": "Bokaro Steel City"}
    - validate_location
    - slot{"check_loc": true}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_search_restaurants
    - slot{"location": "Bokaro Steel City"}
    - utter_ask_email
* negation
    - utter_goodbye
