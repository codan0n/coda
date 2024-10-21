label afterClassOptions:
    "What would you like to do?"
    
    menu:
        "Go somewhere":
            "Where do you want to go?"

            menu:
                "Explore" if afterClassExploration: #if trackDiscovered == False or gardenDiscovered == False or townDiscovered == False or forestDiscovered == False: #if locationsAvailable == False:
                
                    $ randomSelected = renpy.random.choice(afterClassExploration)
                    
                    call expression randomSelected
                    
                    call dormSleep
                
                "Town" if townDiscovered == True:
                    #if there are town events available, do one and then return to dorm for the night. If not, play a generic scene and let the player choose another location
                    
                    if townEvents:
                        $ randomSelected = renpy.random.choice(townEvents)
                        
                        call expression randomSelected
                        
                        call dormSleep
                        
                    else:
                        "You wander around town but don't find anything interesting to do."
                        
                        jump afterClassOptions
                "Track" if trackDiscovered == True:
                    if trackEvents:
                        $ randomSelected = renpy.random.choice(trackEvents)
                        
                        call expression randomSelected
                        
                        call dormSleep

                        
                    else:
                        "You wander around the fitness area but don't find anything interesting to do."
                        
                        jump afterClassOptions
                
                "Forest" if forestDiscovered == True:
                    if forestEvents:
                        $ randomSelected = renpy.random.choice(forestEvents)
                        
                        call expression randomSelected
                        
                        call dormSleep
                        
                    else:
                        "You wander around the forest but don't find anything interesting to do."
                        
                        jump afterClassOptions
                
                "Garden" if gardenDiscovered == True:
                    if gardenEvents:
                        $ randomSelected = renpy.random.choice(gardenEvents)
                        
                        call expression randomSelected
                        
                        call dormSleep
                        
                    else:
                        "You wander around the botanical garden but don't find anything interesting to do."
                        
                        jump afterClassOptions
                "Cafe":
                    if cafeEvents:
                        $ randomSelected = renpy.random.choice(cafeEvents)
                        
                        call expression randomSelected
                        
                        call dormSleep
                        
                    else:
                        "You get something to snack on at the cafe but don't find anything interesting to do."
                        
                        jump afterClassOptions
                    
                "Go back":
                    "jump afterClassOptions"
        "Study at dorm":
            "You decide to return to your dorm early and get some studying in."
            
            call dormStudy
            
    return
    
    
label dormSleep:
    scene bg codadorm with fade

    "The day is just about over. All you can do now is get ready for bed."

    return
    
label dormStudy:
    scene bg codadorm with fade

    n "There's still some time to study before you have to go to bed."
    n "What should you study?"
    
    menu:
        "French":
            $ frenchSkill =+ 1
            n "You pick up your French textbook and practice some lessons."
        "Literature":
            $ literatureSkill =+ 1
            n "You open your totally legally acquired epub of The Death of Ivan Ilyich and start reading."
        "History":
            $ historySkill =+ 1
            n "You crack open your History textbook and read up on some ancient cultures."
        "Statistics":
            $ statsSkill =+ 1
            n "You flip open your statistics book and open a calculator app to crunch some numbers."
            
    n "It took a while, but you now feel more confident in your understanding of the topic."
    n "It's gotten late. Time to get ready for bed."    
    
    scene bg black with fade    
    
    return

    
label nightWalks:
    #alternate between generic scenes and specific ones. Can choose who to hang out with if you've done first part of their arc?
    "You decide to go out for the night."
    
    $ randomSelected = renpy.random.choice(nightEvents)
    
    
    return

label mishkaGarden:
    "mishka garden scene"

    return
    
label avaGarden:
    "ava garden scene"
    
    return
    
label claireForest:
    "claire forest scene"
    return
    
label roseForest:
    "rose forest scene"
    return

label roriTrack:
    "rori track scene"
    #use some workout machines with rori
    return
    

