label chapter1:
    stop music fadeout .5
    
    #scene bg letter

    "You got a letter."
    "The name on the envelope said \"Harmonia University.\""
    "It's rediculous... Could it really be true?"
    "Such a prestegious university wants you...?"
    "You never even applied."
    "Did they send this by mistake?"
    "But it's signed by the dean himself."
    
    "\"Congratulations! You have been admitted to Harmonia University for Fall 2021. We invite you to one of the highest ranked learning institutions in the world to experience a plethora of exciting opportunities!\""
    "\"Our passionate staff will prepare you for a lifetime of success. Join us as you step into the next chapter of your life!\""
    
    "It goes on for a while, full of marketing buzzwords and diversity statistics."
    "There's a note at the bottom."
    
    "\"Given your situation, I would like to personally welcome you and offer you a tour of the campus myself. It would be an honor to have you among us.\""
    "\"I have arranged comfortable living accomodations for you, so that you may focus on getting the most out of your education. Your scholarship will cover all your necessities and then some.\""
    "\"On behalf of Harmonia University, we eagerly await your arrival.\""
    "\"Nicodemus Kaczynski\nDean of Harmonia University\""
    
    "It's strange, but can you really say no?"
    "Might as well go for it. There's nothing left for you at home anymore."
    #there's no reason to stay home anymore
    "Your parents died of that damn disease three years ago. Since then you haven't really done anything."
    "This could be a good opportunity to start fresh."
    
    #your parents died of that damn disease three years ago.
    #yes this bit is just a silent hill 2 reference
    
    scene bg black with fade
    
    "A few weeks later"
    
    ########
    
    scene bg campus_sunny_day with dissolve
    #background names can't have capital letters
    
    show box with Dissolve(.2):
        ypos 0
    
    nicodemus "...that about concludes our tour of Harmonia's campus. What did you think? Not too pretentious, I hope! Bahahaha!"
    nicodemus "I'm reminded of when I was a new student here myself. A bit nervous but so full of wonder and excitement! It felt like anything was possible!"
    nicodemus "Forging lifelong friendships! Making a name for myself in the academic community! Joining clubs and causing a ruckus! Why, I even found love sitting under that cedar tree over there."
    nicodemus "My point is, anybody can blow through four years of university, get their diploma and proceed with their life like it never even happened."
    nicodemus "But I implore you to really make the most of what you've been given!"
    nicodemus "Study hard but take some time to search for something that makes you happy, whether that's being with friends or making your mark on society or just living in the moment!"
    nicodemus "Find what's important to you!"
    nicodemus "Now then, do you have any questions, young lad?"
    
    "To be honest, you weren't really paying attention for the past hour until now."
    "The dean is a short raccoon who wears an old timey but distinguished suit. A pair of small spectacles rests at the edge of his snout. He carries a cane but doesn't lean on it too much."
    "He's like a caricature of a kind old grandpa who tells war stories but leaves the gorey parts out."
    n "He seems like a nice guy and all, but you just can't escape the feeling like you don't belong here."
    
    $ name = "player"
    define player = Character("name", color="#2a2a2a", what_color="#9af3a8", callback=name_callback, cb_name = "player")
    
    $ questionInvite = False
    $ questionFitIn = False
    $ questionTour = False
    $ questionAsked = False
    
    $ questionText = "He seems like a nice guy and all, but you just can't escape the feeling like you don't belong here."

