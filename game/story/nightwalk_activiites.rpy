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
    
    scene bg campus with fade
    
    show box with Dissolve(.2):
        ypos 0
    
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
    
    show ava typical happy at center:
        ypos y_ava
        xoffset -300
        xzoom -1
    show gunner neutral at center:
        ypos y_gunner
        xoffset -670
        xzoom -1
    
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
                    
                    n "Ava is silent but this argument has clearly put a damper on her mood."
                    n "You all stand around quietly until one of you makes up an excuse to go back to your dorm and the others follow suit."
                    
                "Gain respect for Gunner":
                    n "Sounds like he's got a lot more going on than he shows on the surface."
                    n "He may have just acted like a whiny baby in front of his crush, but it took guts to say what's on his mind."
                    
                    player "Y'know, I thought you were just a scumbag dudebro with daddy's money, but maybe you're onto something. Maybe you are a real feline being."
                    
                    gunner @ say "I can be both!"
                    
                    player "A real hustler but a genuine sensitive guy underneath."
                    
                    ava @ say "Aww~"
                    
                    player "Like the kind Rori talks about."
                    
                    gunner @ say "Hey whoa slow down there bucko. That's my roommate you're talking about."
                    
                    ava @ say "Huh? Is Rori into sensitive guys?"
                    ava @ say "Do I have *more* competition to deal with?"
                    
                    gunner @ say "What? No! It's not like that at all!"
                    
                    player "I dunno bro, it's kinda sus that you two sleep in the same room."
                    
                    gunner @ say "H-hey it's not like that at all!"
                    
                    player "And what's all this about being room \'mates\'?"
                    
                    ava @ say "Snrk"
                    ava @ say "Alright I think that's enough teasing, boys~"
                    ava @ say "Let's all just get along now, k?"
                    
                    gunner @ say "Yeah yeah, great bants [name]."
                    
                    player "Thanks. No hard feelings?"
                    
                    gunner @ say "Nah we chill, homie."
                    
                    n "You walk along with Gunner and Ava, cracking dumb jokes until you all become too tired to continue."
                
                    
        "Let it go":
            player "Nothing. Forget it."
            
            gunner @ say "Huh. That's what I thought."
            
            n "Ava chimes in to relieve the tension."
            
            ava @ say "Hey, would you like to walk with us, [name]? You and Gunner bounce off each other so well, it's always fun conversation!"
            
            player "We do?"
            
            gunner @ say "You bet! I'm like the suave schemer and you're the relatable everyman. It's a classic comedy pairing!"
            
            player "Thanks? It sounded like you just called me boring but okay."
            
            gunner @ say "That's exactly what the average ordinary guy would say!"
            
            n "Ava giggles at your impromptu comedy routine."
            
            ava @ say "Oh you two are such a handful~"
            ava @ say "Whatever will I do with you?"
            
            player "This either ends in heartbreak or a threesome."
            
            gunner @ say "There's your signature dry humor! We should do standup!"
            
            player "I agree! Cause I'm not gonna take all your shit lying down!"
            
            ava @ say "Oh boy, here come the puns."
            
            gunner @ say "Yeah [name], think of the poor translators who will have to make that make sense in another language."
            
            player "Sorry, I should have known it'd be hard for them to come up with worse jokes than ours."
            #player "They could come up with an original joke, but they'll have a hard time coming up with ones worse than ours."
            
            ava @ say "They're so bad they're good."
            
            n "You walk along with Gunner and Ava, cracking dumb jokes until you all become too tired to continue."
            
            
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
            
            gunner @ say "And this has nothing to do with your serial killer fetish?"
            
            ava @ say "It's not a fetish!"
            
            player "I've heard this one before. Next she'll say it's \'a lifestyle.\'"
            
            ava @ say "Oh shush you!"
            
            show ava typical unimpressed 
            
            ava @ say "I'm sure you guys masturbate to weirder stuff."
            
            menu:
                "Yeah, I do":
                    player "Actually I do. That's not a problem, is it?"
                    
                    ava @ say "I don't even wanna know what you jerk off to if it's worse than serial killers."
                "No, I don't":
                    show ava typical embarrassed
                    show gunner displeased
                
                    player "I don't actually. HMOFA is less weird than getting off to serial killers."
                    
                    ava @ say "HMOFA? What is that?"
                    
                    player "Human male on female anthro."
                    
                    ava @ say "O-oh gosh! I didn't know you were into that stuff!"
                "Nofap":
                    player "I'm on nofap actually. I didn't know you were such a degenerate."
                    
                    ava @ say "Rude!"
            
            gunner @ say "Never goon."
            
            n "You reflect on Gunner's wise words as you walk alongside him and Ava, bantering about random topics until you become too sleepy to continue and you all return to your dorms."

    return
    
label avaNightWalkLvl2:
    
    
    n "ava night walk part 2"

    return

label avaNightWalkLvl3:
    scene bg track with fade
    
    n "rose night walk part 3"

    return
    
    
