## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- Yes

## intent:negation
- No
- no
- Nope

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- HI
- Hi
- Hello

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- I am looking for [italian](cuisine) restaurants in [bangalore](location) for budget of [less than 300](budget)
- please show me [cheap](budget) restaurant in [Mumbai](location)
- show me [chinese](cuisine) restaurant for price for two people between [300 and 700](budget)
- [South indian] restaurant in [Delhi](location) for budget of  [> 700](budget)
- Find me [Italian](cuisine) restaurant in [Mumbai](location) for [700](budget)
- search me chinese restaurant in [Pune](location) for budget of [more than 700](budget)
- [South indian] restaurant in [Delhi](location) for price of  [> 700](budget)
- search me chinese restaurant in [Pune](location) for price of [more than 700](budget)
- [> 700](budget) price restaurant in [Kolkata](location)
- find me restaurant in [Mumbai](location)
- [300](budget) to [700]{"entity": "budget", "value": " more than 700"}
- find me chienese restaurnat in [sldkajfsdlkj](location) for budget of [less than 300](budget)
- find me [italian](cuisine) restaurant in [lkjdfkj](location) for budget of [less than 300](budget)
- find me [italian](cuisine) restaurant in [adslkj](location) for price of [300 and 700]{"entity": "budget", "value": " 300 to 700"}
- find me [italian](cuisine) restaurant in [lkjadf](location) for budget of [300 to 700]{"entity": "budget", "value": " 300 to 700"}
- find me [Italian](cuisine) restaurant in [lkjadsf](location)
- [lkasjdf](location)
- Find me [Italian](cuisine) restaurant in [Mumbai](location)
- Find me [italian](cuisine) restaurant in [Mumbai](location) for price of [less than 300](budget)
- [amar@gmail.com](email)
- restaurant in [Mumbai](location) for budget of [less than 300](budget)
- [Mexican](cuisine)
- find south indain restaurant in [Mumbai](location) for budget of [less than 300](budget)
- [amarparsekar@gmail.com](email)
- find [south indian](cuisine) restaurant in [chennai](location) for budget between [300 and 700]{"entity": "budget", "value": " 300 to 700"}
- find [north indian](cuisine) restaurant in [chennai](location) for budget between [300 and 700]{"entity": "budget", "value": " 300 to 700"}
- find [north indian](cuisine) restaurant
- find [south indian](cuisine) restaurant
- find [chinese](cuisine) restaurant in [Nashik](location) for price between [300 and 700]{"entity": "budget", "value": " 300 to 700"}
- find me restaurant
- [ahmedabad](location)
- [more than 700](budget)
- [Pune](location)
- [American](cuisine)
- find me restaurant in [Jaipur](location)
- [less than 300](budget)
- find me [chinese](cuisine) restaurant
- [Luckhnow](location)
- find [chinese](cuisine) restaurant in [Mumbai](location)
- [more than 700](budget)
- [amarparsekar@gmail.com](email)
- [Bokaro Steel City](location)
- [surat](location)
- [Warangal](location)

## synonym: 300 to 700
- 300 and 700
- 300 to 700
- 300 & 700
- 300 > and <700
- minimum of 300 and maximum of 700

## synonym: more than 700
- 700
- >700
- greater than 700
- 700 and more
- > 700

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:less than 300
- < 300
- < than 300
- lesser than 300
- less than 300
- cheap
- cheapest

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}


