label chapter1:

#    "test"
#    
#    $ muffin = "delicious"
#    $ bagel = "savory"
#    $ pastry = muffin
#
#
#    if pastry == muffin:
#        n "this pastry is [pastry]"
#
#
#
#    #######
#    
#    label pastry:
#        $ choice = "muffin"
#        
#        return choice
#        
#    n "you chose a [pastry]"
#    #call pastry?
#    # pastryChoice = pastry
#    
#    #test using default to set values not previously set for save compatibility
    



#    scene bg campus summer day clear with fade
#    
#    show gunner neutral at left
#    show rori neutral at right
#    
#    gunner @ say "gunner speaking"
#    
#    rori  @ say "rori speaking" 
#    
#    gunner "gunner speaking"
#    
#    rori "rori speaking"
#    
#    gunner "gunner speaking"
#    
#    rori "rori speaking"
#    
#    
#    
#    "endtest"
#    "test"
#    init:
#        $ timer_range = 0
#        $ timer_jump = 0
#    
#    transform alpha_dissolve:
#        alpha 0.0
#        linear 0.5 alpha 1.0
#        on hide:
#            linear 0.5 alpha 0
#        # This is to fade the bar in and out, and is only required once in your script
#
#    screen countdown:
#        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
#        bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.
#        
#label movingMenu1:
#    
#    $ time = .5
#    $ timer_range = .5
#    $ timer_jump = 'movingMenu2'
#    show screen countdown
#    
#    menu:
#        "Choice 1":
#            hide screen countdown
#            "You chose 'Choice 1'"
#            jump menu1_end
#        "Choice 2":
#            hide screen countdown
#            "You chose 'Choice 2'"
#            jump menu1_end
#   
#label menu1_slow:
#    "You didn't choose anything."
#    
#label menu1_end:
#    "Anyway, let's do something else."
#    
#label movingMenu2:
#    
#    $ time = .5
#    $ timer_range = .5
#    $ timer_jump = 'movingMenu1'
#    show screen countdown
#    
#    menu:
#        "Choice 1":
#            hide screen countdown
#            "You chose 'Choice 1'"
#            jump menu2_end
#        "\[correct\]Choice 2":
#            hide screen countdown
#            "You chose 'Choice 2'"
#            jump menu2_end
#   
#label menu2_slow:
#    "You didn't choose anything."
#    
#label menu2_end:
#    "Anyway, let's do something else."
#    
#        
#    
#    
#    
#    "end test"


    stop music fadeout .5
    
    "Coda is a purely fictional story created by a diverse team with various different backgrounds and beliefs. The actions and views of some characters do not necessarily reflect those of the creators."
    "Viewer discretion is advised."
    "Please note that this is a work in progress build that is unfinished in many places."
    
    scene bg letter with fade
    
    show box with Dissolve(.2):
        ypos 0

    n "You got a letter."
    n "The name on the envelope said \"Harmonia University.\""
    n "It's ridiculous... Could it really be true?"
    n "Such a prestigious university wants you...?"
    n "You never even applied."
    n "Did they send this by mistake?"
    n "But it's signed by the dean himself."
    
    n "\"Congratulations! You have been admitted to Harmonia University's undergraduate program!\""
    n "\"We invite you to one of the highest ranked learning institutions in the world to experience a plethora of exciting opportunities!\""
    n "\"Our passionate staff will prepare you for a lifetime of success. Join us as you step into the next chapter of your life!\""
    
    n "It goes on for a while, full of marketing buzzwords and diversity statistics."
    n "There's a note at the bottom."
    
    n "\"Given your situation, I would like to personally welcome you and offer you a tour of the campus myself. It would be an honor to have you among us.\""
    n "\"I have arranged comfortable living accommodations for you, so that you may focus on getting the most out of your education. Your scholarship will cover all your necessities and then some.\""
    n "\"On behalf of Harmonia University, we eagerly await your arrival.\""
    n "\"Nicodemus Kaczynski\nDean of Harmonia University\""
    
    n "It's strange, but can you really say no?"
    n "Might as well go for it. There's nothing left for you at home anymore."
    #there's no reason to stay home anymore
    n "Your parents died of that damn disease three years ago. Since then you haven't really done anything with your life."
    n "This could be a good opportunity to start fresh."
    
    #yes this bit is just a silent hill 2 reference
    
    scene bg black with fade
    
    n "A few weeks later"
    
    ########
    
    #scene bg campus summer day clear_sunny_day with dissolve
    scene bg campus summer day clear with dissolve
    #background names can't have capital letters
    
    play music "audio/music/vylet - Hard to Say Anything.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
        
    show nicodemus neutral at center with dissolve:
        ypos y_nicodemus
        matrixcolor BrightnessMatrix(0.05)
    
    nicodemus @ say "...that about concludes our tour of Harmonia's campus. What did you think? Not too pretentious, I hope! Bahahaha!"
    nicodemus @ say "I'm reminded of when I was a new student here myself. A bit nervous but so full of wonder and excitement! It felt like anything was possible!"
    nicodemus @ say "Forging lifelong friendships! Making a name for myself in the academic community! Joining clubs and causing a ruckus!"
    nicodemus @ say "Why, I even found the love of my life sitting under that oak tree over there."
    nicodemus @ say "My point is, anybody can blow through four years of university, get their diploma and proceed with their life like it never even happened."
    nicodemus @ say "But I implore you to really make the most of what you've been given!"
    nicodemus @ say "Study hard but take some time to search for something that makes you happy, whether that's being with friends or making your mark on society or just living in the moment!"
    nicodemus @ say "Find what's important to you!"
    nicodemus @ say "Now then, do you have any questions, young lad?"
    
    n "To be honest, you weren't really paying attention for the past hour until now."
    n "The dean is a short raccoon who wears an old timey but distinguished suit. A pair of small spectacles rests at the edge of his snout. He carries a cane but doesn't lean on it too much."
    n "He's like a caricature of a kind old grandpa who tells war stories but leaves the gorey parts out."
    n "He seems like a nice guy and all, but you just can't escape the feeling like you don't belong here."
    
    $ name = "player"
    define player = Character("name", color="#2a2a2a", what_color="#9af3a8", callback=name_callback, cb_name = "player")
    
    default questionInvite = False
    default questionFitIn = False
    default questionTour = False
    default questionAsked = False
    
    $ questionText = "He seems like a nice guy and all, but you just can't escape the feeling like you don't belong here."

label nicodemusQuestions:
    menu:
        n "{cps=0}[questionText]{/cps=0}"
        "Why did you invite me here?" if questionInvite == False:
            $ questionInvite = True
            
            player "I'm grateful to be here, but I don't understand *why* I'm even here."
            player "I never submitted an application."
            
            nicodemus @ say "We keep tabs on \'persons of interest.\' You know, brilliant young students with bright futures to send ads in the mail to. They make for great alumni."
            
            player "Me? Some sort of prodigy?"
            
            nicodemus @ say "Well you *are* the smartest human on Earth at the moment."
            
            player "So I'm just here for the optics? For your marketing team to brag about how the college is so diverse it has a human?"
            
            nicodemus @ say "Precisely."
            nicodemus @ say "That is, at least on paper, the official reason for how I brought you on board."
            nicodemus @ say "The actual reason has more to do with..."
            
            n "He hesitates, seemingly unsure of what words to use."
            
            nicodemus @ say "You see, your predicament reminded me of an old friend of mine. Are you familiar with the Tasmanian tiger?"
            
            "The dean reaches into his coat pocket and pulls out a photograph."
            
            scene bg tasmaniantiger with dissolve
            
            pause 2.3
            
            menu:
                "What about them?":
                    show box with Dissolve(.2):
                        ypos 0
                
                    "You shake your head."
                    
                    player "Never seen them before."
                    
                    nicodemus @ say "No one has, not for a few decades. At least, not a living specimen."
                    nicodemus @ say "I'm afraid they've gone extinct."
                "They're all gone, aren't they?":
                    show box with Dissolve(.2):
                        ypos 0
        
                    player "They're not around anymore, right?"
                    
                    nicodemus @ say "Correct, they went exctinct decades ago. There's not even a color photograph of a living one."
                    
            n "\"Extinct.\""
            n "The word sends chills down your spine."
            n "You've been trying not to think about it, but that's what your species will be once you die."
            n "All that will be left of you are stories and photographs."
            
            scene bg campus summer day clear with dissolve    
            
            show box with Dissolve(.2):
                ypos 0      
                
            show nicodemus neutral at center with dissolve:
                ypos y_nicodemus
                matrixcolor BrightnessMatrix(0.05)
            
            nicodemus @ say "He was a good friend, someone you could always count on. But as time went on, the burden of being the last of his kind got to him."
            nicodemus @ say "He withdrew himself from everyone and eventually withered away, like some forgotten house plant. I'd hate for you to suffer the same fate."
            nicodemus @ say "You see what I'm getting at, don't you?"
            
            n "You give a somber nod."
        "Will I fit in?" if questionFitIn == False:
            $ questionFitIn = True
            
            player "I'm not sure I really fit in here. This seems like the kind of university you only get into if you come from old money."
            
            nicodemus @ say "That was certainly true back in the day, but we've been getting more inclusive over the years. We'll take any money now, not just old money heh."
            nicodemus @ say "So don't feel bad if you don't come from the wealthiest household. Money won't buy you honest friends."
            nicodemus @ say "Just treat people with the kindness and respect they deserve and give them a chance. You're bound to find your niche sooner or later."
        "What's with the tour?" if questionTour == False:
            $ questionTour = True
            
            player "A dean like you must be pretty busy. Why'd you take the time out of your day to personally give *me* a tour of the campus?"
            
            nicodemus @ say "Less busy than you'd imagine! I may run the show around here but the show mostly takes care of itself."
            nicodemus @ say "I usually just sign documents and attend meetings. People look to me for approval, but I'm really just acting as a figurehead most of the time."
            nicodemus @ say "Someone to stand around and look wise."
            nicodemus @ say "The departments handle all the number crunching and recomendations, I just give the final authorization."
            nicodemus @ say "So I don't mind getting out of the office to have a pleasant chat with the students."
            nicodemus @ say "Feel free to break me out of that prison from time to time to discuss whatever's on your mind."
            nicodemus @ say "It's also a great photo opportunity."
            
            n "He points to a photographer in the distance, crouched beside a water fountain trying to look inconspicuous with his giant telephoto lens pointed at you."
        "That's all" if questionAsked == True:
            player "That's all."
            
            jump movingOn
    
    $ questionAsked = True
    
    $ questionText = "Was that all you wanted to ask?"
        
    nicodemus @ say "Was that all you wanted to ask?"
        
    jump nicodemusQuestions
        
label movingOn:
    nicodemus @ say "Very well! I'll let you have a break from my ramblings. I believe your orientation is coming up soon. You remember how to get there? Good."
    nicodemus @ say "It was a pleasure to finally meet you in person! You seem like a real stand up guy and I have no doubt you'll find success and whatever else you're looking for during your time at Harmonia!"
    
    player "Thanks. It was nice to be welcomed by the dean himself."
    
    nicodemus @ say "I'm glad I could be of service! Now then, if you'll excuse me..."
    
    n "Nicodemus gives you a warm smile before slowly trodding away."
    
    hide nicodemus with dissolve
    
    #n "Even as the sun began to set, the campus was swarming with freshly admitted students either in tour groups or exploring their new surroundings on their own."
    n "You don't have much time to spare, so you make your way to your scheduled orientation meeting."
    
    stop music fadeout 2.0

