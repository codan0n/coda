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
    #50% chance for generic scene, 50% chance for specific one if there are any available. Can choose who to hang out with if you've done first part of their arc?
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
    return
    

label gunnerTrack:
    #check if gunnerTrack number x has been seen yet and play the next one. Use a day counter to prevent this scene from being able to be played 2 days in a row
    
    #$ gunnerTrackNumber += 1
    "gunner track scene"
    
    
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