label gunnerTrack:
    #check if gunnerTrack number x has been seen yet and play the next one. Use a day counter to prevent this scene from being able to be played 2 days in a row
    
    #$ gunnerTrackNumber += 1
    
    "You make your way back to the fitness area, past the track to the weights and machines where a multitude of students are exercising."
    "Unsurprisingly, among them is Gunner on a bench press, pushing a bar with a couple of large plates up above his chest."
    "He sharply inhales each time the bar comes down and steadily exhales as he extends his arms upward. His steady form allows him to move the barbell smoothly with grace."
    "After a few reps, he sets it on the rack and sits up. As he reaches for his water bottle he notices you awkwardly standing around and waves you over."
    
    gunner "Sup! I didn't expect to see you here!"
    
    player "What's that supposed to mean?"
    
    gunner "Nothin.\'"
    gunner "You here to get swoll?"
    
    "He flexes his slender bicep as if to accentuate his point."
    
    player "Man, how were you lifting that with those skinny arms? 2 plates? That's what, 180 pounds?"
    
    gunner "Raw strength isn't everything, there's actually a lot of technique that goes into it!"
    gunner "Lemme show you."
    
    n "Gunner leans back and plants his feet firmly on the ground on either sides of the bench. A motivated look covers his face as he adjusts the positions of his grip down to the millimeter and takes a few deep breaths."
    n "His body tenses up and his fur stands on end moments before he arches his back and pushes that bar upward with a grunt, smooth and steady like a rocket ascending."
    
    gunner "See? Easy!"
    
    n "He gently places the bar back on the rack and slides out from under it."
    
    gunner "Your turn! Show me what you've got!"
    
    menu:
        "I haven't even stretched yet!":
            player "Wha? I haven't even stretched yet!"
            
            gunner "Psh, excuses excuses."
            gunner "Go on then, do your stretches."
            
            player "Right. My stretches. That I totally know how to do."
            
            n "You dig through your repository of fitness knowledge and come back with a stretch you remember doing at one point in your life."
            n "It feels kind of awkward to do in public. Is someone gonna stare at your ass while you do this?"
            n "Let's just get this over with quickly. You bend at your waist and try touching your toes with your fingertips."
            n "Almost... almost... Come on, they're right there!"
            
            gunner "Dude, what are you doing?"
            
            player "Uh, touching my toes? Is that a stretch?"
            
            gunner "What part of bench pressing involves stretching like that?"
            
            player "...Getting up at the end?"
            
            gunner "*Sigh*"
            gunner "You're clearly new to this. Come on, lemme show you some warm up stretches."
            
            n "Gunner takes you to a different area out of the way of others and gets you started on some of the basics."
            n "Obviously his feline body is able to contort itself better than yours but at least you learn a few things."
            n "Your muscles come to life with increased blood flow and you feel energized enough to lift something heavy."
            n "Returning to the bench press, you actually manage to knock out a solid number of reps... after taking half the weights off of course."
            
            gunner "Whoa! Color me impressed!"
            
            n "You rack the barbell and sit up, panting."
            
            player "Hey that was... kinda fun?"
            player "Lemme do it again!"
            
            gunner "That's the spirit!"
            
            n "You and Gunner take turns lifting until you're both worn out."
            
            gunner "Whew, how about we call it a day? I'm beat."
            
            player "Yeah, that's enough for today. I'm gonna be sore all week."
            player "How long until I start seeing some gains?"
            
        "Try to lift it":
            n "How hard can it be? You just have to go beast mode and lift some plates, no big deal."
            n "You get underneath the bar, lining it up at about shoulder level then gripping the cold metal that doesn't budge at all as you adjust your grasp on it."
            n "Alright, here goes... You push upwards, feeling the force of the weights dig into your hands, yet they refuse to move."
            n "Harder! You engage more of your arm muscles and feel one end begin to rise up off the rack. You hold your breath and force your other arm upward to get the bar completely off the rack."
            n "You just now realize your hands aren't spaced correctly, making one side heavier than the other and throwing you off balance."
            n "And now that it's away from the guards, you notice you used all your strength getting into this position."
            n "The bar begins to sink towards your chest. Gunner cheers you on, seemingly unaware that you are losing this fight against gravity."
            
            gunner "That's it! Down then up! Up! Don't you know which way up is?"
            
            n "After letting you struggle trying to keep 200 pounds of steel from caving your chest in, Gunner decides to lend a helping paw and pull it off you."
            n "You don't feel safe until the barbell is on the rack for a few seconds, then you ease off and let your arms ragdoll down."
            
            gunner "Jeez dude, you alright? I thought you would have been able to lift that."
            
            player "I did too. Is that a bit much for a total noob?"
            
            gunner "This your first time?"
            gunner "Yeahhhh we should have started you off on some smaller plates."
            
            player "I think I'm done for today."
            
            gunner "No problem, we'll get you off to a better start next time."
            
            player "How long until I start seeing some gains?"
            
        "Take some plates off":
            n "There's no way you're lifting all that. You start by taking one plate off each side while Gunner snickers at you."
            n "Fuck these are heavy. You're not even sure you'll be able to lift the bar after taking half the weight off."
            n "You get underneath the bar, lining it up at about shoulder level then gripping the cold metal."
            n "You gradually apply force to it and at some point it suddenly rises off the rack."
            n "It's actually not that hard just keeping it in the air with your arms extended like this."
            
            gunner "Well? Do a few reps already!"
            
            n "Oh right, you actually have to move the barbell to get those gains."
            n "Your arms begin to shake as you ease it down to your chest. With some effort, you manage to push it all the way back up again."
            n "You don't feel worn out yet, so you try another. Your arms begin to shake but you can do at least one more."
            n "Grunting and breathing hard, you just barely manage to get the bar on the rack again after 3 reps."
            
            player "Hah...hah... how's that?"
            
            gunner "Not bad... for a start."
            gunner "Go drink some water then come back for another set."
            
            n "What?! You have to do it again?? Is he trying to kill you?"
            n "After a rest, you go at it again but you don't fare any better than before. In fact you gradually get worse until you can no longer lift the bar at all."
            n "Gunner seems to consider this a success however."
            
            gunner "Nice going! Feels great, doesn't it?"
            
            player "Is this supposed to make me want to kill myself?"
            
            gunner "Only until you start seeing some gains."
        
            player "And how long will that take?"
            
    gunner "A couple months."
    
    player "Oh my fucking god."
    
    gunner "You should stick with it! You won't regret it!"
    
    player "Ugh. I can't promise I'll be here every day, just when I have nothing better to do."
    
    gunner "Yay!!!"
    gunner "I'm so glad to have a new workout buddy!"
    gunner "Let's do some cooldown stretches then go get something to eat!"
    
    n "You dread having to do any more physical work but the thought of food entices you to just do it and get it over with."
    
    return

