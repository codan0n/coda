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
            n "You open your totally legally acquired epub of [currentbook] and start reading."
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
    #Every other time you go for a nightwalk lets you encounter someone. 
    #Can choose who to hang out with if you've done first part of their arc.
    "You decide to go out for the night."
    
    $ nightWalkIndex = (nightWalkIndex + 1) % 2
    
    if nightWalkIndex == 0:
        n "What will you do?"
        menu:
            "Wander aimlessly":
                $ randomSelected = renpy.random.choice(nightEvents)
            "Meet with Rose" if roseNightWalkActive:
                "You'll see if Rose is around"
            "Meet with Rori" if roriNightWalkActive:
                "You'll see if Rori is around"
            "Meet with Gunner" if gunnerNightWalkActive:
                "You'll see if Gunner is around"
            "Meet with Claire" if claireNightWalkActive:
                "You'll see if Claire is around"
            "Meet with Ava" if avaNightWalkActive:
                "You'll see if Ava is around"
            "Meet with Ellen" if ellenNightWalkActive:
                "You'll see if Ellen is around"
            "Meet with Mishka" if mishkaNightWalkActive:
                "You'll see if Mishka is around"
    else:
        call genericNightWalk
    
    
    
    return
    
label genericNightwalk:
    "You walk around campus but don't find anything interesting. It clears your mind and is refreshing to walk alone in the cool air."
    
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

