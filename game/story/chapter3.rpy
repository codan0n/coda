label chapter3:
    scene bg black with fade
    
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
            $ ellenPoints = ellenPoints + 1
            $ gaveCinRoll = True
            $ badEnd = badEnd + 1
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
            $ clairePoints = clairePoints + 1
            
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
    
    #doctor tells you there's not a trace of corvid-19 in you, but gives you some new pills to take anyway. a preventative measure
    
    n "After checking in to the hospital, a nurse did the routine blood pressure and temperature tests, then left you alone to wait for the doctor."
    n "Your muscles tense up as your mind wanders, fearing the worst."
    n "What if the doctor comes in and tells you you only have a few months left to live?"
    n "You haven't felt like you were gonna pass out in weeks but something still feels off."
    
    show kitsuragi at center with dissolve:
        ypos y_kitsuragi
        
    kitsuragi @ say "Hello [name]. Feeling any better since your last visit?"
    
    player "Yeah. I'm not getting dizzy randomly anymore."
    
    kitsuragi @ say "Good."
    
    