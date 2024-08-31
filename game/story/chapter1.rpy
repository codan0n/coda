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

    show rori neutral at norm with moveinright:
        xpos 600
    
    pause .25

    rori @ say "D-did I miss anything?"

    player "Nothing important."
    #n "You snap out of your daydream and shake your head before returning your attention to the presenter."
    #n "You shake your head and return your attention to the presenter."
    
    hide rori with dissolve

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

    $ calledRoriNerd = False

    menu:
        rori "{cps=0}Computer engineering! I've always loved messing around with computers. I taught myself how to program since my high school didn't have any classes for it.{/cps}"
        "Hahaha nerrrrd":
            $ roriPoints = roriPoints - 1
            $ calledRoriNerd = True

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
    
    ava @ say "Um hi...! My name's Ava and, as you might have guessed, I'm a photography major! I often go out into nature and shoot wildlife and landscapes, but I also dabble in street photography."
    
    show ava excited at hop
    
    ava @ say "I like the idea of capturing rare moments in time that disappear as quickly as they come."
    #ava @ say "I like the idea of capturing the rarely seen or overlooked aspects of life!"
    ava @ say "Umm, I don't know what else to say? I just kind of like experimenting and finding new ways to view things."

    hide ava with dissolve

    show ellen teacher neutral at norm with dissolve

    ellen @ say "Very good! Next, how abouuuuutttt..."
    
    show ellen with move:
        xpos -175
        
    pause .3

    show ellen teacher neutral at flipright
    
    pause .3
    
    show ellen with move:
        ypos 0
        xzoom -1
        xpos 110
        
    pause .4
    
    ellen @ say "You, in the pink sweater!"

    hide ellen with dissolve

    show claire sweater surprised at norm with dissolve:
        xpos 0

    claire @ say "        Moi?        "
    
    show claire sweater derp
    
    claire @ say "Hiiiii, my name's Claire and I left my major undecided cause, well, I couldn't decide what to do!"
    
    show claire sweater wave
    
    claire @ say "Something interesting about myself? I was a cheerleader in high school until I broke my leg, and then I joined the chess team and found out I'm actually pretty good at it??"
    
    show claire sweater overjoyed 
    
    claire @ say "I got to go to a national tournament once and came in third place!"
    claire @ say "It was fun but I'm always looking for new things to try!"

    hide claire with dissolve

    show ellen teacher neutral at norm with dissolve:
        xzoom -1
        xpos -50

    ellen @ say "Nicely done! We'll do a couple more. Let's see..."

    show ellen teacher neutral at flipleft
    
    pause .6

    ellen @ say "Hmm..."
    ellen @ say "How about you!"

    n "Of course she had to pick you. You pretend to think she's pointing at someone else."

    ellen @ say "Yes, you! We don't bite, I promise!"

    n "You let out a quiet sigh and rise from your seat."

    player "Hi, my name's [name] and I'm also an undecided major, mostly for the same reason. I guess something that's interesting about me is that I'm the last human on Earth."
    player "Which is probably the reason I got accepted here with a full scholarship, cause it sure wasn't my grades."

    show ellen teacher melancholy

    n "That gets a few chuckles from the room, but Ms. Ellen just glares at you."

    ellen @ say "Yes well... very good, thank you [name]. Moving on."
    
    show ellen teacher neutral

    n "Ms. Ellen gives a few more announcements before wrapping up her speech and dismissing you all."

    ellen @ say "I hope you all have a wonderful time at Harmonia! That's all I have for you! You're free to go! Have a nice rest of your evening!"

    hide ellen with dissolve
    
    play music "audio/ambient/indoors people talking.ogg" fadein 1.5

    n "It's about time. You were starting to doze off."
    n "Now that that's out of the way, you can return to your dorm and get your things put away."
    #n "When you arrived earlier today, the dean himself greeted you and showed you to your dorm, no doubt a gesture mandated by the affirmative action council."
    #n "When you arrived earlier today, the dean himself greeted you and personally showed you to your dorm, no doubt to make you feel more welcome given your situation."
    #n "You can't help but feel it was an empty gesture though. He made sure to get you a room all to yourself, as if that wouldn't make you feel more alone."
    n "On your way out, you overhear some familiar voices."

    show ava normal neutral:
        xpos 485
    show claire sweater wave at norm:
        xzoom -1
        xpos -350
    with dissolve

    claire @ say "Hey! Cool camera! Is that a nifty fifty on it?"
    
    show ava portrait neutral

    ava @ say "Thanks! I never leave home without it! Fifty millimeter is just so versatile!"

    show claire sweater neutral

    claire @ say "What dorm are you in? I'm in Saint Mary Hall."
    
    show ava normal neutral

    ava @ say "No way! I'm in there too! What room number?"

    claire @ say "209A!"
    
    show ava excited

    ava @ say "Me too!!!"

    claire @ say "Oh my gosh this is perfect! We're gonna become best friends ksksksks!"

    hide ava
    hide claire
    with dissolve

    n "Thank goodness they finally decided to move out of the way. The bunny alone was blocking the double doors leading outside."

    scene bg campus with dissolve

    play music "audio/ambient/outdoors night crickets.ogg" fadein 1.5

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

    show rori neutral at norm with dissolve

    rori @ say "Hey! [name]!"
    rori @ say "Leaving already?"

    player "I don't really have a reason to stick around, do I?"

    rori @ say "Where's your par-"

    show rori anxiety

    rori @ say "...Oh. Sorry."

    #n "You just look at him the same way a janitor would look at a child who was projectile vomitting across three tables in the cafeteria."

    show rori neutral

    rori @ say "A-anyway...! I'm staying in Edgar Hall! What dorm do you live in?"

    player "I'm over in Swanson."

    rori @ say "Ah, I heard that's the rich people's building."

    player "Rich or endangered."

    rori @ say "Hah, yeah I guess..."

    pause .3
    show rori neutral at flipright
    pause .95
    show rori neutral at flipleft

    n "Rori looks around, seemingly unsure of what to say."

    show rori anxiety at shudder

    #rori @ say "M-my parents didn't come either... They just bought me a plane ticket and told me to come back with a degree or don't come back at all."
    rori @ say "M-my parents didn't come either... They just bought me a plane ticket and told me not to contact them until I had a PhD."

    #n "You didn't ask but whatever."

    player "Wow, that's uh... tough."

    show rori neutral

    rori @ say "They just want to see me succeed. I'd probably live in their basement playing games for the rest of my life if they didn't force me out."
    rori @ say "But I am actually really excited to have some freedom for once now that I'm no longer under their supervision!"

    player "That's a good attitude to have."

    show rori laughing

    rori @ say "I guess so!"

    show rori neutral

    rori @ say "Well, I guess I'll see you around. I have to unpack my desktop and run some updates."
    
    show rori anxiety
    
    rori @ say "I haven't had it online in over 48 hours. I hope my package manager doesn't break my xorg session again..."

    if calledRoriNerd == False:
        menu:
            "Need some help with that?":
                $ roriPoints =+ 1
            
                player "Need some help with that?"
                
                n "Rori thinks for a moment before answering."
                
                rori "Hmm... I usually don't have people over but..."
                rori "When else am I gonna get a chance to show off my riced out minimal window manager setup?"
                rori "We can play some games and stuff too."
                
                player "Lead the way."
                
                call roriDormIntro
                
                player "Do you have a roommate? I get the feeling those aren't yours."
                
                n "You point to a dumbells in the corner."
                
                player "Plus the whole bunk bed setup."
                
                rori @ say "Hm? Oh yeah, those are my jock roommate's. He's a sophomore so he didn't have to do the orientation today."
                rori @ say "He's probably out at some party right now, I dunno."
                
                player "Probably crushing pussy while we hook up a gaming computer."
                
                rori @ say "Now lets see if this works. I'm a bit worried about my SSD's firmware acting janky after the last update."
                        
                n "Rori goes over to the desk and hooks up a few wires to the desktop tower. When he presses the power button, a rainbow of LEDS shine through the glass panel of the case."
                n "A moment later, the monitor wakes up and a stream of debug messages scrolls across the monitor."
                n "It stops and prompts him to enter a password. You avert your eyes out of respect for his privacy."
                n "Yet you can't help but notice the rapid fire clattering of his mechanical keyboard goes on for half a minute before he presses the enter key."
                
                player "Damn, your password must be longer than the Pentagon's. What you hiding on that hard drive?"
                
                n "Rori pushes up his glasses and smirks."
                
                rori @ say "16 terabytes of anime bluray rips, 4.5 terabytes of games, 750 gigabytes of jpop, and a couple gigs of source code."
                
                player "All legally acquired?"
    
                rori @ say "Legal in my VPN's host country!"
                
                player "Nice."
                
                rori @ say "Oh what the hell is this?"
                rori @ say "Error: Cryptsetup couldn't resolve device. /dev/nvme0n1p3 is not a valid LUKS device."
                rori @ say "It was working fine 2 days ago."
                
                player "RIP."
                
                rori @ say "Ugh, I'm gonna have to load up a live CD and chroot into this and dig around to find the problem."
                
                player "Average linux boot process."
                
                rori @ say "Haha yeah... Sorry about this but I doubt I'll be able to get this running tonight."
                
                player "Does this mean no games?"
                
                n "Rori looks down sadly."
                
                rori @ say "No games."

                player "What about that?"
                
                n "You point to a console shoved under the desk."
                
                rori @ say "The PS3? I use it as a blueyray player."
                
                player "Doesn't it play games too?"
                
                rori @ say "What games?"
                
                player "Damn, you're right."
                
                rori @ say "I'll have this computer fixed and ready to go next time, I swear. I think something might have gotten corrupted during transport."
                
                player "It's alright. It's pretty late and it's been a long day anyway. I'm just gonna go to my dorm and sleep."
                player "See you around, dude."
                
                rori @ say "Laters!"
                
                jump playerDormOrientationDay
                
            "Have fun with that.":
                player "Have fun with that. Later."
                
                jump afterRoriOrientationDay
    else:
        player "Have fun with that. Later."
        
        jump afterRoriOrientationDay

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

    n "You can't entirely recall how you got here but you made it."
    n "Home sweet home for the next four years."
    n "You had packed as much from home as you could carry in your suitcases but haven't had a chance to unpack yet."
    n "It'll have to wait until tomorrow. You're way too tired to bother with it right now."
    n "Without even bothering to kick off your shoes, you flop directly onto your bed and instantly fall asleep."

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show tsaturday at norm
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7
    
    #___sunday1

