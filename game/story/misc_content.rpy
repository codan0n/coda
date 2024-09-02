label roriDormIntro:
    $ roriDormIntroSeen = True
    #"this is a description of rori's dorm for when you visit it for the first time"
    
    scene bg roridorm with dissolve
    
    n "Scattered throughout Rori's dorm are various electronics that heat the room to rival a sauna."
    n "The glow of several CRT monitors displaying vintage anime pierces your retinas. Toxic fumes from a soldering iron linger in the air, making you cough. The whirring of fans could drown out the sound of a jet engine."
    
    rori "Sorry about the mess. Housing pays for power so I hooked up a few crypto mining ASICs to generate some passive income."
    
    menu:
        "And kill the environment.":
            player "And destroy the environment in the process."
            
            rori "A few kilowatts is nothing in the grand scheme of things."
            rori "There's a nuclear power plant that generates plenty of electricty nearby."
        "Based electricity thief.":
            player "Based electricity thief."
            
            rori "It's not stealing if they're giving it away for free."
            rori "If they didn't want me using 6000 watts, they shouldn't have given me so many electric sockets."
            
            player "I don't think they accounted for daisy chaining power strips like that. Seems like a fire hazard."
            
            rori "Good thing they have insurance then, and I have remote backups."
    
    return
    
label avaClaireDormIntro:
    $ avaClaireDormIntroSeen = True
    
    "this is a description of Claire and Ava's dorm, to be played the first time you enter it."
    "It's split into two halves with a bed on either end. What must be Ava's side is tidy with photography books and expensive camera gear on the desk."
    "Whereas Claire's side is unkempt and disorganized. She has a tendency to leave her underwear in random places."
    
    
    return
    

label sleepingIn:
    #scene plays the first time you sleep in and skip class
    
    $ bedpilled = True
            
    #results in you skipping class but having more time to do stuff after class
    
    n "Without a doubt, the best thing you can do is take care of yourself."
    n "And taking care of yourself means hitting the snooze button from time to time."
    n "By your calculations, five more minutes of shuteye translates to at least an hour of alertness and productivity in the day."
    n "Can you really refuse such a lucrative offer? That's more than a 10x return on investment!"
    n "Yes, it's best to return to your comfy fortress underneath those blankets."
    n "It would be foolish to fall for the sunk cost fallacy line of thinking that you *must* continue your day right now just because you've already gotten out of bed."
    n "You crawl into the cotton's warm embrace and go for round two in the ring of slumber."
    
    scene bg black with fade
    
    pause 0.9
    
    scene bg codadorm with fade
    
    n "Five minutes turned into an hour in the snap of your fingers."
    n "Time's imperceptibly slow march suddenly lurched forward while you were asleep to stab you in the back when you were at your most vulnerable."
    n "Your eyes open and focus in on your clock. Your first class of the day is halfway over by now but you might make it to the second one."
    n "Although you do feel slightly more energized, you forgot to account for diminishing returns."
    n "Plus you now have to pay back your debt to the sleep economy by getting less than an optimal amount of sleep later."
    n "Or you could go to bed earlier, but then you'd miss out on... {i}activities.{/i}"
    n "Just something to consider. For now, you need to get ready and go to class."

    return
    
    
#label weatherSystem:
#    #generates a week's worth of weather values
#    #equal chance of sunny or cloudy weather
#    #cloudy weather makes the next day more likely to be overcast
#    #overcast weather makes the next day more likely to be rainy
#    #chance of precipitation builds up in the absence of precipitation and occurs at least once every 12 days
#
#    $ i = 0
#    $ weeklyWeather = [(currentDay, currentWeather), (Sunday, "sunny"), (Monday, "sunny"), (Tuesday, "sunny"), (Wednesday, "sunny"), (Thursday, "sunny"), (Friday, "sunny"), (Saturday, "sunny")]
#    
#    for i < week.length:
#        i =+1
#        
#        if weather[i-1] = "overcast":
#            overcastValue = 1
#        else:
#            overcastValue = 0
#        if weather[i-1] = "cloudy":
#            cloudyValue = 1
#        else:
#            cloudyValue = 0
#    
#        chancePrecipitation = (daysSinceRain / 12) + .05 + (overcastValue * .1)
#        chanceOvercast = .1 + (cloudyValue * .1)
#        chanceSunny = (1 - chanceRainy - chanceOvercast) / 2 
#        chanceCloudy = chanceSunny
#        
#         randVal = renpy.random(0,100)
#        
#        if randVal / 100 < chancePrecipitation:
#            determinedWeather = "precipitation"
#        elif randVal / 100 < (chancePrecipitation + chanceOvercast):
#            determinedWeather = "overcast"
#        elif randVal / 100 < (chanceSunny + chanceOvercast + chancePrecipitation):
#            determinedWeather = "cloudy"
#        else:
#            determinedWeather = "sunny"
#            
#        weeklyWeather[i, 1] = determinedWeather
#
#
#        
#    
#    
#    
#    return