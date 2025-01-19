label chapter3:
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
            
            ###gunner @ say "Shut up, there's nothing gay about holding your homie's hand."
            #rori takes a pic
        
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
            n "Your very existence is pain but you've learned to live with it. Embrace it. You just have to swallow one more time. 
            
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
                
            else:
                player "Now where's my prize?"
            
                if holdingHands == "Ava":
                    
                if holdingHands == "Claire":
                    
                if holdingHands == "Rori":
                    
                if holdingHands == "Gunner":
                    
            
            
            
            
            
            
            scene bg codadorm with fade
            
            play music "audio/music/vylet - リラックス.ogg" fadein 1.0
            
            show box with Dissolve(.2):
                ypos 0
            
            n "You collapse onto your bed as soon as you make it back to your dorm."
            n "Your phone buzzing is the only thing stopping you from falling back to sleep."
            
            call phone_start from _call_phone_start_52 

            call message_start("Ava", "Hey [name]! You doing alright?", "avaavi.png") from _call_message_start_69 
            call message("Ava", "Sorry we just kinda dumped you at the hospital :/", "avaavi.png") from _call_message_375 

            call reply_message("Yeah.") from _call_reply_message_279 
            call reply_message("wtf happened last night") from _call_reply_message_280

            call message("Ava", "You passed out literally as soon as you finished your bowl", "avaavi.png") from _call_message_376 
            call message("Ava", "But hey at least you won the contest!", "avaavi.png") from _call_message_377 
            
            call reply_message("Woo") from _call_reply_message_281
            call reply_message("My stomach will never be the same") from _call_reply_message_282

            call message("Ava", "RIP", "avaavi.png") from _call_message_378 
            call message("Ava", "I'm glad you're okay though", "avaavi.png") from _call_message_379 
            call message("Ava", "I was kinda rooting for you lol", "avaavi.png") from _call_message_380 
            
            call reply_message("Oh?") from _call_reply_message_283
            call reply_message("You didn't wanna sit in Gunner's lap?") from _call_reply_message_284
            
            if avaPoints >= 4:
                #untested
                #need to determine if points requirement is too high
                call message("Ava", "I'd rather sit in yours :P", "avaavi.png") from _call_message_381 
                
                call reply_message("It's free anytime") from _call_reply_message_285
                
                #call message("Ava", "Noted~", "avaavi.png") 
                #call message("Ava", "Maybe I'll swing by later to \'study\' OvO", "avaavi.png") 
                call message("Ava", "OvO", "avaavi.png") from _call_message_382 
                call message("Ava", "I've got a busy schedule but I'll try to squeeze you in~", "avaavi.png") from _call_message_383 
                
                call reply_message("Lookin forward to it UwU") from _call_reply_message_286
                
                call message("Ava", "Hehe same~", "avaavi.png") from _call_message_384 
                
                call phone_end from _call_phone_end_60         
                
                #call message("Ava", "Allow me to see what my consultant says", "avaavi.png") 
                
                #call message("Claire", "This is Ava's consultant.", "claireavi.png") 
                #call message("Claire", "As a result of unfortunately landing you in the hospital last night, I would like to offer you compensation in the form of a makeout session", "claireavi.png") 
                #call message("Claire", "administered by my client Ava Montblanc at a time of your choosing", "claireavi.png") 
                #call message("Claire", "you can also totally feel her up and stuff lol", "claireavi.png") 
                #call message("Claire", "no bra too", "claireavi.png") 
                
                #call message("Ava", "AAAA WHAT NO I DID NOT AGREE TO THIS", "avaavi.png") 
                
                #call message("Claire", "Too late, the offer's been sent :P", "claireavi.png") 
                
                #call screen phone_reply("Accept offer","avaaccept","Decline offer","avadecline")
                
                #label avaaccept:
                    #call phone_after_menu
                    
                    #call message_start("me", "Deal", "testimage.png") 
                    
                    #call message("Ava", "Oh my gosh Claire whyyyy ;-;", "avaavi.png") 
                    
                    #call message("Claire", "she's acting hard to get but i know she wants it :P", "claireavi.png") 
                    
                    #call reply_message("Claire's influence is truly limitless")
                    
                    #call message("Claire", "just wait until our next sleepover >:3", "claireavi.png") 
                    
                    #call message("Ava", "You guys are so lewd >.>", "avaavi.png") 
                    
                    #call message("Claire", "i am literally handing you a once in a lifetime opportunity to get with a human on a silver platter", "claireavi.png") 
                    #call message("Claire", "you should be more thankful", "claireavi.png") 
                    
                    #call message("Ava", "Hmph!", "avaavi.png") 
                    
                    #call message("Ava", "Hey WTF!", "avaavi.png") 
                    
                    #call message("Claire", "I just put a lock on her underwear drawer", "claireavi.png") 
                    #call message("Claire", "no bra for you until you uphold your end of the deal with [name]!", "claireavi.png") 
                    
                    #call message("Ava", "My panties were in there too!", "avaavi.png") 
                    
                    #call message("Claire", "I guess that sweetens the deal even more :P", "claireavi.png") 
                    
                    #call reply_message("")
                    #ava says she was planning on hanging out with gunner today, player can come with if they want. she says if you play your cards right you'll get your prize
                    #player teases she better hope that thin shirt of hers doesn't get wet, it's supposed to rain tomorrow
                    
                    
                    #grind session at party
                    #negotiating my bird butt
                    
                    #may i spank it
                    
                    #once
                    
                    #good deal

                    #call phone_end
                
                #label avadecline:
                    #$ avaPoints += 1
                    #call phone_after_menu
                    
                    #call message_start("me", "Nah don't worry about it", "testimage.png") 
                    
                    #call message("Claire", "are you sure? i know she's playin hard to get but she's thiiiis close to doin it", "claireavi.png") 
                    
                    #call message("Ava", "I am not!", "avaavi.png") 
                    
                    #call reply_message("Yeah it's fine. I just wanted the glory of beating Gunner last night.")
                    
                    #call message("Claire", "awwww so humble <3", "claireavi.png") 
                    #call message("Claire", "well if you change your mind, I'll be your consolation prize~", "claireavi.png") 
                    
                    #call message("Ava", "Hrmph!", "avaavi.png") 
                    #call message("Ava", "And I guesssss I can give you a smooch on the cheek or something", "avaavi.png") 
                    
                    #call message("Claire", "See! I told you she'd come around! Just needed some jealousy as motivation~", "claireavi.png") 
                    
                    #call reply_message("you're too kind, both of you~")
                    
                    #call message("Claire", "That reminds me!", "claireavi.png") 
                    #call message("Claire", "I'm going fishing with that ram boi if you wanna come~", "claireavi.png") 
                    
                    #call reply_message("Wow, you're really pushing him to get outdoors more huh")
                    #call reply_message("Around what time? I'm feeling kinda beat today")
                    
                    #call message("Claire", "We can go tomorrow but it's gotta be bright and early!", "claireavi.png") 
                    
                    #call reply_message("You coming, Ava?")
                    
                    #call message("Ava", "I would but I already made plans with Gunner", "avaavi.png") 
                    #call message("Ava", "We're going urban exploring again, this time at the old train station", "avaavi.png") 
                    
                    #call screen phone_reply("Go fishing","claireaccept","Ask to join Ava","clairedecline")
                    
                    #label claireaccept:
                        #$ clairePoints += 1
                        #$ roriPoints += 1
                        #call phone_after_menu
                        
                        #call message_start("me", "Ah damn enjoy your adventure. Watch out for hobos.", "testimage.png") 
                        #call reply_message("I'm gonna catch a big fish with Claire and Rori lol")
                        
                        
                    
                    
                    
                    
                    
                    #move the talk about fishing trip/urbex to sunday morning
                    
                    
                    
                
                    #label clairedecline:
                        #$ avaPoints += 1
                        #call phone_after_menu
                        
                        #call reply_message("Is this an Ava x Gunner exclusive or do you have room for one more?")
                        
                        #call message("Ava", "I was hoping you'd ask to join~", "avaavi.png") 
                        #call message("Ava", "As much as I like Gunner, he's kinda.... ", "avaavi.png") 
                        #call message("Ava", "Uhhhh", "avaavi.png") 
                        #call message("Ava", "Well you know how he is", "avaavi.png") 
                        
                        #call reply_message("I get what you mean")
                        
                        #call message("Claire", "I sense a love triangle~", "claireavi.png") 
                        #call message("Claire", "Or perhaps a love quadrilateral if I'm involved idk if I am or not", "claireavi.png") 
                        
                        #call message("Ava", "Shush, the adults are talking", "avaavi.png") 
                        
                        #call message("Claire", "Don't silence me!", "claireavi.png") 
                        #call message("Claire", "Like it or not, you'll have to choose one way or another eventually!", "claireavi.png") 
                        #call message("Claire", "Or a three way if you're so inclined uwu", "claireavi.png") 
                        
                        #call message("Ava", "Blocked", "avaavi.png") 
                        
                        #call message("Claire", "Hey! Rude!", "claireavi.png") 
                        #call message("Claire", "[name] call Ava a whore for me, thx", "claireavi.png") 
                        
                        #you live in the same room, you do it
                        
                        #claire "oh yeah"
                        #claire "Ow! She threw a textbook at me"
                        #claire "And now she's trying to strangle me with a bra"
                        
                        #n "god you wish you could see that"
                        #call reply_message("Claire says you're a slut, Ava")
                        
                        #call message("Ava", "Well it takes one to know one!", "avaavi.png") 
                        
                        #call phone_end
            else:
                #finished
                call message("Ava", "I was leaving it to chance really", "avaavi.png") from _call_message_385 
                call message("Ava", "Or rather, whoever was most determined", "avaavi.png") from _call_message_386 
                call message("Ava", "Which ended up being you! ^v^~", "avaavi.png") from _call_message_387 
                
                call reply_message("Cool so where's my lapdance?") from _call_reply_message_287
                
                call message("Ava", "Hey, I only said I'd sit in the victor's lap!", "avaavi.png") from _call_message_388 
                
                call reply_message("And yet my lap remains empty") from _call_reply_message_288    
                
                call message("Ava", "Can we continue this conversation later? Something just came up.", "avaavi.png") from _call_message_389 
                
                call reply_message("fffffine but don't think i'll just forget about it!") from _call_reply_message_289    
                
                call message("Ava", "Of course not~ I'm excited to see where this goes myself~", "avaavi.png") from _call_message_390 
            
                call phone_end from _call_phone_end_61
                
            #n "That's enough texting for today."
            n "It's a beautiful day out but your stomach still hurts from yesterday, so you resign yourself to catching up on some classwork between watching videos online."
                    
        "Concede":
            #untested
            n "It would be wise to admit defeat. There's no point in hurting yourself over this."
            
            player "No more. I can't go any further."
            
            n "You sit there, brain fried from the traumatic spices, suckling on an ice cube as Gunner finishes his bowl and claims victory."
            
            show ava casual overjoyed
            
            gunner @ say "THROUGH THE FIRE AND FLAMES, I EMERGE VICTORIOUS! *inhale* AAAAAAAAAAAAAAAAAAA"
            
            n "He sits panting for a while before trying to take a sip of water."
            
            gunner @ say "EVEN THE WATER BURNS!!!"
            
            show ava casual happy
            
            ava @ say "You alright, big guy?"
            
            gunner @ say "No"
            gunner @ say "I need"
            gunner @ say "I need your avian ass right here on my lap cause I just owned [name] and brought glory to all of catkind."
            
            show ava casual daydream
            
            n "Ava stifles a giggle."
            
            ava @ say "Oh pft. Fine. I said I would, and I guess you do kinda deserve it."
            
            show ava:
                xpos -150
            with move
            
            pause .1
            
            show ava casual concerned
            
            n "Ava stands up and walks over, visibly hesitant, but a thumbs up from Claire is enough to convince her to go with it."
            
            show ava casual flattered at flipright
            
            n "She pushes out her rear, flaunting her tail feathers and sits down on Gunner's lap."
            n "She lets out a surprised chirp as he grabs her by the waist and pulls her closer."
            n "Feels bad man."
            
            show claire outdoors lusty
            
            claire @ say "Alright, your turn [name]!"
            
            player "Wha"
            
            n "You were too busy chugging water and sulking to notice Claire's giant ass looming over you."
            n "You have no time to prepare as it comes crashing down, making the seat you're sitting in groan and creak as 300 pounds of bunny crushes your legs."
            n "You can't even see over her when she leans back and settles in."
            
            player "This is fine."
            
            n "However, even being pinned between an uncomfortable chair and a BBW (big beautiful waifu) is nothing compared to the smoldering spice lingering in your mouth."
            n "You probably made the right choice in not continuing, even if you do have to pay for the meal now."
            
            show ava casual smile
            
            ava @ say "You comfy, Claire?"
            
            show claire outdoors embarassed
            
            claire @ say "Yup! Ksksksks!"
            
            show ava casual overjoyed
            
            ava @ say "Same~"
            ava @ say "*Chirp*~"
            
            show claire outdoors neutral
            
            claire @ say "I just feel bad cause now Rori's left out!"
            
            rori @ say "O-oh that's quite alright..! I wouldn't want to uh, steal the glory from [name] so you can stay over there with [himher]."
            
            n "You catch a glance at Gunner. The bastard shoots you a smug grin and wraps his arms around the bird sitting in his lap."
            n "Fuck, why did you even suggest this silly contest in the first place?"
            
            show ava casual happy
            
            ava @ say "Mind if I try a bite, [name]?"
            
            player "Wha? Are you sure? I'm literally dying over here."
            
            show ava casual smile
            
            ava @ say "I'm sure I'll be fine~"
            
            n "Ava reacher over with her fork and takes a stab at your red hot molten lava in a bowl."
            n "You watch in horror as she takes a big bite and swallows it."
            
            show ava casual daydream
            
            ava @ say "Hmm. Kinda bland if you ask me."
            
            gunner @ say "Whoaaaa!!! How can you eat something like that so casually?"
            
            show ava casual smile
            
            ava @ say "Hehe~ It's a secret~"
            
            rori @ say "Ohh I think I know! I read that birds don't have receptors for capsaicin, the thing that makes things spicy."
            
            show ava casual overjoyed
            
            ava @ say "Breeee~ Ya got me! It was fun watching you guys suffer from something so mild!"
            
            show ava casual happy
            
            n "Ava pulls your bowl closer to her and continues eating it like it's nothing."
            
            ###if you had ava sit by you during the movie night, comment on how he's getting his revenge
            
            n "The night goes on and eventually Claire gives you a break when you all decide to head back home."
            n "Ava and Gunner sure seemed to have a good time, and even though Rori was maidenless he still seemed to enjoy spending time with everyone."
            n "Even you had a few laughs once you no longer felt like death was preferable to your situation."
            n "Still, losing the contest kinda bummed you out more than expected."
            
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
            
            scene bg codadorm with fade
            
            n "You wake up feeling dizzy, almost kinda hungover."
            n "Your poor intestines are still groaning in pain even after you made several trips to the bathroom."
            n "Last night was not worth the trouble, just to lose."
            
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
            
            n "You're getting pretty tired of this love triangle bullshit. Sooner or later she's gonna have to pick a side."
            n "It's a beautiful day out but your stomach still hurts from yesterday, so you resign yourself to catching up on some classwork between watching videos online."
    
    
    ####spicy food friday night, explore on sunday?
        #the reward for winning the contest is holding hands with ava. loser gets rori or claire
        #claire: Wow ava that's way more lewd than what I suggested!
        #choose who you wanna hold hands with at the start (including gunner "Wh-what?! My brother in Christ, that is a bit sus."), or if you don't care and just want to beat gunner. hold hands as you leave the hospital
    