label exploring_campus:
    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    play music "audio/ambient/morning birds.ogg" fadein 0.1

    n "It's already around noon by the time you wake up."
    n "Luckily classes don't start until tomorrow, so you can get away with sleeping in. For now."
    n "You'll have to sort out your sleep schedule the painful way soon."
    n "However, your primary concern at the moment is the breakfast situation."
    n "You've subsisted on nothign but granola bars during your journey to Harmonia, and it's high time you got a warm meal."
    n "You roll out of bed and take a quick shower, impatiently doing the bare minimum to make yourself presentable before heading out to find some food."

    stop music fadeout 1.0

    scene bg campus with fade

    play music "audio/music/vylet - there.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "It's a bright and sunny day with students bumbling about... {i}socializing{/i}, as if their normie instincts extract vital nourishment from it."
    n "You unfortunately stumble into what must be the hub of social activity on campus today: club registration."
    n "Booths line the street with banners advertising the different clubs and organizations the university has to offer."
    n "There's one for the botany club, debate club, algae bee tea club,  {a=https://4chan.org/trash/hmofa}/hmofa/{/a} club, anime club, vidya club, golf club, and so on."
    n "Going straight across is the quickest way to the restaurants, so you head in with your eyes forward."
    n "You know the moment you look at any of them, some representative will drag you into an involuntary conversation."
    
    $ metGunner = False
    $ metClaire = False
    $ metAva = False
    
    $ randumb = renpy.random.randint(0, 1)
    
    #for testing
    #n "random number is [randumb]"
    
    if randumb == 0:
        $ metClaire = True
        n "You almost managed to get to the end without being harassed by anybody."
        n "Surprisingly it wasn't a booth attendant, rather it's the chatty girls you saw the day prior."
        
        show claire sweater neutral at offscreenright:
                yalign 0
        show ava normal neutral at offscreenleft:
            yalign 0

        show claire sweater neutral at norm:
            xalign 0
            xpos 400
        show ava normal neutral at norm:
            xalign 0
            xzoom -1
            xpos -400
        with move

        claire @ say "Holy Frith, it's you! You were at the thing last night, weren't you?"
        
        show ava bored

        ava @ say "She means the orientation."
        
        show ava normal neutral

        player "Nope, you must have me confused for the other human around here."

        n "Ava smirks at your joke but Claire seems to take a second to get it."

        claire @ say "Oh..."
        
        show claire sweater surprised
                    
        claire @ say "Oh!"
        
        show claire sweater embarassed
        
        claire @ say "Duh!"
        
        show claire sweater wave
        
        claire @ say "What was your name again? [name]?"

        player "Yeah. And you were... Ava and Claire, right?"
        
        show ava excited

        ava @ say "Yup!"
        
        show claire sweater neutral
        show ava normal neutral
        
        claire @ say "So what brings you out here, [name]? Looking to join a club?"

        player "More like looking for a place to get breakfast, but I ended up here somehow."

        ava @ say "One booth was giving out free donuts but they ran out pretty quick."

        player "Aww..."

        claire @ say "I guess you could say the early bird gets the donut~"
        
        show ava portrait neutral
        
        ava @ say "Hehe you're not wrong!~"
        
        show ava normal neutral

        player "So have you signed up for anything so far?"

        claire @ say "I looked into a bunch but I can't decide which one to join!"

        ava @ say "I just went for the obvious one and joined the photography club. Thinking about signing up for the cinematography club too. What about you?"

        player "I'm not really interested in any of them."
        
        claire @ say "*gasp* We should all join a sorority!"
        
        ava @ say "What? Why?"
        
        player "I don't think they'd let me in."
        
        claire @ say "Why not? It's current year!"
        claire @ say "We can hit on sorority sluts! Ksksksksks!"
        
        ava @ say "Pass."
        
        claire @ say "Aww, you're no fun."
        claire @ say "What about you, [name]?"
        
        menu:
            "Yah":
                $ clairePoints =+ 1
                
                player "You know what, sure, sign me up."
                player "Should be funny when they realize I'm not a girl and kick me out."
                
                claire @ say "No way, you could totally pass for a girl with a little makeup!"
                
                player "Uh, thanks..."
                
                #claire @ say "That's the spirit!"
                
                player "You handle the forms though, I have to run."
                
                n "Ava rolls her eyes while Claire squeals in excitement."
                
                claire @ say "Eeeeeee it's gonna be so fun! Ava you're gonna regret not joining!"
                
                ava @ say "If you say so. We'll see you around, [name]!"
                
                player "Yeah, later guys."
                
                claire @ say "Byeeeee!!!"
                
            "Nah":
                player "Nah."
                
                claire @ say "Can't a bun have a little fun?"
                
                ava @ say "No one's stopping you from joining on your own, you know."
                
                claire @ say "But I'll be lonely ;^;"
                
                ava @ say "Isn't the point of joining one so you *won't* be alone?"
                
                claire @ say "I wanna be around my friends though."
                
                ava @ say "Then make some in the sorority!"
                
                claire @ say "But what if they don't like me?"
                
                ava @ say "Oh trust me, I think you'll fit right in."
                
                claire @ say "Really?"
                
                n "Claire looks to you sympathetically."
                n "Your stomach is roaring, demanding that you escape this mundane conversation and go find sustenance."
                
                player "Yeah you'd make a great sorority girl. Lemme know how it goes, I have to run for now."
                
                n "Claire quits pouting and instantly brightens up."
                
                claire @ say "Sure! See you around, [name]!"
                
                ava @ say "Later!"
                
                #n "You wave goodbye to them and hurry away before someone else distracts you from your mission."
        
        hide ava
        hide claire
        with dissolve
        
    else:
        $ metGunner = True
        n "You almost made it to the end without getting poached by some aggressive salesman."
        
        show gunner neutral at norm with dissolve

        gunner @ say "Hey there! I saw you checkin' out the frats and thought you should know Alpha Alpha Alpha is the best one!"
        
        player "I actually wasn't and I don't really care about fraternities."
        
        gunner @ say "That's just the sort of thing an Alpha would say!"
        
        player "I personally identify as a sigma male but okay."
        
        gunner @ say "No worries, we like totally respect your pronouns or whatever. Name's Gunner by the way!"
        #gunner @ say "No worries, we like totally respect your pronouns or whatever stupid bullshit you believe in. Name's Gunner by the way!"
        
        player "[name]. Now if you'll excuse me."
        
        gunner @ say "The strong stoic type, I see! You'd fit right in!"
        
        n "Gunner steps in front of you and blocks your path, waving a clipboard and pen in your face."
        
        gunner @ say "So what do you say? Are you a bad enough dude to join?"
        
        player "Not particularly."
        
        n "You attempt to maneuver around the cat only to bump into someone else."
        
        show rori neutral:
            xzoom -1
            xpos -400
        
        rori @ say "Oh, hello again [name]!"
        rori @ say "I see you've met my roommate."
        
        gunner @ say "Rori! I'm begging you, join my frat!"
        gunner @ say "If I don't get enough new recruits, they're gonna duct tape me to the ceiling again!"
        
        rori @ say "Hrm... already doesn't sound like it's for me."
        rori @ say "What do you even do in a frat?"

        gunner @ say "Let's see, we uh... haze new members, drink cheap beer, hit on sorority chicks, play sports..."
        
        rori @ say "Right... I don't think any of that appeals to me."
        
        gunner @ say "There's also a bunch of hot guys and stuff."
        
        rori @ say "Wha-? I-I don't see what that has to do with anything!"
        
        gunner @ say "Come on dude, I saw the kind of anime you watch."
        
        rori @ say "..."
        
        n "Rori tenses up but doesn't say anything. He's like a deer in headlights, except he's a ram and the headlights are an accusation of being gay."
        
        menu:
            "Which anime?":
                player "Which anime was it?"
                
                gunner @ say "The one with all the buff dudes with ghosts that punch really fast and are also buff dudes half the time."
                
                player "Jojo's Weird Adventure?"
                
                n "Rori nods his head."
                n "Damn, you thought you could defend him but that one is undoubtedly pretty gay."
                
                gunner @ say "Hahahaha if that's your type there's plenty of jacked Alpha guys. They practically live at the gym."
            "Lay off him, dude":
                $roriPoints =+ 1
                
                player "So what? Lay off him, dude."
                
                n "Gunner puts his paws up innocently and scoffs."
                
                gunner @ say "Relax, it's just a bit of banter."
                gunner @ say "Seriously though, some Alphas are jacked. They practically live at the gym."
                
        rori @ say "Thanks for the offer but I'm more into... sensitive guys I guess?"
        
        gunner @ say "Like... feelings? Yeah I dunno if they're good at that."
        gunner @ say "Look, can I just put your names down? You don't have to show up but the more people who sign on, the more money we get."
        gunner @ say "You'll get access to benefits like sports tickets and exclusive parties and stuff. Oh and we have monthly game tournaments!"
        
        n "That last part caught Rori's attention."
        
        rori @ say "Tournaments? What do you play?"
        
        gunner @ say "Usually the yearly Call of Battlefield: Modern Football but sometimes someone will bring in some weird ass Japanese game none of us have ever heard of hahaha!"
        
        n "Rori looks disappointed then shrugs."
        
        rori @ say "Fine, whatever. At least I can probably sell the sports tickets."
        
        gunner @ say "Sweet! Just sign here! And if I come across any uhh... emotional guys? I'll send them your way!"
        
        rori @ say "Suuuure..."
        
        gunner @ say "What about you? You down?"
        
        menu:
            "Join":
                player "Yeah but only for the free stuff."
                
                n "You take the clipboard and lazily scribble your name somewhere on it."
                
                gunner @ say "Yes! You won't regret it!"
                
                n "Gunner holds out his fist."
                n "As is customary, you are forced to give him a fist bump."
                
                player "I better not."
            
            "Don't join":
                player "Nah, I'd rather not."
                
                n "Gunner's ear flicks in annoyance."
                
                gunner @ say "Suit yourself."
                
        player "Now if you're done wasting my time, I have breakfast to catch."
                
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
    n "After giving it a lookover, you decide what you want and walk up to place your order."

    show mishka neutral at norm with dissolve

    mishka @ say "Privyet, welcome to Coffee Zona..."
    
    #show mishka derp
    
    mishka @ say "...er, Zone!"
    
    show mishka neutral
    
    mishka @ say "How can I help you?"
    
    menu:
        "Why are the lights off?":
            player "Why are the lights off? Is the shop open?"
            
            mishka "It's just how I like things. I can turn the lights on if you like."
            
            menu:
                "Please do":
                    player "Please do. I can't see anything in this darkness."
                    
                    mishka @ say "Very well."
                    
                    n "The barista clenches her eyes shut as she puts a claw to the light switch."
                    n "When the lights come on, she winces and slowly opens her eyes."
                "Leave them off":
                    player "It's fine, you can leave them off. It's comfier this way."
                    
                    #mishka @ say ""
        "Place your order":
            player "Yeah can I get uhh...."

    n "You give the barista your order and swipe your card on the machine."

    mishka @ say "And can I get a name for you?"
    mishka @ say "Not that I really need it since we're the only ones in here."
    mishka @ say "But it would be nice to have irregardless."

    player "      [name].      "

    mishka @ say "Alright [name], I'll have your order ready for you soon!"

    player "Thanks uhh..."

    n "You look down at her nametag."
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

            mishka @ say "Yup! Not many Mishkas around here, are there?"

            player "Nope, you're the first I've ever met. Then again, I did just move here."

            n "She begins working on your order while continuing the conversation."

            mishka @ say "Oh? Are you new student?"

    player "Yeah. Can't decide what to major in though."

    mishka @ say "It can be tough choice to make. I wouldn't stress about it though, most people find something after semester or two."

    player "I sure hope so. I wasn't really planning on going to college in the first place, but I also wasn't planning on not going, you know?"
    player "But now I'm here and I still don't know what I'm doing."

    mishka @ say "Many students feel same way. Life can be that way sometimes. You just have to make the best of it while you're here."
    mishka @ say "For now, enjoy coffee and blini!"

    n "Mishka hands you a steaming hot cup and a box."

    player "Thanks! And I appreciate the advice!"
    
    show mishka overjoyed

    mishka @ say "Nyema problyema! Come back soon, it gets pretty lonely here!"
    
    show mishka neutral

    player "For sure!"

    hide mishka with dissolve

    pause .3

    stop music fadeout 1.0

    scene bg campus with dissolve

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
    show tsunday at norm
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

