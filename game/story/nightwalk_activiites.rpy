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
            n "You're still breathing heavily when Rose laps back around."
            
            rose @ say "Wow that was pathetic. You look like you're dying."
            
            n "You flash her an \"OK\" symbol with your hand because you're too winded to talk."
            
            rose @ say "You should just kill yourself now and save yourself further embarrassment."
            
            n "You give her a thumbs up and watch as she jogs another lap."
            n "Maybe you should practice more, then she'll be impressed."
            n "You think you've had enough for tonight. Time to head back to your dorm and get some rest."
            
        "Wait for her to lap around":
            n "She runs pretty fast and you haven't stretched or anything. You're not even wearing the right clothes to be running anyway."
            n "You'll just wait for her to come back around to continue your conversation."
            n "Oh here she comes."
            
            player "You come here often?"
            
            rose @ say "Only when no one else is around."
            
            player "I get it, I'm shy about working out in front of people too. Probably why I don't go to the gym much."
            
            rose @ say "..."
            
            player "Hey, you wanna be running partners?"
            
            rose @ say "No."
            
            n "She runs ahead, leaving you in the dust."
            n "Maybe you should practice running, then she'll be impressed."
            n "You think you've had enough for tonight. Time to head back to your dorm and get some rest."

    
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
    # see ava and gunner walking together, flirting. They're surprised to see you.
    
    n "Walking through the campus at night almost kinda feels like you're breaking and entering, even though it's technically your own home."
    n "It just feels like a place where you're not supposed to be, like any building after operating hours."
    n "That doesn't stop the occasional hooligan from slinking around and howling at random intervals."
    n "You even hear the odd bird chirping despite it being well past their bed time."
    n "Speaking of birds, a familiar voice bounces off the brick walls and into your ears."
    
    ava @ say "Hehehe you're actually kinda funny when you're not being misogynistic or bragging about being rich!"
    
    gunner @ say "Thank you, I try my best to be all three of those things."
    
    ava @ say "I didn't think a guy like you would be so into art either!"
    
    gunner @ say "Well when your house is lined with Van Gogh originals..."
    gunner @ say "Hey, is that who I think it is?"
    
    ava @ say "What are the odds!"
    
    show ava typical happy
    show gunner neutral
    
    gunner @ say "Sup [name]!"
    
    ava @ say "Hii [name]! What are you doing out so late?"
    
    player "Hey guys. I just couldn't sleep so I went out for a walk. Then I overheard you two uh... chatting."
    
    ava @ say "O-oh yeah? Just how much did you hear?"
    
    player "Not much, just that Gunner's an art guy now apparently."
    
    gunner @ say "You know it! I was telling Ava earlier about how much I admire Ansel Adams' deep contrast in his black and white photography."
    
    ava @ say "Truly a pioneer!"
    
    player "Riiiight. Are you sure you didn't just look up who the most famous photographer is 5 minutes before your little hangout?"
    
    gunner @ say "What are you trying to say, bro?"
    
    menu:
        "Chastise him":
            player "That you're a manipulative fraud who's only personality is having money."
            
            gunner @ say "Spoken like a true poor. You let your jealousy blind you to the fact that I'm a real person with real beliefs, ideas, and values."
            
            ava @ say "Hey, Gunner..."
            
            gunner @ say "You and everyone else thinks that just because I'm free from being a debt slave that I gotta be the villain huh? Well newsflash pal, even with your dollar store sneakers you're still richer than 99\% of the planet!"
            
            ava @ say "Maybe chill out a bit..."
            
            gunner @ say "So get over the fact that I'm more popular, taller, more fit, and more ambitious than you, cause money doesn't buy any of that!"
            
            menu:
                "Lose respect for Gunner":
                    n "Wow he really blew up on you out of nowhere. Kinda cringe."
                    
                    player "Dude you need to calm down. I was just bantering and you turned it into a personal attack."
                    
                    gunner @ say "Well maybe I'm sick of people misinterpreting my entire character when I have more depth than all the NPCs around here!"
                    gunner @ say "Everyone dogpiles on me because rich man bad but no one cares to see me for who I really am!"
                    
                    player "Maybe because you're an asshole."
                    
                    gunner @ say "Hey, do I not always try to include everyone and have a good time? Did I not try and be best bros with you?"
                    gunner @ say "Just because I can be crass sometimes doesn't mean I'm invalid as a person."
                    
                    player "Save it for your therapist."
                    
                    gunner @ say "Man, I thought you were a lot cooler, [name]."
                    gunner @ say "Why'd you have to prove me wrong?"
                    
                "Gain respect for Gunner":
                    n "Sounds like he's got a lot more going on than he shows on the surface."
                    n "He may have just acted like a whiny baby in front of his crush, but it took guts to say what's on his mind."
                    
                    player "Y'know, I thought you were just a scumbag dudebro with daddy's money, but maybe you're onto something. Maybe you are a real feline being."
                    
                    gunner @ say "I can be both."
                    
                    
                    
                    
                    
                
                    gunner @ say "Hustlers hustle!"
        "Let it go":
            player "Nothing."
            
        "Name a more obscure artist":
            player "I'm just saying Van Gogh and Ansel Adams are like babies first artists."
            player "Now Ray Metzker? That was a true photographer. He could really tell a story and evoke a feeling without resorting to snapshots of natural landscapes from a high vantage point"
            player "With his more abstract and tesselated works, I think he'd be more your style, Ava."
            
            ava @ say "Yeah, creating something new from composites is pretty cool."
            
            gunner @ say "Well, Metzker was good at transforming the real into fantastical mirages, but if you're talking about true photographers, look no further than Robert Landsburg."
            gunner @ say "Dude was literally dying in a volcano and still taking shots. What a legend."
            gunner @ say "What would you like your final photo to be? I'd want it to be me getting attacked by a great white shark."
            
            menu:
                "Something paranormal":
                    player "I dunno, I guess something paranormal."
                    player "Like that unsolved case where that lady ended up in the rooftop water tower even though there's no way she could have gotten in there."
                "A natural disaster":
                    player "The volcano sounds cool but maybe I could get sucked into a tornado or something and take a shot in the air before some debris kills me."
                "Underwater caving":
                    player "Underwater caving death shots would be exciting. It'd probably take years to even recover the film."
                    player "People would make up urban legends about me and how the cave fish monster got me."
            
            player "What about you, Ava?"
            
            ava @ say "Well um...!"
            ava @ say "You know that one pic of that girl before she got murdered?"
            
            gunner @ say "No? Which one?"
            
            player "Oh yeah, I know the one. Where she's standing on like a pier and holding her arms out and stepping back?"
            
            ava @ say "Yeah that one!"
            
            gunner @ say "So you wanna be murdered?"
            
            ava @ say "I don't *want* to be murdered! That wasn't the question!"
            ava @ say "I'm just saying it would be a really good photo just for the story!"
            
            

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
    
    
