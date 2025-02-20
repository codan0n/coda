label chapter3:
    4 currentSeason = "autumn"
    
    scene bg black with fade
    
    $ townEvents.append("linaTown")
    
    n "A few weeks later"
    
    scene bg cafe with dissolve
    
    play music "audio/music/mere - coffeeLoveLoopInstrumental.exe.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0
        
    n "You decide stop by the cafe on your way to class. They must have updated their menu because you can smell cinnamon and pumpkin spice in the air."
    n "Fitting for the changing color of the leaves outside as autumn takes its hold."
        
    show mishka neutral at center with dissolve:
        xzoom -1
        #xpos -440
        ypos y_mishka

    mishka @ say "Hello [name]! Would you like to try the spice of pumpkin latte? It's part of our fall menu thing."

    player "Actually I was eyeing that cinnamon roll."

    mishka @ say "Oh lucky you, it's our last one! They sell out very quickly!"

    player "They must be good if everyone wants one!"
    
    show mishka overjoyed

    mishka @ say "Yes, fully of sugar and sweetness! When I first came to America I had no concept of a 'cinnamon roll' but it soon became a favorite of mine hehe!"
    
    show mishka neutral

    player "I'll take it to go please. I have to be in class in a few minutes."

    mishka @ say "Gotchya!"

    n "Mishka places the pastry in a bag and slides it over to you as you swipe your card through the machine."
    
    show mishka winki

    mishka @ say "Spasibah! Have great day!"
    
    show mishka neutral
    
    show margaret neutral at offscreenright:
        yalign 0
    
    #hide mishka with dissolve

    #add sound effect of bell as anyone enters the cafe
    
    pause .2

    show margaret neutral:
        xpos 350
        ypos y_margaret
    show mishka:
        xpos -440
    with move

    margaret @ say "Oh hello there, [name]. I guess we're both cutting it short on time before class today, aren't we?"
    
    player "Good morning Ms. Ellen. Sorry but Coffee Zone is worth being late for!"
    
    margaret @ say "I wouldn't be here right now if it wasn't!"
    
    mishka @ say "Oh you~"
    
    margaret @ say "We're just having a quiz today so this gives students some extra time to prepare."
    
    player "Err, quiz?"

    show margaret sad

    margaret @ say "Oh, did you forget?"
    
    show margaret neutral
    
    margaret @ say "You should be fine, as long as you've been keeping up with your reading."
    
    show margaret happy
    
    margaret @ say "Now if you'll excuse me, I'm going to get one of those delicious cinnamon buns. What better way to start autumn, right?"
    #margaret @ say "Why, I'd kill for them! Figuratively, of course!"
    
    show mishka sad

    mishka @ say "Sorry ma'am, I just sold the last one to [name] here..."

    show margaret sad

    margaret @ say "Seriously?"
    margaret @ say "Damn, I was really counting on that cinnamon bun to get me through today..."

    menu:
        margaret "{cps=0}Damn, I was really counting on that cinnamon bun to get me through today...{/cps=0}"
        "Offer Miss Ellen your cinnamon roll":
            $ ellenPoints =+ 1
            $ gaveCinRoll = True
            $ badEnd =+ 1
            
            player "Well... I could give you mine. I don't really mind."
            
            show mishka happy

            show margaret neutral
            
            mishka @ say "Aww how sweet of you!"

            margaret @ say "Oh my goodness, I'm flattered but a teacher could never accept such a gift from a student!"
            
            show mishka neutral

            player "No really, I just remembered I'm not supposed to eat sugary things when I'm on these pills so..."

            show margaret intrigued 
            
            margaret @ say "Hmm..."

            n "Miss Ellen looks around."
            
            show margaret melancholy

            margaret @ say "Well, I suppose I could, just this once..."

            player "Don't worry, I'm not gonna tell on you or anything."
            player "Here you go."

            n "You hand over the bag."
            
            show margaret neutral

            margaret @ say "Aww, thanks [name]!"

            n "Miss Ellen gives you a warm smile and leans in close enough to whisper into your ear."

            margaret @ say "Don't worry about the quiz today~"

            n "Miss Ellen waves to you as she takes a bite of the cinnamon roll."

            margaret @ say "See you in class!"

            hide margaret with dissolve

            player "Yeah, I guess I should get going too. Later, Mishka!"

            mishka @ say "Dah skorovuh!"

            stop music fadeout 1.3

            scene bg lecturehall with fade
            
            play music "audio/music/mere - retrograde.ogg" fadein .5

            show box with Dissolve(.2):
                ypos 0

            show margaret neutral at center with dissolve

            margaret @ say "Good morning class! I hope you studied well for today's quiz!"

            n "Ms. Ellen hands out papers to everyone, giving you a warm smile as she hands you yours."

            if literatureSkill >= 2:
                n "You probably could have aced this quiz anyway, but the extra assurance from your bribe doesn't hurt."
                n "You work through the quiz normally in case she decides to go back on her word."
                n "When you're finished you walk up and turn it in."
            else:
                n "It's a good thing you bribed her with that cinnamon roll, otherwise you'd fail this quiz for sure."
                n "Feels a bit dishonest though..."
                n "Looking over the questions, you have no idea how to answer most of them."
                n "You just write something that kinda makes sense and turn it in when you're done."

        "Don't offer Miss Ellen your cinnamon roll":
            show mishka neutral
            
            player "Better luck next time."

            n "You take a bite out of your cinnamon roll while Miss Ellen glares at you."

            margaret @ say "Yes well... I'll see you in class, [name]."

            hide margaret with dissolve

            n "She storms out of the cafe without even getting a coffee."
            
            #show mishka hopeful
            
            n "You glance at Mishka who just shrugs."

            player "Guess I better go too. Later, Mishka!"
            
            show mishka happy

            mishka @ say "Dah skorovuh!"
            
            stop music fadeout 1.0

            scene bg lecturehall with fade
            
            play music "audio/music/mere - retrograde.ogg" fadein .5

            show margaret neutral at center with dissolve

            show box with Dissolve(.2):
                ypos 0

            margaret @ say "Good morning class! I hope you studied well for today's quiz!"

            n "Ms. Ellen hands out papers to everyone, glaring at you as she hands you yours."
            n "She isn't still mad about the cinnamon roll thing, is she?"
            n "Hopefully she doesn't take it out on your grades."

            if literatureSkill >= 2:
                n "The answers come to you fairly quickly as you go through the quiz, thanks to the time you spent studying."
                n "You feel confident as you walk up and hand in your quiz."
            else:
                n "After looking over the quiz and realizing you're not prepared to answer any of these questions, you begin to regret not giving up your cinnamon roll this morning."
                n "You do the best you can and sheepishly turn it in."
            
    margaret @ say "...Is that everyone's?"
    
    show margaret melancholy
    
    margaret @ say "Very good, what do you say we call it a day?"
    
    show margaret neutral
    
    margaret @ say "I don't want to overload your brains too much, that's what midterms are for!"
    margaret @ say "Which are coming up in two weeks by the way!"
    margaret @ say "Be sure to start studying for it sooner rather than later!"
    margaret @ say "That's all I have for you. Class dismissed!"
    
    scene bg campus with fade
    
    n "Getting out of your first class of the day early sucks because you have to loiter around waiting for your next class."
    n "The minutes pass by and students gradually pour out from the buildings surrounding you."
    n "One of those students notices your idleness and makes a beeline for you."
    
    show claire flannel happy at center with dissolve:
        ypos y_claire
        
    claire @ say "[name]!!! Ohmygosh you waited out here for me???"
    
    player "Huh?"
    
    menu:
        "Of course!":
            $ clairePoints =+ 1
            
            player "Of course! I wanted to walk you to class today."
            
            claire @ say "You're such a sweetheart!!"
            claire @ say "Shall we go then?"
            
            n "Claire holds out her paw and you grab hold of it."
            n "You can hardly keep up with her long strides and the tightness of her grip cuts off the circulation in your hand as she practically drags you along toward French."
            
        "It's just coincidence":
            player "I just got out of class early, that's all."
            
            claire @ say "Don't play coy with me, I can tell you just wanted to walk me to French!"
            claire @ say "Ya know all ya had to do was ask!"
            
            n "Claire grabs hold of your hand, the tightness of her grip cutting off circulation as she practically drags you to your next class."
            
    scene bg classroom with fade
    
    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    show celestine neutral at center with dissolve:
        ypos y_celestine
        
    celestine @ say "Bonjour, étudiants!"
    celestine @ say "Today we'll be getting some more practice with passé composé et imparfait tenses!"
    celestine @ say "Let's see who's been studying!"
    celestine @ say "How would you say this in French?"
    celestine @ say "\"I was doing my homework.\""
    celestine @ say "Care to tell us, [name]?"
    
    menu:
        "Je faisais mes devoirs.":
            $ frenchSkill =+ 1
        
            player "Je faisais mes devoirs."
            
            celestine @ say "Very good!"
            celestine @ say "Note that we use je instead of j'ai, which we would use if we wanted to say \"I did my homework\" or \"I have done my homework.\""
            celestine @ say "See the difference? Anyway, moving on..."
        "J’ai fini mes devoirs.": 
            player "J’ai fini mes devoirs."
            
            celestine @ say "Hmm, not quite. You've used the passé form here, which would be like saying \"I did my homework\" or \"I have done my homework.\""
            celestine @ say "I asked specifically for \"I was doing my homework\" which would be \"Je faisais mes devoirs.\""
            celestine @ say "Note that we use je instead of j'ai. See the difference? Anyway, moving on..."
        "J’ai faisais mes devoirs.":
            player "J’ai faisais mes devoirs."
        
            celestine @ say "Hmm, not quite. You've used the passé form here, which would be like saying \"I did my homework\" or \"I have done my homework.\""
            celestine @ say "I asked specifically for \"I was doing my homework\" which would be \"Je faisais mes devoirs.\""
            celestine @ say "Note that we use je instead of j'ai. See the difference? Anyway, moving on..."
        
    scene bg campus with fade
    
    show ava happy at center:
        ypos y_ava
    show claire flannel happy at center:
        ypos y_claire
    with dissolve
    
    ava @ say "...You two have any plans after class?"
    
    claire @ say "Mmmh nope! Why?"
    
    ava @ say "I wanted to see if you wanted to go out shooting with me!"
    
    claire @ say "I would but I didn't bring my gun!"
    
    ava @ say "I meant with cameras. I'll even let you borrow one!"
    ava @ say "I just love shooting in autumn, it's my favorite season."
    ava @ say "The leaves are so pretty, especially at sunset~"
    
    player "I'd love to join you but I've got a doctor's appointment later today."
    
    ava @ say "Aww, hopefully it's nothing serious?"
    
    player "Just a checkup."
    
    ava @ say "Well, if you ever have a moment to go shooting, just let me know!"
    
    player "I will. See you two later!"
    
    ava @ say "See ya!"
    
    claire @ say "Byeee~"
    
    n "You wave goodbye as Claire and Ava head to their next classes."
    
    scene bg hospital with fade
    
    n "After checking in to the hospital, a nurse did the routine blood pressure and temperature tests, then left you alone to wait for the doctor."
    n "Your muscles tense up as your mind wanders, fearing the worst."
    n "What if the doctor comes in and tells you you only have a few months left to live?"
    n "You haven't felt like you were gonna pass out in weeks but something still feels off."
    
    show kitsuragi at center with dissolve:
        ypos y_kitsuragi
        
    kitsuragi @ say "Hello [name]. Feeling any better since your last visit?"
    
    player "Yeah. I'm not getting dizzy randomly anymore."
    
    kitsuragi @ say "Good."
    
    player "Still kinda feel like a zombie sometimes though."
    
    kitsuragi @ say "Like a... zombie?"
    
    player "Yeah like shambling around not really aware of my surroundings, where I'm going or how I got there."
    
    kitsuragi @ say "Interesting..."
    
    n "She clicks her pen and writes something in her notepad. By 'interesting', she means 'concerning.'"
    
    kitsuragi @ say "Well you haven't dropped dead yet so that's a good sign."
    kitsuragi @ say "In fact, we weren't able to find a single trace of CORVID in you."
    kitsuragi @ say "Whatever's ailing you is something completely different."
    
    n "Did you hear her right? You *don't* have CORVID-19 like every other human in the last hundred years? You can hardly believe it."
    
    player "You mean I'm *not* dying?"
    
    "The doctor shrugs."
    
    kitsuragi @ say "Hell if I know. All I know is it ain't from CORVID."
    kitsuragi @ say "Could be something genetic or some rare human disease. Kinda hard to predict when human medical sciences are 40 years out of date."
    kitsuragi @ say "The good news is we have tons of options for anthromorph-agnostic medications to help with your symptoms."
    
    n "She writes something in her notepad and tears the page out, handing it to you."
    
    kitsuragi @ say "We'll get you started on opalozine and see how it affects you then move on from there."
    kitsuragi @ say "It's a controlled dose but if your symptoms get worse or if you notice any side effects, stop taking it immediately and call me."
    
    n "You're almost too excited by the fact you're not dying of CORVID to acknowledge you might be dying of something else."
    
    kitsuragi @ say "Hey! Are you listening?"
    
    player "Huh? Oh yeah, read warning on label, take new pill, call if I start frothing at the mouth or pissing blood."
    
    kitsuragi @ say "That's the gist of it."
    kitsuragi @ say "That's really all I've got for you for now."
    kitsuragi @ say "Enjoy your life, just don't do anything stupid."
    
    menu:
        "I will.":
            player "Thanks, I will."
            player "Enjoy my life that is."
            player "But also probably do something stupid."
            
            kitsuragi @ say "Just remember you're not a cat, you only live once. Make the most of it."
            
        "I won't":    
            player "Thanks, I won't."
            player "Do anything stupid that is."
            player "I'll try and enjoy my life haha."
            
            kitsuragi @ say "That's all I can ask of you."
            
    hide kitsuragi with dissolve
    
    n "The doctor sees you to the exit and you hang around the pharmacy to pick up your pills, giving you plenty of time to reflect on everything."
    n "Apparently you have similar symptoms to CORVID-19 but you tested negative for it. Could it have been a false negative?"
    n "No, the doctor seems too sure that's not the case. Is it some new strain that's not detectable by known methods?"
    n "Would it even still be CORVID then if it's that different? She said there wasn't a trace of it in you."
    n "Doesn't it go against basic virology for something to be so contagious when the whole target population is dead?"
    n "Other anthromorphs don't carry it, and you were vaccinated against the only strain you'd been in contact with. Your parents caught it shortly after you were born but it's not supposed to infect infants."
    n "Maybe it really is some random disease like when your stomach hurts for a little too long and it'll go away eventually."
    
    scene bg codadorm with fade
    
    n "With your pills in hand, you returned to your dorm for the evening but you're still too giddy to go to sleep."
    n "You legit thought you might be dying and were ready to give up on everything, but now you have a future to look forward to."
    n "It suddenly hits you that things are going pretty well for the first time in your life. You're in an Ivy League university, you've got friends, your bills are paid... what more could you ask for?"
    n "That's it, you can't just lie in bed when you're so full of positive energy. You've gotta go for a /nightwalk/"
    
    call nightWalks
    
    scene bg black with fade
    
    n "The following day..."
    
    scene bg campus with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Another day in history class where Rose is a bitch to you? Who could have guessed!"
    n "At least you got let out early and can prepare for statistics. There were a few homework problems you should double check."
    n "It can wait until after you get a snack at a vending machine though."
    
    scene bg schoolhallways with dissolve
    
    show box with Dissolve(.2):
        ypos 0
    
    n "You went ahead and made your way to the math building. The snacks stocked here are pretty decent and you need to be here anyway."
    n "Except some jackass is standing in front of the vending machine and apparently can't make up his mind."
    n "Seriously, it's been like two minutes and fourteen seconds and he still hasn't moved."
    
    player "Hey buddy, gonna buy a snack sometime today?"
    
    n "The person tenses up and mumbles something."
    
    rori @ say "S-sorry, I'll just be a second."
    
    player "What the...? Rori?"
    
    n "The ram turns his head around to face you."
    
    rori @ say "Huh? Oh hey [name]!"
    
    player "Dude hurry up and buy something already, I'm gonna be late for class at this rate."
    player "Wait, what are you doing?"
    
    n "You just now notice a wire coming from Rori's sleeve that's plugged into the card swiper on the machine."
    
    player "Are you... hacking?"
    
    rori @ say "Shh!"
    rori @ say "It's not hacking!"
    rori @ say "I'm just tricking the machine into giving me what I want."
    
    player "Sounds like hacking to me."
    
    rori @ say "Maybe it would be if it was actually working."
    rori @ say "I can't believe the random code I pulled off github doesn't function as advertised!"
    
    player "Inconceivable!"
    
    n "Rori pulls on his hoodie and reveals a tiny computer thing he's concealing."
    
    rori @ say "Maybe my blueberry pi just doesn't have enough RAM to crack the security code."
    rori @ say "I knew I should have gotten the 4GB model."
    
    n "Rori sighs and unplugs the wire from the card slot."
    
    rori @ say "Whatever. I've spent enough time here looking suspicious. I'll just pay for snacks like a normie."
    
    n "Rori tries swiping his card but the machine gives an error."
    
    rori @ say "Aw what? Don't tell me I bricked it."
    
    menu:
        "LOL":
            player "It would be funny if you did."
            
            rori @ say "Gosh I hope not. I don't wanna get caught vandalizing one of these. It'd cost a fortune to replace it!"
            
            player "Relax, I don't think anyone noticed you. These things break all the time."
        "Let me try it":
            player "Maybe it just doesn't like your card. Let me try mine."
            
            n "You slap your card against it and it gives the same error. Using the chip reader and magnetic strip yield the same result."
            
            player "Yup you borked it."
        "You're going to jail":
            player "RIP, you're going to jail for this."
            
            rori @ say "D-don't say that!"
            
    n "Rori sighs and leans his back against the machine. He slips down it until he's sitting on the floor."
    
    rori @ say "I just wanted to get free snacks for a special someone."
    
    player "Oh?"
    player "You know you don't have to constantly give someone gifts to impress them."
    
    rori @ say "You don't get it."
    
    n "Man, he is really sulking."
    
    menu:
        "Sit next to him":
            $ roriPoints =+ 1
            
            n "You drop down to the floor along side him."
            n "You end up shoulder to shoulder with him, trying not to be an obstruction to the foot traffic of students who look at you weird, but they're all math autists so who cares what they think."
            n "A sudden tingling sensation runs up your arm, followed by some ticklish feeling on your face like whiskers touching your cheeks."
            n "You look down and see a small fuzzy critter with a big bulging eye staring up at you."
            n "It lets out a squeak before jumping off you and into Rori's hooves."
            
            player "What the fuck?"
        "Remain standing":
            n "You remain on your feet, resolute and dignified."
    
            player "Come on man, you look like a kid throwing a tantrum down there. At least stand up."
    
            n "Rori seems to ignore you, instead drawing circles on the floor with a hoof."
            
            player "Please don't be this autistic, you're obstructing the hallway traffic."
            
            n "Rori slowly starts to rise back to his feet. Wait, what the hell is he holding?"
            
    show rori neutral rat at center with dissolve:
        ypos y_rori
            
    player "Is that the rat from the other week?"
    
    rori @ say "Yup. His eye is messed up so I made a cute little eyepatch for him."
    
    player "You befriended him?"
    
    rori @ say "It wasn't hard. I just kept giving him food."
    rori @ say "That's why I was trying to hack the vending machine."
    
    player "You should have said something!"
    player "Based Robinhood stealing from the rich and giving to the poor starving rats."
    
    rori @ say "Heh I don't think he's starving anymore, not with how much I feed him."
    
    player "What's his name?"
    
    rori @ say "I don't know, I didn't think to ask."
    rori @ say "How about... Guts?"
    
    player "Is that a Berzerk reference?"
    #player "Because he has one eye?"
    
    rori @ say "Yes."
    rori @ say "He's had a rough life and only has one eye so it fits."
    
    player "Nice to meet you, Guts."
    
    rori @ say "I think he remembers you."
    
    player "He better, after all the trouble I went through to get those pretzels for him."
    
    ###have a line that says if you gave your money to the hobo or to lina then you don't have any to buy a snack
    
    player "Do you come here just to see him?"
    
    rori @ say "I have a class here earlier in the day. I just check up on him if he happens to be under the vending machine."
    
    player "That reminds me, I should get to class now."
    
    rori @ say "Okay! Take care!"
    
    player "See you guys later."
    
    n "You hold out a finger for Guts to inspect and you give him a little chin rub."
    
    scene bg campus with fade
    
    n "After class, Gunner tagged along with you as usual, but Rori was nowhere to be found."
    n "Instead you're joined by your Tuesday/Thursday friends."
    
    claire @ say "Look Ava, cute boys!"
    
    ava @ say "Where? Oh you mean these two?"
    
    claire @ say "Who else!"
    
    gunner @ say "Hello ladies~"
    
    player "Watch out Gunner, these two are out for blood."
    
    ava @ say "Ah yes, fluffy bunnies and secretary birds, two of the deadliest predators."
    
    player "I've seen Attack of the Killer Rabbits, I know what you're capable of."
    
    claire @ say "It's true, we can be viscious~"
    claire @ say "I wouldn't mind taking a bite out of you in particular, [name]~"
    claire @ say "I bet humans taste delicious~"
    
    ava @ say "Claire everyone knows rabbits are herbivores."
    
    claire @ say "Don't act like you're not curious about what humans taste like too!"
    
    gunner @ say "Ahem."
    gunner @ say "Speaking of lunch, I was gonna suggest we all go out somewhere to eat."
    
    ava @ say "That's a great idea! I just had back to back exams so I'm starving!"
    
    claire @ say "I just ate but I could go for seconds!"
    
    ###variation depending on if the player is into fat bitches
    player "Hnnnnng."
    
    gunner @ say "I know a good Thai place in town if you're down."
    
    claire @ say "Ooh I love Thai food!"
    
    player "Sounds good to me."
    
    ava @ say "Yeah let's hurry before the weekend crowds come."
    
    gunner @ say "Lines won't be a problem, I know the owner of the restaurant."
    gunner @ say "Last time I had to wait longer than 10 seconds I simply threatened to have my dad's goons burn down his establishment and I've never had any problems since."
    
    ava @ say "..."
    
    gunner @ say "I'll text my roommate Rori and see if he wants to come along!"
    
    scene bg town with fade
    
    show box with Dissolve(.2):
        ypos 0
        
    show ava typical happy at center:
        ypos y_ava
        xoffset 300
    show claire sweater happy at center:
        ypos y_claire
        xoffset 650
    show rori neutral at center:
        ypos y_rori
        xzoom -1
        xoffset -325
    show gunner neutral at center:
        ypos y_gunner
        xoffset -775
        xzoom -1
        
    with dissolve
    
    n "Gunner brought you to a lively restaurant in town and Rori joined up with you on the way."
    n "He was right, the seating was quick for your group despite the long line. He got you an outdoors table, fitting for such a pleasant day."
    n "After ordering drinks, you retreated to the restroom to take care of some business."
    n "When you returned, your group of friends eyed you with sinister expressions."
    
    player "What? Why do you all look so smug?"
    
    #show ava typical daydream
    
    ava @ say "You took so long we decided to go ahead and order for you!"
    
    player "Really? Nothing too expensive I hope..."
    
    #show ava casual smile
    
    ava @ say "Quite the contrary! ...If you can finish it, that is."
    
    n "You raise a brow and are about to ask what she meant when the waitress arrives and sets everyone's meals on the table."
    
    #show waitress at center with dissolve
    
    waitress "Aaaand for you the spicy ramen bowl challenge! Remember, it's only free if you manage to finish it all on your own!"
    waitress "Please sign here so we're not liable for any damages to your short term or long term health. Good luck!"
    
    n "She hands you a pen and paper, which you absentmindedly sign, confused as to why you have to sign something just to have hot sauce in your pasta."
    
    waitress "Thank you~ And here's the one for you too!"
    
    n "The waitress hands the pen and a similar paper to Gunner before setting down his bowl."
    
    waitress "Try not to die!"
    
    n "She does a little bow and heads back inside."
    
    hide waitress with dissolve
    
    rori @ say "Yeesh, it's making my eyes water already. I can even taste it from all the way over here!"
    
    gunner @ say "Hahaha sorry [name] but I swear it wasn't my idea! Ava thought it would be funny to order it for you and well, I didn't want you to suffer alone!"
    
    #show ava casual unimpressed
    
    ava @ say "I was only half serious!"
    #ava @ say "Hehehehe *chirp~*"
    
    claire @ say "You can have some of what I got if it's too spicy for you [name]."
    
    #player "It's fine. I mean, how spicy can it be? It smells pretty good in fact."
    player "It's fine. Humans evolved to eat this kinda stuff. In fact, it smells pretty good!"
    
    #show ava casual happy
    
    ava @ say "You sure? I don't wanna be responsible for killing ya."
    
    player "Yeah! I mean, I didn't have any restaurants like this where I grew up but I always enjoyed spicy food. They probably just hype it up for marketing. How hot could it be?"
    
    gunner @ say "I guess we're about to find out!"
    
    n "Gunner grabs his chopsticks, fumbling with them for a bit trying to grab a slice of beef on top of the noodles."
    
    gunner @ say "Goddammit... fuck... almost... dangit... Where's a fork when you need one? Ah screw it."
    
    n "He stabs the meat with a chopstick and puts it in his mouth while the whole squad watches with curiosity and anticipation."
    
    rori @ say "Well. He's not dead yet."
    
    n "Gunner finishes chewing and swallows."
    
    gunner @ say "Huh. That was... not so ba-"
    
    n "He suddenly wheezes and reaches for his drink, downing half the cup before setting it down."
    
    gunner @ say "Okay it doesn't hit you at first but when it does it's like getting hot brass down your shirt."
    gunner @ say "Still not the spiciest I ever had though."
    
    ava @ say "I think it's supposed to get spicier the further down you go."
    
    #player "A real 9 circles of hell, I'm sure."
    
    #show claire outdoors derp
    
    claire @ say "Alright [name], your turn!"
    
    #show claire outdoors neutral
    
    n "Unlike Gunner, you actually know how to use chopsticks and pick up a clump of noodles to slurp. It doesn't taste any different than the generic spicy ramen you could find at any grocery store."
    
    player "Heh, easy."
    
    n "And then it hits you."
    n "You cough uncontrollably for a few seconds as you frantically reach for your drink, taking a few sips until the fire in your mouth has been extinguished."
    
    player "Ack! You were right, it does have a delayed kick to it."
    
    gunner @ say "I told you! Here Rori, have some of this."
    
    rori @ say "What? No way! Keep your peppers off my lemongrass tofu!"
    
    #show ava casual smile
    
    ava @ say "What's the matter, don't think you can finish it all on your own?"
    
    gunner @ say "I'm sure I could, I just dunno if the discount is gonna be worth being bathroom-bound all day tomorrow."
    
    n "You silently take another, smaller bite. You're already sweating."
    
    #show ava casual overjoyed
    
    ava @ say "Look, [name] can do it just fine!"
    
    gunner @ say "Yeah but look how much he's sweating though!"
    
    player "We humans evolved to eat food like this not out of necessity but out of pure dumbfuckery and stubbornness."
    
    #show ava casual flattered
    
    #n "The group snickers at your self-deprecating joke."
    n "As Ava takes a bite out of her meal, Claire leans in and whispers something to her, causing her feathers to floof up and almost makes her choke on her food."
    
    ava @ say "Whaaaat? Claire oh my gosh no!"
    
    gunner @ say "What? What did she say?"
    
    ava @ say "Nothing hahaha nothing!"
    
    #show claire outdoors embarassed
    
    claire @ say "All I'm sayin' is that he's competitive! He'd totally be down for it!"
    
    gunner @ say "What???"
    
    #show claire outdoors derp
    
    claire @ say "I just said there should be a prize for whoever finishes their spicy bowl first!"
    
    #show ava casual annoyed
    
    ava @ say "Claire shush!"
    
    n "Gunner's ears perk up."
    
    player "What sort of prize?"
    
    #show claire outdoors lusty
    
    n "Claire giggles and winks at you."
    
    claire @ say "Whatever you want bby~"
    
    ava @ say "She suggested something rather... spicy."
    ava @ say "Which I'm not gonna do."
    
    claire @ say "But there has to be a priiiiiize!"
    
    ava @ say "There already is one! The bowl is free if you finish it!"
    
    claire @ say "There needs to be one for whoever does it first!"
    
    ava @ say "Well I'm not gonna suck the winner's dick just because they can eat spicy food!"
    
    gunner @ say "OwO"
    
    claire @ say "How about just holding his hand? Or is that still too lewd for you?"
    
    ava @ say "Well... I guess I can do that."
    
    gunner @ say "Sounds like we've got a competition then, [name]!"
    
    player "Can I choose who I hold hands with when I win?"
    
    n "Your friends all look to each other and mutter in agreement."
    
    gunner @ say "Yeah, I don't see why not. Other than the fact that you *won't* be winning this."
    gunner @ say "Hope you won't be too jealous when I walk home holding Ava's wing~"
    
    default holdingHands = "No one"
    
    menu:
        "Do it for Ava":
            $ avaPoints =+ 2
            $ holdingHands = "Ava"
            
            player "Maybe in another one of your lives catboy, because tonight I'll be the one walking her home."
            
            claire @ say "Gee Ava, how come you get *two* cuties competing for you?"
            
            if avaPoints > 4:
                ava @ say "Maybe I'm just that irresistable!"
                ava @ say "Do your best you two~"
            else:
                ava @ say "I dunno but this should be fun to watch!"
                ava @ say "Just try not to die, you two."
                
        "Do it for Rori":
            $ roriPoints =+ 2
            $ holdingHands = "Rori"
        
            player "Nah, I'm gonna win and hold hooves with Rori all the way back to the dorms."
            
            rori @ say "*Bleat!*"
            rori @ say "W-why me?"
            
            player "Because you're cute and those hooves were made for holding human hands."
            
            if roriPoints > 4:
                rori @ say "Well, I guess we can hold hands just this once..."
                
                n "Rori tries to hide his smile but you can see it in his eyes, he wants you to win."
            else:
                rori @ say "If you say so..."
            
            claire @ "D'awww you two are so adorable!"
            
            gunner @ say "..."
            gunner @ say "Whatever floats your boat bro."
        "Do it for Claire":
            $ clairePoints =+ 2
            $ holdingHands = "Claire"
            
            player "Nah, I'm gonna win and hold Claire's paw all the way back to her dorm."
            
            if clairePoints > 4:
                claire @ say "You can hold my paws in my dorm too, all the way til morning~"
                
                ava @ say "Claire! You perv!"
                
                claire @ say "Who's gonna be the pervert when you'll be watching us?"
                
                ava @ say "If [name] wins I'm locking you out of our dorm."
            else:
                claire @ say "R-really?!"
                
                player "At least to your dorm. Maybe further."
                
                claire @ say "Oh yeah, we're definitely going further~"
            
        "Play the reverse card":
            $ avaPoints += 1
            $ holdingHands = "Gunner"
        
            player "The only hand you'll be holding is mine after I win."
            
            n "Gunner nearly spits out his drink."
            
            gunner @ say "Say what?!"
            
            #n "Ava snickers"
            
            #ava @ say "Ooh now I don't know who to root for~"
            ava @ say "Ooh now that would be fun to see~"
            
            claire @ say "My favorite crack ship."
            
            rori @ say "You'll never be able to make gay jokes again, Gunner."
            
            #gunner @ say "If anything, I'll become even more homophobic if I have to hold [name]'s hand."
            
            show gunner eyesclosed smile
            show rori sleepy
            show ava typical unimpressed
            show claire sweater surprised earsup
            
            gunner @ say "Do not underestimate my homophobia."
            
            claire @ say "He's too powerful!"
        
        "I literally don't care":
            $ avaPoints =- 1
            $ clairePoints =- 1
            $ roriPoints =- 1
            $ holdingHands = "No one"
        
            player "I don't care about holding anyone's hand, I'm just doing this to make you lose, catboy."
            
            gunner @ say "A man with nothing to fight for but the sake of fighting. I don't know wether to admire you or pity you."
            
            player "Both works."
            
            gunner @ say "Both it is."
    
    gunner @ say "Enough talking! Let's get this competition started already!"

    n "You and Gunner dig into your bowls, haphazardously taking large bites to get through it quicker."
    n "Gunner is getting better at using the chopsticks, grabbing whole clumps of noodles at once."
    n "Your tongue stings and soon your water runs out. You take to chewing on ice cubes to dull the pain."
    
    claire @ say "Look at 'em go!"
    
    ava @ say "Are you two alright? [name], you are *drenched* in sweat right now."
    
    n "You give a thumbs up and do your best to smile through your suffering."
    
    gunner @ say "Roriii!"
    gunner @ say "Lemme have your drink! I'll give you a thousand dollars for it!"
    
    rori @ say "Hm. No."
    
    gunner @ say "Whaaaaat?! Come on! Two thousand?"
    
    n "Gunner is panting like a dog and tears are running down his cheeks."
    
    gunner @ say "Five grand? That's all I brought with me!"
    
    rori @ say "Sorry but I'm enjoying watching you suffer too much."
    
    n "The pain is unbearable at this point. Your mouth is on fire and you're feeling woozy."
    n "Should you press on?"
    
    menu:
        n "{cps=0}Should you press on?{/cps}"
        "Keep going":
            $ spicyVictory = True
            
            n "No, you're not giving up. You can do this. You must assert your dominance!"
            n "You're nearing the bottom of the bowl now. Gunner is struggling with his last few bites."
            n "Your vision goes blurry and your hands tremble but you do not yield."
            n "Your very existence is pain but you've learned to live with it. Embrace it. You just have to swallow one more time."
            
            claire @ say "Oh my gosh he actually did it!"
            
            player "I-"
            
            stop music fadeout 1.0
            
            scene bg black

            pause .65
            
            scene bg hospital with fade
            
            show box with Dissolve(.2):
                ypos 0
            
            #play music "audio/music/vylet - tenderness.ogg" fadein 1.5
            
            n "Urgh... you feel like death. Every breath you take hurts. Your mouth is numb but you can feel your intestines are punishing you for your hubris."
            n "You can't remember a thing after winning your little contest. You must have passed out."
            
            show kitsuragi at center with dissolve
            
            kitsuragi "Hello again [name]. I wish I could say it's nice to see you again, but the story your friends told me when they dragged you here has left me appalled by your stupidity."
            
            player "It was worth it."
            
            kitsuragi "I'm sure it was."
            #kitsuragi "Anyway, you may be dying but you could at least try not to reduce your lifespan any further."
            #kitsuragi "I guess my speech about not doing anything stupid fell upon deaf ears."
            kitsuragi "I guess my advice about not doing anything stupid fell upon deaf ears."
            
            player "How long am I gonna be stuck here this time?"
            
            kitsuragi "Now that you're awake you're free to go. Take this to the pharmacy, they'll give you some pills to settle your stomach."
            
            n "She hands you a note that just says BUTTHURT with three underlines."
            
            kitsuragi "Now get out of my hospital."
            
            hide kitsuragi with dissolve
            
            n "The doctor leaves the room, leaving you to ponder your life decisions and muster the energy to get up, trying not to put undue stress on your abdomen."
            n "When you reach the hospital lobby you're surprised to see your friends there waiting for you."
            
            show ava typical happy at center:
                ypos y_ava
                xoffset 300
            show claire sweater happy at center:
                ypos y_claire
                xoffset 650
            show rori neutral at center:
                ypos y_rori
                xzoom -1
                xoffset -325
            show gunner neutral at center:
                ypos y_gunner
                xoffset -775
                xzoom -1
                
            with dissolve
            
            
            gunner @ say "Looks like the legend is back among the living!"
            
            rori @ say "[name]! Are you okay?"
            
            claire @ say "We were afraid we like, totally killed you! Ksksksksks!"
            
            ava @ say "You didn't have to do all that just to impress us you know!"
            #ava @ say "But it was still impressive..."
            
            player "But it was impressive, was it not?"
            
            if holdingHands == "No one":
                ava @ say "Mmh, I suppose it was... for a human!"
                
                player "What's that supposed to mean?"
                
                ava @ say "Oh nothing~"
                ava @ say "We're just glad you survived!"
                
                player "Me too. I think I'm gonna be out of commission for the next few days though."
                
                claire @ say "That's alright! Come on, let's walk you home~"
                
                player "You all didn't have to wait on me you know."
                
                gunner @ say "What and just leave you here to die alone? Not a chance!"
                
                rori @ say "We shouldn't have even ordered that stupid dish for you."
                
                claire @ say "Yeahhh our bad. We didn't think it would be like \"go to the hospital\" levels of spicy!"
                
                player "It's alright guys, I had a good time."
                
                ava @ say "So did we!"
                ava @ say "You should have seen the looks on your faces!"
                
                gunner @ say "Hey in our defense those spices are specifically designed to be used as torture devices!"
                
                ava @ say "Birds can eat them just fine!"
                ava @ say "You mammals are so silly~"
                
                rori @ say "It's true, birds have no receptors to taste capsaicin."
                
                claire @ say "She may be able to handle the peppers but can she handle *my* spiciness?~"
                
                ava @ say "I don't think anybody can~"
                
                claire @ say "Ksksksks I'll take that as a compliment~"
                
                n "Eventually you manage to corale your friend group out of the hospital and stop them from making a scene."
                n "Your gut still hurts but you have no regrets."
                n "You'll be out of commission for at least a day or two. Hopefully you didn't just cause permanent damage to your digestive tract."
                
            else:
                player "Now where's my prize?"
                
                n "You hold out your hand expectantly."
            
                if holdingHands == "Ava":
                    ava @ say "After all the trouble you went through, I suppose you deserve it~"
                    
                    if avaPoints > 5:                    
                        n "Ava smiles and wraps her wing around your arm."
                    else:
                        n "Ava takes your hand in her wing. Her feathers are so soft, you can't resist stroking them with your thumb."
                        
                        ava @ say "Hey, watch the plumage! They only go in one direction."
                        
                        player "Woops sorry."
                        
                        n "You hastily straighten out her feathers."
                        
                    gunner @ say "It should have been meeeeee!"
                    
                    player "I have two hands, you can hold my free one."
                    
                    gunner @ say "Not what I meant!"
                    
                    ava @ say "Better luck next time!"
                    
                    claire @ say "And if you strike out again, I know a lonely bunny gal who could keep you company~ Ksksksksks!"
                    
                    n "Gunner shudders."
                    
                    gunner @ say "Ugh. We gonna go back home or stand in the hospital lobby all night?"
                    
                    rori @ say "Yeah, we should head home. It's gotten pretty late."
                    rori @ say "Plus we're kind of making a scene here."
                    
                    n "Basking in the glory of holding Ava's wing, you make your departure from the hospital with your entourage of fluffy companions."
                        
                    if avaPoints > 4:    
                        scene bg codadorm with fade
                        
                        n "Ava leaned on you as you walked back towards campus."
                        n "Almost like she likes you or something. Weird."
                    
                    n "It even seemed like she wanted to stay with you a while longer but your tummy hurts too much and you just want to sleep it off."
                    
                if holdingHands == "Claire":
                    claire @ say "Oh yeah I almost forgot!"
                    
                    n "Claire grabs hold of your hand like she's trying to break it."
                    
                    player "Ow! Ease up some."
                    
                    claire @ say "Sorry, I got a little too excited."
                    
                    n "She relaxes her grip just slightly. You wouldn't be able to break free even if you wanted to."
                    
                    ava @ say "Totally not desperate at all. Nope, not one bit."
                    
                    if clairePoints > 4:
                        claire @ say "I'm never letting go!"
                        
                        player "I guess this is my life now."
                        
                        ava @ say "Try not to sound so excited, [name]!"
                        
                        claire @ say "Are you not happy to hold my paw...?"
                        claire @ say "I thought this is what you wanted."
                        
                        player "I literally risked my life for this moment, why wouldn't I want this?"
                        
                        claire @ say "Ohmygosh you're right! You *could* have died!!"
                        
                        ava @ say "Don't be so dramatic."
                        
                        claire @ say "All just to hold this little bunny's paw?"
                        
                        gunner @ say "\"Little?\""
                        
                        claire @ say "Well I'm all yours now, [name]! Take us back to your dorm and I'll show you what hand holding is all about~"
                        
                        rori @ say "Maybe don't say that super loud in a public setting?"
                        
                        player "Alright, how about we all just head outside?"
                        player "Oh and your paw is very nice to hold by the way."
                        
                        n "You feel Claire's weight tug on you as her body goes limp. Her knees tremble, yet she maintains her grasp on your hand."
                        n "She fans her blushing face with her free paw."
                        
                        claire @ say "Y-yeah it is pretty hot in here, don't you think? *Gulp* haha I feel like I'm about to faint...!"
                        
                        ava @ say "Good thing we're in a hospital in case you do."
                        
                        gunner @ say "Come on guys, exit's this way."
                        
                    else:
                        claire @ say "Don't be jealous~"
                        claire @ say "Well, it's okay to be a little jealous! Who *wouldn't* wanna hold a human male's hand?"
                    
                        gunner @ say "Me."
                        
                        claire @ say "You don't know what you're missing out on~"
                        
                        ava @ say "What's it like?"
                        
                        claire @ say "It's like a fine leather that's warm to the touch and fits perfectly in my paw with a firm yet gentle grasp!"
                        
                        rori @ say "That does sound kinda nice..."
                        
                        gunner @ say "If you guys are done gushing over your human hand fetish, can we please go home?"
                        
                        claire @ say "I could gush more but yeah I'd rather head to [name]'s dorm ASAP."
                    
                    n "You and your crew of fluffy companions file out of the hospital and headed back toward campus."
                    n "Claire was giddy the whole way but the pain in your stomach began to flare up after walking so much."
                    n "She practically begged to stay with you when you reached your dorm but the others managed to pry her off you so you could rest."
                    
                if holdingHands == "Rori":
                    n "Rori looks around shyly before nervously grabbing onto your pinkie finger."
                    
                    player "What is that? You call that hand holding?"
                    
                    rori @ say "Ack! Sorry!"
                    rori @ say "I've never held someone's hand before!"
                    
                    claire @ say "Aww, you're taking away his hand holding virginity!"
                    
                    rori @ say "D-don't say it like that!"
                    
                    n "You pull Rori's hand closer and interweave your fingers between his hoof-finger things."
                    
                    rori @ say "O-o-oh my goshhh t-this is really happening...!"
                    
                    if roriPoints > 4:
                        player "Don't be shy, you know you want this."
                        
                        rori @ say "Maybe, just a little..."
                    
                        gunner @ say "LOL he wants more than just some hand holding."
                    else:
                        player "See? That's not so bad, now is it?"
                        
                        n "You can feel how tense Rori is through his hand."
                        
                        rori @ say "Y-yeah, just two bros holding hands because of some silly bet! Nothing else to it!"
                        
                        gunner @ say "Holy cope lmao"
                        
                    rori @ say "Shut up! Don't ruin this moment!"
                        
                    gunner @ say "Okay bro, chill."
                    
                    ava @ say "Well I think you two look pretty cute together!"
                    
                    if avaPoints > 5:
                        n "She mutters something under her breath."
                        
                        ava @ say "But me and [name] would be even cuter..."
                        
                    rori @ say "Heh, thanks."
                        
                    player "Shall we head back to the dorms then?"
                    
                    rori @ say "Ba-a-a-ah! Of course!"
                    
                    if roriPoints > 4:  
                        rori @ say "But could we maybe take the scenic route? It's a nice night out and..."
                        
                        player "And you wanna hold my hand a little longer. Gotchya."
                        
                        rori @ say "Something like that...!"
                        
                        claire @ say "D'awww~"
                        
                        gunner @ say "Ick."
                        
                    scene bg black with fade
                    
                    n "Rori eventually got more comfortable holding your hand as you walked back to your dorm."
                    n "It became so natural that he didn't want to let go."
                    n "But all good things must come to an end. You thought about inviting him to stay for a sleepover but your tummy had started hurting again and you just wanted to rest."
                        
                    
                if holdingHands == "Gunner":
                    gunner @ say "... You're serious?"
                    
                    player "I didn't dominate you in our competition to *not* hold your paw."
                    
                    claire @ say "Come on, a deal's a deal, Gunner!"
                    
                    ava @ say "Haha yeah just do it! It'll be really funny haha OvO"
                    
                    rori @ say "What's the matter Gunner? Afraid you'll turn gay?"
                    
                    gunner @ say "Shut up, there's nothing gay about holding your homie's hand."
                    
                    n "The cat snatches your hand, trying his best to act nonchalant about it but he can't hide the disgusted look on his face."
                    n "His claws dig into your flesh. He's trying to get you to let go but he underestimates your stubbornness."
                    
                    player "Great! How about we go for a walk through campus now?"
                    
                    gunner @ say "Really bro?"
                    
                    n "Rori snickers and pulls out his phone, snapping a pic of you and your catty cohort with a loud shutter sound."
                    
                    gunner @ say "DELETE THAT!"
                    
                    rori @ say "lol no"
                    
                    n "Gunner lunges to grab Rori's phone but you restrain him."
                    
                    player "Bad kitty!"
                    
                    n "He hisses at you while the rest of the group laughs. Eventually he settles down and accepts his defeat."
                    
                    ava @ say "You two are so cute together! You should hold hands more often~"
                    
                    claire @ say "Yeah Ava's definitely gonna be writing fanfiction about this later."
                    
                    ava @ say "Shush, you!"
                    
                    gunner @ say "The things I put up with to have a chance with a hot secretary bird."
                    
                    claire @ say "Yaoi is so fucking hot."
                    
                    rori @ say "...Bet."
                    
                    gunner @ say "I have no idea why girls are so into this sort of thing."
                    
                    player "Because if one guy is hot then two guys is twice as hot."
                    
                    gunner @ say "Yeah but two guys *together???* What does the woman even get out of this?"
                    
                    ava @ say "Snrk"
                    ava @ say "I'll cut you a deal Gunner, anything you do with [name] while holding hands, I'll do with you~"
                    
                    gunner @ say "Yeah? Well I don't think [name] is gonna let me bend him over and-"
                
                    ava @ say "Before you finish that statement let me be clear that I'm just joking around...!"
                    
                    n "Well? Should you draw out this \"\"\"purely hypothetical\"\"\" scenario to fulfill Ava's desires?"
                    
                    menu:
                        "Aw hell no!":
                            $ rejectedAvasproposal = True
                        
                            n "Aw hell no, you're not letting Ava's indecisiveness decide your actions!"
                            n "You won't indulge in her degenerate fantasies, to play the role of the bottom in some college chick's gay porno ideas. That bird needs to pick a side already!"
                            
                            player "Oh suuuure, let me suck Gunner's dick so he can get some beak later."
                            
                            show gunner cheeky1
                            show ava typical enamored
                            show claire sweater surprised earsup
                            show rori worried noblush
                            
                            gunner @ say "You'd do that? For me...?"
                            
                            player "Hell no!"
                            #player "I'm like an ozone molecule, I form strong bonds in pairs, not trios!"
                            
                            #rori @ say "Ozone is O3, not O2."
                            
                            #player "Well fuck, there goes my college student tier analogy."
                            
                            #player "Ever heard of pairbonding?"
                            #gunner @ say "Well right now it looks like you're pairbonded to *me*"
                            
                            player "I don't want any part of this isoceles love triangle shipwreck-in-progress!"
                            
                            claire @ say "That's right! Human males are for pairbonding only!"
                            
                            n "Ava looks a bit disappointed but quickly stows it away."
                            
                            ava @ say "H-hey it was just a funny thought that popped into my head is all! No need to get so defensive!"
                            
                            n "Gunner shakes his head, seemingly achieving some sense of clarity."
                            
                            gunner @ say "[name]'s right, I could never allow my dick to be touched by another man, not even for guaranteed bird sexo. That would be hella gay."
                            # I just don't swing that way."
                            gunner @ say "Besides..."
                            
                            n "Gunner snaps his paw and winks at Ava."
                            
                            gunner @ say "I don't need a cheap trick like that to win in the end~"
                            gunner @ say "Sometimes you have to lose the battle and hold your bro's hand to win the war."
                            
                            ava @ say "Hmm..."
                            ava @ say "In that case, may the best man win!"
                            
                            claire @ say "I call dibs on the loser!"
                            
                            gunner @ say "...Now I definitely have to win."
                            gunner @ say "Come on, let's get out of here before anybody important sees me like this."
                            
                            n "You made your way back to campus, holding Gunner's paw the whole time. You revelled in how uncomfortable it made him and thwarted his attempts to escape."
                            n "Only when you reached your dorm did you mercifully release him."
                        "Just a smooch":
                            n "You don't know if you're ruining your chances with Ava or boosting them but you're doing this for the memes."
                            
                            player "Best I can do tonight is a smooch."
                            
                            n "Gunner turns his eyes toward Ava, then back to you, then back to Ava before finally coming to a stop looking at you with a mixture of apprehension and gratitude."
                            
                            gunner @ say "...For real?"
                            
                            player "I mean we're already holding hands."
                            player "What's one little kiss gonna do?"
                            player "Aside from giving these fujoshis a nice show that is?"
                            
                            ava @ say "Yes... Ha ha ha... {u}yes{/u}!"
                            
                            gunner @ say "Ughhh you drive a hard bargain!"
                            gunner @ say "This is a classic strong-arming technique I read about in \"The Art of the Deal\" where you try and turn someone's homies into homos."
                            gunner @ say "And to that I say no deal."
                            
                            ava @ say "Aww..."
                            
                            player "Don't worry, he'll come around to the idea."
                            
                            claire @ say "Shoulda bargained better."
                            claire @ say "Offer him a blowie next time!"
                            
                            ava @ say "Claire please."
                            
                            claire @ say "What? That's just common business sense! There's a whole chapter about it in \"The Art of the Deal!\""
                            
                            gunner @ say "Too late, my decision is final!"
                            gunner @ say "Now let's get out of here before anybody important sees me like this."
                            
                            n "You made your way back to campus, holding Gunner's paw the whole time. You revelled in how uncomfortable it made him and thwarted his attempts to escape."
                            n "Only when you reached your dorm did you mercifully release him."
                            
                            
                            
                            
                        "Suggest a compromise":
                            $ rejectedAvasproposal = True
                        
                            player "What? Why do I have to be the bottom?"
                            player "If Ava wants us so bad she can bottom for both of us."
                            
                            ava @ say "T-that...!"
                            ava @ say "...Could actually be arranged~"
                            ava @ say "Purely in a hypothetical sense of course! As a philosophical exercise!"
                            
                            claire @ say "Holy shit they're actually planning a threesome."
                            
                            rori @ say "I know, it's insane."
                            
                            ava @ say "Quiet you two! We're merely discussing the complex social dynamics of intersecting bonding rituals!"
                            
                            claire @ say "Who gets your beak and who gets your tailfeathers?"
                            
                            ava @ say "It's none of your business!"
                            
                            n "You feel Gunner's paw grip tightly around your hand, trembling. You'd almost forgotten that you were bound to him in this way."
                            n "Seeing you two forced to act as an inseperable pair sure is doing a number on Ava, huh?"
                            
                            claire @ say "Fine, keep your secrets! I'll just ask them directly which they'd prefer!"
                            claire @ say "Well? Which would it be, [name]?"
                            
                            menu:
                                "Beak":
                                    n "This conversation is rapidly approaching critical levels of awkwardness. This is definitely not the topic you should be discussing in a hospital lobby at 9PM."
                                    n "You can barely utter out the word."
                                    
                                    claire @ say "Don't try and weasel out of this one, you knew what you were getting into when you suggested a compromise!"
                                    
                                    player "B... Beak."
                                "Tailfeathers":
                                    n "This conversation is rapidly approaching critical levels of awkwardness. This is definitely not the topic you should be discussing in a hospital lobby at 9PM."
                                    n "You can barely utter out the word."
                                    
                                    claire @ say "Don't try and weasel out of this one, you knew what you were getting into when you suggested a compromise!"
                                    
                                    player "T... Tailfeathers."
                                
                            claire @ say "There, I just got you some new fanfic material~"
                            
                            ava @ say "Haha y-yeah just some harmless fanfiction..."
                            
                            n "Gunner appears to be stumped, weighing his options and chances carefully. He suddenly clears his throat and speaks up."
                            
                            gunner @ say "Okay enough of the hypothetical bullshit."
                            gunner @ say "There will be no threesomes unless it's with me, Ava, and Ava's twin sister."
                            gunner @ say "It's all or nothing with me. No compromises."
                            
                            rori @ say "Wow, that's actually... kinda based of you."
                            rori @ say "Or at least it would be if I didn't know you're just afraid of seeing [name]'s dick."
            
                            gunner @ say "Each piece has its role in the grand scheme of things."
                            gunner @ say "I know there's at least one timeline where maximizing my homophobia stat gets me a waifu."
                            
                            player "Hey, if it works good for you."
                            
                            n "Ava finally manages to shake off her horny stupor and feel shame after getting turned down."
                            
                            ava @ say "Haha it was all just a fun hypothetical to ponder anyway! *Yaaawn* is anybody else sleepy? I think we should all forget about this and go to bed."
                            
                            gunner @ say "Agreed."
                            
                            scene bg black
                            
                            n "You made your way back to campus, holding Gunner's paw the whole time. You revelled in how uncomfortable it made him and thwarted his attempts to escape."
                            n "Only when you reached your dorm did you mercifully release him."
                            
                n "It was nice to hold someone's hand all the way back to your dorm though. Makes you feel special."
                n "You should find a way to do it without accepting stupid challenges and tearing up your guts."
                n "The rest of your weekend is spent huddled in a fetal position in bed, recovering from the tummy ache of the century. You won, but at what cost?"
                
                jump chapter3AfterWeekend
                            
                            
        "Concede":
            n "You can't... You just can't go on."
            n "This isn't worth it."
            n "You're feeling woozy and tears are streaming down your cheeks. Is this really worth it?"
            n "If you take one more bite, you're pretty sure you'll be out of commission for the rest of the weekend."
            n "Maybe it's time to give up."
            
            player "That's it, no more."
            
            n "You sit there, brain fried from the traumatic spices, suckling on an ice cube as Gunner finishes his bowl and claims victory."
            
            gunner @ say "THROUGH THE FIRE AND FLAMES, I EMERGE VICTORIOUS!"
            gunner @ say "*Inhales*"
            gunner @ say "AAAAAAAAAAAAAAAAAAA!!!!"
            
            n "The waitress comes by and refills your drinks. Gunner chugs his in one go."
            
            gunner @ say "EVEN THE WATER BURNS!!!"
            
            ava @ say "You alright, big guy?"
            
            gunner @ say "Not really but whatever."
            gunner @ say "I am in"
            gunner @ say "so much pain right now."
            gunner @ say "But it'll be worth it to hold your wing."
            
            n "Ava stifles a giggle."
            
            ava @ say "Oh pft. Fine. I said I would, and I guess you do kinda deserve it."
            
            rori @ say "You put up a good fight, [name]. It just wasn't meant to be."
            
            claire @ say "You put on a good show too!"
            
            ava @ say "You boys looked so silly~"
            ava @ say "Mind if I try a bite, [name]?"
            
            player "You sure? It's kinda spicy."
            
            ava @ say "Oh I think I can handle it~"
            
            n "Ava reacher over with her fork and takes a stab at your red hot molten lava in a bowl."
            n "You watch in horror as she takes a big bite and swallows it."
            
            ava @ say "Hmm. Kinda bland if you ask me."
            
            gunner @ say "The fuck?"
            gunner @ say "How can you eat something so spicy? Are you Mexican or something?"
            
            ava @ say "Breee~ A magician never reveals her secrets!"
            
            rori @ say "Birds don't have receptors of capsaicin, so they can't taste spicy foods."
            
            ava @ say "Ya got me! Hehe it was fun watching you guys struggle with something so mild!"
            
            gunner @ say "Well I'm glad we could offer some amusement for the night."
            gunner @ say "I am never doing this again."
            
            player "Same."
            
            scene bg black with dissolve
            
            n "The rest of the night was a blur. You felt like you were going to pass out a few times but you managed to hold it together."
            n "Gunner was kind enough to pay for your meal but not kind enough to avoid gloating as he held Ava's wing on the way back to campus."
            
            scene bg codadorm with fade
            
            n "You wake up feeling dizzy, almost kinda hungover."
            n "Your poor intestines are still groaning in pain even after you made several trips to the bathroom."
            n "Last night was not worth the trouble just to lose."
            
            if holdingHands == "Ava"
                call phone_start from _call_phone_start_53 

                call message_start("Ava", "Hey [name]! You doing alright?", "avaavi.png") from _call_message_start_70 
                call message("Ava", "Thought I'd check in on you", "avaavi.png") from _call_message_391 

                call reply_message("Yeah, jsut hating every moment of existence.") from _call_reply_message_290 
                
                call message("Ava", "Oof, sorry about last night", "avaavi.png") from _call_message_392 
                call message("Ava", "I thought for sure you'd win!", "avaavi.png") from _call_message_393 
                
                call reply_message("Really? I guess we both underestimated Gunner") from _call_reply_message_291 
                
                call message("Ava", "He's pretty determined, you gotta give him that!", "avaavi.png") from _call_message_394 
                call message("Ava", "Better luck next time~", "avaavi.png") from _call_message_395 
                
                call reply_message("yeah lol") from _call_reply_message_292 
                
                call phone_end from _call_phone_end_62
                
                n "You're getting pretty tired of this love triangle bullshit."
                n "You'd go over and kick Gunner's ass right now if your stomach wasn't in constant agony."
            
            else:
                "Your stomach is still in unrelenting agony so you're just gonna take it easy for now."
            
            n "All you can do today is lie in bed and study while idly browsing the web."
                
            scene bg black with dissolve
            
            scene bg codadorm with dissolve
            
            n "Your intestines have finally settled and you're feeling well enough to go out."
            
            call afterClassOptions
            
        
        jump chapter3AfterWeekend
        