label college_orientation:
    #ACT 1
    #___saturday1

    play sound "audio/sound effects/door opening.wav"

    scene bg lecturehall with fade

    show box with Dissolve(.2):
        ypos 0

    play music "audio/ambient/indoors people talking.ogg" fadein .4
    
    #n "You had some trouble finding the building you're supposed to be in but managed to make it just in time."
    n "After checking in, you were directed to a lecture hall where several others are already seated and chatting among themselves."
    n "You look around for an open spot and find one near the front of the room."
    n "Weird looks are shot in your direction, followed by whispers as you walk past. They act like you don't notice their stares and comments."
    n "You're used to it though, it happens everywhere you go. Understandably so, considering your kind is about as rare as a unicorn."
    n "Is this what college is? It already feels like a prison."
    n "You slump down in your seat and try to ignore the world around you, praying that this will be over with quickly."
    #n "You slump down in a seat and try to astral project into the future, if only to get away from here."
    #n "It's not working."
    n "Eventually a woman walks up to the podium and the voices around you quiet down."

    show margaret neutral at center with Dissolve(.5):
        ypos y_margaret

    stop music fadeout 2.0

    margaret @ say "            Ahem            "

    show margaret happy

    margaret @ say "Welcome to Harmonia University, new students! My name is Margaret Ellen and I'm very excited to introduce you to the next chapter of your lives!"
    margaret @ say "This orientation marks the beginning of your journey into the finest academia has to offer! Everything you'll learn and experience over the next four years starts here."

    hide margaret with dissolve
    
    n "You start to tune out of what she's saying. It's just boring introductory formalities anyway."
    n "You hear the door open, followed by hoofsteps coming down the stairs. Must have been a straggler who arrived late."
    n "The room's pretty full but there's another vacant seat next to yours."
    #n "Please deer god, you pray whoever it is doesn't sit there. You've had a rough day and don't want to have to make friends already."
    n "A moment later, a nerdy looking ram squeezes past you and sits in it."
    
    show rori concerned at center with moveinright:
        ypos y_rori
        xpos 1400
        
    pause .25

    rori @ say "D-did I miss anything?"

    player "Nothing important."
    #n "You snap out of your daydream and shake your head before returning your attention to the presenter."
    #n "You shake your head and return your attention to the presenter."
    
    hide rori with dissolve

    show margaret neutral at center with dissolve:
        ypos y_margaret

    margaret @ say "...If you haven't already, go ahead and introduce yourselves to those sitting around you!"
    margaret @ say "Go on, don't be shy!"

    hide margaret with dissolve

    play music "audio/ambient/indoors people talking.ogg" fadein .4

    show rori worried at center with dissolve:
        ypos y_rori
        xpos 1400

    rori @ say "Hey um... Gosh, I don't know how to do this."
    
    show rori neutral
    
    rori @ say "My name's Rori. What's yours?"

    $ nameValid = False
    define player = Character("[name]", color="#2a2a2a", what_color="#9af3a8", callback=name_callback, cb_name = "player")
    jump namescript
    label namescript:

        python:
            name = renpy.input("What is your name?", length = 14)
            name = name.strip()
            nameValid = True

            if name.upper() == "RORI":
                "Choose another name."
                nameValid = False
            if name.upper() == "MISHKA":
                "Choose another name."
                nameValid = False
            if name.upper() == "AVA":
                "Choose another name."
                nameValid = False
            if name.upper() == "CLAIRE":
                "Choose another name."
                nameValid = False
            if name.upper() == "MARGARET":
                "Choose another name."
                nameValid = False
            if name.upper() == "ELLEN":
                "Choose another name."
                nameValid = False
            if name.upper() == "ROSE":
                "Choose another name."
                nameValid = False
            if name.upper() == "GUNNER":
                "Choose another name."
                nameValid = False
            #if not name:
            if name == "":
                name = "Hugh"
                nameValid = True

        if nameValid == True:
            "Your name is [name]?"
        else:
            "Choose another name."
            jump namescript
            "Your name is [name]?"


    menu:
        "{cps=0}Your name is [name]?{/cps}"
        "That's right":
            #n "You muster up the energy to at least engage in polite conversation."
            #n "Despite all your practice, you can't quite pull off the cool mysterious persona yet so this is the best way to avoid spilling your spaghetti."
            "This is the first person your age that you've spoken to in years. You've almost forgotten how to speak around your peers."
            "All that comes from your throat is a meek and generic greeting."
            
            player "My name's [name]. Nice to meet you."
        "That's wrong":
            jump namescript

    show rori cheery
    
    rori @ say "Nice to meet you too!"
    rori @ say "..."
    
    show rori worried noblush
    
    rori @ say "So... uhhh..."
    
    show rori neutral
    
    rori @ say "What are you majoring in?"
    
    n "Wow, no 'Are you really a human? I thought your kind went the way of the dinosaurs!'"
    n "Like you've heard countless times."

    player "I haven't really decided yet. Thought I'd figure it out while I'm here. What about you?"

    show rori laugh

    rori @ say "Computer engineering! I've always loved messing around with computers. I taught myself how to program since my high school didn't have any classes for it."

    menu:
        rori "{cps=0}Computer engineering! I've always loved messing around with computers. I taught myself how to program since my high school didn't have any classes for it.{/cps}"
        "Hahaha nerrrrd":
            $ roriPoints -= 1
            $ calledRoriNerd = True

            show rori neutral

            player "That stuff's a bit too nerdy for me."
            
            show rori smirk lookingaway

            rori @ say "Oh... that's understandable. It's not for everyone."
            
            n "There's a hint of smugness to his voice."

            player "It requires a lot of math knowledge, doesn't it?"
            
            show rori neutral -lookingaway

            rori @ say "Sorta? I mean it helps to have a solid understanding of algebraic equations and trigonometry."

            player "Ugh, spare me the details. Please."

            show rori laugh

            rori @ say "Hahaha okay! It's actually pretty routine until you come across a bug, then it's like solving a puzzle."

            player "Never been good at puzzles."

            show rori neutral

            rori @ say "Then computer engineering isn't for you."

            player "I'll cross that one off the list."

        "Play any games?":
            $ roriPoints += 1
            
            show rori neutral

            player "You play any games? I got really into World of Boarcraft a few years ago."
            
            show rori soyface

            rori @ say "I love World of Boarcraft! I used to skip school all the time just to play it."
            
            show rori neutral

            player "Not recently, I hope. The newer expansions kinda turned that game into hot garbage."

            rori @ say "Yeah... Still, I used to dream of making games like that."
            rori @ say "I started out learning to write scripts to make the mundane parts of the game easier, then I got banned when I figured out how to edit hex values to give myself infinite gold."

            player "Making games would be pretty cool. I've always had ideas but never the skills or willpower to actually make anything. It seems like it would be really hard."

            rori @ say "Oh you bet it is. I've messed around with some game engines before and it can quickly get overwhelming."
            
            show rori anxious
            
            rori @ say "I've got something I've been working on for a few years. I hope I can still work on it here but I heard my differential equations professor likes to assign a lot of homework."

            player "Damn. Well good luck with that."

            show rori laugh

            rori @ say "Thanks! I'll need it!"

        "At least you know what you wanna do.":
            show rori neutral

            player "That's cool. At least you know what you wanna do."
            
            show rori cheery blush

            rori @ say "Haha thanks but I'm actually not sure about that. It's a pretty broad field and I don't exactly know where I'm gonna end up."

            show rori anxious

            rori @ say "I wouldn't wanna end up administrating some boring office's network, ya know? I got into computers cause I wanted to live in like a science fiction world."

            player "Yeah? Boring office work can be good money though."

            show rori neutral

            rori @ say "I guess it's not really about the money for me. Don't get me wrong, money's nice and all but I'd rather make my dream game or develop an AI companion or something cool like that."

            player "I get what you mean. I'm just here to figure out what I'll enjoy doing for the rest of my life."
            
            show rori cheery
            
            rori @ say "No plans huh? Well I hope you can figure something out sooner than later!"
            
            show rori neutral
            
            player "Thanks, me too haha."

    n "You chat with Rori for a bit longer until Ms. Ellen clears her throat and gets the rooms attention."

    hide rori with dissolve

    show margaret neutral at center with dissolve:
        ypos y_margaret

    stop music fadeout 2.0

    margaret @ say "Ahem. Now that you've become acquainted with your neighbors, I'd like to know more about you!"
    margaret @ say "I'll pick a few students at random... Please say your name, what you're majoring in, and something about yourself."

    n "Ms. Ellen points to a girl toward the back of the room."
    
    show margaret happy

    margaret @ say "You there! With the camera!"

    hide margaret with dissolve
    
    pause .1

    show ava typical happy at left:
        ypos y_ava
        xoffset 75
        xzoom -1
    with dissolve
    
    ava @ say "Um hi...! My name's Ava and, as you might have guessed, I'm a photography major! I often go out into nature and shoot wildlife and landscapes, but I also dabble in street photography."
    
    show ava excited at hop
    
    ava @ say "I like the idea of capturing rare moments in time that disappear as quickly as they come."
    #ava @ say "I like the idea of capturing the rarely seen or overlooked aspects of life!"
    
    show ava happy
    
    ava @ say "Umm, I don't know what else to say? I just kind of like experimenting and finding new ways to view things."

    hide ava with dissolve

    show margaret neutral at center with dissolve:
        ypos y_margaret

    margaret @ say "Very good! Next, how abouuuuutttt..."
    
    pause .05
    
    margaret "{nw}"
    
    pause .05
        
    #pause .3

    show margaret neutral at flipright
    
    pause .3
    
    #show margaret with move:
    #    xzoom -1
    #    xoffset 500
        
    pause .3
    
    show margaret neutral at flipleft
    
    pause .2
    
    show margaret with move:
        ypos y_margaret
        xoffset -250
        
    pause .4
    
    margaret @ say "Hmm..."
    
    show margaret neutral at flipright
    
    pause .5
    
    margaret @ say "You, in the pink sweater!"

    hide margaret with dissolve

    show claire sweater surprised earsup at center with dissolve:
        ypos y_claire
        xoffset 450

    claire @ say "        Moi?        "
    
    show claire sweater derp
    
    claire @ say "Hiiiii, my name's Claire and I left my major undecided 'cause, well, I couldn't decide what to do!"
    
    show claire sweater wave happy
    
    claire @ say "Something interesting about myself? I was a cheerleader in high school until I broke my leg, and then I joined the chess team and found out I'm actually pretty good at it??"
    
    show claire sweater overjoyed 
    
    claire @ say "I got to go to a national tournament once and came in third place!"
    
    show claire sweater happy -wave
    
    claire @ say "It was fun but I'm always looking for new things to try!"

    hide claire with dissolve

    show margaret neutral at center with dissolve:
        xzoom -1
        xoffset -170
        ypos y_margaret

    margaret @ say "Nicely done! We'll do a couple more. Let's see..."

    show margaret neutral at flipleft
    
    pause .6
    
    show margaret neutral at flipright
    
    pause .6
    
    show margaret neutral at flipleft

    margaret @ say "..."
    margaret @ say "How about you!"

    n "Of course she had to pick you. You pretend to think she's pointing at someone else."

    margaret @ say "Yes, you! We don't bite, I promise!"

    n "You let out a quiet sigh and rise from your seat."

    player "Hi, my name's [name] and I'm also an undecided major, mostly for the same reason. I guess something that's interesting about me is that I'm the last human on Earth."
    player "Which is probably the reason I got accepted here with a full scholarship, 'cause it sure wasn't my grades."

    show margaret melancholy

    n "That gets a few chuckles from the room, but Ms. Ellen just glares at you."

    margaret @ say "Yes well... very good, thank you [name]. Moving on."
    
    show margaret neutral

    n "Ms. Ellen gives a few more announcements before wrapping up her speech and dismissing you all."

    margaret @ say "I hope you all have a wonderful time at Harmonia! That's all I have for you! You're free to go! Have a nice rest of your evening!"

    hide margaret with dissolve
    
    play music "audio/ambient/indoors people talking.ogg" fadein .4

    n "It's about time. You were starting to doze off."
    n "Now that that's out of the way, you can return to your dorm and get your things put away."
    #n "When you arrived earlier today, the dean himself greeted you and showed you to your dorm, no doubt a gesture mandated by the affirmative action council."
    #n "When you arrived earlier today, the dean himself greeted you and personally showed you to your dorm, no doubt to make you feel more welcome given your situation."
    #n "You can't help but feel it was an empty gesture though. He made sure to get you a room all to yourself, as if that wouldn't make you feel more alone."
    n "On your way out, you overhear some familiar voices."

    show ava typical happy at center:
        xoffset 400
        ypos y_ava
    show claire sweater wave happy at center:
        xzoom -1
        xoffset -400
        ypos y_claire
    with dissolve

    claire @ say "Hey! Cool camera! Is that a nifty fifty on it?"
    
    show ava profile whimsical

    ava @ say "Thanks! I never leave home without it! Fifty millimeter is just so versatile!"

    show claire sweater -wave happy

    claire @ say "What dorm are you in? I'm in Saint Mary Hall."
    
    show ava typical excited

    ava @ say "No way! I'm in there too! What room number?"
    
    show ava happy
    show claire earsup

    claire @ say "209A!"
    
    show ava overjoyed

    ava @ say "Me too!!!"
    
    show claire overjoyed

    claire @ say "Oh my gosh this is perfect! We're gonna become best friends ksksksks!"

    hide ava
    hide claire
    with dissolve

    n "Thank goodness they finally decided to move out of the way. The bunny alone was blocking the double doors leading outside."

    scene bg campus summer night clear with dissolve

    play music "audio/ambient/outdoors night crickets.ogg" fadein .4

    show box with Dissolve(.2):
        ypos 0

    n "The sun has passed under the horizon but a few remnants of light illuminate the sky."
    n "You feel exhausted. You're not used to society's hustle and bustle. The tempo is difficult to keep up with after the past few years of keeping to yourself. "
    n "You're not sure you even want to be here, but you figured it would be a waste not to try. You can always quit and go back home if you hate it that much."
    n "Some obnoxious noise fills the air, getting louder."
    n "Oh, it's just a group of people approaching. They appear to be the parents of the other freshmen completing their own tour of the campus."
    n "As they reunite with their kids, they embrace each other, wave goodbye, and some even shed tears."
    n "This must be the moment where they see their babies one last time before pushing them out of the nest."
    n "As you walk past, you overhear them talking about how proud they are of their children and how much they'll miss them."
    n "Damn, these people need to chill. It's not like they won't see each other again during the holidays. Or they can just call. We have the technology."
    #n "Everyone's hugging and saying goodbye like they're not just gonna come back home in a few months for Thanksgiving and Christmas."
    #n "Oh god some of them are even crying."
    #n "Mostly the moms and some of the sons."

    n "Rori sees you slinking off and calls out your name."

    show rori neutral at center with dissolve:
        ypos y_rori
        matrixcolor BrightnessMatrix(-0.05)

    rori @ say "Hey! [name]!"
    rori @ say "Leaving already?"

    player "I don't really have a reason to stick around, do I?"

    rori @ say "Where's your par-"

    show rori anxious at shudder

    rori @ say "...Oh. Sorry."
    
    player "..."

    #n "You just look at him the same way a janitor would look at a child who was projectile vomitting across three tables in the cafeteria."

    show rori yawn lookingaway blush

    rori @ say "A-anyway...! I'm staying in Edgar Hall! What dorm do you live in?"
    
    show rori neutral -lookingaway

    player "I'm over in Swanson."
    
    show rori happy

    rori @ say "Ah, I heard that's the rich people's building."

    player "Rich or endangered."
    
    show rori cheery

    rori @ say "Hah, yeah I guess..."
    
    show rori neutral
    
    rori @ say "..."

    pause .3
    show rori neutral at flipright
    pause .95
    show rori neutral at flipleft

    n "Rori looks around, seemingly unsure of what to say."

    show rori anxious at shudder

    #rori @ say "M-my parents didn't come either... They just bought me a plane ticket and told me to come back with a degree or don't come back at all."
    rori @ say "M-my parents didn't come either... They just bought me a plane ticket and told me not to contact them until I had a PhD."

    #n "You didn't ask but whatever."

    player "Wow, that's uh... tough."

    show rori worried noblush

    rori @ say "They just want to see me succeed. I'd probably live in their basement playing games for the rest of my life if they didn't force me out."
    
    show rori soyface
    
    rori @ say "But I am actually really excited to have some freedom for once now that I'm no longer under their supervision!"
    
    show rori neutral

    player "That's a good attitude to have."

    show rori laugh

    rori @ say "I guess so!"

    show rori neutral

    rori @ say "Well, I guess I'll see you around. I have to unpack my desktop and get everything set up."
    
    show rori anxious
    
    rori @ say "I haven't had it online in over 48 hours and I need to run some updates. I hope my package manager doesn't break my Xorg session again..."

    if calledRoriNerd == False:
        menu:
            rori "{cps=0}I haven't had it online in over 48 hours and I need to run some updates. I hope my package manager doesn't break my Xorg session again...{/cps}"
            "Cool, you use Loonix?":
                $ roriPoints += 1
                
                show rori neutral
            
                player "You use Loonix? That's so cool."
                
                show rori happy
                
                rori @ say "Of course! Using an operating system that respects your freedom is just so comfy!"
                rori @ say "And I can customize it however I want!"
                
                show rori flattered blushing
                
                n "Rori lowers his voice and asks shyly."
                
                rori @ say "Um, would you like to see my riced out tiling window manager setup?"
                rori @ say "I just rewrote my conf files from scratch a couple weeks ago."
                
                show rori smug -blushing
                
                rori @ say "We can play some games and stuff too."
                
                player "Sure. Lead the way."
                
                show rori laugh
                
                rori @ say "*happy bleat*"
                
                n "Rori seems excited to have someone to nerd out with as he takes you to his dorm."
                
                call roriDormIntro from _call_roriDormIntro
                
                player "Do you have a roommate? I get the feeling those aren't yours."
                
                n "You point to a dumbells in the corner."
                
                player "Plus the whole bunk bed setup."
                
                rori @ say "Hm? Oh yeah, those belong to my jock roommate. He's a sophomore so he didn't have to do the orientation today."
                
                show rori sleepy
                
                rori @ say "He's probably out at some party right now, I dunno."
                
                player "Probably crushing pussy while we hook up a gaming computer."
                
                show rori neutral
                
                rori @ say "Yup. But I'd rather be doing this."
                rori @ say "Pass me that displayport cable please."
                rori @ say "Now let's see if this works. I'm a bit worried about my SSD's firmware acting janky after the last update."
                        
                n "Rori reaches behind the desk and hooks up a few wires to the desktop tower. When he presses the power button, a rainbow of LEDS shine through the glass panel of the case."
                n "A moment later, the monitor wakes up and a stream of debug messages scrolls across the monitor."
                n "It stops and prompts him to enter a password. You avert your eyes out of respect for his privacy."
                n "Yet you can't help but notice the rapid fire clattering of his mechanical keyboard goes on for half a minute before he presses the enter key."
                
                player "Damn, your password must be longer than the Pentagon's. What you hiding on that hard drive?"
                
                show rori smirk lookingaway
                
                n "Rori pushes up his glasses and smirks."
                
                rori @ say "16 terabytes of anime bluray rips, 4.5 terabytes of games, 750 gigabytes of jpop, and a couple gigs of leaked government documents and source code."
                
                player "All legally acquired?"
                
                show rori happy
    
                rori @ say "Legal in my VPN's host country!"
                
                player "Nice."
                
                show rori anxious
                
                rori @ say "Oh what the hell is this?"
                rori @ say "Error: Cryptsetup couldn't resolve device. /dev/nvme0n1p3 is not a valid LUKS device."
                rori @ say "Argh, it was working fine a couple days ago!"
                
                player "RIP."
                
                show rori sleepy
                
                rori @ say "This stupid cheap SSD has been flipping bits since I bought it."
                rori @ say "I'm gonna have to load up a live CD and chroot into this and dig around to find the problem."
                rori @ say "I might as well reinstall the OS at this point."
                
                player "Typical loonix boot process."
                
                show rori worried
                
                rori @ say "Haha yeah... Sorry about this but I doubt I'll be able to get this running tonight."
                
                player "Does this mean no games?"
                
                show rori sleepy blushing
                
                n "Rori looks down sadly."
                
                rori @ say "No games."

                n "You point to a console shoved under the desk."

                player "What about that?"
                
                show rori neutral -blushing
                
                rori @ say "My PS3? I use it as a blueyray player. Or more often a doorstop."
                
                player "Doesn't it play games too?"
                
                rori @ say "It's technically capable of it but..."
                rori @ say "What games?"
                
                player "Oh yeah lol"
                
                rori @ say "I'll have this computer fixed and ready to go next time, I swear. I think something might have gotten corrupted during transport."
                
                player "It's alright. It's pretty late and it's been a long day anyway. I'm just gonna go to my dorm and sleep."
                player "See you around, dude."
                
                rori @ say "Laters!"
                
                stop music fadeout 2.0
                
                jump playerDormOrientationDay
                
            "Have fun with that.":
                show rori neutral
                
                n "Sounds like his problem to deal with. That's the price you pay when you let your computer run your life."
            
                player "Have fun with that. I gotta finish unpacking my own things. See you later."
                
    else:
        show rori neutral
        
        n "Sounds like his problem to deal with. That's the price you pay when you let your computer run your life."
            
        player "Have fun with that. I gotta finish unpacking my own things. See you later."
    
    rori @ say "Laters!"

label afterRoriOrientationDay:
    hide rori with dissolve

    n "He waves goodbye as he walks off to Edgar Hall. You head in the opposite direction to your own dorm."

    #show bg static1

    #pause .02

    #show bg campus

    #n "You feel like you could fall asleep any minute now."
    #n "Better hurry to your dorm before you faceplant into the ground. Thankfully it's not too far away."

label playerDormOrientationDay:
    stop music fadeout 1.5

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    #n "You can't entirely recall how you got here but you made it."
    n "Here it is. Home sweet home for the next four years."
    n "You had packed as much from home as you could carry in your suitcases but haven't had a chance to unpack yet."
    n "It'll have to wait until tomorrow. You're way too tired to bother with it right now."
    n "You quickly get ready for bed and flop directly onto the covers, falling asleep instantly."

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show tsaturday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7
    
