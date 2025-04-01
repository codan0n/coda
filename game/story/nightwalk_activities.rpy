###nightwalk events

label roseNightWalkLvl1:
    scene bg campus summer night clear with fade
    
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
    
    show rose athletic dismissive at center with move:
        ypos y_rose
    
    menu:
        n "{cps=0}It turns out to be your history project partner!{/cps}"
        "Be polite":
            n "Heya Rose! I love the new outfit! What are you doing out so late?"
        "Call her a slur":
            player "Well if it isn't the trashiest of pandas! What are you doing out so late?"
            
            show rose athletic furious
        "Politely call her a slur":
            player "Hi Rose! What's the least trashy trash panda I know doing out so late?"
            
            show rose athletic furious

    rose @ say "What does it look like? I'm running."
    
    player "Hey that's cool. Running and stuff. Y'know humans can run too. We're like the best at it too. Endurance hunters and all that."
    
    show rose athletic dismissive lookingaway
    
    rose @ say "Psh yeah whatever."
    
    pause .2
    
    show rose at offscreenleft with move:
        ypos y_rose
    
    n "Rose scoffs and speeds along, vanishing from your sight."
    
    show rose at offscreenright:
        ypos y_rose
    
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
            
            pause .1
    
            show rose athletic dismissive -lookingaway at center with move:
                ypos y_rose
            
            rose @ say "Wow that was pathetic. You look like you're dying."
            
            n "You flash her an \"OK\" symbol with your hand because you're too winded to talk."
            
            show rose athletic irritated
            
            rose @ say "You should just kill yourself now and save yourself further embarrassment."
            
            pause .2
    
            show rose at offscreenleft with move:
                ypos y_rose
            
            n "You give her a thumbs up and watch as she jogs another lap."
            n "Maybe you should practice more, then she'll be impressed."
            n "You think you've had enough for tonight. Time to head back to your dorm and get some rest."
            
        "Wait for her to lap around":
            n "She runs pretty fast and you haven't stretched or anything. You're not even wearing the right clothes to be running anyway."
            n "You'll just wait for her to come back around to continue your conversation."
            n "Oh here she comes."
            
            show rose athletic dismissive -lookingaway at center with move:
                ypos y_rose
            
            player "You come here often?"
            
            show rose athletic furious
            
            rose @ say "Only when no one else is around."
            
            player "I get it, I'm shy about working out in front of people too. Probably why I don't go to the gym much."
            
            show rose athletic irritated
            
            rose @ say "..."
            
            player "Hey, you wanna be running partners?"
            
            show rose dismissive
            
            rose @ say "No."
            
            pause .2
    
            show rose at offscreenleft with move:
                ypos y_rose
            
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
    
    scene bg campus summer night clear with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Walking through the campus at night almost kinda feels like you're breaking and entering, even though it's technically your own home."
    n "It just feels like a place where you're not supposed to be, like any building after operating hours."
    n "That doesn't stop the occasional hooligan from slinking around and howling at random intervals."
    n "You even hear the odd bird chirping despite it being well past their bed time."
    n "Speaking of birds, a familiar voice bounces off the brick walls and into your ears."
    
    ava @ say "Hehehe you're actually kinda funny when you're not being misogynistic or flaunting your wealth!"
    
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
    with dissolve
    
    gunner @ say "Sup [name]!"
    
    show ava typical excited
    
    ava @ say "Hii [name]! What are you doing out so late?"
    
    show ava typical happy
    
    player "Hey guys. I just couldn't sleep so I went out for a walk. Then I overheard you two uh... chatting."
    
    show ava reaching concerned
    
    ava @ say "O-oh yeah? Just how much did you hear?"
    
    player "Not much, just that Gunner's an art guy now apparently."
    
    show gunner eyesclosed catface
    show ava typical shy
    
    gunner @ say "You know it!"
    
    show gunner determined
    
    gunner @ say "I was telling Ava earlier about how much I admire Ansel Adams' deep contrast in his black and white photography."
    
    show ava typical overjoyed
    show gunner optimistic
    
    ava @ say "Truly a pioneer in his field!"
    
    show gunner neutral
    
    player "Riiiight. Are you sure you didn't just look up who the most famous photographer is 5 minutes before your little hangout?"
    
    show gunner annoyed
    show ava typical concerned
    
    gunner @ say "What are you trying to say, bro?"
    
    menu:
        "Chastise him":
            player "That you're a manipulative fraud who's only personality is having money!"
            
            show gunner displeased
            
            gunner @ say "Spoken like a true poor. You let your jealousy blind you to the fact that I'm a real person with real beliefs, ideas, and values."
            
            show ava pose concerned
            
            ava @ say "Hey now, Gunner..."
            
            gunner @ say "You and everyone else thinks that just because I'm free from being a debt slave that I gotta be the villain huh? Well newsflash pal, even with your dollar store sneakers you're still richer than 99\% of the planet!"
            
            show ava reaching concerned
            
            ava @ say "Maybe chill out a bit..."
            
            gunner @ say "So get over the fact that I'm more popular, taller, more fit, and more ambitious than you, cause money doesn't buy any of that!"
            
            menu:
                "Lose respect for Gunner":
                    n "Wow he really blew up on you out of nowhere. Kinda cringe."
                    
                    player "Dude you need to calm down. I was just bantering and you turned it into a personal attack."
                    
                    gunner @ say "Well maybe I'm sick of people misinterpreting my entire character when I have more depth than all the NPCs around here!"
                    gunner @ say "Everyone dogpiles on me because rich man bad but almost no one cares to see me for who I really am!"
                    
                    player "Maybe because you're an asshole."
                    
                    gunner @ say "Hey, do I not always try to include everyone and have a good time? Did I not try and be best bros with you?"
                    gunner @ say "Just because I can be crass sometimes doesn't mean I'm invalid as a person."
                    
                    player "Save it for your therapist."
                    
                    show gunner itsover
                    
                    gunner @ say "Man, I thought you were a lot cooler, [name]."
                    gunner @ say "Why'd you have to prove me wrong?"
                    
                    #show ava profile concerned
                    
                    n "Ava is silent but this argument has clearly put a damper on her mood."
                    n "You all stand around quietly until one of you makes up an excuse to go back to your dorm and the others follow suit."
                    
                    hide gunner
                    hide ava
                    with dissolve
                    
                "Gain respect for Gunner":
                    n "Sounds like he's got a lot more going on than he shows on the surface."
                    n "He may have just acted like a whiny baby in front of his crush, but it took guts to say what's on his mind."
                    
                    player "Y'know, I thought you were just a scumbag dudebro with daddy's money, but maybe you're onto something. Maybe you are a real feline being."
                    
                    show gunner motivated
                    
                    gunner @ say "I can be both!"
                    
                    show ava typical happy
                    
                    player "A real hustler but a genuine sensitive guy underneath."
                    
                    show ava profile overjoyed
                    
                    ava @ say "Aww~"
                    
                    player "Like the kind Rori talks about."
                    
                    show gunner hissing
                    
                    gunner @ say "Hey whoa slow down there bucko. That's my roommate you're talking about."
                    
                    show ava typical shocked
                    show gunner neutral
                    
                    ava @ say "Huh? Is Rori into sensitive guys?"
                    
                    show ava typical embarrassed
                    
                    ava @ say "Do I have *more* competition to deal with?"
                    
                    show gunner uncomfy
                    
                    gunner @ say "What? No! It's not like that at all!"
                    
                    player "I dunno bro, it's kinda sus that you two sleep in the same room."
                    
                    gunner @ say "H-hey it's not like that at all!"
                    
                    player "And what's all this about being room \'mates\'?"
                    
                    show ava typical whimsical
                    
                    ava @ say "Snrk"
                    
                    show ava typical shy
                    
                    ava @ say "Alright I think that's enough teasing, boys~"
                    
                    show ava typical happy
                    
                    ava @ say "Let's all just get along now, k?"
                    
                    show gunner eyesclosed catface
                    
                    gunner @ say "Yeah yeah, great bants [name]."
                    
                    show gunner neutral
                    
                    player "Thanks. No hard feelings?"
                    
                    gunner @ say "Nah we chill, homie."
                    
                    show ava typical excited
                    
                    ava @ say "Good! Can't have my two favorite guys fighting like that!"
                    
                    show ava typical happy
                    
                    n "You walk along with Gunner and Ava, cracking dumb jokes until it gets too late out."
                
                    
        "Let it go":
            player "Nothing. Forget it."
            
            gunner @ say "Huh. That's what I thought."
            
            n "Ava chimes in to relieve the tension."
            
            show ava typical excited
            
            ava @ say "Hey, would you like to walk with us, [name]? You and Gunner bounce off each other so well, it's always fun conversation!"
            
            show ava typical happy
            show gunner disgusted
            
            player "We do?"
            
            show gunner charming
            
            gunner @ say "You bet! I'm like the suave schemer and you're the relatable everyman. It's a classic comedy pairing!"
            
            player "Thanks? It sounded like you just called me boring but okay."
            
            gunner @ say "That's exactly what the average ordinary guy would say!"
            
            show ava typical whimsical
            
            n "Ava giggles at your impromptu comedy routine."
            
            ava @ say "Oh you two are such a handful~"
            ava @ say "Whatever will I do with you?"
            
            player "This either ends in heartbreak or a threesome."
            
            show ava typical shy
            show gunner cheeky1
            
            gunner @ say "There's your signature dry humor! We should do standup!"
            
            player "I agree! Cause I'm not gonna take all your shit lying down!"
            
            show ava typical neutral
            
            ava @ say "Oh boy, here come the puns."
            
            show gunner displeased
            
            gunner @ say "Yeah [name], think of the poor translators who will have to make that make sense in another language."
            
            player "Sorry, I should have known it'd be hard for them to come up with worse jokes than ours."
            #player "They could come up with an original joke, but they'll have a hard time coming up with ones worse than ours."
            
            show ava typical smug
            show gunner neutral
            
            ava @ say "They're so bad they're good."
            
            n "You walk along with Gunner and Ava, cracking dumb jokes until it gets too late out."
            
            
        "Name a more obscure artist":
            player "I'm just saying Van Gogh and Ansel Adams are like baby's first artists."
            player "Now Ray Metzker? That was a true photographer. He could really tell a story and evoke a feeling without resorting to snapshots of natural landscapes from a high vantage point"
            
            show ava typical shy
            
            player "With his more abstract and tesselated works, I think he'd be more your style, Ava."
            
            show ava typical suggestive
            
            ava @ say "Yeah, creating something new from composites is pretty cool."
            
            show ava typical smug
            
            gunner @ say "Well, Metzker was good at transforming the real into fantastical mirages, but if you're talking about true photographers, look no further than Robert Landsburg."
            
            show gunner eyesclosed smile
            
            gunner @ say "Dude was literally dying in a volcano and still taking shots. What a legend."
            
            show gunner optimistic
            
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
            
            show ava typical enamored
            
            ava @ say "Well um...!"
            ava @ say "You know that one pic of that girl before she got murdered?"
            
            show gunner frown1
            
            gunner @ say "No? Which one?"
            
            player "Oh yeah, I know the one. Where she's standing on like a pier and holding her arms out and stepping back?"
            
            show ava typical embarrassed
            
            ava @ say "Yeah that one!"
            
            gunner @ say "So you wanna be murdered?"
            
            ava @ say "I don't *want* to be murdered! That wasn't the question!"
            ava @ say "I'm just saying it would be a really good photo just for the story!"
            
            gunner @ say "And this has nothing to do with your serial killer fetish?"
            
            ava @ say "It's not a fetish!"
            
            player "I've heard this one before. Next she'll say it's \'a lifestyle.\'"
            
            show ava typical angry
            
            ava @ say "Oh shush you!"
            
            show ava typical unimpressed 
            
            ava @ say "I'm sure you guys masturbate to weirder stuff."
            
            menu:
                "Yeah, I do":
                    player "Actually I do. That's not a problem, is it?"
                    
                    show gunner disgusted
                    show ava 
                    
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
                    
                    show gunner neutral
                    
                    show ava typical annoyed
                    
                    ava @ say "Rude!"
                    
            show gunner itsover
            
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
    scene bg campus summer night clear with fade
    
    show box with Dissolve(.2):
        ypos 0

    n "Bumbling around in the night sure is fun. You never know who you might bump into."
    n "Literally."
    n "You trip over something low to the ground, but instead of chipping your teeth on the asphalt below, you land on something incredibly soft."
    n "And large."
    
    claire @ say "Oh my, [name], right here in the middle of the street?~"
    
    n "You found yourself on top of Claire, who was crouched on all fours for some reason."
    n "You roll off of her and turn on your phone's flashlight."
    n "She appears to have her arm buried in a storm water drain on the side of the street."
    
    show claire sweater wave happy at center with dissolve:
        ypos y_claire
    
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
    $ lastChecked = ""

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
        player "Yeah, let's get out from under here."
    
        n "As you're squeezing past the metal framework of the bleachers, your foot strikes a support beam."
        
        player "Ow!"
        
        claire @ say "Wait, did you hear that?"
        
        player "Hear what?"
        
        claire @ say "Kick that beam again!"
        
        n "You hesitate, considering the pain in your toes from the last kick, before going for it anyway."
        
        claire @ say "It sounded like a loose latch being jostled!"
        
        n "Claire follows the diagonal beam up to where it joins the rest of the structure."
        n "It wasn't visible from the underside but now that you're behind the bleachers, you can make out a metallic box resting in a cranny where support beams meet."
        
        claire @ say "Good work, [name]!"
        
        n "Claire brings the box down and pops open the latches."
        
    elif lastChecked == "lamp":
        player "I guess we could just walk around until we find another potential hiding spot."
        
        claire @ say "Yeah, that looks like our only option."
        
        n "As you explore the area, you notice a section that's particularly dark. Upon closer inspection, it appears a lamp post is supposed to be illuminating this place but the bulb is burnt out."
        n "It's the only one you haven't checked so you tug on the base covering, not really expecting anything."
        n "To yours and Claire's shock, a metallic box similar to the one she found earlier lies beneath."
        
        claire @ say "Ohmygosh what a sneaky spot!"
        claire @ say "Good find, [name]!"
        
        n "Claire pops open the latches and lifts the lid."
        
    elif lastChecked == "shed":
        n "As you're exiting the shed, you notice a sparkle in the corner of your eye."
        n "There's a ridge under the awning and you can make out a shiny piece of metal up there."
        n "You point to it."
        
        player "Do you see that? Can you reach it?"
        
        n "Claire has no trouble grabbing hold of it and pulling it down. In her paws is a box similar to the one she found before."
        
        claire @ say "Aha! Good eye, [name]!"
        
        n "She sets it down on the ground and opens the latches."
        
    n "Inside, the box is empty aside from a pencil and a sheet of paper taped to the bottom."
    n "Only one name is written on it, and it dates back two years."
    
    claire @ say "That must be whoever set up this geocache."
    claire @ say "This makes us the first to find it!!"
    
    n "Claire scrawls down your names and the current date."
    
    claire @ say "Dang, I didn't bring another reward. Now whoever finds this will think I'm just a taker and not a giver!"

    menu:
        "Put your new trinket inside":
            n "You pull your newly acquired trinket from the last box and deposit it inside."
            n "Better to leave the next geocacher with a fun prize than for you to carry around more junk."
            
            claire @ say "Aww how sweet of you!"
            
            n "Claire pulls you into a side hug and nuzzles the top of your head."
            
            player "Just trying to be a good geocacher."
            
            claire @ say "The next finder will appreciate it! Ksksksks!"
            
            n "Claire puts the lid back on and secures the latches, returning the box to its original location."
        "Leave it empty":
            n "You decide to hold onto your memento as a reminder of tonight's events."
            n "Sorry next cacher, you get nothing."
            
            player "It's ok, I'm sure they'll understand."
            
            n "Claire dejectedly puts the lid back on and secures the latches, returning the box to its original location."
            
    claire @ say "Well, that's geocaching for you! What did you think?"
    
    player "It's... something."
    
    claire @ say "I'm glad I started doing it! There's a bunch of caches around here."
    claire @ say "When we were talking about hobbies earlier it got me thinking I needed a new one! So I looked up stuff to do and this was one I hadn't tried before!"
    claire @ say "Soooo thanks for leading me down this rabbit hole!"
    
    n "She's really happy to have something new to do."
    n "She'd probably love to do this again with you."
    
    claire @ say "This was a lot of fun!"
    claire @ say "I'd love to do this again with you!"
    
    n "Wow it's like she can read your mind."
    
    ###if you have high claire points
    
    claire "You like big bunnies, don't you [name]?"
    
    n "GET OUT OF MY HEAD!!!"
    
    player "Maybe we can do this again next time I go out on one of my signature nightwalks."
    
    claire @ say "Yeah!"
    
    n "You bid Claire a good night and return to your dorm for some much needed sleep."

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
    scene bg campus summer night clear with fade
    
    show box with Dissolve(.2):
        ypos 0

    #rori climbs stuff due to his instincts, but only does it at night where he's less likely to be caught. He get paranoid and jumpy when the player discovers him and embarrassed, but offers to teach you how to climb

    n "Your nightwalk brings you to an unassuming brick wall, much like any other brick wall the building here are made of."
    n "But this one is different. Tiny pebbles fall from it and pelt your head."
    n "When you step away from it and look up, you see a shadowy figure scaling the face of the building, jumping from brick to brick."
    n "He's on his way down and takes the last few jumps quicker than you expect. When he reaches the ground, his momentum leads him to nearly collide with you."
    
    show rori angry at center:
        ypos -3000
        
    pause .2
    
    show rori with move:
        ypos y_rori
    
    rori @ say "Aaaaah!"
    
    show rori armscrossed embarrassed2
    
    rori @ say "I'msosorrypleasedon'tcallthecops."
    
    player "Whoa take it easy. You didn't even bump into me."
    
    show rori armscrossed neutral
    
    rori @ say "Huh? Oh it's just you [name]. I take it you couldn't sleep either?"
    
    player "Nah, so I came out for a night walk."
    player "It looks like you went out for a night climb though! How do you even do that? There's nowhere to grip."
    
    show rori armscrossed surprised
    
    rori @ say "Oh gosh, you saw all that? Just- please delete that from your memory please."
    
    player "What? Why? It looked cool!"
    
    show rori armscrossed worried2
    
    rori @ say "It's an addiction! There's nothing cool about it!"
    
    player "You're addicted... to climbing?"
    
    show rori armscrossed anxious
    
    rori @ say "Shshshshsh! Not so loud!"
    rori @ say "I just can't help myself! These hooves were built for it!"
    
    show rori armscrossed embarrassed2
    
    rori @ say "My only comfort is that I can restrain myself long enough to wait until night so nobody will see me but apparently that's not good enough!"
    
    player "Dude chill, it's not that big a deal."
    
    show rori armscrossed surprised eyesclosed
    
    rori @ say "Please don't tell me you saw me lick the wall too!"
    
    show rori armscrossed anxious at center:
        ypos y_rori
    
    rori @ say "You gotta understand, there's *salt* on the walls bro! It's irresistable!"
    
    player "I didn't see you lick the wall."
    
    show rori none
    show rori concerned
    
    rori @ say "Oh."
    
    player "..."
    
    rori @ say "..."
    
    player "Does it taste good?"
    
    show rori neutral
    
    rori @ say "When you get up to the 4th floor or so."
    
    player "Nice."
    
    menu:
        "I wanna climb":
            n "You feel around the wall, searching for any place to grip. The mortar between the bricks is rough but too narrow, only the very tips of your fingers can rest between them."
            
            show rori anxious
            
            rori @ say "What are you doing?"
        
            player "Trying to see if I can climb this. Was there a ledge you used or something?"
            
            show rori neutral
            
            rori @ say "No, the bricks were enough for me."
            
            show rori armscrossed concerned
            
            rori @ say "You really shouldn't be trying to climb this though."
            
            player "Why? Think I'll fall and hurt myself?"
            
            show rori armscrossed embarrassed2
            
            rori @ say "I'm worried you'll get addicted to it!"
            
            hide rori with dissolve
            
            n "You don't really have a plan but decide to test your abilities regardless by clamping down on a brick with all your finger strength and pushing both feet off the ground."
            n "You lodge the edges of your boots into the mortar a few inches above the ground and manage to stay clinging to the wall for a few seconds before your hands give out, dropping back down to the ground."
            
            player "Whew! Are you *sure* you don't have some antigravity tech that gets you up there?"
            
            show rori armscrossed neutral at center with dissolve:
                ypos y_rori
            
            rori @ say "It's all just in the weight balance. It helps to have upper body strength too."
            
            player "Gotchya."
            
            n "You give it one more attempt but manage to hold on for even less time than before."
            
            show rori none
            show rori yawn lookingaway blush
            
            rori @ say "You probably just need to start on something easier."
            
            show rori angry neutral
            
            rori @ say "*Not* that I'm advocating for this filthy habit, I'm just saying."
            
            show rori neutral
            
            player "Heh, I'll get to your level someday."
            
            show rori concerned
            
            rori @ say "Hopefully not!"
            
            player "Just you wait and see, hoofboy~"
            
            show rori angry
            
            rori @ say "D-don't call me that!"
            
        "I'm good on the ground":
            n "You look up at the building, counting six stories including the ground floor."
            
            player "I don't know how you do it. I'd fall right off instantly."
            
            show rori armscrossed cheery
            
            rori @ say "It's not so hard, you just slip your hooves into the grooves and balance your weight on the contact points."
            rori @ say "This wall even has a 0.5 degree incline so I could stay up there all day if I wanted to."
            
            hide rori with dissolve
            
            player "I guess having hooves is a prerequisite."
            
            n "You pull your hands out of your pockets and wiggle your fingers."
            
            player "These things would let me down once I got high enough to fall to my death."
            
            show rori armscrossed neutral at center with dissolve:
                ypos y_rori
            
            rori @ say "Yeah, probably."
            rori @ say "You'd have to work your way up."
            
            show rori armscrossed anxious at shudder
            
            rori @ say "Not that you'd *want* to. You may think you want to but that's how every addiction starts."
            
            player "Haha I don't think I'm gonna get addicted to climbing."
            
            show rori armscrossed embarrassed2
            
            rori @ say "That's how it gets you! Nobody expects it to happen to them, but it's such an alluring habit that'll ruin your life!"
            
            player "I'll take your word for it, hoofboy."
            
            show rori angry
            
            rori @ say "D-don't call me that!"
            
    hide rori with dissolve
            
    n "You walk Rori back to his dorm and bid him a good night before returning to your own dorm for some sleep now that you've gotten the zoomies out of you."

    return
    