label chapter3AfterWeekend:
    #knock over rose's cassette player in class on accident, can give her the repair gear if you have it or offer to cashapp her but she doesn't have the app (or a phone)
    n "Monday again."
    n "At least your guts are no longer begging for death after Friday's dinner and you can return to class in peace."
    
    n "The classroom is pretty lively by the time you arrive. Everyone's chatting and laughing except for Rose."
    n "She sits with her head facing towards the window, staring out at the courtyard. A small rectangular box sits on her desk with a wire snaking around and splitting off into two ends that terminate at her ears."
    n "Weird, it doesn't look like any phone you've seen before."
    n "As you're squeezing between the row of desks you hear something fall to the ground with the sound of clattering plastics and shattering glass."
    n "The whole room goes silent and all eyes are on you."
    
    rose @ say "Hey!"
    
    n "Tiny paws pull at your shirt and you come face to face with a pissed-off raccoon."
    n "She's standing atop her desk and only barely matches your height."
    
    rose @ say "Pick that up. Now!"
    
    n "She points to all the pieces of her contraption scattered across the floor."
    
    menu:
        "Refuse":
            $ rosePoints =- 1
            
            player "You've got hand-like paws, pick it up yourself."
            
            rose @ say "You fucking knocked it over!"
            
            player "And who's fault is that? Try not leaving your toys hanging precariously over your desk next time."
    
            ###knife sprite
    
            rose @ say "I'm going to kill y-"
        
            rothbauer @ say "Good morning class! I hope you're all had a nice weekend!"
            
            n "Rose silently folds her knife and sits back in her chair."
            n "She reaches down and picks up the main body of the device. The individual plastic pieces have all popped out of their sockets."
            n "You can see now it was one of those old portable cassette players. The tape is still inside, albeit spilling out of the cassette itself in an unholy tangled mess."
            n "Rose sighs and tosses the chassis into her bag, not even bothering with the other pieces strewn about the floor."
            n "She spends half the class sullenly untangling the tape and spooling it back into the cassette."
            n "To your surprise, she doesn't stab you after class. She just picked up her bag and left, looking too sad to be angry."
        
        "Comply":
            player "O-okay."
            
            n "You drop down to your knees and pick up every bit you find and deposit it onto Rose's desk."
            
            rose @ say "Ugh, what am I supposed to do with broken pieces of plastic and shards of glass? Kindly cut your throat open with those if you find a piece that's long enough."
            
            player "I'll get right on that."
            
            n "Rose slots the pieces back together as you find them, though some are obviously too broken to be repaired like the window and some clips."
            n "You've gathered all the parts, or at least all the ones you can see from this aisle. Wait, there's one more under your desk."
            n "You reach for it and pass it up to Rose before sitting in your chair."
            
            rose @ say "Is that the flywheel? God dammit it's cracked to hell. Cheap piece of shit plastic, probably made by inferior human hands..."
            rose @ say "You're paying for this!"
            
            if gnugift = True:
                $ rosePoints =+ 1
                n "Wait a minute, that looks just like the gizmo that based homeless guy gave you."
                n "You've been carrying it around just like he said and now it finally has a use."
                
                player "Wait a second, try using this."
                
                n "You hold out the wheel to her. She gives you a skeptical look."
                
                rose @ say "Why do you have one of these?"
                
                player "That psychic hobo told me to!"
                
                rose @ say "Do you always take advice from crackheads?"
                rose @ say "This probably isn't going to work but I'm desperate enough to try it."
                
                n "Rose slots the flywheel into place and wraps a rubber band around it, connecting it to another series of wheels and gears within the cassette box."
                n "Her eyes go wide when she presses the play button and the rotors spin, pulling the tape along and producing muffled music from the earphones."
                
                rose @ say "It... actually works!"
                rose @ say "That's one hell of a coincidence."
                
                player "It's no coincidence, I think that guy could really see the future!"
                
                rose @ say "I see a future where he steals your kidneys if you meet again."
                
                player "You should thank him for giving me that piece to fix your cassette player!"
                
                rose @ say "No, *you* should watch where you're going next time and avoid knocking over my things in the first place!"
                
                n "You mutter under your breath."
                
                player "Maybe don't leave fragile objects leaning off your desk..."
                
                rose @ say "What was that?"
                
                rothbauer @ say "Good morning class! Let's get right into it today, why don't we!"
                
                n "Thank you professor, you came in at just the right time to get Rose off your back."
            else:
                player "For the wheely thing?"
                
                rose @ say "For the whole thing! It's ruined!"
                
                player "Okay okay, so like how much? 5 bucks? 10?"
                
                rose @ say "You just destroyed a vintage Walkfan WM-3X Special Edition, of which there are only like a dozen left in the world!"
                
                player "So it's priceless is what I'm hearing."
                
                rose @ say "Well I'm definitely not gonna find another one up for sale!"
                rose @ say "I don't know, maybe I can retrofit the guts of a TCM-100 into the shell and pretend it's the same thing."
                
                player "And how much for one of those?"
                
                rose @ say "$500."
                
                player "Five hudred dollarydoos?!"
                
                rose @ say "Yeah, just 500. You're not poor are you?"
                
                player "Uhh..."
                
                n "500 dollars is a substantial chunk of your life savings."
                
                menu:
                    "Pay":
                        $ rosePoints =+ 1
                        
                        n "This kind of is your fault, even if Rose is being a cunt about it."
                        
                        player "You have cashapp?"
                        
                        n "Rose's signature glare becomes even more condescending than usual."
                        
                        rose @ say "No, I don't use demonic proprietary junkware like that."
                        
                        player "Well I don't walk around with $500 in my pocket every day!"
                        
                        rose @ say "You could have just said you're poor then."
                        
                        player "Doesn't your grandpa like own the university? Why don't you ask him to buy you a million Walkfans?"
                        player "Those things are so old he probably has a bunch lying around from when he was a kid."
                        player "Pretty sure that tech dates back to the cretaceous period."
                        
                        rothbauer @ say "Did I hear someone mention the cretaceous period?"
                        
                        n "Mr. Rothbauer may have just saved your life. Rose looked like she was ready to maul you before he stepped in."
                        
                        rothbauer @ say "Oh is that a cassette tape? Ah, I have fond memories of those back in my day!"
                        rothbauser @ say "Of course they were marketed as the hip new thing despite existing for millions of years. Probably."
                        rothbauer @ say "They had that technology mastered in the early cretaceous period. At least that's how the theory goes."
                        rothauer @ say "The government doesn't want you to know this but so much of modern technology is based on the dinosaurs' achievements."
                        rothbauer @ say "I'll save it for another day though because we've got a lot to cover today!"
                        
                        n "You dig out your notebook and avoid looking at Rose for the rest of the class. Hopefully she just forgets about your debt."
                    "Don't pay":
                        player "Actually yes, I am poor."
                        
                        rose @ say "Well stop it!"
                        
                        player "Stop... being poor?"
                        
                        rose @ say "Yes! If there's one thing that rivals how deplorable humans are, it's poor \"\"\"people.\"\"\""
                        rose @ say "Being poor isn't just something that happens by misfortune, poverty is literally God telling you that you suck."
                        rose @ say "Poors just don't have what it takes to have money and power. They'd rather coast by living paycheck to paycheck doing silly things like renting apartments and paying taxes."
                        
                        player "Hey, it's not that easy being poor! Imagine if you couldn't afford stuff."
                        
                        rose @ say "Then I'd kill myself."
                        rose @ say "Consider that a recommendation for you and your kind."
                        
                        player "So does this mean you'll let me off the hook for the $500?"
                        
                        rose @ say "*Sigh*"
                        rose @ say "If your kind weren't so despicable, I might pity you."
                        rose @ say "There's no point in hounding you for the money, you'll just end up robbing some innocent wealthy person for the money if you get desperate."
                        rose @ say "Instead all I ask in exchange for you breaking my practically one-of-a-kind vintage cassette player, is that you consider suicide."
                        
                        player "Deal!"
                        
                        n "Sucker."
                        n "You already do that every night."
                        
                        n "Rose scoffs and shoves the remains of her cassette player into her bag. Shortly afterwards, Mr. Rothbauer arrives to begin the lecture."
                    
    scene bg lecturehall with fade
    
    gunner @ say "Duuuuude Ava texted me yesterday!"
    
    player "So?"
    
    gunner @ say "Get this, she texted *me* first! That's how you know she wants to have sex with me!"
    
    player "Oh? Congratulations."
    player "But I think she's texted me first before. Does that mean she wants to have sex with me too?"
    
    gunner @ say "Counterpoint: women don't know what they want."
    gunner @ say "She was probably confused and hysterical. Many such cases."
    gunner @ say "But this time I'm sure she wants big catboy cock."
    
    player "And why's that?"
    
    gunner @ say "Because she invited me to go \"shooting\" with her this weekend."

    player "Like a photoshoot? Where?"
    
    gunner @ say "Yeah we're gonna hike up this mountain, take some pics of trees or whatever, then I'm gonna shoot my load in her."
    
    player "Did either of you explicitly mention that last part?"
    
    gunner @ say "No, but it was implied."
    
    menu:
        "Cool, have fun":
            #$ avaPoints =- 1
            
            player "Cool, have fun with that."
            player "I'm probably gonna watch boating accident documentaries or something this weekend."
            
            gunner @ say "Nice."
            gunner @ say "I was in a \"boating accident\" once."
            gunner @ say "And now I have a closet full of untraceable guns."
        "Doubt":
            $ avaPoints += 1
            
            player "I doubt that but okay."
            player "Are you sure she didn't get mixed up and mean to send those messages to me?"
            
            gunner @ say "Nah she'd know something was off if she detected the slightest hint of rizz from you."
            
    n "*Bzzz bzzz*"
    n "Oh look you've got a text. You wonder who it could be from."
            
    call phone_start
    
    call message_start("Ava", "Hiya [name]! You busy this weekend?", "avaavi.png") 
    
    call reply_message("Not sure yet. Why what's up?") 
            
    call message("Ava", "I was just wondering if you'd wanna come hiking in the mountains with Gunner and me ^v^", "avaavi.png") 
            
    call phone_end         
    
    player "Ava just invited me to come with you two."
    
    gunner @ say "Whaaaa?!"
    gunner @ say "Dude say no!"
    
    player "Why? It sounds like a fun time."
    
    gunner @ say "I don't want this hike to be a sausagefest! Just tell her you already have plans."
    
    n "Gunner slips a $100 bill onto your desk."
    
    menu:
        "Accept his bribe":
            $ avaPoints =- 1
            
            player "Fine, I didn't wanna go anyway."
            player "I'll text her and say I already made plans with someone."
            
            call phone_start
    
            call message_start("me", "Hey sorry I just remembered I promised to hang out with Rori this weekend", "testimage.png") 
            
            call message("Ava", "Aww oki", "avaavi.png") 
            call message("Ava", "Maybe next weekend you and I can go somewhere!", "avaavi.png") 
            call message("Ava", "just the two of us lol", "avaavi.png") 
            
            call reply_message("Maybe!") 
            call reply_message("Have a nice hike! Take some pretty photos!") 
            
            call message("Ava", "I will!", "avaavi.png") 
                    
            call phone_end         
            
            player "Done."
            player "Good luck with your date."
            
            gunner @ say "Thanks bro, you're a livesaver :3c"
        
        "Decline":
            player "Hmm. No thanks, a hundred dollars isn't worth much compared to a date with Ava."
        
            gunner @ say "Name your price then."
            
            player "Your entire net worth plus one Zimbabwe dollar."
            
            gunner @ say "But if I acquire one Zimbabwe dollar then that gets added to my net worth so I have to get another one which also adds to my net worth!"
            gunner @ say "It's an infinite financial loop!"
            
            player "Bingo."
            
            gunner @ say "Hmph!"
            gunner @ say "Fine, I guess I can't stop you from tagging along."
            gunner @ say "But at the end of the day Ava's will only be falling for *me.*"
            
            player "If you say so."
            
            call phone_start
    
            call message_start("me", "Yeah that sounds like a great time!", "testimage.png") 
            
            call message("Ava", "Yay ^v^", "avaavi.png") 
            call message("Ava", "We'll come get you on Saturday", "avaavi.png") 
            call message("Ava", "Be sure to bring water and snacks!", "avaavi.png") 
            
            call reply_message("Will do!") 
            call reply_message("Can't wait to see a master photographer in action!") 
            
            call message("Ava", "Hehe *snap*", "avaavi.png") 
                    
            call phone_end         
            
            player "Yup, this'll be a weekend to remember!"
            
            n "Gunner just glares at you, clearly displeased."
        
        "Make it $200":
            $ avaPoints =- 2
            $ badEnd =+ 1
            
            n "You stash the money into your pocket, but you can definitely get more from him."
            
            player "Only $100? I thought you liked Ava more than that."
    
            gunner @ say "Yeah I'm lowballing you lmao"
            
            player "Make it $200 and we have a deal."
            
            gunner @ say "Easy."
            
            n "Gunner opens his wallet and flips through a large stack of crisp green banknotes."
            
            gunner @ say "Oop, this is kinda embarassing. Do you have change for a $10,000 bill?"
            
            player "I didn't even know they made those."
            
            gunner @ say "Ah screw it, let me just send it to you on PayPossum. What's your account name?"
            
            n "You give him your email and he types it into his phone. A minute later you get a notification saying you've received $1000."
            
            player "You sent me $1000?"
            
            gunner @ say "Did I? I must have hit too many zeros. Whatevs, you can keep it."
            
            player "Man, I should do business with you more often."
            
            gunner @ say "Yeah yeah, now text Ava and tell you you can't come."
            
            call phone_start
    
            call message_start("me", "Hey sorry I just remembered I promised to hang out with Rori this weekend", "testimage.png") 
            
            call message("Ava", "Aww oki", "avaavi.png") 
            call message("Ava", "Maybe next weekend you and I can go somewhere!", "avaavi.png") 
            call message("Ava", "just the two of us lol", "avaavi.png") 
            
            call reply_message("Maybe!") 
            call reply_message("Have a nice hike! Take some pretty photos!") 
            
            call message("Ava", "I will!", "avaavi.png") 
                    
            call phone_end         
            
            player "Done."
            player "Good luck with your date."
            
            gunner @ say "Thanks bro, you're a livesaver :3c"
            
    herschel @ say "Good day class! Today will be an easy day since we'll just have a quiz then go over some homework problems."
    
    gunner @ say "The fuck? A quiz and *then* a review of the lesson?"
    gunner @ say "Bitch is *trying* to fail us."
    
    herschel @ say "Clear your desks except for a pencil and a scratch sheet of paper!"
    
    scene bg black with fade
       
    n "The rest of the day passes by uneventfully."

    scene bg schoolhallways with fade

    n "As you're going up the stairs on your way to literature, you catch a whiff of cigarette smoke."
    n "Where there's smoke, there's probably a vaguely depressed literature professor dog having a midlife crisis moment."
    n "Better check the roof. You've got time as long as she's still up there."
    
    scene bg roof with dissolve
    
    $ cafeEvents.append("margaretCafe")
    
    n "Your suspicions are confirmed when you see Ms. Ellen leaning on the wall watching the horizon."
    
    player "Couldn't wait until you got up on the roof to light up, huh?"
    
    margaret @ say "Hm?"
    
    player "The stairwell reeks of tobacco."
    
    margaret @ say "Oh shoot. Ah well, nothing to do about it now."
    
    n "She takes a long drag from her cigarette, seemingly amused by her own defiance of the rules."
    
    player "So what brings you up here again?"
    
    margaret @ say "Just wanted to admire the view~"
    margaret @ say "Sure is a long way down, isn't it?"
    
    player "You're telling me after I just climbed six flights of stairs."
    
    margaret @ say "I guess it's a long way up too."
    margaret @ say "By the way, how are you feeling? I don't have to worry about you falling out of your chair again do I?"
    
    player "I don't think so. I got it looked at and the doctor was like \"Yeah I don't know what's wrong with you but these meds will help. Probably.\""
    
    margaret @ say "And do they?"
    
    player "I think so."
    player "That doctor also smokes ciggies where they're not allowed."
    
    #margaret @ say "Sounds like you've got a type."
    
    margaret @ say "Ya gotta do what ya gotta do to survive the work day."
    margaret @ say "...But it does seem a tad irresponsible to smoke in a hospital."
    
    n "There's a brief lull in the conversation as neither of you are sure what to say next."
    n "You try and think of something while she looks off to the side and blows out smoke."
    
    player "Can I ask you a question?"
    
    margaret "I'm a professor, it's my job to answer your questions."
    
    n "Perhaps a personal question to get to understand her better."
    
    menu:  
        "Why did you become a professor?"
            player "What made you want to become a professor?"
         
            margaret @ say "You're acting like this was my first choice of profession."
            
            player "Well what was that?"
            
            n "She hesitates. Not because she's uncomfortable answering but rather because she's reminiscing."
            
            margaret @ say "I wanted to be a writer."
            
            player "And instead you became a... professional reader?"
            
            margaret @ say "Well you know how the saying goes. \"Those who can't do, teach.\""
            
            player "What do you mean? You couldn't write? But tons of borderline illiterate people write for a living."
            
            margaret @ say "That's part of the problem. You either make it writing at the highest level or you succeed making slop. There's not much room anywhere in between."
            margaret @ say "And guess where my writing skills lie."
            
            player "Dang."
            player "Too smart to write young adult vampire fanfiction disguised as literature, but not smart enough to dethrone Shakespeare."
            
            margaret @ say "Unfortunately my circumstances aren't particularly rare. I'm just one of the lucky ones to at least get a job that's at least related to my lit degree."
            margaret @ say "But I can't say I'm too happy with the result."
            
        "Did you ever actually enjoy teaching?":
            player "You don't seem to have much passion for teaching."
            player "Was it ever enjoyable for you?"
            
            margaret @ say "At one point I thought it was. Or at least I tried to convince myself of that."
            margaret @ say "The thing about abandoning your dreams in favor of some silly career that's meant to be serious, is that you convince yourself that you actually wanted this."
            margaret @ say "And that all your past hopes weren't realistic. They were just some delusions you had, so now's it time to find happiness in this new thing you thought you'd hate."
            
            player "That's kinda bleak. Is becoming a real adult supposed to be like that?"
            
            #margaret @ say "From what I gather, yes."
            #margaret @ say "At least that's the situation most people find themselves in once they grow up."
            margaret @ say "I don't know if there's any way it's 'supposed' to go, I just know nothing in life has ever worked out the way I wanted it to."
            margaret @ say "Unfortunately my circumstances aren't particularly rare. I'm just one of the lucky ones to at least get a job that's at least related to my lit degree."
            margaret @ say "But I can't say I'm too happy with the result."
            
        "How did you get into literature?":
            player "How did you get into literature?"
            
            margaret @ say "The same way anyone does, I spent my youth reading books."
            margaret @ say "You read enough of the right literature, and you become captivated by the sheer expanse of imagination and creativity an author can tame."
            margaret @ say "Something like a mere painting or photograph only captures a moment in a scene, but a novel gives you a whole world crafted from all kinds of feelings and messages the writer wishes to express."
            margaret @ say "For the same reason I enjoy watching movies but those really don't have the same impact since they're over and done with so quickly."
            margaret @ say "Simply put, I just like a good story!"
            
            player "Who doesn't?"
            player "But I get what you mean. There's a lot you can do in writing to evoke a certain feeling while still giving enough room for interpretation."
            
            margaret @ say "Exactly! No two people will read a book the same way! Even going back and rereading a book makes me feel a different way each time as I've grown older."
            margaret @ say "Though at this point I've become so familiar with the required reading for this course, the magic is gone for those books I used to adore."
            
            player "If you love stories so much why don't you write some of your own?"
    
            margaret @ say "That's the problem, hun. I haven't got any to tell."
            
            player "Surely you could come up with something. You're a literature professor after all! You should know what makes for a good book."
            
            margaret @ say "I'm afraid it doesn't work that way. I'm as close to writing a good book as I am directing a blockbuster movie or painting the Sistine Chapel."
            margaret @ say "Just because I can pick apart good writing from bad doesn't mean I can produce something original."
            margaret @ say "People can only write what they know, and all I know is reading books and one bad romance."
            
            n "Ms. Ellen takes a drag from her cigarette, then adds"
            
            margaret @ say "Not to say I didn't give it a shot, but I'm a much better professor than I am a writer. And I'm a pretty lousy professor."
            
            player "So why'd you become one?"
            
            n "She has to think for a moment, as if she's being searching for an answer to that question for a long time."
            
            margaret @ say "I thought if I could have a career being around the books I held so dear that everything would be alright."
            margaret @ say "And that I wouldn't become bitter and begin to resent the only thing in life that brought me joy."
            
            player "I'm sorry to hear that. If it means anything, you're my favorite professor."
            
            margaret @ say "Aww, they say flattery will get you nowhere but..."
            
            n "Her tail is wagging. You feel like you've just been standing around and listening to her talk but you must be doing something right."
            n "Ms. Ellen takes another puff and her grin fades away."
            
    margaret @ say "I was fooled into thinking that becoming a professor would make me feel... prestigious."
    margaret @ say "When all I do is explain old books to rich brats."
    
    player "Some people need books explained to them."
    
    margaret @ say "I agree, however..."
    
    n "Ms. Ellen reaches the end of her cigarette. She flicks it to the ground, letting it burn out on the concrete."
    
    margaret @ say "This is not the life I wanted."
    
    menu:
        "And that would be...?":
            player "And that would be...?"
            
            margaret @ say "Something more... adventurous I'll say."
            margaret @ say "More travel, less desk work. Something worth writing about."
        "Most people don't get the life they want":
            player "Most people don't get the life they want."
            
            margaret @ say "That may be true but..."
            
    n "She pulls out another cigarette and puts it to her mouth but pauses before lighting it. Seemingly changing her mind, she puts the ligher away."
    
    margaret @ say "It's about time for class to begin, isn't it?"
    margaret @ say "Go ahead and run along now."
    margaret @ say "Don't wait up for me. Wouldn't want to get caught coming down from here with a student~"
    
    player "Sure thing. See you in class."
    
    n "She gives you a wave as you go back to the stairwell. Looking back one last time, you see her light the cigarette in her mouth."
    
    scene bg lecturehall with fade
    
    margaret @ say "...So we see that The Odyssey is really a tale about overcoming the many relentless challenges in life and reaping the rewards."
    margaret @ say "It's as tragic as it is uplifting! And although most of us will never get shipwrecked or fight giant cyclopses..."
    margaret @ say "...the underlying hero's journey has a universal quality that everyone can relate to and forms the basis for pretty much every story told since."
    margaret @ say "Be sure to review the key terms we discussed during this module because they will definitely make an appearance on the test!"
    margaret @ say "That's all for today. Class dismissed!"
    
    n "Damn, Ms. Ellen is good at flipping a switch and acting like nothing's wrong when she lectures. If you didn't know any better you'd think she's pretty happy with her life."
    n "The way she smiles at students and wags her tail on the way out of the lecture hall disguises the Ellen you know on the rooftops."
    
    scene bg classroom with dissolve
    
    celestine @ say "...On se voit jeudi, la classe!"
    celestine @ say "You're all doing so well, I'm very proud of you!"
    celestine @ say "Keep up your studies and I'm sure you'll all pass with flying colors!"
    
    claire @ say "Don't you just love French, [name]?"
    claire @ say "They say it's the language of love~"
    
    menu:
        "I hate it":
            $ clairepoints =- 1
            
            player "I hate the French with every fiber of my being."
            
            claire @ say "Aww don't be such a downer! If not for the French we might not have a class together!"
            
            player "Yeah now I hate them even more."
            
            claire @ say "What's that supposed to mean?"
            
            player "Uhh..."
            
            n "Quick, press spacebar to distract her and avoid a dramatic overreaction!"
            
            player "Hey do you wanna get coffee?"
            
            claire @ say "Hell yeah!!"
        "It's nice when you speak it":
            $ clairepoints =+ 1
            
            player "I like whenever you speak it."
            player "You already sound like it's your native tongue."
            
            claire @ say "Ksksksks merci beaucoup, [name]~"
            
            player "Hnnnng that's so hot!"
            
            claire @ say "Oui? Wait til you hear what I sound like in bed~"
            
            n "What could she possibly mean by this? Does she snore when she sleeps? Maybe you should ask Ava later."
            
            claire @ say "By the way, you wanna get coffee with me and Ava today?"
            
            n "You've got nothing better to do."
            
            player "Why not."
            
            claire @ say "Yay~"
        "No strong feelings":
            player "I have no strong feelings towards it."
            player "It's just an elective credit I have to get out of the way."
    
            claire @ say "Well I'm glad we just happened to be together in the same class and sit right next to each other and be study partners and get to hang out every other day~"
            
            n "Claire has a dumb grin on her face. She's leaning so far into you that her desk is left balancing on two legs."
            
            player "Yeah it's pretty cool I guess."
            
            claire @ say "You guess??"
            
            n "Her desk topples back to its original position with a loud thud that reverberates around the entire room a few times."
            
            player "I mean uhh... yeah I'm glad to get to see you so often."
            
            claire @ say "Really???"
            
            player "Yeah in fact I was thinking we could get coffee?"
            
            claire @ say "Right now?"
            
            player "Uh huh."
            
            claire @ say "Ohmygosh I have to tell Ava about this!"
            
            player "Tell her about what? We're just getting coffee together..."
            
            n "Claire pulls out her phone and ignores you while texting up a storm to Ava."
            
    
     #ask ava about her trip with gunner. claire tries to get in but ava denies her. Claire gets upset and plans her own hiking trip with rori.(claire "I see, you wanna hog alllll the boys to yourself!") 
    
    
    
        