label exploring_campus:
    #___sunday1
    
    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    play music "audio/ambient/morning birds.ogg" fadein 0.1

    n "It's already around noon by the time you wake up."
    n "Luckily classes don't start until tomorrow, so you can get away with sleeping in. For now."
    n "You'll have to sort out your sleep schedule the painful way soon."
    n "However, your primary concern at the moment is the breakfast situation."
    n "You've subsisted on nothing but granola bars during your journey to Harmonia, and it's high time you got a warm meal."
    n "You roll out of bed and take a quick shower, impatiently doing the bare minimum to make yourself presentable before heading out to find some food."

    stop music fadeout 1.0

    scene bg campus summer day clear with fade

    play music "audio/music/vylet - there.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "It's a bright and sunny day with students bumbling about... {i}socializing{/i}, as if their normie instincts extract vital nourishment from it."
    n "You unfortunately stumble into what must be the hub of social activity on campus today: club registration."
    n "Tables and booths line the street with banners advertising the different clubs and organizations the university has to offer."
    n "There's one for the botany club, debate club, algae bee tea club,  {a=https://4chan.org/trash/hmofa}/hmofa/{/a} club, anime club, vidya club, golf club, and so on."
    n "Going straight across is the quickest way to the restaurants, so you head in with your eyes forward."
    n "You know the moment you look at any of them, some representative will drag you into an involuntary conversation."
    n "Almost there... Almost... Just a few more meters."
        
    $ randumb = renpy.random.randint(0, 1)
    
    #for testing
    #n "random number is [randumb]"
    
    if randumb == 0:
        $ metClaire = True
        $ metAva = True
        
        n "You almost managed to get to the end without being harassed by anybody."
        
        show claire sweater happy at center:
            ypos y_claire
            xoffset 2000
        show ava typical neutral at center:
            ypos y_ava
            xoffset -2000
        
        n "Surprisingly it wasn't a club representative, rather it's the chatty girls you saw the day prior."

        show claire sweater happy wave:
            ypos y_claire
            xoffset 400
            matrixcolor BrightnessMatrix(0.05)
        show ava typical happy:
            ypos y_ava
            xzoom -1
            xoffset -400
            matrixcolor BrightnessMatrix(0.05)
        with move

        claire @ say "Holy Frith, it's you! You were at the thing last night, weren't you?"
        
        show ava neutral
        show claire -wave

        ava @ say "She means the orientation."
        
        show ava typical happy

        player "Nope, you must have me confused for the other human around here."
        
        show ava typical smug

        n "Ava smirks at your joke but Claire seems to take a second to get it."

        claire @ say "Oh..."
        
        show claire sweater surprised earsup
                    
        claire @ say "Oh!"
        
        show claire sweater flustered -earsup
        
        claire @ say "Duh!"
        
        show claire sweater happy wave
        
        claire @ say "What was your name again? [name]?"

        player "Yeah. And you were... Ava and Claire, right?"
        
        show ava excited

        ava @ say "Yup! Nice to meet you [name]!"
        
        show claire sweater happy -wave
        show ava typical happy
        
        claire @ say "So what brings you out here? Looking to join a club?"

        player "More like looking for a place to get breakfa- err, lunch, but I ended up here somehow."

        ava @ say "One booth was giving out free donuts but they ran out pretty quick."

        player "Aww..."

        claire @ say "I guess you could say the early bird gets the donut~"
        
        show ava profile whimsical
        
        ava @ say "Hehe you're not wrong!~"
        
        show ava typical happy

        player "So have you signed up for anything so far?"
        
        show claire sweater derp

        claire @ say "I looked into a bunch but I can't decide which one to join!"
        
        show claire sweater happy
        show ava neutral

        ava @ say "I just went for the obvious one and joined the photography club. Thinking about signing up for the cinematography club too. What about you?"
        
        show ava happy

        player "I'm not really interested in any of them."
        
        show claire giggle
        
        claire @ say "*gasp* We should all join a sorority!"
        
        show ava unamused
        
        ava @ say "What? Why?"
        
        player "I don't think they'd let me in."
        
        show claire happy
        
        claire @ say "Why not? It's current year!"
        claire @ say "We can infiltrate their organization and hit on all the sorority sluts! Ksksksksks!"
        
        ava @ say "Pass."
        
        show claire sad
        
        claire @ say "Aww, you're no fun."
        
        show claire happy
        show ava happy
        
        claire @ say "What about you, [name]?"
        
        menu:
            claire "{cps=0}What about you, [name]?{/cps}"
            "Yah":
                $ clairePoints += 1
                $ signedUpForSorority = True
                
                player "You know what, sure, sign me up."
                player "Should be funny when they realize I'm not a girl and kick me out."
                
                claire @ say "No way, you could totally pass for a girl with a little makeup!"
                
                player "Uh, thanks?"
                
                #claire @ say "That's the spirit!"
                
                player "You handle the forms though, I have to run."
                
                show ava unimpressed
                show claire overjoyed
                
                n "Ava rolls her eyes while Claire squeals in excitement."
                
                claire @ say "Eeeeeee it's gonna be so fun! Ava you're gonna regret not joining!"
                
                show ava happy
                
                ava @ say "If you say so. We'll see you around, [name]!"
                
                show claire happy
                
                player "Yeah, later guys."
                
                show claire happy wave
                
                claire @ say "Byeeeee!!!"
                
            "Nah":
                player "Nah."
                
                show claire sad
                
                claire @ say "Can't a bun have a little fun?"
                
                show ava unimpressed
                
                ava @ say "No one's stopping you from joining on your own, you know."
                
                claire @ say "But I'll be lonely ;^;"
                
                show ava shocked
                
                ava @ say "Isn't the point of joining one so you *won't* be alone?"
                
                claire @ say "I wanna be around my friends though."
                
                ava @ say "You'll make some in the sorority!"
                
                claire @ say "But what if they don't like me?"
                
                show ava unimpressed
                
                ava @ say "Oh trust me, I think you'll fit right in."
                
                claire @ say "Really?"
                
                n "Claire looks to you sympathetically."
                n "Your stomach is roaring, demanding that you escape this mundane conversation and go find sustenance."
                
                player "Yeah you'd make a great sorority girl. Lemme know how it goes, I have to run for now."
                
                show claire happy
                
                n "Claire quits pouting and instantly brightens up."
                
                claire @ say "Sure! See you around, [name]!"
                
                show ava happy
                
                ava @ say "Later!"
                
                #n "You wave goodbye to them and hurry away before someone else distracts you from your mission."
        
        hide ava
        hide claire
        with dissolve
        
    else:
        $ metGunner = True
        n "You almost made it to the end without getting poached by some aggressive salesman."
        
        show gunner neutral at center with dissolve:
            ypos y_gunner
            xoffset 375
            matrixcolor BrightnessMatrix(0.05)

        gunner @ say "Hey there! I saw you checkin' out the frats and thought you should know Alpha Alpha Alpha is the best one!"
        
        player "I actually wasn't and I don't really care about fraternities."
        
        show gunner determined
        
        gunner @ say "That's just the sort of thing an Alpha would say!"
        
        player "I personally identify as a sigma male but okay."
        
        show gunner cutie
        
        gunner @ say "No worries, we like totally respect your pronouns or whatever. Name's Gunner by the way!"
        #gunner @ say "No worries, we like totally respect your pronouns or whatever stupid bullshit you believe in. Name's Gunner by the way!"
        
        player "[name]. Now if you'll excuse me."
        
        show gunner motivated
        
        gunner @ say "The strong stoic type, I see! You'd fit right in!"
        
        n "Gunner steps in front of you and blocks your path, waving a clipboard and pen in your face."
        
        show gunner neutral
        
        gunner @ say "So what do you say? Are you a bad enough dude to join?"
        
        player "Not particularly."
        
        n "You attempt to maneuver around the cat only to bump into someone else."
        
        show rori neutral at center with dissolve:
            xzoom -1
            xpos 385
            ypos y_rori
            matrixcolor BrightnessMatrix(0.05)
        
        rori @ say "Oh, hello again [name]!"
        rori @ say "I see you've met my roommate."

        show gunner disgusted
        
        gunner @ say "Rori! I'm begging you, join the Alphas!"
        
        show gunner displeased
        
        gunner @ say "If I don't get enough new recruits, the boys are gonna duct tape me to the ceiling again!"
        
        show rori sleepy
        
        rori @ say "Hrm... already doesn't sound like it's for me."
        rori @ say "What do you even do in a fraternity?"
        
        show gunner optimistic

        gunner @ say "Cool bro stuff like uhh... hazing new members, drinking shitty beer, hitting on sorority chicks, playing sports..."
        
        show rori soyface smug
        
        rori @ say "Right... I don't think any of that appeals to me."
        
        show rori sleepy
        
        show gunner cutie
        
        gunner @ say "There's also a bunch of hot guys and stuff."
        
        show rori anxious
        
        rori @ say "Wha-? I-I don't see what that has to do with anything!"
        
        show gunner determined
        
        gunner @ say "Come on dude, I saw the kind of anime you watch."
        
        rori @ say "..."
        
        n "Rori tenses up but doesn't say anything. He's like a deer in headlights, except he's a ram and the headlights are an accusation of being gay."
        
        menu:
            "{cps=0}Rori tenses up but doesn't say anything. He's like a deer in headlights, except he's a ram and the headlights are an accusation of being gay.{/cps}"
            "Which anime?":
                player "Which anime was it?"
                
                show gunner neutral
                
                gunner @ say "The one with all the buff dudes with ghosts that punch really fast and are also buff dudes half the time."
                
                player "Jojo's Strange Journey?"
                
                n "Rori nods his head."
                n "Damn, you thought you could defend him but that one is undoubtedly pretty gay."
                
                show gunner cheeky1
                
                gunner @ say "Hahahaha if that's your type there's plenty of jacked Alpha guys. They practically live at the gym."
            "Lay off him, dude":
                $ roriPoints += 1
                
                player "So what? Lay off him, dude."
                
                show gunner itsover
                
                n "Gunner puts his paws up innocently and scoffs."
                
                gunner @ say "Relax, it's just a bit of banter."
                
                show gunner neutral
                
                gunner @ say "Seriously though, some Alphas are jacked. They practically live at the gym."
        
        show rori worried
        show gunner neutral
                
        rori @ say "Thanks for the offer but I'm more into... sensitive guys I guess?"
        
        show gunner frown1
        
        gunner @ say "Like... feelings? Yeah I dunno if they're good at that."
        gunner @ say "Look, can I just put your names down? You don't have to show up but the more people who sign on, the more money we get from the university."
        
        show gunner neutral
        
        gunner @ say "You'll get access to benefits like sports tickets and exclusive parties and stuff. Oh and we have monthly game tournaments!"
        
        show rori concerned
        
        n "That last part caught Rori's attention."
        
        rori @ say "Tournaments? What do you play?"
        
        show gunner optimistic
        
        gunner @ say "Usually the yearly Call of Battlefield: Modern Football but sometimes someone will bring in some weird ass Japanese game none of us have ever heard of hahaha!"
        
        show rori sleepy
        
        n "Rori looks disappointed then shrugs."
        
        rori @ say "Fine, whatever. Sign me up I guess. At least I can probably sell the sports tickets."
        
        show gunner wink catface
        
        gunner @ say "Sweet! I just need your signature here! And if I come across any uhh... emotional guys? I'll send them your way!"
        
        show gunner neutral
        
        rori @ say "Suuuure..."
        
        gunner @ say "What about you? You down?"
        
        menu:
            gunner "{cps=0}What about you? You down?{/cps}"
            "Join":
                $ signedUpForFraternity = True
                $ gunnerPoints += 1
                
                player "Yeah but only for the free stuff."
                
                n "You take the clipboard and lazily scribble your name somewhere on it."
                
                show gunner cheeky1
                
                gunner @ say "Yes! You won't regret it!"
                
                player "I better not."
                
                n "Gunner holds out his fist."
                n "As is customary, you are forced to give him a fist bump."
            "Don't join":
                $ gunnerPoints -= 1
                
                player "Nah, I'd rather not."
                
                show gunner annoyed
                
                n "Gunner's ear flicks in annoyance."
                
                gunner @ say "Suit yourself."
                
        player "Now if you're done wasting my time, I have breakfast to catch."
        
        show gunner neutral
                
        gunner @ say "No problem dude. I'll see you around!"
        
        rori @ say "See you later, [name]!"
        
        hide rori
        hide gunner
        with dissolve
        
    n "You wave goodbye to the duo and hurry away before someone else distracts you from your mission."
    n "A few restaurants catch your eye, but the long lines accompanying them dissuade you from bothering with them."
    n "You weren't about to escape one crowd only to end up in another."
    n "When all hope seemed lost, the scent of coffee and bagels in the air came to your rescue, leading you to a small building hidden behind the library."

    stop music fadeout 1.3

    scene bg cafe with fade

    play music "audio/music/mere - coffeeLoveIntro.exe.ogg" 

    show box with Dissolve(.2):
        ypos 0

    #n "Smooth jazzy music plays from speakers mounted on the walls. Thank raptor Jesus it's not the obnoxious music they blast at  so loud you can't even hear the barista call your name."
    n "The interior is dim and so quiet you can hear your footsteps echo. You'd think it was abandoned if not for the barista watering a plant at the counter."
    n "Written on the chalkboard on the far end of the room is a phrase in cyrillic and underneath is the menu, thankfully in English."
    #n "Calming music plays from the speakers mounted to the walls. This would be a nice place to study."
    n "After giving it a look over, you decide what you want and walk up to place your order."

    show mishka neutral at center with dissolve:
        ypos y_mishka

    mishka @ say "Privyet, welcome to Coffee Zona..."
    
    show mishka shy
    
    mishka @ say "...er, Zone!"
    
    show mishka neutral
    
    mishka @ say "How can I help you?"
    
    menu:
        mishka "{cps=0}How can I help you?{/cps}"
        "Why are the lights off?":
            player "Why are the lights off? Is the shop open?"
            
            show mishka anxious smile
            
            mishka "It's just how I like things. I can turn them on if you like."
            
            menu:
                mishka "{cps=0}It's just how I like things. I can turn them on if you like.{/cps=0}"
                "Please do":
                    $ cafeLightsOn = True
                    
                    player "Please do. I can't see anything in this darkness."
                    
                    mishka @ say "Duzhe dobre."
                    
                    show mishka asleep
                    
                    n "The barista clenches her eyes shut as she puts a claw to the light switch."
                    n "When the lights come on, she winces and slowly opens her eyes."
                    
                    show mishka neutral -anxious
                    
                    mishka @ say "Now what can I get for you?"
                "Leave them off":
                    $ mishkaPoints += 1
                    
                    player "It's fine, you can leave them off. It's comfier this way."
                    
                    show mishka anxious neutral
                    
                    n "She seems pleased with your response."
                    
                    show mishka neutral -anxious
                    
                    mishka @ say "Now what can I get for you?"
        "Place your order":
            player "Yeah can I get uhh...."

    n "You give the barista your order and swipe your card on the machine."

    mishka @ say "And can I get a name for you?"
    
    show mishka nervous
    
    mishka @ say "Not that I really need it since we're the only ones in here."
    mishka @ say "But it would be nice to have irregardless."

    player "      [name].      "
    
    show mishka happy

    mishka @ say "Alright [name], I'll have your order ready for you soon!"
    
    show mishka neutral

    player "Thanks uhh..."

    n "You look down at her name tag."
    n "It's in cyrillic."
    n "{font=ahellya.ttf}Мишка{/font}"
    
    menu:
        "Myewka?":
            player "Thanks ...Myewka? I don't know how to say that."
        
            show mishka depressed
            
            mishka @ say "It's Mishka."
            
            show mishka neutral
            
            n "She begins working on your order while continuing the conversation."
            
            mishka @ say "I don't recall seeing you before. You must be new student."
        "Mnyeka?":
            player "Thanks ...Mnyeka? I don't know how to say that."
        
            show mishka depressed
            
            mishka @ say "It's Mishka."
            
            show mishka neutral
            
            n "She begins working on your order while continuing the conversation."
            
            mishka @ say "I don't recall seeing you before. You must be new student."
        #"{font=ahellya.ttf}Мишка{/font}":
        "Meeshka":
            n "You've pirated enough Russian malware to be able to sound out the letters."
            
            player "Thanks uhh, Meesh...ka! Am I saying that right?"
            
            show mishka happy

            mishka @ say "Yup! Not many Mishkas around here, are there?"
            
            show mishka neutral

            player "Nope, you're the first I've ever met. Then again, I did just move here."

            n "She begins working on your order while continuing the conversation."

            mishka @ say "Oh? Are you new student?"

    player "Yeah. Can't decide what to major in though."

    mishka @ say "It can be tough choice to make. I wouldn't stress about it though, most people find something after semester or two."

    player "I sure hope so. I wasn't really planning on going to college in the first place, but I also wasn't planning on not going, you know?"
    player "But now I'm here and I still don't know what I'm doing."

    show mishka shy sad

    mishka @ say "Many students feel same way. Life can be that way sometimes. You just have to make the best of it while you're here."
    
    show mishka neutral eyesclosed
    
    mishka @ say "For now, enjoy coffee and blini!"

    show mishka neutral -eyesclosed
    
    n "Mishka hands you a steaming hot cup and a box."

    player "Thanks! And I appreciate the advice!"
    
    show mishka mousey wink right

    mishka @ say "Nyema problyema! Come back soon, it gets pretty lonely here!"
    
    show mishka neutral -right

    player "For sure!"

    hide mishka with dissolve

    pause .3

    stop music fadeout 1.0

    scene bg campus summer day clear with dissolve

    play music "audio/ambient/outdoors people talking.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "You walk out the door, feeling somewhat uplifted by the barista's words, and find a place to sit and enjoy your breakfast."
    n "A light breeze passes by as you open your box and stab a fork into your pancakes."
    n "You take a sip of coffee and watch the other students walking around."
    n "It's pretty easy to pick out who's a freshman like you and who's been here for a while."
    n "The new people are still basically high schoolers at this point. Practically still kids, and it shows in the way they carry themselves."
    n "Unsure about the world but excited about all the possibilities."
    n "The upperclassmen on the other hand seem a bit more grizzled, beaten down by the world but tougher for it."
    n "Less optimistic, more realistic."
    n "Man."
    n "To be honest, you're kinda glad you're back in school."
    n "The past few years hadn't been kind to you. You basically had to drop out of high school to take care of your parents in their final moments."
    n "It'll be nice going back to a structured life with classes but with the added liberty of being a \"\"\"real\"\"\" adult."
    n "You finish up your meal, gathering your scraps and throwing them away as you ponder what to do with the rest of your day."
    n "This is your last day of total freedom before you become a full time student."
    n "It's already afternoon and you're already feeling tired."
    n "Is this what it's like to be an adult?"
    n "You feel like you should be cruising down the city streets on your way to some beach party, where you'll chat up a cutie by the bonfire and watch the stars together."
    #n "Living life to its fullest."
    n "Alas, you still need to unpack your belongings and tidy up your dorm. You should also do a bit of grocery shopping on the way back." 
    n "You best go to bed early too, you don't want to be late for class tomorrow."
    n "No sense in wasting any more time. You'll get these errands done now so you can be well rested tomorrow."
    
    stop music fadeout 1.0

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show tsunday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

label firstDayOfClass:
    scene bg codadorm with fade

    play music "audio/ambient/morning birds.ogg" fadein .4

    show box with Dissolve(.2):
        ypos 0

    #n "It turns out going to bed early does nothing to guarantee restfulness"
    n "Welp, today's the day."
    n "Starting a new school year always gives you a mixture of anxiety and excitement."
    n "It's a chance to kind of reset things and try new things, be a new person."
    n "But it's also a huge obligation to keep up with studies."
    n "Still better than being a wageslave you guess."

    stop music fadeout 1.5

    scene bg classroom with fade

    play music "audio/music/mere - schooldaze.ogg" fadein .4

    show box with Dissolve(.2):
        ypos 0

    n "You vastly overestimated your ability to get around campus quickly and arrive ten minutes late to your history class."
    n "All eyes are on you as you bust through the doorway."

    show rothbauer at center with dissolve:
        ypos y_roth

    rothbauer @ say "Ah, nice of you to join us. You must be..."
    
    n "He flips through the papers on his desk."
    
    rothbauer @ say "... Mister [name] Mann, correct? Did I say that right?"
    rothbauer @ say "I'll let your tardiness slide since it's the first day, but please make more of an effort to be on time in the future."
    rothbauer @ say "Go ahead and take a seat."

    n "Fuck yeah, human privilege."
    n "The only available seat is toward the back of the classroom. You walk down the aisle, careful not to trip over everyone's backpacks as you pass by each desk but you do anyway."

    rothbauer @ say "Now where was I? Oh yes, the group project that is due at the end of the semester!"
    rothbauer @ say "You will be responsible for researching an ancient civilization, writing a ten page paper detailing its rise and fall and putting together a presentation."
    rothbauer @ say "You'll find more information about the requirements and grading rubric in the syllabus."
    rothbauer @ say "I'll let you go ahead and form groups of three now. I know most of you don't know each other but this will be a good opportunity to make friends!"

    hide rothbauer with dissolve

    n "Forming groups already? Welp, time to kill yourself."
    n "Oh wait, the girl next to you is pretty cute. Maybe she's into humans."

    player "Hey uh, wanna be partners?"
    
    show rose skirt armscrossed dismissive pendant at center with dissolve:
        xoffset -350
        ypos y_rose
    
    rose @ say "    Psh.    "
    rose @ say "     No.     "

    n "She scooches her desk away from you and faces the other way."

    show rose with move:
        linear .54 xoffset -500
    pause .2
    show rose with move:
        linear .54 xoffset -800
    pause .4
    show rose with move:
        linear .54 xoffset -1450

    n "Damn, maybe you came on too strong."
    n "You try partnering up with some others but it seems everyone's already established their own group."
    #n "You try partnering up with some others but as usual you get ignored."
    n "You take another look at that raccoon girl. She didn't even attempt to talk to any of the other students. She's just staring out the window."
    
    show rothbauer at center with dissolve:
        ypos y_roth

    rothbauer @ say "Hopefully everyone's found a group by now."

    n "Mr. Rothbauer asks who everyone is partnered with and jots it down in a notebook while you silently panic."

    rothbauer @ say "[name], what about you? Who's group are you in?"

    player "Err, I couldn't find one..."

    rothbauer @ say "Oh? Does the class not divide evenly? Hah, this is why I'm a history teacher and not a math one!"
    rothbauer @ say "Does anyone else not have a partner? What about you, Miss Kaczynski, who's group are you in?"
    
    n "Kaczynski huh? Is she related to the dean?"

    show rothbauer with move:
        xoffset 350
        
    show rose skirt handonhip shy pendant at center with dissolve:
        xoffset -450
        ypos y_rose

    rose @ say "...Nobody's."
    rose @ say " And just call me Rose."

    rothbauer @ say "Very well, Rose, you and [name] can be a group of two then!"
    
    show rose skirt armscrossed dismissive pendant

    #rose @ say "Ugh. Do I have to?"
    rose @ say "I can do the assignment on my own."
    
    rothbauer @ say "I'm sure you could, but that's not the point of this exercise. It's important for students to learn how to work with others, like in a real work environment!"
    rothbauer @ say "I'll be checking in from time to time with each student to monitor each individual's progress and contributions to the project, so please make sure everyone in your group is pulling their weight."
    #rothbauer @ say "It's a great exercise in leadership and compromise that will serve you more in the long run than any history knowledge."

    rose @ say "Fine, whatever."
    
    rothbauer @ say "Good! I'll put you and [name] into your own group then."

    n "While Rothbauer writes your names in his notebook you hear crumpling paper beside you."
    
    n "You glance towards Rose and see her clenching her fist, balling up a sheet of paper."
    n "She turns to you and mutters something."
    
    show rose skirt furiouspose pendant

    rose @ say "To hell with that. I'll do it all on my own."

    hide rose with dissolve
    
    show rothbauer with move:
        ypos y_roth
        xoffset 0

    rothbauer @ say "Ahem well... now that that's settled, let's begin our first lesson!"
    rothbauer @ say "This course and the follow up World History II are designed to give you an understanding of how civilization has progressed alllll the way back from when the dinosaurs roamed the earth..."

    n "Mr. Rothbauer circles a crude drawing of a pterodactyl on the chalk board and starts drawing an arrow pointing to some stick figures."

    rothbauer @ say "...to the rise and fall of humanity, leading into the current era, Societas Animalium, that is 'Society of Animals' as they say."
    rothbauer @ say "Of course, not much is known about how the dinosaurs lived since a meteor striking the planet destroyed nearly every bit of evidence they were here at all!"
    rothbauer @ say "After the world was buried under a blanket of smoke and ash, smothering their existence. It took millions of years before a civilization was able to form again."
    #rothbauer @ say "But what if I told you that we are not so different from the dinosaurs?"
    #rothbauer @ say "This... goes a bit against the curriculum but the evidence is there to suggest that our prehistoric ancestors were quite advanced!"
    #rothbauer @ say "The government doesn't want you to know that ancient integrated circuits have been discovered deep underground alongside the fossilized remains of Mesozoic era creatures."
    #rothbauer @ say "To develop such advanced technology implies the existence of organized civilization!"
    #rothbauer @ say "Ahem, excuse me, I'm just very passionate about that particular time period."
    rothbauer @ say "In any case, anything before the agricultural revolution humans kickstarted circa 10,000BCE won't be on the test."
    rothbauer @ say "A big thank you to [name]'s ancestors for that!"

    n "A few students turn around in their seat and look back at you."
    n "This is so uncomfortable."
    n "Are you supposed to say anything?"
    n "Why did Mr. Rothbauer have to call you out like that?"
    n "It's not your fault your ancestors forced everyone to live in a society."

    rothbauer @ say "Anyway, where was I? Oh yes, the human population was increasing exponentially during this time and they quickly established themselves as the dominant species..."

    n "You take out a notebook and start taking notes as Mr. Rothbauer lectures for the next hour."

    stop music fadeout 1.0

    scene bg campus summer day clear with fade

    play music "audio/ambient/outdoors people talking.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "Next up you've got Introduction to Probability and Statistics. You signed up for it so you could learn how to properly balance your crit chance with other stats in role playing games."

    if metGunner == True:
        n "Along the way you bump into a familiar feline."

        show gunner neutral at center with dissolve:
            ypos y_gunner

        gunner @ say "Sup, [name]! Where ya goin'?"

        player "Oh hey, you again. I'm on my way to statistics."

        gunner @ say "With Mrs. Herschel?"

        player "Yeah I think so."

        gunner @ say "Ayy, that makes us classmates!"
        gunner @ say "Fair warning though, this class is hella hard."
        
        player "Fantastic."
        
        gunner @ say "We better hurry there, Mrs. Herschel hates it when students are late."
            
        scene bg lecturehall with fade

        play music "audio/music/mere - schooldaze faster.ogg" fadein .4

        show box with Dissolve(.2):
            ypos 0
        
        show herschel:
            xpos 2000
            yalign 0

        n "Looks like you made it before the teacher arrived."
        n "Nobody else is brave enough to sit in the front row, leaving you no choice but to take a seat there. Gunner sits right next to you."
        n "Once you've settled in and got your pencil and notebook out, Mrs. Herschel walks in."

    else:
        scene bg lecturehall with fade

        play music "audio/music/mere - schooldaze faster.ogg" fadein .4

        show box with Dissolve(.2):
            ypos 0
        
        show herschel:
            xpos 2000
            yalign 0

        n "Looks like you made it before the teacher arrived."
        n "Nobody else is brave enough to sit in the front row, leaving you no choice but to take a seat there."
        n "Somone sits right next to you and starts chatting you up like you're best friends."
        
        show gunner cheeky1 at center with dissolve:
            ypos y_gunner
        
        gunner @ say "Yeah so summer vacation was pretty lit. Went on this week long fishing trip on my dad's yacht with the bros and my portfolio is up 20\% from the start of the quarter."

        menu:
            gunner "{cps=0}Yeah so summer vacation was pretty lit. Went on this week long fishing trip on my dad's yacht with the bros and my portfolio is up 20\% from the start of the quarter.{/cps}"
            "Are you talking to me?":
                player "Huh? Are you talking to me?"
                
                show gunner determined
                
                gunner @ say "Uh yeah? That's not a problem is it?"
                
                player "No, it's just weird you would think I give a shit about your yacht."
                
                show gunner eyesclosed catface
                
                gunner @ say "Ohh sorry, sorry! You're more of a helicopter guy I see, my mistake."
                
                show gunner wink catface
                
                gunner @ say "Man, I need to get one of those for myself. Maybe I'll ask for one for my birthday."
            "Wow money is so cool.":
                player "Wow money is just so cool, isn't it?"
                
                n "He evidently doesn't pick up on your sarcasm, because there isn't a hint of irony in his response."
                
                show gunner wink catface
                
                gunner @ say "I know right? I don't get why people choose to be poor. It's weird."

        show gunner neutral
        
        gunner @ say "I'm Gunner by the way! What's your name?"
        
        player "[name]."
        
        n "At least he's not pestering you with questions about what it's like being the last human. In fact, you don't know if he is even aware of that fact."
        n "It seems he's more concerned with his own status and appearance."
        
        show gunner cheeky1
        
        gunner @ say "[name], huh? Lemme tell you a funny story."
        gunner @ say "This building was used for the feminist studies college last semester. They switched it over to math over the summer."
        
        show gunner mischief
        
        gunner @ say "So when I saw I had stats here my first thought was \"The hell? Are we gonna learn how to find the hypotenuse while folding laundry or something?\""
        
        menu:
            gunner "{cps=0}So when I saw I had stats here my first thought was \"The hell? Are we gonna learn how to find the hypotenuse while folding laundry or something?\"{/cps}"
            "Laugh":
                n "You have to admit, that got a chuckle out of you. You try to hide it, but your true colors make themselves known."
                
                show gunner motivated
                
                gunner @ say "Hah, don't be afraid to laugh, I know I'm funny!"
            "Don't say anything":
                $ gunnerPoints -= 1
                
                n "You pretend you're still waiting for the punchline and remain silent."
                
                show gunner frown1
                
                gunner @ say "Like folding a towel or something into a triangle and-"
                
        n "Gunner goes quiet as an old lady walks into the room. That must be the professor."
        
    hide gunner with dissolve

    show herschel at center with dissolve:
        ypos y_herschel

    herschel @ say "Good afternoon everyone! My name is Mrs. Herschel and I'm very excited to teach probability and statistics again this year!"
    pause .1
    herschel "{nw}"
    
    show herschel with move:
        xoffset 270

    show gunner wink catface at center with dissolve:
        xzoom -1
        ypos y_gunner
        xoffset -470

    gunner @ say "Looking good, Mrs. Herschel! I'm very excited to learn probability and statistics again this year!"

    herschel @ say "Flattery will get you nowhere Gunner. I'm afraid you'll be learning this subject for the first time this year judging by your grades last year."
    
    show gunner displeased

    gunner @ say "Hey I still remember y = mx + b!"

    herschel @ say "That's geometry, dear."
    
    show gunner frown1

    gunner @ say "..."
    gunner @ say "Oh yeah."

    hide gunner with dissolve
    
    show herschel with move:
        xoffset 0

    herschel @ say "That reminds me, I wanted to point out this can be a very challenging class."
    herschel @ say "I recommend spending half an hour every night studying the textbook and working through the example problems."
    #herschel @ say "That being said, feel free to ask as many questions as you'd like! If a student fails, then I've failed as a teacher after all."
    herschel @ say "Now then, we have much to get through and not a lot of time, so let's begin with some basics! A set is defined as a collection of elements..."

    hide herschel with dissolve

    n "You notice Gunner aggressively taking notes throughout the whole class."
    n "He even stays behind to ask Mrs. Herschel questions after she dismisses the class."
    n "Is this stuff really that difficult? You understood it just fine but maybe it gets harder later."
    n "Since you're done with classes for the day, you think you'll get a bite to eat then study a bit and call it a day."

    stop music fadeout 1.0

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show tmonday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