label nicodemusQuestions:
    menu:
        n "{cps=0}[questionText]{/cps=0}"
        "Why did you invite me here?" if questionInvite == False:
            $ questionInvite = True
            
            player "I'm grateful to be here, but I don't understand *why* I'm even here."
            player "I never submitted an application."
            
            nicodemus "We keep tabs on \'persons of interest.\' You know, brilliant young students with bright futures to send ads in the mail to. They make for great alumni."
            
            player "So I'm just here for the optics? For your marketing team to brag about how the college is so diverse it has a human?"
            
            nicodemus "Precisely."
            nicodemus "That is, at least on paper, the official reason for how I brought you on board."
            nicodemus "The actual reason has more to do with..."
            
            "He hesitates, seemingly unsure of what words to use."
            
            nicodemus "You see, your predicament reminded me of an old friend of mine. Are you familiar with the Tasmanian tiger?"
            
            "The dean reaches into his coat pocket and pulls out a photograph."
            
            scene bg tasmaniantiger with dissolve
            
            pause 2.3
            
            menu:
                "What about them?":
                    show box with Dissolve(.2):
                        ypos 0
                
                    "You shake your head."
                    
                    player "Never seen them before."
                    
                    nicodemus "No one has, not for a few decades. At least, not a living specimen."
                    nicodemus "I'm afraid they've gone extinct."
                "They're gone, aren't they?":
                    show box with Dissolve(.2):
                        ypos 0
        
                    player "They're not around anymore, right?"
                    
                    nicodemus "Yes, they went exctinct decades ago. There's not even a color photograph of one."
                    
            "\"Extinct.\""
            "The word sends chills down your spine."
            "You've been trying not to think about it, but that's what your species will be once you die."
            "All that will be left of you are stories and photographs."
            
            scene bg campus_sunny_day with dissolve    
            
            show box with Dissolve(.2):
                ypos 0                
            
            nicodemus "He was a dear friend, someone you could always count on. But as time went on, the burden of being the last of his kind got to him."
            nicodemus "He withdrew himself from everyone and eventually withered away, like some forgotten flower. I'd hate for you to suffer the same fate."
            nicodemus "You see what I'm getting at, don't you?"
            
            "You give a somber nod."
        "Will I fit in?" if questionFitIn == False:
            $ questionFitIn = True
            
            player "I'm not sure I really fit in here. This seems like the kind of university you only get into if you come from old money."
            
            nicodemus "That was certainly true back in the day, but we've been getting more inclusive over the years. We'll take any money now, not just old money heh."
            nicodemus "So don't feel bad if you don't come from the wealthiest household. Money won't buy you honest friends."
            nicodemus "Just treat people with the kindness and respect they deserve and give them a chance. You're bound to find your niche sooner or later."
        "What's with the tour?" if questionTour == False:
            $ questionTour = True
            
            player "A dean like you must be pretty busy. Why'd you take the time out of your day to personally give *me* a tour of the campus?"
            
            nicodemus "Less busy than you'd imagine! I may run the show around here but the show mostly takes care of itself."
            nicodemus "I mostly just sign documents and attend meetings. People look to me for approval, but I'm really just acting as a figurehead most of the time."
            nicodemus "Someone to stand around and look wise."
            nicodemus "The departments handle all the number crunching and recomendations, I just give the final authorization."
            nicodemus "So I don't mind getting out of the office to have a pleasant chat with the students."
            nicodemus "Feel free to break me out of that prison from time to time to talk about whatever's on your mind."
            nicodemus "It's also a great photo opportunity."
            
            "He points to a photographer in the distance, crouched beside a water fountain trying to look inconspicuous with his giant telephoto lens pointed at you."
        "That's all" if questionAsked == True:
            player "That's all."
            
            jump movingOn
    
    $ questionAsked = True
    
    $ questionText = "Was that all you wanted to ask?"
        
    nicodemus "Was that all you wanted to ask?"
        
    jump nicodemusQuestions
        
label movingOn:
    nicodemus "Very well! I'll let you have a break from my ramblings. I believe your orientation is coming up soon. You remember how to get there? Good."
    nicodemus "It was a pleasure to finally meet you in person! You seem like a real stand up guy and I have no doubt you'll find success and whatever else you're looking for during your time at Harmonia!"
    
    player "Thanks. It was nice to be welcomed by the dean himself."
    
    nicodemus "I'm glad I could be of service! Now then, if you'll excuse me..."
    
    "Nicodemus gives you a warm smile before slowly trodding away."
    
    "Even as the sun began to set, the campus was swarming with freshly admitted students either in tour groups or exploring their new surroundings on their own."
    "You don't have much time to spare, so you make your way to the building where your scheduled orientation is soon to take place."

