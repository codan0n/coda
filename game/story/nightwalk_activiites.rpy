###nightwalk events

label roseNightWalkLvl1:
    scene bg campus with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Ah, the outdoors gym. It's emptiness is eerie at night."
    n "Stadium lights illuminate some sections of the track but leave others in darkness."
    n "You're compelled to wander on to it, to walk in circles mindlessly like a hamster on a wheel."
    n "You kick a pebble along until it gets lost in the dark."
    
    show rose athletic furious at offscreenright:
        ypos y_rose
        xzoom -1
        
    n "The same pebble suddenly flies back at you, pelting your shin before a figure emerges into the light at high speed."
    
    rose @ say "Outta the way!"
    
    pause .1
        
    show rose at offscreenleft with move:
        ypos y_rose
    
    n "Some gremlin type creature barrels past you, visible for only a brief moment before disappearing into the vast darkness from whence she came."
    
    show rose at offscreenright:
        ypos y_rose
    
    rose @ say "You're going the wrong way, retard!"
    
    n "You look down at the track. Indeed, painted on the surface are arrows indicating which direction to travel."
    n "You put your hands in your pockets and sheepishly turn around, acting like you were going this way all along. You won't let someone gaslight you into thinking you weren't."
    n "Eventually the gremlin laps back around and you get a better look at it."
    n "It turns out to be your history project partner!"
    
    pause .1
    
    show rose at center with move:
        ypos y_rose
    
    menu:
        n "{cps=0}It turns out to be your history project partner!{/cps}"
        "Be polite":
            n "Heya Rose! I love the new outfit! What are you doingout so late?"
        "Call her a slur":
            player "Well if it isn't the trashiest of pandas! What are you doing out so late?"
        "Politely call her a slur":
            player "Hi Rose! What's the least trashy trash panda I know doing out so late?"

    rose @ say "What does it look like? I'm running."
    
    player "Hey that's cool. Running and stuff. Y'know humans can run too. We're like the best at it too. Endurance hunters and all that."
    
    rose @ say "Psh yeah whatever."
    
    n "Rose scoffs and speeds along, vanishing from your sight."
    
    menu:
        "Try and catch up to her":
            n "You're not properly dressed for this but you can easily catch up to her. Probably."
            n "Slowly accelerating your gait, you start to jog, then go into a run."
            n "At this point you're matching Rose's speed but you had such a late start you'll never catch up. Your only option is to sprint."
            n "With a quick lunge forward, you take long strides, practically leaping forward with each step."
            n "Oh no."
            n "It suddenly hits you how out of shape you are. The first few steps were nearly effortless but the moment you need to take a breath, you're done for."
            n "Gasping for air, you feel your body drained of energy and your sprint slows to a pitiful shamble."
            
        "Wait for her to lap around":
            n "She runs pretty fast and you haven't stretched or anything. You're not even wearing the right clothes to be running anyway."
            n "You'll just wait for her to come back around to continue your conversation."



    
    
    return
    
label roseNightWalkLvl2:
    scene bg track with fade
    
    #you brought running clothes with you this time, rose tells you you have bad form. you adjust and try catching up to her but just fail
    
    n "rose night walk part 2"

    return

label roseNightWalkLvl3:
    scene bg track with fade
    
    #run alongside rose and she's a little impressed
    
    n "rose night walk part 3"

    return
    
    
label gunnerNightWalkLvl1:
    n "gunner nightwalk part 1"

    return
    
label gunnerNightWalkLvl2:
    
    
    n "gunner night walk part 2"

    return

label gunnerNightWalkLvl3:
    
    
    n "gunner night walk part 3"

    return
    
    
label avaNightWalkLvl1:
    #
    
    n "ava nightwalk part 1"
    

    return
    
label avaNightWalkLvl2:
    
    
    n "ava night walk part 2"

    return

label avaNightWalkLvl3:
    scene bg track with fade
    
    n "rose night walk part 3"

    return
    
    
label claireNightWalkLvl1:
    
    
    n "claire nightwalk part 1"
    

    return
    
label claireNightWalkLvl2:
    
    n "claire night walk part 2"

    return

label claireNightWalkLvl3:
    
    
    n "claire night walk part 3"

    return
    
    
label ellenNightWalkLvl1:
    
    
    n "ellen nightwalk 1"

    return
    
label ellenNightWalkLvl2:
    
    
    n "ellen night walk part 2"

    return

label ellenNightWalkLvl3:
    
    
    n "ellen night walk part 3"

    return
    
    
label roriNightWalkLvl1:
    n "rori nightwalk 1"
    
    return
    
label roriNightWalkLvl2:
    
    n "rori night walk part 2"

    return

label roriNightWalkLvl3:
    
    
    n "rori night walk part 3"

    return
    
    
label mishkaNightWalkLvl1:
    n "mishka nightwalk 1"

    return
    
label mishkaNightWalkLvl2:
    
    n "mishka night walk part 2"

    return

label mishkaNightWalkLvl3:
    
    
    n "mishka night walk part 3"

    return
    
    