label secondDayOfClass:
    #___tuesday1
    scene bg codadorm with fade

    play music "audio/ambient/morning birds.ogg" fadein .4

    show box with Dissolve(.2):
        ypos 0

    n "You roll out of bed and start your morning ritual in preparation for class."
    n "Today you have Literature 101 and then Intro to French Language."
    n "A couple weeks ago you received an email with the books you'll need. The first one you'll be going over in literature is the novella \"The Death of Ivan Ilyich.\""
    n "You pack your ebook reader that's loaded with all the books you could find on the pirate bay into your bag along with the French textbook and venture out."

    stop music fadeout 1.0

    scene bg lecturehall with fade

    play music "audio/music/mere - retrograde slowed.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "You step into a large lecture hall with a projector already beaming a desktop onto a screen at the front. Students trickle in until the room is full."
    n "A couple minutes before class is scheduled to begin, a woman comes in through a door near the podium."
    n "To your dismay, the teacher of this class is the same lady who gave the orientation speech the other day."
    n "You don't think you made the best first impression the other day. Hopefully she doesn't hold a grudge."
    n "She double clicks a file and brings up a slideshow."

    show margaret happy at center with dissolve:
        ypos y_margaret

    margaret @ say "Good morning and welcome to Literature 101!"
    margaret @ say "Today we'll go over the syllabus and what you can expect from this class. Then we'll finish up with some discussion on the assigned reading!"

    show margaret neutral

    n "She clicks a button and the slideshow advances to the next slide, going over some information about herself."

    margaret @ say "My name is Miss Ellen and I've been teaching at Harmonia for about a decade so I like to think I've gotten quite good at it!"

    show margaret sad at shudder

    margaret @ say "Oop, ignore the Mrs. in front of my name on the slide... I guess I forgot to update that..."
    
    show margaret melancholy
    
    margaret @ say "Haha recently divorced... you know how it goes..."

    n "She quickly advances forward a few more slides."

    show margaret neutral

    margaret @ say "Ahem where was I? Oh yes, this course will introduce you to literature across a variety of different cultures throughout different time periods."
    margaret @ say "In the interest of time, most of the reading will be on the short side, or at least limited to excerpts from longer works."
    margaret @ say "In case you didn't get my email, you'll be responsible for procuring your own books, starting with a favorite of mine, Tolstoy's \"The Death of Ivan Ilyich!\""
    margaret @ say "You won't have a test on it until the end of next week but I'll expect you all to read the assigned chapters every night and keep up with the discussions in class."

    n "Miss Ellen gives an overview of the rest of the books you'll be reading and how she'll be grading responses to open ended questions."
    n "Somehow she manages to stretch it to half the duration of the class time before starting with the lesson."
    n "She explains the historical context and some biographical information regarding the first assigned story."

    margaret @ say "Leo Tolstoy is considered one of the greatest authors of all time, his works often taking on philosophical questions like 'What is the meaning of death?'"
    margaret @ say "That, in fact, is the main topic of his novella \"The Death of Ivan Ilyich!\""
    margaret @ say "We'll dive into the life of a man as his life crumbles apart and he learns to deal with his inevitable death."
    margaret @ say "Indeed, this wasn't the first time Tolstoy wrote on the subject of death, as he had earlier written \"A Confession,\" considering the possible interpretations and attitudes toward death."
    margaret @ say "Although he struggled with his own mortality, Tolstoy seems to have come to a conclusion on what a good death means."
    margaret @ say "Please open your books and we'll hop right in!"

    hide margaret with dissolve

    n "You pull the book out of your bag and open your notebook to a fresh page."
    n "Miss Ellen goes over the first chapter of the novella, explaining some things and asking the class for their thoughts along the way."
    n "Time flies by quickly and the end of the hour is upon you before you realize it."

    show margaret neutral at center with dissolve:
        ypos y_margaret

    margaret @ say "That's all for today! We'll continue this discussion next time! Have a nice day!"

    hide margaret with dissolve

    n "You pack your things and stand up."
    n "Next up is French class. You always wanted to learn another language. Unfortunately the classes for all the good languages were already filled."
    
    stop music fadeout 1.0

    scene bg classroom with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    show celestine neutral at center with dissolve:
        ypos y_celestine

    celestine @ say "Bon après-midi! I am Mrs. Celestine and I'll be your French teacher for this semester, and hopefully the next one as well if you decide to stick with it!"

    n "You become distracted from her introduction by the strange ripples that seem to appear out of nowhere in the translucent bottle of water on the professor's desk."
    n "As the water starts to bounce more violently in the glass, you hear a rhythmic low pitched thud gradually getting louder."
    n "A moment later, the door crashes open and a wall of fluff squeezes through the doorframe."

    if metClaire == True:
        n "Isn't that Claire?"
        n "What a coincidence you have a class with her."
    else:
        n "You've seen that fat rabbit before. She's the ditzy girl from orientation night."
        
    show celestine with move:
        xoffset 400
        
    show claire sweater flustered at center with moveinleft:
        xzoom -1
        xoffset -480
        ypos y_claire
        
    claire @ say "*Huff huff* Sorry I'm late!"
    
    celestine @ say "Pas de soucis! You must be Madame Whitney!"
    ###ah please join us sil vous plais, madame,whitney
    
    show claire sweater derp
    
    claire @ say "Ksksksks just Claire is fine!"
    
    show celestine excited
    
    celestine @ say "Very well! Please take a seat and we'll begin introductions!"
    
    hide celestine with dissolve
    
    show claire sweater happy with move:
        xoffset 500
        
    pause .05

    show claire at flipleft

    n "Claire makes her way over to the desks and looks you dead in the eye."

    if metClaire == False:
        show claire sweater leaning suggestive
        
        claire @ say "Heyyy cutie~"
        claire @ say "Mind if I sit next to you?"
        
        menu:
            claire "{cps=0}Mind if I sit next to you?{/cps}"
            "Sure?":
                player "I guess not?"
                
                show claire sweater pose laughing
                
                claire @ say "Good, cause I was gonna sit here anyway."
            "Go right ahead!":
                $ clairePoints += 1
                
                player "Go ahead! Here lemme get that for you."
                
                n "You pull the chair out for her, just to be nice."
                
                show claire sweater pose laughing
                
                claire @ say "Such a gentleman! Ksksksks!"
        
        show claire sweater suggestive
        
        claire @ say "I'm Claire bee tee double-U~"
         
        n "The plastic of the chair squeals and groans under the weight of the oversized rabbit with the bun's buns barely even able fit on the seat."
        n "Not that you were staring, it's just hard to ignore an object so immense it bends space and time and curves the path of the photons straight into your pupils."
    else:
        show claire sweater overjoyed
    
        claire @ say "OMG [name]! You're in this class too??? How unexpected!"
        
        show claire sweater suggestive

        claire @ say "Imma sit next to you, k?~"
        
        #player "I guess I can't stop you."
        
        show claire sweater happy

        n "Claire takes the seat next to yours and starts rummaging around in her bag."

    hide claire with dissolve
    
    show celestine excited at center with dissolve:
        ypos y_celestine

    celestine @ say "Génial! Looks like everyone is present and accounted for!"
    
    show celestine neutral
    
    celestine @ say "I'll say a few things about myself, then you can all tell me about yourselves and why you decided to learn French!"
    celestine @ say "I was born in France and learned both French and English before moving to America at a young age."
    celestine @ say "In high school I studied Arcoonian, then in college I learned a bit of Pandarianese."
    celestine @ say "Learning languages opens up so many opportunities you'd otherwise never have!"
    celestine @ say "I love to travel and I always learn a bit of the native language and dialect before going so I can converse with the locals."
    celestine @ say "It's especially helpful for finding the best restaurants in a particular area hehe!"
    celestine @ say "I'll be sure to share some stories from my travels throughout the semester but for now, I'd like to hear some things about you guys!"
    celestine @ say "What brings you all to French 101?"

    pause .2

    show celestine at flipright

    pause .3

    celestine @ say "Starting with you, since you were late!"
    
    pause .3
    
    show celestine with move:
        xoffset -400
        
    pause .3

    show claire sweater derp at center with dissolve:
        ypos y_claire
        xoffset 300

    claire @ say "Umm like, I dunno, I kinda just picked it on a whim! I guess I like to try new things and leave things to chance!"

    hide claire with dissolve

    celestine @ say "Good! That mindset has lead me to some very... intéressante places in the world."
    
    pause .1
    
    show celestine with move:
        xoffset 0
        
    celestine @ say "Next up, you there!"

    menu:
        celestine "{cps=0}Next up, you there!{/cps}"
        "Same as Claire, it was random.":
            $ clairePoints += 1
            
            n "You shrug."

            player "Same as Claire, it was just kind of random and all the other language classes were taken."

            show celestine excited

            celestine @ say "Ah, perhaps it was fate then!"
            
            celestine @ say "Do you believe in fate?"
            
            menu:
                celestine "{cps=0}Do you believe in fate?{/cps}"
                "Not really":
                    player "Like I was somehow meant to be here? Not really."
                    
                    show celestine neutral
                    
                    celestine @ say "Ah, but all the factors lined up to guide you here, did they not?"
                "Kinda":
                    player "Maybe kinda, I'm not sure."
                    
                    show celestine neutral
                    
                    celestine @ say "We often find ourselves in situations due to factors outside of our control, don't we?"
                    
            celestine @ say "Outside forces guide us to certain places at particular moments in time, which in turn funnels us into the next fated event."
            celestine @ say "But that's not to say we are completely bound to a predetermined route!"        
            celestine @ say "Rather, I believe there are set milestones in your life that you will reach, but you have some freedom in how you react to them *and* how you arrive at next one."
            celestine @ say "Perhaps you let fate roll the die and choose this class for you, but what you get out of it is still up to you!"
            celestine @ say "In other words, the amount of choices you can make are limited by others, but the decisions you make are yours alone!"
            celestine @ say "Life is a story with branching paths you may not have written yourself, but you at least choose which ones you take."
            #celestine @ say "It may even be possible to take unintended paths if you're clever enough!"
            
            player "I thought this was a French class, not a philosophy one."

            celestine @ say "Some of the most renowned philosophers come from France you know~"
            celestine @ say "Voltaire wrote a story called \"Zadig,\" which is the French word for Destiny and--"
            celestine @ say "Oh sorry, I went on a bit of a tangent there! I do that from time to time. We best move on before class ends."

            #n "Everything has a meaning? Could that really be true? Or are some things really just arbitrary?"

        "Wanted to travel.":
            $ wantToTravel = True
            
            n "You shrug."

            player "I guess I just wanted to visit France someday."

            celestine @ say "Oh là là! France is such a beautiful and worthwhile place to visit! I could go on for hours, telling you the best spots to go!"
            celestine @ say "France is pretty tourist friendly, but of course it helps a lot to know the language before going!"
            celestine @ say "Just like I was saying earlier, you can always find interesting conversation in new places, provided you know what they're saying!"
            ###maybe add something here
            

    n "The rest of the students give their reasons for being here, which ends up taking most of the class time."
    n "Mrs. Celestine only has a few minutes to go over the very basics of French like pronunciations and greetings."

    celestine @ say "Looks like we're out of time for today. Be sure to study and practice not only reading, but speaking in French as well!"
    celestine @ say "You might find it helpful to get a study partner to practice conversing in French!"

    hide celestine with dissolve

    n "Claire turns to you with a devious grin."

    show claire sweater wave happy at center with dissolve:
        ypos y_claire

    claire @ say "Heyyyyy, wanna be study partners?"

    menu:
        claire "{cps=0}Heyyyyy, wanna be study partners?{/cps}"
        "Sure, why not?":
            $ clairePoints += 1
            
            player "Sure, why not?"
            
            show claire sweater overjoyed

            claire @ say "Yay! I can't wait!"
            
            show claire sweater flustered
            
            claire @ say "I have to go to chemistry right now, but we can study later!"

            player "I had literature earlier so I'm done for the day."
            
            show claire sweater derp

            claire @ say "Great! That means you can walk me to my next class!"
            
        "I don't need a study partner.":
            player "I don't need a study partner."
            
            show claire sweater giggle

            #claire @ say "But I do!"
            claire @ say "Wow you must be really smart!"
            
            show claire sweater laughing
            
            claire @ say "In that case you can be my tutor!"

            player "That's not what I meant..."            
        
    stop music fadeout 1.0

    scene bg campus summer day clear with fade

    show box with Dissolve(.2):
        ypos 0

    show claire sweater happy at center with dissolve:
        xzoom -1
        ypos y_claire
        matrixcolor BrightnessMatrix(0.05)
        
    play music "audio/music/Evan Schaeffer - Aqueduct.ogg" fadein .5

    claire @ say "...and that was around the time I picked up sousaphone for my school's marching band and --"
    
    show claire sweater surprised earsup
    
    claire @ say "Ohmygosh it's Ava! She's like my best friend foreverrr!!!"
    
    show claire sweater wave happy
    
    claire @ say "Avaaaa! Over here!!!"

    n "Claire waves to the bird in the distance holding a camera pointed in your general direction."
    n "She seems annoyed as she looks over the viewfinder and flutters over."
    
    #gunner "{nw}"
    pause .3
    
    show claire sweater happy -wave with move:
        xoffset -450
    show ava pose annoyed at center with moveinright:
        ypos y_ava
        xoffset 450
        matrixcolor BrightnessMatrix(0.05)
        
    claire @ say "What's up?"

    ava @ say "You know, street photography is sorta like wildlife photography."
    
    show claire sweater surprised earsup

    claire @ say "What do you mean?"

    ava @ say "It's about capturing the moment in as natural a state as possible. Me and my camera are supposed to be invisible."
    
    show claire sweater sad

    claire @ say "Oh did I ruin your shot? Sorry..."
    
    show ava typical neutral

    ava @ say "It's no big deal, I was just warming up anyway."
    
    show ava typical happy
    
    if metAva == False:
        show claire sweater happy -earsup
        
        ava @ say "I see you brought a friend."
        ava @ say "I'm Ava. Claire and I are roommates."
        
        player "[name]. Nice to meet you."
        
        claire @ say "Ava is such a good photographer! She's like one of those surveillance birds, she really has an eye for that sort of thing!"
        
        show ava typical shocked
        
        ava @ say "Surveillance bird?! You mean a secretary bird??"
        
        claire @ say "No I mean like one of those birds the government uses to take secret spy photos!"
        
        show ava typical unimpressed
        
        ava @ say "Oh. Those."
        
        show ava typical unamused
        
        ava @ say "I'm more in it for the artistic qualities but I suppose street photography and reconnaissance have their similarities."
    else:
        ava @ say "I see you've found that boy you totally don't have a crush on."
        
        show claire sweater flustered
        
        claire @ say "Wh-who, [name]?? We just happened to have French together just now! I wasn't, like, stalking him or anything!"
        
        show ava typical suggestive
        
        ava @ say "Sure~"
        
        show ava smug
        
        n "You get the feeling that some part of this conversation has flown over your head, but are struggling to decipher what these ladies could possibly be talking about."
        n "You had your suspicions that Claire might be into you, but Ava's exceptionally straightforward words have put that idea to rest."
        
    show claire sweater happy
    show ava happy
    
    claire @ say "Oop, I have to be in class in a minute! But we should all get lunch later!"
    
    n "Ava shrugs."
    
    ava @ say "Today's no good for me. I have to do some club stuff."
    
    claire @ say "Tomorrow then?"
    
    show ava pose happy
    
    ava @ say "Works for me!"
    
    claire @ say "What about you, [name]?"

    menu:
        claire "{cps=0}How does lunch tomorrow sound?{/cps}"
        "Heck yeah!":
            $ avaPoints += 1
            $ clairePoints += 1
            $ avaClaireLunch = True
            
            player "Heck yeah, that sounds nice."

            show claire sweater overjoyed
            
            claire @ say "Yes!"
            
            n "Claire pulls you into a suffocating hug. Ava has to pry her off of you."
            
            show ava pose whimsical
            
            ava @ say "Come on Claire, we've got class to get to."
            
            show ava pose happy
            show claire happy wave
            
            claire @ say "Bye [name]!"
            
            show claire sweater leaning suggestive
            
            claire @ say "Wait!! Lemme get your number!!!"
            
            show ava typical excited
            
            ava @ say "Oh me too!"
            ###(later) claire "I forgot we don't have class together on wednesdays and wouldn't see each other!"

        "I already have plans":
            $ avaClaireLunch = False
            
            player "Sorry, I already have plans. Maybe another time?"
            
            show claire sweater surprised earsup
            show ava typical shocked
            
            claire @ say "Oh uh... sure! When are you free?"
            
            player "Dunno."
            
            show claire sweater sad
            show ava typical unimpressed
            
            claire @ say "Oh..."
            
            show claire sweater derp
            
            claire @ say "Th-that's alright! Just gimme your number and we'll work something out later."
            
            #n "This bunny is desperate to get your phone number. Maybe she *does* have a crush on you."
            n "What's the worst that could happen?"
            
    show ava typical happy
    show claire sweater happy
    
    player "Sure, it's..."
    
    n "Claire and Ava type your digits into their phones."

    ava @ say "We have to get to class now! We'll text you later!"
    
    player "See ya!"
    
    show claire wave
    
    claire @ say "Byeee~"
    
    show ava profile smug
    
    ava @ say "Later!"
    
    hide claire
    hide ava
    with dissolve

    stop music fadeout 1.0

    scene bg black with fade

    hide box

    show bg calendar
    show ttuesday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

label thirdDayOfClass:
    #___wednesday1
   
    play music "audio/ambient/morning birds.ogg" fadein .5

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    n "Dragging your ass out of bed at the unfathomably early hour of..."
    n "You check the time on your phone."
    n "...9:00AM?!"
    n "My god, the sun probably isn't even up yet. You could stand to lie back down for a few more minutes. Catch a few more Z's so you can start making A's."
    
    default bedpilled = False
    
    menu:
        "Go back to bed":
            $ bedpilled = True
            
            call sleepingIn from _call_sleepingIn
            #this class skip is lenient and results in only missing the first one of the day
            
            jump thirdDayOfClassStats
        "Be a productive member of society":
            n "You'll have time to rest when you're dead. Or tonight, whichever comes first."
            n "Either way, these classes aren't going to attend themselves."
    
    stop music fadeout .5

    scene bg classroom with fade
    
    play music "audio/music/mere - schooldaze.ogg" fadein .4

    show box with Dissolve(.2):
        ypos 0

    n "Time to learn about the lore of the world."
    
    show rothbauer at center with dissolve:
        ypos y_roth
    
    rothbauer @ say "Good day, class! Today we will be looking at some of the other civilizations that had cropped up around the dawn of humanized history."
    rothbauer @ say "Let's start with one of their closest genetic relatives, the chimpanzees!"
    rothbauer @ say "The civilized apes at this time were living quite similarly to their feral counterparts, who already live in impressively social tribes."
    rothbauer @ say "It's thought that the key difference was the ability to develop sophisticated language that allowed them to become more organized."
    rothbauer @ say "Structure brought order, something common to all functional civilizations."

    n "The lecture continues, describing a few early primate based societies."
    
    rothbauer @ say "That's all for today! Be sure to read up on the bonobos in your textbook! If you want to pass the quiz that is, hint hint."
    
    hide rothbauer with dissolve
    
    n "You pack your things and get ready for your next class. On your way out, you decide to ask Rose about what you should do for the group project."
    
    show rose skirt handonhip shy pendant at center with dissolve:
        ypos y_rose
        xoffset -350
    
    player "Hey, what civilization are we doing for the-"
    
    rose @ say "Don't talk to me."
    
    pause .1
    
    show rose at offscreenright with move:
        ypos y_rose
        xoffset 400
    
    n "She walks off without even giving you a glance."
    n "Already off to a better start than every other group project you've been a part of."
    