label claireNightWalkLvl1:
    #find claire geocaching. she does it at night so nobody sees her and finds the caching spots
    #she shows you one in a sewer drain and one in a dead street lamp
    
    n "Bumbling around in the night sure is fun. You never know who you might bump into."
    n "Literally."
    n "You trip over something low to the ground, but instead of chipping your teeth on the asphalt below, you land on something incredibly soft."
    n "And large."
    
    claire @ say "Oh my, [name], right here in the middle of the street?~"
    
    n "You found yourself on top of Claire, who was crouched on all fours for some reason."
    n "You roll off of her and turn on your phone's flashlight."
    n "She appears to have her arm buried in a storm water drain on the side of the street."
    
    player "Claire? What are you doing down there at this hour?"
    
    claire @ say "Shhshshsh! Turn that light off or everyone will see!"
    
    n "You oblige her and turn off your light."
    
    player "What's all this about?"
    
    claire @ say "Aha! Got it!"
    
    n "You hear the scraping of metal against concrete as Claire pulls a small box out from the drain."
    
    player "What is that?"
    
    claire @ say "It's a box!"
    
    n "She pops the latches up and opens the box. You're half expecting there to be a severed hand or something equally creepy inside."
    n "But it turns out to just be a bunch of random junk and some scraps of paper."
    
    player "Who's box is this?"
    
    claire @ say "No one's!"
    
    player "Why was it in the drain?"
    
    claire @ say "Because someone put it there!"
    
    player "Why is it full of junk?"
    
    claire @ say "People put whatever they happen to have in here!"
    
    player "...Why?"
    
    claire @ say "That's what geocaching is all about!"
    
    player "Geocaching?"
    
    claire @ say "Yeah! You know, geographical caching."
    
    player "But why??????"
    
    n "Claire pulls a bead bracelet out from her pocket and deposits it into the box."
    
    claire @ say "It's like a game! You gotta find the box and your reward is a little trinket to put in the next box!"
    claire @ say "See anything you want?"
    
    n "She holds the box up to your face. What catches your eye are some toy army men, trading cards, bottlecaps, a rubber duck."
    n "Which should you take?"
    
    menu:
        "Army men":
            n "You pick up one of the based army dudes holding a rifle over his head like he's crossing water."
            n "He was probably on his way to commit war crimes in some third world country but got taken prisoner in that box for who knows how long."
            #n "Don't worry little guy, you can live out the rest of your life in peace and get your domestic abuse charges dropped and classified as PTSD incidents."
            
            n "You pocket the trinket and turn to Claire."
            
            player "Okay, now what?"
                    
            claire @ say "Now as proof of our achievement..."
            
            n "She picks up the pencil that was in the box and unfolds a sheet of paper. Scrawled on it are various names and dates."
            n "These must be the people who found this cache and when."
            n "She writes her name as well as yours on it, dates it, then folds it back up and closes the box before returning it to its original position."
            
            claire @ say "Whew, wasn't that fun!"
            
            player "I don't know? I just got here and now I have a plastic army man."
            
        "Trading cards":
            n "The cards are of the common variety but they're pretty old. You might even say vintage."
            n "Oh god no don't call them that, these are the same cards you had when you were like 5. You're not vintage yet."
            n "You've seen the prices some of the cards from this generation go for nowadays but these are just the filler cards they filled half the packs with."
            
            n "You pocket the trinket and turn to Claire."
            
            player "Okay, now what?"
                    
            claire @ say "Now as proof of our achievement..."
            
            n "She picks up the pencil that was in the box and unfolds a sheet of paper. Scrawled on it are various names and dates."
            n "These must be the people who found this cache and when."
            n "She writes her name as well as yours on it, dates it, then folds it back up and closes the box before returning it to its original position."
            
            claire @ say "Whew, wasn't that fun!"
            
            player "I don't know? I just got here and now I have some old trading cards."
        
        "Bottlecaps":
            n "You scoop up a handful of bottlecaps. Some of them have jokes on the underside, some are blank."
            n "One of them has the soda company's logo that they haven't used in like 50 years. This one has gotta be worth more than 5 cents at least."
            
            n "You pocket the trinket and turn to Claire."
            
            player "Okay, now what?"
                    
            claire @ say "Now as proof of our achievement..."
            
            n "She picks up the pencil that was in the box and unfolds a sheet of paper. Scrawled on it are various names and dates."
            n "These must be the people who found this cache and when."
            n "She writes her name as well as yours on it, dates it, then folds it back up and closes the box before returning it to its original position."
            
            claire @ say "Whew, wasn't that fun!"
            
            player "I don't know? I just got here and now I have a vintage bottle cap."
        
        "Rubber duck":
            n "Rubber duck my beloved..."
            n "This cold hard box is no place for you. You belong in a warm bubble bath."
        
            n "You pocket the trinket and turn to Claire."
            
            player "Okay, now what?"
                    
            claire @ say "Now as proof of our achievement..."
            
            n "She picks up the pencil that was in the box and unfolds a sheet of paper. Scrawled on it are various names and dates."
            n "These must be the people who found this cache and when."
            n "She writes her name as well as yours on it, dates it, then folds it back up and closes the box before returning it to its original position."
            
            claire @ say "Whew, wasn't that fun!"
            
            player "I don't know? I just got here and now I have a rubber duck."
            
    player "Why did we have to do this in darkness again?"
    
    claire @ say "It's like hide and seek! If we found the cache when everyone could see us, then everyone would know its location!"
    claire @ say "Hmm, how about we do another one? Then you can join me for the full adventure!"
    
    player "Do I have a choice?"
    
    claire @ say "Nope!"
    
    n "Claire grabs your hand and rushes you along the campus streets. You can barely keep up with her excited hopping."
    n "You wind up at the school's running track, where half the area is illuminated by large stadium lights."
    
    claire @ say "Okayokayokay so someone hides a cache and then posts the approximate GPS coordinates for it online and then geocachers go out and find it!"
    
    player "That's it? So it really is just hide and seek but with an inanimate object."
    
    claire @ say "Yup! It's a lot of fun actually and gets you exploring~"
    claire @ say "The coordinates say it's somewhere in this area. There's a lot of places it could be hidden though! Any idea where we should start looking?"
    
    $ checkedBleachers = False
    $ checkedLamp = False
    $ checkedShed = False

