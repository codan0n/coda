label chapter2start:

    ###CHAPTER 2
    ###weather is randomized and affects what you can do after class
    ###once a week you can sleep in and get a night scene
    ###can also do night scenes on weekends more freely
    ###pass out in class on thursday and take the next day off
    ###can sometimes study a topic after class
    
    
    ###week 2 monday rose stays behind in class to talk to rothbauer
    ###week 2 wednesday he gives you a book about your project
    
    "weather test start"

    python:
        ###weather function written by iggy
        import random
        
        def generate_weather(): # 1 usage
            SUNNY = 'Sunny' # these strings should represent labels or scenes in renpy
            CLOUDY = 'Cloudy'
            OVERCAST = 'Overcast'
            PRECIP = 'Rainy'
            
            weather_list = [] # this is where we store the weather strings
            # initialized as an empty array
            
            previous_weather = SUNNY # previous_weather initialized as SUNNY
            
            def get_next_weather(previous):
                #bear in mind that the random() function returns a float number between 0.1 and .99
                if previous == SUNNY:
                    return SUNNY if random.random() < 0.5 else CLOUDY
                elif previous == CLOUDY:
                    return OVERCAST if random.random() < 0.7 else CLOUDY
                elif previous == OVERCAST:
                    return PRECIP if random.random() < 0.7 else OVERCAST
                elif previous == PRECIP:
                    return SUNNY if random.random() < 0.5 else CLOUDY
            
            for day in range(7):
                next_weather = get_next_weather(previous_weather)
                weather_list.append(next_weather)
                previous_weather = next_weather
                
            if PRECIP not in weather_list:
                weather_list[random.randint(0, 6)] = PRECIP
                
            return weather_list
            
            
        print(generate_weather())
        
    $ tmpstring = generate_weather()
    
    "weather is [tmpstring]"

    "weather function finished"
    