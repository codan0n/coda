label afterClassOptions:
    "What would you like to do?"
    
    menu:
        "Go somewhere":
            "Where do you want to go?"

            menu:
                "Explore" if trackDiscovered == False or arboretumDiscovered == False or townDiscovered == False or forestDiscovered == False: #if locationsAvailable == False:
                
                    $ randomSelected = renpy.random.choice(afterClassExploration)
                    
                    call expression randomSelected
                
                "Town" if townDiscovered == True:
                    #if there are town events available, do one and then return to dorm for the night. If not, play a generic scene and let the player choose another location
                    
                    if townEvents = True:
                        $ randomSelected = renpy.random.choice(townEvents)
                        
                        call expression randomSelected
                        
                    else:
                        "You wander around town but don't find anything interesting to do."
                        
                        jump afterClassOptions
                "Track" if trackDiscovered == True:
                    if trackEvents = True:
                        $ randomSelected = renpy.random.choice(trackEvents)
                        
                        call expression randomSelected
                        
                    else:
                        "You wander around the fitness area but don't find anything interesting to do."
                        
                        jump afterClassOptions
                
                "Forest" if forestDiscoverd == True:
                    if forestEvents = True:
                        $ randomSelected = renpy.random.choice(forestEvents)
                        
                        call expression randomSelected
                        
                    else:
                        "You wander around the forest but don't find anything interesting to do."
                        
                        jump afterClassOptions
                
                "Arboretum" if arboretumDiscovered == True:
                    if arboretumEvents = True:
                        $ randomSelected = renpy.random.choice(arboretumEvents)
                        
                        call expression randomSelected
                        
                    else:
                        "You wander around the arboretum but don't find anything interesting to do."
                        
                        jump afterClassOptions
                "Cafe":
                    if cafeEvents = True:
                        $ randomSelected = renpy.random.choice(cafeEvents)
                        
                        call expression randomSelected
                        
                    else:
                        "You get something to snack on at the cafe but don't find anything interesting to do."
                        
                        jump afterClassOptions
                    
                "Go back":
                    "jump afterClassOptions"
        "Study at dorm":
            "you go back to your dorm to study"
            
    return
    
label nightWalks:
    "You decide to go out for the night."
    
    $ randomSelected = renpy.random.choice(nightEvents)
    
    
    return

label mishkaArboretum:

    return
    
label avaArboretum:

    return
    
label claireForest:

    return
    
label roseForest:

    return

label roriTrack:

    return
    

label gunnerTrack:
    #check if gunnerTrack number x has been seen yet and play the next one. Use a day counter to prevent this scene from being able to be played 2 days in a row
    
    $ gunnerTrackNumber += 1
    
    
    
    return

label linaTown:
    #remove linaTown from townEvents list, maybe add linaTown2 if there will be a scene for that later
    $ townEvents.remove("linaTown")

    return

label celestineTown:
    $ townEvents.remove("celestineTown")

    return
    
label celestineEllenTown:
    $ townEvents.remove("celestineEllenTown")
    
    return
    
    


label roseCafe:

    return


label roriCafe:

    return


label gunnerCafe:

    return


label mishkaCafe:

    return


label claireCafe:

    return


label avaCafe:

    return


label trishCafe:

    return


label ellenCafe:

    return


    
label deanCafe:

    return


label avaGunnerNight:

    
    return


label roriNight:

    
    return


label roseNight:

    
    return


label mishkaNight:

    
    return


label claireNight:

    
    return

label avaNight:

    
    return
    
    
label gunnerNight:

    
    return