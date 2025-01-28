label liberation_day:
    scene bg codadorm with fade

    show box:
        ypos 0
    
    play music "audio/ambient/morning birds.ogg" fadein 0.1

    n "Today is Anthromorphs' Liberation Day."
    n "You've always felt awkward about this holiday."
    n "Like it's not for you or something."
    n "Maybe a hundred years ago it was about the alliance between humans and anthromorphs."
    n "But nowadays it's been recontextualized as the rise of animal people after your kind died off."
    n "It's a really strange feeling. The world you inhabit was shaped by humans who are just gone now, aside from you."
    n "Your great grandpa would have been horrified to see you hanging out with your current friends."
    n "He claimed he was allergic to any kind of fur but he always looked so smug when detailing the battles he had fought in where he killed anthromorphs."
    n "And now he's dead and your only friends are animal people."
    n "The age of humans is over and a new generation has inherited the world."

    if avaUrbex == True:
        n "*sigh*"
        n "At least you get to hang out with a cute bird (who might be into you??) today."

        hide box

        call phone_start from _call_phone_start_29

        call message_start("me", "Hey", "testimage.png") from _call_message_start_63

        call message("Ava", "Hi!!!", "avaavi.png") from _call_message_352

        call reply_message("So we're going to this old hospital today?") from _call_reply_message_256

        call message("Ava", "Yup! I'm ready whenever you are ^v^", "avaavi.png") from _call_message_353

        call reply_message("Where exactly is it?") from _call_reply_message_257

        call message("Ava", "Hang on lemme get the coordinates", "avaavi.png") from _call_message_354

        call phone_end from _call_phone_end_55

        show box:
            ypos 0

        n "She sends you the coordinates which open in your map app when you tap on them."
        n "You can barely tell there's a building there from the satellite images since it's so overgrown with trees and bushes."
        n "Ava sends you a text telling you to meet her there in an hour."
        n "You prepare your backpack, stuffing it with a couple water bottles and snacks, then proceed to head out."

        scene bg oldhospital foyer with fade

        #play music "audio/ambient/spooky.ogg" fadein 1.0
        #play music "audio/music/vylet - Cavern Lurker.ogg" fadein 1.0
        play music "audio/music/Vylet Pony - Reflected in the Eyes of the Cavern Lurker.ogg" fadein 1.0

        show box with Dissolve(.2):
            ypos 0

        n "Ava wasn't kidding when she said this place was abandoned."
        n "Graffiti lines the walls and weeds grow out of cracks in the concrete. You'd be afraid to enter a place like this alone, but luckily you have a dainty liberal arts student here to protect you."

        show ava typical happy at center with dissolve:
            ypos y_ava

        #ava @ say "Hey [name]! Glad you could make it!"

        #player "It took a while to find it! There's no trail or signs or anything."

        ava @ say "It's probably been years since anyone has last stepped foot here."
        
        player "Any functioning member of society at least."
        
        show ava excited
        
        ava @ say "Come on, let's get exploring!"
        
        hide ava with dissolve
        
        scene bg oldhospital hall1 with dissolve
        
        show box:
            ypos 0

        n "Ava leads the way as you go deeper inside, pulling away some boarding planks and debris along the way."
        n "She looks around before deciding on a place to compose a shot and snapping a picture."

        player "That's not your usual camera, is it?"
        
        show ava typical happy at center with dissolve:
            xzoom -1
            ypos y_ava

        ava @ say "Hm? Oh this?"
        ava @ say "I brought one of my old film cameras along. Thought some vintage black and white film would fit the mood of the place, y'know?"
        
        player "It's not because ghosts can only be recorded on analogue, is it?"
        
        show ava pose smug
        
        ava @ say "Well, that too."

        n "She pulls a lever on the camera, loading the next frame."
        
        show ava typical happy

        ava @ say "And it just wouldn't feel right shooting this place in color."
        ava @ say "I don't even think color film was invented yet when they built this place."

        player "What about lead paint and asbestos?"
        
        show ava at flipleft
        
        pause .7
        
        show ava at flipright
        
        pause .4

        ava @ say "Hehe, I dunno! Try not to lick the walls just in case."
        
        hide ava with dissolve

        n "You make your way through the building slowly, being careful not to step on any rusty nails or fall through any floorboards."
        n "Dust kicks up as you explore, mixing with the smell of mildew in the humid air. Every now and then you hear creaks and pops from other rooms echoing throughout the building."
        n "Water drips down from the ceiling into little puddles full of moss and weird sludge you don't dare touch."
        n "Luckily the holes in the walls provide enough light for you to navigate."
        n "You and Ava make your way to the end of the hall where a staircase lies, the steps covered in rubble from the crumbling walls and steps above."
        n "Ava crouches down and turns her camera 90 degrees to take a shot of it."
        n "Her feathers stick up and you jump a little when a loud noise comes from behind, echoing throughout the hall."
        
        show ava pose concerned at center with dissolve:
            ypos y_ava
        
        n "You speak in a hushed tone."

        player "...Did you hear that?"

        ava @ say "Yeah... is someone here?"
        
        n "As if to answer her question, the sound of rubble being kicked around echoes throughout the concrete walls."
        
        player "M-must have been the wind?"
        
        ava @ say "I don't think we're alone. Come on, let's go up the stairs, quick!"
        
        n "Ava goes first, lightly stepping between the larger piles of debris while you struggle with these non-OSHA compliant stair sizes."
        n "She flutters over a precarious gap in the steps that you unfortunately end up getting your foot stuck in."
        
        player "Agh! My foot!"
        
        show ava typical shocked
        
        ava @ say "[name]!"
        
        n "Ava doubles back and helps pull you out, oblivious to the pain shooting through your ankle. You try to keep quiet so she doesn't think you're a pussy."
        n "You hobble up the remaining stairs and into a room, closing the door behind you, bracing it with your body."
        
        stop music fadeout 2.0
        
        scene bg oldhospital darkroom with fade
        
        show box:
            ypos 0
        
        n "For a few moments it's just you and Ava in a dark room trying not to breathe heavily after the jumpscare. You put your ear to the door and listen for any sounds."
        n "Ava listens too, leaning against you. Her soft wings are wrapped around you."
        n "Her camera is jabbing into your side uncomfortably but you can feel her heartbeat against your chest, which is oddly calming."
        n "You guess if you're gonna get stabbed by a hobo, this would be a nice final memory. Cute bird in your arms. Maybe someone will find the film and develop it."
        n "Then make a documentary about you."
        n "'Two dumbasses go venturing in dangerous hobotopia, shockingly get murdered in most gruesome way possible.'"
        n "After a minute passes, Ava speaks up in a hushed tone."
        
        show ava typical neutral at center with dissolve:
            ypos y_ava
        
        ava @ say "I think whoever that was is gone. Or at least they didn't follow us."
        
        ava @ say "It was probably just a stray cat. They like to hang around places like this."
        
        player "Yeah hopefully it was just a wild animal and not like a psycho stalker serial killer."
        
        show ava annoyed
        
        ava @ say "Ugh you just reminded me of something."
        
        player "What?"
        
        ava @ say "Promise you won't cringe."
        
        player "Oh please, whatever it is, I guarantee I've done worse."
        
        show ava agitated
        
        ava @ say "I had blocked this memory out for so long but... in freshman year of high school I would actually send letters to serial killers who were in jail that I thought were cool."
        
        show ava angry
        
        ava @ say "I was confused at the time okay???"
        
        menu:
            ava "{cps=0}I was confused at the time okay???{/cps}"
            "What was the appeal?":
                player "That's uh... quite unexpected. What's the appeal?"
                
                show ava typical neutral
                
                ava @ say "I dunno, I guess the forbidden nature of it combined with the gruesomeness?"
                ava @ say "A murderer is just an interesting type of person!"
                ava @ say "You just wanna know \'What made you do it?\'"
                ava @ say "Cause you have to wonder if you could become a murderer too if you grew up just a little differently."
                ava @ say "You'd know you're not just with any regular shmuck if he had the guts to kill somebody!"        
            "I sorta get it":
                player "I feel the same way kinda."
                
                show ava typical neutral
                
                player "There's something sexy about someone who can straight up murder in cold blood."
                player "That sort of evil is mesmerizing, isn't it?"
                
                ava @ say "I know right??"
                ava @ say "Maybe it's like a primal instinct thing. Like wanting a brutish man who can protect you."
                ava @ say "By violently murdering your enemies."
                ava @ say "I mean, uh, that's probably what I was thinking back then."
                ava @ say "You don't have to murder anyone for me to like you."
                
                player "Noted."
        
        player "Did any of them ever write you back?"
        
        ava @ say "I dunno. My parents probably would have shredded the letters if we got any before I'd ever gotten a chance to see them."

        n "You feel Ava pull away from you."
        
        show ava with move:
            xoffset -1500
            
        hide ava
        
        player "Careful, it's dark and we don't know if this is where they stored the rusty nails."
        
        n "*Crck*"
        n "A dim purplish glow gradually fills the room."
        
        show ava typical glowy agitated at center with dissolve:
            ypos y_ava
        
        ava @ say "I brought some glowsticks. Good to have in case your batteries run out. Or for creating ambiance."
        ava @ say "And they're my favorite color."
        
        player "Whoa! Ava, your feathers..!"
        
        n "She turns around, looking over her plumage."
        
        show ava at flipright
        
        pause .5
        
        show ava at flipleft
        
        pause .37
        
        ava @ say "Hm? What about them?"
        
        player "They're all pretty and stuff!"
        
        ava @ say "Oh my gosh thanks? I didn't really do anything special with them today though."
        
        player "But you have patterns on them now!"
        
        ava @ say "I always have patterns on them. That's just how they are."
        
        player "I never noticed them before!"
        
        ava @ say "Hmm, okay I think I know what's going on."
        
        n "She waves a glowstick over her wing feathers and more patterns become visible."
        
        ava @ say "The ultraviolet frequencies from the glowstick must be close enough to your visible light spectrum to reveal these."
        ava @ say "It's like a blacklight."
        ava @ say "You're probably only seeing a fraction of them. They're normally only visible to avians."
        
        player "Wow. Do all birds have patterns on their feathers?"
        
        ava @ say "Just the pretty ones~"
        
        n "Ava cracks another glowstick and wanders further into the room."
            
        ava @ say "You comin- oh god [name]! What's with your foot?"
        
        player "Huh?"
        
        n "You look down to see your foot bent at an unnatural angle."
        
        player "Oh. Fuck."
        
        ava @ say "Holy Hoole that looks bad... Stay right there, I'll- I dunno, I'll figure something out."
        
        n "Ava looks around and finds an old wooden cane for you to lean on."
        
        ava @ say "Lucky we're in a hospital right? Haha..."
        
        n "Her attempt at making light of the situation is appreciated but now that the adrenaline is wearing off, you're starting to feel excruciating pain."
        
        player "Where's a doctor when you need one?"
        
        ava @ say "Can you walk? We should get you to a real hospital asap."
        
        n "Ava lets you lean on her as the two of you exit the room and head back down the stairway."
        n "It takes a long time but you eventually make it back to the ground floor."
        
        scene bg oldhospital hall2 with fade
        
        play music "audio/music/vylet - dance of the macabre.ogg" fadein 1.0
        
        show box:
            ypos 0
        
        n "As you're trying to figure out which direction you came from, you notice Ava seems preoccupied with a corridor you hadn't explored."
        
        show ava typical concerned at center with dissolve:
            ypos y_ava
            xoffset 0
        
        ava @ say "..."
        
        player "Go ahead, I can tell you've got a photo in mind."
        
        show ava excited
        
        ava @ say "Whew thanks! I'll be just a second, alright?"
        
        hide ava with dissolve
        
        n "You lean on your cane while she flutters up to a high perch and lines up a shot."
        n "Suddenly a loud noise startles both of you and Ava comes crashing down."
        
        show ava reaching concerned:
            ypos -3000
            xpos 700
            
        show ava with move:
            ypos 1080
            
        pause .2
                    
        player "Ava!"
        
        show ava typical concerned at center:
            ypos 2500
            
        pause .2
        
        show ava with move:
            ypos y_ava
        
        ava @ say "I'm okay!"
        
        player "What the fuck was that?"
        
        show ava at shudder
        
        ava @ say "I dunno but we better get out of here now before we get murdered."
        
        player "Don't you wanna meet your serial killer husbando?"
        
        show ava angry
        
        ava @ say "Shut up or I'll leave you here without your crutch."
        
        player "Okay okay, let's just get out of here. Which is... that way I think? I'm not sure, this place is like a maze."
        
        show ava typical neutral

        n "You approach a corner and poke your heads around it."

        player "Do you see anything?"

        ava @ say "Nada."
        ava @ say "Wait."
        ava @ say "Wasn't that window boarded up earlier?"

        player "I don't remember! There's a lot of boarded up windows."
        
        show ava happy

        ava @ say "It looks like it leads outside. I'll help you through it."
        
        hide ava with dissolve

        n "Ava puts forth her best effort in pushing you through the window, though a petite bird like her is unable to offer much help."
        n "You get your upper body onto the windowsill and then roll over the edge."
        
        stop music fadeout 1.0
        
        stop music fadeout 2.0
        
        scene bg oldhospital exterior with fade
        
        show box:
            ypos 0
        
        play music "audio/ambient/outdoors night crickets.ogg" fadein 1.0
        
        n "With the last bit of sunlight fading from the sky, it was hard to see exactly where you were crashing. And Ava wasn't waiting around to get murdered just because your foot hurts."
        n "Fortunately you only feel nice soft grass on the ground and not broken glass."
        n "Every little vibration in your foot still hurts like hell though."
        
        player "Ow."
        
        show ava typical concerned at center with dissolve:
            xoffset 450
            ypos y_ava
        
        ava @ say "You alright? Here's your cane."
        
        n "The tall grass ahead of you rustles, parting away as something gets closer."
        
        show ava shocked
        
        ava @ say "What was that?"
        
        n "A pair of glowing eyes shines in the dim light, staring you down and getting closer."
        
        show gunner neutral at center with dissolve:
            ypos y_gunner
            xzoom -1
            xoffset -450
        
        gunner @ say "[name]! Ava! Fancy seeing you here!"
        
        show ava annoyed
        
        ava @ say "Gunner? What the hell are you doing here?!"
        
        gunner @ say "Oh y'know, just some urban exploration. Urbex as they say. Which I'm totally into by the way."
        
        player "I thought you were going on a panty raid today."
        
        show gunner eyesclosed smile
        
        gunner @ say "Nah today was the scouting day. We finished early so I thought I'd take a look around this place."
        
        show ava angry
        show gunner disgusted
        
        ava @ say "A *what* raid?!"
        
        gunner @ say "N-nothing, just a silly frat tradition."
        
        show gunner displeased
        
        gunner @ say "Hey is your foot alright, [name]? I'm no expert in human anatomy but I don't think you can twist yours back almost 180 degrees normally."
        
        player "Yeah it's definitely sprained or something."
        
        show ava at hop
        
        ava @ say "Dammit Gunner we thought you were a stalker and [name] got injured because of you!"
        
        gunner @ say "Hey, don't blame me because [name] clumsily tripped over their own feet!"
        gunner @ say "It's not like I pushed them down the stairs or anything."
        
        show ava annoyed
        
        ava @ say "Ugh, whatever. Let's just get [name] to a doctor. You can carry him since you're the most responsible for them getting hurt in the first place."
        
        gunner @ say "Hmph. Fine."
        
        n "You kinda tuned out of the conversation. This hospital sucks. Can you go home now? Your feet hurt."
        n "Gunner gingerly picks you up in a bridal carry."
        n "What the fuck this actually feels kinda nice."
        
        show gunner frown1
        
        gunner @ say "Sorry about all this, buddy. I just wanted to hang out and stuff."
        
        n "The trip to the hospital is quiet and tense."
        
        stop music fadeout 1.0
        
        scene bg hospital with fade
        
        show box with Dissolve(.2):
            ypos 0
        
        play music "audio/music/Vylet Pony - lemonade.ogg" fadein 0.1
        
        show kitsuragi at center:
            xoffset -500
            xzoom -1
            ypos y_kitsuragi
        show gunner optimistic at center:
            xoffset 350
            ypos y_gunner
        show ava typical neutral at center:
            xoffset 540
            ypos y_ava
        with dissolve
        
        kitsuragi @ say "Welp. I expected to see you again soon but not for something like this."
        kitsuragi @ say "You're lucky you have friends to drag your ass here all the time."
        
        player "It's a bonding experience."
        
        show gunner neutral
        
        gunner @ say "Again, super sorry this happened, [name]! I'll make it up to you, I promise."
        
        show ava angry
        
        ava @ say "You better!"
        
        gunner @ say "You played your part in this happening too! I reckon you owe [name] something too!"
        
        kitsuragi @ say "I'll leave you all to figure that out on your own."
        kitsuragi @ say "[name], you'll be in pain for a while but there's no major damage. You'll be able to walk without a crutch in a few days."
        kitsuragi @ say "In the mean time, try not to put too much pressure on your ankle."
        kitsuragi @ say "You're free to go whenever. Or you can stay the night, I don't care."
        
        n "You sip on the complimentary juice box she gave you for being brave after she twisted your foot back into place and nod."
        
        hide kitsuragi with dissolve
        
        show gunner with move:
            xoffset -300
        
        n "Gunner and Ava awkwardly stand around, looking at the ground in opposite directions."
        n "You cough to break the silence."
        
        player "Sooooo..."
        
        show ava pose concerned
        
        ava @ say "Soooo...?"
        
        #gunner @ say "....Yeah."
        
        show gunner at flipright
        
        player "This was a fun day. If I wasn't already traumatized by hospitals, I sure will be now."
        
        show ava pose shy
        
        ava @ say "Heh yeah... This place is even spookier than the old abandoned one, huh?"
        
        show ava pose happy
        
        gunner @ say "You gonna stay the night here or go back to your dorm?"
        
        menu:
            gunner "{cps=0}You gonna stay the night here or go back to your dorm?{/cps}"
            "I'll stay here.":
                player "I don't really feel like moving. I'll wait and see if my foot is better in the morning."
                
                gunner @ say "I'll stay here with you then. I don't want you to be alone in this shitty place."
                
                player "Aww, how sweet of you."
                
                ava @ say "I'll stay too!"
                
                show gunner:
                    xzoom -1
                
                player "Nah, one is enough to suffer here with me. Thanks though."
                
                show ava concerned
                
                n "Ava looks slightly disappointed but nods."
                
                ava @ say "Alright then..."
                
                show ava pose angry
                
                ava @ say "I'll go but if Gunner tries to break your other leg, gimme a call and I'll come flying!"
                
                player "Heh will do~"
                
                show ava typical happy
                
                ava @ say "Take care, [name]. I'll see you later, k?"
                
                player "For sure. Later birdy~"
                
                show ava profile shy
                
                ava @ say "Later, human~"
                
                hide ava with dissolve
                
                show gunner annoyed
                
                gunner @ say "Cute."
                
                pause .1
                
                show gunner with move:
                    xoffset -500
                
                n "Gunner plops down in the chair across from you."
                n "It seems like he has a lot on his mind."
                
                player "What's with you today? Why'd you follow us like a creep?"
                
                show gunner displeased
                
                gunner @ say "I wasn't following *you!* I was-"
                
                n "He looks away, unsure of what to say."
                
                show gunner gruff
                
                gunner @ say "I was just trying to get closer to Ava."
                
                show gunner frown1
                
                player "You hijacked our adventure dude."
                player "You should have just asked to come along."
                
                show gunner uncomfy
                
                gunner @ say "Yeah lemme ask to be the third wheel on your date next time."
                gunner @ say "Don't worry, I'll provide my own cuck chair."
                
                player "It wasn't even a date!"
                player "I didn't ask her out or anything."
                
                show gunner pissed
                
                gunner @ say "Oh so *she* asked you out?"
                
                show gunner displeased
                
                player "It's not like that. She just didn't wanna go to some dangerous place on her own."
                player "She probably would have asked you to go with her if she happened to see you first."
                
                show gunner cutie
                
                gunner @ say "Sooo... you're not into her?"
                
                menu:
                    gunner "{cps=0}Sooo... you're not into her?{/cps}"
                    "I didn't say that":
                        player "I didn't say that."
                        player "I'm just saying I didn't pull any moves on her."
                    "She's not my type":
                        player "Nah she's not really my type."
                        player "We were just hanging out as friends."
                    "Maybe I am":
                        player "Maybe I am, maybe I'm not."
                        player "Whatever happens happens. I'm not pushing for it nor am I resisting."
                        
                show gunner uncomfy
                
                n "Gunner slumps in his seat, his usual confidence replaced with a pitiful sense of shame."
                
                player "Why are you even into her? You've been around each other like twice."
                player "Hell, you both use me to relay messages between each other."
                
                show gunner optimistic
                
                gunner @ say "Yeah but did you see the way she looks at me?"
                
                player "Just 'cause she thinks you're hot doesn't mean she wants a relationship with you."
                
                show gunner itsover
                
                gunner @ say "She's like the only girl who's nice to me though."
                
                player "Oh my god your incel is showing. She's just being polite, like she is to everyone."
                player "Claire and Mishka are nice to you too."
                
                show gunner wink frown
                
                gunner @ say "Yeah but they're ug- not my type."
                
                show gunner frown1
                
                player "Look, I'm not saying Ava wouldn't be into you, just that right now you two are practically strangers."
                player "I only talk to her because I have French with her roommate and we meet up after class."
                
                gunner @ say "So what am I supposed to do? Take a class with her?"
                
                player "No, I think you should just talk to her. If she likes you then she'll let you know."
                player "Just be yourself instead of coming up with schemes to try and get her to like you."
                
                show gunner determined
                
                gunner @ say "You must not know many cats. Scheming is in our nature."
                gunner @ say "We don't just sit back and let things happen, we have nine lives and shit."
                
                player "What on Earth is that supposed to mean?"
                
                gunner @ say "It means we can afford to take risks! If it doesn't work out in this life it'll go better in the next one. Probably."
                
                player "So your strategy is to do a bunch of goofy shit on the off chance that it works because if you do it enough eventually you'll succeed?"
                
                gunner @ say "You make it sound lame."
                gunner @ say "The idea is that you live your first life normal, then you relive it eight more times where you defy your original fate more and more as you learn how to game the system."
                
                player "And which life are you on right now?"
                
                gunner @ say "No idea but I feel like it's definitely between 4 and 7. Most likely 6."
                
                n "He's pulling these number out of his ass."
                
                menu:
                    n "{cps=0}He's pulling these number out of his ass.{/cps}"
                    "That's bullshit":
                        player "That's bullshit but you might be onto something."
                        
                        gunner @ say "I didn't make it up, it was discovered thousands of years ago. It's literally science."
                        
                        show gunner mischief
                        
                        gunner @ say "You trust science, don't you?"
                        
                        show gunner neutral
                        
                        player "I have my doubts that this is the singular paranormal phenomenon in the world to be proven true, before the scientific method was developed no less."
                        player "But choices are a thing, right? I could have chosen not to even go urbex'ing today."
                        player "Who's to say there isn't an alternate timeline where I went on the panty raid with you and Rori instead?"
                        
                        gunner @ say "Now you're getting it! And now you know for next time to just do the panty raid if you don't want your ankle getting twisted."
                        
                        player "I'll keep that in mind."
                        player "So you think there's a timeline where you get with Ava?"
                        
                        show gunner itsover
                        
                        gunner @ say "There's gotta be at least one. I'm just hoping it's this one."
                        
                        show gunner frown1
                        
                        player "Girls love that spiritual stuff. Protip: find out which astrological sign is most compatible with hers then legally change your birthday so you have that sign."
                        
                        show gunner cheeky1
                        
                        gunner @ say "Hey that's not a bad idea!"
                        
                        n "He doesn't seem to have caught on that you were joking."
                        n "The two of you chat more about philosophy and girls into the night."
                        
                    "Not how fate works":
                        player "That's not how fate works, otherwise it wouldn't *be* fate."
                        player "We're all locked into one set path, no matter how much it looks like we can change it."
                        
                        gunner @ say "Maybe it's that way for you."
                        gunner @ say "But we felines define our own fate! It is our destiny to defy the chains of uhh... destiny!"
                        
                        player "Nice self fulfilling prophecy you got there. What if your fate is to get with Ava and you're unknowingly working against it?"
                        
                        show gunner disgusted
                        
                        gunner @ say "Oh shit could that really happen?"
                        
                        player "You're the one who believes in real life RNG manipulation, not me."
                        
                        show gunner eyesclosed catface
                        
                        gunner @ say "It's a cat exclusive ability."
                        
                        player "If you say so. I don't want us to fight over some girl though."
                        player "Bros before hoes and such."
                        
                        show gunner neutral
                        
                        gunner @ say "Ay, true."
                        gunner @ say "But don't call my crush a hoe."
                        
                        player "Oh sorry."
                        player "But for real, I'm not even actively pursing anyone, I don't think? If Ava wants to go out with me or you or whoever, that's her choice."
                        #I'm just gonna let Ava decide who she wants."
                        
                        show gunner disgusted
                        
                        gunner @ say "I guess that's... fair?"
                        
                        player "Cool, I'm glad you're not mad at me."
                        
                        show gunner cheeky1
                        
                        gunner @ say "Same."
                        gunner @ say "I wouldn't wanna lose one of my best bros over this."
                        gunner @ say "Don't expect me to hold back though. I'm gonna end up with Ava no matter what."
                        
                        player "We'll see about that."
                        
                        stop music fadeout 1.0
                        
                        hide box

                        scene bg black with fade

                #___saturday4
                
                scene bg codadorm with fade
                
                show box with Dissolve(.2):
                    ypos 0
                
                n "After talking with Gunner a bit more last night you both fell asleep. When you woke up you felt good enough to walk back to your dorm."
                n "Gunner made sure you got here fine then left to do cat things while you rest up."
                n "It doesn't look like you'll be doing anything else exciting for the weekend on this limp foot of yours."
                
                jump ch2End
                    
            "Screw this place.":
                player "Yeah no, screw this place, I'm going home."
                
                n "Gunner hands you your crutch as you get into a sitting position and begin to stand up."
                
                gunner @ say "I can carry you back if you want."
                
                player "That won't be necessary."
                
                show gunner:
                    xzoom -1
                
                show ava profile concerned
                
                ava @ say "You gonna be okay?"
                
                player "I think so, aside from the nightmares I'll probably get from that spooky hospital."
                
                show ava profile smug
                show gunner frown1
                
                ava @ say "Aww, want me to snuggle you tonight and protect you?~"

                #menu:
                #    ava "{cps=0}Aww, want me to snuggle you tonight and protect you?~{/cps}"
                #    "Yes please":
                $ avaPoints =+ 1
                
                player "That would be delightful."
                
                show ava reaching embarrassed

                n "Ava looks caught off guard, like she didn't expect that response."

                ava @ say "I-I was just joking you know!"
                
                show ava typical shy -
                show ava at flipright

                n "She looks away but can't hide her blush."
                
                show ava annoyed
                
                show ava at flipleft

                ava @ say "Fine, I'll do it! Just for tonight though!"
                
                n "You didn't even agg her on. She actually wants to do it but she had to play hard to get for all of 2 seconds."
                
                player "Sounds good to me!"
                
                hide ava
                hide gunner
                with dissolve
                
                n "Gunner quietly seethes in the corner."
                n "Better luck next time, buddy."
                n "Gunner walks you back to your dorm, being unusually quiet while you joke about the day's events with Ava."
                n "After what you've been through, it's nice to lighten up a little."
                n "Gunner can be pissy if he wants, you're gonna enjoy some birdy snuggles tonight."
                
                stop music fadeout 1.0
                
                scene bg codadorm with fade
                
                #play music "audio/exports/【Music】こんにちは! ♡ [lQQkCtUahHE].opus" fadeout 1.0
                play music "audio/music/vylet - yeah i'm ok thanks for asking.ogg" fadein 1.0

                show box:
                    ypos 0

                n "You made it back to your dorm in one piece."
                n "Gunner went back to his own dorm and you left Ava to her own devices while you took a quick shower."
                n "You step out of the steamy bathroom wearing some ultra comfy pajamas to cuddle up in. You turn your head and catch Ava preening her feathers on your bed."
                
                show ava reaching embarrassed at center with dissolve:
                    ypos y_ava
                    
                ava @ say "Aaa! [name], don't look!"
                
                player "S-sorry."
                
                hide ava with dissolve
                
                n "She turns away from you and quickly buttons up her shirt."
                
                show ava typical annoyed -reaching at center:
                    ypos y_ava
                with dissolve
                
                ava @ say "You should knock first!"
                
                player "It's my room."
                
                #show ava angry
                
                ava @ say "Still! I could have been nude!"
                
                player "Is that foreshadowing?"
                
                show ava angry
                
                ava @ say "No!"
                
                player "Dang."
                
                show ava typical happy
                
                ava @ say "I came here for friendly clothes-on cuddling, nothing more."
                
                player "Well then, shall we get to business?"
                
                n "You crawl into bed and Ava lies down next to you, seemingly unsure of what to do next."
                
                ava @ say "I've never done this before..."
                
                player "Really? Me neither."
                
                ava @ say "I guess I'm supposed to..."
                
                n "She tries wrapping her wings around you but she struggles getting the one between the mattress and your body."
                
                show ava annoyed
                
                ava @ say "God dammit why is this so difficult."
                
                player "Here, lemme just..."
                
                n "You try holding onto her but run into the same issue. Once you get your arms around her, the one pinned between her body and the mattress loses bloodflow."
                
                show ava neutral
                
                ava @ say "...This isn't very comfortable is it?"
                
                player "Not really."
                
                show ava concerned
                
                ava @ say "We can just sleep next to each other if you want."
                
                show ava typical happy
                
                player "Deal. Now gimme back my arm before it needs to be amputated."
                
                n "You eventually find a comfortable position facing away from each other but at least you can feel her soft feathers against your skin, which feels nice."
                n "Soon you both fall asleep. Maybe it's because of your bird guardian but you don't have any nightmares."
                
                stop music fadeout 1.0
                
                hide box

                scene bg black with fade

                hide box    

                show bg calendar
                show tfriday at center
                with Dissolve(.5)

                pause .6
                show tforwardslash
                pause .2
                show tbackslash

                pause .7

                #___saturday4
                
                scene bg codadorm with fade

                show box with Dissolve(.2):
                    ypos 0

                play music "audio/ambient/morning birds.ogg" fadein 1.0
                
                if avaPoints >= 3:
                    n "You're woken up earlier than usual by Ava's stirring."
                    n "It's not even daylight out and she's stretching and tweeting."
                    n "She rolls over and rests a wing on you."
                    
                    show ava typical excited at center:
                        ypos y_ava
                        xzoom -1
                        xoffset -175
                    
                    ava @ say "Morning~"
                    
                    show ava happy
                    
                    n "You make an unsatisfied caveman grunt as your natural desire is to sleep in."
                    
                    ava @ say "I don't know why but I'm feeling really refreshed!"
                    
                    show ava overjoyed
                    
                    ava @ say "Perhaps that's the power of snuggles?"
                    
                    player "We weren't even really snuggling."
                    
                    show ava typical happy
                    
                    ava @ say "Yeah but our bodies don't know that! It's the proximity that counts!"
                    
                    player "Next time can we at least not be fully clothed?"
                    
                    ava @ say "Hmm..."
                    
                    show ava overjoyed
                    
                    ava @ say "Sure!"
                    
                    show ava profile shy
                    
                    ava @ say "*If* there's a next time hehe~"
                    
                    player "Wow, you really are in a great mood today."
                    
                    show ava typical overjoyed -
                    
                    ava @ say "Breeee~"
                    ava @ say "I guess I am! Very unusual, isn't it?"
                    
                    player "Must be the endorphins."
                    
                    show ava typical happy
                    
                    ava @ say "Maybe!"
                    ava @ say "Nothing gets me more excited than adventure and yesterday sure was one!"
                    
                    n "Ava hops out of bed and unlocks your window."
                    
                    player "Hey, where are you going?"
                    
                    ava @ say "Got a busy day of shooting ahead of me!"
                    
                    player "With your camera, right?"
                    
                    ava @ say "Of course!"
                    
                    n "She takes a dive through the window. A moment later you see her swoop up into the sky."
                    
                    hide ava with dissolve
                    
                    n "Just like that, she's gone."
                    n "The cuddles were pretty disappointing but the way she smiled at you made your heart skip a beat."
                    
                    jump ch2End
                    
                else:
                    n "You're woken up earlier than usual by Ava's stirring."
                    n "It's not even daylight out and she's stretching and chirping."
                    
                    show ava typical happy at center:
                        ypos y_ava
                        xzoom -1
                        xoffset -175
                    
                    ava @ say "Morning."
                    
                    n "You make an unsatisfied caveman grunt as your natural desire is to sleep in."
                    n "Ava gets up and awkwardly wanders around the room, yawning."
                    
                    show ava embarrassed
                    
                    ava @ say "Did you... enjoy the snuggles?"
                    
                    player "Mhm."
                    
                    show ava concerned
                    
                    ava @ say "How's your ankle?"
                    
                    player "Hurts less today."
                    
                    ava @ say "That's good. You just gonna stay in bed all day?"
                    
                    n "You take a look at the clock on your phone."
                    
                    player "Only probably for another 4 hours or so."
                    
                    show ava annoyed
                    
                    ava @ say "Well I'm gonna go out and find a good place to take some shots before the sun comes up."
                    
                    player "Have fun with that!"
                    
                    hide ava with dissolve
                    
                    n "You roll over and bury your face in your pillow."
                    n "Wait, is she mad at you or something?"
                    n "Your sleepy brain is too slow to react. She already opened the window and flew out, leaving a cool draft to chill your bones."
                    n "Too tired to get up and close the window, you pull up your blanket over your head and fall back to sleep for a few hours."
                    
                    scene bg black with dissolve
                    
                    pause .8
                    
                    scene bg codadorm with dissolve
                    
                    show box:
                        ypos 0
                    
                    n "The sun has come up and you're fully- er, mostly rested."
                    
                    jump ch2End
                        
                    #"We can all snuggle together at my place":
                    #    player "Hey that's a great idea! We can all snuggle at my dorm."
                    #    
                    #    show ava waitwhat
                    #    
                    #    ava @ say "A-all three of us??"
                    #    ava @ say "Uhh you sure that's a good idea?"
                    #    
                    #    n "Gunner shrugs."
                    #    
                    #    gunner @ say "Eh, I'll take what I can get. I'm game."
                    #    
                    #    show ava angry
                    #    
                    #    ava @ say "W-well I'm not gonna just let you and Gunner have all the fun! I'm going too!"
                    #    
                    #    player "That settles it then! Snuggle party at my dorm!"
                    #    
                    #    show ava concerned
                    #    
                    #    n "Ava and Gunner look at each other with a uncertain expressions."
                    #    
                    #    scene bg codadorm with fade
                    #    
                    #    show box with Dissolve(.2):
                    #        ypos 0
                    #    
                    #    show gunner neutral at center:
                    #        xpos 300
                    #        xzoom -1
                    #    show ava typical neutral at center:
                    #        xpos -300
                    #    with dissolve
                    #    
                    #    gunner @ say "So...."
                    #    
                    #    show ava bored
                    #    
                    #    ava @ say "How are we gonna do this?"
                    #    
                    #    player "Good question. I'm not a pro at this by any means."
                    #    
                    #    show ava typical neutral
                    #    
                    #    n "You sit on your bed and try to recall just what you were thinking when you invited the whole love triangle to cuddle together."
                    #    n "Lost in thought, you don't notice your two snuggle buddies hopping onto the bed on either side of you."
                    #    
                    #    show ava at flipright
                    #    show gunner at flipleft
                    #    
                    #    show ava smile
                    #    
                    #    ava @ say "Let's try this. Just lie down and relax~"
                    #    
                    #    n "Ava gently pushes you onto your back and wraps her soft feathery wings around you."
                    #    n "A moment later, you feel Gunner's fur brushing against you from the other side."
                    #    
                    #    gunner @ say "You alright? You're shaking."
                    #    
                    #    player "Yeah, j-just cold is all..."
                    #    
                    #    n "You've never been so nervous before. You can't even think straight. Was it a mistake to bring Gunner here? Oh god what's he doing?"
                    #    n "You feel his scratchy tongue combing your hair like your some sort of stupid baby kitten who is too dumb to groom yourself." 
                    #    n "Gunner is literally grooming you."
                    #    
                    #    gunner @ say "Purrrr~"
                    #    gunner @ say "Calm down bro, we'll warm ya up~"
                    #    
                    #    n "This is a classic power play by felines."
                    #    n "First they play nice and cuddly to lower your guard, then they start licking you to assert dominance, next he's gonna try and fuck the bird in your bed."
                    #    
                    #    show ava suggestive
                    #    
                    #    ava @ say "Everything alright, [name]?"
                    #    
                    #    show ava smile
                    #    
                    #    player "Y-yeah, I just need to-"
                    #    
                    #    menu:
                    #        player "{cps=0}Y-yeah, I just need to-{/cps}"
                    #        "Turn towards Ava":
                    #            $ avaPoints += 1
                    #            n "You adjust yourself and turn to face Ava, leaving you backside to Gunner."
                    #            n "A risky move, as it puts you in a position of vulnerability, but it also blocks Gunner's path to Ava."
                    #            n "You hold onto Ava tightly, face buried in her plumage."
                    #            
                    #            player "That's better."
                    #            
                    #            show ava flattered
                    #            
                    #            ava @ say "Breee~ This works too~"
                    #            
                    #            n "You can feel Gunner staring daggers at the back of your head."
                    #            n "It doesn't matter though, the bird is in your arms, not his."
                    #            n "In retaliation, he doubles down on brushing your hair with his scratchy cat tongue, purring ever louder and even pulling your hips closer to him."
                    #            n "The prices you pay for love."
                    #            n "And you *know* neither of you are enjoying this, but Ava seems to be all for it."
                    #            
                    #            show ava portrait overjoyed
                    #            
                    #            ava @ say "Heeheehee~ You two are so cute~ *chirp!*"
                    #            
                    #            gunner @ say "*Purrpurrpurrpurrpurrpurr~*"
                    #            
                    #            show ava portrait happy
                    #            
                    #            n "Gunner's going for the humiliation tactic but as long as his paws and tongue are on you, they're not on Ava and that's the best available outcome."
                    #            n "You close your eyes and mentally prepare for an awkward morning."
                    #            n "Somehow you manage to fall asleep amidst the tension running so high."
                    #        "Turn towards Gunner":
                    #            n "It's said that to emerge victorious in war, you must be unpredictable, and that's precisely what you're going for."
                    #            n "You roll onto your side facing Gunner and wrap him in your arms."
                    #            n "Got you now, you son of a bitch!"
                    #            
                    #            gunner @ say "Oh? Whatchya doin' there, bud?"
                    #            
                    #            show ava portrait overjoyed
                    #            
                    #            ava @ say "Ohmygosh this is so hot!"
                    #            
                    #            show ava portrait concerned
                    #            
                    #            ava @ say "I mean, it's so hot in here, right?"
                    #            
                    #            show ava portrait smile
                    #            
                    #            player "Just snuggling with my bro. Nothing wrong with that, is there?"
                    #            
                    #            n "You pull him in so tight he won't even think about escaping."
                    #            
                    #            gunner @ say "N-no, of course not!"
                    #            
                    #            n "He gives you a lick with his rough tongue on your face and digs his claws into your side."
                    #            n "Better you than Ava you suppose."
                    #            n "At least she's enjoying the show."
                    #            
                    #            ava @ say "You two are so cute~"
                    #            
                    #            n "You feel her nuzzle the back of your head and lay her wing on top of you. You make sure Gunner's paw gets nowhere near it."
                    #            n "You close your eyes and mentally prepare for an awkward morning."
                    #            n "Somehow you manage to fall asleep amidst the tension running so high."
                    #            
                    #    stop music fadeout .7
                    #            
                    #    scene bg codadorm with fade
                    #    
                    #    show box with Dissolve(.2):
                    #        ypos 0
                    #    
                    #    play music "audio/ambient/morning birds.ogg" fadein 1.5
                    #    
                    #    n "When your consciousness begins to reboot the following day, you question whether yesterday's events were just a dream until you realize you have a bird in your arms."
                    #    n "And then comes the nightmarish reality that is a snoozing Gunner inches from your face."
                    #    n "Somehow in the middle of the night you and Ava switched position so that she was in the middle of you two."
                    #    n "You guess this round of flirting with Ava ended up being a draw."
                    #    
                    #    show ava typical neutral at center:
                    #        xpos -200
                    #        xzoom -1
                    #    with dissolve
                    #    
                    #    ava @ say "*Yaaawn~*"
                    #    ava @ say "Morning~"
                    #    
                    #    player "Sleep well?"
                    #    
                    #    show ava overjoyed
                    #    
                    #    ava @ say "Amazingly well!"
                    #    
                    #    show ava typical neutral
                    #    
                    #    ava @ say "How's your ankle?"
                    #    
                    #    player "Fine, I think."
                    #    
                    #    n "You pull the blanket away and set foot on the floor."
                    #    n "It's still painful but you can deal with it."
                    #    n "Gunner begins to stir, stetching out his arms and yawning."
                    #    
                    #    show gunner neutral at center:
                    #        xpos 200
                    #    with dissolve
                    #    
                    #    gunner @ say "Morning cutie~"
                    #    gunner @ say "Oh hey [name], didn't see ya there."
                    #    gunner @ say "Man, they really hooked you up with the best everything in here huh? Your bed is so much softer than the one in my dorm."
                    #    
                    #    player "Yeah well don't get used to sleeping in it. My ankle's all better so you can go home now."
                    #    
                    #    gunner @ say "Oof, kicking us out so soon? Was I not a good snuggler?"
                    #    
                    #    ava @ say "You were pretty good! Both of you were!"
                    #    
                    #    player "Sorry, I've just got a busy day ahead of me."
                    #    
                    #    gunner @ say "That's alright, we'll head out soon. Thanks for having us over~"
                    #    
                    #    n "Gunner purrs and gives you a playful lick, surely an attempt to intimidate you, as he gets out of bed."
                    #    
                    #    gunner @ say "If either of you need top tier snuggles again, you know where to find me~"
                    #    
                    #    ava @ say "I'll keep both of you in mind~"
                    #    
                    #    player "See you two later."
                    #    
                    #    hide gunner
                    #    hide ava
                    #    with dissolve
                    #    
                    #    
                    #            
                    #            
                    #    
                    #    #"gunner snuggles behind you. you're starting to regret this"
                    #
                    #
                    #    #gunner licks ava and you
                    #    
                    #"Spill your spaghetti":
                    #    player "N-no thanks, that's what my tulpa waifu is for."
                    #    
                    #    #ava @ say "Do you wanna snuggle Gunner instead?"
                    #    
                    #    show ava waitwhat
                    #
                    #    ava @ say "You have a tulpa?"
                    #
                    #    n "Fuck, why did you say that?"
                    #
                    #    ava @ say "That's so cool!"
                    #
                    #    player "Really?"
                    #    
                    #    show ava overjoyed
                    #    
                    #    ava @ say "You should tell me about her!"
                    #    
                    #    player "M-maybe later..."
                    #    
                    #    n "Great, now you have to make up a schizo imaginary girlfriend to impress Ava."
                    #    n "Or make her jealous."
                    #    
                    #    show ava typical neutral
                    #    
                    #    player "Let's get out of this hospital first. I'm already sick of being here."
                    #    
                    #    gunner @ say "Agreed."
                    #    
                    #    hide gunner
                    #    hide ava
                    #    with dissolve
                    #    
                    #    n "Ava and Gunner walk you back to your dorm. Ava asks if you're sure you don't need a snuggle buddy but you're still too ashamed from before to take her up on the offer."
                    #    n "That and you don't want Gunner to break your other ankle tonight."
                    #    n "Thankfully he acts pretty chill on the way back, and you all make light of the events of the day."
                    #    n "After what you've been through, it's nice to ease up a little."
                    #    n "Your ankle still kinda hurts but you make it back to your dorm and get into bed, texting your friends until you fall into slumber."
                    #    
                    #    stop music fadeout 1.0
                    #    
                    #    scene bg black with fade
                    #
                    #    hide box    
                    #
                    #    show bg calendar
                    #    show tfriday at center
                    #    with Dissolve(.5)
                    #
                    #    pause .6
                    #    show tforwardslash
                    #    pause .2
                    #    show tbackslash
                    #
                    #    pause .7

        #___saturday4

        scene bg codadorm with fade

        show box with Dissolve(.2):
            ypos 0

        play music "audio/ambient/morning birds.ogg" fadein 1.0
        
        jump ch2End

    
    elif gunnerRaid == True:
        n "And you have some animal panties to raid."
        n "Gunner said he wanted to meet up to start scouting out potential targets today."
        
        scene bg campus with fade
        
        play music "audio/music/vylet - wish.ogg" fadein 1.0
        
        show box with Dissolve(.2):
            ypos 0
            
        show gunner neutral at center:
            ypos y_gunner
            xzoom -1
            xoffset -500
        show rori neutral at center:
            ypos y_rori
            xoffset 450
        with dissolve
            
        gunner @ say "Gentlemen, we have assembled here today for the most noble of goals."
        gunner @ say "We are united in our mission to secure women's panties for the 200 year tradition of Harmonia."
        gunner @ say "Former presidents of this fine nation have lead such glorious raids here in the past and it is our honor - nay, our *duty* - to carry that torch into a brighter future!"
        gunner @ say "Oohrah!"
        
        show rori sleepy
        
        rori @ say "Meh."
        
        player "Cool so who are we raiding?"
        
        gunner @ say "That's what we're here to find out. Any suggestions?"

        rori @ say "I seriously don't care."
        
        show gunner optimistic
        
        gunner @ say "I'm liking the enthusiasm! We'll definitely put that into consideration!"
        
        n "Gunner is desperately trying to keep this event upbeat and fun."
        
        show gunner neutral
        
        gunner @ say "What about you, [name]? Got any preferences?"
        
        menu:
            gunner "{cps=0}What about you, [name]? Got any preferences?{/cps}"
            "Rose":
                player "There's this raccoon bitch named Rose in my history class..."
                
                gunner @ say "I think I've seen her before. She probably deserves it."
                gunner @ say "One problem though: we can only really do this to sorority girls. It's like codified in the traditions and I don't think Rose is in a sorority."
                
                player "What the fuck? I don't know many sorority girls. That limits us to just..."
                
                gunner @ say "Claire?"
                
                show gunner charming
                
                n "A devious grin creeps up on Gunner's face."
                
                gunner @ say "This is where it gets interesting. There's a loophole in the system."
                gunner @ say "If we raid Claire's room, nobody can blame us if we get a little mixed up."
            "Mishka":
                player "So hear me out... Mishka?"
                
                gunner @ say "Interesting choice, I didn't expect that from you."
                gunner @ say "But I don't think she lives on campus dude. We're safe only as long as we stay on uni grounds. Outside of that it's like felony level breaking and entering."
                gunner @ say "In fact, we're only supposed to be able to do this to girls who are in a sorority."
                
                player "What the fuck? I don't know many sorority girls. That limits us to just..."
                
                gunner @ say "Claire?"
                
                show gunner charming
                
                n "A devious grin creeps up on Gunner's face."
                
                gunner @ say "This is where it gets interesting. There's a loophole in the system."
                gunner @ say "If we raid Claire's room, nobody can blame us if we get a little mixed up."
            "Miss Ellen":
                player "Haha wouldn't it be funny if we nabbed my literature professor's knickers haha I bet nobody's done that before."
                
                gunner @ say "Sounds epic but she probably lives off campus. We're safe only as long as we stay on uni grounds. Outside of that it's like felony level breaking and entering."
                gunner @ say "In fact, we're only supposed to be able to do this to girls who are in a sorority."
                
                player "What the fuck? I don't know many sorority girls. That limits us to just..."
                
                gunner @ say "Claire?"
                
                show gunner charming
                
                n "A devious grin creeps up on Gunner's face."
                
                gunner @ say "This is where it gets interesting. There's a loophole in the system."
                gunner @ say "If we raid Claire's room, nobody can blame us if we get a little mixed up."
            "No idea":
                player "I got nothing."
                
                gunner @ say "Great! I mean, I just had one in mind and if you two don't have any objections..."
                
                rori @ say "Is it that bird girl you're always gooning over?"
                
                gunner @ say "Whoa are you psychic or something?"
                
                rori @ say "Just a lucky guess."
                
                gunner @ say "It's a bit of a legal grey area 'cause we're only really allowed to raid sorority girls' panties and Ava's not in one."
                gunner @ say "But she's roommates with someone who *is.*"
                gunner @ say "You see where I'm going with this?"
                
        player "So we raid Claire's dorm and take whatever we find?"
        
        gunner @ say "Precisely."
        
        show rori concerned
        show gunner optimistic
        
        rori @ say "I still don't know about this."
        
        player "How are we supposed to get in anyway? It's not like we can waltz in in broad daylight, pick the lock and break in."
        
        show rori worried noblush
        
        rori @ say "Yeah, boys aren't even allowed in the girls' dorm building without being accompanied by a resident."
        rori @ say "And even then there's a curfew."
        
        show rori concerned
        
        gunner @ say "Right, so I'm thinking we scout out the girls' dorm, find out the exact time when the guard shift changes, that'll be our best chance to sneak in and-"
        
        show gunner neutral
        
        player "Why don't we just ask Claire for help? She'd probably be down."
        
        gunner @ say "You think so??"
        
        player "Yeah lemme text her."
        
        call phone_start from _call_phone_start

        call message_start("me", "Sup Claire", "testimage.png") from _call_message_start
        call reply_message("Can you do me and the boys") from _call_reply_message 
        call reply_message("A favor?") from _call_reply_message_1 

        call message("Claire", "You got me excited before that linebreak", "claireavi.png") from _call_message 
        call message("Claire", "But sure what's up?", "claireavi.png") from _call_message_1 

        call reply_message("We need to get into the girls' dorm tomorrow night") from _call_reply_message_2 
        call reply_message("You know a way for us to get in?") from _call_reply_message_3 

        call message("Claire", "Hmmm", "claireavi.png") from _call_message_2 
        call message("Claire", "I can't bring you in at night :/", "claireavi.png") from _call_message_3 
        call message("Claire", "Even if I could, Imma be busy tomorro", "claireavi.png") from _call_message_4 
        call message("Claire", "BUT", "claireavi.png") from _call_message_5 
        call message("Claire", "I bet I could unlock a window for you~", "claireavi.png") from _call_message_7 
        
        call reply_message("Perfect!") from _call_reply_message_4 
        call reply_message("You're the best :3") from _call_reply_message_6 
        call reply_message("One more thing") from _call_reply_message_7 
        call reply_message("could you leave your dorm key by the window") from _call_reply_message_18 
        
        call message("Claire", "Ksksksks anything for you~", "claireavi.png") from _call_message_19 
        call message("Claire", "I gotta ask something in return tho", "claireavi.png") from _call_message_20 
        
        call reply_message("Oh?") from _call_reply_message_19 
        call reply_message("I suppose that's fair.") from _call_reply_message_20 
        
        call message("Claire", "Ksksksks let's just say I'm gonna need to borrow you once you're done~", "claireavi.png") from _call_message_21 
        
        call reply_message("W-what for?") from _call_reply_message_21 
        
        call message("Claire", "Nothing too spicy I promise!", "claireavi.png") from _call_message_22 
        call message("Claire", "Just wanna introduce you to the girls :3c", "claireavi.png") from _call_message_23 
        
        call reply_message("Hmm") from _call_reply_message_22 
        call reply_message("Ok deal") from _call_reply_message_23 

        call phone_end from _call_phone_end 
            
        gunner @ say "Well? What did she say?"
        
        player "She'll leave a window open and leave her dorm key for us."
        player "But I won't be able to stick around and celebrate once the job is done."
        player "She wants me to hang out with a bunch of girls that night."
        
        gunner @ say "Thanks for taking one for the team."
        
        show rori neutral
        
        rori @ say "So is that it then? Scouting mission accomplished? Can we go home now?"
            
        show gunner cheeky1    
        
        gunner @ say "Yeah. Briefing complete, you're dismissed!"
        
        show rori sleepy
        
        rori @ say "Good. I'm gonna spend the rest of the night playing VR Cat."
        
        player "I'm starting to get excited for this. It's actually happening!"
        
        show gunner determined
        
        gunner @ say "Nothing's gonna stop us from getting our paws on some bird panties!"
        gunner @ say "Rest up boys, we've got a heist to pull off tomorrow!"
        
        hide gunner
        hide rori
        with dissolve
        
        n "Your little group disbands for the day, each contemplating this raid will change your lives."
        
        stop music fadeout 2.0
        
        scene bg black with fade

        hide box

        show bg calendar
        show tfriday at center
        with Dissolve(.5)

        pause .6
        show tforwardslash
        pause .2
        show tbackslash

        pause .7

        scene bg codadorm with fade
        
        play music "audio/music/vylet - tenderness.ogg" fadein 1.0
        
        show box with Dissolve(.2):
            ypos 0    
        
        n "Today's the day."
        n "Your phone buzzes. You've got a message about Rori."
        n "He better not be trying to weasel out of this raid."
        
        call phone_start from _call_phone_start_5
        
        call message_start("Rori", "Hey [name] I'm not really feeling good today", "roriavi.png") from _call_message_start_5
        call message("Rori", "Can we all just stay in and play video games instead?", "roriavi.png") from _call_message_24 
        
        call reply_message("Are you worried about getting caught?") from _call_reply_message_24 
        
        call message("Rori", "A little", "roriavi.png") from _call_message_25 
        call message("Rori", "But more concerned about the moral implications", "roriavi.png") from _call_message_27 
        call message("Rori", "of breaking into a stranger's residence", "roriavi.png") from _call_message_28 
        call message("Rori", "and stealing their underwear", "roriavi.png") from _call_message_29 
        
        call screen phone_reply("Encourage","choiceEncourage","Sympathize","choiceSympathize")
        
        label choiceEncourage:
            call phone_after_menu from _call_phone_after_menu
            
            call message_start("me", "Come on where's your sense of adventure?", "testimage.png") from _call_message_start_6
            call reply_message("This is supposed to be fun and exciting!") from _call_reply_message_25 
            
            call message("Rori", "I guess", "roriavi.png") from _call_message_30 
            call message("Rori", "I just don't have the same sense of adventure as you and Gunner do", "roriavi.png") from _call_message_31 
            
            call reply_message("It's all in your head bro") from _call_reply_message_46 
            call reply_message("just imagine you're in an rpg or vn") from _call_reply_message_71 
            call reply_message("and you're on a quest for a key item") from _call_reply_message_72 
            
            call message("Rori", "Hmm", "roriavi.png") from _call_message_32 
            call message("Rori", "I'll try", "roriavi.png") from _call_message_33 
            call message("Rori", "But I'm not a fan of forced stealth segments", "roriavi.png") from _call_message_34 
            
            call reply_message("We'll be quick, in and out") from _call_reply_message_73 
            
            call message("Rori", "Okayyyy", "roriavi.png") from _call_message_35 
            call message("Rori", "I'm not touching any panties though", "roriavi.png") from _call_message_93 
            
            call reply_message("As you wish") from _call_reply_message_74 
            
            call phone_end from _call_phone_end_5
            
            jump raidStart
        
        label choiceSympathize:
            $ roriPoints =+ 1
            
            call phone_after_menu from _call_phone_after_menu_1
            
            call message_start("me", "I get what you mean but I'm pretty sure Claire is into this", "testimage.png") from _call_message_start_7
            
            call message("Rori", "What about Ava?", "roriavi.png") from _call_message_94 
            
            call reply_message("I think she has a crush on Gunner so I don't think she minds either") from _call_reply_message_75 
            
            call message("Rori", "Wait so this is all just one big breaking and entering LARP?", "roriavi.png") from _call_message_95 
            
            call reply_message("Pretty much") from _call_reply_message_76 
            
            call message("Rori", "Courtship rituals are weird man", "roriavi.png") from _call_message_96 
            call message("Rori", "If I wanted to bang someone I'd just invite them over to play vidya or something", "roriavi.png") from _call_message_97 
        
            call reply_message("ikr but this is how straight people work") from _call_reply_message_78 
            
            call message("Rori", "Okayyyy", "roriavi.png") from _call_message_98 
            call message("Rori", "I'll go along with it", "roriavi.png") from _call_message_101 
            call message("Rori", "But I'm not touching any panties", "roriavi.png") from _call_message_102 
            
            call reply_message("As you wish") from _call_reply_message_79 
        
            call phone_end from _call_phone_end_10
            
            jump raidStart
    
        label raidStart:
            n "The hours pass and your anticipation grows. Your mind starts to wander, thinking about all the things that could go wrong."
            n "But also all the things that could go right."
            n "The feeling of victory and conquest waiting for you at the end."
            n "How could you resist?"
            
            call phone_start from _call_phone_start_9

            call message_start("Gunner", "You ready?", "gunneravi.png") from _call_message_start_13
            
            call reply_message("You know it") from _call_reply_message_81 
            
            call message("Gunner", "Good", "gunneravi.png") from _call_message_104 
            call message("Gunner", "It'll get dark out soon", "gunneravi.png") from _call_message_105 
            call message("Gunner", "And all the sluts will leave their dorm to get drunk and go be whores", "gunneravi.png") from _call_message_109 
            call message("Gunner", "Except for Ava, she's pure", "gunneravi.png") from _call_message_110 
            call message("Gunner", "But she'll be out too, going on a night flight", "gunneravi.png") from _call_message_111 
            call message("Gunner", "Meet me outside her dorm building", "gunneravi.png") from _call_message_112 
            
            call reply_message("k see you there") from _call_reply_message_83 
            
            call message("Gunner", "Godspeed", "gunneravi.png") from _call_message_113 
            
            call phone_end from _call_phone_end_11
            
            n "It's now or never."
            
            stop music fadeout 2.0
            
            scene bg campus with fade
                
            show box with Dissolve(.2):
                ypos 0
                
            play music "audio/ambient/outdoors night crickets.ogg" fadein 1.5
            
            n "You walk along the pathway encircling the girls' dorm, trying to appear casual while taking quick side glances at the building."
            n "A voice in the bushes calls out to you."
            
            gunner "Psst! Over here!"
            
            n "You look around to make sure nobody's watching, then swiftly steer yourself into the foliage."
            n "In the darkness, nobody can see you here. You can barely even see Gunner and Rori."
            
            show gunner neutral at center:
                ypos y_gunner
                xoffset 500
            show rori neutral at center:
                ypos y_rori
                xzoom -1
                xoffset -500
            with dissolve
            
            n "He speaks in a hushed tone."
            
            show gunner determined
            
            gunner @ say "You made it!"
            
            rori @ say "Now that everyone is present and accounted for, can we hurry this along?"
            
            show rori worried
            
            rori @ say "I feel so vulnerable just sitting here."
            
            player "Relax, I couldn't see you at all. It's too dark here."
            
            show rori concerned
            
            rori @ say "So you say, but humans don't have particularly good night vision."
            
            show gunner frown1
            
            gunner @ say "Rori's right, we need to be quick, quiet, and careful."
            
            show gunner neutral
            
            gunner @ say "Follow me."
            
            hide gunner
            hide rori
            with dissolve
            
            n "The three of you sneak around to the side of the building where a tall window on each floor is embedded into the wall."
            n "Inside you can see a dimly lit stairwell. A pair of girls are making their way down now, dressed up for the night and unaware of your presence."
            n "The window is higher up than you expected but Gunner jumps up and clings to the ledge with ease."
            n "He pushes it up and climbs inside, then helps you and Rori up."
            
            ###choose who goes into the building first
                #rori is the tallest but gunner doesn't need help jumping up. or you can go in
                
            stop music fadeout 2.0
            
            scene bg oldhospital
            
            show box with Dissolve(.2):
                ypos 0
                
            play music "audio/ambient/spooky.ogg" fadein 1.5            
            
            n "The interior is so dilapidated, you could mistake it for being abandoned, or perhaps a crack den."
            
            show gunner neutral at center:
                ypos y_gunner
                xoffset 500
            show rori neutral at center:
                ypos y_rori
                xzoom -1
                xoffset -500
            with dissolve
            
            show gunner disgusted
            
            gunner @ say "Damn, these bitches live like this?"
            
            show gunner optimistic
            
            rori @ say "Did you grab the key?"
            
            show gunner determined
            
            gunner @ say "Got it right here."
            
            player "Now we just have to find Ava's dorm."
            
            show gunner neutral
            
            gunner @ say "Come on, it's this way."
            
            n "Gunner leads you down the hall. You can hear girls giggling and walking on the floor above you."
            n "He stops at a door and inserts the key into the lock."
            
            gunner @ say "Bingo."
            
            stop music fadeout 2.0
            
            scene bg avadorm with dissolve
            
            play music "audio/music/vylet - dance of the macabre.ogg" fadein 1.0
            
            show box with Dissolve(.2):
                ypos 0
                
            n "In the darkness, you can barely make out any details."
            
            show gunner neutral at center:
                ypos y_gunner
                xoffset 500
            show rori neutral at center:
                ypos y_rori
                xzoom -1
                xoffset -500
            with dissolve
            
            gunner @ say "Leave the lights off! We don't wanna draw any attention."
            
            show rori concerned blushing
            
            rori @ say "You guys look around and I'll uh"
            
            show rori anxious 
            
            rori @ say "Keep watch I guess."
            
            hide rori with dissolve
            
            n "Rori goes to stand guard by the door while you and Gunner locate the drawers and begin sifting through them."
            n "Your fingers run across the smooth fabric of cotton shirts and denim pants, searching for silk panties."
            n "Finally inside the bottom drawer you feel it."
            n "But something isn't right."
            n "This is way too large to fit around Ava's tiny waist."
            n "Gunner snickers at you and holds up a cute pair of pastel pink panties that only Ava could fit into."
            
            show gunner motivated
            
            gunner @ say "Looks like you found the jackpot heheh!"
            
            menu:
                gunner "{cps=0}Looks like you found the jackpot heheh!{/cps}"
                "Take Ava's panties":
                    $ avaPantsu = True
                    $ avaPoints += 1
                    
                    n "You snatch them right from Gunner's paw. He just laughs and grabs another one from the drawer before closing it."
                "Take Claire's panties":
                    $ clairePantsu = True
                    $ clairePoints += 1
                    
                    n "Gunner can keep those, you came here for the real prize. You pull the bunny's bottoms out of the drawer and close it."
                    n "Now that you're holding the entire thing, you can feel how oversized they are. You could probably jump out the window and use this thing as a parachute."
                "Take none":
                    n "One pair is enough for the mission to be considered a success. The glory is shared between you and your cohorts, now all you have to do is escape."
                    
            show gunner neutral
            
            player "Alright we got what we came for. Rori is the hallway clear?"
            
            show rori yawn lookingaway blush at center with dissolve:
                ypos y_rori
                xzoom -1
                xoffset -500
            
            rori @ say "Yeah. Let's get out of here."
            
            n "You all line up at the doorway and file out stealthily, trying to hide your excitement until you're in the clear."
            
            stop music fadeout 2.0
            
            scene bg oldhospital with fade
            
            show box with Dissolve(.2):
                ypos 0    
            
            n "It's eerily quiet."
            n "You're right in the middle of the hall. Should you try going slow and quiet or fast and loud?"
            n "The others are erring on the side of caution for now, choosing to remain vigilant and stealthy. You can see their fur standing up on end."
            n "About a quarter of the way through, a security officer bursts through a doorway and tackles Gunner to the ground."
            
            show gunner disgusted at center with dissolve:
                ypos y_gunner
            
            gunner @ say "Ack! She's got me!"
            gunner @ say "Go! Be free!"
            
            hide gunner with dissolve
            
            n "She's trying to restrain him and cuff his hands but in a last ditch effort he manages to fling Ava's panties into the air."
            n "Spooked by the noise, Rori instinctively jumps over the security guard and runs to the exit. The panties get caught up in his horns."
            n "You try to follow him but the guard grabs you by the ankle as you try jumping over her, causing you to smack back down to the ground."
            n "With his paws cuffed, Gunner gets behind her and uses the chains to put her in a chokehold."
            
            gunner @ say "Now! Run!!!"
            
            n "Distracted, the guard lets you go and turns her attention to Gunner."
            n "You manage to run to the end of the hall and take one last look back."
            n "She's successfully restrained Gunner and is pointing a taser at you."
            n "You barely manage to dive around the corner before she fires, at the cost of you tumbling down the stairwell."
            
            player "Ugh..."
            
            n "You bumped your head on the way down. You can hear the guard's footsteps getting closer as you limp along to the exit window."
            n "You're fading in and out of consciousness when you feel someone grab you by your jacket collar and lift you up."
            
            scene bg black with fade
            
            pause .5
            
            scene bg campus with fade
            
            play music "audio/music/vylet - wish.ogg" fadein 1.0
            
            show box with Dissolve(.2):
                ypos 0
            
            n "As you come to, the first thing you notice are several eyes pointed at you."
            
            trish "Oh my god he's waking up!"
            
            lina "It's about time!"
            
            olivia "Was the mouth to mouth resuscitation really necessary? It wasn't like he was drowning."
            
            n "A more familiar voice joins them."
            
            show claire sweater happy at center with dissolve:
                ypos y_claire
                xzoom -1
            
            claire @ say "Of course it was!"
            claire @ say "See, he's alive now!"
            
            n "Your vision gradually unblurs to reveal Claire and several other girls standing around you."
            
            show claire with move:
                xoffset -720
            
            show trish notext neutral at center:
                ypos y_trish
                xoffset 850
            show lina neutral at center:
                ypos y_lina
                xoffset 130
            show olivia neutral at center:
                ypos y_olivia
                xoffset 450
            with dissolve
            
            olivia @ say "I dunno, he still kinda looks dead to me."
            
            lina @ say "Are you alright? Looks like you took quite the fall!"
            
            trish @ say "He looks like he's into anthro women~"
            
            player "Wha? Where am I? How did I get here?"
            
            claire @ say "Oh don't worry about that!"
            claire @ say "All that matters is your mission was a success!"
            
            show claire leaning suggestive
            
            claire @ say "And now it's time for you to return the favor~"
            
            show claire happy wave
            
            claire @ say "Say hello to my friends from the sorority!"
            
            show olivia at hop
            show trish at hop
            show lina at hop
            
            image bubble1 = "images/speechbubble.png"
            image bubble2 = "images/speechbubble.png"
            image bubble3 = "images/speechbubble.png"
            
            show bubble1:
                xzoom .65
                yzoom .68
                pos (1420,220)
            show bubble2:
                xzoom .9
                yzoom 1
                pos (1070,220)
            show bubble3:
                xzoom .92
                yzoom .92
                pos (800,220)
            
            #$ renpy.show("speechbubble.png",layer = "transient")
            #$ renpy.show("speechbubble.png", layer = "overlay")
            #$ renpy.show("speechbubble.png",layer = "screens")
            
            trish @ say "Hiiiii [name]!~" (multiple=3)
            olivia @ say "Hiiiii [name]!~" (multiple=3)
            lina @ say "Hiiiii [name]!~" (multiple=3)
            
            show claire happy -wave
            
            hide bubble1
            hide bubble2
            hide bubble3
            with dissolve
            
            n "Maybe it's just your headache, but these ladies appear... intimidating in some way."
            n "You face them and give a meager wave."
            
            player "H-hi..."
            
            n "You turn back to Claire."
            
            player "So what did you have in mind?"
            
            show claire sweater giggle -
                
            n "Claire giggles. That can't be a good sign."
            
            claire @ say "Ksksksksks wellllll~"
            claire @ say "You live in that big fancy dorm room all by yourself, don't you?"
            
            player "Uh huh..."
            
            show claire leaning suggestive
            
            claire @ say "And your building is mixed male and female so you don't have any silly curfews for bringing guests of the opposite gender overrrr~"
            
            player "Right..."
            
            show claire derp
            
            claire @ say "So we were just thinking you could let us in and accompany us to your room~"
            claire @ say "Just to like, check it out and stuff~"
            
            player "Sure, that seems innocuous enough."
            
            show claire flustered
            
            claire @ say "Ksksksks thanks [name], I knew we could count on you~"
            
            show claire happy earsup
            
            claire @ say "Alright ladies, let's go!"
            
            n "To your surprise, the mob picks you up and rushes to your dorm while you still try to catch up on what just happened."
            
            stop music fadeout 2.0
            
            scene bg codadorm with fade
            
            play music "audio/music/Vylet Pony - Cozy Pone.ogg" fadein 1.0
            
            show box with Dissolve(.2):
                ypos 0
                
            show trish notext neutral at offscreenleft:
                ypos y_trish
                xzoom -1
                xoffset -200
            show olivia looking at offscreenleft:
                ypos y_olivia
                xzoom -1
                xoffset -1600
            show lina neutral at offscreenleft:
                ypos y_lina
                xzoom -1
                xoffset -700
            show claire sweater happy at offscreenleft:
                ypos y_claire
                xoffset -2000
                xzoom -1
        
            player "So uh yeah this is my dorm. Feel free to make yourselves at home I guess."
            
            show trish notext neutral at offscreenright:
                ypos y_trish
                xoffset 1700
            show olivia looking at offscreenright:
                ypos y_olivia
                xoffset 200
            show lina neutral at offscreenright:
                ypos y_lina
                xoffset 900
            show claire sweater happy at offscreenright:
                ypos y_claire
                xoffset 1000
            with MoveTransition(1.4)
            
            n "The girls push past you and immediately start rummaging around your belongings, digging through piles of laundry and pulling the drawers out of the dresser."
            n "If this is how they treat their home, you can understand the sorry state the girls' dorm was in."
            
            trish @ say "I FOUND IT!!!"
            
            n "All the girls huddle around something."
            n "Hey is that your underwear drawer?"
            n "Before you can intervene, they all snatch a pair and rush out of your room, giggling and screaming with joy."
            
            olivia @ say "Raid successful!"
            
            pause .2
            
            show trish notext neutral at offscreenleft:
                ypos y_trish
                xoffset -200
                xzoom 1
            show olivia looking at offscreenleft:
                ypos y_olivia
                xoffset -1600
                xzoom 1
            show lina neutral at offscreenleft:
                ypos y_lina
                xoffset -700
                xzoom 1
            show claire sweater happy at offscreenleft:
                ypos y_claire
                xoffset -2000
                xzoom 1
            with MoveTransition(1.4)
            
            hide claire
            
            n "Once again, you're knocked to the floor."
            n "All you can see when you get up is Claire with a devilish grin looking down at you."
            
            show claire sweater leaning suggestive at center with dissolve:
                ypos y_claire
            
            claire @ say "Thanks for giving the girls a fun night~"
            
            hide claire with dissolve
            
            n "The bunny plants a smooch on her own paw, then pushes the same paw against your forehead with enough force to knock you back onto your bed."
            n "With your consciousness fading, the last thing you see is Claire's fluffy little cotton ball tail leaving the room and your door slamming shut."
            
            stop music fadeout 2.0
            
            scene bg black with fade
            
            scene bg codadorm with fade
            
            show box with Dissolve(.2):
                ypos 0
                
            n "Your head is still pounding when the sun rises."
            n "Last night felt like a dream."
            
            if avaPantsu == True:
                n "You check your jacket's inner pocket and pull out a silky smooth petite pair of panties that once belonged to Ava."
                n "Last night was a success after all."
                n "But at what cost?"
            if clairePantsu == True:
                n "You check your jacket's inner pocket and pull out a silky smooth humongous pair of panties that once belonged to Claire."
                n "Last night was a success after all."
                n "But at what cost?"
                
            n "You look over to your decimated underwear drawer, still lying miserably, upturned on the floor."
            n "Only a couple of boxers remain. You'll have to go shopping for more soon."
            n "You reach for your phone and check the messages."
            
            call phone_start from _call_phone_start_10

            call message_start("Gunner", "You make it out alive?", "gunneravi.png") from _call_message_start_14
            
            call reply_message("Yeah. You?") from _call_reply_message_84 
            
            call message("Gunner", "Just barely", "gunneravi.png") from _call_message_114 
            call message("Gunner", "Did you see how fucking fat that security guard was??", "gunneravi.png") from _call_message_122 
            call message("Gunner", "I thought she was gonna break my neck when she was kneeling on it", "gunneravi.png") from _call_message_123 
            
            call reply_message("Holy shit lmao") from _call_reply_message_85 
            call reply_message("I'm guessing she let you go?") from _call_reply_message_86 
            
            call message("Gunner", "Yeah I had to spend last night in gay baby jail", "gunneravi.png") from _call_message_132 
            call message("Gunner", "But they let met out like an hour ago", "gunneravi.png") from _call_message_133 
            call message("Gunner", "Said I was lucky I didn't have any contraband on me", "gunneravi.png") from _call_message_134 
            call message("Gunner", "Or I'd be spending the weekend in there at least", "gunneravi.png") from _call_message_135 
            call message("Gunner", "lol", "gunneravi.png") from _call_message_136 
            
            call reply_message("That reminds me, what happened to Rori?") from _call_reply_message_87 
            
            call message("Gunner", "Dunno", "gunneravi.png") from _call_message_137 
            call message("Gunner", "Maybe his homosexuality was cured once he touched those panties", "gunneravi.png") from _call_message_138 
            call message("Gunner", "I'll check in on him", "gunneravi.png") from _call_message_139 
            call message("Gunner", "I'm on my way back to our dorm now", "gunneravi.png") from _call_message_140 
            
            call reply_message("Cool. I'll send him a text.") from _call_reply_message_92 
            
            call phone_end from _call_phone_end_13
            
            n "Let's see what Rori has to say."
            
            call phone_start from _call_phone_start_12
            
            call message_start("me", "Rori where'd you go?", "testimage.png") from _call_message_start_16
            
            call message("Rori", "Where do you think?", "roriavi.png") from _call_message_141 
            call message("Rori", "I went back to my dorm and booted up War Lightning", "roriavi.png") from _call_message_142 
            
            call reply_message("What happened to the panties?") from _call_reply_message_93 
            call reply_message("Last time I saw them they were stuck in your horns") from _call_reply_message_102 
            
            call message("Rori", "Oh those", "roriavi.png") from _call_message_143 
            call message("Rori", "After Gunner got arrested I snuck back in and put them back where we found them", "roriavi.png") from _call_message_144 
            
            call reply_message("DUDE") from _call_reply_message_103 
            call reply_message("Gunner's gonna be pissed") from _call_reply_message_104 
            
            call message("Rori", "I'll just tell him they fell off somewhere", "roriavi.png") from _call_message_145 
            call message("Rori", "It was more about the adventure, wasn't it?", "roriavi.png") from _call_message_146 
            
            call reply_message("Nah I'm pretty sure Gunner was in it for bird pantsu") from _call_reply_message_105 
            
            call message("Rori", "Too bad, he can ask for them direct from Ava if he wants them so bad", "roriavi.png") from _call_message_151 
            
            call reply_message("lol") from _call_reply_message_106 
            call reply_message("u gotta admit tho it was pretty fun") from _call_reply_message_107 
            
            call message("Rori", "Exhilerating? Maybe.", "roriavi.png") from _call_message_152 
            call message("Rori", "Fun? No.", "roriavi.png") from _call_message_154 
            
            call reply_message("You probably would have enjoyed the boxer raid more huh") from _call_reply_message_110 
            
            call message("Rori", "OwO", "roriavi.png") from _call_message_155 
            call message("Rori", "The what?!", "roriavi.png") from _call_message_156 
            
            call reply_message("Claire's sorority tricked me into letting them into my dorm") from _call_reply_message_111 
            call reply_message("And they raided my boxer drawer") from _call_reply_message_112 
            
            call message("Rori", "wow", "roriavi.png") from _call_message_157 
            call message("Rori", "that's uh", "roriavi.png") from _call_message_158 
            call message("Rori", "kinda hot ngl", "roriavi.png") from _call_message_159 
            
            call reply_message("lmao I'll hook you up with them next year") from _call_reply_message_113 
            
            call message("Rori", "UwU", "roriavi.png") from _call_message_160 
            call message("Rori", "I'm glad you didn't die or get arrested", "roriavi.png") from _call_message_161 
            
            call reply_message("same to you") from _call_reply_message_114 
            call reply_message("i just hit my head so I think i'm outta commission for the rest of the weekend") from _call_reply_message_115 
            
            call message("Rori", "Oki", "roriavi.png") from _call_message_162 
            call message("Rori", "I'm just gonna chill too", "roriavi.png") from _call_message_163 
            call message("Rori", "Lemme know if you want me to come over and bring some vidya", "roriavi.png") from _call_message_164 
            
            call reply_message("k") from _call_reply_message_116 
            
            call phone_end from _call_phone_end_14
                
            jump ch2End
        
    else:
        n "At least you can get some extra credit by going to that parade today."
        n "That way you'll be able to work 2\% less hard and still pass your history class, which sounds like a fair tradeoff."

        scene bg town with fade
        
        play music "audio/music/vylet - manehattan's finest.ogg" fadein .5

        show box with Dissolve(.2):
            ypos 0

        n "As you've come to expect, your sense of timing as well as your sense of direction have failed you yet again."
        n "It's way past when the parade was scheduled and you're still stuck on some backroads looking over your shoulder wondering when you'll get shanked."
        n "Maybe you should just call it quits and try going back home, if you can find it that is."
        n "For the nth time, your map app has you pointed in the exact opposite direction you're facing and is telling you to walk in circles for the next two hours."
        n "You have to mentally figure out where you are and plot your own course like it's the fucking 1600s."
        n "Ok, you think you just have to cross this street here then round that corner and it's mostly a straight shot to-"

        rose "What the hell are you doing?!"

        n "You feel someone grab onto the back of your shirt and pull you onto the sidewalk."
        
        player "Hey, get your paws off me!"
        
        n "A moment later a semi truck speeds through the street, right where you had stepped foot a mere fraction of a second ago."
        
        show rose jacket handonhip growling at center with dissolve:
            ypos y_rose

        rose @ say "How dumb are you? You'd be dead if I didn't just save your ass!"

        player "Wha?"

        n "You blink, dumbstruck as your brain replays everything that just happened in slow motion."
        
        show rose jacket armscrossed furious

        rose @ say "Didn't you ever learn to look both ways before crossing?"

        player "I did! The light even said to cross!"

        n "You point to the crosswalk sign, but to your surprise it says \"DO NOT CROSS\""
        n "It turns to white and says to cross a second later."

        player "How the...? I was sure I looked before I crossed!"

        show rose jacket armscrossed dismissive

        rose @ say "Ugh, where's your wrangler when you need them?"

        n "There's no way to respond to that without sounding mad so you just keep quiet."

        rose @ say "Where are you trying to get to anyway? Everywhere is closed for the holiday."

        player "The parade?"

        rose @ say "Ended an hour ago."

        player "I figured. I just wanna go home now."
        
        show rose jacket handonhip annoyed

        rose @ say "*sigh*"
        rose @ say "I know natural selection wants you dead, but letting my project partner die on the streets might affect my grade so..."
        rose @ say "I guess I'm walking you home."

        player "I can walk myself home."
        
        show rose jacket handonhip shy

        rose @ say "You sure? Cause you were going the wrong way. The university is this way."

        player "Fine, if you really wanna take me home so bad you can."

        show rose jacket fistsclenched annoyed

        rose @ say "I don't *want* to walk you home but you obviously can't be trusted to do anything on your own!"

        player "Whatever, just lead the way."

        hide rose with dissolve

        n "Rose scowls and storms off, taking you down streets and alleyways that start to look more familiar as you get closer to campus."
        n "For someone so short she walks pretty quick. You can barely keep up."
        n "She only slows down when a large crowd blocks her way."
        n "When the crowd disperses a lone figure in robes stands in the middle of the sidewalk."
        n "He turns around and looks down at you and Rose."

        show fortune at center with dissolve:
            xoffset -450
            xzoom -1
            ypos y_fortune

        fortune @ say "I've been expecting you."

        player "Huh? Who are you?"

        show rose jacket handonhip dismissive at center with dissolve:
            xzoom -1
            xoffset 420
            ypos y_rose

        rose @ say "He's just some homeless guy."
        rose @ say "Move. You're in the way."
        
        show rose:
            linear .5 xoffset -150    
        pause .08
        show fortune with move:
            xoffset -550
            
        pause .1
        
        show rose with move:
            xoffset 150

        n "Rose tries to walk around him but he steps in her path."

        fortune @ say "Homeless I am not. The world is my home."
        
        show rose jacket handonhip growling

        rose @ say "Even worse than homeless, this guy's a hippie."
        #Oh he's worse than I thought, he's a hippie."

        n "Rose tries once more to maneuver around him, but it's almost like he knows which direction she'll go before she does."
        
        show rose:
            linear .4 xoffset -250    
        pause .1
        show fortune with move:
            xoffset -659
            
        pause .3
        
        show rose:
            linear .5 xoffset 200
        pause .1
        show fortune with move:
            xoffset -450
        
        show rose jacket handonhip furious

        rose @ say "Get out of the way!"

        #rose @ say "You're starting to piss me off. Move or you'll regret it!"
        
        show rose jacket fistsclenched angry knife
        
        n "Rose pulls something out from her pocket out of view of the hobo and holds it concealed in her clenched fist."
        n "Is that a... knife?"

        fortune @ say "Your blade does not deter me. I have seen the future. You are all bark and no bite."

        n "Rose grips her knife tighter."

        rose @ say "What do you want? Money? Nobody carries cash anymore."
        
        #fortune "I have no need for money, everything I work with is free."
        fortune @ say "I am merely one of fate's messengers."
        fortune @ say "You may decline to hear your fortune if you wish, but it will reach you one way or another, sooner or later."
        #fortune teller gives rose a false fortune, knowing that she doesn't pay?
        
        show rose armscrossed dismissive

        rose @ say "I'll decline your \'fortune\' thank you."
        rose @ say "Come on, [name], I'm not sticking around."

        n "Rose starts to walk across the street to the other sidewalk."
        
        pause .1
        
        show rose:
            xoffset -600
        show fortune:
            xoffset 160
        with move

        menu:
            n "{cps=0}Rose starts to walk across the street to the other sidewalk.{/cps}"
            "Aw come on, I wanna hear my fortune!":
                player "Aw come on, I at least wanna hear my fortune!"
                
                show rose handonhip annoyed at flipleft

                rose @ say "Why? He's just gonna make up some bullshit."
                rose @ say "Here's my fortune: I'm gonna walk back to campus without you and you'll get hit by a car and die."

                fortune @ say "Wrong."

                #rose @ say "What did you say?"

                fortune @ say "[name] will not perish today. Nor tomorrow, nor the next day."
                fortune @ say "There is something special about you. Your fate diverges. It is not yet sealed."
                fortune @ say "It seems you have a mission in life to be completed before you pass away."

                player "Wait, so I'm not dying?"

                fortune @ say "Not yet."
                
                show rose dismissive

                rose @ say "Could you be any more vague?"

                player "Rose, this guy might be legit! He knew my name and I didn't even tell him!"
                
                show rose fistsclenched angry

                rose @ say "He probably just overheard me saying it!"

                fortune @ say "Your fate is also divergent, Rose."

                player "See, he even knows your name too!"

                show rose angry

                rose @ say "Because you just said it!"

                fortune @ say "Perhaps your destiny is related to [name]'s? Unfortunately, I cannot give definitive answers for such people."

                show rose armscrossed dismissive

                rose @ say "What a great fortune teller you are."
                rose @ say "Now if you're done, we'll be on our way."

                fortune @ say "There is more. I can see several potential destinies and the paths you may take to reach them."
                fortune @ say "For a small donation I will-"

                rose @ say "Forget it. Like I said, nobody carries cash anymore, boomer."
                
                fortune @ say "I take etherium. My wallet address is 0x1AF7aD03CbB3e40a55392D518D585eA3EBB8F4B8."
                
                rose @ say "Cryptocurrency is fake and g- "
                
                n "A nearby truck drives by and honks it's horn, cutting off the end of Rose's sentence before she walks off."
                
                show rose at flipright
                    
                pause .2

                show rose with move:
                    xoffset -1500
                    
                pause .1
                
                show fortune with move:
                    xoffset 0

                #n "Rose waits for an opening in traffic and crosses the street."

                fortune @ say "Ah of course. You zoomers will donate to millionaire streamers and girls taking photos of their hooves in bad lighting but won't even consider giving to the needy?"

                player "Sorry, I don't have any cash either."
                
                fortune @ say "What about that bill you're carrying in your back pocket?"

                player "What? I don't have a-"

                n "You reach into your pocket and to your surprise pull out a five dollar bill."

                fortune @ say "You have history with that young lady, don't you?"

                player "Not really? I only just met her recently and- oh you mean history class?"

                n "The fortune teller smiles and winks."

                fortune @ say "I think I know how you can have a future with her as well."

                n "Give money to the fortune teller?"

                menu:
                    n "{cps=0}Give money to the fortune teller?{/cps}"
                    "Yes":
                        $ gnugift = True
                        $ moneySpent =+ 5
                        
                        n "You won't be any poorer for giving him the money since you didn't realize you had it in the first place."
                        n "You hand over the crumpled bill and await the wisdom of the gnu."
                        n "He leans over and takes it with his teeth and begins chewing on it."
                        n "With your hand still extended, he grabs hold of it and places something in your palm and wrapping your fingers around it."

                        fortune @ say "Carry that with you. You'll need it someday soon."

                        n "With that, the gnu steps back and into the shadows."

                        hide fortune with dissolve

                        n "You unclench your fist and look down at what he gave you."
                        n "It's a short cable with a USB C connector at one end and a headphone jack input on the other."
                        n "What the hell kind of puzzle game bullshit is this?"
                        n "You look up with a confused expression, about to ask what this is for but the fortune teller is nowhere to be found."
                    "No":
                        player "Thanks but I'd rather let it come as a surprise."

                        fortune @ say "Fair enough. I won't keep you any longer."

                        n "The gnu steps back and into the shadows."

                        hide fortune with dissolve

                        n "Man, that was weird."
                        n "But at least you came out five dollars richer than you thought you were."

                n "You look around for Rose and see her among a crowd of people waiting for the next crosswalk light."

                player "Hey, wait up!"

                n "You chase after her, narrowly avoiding getting hit by a car as you jog across the street."
                n "Rose glares at you and shakes her head."
                
            "Yeah, let's bail":
                player "Yeah, let's get away from this weirdo."
                
                rose @ say "Come on, hurry up."
                
                pause .1
                
                show rose with move:
                    xoffset -1800

                fortune @ say "As you wish. I won't keep you from your fate any longer."

                n "The gnu steps back and into the shadows."

                hide fortune with dissolve

                n "You follow Rose, looking over your shoulder."
                n "Luckily that creepy gnu isn't following you."
                n "In fact, it's like he vanished into thin air."

        n "When you get close to the campus, Rose chases you away with some colorful vocabulary and you hurry back to your dorm, ready for a nice long sleep."
        
        stop music fadeout 1.0

        scene bg codadorm with fade

        show box:
            ypos 0

        n "Drained from today's excursion, you flop onto your bed and pull up the covers, falling asleep quickly."

        hide box

        scene bg black with fade

        hide box    

        show bg calendar
        show tfriday at center
        with Dissolve(.5)

        pause .6
        show tforwardslash
        pause .2
        show tbackslash

        pause .7

        scene bg codadorm with fade

        show box with Dissolve(.2):
            ypos 0
        
        if mishkaMall == True:
            n "Today's the day you finally get to hang out with Mishka."
            n "You put on your nicest casual clothes and head out."
        
            scene bg mall with fade
            
            play music "audio/music/vylet - earnest (feat. Sylver Stripe & Namii).ogg" fadein 1.0
            
            show box with Dissolve(.2):
                ypos 0
                
            n "When you arrive, it feels like you've stepped into some sort of corporate cemetary full of zombies trudging from shop to shop to look at cheaply made goods."
            n "It's not at all like how TV shows portrayed it."
            n "You look around for the barista rat and find her sitting on a bench in the center of the building."
            n "She's looking around at the various shops and decorations, clearly overwhelmed."
            
            player "Mishka!"
            
            n "She jumps, startled by your sudden appearance."
            
            show mishka anxious neutral at center with dissolve:
                ypos y_mishka
                
            mishka @ say "Oh! [name] it's just you."
            mishka @ say "Sorry, I'm kinda nervous. There's so many people and it's noisy and the lighting is kinda harsh and-"
            mishka @ say "Sorry! I don't mean to sound like I don't want to be here!"
            
            player "It's alright, malls always feel kinda alien."
            player "I'm glad you're here, I didn't wanna come here alone either."
            player "Do you wanna explore a bit?"
            
            n "She stands up."
            
            mishka @ say "Dah!"
            
            n "She walks along side you, the both of you constantly swiveling your heads to look into the colorful stores."
            
            #mishka @ say "I didn't really go into any shops last time."            
        else:
            n "What should you do with the rest of your long weekend?"
            n "Your friends are busy so you're on your own today."
            n "Hmm, there was that mall you passed by yesterday you thought about checking out."
            n "That's as good a place as any other. Off you go."
            
            scene bg mall with fade
            
            play music "audio/music/vylet - earnest (feat. Sylver Stripe & Namii).ogg" fadein 1.0
            
            show box with Dissolve(.2):
                ypos 0

            n "When you arrive, it feels like you've stepped into some sort of corporate cemetary full of zombies trudging from shop to shop to look at cheaply made goods."
            n "It's not at all like how TV shows portrayed it."
            n "Wait, who's that sitting on the bench?"
            n "No way, she's the last person you'd expect to find here."
            
            player "Mishka!"
            
            n "She jumps, startled by your sudden appearance."
            
            show mishka anxious neutral at center with dissolve:
                ypos y_mishka
                
            mishka @ say "Oh! [name] it's just you."
            
            show mishka nervous
            
            mishka @ say "Sorry, I'm kinda nervous. There's so many people and it's noisy and the lighting is kinda harsh and-"

            player "Didn't think I'd see you here. You meeting up with someone?"
            
            show mishka happy -nervous -anxious
            
            mishka @ say "No, I just came here on a whim today."
            
            show mishka neutral
            
            mishka @ say "I don't know why, the thought just popped into my head to try going to a mall. It's my first time at one!"
        
            player "In that case, wanna explore with me?"
            
            n "She stands up."
            
            show mishka happy
            
            mishka @ say "Dah!!"
            
            n "She walks along side you, the both of you constantly swiveling your heads to look into the colorful stores."
            
        show mishka nervous
            
        mishka @ say "I don't think I understand what the point of the mall is."
        
        n "You shrug."
        
        player "It's just a bunch of novelty stores. You're supposed to look around and buy whatever you think is interesting."
        
        show mishka despondent
        
        mishka @ say "You don't know what you want beforehand?"
        
        player "Nope. That's the fun of it. It's like an amusement park but for consumerism."
        
        show mishka neutral
        
        n "Mishka nods thoughtfully."
        
        mishka @ say "I see."
        
        player "See anywhere you wanna go?"
        
        show mishka anxious smile
        
        mishka @ say "Umm... it's very hard to pick one because I'm not sure what I'm looking for..."
        
        player "How about..."
        
        n "You look around for the closest store that isn't a cheap clothing store for teenagers."
        n "There's an electronics store nearby that might have some interesting gadgets."
        n "You point to it."
        
        show mishka anxious neutral
        
        player "That one?"
        
        n "Mishka sticks her head out and looks it over."
        
        show mishka happy
        
        mishka @ say "Sure!"
        
        hide mishka with dissolve
        
        n "Inside you find a pretty random assortment of objects, with the only unifying theme being that they all consume electricity."
        n "There's massage chairs, digital clocks, speakers, remote controlled cars and helicopters, turntables, fake fireplaces, electronic notepads, and so on."
        n "Most of it is impractical and overpriced junk but Mishka seems to have taken an interest in the RC vehicles."
        n "They're set up so you can play around with a demo unit in the store but she's having difficulty with the controls."
        
        show mishka anxious sad at center with dissolve:
            ypos y_mishka
        
        mishka @ say "I don't think I'm doing it right."
        
        n "The toy car flashes its headlights and steers its front wheels but refuses to accelerate."
        
        player "Maybe you have to hold a button while pushing the stick up?"
        
        #show mishka tired happy
        
        n "You reach over and press a button while Mishka fiddles with the control stick."
        n "Suddenly the vehicle lurches backward, crashing into a stack of boxes and toppling them all to the floor."
        n "Must have been the turbo button."
        
        show mishka depressed
        
        n "Mishka looks shocked and freezes up."
        n "You take the controller from her and set it on a shelf, then quickly guide her out of the store before the staff can figure out it was you who knocked over the display."
        
        show mishka neutral
        
        player "Ok haha looks like it's broken, come on let's go."
        
        n "Outside of the store, you continue walking, searching for your next stop."
        
        mishka @ say "Well, it was fun while it lasted."
        
        player "Really it was their own fault for carelessly leaving boxes in the way of the RC car."
        
        n "When you turn the corner, Mishka gasps and giddily points ahead at a dazzling display of lights."
        
        show mishka at hop
        
        mishka @ say "Look! Do you see it??"
        
        n "How could you not? There's a massive carousel taking up your field of view."
        n "The plastic horses stare at you with malice."
        
        menu:
            n "{cps=0}The plastic horses stare at you with malice.{/cps}"
            "Do you wanna ride it?":
                n "You're going to feel silly doing this as an adult but..."
                
                player "Do you uh, wanna ride it?"
                
                show mishka anxious tongueout wink left
                
                mishka @ say "You can do that???"
                
                player "Yeah, it's not just for show."
                
                show mishka happy tongueout
                
                mishka @ say "Then let's go!!"
                
                hide mishka with dissolve
                
                n "Mishka can hardly contain her excitement as you pay the operator and step onto the platform."
                n "You help her onto one of the mounts, then take one for yourself."
                n "The carousel slowly begins to spin, and the lights flicker in time with the music."
                n "The mall becomes a blur and your horse gently pushes you up and down."
                n "Looking back towards Mishka, she seems to be having the time of her life."
                n "She smiles and waves to you. You try to wave back but almost lose your balance and slip off the horse."
                n "When the ride comes to an end, you're a bit dizzy but wish it had gone on just a while longer."
                
            "This thing scares you":
                n "Something about the way the horses are impaled on rods and painted to look like jolly parade ornaments disturbs you."
                
                show mishka happy
                
                mishka @ say "Look! It says we can ride on them!"
                
                player "I-it's probably really expensive..."
                
                show mishka neutral
                                
                mishka @ say "Not really! The sign says couples can ride for just five dollars!"
                
                player "Yeah but we're not really a couple so..."
                
                show mishka neutral wink left
                
                mishka @ say "The operator doesn't know that! Come on, I'll pay for us!"
                
                hide mishka with dissolve
                
                n "Mishka practically drags you up to the carousel and onto one of the mounts."
                n "Your fear of the horse models is rivaled only by your sense of discomfort being the only two people on the ride."
                n "It's like you're on display for the rest of the mall-goers."
                n "It was embarrassing when you were a child and it's even more humiliating now."
                n "But it's a small price to pay to see Mishka happy. It's probably her first time on such a ride."
                n "You crane your neck around to see her grinning from ear to ear on the mount behind you."
                n "As the ride goes on, you start to relax and get used to it. Even enjoy it a little."
                n "By the time it ends, you're a bit dizzy but wish it had gone on just a while longer."
                
        show mishka derp at center with dissolve:
            ypos y_mishka
            
        n "You both step off the platform and have trouble walking in a straight line."
        n "Mishka stumbles around and falls into your arms."
        
        show mishka anxious wink right
        
        mishka @ say "That was so much fun!!"
        mishka @ say "Thanks for coming along with me!"
        
        show mishka neutral -anxious -wink -right
        
        player "Heh, I haven't been on one of these in ages."
        player "I forgot how dizzying they are."
        
        n "You take a step forward and feel the world tilt underneath you."
        
        player "Let's sit down for a bit."
        
        show mishka happy
        
        mishka @ say "Hehe good idea~"
        
        hide mishka with dissolve
        
        n "You find a bench and rest until you can both walk like you're not drunk."
        n "For the rest of the day, you look around random stores, checking out jewelry, clothes, perfumes, and whatever else seems interesting."
        
        #buy cheap gift or expensive gift
        #hippie shop that sells incense and rocks (you figure mishka would like it)
        #this was nice but I have no desire to ever return!
        
        show mishka neutral at center with dissolve:
            ypos y_mishka
        
        player "Well Mishka, are you a mall rat now?"
        
        mishka @ say "Mmh, I don't think so~"
        mishka @ say "I enjoyed our time here but I think we've seen it all!"
        
        show mishka anxious tongueout wink left
        
        mishka @ say "We should go somewhere else next time!"
        
        show mishka anxious neutral
        
        player "We'll find some place."
        player "This was a lot of fun but maybe we can find a more chill place next time."
        
        show mishka at hop
        
        mishka @ say "Mhm!"
        
        hide mishka with dissolve
        
        n "Mishka walks you back to your dorm and wishes you a good night."
        n "It's been a fulfilling weekend. You wouldn't mind just relaxing on your own tomorrow."
        
        stop music fadeout 2.0
        
        scene bg black with fade
        
        scene bg codadorm with fade
        
        show box with Dissolve(.2):
            ypos 0
        
        jump ch2End

        
label ch2End:
    n "The rest of your weekend passes uneventfully."
    n "You just recover from all the excitement of the past couple of days, browse the web, do a bit of studying, and rest up for your return to class."
    
    
    jump chapter3