label firstDayOfClass:
    scene bg codadorm with fade

    play music "audio/ambient/morning birds.ogg" fadein 1.5

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

    play music "audio/music/mere - schooldaze.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0

    n "You vastly overestimated your ability to get around campus quickly and arrive ten minutes late to your history class."
    n "All eyes are on you as you bust through the doorway."

    show rothbauer at norm with dissolve

    rothbauer @ say "Ah, nice of you to join us. You must be [name]."
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
    
    show rose neutral at norm with dissolve:
        xzoom -1
        xpos -400
    
    rose @ say "    Psh.    "
    rose @ say "     No.     "

    n "She scooches her desk away from you and faces the other way."

    show rose with move:
        linear .54 xpos -510
    pause .15
    show rose with move:
        linear .54 xpos -750
    pause .33
    show rose with move:
        linear .54 xpos -1700

    n "Damn, maybe you came on too strong."
    n "You try partnering up with some others but it seems everyone's already established their own group."
    #n "You try partnering up with some others but as usual you get ignored."
    n "You take another look at that raccoon girl. She didn't even attempt to talk to any of the other students. She's just staring out the window."
    
    show rothbauer at norm with dissolve

    rothbauer @ say "Hopefully everyone's found a group by now."

    n "Mr. Rothbauer asks who everyone is partnered with and jots it down in a notebook while you silently panic."

    rothbauer @ say "[name], what about you? Who's group are you in?"

    player "Err, I couldn't find one..."

    rothbauer @ say "Oh? Does the class not divide evenly? Hah, this is why I'm a history teacher and not a math one!"
    rothbauer @ say "Does anyone else not have a partner? What about you, Miss Kaczynski, who's group are you in?"

    show rothbauer with move:
        xpos 250
        
    show rose neutral at norm with dissolve:
        xzoom -1
        xpos -550

    rose @ say "...Nobody's."
    rose @ say " And just call me Rose."

    rothbauer @ say "Very well, Rose, you and [name] can be a group of two then!"
    
    show rose unimpressed

    #rose @ say "Ugh. Do I have to?"
    rose @ say "I can do the assignment on my own."
    
    rothbauer @ say "I'm sure you could, but that's not the point of this exercise. It's important for students to learn how to work with others, like in a real work environment!"
    rothbauer @ say "I'll be checking in from time to time with each student to monitor each individual's progress and contributions to the project, so please make sure everyone in your group is pulling their weight."
    #rothbauer @ say "It's a great exercise in leadership and compromise that will serve you more in the long run than any history knowledge."

    rose @ say "Fine, whatever."
    
    rothbauer @ say "Good! I'll put you and [name] into your own group then."

    n "While Rothbauer writes your names in his notebook you hear crumpling paper beside you."
    
    show rose furious
    
    n "You glance towards Rose and see her clenching her fist, balling up a sheet of paper."
    n "She turns to you and mutters something."

    rose @ say "To hell with that. I'll do it all on my own."

    hide rose with dissolve
    
    show rothbauer with move:
        xpos 0

    rothbauer @ say "Ahem well... now that that's settled, let's begin our first lesson!"
    rothbauer @ say "This course and the follow up World History II are designed to give you an understanding of how civilization has progressed alllll the way back from when the dinosaurs roamed the earth..."

    n "Mr. Rothbauer circles a crude drawing of a pterodactyl on the chalk board and starts drawing an arrow pointing to some stick figure people."

    rothbauer @ say "...to the rise and fall of humanity, leading into the current era, Societas Animalium, that is 'Society of Animals' as they say."
    rothbauer @ say "Of course, not much is known about how the dinosaurs lived since a meteor striking the planet destroyed nearly every bit of evidence they were here at all!"
    rothbauer @ say "The world was buried under a blanket of smoke and ash, smothering their existence. It took millions of years before a civilization was able to form again."
    rothbauer @ say "But what if I told you that we are not so different from the dinosaurs?"
    rothbauer @ say "This... goes a bit against the curriculum but the evidence is there to suggest that our prehistoric ancestors were quite advanced!"
    rothbauer @ say "The government doesn't want you to know that ancient integrated circuits have been discovered deep underground alongside the fossilized remains of Mesozoic era creatures."
    rothbauer @ say "To develop such advanced technology implies the existence of organized civilization!"
    rothbauer @ say "Ahem, excuse me, I'm just very passionate about that particular time period."
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

    scene bg campus with fade

    play music "audio/ambient/outdoors people talking.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "Next up you've got Introduction to Probability and Statistics. You signed up for it because you thought it would teach you how to game drop rates in RPGs."

    if metGunner == True:
        n "Along the way you bump into a familiar feline."

        show gunner neutral at norm with dissolve

        gunner @ say "Sup, [name]! Where ya goin'?"

        player "Oh hey, you again. I'm on my way to statistics."

        gunner @ say "With Mrs. Herschel?"

        player "Yeah I think so."

        gunner @ say "Ayy, that makes us classmates!"
        gunner @ say "Fair warning though, this class is hella hard."
        
        player "Fantastic."
        
        gunner @ say "We better hurry there, Mrs. Herschel hates it when students are late."
        
            
        scene bg lecturehall with fade

        play music "audio/music/mere - schooldaze faster.ogg" fadein 1.5

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

        play music "audio/music/mere - schooldaze faster.ogg" fadein 1.5

        show box with Dissolve(.2):
            ypos 0
        
        show herschel:
            xpos 2000
            yalign 0

        n "Looks like you made it before the teacher arrived."
        n "Nobody else is brave enough to sit in the front row, leaving you no choice but to take a seat there."
        n "Somone sits right next to you and starts chatting you up like you're best friends."
        
        show gunner neutral at norm with dissolve
        
        gunner @ say "Yeah so summer vacation was pretty lit. Went on this week long fishing trip on my dad's yacht with the bros and my portfolio is up 20\% from the start of the quarter."

        menu:
            "Are you talking to me?":
                player "Huh? Are you talking to me?"
                
                gunner @ say "Uh yeah? That's not a problem is it?"
                
                player "No, it's just weird you would think I give a shit about your yacht."
                
                gunner @ say "Ohh sorry, sorry! You're more of a helicopter guy I see, my mistake."
                gunner @ say "My family doesn't have one of those yet but maybe I'll ask for one for my birthday."
            "Wow money is so cool.":
                player "Wow money is just so cool, isn't it?"
                
                n "He evidently doesn't pick up on your sarcasm, because there isn't a hint of irony in his response."
                
                gunner @ say "I know right? I don't get why people like, choose to be poor? It's weird."

        gunner @ say "I'm Gunner by the way! What's your name?"
        
        player "[name]."
        
        n "At least he's not pestering you with questions about what it's like being the last human. In fact, you don't know if he is even aware of that fact."
        n "It seems he's more concerned with his own status and appearance."
        
        gunner @ say "[name], huh? Lemme tell you a funny story."
        gunner @ say "This building was used for the feminism studies college last semester. They switched it over to math over the summer."
        gunner @ say "So when I saw I had stats here my first thought was \"The hell? Are we gonna learn how to find the hypotenuse while folding laundry or something?\""
        
        menu:
            "Laugh":
                n "You have to admit, that got a chuckle out of you. You try to hide it, but your true colors make themselves known."
                
                gunner @ say "Hah, don't be afraid to laugh, I know I'm funny!"
            "Don't say anything":
                n "You pretend you're still waiting for the punchline and remain silent."
                
                gunner @ say "Like folding a towel or something into a triangle and-"
                
        n "Gunner goes quiet as an old lady walks into the room. That must be the professor."

    show herschel with dissolve:
        xpos 0

    herschel @ say "Good afternoon everyone! My name is Mrs. Herschel and I'm very excited to teach probability and statistics again this year!"

    show gunner neutral at norm with dissolve:
        xzoom -1
        xpos -500

    gunner @ say "Looking good, Mrs. Herschel! I'm very excited to learn probability and statistics again this year!"

    herschel @ say "Flattery will get you nowhere Gunner. I'm afraid you'll be learning this subject for the first time this year judging by your grades last year."

    gunner @ say "Hey I still remember y = mx + b!"

    herschel @ say "That's geometry, dear."

    gunner @ say "..."
    gunner @ say "Oh yeah."

    hide gunner with dissolve

    herschel @ say "That reminds me, I wanted to point out this can be a very challenging class. I recommend spending half an hour every night studying the textbook and working through the example problems."
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
    show tmonday at norm
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7