label thirdDayOfClassStats:
    scene bg lecturehall with fade

    play music "audio/music/mere - schooldaze faster.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0
        
    show gunner neutral at center with dissolve:
        ypos y_gunner
    
    gunner @ say "Sup [name]!"
    
    show gunner motivated
    
    gunner @ say "You ready to fuck up some mathematics?"
    
    player "I have no idea what that's supposed to mean."
    
    show gunner neutral
    
    gunner @ say "It's just an expression."
    gunner @ say "Hey before I forget, lemme get your number."
    
    player "What? Why?"
    
    gunner @ say "So we can help each other with homework problems."
    
    show gunner wink catface
    
    gunner @ say "And y'know chat and stuff."
    
    n "You're not sure if Gunner will make for a good study partner but you can't think of a polite way to say no."
    
    show gunner neutral
    
    player "Fine. Here."
    
    n "He types your number into his phone."
    
    show gunner displeased
    
    gunner @ say "Shit, here comes Mrs. Herschel. She'll fail you if she sees you on your phone. I'll send you a text later."
    
    hide gunner with dissolve
    
    show herschel at center with dissolve:
        ypos y_herschel

    herschel @ say "Good afternoon class!"
    herschel @ say "We have a lot to go over and precious little time, so let's jump straight into it!"
    #herschel @ say "I hope you're mentally alert because this is where the material starts to get a little hard..."
    #herschel @ say "...and without a solid foundation of the principles of probability, you're going to be struggling for the rest of the semester."
    herschel @ say "Recall from yesterday, the intersection of two events is equal to the product of the probability of event A and event B."

    n "She writes the formula on the board."

    herschel @ say "Conditional probability is just the chance that something will happen when given that a certain condition is true."
    herschel @ say "So given B is true, the formula for finding the probability of A goes like this..."

    n "She writes another formula on the board."

    herschel @ say "The probability of A and B together divided by just the probability of B."
    herschel @ say "Alternatively it can often be more useful to rearrange this into the probability of A and B is equal to the probability of A given B multiplied by B."
    herschel @ say "Let me give you an example...."

    n "Mrs. Herschel explains how to solve the probability of drawing two queens in a row from a deck of cards."
    n "Gunner leans over and whispers to you."
    
    show herschel with move:
        xoffset 350

    show gunner disgusted at center with moveinleft:
        xzoom -1
        ypos y_gunner
        xoffset -650
        
    gunner @ say "Psst [name], did you understand any of that?"

    menu:
        gunner "{cps=0}Psst [name], did you understand any of that?{/cps}"
        "Of course.":
            player "Yeah, it's real basic stuff."
            
            show gunner uncomfy
            
            gunner @ say "Really? How the fuck can you move the letters around like that?"
            
            player "It's simple algebra."
            
            show gunner annoyed
            
            gunner @ say "Who do I look like, Isaac Newton?"
        "Not really.":
            player "Not really. She's going through it so quickly..."
            
            show gunner annoyed
            
            gunner @ say "I know right? This bitch needs to slow down."

    hide gunner with dissolve

    herschel @ say "Moving on, let's get into expected values which are simply defined as the summation of the probability of each possible value multiplied by the outcome of each of those probabilities!"

    n "Gunner groans and buries his head in his notebook."

    stop music fadeout .5

    scene bg campus summer day clear with fade

    play music "audio/music/vylet - by the seaside.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "Gunner stayed behind to talk to Mrs. Herschel while you and the rest of the class left."
    
    if avaClaireLunch == True:
        n "You don't have any more classes today but weren't you supposed to do something else?"
        n "That's right, you're having lunch with Ava and Claire? But where exactly?"
        n "It dawns on you that you never settled on a time nor location. You gave them your number but you forgot to plug in your phone last night so it's dead."
        n "Perhaps if you wander around campus for a while you'll run into them. It can't be that hard to spot Claire among a crowd. Ava might be harder to find though."
        n "Ah there she is, towering above everyone else. She reminds you of a great white shark swimming through a school of fish who disperse stay out of her path."
        
        player "Claire! Over here!"

        n "Her ears turn in your direction and she comes hopping toward you with Ava fluttering along by her side."

        show claire sweater overjoyed at center:
            ypos y_claire
            xoffset 500
            matrixcolor BrightnessMatrix(0.05)
        show ava typical happy at center:
            xzoom -1
            xoffset -520
            ypos y_ava
            matrixcolor BrightnessMatrix(0.05)
        with dissolve
        
        show claire sweater overjoyed

        claire @ say "[name]!!! What's up?"
        
        show ava overjoyed
        show claire happy

        ava @ say "Hey [name]! We were afraid we'd never find you haha!"
        
        show ava typical happy
        
        player "Sorry, my phone's dead."
        player "So where are we going to eat?"

        show claire sweater laughing
        
        claire @ say "We still haven't decided yet!"
        
        show ava typical agitated

        ava @ say "Claire keeps shooting down my ideas!"
        
        show claire sweater derp

        claire @ say "I do not!!! Ksksksks!"

        player "How about the cafe?"
        
        show claire sweater surprised earsup
        show ava unimpressed

        ava @ say "You mean Starbees? That place is hella crowded all the time."
        
        show claire sweater happy -earsup
        show ava concerned

        player "No, the one behind the library. Coffee Zone I think? It was pretty quiet when I went there a few days ago."

        claire @ say "I've never heard of it but that sounds good!"
        
        show ava excited
        
        ava @ say "Then it's settled! Lead the way, [name]!"

        scene bg cafe with fade

        play music "audio/music/mere - coffeeLoveInstrumentalEditSlowexe.ogg" fadein .4

        show box with Dissolve(.2):
            ypos 0
            
        n "The cafe is vacant save for the barista and a feline sitting at a table reading a textbook while listening to his headphones."
        n "He notices you when you walk in and waves you over."

        show gunner neutral at center with dissolve:
            xzoom -1
            ypos y_gunner

        player "Gunner? What are you doing here?"

        gunner @ say "I like to come here to study 'cause the smell of coffee keeps me awake."
        gunner "{nw}"
        
        pause .1
        
        show gunner with move:
            xoffset -630
            
        pause .1
        
        show claire sweater happy at center:
            ypos y_claire
            xoffset 610
        show ava typical happy at center:
            ypos y_ava
            xoffset 280
        
        with moveinright

        claire @ say "[name], you know this guy?"

        player "Oh, right. Claire, Ava, this is Gunner. We have statistics together."
        
        show ava pose shy

        ava @ say "Nice to meet you, Gunner!"
        
        show claire sweater derp

        claire @ say "I hope you don't mind us intruding on your territory!"
        
        show ava pose happy
        show claire sweater happy -

        gunner @ say "It's all good, I could use a break from this anyhow."
        
        player "Riiiight..."
        
        n "It's been less than 15 minutes since class ended, so he couldn't have been studying for long."
        
        show gunner cheeky1
        
        gunner @ say "You all want some coffee? It'll be my treat~"
        
        player "We actually stopped by to get lunch."
        
        show gunner neutral
        
        #shrug sprite
        gunner @ say "No problem, order whatever you want."
        gunner @ say "I accidentally withdrew too much cash and now my wallet barely fits in my pocket, so I don't mind."

        menu:
            gunner "{cps=0}I accidentally withdrew too much cash and now my wallet barely fits in my pocket, so I don't mind.{/cps}"
            "Decline":
                $ acceptedGunnersMoney = False
                
                player "I can pay for myself."
                
                gunner @ say "Heh suit yourself."
                
                n "Gunner leans in and whispers to you."
                
                show gunner charming
                
                gunner @ say "Wouldn't want these chicks to think you're poor, I get it."                
            "Accept":
                $ acceptedGunnersMoney = True
                
                n "Maybe Gunner's cool after all."
                
                player "I'd never turn down free food. Thanks man."
                
                show gunner eyesclosed catface
                
                gunner @ say "Of course! What kind of friend would I be if I didn't offer to cover something as small as lunch?"
                
        show gunner optimistic
        
        gunner @ say "Ladies? What about you?"
        
        claire @ say "I'll take you up on that offer! What a sweet guy!"
        
        show ava typical smug
        
        ava @ say "Yeah that would be very kind of you~"
        
        show gunner cutie
        
        gunner @ say "Aw don't sweat it!"
        gunner @ say "Go ahead and order while I finish this homework problem."
        
        n "He reaches into his pocket and pulls out his massive bulging wallet."
        
        show gunner cheeky1
        show ava happy
        
        gunner @ say "This should cover it. Just give the change to the barista as a tip."
        
        player "K. We'll be right back."
        
        hide gunner with dissolve
        
        n "Gunner gave you like $200. How much does he think lunch costs?"
        n "Maybe he figured Claire would need a lot."
        
        #either take credit for the tip or say it was gunner's idea

        show mishka neutral at center with moveinleft:
            xzoom -1
            xoffset -500
            ypos y_mishka
            
        #show mishka overjoyed

        mishka @ say "Hello again, [name]! And you brought friends!"
        
        show mishka neutral

        player "Hi Mishka! Yeah we're just stopping by to get something to eat after class."
        
        show claire sweater overjoyed

        claire @ say "Ohmygosh your accent is so cute! Tih rooskie?"

        show mishka sad wave
        show claire happy

        mishka @ say "Nyet, no ya nyemnogo govaryu po-Rooskie..."
        
        show mishka depressed
        
        n "Mishka turns to show the Ukrainian flag patch on her jacket."
        
        mishka @ say "I am from village near the border of Ookrainie ta Rossie."
        mishka @ say "So perhaps some Rossiskie has infected my way of speaking."

        claire @ say "Ahh, mnyeh zshal uhh... kak eto skazat... sleeshad eto. Ya nyemnogo znayu tolkuh Russkie, no slihshal, shto Ookrainskie pokhozh."
        
        show mishka neutral

        mishka @ say "Nu vih dobre tse hovoryt!"

        claire @ say "Spasibo!"

        n "You're left dumbfounded as to what they're saying. You had no idea Claire knew Russian. If she can learn a complicated language like that, French should be a breeze for her."

        mishka @ say "Now then! What I can get for you?"
        
        if acceptedGunnersMoney == False:
            n "You place your order and swipe your card then step aside so Ava and Claire can place theirs."
        else:
            n "You place your order then step aside so Ava and Claire can place theirs."
            
        n "When they're done, you slip Mishka the bills Gunner gave you."
            
        player "Keep the change."
        
        n "Mishka's eyes go wide as she subtracts the amount owed and is still left with a hefty sum."
        
        mishka @ say "Are you certain? This is a big amount of money to just give away!"
        mishka @ say "Usually people just leave behind the coins."

        menu:
            mishka "{cps=0}Usually people just leave behind the coins.{/cps}"
            "It was Gunner's idea":
                player "It was his idea."
                
                n "You gesture back toward Gunner."
                
                show mishka happy
                
                mishka @ say "Oh! Could you tell him dyakooyoo vam for me?"

                player "Uhh..."
                
                show mishka neutral -
                
                claire @ say "Don't worry, I got it~"
            "It's nothing, really.":
                player "It's nothing really. You deserve it for your hard work."
                
                show mishka happy
                
                mishka @ say "Oh my, well if you think so! Dyakooyoo vam haha!"
                
                player "Haha right uhh... Claire?"
                
                n "Claire whispers what to say into your ear."
                
                show mishka neutral -
                
                player "Bood laska...? Did I pronounce that right?"
                
                mishka @ say "Close enough!"

        mishka @ say "I will get started on your orders and have them ready for you at the end of the counter shortly!"
        
        hide mishka with dissolve
        
        n "You return to Gunner's table and sit beside him while you wait. He's packed his textbook and notes into his bag."
        
        show ava:
            xoffset -350
        show claire:
            xoffset -670
        with move
        
        pause .2
        
        show claire at flipright
        pause .1
        show ava at flipright
                
        jump avaClaireGunnerLunch
        
    else:
        n "As you're walking around campus thinking about where to get lunch, Gunner comes running up behind you."

        show gunner neutral at center with dissolve:
            ypos y_gunner

        gunner @ say "[name]! Wait up!"

        player "Hm? What's up?"

        gunner @ say "I just got done talking with Mrs. Herschel and she said I should get a study buddy."
        
        player "And..?"
        
        show gunner determined
        
        gunner @ say "Aaaaand you should totally study with me!"

        player "Why?"
        
        show gunner eyesclosed catface

        gunner @ say "Cause I'll buy you lunch if you do."
        
        show gunner cheeky1
        
        gunner @ say "And it'll be fun to hang out more!"
        
        show gunner neutral

        n "Free lunch is too good to pass up."

        player "Fine."

        gunner @ say "Yes!!!"
        
        show gunner neutral
        
        gunner @ say "You free right now? 'Cause I know a good place to study and get some food."

        player "Yeah I could eat."

        stop music fadeout .5

        scene bg cafe with fade

        play music "audio/music/mere - coffeeLoveInstrumentalEditSlowexe.ogg"

        show box with Dissolve(.2):
            ypos 0

        show gunner neutral at center with dissolve:
            ypos y_gunner

        gunner @ say "This is my secret study spot. I like coming here 'cause it's quiet and the smell of coffee keeps me awake."
        
        player "Yeah this place is cool."
        
        n "While you're pondering what to order, the door behind you opens up and you hear a pair of familiar voices."
        
        claire @ say "...I usually get a salted caramel cappuccino but I'm feeling like a cinnamon almondmilk latte today."

        ava @ say "Ooh both of those sound pretty good."
        
        show gunner at flipright
        
        pause .6
        
        show gunner with move:
            xoffset -650
            ypos y_gunner
        
        show ava typical happy at center:
            ypos y_ava
            xoffset 300
        show claire sweater happy at center:
            ypos y_claire
            xoffset 670
        with dissolve
        
        show gunner frown1

        claire @ say "Oh my gosh, look who it is! Heyyyy!!!~~~"
        
        n "You turn around and are greeted with an involuntary hug you can't escape from."
        
        show ava typical whimsical
        
        ava @ say "Easy there Claire, before you crack his ribs."
        
        n "Judging by the popping of your bones, she absolutely could."
        n "Yet, you feel nothing but comfort, smothered in death's sweet embrace."
        n "Claire eases her grip and you're allowed to breathe once more."
        
        show gunner optimistic
        show ava happy
        show claire sweater giggle
        
        claire @ say "You alright? Your spine still intact?"
        
        player "I think so."
        
        show claire sweater laughing
        
        claire @ say "Good!"
        
        show claire sweater happy
        
        claire @ say "We'll let you two get back to your date now~"
        
        show gunner disgusted
        
        gunner @ say "Date?! We just came here to study, that's all!"
        
        show claire sweater suggestive
        
        claire @ say "Suuurrree~"
        
        show gunner optimistic
        show claire happy
        show ava pose happy
        
        ava @ say "Don't let us interrupt you! We're just stopping by real quick to get lunch."
        
        show gunner charming
        
        n "Gunner looks at you with a scheming look in his eyes."
        
        gunner @ say "Hey [name], we've been studying for a while, think we could take a break?"
        
        n "Seems he has other things on his mind. You don't really care if you end up studying with him or not as long as you get a free lunch."
        
        player "Fine."
        
        show gunner optimistic
        
        gunner @ say "Perfect! Why don't we all sit together then! I'm Gunner by the way. [name] and I have stats class together."

        show ava pose shy

        ava @ say "Nice to meet you, Gunner! I'm Ava and this is Claire. We don't have any classes together but we're roommates."
        
        show ava pose happy
        show claire sweater happy earsup

        claire @ say "Not to mention besties~"
        
        show claire sweater happy -earsup
        show ava pose whimsical
        
        ava @ say "As close to besties as we can be after knowing each other for less than a week haha."
        
        show ava pose happy
        show claire giggle
        
        claire @ say "Is this what you meant when you said you'd be busy today, [name]?"
        
        show claire overjoyed
        
        claire @ say "You should have told me you were taking stats! I got an A in my advanced statistics and stochastic processes in high school! I'd be down to explain it to you guys!"
        
        show gunner disgusted
        show claire happy

        #yik pose 2 gunner here
        gunner @ say "What the fuck are stochastic processes?"
        
        n "The emptiness in your stomach rears its ugly head and demands that you hurry up with this boring small talk."
        
        show gunner neutral
        
        player "You all know what you want? I'm ready to order."
        
        claire @ say "Hmmm.... Yeah I think so!"
        
        n "You make your way to the counter where Mishka is standing, watering the plants that adorn the area."
        
        hide gunner
        hide claire
        hide ava
        with dissolve
        
        show mishka neutral at center with moveinleft:
            xzoom -1
            ypos y_mishka
            xoffset -600
        
        mishka @ say "Hello again, [name]! And nice to see you as well, Gunner!" 
        
        pause .1       
        
        show gunner optimistic at center with dissolve:
            ypos y_gunner
            xoffset 350
        
        gunner @ say "Heya Mishka! Yeah, I've got a lot of studying to do so expect to see me a lot this semester. Luckily I've got a study buddy to help me out!"
        
        show mishka neutral eyesclosed tongueout

        mishka @ say "Is that so? Hopefully you're getting paid well, [name]!"
        
        show mishka neutral -eyesclosed -tongueout

        gunner @ say "Hey, I'm paying for lunch! That's a decent rate!"
        
        show mishka nervous

        mishka @ say "If you say so xaxa"
        
        hide gunner with dissolve
        
        show claire sweater happy at center with dissolve:
            ypos y_claire
            xoffset 400
        
        claire @ say "Ohmygosh your accent is so cute! Tih rooskie?"

        show mishka sad wave

        mishka @ say "Nyet, no ya nyemnogo govaryu po-Rooskie..."
        
        show mishka depressed
        
        n "Mishka turns to show the Ukrainian flag patch on her jacket."
        
        mishka @ say "I am from village near the border of Ookrainie ta Rossie."
        mishka @ say "So perhaps some Rossiskie has made its way into my speech."

        claire @ say "Ahh, mnyeh zshal uhh... kak eto skazat... sleeshad eto. Ya nyemnogo znayu tolkuh Russkie, no slihshal, shto Ookrainskie pokhozh."
        
        show mishka neutral

        mishka @ say "Nu vih dobre tse hovoryt!"

        claire @ say "Spasibo!"

        n "You're left dumbfounded as to what they're saying. You had no idea Claire knew Russian. If she can learn a complicated language like that, French should be a breeze for her."

        mishka @ say "So, what can I get for you?"
        
        show gunner neutral at center with dissolve:
            ypos y_gunner
            xoffset 700
        
        gunner @ say "Go ahead and order, you guys. It'll be my treat."
        
        claire @ say "Ohmygosh thank you~~ Such a gentleman!"
        
        hide gunner with dissolve
        
        show ava pose smug at center with dissolve:
            ypos y_ava
            xoffset 700
        
        ava @ say "Wow, that was pretty forward."
        
        show ava pose whimsical
        
        ava @ say "But I'll take you up on that offer~"
        
        show ava pose happy
        
        n "Everyone places their order and Gunner pays for it with a $100 bill. Show off."
        n "He takes the change and dumps it in the barista's tip jar. Oh now he's really showing off."
        
        show mishka happy
        
        mishka @ say "Thank you very much!! I will have that ready for you in just a few minutes!"
       
        hide mishka with dissolve
        
        show ava:
            xoffset -350
        show claire:
            xoffset -670
        with move
        
        pause .2
        
        show claire at flipright
        pause .1
        show ava at flipright
        
        show gunner neutral at center with moveinright:
            ypos y_gunner
            xoffset 600
        
        n "Your small group goes to find a table. Gunner takes the seat beside you and the ladies sit across from you."

        jump avaClaireGunnerLunch