label college_orientation:
        #ACT 1
    #___saturday1

    play sound "audio/sound effects/door opening.wav"

    scene bg lecturehall with fade

    show box with Dissolve(.2):
        ypos 0

    play music "audio/ambient/indoors people talking.ogg" fadein 1.5
    
    
    #n "You had some trouble finding the building you're supposed to be in but managed to make it just in time."
    n "After checking in, you were directed to a lecture hall where several others are already seated and chatting amongst themselves."
    n "You look around for an open spot and find one near the front of the room."
    n "Weird looks are shot in your direction, followed by whispers as you walk past. They act like you don't notice their stares and comments."
    n "You're used to it though, it happens everywhere you go. Understandably so, considering your kind is about as rare as a unicorn."
    n "Is this what college is? It already feels like a prison."
    n "You slump down in your seat and try to ignore the world around you, praying that this will be over with quickly."
    #n "You slump down in a seat and try to astral project into the future, if only to get away from here."
    #n "It's not working."
    n "Eventually a woman walks up to the podium and the voices around you quiet down."

    show ellen teacher neutral at norm with Dissolve(.5)

    stop music fadeout 2.0

    ellen @ say "            Ahem            "

    show ellen teacher happy

    ellen @ say "Welcome to Harmonia University, new students! My name is Margaret Ellen and I'm very excited to introduce you to the next chapter of your lives!"
    ellen @ say "This orientation marks the beginning of your journey into the finest acadamia has to offer! Everything you'll learn and experience over the next four years starts here."

    hide ellen
    with dissolve

    n "You start to tune out of what she's saying. It's just boring introductory formalities anyway."
    n "You hear the door open, followed by hoofsteps coming down the stairs. Must have been a straggler who arrived late."
    n "The room's pretty full but there's another vacant seat next to yours."
    #n "Please deer god, you pray whoever it is doesn't sit there. You've had a rough day and don't want to have to make friends already."
    n "A moment later, a nerdy looking ram squeezes past you and sits in it."

    #show rori neutral at norm with moveinright:
        #xpos 600
    
    #pause .25

    #rori @ say "D-did I miss anything?"

    #player "Nope"
    #n "You snap out of your daydream and shake your head before returning your attention to the presenter."
    #n "You shake your head and return your attention to the presenter."
    
    #player "Nope."

    #hide rori with dissolve

    show ellen teacher neutral at norm with dissolve

    ellen @ say "...If you haven't already, go ahead and introduce yourselves to those sitting around you!"
    ellen @ say "Go on, don't be shy!"

    hide ellen with dissolve

    play music "audio/ambient/indoors people talking.ogg" fadein 1.5

    show rori neutral at norm with dissolve:
        xpos 600

    rori @ say "Hey um... Gosh, I don't know how to do this."
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
                name = "Coda"
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

    rori @ say "Nice to meet you too!"
    rori @ say "..."
    rori @ say "So... uhhh..."
    rori @ say "What are you majoring in?"
    
    n "Wow, no 'Are you really a human? I thought your kind went the way of the dinosaurs!' like you've heard countless times."

    player "I haven't really decided yet. Thought I'd figure it out while I'm here. What about you?"

    show rori laughing

    rori @ say "Computer engineering! I've always loved messing around with computers. I taught myself how to program since my high school didn't have any classes for it."

    menu:
        rori "{cps=0}Computer engineering! I've always loved messing around with computers. I taught myself how to program since my high school didn't have any classes for it.{/cps}"
        "Hahaha nerrrrd":
            $ roriPoints = roriPoints - 1

            show rori neutral

            player "That stuff's a bit too nerdy for me."

            rori @ say "Oh... that's understandable. It's not for everyone."

            player "It requires a lot of math knowledge, doesn't it?"

            rori @ say "Sorta? I mean it helps to have a solid understanding of algebraic equations and trigonometry."

            player "Ugh, spare me the details. Please."

            show rori laughing

            rori @ say "Hahaha okay! It's actually pretty routine until you come across a bug, then it's like solving a puzzle."

            player "Never been good at puzzles."

            show rori neutral

            rori @ say "Then computer engineering isn't for you."

            player "I'll cross that one off the list."

        "Play any games?":
            $ roriPoints = roriPoints + 1
            
            show rori neutral

            player "You play any games? I got really into World of Boarcraft a few years ago."

            rori @ say "I love World of Boarcraft! I used to skip school all the time just to play it."

            player "Not recently, I hope. The newer expansions kinda turned that game into hot garbage."

            rori @ say "Yeah... Still, I used to dream of making games like that."
            rori @ say "I started out learning to write scripts to make the mundane parts of the game easier, then I got banned when I figured out how to edit hex values to give myself infinite gold."

            player "Making games would be pretty cool. I've always had ideas but never the skills or willpower to actually make anything. It seems like it would be really hard."

            rori @ say "Oh you bet it is. I've messed around with some game engines before and it can quickly get overwhelming."
            rori @ say "I've got something I've been working on for a few years. I hope I can still work on it here but I heard my compsci professor likes to assign a lot of homework."

            player "Damn. Well good luck with that."

            show rori laughing

            rori @ say "Thanks! I'll need it!"

        "At least you know what you wanna do.":
            show rori neutral

            player "That's cool. At least you know what you wanna do."

            rori @ say "Haha thanks but I'm actually not sure about that. It's a pretty broad field and I don't exactly know where I'm gonna end up."

            show rori anxiety

            rori @ say "I wouldn't wanna end up administrating some boring office's network, ya know? I got into computers cause I wanted to live in like a science fiction world."

            player "Yeah? Boring office work can be good money though."

            show rori neutral

            rori @ say "I guess it's not really about the money for me. Don't get me wrong, money's nice and all but I'd rather make my dream game or develop an AI companion or something cool like that."

            player "I get what you mean. I'm just here to figure out what I'll enjoy doing for the rest of my life."
            
            rori @ say "No plans huh? Well I hope you can figure something out sooner than later!"
            
            player "Thanks, me too haha."

    n "You chat with Rori for a bit longer until Ms. Ellen clears her throat and gets the rooms attention."

    hide rori with dissolve

    show ellen teacher neutral at norm with dissolve

    stop music fadeout 2.0

    ellen @ say "Ahem. Now that you've become acquainted with your neighbors, I'd like to know more about you!"
    ellen @ say "I'll pick a few students at random... Please say your name, what you're majoring in, and something about yourself."

    n "Ms. Ellen points to a girl toward the back of the room."
    
    show ellen teacher happy

    ellen @ say "You there! With the camera!"

    hide ellen with dissolve

    show ava normal neutral at norm with dissolve
    
    #ava says she's a bird photographer




































    
    return