label cachingHunt1:
    if checkedBleachers == False or checkedLamp == False or checkedShed == False:
        menu:
            "Bleachers" if checkedBleachers == False:
                $ lastChecked = "bleachers"
                $ checkedBleachers = True
                
                player "Let's check under the bleachers. There's tons of places you could hide a small box and it would blend right in."
                
                claire @ say "Good thinking! You take the one on the right and I'll check the one on the left."
                
                n "That'll make things faster but with only one pair of eyes, you might overlook the box. Using your phone as a flashlight, you slink around to the back side of the bleachers and commence your search."
                n "Wind rattles the thin aluminum seats. It feels like the whole thing will collapse onto you at any moment."
                n "All the shadows from the stands dance as you move your light source around, making it hard to look for anything."
                n "You scan the ridges under the seats but come up empty."
                n "After looking over everything twice, Claire returns to you from across the field."
                
                claire @ say "Find anything yet?"
                
                player "Nothing."
                
                claire @ say "Dang. Wanna try looking somewhere else?"
                
                jump cachingHunt1
            "Lamp posts" if checkedLamp == False:
                $ lastChecked = "lamp"
                $ checkedLamp = True
                
                player "How about the around lamp posts?"
                
                claire @ say "Good idea! Sometimes they have covers at the base you can lift up and hide things in."
                claire @ say "You go that way along the track and I'll go this way so we each only have to check half of them."
                
                player "K. Meet you at the other end of the track."
                
                n "You head in the opposite direction of Claire, inspecting every lamp post along the way."
                n "Just as Claire said, some of them have a shroud covering some wires that you can just lift up."
                n "No geocaching boxes to be found however."

                claire @ say "You find it??"
                
                player "Nope."
                
                claire @ say "Aaargh!"
                claire @ say "Got any other ideas?"
                
                jump cachingHunt1
            "Equipment shed" if checkedShed == False:
                $ lastChecked = "shed"
                $ checkedShed = True
                
                player "That equipment shed probably has some good hiding spots."
                
                claire @ say "Agreed! Non-cachers would probably just think it's supposed to be there if they did stumble upon it."
                
                player "Can we even get inside? It's probably locked up at night."
                
                n "Claire bends down and hoists the garage door up."
                
                claire @ say "You were saying?~"
                
                n "Judging by the screeching of the door, it probably was locked. These doors just aren't built to withstand the bnnuy though."
                n "You and Claire begin rummaging through the various pieces of equipment in the shed."
                n "It reeks of gasoline and grass clippings thanks to the lawnmower that's stored here. You cover your nose and dig around in every place that could conceal a box."
                
                claire @ say "I don't think it's in here."
                
                player "Yeah, I don't see anywhere it could be."
                
                claire @ say "Wanna try looking somewhere else?"
                
                player "Yeah let's get out of here."
                
                n "Claire yanks on the garage door and pulls it down after you step outside."
                
                jump cachingHunt1
        
    if lastChecked == "bleachers":
    
    
        
    elif lastChecked == "lamp":
    
    
        
    elif lastChecked == "shed":
        n "As you're "
    
    
    
    
    claire @ say "When we were talking about hobbies earlier it got me thinking I need a new one! So I looked up hobbies and this was one I hadn't tried!"
    
    n "She's really happy to have something new to do."
    n "She'd probably love to do this again with you."
    
    claire @ say "This was a lot of fun!"
    claire @ say "I'd love to do this again with you!"
    
    
    
    
    

    return
    
label claireNightWalkLvl2:
    #underside of the campus fountain statue
    
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
    #rori climbs stuff due to his instincts, but only does it at night where he's less likely to be caught. He get paranoid and jumpy when the player discovers him, but offers to teach you how to climb

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
    
    