label avaClaireGunnerLunch:    
    show gunner neutral at center with moveinright:
        ypos y_gunner
        xoffset 600

    show claire sweater suggestive

    claire @ say "Thanks again for lunch~"
    
    show ava typical happy -pose
    show claire happy
    show ava typical excited at hop
    
    ava @ say "Yeah, especially since we're basically strangers!"
    
    show ava happy
    show gunner eyesclosed catface
    
    gunner @ say "Hey, any friend of [name]'s is a friend of mine!"
    
    show gunner neutral
    
    gunner @ say "Besides, what better way to get to know someone than over lunch?"
    
    show gunner optimistic
    
    gunner @ say "You two freshmen? I haven't seen you around before."
    
    show ava excited
    
    ava @ say "Yup! I can't believe I actually got accepted here of all places!"
    
    show claire overjoyed
    
    claire @ say "I know right?? It's like a dream come true!"
    
    show claire happy
    show ava happy
    
    player "Yeah Harmonia is pretty cool I guess. Never thought I'd end up *here.*"
    
    ava @ say "So, what are you majoring in Gunner?"
    
    show gunner eyesclosed smile
    
    gunner @ say "Political science. It's not my passion or anything but what else is the son of a wealthy oil baron supposed to do?"
    
    show gunner optimistic
    
    gunner @ say "What about you?"
    
    show ava smug
    
    ava @ say "Oh just photography. I have an eye for it and thought I could make connections here to build a career out of it. I'd love to travel and just shoot people all day~"
    
    show ava shocked
    
    ava @ say "With my camera I mean..!"
    
    show ava happy
    show claire laughing
    
    claire @ say "Ksksksks y'all are so cute with your dreams and plans! And here I am going in raw with my undecided major!"
    
    show claire flustered
    
    claire @ say "There's so many options, I can't just pick one thing to specialize in for the rest of my life!!"
    
    ava @ say "Well, what are your hobbies?"
    
    show claire derp
    
    claire @ say "Um um I don't know, I like doing everything and trying new things?"
    
    show ava unimpressed
    
    ava @ say "That's not a hobby."

    gunner @ say "How about... golfing? That's a useful skill for political science."
    
    show claire happy
    
    claire @ say "Got bored of it after getting a hole in one on every course in my state."
    
    show ava unamused
    
    ava @ say "Ever try drawing?"
    
    #claire @ say "Already drew everything I wanted to draw."
    claire @ say "They had to build a whole new wing at my local museum just for my paintings."
    
    gunner @ say "Fishing?"
    
    #claire @ say "My fishing career peaked when I harpooned a 600 pound tuna in my rowboat and spent 3 days fighting sharks to bring it back home."
    claire @ say "I already caught so many fish, I started reeling in undiscovered species."
    
    show ava concerned
    
    ava @ say "Cooking?"
    
    claire @ say "Had a good run with a critically acclaimed reality cooking show that lasted 5 seasons."
    
    show gunner uncomfy
    
    gunner @ say "Music?"
    
    claire @ say "Never looked back after dropping a single that topped the charts for a few months."
    
    #ava @ say "Fashion?"
    #claire @ say "Banned from the industry after trolling a high end runway show with an all plus-sized lineup."
    
    show ava annoyed
    
    ava @ say "Ever thought about working out?"
    
    show claire flustered
    
    claire @ say "Hey underneath all this fat I'm pure muscle!"
    
    #ava @ say "Acting?"
    
    #show claire flustered
    
    #claire @ say "Blacklisted from the industry for... reasons."
    
    gunner @ say "Do you like guns?"
    
    show claire derp
    
    claire @ say "I use my gold medal from the Olympics shooting competition as a coaster."
    
    n "Wow, she's already done it all and she's not even in her 20s. She's like the total opposite of you."
    
    show gunner determined
    show ava embarrassed
    
    gunner @ say "You could always make an Onlyfawns account. I know *tons* of guys who would pay to see you."
    
    show claire suggestive earsup
    
    claire @ say "Ksksks you think so?~"
    
    show claire laughing -earsup
    show ava neutral
    
    claire @ say "Sorry, but the big bunny boobas are not for sale~"
    
    show gunner neutral
    show ava happy
    show claire happy
    
    gunner @ say "What do you think [name]? What are some of your hobbies that Claire might enjoy?"
    
    n "Browsing internet image boards is not something you can admit to enjoying in front of normies."
    n "Quickly, you have to come up with a cooler hobby."
    
    menu:
        n "{cps=0}Quickly, you have to come up with a cooler hobby.{/cps}"
        "Climbing":
            $ chosenHobby = "climbing"
            
            player "I like to climb stuff."
            
            show ava concerned
            
            ava @ say "What, like mountains?"
            
            show gunner motivated
            
            gunner @ say "Or at the rock climbing gym?"
            
            show gunner neutral
            show ava happy
            
            player "Uhh both. Buildings too."
            
            show claire happy earsup
            
            claire @ say "Wow that sounds pretty cool!"
            claire @ say "You gotta show us sometime!"
            
            show ava typical enamored
            show claire giggle
            show gunner disgusted
            
            player "I'd love to but I'm currently recovering from an injury. Fell like 30 feet while freeclimbing. Into a pit full of venomous snakes. Barely survived."
            
            show claire happy -earsup
            show gunner neutral
            show ava reaching concerned
            
            ava @ say "Aww, hope you get better soon."
            
            show ava typical happy -reaching
            show claire flustered
            
            claire @ say "It must be so much fun, but can you imagine my fat ass scaling a cliff? The rocks would crumble under my weight ksksksks!"
            
        "Driving":
            ###you end up watching initial D and playing racing sims
            #later on someone has to drive. "does anyone know how to drive manual?"
            
            $ chosenHobby = "driving"
            
            player "..."
            player "......"
            player "........."
            
            show ava typical enamored
            show claire sweater surprised earsup
            show gunner determined
            
            player "I drive."
            
            n "Why did you say that? You don't even have a car."
            #n "You barely even have a driver's license. It's set to expire this month"
            n "Acting cool and stoic about it somehow garnered the fascination of your peers however."
            
            show claire giggle
            
            claire @ say "Whoa, like a racecar driver?"
            
            player "..."
            player "Something like that."
            
            show gunner cheeky1
            
            gunner @ say "Or a stunt driver?"
            
            player "..."
            player "Getting closer."
            
            show ava motivated
            
            ava @ say "Don't tell us you're a getaway driver."
            
            show ava happy
            
            player "..."
            
            show ava enamored
            
            player "Bingo."
            
            show claire laughing
            
            claire @ say "Ohmygosh that's so cool!!"
            claire @ say "You're like a secret underground criminal on the run from the police!"
            
            show ava excited
            
            ava @ say "That must be so exciting!!"
            
            show gunner motivated
            
            gunner @ say "Heh, I know who I'm calling if I decide to rob a bank."    
            
        "Bushcraft":
            ###if you choose this option, you start looking into that hobby and can build a fire for claire later on
            
            $ chosenHobby = "bushcraft"
            
            n "What's a word nobody actually uses? Maybe you can confuse them to avoid having to talk about it."
            
            player "I do bushcraft."
            
            show claire surprised earsup
            show ava shocked
            
            claire @ say "Like outdoors survival stuff?"
            
            show claire sweater happy -earsup
            
            n "Well shit, you should have known Claire would have knowledge of esoteric camping lingo."
            
            player "Er yeah, chopping down trees and building shelter... making fires in thunderstorms... hunting and foraging for food."
            
            n "The only survival you've ever done is in Meincraft. It's close enough, right?"
            
            show claire sweater pose suggestive
            show ava happy
            
            claire @ say "I've done a little bit of that! It was fun! I'd love to delve deeper and do some real survival!"
            
            show ava excited
            
            ava @ say "There you go! New hobby!"
            
            show ava happy
            show gunner itsover
            
            gunner @ say "Yeah but it's not like you can major in camping."
            
            show gunner neutral
            
            ava @ say "Maybe she can be a park ranger or... one of those search and rescuers."
    
    show ava happy
    show claire happy earsup
    show gunner neutral
    
    mishka @ say "Orders are ready for pickup!"
    
    show claire happy -earsup
    
    claire @ say "Oh, there's our food!"
    
    if avaClaireLunch == False:        
        player "I got it."
        
        n "It's the least you could do since Gunner paid for it. And you don't want to let him show off anymore."
        
        hide gunner
        hide ava
        hide claire
        with dissolve
        
        n "You stand up and walk over to the counter."
        
        show mishka neutral at center with dissolve:
            xzoom -1
            ypos y_mishka
        
        mishka @ say "Enjoying the company?"
        
        show mishka anxious smile
        
        mishka @ say "That rabbit sure has many talents."
        
        player "Huh? Oh haha, you could hear our conversation?"
        
        show mishka happy
        
        n "She flicks her big rat ears."
        
        mishka @ say "We rats can hear pretty well."
        
        show mishka anxious neutral
        
        mishka @ say "It's nice you've found so many friends already..."
        
        player "I've only just met them but they seem to pop up everywhere I go."
        
        show mishka happy
        
        mishka @ say "Perhaps they are hunting you down hehe"
        
        show mishka anxious neutral
        
        player "Kinda feels like it haha!"
        
        show mishka neutral -anxious
        
        mishka @ say "Well, enjoy the food and take care!"
        
        player "Thanks!"
        
        hide mishka with dissolve
        
        n "Grabbing food and drinks for four is as difficult as it sounds and Gunner has to come and bail you out when he sees you struggling."
        
        show gunner neutral at center with dissolve:
            ypos y_gunner
            
        gunner "Whoa, lemme carry some of that before it falls."
        
        player "Thanks dude."
        
        gunner @ say "Don't mention it."
        
        n "Even with the two of you, it proves to be a challenge but you manage to bring it all to the table in one trip without dropping anything."
    else:
        gunner @ say "You all chill here, I'll go pick it up."
    
        hide gunner with dissolve
        show claire sweater giggle
        
        show ava:
            xoffset -100
        show claire:
            xoffset -550
        with move

        claire @ say "I totally saw you checking him out, Ava!"
            
        show ava typical shocked at flipleft
        
        ava @ say "What? Who?!"
        
        claire @ say "That Gunner boy duh! Ksksksksksks!"
        
        show ava unimpressed

        ava @ say "Oh my god, I was not!"
        
        claire @ say "You were too!"
        
        show claire sweater pose suggestive

        claire @ say "What do you think, [name]? Was she not looking at him with hearts in her eyes?"
        
        show ava concerned

        ava @ say "Shush up or he'll hear you!"
        
        show claire surprised earsup

        claire @ say "Ksksksksks so I was right!"
        
        show ava annoyed

        ava @ say "Nuh uhhhh! He may be cute but I don't even know anything about him!"
        
        show claire sweater pose suggestive

        claire @ say "Oh so now you think he's cute?"
        
        show ava typical embarrassed

        ava @ say "I didn't mean-!"
        
        n "You look back and see Gunner struggling to carry everything. To be fair, three cups is a challenge in itself. Adding food to the equation makes it nearly impossible."
        n "As Claire teases an increasingly flustered Ava, you get up to help your feline friend."

        hide ava
        hide claire
        with dissolve
        
        show gunner neutral at center:
            ypos y_gunner

        gunner @ say "Thanks bro. I underestimated how hard it would be to balance three hot coffees in one paw and the rest in the other."
        
        player "No problem dude."
        
        n "The two of you manage to bring it all to the table in one trip without dropping anything."
        
    show gunner with move:
        xoffset 600
        
    gunner @ say "Bon appetit!"
    
    show ava typical happy at center:
        xoffset -350
        ypos y_ava
        xzoom -1
    show claire sweater happy at center:
        xoffset -670
        ypos y_claire
        xzoom -1
    with dissolve

    claire @ say "Ooh, that smells good~"
    claire @ say "What were we talking about just now?"
    
    show ava neutral
    
    ava @ say "Dunno. Don't care anymore."
    
    show ava happy
    
    n "The conversation slows down as you enjoy a good meal."
    n "You end up chatting until evening arrives."
    
    show gunner frown1
    
    gunner @ say "Whoa, it's already starting to get dark out. I'd love to stay in such good company but I've got some things to take care of."
    
    show gunner neutral
    show ava excited
    
    ava @ say "Yeah, this was a pretty long lunch, wasn't it! We should do this again sometime!"
    
    show ava happy
    show claire at hop
    
    claire @ say "I'm down to hang out more!"
    
    n "You have to admit, chilling with these three was kinda fun."
    
    player "Count me in too."
    
    gunner @ say "Sweet. I'll catch you all later!"
    
    n "Claire pulls everyone into a tight hug."
    
    claire @ say "Bye guys!!! I'll miss youuuuu!"
    
    show ava agitated
    
    ava @ say "You'll still have me!"
    
    show gunner wink frown
    
    gunner @ say "Can't... breathe..."
    
    show claire surprised earsup
    
    claire @ say "Oops."
    
    show gunner neutral
    show ava happy
    
    n "Claire lets you all go."
    
    show claire derp
    
    claire @ say "Sorry 'bout that! I just got so excited!"
    
    gunner @ say "It's alright, I think my ribs are intact."
    
    player "Same."
    
    claire @ say "Can't wait to hang out with you all again!!!"
    
    hide ava
    hide gunner
    hide claire
    with dissolve
    
    n "You go your separate ways and return to your dorms for the night."
    
    #Can't stay up too late when you've still got class tomorrow."

    stop music fadeout 1.0

    scene bg codadorm with fade
    
    play music "audio/music/vylet - wish.ogg" fadein 0.5

    show box with Dissolve(.2):
        ypos 0

    n "After winding down a bit in your dorm, you lie in bed and look at your phone."
    
    $ cafeEvents.append("claireCafe")

    call phone_start from _call_phone_start_1

    call message_start("Claire", "Hey [name]! It was cool seeing you at coffee zone today!", "claireavi.png") from _call_message_start_1
    call message("Claire", "This is Claire btw", "claireavi.png") from _call_message_165

    call reply_message("Yeah it was fun hanging out with everyone") from _call_reply_message_5

    call message("Claire", "Maybe we can go together someday", "claireavi.png") from _call_message_6
    call message("Claire", "Just the two of us~", "claireavi.png") from _call_message_166

    call screen phone_reply("To study?","toStudy","Would be nice","wouldBeNice")
    
label toStudy:
    call phone_after_menu from _call_phone_after_menu_4
    
    call message_start("me", "What, like to study?", "testimage.png") from _call_message_start_17
    
    call message("Claire", "lol if you want to", "claireavi.png") from _call_message_167
    
    call reply_message("Maybe if I have the time. I'm still getting used to living on a schedule again") from _call_reply_message_117
    
    call message("Claire", "np just lemme know when!", "claireavi.png") from _call_message_168
    
    call reply_message("will do") from _call_reply_message_118
    
    call phone_end from _call_phone_end_15
    
    jump afterClairePhone1
label wouldBeNice:
    call phone_after_menu from _call_phone_after_menu_5
    
    call message_start("me", "That would be nice", "testimage.png") from _call_message_start_18

    call message("Claire", "Yes, it would :P", "claireavi.png") from _call_message_169
    call message("Claire", "Just lemme know when you're free!", "claireavi.png") from _call_message_170
    
    call reply_message("I'll text you when my schedule frees up") from _call_reply_message_119
    
    call message("Claire", "Okii ^w^", "claireavi.png") from _call_message_171

    call phone_end from _call_phone_end_1
    
    jump afterClairePhone1
    
label afterClairePhone1:
    play audio "audio/sound effects/vibrate.ogg"

    n "*buzz buzz*"
    n "What now?"

    call phone_start from _call_phone_start_47
    
    call message_start("Ava", "Heyyyy [name] :>", "avaavi.png") from _call_message_start_57
    
    call reply_message("That's a lot of y's") from _call_reply_message_203
    call reply_message("Either you're into me or you want a favor") from _call_reply_message_204
    
    call message("Ava", "^v^;", "avaavi.png") from _call_message_172 
    
    call reply_message("I'm guessing this is Ava?") from _call_reply_message_120

    call message("Ava", "Aaaaa you figured me out!", "avaavi.png") from _call_message_293
    call message("Ava", "I was just wondering... if you could give me that catboy's number pls <3", "avaavi.png") from _call_message_294

    call reply_message("You mean Gunner? Why didn't you ask him yourself?") from _call_reply_message_77
    
    call message("Ava", "IDK how to ask a boy for his number out of the blue!", "avaavi.png") from _call_message_26
    
    call reply_message("You just... ask? It's not difficult.") from _call_reply_message_80
    
    call message("Ava", "UGH it's not that simple!", "avaavi.png") from _call_message_99
    
    call reply_message("It really is.") from _call_reply_message_82
    call reply_message("But sure, I'll send it to you.") from _call_reply_message_88

    call message("Ava", "Thxx pls don't tell claire tho XvX", "avaavi.png") from _call_message_295

    call reply_message("Lol i won't") from _call_reply_message_206
    call reply_message("You planning on asking gunner out?") from _call_reply_message_207

    call message("Ava", "Idk", "avaavi.png") from _call_message_296
    call message("Ava", "I mean he;s cute and all but", "avaavi.png") from _call_message_297
    call message("Ava", "I hardly even know him", "avaavi.png") from _call_message_298

    call screen phone_reply("He's nice","hesnice","He's gay","hesgay")

    label hesnice:
        #$ avaPoints = avaPoints - 1
        call phone_after_menu from _call_phone_after_menu_10

        call message_start("me", "He's nice", "testimage.png") from _call_message_start_58

        call message("Ava", "You think so??", "avaavi.png") from _call_message_299

        call reply_message("I mean I only just met him earlier this week but yeah?") from _call_reply_message_208

        call message("Ava", "Okayy thanks :>!!!", "avaavi.png") from _call_message_300

        call reply_message("No problem") from _call_reply_message_209
        
        call phone_end from _call_phone_end_16 

        jump afterAvaText1
    
    label hesgay:
        call phone_after_menu from _call_phone_after_menu_6
        $ avaPoints = avaPoints + 1
        $ trolledAva = True
        
        call message_start("me", "He's gay", "testimage.png") from _call_message_start_23
        
        call message("Ava", "Whaaaaaaat?!", "avaavi.png") from _call_message_100
        call message("Ava", "No way!!!", "avaavi.png") from _call_message_103
        
        call reply_message("Yup it's true") from _call_reply_message_89
        
        call message("Ava", "How do you know??", "avaavi.png") from _call_message_106
        
        call reply_message("His boyfriend told me") from _call_reply_message_90
        
        call message("Ava", "Nuuuu ;-;", "avaavi.png") from _call_message_107
        
        call reply_message("What teh problem?") from _call_reply_message_91
        
        call message("Ava", "Nothing", "avaavi.png") from _call_message_108
        call message("Ava", "Why are all the cute ones always gay >.<", "avaavi.png") from _call_message_115
        
        call reply_message("Shrug") from _call_reply_message_108
        call reply_message("That's the way it goes") from _call_reply_message_109
        
        call message("Ava", "well... thanks for lettin me know", "avaavi.png") from _call_message_116
        
        call reply_message("Np") from _call_reply_message_183
        
        call phone_end from _call_phone_end_19
        
        n "How devilish of you."
        #n "You feel as though you've altered the course of history."
    
        jump afterAvaText1
    