label secondDayOfClass:
    #___tuesday1
    scene bg codadorm with fade

    play music "audio/ambient/morning birds.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0

    n "You roll out of bed and start your morning ritual in preparation for class."
    n "Today you have World Literature and then French Language 101."
    n "A couple weeks ago you received an email with the books you'll need. The first one you'll be going over in literature is the novella \"The Death of Ivan Ilyich.\""
    n "You pack the book in your bag along with the French textbook and venture out."

    stop music fadeout 1.0

    scene bg lecturehall with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "You step into a large lecture hall with a projector already beaming a desktop onto a screen at the front. Students trickle in until the room is full."
    n "A couple minutes before class is scheduled to begin, a woman comes in through a door near the podium."
    n "To your dismay, the teacher of this class is the same lady who gave the orientation speech the other day."
    n "You don't think you made the best first impression the other day. Hopefully she doesn't hold a grudge."
    n "She double clicks a file and brings up a slideshow."

    show ellen teacher happy at norm with dissolve

    ellen @ say "Good morning and welcome to World Literature I!"
    ellen @ say "Today we'll go over the syllabus and what you can expect from this class. Then we'll finish up with some discussion on the assigned reading!"

    n "She clicks a button and the slideshow advances to the next slide, going over some information about herself."
    
    show ellen teacher neutral

    ellen @ say "My name is Miss Ellen and I've been teaching at Harmonia for 13 years so I like to think I've gotten quite good at it!"

    show ellen teacher sad at shudder

    ellen @ say "Oop, ignore the Mrs. in front of my name on the slide... I guess I forgot to update that..."
    ellen @ say "Haha recently divorced... you know how it goes..."

    n "She quickly advances forward a few more slides."

    show ellen teacher neutral at norm

    ellen @ say "Ahem where was I? Oh yes, this course will introduce you to literature across a variety of different cultures throughout different time periods."
    ellen @ say "In the interest of time, most of the reading will be on the short side, or at least limited to excerpts from longer works."
    ellen @ say "In case you didn't get my email, you'll be responsible for procuring your own books, starting with a favorite of mine, Tolstoy's \"The Death of Ivan Ilyich!\""
    ellen @ say "You won't have a test on it until the end of next week but I'll expect you all to read the assigned chapters every night and keep up with the discussions in class."

    n "Miss Ellen gives an overview of the rest of the books you'll be reading and how she'll be grading responses to open ended questions."
    n "Somehow she manages to stretch it to half the duration of the class time before starting with the lesson."
    n "She explains the historical context and some biographical information regarding the first assigned story."

    ellen @ say "Leo Tolstoy is considered one of the greatest authors of all time, his works often taking on philosophical questions like 'What is the meaning of death?'"
    ellen @ say "That, in fact, is the main topic of his novella \"The Death of Ivan Ilyich!\""
    ellen @ say "We'll dive into the life of a man as his life crumbles apart and he learns to deal with his inevitable death."
    ellen @ say "Indeed, this wasn't the first time Tolstoy wrote on the subject of death, as he had earlier written \"A Confession,\" considering the possible interpretations and attitudes toward death."
    ellen @ say "Although he struggled with his own mortality, Tolstoy seems to have come to a conclusion on what a good death means."
    ellen @ say "Please open your books and we'll hop right in!"

    hide ellen with dissolve

    n "You pull the book out of your bag and open your notebook to a fresh page."
    n "Miss Ellen goes over the first few pages of the novella, explaining some things and asking the class for their thoughts along the way."
    n "Time flies by quickly and the end of the hour is upon you before you realize it."

    show ellen teacher neutral at norm with dissolve

    ellen @ say "That's all for today! We'll continue this discussion next time! Have a nice day!"

    hide ellen with dissolve

    n "You pack your things and stand up."
    n "Next up is French class. You always wanted to learn another language. Unfortunately the classes for all the good languages were already filled."
    
    stop music fadeout 1.0

    scene bg classroom with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    show celestine neutral at norm with dissolve

    celestine @ say "Bon après-midi! I am Mrs. Celestine and I'll be your French teacher for this semester, and hopefully the next one as well if you decide to stick with it!"

    n "You become distracted from her introduction by the strange ripples that seem to appear out of nowhere in the translucent bottle of water on the professor's desk."
    n "As the water starts to bounce more violently in the glass, you hear a rhythmic low pitched thud gradually getting louder."
    n "A moment later, the door crashes open and a wall of fluff squeezes through the doorframe."

    if metClaire == True:
        n "Isn't that Claire?"
        n "What a coincidence you have a class with her."
    else:
        n "You've seen that fat rabbit before. She's the ditzy girl from orientation night."
        
    show claire outdoors embarassed at norm with moveinleft:
        xzoom -1
        xpos -650

    claire @ say "*Huff huff* Sorry I'm late!"
    
    celestine @ say "No worries! I'm just glad you arrived at all!"
    celestine @ say "Anywho, go ahead and take a seat and we'll begin introductions!"
    
    #show claire sweater neutral

    n "Claire makes her way over to the desks and looks you dead in the eye."

    show claire sweater neutral at norm with move:
        xpos 560

    pause .05

    show claire sweater neutral at flipleft

    if metClaire == False:
        claire @ say "Heyyy cutie~"
        claire @ say "Mind if I sit next to you?"
        
        menu:
            "Sure?":
                player "I guess not?"
                
                claire @ say "Good, cause I was gonna sit here anyway."
            "Go right ahead!":
                $ clairePoints =+ 1
                player "Go ahead! Here lemme get that for you."
                
                n "You pull the chair out for her, just to be nice."
                
                claire @ say "Such a gentleman! Ksksksks!"
        
        claire @ say "I'm Claire bee tee double you~"
         
        n "The plastic of the chair squeals and groans under the weight of the oversized rabbit with the bun's buns barely even able fit on the seat."
        n "Not that you were staring, it's just hard to ignore an object so immense it bends space and time and curves the path of the photons straight into your pupils."
    else:
        claire @ say "OMG [name]! You're in this class too??? How unexpected!"
        
        show claire sweater lusty

        claire @ say "Imma sit next to you, k?~"
        
        #player "I guess I can't stop you."
        
        show claire sweater neutral

        n "Claire takes the seat next to yours and starts rummaging around in her bag."

    hide claire with dissolve

    celestine @ say "Génial! Looks like everyone is present now! I'll say a few things about myself, then you can all tell me about yourselves and why you decided to learn French!"
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

    show claire sweater derp at norm with dissolve:
        xpos 560

    claire @ say "Umm like, I dunno, I kinda just picked it on a whim! I guess I like to try new things and leave things to chance!"

    hide claire with dissolve

    celestine @ say "Good! That mindset has lead me to some very... intéressante places in the world."
    celestine @ say "Next up, you there!"

    menu:
        celestine "{cps=0}Next up, you there!{/cps}"
        "Same as Claire, it was random.":
            $ clairePoints = clairePoints + 1
            n "You shrug."

            player "Same as Claire, it was just kind of random and all the other language classes were taken."

            show celestine happy

            celestine @ say "Ah, perhaps it was fate then!"
            celestine @ say "Do you believe in fate?"
            
            menu:
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

            celestine @ say "Some of the most reknowned philosophers come from France you know~"
            celestine @ say "Voltaire wrote a story called \"Zadig,\" which is the French word for Destiny and--"
            celestine @ say "Oh sorry, I went on a bit of a tangent there! I do that from time to time. We best move on before class ends."

            #n "Everything has a meaning? Could that really be true? Or are some things really just arbitrary?"

        "Wanted to travel.":
            n "You shrug."

            player "I guess I just wanted to visit France someday."

            celestine @ say "Oh là là! France is such a beautiful and worthwhile place to visit! I could go on for hours, telling you the best spots to go!"
            celestine @ say "France is pretty tourist friendly, but of course it helps a lot to know the language before going!"
            celestine @ say "Just like I was saying earlier, you can always find interesting conversation in new places, provided you know what they're saying!"
            
            

    n "The rest of the students give their reasons for being here, which ends up taking most of the class time."
    n "Mrs. Celestine only has a few minutes to go over the very basics of French like pronunciations and greetings."

    celestine @ say "Looks like we're out of time for today. Be sure to study and practice not only reading, but speaking in French as well!"
    celestine @ say "You might find it helpful to get a study partner to practice conversing in French!"

    hide celestine with dissolve

    n "Claire turns to you with a devious grin."

    show claire sweater wave at norm with dissolve:
        xpos 560

    claire @ say "Heyyyyy, wanna be study partners?"

    menu:
        claire say "{cps=0}Heyyyyy, wanna be study partners?{/cps}"
        "Sure, why not?":
            $ clairePoints =+ 1
            
            player "Sure, why not?"
            
            show claire sweater overjoyed

            claire @ say "Yay! I can't wait!"
            
            show claire sweater embarassed
            
            claire @ say "I have to go to chemistry right now, but we can study later!"

            player "I had literature earlier so I'm done for the day."
            
            show claire sweater derp

            claire @ say "Great! That means you can walk me to my next class!"
            
        "I don't need a study partner.":
            player "I don't need a study partner."
            
            show claire sweater giggle

            #claire @ say "But I do!"
            claire @ say "Wow you must be really smart!"
            
            show claire sweater heyeah
            
            claire @ say "In that case you can be my tutor!"

            player "That's not what I meant..."            
            
            
            
            
            
            
            
            
            
            
            
            

    stop music fadeout 1.0

    scene bg campus with fade

    show box with Dissolve(.2):
        ypos 0

    show claire sweater neutral at norm with dissolve:
        xzoom -1
        xpos -300
        
    play music "audio/music/Evan Schaeffer - Aqueduct.ogg" fadein .5

    claire @ say "...and that was around the time I picked up sousaphone for my school's marching band and --"
    
    show claire sweater surprised
    
    claire @ say "Ohmygosh it's Ava! She's like my best friend foreverrr!!!"
    
    show claire sweater wave
    
    claire @ say "Avaaaa! Over here!!!"

    n "Claire waves to the bird in the distance holding a camera pointed in your general direction."
    n "She seems annoyed as she looks over the viewfinder and flutters over."
    
    show claire sweater neutral
    show ava pose annoyed at norm with moveinright:
        xpos 400
        
    claire @ say "What's up?"

    #ava @ say "You know, the point of street photography is to capture reality without the photographer interacting with their subjects."
    #ava @ say "You know, the point of street photography is to capture reality without the photographer's influence."
    #ava @ say "I can't really do that with you looking directly at the camera and flailing your arms."
    ava @ say "You know, street photography is sorta like wildlife photography."
    
    show claire sweater surprised

    claire @ say "What do you mean?"

    ava @ say "It's about capturing the moment in as natural a state as possible. Me and my camera are supposed to be invisible."
    
    show claire sweater cry

    claire @ say "Oh did I ruin your shot? Sorry..."
    
    show ava pose happy

    ava @ say "It's no big deal, I was just warming up anyway."
    ava @ say "I see you brought a friend."
    #if metAva:
    #else:
    
    show claire sweater neutral

    claire @ say "Yup! Me and [name] here have French together so we're gonna be study buddies!"

    ava @ say "Is that so? I took French in high school but I could never retain any of it."
    
    show claire sweater giggle
    
    claire @ say "How do you not remember your native tongue?"
    
    show ava pose concerned
    
    ava @ say "What? I hatched in Oregon."
    
    show claire sweater surprised

    claire @ say "You mean... you're not French?"
    
    ava @ say "?"
    ava @ say "No? Why would you think that I was?"
    
    show claire sweater embarassed
    
    claire @ say "It's just... you're artsy and your last name is Montblanc, like that mountain in France."
    
    show ava pose annoyed
    
    ava @ say "That doesn't mean *I've* ever been to France! That just means someone in my family was probably from there at some point!"
    ava @ say "That's like me assuming you were born in the Netherlands just 'cause you're a Flemish giant rabbit!"
    
    claire @ say "Is that what I am??"
    
    show ava pose angry
    
    ava @ say "How do you not know these things?"
    
    show claire sweater derp
    
    #claire @ say "I guess I'm not all that smart huh..."
    claire @ say "I guess I'm not such a clever bunny, huh..."
    
    show claire sweater surprised
    
    claire @ say "Oh, here's the science building! I'll catch you two later, k?"
    
    show claire sweater neutral 
    show ava pose happy
    claire @ say "How does lunch tomorrow sound?"

    menu:
        claire "{cps=0}How does lunch tomorrow sound?{/cps}"
        "Sure!":
            #finished
            $ avaPoints = avaPoints + 1
            $ clairePoints = clairePoints + 1
            $ avalunch = True
            player "Sure, that sounds cool."

            show claire sweater overjoyed
            
            claire @ say "Yes!"
            
            n "Claire pulls you into a suffocating hug. Ava has to pry her off of you."
            
            show ava pose ohyou
            
            ava @ say "Come on Claire, we've got class to get to."
            
            show ava pose happy
            
            ava @ say "Bye [name]! We'll see you tomorrow!"
            
            player "Can't wait!"
            
            show claire sweater wave
            
            claire @ say "See you tomorrow!"
            
            n "Claire waves to you while Ava pushes her into the science building."
            
            show claire at offscreenleft:
                yalign 0
            show ava at offscreenleft:
                yalign 0
            with move
            
            n "The bird smiles to you before flapping her wings and taking off into the sky to wherever her own class is."
            
            show text "{color=c8f8ff} {/color}":
                ypos 46
                xpos 940
            
            #ava @ say "Bye [name]!{nw}"
            show text "{color=c8f8ff}Bye [name]!{/color}":
                ypos 46
                xpos 940

            show ava at offscreenright with MoveTransition(delay=.8):
                xzoom -1
                yalign .2

            hide text
            
            pause .6
            

            #ava @ say "Welp, I have to get to class as well. See you later, [name]!"
            
            #player "Salut!"
        
            #ava @ say "?"
            #ava @ say "Oh haha French words."
            #ava @ say "Au revoir or however they say it."

        "I already have plans":
            #untested
            $ avalunch = False
            $ roriPoints = roriPoints + 1
            player "Sorry, I already have plans."
            
            show claire sweater cry

            claire @ say "Oh... I guess you must be pretty busy. Maybe another time then?"
            
            player "Maybe."
            
            claire @ say "Maybe. Okay, yeah, maybe."
            claire @ say "See you later for real this time!"

            show claire sweater cry at offscreenleft with moveinleft:
                xzoom 1
                yalign 0

            n "Claire hurries off into the science building."

            ava @ say "What's her problem?"
            ava @ say "Whatever, she'll be fine. I've got a class to get to."
            ava @ say "See you around, [name]!"

            player "Later!"
            
            hide ava with dissolve

    n "You're suddenly feeling very tired. Social interaction always makes you feel drained of energy. You decide to retire to your dorm."

    stop music fadeout 1.0



        
            
            
            
            
            
            
            
    claire @ say "Hey is that Ava?"
    
    show claire sweater wave
    
    claire @ say "Avaaaa! Over here!!!"

    n "Claire waves to the bird in the distance taking photos in your general direction."
    n "She looks annoyed as she lowers her camera and walks over."
    
    show claire sweater neutral
    show ava pose annoyed at norm with moveinright:
        xpos 400

    #ava @ say "You know, the point of street photography is to capture reality without the photographer interacting with their subjects."
    #ava @ say "You know, the point of street photography is to capture reality without the photographer's influence."
    #ava @ say "I can't really do that with you looking directly at the camera and flailing your arms."
    ava @ say "You know, street photography is sorta like wildlife photography."
    
    show claire sweater surprised

    claire @ say "What do you mean?"

    ava @ say "It's about capturing the moment in as natural a state as possible. Me and my camera are supposed to be invisible."
    
    show claire sweater cry

    claire @ say "Oh did I ruin your shot? Sorry..."
    
    show ava pose happy

    ava @ say "It's no big deal, I was just warming up anyway."
    ava @ say "I see you brought a friend."
    
    show claire sweater neutral

    claire @ say "Yup! Me and [name] here have French together so we're gonna be study buddies!"

    ava @ say "Is that so? I took French in high school but I could never retain any of it."

    show claire sweater pose neutral

    claire @ say "Ksksksks hopefully we won't end up the same way!"
    claire @ say "*Sigh*"
    claire @ say "I'd just love to visit Paris one day!"

    ava @ say "The only thing I remember is they say it like \"Pah ree\" over there."

    player "Then why'd they put an \"s\" at the end of it?"

    n "Ava shrugs."
    
    show ava bored

    ava @ say "You have to ignore half the letters when it comes to French."

    claire @ say "I guess so!"
    
    show claire sweater surprised
    
    #claire @ say "Wait, Ava, aren't you *from* France??"
    claire @ say "To be honest, this whole time I thought you were from France!"
    
    ava @ say "?"
    ava @ say "No? Where'd you get that idea?"
    
    show claire sweater neutral
    
    claire @ say "Cause you're artsy and your last name is Montblanc? As in that tall mountain in France?"
    
    show ava normal neutral
    
    ava @ say "Huh, is that where it comes from?"
    
    show ava angry
    
    ava @ say "Wait, did you just assume my nationality because I'm 'artsy?'"
    
    show claire sweater embarassed
    
    claire @ say "I mean, I just thought uhhh..."
    claire @ say "Oop well here's the science building, gotta go, see you later!"
    
    #show claire at offscreenleft with move
    show claire at hopaway
    
    #make little animation of claire 'hopping' away
    
    show ava normal neutral
    
    n "Claire hops away as if Ava were a bird of prey about to catch and fly off with her."
    n "Even though she probably weighs quadruple Ava's weight."
    n "Animal people instincts are funny like that."
    n "Suddenly she turns on her heel and hops right back."
    
    #show claire sweater neutral at norm with dissolve:
    #    xzoom -1
    #    xpos -180
    show claire sweater neutral at hopback
    
    pause .7
    
    claire @ say "Oh, before I forget..."
    claire @ say "[name], would you like to have lunch with us tomorrow?"

    menu:
        claire @ say "{cps=0}[name], would you like to have lunch with us tomorrow?{/cps}"
        "Sure!":
            $ avaPoints = avaPoints + 1
            $ clairePoints = clairePoints + 1
            $ avalunch = True
            player "Sure, that sounds cool."

            show claire sweater overjoyed
            
            claire @ say "Yes!"
            
            n "Claire pulls you into a suffocating hug. Ava has to pry her off of you."
            
            ava @ say "Come on Claire, we've got class to get to."
            
            show claire sweater wave
            
            claire @ say "See you tomorrow, [name]!"
        
            player "Salut!"
    
            ava @ say "?"
            ava @ say "Oh haha French words."
            ava @ say "Au revoir or however they say it."
            
            n "Claire waves to you while Ava pushes her into the science building."
            
            show claire at offscreenleft:
                yalign 0
            show ava at offscreenleft:
                yalign 0
            with move
            
            n "The bird smiles to you before flapping her wings and taking off into the sky to wherever her own class is."
            
            show text "{color=c8f8ff} {/color}":
                ypos 46
                xpos 940
            
            #ava @ say "Bye [name]!{nw}"
            show text "{color=c8f8ff}Bye [name]!{/color}":
                ypos 46
                xpos 940

            show ava at offscreenright with MoveTransition(delay=.8):
                xzoom -1
                yalign .2

            hide text
            
            pause .6

        "I already have plans":
            $ avalunch = False
            $ roriPoints = roriPoints + 1
            player "Sorry, I already have plans."
            
            show claire sweater cry

            claire @ say "Oh... I guess you must be pretty busy. Maybe another time then?"
            
            player "Maybe."
            
            claire @ say "Maybe. Okay, yeah, maybe."
            claire @ say "See you later for real this time!"

            show claire sweater cry at offscreenleft with moveinleft:
                xzoom 1
                yalign 0

            n "Claire hurries off into the science building."

            ava @ say "What's her problem?"
            ava @ say "Whatever, she'll be fine. I've got a class to get to."
            ava @ say "See you around, [name]!"

            player "Later!"
            
            hide ava with dissolve

    n "You're suddenly feeling very tired. Social interaction always makes you feel drained of energy. You decide to retire to your dorm."
    
    stop music fadeout 1.0

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    #n "Damn, these classes sure take a lot out of you. 
    n "You can't remember the last time you felt so exhausted. It's probably just because you're not used to the school routine after being left to your own devices for so long."
    n "Literally. You haven't needed to go out or do much of anything since you've always had a computer within arm's reach."
    n "Speaking of which..."

    if fratsoro == "frat":
        n "You flop down in bed and browse an Ethiopian alternative cryptocurrency fansite on your phone until you fall asleep."
    else:
        n "You flop down in bed and browse a Bangladeshi kite testing IRC channel on your phone until you fall asleep."

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show ttuesday at norm
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7













































    
    return
