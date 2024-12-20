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

    player "They must be good then."
    
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
    show mishka:
        xpos -440
    with move

    ellen @ say "Oh hello there, [name]. I didn't expect to see one of my students here just before class. Are you feeling any better?"

    player "Yes ma'am. I ended up going to the hospital and they gave me some pills so I won't pass out in your class anymore."
    
    show margaret happy

    ellen @ say "That's good to hear! I'd certainly hope you're feeling well today since we're having a quiz!"

    player "Err, quiz?"

    show margaret sad

    ellen @ say "Oh didn't anybody let you know?"
    
    show margaret neutral
    
    ellen @ say "You should be fine though, as long as you've been keeping up with your reading."
    
    show margaret happy
    
    ellen @ say "Now if you'll excuse me, I'm going to get one of those delicious cinnamon buns. What better way to start autumn, right?"
    #ellen @ say "Why, I'd kill for them! Figuratively, of course!"
    
    show mishka sad

    mishka @ say "Sorry ma'am, I just sold the last one to [name] here..."

    show ellen sad

    ellen @ say "Seriously?"
    ellen @ say "Damn, I was really counting on that cinnamon bun to get me through today..."

    menu:
        ellen "{cps=0}Damn, I was really counting on that cinnamon bun to get me through today...{/cps=0}"
        "Offer Miss Ellen your cinnamon roll":
            #finished
            $ ellenPoints = ellenPoints + 1
            $ gaveCinRoll = True
            $ badEnd = badEnd + 1
            player "Well... I could give you mine. I don't really mind."
            
            show mishka happy

            show margaret neutral
            
            mishka @ say "Aww how sweet of you!"

            ellen @ say "Oh my goodness, I'm flattered but a teacher could never accept such a gift from a student!"
            
            show mishka neutral

            player "No really, I just remembered I'm not supposed to eat sugary things when I'm on these pills so..."

            show margaret intrigued 
            
            ellen @ say "Hmm..."

            n "Miss Ellen looks around."
            
            show margaret melancholy

            ellen @ say "Well, I suppose I could, just this once..."

            player "Don't worry, I'm not gonna tell on you or anything."
            player "Here you go."

            n "You hand over the bag."
            
            show margaret neutral

            ellen @ say "Aww, thanks [name]!"

            n "Miss Ellen gives you a warm smile and leans in close enough to whisper into your ear."

            ellen @ say "Don't worry about the quiz today~"

            n "Miss Ellen waves to you as she takes a bite of the cinnamon roll."

            ellen @ say "See you in class!"

            hide ellen with dissolve

            player "Yeah, I guess I should get going too. Later, Mishka!"

            mishka @ say "Dah skorovuh!"

            stop music fadeout 1.3

            scene bg lecturehall with fade

            #play music "audio/ai21.ogg" fadein .5
            play music "audio/music/mere - retrograde.ogg" fadein .5

            show box with Dissolve(.2):
                ypos 0

            show margaret neutral at center with dissolve

            ellen @ say "Good morning class! I hope you studied well for today's quiz!"

            n "Ellen hands out papers to everyone, giving you a warm smile as she hands you yours."

            if studied == "lit":
                #finished
                n "You probably could have aced this quiz anyway. You had plenty of time to read over it during your stay at the hospital after all."
                n "But the extra assurance certainly doesn't hurt."
                n "You work through the quiz normally in case she decides to go back on her word."
                n "When you're finished you walk up and turn it in."
            else:
                #finished
                n "It's a good thing you bribed her with that cinnamon roll, otherwise you'd fail this quiz for sure."
                n "Feels a bit dishonest though..."
                n "Looking over the questions, you have no idea how to answer most of them."
                n "You just write something that kinda makes sense and turn it in when you're done."


        "Don't offer Miss Ellen your cinnamon roll":
            #untested
            show mishka neutral
            
            player "Better luck next time."

            n "You take a bite out of your cinnamon roll while Miss Ellen glares at you."

            ellen @ say "Yes well... I'll see you in class, [name]."

            hide ellen with dissolve

            n "She storms out of the cafe."
            
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

            ellen @ say "Good morning class! I hope you studied well for today's quiz!"

            n "Ellen hands out papers to everyone, glaring at you as she hands you yours."
            n "She isn't still mad about the cinnamon roll thing, is she?"
            n "Hopefully she doesn't take it out on your grades."

            if studied == "lit":
                n "The answers come to you fairly quickly as you go through the quiz, thanks to the time you spent studying while bedridden."
                n "You feel confident as you walk up and hand in your quiz."
            else:
                n "After looking over the quiz and realizing you're not prepared to answer any of these questions, you begin to regret not giving up your cinnamon roll this morning."
                n "You do the best you can and sheepishly turn it in."
            

    ellen @ say "...Is that everyone's?"
    
    show margaret melancholy
    
    ellen @ say "Very good, what do you say we call it a day?"
    
    show margaret neutral
    
    ellen @ say "I don't want to overload your brains with too much stress. If you felt like this quiz was difficult, take this opportunity to reassess how you study."
    ellen @ say "And be sure to read every page assigned to you! There are no shortcuts when it comes to literature!"
    ellen @ say "That's all I have for you. Class dismissed!"

    scene bg classroom with fade