label afterAvaText1:
    n "*buzz buzz*"
    n "Another new message? That must be Gunner."
    #n "Nobody else has your number."

    call phone_start from _call_phone_start_13

    call message_start("Gunner", "Sup dude", "gunneravi.png") from _call_message_start_19    
    call message("Gunner", "Your friends are hot", "gunneravi.png") from _call_message_173    
    call message("Gunner", "At least the bird one is", "gunneravi.png") from _call_message_174    
    
    call reply_message("Thanks?") from _call_reply_message_121
    
    call message("Gunner", "Was wondering if you could do me a favor", "gunneravi.png") from _call_message_148 
    call message("Gunner", "You have her number right?", "gunneravi.png") from _call_message_149 

    call reply_message("Ava?") from _call_reply_message_205 

    call message("Gunner", "Yeah! Would you mind sending it to me? :3", "gunneravi.png") from _call_message_150 

    call reply_message("Why?") from _call_reply_message_230 

    call message("Gunner", "Cause I wanna ask her out", "gunneravi.png") from _call_message_153 

    call reply_message("By unsolicted text?") from _call_reply_message_231 

    call message("Gunner", "Pshh no", "gunneravi.png") from _call_message_218 
    call message("Gunner", "So i can stalk her pinstagram", "gunneravi.png") from _call_message_244 
    
    if trolledAva == True:
        call reply_message("U know she's a lesbian right?") from _call_reply_message_233 

        call message("Gunner", "Whaaaaaat?!", "gunneravi.png") from _call_message_245 
        call message("Gunner", "How do you know?", "gunneravi.png") from _call_message_246 
        
        call reply_message("I have french with her roommate") from _call_reply_message_234 
        call reply_message("she told me") from _call_reply_message_235 

        call message("Gunner", "Man that's gay", "gunneravi.png") from _call_message_247 
        call message("Gunner", "Why are all the hot ones always lesbians", "gunneravi.png") from _call_message_248 

        call reply_message("idk i guess it's hard to resist babes even if you're a girl yourself") from _call_reply_message_236 
        
        call message("Gunner", "I guess that makes sense", "gunneravi.png") from _call_message_249 
        call message("Gunner", "I mean if I was a girl I'd be a raging lesbian too", "gunneravi.png") from _call_message_250 
        call message("Gunner", "They'd call me Stacy Thunderpussy after I fucked every last lesbian on earth", "gunneravi.png") from _call_message_251 
        call message("Gunner", "All the hot ones at least", "gunneravi.png") from _call_message_175 
        
        #what, all 10 of them?
        call reply_message("what an ambitious fantasy") from _call_reply_message_122  
        
        call message("Gunner", "Yeah I'm a real tour de france", "gunneravi.png") from _call_message_253 
        
        call reply_message("I'll leave you to your lesbian fantasies") from _call_reply_message_123 
        
        call message("Gunner", "See you in class!", "gunneravi.png") from _call_message_176  
        
        call phone_end from _call_phone_end_17
        
        n "Well this ought to be fun to watch play out."
        n "A little trolling never hurt anyone, right?"
    else:
        call reply_message("fine i'll send it to you just don't be creepy") from _call_reply_message_124
        
        call message("Gunner", "based", "gunneravi.png") from _call_message_177 
        call message("Gunner", "thanks man", "gunneravi.png") from _call_message_178 
        call message("Gunner", "i owe you a favor", "gunneravi.png") from _call_message_179 

        call reply_message("cool") from _call_reply_message_125
        call reply_message("It's getting late. I'll see you in class later") from _call_reply_message_126
   
        call message("Gunner", "K goodnight dude", "gunneravi.png") from _call_message_180 
        
        call phone_end from _call_phone_end_18

    if bedpilled == True:
        n "With your head resting on your pillow, you stare at the ceiling."
        n "It's dark out and you have class in the morning but you're not tired enough for bed on account of sleeping in earlier."
        n "There's no point in lying here wide awake when you could be doing anything else."
        n "You could be a responsible student and study to make up for the class time you missed... or you could go out on a nightwalk on campus."
        n "You know which one your heart is telling you."
        
        scene bg campus summer night clear with fade
        
        play music "audio/music/vylet - yeah i'm ok thanks for asking.ogg" fadein .4
        
        show box with Dissolve(.2):
            ypos 0
        
        n "The night air is cool with a constant brisk wind buffetting your jacket."
        n "Gone is the hustle and bustle of the campus's daytime operations, replaced with a sense of isolation and abandonment."
        n "With only the street lamps to light the way, your surroundings become an unfamiliar void where only the odd stranger lurks."
        n "So it seems, until a friendly figure emerges from the shadows and locks eyes with you."
        
        show rori concerned at center with dissolve:
            ypos y_rori
            matrixcolor BrightnessMatrix(-0.05)
        
        rori @ say "[name]? What are you doing out so late?"
        
        player "I could ask you the same thing."
        
        show rori worried noblush
        
        rori @ say "I'm just out for a walk. I always do this when I get stuck on something and need a moment away from it."
        
        show rori cheery
        
        rori @ say "It lets me come back to it with a fresh perspective."
        
        player "Did you loonix install break again?"
        
        show rori neutral
        
        rori @ say "..."
        
        show rori sleepy blushing
        
        rori @ say "... Yes."
        
        show rori surprised
        
        rori @ say "B-but I can fix it!"
        
        show rori neutral -lookingaway
        
        player "Then why are you out here instead of fixing it?"
        
        show rori concerned
        
        rori @ say "Because I'm thinking."
        
        player "About?"
        
        show rori anxious
        
        rori @ say "About... well, nevermind. It's dumb."
        
        menu:
            rori "{cps=0}About... well, nevermind. It's dumb.{/cps}"
            "It's probably not dumb":
                $ roriPoints += 1
                
                player "If you're thinking about it so hard, it's probably not dumb."
                
                show rori concerned
                
                rori @ say "I dunno..."
                rori @ say "I'm just wondering if I'm wasting my time."
                
                player "With the computer thing?"
                
                rori @ say "No, with ALL the computer things."
                
                player "I thought you wanted to be a programmer."
                
                show rori worried noblush
                
                rori @ say "I do but..."
                
                show rori concerned
                
                rori @ say "Nevermind. See, I told you it was dumb."
                
                player "Hmm. I feel like I'm not seeing the full picture here."
                
                show rori sleepy
                
                rori @ say "It's nothing, really. Just me worrying too much."
                
            "Think about something else then":
                player "Have you tried thinking about something else?"
                
                show rori concerned
    
                rori @ say "Yeah but my thoughts usually end up back to wondering if I'm wasting my time."
                
                player "Why would you think that?"
                
                rori @ say "'Cause maybe I am? What if like a solar flare destroys all the electronics on Earth and then everything I've worked towards will be for nothing."
                
                player "Uhh yeah that would suck."
                player "But is that really something worth worrying about?"
                
                show rori worried noblush
                
                rori @ say "Okay maybe that's a bit of an extreme example but I just feel like all the virtual stuff is..."
                
                show rori sleepy
                
                rori @ say "I dunno. You're right, I should think about something else."
                
        show rori neutral
                
        rori @ say "You never told me what you're doing out at this hour."
        
        player "I'm a nightwalker. It's what I do."
        player "I guess it clears my mind. Not to mention it's comfy as fuck."
        player "Not many people around and the darkness feels... liberating?"
        player "I don't mean that in an edgy way I mean I feel like no one is watching me."
        
        rori @ say "Ohh yeah."
        rori @ say "I guess that's why I prefer coming out at night rather than the day too."
        
        show rori anxious
        
        rori @ say "Even if it is more... eerie."
        
        show rori neutral
        
        player "Yeah, never know what's out there. I'm not sure what's scarier, walking around the woods in darkness or being in the city at night."
        
        rori @ say "...Probably the city. I never leave home without a weapon."
        
        n "He pulls his hoof out from his jacket pocket and shows you the folded knife in his grasp before quickly shoving it back out of sight."
        
        player "Good thinking."
        
        n "The two of you stand around awkwardly, not sure where to take the conversation next."
        
        rori @ say "Well uh, I'll see you later then, k?"
        
        player "Yeah I think this has been a successful nightwalk and I can go to bed now."
        
        rori @ say "Cool. Don't be afraid to say hi if you see me walking around at night again."
        
        show rori laugh
        
        rori @ say "I promise I won't stab you... But don't startle me just in case."
        
        player "Haha sure. Goodnight Rori."
        
        show rori smirk
        
        rori @ say "Goodnight [name]!"
        
        n "You continue in your separate directions and loop your way back to your dorm, where you have no trouble falling asleep."
    
    else:
        n "With your head resting on your pillow, you close your eyes and soon fall into slumber."

    stop music fadeout .5

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show twednesday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7
    
label thursday1:
    #thursday

    scene bg lecturehall with fade
    
    play music "audio/music/mere - retrograde slowed.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    show margaret neutral at center with dissolve:
        ypos y_margaret
    
    margaret @ say "Good morning class, today we'll continue our discussion on The Death of Ivan Ilyich!"
    margaret @ say "We've seen that Ivan's social circle is more concerned with status and convenience than compassion."
    margaret @ say "Now we'll get into the life that Ivan lived. Like his peers, his primary motives revolved around gaining approval from others and climbing the social ladder."
    margaret @ say "Convinced by his associates, he entered a loveless marriage, that which he neglected in favor of his work."
    margaret @ say "\"...within a year of his wedding, Ivan Ilych had realized that marriage... is in fact a very intricate and difficult affair...\""
    margaret @ say "The more his wife expected of him, the more he retreated into his career... "
    
    show margaret sad
    
    margaret @ say "Oh Tolstoy, how right you were all along. How disappointing marriage turned out to be."
    margaret @ say "If only I'd listened to you, maybe I wouldn't have wasted 15 years of my life...!"
    
    show margaret sad shocked
    
    margaret @ say "Er... I'm sorry, that was unprofessional... Let's just forget about that and move on shall we?"
    
    show margaret melancholy
    
    margaret @ say "...So Ivan Ilyich had deluded himself into thinking he was happy by ignoring his troubles and taking misplaced pride in an uncaring workplace."
    margaret @ say "But as we'll soon see, his life was anything but enjoyable and it was only as he laid dying did he realize his flawed perception of life..."

    scene bg classroom with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box:
        ypos 0

    n "Miss Ellen sure seemed to be in a bad mood today, but Mrs. Celestine is bursting with energy."

    show celestine neutral at center:
        ypos y_celestine
        xzoom -1

    celestine @ say "Good morning class! It's such a lovely day to learn some French, n'est-ce pas?"
    celestine @ say "Today we'll practice some common phrases like \"Comment ca va?\" and \"Bonne journée!\""

    n "She writes out some sentences on the board and explains their meanings along with how to pronounce them."
    n "After getting the class to say them aloud a few times, she pairs you all up with a partner to practice some basic sentences with each other."

    celestine @ say "Go ahead and try making conversation with your partner! Don't be afraid of saying things wrong, you'll get it sooner or later!~"
    
    show claire sweater happy at center:
        ypos y_claire
        xoffset 1300

    hide celestine with dissolve

    n "Claire pushes her desk next to yours."

    show claire sweater happy:
        xoffset 1000
    with move
    
    pause .2
    
    show claire sweater happy:
        xoffset 750
    with move
    
    pause .2
    
    show claire sweater happy:
        xoffset 500
    with move

    pause .1

    show claire sweater wave happy

    claire @ say "Heyyyy~"
    claire @ say "Oops, I mean bonjourrrr~"

    player "Uhh... Salut, comment ca va?"
    
    show claire sweater derp

    claire @ say "Je suis tres bon! Comment allez-vous?"
    
    player "Bien, merci."

    n "Claire grins and leans closer, whispering something in your ear."
    
    show claire sweater leaning suggestive

    claire @ say "Je ne porte pas de culotte aujourd'hui~"
    
    menu:
        claire "{cps=0}Je ne porte pas de culotte aujourd'hui~{/cps}"
        "Quoi?":
            player "What?"
            player "I mean, quoi?"
            
            show claire sweater giggle

            claire @ say "Ksksksks don't worry about it!"
        "Moi non plus":
            n "You flip through the pages of your book to find an appropriate response."
            n "The closest you can find is this."
            
            player "Moi non plus."
            
            show claire surprised earsup
            
            claire @ say "Q-quoi?"
            
            show claire suggestive
            
            claire @ say "Ksksksks tu es tellement drôle!"
        "Montre-moi":
            n "You flip through the pages of your book to find an appropriate response."
            n "Ah, here's a page that shows a similar conversation."
            
            player "Montre-moi."
            
            show claire giggle
            
            claire @ say "Ksksksks retrouve-moi après les cours~"

    hide claire with dissolve
    
    n "You don't really know what just happened."
    n "You shrug and continue your French practice until Mrs. Celestine hands out some homework and dismisses the class."

    show celestine excited at center with dissolve:
        ypos y_celestine

    celestine @ say "Good work class! I can tell you're already making so much progress!"
    
    show celestine neutral
    
    celestine @ say "Keep it up, and do your best on the homework! Some of it may be challenging but I'd like for you to give it your best shot without using translation software!"
    celestine @ say "Passez une merveilleuse journée!"

    stop music fadeout 1.0

    scene bg campus summer day clear with fade

    #play sound "audio/ambient talking.ogg" fadein .5
    play music "audio/music/Vylet Pony - Cozy Pone.ogg"

    show box:
        ypos 0

    show claire sweater happy at offscreenright:
        ypos y_claire
        matrixcolor BrightnessMatrix(0.05)

    claire "[name]! Wait up!!!"

    show claire sweater happy at center with move:
        ypos y_claire

    claire @ say "Do ya wanna come over to my dorm to..."
    
    show claire sweater suggestive
    
    claire @ say "'...study?'"

    n "She says with a wink and playfully nudges you."

    menu:
        n "{cps=0}She says with a wink and playfully nudges you.{/cps=0}"
        "I'd love to!":
            $ frenchSkill += 1
            $ clairePoints += 1
            $ claireFrenchSession = 1
            
            player "I'd love to!"
            
            show claire surprised earsup
            
            claire @ say "Ohmygosh really??"
            
            show claire overjoyed
            
            claire @ say "Let's go then!"
            
            player "What right now? Don't you have chemistry?"
            
            show claire pose suggestive
            
            claire @ say "We can study our 'chemistry' while we practice French~"
            
            n "Wow she's really eager to study."
            n "Claire grabs your hand and rushes you to her dorm."
            
            if avaClaireDormIntroSeen == True:
                scene bg avadorm with fade
    
                play music "audio/music/vylet - I Wish I Could Tell You.ogg" fadein .4
                
                show box with Dissolve(.2):
                    ypos 0
                    
            else:
                call avaClaireDormIntro from _call_avaClaireDormIntro
            
            n "Ava is lying on her bed reading a magazine while listening to headphones."
            n "She turned her eyes over to you when when Claire crashed through the doorway."            
            
            show ava reaching concerned at center with dissolve:
                ypos y_ava
                xoffset -600
                xzoom -1
            
            ava @ say "Heya Claire. You alright?"
            
            show claire sweater happy at center with dissolve:
                ypos y_claire
                xoffset 500
            
            claire @ say "Ava, get out."
            
            show claire sweater leaning suggestive
            
            claire @ say "...unless you wanna join in on this 'study session' [name] and I are about to have."
            
            show ava reaching embarrassed
            
            ava @ say "I'll just uh, give you two some privacy."
            ava "{nw}"
            
            pause .1
            
            show ava with move:
                xoffset 2400
            
            n "Ava grabs her bag and flutters out of the room."
            n "Without hesitation, Claire pins you between her warm soft body and the cold hard wall. She has a crazed look in her eyes and all you've got is your textbook to protect you."
            
            claire @ say "So~ Where did you want to begin~"
            
            player "Um well..."
            player "Chapter 2-2 was giving me some trouble. I can't tell how to pronounce some of these French words that are a jumble of vowels."
            
            claire @ say "Ksksksks you're so adorable, acting committed to the role~"
            
            n "Role?"
            n "Claire seems to think you're roleplaying like the textbook suggests."
            n "You recall a scenario where one of you acts as a tourist in France needing help with the language. You guess you'll play along."
            
            claire @ say "Laisse-moi t'apprendre~"
            
            n "Claire lifts you off your feet and sets you down in a chair. She brushes aside a pair of panties on the desk and slams your textbook down where it was."
            n "You feel something heavy and squishy rest atop your head as she leans over you."
            
            claire @ say "Il fait chaud ici, n'est-ce pas?"
            
            n "You think she's saying something about it being hot? You flip open your book and look around for an appropriate response."
            
            player "Uhh... oui assez chaud."
            
            show claire pose suggestive earsup
            
            claire @ say "Ça te dérange si j'enlève mon pull?"
            
            n "She tugs at the bottom of her sweater, airing out the heat beneath the fabric."
            n "It's becoming difficult to keep track of the conversation as she uses more words you don't know."
            n "She must have been reading ahead."
            n "All you can offer is a basic observation about the sweater."
            ###in later scenes if you've studied more you can say better things
            
            player "C'est un beau pull. Ça te va bien."
            
            show claire flustered
            
            claire @ say "Hrmm..."
            
            n "Claire racks her claws against the table impatiently while thinking."
            
            claire @ say "Il fait tellement chaud que je pourrais m'évanouir! Allons au lit!~"
            
            n "Before you have time to translate, you're hoisted out of the chair and thrown onto Claire's bed, face up."
            
            scene claire pov edited with fade
            
            show box:
                ypos 0
            
            n "In the blink of an eye, the bunny pounces on top of you, thankfully propping herself up on her paws so as to not crush your frail human body."
            n "Without your textbook to protect you, you'll have an even harder time navigating this strange conversation. You're still unfamiliar with the customs of France but Claire seems to be guiding you."
            n "Perhap if you study more in your free time you'll have a better grasp on things."
            
            player "Is this how people normally talk in France?"
            
            claire "...From what I've read, yes."
            claire "Maintenant, ne sois pas si timide~"
            
            scene bg black with dissolve
            
            stop music fadeout 2.0
            
            pause .8
            
            scene bg avadorm with fade
            
            play music "audio/music/vylet - blockhead.ogg" fadein .4
            
            show box with Dissolve(.2):
                ypos 0
            
            n "An eternity passes with you and your study partner frequently changing position and whispering broken French to each other in this hot and sweaty room."
            n "Though the odd body language still confuses you, you feel like you've learned a few new words and grammatical rules."
            n "You've ended up lying on your back with your head in Claire's lap while she strokes your hair."
            n "It's an incredibly soothing feeling. You could fall asleep right here."
            n "You let out a yawn and check the time on your phone."
            
            show claire sweater happy at center with dissolve:
                ypos y_claire

            player "Man, it's getting late. I should get back to my dorm and get ready for tomorrow."
            
            n "You sit up, roll out of bed, and begin collecting your belongings."
            
            player "This was actually kinda fun. Like the whole 'roleplaying in French' thing. And I learned a lot!"
            player "We should do this again sometime!"
            
            show claire sad
            
            claire @ say "...Seriously?"
            
            player "What?"
            
            claire @ say "Nothing... I had fun too."
            
            n "She seems disappointed. Was there something else she wanted to do?"
            
            show claire sweater pose suggestive
            
            claire @ say "Maybe next time we can do something... more fun than studying?~"
            
            n "Ohh she probably means playing video games."
            ###download some french translated games for next time
            
            player "Sure, we can play around next time."
            
            claire @ say "Okay <3"
            claire @ say "Yay <3"
            
            player "See you in class!"
            
            claire @ say "À un de ces quatre!"
            
            hide claire with dissolve
            
            stop music fadeout 2.0
            
            scene bg codadorm with fade
            
            show box with Dissolve(.2):
                ypos 0
            
            n "You didn't mean to bore her with all that school work."
            n "You should download some games on your laptop to bring next time. Maybe you can get some that are translated in French so you can still learn while playing them."
            
            jump thursday1End
            
        "Maybe another time":
            player "Sorry, I have somewhere to be."
            
            show claire sweater sad

            n "Claire looks extremely disheartened."

            claire @ say "Aww..."
            
            show claire sweater derp
            
            claire @ say "It's alright. I'll just uh, see if Ava wants to study with me."

            player "Oh? I didn't know you had any classes together."

            claire @ say "We don't."
            
            show claire happy

            player "Hmm."

            n "What did she mean by this?"
            n "The air around you has suddenly gotten uncomfortable. You're just gonna excuse yourself and go back to your dorm."
            
            player "Alright, time to go. I'll see you in class."
            
            show claire sad
            
            claire @ say "Yeah... See you later."
            
            n "You wave goodbye and turn in the direction of your dorm, purposely avoiding Ava's sight line as she approaches Claire."
            
            jump thursdayNight1Study
            
        "Sorry, I'm not into fat chicks.":
            $ claireBias += 1
            $ calledClaireFat += 1
            $ intoFatChicks = False
            
            player "Sorry, I'm not into fat chicks."
            
            show claire sweater surprised earsup
            
            claire @ say "Wha-?"
            
            show claire sweater sad
            
            claire @ say "Oh, I get it..."
            claire @ say "Forget I asked."
            claire @ say "I'll see you in class, [name]."
            
            hide claire with dissolve
            
            n "Claire sullenly walks off."
            n "Was it something you said?"
            
            stop music fadeout 1.0
            stop sound fadeout 1.0
            
            jump thursdayNight1Study
    
    
label thursdayNight1Study:
    stop music fadeout 2.0
    
    scene bg codadorm with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Back in your comfy zone."
    n "There's enough time in the day left to study a topic before bed."
    #or you could be a slacker and do some leisure activity
    n "What should you study?"
    
    menu:
        n "{cps=0}What should you study?{/cps}"
        "French":
            $ frenchSkill += 1
            n "You pick up your French textbook and practice some lessons."
        "Literature":
            $ literatureSkill += 1
            n "You open your totally legally acquired epub of [currentbook] and start reading."
        "History":
            $ historySkill += 1
            n "You crack open your History textbook and read up on some ancient cultures."
        "Statistics":
            $ statsSkill += 1
            n "You flip open your statistics book and open a calculator app to crunch some numbers."
            
    n "It took a while, but you now feel more confident in your understanding of the topic."
    n "It's gotten late. Time to get ready for bed."
    
label thursday1End:
    scene bg black with dissolve

    n "You do your usual nightly routine and crawl under the blankets to rest until the next day."

    scene bg black with fade

    hide box

    show bg calendar
    show tthursday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

