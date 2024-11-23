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

    if avahangout1 == True:
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
        n "Ava sends you a text telling you to meet her there in half an hour."
        n "You prepare your backpack, stuffing it with a couple water bottles and snacks, then proceed to head out."

        scene bg oldhospital foyer with fade
        
        show box:
            ypos 0

        #play music "audio/ambient/spooky.ogg" fadein 1.0
        #play music "audio/music/vylet - Cavern Lurker.ogg" fadein 1.0

        show box with Dissolve(.2):
            ypos 0

        n "Ava wasn't kidding when she said this place was abandoned."
        n "Graffiti lines the walls and weeds grow out of cracks in the concrete. You'd be afraid to enter a place like this alone, but luckily you have a dainty liberal arts student to protect you."

        show ava typical neutral at center with dissolve

        #ava @ say "Hey [name]! Glad you could make it!"

        #player "It took a while to find it! There's no trail or signs or anything."

        #ava @ say "I know, right? It's so exciting! It's probably been years since anyone has last stepped foot here."
        ava @ say "It's probably been years since anyone has last stepped foot here."
        
        player "Any functioning member of society at least."
        
        show ava excited
        
        ava @ say "Come on, let's get exploring!"
        
        scene bg oldhospital hall1 with dissolve
        
        show box:
            ypos 0

        n "Ava leads the way as you go deeper inside, pulling away some boarding planks and debris along the way."
        n "She looks around before deciding on a place to compose a shot and snapping a picture."

        player "That's not your usual camera, is it?"
        
        show ava typical neutral at center with dissolve:
            xzoom -1

        ava @ say "Hm? Oh this?"
        ava @ say "I brought one of my old film cameras along. Thought some vintage black and white film would fit the mood of the place, y'know?"
        
        player "It's not because ghosts can only be recorded on analogue, is it?"
        
        show ava pose smile
        
        ava @ say "Well, that too."

        n "She pulls a lever on the camera, loading the next frame."
        
        show ava typical neutral

        #ava @ say "But I also wanted to capture the feeling of those old historical photos with the inky blacks and softness to the frame."
        
        #player "Black and white means it's art, right?"

        #ava @ say "Hey, I like black and white for portraits!"
        ava @ say "And it just wouldn't feel right shooting this place in color."
        ava @ say "I don't even think color film was invented yet when they built this place."

        player "What about lead paint and asbestos?"
        
        show ava at flipleft
        
        pause .8
        
        show ava at flipright
        
        pause .4

        ava @ say "Hehe, I dunno! Try not to lick the walls just in case."

        n "You make your way through the building slowly, being careful not to step on any rusty nails or fall through any floorboards."
        n "Dust kicks up as you explore, mixing with the smell of mildew in the humid air. Every now and then you hear creaks and pops from other rooms echoing throughout the building."
        n "Water drips down from the ceiling into little puddles full of moss and weird sludge you don't dare touch."
        n "Luckily the holes in the walls provide enough light for you to navigate."
        
        show ava waitwhat
        
        ava @ say "Whoa, check this out!"
        
        scene bg oldhospital room with dissolve
        
        show box:
            ypos 0

        n "Ava motions for you to look through a crack in the wall. When you bend over to peer inside all you see is a seemingly ordinary waiting room."

        player "I don't get it, what's so special about this?"
        
        show ava unsure at center with dissolve

        ava @ say "Oh right, I guess you wouldn't be able to see it with your weak human eyes."
        
        player "Hey! My eyes are optimized for tracking movement and identifying photoshopped pixels!"
        
        show ava seriously
        
        ava @ say "Hmm okay how do I describe this..."
        ava @ say "You know how in those crime shows they shine a blacklight and they can see bloodstains and stuff? It's like that."
        
        player "Whoa really? So this room was covered in blood at some point?"

        ava @ say "Err... actually blood doesn't glow like in the movies and stuff."
        ava @ say "Other bodily fluids will though."

        player "Gross!"
        
        show ava pose overjoyed

        ava @ say "That doesn't mean this building didn't see its fair share of blood though!"
        
        show ava ohyou
        
        ava @ say "The doctors at this hospital was known for their eagerness to amputate limbs."
        ava @ say "Like, if you came in with a cold they'd amputate your leg."

        player "Wow, that's uh..."
        
        show ava pose smile

        ava @ say "There's even a \'cemetary\' for all the disembodied limbs out back!"

        player "How do you know all this?"
        
        show ava pose happy

        ava @ say "I saw a video on it."
        ava @ say "Whenever I can't sleep I put on morbid videos."

        player "Doesn't that give you nightmares?"

        ava @ say "Not really? I don't dream much."
        ava @ say "Do you?"

        player "Sometimes."

        ava @ say "About what?"

        player "Usually something completely random and unnoteworthy."
        player "But sometimes they feel real and can make me anxious."

        n "Ava pokes her camera through the crack and adjusts the dials and rings on the camera."

        ava @ say "Sometimes I daydream. Whatever I'm doing, my brain just goes on autopilot while I think about things I wanna shoot."

        player "Shoot as in with your camera, right?"
        
        ava @ say "Hm? Yeah."
        
        player "Like spooky hospitals?"

        ava @ say "Actually yeah, this is the sort of things I imagine, but more abstract."
        
        hide ava with dissolve

        n "Ava clicks the shutter button and takes a photo."

        #player "What are you doing?"

        #ava @ say "Rewinding the film."

        #player "Oh."
        #player "...Why?"

        #ava @ say "Oh sorry, I should have explained."
        #ava @ say "I wanted to try taking some double exposures, y'know, where you take a shot on top of an already exposed piece of film."
        #ava @ say "It's a technique that I've thought about using more but the results can look kinda random so it's hard to imagine how it'll turn out."
        
        n "You and Ava make your way to the end of the hall where a staircase lies, the steps covered in rubble from the crumbling walls and steps above."
        n "Ava crouches down and turns her camera 90 degrees to take a shot of it."
        n "Her feathers stick up and you jump a little when a loud noise comes from behind, echoing throughout the hall."
        
        show ava pose concerned at center with dissolve
        
        n "You speak in a hushed tone."

        player "...Did you hear that?"

        ava @ say "Yeah... is someone here?"
        
        n "As if to answer her question, the sound of stone clattering onto the floorboards reaches you."
        
        player "M-must have been the wind?"
        
        ava @ say "I don't think we're alone. Come on, let's go up the stairs, quick!"
        
        n "Ava goes first, lightly stepping between the larger piles of debris while you struggle with these non-OSHA compliant stair sizes."
        n "She flutters over a precarious gap in the steps that you unfortunately end up getting your foot stuck in."
        
        player "Agh! My foot!"
        
        show ava unsure
        
        ava @ say "[name]!"
        
        n "Ava doubles back and helps pull you out, oblivious to the pain shooting through your ankle. You try to hold your tongue to not reveal your position to the other intrudor."
        n "You hobble up the remaining stairs and into a room, closing the door behind you, bracing it with your body in case they try breaking in."
        
        scene bg oldhospital darkroom with fade
        
        show box:
            ypos 0
        
        n "For a few moments it's just you and Ava in a dark room trying not to breath heavily after the scare and rapid ascent so you can listen."
        n "With your back against the door, you hold onto Ava. She's got both her wings wrapped around you."
        n "Her camera is jabbing into your side uncomfortably but you can feel her heartbeat against your chest, which is oddly calming."
        n "You guess if you're gonna get stabbed by a hobo, this would be a nice final memory. Cute bird in your arms. Maybe someone will find the film and develop it."
        n "Maybe someone will make a documentary about you."
        n "'Two dumbasses go venturing in dangerous hobotopia, shockingly get murdered in most gruesome way possible.'"
        #player "I wonder who they'd get to reenact me in the documentary? Maybe they'd shave a chimpanzee for it?"
        n "After a few minutes, Ava speaks up, still in a hushed tone."
        
        show ava typical neutral at center with dissolve
        
        ava @ say "I think whoever that was is gone. Or at least they didn't follow us."
        
        player "Yeah. We probably scared them off with the noise we made climbing up the stairs."
        player "Hopefully it was just a wild animal and not like a psycho stalker serial killer."
        
        ava @ say "Ugh you just reminded me of something."
        
        player "What?"
        
        ava @ say "Promise you won't cringe."
        
        player "Oh please, whatever it is, I guarantee I've done worse."
        
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
            "Nah, I get it.":
                player "I completely understand."
                
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
            xpos -300
        
        player "Careful, it's dark and I don't know if this is the rusty nail room."
        
        n "*Crck*"
        n "A dim purplish glow gradually fills the room."
        
        show ava glowy unimpressed with dissolve
        
        ava @ say "I brought some glowsticks. Good to have in case your batteries run out. Or for creating ambiance."
        ava @ say "And they're my favorite color."
        
        player "Whoa! Ava, your feathers..!"
        
        show ava at flipright
        
        ava @ say "Hm? What about them?"
        
        player "They're all pretty and stuff!"
        
        ava @ say "Oh my gosh thanks? I didn't really do anything special with them today though."
        
        player "But you have patterns on them now!"
        
        ava @ say "I always have patterns on them. That's just how they are."
        ava @ say "Wait, you mean the spirals?"
        
        player "Yeah those."
        
        ava @ say "You're just now noticing them? Those have always been there."
        ava @ say "Hmm, okay I think I know what's going on."
        
        n "She waves a glowstick over her wing feathers and the patterns become more visible the closer they are to the light."
        
        ava @ say "Just like what I was saying before. The glowstick must be acting like a blacklight."
        ava @ say "With these you can see what I see all the time."
        
        player "Wow. Do all birds have patterns on their feathers?"
        
        #show ava portrait neutral
        
        ava @ say "Just the pretty ones~"
        
        #show ava typical neutral
        
        #player "You'd be fun at one of those glowstick raves"
        
        #player "It certainly makes the thought of getting stabbed by a crackhead here more palatable."
        
        #ava @ say "Haha I was thinking the same thing!"
        
        n "Ava breaks another glowstick and wanders further into the room."
        
        #ava @ say "If I was a serial killer on the run from the police, this is the type of place I'd hang around in."
        
        show ava:
            ypos 15
            xzoom -1
            linear .15 ypos 0
            
        #show ava pose concerned
            
        ava @ say "You comin- oh god [name]! What's with your foot?"
        
        player "Huh?"
        
        n "You look down to see your foot bent at an unnatural angle."
        
        player "Oh. FUck."
        
        ava @ say "Holy Hoole that looks bad... Stay right there, I'll- I dunno, I'll figure something out."
        
        n "Ava looks around and finds an old wooden cane for you to lean on."
        
        ava @ say "Lucky we're in a hospital right? Haha..."
        
        n "Her attempt at making light of the situation is appreciated but now that the adrenaline is wearing off, you're starting to feel excruciating pain."
        
        player "Where's a kitsuragi when you need one?"
        
        ava @ say "Can you walk? We should get you to a real hospital asap."
        
        n "Ava lets you lean on her as the two of you exit the room and head back down the stairway."
        n "It takes a long time but you eventually make it back to the ground floor."
        
        scene bg oldhospital hall2 with fade
        
        show box:
            ypos 0
        
        show box with Dissolve(.2):
            ypos 0
        
        n "As you're trying to figure out which direction you came from, you notice Ava seems preoccupied with a corridor you hadn't explored."
        
        show ava concerned at center with dissolve:
            xpos 0
        
        ava @ say "..."
        
        player "Go ahead, I can tell you've got a photo in mind."
        
        show ava excited
        
        ava @ say "Whew thanks! I'll be just a second, alright?"
        
        hide ava with dissolve
        
        n "You lean on your cane while she flutters up to a high perch and lines up a shot."
        n "Suddenly a loud crashing noise startles both of you and Ava comes crashing down."
        
        
        show ava reaching concerned:
            ypos -3000
            
        show ava with move:
            ypos 1080
            
        pause .2
            
        show ava with move:
                ypos 0
                
        show ava at shudder
        
        show ava unsure
        
        
        
        
        #show ava unsure at center:
        #    ypos -3080
            
        #pause .1
        
        #show ava:
        #    ypos 1080
        #with move
        
        #pause .2
        
        #show ava:
        #    ypos 0
        #with move
        
        
        player "Ava!"
        
        ava @ say "I'm okay!"
        
        player "What the fuck was that?"
        
        ava @ say "I dunno but we better get out of here now before we get murdered."
        
        player "Don't you wanna meet your serial killer husbando?"
        
        show ava angry
        
        ava @ say "Shut up or I'll leave you here without your crutch."
        
        ### ava flying up to higher floors and helping you up, more gunner stalking, he gets caught in the end, 
        
        #n "As Ava lines up another shot, the two of you are startled by a sudden loud noise that echoes throughout the building."
        
        player "Okay okay, let's just get out of here. Which is... that way I think? I'm not sure, this place is like a maze."
        
        show ava typical neutral

        n "You poke your heads out of the room you're in."

        player "Do you see anything?"

        ava @ say "Nada."
        ava @ say "Wait."

        n "You turn your head to the direction she's facing."

        ava @ say "Wasn't that window boarded up earlier?"

        player "I don't remember, there's a lot of boarded up windows."

        ava @ say "It looks like it leads outside. I'll help you through it."
        
        hide ava with dissolve

        n "Ava puts forth her best effort in pushing you through the window, though a petite bird lass like her is unable to offer much help."
        n "You basically get your upper body onto the windowsill and then roll over the edge."
        
        stop music fadeout 1.0
        
        scene bg oldhospital exterior with fade
        
        show box:
            ypos 0
        
        play music "audio/ambient/outdoors night crickets.ogg" fadein 1.0
        
        n "With the last bit of sunlight fading from the sky, it was hard to see exactly where you were crashing. And Ava wasn't waiting around to get murdered just cause your foot hurts."
        n "Fortunately you only feel nice soft grass on the ground and not broken glass."
        n "Any minute vibration in your foot still hurts like hell though."
        
        player "Ow."
        
        show ava typical neutral at center with dissolve:
            xpos 300
            yalign 0
        
        ava @ say "You alright there? Here's your cane."
        
        n "As you stand back up you swear you can hear footsteps in the grass."
        n "And yup that is definitely a pair of eyes staring at you."
        
        show gunner neutral at left with dissolve:
            yalign 0
            xzoom -1
            xpos -300
        
        gunner @ say "[name]! Ava! Sup?"
        
        show ava concerned
        
        ava @ say "Gunner? What the hell are you doing here?!"
        
        #gunner @ say "Oh y'know, just some urban exploration. Urbex as they say. Which I'm totally into by the way."
        
        #ava @ say "Dammit Gunner, [name] got hurt cause you scared us!"        
        
        gunner @ say "Oh y'know, just some urban exploration. Urbex as they say. Which I'm totally into by the way."
        
        ava @ say "I thought you had fishing trip with your frat today?"
        
        gunner @ say "Oh, that? Uhh, we decided not to, due to concerns. Ethical concerns. About fishing."
        gunner @ say "Did you know the yellowtail population has decreased by 81 percent since 1913? I just thought that was interesting."
        gunner @ say "Hey is your foot alright, [name]? I'm no expert in human anatomy but I don't think you can twist yours back 180 degrees normally."
        
        player "Yeah it's def sprained or something."
        
        show ava angry
        
        ava @ say "Dammit Gunner we thought you were a stalker and [name] got injured because of you!"
        
        gunner @ say "Hey, don't blame me because [name] clumsily tripped over their own feet!"
        
        #ava @ say "Says the scaredy cat afraid of ghosts!"
        
        #gunner @ say "Now those are actually scary!"
        #gunner @ say "I just wanted to have a nice relaxing stroll through this abandoned hospital, and by coincidence you happened to show up at the same time and [name] had an unfortunate accident."
        gunner @ say "It's not like I pushed them down the stairs or anything."
        #gunner @ say "It's your own fault for rushing."
        
        show ava annoyed
        
        ava @ say "Ugh, whatever. Let's just get [name] to a doctor. You can carry them since you're the most responsible for them getting hurt in the first place."
        
        gunner @ say "Hmph. Fine."
        
        n "You kinda tuned out of the conversation. This hospital sucks. Can you go home now? Your feet hurt."
        n "Gunner gingerly picks you up in a bridal carry. Oh god this feels so nice what the fuck."
        
        gunner @ say "Sorry about all this, buddy. I really did just wanna hang out and stuff."
        
        n "The trip to the hospital is quiet and tense."
        
        stop music fadeout 1.0
        
        scene bg hospital with fade
        
        show box with Dissolve(.2):
            ypos 0
        
        play music "audio/music/Vylet Pony - lemonade.ogg" fadein 0.1
        
        show kitsuragi at center:
            xpos -500
            xzoom -1
        show gunner neutral at center:
            xpos 350
        show ava typical neutral at center:
            xpos 533
        with dissolve
        
        kitsuragi @ say "Welp. I expected to see you again soon but not for something like this."
        kitsuragi @ say "You're lucky you have friends to drag your ass here all the time."
        
        player "It's a bonding experience."
        
        gunner @ say "Again, super sorry this happened, [name]! I'll make it up to you, I promise."
        
        show ava angry
        
        ava @ say "You better!"
        
        gunner @ say "You played your part in this happening too! I reckon you owe [name] something too!"
        
        kitsuragi @ say "I'll leave you all to figure that out on your own."
        kitsuragi @ say "[name], you're free to go whenever. Or you can stay the night, I don't care."
        
        n "You sip on the complimentary juice box she gave you for being brave while she twisted your foot back into place and nod."
        
        hide kitsuragi with dissolve
        
        show gunner with move:
            xpos 0
        
        n "Gunner and Ava awkwardly stand around, looking at the ground in opposite directions."
        n "You cough to break the silence."
        
        player "Sooooo..."
        
        show ava pose concerned
        
        ava @ say "Soooo...?"
        
        #gunner @ say "....Yeah."
        
        player "This was a fun day. If I wasn't already traumatized by hospitals, I sure will be now."
        
        show ava pose flattered
        
        ava @ say "Heh yeah... This place is even spookier than the old abandoned one, huh?"
        
        show ava typical neutral
        
        gunner @ say "You gonna stay the night here or go back to your dorm?"
        
        menu:
            gunner "{cps=0}You gonna stay the night here or go back to your dorm?{/cps}"
            "I'll stay here.":
                #finished
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
                
                show ava motivated
                
                ava @ say "I'll go but if Gunner tries to break your other leg, gimme a call and I'll come flying!"
                
                player "Heh will do~"
                
                show ava typical neutral
                
                ava @ say "Take care, [name]. I'll see you later, k?"
                
                player "For sure. Later birdy~"
                
                ava @ say "Later, human~"
                
                hide ava with dissolve
                
                gunner @ say "Cute."
                
                n "Gunner plops down in the chair across from you."
                
                player "Is this how you imagined today would go?"
                
                gunner @ say "No. I dunno how I thought it would go. I just kinda went for... *something* and hoped it would work out okay."
                
                player "Mhhm. I know how that feels."
                player "Maybe you just have to do nothing and things work out better that way."
                
                gunner @ say "You think so?"
                
                player "Sometimes. It's more uhh, natural that way?"
                player "If you try to force something to happen, it won't go the way you want it to."
                
                gunner @ say "But if I don't try, I won't get what I want. I'll just be at the mercy of whatever life throws at me."
                gunner @ say "It's not fucking fair. You don't even try and girls practically throw themselves at you."
                
                player "They do? I never noticed."
                
                gunner @ say "Wait..."
                
                n "Gunner looks like he just realized something."
                
                gunner @ say "You don't even have a scheme to get with Ava, do you?"
                
                player "A scheme? No, she just keeps inviting me to stuff and I keep going."
                
                gunner @ say "Unbelievable! Hah!"
                gunner @ say "It must be a plot to make me jealous, is that it?!"
                
                player "No dude, we just naturally get along I guess??"
                player "It's just fate that she happened to ask me to hang out first."
                player "You can't really plan for that."
                
                gunner @ say "So you're telling me to quit trying?"
                
                player "Sort of. It seems to be working for me pretty well."
                player "I think you'll reach a better outcome if you just be yourself instead of trying to manipulate events in your favor."
                
                gunner @ say "You must not know many cats."
                gunner @ say "Manipulating fate in our favor *is* our nature."
                #gunner @ say "They say every time a cat does something, Ecaflip rolls a nine sided die to determine our success."
                gunner @ say "They say our lord and savior Ecaflip gave us nine lives so we can fail and learn from our mistakes in eight of them, then succeed in our nineth."
                gunner @ say "I believe there's always a path to victory, it's just a matter of finding it and doing what you need to do to get there."
                
                menu:
                    gunner "{cps=0}I believe there's always a path to victory, it's just a matter of finding it and doing what you need to do to get there.{/cps}"
                    "Good luck with that":
                        #finished
                        player "I don't know what to say to that other than good luck."
                
                        gunner @ say "I don't need your luck. I make my own luck."
                        
                        n "Gunner's tone had become more standoffish. There's a tense moment of silence. You guess neither of you have anything left to add to the conversation."
                        n "Gunner pulls out his phone and doesn't say anything to you for the rest of the night."
                        
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
                        
                        scene bg codadorm with fade
                        
                        show box with Dissolve(.2):
                            ypos 0
                        
                        n "Gunner was still a little bitter this morning, but at least he walked you home."
                    "I guess we have different ideas of fate":
                        #finished
                        player "I guess we have different ideas of fate then."
                        player "I always saw it as something you can't change. Like me being the last human and ending up in this hospital tonight with an injured ankle was unavoidable despite our illusions of choice."
                        
                        gunner @ say "Maybe it is that way for you."
                        gunner @ say "But we felines define our own fate! It is our destiny to defy the chains of uhh... destiny!"
                        
                        player "Nice self fulfilling prophecy you got there. What if your fate is to get with Ava and you're unknowingly working against it?"
                        
                        gunner @ say "Oh shit could that really happen?"
                        
                        player "You're the one who believes in real life RNG manipulation, not me."
                        
                        #gunner @ say "Just you wait, I just have to figure out the right order of steps to take and dust clouds to kick up and I'll win the lottery!"
                        gunner @ say "It's a cat exclusive ability."
                        
                        player "If you say so. I don't want us to fight over some girl though."
                        player "Bros before hoes and such."
                        
                        gunner @ say "Ay, true."
                        gunner @ say "But don't call my crush a hoe."
                        
                        player "Oh sorry."
                        player "But for real, I'm not even actively pursing anyone, I don't think? If Ava wants to go out with me or you or whoever, that's her choice."
                        #I'm just gonna let Ava decide who she wants."
                        
                        gunner @ say "I guess that's... fair?"
                        
                        player "Cool, I'm glad you're not mad at me."
                        
                        gunner @ say "Same."
                        gunner @ say "Don't expect me to hold back though. I'm gonna end up with Ava no matter what."
                        
                        player "We'll see about that."
                        
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
                        
                        n "After talking with Gunner a bit more last night you both fell asleep. When you woke up you felt good enough to walk back to your dorm."
                        n "Gunner made sure you got here fine then went back to his dorm."
                        
                
                
            "Screw this place.":
                player "Yeah no, screw this place, I'm going home."
                
                n "Gunner hands you your crutch as you get into a sitting position and begin to stand up."
                
                gunner @ say "I can carry you back if you want."
                
                player "That won't be necessary."
                
                show gunner:
                    xzoom -1
                
                show ava portrait concerned
                
                ava @ say "You gonna be okay?"
                
                player "I think so, aside from the nightmares of getting stalked by hobos."
                
                show ava portrait smile
                
                ava @ say "Aww, want me to snuggle you tonight and protect you?~"

                menu:
                    ava "{cps=0}Aww, want me to snuggle you tonight and protect you?~{/cps}"
                    "Yes please":
                        $ avaPoints = avaPoints + 1
                        player "That would be delightful."
                        
                        show ava embarassed

                        n "Ava looks caught off guard, like she didn't expect that response."

                        ava @ say "I-I was just joking you know!"
                        
                        show ava at flipright

                        n "She looks away but can't hide her blush."
                        
                        show ava annoyed
                        
                        show ava at flipleft

                        ava @ say "F-f-fine! Just for tonight though!"
                        
                        player "Good enough for me!"
                        
                        hide ava
                        hide gunner
                        with dissolve
                        
                        n "Gunner quietly seethes in the corner."
                        #n "Too bad buddy, should have broken your ankle if you wanted bird snuggles."
                        n "Too bad buddy, shouldn't have gotten my ankle broken."
                        
                        #ava @ say "And you have to be the little spoon."
                        
                        n "Gunner walks you back to your dorm, being unusually quiet and ocassionally glaring at you while you joke about the day's events with Ava."
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
                        
                        show ava reaching embarassed at center
                        
                        ava @ say "Aaa! [name], don't look!"
                        
                        player "S-sorry."
                        
                        n "She turns away from you and quickly buttons up her shirt."
                        
                        show ava annoyed at center:
                            xpos 0
                        with dissolve
                        
                        ava @ say "You should knock first!"
                        
                        player "It's my room."
                        
                        #show ava angry
                        
                        ava @ say "Still! I could have been nude!"
                        
                        player "Is that foreshadowing?"
                        
                        show ava angry
                        
                        ava @ say "No!"
                        
                        player "Dang."
                        
                        show ava typical neutral
                        
                        ava @ say "I came here for friendly clothes-on cuddling, nothing more."
                        
                        player "Well then, shall we get to business?"
                        
                        n "You crawl into bed and Ava lies down next to you, seemingly unsure of what to do next."
                        
                        ava @ say "I've never done this before..."
                        
                        player "Really? Me neither."
                        
                        ava @ say "I guess I'm supposed to..."
                        
                        n "She tries wrapping her wings around you but she struggles getting the one between the mattress and your body."
                        
                        ava @ say "God dammit why is this so difficult."
                        
                        player "Here, lemme just..."
                        
                        n "You try holding onto her but run into the same issue. Once you get your arms around her, the one pinned between her body and the mattress loses bloodflow."
                        
                        show ava bored
                        
                        ava @ say "...This isn't very comfortable is it?"
                        
                        player "Not really."
                        
                        show ava concerned
                        
                        ava @ say "We can just sleep next to each other if you want."
                        
                        show ava typical neutral
                        
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
                            n "It's not even daylight out and she's stretching and chirping and tweeting."
                            n "She rolls over and rests a wing on you."
                            
                            show ava typical neutral at center:
                                yalign 0
                                xzoom -1
                                xpos -175
                            
                            ava @ say "Morning~"
                            
                            n "You make an unsatisfied caveman grunt as your natural desire is to sleep in."
                            
                            ava @ say "I don't know why but I'm feeling really refreshed!"
                            
                            show ava overjoyed
                            
                            ava @ say "Perhaps that's the power of snuggles?"
                            
                            player "We weren't even really snuggling."
                            
                            show ava typical neutral
                            
                            ava @ say "Yeah but our bodies don't know that! It's the proximity that counts!"
                            
                            player "Next time can we at least be nude?"
                            
                            ava @ say "Hmm..."
                            ava @ say "Sure!"
                            
                            show ava portrait neutral
                            
                            ava @ say "*If* there's a next time hehe~"
                            
                            player "Wow, you really are in a great mood today."
                            
                            show ava overjoyed
                            
                            ava @ say "Breeee~"
                            ava @ say "I guess I am! Very unusual, isn't it?"
                            
                            player "Must be the endorphins."
                            
                            show ava typical neutral
                            
                            #ava @ say "?"
                            #ava @ say "Oh, endorphins. Maybe!"
                            ava @ say "Maybe!"
                            ava @ say "Nothing gets me more excited than adventure and yesterday sure was one!"
                            
                            n "Ava hops out of bed and unlocks your window."
                            
                            player "Hey, where are you going?"
                            
                            show ava typical neutral
                            
                            ava @ say "Got a busy day of shooting ahead of me!"
                            
                            player "With your camera, right?"
                            
                            ava @ say "Of course!"
                            
                            n "She takes a dive through the window. A moment later you see her swoop up into the sky."
                            
                            hide ava with dissolve
                            
                            n "Just like that, she's gone."
                            n "The cuddles were pretty disappointing but the way she smiled at you made your heart skip a beat."
                            n "You flop out of bed and pace around the room a few times."
                        else:
                            n "You're woken up earlier than usual by Ava's stirring."
                            n "It's not even daylight out and she's stretching and chirping and tweeting."
                            
                            show ava typical neutral at center:
                                yalign 0
                                xzoom -1
                                xpos -175
                            
                            ava @ say "Morning."
                            
                            n "You make an unsatisfied caveman grunt as your natural desire is to sleep in."
                            n "Ava gets up and awkwardly wanders around the room, yawning."
                            
                            ava @ say "Did you... enjoy the snuggles?"
                            
                            player "Mhm."
                            
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
                            
                        jump dayafterurbexcont
                        
                    "We can all snuggle together at my place":
                        player "Hey that's a great idea! We can all snuggle at my dorm."
                        
                        show ava waitwhat
                        
                        ava @ say "A-all three of us??"
                        ava @ say "Uhh you sure that's a good idea?"
                        
                        n "Gunner shrugs."
                        
                        gunner @ say "Eh, I'll take what I can get. I'm game."
                        
                        show ava angry
                        
                        ava @ say "W-well I'm not gonna just let you and Gunner have all the fun! I'm going too!"
                        
                        player "That settles it then! Snuggle party at my dorm!"
                        
                        show ava concerned
                        
                        n "Ava and Gunner look at each other with a uncertain expressions."
                        
                        scene bg codadorm with fade
                        
                        show box with Dissolve(.2):
                            ypos 0
                        
                        show gunner neutral at center:
                            xpos 300
                            xzoom -1
                        show ava typical neutral at center:
                            xpos -300
                        with dissolve
                        
                        gunner @ say "So...."
                        
                        show ava bored
                        
                        ava @ say "How are we gonna do this?"
                        
                        player "Good question. I'm not a pro at this by any means."
                        
                        show ava typical neutral
                        
                        n "You sit on your bed and try to recall just what you were thinking when you invited the whole love triangle to cuddle together."
                        n "Lost in thought, you don't notice your two snuggle buddies hopping onto the bed on either side of you."
                        
                        show ava at flipright
                        show gunner at flipleft
                        
                        show ava smile
                        
                        ava @ say "Let's try this. Just lie down and relax~"
                        
                        n "Ava gently pushes you onto your back and wraps her soft feathery wings around you."
                        n "A moment later, you feel Gunner's fur brushing against you from the other side."
                        
                        gunner @ say "You alright? You're shaking."
                        
                        player "Yeah, j-just cold is all..."
                        
                        n "You've never been so nervous before. You can't even think straight. Was it a mistake to bring Gunner here? Oh god what's he doing?"
                        n "You feel his scratchy tongue combing your hair like your some sort of stupid baby kitten who is too dumb to groom yourself." 
                        n "Gunner is literally grooming you."
                        
                        gunner @ say "Purrrr~"
                        gunner @ say "Calm down bro, we'll warm ya up~"
                        
                        n "This is a classic power play by felines."
                        n "First they play nice and cuddly to lower your guard, then they start licking you to assert dominance, next he's gonna try and fuck the bird in your bed."
                        
                        show ava suggestive
                        
                        ava @ say "Everything alright, [name]?"
                        
                        show ava smile
                        
                        player "Y-yeah, I just need to-"
                        
                        menu:
                            player "{cps=0}Y-yeah, I just need to-{/cps}"
                            "Turn towards Ava":
                                $ avaPoints += 1
                                n "You adjust yourself and turn to face Ava, leaving you backside to Gunner."
                                n "A risky move, as it puts you in a position of vulnerability, but it also blocks Gunner's path to Ava."
                                n "You hold onto Ava tightly, face buried in her plumage."
                                
                                player "That's better."
                                
                                show ava flattered
                                
                                ava @ say "Breee~ This works too~"
                                
                                n "You can feel Gunner staring daggers at the back of your head."
                                n "It doesn't matter though, the bird is in your arms, not his."
                                n "In retaliation, he doubles down on brushing your hair with his scratchy cat tongue, purring ever louder and even pulling your hips closer to him."
                                n "The prices you pay for love."
                                n "And you *know* neither of you are enjoying this, but Ava seems to be all for it."
                                
                                show ava portrait overjoyed
                                
                                ava @ say "Heeheehee~ You two are so cute~ *chirp!*"
                                
                                gunner @ say "*Purrpurrpurrpurrpurrpurr~*"
                                
                                show ava portrait happy
                                
                                n "Gunner's going for the humiliation tactic but as long as his paws and tongue are on you, they're not on Ava and that's the best available outcome."
                                n "You close your eyes and mentally prepare for an awkward morning."
                                n "Somehow you manage to fall asleep amidst the tension running so high."
                            "Turn towards Gunner":
                                n "It's said that to emerge victorious in war, you must be unpredictable, and that's precisely what you're going for."
                                n "You roll onto your side facing Gunner and wrap him in your arms."
                                n "Got you now, you son of a bitch!"
                                
                                gunner @ say "Oh? Whatchya doin' there, bud?"
                                
                                show ava portrait overjoyed
                                
                                ava @ say "Ohmygosh this is so hot!"
                                
                                show ava portrait concerned
                                
                                ava @ say "I mean, it's so hot in here, right?"
                                
                                show ava portrait smile
                                
                                player "Just snuggling with my bro. Nothing wrong with that, is there?"
                                
                                n "You pull him in so tight he won't even think about escaping."
                                
                                gunner @ say "N-no, of course not!"
                                
                                n "He gives you a lick with his rough tongue on your face and digs his claws into your side."
                                n "Better you than Ava you suppose."
                                n "At least she's enjoying the show."
                                
                                ava @ say "You two are so cute~"
                                
                                n "You feel her nuzzle the back of your head and lay her wing on top of you. You make sure Gunner's paw gets nowhere near it."
                                n "You close your eyes and mentally prepare for an awkward morning."
                                n "Somehow you manage to fall asleep amidst the tension running so high."
                                
                        stop music fadeout .7
                                
                        scene bg codadorm with fade
                        
                        show box with Dissolve(.2):
                            ypos 0
                        
                        play music "audio/ambient/morning birds.ogg" fadein 1.5
                        
                        n "When your consciousness begins to reboot the following day, you question whether yesterday's events were just a dream until you realize you have a bird in your arms."
                        n "And then comes the nightmarish reality that is a snoozing Gunner inches from your face."
                        n "Somehow in the middle of the night you and Ava switched position so that she was in the middle of you two."
                        n "You guess this round of flirting with Ava ended up being a draw."
                        
                        show ava typical neutral at center:
                            xpos -200
                            xzoom -1
                        with dissolve
                        
                        ava @ say "*Yaaawn~*"
                        ava @ say "Morning~"
                        
                        player "Sleep well?"
                        
                        show ava overjoyed
                        
                        ava @ say "Amazingly well!"
                        
                        show ava typical neutral
                        
                        ava @ say "How's your ankle?"
                        
                        player "Fine, I think."
                        
                        n "You pull the blanket away and set foot on the floor."
                        n "It's still painful but you can deal with it."
                        n "Gunner begins to stir, stetching out his arms and yawning."
                        
                        show gunner neutral at center:
                            xpos 200
                        with dissolve
                        
                        gunner @ say "Morning cutie~"
                        gunner @ say "Oh hey [name], didn't see ya there."
                        gunner @ say "Man, they really hooked you up with the best everything in here huh? Your bed is so much softer than the one in my dorm."
                        
                        player "Yeah well don't get used to sleeping in it. My ankle's all better so you can go home now."
                        
                        gunner @ say "Oof, kicking us out so soon? Was I not a good snuggler?"
                        
                        ava @ say "You were pretty good! Both of you were!"
                        
                        player "Sorry, I've just got a busy day ahead of me."
                        
                        gunner @ say "That's alright, we'll head out soon. Thanks for having us over~"
                        
                        n "Gunner purrs and gives you a playful lick, surely an attempt to intimidate you, as he gets out of bed."
                        
                        gunner @ say "If either of you need top tier snuggles again, you know where to find me~"
                        
                        ava @ say "I'll keep both of you in mind~"
                        
                        player "See you two later."
                        
                        hide gunner
                        hide ava
                        with dissolve
                        
                        jump dayafterurbexcont
                                
                                
                        
                        #"gunner snuggles behind you. you're starting to regret this"
                    
                    
                        #gunner licks ava and you
                        
                    "Spill your spaghetti":
                        player "N-no thanks, that's what my tulpa waifu is for."
                        
                        #ava @ say "Do you wanna snuggle Gunner instead?"
                        
                        show ava waitwhat

                        ava @ say "You have a tulpa?"

                        n "Fuck, why did you say that?"

                        ava @ say "That's so cool!"

                        player "Really?"
                        
                        show ava overjoyed
                        
                        ava @ say "You should tell me about her!"
                        
                        player "M-maybe later..."
                        
                        n "Great, now you have to make up a schizo imaginary girlfriend to impress Ava."
                        n "Or make her jealous."
                        
                        show ava typical neutral
                        
                        player "Let's get out of this hospital first. I'm already sick of being here."
                        
                        gunner @ say "Agreed."
                        
                        hide gunner
                        hide ava
                        with dissolve
                        
                        n "Ava and Gunner walk you back to your dorm. Ava asks if you're sure you don't need a snuggle buddy but you're still too ashamed from before to take her up on the offer."
                        n "That and you don't want Gunner to break your other ankle tonight."
                        n "Thankfully he acts pretty chill on the way back, and you all make light of the events of the day."
                        n "After what you've been through, it's nice to ease up a little."
                        n "Your ankle still kinda hurts but you make it back to your dorm and get into bed, texting your friends until you fall into slumber."
                        
                        stop music fadeout 1.0
                        
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

                        jump dayafterurbexcont
        
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
        n "You have to mentally figure out where you are and plot your own course like it's the fucking 1800s."
        n "Ok, you think you just have to cross this street here then round that corner and it's mostly a straight shot to-"

        rose "What the hell are you doing?!"

        n "You feel someone grab onto the back of your shirt and pull you onto the sidewalk."
        
        player "Hey, get your paws off me!"
        
        n "A moment later a semi truck speeds through the street, right where you had stepped foot a mere fraction of a second ago."
        
        show rose angry at center with dissolve

        rose @ say "How dumb are you? You would have been dead if I didn't just save your ass!"

        player "Wha?"

        n "You blink, dumbstruck as your brain replays everything that just happened in slow motion."

        rose @ say "Didn't you ever learn to look both ways before crossing?"

        player "I did! The light even said to cross!"

        n "You point to the crosswalk sign, but to your surprise it says \"DO NOT CROSS\""
        n "It turns to white and says to cross a second later."

        player "How the...? I was sure I looked before I crossed! There weren't any cars!"

        show rose unimpressed

        rose @ say "Ugh, where's your wrangler when you need them?"

        n "There's no way to respond to that without sounding mad so you just keep quiet."

        rose @ say "Where are you trying to get to anyway? Everywhere is closed for the holiday."

        player "The parade?"

        rose @ say "Ended an hour ago."

        player "I figured. I just wanna go home now."

        rose @ say "*sigh*"
        rose @ say "I know natural selection wants you dead, but letting my project partner die on the streets might affect my grade so..."
        rose @ say "I guess I'm walking you home."

        player "I can walk myself home."

        rose @ say "You sure? Cause you were going the wrong way."

        player "Fine, if you really wanna take me home so bad you can."

        show rose armscrossed angry

        rose @ say "I don't want to walk you home but you obviously can't be trusted to do anything on your own!"

        player "Whatever, just lead the way."

        hide rose with dissolve

        n "Rose scowls and heads in the opposite direction, taking you down streets and alleyways that start to look more familiar as you get closer to campus."
        n "For someone so short she walks pretty quick. You can barely keep up."
        n "She only slows down when a large crowd blocks her way."
        n "When the crowd disperses a lone figure in robes stands in the middle of the sidewalk."
        n "He turns around and looks down at you and Rose."

        show fortune at center with dissolve:
            xpos 300

        fortune @ say "I've been expecting you."

        player "Huh? Who are you?"

        show rose neutral at center with dissolve:
            xzoom -1
            xpos -300

        rose @ say "He's just some homeless guy."
        rose @ say "Move. You're in the way."
        
        show rose:
            linear .5 xpos -150    
        pause .1
        show fortune with move:
            xpos 450

        n "Rose tries to walk around him but he steps in her path."

        fortune @ say "Homeless I am not. The world is my home."
        
        show rose unimpressed

        rose @ say "Even worse than homeless, this guy's a hippie."
        #Oh he's worse than I thought, he's a hippie."

        n "Rose tries once more to manuever around him, but it's almost like he knows which direction she'll go before she does."
        
        show rose:
            linear .4 xpos -250    
        pause .1
        show fortune with move:
            xpos 350
            
        pause .3
        
        show rose:
            linear .5 xpos -100    
        pause .1
        show fortune with move:
            xpos 500
        
        show rose angry

        rose @ say "Get out of the way!"

        #rose @ say "You're starting to piss me off. Move or you'll regret it!"
        
        show rose roseknife
        
        show rose:
            ypos 15
            linear .15 ypos 0

        n "Rose pulls something out from her pocket out of view of the hobo and holds it concealed in her clenched fist."
        n "Is that a... knife?"

        fortune @ say "Your blade does not deter me. I have seen the future. You are harmless."

        n "Rose grips her knife tighter."

        rose @ say "What do you want? Money? Nobody carries cash anymore."
        
        #fortune "I have no need for money, everything I work with is free."
        fortune @ say "I am merely one of fate's messengers."
        fortune @ say "You may decline to hear your fortune if you wish, but it will reach you one way or another, sooner or later."
        #fortune teller gives rose a false fortune, knowing that she doesn't pay?
        
        show rose unimpressed

        rose @ say "Good to know. I'll decline your \'fortune\' thank you."

        show rose neutral

        rose @ say "Come on, [name], I'm not sticking around."
        
        show rose:
            ypos 15
            xzoom 1
            linear .15 ypos 0
        
        pause .33
        
        show rose with move:
            xpos -450

        n "Rose starts to walk across the street to the other sidewalk."

        $ gnugift = False

        menu:
            n "{cps=0}Rose starts to walk across the street to the other sidewalk.{/cps}"
            "Aw come on, I wanna hear my fortune!":
                player "Aw come on, I at least wanna hear my fortune!"
                
                show rose:
                    ypos 15
                    xzoom -1
                    linear .15 ypos 0

                rose @ say "Why? He's just gonna make up some bullshit."
                rose @ say "Here's my fortune: I'm gonna walk back to campus without you and you'll get hit by a car and die."

                fortune @ say "Wrong."

                #rose @ say "What did you say?"

                fortune @ say "[name] will not perish today. Nor tomorrow, nor the next day."
                fortune @ say "There is something special about you. Your fate diverges. It is not yet sealed."
                fortune @ say "It seems you have a mission in life to be completed before you pass away."

                player "Wait, so I'm not dying?"

                fortune @ say "Not yet."

                rose @ say "Could you be any more vague?"

                player "Rose, this guy might be legit! He knew my name and I didn't even tell him!"

                rose @ say "He probably just overheard me saying it!"

                fortune @ say "Your fate is also divergent, Rose."

                player "See, he even knows your name too!"

                show rose angry

                rose @ say "Because you just said it!"

                fortune @ say "Perhaps your destiny is related to [name]'s? Unfortunately, I cannot give definitive answers for such people."

                show rose neutral

                rose @ say "What a great fortune teller you are."
                rose @ say "Now if you're done, we'll be on our way."

                fortune @ say "There is more. I can see several potential destinies and the paths you may take to reach them."
                fortune @ say "For a small donation I will-"

                rose @ say "Forget it. Like I said, nobody carries cash anymore, boomer."
                
                fortune @ say "I take etherium. My wallet address is 0x1AF7aD03CbB3e40a55392D518D585eA3EBB8F4B8."
                
                rose @ say "Cryptocurrency is fake and- "
                
                n "A nearby truck drives by and honks it's horn, cutting off the end of Rose's sentence before she walks off."
                
                show rose:
                    ypos 15
                    xzoom 1
                    linear .15 ypos 0
                    
                pause .2

                show rose with move:
                    xpos -1500

                #n "Rose waits for an opening in traffic and crosses the street."

                fortune @ say "Ah of course. You zoomers will donate to millionaire streamers and girls taking photos of their hooves in bad lighting online but won't even consider giving to the needy?"

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
                        n "You look up with a confused expression, ready to ask what this is for but the fortune teller is nowhere to be found."
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

                fortune @ say "As you wish. I won't keep you from your fate any longer."

                n "The gnu steps back and into the shadows."

                hide fortune with dissolve

                n "You follow Rose, looking over your shoulder."
                n "Luckily that creepy gnu isn't following you."
                n "In fact, it's like he vanished into thin air."

        n "When you get close to the campus, Rose chases you away with some colorful vocabulary and you hurry back to your dorm, ready for a nice long sleep."

        #meet fortune tellers. Rose is skeptical and gets angry when teller says they will end up together, refuses to pay
        #teller mentions coda has a terrible fate coming but warns not to worry about it
        
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