label roriNightWalkLvl2:
    
    n "rori night walk part 2"

    return

label roriNightWalkLvl3:
    
    
    n "rori night walk part 3"

    return
    
    
label mishkaNightWalkLvl1:
    scene bg campus summer night clear with fade
    
    show box with Dissolve(.2):
        ypos 0

    n "Your night walk through the campus leads you past the cafe. A dim glow shines through the windows, and for a moment you realize what it feels like to be a moth because you're oddly drawn to it."
    n "The glass is foggy but you can make out some movement inside."
    n "Is Coffee Zone really open this late at night or is it just like a janitor or something cleaning up?"
    n "Ah fuck it, you could go for a drink if the door isn't locked."
    n "To your surprise, it's not."
    
    scene bg cafe with fade
    
    show box with Dissolve(.2):
        ypos 0
            
    n "Inside only half the lights are on. You find nobody at the counter, but a repetitive clicking sound reaches your ears."
    n "Sitting in a dark corner, Mishka fiddles with a machine atop a table, pushing something through it."
    
    show mishka jacketless frown at center:
        ypos y_mishka
    
    mishka @ say "*Squeak!*"
    
    show mishka jacketless tongueout
    
    mishka @ say "Goodness [name], you nearly scared me to death!"
    
    show mishka jacketless neutral
    
    player "Sorry, didn't mean to. I almost jumped out of my socks when I saw you there myself."
    player "What are you doing here so late?"
    
    show mishka jacketless nervous anxious
    
    n "Mishka looks away, almost bashfully."
    
    mishka @ say "Ah you know, just doing some sewing."
    
    mishka @ say "There was another tear in this coat I needed to patch up."
    
    n "She sticks her claws through a hole in the fabric."
    
    show mishka jacketless neutral
    
    mishka @ say "I could have just sewn it by hand but I didn't have the right colored thread at home so I figured I would just do it here."
    
    player "...Why does the cafe have a sewing machine?"
    
    show mishka jacketless sad2 nervous
    
    n "Mishka releases the pedal and the machine stops. She appears to be caught off guard."
    
    mishka @ say "Well uh... I'm not sure how to say..."
    
    menu:
        "Go on":
            player "Go on."
            
            mishka @ say "It's just... my apartment is rather small after all."
            mishka @ say "I don't have a good place to set up a sewing machine. So I keep it in the closet here."
            
            show mishka jacketless frown
            
            mishka @ say "Please don't tell anybody! I know I'm not supposed to have it here but using a machine is so much faster!"
            
            player "Your secret is safe with me."
            
            show mishka jacketless overjoyed
            
            mishka @ say "Oh duzhe dyakuyu!!"
        "Drop it":
            player "Hey that's pretty cool. I guess if I ever need to sew something while sipping coffee I can just come here!"
            
            show mishka jacketless anxious nervous
            
            mishka @ say "R-right! Anytime!"
            
    show mishka jacketless neutral
    
    n "She finishes up sewing on the patch in no time, with straight and even stitching all throughout."
    
    player "Nice. It looks almost good as new!"
    
    show mishka jacketless frown
    
    n "Mishka sighs."
    
    mishka @ say "Just one more patch added on. Soon it will be nothing but patchwork."
    
    menu:
        "It gives it character":
            player "The repairs give it character. Patches are in style!"
            
            mishka @ say "I don't want it to be stylish! I want it without coffee stains and scuffs and tears and bullet holes!"
            
        "Can't be hard to find a new one":
            player "A new milsurp jacket shouldn't be too hard to find once that one wears down."
            
            mishka @ say "I don't want a new one, this one is special!"
            
    show mishka at flipright
    show mishka jacketless nervous anxious
            
    n "In a rare display of frustration, she huffs and turns away from you."
    
    n "You wait a moment before muttering some kind of apology, unsure of what you did."
    
    show mishka jacketless nervous sad
    
    mishka @ say "Nemaye, I shouldn't have raised my voice."
    
    show mishka jacketless nervous sad2
    
    mishka @ say "I'm just upset whenever a piece of this fabric gets destroyed because it once belonged to my father."
    
    show mishka jacketless frown
    
    n "She holds up the jacket, inspecting the new patch's stitches from both the exterior and the interior."
    
    mishka @ say "It's like losing a little piece of him each time but I don't want to stop wearing it."
    
    n "It suddenly all makes sense. This isn't just some memento from home, it has sentimental value."
    n "She almost never takes that jacket off, even when it's hot."
    
    hide mishka with dissolve
    
    pause .35
    
    show mishka sad at center with dissolve:
        ypos y_mishka
        xzoom -1
    
    n "Even now, she puts it back on once she's satisfied with the stitching."
    
    player "It must mean a lot to you."
    
    mishka @ say "It means so much."
    
    player "You may have to repair it sometimes and cover it up with patches but the inner lining is always the same."
    player "You'll always be wearing your father's jacket because all these patches and threads are sewn into the original fabric."
    
    mishka @ say "Yeah, I guess so."
    mishka @ say "Dyakuyu [name]..."
    
    show mishka neutral standing
    
    n "She turns back to you with a soft smile."
    
    mishka @ say "Would you... like to stay and have a coffee with me?"
    
    player "Of course!"
    
    show mishka happy tongueout
    
    mishka @ say "Oorah!"
    
    n "Mishka unplugs the sewing machine and hauls it over to the closet, then gets started on your drinks. You stay up late into the night chatting, even after your cups are empty."

    return
    
label mishkaNightWalkLvl2:
    
    n "mishka night walk part 2"

    return

label mishkaNightWalkLvl3:
    
    
    n "mishka night walk part 3"

    return
    
    