label friday1:
    scene bg codadorm with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "You've made it to the end of your first week back in school."
    n "Just have to get today's classes knocked out, then you'll be free for two whole days."
    
    scene bg campus summer day clear with fade
    
    play music "audio/ambient/outdoors people talking.ogg" fadein .5
    
    show box with Dissolve(.2):
        ypos 0
    
    n "You're blessed with a relatively quick and painless classroom experience and are done with your obligations for the day."
    n "Now you'll have to find some way to occupy yourself for the weekend."
    n "Probably something indoors, at least for now, seeing as how those storm clouds in the distance are fast approaching."
    n "The wind is picking up and you can already see flashes of lightning."
    n "Better hurry to your dorm before it starts raining too."
    
    stop music fadeout 1.5
    
    scene bg codadorm with fade
    
    play music "audio/music/vylet - im sorry (apathy).ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    n "After a long week, you decide you're deserving of some carefree relaxation while the storm rages outside."
    n "At some point you get a text from Gunner."
    
    #hide box
    
    play audio "audio/sound effects/vibrate.ogg"
    
    call phone_start from _call_phone_start_14
   
    call message_start("Gunner", "Heyyyy [name] :3c", "gunneravi.png") from _call_message_start_24 

    call reply_message("What's up") from _call_reply_message_184 

    call message("Gunner", "Just wanted to see if you'd wanna hang out with me and my roommate Rori tomorrow", "gunneravi.png") from _call_message_117
    #gunner "he's gay but dw he's cool"
    call message("Gunner", "I'm bringing bear", "gunneravi.png") from _call_message_118 
    call message("Gunner", "Beer*", "gunneravi.png") from _call_message_119 

    call reply_message("Maybe, if I'm not doing anything") from _call_reply_message_185 
    call reply_message("Where and when") from _call_reply_message_186 

    call message("Gunner", "Meet us atop the literature building after sundown", "gunneravi.png") from _call_message_120 
    call message("Gunner", "There's gonna be a party up there as long as it's not still raining", "gunneravi.png") from _call_message_181 

    call reply_message("wtf that sounds kinda dangerous") from _call_reply_message_187 
    call reply_message("what if we get caught") from _call_reply_message_188 

    call message("Gunner", "Bro don't worry about it I used to do this like every week last year", "gunneravi.png") from _call_message_121 
    call message("Gunner", "It'll be cool trust me", "gunneravi.png") from _call_message_124 

    call reply_message("Hmm") from _call_reply_message_189  
    call reply_message("Am I willing to risk getting hazed for some shitty beer tho") from _call_reply_message_191 

    call message("Gunner", "This isn't like a frat thing this is a \"i wanna hang out and get to know my bros\" thing", "gunneravi.png") from _call_message_147 
    
    call reply_message("how thoughtful") from _call_reply_message_127 
    call reply_message("I'll try and be there i guess") from _call_reply_message_128 

    call message("Gunner", "Alright dude, hope you can make it", "gunneravi.png") from _call_message_182 
    
    call phone_end from _call_phone_end_20
    
    n "That gives you something to do tomorrow if you get too bored."
    n "The hours pass by in leisure until the urge to sleep becomes too hard to resist."
    
    stop music fadeout 1.5
    
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

label rooftop_party:
    # saturday 2
    
    scene bg codadorm with fade
    
    play music "audio/ambient/morning birds.ogg" fadein 0.1    

    show box with Dissolve(.2):
        ypos 0

    n "You've been thinking about this roof party thing Gunner invited you to all day."
    n "You keep flipping between wanting to go or just staying home."
    n "You guess you should try new things while you're here. You've never even had a beer before. Hard to buy when you're only 20."
    n "What's the worst that could happen?"
    n "If you don't like it you can always leave."
    n "Fuck it, you can afford to not be a shut-in for one weekend, right?"

    stop music fadeout 1.0

    scene bg roof with fade

    #play music "audio/Monkey Warhol - Boots & Pants (Instrumental Mix).mp3" fadein .4
    #https://freemusicarchive.org/music/Monkey_Warhol/boots-pants-ep/boots-pants-instrumental-mix

    play music "audio/music/Monkey Warhol - Boots & Pants (Sidekick Wave Instrumental Remix).ogg" fadein .4
    #https://freemusicarchive.org/music/Monkey_Warhol/boots-pants-ep/boots-pants-sidekick-wave-instrumental-remix

    show box with Dissolve(.2):
        ypos 0

    n "Looks like the party's already started. Neon strobe lights highlight flashes of people dancing while obnoxious techno pop music blasts through a low quality bluefang speaker."
    n "Clouds still cover the sky but you don't hear thunder and it hasn't rained all day. You still have to watch out for the puddles from the previous day."
    n "At least, you hope those are just puddles of rainwater and not something else."
    n "You spot Gunner on the other side of the roof and have push your way past a group of people dancing and grinding on each other to reach him."

    show gunner cheeky1 at center with dissolve:
        ypos y_gunner
        matrixcolor BrightnessMatrix(-0.05)

    gunner @ say "[name]!!!! Ya made it!"

    player "Sup Gunner. Nice music."
    
    show gunner neutral

    gunner @ say "Thanks bro! Here, have a beer."

    n "Gunner tosses a can vaguely in your direction. You don't even try to catch it cause his throw was so off that it just goes flying off the side of the building."
    n "A couple seconds later you hear it explode on the concrete."
    
    show gunner cutie

    gunner @ say "Haha woops. Here's another one."

    n "He digs another one out of a cooler and hands it to you."
    
    show gunner neutral

    player "Thanks. Hey, wasn't Rori supposed to be here?"

    show rori concerned at center:
        xzoom -1
        xoffset -475
        ypos y_rori
        matrixcolor BrightnessMatrix(-0.05)
    show gunner neutral:
        xoffset 450
    with move

    n "Rori emerges from the mosh pit, looking dishevelled."
    n "He adjusts his glasses and walks up to you."

    rori @ say "Gunner! I looked away for like two seconds and lost track of you!"
    
    show gunner annoyed

    gunner @ say "Ah there he is. He's been trailing me all night."
    gunner @ say "You know you don't have to be my shadow, right? You're free to mingle with other people. Go make some friends."

    show rori anxious

    rori @ say "M-make friends? How do I do that??"
    
    show gunner determined

    gunner @ say "Bro, relax. Just have a beer and start talkin' to somebody."
    
    show gunner neutral

    rori @ say "I dunno..."

    show rori soyface at hop
    
    pause .15

    rori @ say "Oh but hey [name]! Glad to see you here! How are you liking Harmonia so far?"
    
    show rori neutral
    
    gunner "{nw}"
    
    pause .1

    show rori neutral:
        xoffset -275
    show gunner:
        xoffset 1700
    with move

    ###do transitions where one sprite dissolves away and the other one moves into center view

    player "It's pretty cool. I've never been around so many people so it's taking some time to adjust."

    rori @ say "Same. Usually on a Saturday night I'd be coding some game mods or painting figurines."

    show rori laugh

    rori @ say "But this is kinda exciting!"

    show rori anxious
    
    rori @ say "A little nerve-wracking, but exciting!"

    player "That's good to hear. I guess we're both getting new experiences."

    show rori neutral

    rori @ say "That's what college is supposed to be for!"

    player "So they say."

    n "You take a sip of your beer and Gunner comes back with a new pack."

    show gunner neutral at center:
        xoffset 425
        ypos y_gunner
    show rori:
        xoffset -485
    with move

    gunner @ say "I'm back! Here Rori, take this."

    n "Gunner shoves a can in to Rori's hooves and pushes him back onto the dance floor."
    
    show rori concerned blushing

    rori @ say "Noooo stoppp! I don't know how to daaaaaance..!"
    
    gunner "{nw}"
    
    pause .1

    show gunner neutral at offscreenleft:
        ypos y_gunner
    show rori neutral at offscreenleft:
        ypos y_rori
    with move

    pause .1
    
    n "You look on as Rori disappears into the crowd."

    show gunner neutral at center with move:
        xzoom -1
        xoffset 0 
        ypos y_gunner

    gunner @ say "Sometimes ya gotta push the young ones out of the nest and watch them fly."
    gunner @ say "Enjoying the beer?"

    menu:
        gunner "{cps=0}Enjoying the beer?{/cps}"
        "Yeah":
            player "Yeah man it's great."

            gunner @ say "You don't have to lie bro, I know it tastes like piss."
        "Tastes like piss.":
            player "Tastes like piss."

            gunner @ say "Hahaha I know right!"

    gunner @ say "Want another?"

    n "You shrug."

    player "Sure why not."

    n "You and Gunner stand around and chat with random guests between beers."
    #n "Throughout the night Gunner keeps looking over his shoulder, even though there's nothing behind him other than the edge of the roof."
    
    show gunner frown1
    
    n "Throughout the night Gunner keeps looking up at the sky."

    player "You okay?"

    gunner @ say "Huh? Oh yeah. I'm just like, waiting for someone."

    player "Is it Ava?"
    
    show gunner cheeky1

    gunner @ say "How'd you know???"
    
    show gunner cutie
    
    gunner @ say "Yeah it's Ava. I keep expecting her to fly up any moment now."
    
    show gunner optimistic
    
    gunner @ say "...Aaaany moment now."

    player "Cool, I didn't know you invited her."
    
    show gunner motivated

    gunner @ say "Yeah I climbed her dorm building and taped a flier to her window."
    
    player "Uhh..."

    gunner @ say "She'll swoop down any minute now and I'll offer her a beer and she'll be like 'Teehee thanks!' and we'll totally hit it off."
    
    show gunner neutral

    n "You nod your head and tune out of the delusional words coming out of Gunner's mouth."
    n "He leans up against the wall and rambles on and on."
    n "Eventually he gets on the topic of school."
    
    show gunner displeased

    gunner @ say "...And it's like, okay Dad, I didn't even want to go to college, but then he's like \"You either go and get an education or I ship you off to boot camp.\""

    player "Damn, that's rough."

    gunner @ say "I guess I can't complain too much though. He's paying for me to be here. A lot of people would kill to be in my position."
    gunner @ say "I just"
    gunner @ say "I dunno."
    gunner @ say "He wants me to graduate and be like a marine corp officer or some shit."

    player "He can't control what you do. You're an adult, you can do whatever you want."

    gunner @ say "Yeah but he said he'll cut off my cash flow if I don't go with the major he picked out for me."
    gunner @ say "I'd rather try doing something creative and artsy but he'd disown me if I got \"one of those damn worthless liberal arts degrees.\""

    menu:
        gunner "{cps=0}I'd rather try doing something creative and artsy but he'd disown me if I got \"one of those damn worthless liberal arts degrees.\"{/cps=0}"
        "Maybe he's got a point.":
            player "Maybe he's got a point."
            player "It'll be easier to land a job with a more practical degree."
            
            show gunner itsover

            n "Gunner sighs."

            gunner @ say "I know but that's not-."
            
            show gunner annoyed
            
            gunner @ say "Fuck it, I'm an adult! I can make my own decisions!"
            gunner @ say "I don't wanna work at some corporate hellhole or push papers in the military!"
            #gunner @ say "Fuck working for other people's interests!"
            
        "Maybe get a minor?":
            player "Maybe you could get a minor in something you enjoy?"
            player "Let your father be happy you got your serious big boy degree while you work on your own thing."
            player "That way you'll have a backup to fall back on if you become a starving artist."

            gunner @ say "That could work."
            gunner @ say "...If I wasn't already swamped with studies and failing half my classes."

    gunner @ say "Damn it, I don't wanna even think about it anymore."

    n "Gunner hops up onto the guard rail, balancing on it with feline precision."
    
    show gunner optimistic

    gunner @ say "I'm here to get drunk and find a cute avian girlfriend!!!"

    n "You hear a few cheers from behind you."

    player "Hey, I'll drink to that."

    show gunner neutral

    gunner @ say "Hell yeah [name], I knew you were a bro from the moment I first saw ya!"

    n "You and Gunner throw your heads back and down the rest of your drinks."

    hide gunner with dissolve

    n "You gotta admit, as the night has gone on, you've gradually become more relaxed and stopped worrying about every little thing."
    n "You can just turn off your brain and enjoy the moment for once."
    n "Maybe this is why people drink this stuff."
    n "As you finish off your can, you notice Gunner is missing."

    gunner @ say "Woooooo!"

    player "...Gunner?"
    player "Where'd you go?!"

    n "His voice echoed off the surrounding buildings but he's nowhere to be found."
    n "Holy shit, did he just...?"
    n "You hesitantly peek over the edge of the roof and look down."
    n "A small crowd forms around you, sharing your curiosity."

    stop music fadeout 1.0

    n "\"Oh my gosh, did that guy fall off?\""
    n "\"What the fuck, is he alright??\""
    n "\"Did my boy Gunner just die?\""
    n "Voices from the partygoers drown out your own thoughts but share your sentiment."
    n "\"There he is!\""
    n "Someone points down at a stumbling Gunner as he walks into the glow of a streetlight."

    #show gunner neutral at center with dissolve

    gunner @ say "I'm okay! I landed on my feet!"

    n "The crowd lets out a triumphant cheer and the party goes on like nothing happened."

    play music "audio/music/Monkey Warhol - Boots & Pants (Sidekick Wave Instrumental Remix).ogg" fadein .4

    n "You wave down to Gunner and he waves back but suddenly jumps into some nearby bushes."

    #hide gunner with dissolve

    n "A few seconds later you feel your phone vibrate."

    call phone_start from _call_phone_start_49

    call message_start("Gunner", "oh shit i think the cops are here", "gunneravi.png") from _call_message_start_61
    call message("Gunner", "grab rori and gtfo", "gunneravi.png") from _call_message_321

    call phone_end from _call_phone_end_53

    n "Gotta get out of here before the police bust everyone."
    n "You push your way past the drunken dancers and take Rori's hoof."

    show rori drunk at center with dissolve:
        xzoom -1
        xoffset 0
        ypos y_rori
        matrixcolor BrightnessMatrix(-0.05)

    player "Hey, we gotta go. Now."

    rori @ say "Wha-? But I'm just starting to have fun!"

    stop music fadeout 1.0

    n "Ignoring his complaints, you drag him from the crowd and head down the stairway into the building."

    scene bg schoolhallways with dissolve

    play music "audio/music/Monkey Warhol - Boots & Pants (Instrumental Mix).ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "You peek around corners to make sure the coast is clear before hurrying down the corridors."
    n "Looks like the cops already have the nearest staircase blocked in case someone like you tried sneaking away."
    n "A security guard patrols the area around it but you don't think he saw you. You'll have to make your way to the stairway on the other side of the building."

    show rori drunk at center with dissolve:
        xzoom -1
        xoffset 0
        ypos y_rori

    rori @ say "What the hell man?"

    player "Shh!"

    n "You pull the ram into a dark classroom and put your hand over his mouth."
    n "A moment later you can hear the sound of boots in the hallway."
    n "Rori fidgets in your grasp, trying to escape but you manage to hold him still until it's safe to go."

    player "Sorry about that. Gunner warned me the cops were on their way."
    
    show rori drunk alert

    rori @ say "Wha, for realll?"
    rori @ say "We need to get outta here!!"
    
    player "What do you think I've been trying to do??"

    hide rori with dissolve

    n "You and Rori peek around the corner and commence sneaking away, avoiding the main entrance which was almost certainly guarded by some boomer rent-a-cop."

    stop music fadeout .5

    scene bg campus summer night clear with dissolve

    #play sound "audio/ambient/outdoors night crickets.ogg" fadein .4
    play music "audio/music/vylet - wish.ogg"

    show box with Dissolve(.2):
        ypos 0
    
    show gunner at offscreenleft:
        yalign 0
        matrixcolor BrightnessMatrix(-0.05)
    
    show rori drunk at center with dissolve:
        xoffset 500
        ypos y_rori
        matrixcolor BrightnessMatrix(-0.05)

    n "Once outside, you hear some rustling in the leaves and Gunner appears."

    show gunner neutral at center:
        xzoom -1
        ypos y_gunner
        xoffset -400
    with move
    
    gunner @ say "Bros! You made it out alive!"

    player "Gunner! How'd you survive that fall?"

    gunner @ say "Don't you know cats don't take fall damage? Hahaha!"

    #show rori at shudder

    rori @ say "Shouldn't we have warned the others...?"
    
    show gunner optimistic

    gunner @ say "Nah, y'all woulda got caught up in the mad dash to escape and probably gotten trampled. Happened to me before."

    player "Thanks for the warning."

    rori @ say "Yeah, it probably doesn't look good having underaged drinking and trespassing on your record."

    gunner @ say "Come on, let's get out of here before the cops do a full sweep."
    
    show rori drunk alert

    rori @ say "Hmm..."

    gunner @ say "What's wrong?"
    
    show rori drunk -alert

    rori @ say "I was kinda having fun up there. Shame it had to end so suddenly."
    
    show gunner eyesclosed catface

    gunner @ say "Well..."
    
    show gunner cheeky1
    
    gunner @ say "The night's still young! We can order pizza and play some games."
    gunner @ say "[name], you're more than welcome to hang out at our dorm tonight!"

    player "It's no wild college party, but that sounds pretty nice."
    
    show gunner determined

    gunner @ say "Hell yeah!"

    hide rori
    hide gunner
    with dissolve

    n "The three of you stumble back to the dorms, where you spend a few hours getting dunked on by Rori in various video games."
    
    stop music fadeout 2.0

    scene bg black with fade

    hide box

    show bg calendar
    show tsaturday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

label sunday2:
    scene bg roridorm with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Your head pulsates with the inconvenience of a minor hangover, enough to make your conscious existence miserable."
    n "Looking around, it seems you'd fallen asleep in Rori and Gunner's dorm. They're passed out in their respective beds."
    n "No reason to stick around. You feel groggy and sweaty and gross and you need a shower and some coffee as soon as possible."
    
    scene bg cafe with fade

    play music "audio/music/mere - coffeeLove.exe.ogg" fadein .4

    show box with Dissolve(.2):
        ypos 0

    n "After a shower at your dorm, you made your way to the cafe on campus to get a nice big sobering cup of black coffee."
    n "It's started to pour down freezing cold rain outside, chilling you to the bone even underneath your umbrella."
    n "As you're closing the umbrella and stepping into the cafe, you nearly step on a tiny furry creature."
    
    show rose skirt handonhip annoyed at center with dissolve:
        xoffset -400
        ypos y_rose

    rose @ say "Watch where you're going."

    player "Sorry."
    
    show rose with move:
        xoffset 450

    n "Rose walks past you but stops at the door."
    
    show rose skirt armscrossed dismissive

    rose @ say "Ugh, will this rain ever let up?"
    
    show rose at flipright

    player "Need to be somewhere?"
    
    show rose skirt armscrossed annoyed

    rose @ say "Yeah, anywhere but here."

    player "Didn't you bring an umbrella?"

    n "She silently glares at you."
    n "You'll take that as a no."

    menu:
        n "{cps=0}You'll take that as a no.{/cps=0}"
        "Offer your umbrella.":
            $ goodEnd = goodEnd + 1
            $ rosePoints = + 1
            $ gaveUmbrella = True
            
            n "You can't let her go out in that storm without at least an umbrella."
            n "You hold it out for her to take."

            player "Here."
            
            show rose dismissive

            n "Rose scoffs."

            rose @ say "What, you think I need your generosity?"

            player "No but an umbrella would be nice to have, wouldn't it?"

            n "She looks back to the increasing rain before snatching the umbrella from your hands."
            
            show rose skirt fistsclenched angry

            rose @ say "Tch. Don't think I owe you anything for this."

            player "Wouldn't dream of it."

            hide rose with dissolve

            n "Without even looking back she pushes the door open and walks out into the rain, nice and dry under your umbrella."
            n "You may end up getting drenched later but at least you've done a good deed for the day."
            
        "Don't offer your umbrella.":
            n "Sucks to suck but it's not your problem. Should have came prepared."
            n "You shrug and go about your way. If she wants to act tough, she can stand to get a little wet."

            hide rose with dissolve
            
    show mishka neutral at center with dissolve:
        ypos y_mishka

    mishka @ say "Privyet [name]! Good to see you still yet! Not many customers on days like these."

    player "Hi Mishka! I'm kinda hungover and..."

    mishka @ say "I see. I think I know what you need. I will get you some coffee."
    
    player "Heh, thanks."
    
    hide mishka with dissolve
    
    n "You slump over a table while waiting, listening to the roar of rainfall with the occasional rumble of thunder that shakes the building."
    n "Some moments later, Mishka stops by your table and sets down a ceramic mug filled with rich dark coffee."
    
    show mishka anxious wink right at center with dissolve:
        ypos y_mishka
    
    mishka @ say "Hang in there."
    
    hide mishka with dissolve
    
    n "You mumble a thanks and she returns to her counter where she inspects her potted plants, checking the moisture levels in the soil."
    n "Sitting up, you blow on the steaming hot surface and take little sips brief enough to avoid scalding your tongue."
    n "Odd how a stimulant like coffee can be so relaxing."
    n "Your troubles seem to wash away as you focus on the richness of the drink."
    n "Sadly, all good things must come to an end and this drink is no different."
    
    stop music fadeout 2.0

label sunday2Evening:
    scene bg codadorm with fade
    
    show box with Dissolve(.2):
        ypos 0    

    n "There's still some time to study before you have to go to bed."
    n "What should you study?"
    
    menu:
        n "{cps=0}What should you study?{/cps}"
        "French":
            $ frenchSkill += 1
            n "You pick up your French textbook and practice some lessons."
        "Literature":
            $ literatureSkill += 1
            n "You open your totally legally acquired epub of [currentbook] and start reading."
        "History":
            $ historySkill += 1
            n "You crack open your History textbook and read up on some ancient cultures."
        "Statistics":
            $ statsSkill += 1
            n "You flip open your statistics book and open a calculator app to crunch some numbers."
            
    n "It took a while, but you now feel more confident in your understanding of the topic."
    n "It's gotten late. Time to get ready for bed."    
    
    scene bg black with fade

    hide box

    show bg calendar
    show tsunday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    jump chapter2start
    

    #return
