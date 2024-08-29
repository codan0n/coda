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

    $ randumb = renpy.random.randint(0, 1)
    
    #for testing
    #n "random number is [randumb]"
    
    if randumb == 0:
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
        n "You almost made it to the end without getting poached by some aggressive salesman."
        
        show gunner neutral at norm with dissolve

        gunner @ say "Hey there! I saw you checkin' out the frats and thought you should know Alpha Alpha Alpha is the best one!"
        
        player "I actually wasn't and I don't really care about fraternities."
        
        gunner @ say "That's just the sort of thing an Alpha male would say!"
        
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
                
                gunner @ say "The one with all the buff dudes and magic powers that are also buff dudes half the time."
                
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
    n "After giving the menu a look, you decide what you want and walk up to the counter."

    show mishka neutral at norm with dissolve

    mishka @ say "Privyet, welcome to Coffee Zona..."
    
    #show mishka derp
    
    mishka @ say "...er, Zone!"
    
    show mishka neutral
    
    mishka @ say "How can I help you?"

    player "Yeah can I get uhh...."

    n "You give the barista your order and pay with your debit card."

    mishka @ say "And can I get name for you?"
    mishka @ say  "Not that I really need it since we're the only ones in here."
    mishka @ say "But it would be nice to have irregardless."

    player "      [name].      "

    mishka @ say "Alright [name], I'll have that your order ready for you soon!"

    player "Thanks uhh..."

    n "You look down at her nametag."

    if roriPoints < 0:
        n "It's in cyrillic."
    
        player "Thanks ...Mnwka? I don't know how to say that."
        
        show mishka depressed
        
        mishka @ say "It's Mishka."
        
        show mishka neutral
        
        n "She begins working on your order while continuing the conversation."
        
        mishka @ say "I don't recall seeing you before. You must be new student."
    
    else:
        player "Thanks, Mishka! Am I saying that right?"

        mishka @ say "Yup! Not many Mishkas around here, are there?"

        player "Nope, you're the first I've ever met. Then again, I did just move here."

        n "She begins working on your order while continuing the conversation."

        mishka @ say "Oh? Are you new student?"

    player "Yeah. Can't decide what to major in though."

    mishka @ say "It can be tough choice to make. I wouldn't stress about it though, most people find something after semester or two."

    player "I sure hope so. I wasn't really planning on going to college in the first place, but I also wasn't planning on not going, you know?"
    player "But now I'm here and I still don't know what I'm doing."

    mishka @ say "Many students feel the same way. Life can be that way sometimes. You just have to make best of it while you're here."
    mishka @ say "For now, enjoy coffee and bagels!"

    n "Mishka hands you a steaming hot cup and a bag."

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

    n "You walk out the door, feeling somewhat uplifted by the barista's wise words, and find a place to sit and enjoy your breakfast."
    n "A light breeze passes by as you bite into your bagel and watch the other students walking around."
    n "It's pretty easy to pick out who's a freshman like you and who's been here for a while."
    n "The new people are still basically high schoolers at this point. Practically still kids, and it shows in the way they carry themselves."
    n "Unsure about the world but excited about all the possibilities."
    n "The upperclassmen on the other hand seem a bit more grizzled, beaten down by the world but tougher for it."
    n "Less optimistic, more realistic."
    n "Man."
    n "To be honest, you're kinda glad you're back in school."
    n "The past few years hadn't been kind to you. You basically had to drop out of high school to take care of your parents in their final moments."
    n "It'll be nice going back to a structured life with classes but with the added freedom of being a \"\"\"real\"\"\" adult."
    n "You finish up your meal, gathering your scraps and throwing them away as you ponder what to do with the rest of your day."
    if fratsoro == "frat":
        n "Maybe you'll just go back to your dorm and post on your favorite Lithuanian underwater basketweaving forum in bed for a while."
    else:
        n "Maybe you'll just go back to your dorm and post on your favorite Turkish astral projection forum in bed for a while."
    n "Yeah, that sounds like a good idea."

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

    


































    
    return
