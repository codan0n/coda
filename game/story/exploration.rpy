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
                    
                    #$ trackEventsCurrentWeather = 
                    
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
    
    
    #only available on sunny days
    
    "gunner track scene"
    
    
    return

label linaTown:
    #remove linaTown from townEvents list, maybe add linaTown2 if there will be a scene for that later
    $ townEvents.remove("linaTown")
    
    scene bg town with fade
    
    init:
        $ renpy.music.register_channel("channel1", loop=True)

    init python:
        renpy.music.register_channel("channel2", loop=True)
    
    
    play channel1 "audio/ambient/outdoors people talking.ogg" fadein .5
    
    show box:
        ypos 0
    
    n "After class, you decided to walk around town on nothing more than a whim."
    n "It's a little crowded but it's something fresh and exciting. You do a fair bit of window shopping, eyeing the useless trinkets and things shopkeeps put out for display."
    n "$200 for a knife? Get real."
    n "... You might go back for it, it was a really nice knife."
    n "Is that really all there is to do in the city though? Buy stuff you didn't know you wanted?"
    
    play music "audio/music/vylet - glamour.ogg"
    
    n "The sound of live music hits your ears among the incessant chattering. Now that might be worth checking out."
    n "You follow the sound and are somewhat disappointed to see it's just a lone street performer and not part of a bigger event."
    n "Still, you came out all this way, you might as well stick around to enjoy the tune."
    n "People walk by, some dropping coins and bills into the open saxophone case at the performer's feet."
    n "She even has an electronic card reader set up for tips as well."
    n "Beggars sure have gotten pretty advanced these days."
    n "When she finishes her song she waves to you. You should have expected this. You haven't donated anything yet but you're the only one who hadn't quickly moved on."
    
    show lina at norm with dissolve
    
    lina @ say "Heya! I've seen you around before!"
    
    player "You have?"
    
    lina @ say "Yeah, on campus! You're a student too, aren't you?"
    
    player "Oh there, right. I'm afraid I never noticed you."
    
    lina @ say "That's alright. I'm just kinda in the background."
    
    player "Well it's nice to finally meet you I guess! My name's [name]."
    
    lina @ say "I'm Lina! A pleasure to finally get to meet you as well!"    
    lina @ "You're a human!"
    
    player "And you're a... bird?"
    
    lina @ say "A harpy eagle to be precise. We can see from pretty far away."
    lina @ say "It's always easy to spot you 'cause you're the only human around!"
    
    player "Thanks? I think? You haven't been stalking me, have you?"
    
    lina @ say "Noooo, nothing like that! I just see you talking with that bunny girl and secretary bird all the time."
    
    player "Yeah they're... something haha."
    player "So uhh, you come here often?"
    
    lina @ say "Usually on the weekends! That's when lots of people are out and about and usually have a buck to spare *chirp~*"
    
    n "You take a look inside her saxohone case. There's probably around $50 in there."
    
    player "How long have you been out today?"
    
    lina @ say "A couple hours! But y'know how it is, tuition ain't gonna pay for itself!"
    
    player "Haha yeah..."
    
    n "You have a brief moment of clarity on how lucky you are to not have to work."
    
    player "Well I don't wanna cut into your time too much-"
    
    lina @ say "No don't worry about it! I love talking with strangers!"
    lina @ say "Unless you've got someplace to be..."
    
    menu:
        lina "{cps=0}Unless you've got someplace to be...{/cps}"
        "Stay and chat.":
            #finished
            $ goodEnd = goodEnd + 1
            player "In that case, I suppose I can stay and chat a while longer."
            
            lina @ say "Yeah it's totally fine! I need a break from playing every now and then anyway."
            
            n "She picks up a bottle of water from next to her case and takes a sip."
            
            player "I take it you're in the band at Harmonia?"
            
            lina @ say "Yup!"
            lina @ say "The marching band, the concert band, and the jazz band!"
            lina @ say "Jazz band is my favorite~"
            
            player "Wow, you're one of those over-achiever types aren't you? I wish I had that level of dedication."
            
            lina @ say "Not really? At least it doesn't feel like it. I just enjoy playing music!"
            lina @ say "So to that end it doesn't really feel like work. I'm just having fun!"
            
            player "That sounds like a nice attitude to have."
            player "I guess I'm still trying to figure out what I enjoy doing."
            
            lina @ say "I dunno what I'd do without a saxophone in my wings!"
            lina @ say "I just picked it up on a whim one day and 8 years later here I am!"
            
            player "Don't you ever get bored of it?"
            
            lina @ say "Hmmm...."
            lina @ say "Nope! I'm thinking about compositions pretty much every day. I get into a flow, you know?"
            lina @ say "I feel like it's exactly what I'm meant to do."
            #lina @ say "Nope! Well, not for long anyway."
            #lina @ say "Sometimes I go a few days without practicing but then I get the itch to bust out a new tune or play an old favorite!"
            
            player "How do you even play sax with a beak anyway?"
            
            lina @ say "Like this!"
            
            n "She holds the mouthpiece up to her beak and plays a scale. You're still not sure how this works."
            
            player "I... see."
            
            lina @ say "Try not to think about it too much."
            
            player "Right... well it was nice finally meeting you Lina! I'm gonna head back to my dorm for now but don't be afraid to say hi if you spot me later!"
            
            lina @ say "I'll try! It was nice to finally hear your voice!"
            
            n "You should give her a tip."
            
            menu:
                "Tip $5":
                    n "You pull a 5 dollar bill from your wallet and drop it in her case."
                    
                    lina @ say "Thanks!~"
                
                "Tip $20":
                    n "Oh what the hell, she deserves it more than you do."
                    n "You drop a 20 in her case and watch her eyes light up."
                    
                    lina @ say "Ohmygosh thanks!~"
                    
            stop sound fadeout 1.0
            
            n "You smile and give her a parting wave, then make your way back to your dorm."
            
            
            stop music fadeout 1.5
            stop channel1 fadeout 1.0
            hide lina with dissolve
        "Leave":
            #unfinished
            $ avaPoints += 1
            player "Yeah, sorry I have to be somewhere soon."
            
            lina @ say "Ahh ok! Sorry to keep you!"
            
            player "No worries. I hope to see you around later."
            
            menu:
                "Tip $5":
                    n "You pull a 5 dollar bill from your wallet and drop it in her case."
                    
                    lina @ say "Thanks!~"
                
                "Tip $20":
                    n "Oh what the hell, she deserves it more than you do."
                    n "You drop a 20 in her case and watch her eyes light up."
                    
                    lina @ say "Ohmygosh thanks!~"
                    
            stop sound fadeout 1.0
            
            n "You smile and give her a parting wave, then make your way back to your dorm."
            
            hide lina with dissolve
            
            n "However it's not long before you bump into Ava."
            
            show ava casual unimpressed at norm with dissolve
            
            ava @ say "Who was that you were talking to?"
            
            player "Uhh I think she said her name is Lina? She-"
            
            ava @ say "Oh you're talking to other bird girls now? That's nice."
            
            player "She actually said hi first so..."
            
            show ava annoyed
            
            ava @ say "What was that you gave her?"
            
            player "Yeah it was just a tip for-"
            
            show ava unsure
            
            ava @ say "You paid *her*??? For what? Loitering and playing annoying music? Do you also pay people when they blast music on their phones?"
            
            player "That's completely differ-"
            
            show ava seriously
            
            ava @ say "Jazz is just playing random notes and pretending it sounds good!"
            ava @ say "It's not a true art!"
            
            menu:
                "Like photography?":
                    $ avaPoints = avaPoints - 2
            
                    player "Like how photography is just pointing and clicking?"
                    
                    show ava angry
                    
                    ava @ say "Bite your tongue! Don't talk about what you don't understand!"
                    ava @ say "Good photographers know how to frame a shot and *create* a message! We have to manage lighting, contrast, color spaces, attention lines, -"
                    
                    player "I dunno, it seems like anybody can just open the camera app on their phone and take a good shot."
                    
                    ava @ say "Amateur! You think your overblown highlights and tacky oversaturation deserves to be put in a museum?!"
                    
                    player "I'm just saying nobody cares about photography as an art form anymore."
                    
                    show ava portrait angry
                    
                    ava @ say "That's the problem! An artist is someone who transfers feelings from their heart onto a medium that can't be expressed in language alone."
                    
                    player "I think that's what Lina was telling me. She said she lives to play music or something like that."
                    
                    show ava unsure
                    
                    ava @ say "That-!"
                    ava @ say "Hmph! What does she know?"
                "You're overreacting.":
                    
                    n "ava bitches about never getting paid for her art, recounts not selling anything at a fair"
            
            stop channel1 fadeout 1.0
            stop music fadeout 1.5
            
    
    
    
    
   
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
            player "Please do."
            
            n "You patiently wait for Mishka to finish your drink."
        "I'll just take the one Olivia left behind.":
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