label linaTown:
    #remove linaTown from townEvents list, maybe add linaTown2 if there will be a scene for that later
    $ townEvents.remove("linaTown")
    "lina town scene"
    return

label celestineTown:
    $ townEvents.remove("celestineTown")
    "celestine town tea scene"
    return
    
label celestineEllenTown:
    $ townEvents.remove("celestineEllenTown")
    "ellen and celestine town scene"
    return
    
    


label roseCafe:
    "rose cafe scene"
    return


label roriCafe:
    "rori cafe scene"
    return


label gunnerCafe:
    "gunner cafe scene"
    return


label mishkaCafe:
    "mishka cafe scene"
    return


label claireCafe:
    "claire cafe scene"
    return


label avaCafe:
    "ava cafe scene"
    return


label trishCafe:
    "trish cafe scene"
    return


label ellenCafe:
    "ellen cafe scene"
    return


    
label deanCafe:
    "dean cafe scene"
    return


label avaGunnerNight:
    "ava and gunner night scene"
    
    return


label roriNight:
    "rori night scene"
    
    return


label roseNight:
    "rose night scene"
    
    return


label mishkaNight:
    "mishka night scene"
    
    return


label claireNight:
    "claire night scene"
    
    return

label avaNight:
    "ava night scene"
    
    return
    
    
label gunnerNight:
    "gunner night scene"
    
    return
    
label generateWeather:
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
    

    return