label oliviaCafe:
    $ cafeEvents.remove("oliviaCafe")
    
    scene bg campus with fade

    show box:
        ypos 0

    #play music "audio/ambient/outdoors people talking.ogg" fadein 1.3

    n "On your way to Coffee Zone for some lunch, you end up walking a few paces behind a reptile in a wheelchair."
    n "Being from a small town and never really socializing, you thought they were just a myth, something they put in movies to scare young children."
    n "Wheelchairs, that is. Not alligators. You're quite familiar with gators. Your uncle got arrested for wrestling one at the zoo a couple times."

    show text "{color=d0dbff}*nyoooom*{/color}":
        ypos 46
        xpos 940

    show olivia neutral at offscreenright:
        yalign 0
    show olivia at offscreenleft with MoveTransition(delay=1.0):
        yalign 0

    pause 1
    hide text


    #n "*nyoooom*"
    n "Holy hell, she's fast on those wheels."
    n "Fuck, you're staring aren't you? You shouldn't stare."
    n "She's so goddamn large though it's hard to look anywhere else."
    n "It looks like she's going to the cafe too."
    n "You speed up your pace to open the door for her but she manages to do it on her own without any problem."
    n "In fact, she ends up holding it open for you with her tail."

    scene bg cafe with dissolve

    play music "audio/music/Mere Notilde - Empty Room.ogg" fadein 1.0
    #play music "audio/music/vylet - glamour.ogg" fadein 1.0

    show box:
        ypos 0

    show mishka neutral at offscreenleft
    show olivia looking at norm with dissolve:
        xpos 520

    player "Thanks."

    olivia @ say "No problem."

    n "She wheels herself over to the counter."

    show olivia neutral at norm with move:
        xpos 300

    show mishka neutral at norm with dissolve:
        xzoom -1
        xpos 1400

    olivia @ say "How's my second favorite rat?"
    
    show mishka happy

    mishka @ say "Dobre! A tih?"

    olivia @ say "Uhh, horuh... horush... horrorshow... horuhshow? Is that how you say it?"
    
    show mishka winki

    mishka @ say "Mh-hm!"
    
    #show mishka neutral
    
    mishka @ say "So what'll it be for you today?"

    olivia @ say "Hm. Can I get a rum and coke?"

    show mishka sad

    mishka @ say "Err... Nyet, I'm afraid we don't sell the alcohols..."

    olivia @ say "I'm just kiddin'."
    olivia @ say "I'll have a black coffee."
    
    show mishka happy

    mishka @ say "Oh haha you joker! Of course, coming right up!"

    olivia @ say "Thanks~"
    
    show mishka neutral

    n "The gator lady swipes her card and rolls out of the way."

    show olivia at offscreenleft with move:
        yalign 0
        
    show mishka with move:
        xpos 1550

    mishka @ say "Hey [name]! How are your affairs today?"

    player "I'm good. You?"
    
    show mishka sad wave

    mishka @ say "Meh, could be worse. Will it be the usual today?"
    
    show mishka neutral

    player "Actually I was thinking of trying something new today."

    mishka @ say "Oh?"

    player "Yeah, I'm in the mood for something really sweet."
    
    show mishka anxious grin

    mishka @ say "Hmm... I think I've got just the thing for you!"

    player "Really? What is it?"
    
    show mishka silly wink

    mishka @ say "It's a surprise!"

    player "Alright, I'm trusting you on this."
    
    show mishka -silly -wink -anxious -grin happy

    mishka @ say "You will not be disappointed!~"

    n "You hold out your debit card and she swipes it through the machine."
    
    show mishka neutral

    mishka @ say "It'll be ready in just a minute!"

    player "Thanks!"

    hide mishka with dissolve

    n "You wander over to a table to sit and idly swipe through your phone's homescreen while Mishka works on the drinks."
    n "A short while later she calls the alligator girl up to take hers."

    show mishka neutral at norm with dissolve

    hide olivia

    show olivia neutral at offscreenleft:
        xzoom -1
        yalign 0

    mishka @ say "Olivia!"

    n "The scaly lady rolls past the pick-up counter, taking her drink."
    show text "{color=d0dbff} {/color}":
        ypos 46
        xpos 940
    olivia "Thanks!{nw}"
    show text "{color=d0dbff}Thanks!{/color}":
        ypos 46
        xpos 940

    #show say with MoveTransition(delay=.3):
        #xpos 500

    show olivia say at offscreenright with MoveTransition(delay=1.5):
        yalign 0

    #show olivia with MoveTransition(delay=.3):
     #   xpos 560

    #show olivia say with MoveTransition(delay=.52):
     #   xpos 1610

    #show olivia at offscreenright with MoveTransition(delay=.49)

    #show olivia at offscreenright
    #show say at norm
    #with MoveTransition(delay=1.5)

    #show olivia say at offscreenright with MoveTransition(delay=1.5)

    hide text

    n "A moment later Mishka calls you up."

    mishka @ say "And here's yours, [name]!"

    player "Thank you!"
    
    show mishka nya

    mishka @ say "I hope you enjoy! Tell me if you like it!"

    hide mishka with dissolve
    hide olivia
    show olivia at offscreenright:
        yalign 0

    n "You take your drink back over to your table and wait for it to cool before taking a sip."
    n "It's as bland as the yearly Call of Battlefield games and more bitter than the virgins on the Mongolian spearfishing forum you frequent."
    n "What the hell Mishka, is this what you consider sweet back home...?"

    olivia "Pleh! What is this sugary bullshit!?"

    n "You hear angry rolling noises whoosh past you."

    show mishka despondent at norm with dissolve:
        xzoom -1
        xpos -350
    show olivia neutral at norm with move:
        xzoom 1
        xpos 200

    olivia @ say "One sip was enough to give me diabetes! And I'm pretty sure I didn't ask for milk either."
    olivia @ say "You ever heard of a reptile who drinks milk?"

    n "You walk up to the counter."
    
    show olivia looking

    player "Yeah, unless my taste buds are on the fritz I think you gave me her drink."
    
    show olivia neutral

    show mishka derp
    
    mishka @ say "Ah, I am so sorry! Did I get them mixed up...?"

    olivia @ say "Here, lemme see that."

    n "Olivia snatches the drink right out of your hand and takes a big gulp."

    olivia @ say "Ahhh... that's the stuff."
    olivia @ say "Hey sorry for flipping out at you. You know how it is in the morning before you've had your coffee, am I right?"
    
    show mishka anxious grin

    mishka @ say "O-of course!"

    olivia @ say "I'll see ya around, rat girl."
    
    show mishka neutral

    mishka @ say "Later gator!"

    show olivia:
        xzoom -1
        
    pause .6

    show olivia at offscreenright with move:
        yalign 0

    n "Well that sure was something."
    n "That Olivia certainly lives up to the stereotype of crocodilians being chill except when it comes to food, then they become aggressive killing machines."
    
    show mishka sad wave

    mishka @ say "Vybachte, [name], I must not have been paying attention to which drink was which."
    mishka @ say "I will make you a new one."

    menu:
        mishka "{cps=0}I will make you a new one.{/cps=0}"
        "Please do.":
            #finished
            player "Please do."
            


            n "You patiently wait for Mishka to finish your drink."
        "I'll just take the one Olivia left behind.":
            #finished
            n "You notice Olivia left the drink you ordered on the counter."
            n "No reason to let it go to waste, right?"
            n "Haha it's not like you want to drink out of the same cup she drank from"
            n "Putting your lips where hers were just a moment ago"
            n "Probably tastes like gator saliva haha gross"

            player "It's fine, Mishka, I'll just take this one."
            
            show mishka despondent

            mishka @ say "Are you... are you sure?"

            player "Hahayeahit'sfinedon'tworryaboutit!"

            n "Mishka gives you a strange look and shrugs."
            
            show mishka neutral


    n "Eager to finally taste this \"sugary bullshit\" you give it a good blow and take a sip as soon as she hands it to you."
    n "Mishka watches in anticipation as you hold the cup to your mouth."

    show mishka anxious grin
    
    mishka @ say "Well? What do you think?"

    n "It certainly is sweet. Even with such a tiny sip, your mouth is filled with a multitude of overpowering flavors."
    n "Peppermint, honey, and vanilla burn into your taste buds, tamed only by the cinnamon sticking to the back of your throat."

    player "Mmh. It's... definitely unique."
    
    show mishka cute

    mishka @ say "It's something my mother used to make around Christmas time! Perfect for long Ukranian winters!"
    mishka @ say "I know it's kinda early for that but I thought you might like it!"

    n "You take another sip. Now that you know what to expect you can appreciate it more. It's thick and creamy and would be perfect next to a fireplace."

    player "Yeah, this is making me wish it was December already."
    
    show mishka happy

    mishka @ say "I'm glad you like it! It's not really on the menu but I'd be happy to make it for you any time!"

    player "Aww, that's really sweet of you! Any sweeter and I'd get diabetes."
    
    show mishka nya

    mishka @ say "Heh... I do not know what that is..."

    player "Oh. Don't worry about it then. Point is, thanks for the secret menu drink."
    player "Andalsoforbeingsonicetomeallthetimeandstuff"
    
    show mishka shy

    mishka @ say "What was that?"

    player "Nothing!"
    player "Hey I gotta run but I'll see you around, k?"
    
    show mishka neutral

    mishka @ say "Of course! Dah skorovuh!"

    stop music fadeout 1.0
    
    scene bg codadorm with fade

    show box:
        ypos 0

    n "You tried your best to ration your drink on your walk back to your dorm to enjoy it longer, but you couldn't stop yourself from taking big sips and emptying it before you even reached the door."

    show bg static1
    pause .04
    show bg static3
    pause .02
    show bg static2
    pause .04
    show bg static3
    pause .02
    show bg codadorm

    n "Oh well, that just gives you an excuse to go back to the cafe and see Mishka again soon."
    
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