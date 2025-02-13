label chapter2start:

    ###CHAPTER 2
    ###weather will be randomized (starting in week 4?) and affects what you can do after class
    ###once a week you can sleep in and get a chance at a unique night scene?
    ###can also do night scenes on weekends more freely?

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0
    
    play music "audio/ambient/morning birds.ogg" fadein 0.1
    
    n "Farewell sweet weekend, you must return to class for now. Don't worry, you'll be back soon."
    n "You stuff your things into your bag and head out to your first class of the day, History."
    
    scene bg classroom with fade

    play music "audio/music/mere - schooldaze.ogg" fadein .4

    show box with Dissolve(.2):
        ypos 0

    show rothbauer at center with dissolve:
        ypos y_roth

    rothbauer @ say "Good morning, class!"
    rothbauer @ say "From today forward, we will be discussing the intersections of human civilizations with those of other anthromorphs! How exciting!"
    rothbauer @ say "From as far back as 4000BCE, humans developed bonds with species of all different sorts and introduced them to their cities and way of living."
    rothbauer @ say "Now, what picture comes to mind when you think of ancient civilizations and human fondness for furry friends?"
    rothbauer @ say "Anyone?"
    
    menu:
        rothbauer "{cps=0}Anyone?{/cps}"
        "Ancient Egypt":
            "No one else says anything so you raise your hand and take a guess."
            
            player "Ancient Egypt?"
            
            rothbauer @ say "Someone's been studying!"
            rothbauer @ say "That's correct! When you think of ancient Egypt, you think of the Great Sphinx of Giza of course!"
        "Ancient Greece":
            "No one else says anything so you raise your hand and take a guess."
            
            player "Ancient Greece?"
            
            rothbauer @ say "Hmm, I'm afraid that's not quite what I had in mind."
            rothbauer @ say "I'm talking about ancient Egypt where the Great Sphinx of Giza lies!"
        "Ancient America":
            "No one else says anything so you raise your hand and take a guess."
            
            player "Ancient America?"
            
            rothbauer @ say "Not quite..."
            rothbauer @ say "I'm talking about ancient Egypt where the Great Sphinx of Giza lies!"
            
        "Don't answer":
            n "You decide not to answer. Unfortunately so does everyone else, leading to an uncomfortably long silence while Rothbauer waits."
            n "Eventually he just gives the answer."
    
            rothbauer @ say "I'm talking about ancient Egypt where the Great Sphinx of Giza lies!"
            #rothbauer @ say "Why, the Great Sphinx of Giza of course!"
            
    rothbauer @ say "Constructed in around 2500BCE, the Sphinx is one of the most iconic monuments representing interspecies relations with its human face and feline body."
    
    n "Haha he said interspecies relations."
    
    rothbauer @ say "Felines were particularly adored by the ancient Egyptian humans and they would often have close ties to rulers and upper class."
    rothbauer @ say "This marked the beginning of an era where anthromorphs gradually became indoctrinated into humanized civilizations around the globe."
    
    n "Mr. Rothbauer lectures about ancient Egyptian kingdoms for the rest of class."
    n "You have a feeling they saw catgirls as more than just friends."
    n "After class ends, you overhear Rose talking with the professor."
    
    show rothbauer with move:
        xoffset 300
    
    show rose skirt handonhip shy pendant at left with dissolve:
        ypos y_rose
    
    rose @ say "About the group project..."
    rose @ say "I started working on researching Arcoonian civilization but couldn't find much in the library."
    rose @ say "I was wondering if you had any sources I could look into."
    
    rothbauer @ say "Ah a fascinating society you've chosen!"
    rothbauer @ say "I can't say I'm surprised by the lack of material in the university library."
    rothbauer @ say "Much of their culture was wiped out and what little has survived... doesn't find its way into public knowledge."
    
    n "Rothbauer thinks for a moment."
    
    rothbauer @ say "Hmm... You know, I think I have some books in my personal collection I could loan you."
    rothbauer @ say "Please be aware that the contents of them are... contested among historians."
    rothbauer @ say "But for the purposes of your project, I will consider them a valid source!"
    
    show rose skirt handonhip smug pendant
    
    rose @ say "Thank you, that would be a great help."
    
    hide rose
    hide rothbauer
    with dissolve
    
    n "She's doing the project on Arcoonians, huh? From what you recall, they were related to raccoons in ancient America but mysteriously vanished without a trace."
    n "You'll have to look into it later. For now you have to run to Statistics."
    
    scene bg lecturehall with fade

    play music "audio/music/mere - schooldaze faster.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0
        
    show herschel at center with dissolve:
        ypos y_herschel
    
    herschel @ say "Hello class, I hope you all had a pleasant weekend!"
    herschel @ say "Today we'll be going over Bayes' theorem, which is a way of determining probability of a cause from its effect."
    herschel @ say "This is how insurance companies derive your potential risk from factors such as age, previous conditions, and family history."
    herschel @ say "It basically allows you to apply conditions to a set of data and find all sorts of statistical probabilities!"
    herschel @ say "Let's get started with some examples..."
    
    hide herschel with dissolve
    
    n "Mrs. Herschel goes through some problems, starting off with a basic one then adding further complexities to subsequent ones."
    
    stop music fadeout 2.0
    
    scene bg campus with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Gunner ran off after class, saying something about fraternity obligations."
    n "That leaves you free for the rest of the day."
    
    call afterClassOptions from _call_afterClassOptions
    
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
    
label week2Tuesday:
    scene bg lecturehall with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    show margaret happy at center with dissolve:
        ypos y_margaret

    margaret @ say "Good morning everyone. Today we'll be finishing up The Death of Ivan Ilyich. I'll be sad to see him go but we have plenty of other great books to get through and so little time."
    
    show margaret neutral
    
    margaret @ say "After Ivan falls and injures his side, he suffers from worsening pain that causes him to become irritable and further destabilize his relationship with his family."
    margaret @ say "His condition eventually leaves him bedridden and unable to work. Faced with both his mortality and the loss of his sense of purpose, he reflects on what it truly means to die."
    
    show margaret melancholy
    
    margaret @ say "He comes to realize that the perception of death revolves around the fulfillment of life one has made for themself."
    margaret @ say "He had once believed he led a fulfilling life by acquiring prestige and status, but as he lay dying, none of his achievements mattered so much as the sympathy he received from his servant."
    
    show margaret happy at hop
    
    margaret @ say "Moved by its sheer authenticity, Ivan finally understood while on his deathbed that by pursuing his own interests, he had neglected to foster a caring family."
    
    show margaret neutral
    
    margaret @ say "Their relationship resembled that of business partners, where one is only good for the convenience and profits they bring in, but by this time Ivan was nothing but dead weight."
    margaret @ say "His existence brought about an impersonal and artificial partnership that could only acknowledge each other as far as how one benefitted the other."
    margaret @ say "And thus his death would be a relief to them."
    
    n "Damn, what a downer."
    n "You suppose that's about as happy an ending as you can get when it comes to Russian literature though."
    n "Ms. Ellen talks about some interpretations and gets some students' opinions before hinting that an analysis of life and death in Tolstoy's context will be on the test."
    
    scene bg classroom with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    show celestine neutral at center with dissolve:
        ypos y_celestine

    celestine @ say "Bonne journée, classe! How was your weekend? Have any of you encountered any French words in your day to day life you never noticed before?"
    
    n "Claire waves her paw in the air energetically."
    
    show celestine at flipright
    
    pause .3
    
    show celestine with move:
        xoffset -500
    
    show claire sweater happy at center with dissolve:
        ypos y_claire
        xoffset 500
    
    claire @ say "I did!! Lots of food and stuff at cafes and bakeries are French! There's umm cafe au lait which is coffee with milk..."
    claire @ say "And fondant and macrons and brioche and savarin..."
    
    celestine @ say "Oui! France is of course known for its culinary arts! It's only natural that many of their words for cuisine would end up in English."
    
    show celestine excited
    
    celestine @ say "And they sure do love their cafes and bistros! If you go to Paris, you will find one on every corner!"
    
    show celestine neutral
    
    celestine @ say "That brings us to today's topic: basic conversation you might experience while out in town shopping."
    
    hide celestine
    hide claire
    with dissolve
    
    n "Mrs. Celestine goes over some terms and typical everyday sayings, then has the class recite them and practice in groups."
    
    scene bg campus with fade
    
    play music "audio/music/vylet - Hard to Say Anything.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    show claire sweater happy at center with dissolve:
        ypos y_claire
    
    claire @ say "Wish I could stay and chat [name] but I've got sorority duties to take care of today!"
    claire @ say "See you later!"
    
    n "Claire pulls you into one of her signature suffocating hugs before zooming off to do whatever sorority girls do."
    
    hide claire with dissolve 
    
    n "Off in the distance you see Ava fluttering from perch to perch taking photos. She waves to you as she soars above and disappears over a building."
    n "Seems like everyone has something to do today."
    n "As you wander around campus pondering what to do with the rest of *your* day, you bump into your favorite coffee rat."
    
    show mishka neutral at center with dissolve:
        ypos y_mishka
        
    mishka @ say "Hello!"
    
    player "Oh hey Mishka. It's weird seeing you somewhere other than the cafe."
    
    show mishka anxious tongueout wink left
    
    mishka @ say "I could say the same thing about you!"
    
    n "You hadn't considered that before. To you she's the coffee rat but from her point of view, you're just the coffee human."
    
    show mishka neutral -wink -left -tongueout
    
    player "I just got done with class. You going somewhere?"
    
    show mishka nervous
    
    mishka @ say "Just doing a walk. I'm on my break."
    
    player "Cool, cool."
    
    menu:
        player "{cps=0}Cool, cool.{/cps}"
        "Ask if she wants to hang out":
            $ mishkaMall = True
            
            n "You're not sure how else to ask, so you put it bluntly."
            
            player "You uh... wanna hang out?"
            
            show mishka anxious neutral
            
            mishka @ say "Hang...out?"
            
            n "She seems confused."
            
            player "Yeah, you know... go somewhere and do something together?"
            
            show mishka happy
            
            mishka @ say "Oh!"
            
            show mishka nervous2
            
            mishka @ say "I'd love to, but I have to get back to work in a minute."
            
            n "Damn, that's code for \'hell no,\' isn't it?"
            
            show mishka neutral eyesclosed
            
            mishka @ say "But maybe this weekend will work for you?"
            
            n "Maybe it's not! You still have a chance!"
            n "Don't fuck this up."
            
            show mishka neutral -eyesclosed
            
            player "This weekend works! How about..."
            
            n "Your mind races to think of a cool place to take her but comes up blank."
            
            mishka @ say "There's the mall in town if you would like to go."
            mishka @ say "I've never been to it so I don't know what it's like..."
            
            player "Sounds perfect!"
            
            n "You pull out your phone, pretending to pull up your calendar to make sure it's free."
            
            player "Saturday works for me. You got a number so I can text you when I'm there?"
            
            show mishka anxious smile
            
            mishka @ say "Hah... I don't actually."
            mishka @ say "Let's just meet there at 3 if that's a good time for you."
            
            player "Yup 3 works."
            
            show mishka happy
            
            mishka @ say "Great! See you there~"
            
            show mishka anxious neutral
            
            mishka @ say "I have to return to work now but I'm glad I ran into you!"
            
            player "Same! See you at the mall later!"
            
        "Stand around awkwardly":
            n "Nothing comes to mind. No conversation starters, no pickup lines, no funny hypothetical questions."
            n "So you just stand there, looking around aimlessly and giving polite smiles whenever your eyes meet."
            n "To your credit, Mishka also seems to be in the same akward state of not know what to do or say."
            
            show mishka anxious neutral -
            
            mishka @ say "Well it was nice standing here with you."
            mishka @ say "I have to return to work now but maybe we can do this again sometime?"
            
            n "Her statement is totally sincere without a hint of sarcasm."
            
            player "Whenever you're free."
            
            show mishka neutral -
            
            mishka @ say "Hehe see you at the cafe later, [name]!"
            
    hide mishka with dissolve
            
    n "Mishka gives you a wave and heads in the direction of the cafe."
    n "You're feeling tired from classes so you retire to your dorm early."
    
    stop music fadeout 2.0
    
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
    
    scene bg classroom with fade

    play music "audio/music/mere - schooldaze.ogg" fadein .4

    show box with Dissolve(.2):
        ypos 0
        
    show rothbauer at center with dissolve:
        ypos y_roth
        xoffset 400

    rothbauer @ say "Good morning class! I hope you're prepared for today's quiz!"

    player "Wha-? Quiz?"

    show rose skirt armscrossed shy pendant at center with dissolve:
        xoffset -500
        ypos y_rose

    rose @ say "It's listed on the syllabus."

    player "He could have at least given us a reminder."

    rose @ say "Sucks to suck."
    
    rothbauer @ say "When you're finished, set your paper down on my desk and you'll be free to leave after that."

    hide rothbauer
    hide rose
    with dissolve

    n "Rothbauer passes out the quiz sheets and you rack your brain trying to remember what he taught over the past week and a half."
    n "Your eyes wander over to Rose's desk and you can totally see her answers."
    n "You stretch and yawn, taking the opportunity to check if Mr. Rothbauer is watching."
    n "He's not."

    menu:
        n "{cps=0}He's not.{/cps}"
        "Look at Rose's answers.":
            $ rosePoints =- 1
            $ badEnd =+ 1
            
            n "Any way to pass, right? It's not like history is that important anyway."
            n "You sneak a few glances at Rose's sheet until she seems to notice."

            if gaveUmbrella == True:
                $ historyCheated = True
                
                n "Rose gives you an angry look but decides to move her paper a little closer so you can read it more easily."
                n "Is this thanks for giving her your umbrella the other day?"
                n "You need to ask her to return that some time."
                n "You quickly copy as many of her answers as you can."
            else:
                n "Rose covers up her sheet with her arm."
                n "Welp, there goes any chance of you passing this quiz."

        "Don't look at Rose's answers.":
            n "Maybe you shouldn't cheat, partly because it's morally wrong and partly because Rose would probably kill you if she caught you."
   
    n "Rose finishes before anyone else and turns in her sheet when you're only halfway done."
    n "You spend the rest of the class's duration trying to fill in the remaining blanks."
    n "When time runs out, you stand up and turn in your quiz."
    n "On your way out, Mr. Rothbauer stops you before you can leave."
    
    show rothbauer at center with dissolve:
        ypos y_roth
    
    rothbauer @ say "Oh, [name], I almost forgot!"
    rothbauer @ say "I meant to give this to Rose earlier but she's already left it seems."
    rothbauer @ say "Since you're partners on the project, I thought it just as well to entrust you with this book. Please do be careful with it, it's quite old and copies of it are rare."
    
    n "He dumps a heavy tome into your hands. The title on the cover reads The Rise and Fall of the Arcoonians."
    
    rothbauer @ say "Give it a look and be sure to give Rose a chance to read through it as well."
    rothbauer @ say "That's all I have for you! Carry on, I don't want to make you late for your next class!"
    
    scene bg lecturehall with fade

    play music "audio/music/mere - schooldaze faster.ogg" fadein .4

    show box with Dissolve(.2):
        ypos 0

    n "For some reason, you can barely concentrate in Statistics today."
    n "Your head is pounding and your vision blurry."
    n "You look down at your notebook and it's all just illegible scribbles and a few drool stains."

    show gunner frown1 at center with dissolve:
        ypos y_gunner
    
    gunner @ say "Bro, you still alive? You don't look so good."
    
    player "Ugh, this headache is killing me. I feel like I'm about to throw up."
    
    gunner @ say "Hang in there dude, class'll be over in like five minutes."
    
    hide gunner with dissolve
    
    n "Somehow you manage to endure five agonizing minutes that seem to last hours."
    n "Once class is over, you try to stand up but it's like your legs are gelatin."
    n "Gunner notices you struggling and comes to help you up."
    
    show gunner determined at center with dissolve:
        ypos y_gunner
    
    gunner @ say "How wasted did you get last night to come to class this hungover?"
    
    player "I didn't drink anything last night! I dunno where this is all coming from."
    
    show gunner frown1
    
    gunner @ say "Maybe you ate something bad? You should take it easy for the rest of the day my guy."
    gunner @ say "C'mon, I'll take you to your dorm."
    
    stop music fadeout 2.0
    
    scene bg codadorm with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Gunner practically drags you across campus to your dorm where he tucks you into bed and reads you a bedtime story."
    n "Okay you're pretty sure you hallucinated that last part but the point is you're in bed and rapidly falling asleep."
    
    show gunner neutral at center with dissolve:
        ypos y_gunner
    
    gunner @ say "Hope you feel better soon. Text me if you need anything!"
    
    player "Thanks. See you in class if I survive."
    
    gunner @ say "You better!"
    
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
    
    #thursday 2

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0
    
    #play music "audio/ambient/morning birds.ogg" fadein 0.1
    
    n "Stirring from your slumber, you take a deep breath and stretch."
    n "You seem to have slept off whatever was ailing you last night but something still feels off."
    
    show bg codadormshake
    
    n "As you throw the blanket off you and take your first steps of the day, a sudden dizziness overtakes you."
    n "The whole room is spinning..."
    n "..."

    show bg codadorm with dissolve
    
    stop music fadeout 1.5

    n "It's over now."
    n "What was that all about? Did you get up too quickly or something?"
    n "Strange, but you feel normal now."
    n "You do your usual morning routine and pack your bag for today's classes."

    play music "audio/music/mere - retrograde.ogg" fadein .5

    scene bg lecturehall with fade

    show box with Dissolve(.2):
        ypos 0
        
    $ currentbook = "The Odyssey"

    show margaret neutral at center with dissolve:
        ypos y_margaret

    margaret @ say "Today we'll be starting a new story, this time originating from ancient Greece in the 5th century BCE."
    margaret @ say "It is the archetypal hero's journey so often found in literature that succeeded it, as well as in our own lives!"
    
    show margaret happy
    
    margaret @ say "This is the tale first told by Homer, \"The Odyssey!\""
    
    show margaret neutral
    
    margaret @ say "What's especially interesting about these old poems passed down through oral tradition rather than written word, is that every generation adds their own spin."
    margaret @ say "So the version we'll be reading today is not the same as the original, but is instead an accumulation of the values of various cultures throughout time."
    
    n "Miss Ellen describes some of the historical context and impact of the story but it all blends together into a jumble of incomprehensible words as your brain once again falls into a stupor."

    n "The room starts to spin and you lose your sense of balance."

    stop music fadeout .5

    hide margaret
    hide box

    show bg static1
    pause .05
    show bg static2
    pause .05
    show bg static3
    pause .05

    show box:
        ypos 0
    show bg lecturehall

    ###make textbox all spikey and play a sound effect to show urgency. or animate it shaking left to right
    margaret @ say "[name]! Are you alright?"

    stop music fadeout 1.0

    n "You snap out of your dizzy spell but find that you've fallen out of your seat with the whole class looking at you."
    n "Ms. Ellen is looking down at you with a look of genuine concern."

    show margaret sad at center with dissolve:
        ypos y_margaret

    play music "audio/ambient/indoors people talking.ogg" fadein .5

    show margaret sad

    margaret @ say "[name]?"
    
    show margaret sad at shudder
    
    margaret @ say "You collapsed all of a sudden..."
    margaret @ say "Do you need a doctor??"

    show margaret sad

    n "You pull yourself back into your seat and shake your head."

    player "N-no, that won't be necessary. I'm fine."

    margaret @ say "Are you sure? It's not every day a student of mine passes out like that."

    player "Y-yeah, I think I'm just dehydrated or something."

    show margaret neutral at hop
        
    pause .1

    margaret @ say "Hmm. You better drink more!"
    margaret @ say "And just to be on the safe side, I want you to go home and get some rest. You're excused from class today."

    #n "A day off? Sounds too good to be true. You decide to take her up on the offer before she changes her mind."

    player "Err, thanks."

    n "You pack your things and head out the door, stumbling on the stairs on your way out."

    margaret @ say "Be sure to read the assigned chapters for next time!"

    show margaret

    stop music fadeout 1.0

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    play music "audio/ambient/morning birds.ogg" fadein 0.1

    n "You feel like you could have continued on with class but these dizzy spells hit you with no warning. Perhaps it's best if you lie down for a while."
    n "You can listen to music and chill and get some homework done."
    
    menu:
        n "{cps=0}You can listen to music and chill and get some homework done.{/cps}"
        "Arcoonian book":
            $ readArcoonianBook = True
            $ rosePoints += 1
            
            n "You take a look at the book Mr. Rothbauer gave you, \"The Rise and Fall of the Arcoonians.\""
            n "Skimming through its pages, you glean some information about their culture and role in ancient North America."
            n "Their society followed the principles of scholarly warriors who loosely ruled the continent."
            n "Honor, self reliance, freedom, sustainability, and harmony with nature were some of their ideals."
            n "Suffering and rising above one's particular life challenges were glamorized as being noble."
            n "Arcoonians fostered a fiercely individualist mindset that idealized liberty and sovereign freedom."
            n "Despite being united under general governance, battles between settlements were common. It's unclear what they fought over but the ruling class believed that it \"culled the weak.\""
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
    
    
    n "You're starting to feel exhausted, both physically and mentally."
    n "You set aside your reading materials and nestle under your blanket."
    n "A few seconds after closing your eyes, your phone buzzes."

    call phone_start from _call_phone_start_2

    call message_start("Claire", "Where r u ?", "claireavi.png") from _call_message_start_2

    call reply_message("Not feeling well. Had to skip class today.") from _call_reply_message_8

    call message("Claire", "Aw :( hope u get well soon", "claireavi.png") from _call_message_8

    call reply_message("Thanks :)") from _call_reply_message_9
    call reply_message("Gonna try and sleep it off. Text yo u later.") from _call_reply_message_10

    call message("Claire", "K, let me know if I can do anything.", "claireavi.png") from _call_message_9

    call phone_end from _call_phone_end_2

    n "You set your phone on silent and put it on the nightstand."

    stop music fadeout 1.0

    n "You start to feel funny again."
    n "You take a deep breath and close your eyes, hoping you'll fall asleep before it hits you again."

    hide box

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

    #___friday2

    scene bg codadorm with fade

    ##play sound "audio/ambient/morning birds.ogg" fadein .4
    play music "audio/music/vylet - yeah i'm ok thanks for asking.ogg" fadein .4
    #play music "audio/exports/【Music】こんにちは! ♡ [lQQkCtUahHE].opus"
    
    show box with Dissolve(.2):
        ypos 0

    n "You wake up feeling more tired than when you fell asleep but the bright sunlight streaming through the window urges you to get up."
    n "You reach for your phone and check the time. It's already past noon."
    n "Stats class is ending right about now."
    n "No use going out today. Might as well stay in and recover from this mystery illness that's plaguing you."
    n "You actually don't feel terrible right now but who knows if it will flare up again later."
    
    call phone_start from _call_phone_start_15
    
    call message_start("Ava", "Hey [name]! Claire told me you were feeling under the weather", "avaavi.png") from _call_message_start_20 
    call message("Ava", "but if you're feelin better this weekend wanna go somewhere with us?", "avaavi.png") from _call_message_183 

    call reply_message("I don't feel so bad today") from _call_reply_message_129 
    call reply_message("I think I'll be fine tomorrow") from _call_reply_message_130
    call reply_message("Where you going?") from _call_reply_message_131
    
    call message("Ava", "I'm not sure!", "avaavi.png") from _call_message_184 
    call message("Ava", "Claire says she picked out a spot", "avaavi.png") from _call_message_185 
    call message("Ava", "'Somewhere special' she says", "avaavi.png") from _call_message_186 
    call message("Ava", "Whatever that means", "avaavi.png") from _call_message_187 
    
    call reply_message("Interesting...") from _call_reply_message_132
    call reply_message("sure, I'll go") from _call_reply_message_133
    
    call message("Ava", "Yay ^v^", "avaavi.png") from _call_message_188 
    call message("Ava", "I'll let her know", "avaavi.png") from _call_message_189 
    call message("Ava", "meet us tomorrow at around 9 where we usually meet after class", "avaavi.png") from _call_message_190 
    
    call reply_message("k") from _call_reply_message_134
    
    call phone_end from _call_phone_end_21
    
    n "You wonder where this special place that Claire wants you to go to is."
    n "Hopefully you're feeling good enough to go tomorrow."
    n "You'll just take it easy today and be well rested for the next day."    
    
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
    
    scene bg campus with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    play music "audio/music/vylet - tenderness.ogg" fadein .4
    
    ### $ gardenEvents.append("avaGarden")
    
    $ avaClaireGarden = True
        
    n "Claire and Ava are already waiting for you at your usual hangout spot."
    
    show ava typical happy at center:
        ypos y_ava
        xoffset 500
    show claire sweater happy at center:
        ypos y_claire
        xoffset -500
        xzoom -1
    with dissolve
        
    ava @ say "[name]!! You're here!"
    
    claire @ say "I'm so glad you could make it!"
    
    player "Heh, glad I'm feeling well enough to... what is it that we're doing exactly?"
    
    claire @ say "There's like this huuuuuge garden on the other side of campus so I thought it would be fun to get lost in it with my pals~"
    
    ava @ say "Ooh that does sound like fun! I bet it's super pretty too! Glad I brought my camera~"
    
    claire @ say "As if you ever go anywhere without that thing ksksksksk!"
    
    ava @ say "True~"
    
    player "Shall we get going then?"
    
    claire @ say "Yeah!"
    
    n "Claire leads you across campus to the gardens. It's easy to spot from a distance thanks to the vibrant colors of all the flowers."
    
    scene bg garden with dissolve

    show box with Dissolve(.2):
        ypos 0

    #play music "audio/music/vylet pony - Reading at Night.ogg" fadein .4
    play music "audio/music/vylet - someday.ogg" fadein .4
    
    if gardenDiscovered == True:
        n "This is the same garden you've visited before, just at one of the other entrances. The area is quite expansive and you haven't been to this part before."

    show ava typical happy at center:
        #xzoom -1
        xoffset 450
        ypos y_ava
    show claire sweater happy at center:
        xzoom -1
        xoffset -450
        ypos y_claire
    with dissolve

    n "Claire hops around whimsically from one plant to another, sniffing the flowers and admiring the multitude of plants."
    
    show claire sweater pose happy

    claire @ say "It's such a lovely day to go for a walk in the gardens, isn't it?"

    player "Yeah, I guess it's better than being cooped up in my dorm all day."
    
    show ava pose whimsical

    ava @ say "Sunlight is good for you. Not just for your skin but also your mental health."
    
    show ava pose happy

    player "Huh. I didn't know that."

    #n "Maybe that's why you've always been depressed."
    
    show claire derp

    claire @ say "Just be careful not to get a sunburn! And remember to stay hydrated UwU"

    player "What... was that sound you just made?"
    
    show claire giggle

    claire @ say "What? UwU?"
    
    show claire flustered
    show ava typical unimpressed -

    player "Nevermind. Which way should we go? There's like a dozen branching paths."
    
    show ava typical excited -pose
    show claire surprised earsup

    ava @ say "Hmm, let's gooooo... this way!"
    
    show claire happy -earsup
    show ava happy

    n "She seems to pick a direction at random and pulls you and Ava along with her, deep into the garden."
    n "Before long, you're surrounded by a variety of shrubs and flowers to the point where you can't even see any of the university buildings anymore."
    n "Ava managed to escape to take photos of plants, getting particularly excited when she catches a hummingbird or butterfly sipping from a flower, but Claire maintains her death grip on your hand."
    
    ava @ say "Ooh, I have these in my garden back home. It's called a cardinal flower. Can you guess why?"

    player "Cause it's red like cardinals?"
    
    claire @ say "Only the males~"
    
    show ava excited at hop

    ava @ say "Yup! Such a pretty red~"
    
    show ava happy
    show claire giggle

    claire @ say "She's got a thing for cardinal boys~"

    show ava annoyed

    ava @ say "Shush up, I do not!"

    claire @ say "Ksksksks! Just teasin'!"
    
    show claire happy
    show ava typical neutral

    n "Ava and Claire continue to bicker and share fun plant facts as you go along."
    n "After a while, you come to a bench with an arch over it with vines growing all over."
    
    show ava pose concerned

    ava @ say "Whew, it's gettin' kinda hot! Can we take a break?"
    
    show claire flustered

    claire @ say "Yeah, my legs are killing me!"

    player "Same."
    
    show claire happy
    show ava pose happy

    n "Claire and Ava sit under the arch and begin reviewing the photos they've taken so far."
    n "There's only room for two so you just lean against a nearby tree, taking sips of water from your bottle and watching the bees zoom around."

    claire @ say "Hey [name], you wanna get a shot of us under the arch?"
    
    show ava typical happy -

    ava @ say "I'll let you use my camera as long as you promise not to drop it. It costs more than a semester's worth of tuition!"

    player "Sure, but I don't really know how to use one of those fancy cameras."

    ava @ say "Don't worry, I'll preset the exposure settings. All you have to do is point and click the button."

    n "Ava flicks some switches and dials on the camera before handing it over to you."
    n "You take a few steps back, compose your shot and press the button with a satisfying shutter sound."
    
    claire @ say "How'd it turn out? Lemme see lemme see lemme see!!"
    
    n "You turn the camera around and show Claire."
    
    show claire laughing
    
    claire @ say "Ohmygosh we look great! This is just the perfect day, isn't it!"

    n "Ava gets up and gestures to the bench."
    
    show claire happy
    show ava excited

    ava @ say "Ok now it's your turn, [name]!"

    menu:
        ava "{cps=0}Ok now it's your turn, [name]!{/cps}"
        "I don't like getting my picture taken.":
            player "Sorry, I don't like getting my picture taken."
            
            show ava pose shy

            ava @ say "I understand. I'm kinda the same way haha! But I've been getting more comfortable with it."
            
            show claire sad
            
            n "Claire lets out a disappointed sigh but doesn't say anything."
        "Okay!":
            $ clairePoints =+ 1
            
            show ava happy
            
            player "Okay!"

            n "You sit down next to Claire and smile for the camera."
            
            show claire leaning suggestive
            
            n "Just before Ava takes the shot, Claire wraps her arm around you, pulling you in close."
            
            show ava overjoyed

            ava @ say "Aww, you two are so cute~"

            show claire overjoyed
            show ava happy

            claire @ say "Show us the pic!"

            n "Ava comes around and shows you the picture. Your face has a look of surprise mixed with fear as Claire's sudden death grip took hold of you."

            player "Great..."
        "Alright but I'm getting my picture taken with you next.":
            $ clairePoints =- 1
            $ avaPoints =+ 1
            
            show ava happy
            
            player "Alright but I'm getting my picture taken with you next."

            show ava enamored

            ava @ say "Who, me??"

            n "She looks to Claire, as if seeking her approval."
            
            show claire flustered

            claire @ say "Sure, go for it!"
            
            show claire happy
            show ava typical happy

            n "Ava stands back to take a shot of you and Claire."

            ava @ say "Say cheese~"

            n "You smile for the photo and Ava clicks the shutter button."

            ava @ say "Aww, you two look so cute~"

            claire @ say "I bet!~"

            n "Ava comes around and shows you the picture. It's definitely a better shot than you could have taken with your phone."

            ava @ say "Alright, I guess it's my turn! Here you go Claire."

            n "Ava racks the zoom ring, presumably to set the shot up for a closeup. No need for a wide angle when Claire is out of the frame."
            n "She hands the camera to the bunny and sits down beside you. Claire hops back and has to bend over a bit to frame the shot."
            n "Claire motions for you to get closer together and Ava scoots more toward you, enough that you can feel her feathers brushing up against you skin."
            
            show ava smug

            claire @ say "One... two... three!"

            n "You smile for the camera and Claire releases the shutter."
            
            claire @ say "Got it!"
            
            show ava typical happy

            n "Ava excitedly flutters over to see how it turned out."

            ava @ say "Come here [name], check it out!"

            n "You think you both look a little bashful in the shot but you like it more than the other shot."

            player "Aww nice!"

            ava @ say "The sunlight coming from behind really worked in our favor."
            
            player "For sure. It makes your feathers glow so nicely!"
            
            show ava typical shy -
            
            ava @ say "You think so?"
            
            n "Ava shyly smiles, turning away from you."

    show claire happy
    show ava happy

    claire @ say "Right then, shall we continue our little adventure?"

    ava @ say "Sure! I think I'm all rested up and ready to go!"

    player "Sounds good to me!"
    
    hide ava
    hide claire
    with dissolve

    n "The three of you spend the rest of the day getting lost in the gardens, laughing, and having an all around good time."
    n "Eventually you find your way back to the entrance where you bid adieu and return to your respective dorms for the day."

    hide box
    
    stop music fadeout 1.0
    
    scene bg black with fade

    show bg calendar
    show tsaturday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    scene bg codadorm with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "You've fallen behind on homework and assigned reading. It's too easy to get distracted when you have the luxury of staying in your dorm without pants on."
    n "Maybe you need a place to study. Somewhere quiet. The library perhaps?"
    n "You pull back the curtain to check the weather just in time for a lightning strike to flashbang you."
    n "A roar of thunder rattles the building, soon followed by a flurry of water droplets pelting the window."
    n "...Better bring a rain coat."
    
    scene bg library with fade
    
    $ libraryDiscovered = True
    
    play music "audio/music/Vylet Pony - Cozy Pone.ogg" fadein .5
    
    show box with Dissolve(.2):
        ypos 0
        
    n "Wandering the labyrinth that is Harmonia's famously huge library, you happen to see someone you know out of the corner of your eye."
    n "No one else you've seen emits more 'goth bitch' vibes than her. You could smell her haunted graveyard perfume before you even turned the corner."
    n "She's just sitting there flipping through some oversized history book with her little paws."
    n "Didn't you have something for her?"
    n "Oh yeah, the book Mr. Rothbauer gave you! Is it still in your backpack?"
    n "While you're unzipping its pouches and digging through papers, Rose closes her book and begins to walk away."

    player "Rose! Wait up!"

    show rose armscrossed dismissive pendant at center with dissolve:
        ypos y_rose
        xzoom -1

    rose @ say "Hm? Oh, it's you. What do you want?"

    n "You pull the tattered book from your bag and hold it out for her."
    
    n "She seems confused at first but quickly snatches it from your grasp and continues on her way."

    player "Not even a 'thank you?'"

    show rose skirt fistsclenched angry pendant

    n "Rose snaps back around and glares at you."

    rose @ say "I told you I don't need your help. Now leave me alone."

    n "You pull a few loose papers from the pocket the book was in."

    player "What about these pages that fell out? Do you want those too?"

    show rose skirt furiouspose pendant

    rose @ say "Give those to me. Now."

    menu:
        rose "{cps=0}Give those to me. Now.{/cps=0}"
        "Only if you let me write a page of the project":
            $ goodEnd =+ 1
            
            n "You might end up regretting this later but you feel bad for making Rose do all the work."
            n "You have to at least put in a minimal effort."
            
            player "You can have them only if you let me write a page of the project."
            
            show rose skirt handonhip dismissive pendant

            rose @ say "Not gonna happen."

            player "I guess you'll never read these rare first hand accounts from..."

            n "You take a look at the pages, unfolding a crease that had formed on one."

            player "The Midwest Arcoonia tribe...?"
            
            show rose skirt fistsclenched angry pendant

            rose @ say "Get your filthy human hands off those!"

            n "She tries to take them but your superior opposable thumbs refuse to let go."

            player "Careful, you don't wanna rip them by accident."
            
            show rose skirt armscrossed furious pendant

            rose @ say "Ugh, fine! ONE page, that's it!"

            n "You let go of the papers with a smirk on your face."

            player "Deal!"
            
            n "Rose snatches the pages and turns away from you."
            
            show rose furiouspose 
            
            rose @ say "What the hell is this?!"
            
            n "Rose throws the papers right back into your face."
            n "Crude doodles and barely legible class notes drift past your eyes on their way to the floor."
            
            player "Woops, I guess those weren't pages that fell out of the book after all! Just my history notes~"
            
            show rose skirt fistsclenched angry pendant
            
            rose @ say "Ugh! Go to hell."

            hide rose with dissolve
            
            n "That went well."
            n "You find a table to sit at and crack open some books."
        "I'll trade them for something.":
            $ roseTrade = True
            
            player "Sure but you have to give me something in return."

            rose @ say "Are you out of your mind?! I'm not giving you anything!"

            player "I guess you'll never read these rare first hand accounts from..."

            n "You take a look at the pages."

            player "The Midwest Arcoonia tribe...?"
            
            show rose skirt fistsclenched angry pendant

            rose @ say "Get your filthy human hands off those!"

            n "She tries to take them but your superior opposable thumbs refuse to let go."

            player "Careful, you don't wanna rip them by accident."
            
            show rose armscrossed dismissive

            rose @ say "Ugh, unbelievable."
            rose @ say "..."
            rose @ say "*sigh*"
            
            show rose handonhip smug
            
            rose @ say "Fine, I'll give you something."
            rose @ say "Close your eyes."
            
            player "What is it?"
            
            rose @ say "Don't worry about it. Just close your eyes and relax. And lean down a little for me."
            
            scene bg black with dissolve
            
            n "You close your eyes as instructed. You're not sure whether to be anxious or excited."
            n "Is she getting closer? Your heart is racing. You're practically choking on her perfume."
            n "You feel something gently touching your cheek."
            n "Is that... Rose's paw?"
            n "You suddenly feel claws raking down your face, slicing into your skin."
            n "Your eyes shoot open and you reach up to your face with your hand to check if you're bleeding."
            n "You guess it was her paw after all."
                        
            scene bg library with dissolve
            
            show box with Dissolve(.2):
                ypos 0
                
            player "Ahh fuck! What the hell?!"
            
            n "While you're staring at your bloody fingers, Rose takes the opportunity to snatch the sheets of paper from your other hand."
            
            show rose skirt armscrossed annoyed pendant at center with dissolve:
                ypos y_rose
            
            rose @ say "What did you expect?"
            rose @ say "Life's not like one of your creepy animes. Learn to treat people properly or don't be surprised if you end up dead like the rest of your species sooner than later."
            rose @ say "It's a raccoon's world now and you're just living in it."

            hide rose with dissolve
            
            n "Holy hell that stung."
            n "Both the scratch and the insult."
            n "She better not have given you rabies just now."
            n "You walk away in shame to the restroom to clean yourself up."
            n "After cleaning the blood off your cheek, you find a table to sit at and crack open some books."
            
    n "What should you study?"
    
    menu:
        n "{cps=0}What should you study?{/cps}"
        "French":
            $ frenchSkill =+ 2
            n "You pick up your French textbook and practice some lessons."
        "Literature":
            $ literatureSkill =+ 2
            n "You open your totally legally acquired epub of [currentbook] and start reading."
        "History":
            $ historySkill =+ 2
            n "You crack open your History textbook and read up on some ancient cultures."
        "Statistics":
            $ statsSkill =+ 2
            n "You flip open your statistics book and open a calculator app to crunch some numbers."
            
    n "Without the distractions in place you feel like you learned more than you normally do."
    n "On your way out, a bulletin board catches your eye."
    n "A variety of flashy advertisements, events, and other announcements adorn the wall."
    n "Might as well take a quick look and see if anything interesting is coming up soon."
    
    label bulletinboard1:
        menu:
            n "{cps=0}Might as well take a quick look and see if anything interesting is coming up soon.{/cps}"
            "Local Student Dies...":
                n "You take a look at a newspaper clipping pinned to the board and move aside a piece of paper covering the rest of the headline."
                n "The full text is \"Local Student Dies in Horrific Vaping Accident\""
                n "Apparently he vaped so much he died. That's pretty much all there is to the story."
                n "Well if the cringe of being caught vaping wasn't enough to deter you from trying it, this cautionary tale will surely prevent you from even considering it."
                
                jump bulletinboard1
            "Gayest Pride Parade Ever":
                n "\"Come join the Gay Gay Homosexual Gay Club's 5th annual queerfest!\""
                n "It's a flyer for an upcoming traffic obstruction event... that happened 6 months ago."
                n "All the text is obnoxiously rainbow colored. All of it."
                n "How many times can they fit the word \"gay\" on a 4x5 inch sheet of paper?"
                n "You haven't been bombarded with this word this much since playing on Xbawks Live in middle school."
                
                jump bulletinboard1
            "Sick of Being a Furry?":
                n "\"Hate how your fur/feathers/scales look?\""
                n "\"Wish you had beautiful soft skin?\""
                n "\"Look no further than the skinwalker workshop every 3th Tuesday after a full moon at 2:14AM where we engage in roleplay with our inner human personas!\""
                n "This is borderline offensive to you."
                
                jump bulletinboard1
            "Generic Anti Suicide Poster":
                n "It literally says \"Generic Anti Suicide Poster\""
                n "It has a stock image of an office worker standing on his desk with a noose around his neck and giving a thumbs up."
                n "Oh my god it even has a watermark." 
                n "I guess they couldn't be bothered to put any effort into making this."
                n "The guy in charge of designing it probably killed himself and they had to outsource it."
                
                jump bulletinboard1
            "Quit reading":
                n "That's enough reading for one day. You've got places to do and things to be."

    stop music fadeout 1.3

    scene bg campus with fade

    show box with Dissolve(.2):
        ypos 0
        
    play music "audio/music/vylet - Ordinarily.ogg" fadein .4

    n "The following day..."
    
    show gunner neutral at center with dissolve:
        ypos y_gunner
        xzoom -1
        xoffset -480
    
    gunner "Yeah so then I'm like \"fuck you\" and -- oh hi Rori!"
    
    show gunner optimistic
    
    n "Gunner started following you after class and telling you frat boy stories until you came across Rori sitting on the grass working on something on his laptop."
    
    show rori surprised at center with dissolve:
        ypos y_rori
        xoffset 480
    
    rori @ say "Aaah!"
    
    n "It seems you've startled him."
    
    show rori sleepy
    
    rori @ say "Oh it's just you."
    
    show rori neutral
    
    rori @ say "I was just really deep into some spaghetti code and so focused on it I didn't see you there!"
    
    show gunner disgusted
    
    gunner @ say "Bruh you are *always* on your laptop fiddling with some command line shit."
    
    show gunner displeased
    
    gunner @ say "Why don't you ever I dunno, live your life?"
    
    show rori worried noblush
    
    rori @ say "This *is* my life."
    
    show gunner uncomfy
    
    gunner @ say "That is so sad."
    
    show gunner frown1
    
    gunner @ say "[name] we gotta intervene. I can't stand to see my roommate like this."
    
    player "What do you propose we do?"
    
    show gunner neutral
    
    gunner @ say "I dunno, how's that saying go? \"Be a faggot, break the law?\""

    show rori sleepy
    
    rori @ say "I think you mean \"Be gay, do crime.\""
    
    show gunner determined
    
    gunner @ say "Exactly! Let's commit a crime!"
    
    show gunner eyesclosed catface
    
    gunner @ say "No homo."
    
    show rori anxious
    
    rori @ say "W-why would I wanna do that?"
    
    show gunner wink catface
    
    gunner @ say "Cause it'll be fun? Back me up, [name]."
    
    menu:
        gunner "{cps=0}Cause it'll be fun? Back me up, [name].{/cps}"
#        "Gunner's right, we should all be gay":
#            player "Gunner's right, we should all be gay."
#            
#            show gunner hissing
#            
#            gunner @ say "What?! That's not...!"
#            
#            show rori laugh
#            
#            n "Rori laughs at your response and Gunner's reaction."
#            
#            show gunner frown1
#            show rori supersmug
#            
#            rori @ say "Alright I'm in. Can't be gay without a little crime, right?"
#            
#            player "Only in certain countries!"
#            
        "Gunner's right, we should all commit a crime":
            player "Gunner's right, commiting crime is fun."
            
            show gunner neutral
            show rori neutral
            
            gunner @ say "Exactly! What better way to bond with the bros than getting into some comic mischief?"
            
            show rori concerned
            
            rori @ say "Hmm."
            rori @ say "As long as it's not anything extreme, I guess I'll join in."
            
            gunner @ say "Right, no breaking into the White House today."
#        "\[Gay\] Maybe we shouldn't become criminals":
#            player "Can't we just be gay and not do crime?"
#            
#            show gunner displeased
#            
#            gunner @ say "Where's the fun in that?"
#            gunner @ say "You guys are so boooooring!"
#            
#            show rori soyface
#            
#            rori @ say "H-hey, I'm sure we can find a fun crime to commit!"
#            
        "Maybe we shouldn't become criminals":
            player "Maybe we could just do something legal?"
            
            show gunner displeased
            
            gunner @ say "Where's the fun in that?"
            gunner @ say "You guys are so boooooring!"
            
            show rori soyface
            
            rori @ say "H-hey, I'm sure we can find a fun crime to commit!"
            
    show gunner neutral
    show rori neutral
    
    player "Hmm... What's a good crime?"
    
    rori @ say "It has to be victimless. Like piracy."
    
    show gunner disgusted
    
    gunner @ say "Bruh have you seen what Somali pirates do?"
    
    show gunner uncomfy
    show rori smug
    
    rori @ say "No I mean like downloading movies for free."
    
    player "Is there any other way to download them?"
    
    show gunner itsover
    show rori neutral
    
    gunner @ say "Can we please not do some made up digital crime? The whole point of this is to get away from that nerdy stuff."
    
    show rori anxious
    show gunner optimistic
    
    rori @ say "Okay tough guy, what are your ideas?"
    
    show rori sleepy
    show gunner determined
    
    gunner @ say "We could rob a bank!"
    gunner @ say "[name] can be our getaway driver!"
    
    player "I thought we *weren't* gonna be harming anyone."
    
    gunner @ say "Bank money is federally insured. Nobody loses a cent!"
    
    rori @ say "What about the taxpayers?"
    
    gunner @ say "The government just reprints what gets stolen. It's like it never even happened."
    
    rori @ say "Still sounds too risky."
    
    show rori neutral
    show gunner neutral
    
    player "What if we were vigilantes?"
    
    show rori cheery
    
    rori @ say "Like Robinhood, stealing from the rich and giving to the poor?"
    
    show gunner frown1
    show rori neutral
    
    gunner @ say "But [name], I am the rich."
    
    show rori neutral
    
    rori @ say "Okay then you can be like Catman."
    
    show gunner optimistic
    
    gunner @ say "A loaded superhero who fights crime with crime? You might be onto something."
    
    player "Maybe we should start with something small. Like if we see someone steal a lady's purse we can beat him up and take his wallet."
    
    show gunner mischief
    
    gunner @ say "That's perfect! Now we just have to wait for some thug to commit a robbery in broad daylight on this wealthy college campus with cops who drive by every 5 minutes."
    
    show rori cheery
    
    rori @ say "Keep on the lookout boys, we've got crimes to..."
    
    show gunner frown1
    show rori concerned
    
    rori @ say "Wait are we doing crime or stopping it?"
    
    player "Both I think?"
    
    show gunner hissing
    
    gunner @ say "I say we're doing neither at this rate!"
    gunner @ say "Come on, crimes aren't just gonna come to us! We gotta go to the crimes!"
    
    show gunner displeased
    
    n "Gunner picks a seemingly random direction and confidently marches off. You look to Rori and the two of you wordlessly agree to follow him."
    
    stop music fadeout 2.0
    
    scene bg schoolhallways with fade
    
    play music "audio/music/vylet - there.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Hours passed with nary a crime to commit nor one to prevent. You've searched the university high and low but the problem is that there are just too many cameras and not enough potential victims."
    n "As hope fades away, a glimmer shines in some forgotten corner, drawing you towards it."
    
    player "Guys... You're gonna wanna see this."
    
    n "With perked up ears, Gunner and Rori trail behind you to a vending machine, one of many found throughout the hallways of Harmonia."
    n "But this one is different."
    n "Lodged between the glass and the shelves inside is a sad looking bag of pretzels someone had clearly paid for but been scammed by the unreliable mechanism."
    
    show gunner neutral at center with dissolve:
        ypos y_gunner
        xoffset -375
        xzoom -1
    show rori neutral at center with dissolve:
        ypos y_rori
        xoffset 375
    
    gunner @ say "Just look at how close that bag is to falling! You could blow on it and it'd come down!"
    
    rori @ say "Would it even be a crime to take it? It's already been paid for."
    
    n "Rori reaches his hoof into the slot at the bottom and tries fishing the bag out but is unable to reach far enough in."
    
    player "Check it."
    
    n "You point to the sticker on the case that says \"DO NOT SHAKE VENDING MACHINE\"."
    
    player "Are you thinking what I'm thinking?"
    
    n "Rori stands back up and rubs his chin."
    
    show rori smirk lookingaway
    
    rori @ say "Hmm. That definitely counts as a crime, right?"
    
    show rori smirk -
    show gunner mischief
    
    gunner @ say "I mean, we'd be liable for any damages to property or personel as a result of giving this bitch a shake, wouldn't we?"
    
    player "Sure sounds like criminal activity to me."
    
    show gunner determined
    
    gunner @ say "Gentlemen? Shall we?"
    
    n "With a collective nod, the three of you go on the offensive, kicking, shoving and jostling the machine. The pretzels hang tantalizingly but hold steady through your barrage."
    n "You're all left panting and exhausted, losing the will to continue this fight and slumping against the machine."
    
    show gunner annoyed
    
    gunner @ say "Gah! It's hopeless! It's stuck in there!"
    
    show rori worried noblush
    
    rori @ say "Hold on, I might have a few quarters. We can probably get two bags for the price of one."
    
    player "To hell with that! We didn't come this far just to be law abiding citizens did we?!"
    
    n "You bang your fist against the glass in frustration one last time and that seems to do the trick. Without any fanfare, the bag plops down into the receiving area."
    
    show gunner neutral
    show rori surprised
    
    gunner @ say "WE DID IT BOYS!!!!"
    
    show rori laugh

    rori @ say "Huzzah!"
    
    n "You reach in and grab your prize."
    
    show rori smirk
    
    player "Let us enjoy the spoils of our hardships, lads!"
    
    n "You rip open the top and reach in to grab a salty treat to chomp down on."
    
    player "Aww what the fuck? They're stale."
    
    show gunner frown1
    show rori concerned
    
    gunner @ say "No way. Lemme try!"
    gunner @ say "*cronch*"
    
    show gunner displeased
    
    gunner @ say "Ugh. Nope. Not worth it."
    
    n "Rori takes the bag and bites into a pretzel as well and gives an unsatisfactory grimace."
    
    rori @ say "Hmm. Just barely inedible."
    
    player "After all that work. Disappointing."
    
    show rori worried noblush
    
    rori @ say "Hey what's that?"
    
    n "You look to where Rori is pointing. In the shadows something skitters across the floor."
    
    show gunner frown1
    
    gunner @ say "Is that a rat?"
    
    show rori concerned
    
    n "Gunner pounces at it but it runs under the vending machine."
    
    show rori soyface
    
    rori @ say "Dude cut it out! He's just a little guy."
    
    show rori cheery
    
    rori @ say "He's probably just out looking for food. Here you go, have some pretzels."
    
    n "Rori places the bag on the ground with the open end facing the machine. Lightning quick, the rat comes out and snatches it, dragging it back into its lair."
    
    show rori neutral
    
    n "You, Gunner and Rori crouch down and peek into the gap between the floor and vending machine."
    n "Rori flashes the light from his phone, revealing a ragged grey rat digging through the bag and nibbling on pretzels."
    n "It ravenously chews through them, ignoring your gaze."
    
    show rori smirk
    
    rori @ say "Aww. Cute lil' guy."
    
    show gunner displeased
    
    gunner @ say "Yeesh, I didn't know Harmonia had a rat problem."
    
    show gunner frown1
    show rori neutral
    
    rori @ say "He's just trying to survive."
    
    player "Let's leave him to enjoy his feast."
    
    rori @ say "Yeah, I think that's enough crime for one day."
    
    stop music fadeout 2.0
    
    scene bg campus with dissolve
    
    show box with Dissolve(.2):
        ypos 0
        
    play music "audio/music/vylet - wish.ogg" fadein .4
        
    show gunner neutral at center:
        ypos y_gunner
        xoffset -375
        xzoom -1
    show rori neutral at center:
        ypos y_rori
        xoffset 375
    with dissolve
    
    show gunner snoring
    
    gunner @ say "Well this was a waste. I was looking forward to some quality law breaking time with my bros."
    
    show gunner frown1
    
    player "Eh, I thought it was a fun little sidequest."
    
    show rori smirk
    
    rori @ say "Perhaps the real crimes were the friends we made along the way."
    
    show gunner optimistic
    
    gunner @ say "Heh maybe you're right."
    
    n "Gunner yawns."
    
    gunner @ say "Man, I still gotta work on some homework before bed. We'll have to do some more illegal shit later."
    
    player "For sure."
    
    rori @ say "Yeah, I guess we'll be heading back to our dorms now. See you later [name]! This was a lot of fun!"
    
    player "Hell yeah. See you guys later."
    
    gunner @ say "Later man!"
    
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

label beauty_and_the_beast:

    scene bg codadorm with fade

    play music "audio/ambient/morning birds.ogg" fadein 0.1

    show box with Dissolve(.2):
        ypos 0

    n "You're woken up by a text notification."
    n "Stretching, you reach for your phone and see you have a new message from Claire."

    call phone_start from _call_phone_start_11

    call message_start("Claire", "Bonjour [name]! Excited for French today? c:", "claireavi.png") from _call_message_start_15

    call reply_message("Should I be?") from _call_reply_message_94

    call message("Claire", "We're gonna watch a french movie in class lol", "claireavi.png") from _call_message_125

    call reply_message("Aw sweet!") from _call_reply_message_95
    call reply_message("In that case yes I am excited for french today") from _call_reply_message_96

    call message("Claire", "Ye we're gonna watch an old black and white version of beauty and the beast from like the 40's", "claireavi.png") from _call_message_126
    call message("Claire", "It's one of my favorite stories so it'll be cool to see this version of it ^w^", "claireavi.png") from _call_message_127

    call reply_message("lol I can't wait") from _call_reply_message_97
    call reply_message("I like chill movie days") from _call_reply_message_98

    call message("Claire", "I'd be down for some movies and chill at my dorm if you want~", "claireavi.png") from _call_message_128
    call message("Claire", "I'm sure Ava wouldn't mind", "claireavi.png") from _call_message_129
    call message("Claire", "She might even join in~", "claireavi.png") from _call_message_351
    #call message("Claire", "Or at least watch", "claireavi.png")

    call reply_message("Better yet we could all just hang at my dorm") from _call_reply_message_99
    call reply_message("It gets lonely here cause I'm by myself") from _call_reply_message_100

    call message("Claire", "That works too~", "claireavi.png") from _call_message_130

    call reply_message("I have to get ready to go to literature now. See you in a couple hours!") from _call_reply_message_101

    call message("Claire", "Au revoir!", "claireavi.png") from _call_message_131

    call phone_end from _call_phone_end_12
    
    n "With that, you pack your things and get ready for class."
    
    scene bg schoolhallways with fade
    
    play music "audio/ambient/indoors people talking.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Looks like you're early today. So early that the previous class is still in session."
    n "What else is there to do other than loiter around waiting for your class to begin?"
    n "You wander around the halls, reading bulletin boards and mindlessly scrolling back and forth on your phone's home screen."
    n "The vending machine on this floor is out of your preferred snack. Maybe the one on the floor below you has it in stock?"
    n "As you push past the stairwell doors, you catch sight of an orange tail turning the corner on the stairs above."
    n "That's odd, this is the top floor. All that's above here is the rooftop level."
    n "Perhaps the rooftop access is unlocked? This warrants an investigation."
    
    stop music fadeout 2.0
    
    scene bg roof with fade
    
    #make ellen gentler
    
    play music "audio/music/vylet - glamour.ogg"

    show box with Dissolve(.2):
        ypos 0

    n "A gust of wind blows into your face as you open the rooftop door, reeking of cigarette smoke."
    
    show margaret smoking intrigued at center with dissolve:
        ypos y_margaret

    margaret @ say "Hm? [name]? You shouldn't be up here."

    n "You point at the no smoking sign on the wall."

    player "I'm pretty sure you're not supposed to be up here either."
    
    show margaret smoking happy

    margaret @ say "Bah, you got me. I promise not to rat you out if you don't say anything."

    player "Deal."
    
    show margaret smoking neutral

    n "You lean on the wall next to her."

    player "What are you doing up here anyway?"

    margaret @ say "What's it look like? I'm on break."

    player "Didn't think you were the type to smoke."
    
    show margaret smoking sad shocked
    
    margaret @ say "I'm not. Or at least I wasn't. I've just got things on my mind."

    hide margaret
    show margaret smoking neutral at center:
        ypos y_margaret

    #show margaret smoking melancholy

    player "Such as?"
    
    margaret @ say "Private things."

    player "Oh."

    margaret @ say "What about you?"

    show margaret smoking neutral

    player "Oh I just came up here cause I was curious if the door was unlocked and-"

    margaret @ say "No I mean, what have you got going on."

    player "Excuse me?"

    margaret @ say "I've taught hundreds of students, I can tell when one of them is struggling with something in their life."
    margaret @ say "Especially when they pass out and fall out of their chair in the middle of class."
    
    player "I don't... think anything is wrong?"
    
    margaret @ say "Hm."
    
    n "She takes a drag from her cigarette."
    
    margaret @ say "Or perhaps you don't know yet?"
    margaret @ say "In that case..."
    
    n "She pushes her cigarette tip against the cool concrete wall, smothering it and letting it fall to the floor."
    
    margaret @ say "Class is about to begin. See you there."
    
    hide margaret with dissolve
    
    stop music fadeout 2.0
    
    n "She walks past you, her fluffy tail brushing against your arm before she descends the staircase back into the building."
    n "Stunned, you stand in the breeze, motionless and thoughtless."
    n "What was that all about?"
    n "You hardly have time to ponder it, you have to get to class."
    
    scene bg lecturehall with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0
        
    show margaret happy at center with dissolve:
        ypos y_margaret
        
    margaret @ say "That's all for today! See you all later this week! And don't forget to read ahead!"
    
    hide margaret with dissolve
    
    n "You give Ms. Ellen a glance as you're walking out but she's busy with a stack of papers."
    n "She didn't seem like herself on the roof earlier."
    n "Or perhaps she's not herself when she's lecturing."
    n "You kinda wanna talk to her more but you have to hurry to your next class."
    
    scene bg classroom with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "As you walk into the classroom you notice the projector displaying the DVD menu for the film Claire mentioned you were gonna watch today."
    n "Not even a BlueyRay... Where does Harmonia's budget even go towards??"

    show claire sweater wave happy at center with dissolve:
        xoffset 500
        ypos y_claire

    claire @ say "Hey [name]! Glad you could make it today!"
    
    show claire -wave

    player "Hey Claire! Yeah, I really wasn't feeling too good the other day..."
    
    show claire sweater happy

    claire @ say "Being sick is the wooooorst! I'm happy you're feeling better!"

    player "Tell me about it..."

    hide claire with dissolve

    show celestine excited at center with dissolve:
        ypos y_celestine

    celestine @ say "Good afternoon class! Today we're going to be watching a favorite of mine, Beauty and the Beast!"
    
    show celestine neutral
    
    celestine @ say "I'm sure you're all familiar with the story, so you should be able to follow along and hopefully pick out some of the words they use."
    celestine @ say "It's good you were able to join us today, [name]! It would have been a shame for you to miss such a masterpiece."
    celestine @ say "Oh and it's a wonderful learning opportunity as well! I'm a firm believer that watching movies in another language is extremely helpful for familiarizing yourself with the language!"
    
    show celestine excited
    
    celestine @ say "Without further adieu, let's get into it!"

    hide celestine with dissolve

    n "Mrs. Celestine turns off the lights and hits play on the menu."
    ##n "During the film, you notice Claire idly sketching something in her notebook but it's too dark for you to tell what."
    n "The plot is generally the same as the animated version you watched as a kid but in terms of live action versions, this one is clearly superior to the more recent one."
    n "The lack of color makes the castle a lot spookier than it has any right to be, but you guess a little creepiness should be expected from a movie about a horrific beast."
    n "Mrs. Celestine interjects throughout the film to point out some interesting facts and translate a few not-so-obvious parts."
    n "Overall it's an interesting take on the story and it was fun trying to piece together sentences in a language you're barely versed in."

    show celestine neutral at center with dissolve:
        ypos y_celestine
        xzoom -1

    celestine @ say "C'est la fin! What did you all think of it?"
    
    pause .1
    
    show celestine with move:
        xoffset -400

    show claire sweater happy at center with dissolve:
        ypos y_claire
        xoffset 550

    claire @ say "I liked it! I picked up a few words they were saying and could infer what they were saying pretty well I think."

    celestine @ say "Tres bon! I may pick a few more movies to show in class in the coming months..."
    celestine @ say "But for now, enjoy your afternoon! You're all dismissed!"

    stop music fadeout 1.0

    scene bg campus with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    play music "audio/music/Evan Schaeffer - Aqueduct.ogg" fadein .5

    show claire sweater pose suggestive at center with dissolve:
        xzoom -1
        ypos y_claire
        xoffset -450
    
    show ava at offscreenright:
        ypos y_ava

    claire @ say "...That was a pretty good movie, wasn't it? I'm a sucker for any kind of romantic film!"

    player "Yeah, it wasn't bad. I'd sooner re-watch the animated version though."
    
    show claire sweater overjoyed

    claire @ say "The animated version will always hold a special place in my heart ksksksks!"
    gunner "{nw}"
    
    pause .1

    show ava typical happy at center:
        xoffset 350
        ypos y_ava
    with move

    show ava excited

    ava @ say "Hey guys!"
    
    show ava happy
    
    ava @ say "How was class?"
    
    show claire sweater happy
    
    player "We just got done watching La Belle et la Bête."
    
    show ava concerned

    n "Ava looks confused for a bit before figuring it out."
    
    show ava whimsical

    ava @ say "Ah right, French class."

    claire @ say "How was philosophy?"
    
    show ava annoyed

    ava @ say "Boring. It's all stuff I've already learned. I can't believe they didn't take my credits from high school."
    
    show claire derp

    claire @ say "Aww... at least you don't have to worry about your grade if you already know all the material!"
    
    show ava unimpressed
    
    ava @ say "Yeah. Honestly I might just start skipping class."
    
    show claire giggle
    
    claire @ say "Gasp!"
    
    n "She actually says the word gasp."
    
    claire @ say "What a naughty student you are!"
    
    ava @ say "Meh."
    
    show claire happy
    
    claire @ say "Actually, this gives me an idea..."
    
    n "Suddenly, your head feels so heavy it's going to drag you down to the ground as it painfully pulsates."
    n "You stumble back and take a deep breath."
    
    show ava shocked
    show claire sweater surprised earsup
    
    player "Ugh, I'd love to stay and chat but I've got a killer headache."
    player "I think I'm just gonna go back to my dorm and sleep it off."
    
    ava @ say "Hope you feel better soon!"
    
    claire @ say "Maybe you're still getting over your illness?"
    
    player "Yeah maybe."
    
    show claire happy wave
    show ava happy
    
    claire @ say "Take care [name]!"
    
    ava @ say "See you later!"
    
    player "Later guys."
    
    stop music fadeout 2.0
    
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
    
    scene bg campus with fade

    play music "audio/ambient/outdoors people talking.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "It's a lovely day out. Sun shines through the clouds and a light breeze rustles the leaves in the trees."
    n "You make it about halfway to the history building when you start to feel strange again."

    show bg static2
    pause .02
    show bg campus

    n "It becomes difficult to breathe and you feel a sharp pain thrashing about your whole body."
    n "Your vision begins to fade as you drop down to your hands and knees."

    show bg static1
    pause .02
    show bg static2
    pause .02
    show bg campus

    n "The last thing you recall is slumping to the ground and hearing someone call your name."

    rori @ say "[name]!!"

    stop music fadeout .5

    hide box

    #___thursday
label hospital_bound:

    scene bg black with fade

    n "..."
    n "....."
    n "......."

    scene bg hospital with fade

    show box with Dissolve(.2):
        ypos 0

    play music "audio/music/Mere Notilde - Empty Room.ogg" 

    show box with Dissolve(.2):
        ypos 0

    n "...Huh?"
    n "Where are you?"
    n "You hear beeps from a heart monitor."
    n "You try to look around but your whole body is aching."

    show rori concerned at center with dissolve:
        ypos y_rori

    rori @ say "[name]? You're finally awake!"
    rori @ say "Wait right here, I'll go get the doctor!"
    
    rori "{nw}"
    pause .1
    
    show rori at offscreenleft with move:
        ypos y_rori

    n "Before you can even respond, he runs out of the room."
    n "Did he bring you here? How long have you been out?"

    show kitsuragi at offscreenright:
        ypos y_kitsuragi

    n "He returns a few minutes later with a panda lady wearing a doctor's coat and carrying a clipboard."

    show rori neutral at center:
        xzoom -1
        ypos y_rori
        xoffset -450
    show kitsuragi at center:
        xoffset 450
        ypos y_kitsuragi
    with move
    
    pause .3

    kitsuragi @ say "Hello, [name]. I am Dr. Kitsuragi."
    kitsuragi @ say "First thing's first, how are you feeling? You seem to have taken a nasty fall but I'm more concerned about what may have caused it in the first place."

    player "Well... my body is pretty sore in general."
    
    n "You take a moment to listen to what your body is telling you."
    
    player "I guess I feel hungover?"
    
    n "The doctor raises a brow. She must have seen your records and knows you're below the legal age to consume alcohol."
    
    player "Not that I would really know what that feels like since I don't drink."
    player "I just have a throbbing headache and my muscles feel like I haven't moved in a week."
    player "And my throat is pretty dry."

    rori @ say "Oh, I've got a bottle of water!"

    n "Rori digs around in his backpack and hands you the bottle."
    n "You can barely reach your arm up to grasp it and opening the lid proves to be a challenge."
    n "The doctor raises her clipboard and jots down a note."

    kitsuragi @ say "Have you been experiencing these symptoms or any other strange sensations lately?"

    player "Err kinda? I've been having dizzy spells for the past week and I passed out in class yesterday."
    player "And I've been feeling really thirsty all the time for no reason. I'm plenty hydrated."
    
    show rori anxious

    rori @ say "Y-you passed out in class?!"

    kitsuragi @ say "And you didn't think to contact us before?"
    kitsuragi @ say "You realize that's a bit out of the ordinary, don't you?"

    player "I guess I figured it would just sorta fix itself if I ignored it..."
    
    show rori neutral

    kitsuragi @ say "I'd like to perform some tests that will hopefully determine the cause of these dizzy spells."
    kitsuragi @ say "You were unconscious for two whole days and I'm afraid to put you back on your feet."

    menu:
        kitsuragi "{cps=0}You were unconscious for two whole days and I'm afraid to put you back on your feet.{/cps}"
        "Two days?!":
            player "Two days?! There goes my attendance record."
            
            kitsuragi @ say "Your friend here waited by your side the whole time."
            
            player "Aww thanks Rori, you didn't have to do that."
            
            show rori cheery
            
            rori @ say "It's alright. I didn't want you to be alone."
            
            show rori neutral
            
            kitsuragi @ say "You can get caught up on your studies over the weekend. There are more pressing matters to tend to right now."
        "I can walk fine":
            player "I can walk just fine. See?"
            
            n "You throw the blanket off you and swing your legs over the edge of the bed."
            n "You can already tell this isn't going to end well but you've already committed to the bit."
            n "When your feet touch the cool tile floor, a numb sensation runs across your skin. The muscles that would normally hold your body up simply fail to do anything and you come crumpling down."
            
            show rori surprised
            
            rori @ say "[name]!"
            
            show rori concerned
            
            n "Rori helps you up and tucks you back into bed like a dumb useless baby."
            
            player "See? Perfectly normal."
            
            show rori neutral
            
            kitsuragi @ say "Riiiight..."
            
    kitsuragi @ say "In any case, I would encourage you to return home, Rori. Don't worry, we'll keep a close eye on [name]."
    
    show rori anxious

    rori @ say "Aww... Alright."

    n "Rori looks somewhat disappointed but understanding."

    player "Here Rori, lemme give you my phone number so I can update you when they find out what's wrong with me."
    
    show rori soyface

    n "Rori immediately brightens up and pulls out his phone."

    rori @ say "Sure! What is it?"
    
    show rori neutral

    n "You tell him your number and he types it into his contact list."

    rori @ say "Aaaaand done!"
    rori @ say "I'll text you later [name]. Get well soon!"

    player "Thanks Rori!"

    n "He grabs his backpack and gives you a fist bump on his way out."

    hide rori with dissolve

    show kitsuragi with move:
        xoffset 0

    n "The doctor waits for Rori to be out of earshot before sighing and turning to you."
    
    kitsuragi @ say "Is there anything else you've experienced lately? Hallucinations perhaps?"
    
    player "Nah but schizophrenia does run in the family."
    
    kitsuragi @ say "I see."
    kitsuragi @ say "And your memory? Are you have trouble remembering things?"
    
    player "Sometimes I end up somewhere without any recollection of *how* I got there. It feels like time is just skipping randomly."
    
    kitsuragi @ say "Mh-hm."
    
    n "She produces a small pen light from her coat pocket and turns it on."
    
    kitsuragi @ say "Please bear with me. This will be uncomfortable but try to look straight ahead. You will be blinded momentarily but this won't cause permanent damage."
    
    n "You don't say anything. You just brace yourself and let the doctor shine a cool white beam of light directly into your eyes, one at a time."
    n "The light shuts off but it takes a while for your vision to return."
    
    player "What did you see?"
    
    kitsuragi @ say "Hm."
    
    n "She's busy writing a long winded note on her clipboard, the sound of a ballpoint pen scratching against paper bouncing off the walls as you wait in unbearable anticipation."
    n "Eventually, she clicks her pen and sighs."

    kitsuragi @ say "Given your... situation..."
    kitsuragi @ say "I don't want to jump to conclusions, but you know what these symptoms remind me of?"

    player "Yeah..."
    
    n "You look down."
    n "You had always known this moment would come, but nothing could ever prepare you for it. So you chose to ignore it until now."
    n "Can't exactly ignore something that's staring you in the face, can you?"
    
    player "I figured it was only a matter of time but I never expected it to start so soon."

    kitsuragi @ say "Hey, all I have to go on is a hunch. I haven't even taken your blood for testing or anything yet."
    kitsuragi @ say "We'll get started on some tests soon. There's no point in worrying until we have a proper diagnosis."
    kitsuragi @ say "I'll be back in a little bit."

    hide kitsuragi with dissolve
    
    n "The disease that took your parents' lives, as well as the lives of billions of humans over the past one hundred and fifty years, rendering them to the brink of extinction... "
    n "Has it come to take you as well?"
    n "You were vaccinated against the most recent known strain when you were little, but it has a tendency to mutate rapidly."
    n "Maybe you are just jumping to conclusions. There's still no confirmation you have it. For now."
    n "There's a knock on the door and Dr. Kitsuragi returns with a cart full of testing equipment."
    n "This is going to take a while."

    stop music fadeout 1.0

    hide box

    scene bg black with fade

    hide box

    scene bg hospital with fade

    #play music "audio/music/Evan Schaeffer - Encomium.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "After several hours worth of tests, they made you stay the night here."
    n "You're already tired of this place. There's nothing more uncomfortable than lying in a hospital bed, no matter how soft the pillows are."
    n "But they insist that you remain here at least until they can get the dizzy spells under control."
    n "At least now you have a convenient excuse for falling behind in class."

    play audio "audio/sound effects/vibrate.ogg"

    n "Huh? Sounds like you got a text. You reach for your phone."

    call phone_start from _call_phone_start_3

    call message_start("Gunner", "Why did you skip stats lol", "gunneravi.png") from _call_message_start_3

    call reply_message("Wasn't feeling well, went to the doctor.") from _call_reply_message_11

    call message("Gunner", "Oh shit for real??? Are you ok", "gunneravi.png") from _call_message_10

    call reply_message("Yeah just fell down and stuff.") from _call_reply_message_12

    call message("Gunner", "Alright well I hope you feel better soon", "gunneravi.png") from _call_message_11
    call message("Gunner", "BTW herschel said to do the homework problems for lesson 2-3", "gunneravi.png") from _call_message_12

    call reply_message("Thanks") from _call_reply_message_13

    call message("Gunner", "See you on Monday!", "gunneravi.png") from _call_message_13

    call phone_end from _call_phone_end_3

    n "Gunner is probably still lost in that class. Maybe you should work on the homework so you don't fall too far behind."
    n "You think you still have all your textbooks in your bag. It's lying just within reach beside the bed."
    n "What should you study?"
    
    menu:
        n "{cps=0}What should you study?{/cps}"
        "French":
            $ frenchSkill =+ 1
            n "You pick up your French textbook and practice some lessons."
        "Literature":
            $ literatureSkill =+ 1
            n "You open your totally legally acquired epub of [currentbook] and start reading."
        "History":
            $ historySkill =+ 1
            n "You crack open your history textbook and read up on some ancient cultures."
        "Statistics":
            $ statsSkill =+ 1
            n "You flip open your statistics book and open a calculator app to crunch some numbers."
    
    n "Time flies and before you know it, it's dark out."
    n "Oh shoot, Rori is probably still wondering if you're alright! Better send him a text."
    
    call phone_start from _call_phone_start_16
    
    call message_start("me", "Hey Rori", "testimage.png") from _call_message_start_21
    call reply_message("Thanks for dragging my ass to the hospital") from _call_reply_message_135 
    
    call message("Rori", "Np", "roriavi.png") from _call_message_191 
    call message("Rori", "I actually carried you btw", "roriavi.png") from _call_message_192 
    
    call reply_message("Oh for real?") from _call_reply_message_136
    call reply_message("Damn you must be strong") from _call_reply_message_137 
    
    call message("Rori", "It actually wasn't that hard once I got you up on my shoulder", "roriavi.png") from _call_message_193 
    call message("Rori", "You alright?", "roriavi.png") from _call_message_194 
    
    call reply_message("Myeah probably") from _call_reply_message_138
    call reply_message("I'm still at the hospital cause they wanna do more tests") from _call_reply_message_139
    
    call message("Rori", "Fug that's a long time", "roriavi.png") from _call_message_195 
    call message("Rori", "Hope it's nothing serious", "roriavi.png") from _call_message_196 
    
    call reply_message("They just want me to stay here until they're sure I won't randomly pass out in the middle of the street again.") from _call_reply_message_140 

    call message("Rori", "Ahh makes sense", "roriavi.png") from _call_message_197 
    call message("Rori", "Need me to bring you anything ?", "roriavi.png") from _call_message_198 

    call reply_message("Nah I'm good. I got my school books and stuff.") from _call_reply_message_141 
    call reply_message("Thanks tho") from _call_reply_message_142 
    
    call message("Rori", "Text me if you want anything", "roriavi.png") from _call_message_199 
    call message("Rori", "I know hospital food sucks", "roriavi.png") from _call_message_200 
    
    call reply_message("Thx will do") from _call_reply_message_143 
    
    call phone_end from _call_phone_end_22
    
    n "You put the phone down and sigh, wondering how much longer you'll be confined here."
    n "With not much else to do, you pull up the blanket and try to fall asleep."
    
    stop music fadeout 1.0

    hide box

    scene bg black with fade

    hide box

    #___saturday

    scene bg hospital with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    play music "audio/music/Evan Schaeffer - Encomium.ogg" fadein .5

    n "Ugh it's already Saturday."
    n "The hospital must be trying to milk your insurance money dry because they're still not letting you leave."
    n "You're tempted to just get up and walk out the front door."
    n "What are they gonna do, call the police and arrest you?"
    
    play audio "audio/sound effects/vibrate.ogg"
    
    n "Hm?"

    call phone_start from _call_phone_start_4

    call message_start("Ava", "Hey [name] I heard you weren't feeling well so I just wanted to check in on you.", "avaavi.png") from _call_message_start_4

    call reply_message("Hey Ava. Yeah everything's fine, just feeling a little under the weather.") from _call_reply_message_14

    call message("Ava", "Oh nooo ;^;", "avaavi.png") from _call_message_14
    call message("Ava", "Hopefully nothing serious?", "avaavi.png") from _call_message_15

    call reply_message("Nah but I'm confined to bed unfortunately.") from _call_reply_message_15

    call message("Ava", "Dang, I was gonna see if you wanted to come to this party with me and Claire..", "avaavi.png") from _call_message_16

    call reply_message("Sorry, I would totally go if I could :/") from _call_reply_message_16

    call message("Ava", "That's fine, there will be plenty more parties I'm sure! ^v^", "avaavi.png") from _call_message_17
    call message("Ava", "Get well soon~", "avaavi.png") from _call_message_18

    call reply_message("Thank") from _call_reply_message_17

    call phone_end from _call_phone_end_4
    
    pause .2
    
    n "That party sure sounds fun... if only you weren't stuck here."
    
    if mishkaMall == True:
        n "More importantly, Mishka is probably leaving to go to the mall right about now."
        n "What's she going to think when she doesn't see you there?"
    
    menu:
        "Try to escape":
            n "You've gotta get out of here."
            n "You windows are too small for you to squeeze through. You'll have to just get up and walk through the front door."
            n "Can't be that hard, right? It's not like everybody is on the lookout for you, and for all they know you're cleared to leave."
            n "You quietly slip out of bed and put your shoes on before grabbing your bag and approaching the door."
            
            scene bg schoolhallways with dissolve
            
            show box with Dissolve(.2):
                ypos 0
            
            n "Phase one complete."
            n "Now you're confronted with a problem you didn't anticipate: How the hell do you get out of here?"
            n "You have no recollection of how you got here and the hallways are like a maze."
            
            kitsuragi "Hey!"
            
            n "Busted!"
            n "You look around for a good place to escape but you're cornered."
            
            show kitsuragi at center with dissolve:
                ypos y_kitsuragi
            
            kitsuragi @ say "You get lost on the way to the bathroom or something?"
            
            n "She looks at your bag and shoes."
            
            kitsuragi @ say "Or were you just trying to escape?"
            
            menu:
                kitsuragi "{cps=0}Or were you just trying to escape?{/cps}"
                "Just had to pee haha":
                    n "You feel like a small child who's been caught with his hand in the cookie jar."
                    n "You know that she knows that you know that you were trying to escape, but we can all just play dumb here and act like this never happened."
                    
                    player "Haha yeah, just had to pee and forgot how to get to the restroom."
                    
                    kitsuragi @ say "The one directly across from your room?"
                    
                    player "Yes, that one."
                    
                    kitsuragi @ say "It's down the hall and to the left. Not to the right, that way leads to the exit where the security guard will check if you're cleared to leave."
                    kitsuragi @ say "And definitely not the way you were heading toward the fire escape. That'd trigger an alarm and get you a misdemeanor."
                    
                    player "Thanks..."
                    
                    kitsuragi @ say "Anytime."
                    
                    hide kitsuragi with dissolve
                    
                    n "You sheepishly follow her directions and return to your room."
                    
                "Screw this place":
                    n "You feel like a small child who's been caught with his hand in the cookie jar."
                    n "But then a rage suddenly bubbles up from within."
                    
                    player "Screw this place! I've had enough! You can't keep me here!"
                    
                    kitsuragi @ say "Maybe I can't but security can."
                    kitsuragi @ say "The guard at the door knows to not let you leave. Only other way out is through the fire escape."
                    kitsuragi @ say "Which is a misdemeanor to use if there's no emergency by the way."
                    
                    player "So this place really is a jail, huh?"
                    
                    kitsuragi @ say "Pretty much."
                    kitsuragi @ say "Go back to your room. I'll see you tomorrow."
                    
                    hide kitsuragi with dissolve
                    
                    n "The doctor turns around and walks away."
                    n "Nothing left for you to do but return to your cell."
                    
        "Stay here":
            n "Can you really just get up and leave? Won't somebody notice?"
            n "You really don't feel like getting tackled by security right now."
            n "You should just stay put and study like a good student."
            n "Or at least pass the time browsing the web."

            menu:
                n "{cps=0}Or at least pass the time browsing the web.{/cps}"
                "Read for literature":
                    $ literatureSkill =+ 1
                    
                    n "You lean over and reach into your backpack to pull out your copy of [currentBook]."
                    n "Luckily you had your headphones in your bag as well. You put them on and get to reading."
                "Work on stats homework":
                    $ statsSkill =+ 1
                    
                    n "You lean over and reach into your backpack to pull out your stats textbook."
                    n "Luckily you had your headphones in your bag as well. You put them on and get to studying."
                    n "\"Given the rarity of a particular disease .02 and the chance of a false negative .08, find the probability that a patient actually has the disease if the test yields a positive result...\""
                "Study history":
                    $ historySkill =+ 1
                    
                    n "You don't have any homework in history but it would still do you some good to crack open the textbook and do a bit of studying for the test."
                    n "Luckily you had your headphones in your bag as well. You put them on and start reading."
                    n "You don't remember where class left off so you flip to a random page."
                    n "In his final moments before his execution, the leader of the expedition famously said to the Arcoonian tribe..."
                "Practice French":
                    $ frenchSkill =+ 1
                    
                    n "Better brush up on your French, it's one of those things where if you don't use it you lose it."
                    n "Luckily you had your headphones in your bag as well. You put them on and start reading."
                    n "Il fait un temps affreux translates to the weather is terrible! Take note of the use of Il fait, which means it makes or it does, rather than it is..."
                "Browse pinstagram":
                    $ avaPoints =+ 1
                    
                    n "You know what, you really don't feel like doing homework right now."
                    n "Instead, you'd like to indulge in the finer arts society has to offer."
                    n "You tap the pinstagram app on your phone and instantly receive a dopamine rush as dozens of random images crowd your screen."
                    n "After a bit of scrolling, you stumble upon Ava's profile."
                    n "The software must have automatically detected you have her number in your contacts and added her to your news feed."
                    n "Sometimes the FBI agent monitoring your internet connections is pretty cool like that."
                    n "Ava's got some nice pics on here. Just like she said, she's really into landscape shots."
                    n "Some of these look like they're taken from high up. She's probably perched in a tree judging by the looks of it."
                    n "Kinda makes you wanna go out and explore. Maybe you will once you're free from this dreaded hospital."

    scene bg black with fade
    
    stop music fadeout 2.0

    play audio "audio/sound effects/vibrate.ogg"

    n "*Buzz buzz*"

    scene bg hospital with fade

    show box with Dissolve(.2):
        ypos 0

    n "You look around as your brain scrambles to recall where you are."
    n "Oh right, you're still in this dreadful hospital."
    n "You must have fallen asleep."
    n "You check your phone and see you just received a new message from Claire."

    hide box

    call phone_start from _call_phone_start_6

    call message_start("Claire", "Heyyyyyyy [name] c:", "claireavi.png") from _call_message_start_8

    call reply_message("Hey?") from _call_reply_message_26

    call message("Claire", "I mnt to text u earlrie but got distractedddddddd sorry", "claireavi.png") from _call_message_36

    call reply_message("It's ok") from _call_reply_message_27

    call message("Claire", "Wishj u werehere w tih us", "claireavi.png") from _call_message_37

    call reply_message("?") from _call_reply_message_28

    call message("Claire", "Me an d ava", "claireavi.png") from _call_message_38
    call message("Claire", "We 're at pqrty", "claireavi.png") from _call_message_39
    call message("Claire", "Partyr", "claireavi.png") from _call_message_40
    call message("Claire", "Panties", "claireavi.png") from _call_message_41
    call message("Claire", "Party", "claireavi.png") from _call_message_42

    call reply_message("Oh") from _call_reply_message_29
    call reply_message("How is it") from _call_reply_message_30

    call message("Claire", "Im drunk olo", "claireavi.png") from _call_message_43
    call message("Claire", "Lol", "claireavi.png") from _call_message_44

    call reply_message("Cool") from _call_reply_message_31

    call message("Claire", "Ur cute btw", "claireavi.png") from _call_message_45

    call screen phone_reply("Me??","choice3","No u","choice4")

    label choice3:
        $ clairephonewhat = True

        call phone_after_menu from _call_phone_after_menu_2

        call message_start("me", "Me??", "testimage.png") from _call_message_start_9

        call message("Claire", "Yeah you!", "claireavi.png") from _call_message_46

        call reply_message("Idk about that") from _call_reply_message_33

        call message("Claire", "Wait", "claireavi.png") from _call_message_47

        call reply_message("?") from _call_reply_message_35

        call message("Claire", "Nvm", "claireavi.png") from _call_message_48

        call reply_message("aargh") from _call_reply_message_36

        call message("Claire", "Aav advised me to 'shut the hell up oh my god'", "claireavi.png") from _call_message_49

        call reply_message("Maybe you should take her advice") from _call_reply_message_37

        call message("Claire", "Idc if I regert th is later but fuck it", "claireavi.png") from _call_message_50
        call message("Claire", "Srsly I think your cute and I wann a kiss youre face", "claireavi.png") from _call_message_51
        call message("Claire", "Ok wow rude", "claireavi.png") from _call_message_52

        call reply_message("Sorry, I'm just frustrated cause I'm stuck in this hospital potentially dying and can't party with you") from _call_reply_message_38

        call message("Claire", "...", "claireavi.png") from _call_message_53
        call message("Claire", "Are you being sarcasm ?", "claireavi.png") from _call_message_54

        call reply_message("maybe idk") from _call_reply_message_39
        call reply_message("fuk") from _call_reply_message_40

        call phone_end from _call_phone_end_6

        show bg static1
        pause .05
        show bg hospital

        stop music fadeout 2.0

        show box with Dissolve(.2):
            ypos 0

        n "The headache returns with a vengeance and your phone drops to the floor."

        show bg static2
        pause .05

        show bg hospital

        n "Your head hurts so much."

        show bg static1
        pause .05
        show bg static3
        pause .05
        show bg static1
        pause .05
        show bg static2
        pause .05

        show bg hospital

        n "You shut your eyes tight and before you even realize it, you're out cold."

        hide box

        show bg static2
        pause .1
        show bg static1
        pause .1
        show bg static3
        pause .1
        show bg static2
        pause .1
        show bg static3
        pause .1
        show bg static2
        pause .1
        show bg static1
        pause .1
        show bg static3
        pause .1
        show bg static2
        pause .1
        show bg static3
        pause .1

        jump aftermenu2

    label choice4:
        $ clairePoints =+ 1
        $ clairephonethx = True

        call phone_after_menu from _call_phone_after_menu_3
        call message_start("me", "No u~", "testimage.png") from _call_message_start_10

        call message("Claire", "Aaaaaaaa thxhxhxhxhxadsfjaksdfafokdwjpoiqefsa", "claireavi.png") from _call_message_55

        call reply_message("Ok i think you've had too much to drink") from _call_reply_message_41

        call message("Claire", "Naaaaahhhhh you should see Ava tho omg", "claireavi.png") from _call_message_56
        call message("Claire", "Literal featherweight", "claireavi.png") from _call_message_57

        call reply_message("Sounds like a good time") from _call_reply_message_42
        call reply_message("Wish I wasn't stuck in this stupid hospital") from _call_reply_message_43

        call message("Claire", "Yeah ;(", "claireavi.png") from _call_message_58
        call message("Claire", "Hold on", "claireavi.png") from _call_message_59
        call message("Claire", "I got smth thatll cheer u up", "claireavi.png") from _call_message_60

        call reply_message("What is it") from _call_reply_message_44
        call reply_message("????") from _call_reply_message_45

        call message("Claire", "Sry keep u waiiting, took a bit to conmvince ava", "claireavi.png") from _call_message_61
        call message_img("Claire", "Enjoy~", "pic1.png") from _call_message_img
        
        call reply_message("BOOBA") from _call_reply_message_144

        call phone_end from _call_phone_end_7

        show bg static2
        pause .05

        show bg hospital

        stop music fadeout 2.0

        show box with Dissolve(.2):
            ypos 0

        n "Your phone slips out of your hand and falls to the floor as an immense headache washes over you."

        show bg static1
        pause .05
        show bg static3
        pause .05
        show bg static1
        pause .05
        show bg static2
        pause .05

        show bg hospital

        n "Your head hurts so much."

        n "You shut your eyes tight and before you even realize it, you're out cold."

        hide box

        show bg static2
        pause .1
        show bg static1
        pause .1
        show bg static3
        pause .1
        show bg static2
        pause .1
        show bg static3
        pause .1
        show bg static2
        pause .1
        show bg static1
        pause .1
        show bg static3
        pause .1
        show bg static2
        pause .1
        show bg static3
        pause .1

        jump aftermenu2

label aftermenu2:

    stop music fadeout 1.0

    scene bg black with fade

    n "..."

    #___sunday
label leaving_hospital:

    scene bg hospital with fade

    play music "audio/ambient/morning birds.ogg" fadein 0.1

    show box with Dissolve(.2):
        ypos 0

    n "Morning light shines through the window."
    n "What day is it?"
    n "How much longer are you gonna be stuck here?"
    n "You reach over to the nightstand for your phone and notice the doctor standing by the door."

    show kitsuragi at center with dissolve:
        ypos y_kitsuragi

    kitsuragi @ say "Good morning, [name]. How are you feeling?"

    player "Better than last night. Had another one of those migraines but I'm fine now."

    kitsuragi @ say "Well I have some good news for you."
    kitsuragi @ say "While we don't know for certain what's causing these migraines and dizzy spells, we managed to get ahold of something that should reduce their intensity."

    n "The doctor tosses a bottle of pills at you."

    kitsuragi @ say "Read the instructions carefully otherwise ya might die."
    kitsuragi @ say "...I'm kidding! Well, kinda. Seriously, read the instructions. Two a day. Any more than that and you're bound to undergo some strange side effects."
    kitsuragi @ say "Contact us immediately if you experience another one of these incidents."

    player "You mean I'm free to leave?"

    kitsuragi @ say "That's correct. We ask that you take it easy though since we don't know what exactly triggers your symptoms."
    kitsuragi @ say "In the mean time, we'll continue our tests and we'll let you know as soon as we discover anything."

    player "So you still don't even know if I'm dying? Like, when would the tests show that?"

    kitsuragi @ say "It's hard to say. We don't have all the equipment here to test for it so we had to send your blood across the country to find out."
    kitsuragi @ say "From what we can tell here though, you appear to be fine. I actually really doubt it's anything to be seriously concerned about."
    kitsuragi @ say "You said you started experiencing symptoms shortly after you moved here, right?"
    kitsuragi @ say "Well, city water isn't as pure as they'd like you to believe. If you can, try drinking bottled water or get one of those fancy filters."

    player "Damn government putting chemicals in the water."

    kitsuragi @ say "Haha yeah."

    n "She helps you out of bed and makes sure you can walk before letting you loose."

    kitsuragi @ say "Stay safe, kid. Don't hesitate to call us with any questions you may have!"

    player "Thanks. I'll let you know if anything comes up."

    kitsuragi @ say "You better!"

    hide kitsuragi with dissolve

    n "The doctor accompanies you to the lobby and sees you out."

    n "From there, you decide to head back to your dorm and chill in the comfort of your own home, away from that gross hospital."

    stop music fadeout 1.0

    scene bg codadorm with fade

    play music "audio/music/vylet pony - Reading at Night.ogg"

    show box with Dissolve(.2):
        ypos 0

    n "After taking a shower and fixing yourself a bowl of cereal, you nestle up in bed and check on your texts."

    if clairephonethx == True:
        call phone_start from _call_phone_start_7

        call message_start("Claire", "Ahahahah I k new youd like tht~", "claireavi.png") from _call_message_start_11
        call message("Claire", "Plenty more where that came from~", "claireavi.png") from _call_message_62
        call message("Claire", "...", "claireavi.png") from _call_message_63
        call message("Claire", "[name]?", "claireavi.png") from _call_message_64
        call message("Claire", "Hellooooooo ?", "claireavi.png") from _call_message_65

        call reply_message("Hey sorry I passed out") from _call_reply_message_47
        call reply_message("I think that pic you sent almost killed me lmao") from _call_reply_message_48

        call message("Claire", "Rly?? Lmao", "claireavi.png") from _call_message_66
        call message("Claire", "Last night was sooo wild. You shoulda been there!", "claireavi.png") from _call_message_67

        call reply_message("Believe me, there's no other place I would have rather been.") from _call_reply_message_49
        call reply_message("Oh I'm free from the hospital now btw!") from _call_reply_message_50

        call message("Claire", "No way! We should celebrate!", "claireavi.png") from _call_message_68

        call reply_message("Yeah lol I'm interested in what that 'plenty more where that came from' really meant") from _call_reply_message_51

        call message("Claire", "OMG ksksksksks", "claireavi.png") from _call_message_69
        call message("Claire", "You'll have to buy me a few drinks first ;)", "claireavi.png") from _call_message_70

        call reply_message("That, I can do.") from _call_reply_message_52

        call message("Claire", "Mmmmaybe wait til next weekend when I'm not hungover lol", "claireavi.png") from _call_message_71
        call message("Claire", ":P", "claireavi.png") from _call_message_72
        call message("Claire", "Ava says hi btw", "claireavi.png") from _call_message_73

        call reply_message("Tell her I said hi") from _call_reply_message_53
        call reply_message("Also thx for the pic last night >:3") from _call_reply_message_54

        call message("Claire", "Ksksksksks she says she'll kill you if you show anyone that pic!", "claireavi.png") from _call_message_74

        call reply_message("Never would have thought she'd be camera shy~") from _call_reply_message_55

        call message("Claire", "She'd really kill you if you said that to her LOL", "claireavi.png") from _call_message_75

        call reply_message("Heh") from _call_reply_message_56
        call reply_message("Well I'll let you get back to your hangover. I'll see you in French later!") from _call_reply_message_57

        call message("Claire", "See yaaaaaa!!!!", "claireavi.png") from _call_message_76
        call message("Claire", "Cutie~ :3", "claireavi.png") from _call_message_77

        call phone_end from _call_phone_end_8

    elif clairephonewhat == True:
        call phone_start from _call_phone_start_8

        call message_start("Claire", "Uhh ok?????", "claireavi.png") from _call_message_start_12
        call message("Claire", "I mean I just gace y ou a conplimemt nd u kinda just blew up on me so", "claireavi.png") from _call_message_78
        call message("Claire", "Whatevr", "claireavi.png") from _call_message_79
        call message("Claire", "[name]?", "claireavi.png") from _call_message_80
        call message("Claire", "Hellooooooo ?", "claireavi.png") from _call_message_81

        call reply_message("Hey sorry I passed out") from _call_reply_message_58
        call reply_message("Again, sorry about last night. I wasn't feeling well.") from _call_reply_message_59
        call reply_message("Good news is that I'm out of the hospital now and they gave me some pills that may or may not help with that.") from _call_reply_message_60

        call message("Claire", "Ohmygosh I'm sooooo sorry about all that!", "claireavi.png") from _call_message_82
        call message("Claire", "I was being so cringe Dx", "claireavi.png") from _call_message_83

        call reply_message("What no, I was being cringey") from _call_reply_message_61

        call message("Claire", "Lol let's just say we both were", "claireavi.png") from _call_message_84
        call message("Claire", "And let's agree never to speak of it again, k?", "claireavi.png") from _call_message_85

        call reply_message("Lmao k") from _call_reply_message_62
        call reply_message("How was the party?") from _call_reply_message_63

        call message("Claire", "It was fun! Me and Ava had a great time!", "claireavi.png") from _call_message_86
        call message("Claire", "Hangovers are a biiiitch tho", "claireavi.png") from _call_message_87

        call reply_message("I can imagine.") from _call_reply_message_64

        call message("Claire", "I hope you're feeling better than us lol", "claireavi.png") from _call_message_88

        call reply_message("I'm feeling alright") from _call_reply_message_65
        call reply_message("For now") from _call_reply_message_66

        call message("Claire", "Das gud", "claireavi.png") from _call_message_89
        call message("Claire", "I got worried when you said you were in the hospital,", "claireavi.png") from _call_message_90

        call reply_message("Meh, it's nothing serious.") from _call_reply_message_67
        call reply_message("These pills should help") from _call_reply_message_68

        call message("Claire", "Hope so!", "claireavi.png") from _call_message_91

        call reply_message("Lol") from _call_reply_message_69
        call reply_message("Well I'll let you get back to your hangover. I'll see you in French later!") from _call_reply_message_70

        call message("Claire", "See yaaaaaa!!!!", "claireavi.png") from _call_message_92

        call phone_end from _call_phone_end_9

    n "You eat your cereal while watching videos, remembering to take one of your pills."
    n "You've got some free time today, what should you do?"
    
    if mishkaMall == True:
        $ mishkaMallSpecialActive = True
    
    call afterClassOptions from _call_afterClassOptions_1
    
    #n "The doctor said to take it easy, so you're just gonna relax in bed all day."
    
    #n "You still have class in a few hours after all."
    #n "When it comes time for you to go to bed, you pop another one of those pills, as instructed."
    #n "You're already getting sick of them but you gotta do what you gotta do to stay alive you guess."
    #n "You rest your head on your pillow and pray nothing bad happens tomorrow as sleep overtakes you."

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
    
label monty_hall:
    scene bg codadorm with fade

    play music "audio/ambient/morning birds.ogg" fadein .4

    show box with Dissolve(.2):
        ypos 0

    n "You wake up and pop one of the pills the doctor gave you."
    n "You're not sure if it's just placebo, but for the first time in nearly a week you don't feel like death which is a good sign."
    n "Returning to class is kind of a drag but it's better than being in that hospital."
    
    stop music fadeout 1.5
    
    scene bg classroom with fade
    
    play music "audio/music/mere - schooldaze.ogg" fadein .4

    show box with Dissolve(.2):
        ypos 0
    
    n "You drifted off into a daydream during history class, only returning to reality when you heard your name called."
    
    show rothbauer at center with dissolve:
        ypos y_roth

    rothbauer @ say "[name], could you tell the class why there's no class on Friday?"

    player "Huh? I've been coming in on Fridays for nothing?"

    n "Mr. Rothbauer sighs. You get the feeling that was supposed to be an easy question."

    rothbauer @ say "Must have been a long night studying, eh?"
    rothbauer @ say "*This* Friday is a holiday. Anthromorph's Liberation Day!"
    rothbauer @ say "89 years ago, following the mass reduction in human population, the National Liberties Act was signed which gave anthromorphs equal rights to humans."
    rothbauer @ say "It took several rebellions, riots, and even wars throughout centuries to reach this monumental turning point in history."
    rothbauer @ say "Though it was population dynamics that accelerated this inevitable conclusion into existence."
    rothbauer @ say "Humanity would struggle to hold absolute power as their numbers dwindled following the failure to contain the disease that..."
    
    n "Mr. Rothbauer seems to suddenly realize he's lecturing someone who has personally been affected by the mass extinction event he's describing."
    
    rothbauer @ say "Ahem well, at any rate, coming off the heels of the industrial revolution, you could say this was the beginning of the modern era!"
    rothbauer @ say "Anyway, that's all I have for you today."
    rothbauer @ say "Oh wait, there's still one more thing!"
    rothbauer @ say "There will be a parade in town to celebrate the holiday. I'll add 2 percent to your final grade if you show up and prove you were there by taking a selfie haha!"
    rothbauer @ say "You kids all love taking those funny little self portraits, don't you? Well this will be a good opportunity for you take another one while going out gaining an appreciation for historical events!"
    rothbauer @ say "Why, back in my day when I was the director of Harmonia's Anthromorphs Liberation Day committee I..."

    n "As he goes on with his rant, students start leaving. It's 5 minutes past the end of class after all. You decide to join them."
    
    stop music fadeout 1.0

    scene bg lecturehall with fade
    
    play music "audio/music/mere - schooldaze faster.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    show herschel at center with dissolve:
        ypos y_herschel
        
    herschel @ say "...alright, I think that's enough for today's lesson but we still have a bit of time leftover!"
    
    pause .1
    
    show herschel with move:
        xoffset 300
    
    show gunner neutral at center with dissolve:
        xoffset -550
        ypos y_gunner
        xzoom -1
    
    gunner @ say "Does that mean we can go home early?"
    
    show gunner annoyed
    
    herschel @ say "Of course not! Instead what I have in mind is an extra credit opportunity, something you of all students should be particularly interested in."
    
    n "Gunner mutters something under his breath."
    
    gunner @ say "This fucking bitch..."
    
    hide gunner with dissolve
    
    n "Lucky for him, Mrs. Herschel doesn't seem to have heard his remark."
    
    herschel @ say "I have something of a math riddle for you to solve!"
    herschel @ say "Say you have three doors to choose from and behind one of them lies a prize."
    herschel @ say "After making your selection, someone comes along and opens one of the doors that you did not choose and shows that it contains no prize."
    herschel @ say "You're given a choice to change your selection to the remaining door. Should you do it?"
    
    n "As usual the class is dead silent and Mrs. Herschel has infinite patience for someone to speak up."
    n "Gunner is engrossed in his notebook, drawing diagrams and writing out formulas in an attempt to find the solution."
    n "He's clearly failing to find one, meaning you're gonna have to take one for the team and come up with an answer."
    
    menu:
        n "{cps=0}He's clearly failing to find one, meaning you're gonna have to take one for the team and come up with an answer.{/cps=0}"
        "Keep your initial choice":
            n "You raise your hand and the pine marten calls on you."
            
            player "Um, I guess I'd keep my initial choice. At this point it's a 50/50 chance so either door is equally likely to be a winner, right?"
            
            herschel @ say "A 50/50 shot you say? Ah, that's where you're wrong."
            herschel @ say "Are the chances really as equal as they seem?"
            
            n "Gunner circles something and puts down his pencil."
            
            show gunner neutral at center with dissolve:
                xoffset -500
                ypos y_gunner
                xzoom -1
            
            gunner @ say "Wouldn't you be twice as likely to win if you choose the other door?"
            
            herschel @ say "Precisely! Very good Gunner! Tell us how you came to that conclusion, won't you?"
            
            gunner @ say "Well uh, I'm not really sure to be honest. But like in the beginning you have a 1 in 3 chance right?"
            gunner @ say "Then you get rid of one door but that can't possibly affect the chances of your decision in the past can it?"
            gunner @ say "So all that chance of winning from the two doors you didn't choose is set in stone. All the other guy did was get rid of a losing option."
            
            herschel @ say "Correct! Your initial choice has a 1/3 chance, so recall that what you don't choose is 1 minus your chance."
            herschel @ say "You wind up with the other two doors combined having a 2/3 chance of having a prize behind one of them."
            herschel @ say "It may help to think in terms of quantities rather than chance. Imagine you know your door has 1/3 of the prize, so then the doors you didn't choose have a combined 2/3 of the prize."
            herschel @ say "Then someone opens of of them and reveals nothing behind it, so they remaining door you didn't choose must contain the larger prize!"
            herschel @ say "Very good Gunner, I'll add a point to your final grade."
            
        "Change your selection":
            $ goodEnd =+ 1
            
            n "Before you can say anything, Gunner pipes up."
            
            show gunner neutral at center with dissolve:
                xoffset -550
                ypos y_gunner
                xzoom -1
            
            gunner @ say "What difference does it make? It's a 50/50 chance at that point... right?"
            
            herschel @ say "Is that your final choice? Perhaps someone else would choose otherwise..?"
            
            n "She's making it sound like Gunner is wrong. You should go for the opposite answer."
            
            player "I'd change my decision."
            
            herschel @ say "And you'd be right to do so! You'd enjoy a 2/3 chance of success if you switch to the other door."
            
            gunner @ say "How the hell...? That can't be right, how does a door suddenly gain a higher chance without doing anything?"
            
            herschel @ say "I told you it was a riddle, so the answer could never be obvious!"
            herschel @ say "The trick lies in eliminating a losing option after making your choice."
            herschel @ say "Your door has a 1/3 chance of winning, yes? So that means the other two doors have a combined 2/3 chance of winning, at least in the beginning."
            herschel @ say "When you remove one of those doors, where does that extra chance go? Nowhere! It stays right where it was!"
            herschel @ say "It's just that where it was is where you're not. Which is why you should change your choice."
            
            n "Gunner mutters something again."
            
            show gunner disgusted
            
            gunner @ say "What the fuck kind of reasoning is that..?"
            
            herschel @ say "Very good [name], I'll add one point to your final grade."
            
    stop music fadeout 1.0
    
    scene bg campus with fade
    
    play music "audio/music/vylet - Ordinarily.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Gunner walks with you after class and you once again find Rori on his laptop out on the field."
    
    show rori neutral at center:
        ypos y_rori
        xoffset 450
    show gunner neutral at center:
        ypos y_gunner
        xoffset -450
        xzoom -1
    with dissolve
    
    rori @ say "Sup. You all done for the day?"
    
    gunner @ say "Yeah. You out here doing your compsci homework again?"
    
    show rori sleepy
    
    rori @ say "Computer *engineering* not science. There's a difference."
    
    show gunner eyesclosed smile
    
    n "Gunner shrugs nonchalantly."
    
    gunner @ say "If you say so. Both look like coding to me."
    
    show gunner neutral
    show rori neutral
    
    n "Rori looks up from his screen and seems to just now notice you're there."
    
    show rori smirk
    
    rori @ say "Hey [name]! Glad you're out of the hospital!"
    
    player "I know right? About time. They kept me there like a prisoner all weekend."
    
    show gunner disgusted
    
    gunner @ say "Yeah man, what was with that?"
    
    show gunner frown1
    show rori neutral
    
    player "I dunno, just been feeling dizzy and stuff lately."
    player "But they gave me some pills and now I feel fine."
    
    show rori soyface
    
    rori @ say "Well I'm glad you're okay now. You looked dead when I found you!"
    
    show rori neutral
    show gunner determined
    
    gunner @ say "You still kinda look like it."
    
    player "Gee, thanks..."
    
    show gunner cutie
    
    gunner @ say "I'm just kiddin!'"
    gunner @ say "Hey, you guys wanna get into some shenanigans today?"
    
    n "Rori raises a brow but doesn't say anything."
    
    player "I dunno, I'm still trying to take it easy, at least for a few days."
    
    show gunner neutral
    
    gunner @ say "Ah alright then. Later this week maybe? We got a three day weekend coming up LET'S GOOOO!"
    
    player "Yeah maybe."
    
    rori @ say "You should get some rest, [name]. Better safe than sorry."
    
    player "Yeah that's what I was thinking. Just gonna chill at my dorm."
    
    gunner @ say "Cool. See you in stats later!"
    
    player "Later guys!"
    
    hide rori
    hide gunner
    with dissolve
    
    n "You return to your dorm and lazily flip through homework and internet pages until you feel like going to sleep."
    
    stop music fadeout 2.0
    
    scene bg black with fade
    
    show bg calendar
    show tmonday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

label ellen_feeding_ducks:
    scene bg campus with fade
    
    play music "audio/music/vylet - Tranquility and Happiness.ogg" 
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Amid the myriad of fuzzy animals passing by on their way to class, you spot a glum dog sitting on a bench overlooking a pond."
    n "Wild ducks and squirrels surround her, feeding on the bits of bread and seeds she scatters about."
    n "Is that Ms. Ellen?"
    n "Without thinking, you decide to sit next to her. All the animals scatter as you approach and the professor raises her head."
    
    show margaret sad at center with dissolve:
        ypos y_margaret
    
    margaret @ say "Hm? Oh it's you."
    
    player "Yup."
    
    n "An uncomfortable silence passes."
    
    menu:
        n "{cps=0}An uncomfortable silence passes.{/cps}"
        "What are you doing here?":
            player "What are you doing out here? Isn't class about to begin"
            
            margaret @ say "I don't live in the lecture hall you know."
            margaret @ say "And I've gotta do something to pass the time, don't I?"
            
            player "I just thought you'd be more into reading books or something."
            
            margaret @ say "I've read enough books for one lifetime, I think."
            margaret @ say "The animals around here don't seem to care about my interpretations of Virginia Wolf however."
            
            player "...Well what *are* your interpretations of Virginia Wolf?"
            
            margaret @ say "I'm not fond of her. Her streams of consciousness are a bore and her brand of feminism is too pompous for my tastes."
            margaret @ say "I won't blame you if you just read summaries online instead of reading her books when we go over her."
            
            menu:
                margaret "{cps=0}I won't blame you if you just read summaries online instead of reading her books when we go over her.{/cps}"
                "You're pretty chill, huh?":
                    player "Wow, you're actually really lax on the whole teaching thing, aren't you?"
                    
                    margaret @ say "I wasn't always like this. I used to care a lot more."
                    margaret @ say "But times change, as they always do."
                    
                    player "I dunno, you seem to have strong opinions on literature."
                    
                    margaret @ say "Literature's all I know."
                    margaret @ say "I suppose I put on a front to appear like I still care about teaching, but I really don't anymore."
                    
                    player "Did something happen?"
                    
                    margaret @ say "No. At least not just one thing. My dissatisfaction has been accumulating for a while."
                    margaret @ say "I like to think I make my own paths in life, for better or worse."
                    margaret @ say "Though I can't help but feel I've been on a streak of bad decisions for quite a long time."
                
                    player "Same, but... I think I'm making the most of it?"
                    player "I always felt like I'm mindlessly drifting through life like uhh..."
                    
                    n "You try coming up with some literary metaphor. Or is it a simile?"
                    
                    player "Like a jellyfish being pulled by currents. Not really going anywhere, just letting myself exist."
                    
                    show margaret sad shocked
                    
                    margaret @ say "And where has that taken you?"
                    
                    player "It brought me to this fancy pants university."
                    
                    show margaret melancholy -shocked
                    
                    margaret @ say "Then perhaps you're doing quite well as a jellyfish~"
                    margaret @ say "I suppose I'm more like a wolf. Always chasing after things, relentlessly, until I left my pack behind."
                    
                    player "Why not start a new pack? I was sort of a lone wolf too until I got here and started making friends."
                    
                    show margaret sad -melancholy
                    
                    margaret @ say "Oh it's far too late for me to start over."
                    margaret @ say "You ought to cherish the time you have with your friends while you're young."
                    
                    player "You make it sound like it's game over once you reach a certain age."
                    
                    margaret @ say "Well, it sort of is if you don't have your life together by a certain time."
                    
                    player "You can't be at that point already. There's still plenty of time."
                    
                    show margaret shocked leaningback
                    
                    margaret @ say "Oh?"
            
                "Isn't that academic dishonesty?":
                    player "Wow, a professor openly telling me to be academically dishonest?"
                    
                    show margaret happy
                    
                    margaret @ say "It's more likely than you think."
                    
                    show margaret melancholy
                    
                    margaret @ say "I've long since lost the passion for teaching, if it ever existed in the first place. My knowledge of literature has never gotten anyone anywhere."
                    
                    show margaret sad 
                    
                    margaret @ say "Every English major I taught ended up killing themselves or wanting to."
                    
                    player "That's not really your fault."
                    
                    margaret @ say "I know. I still consider my job to be rather worthless though."
                    
                    player "Why not quit?"
                    
                    margaret @ say "And do what? I'm too old to find a new career I enjoy, and the pay is good here."
                    
                    player "Is money everything? I've never had much so I dunno if it's worth working for. And you're not that old."
                    
                    margaret @ say "You get used to a certain amount and then it becomes difficult to go back."
                    
                    show margaret neutral
                
        "Everything okay?":
            player "Is everything okay? You look kinda sad."
            
            margaret @ say "Can't a lady feed the local wildlife without being judged?"
            
            n "The pond animals have started to make their way back and Ms. Ellen tosses them some bread crusts."
            
            margaret @ say "Honestly, I don't know why I even bother. What have ducks ever done for me?"
            
            menu:
                ellen "{cps=0}Honestly, I don't know why I even bother. What have ducks ever done for me?{/cps}"
                "They're a part of nature.":
                    player "They don't have to do anything, they're ducks."
                    player "They're a part of nature, so perhaps they're inherently, I don't know, beautiful or something?"
                    player "And we're technically a part of that nature so they're like our siblings. Little duck siblings."
                    
                    show margaret neutral
                    
                    n "You catch Ms. Ellen smirking."
                    
                    show margaret happy
                    
                    margaret @ say "Do yourself a favor and drop philosophy class."
                    
                    player "I'm not even taking philosophy!"
                    
                    show margaret neutral
                    
                    margaret @ say "In that case, consider trying it out next semester~"
                    margaret @ say "You might learn a thing or two hehehe."
                    
                    player "Maybe I'll major in it out of spite."
                    
                    margaret @ say "And end up being a teacher like me."
                    
                    player "That doesn't sound too bad."
                    
                    margaret @ say "Trust me, it is."
                    margaret @ say "Maybe some people are content to waste their lives away but it eats at me knowing I could have done something else."
                    
                    player "What else would you have done?"
                    
                    show margaret melancholy
                    
                    margaret @ say "Honestly, any other path would have been better for me."
                    
                    show margaret sad
                    
                    margaret @ say "But now I'm old and stuck on this path."
                    
                    player "You're not that old."
                    
                    margaret @ say "Oh?"
                
                "Then don't bother?":
                    player "Then don't bother? I mean, you're the one who made the conscious decision to come sit out here with a bag of bread instead of playing on your phone like everyone else does."
                    
                    margaret @ say "I suppose it's out of habit."
                    margaret @ say "It's just something my hus-- ex husband and I used to do."
                    
                    player "Oh."
                    player "..."
                    
                    show margaret neutral
                    
                    margaret @ say "You wanna try?"
                    
                    n "She nudges the bread bag closer to you."
                    n "You grab a few slices and start tearing off pieces."
                    
                    player "Oh gross, there's mold on it."
                    
                    margaret @ say "Why do you think I've been giving it away for free?"
                    
                    player "Won't they get sick?"
                    
                    margaret @ say "They've never complained before."
                    
                    n "You toss a few pieces and the ducks come running with their wings outstretched."
                    n "One gives you an appreciative quack."
                    n "Another one agressively rips a whole slice of bread from your hand."
                    
                    player "Ow! That one bit me!"
                    
                    margaret @ say "Him? He's always been that way. Ever since he was a baby, he's been biting me every time I come to feed them."
                    
                    player "You've been doing this for a while, huh?"
                    
                    margaret @ say "Yup."
                    margaret @ say "This was the first date I went on with my ex, ages ago."
                    
                    show margaret melancholy
                    
                    margaret @ say "Now I'm just an old lady feeding the birds on my own."
                    
                    n "She looks over to you, then back at the ducks."
                    
                    #margaret @ say "Sometimes with a curious student, but not often."
                    
                    player "Come on, you're not that old."
                    
                    margaret @ say "Oh?"
    
    show margaret neutral
                    
    margaret @ say "And just how old do you think I am, young man?"
    
    menu:
        ellen "{cps=0}And just how old do you think I am, young man?{/cps}"
        "20s":
            $ ellenPoints += 1
            
            #later student ellen comments "you said so yourself, I could pass for being in my 20s!"
            player "I dunno, late 20s?"
            
            n "Miss Ellen snickers."
            n "You can hear her tail brushing against the back of the bench as it wags happily."
            
            show margaret happy
            
            margaret @ say "Either you're flattering me or you don't know what a woman in her late 20s looks like."
            
            player "Hey, I'm pretty sure I've seen students who look older than you!"
            
            show margaret neutral
            
            margaret @ say "I'll take that as a compliment~"
            margaret @ say "Some students just have a late start but I've had a few who inexplicably show up once then retake the class years later."
            
            player "Heh, wouldn't you be happy to see me in your class again in a few years?"
            
            show margaret happy
            
            margaret @ say "I'd rather see you in my graduate course~"
            margaret @ say "What about you? Would you want to see me again?"
            
            player "Only if you're still as beautiful."
            
            show margaret intrigued
            
            margaret @ say "..."
            
            show margaret happy 
            
            margaret @ say "Oh you! Hehehehe you're really quite the jester, aren't you?"
            margaret @ say "Smart move. Only the fool can be spared the queen's wrath after all~"
            
            player "Hahaha really though, I think it would be cool to see you again after this semester. Maybe we could get coffee or something?"
            
            show margaret neutral
            
            margaret @ say "Careful [name], it almost sounds like you're flirting with your professor!~"
            
            player "I swear I'm not, I don't even know how to flirt."
            
            margaret @ say "So this is just you being your sweet normal self, huh?"
            
            player "I guess?"
            
            margaret @ say "Well it is pretty cute. Just don't expect me to boost your grade for it.... at least not by much!"
            margaret @ say "And yes, coffee together sounds fantastic~"
        "30s":
            player "Early 30s I guess?"
            
            show margaret melancholy
            
            margaret @ say "Try 37, dear."
            margaret @ say "Today is this old dog's 37th birthday."

            player "Hey that's still prime."
            
            show margaret shocked leaningback
            
            margaret @ say "Excuse me???"
            
            player "Mathematically speaking."
            
            show margaret neutral
            
            margaret @ say "Hm. I suppose it is."
            
            player "Happy birthday by the way."
            
            show margaret sad
            
            margaret @ say "Thanks but there's nothing happy about it."
            margaret @ say "Getting old sucks. I miss when I was a cute 20-something like you."
            
            player "You think I'm cute?"
            
            show margaret sad
            
            margaret @ say "Woops, did that really slip out of my mouth? I meant cute like uhh..."
            
            show margaret melancholy
            
            margaret @ say "Like one of these baby ducks!"
            
            player "Thanks? I think?"
            
            show margaret neutral
            
            margaret @ say "Don't think too much about it."
        "40s":
            player "You're not old until you're like, grandma age."
            
            show margaret sad
            
            n "Miss Ellen sighs."
            
            margaret @ say "I suppose I could be a grandmother at my age. If I had any children of my own, that is."
            
            show margaret at shudder
            
            margaret @ say "Sorry, I didn't mean to make things awkward."
            
            player "It's fine. I mean, isn't it awkward of me to walk up to my literature professor and while she's feeding ducks?"
            
            show margaret neutral
            
            margaret @ say "Not really! This is how people made friends before we had technology to enslave our minds after all."
            
            player "Hahaha do you think you and I could be friends if you weren't my professor?"
            
            margaret @ say "Of course!"
            margaret @ say "I think we could be friends even with you as my student. People forget that such things used to be common. It still happens in a lot of other countries!"
            margaret @ say "A relationship can be formed by anyone who enjoys each other's company, regardless of status."
            
            show margaret melancholy
            
            margaret @ say "You're quite a good listener and I enjoy your unique perspective and funny comments. That's really all I need."
            
            player "That's pretty sweet of you to say! I guess you kinda are like a kind old grandma hahah!"
            
            show margaret flattered
            
            margaret @ say "Well, let's not say that..."
            
            show margaret neutral
            
            margaret @ say "But don't be afraid to say hi whenever you see me~"
            
            player "Same goes for you! I'd love to sit and chat with you over a coffee sometime."
            
            margaret @ say "I'm sure that can be arranged~"
            #and if it's your treat, I'll be sure to give you a treat in return~
            
    n "You sit with Ellen for a few more minutes, making idle chatter and feeding ducks until you run out of bread."
    n "After a while, Miss Ellen stands up."
    
    margaret @ say "I wish we could talk longer but it's almost time for class."
    
    player "Yeah. I'll see you there in a few minutes."
    
    margaret @ say "Thanks for talking with me."
    
    player "Anytime."
    
    hide margaret with dissolve
    
    stop music fadeout 2.0
            
#make this part of ellen's cafe scene
#    n "Ms. Ellen reclines against the bench and sighs."
#
#    show margaret melancholy
#
#    margaret @ say "It's nice to get to talk to one of my students like this."
#    margaret @ say "Most are either intimidated by me or just see me as an obstacle to their degree."
#
#    player "Yeah I'm not really too into the whole college thing."
#    player "I just come to class out of habit and sometimes I learn interesting things."
#    player "I like hearing your rants about authors' beliefs."
#
#    show margaret flattered
#
#    margaret @ say "Is that so? I always feel so embarrassed after those little tirades! I suppose I just can't help myself."
#
#    player "I guess literature would lend itself most to expression. Not much room for interpretation in statistics or French."
#
#    show margaret neutral
#
#    margaret @ say "Au contraire, le langage limite nos pensées."
#
#    player "What??"
#
#    margaret @ say "There's certain things you can't express in one language alone."
#    margaret @ say "Even if you mastered English, which very few people have done mind you, other languages open your mind up to new thoughts."
#    #margaret @ say "That's what Celestine taught me. You know her, right?"
#    margaret @ say "That's what Sera taught me. You might know her as Mrs. Celestine."
#
#    player "Yeah, she's my French teacher."
#
#    margaret @ say "I thought so. She's nice. And wise. You should listen to her."
#    margaret @ say "She's told me about you."
#
#    player "Wait, you know Mrs. celestine??"
#
#
#
#
#    #reserved for part 2
#
#                    margaret @ say "I didn't used to be. I used to try really hard."
#                    margaret @ say "But after teaching here... I've seen so many cheaters graduate. So many people dumber than a rock coast through their degree with their parents' money and end up in important jobs."
#                    margaret @ say "That's just the path in life they've had given to them."
#                    margaret @ say "The administration pressures us to just shut up and take the bribes. Not little things like cinnamon rolls, I'm talking cars and vacation homes."
#                    
#                    player "How many vacation homes does a professor need??"
#                    
#                    margaret @ say "I wish I had one. They only offer those to smooth things over when senator So-and-So's dipshit son gets in trouble with the law for assaulting some poor sorority girl."
#                    margaret @ say "The most I've ever got was a strange case where I think the student enjoyed giving me money?"
#                    margaret @ say "I suckered him out of nearly twenty grand over a couple semesters."
#                    
#                    player "You lucky dog."
#                    
#                    show margaret happy
#                    
#                    margaret @ say "Hehehehe~"
#                    
#                    show margaret neutral
#                    
#                    margaret @ say "You won't have to do that much to pass my class though. Just listening to me rant is enough for me. It's a lot cheaper than therapy, that's for sure."
#                    
#                    n "Ms. Ellen sighs."
#                    
#                    show margaret sad
#
#
#
#^split this scene into 2 parts because it drags on for too long. Split at the "just how old do you think I am" part? have a flashback to it later when you sit on the bench alone? Or make this part part of the ellen cafe scene later
#    show margaret melancholy
#            
#    margaret @ say "Thanks for sitting and talking with me. It really made my day worthwhile."
#    margaret @ say "There's more to you that makes you special than just being the last human."        
#
#    player "I don't know about that. I'm just like anyone else. Just doing whatever society expects me to do. Go to school. Pay taxes. That sort of thing."
#    
#    margaret @ say "You're very kind and have your own unique perspective. You can uplift people without realizing it."
#    
#    player "I'm glad you think so. I try. Well no, I don't really try. I just want to live a comfortable life and be happy with others."
#
#    show margaret neutral
#    
#    margaret @ say "Perhaps that's all you need to do."

    scene bg lecturehall with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0
        
    n "Once again, Miss Ellen goes on with class as if nothing even happened."
    n "She seemed pretty down earlier but she's her usual self while teaching."
    
    show margaret neutral at center with dissolve:
        ypos y_margaret
        
    margaret @ say "That's all for today. Class dismissed!"
    
    hide margaret with dissolve
    
    n "She gathers her papers and disappears through the lecture hall's back door before you can say anything to her."
    n "Oh well, off to French class you go."
    
    scene bg classroom with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    show celestine neutral at center with dissolve:
        ypos y_celestine
    
    celestine @ say "...et voila! I hope that helps you understand some of the differences in phrasing between English and French."
    celestine @ say "Au revoir, class!"
    
    hide celestine with dissolve
    
    stop music fadeout 2.0
    
    scene bg campus with fade
    
    play music "audio/music/vylet - Catching On.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    show claire sweater happy at center:
        ypos y_claire
        xoffset -500
        xzoom -1
    show ava typical happy at center:
        ypos y_ava
        xoffset 500
    with dissolve
    
    ava @ say "Glad you're back among the living [name]! We were starting to get seriously worried about you."
    
    player "Glad to be back. Still annoyed I missed that party though. Sounded like you two had a lot of fun."
    
    show claire pose suggestive
    
    claire @ say "We sure did~"
    claire @ say "It was Ava's first time drinking!"
    
    show ava unamused
    
    ava @ say "Ugh, don't remind me."
    
    show claire derp
    
    claire @ say "I had to drink like an entire keg of beer to even feel anything!"
    
    show ava unimpressed
    
    ava @ say "I don't know how you can stomach it."
    
    show claire sweater leaning suggestive -
    
    claire @ say "I guess I'm just built different!"
    
    n "Ava looks up and down Claire."
    
    ava @ say "Uh huh."
    
    menu:
        claire "{cps=0}I guess I'm just built different!{/cps}"
        "Must be her genes":
            player "Must be your genes."
            
            show claire happy
            
            claire @ say "I know right??"
            
            ava @ say "You're too big for your genes."
            
            show claire suggestive earsup
            
            claire @ say "Too big for my bras too."
            
            show ava shocked
            
            ava @ say "W-where did that come from?!"
            
        "She's FAT!":
            $ calledClaireFat =+ 1
            
            player "It's because you're fat."
            
            show claire surprised earsup
            
            claire @ say "Oh?"
            
            show claire leaning suggestive
            
            claire @ say "And is that a bad thing?"
            
            show ava unamused
            
            ava @ say "Please respond wisely."
            
            menu:
                "{cps=0}Is that a bad thing?{/cps}"
                "Hell no!":
                    $ clairePoints =+ 1
                    $ avaPoints =- 1
                    
                    player "Hell no! I like chunky bunnies. Thick rabbits are the best."
                    
                    show claire surprised earsup
                    
                    claire @ say "!"
                    
                    show claire sweater suggestive -
                    
                    claire @ say "Oh you~"
                    
                    if calledClaireFat1 == True:
                        claire @ say "I knew you were just playing hard to get when you said you weren't into fat girls before~"
                    
                    show ava shocked
                    
                    player "You could even stand to put on a few more pounds haha"
                    
                    show claire sweater flustered
                    
                    claire @ say "You think so??"
                    
                    show ava typical annoyed
                    
                    ava @ say "Okay enough with the thinly veiled weight gain fetish talk."
                "Kinda":
                    $ clairePoints =- 1
                    
                    player "N-not at all. You're perfectly friend shaped."
                    
                    show claire sad
                    
                    claire @ say "Just \"friend\" shaped?"
                    
                    show ava reaching concerned
                    
                    ava @ say "Oof."
                "Yes":
                    $ claireBias =+ 1
                    $ calledClaireFat =+ 1
                    
                    player "I'm just saying your should eat a salad every so often."
                    
                    show claire happy
                    
                    claire @ say "I do!"
                    
                    player "Maybe a smaller one then."
                    
                    show claire sad
                    show ava reaching concerned
                    
                    claire @ say "Hmph!"
                    claire @ say "I'm not *that* fat, I'm mostly fluff and muscle!"
                    
                    player "Keep telling yourself that."
                    
                    n "Claire pouts and makes a whining sound."
                    
                    ava @ say "Hey, be nice to her."
                    
                    claire @ say "Let's just... talk about something else."
            
        "She's *ahem* high in mass":
            player "More body mass means you need more alcohol to get fucked up."
            
            show claire happy
            
            claire @ say "Well duh!"
            claire @ say "But I ran the numbers for how much a bunny of my size should have to drink and it wasn't even close!"
            
            player "Huh. Maybe you really are built different."
            
            show ava smug
            
            ava @ say "Built like a tank."
            
            show claire suggestive
            
            claire @ say "Optimized."
            
    show claire sweater happy -
    show ava typical happy -
    
    n "You chat for a bit longer then remember it's a short week."
    
    player "You guys are alright, don't come to school on Friday."

    show claire at hop

    claire @ say "Oh yeah! What are y'all's plans for the three way-"
    
    show claire giggle
    
    claire @ say "I mean three day weekend?"
    
    show claire happy
    
    player "I got nothin' so far."
    
    show ava whimsical
    
    ava @ say "I was thinking of taking some shots on film at this spooky abandoned hospital nearby."
    
    show ava smug
    
    ava @ say "I could use a partner to make sure I don't get shanked by a crazed hobo if either of you wanna come."
    
    claire @ say "Sorry, I'm gonna be busy with some sorority stuff. Top secret sorority stuff."

    ava @ say "Mysterious~ How about you, [name]?"
    
    if mishkaMallSpecialPlayed == True:
        player "Sorry, I already have plans to meet with Mishka on Saturday and I can't risk getting stuck in the hospital again."
        
        ava @ say "Aww..."
        ava @ say "Guess I'll go on my own then."
    else:
        menu:
            ava "{cps=0}How about you, [name]?{/cps}"
            "That sounds fun!":
                $ avaPoints += 1
                $ avaUrbex = True
                
                show claire sweater happy
                
                player "That sounds fun! I'd love to go with you!"
                
                show ava overjoyed

                ava @ say "Sweet! You don't mind if it's haunted, do you? Cause it's probably haunted."
                
                show ava happy

                player "No, haunted is fine."
                
                show claire suggestive

                claire @ say "Ksksksks you two are so cute!"

                show ava profile angry

                ava @ say "We are not!"
                
                show claire sweater derp
                
                claire @ say "Girl chill! I'm just joking!"
                
            "I'll pass.":
                show claire sweater happy
                
                player "Sounds cool but I'll pass. I'm supposed to go to the parade in town to get extra credit in history."
                
                show ava typical unamused

                ava @ say "Aww..."
                ava @ say "Guess I'll go on my own then."
                
    show ava typical happy
    show claire happy
            
    n "You stand around chatting some more until Ava and Claire have to run to class, then you return to your dorm for the day."
            
    hide ava
    hide claire
    with dissolve
    
    #n "Now you can do something with your free time."
    
    
    
    #call afterClassOptions from _call_afterClassOptions_1

    hide box
    
    stop music fadeout 2.0

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
    
    scene bg lecturehall with fade

    play music "audio/music/mere - schooldaze faster.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0
        
    show herschel at center with dissolve:
        ypos y_herschel
        
    herschel @ say "Very good class! Remember to study hard over the weekend!"
    herschel @ say "Class dismissed!"
    
    hide herschel with dissolve
    
    stop music fadeout 2.0
    
    scene bg campus with fade
    
    play music "audio/music/vylet - Destiny Station.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    show gunner neutral at center with dissolve:
        ypos y_gunner
        xoffset 500
    
    gunner @ say "LMAO are you gonna \'study hard\' this weekend, [name]?"
    
    menu:
        gunner "{cps=0}LMAO are you gonna \'study hard\' this weekend, [name]?{/cps}"
        "Nope":
            player "Nope. Cool people don't study."
            
            gunner @ say "Right on, brother!"
            
            n "Gunner's fist demands a bump and you do not disappoint."
            
            show gunner motivated
            
            gunner @ say "So what you got planned?"
            
            if avaUrbex == True:
                player "I'm going urban exploring with some chick."
                
                gunner @ say "Oh so like a date?"
                
                player "Not really."
                
                show gunner mischief
                
                gunner @ say "You're at least gonna fuck her, right?"
                
                player "I wasn't planning on it."
            else:
                player "Nothing at all."
                
                show gunner displeased
                
                gunner @ say "Bruh."
        "I might":
            player "I dunno, I might if I get bored of fucking your mom."
            
            n "You just blurted out the first thing that came to mind. It seems that Gunner's rhetoric has rubbed off on you."
            
            gunner @ say "Hah! You couldn't handle my mom even if she gave you a chance."
            gunner @ say "She scratched out my dad's only good eye because he insulted her cooking."
            
            player "Joke's on you, I'm into that!"
            
            gunner @ say "Funny, he said the same thing."
            gunner @ say "Then she cut off his balls and threw them into a soup the next day."
            
            player "Dude what the fuck."
            
            show gunner eyesclosed smile
            
            gunner @ say "If you can't handle her at her best, you don't deserve her at her worst."
            
            show gunner wink catface
            
            gunner @ say "I'm just messin' with ya."
            
            show gunner neutral
            
            gunner @ say "My mom's a sweet lady, she's only tried to have my dad assassinated three or four times."
        "Actually yeah":
            player "Yeah actually, I'm really behind on everything."
            
            show gunner uncomfy
            
            gunner @ say "That's gay."
            
            player "Maybe so but I still need to pass my classes."
            
    show gunner optimistic
            
    n "Rori sees you two approaching and closes his laptop"
    
    show rori neutral at center with dissolve:
        ypos y_rori
        xzoom -1
        xoffset -500
        
    rori @ say "Sup guys."
    
    player "Heya."
    
    gunner @ say "Rori please tell me you've got something good planned for the weekend."
    
    show rori cheery
    
    rori @ say "Hmm... Nope, not really."
    
    show rori smirk
    
    rori @ say "Was just gonna work on my projects and maybe torrent a new anime."
    
    show gunner pissed
    
    gunner @ say "Ugh, don't you guys even celebrate Anthromorph's Liberation Day?"
    
    show rori sleepy
    
    rori @ say "Does anyone? It's just a day off from work or school."
    
    player "I'm not even an anthromorph, so no."
    
    show gunner motivated
    
    gunner @ say "Oh right, you guys are freshmen so you wouldn't be in the *know.*"
    
    show rori neutral
    
    rori @ say "The *know?*"
    
    gunner @ say "Here at Harmonia, we have traditions. Sacred traditions."
    
    n "Gunner gestures for you both to come closer so he can whisper something."
    
    gunner @ say "Every year on Liberation Day, the fraternities conduct..."
    gunner @ say "A panty raid!"
    
    show rori surprised
    
    rori @ say "A... panty raid? What is that? Is that a dungeon in Boarcraft?"
    
    show gunner determined
    
    gunner @ say "It's where you sneak into a girl's room and steal her panties."
    
    show rori sleepy
    
    rori @ say "That's it? Sounds kinda lame."
    
    show gunner itsover
    
    gunner @ say "Oh my God Rori you cannot be this homosexual."
    
    player "Panty raids aren't real. It's just some dumb thing Hollywoo came up with for college propaganda movies to trick people into taking out loans to get a worthless degree."
    
    show gunner motivated -
    
    gunner @ say "Where do you think they got the idea from?"
    
    show gunner optimistic
    
    gunner @ say "Me and the boys did it last year. Are you two down to join me this year?"
    
    rori @ say "This sounds like the worst risk versus reward ratio of all time."
    
    gunner @ say "Nah bro, it's like unofficially sanctioned by the university. It's a loooooong time tradition."
    gunner @ say "Our dean did it, Albert Einstein did it, George Washington did it, Plato did it..."
    gunner @ say "I'm pretty sure cavemen did it too."
    gunner @ say "Nobody's ever gotten in serious trouble for it."
    
    show rori concerned
    
    rori @ say "Can't you do it on your own? Why do you want us to come along?"
    
    gunner @ say "'Cause you still need someone to watch your back!"
    gunner @ say "It may be technically *allowed* but they still have to put up the illusion that it's not. It's part of the game."
    gunner @ say "Come on, it'll be fun I promise!"
    
    show rori sleepy
    
    n "Rori lets out a frustrated huff."
    
    rori @ say "Fine, I'll tag along."
    rori @ say "But only to make sure you don't do anything *too* stupid."
    
    show gunner mischief
    
    gunner @ say "Yes!!!"
    
    show gunner determined
    
    n "Gunner looks at you expectantly."
    
    gunner @ say "And what about you?"
    
    if mishkaMallSpecialPlayed == True:
        player "Sorry, I already have plans to go to the mall with Mishka and I can't afford to get arrested and miss it."  
      
        gunner @ say "Fine, do what you want. Just don't expect me and Rori to share the spoils from our treasure hunt!"
                
        player "You two have fun with that. I gotta run for now."
    
    elif avaUrbex == True:
        player "I already make plans to do some urbex stuff with someone this weekend. Sorry."
        
        gunner @ say "No sweat. Just be sure your schedule's free next year!"
        
        rori @ say "And save me from having to go."
        
        show gunner cutie
        
        gunner @ say "Do it for Rori."
        
        show gunner neutral
        show rori neutral
        
        player "Haha sure."
        player "You two have fun with the panty raid. I gotta run for now."
    else:
        menu:
            gunner "{cps=0}And what about you?{/cps}"
            "Let's do it":
                $ gunnerRaid = True
                
                player "Count me in."
                
                n "Gunner pumps his fist in the air."
                
                gunner @ say "Sickkk!"
                gunner @ say "We'll meet up on Friday to do some scouting, then conduct the raid on Saturday night when everyone's out."
                
                rori @ say "Sounds like a plan."
                rori @ say "Not a very good one, but it's better than nothing."
                
                player "Cool, I'll see you guys then. I gotta run for now though."
            "Count me out":
                player "Nah bro, the vibes are off on this one."
                
                gunner @ say "Dude what."
                gunner @ say "Are you gay or something?"
                gunner @ say "You can ogle Rori's ass while we sneak around if that's the case."
                
                show rori anxious
                
                rori @ say "H-hey!"
                
                player "I just have better things to do."
                
                show rori neutral
                
                n "Gunner shrugs, pretending like he doesn't care."
                
                gunner @ say "Fine, do what you want. Just don't expect me and Rori to share the spoils from our treasure hunt!"
                
                player "You two have fun with that. I gotta run for now."
                
    gunner @ say "Laters."
    
    rori @ say "Laters."
    
    hide gunner
    hide rori
    with dissolve
    
    if mishkaMallSpecialActive == True:
        $ badEnd =+ 1
    
    #set to false because you're missing mishka's mall scene if you go with gunner or ava
    $ mishkaMallSpecialActive = False
    
    
    n "What should you do with your free time?"
    
    call afterClassOptions from _call_afterClassOptions_2
                
    stop music fadeout 2.0            
    
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
    
label liberation_eve:

    scene bg lecturehall with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    show margaret neutral at center with dissolve:
        ypos y_margaret

    margaret @ say "Good morning class!"
    
    show margaret happy
    
    margaret @ say "I'm sure you're all as excited about the long weekend as I am so how does a short day sound?"
    
    show margaret melancholy

    n "The class erupts into a half-hearted cheer followed by a dull murmur that takes a while for Ms. Ellen to calm down."

    margaret @ say "Alright alright, the sooner you all shut up the sooner you can go home."

    n "She rubs her temples like she has a migraine until the class quiets down."

    show margaret sad

    margaret @ say "Ugh..."
    margaret @ say "Let's get this over with..."

    n "Ms. Ellen sluggishly gives her lesson but cuts it off after only half an hour."
    
    show margaret neutral

    margaret @ say "You know what? I think that's enough for today. Enjoy your weekend, everybody!"

    hide margaret with dissolve

    n "She hastily gathers her papers and hurries out of the room."
    n "You've got some time before French. Maybe you should try and talk to her?"
    
    menu:
        n "{cps=0}You've got some time before French. Maybe you should try and talk to her?{/cps}"
        "Follow her":
            $ frenchSkill =- 1
            
            n "Ms. Ellen seemed kinda out of it today. Perhaps it'd cheer her up if one of her students checked to see if she's alright."
            n "You manage to spot her among the crowd and follow her into the stairwell. The clacking of her heels against the concrete stairs echoes as she approaches the rooftop access door."
            
            stop music fadeout 2.0
            
            scene bg roof with fade
            
            play music "audio/music/Vylet Pony -  Colourless.ogg" fadein .4
            
            show box with Dissolve(.2):
                ypos 0
            
            n "By the time you reached the doorway, Miss Ellen had already lit a cigarette."
            
            show margaret smoking sad shocked at center with dissolve:
                ypos y_margaret
                
            margaret @ say "Following me up here again?"
            
            show margaret smoking neutral
            
            margaret @ say "I must be your favorite professor, huh?"
            
            player "Something like that."
            player "Couldn't wait to go on break, could you?"
            
            show margaret melancholy
            
            margaret @ say "I just needed some fresh air."
            
            n "You point to the cigarette."
            
            player "You call that fresh air?"
            
            show margaret happy
            
            margaret @ say "My, we have a detective on the scene!"
            
            show margaret smoking intrigued
            
            n "Miss Ellen takes a drag of her cigarette and winces."
            
            show margaret smoking sad shocked
            
            margaret @ say "Ugh, this damn hangover..."
            
            player "Aha, I knew you were acting strange in class!"
            
            show margaret smoking intrigued -
            
            margaret @ say "Was it that obvious?"
            
            hide margaret
            show margaret smoking intrigued at center:
                ypos y_margaret
            
            player "Yeah but I don't think anyone minded."
            player "Why are you hungover? It's the middle of the week."
            
            show margaret smoking melancholy
            
            margaret @ say "Because I was drinking last night. Heavily."
            
            player "Yeah I got that part. But why? Is everything alright?"
            
            n "She looks at you. You can see it in her eyes, she's tired of it all."
            
            menu:
                n "{cps=0}She looks at you. You can see it in her eyes, she's tired of it all.{/cps}"
                "She feels trapped":
                    n "She feels trapped in this neverending nightmare of mediocrity."
                    n "The spark of optimism is gone, replaced with reality's dull edge cutting into her."
                "She's unhappy":
                    n "She's unhappy and she's finally come to terms with that."
                    n "No more denying it, her life officially sucks."
                "She's hit rock bottom":
                    n "She's hit rock bottom. Classic mid life crisis."
                    n "She's having the worst time of her life and wondering how it all happened and why she didn't prevent it."
            
            margaret @ say "I'm just tired."
            
            n "She's silent for a while, letting her cigarette burn out."
            
            show margaret smoking melancholy shocked
            
            margaret @ say "You don't look so good yourself."
            
            show margaret smoking intrigued -shocked
            
            player "Oh right. That."

            menu:
                player "{cps=0}Oh right. That.{/cps=0}"
                "I think I'm dying":
                    $ ellenPoints =+ 1

                    player "I think I'm dying."

                    margaret @ say "..."

                    n "Miss Ellen's expression doesn't change."

                    margaret @ say "What, for real?"

                    player "Yeah. I probably have that disease that only kills humans."
                    
                    show margaret smoking melancholy shocked
                    
                    margaret @ say "What a shame."

                    player "I mean, the doctor said I probably *don't* have it but I dunno whether to believe that."
                    
                    show margaret smoking melancholy -shocked
                    
                    margaret @ say "I hope you don't have it."
                    margaret @ say "Growing old sucks but it's better than the alternative I guess."
                    
                    player "I try not to think about it. No point in worrying, ya know?"
                    
                    margaret @ say "Mmh."
                    
                    n "You and Miss Ellen stand in the breeze, watching over the university from your vantage point. Neither of you are quite sure of what to say."
                    n "After a while, Miss Ellen lets her cigarette fall to the ground and steps on it."

                    show margaret smoking neutral

                    margaret @ say "If you wanna talk more, my number's on the syllabus. I'll listen to whatever you have to say."
                "Don't wanna talk about it.":
                    player "Umm, I dunno if I'm ready to talk about that with anyone yet."
                    
                    show margaret smoking melancholy

                    margaret @ say "Fair enough."

                    n "You and Miss Ellen stand in the breeze, watching over the university from your vantage point. Neither of you are quite sure of what to say."
                    n "After a while, Miss Ellen lets her cigarette fall to the ground and steps on it."
                    
                    show margaret smoking neutral

                    margaret @ say "I can tell something's seriously bothering you though. My number's on the syllabus if you ever wanna talk."
                    
            margaret @ say "For now, I'm gonna return to my office and pass out."    
            
            hide margaret    
                    
            n "You swear you can just barely hear her giggle as she walks past you, brushing her fluffy tail against your arm."
            n "You stand on the roof for a while longer until you realize you're late for your next class."
            n "Better hurry along now!"

        "Don't follow her":
            n "It's kinda creepy to stalk your professor like that. You should just chill for the next half hour you have before your next class."
            n "You loiter around the campus until a couple of familiar faces approach you, one with a friendly smile and the other looking like she wants to kill you."
            
            show nicodemus
            show rose
            
            nicodemus @ say "Good day, [name]! Enjoying the fair weather?"
            
            rose @ say "There, we said hi. Can we go now?"
            
            nicodemus @ say "What's the rush, lass? Can't a dean have a pleasant chat with his future alumni?"
            
            player "Nice to see you again, Mr. Kazcynski. What do I owe the pleasure?"
            
            #nicodemus @ say "There's hardly an occasion, I just happened to see you there while I was out walking with my... granddaughter here."
            nicodemus @ say "There's hardly an occasion, I just happened to see you there while I was out walking with my granddaughter here."
            
            n "Rose looks away, clearly uninterested in the conversation."
            
            nicodemus @ say "I hear the two of you have a history course together! My little Rose just adores history! It was her favorite subject in high scool!"
            nicodemus @ say "It may seem like the past is this finite thing that's gone and left us, but there are more stories than can be told in a lifetime, showing what civilization is truly capable of!"
            nicodemus @ say "I think it was my war stories that got Rose interested in the first place bahaha!"
            
            rose @ say "Grandpa... shut up already, you said we'd get coffee before my next class."
            
            n "The dean checks his wristwatch and smiles."
            
            nicodemus @ say "We've still got plenty of time! Humor me!"
            
            n "Rose huffs and crosses her arms."
            
            player "Well I got out of literature early so I'm just waiting for French to start."
            
            nicodemus @ say "French huh! The only French I know are the battle cries of my comrades as we pushed to liberate Paris!"
            nicodemus @ say "\"Avec moi!\" \"Au feu! Au feu!\" \"En avant!\""
            nicodemus @ say "And let me tell you, those Parisian women sure were grateful for la résistance and their allies!"
            
            n "As annoyed as Rose wants to be, she can't help but smirk at her grandfather's gusto."
            
            #rose @ say "We get it, you were a solder who saw some action."
            
            nicodemus @ say "But that's all in the past now, today I'm just a humble university dean."
            nicodemus @ say "Which means I'm curious as to how your experience here at Harmonia is going, [name]. I trust your grades are satisfactory."
            nicodemus @ say "More importantly, have you made any significant bonds?"
            
            menu:
                "I think so":
                    $ avaPoints += 1
                    $ clairePoints += 1
                    $ roriPoints += 1
                
                    player "I think so. I have a group I hang out with pretty regularly."
                    
                    nicodemus @ say "Good!"
                    nicodemus @ say "I'd hate for you to have your nose in the books all day and miss out on making friends."
                    nicodemus @ say "And what about a girlfriend? Have you found one yet?"
                    
                    player "Err, no."
                    
                    nicodemus @ say "You hear that, Rose? This could be your chance."
                    
                    rose @ say "Pass."
                    
                    nicodemus @ say "Whaaat? Why not? [name] is a perfectly suitable young lad!"
                    
                    rose @ say "He's not my type."
                    
                    nicodemus @ say "Fine, have it your way."
                    nicodemus @ say "Sorry [name], my granddaughter has a tough exterior but I promise she's a real sweetheart once you get to know her!"
                    
                    rose @ say "Hmph!"
                    
                    nicodemus @ say "Well we better be off to get that coffee I promised. It was good seeing you again!"
                    
                    player "It was nice talking with you again, sir."
                    
                    nicodemus @ say "I'd like to sit down and have coffee with you as well sometime when we're not all in a hurry."
                    nicodemus @ say "Then you can go into depth about all the hijinx you and your friends have been up to! Bahaha!"
                    
                    player "Of course!"
                    
                    rose @ say "We really have to be on our way now."
                    
                    nicodemus @ say "Right, sorry to cut into our weekly coffee time Rose."
                    nicodemus @ say "Have a nice holiday, [name]!"
                    
                "I'm not sure":
                    $ rosePoints =+ 1
                    $ ellenPoints =+ 1
                    
                    player "I'm not really sure. I talk to a few people but I dunno if we're still gonna be talking in a few years."
                    
                    nicodemus @ say "I see."
                    nicodemus @ say "Perhaps it will take some more time for you to establish a strong relationship. But keep at it!"
                    nicodemus @ say "Rose also has trouble making friends. Maybe you two could-"
                    
                    rose @ say "No thanks."
                    
                    nicodemus @ say "Come now Rose, how long do you plan to be a loner?"
                    
                    rose @ say "With any luck, the rest of my life."
            
                    nicodemus @ say "Hah! Such dry humor, I love it!"
                    nicodemus @ say "Don't worry, you'll find your match some day."
                    nicodemus @ say "Both of you will, I'm sure of it."
                    
                    rose @ say "Whatever."
                    rose @ say "Can we go now?"
                    
                    nicodemus @ say "Someone's eager for some caffeine, isn't she! Bahaha you always were crabby without it!"
                    nicodemus @ say "You know she started drinking coffee when she was 12 years old! Always black, she's never even tried it with creamer!"
                    
                    rose @ say "I like it as it is, no need to ruin the flavor with extra junk."
                    
                    nicodemus @ say "Well I suppose we better be off now. It was good chatting with you again [name]!"
                    
                    n "You mostly just sat and listened but it was still a pleasant interaction."
                    
                    player "Always a pleasure to have a casual chat with the dean."
                    
                    nicodemus @ say "I do hope we can get together for coffee sometime and have a nice sit-down conversation. Get to know how your studies and experience are going in more detail."
                    
                    player "Yeah, maybe next time. I gotta run to French now."
                    
                    nicodemus @ say "Au revoir! Bahaha!"
                    nicodemus @ say "And have a nice holiday!"
                    
            player "Thanks, you too!"
                    
            n "The raccoons head off in the direction of the cafe. Rose is probably complaining she had to endure a few minutes talking with you, but she seems to admire her grandfather."
            n "Likewise, he seems to care deeply for her. It almost seemed like he was the one who raised her."
            n "There's still some time before class begins so you enjoy a stroll at a leisurely pace, basking in the crisp autumn air while being warmed by the sun's light."
    
    $ cafeEvents.append("nicodemusCafe")
    
    scene bg classroom with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    show celestine excited at center with dissolve:
        ypos y_celestine

    celestine @ say "Bonjour class! Happy Anthromorphs's Liberation Day Eve!!"
    
    show celestine neutral
    
    celestine @ say "Obviously this is an American holiday but I wanted to go over related holidays other countries celebrate!"
    celestine @ say "France is actually credited with kickstarting the push for us animal folk to have equal rights in this era!"
    celestine @ say "It sure sends a message when the human elites get brutally murdered and eaten by commoners, huh?"
    celestine @ say "Sometimes that's what it takes to change the world!"
    celestine @ say "I highly recommend visiting France during the week long celebration they have! It's like Mardis Gras on crack! Heehee~"
    celestine @ say "Though France didn't see a long-standing animal leader for a while, Britain had one the next decade! To this day, Queen Mary is celebrated by having her portrait on their currency!"
    
    hide celestine with dissolve

    n "Mrs. Celestine rambles on about other countries and their various transitions from human dominated society to rule of animal people."
    n "Maybe one day you'll get your face on the dollar bill as a memory of the last human."
    n "Either that or they'll talk shit about you in textbooks for being an evil human who oppressed every other species for millennia."
    n "For all her love of this holiday, she doesn't cut you a break and let the class leave early."
    n "If someone hadn't interrupted her, she probably would have ranted well into the evening."
    
    show celestine excited at center with dissolve:
        ypos y_celestine

    celestine @ say "Oop! Seems I got a bit too excited! Class is dismissed! Enjoy your weekend!"

    hide celestine with dissolve
    
    show claire sweater happy earsup at center with dissolve:
        ypos y_claire
        xoffset 550

    claire @ say "Whew! The long weekend has officially begun! Wanna stop by the coffee shop, [name]?"
    
    show claire -earsup
    
    player "Why not? I am getting kinda hungry."
    
    claire @ say "I'll text Ava to meet us there!"
    
    stop music fadeout 2.0
    
    scene bg cafe with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    play music "audio/music/mere - coffeeLove.exe.ogg" fadein .4
    
    show claire sweater happy at center:
        ypos y_claire
        xoffset 550
    with moveinright
    
    n "Claire holds the door open for you and lets you go inside first."
    n "Ava is already here waiting for you."
    
    show ava typical whimsical at center with dissolve:
        ypos y_ava
        xoffset -500
        xzoom -1
    
    ava @ say "*Chirp~*"
    
    show ava happy
    
    ava @ say "Hey guys!"
    
    show ava typical happy
    
    claire @ say "Heyyy~"
    
    show claire suggestive
    
    claire @ say "OMG is that who I think it is?"
    
    n "Claire points to a pair of cat ears sticking up over a booth. He's facing away. but, Ava has to flutter up to even see him."
    n "Sitting across from him is Rori, flipping through pages in a textbook."
    
    show ava at flipleft
    
    pause .5
    
    show ava at flipright
    
    pause .3
    
    ava @ say "What? Who?!"
    
    claire @ say "That catboy you have a crush on!"
    
    show ava pose angry
    
    ava @ say "Shshshshush or he'll hear you!"
    
    n "Gunner's ear flicks and he turns around to see what the commotion is all about."
    
    show claire happy with move:
        xoffset 700
    hide ava with dissolve
    show ava typical happy at center with dissolve:
        ypos y_ava
        xoffset 450

    show rori neutral at center:
        xoffset -340
        ypos y_rori
        xzoom -1
    show gunner optimistic at center:
        xzoom -1
        ypos y_gunner
        xoffset -750
    with dissolve

    gunner @ say "Hello there ladies~"
    
    show gunner neutral
    
    gunner @ say "And [name]."
    
    n "Rori throws down his pencil."
    
    show rori sleepy
    
    rori @ say "I don't know how you expect me to tutor you if you turn around to greet every girl who walks in."

    player "Hey guys. You helping Gunner learn basic math? How's that going?"
    
    show rori concerned

    rori @ say "It's... not."
    
    show gunner annoyed

    gunner @ say "Hey, chi-squared tests are not basic math! Seriously, does anybody ever use this stuff?"
    
    show claire giggle
    
    claire @ say "I use it all the time! It's a useful statistical analysis to determine the validity of quantitative experiments compared against a null hypothesis."
    
    show ava whimsical
    show gunner optimistic
    
    ava @ say "Sorry to interrupt your study session!"
    
    gunner @ say "It's alright, we could use a break anyway."
    
    show ava happy
    
    n "Claire turns to Rori with a friendly grin."
    
    show claire sweater suggestive earsup
    
    claire @ say "Hiya! I don't think we've met! I'm Claire and this is Ava!"
    
    show rori anxious
    show claire sweater happy -earsup

    n "Rori looks kinda nervous. You're not sure if it's just because he's shy or if it's Claire intimidating him."
    
    rori @ say "N-nice to meet you. My name's Rori."
    
    show claire sweater suggestive

    claire @ say "I like your horns~"
    
    show rori worried

    rori @ say "I- my... horns? Thanks? I don't really do anything too fancy with 'em."

    show ava annoyed

    ava @ say "Claire can you please stop flirting with every boy you meet?"
    
    show claire giggle

    claire @ say "Hey I hit on girls too."
    
    show ava typical neutral

    ava @ say "This is why I'm embarrassed to go out in public with you."
    
    show claire derp

    claire @ say "Ksksksks love you too Ava <3"
    
    show claire happy
    show ava profile whimsical

    ava @ say "We'll just be moving along now. Don't mind us!"

    gunner @ say "Hey it's no problem, awkward flirting is infinitely more fun than doing math problems."

    ava @ say "See you around, guys!"
    
    show claire sweater suggestive

    claire @ say "À un de ces quatre! Ksksksksk!"

    player "Later guys. And good luck with the homework."

    hide gunner
    hide rori
    hide ava
    hide claire
    with dissolve

    n "You walk up to the counter with Ava and Claire at your side."
    n "As usual, Mishka is there to greet you with a smile... or half of one. Maybe a third."
    
    show mishka neutral at center:
        ypos y_mishka
        xzoom -1
        xoffset -550
    show claire sweater happy at center:
        ypos y_claire
        xoffset 620
    show ava typical happy at center:
        ypos y_ava
        xoffset 330
    with dissolve
    
    if mishkaMall == True and mishkaMallSpecialPlayed == False:
        n "It dawns on you that you haven't seen her since you made plans to go to the mall together."
        n "Which you failed to do."
        
        player "Hey Mishka. Sorry about the mall thing. I was stuck in the hospital all weekend."
        
        mishka @ say "Oh no, are you alright??"
        
        player "Yeah, I just fell down and stuff."
        
        mishka @ say "Well, if you are able... maybe we could still go somewhere this weekend?"
        
        if gunnerRaid == True or avaUrbex == True:
            player "I'd love to but... I kinda already made plans for the weekend."
            
            mishka @ say "Oh..."
            
            player "I'm sorry. I'll make it up to you, I promise."
            
            mishka @ say "Don't worry about it. The mall wasn't that fun anyway."
            
        else:
            player "Yeah!! I won't miss it this time even if it kills me!"
            
            mishka @ say "Hehe I don't think that is necessary! Let's just meet at the mall this Saturday, okay?"
            
            player "Sounds great!"
            
            claire @ say "Ooh, is that a date?"
            
            mishka @ say "No, just a friendly thing. You can come too if you want!"
            
            show claire flustered
            
            claire @ say "Aaaaaa I would if I didn't already have plans!"
            
            show claire happy
    
            mishka @ say "Another time then."
            
    mishka @ say "Can I get you something to drink?"

    player "The usual please."

    n "You scan your card and step off to the side."

    mishka @ say "And for you two?"

    claire @ say "Can I get a large chai tea latte, hot, with almond milk and extra honey and salt aaaaaand five chocolate chip cookies?"
    
    #player "You don't have to get me anything lol"
    player "Oh nice you're getting a cookie for everyone?"
    
    show claire sweater surprised earsup
    
    claire @ say "Huh? Um, no?"
    
    #show claire sweater happy -earsup
    show ava agitated
    
    ava @ say "They're all for you, aren't they?"
    
    show claire sweater flustered -earsup
    
    claire @ say "I gotta maintain my figure somehow!"
    
    show ava typical happy
    
    ava @ say "I'll just have a mocha please!"
    
    show claire sweater happy
    show mishka happy
    
    mishka @ say "Konyechnya! I'll have that ready for you all shortly!"

    hide mishka with dissolve

    n "While Mishka starts work on your orders, you hang off to the side with Ava and Claire."

    claire @ say "So, got any plans for the rest of today, [name]?"

    player "Hmm... Not really. Pretty lazy day honestly."
    player "The real fun starts tomorrow."

    ava @ say "A lazy day every now and then is nice."
    
    show claire sweater laughing

    claire @ say "I looooove staying in bed all day, wrapped up in a nice warm blanket and watching movies."
    
    show claire sweater giggle
    
    claire @ say "*Gasp*"
    
    show claire sweater overjoyed
    
    claire @ say "We should have a movie night!"
    
    show ava overjoyed

    ava @ say "Ooh, that sounds fun~"
    
    player "I dunno, my dorm is kind of a wreck and I don't have anything to watch and"
    
    show claire sweater happy
    show ava typical happy

    claire @ say "Come on, you promised!"

    player "I did? I don't remember that..."
    
    show ava smug
    
    ava @ say "Yeah, I'm pretty sure we talked about this before."
    
    player "Am I being gaslit right now?"
    
    #show ava annoyed
    show ava typical happy
    
    ava @ say "No, you definitely promised us a movie night at some point."

    claire @ say "Perfect! We'll meet at your dorm at 7 then!"
    claire @ say "You better pick out some good movies~"

    n "In that case you'll have to dust off your old pirate hat and update your torrent client when you get back to your dorm."
    #n "What kind of movies do normies like again?"
    n "Maybe you should invite Mishka over as well. She's always had your back even though you've never even hung out with her."
    n "She walks over with your drinks right at the perfect time."

    show mishka neutral at center with dissolve:
        xzoom -1
        xoffset -550
        ypos y_mishka

    mishka @ say "Here's your drinks and snacks! Enjoy!"

    player "Thanks!"
    player "Hey uh Mishka, I was wondering if you'd wanna come hang out with us later today. We're gonna be watching some movies at my dorm."

    show mishka sad
    
    mishka @ say "Oh? I'd love to, but unfortunately I am having a busy today..."
    mishka @ say "Perhaps another day?"

    claire @ say "Aww... Don't worry Mishka, we'll find a day where we can all hang out together!"
    
    show mishka happy
    
    mishka @ say "Really..? I would enjoy that very much!"
    
    show mishka anxious neutral

    ava @ say "Yeah, you're really cool! You must be really busy though having to work here all the time on top of going to class."

    show mishka depressed

    mishka @ say "Heh, yeah... class and work all of the time..."
    
    show mishka despondent
    
    mishka @ say "Well uh, here your foods and drinks. Be careful, they are hot!"

    player "Thanks again Mishka! We'll see you later!"

    hide mishka with dissolve
    
    pause .1
    
    show ava:
        xoffset -250
    show claire:
        xoffset 320
    with move
    
    n "On your way out, Ava stops you."
    
    show ava excited

    ava @ say "Why don't we invite them to come along too? They seem pretty cool."
    
    show ava happy
    show claire sweater leaning suggestive

    claire @ say "Ah I see how it is. You wanna spend some time with that Gunner boy, donchya?~"
    
    show ava annoyed at flipright

    ava @ say "You're the one who was into that cute ram!"
    
    show ava angry 
    show claire sweater laughing

    claire @ say "Ksksksks so now you think Rori's cute too?"

    ava @ say "Claire I swear on my tyrannosaurus ancestors-"

    n "You let them continue bickering while you walk over Gunner and Rori."

    hide ava
    hide claire
    with dissolve

    show gunner neutral at center:
        xzoom -1
        xoffset -450
        ypos y_gunner
    show rori neutral at center:
        xoffset 450
        ypos y_rori
    with dissolve

    player "Hey guys. Apparently I'm hosting a movie night tonight. Wanna come with so I'm not stuck listening to these two bicker for hours all on my lonesome?"

    gunner @ say "Oh hell yes."

    rori @ say "Hmm, I guess I could skip tonight's raid and join you. What are you all watching?"

    player "To be honest I have no idea. I was just gonna download whatever comes up when I search 'guns cars explosions movie'"
    
    show rori laugh

    rori @ say "I've got a flash drive with a bunch of kinos we could watch!"

    player "Sweet, that works! See ya at my dorm at around 7!"
    
    show rori neutral

    gunner @ say "We'll be there!"

    n "You give a thumbs up then turn back to Ava and Claire."

    hide gunner
    hide rori
    with dissolve

    show ava typical happy at center:
        xoffset -350
        xzoom -1
        ypos y_ava
    show claire sweater happy at center:
        xoffset 450
        ypos y_claire
    with dissolve

    player "They're on board."
    
    show ava overjoyed

    ava @ say "Awesome! We'll see ya later tonight [name]!"
    
    show claire laughing

    claire @ say "Yeah, thanks for hosting! I can't wait~"
    
    hide claire
    hide ava
    with dissolve

    stop music fadeout 1.3

    scene bg codadorm with fade

    ##play sound "ambient/outdoors night crickets.ogg"

    show box with Dissolve(.2):
        ypos 0

    n "Later that evening..."
    
    play music "audio/ambient/outdoors night crickets.ogg" fadein .4

    player "Gosh darn dangit raptor jesus god gosh darn dammit goshhhh"
    player "Where the heck is Rori???"

    n "It's a bit past 7 o'clock and he's still not here and your backup movie you began torrenting stalled."
    n "You hear some noise outside your door followed by knocking."
    n "Please let that be Rori."

    show rori neutral at center with dissolve:
        ypos y_rori
    
    play music "audio/music/Vylet Pony - Cozy Pone.ogg" fadein .5
    #play music "audio/music/vylet - リラックス.ogg" fadein .5
    
    show rori soyface

    rori @ say "Hi! Sorry I'm late."
    
    show rori neutral

    player "It's fine. Did you bring the movies? And where's Gunner?"
    
    show rori supersmug
    
    rori @ say "He's had to do something but he'll be here soon. And yeah I got 'em right here."

    n "He whips out a flash drive."

    player "Cool, let's see what you got."
    
    hide rori with dissolve

    n "You plug the drive into your laptop and browse the files on it."
    n "Deer god..."
    n "Why are half of these file names in Japanese?"
    n "Rori, you didn't..."
    n "You open one and skip to the middle. You are greeted with a barrage of bright colors and a high pitched \"ONI-CHAAAAAAN!~\""
    n "You immediately slam the laptop lid shut."
    n "What the fuck Rori"
    
    show rori neutral at center with dissolve:
        ypos y_rori

    player "I thought you said you had some good movies..."
    
    show rori laugh

    rori @ say "These *are* good."
    
    show rori neutral

    player "How am I supposed to explain this weeb shit to a normie like Ava?"
    
    rori @ say "Idk just tell her it's a foreign film."
    rori @ say "She'll think you're cultured."
    
    hide rori with dissolve

    n "Before you can come up with a backup movie, you hear another knocking at your door."
    n "As you turn the knob, Claire's fat bunny ass bursts through the doorway, knocking you onto the ground, semi-conscious."

    show ava typical happy at center:
        xoffset -225
        ypos y_ava
        xzoom -1
    show claire sweater happy wave at center:
        xoffset -700
        ypos y_claire
        xzoom -1
    show gunner neutral at center:
        xoffset 760
        ypos y_gunner
    with dissolve

    claire @ say "Heyyyy~"
    
    show ava pose whimsical
    show claire sweater happy -wave

    ava @ say "I hope you didn't start without us!"
    
    show ava pose happy

    gunner @ say "Heya [name]. I see Rori made it here in one piece."

    n "Yeah not to mention he brought 12 gigabytes of One Peace."
    n "You pick yourself off the ground and welcome everyone in."
    
    player "Come on in guys, I'm glad you all could make it!"
    player "Help yourself to some snacks. I have some sodas in the mini fridge too if you want any."

    gunner @ say "Daaaamn, your dorm came with a mini fridge?"
    
    n "Gunner picks up the empty box of dino nuggies you left beside your microwave."
    
    gunner @ say "You even have a microwave! They don't allow us peasants to have these because someone managed to burn down a whole dorm building with one."
    
    player "I thought you were supposed to be loaded. Why aren't you living in this building or like some mansion?"
    
    show gunner determined
    
    gunner @ say "And miss out on the authentic college experience? Nah bro, couldn't be me."
    
    show gunner eyesclosed catface
    
    gunner @ say "I like having a roommate and slumming it up eating ramen noodles like I was raised on the street."
    
    show gunner optimistic
    
    hide ava
    hide claire
    with dissolve
    
    show rori sleepy at center with dissolve:
        ypos y_rori
        xoffset -400
        xzoom -1
    
    rori @ say "Dude you buy imported authentic ramen that costs like $40 per bowl."
    
    gunner @ say "I know right? Isn't poor people food just the best?"
    
    hide rori with dissolve
    
    show ava typical happy at center:
        xoffset -275
        ypos y_ava
        xzoom -1
    show claire sweater suggestive earsup at center:
        xoffset -750
        ypos y_claire
        xzoom -1
    with dissolve

    claire @ say "Pretty swanky place you got here~"
    
    show claire sweater happy -earsup

    player "Thanks. Go ahead and have a seat wherever and we'll start watching something."
    
    show ava overjoyed

    ava @ say "Hey Rori! Was that Boku no Doki Doki Phantasm Gx; R-EVerSe?"
    
    show ava typical happy
    show rori neutral at center with dissolve:
        ypos y_rori
        xoffset 250

    n "To your surprise, Ava is leaning over Rori, who is busy connecting the laptop to the television and has his anime folder open in clear view on the screen."

    rori @ say "Yeah! Have you been keeping up with season 15?"
    
    show ava motivated

    ava @ say "I have! It looks like they're hyping up Golden Stardust to go Requiem Mode: Super Blue Évolution for the fight against Diamond Moonlight!"
    
    show ava happy
    show claire sweater laughing

    claire @ say "I can't wait to see her final Perfect Vampire form!"
    
    show claire happy
    show gunner optimistic

    gunner @ say "I just hope they don't stray too far from the manga version."
    
    show ava angry

    ava @ say "Don't spoil it!"

    gunner @ say "I won't, I won't!"

    n "Apparently everyone here is a weeb."
    n "Maybe tonight won't be a disaster after all."

    hide ava
    hide claire
    hide rori
    hide gunner
    with dissolve

    n "Once everybody gets situated and Rori picks out a film, you're faced with a predicament."
    n "A life altering decision presents itself."
    n "Who do you sit next to?"
    n "This room wasn't meant to accomodate five people so there's not a lot of places to sit."
    n "Everyone but you and Gunner has snagged a seat. He's distracted by his insatiable urge to rub his face against the edge of every piece of furniture in the room."
    n "Now's your chance." 

    ###maybe extend the scene after the credits roll and you're alone with whoever you sat with after the others leave
    menu:
        n "{cps=0}Now's your chance.{/cps=0}"
        "Sit next to Claire":
            $ clairePoints =+ 1
            
            n "Surprisingly, Claire has not occupied your bed and has instead opted recline against it whilst sitting on the floor, her arm elbow deep in a bag of chips."
            n "You decide to join her down there and grab a handful of chips when she takes her paw out."

            show claire sweater happy at center with dissolve:
                ypos y_claire

            claire @ say "Sup."

            player "There's room on the bed you know."

            claire @ say "I didn't wanna get crumbs in your sheets."

            player "How thoughtful."

            hide claire with dissolve

            #n "Gunner looks up from his phone as Rori hits the play button."
            n "Rori hits the play button and the intro credits begin."

            show ava typical overjoyed at offscreenright:
                ypos y_ava
            show gunner neutral at center with dissolve:
                xoffset -600
                ypos y_gunner
                xzoom -1

            gunner @ say "Hmm, where to sit...?"
            
            pause .1

            show ava typical overjoyed at center with moveinright:
                xoffset 350
                ypos y_ava

            ava @ say "You can come sit next to me!"

            n "Ava pats the space beside her on the bed."
            n "Gunner climbs onto your bed, sitting next to Ava with their backs propped up against the wall."

            show gunner neutral with move:
                xoffset 660
                
            pause .15
            
            show gunner at flipleft
                
            pause .3

            hide gunner
            hide ava
            with dissolve

            show claire sweater happy earsup at center with dissolve:
                ypos y_claire

            claire @ say "...and I figured those two would wanna sit together~"

            show claire -earsup
            
            player "Aww."
            
            player "Well I don't mind sitting down here if it's next to you."
            player "Even if the hard bedframe is killing my back."
            
            show claire sweater suggestive earsup

            claire @ say "You can always lay on me you know~"

            player "...I wouldn't mind that either."
            
            show claire happy -earsup
            show ava typical annoyed at center with dissolve:
                xoffset 600
                ypos y_ava

            ava @ say "Shh! The movie's starting!"

            hide ava
            hide claire
            with dissolve

            n "Claire wraps an arm around you and pulls you in close as the movie begins to play."
            #n "Your conversation will have to continue later, since the opening credits have rolled and the movie starts to play."
            n "You have to admit, it's a pretty good movie. The voicework is good, the animation's fluid, and the plot is interesting enough even if it doesn't make any sense whatsoever."
            n "Claire's constant munching was kind of distracting but it was kinda cute how she looked over to you and smiled when both of you reached into the chip bag at the same time."
            #n "At some point the discomfort from the bed frame digging into your spine was too much to ignore so you took up the bun's offer and decided to use her gut as a backrest."
            n "She's so soft and warm... You almost want to fall asleep like this."
            n "Oh god she's even stroking your hair"
            n "You're in heaven right now."
            n "Unfortunately the movie must end sometime and when it does, everyone gets up to stretch and banter a bit before heading home for the night."
            n "Claire however stays behind a little while longer and gives you a hug before leaving."
            n "Overall, you had a pretty good time with everyone. 10/10 would do again."
            n "*Yaaawn*"
            n "You're getting pretty sleepy though so you hurry and get ready for bed."

        "Sit next to Ava":
            $ avaPoints =+ 1
            
            n "Ava had decided to occupy your bed, which is fine because it's the most comfortable spot and you wanted to sit next to her anyway."
            n "You plop down on it, bouncing her up into the air."
            n "She glides back down with her wings outstretched."
            
            show ava reaching concerned shirtopen:
                ypos -3000
                xpos 700

            show ava with move:
                ypos 1080
            
            pause .2
                
            show ava at center:
                ypos 2500
                
            pause .2
            
            show ava with move:
                ypos y_ava
            
            show ava at shudder

            ava @ say "Brreeee! Easy there, [name]!"
            
            
            #show ava typical neutral at center with move:
                #xzoom -1
            #show ava with move:
            #    ypos y_ava
                
            #pause .01
            
            #show ava with MoveTransition(delay=.05)
             
            player "Sorry, forgot birds have hollow bones."

            ava @ say "They're actually denser to account for that, so they're not any lighter than your mammal bones."
            ava @ say "I'm just small and dainty."
            ava @ say "A strong breeze is enough to knock me over haha."
            
            show claire sweater giggle at center with dissolve:
                xzoom -1
                ypos y_claire
                xoffset -600
                
            claire @ say "Ksksksksks"
            claire @ say "[name] knocked you up so hard your shirt started taking itself off!~"
            
            ava @ say "?"
            
            show ava profile embarrassed
            
            ava @ say "Wha-!"
            
            n "Ava quicky buttons up her shirt."
            
            show ava typical unimpressed -
            show claire happy
            
            ava @ say "Just pretend that didn't happen."
            
            n "Gunner looks up from his phone."
            
            show gunner neutral at center with dissolve:
                xoffset 550
                ypos y_gunner
            
            gunner @ say "Damn, what did I miss?"
                
            show ava embarrassed at flipright
            
            ava @ say "Nothing!"

            #player "I'll be more careful around you then lol"
            
            hide ava with dissolve

            gunner @ say "Hrm..."
            gunner @ say "[name], you got any more chairs around here?"

            show claire sweater suggestive

            claire @ say "Come sit next to me!"

            n "Claire pats the space beside her on the floor."
            
            show gunner uncomfy
            
            n "Gunner grimaces and looks around for any alternatives."

            #pause .1

            show gunner at flipright
                
            pause .5
            
            show gunner at flipleft
            
            pause .5
            
            show gunner at flipright
                
            pause .2
            
            show gunner at flipleft
            
            pause .3
            
            show gunner at flipright
                
            pause .2
            
            show gunner at flipleft
            
            pause .1

            show gunner at center with move:
                xoffset -200
                ypos y_gunner
                
            pause .01
            
            show gunner at flipright            
                
            n "Alas, with nowhere else to sit, he's forced to plop down next to her."
            
            show claire sweater suggestive earsup
            
            n "Claire wraps an arm around him and he disappears into her floof."
            
            show gunner at offscreenleft:
                ypos y_gunner
            show claire at offscreenleft:
                ypos y_claire
            with move
            
            n "RIP"
            
            show rori neutral at center with dissolve:
                ypos y_rori
                
            rori @ say "Shshshsh! The movie's starting!"

            hide gunner
            hide claire
            hide rori
            hide ava
            with dissolve

            n "As the opening credits play, Ava scoots closer to you, her feathers brushing up against your skin."
            n "The movie goes on and it's better than you thought it would be."
            n "Detailed art, fluid animation, and an interesting plot that doesn't make any sense but it's still fun to watch."
            n "Before you realize it, Ava is full-on clinging to you."
            n "Not that you mind. She's really soft. No wonder they used to make pillow stuffing out of feathers."
            n "You can't resist wrapping an arm around her which only entices her to snuggle you closer."
            n "When the movie ends, everyone gets up to stretch and banter a bit before heading home for the night."
            n "Ava even stays behind a little while longer and gives you a hug before leaving."
            n "Overall, you had a pretty good time with everyone. 10/10 would do again."
            n "*Yaaawn*"
            n "You're getting pretty sleepy so you hurry and get ready for bed."

        "Sit next to Rori":
            $ roriPoints =+ 1

            n "You approach Rori, who is sitting in your desk chair."

            show rori neutral at center with dissolve:
                ypos y_rori

            rori @ say "Oh, am I in your spot?"

            player "Yeah but it's no big deal."

            show rori anxious

            rori @ say "Wh-whoa what are you-"

            n "You simply lift Rori up and take your seat back before lowering him onto your lap."
            
            rori @ say "*Bleat!*"
            
            n "The others stare and laugh as Rori tries to cover his blushing face."
            
            show ava typical neutral at offscreenright:
                ypos y_ava

            show gunner neutral at center with dissolve:
                xoffset 650
                ypos y_gunner

            n "Gunner nods to you."

            gunner @ say "Establishing dominance in your home. A real alpha move, [name]."

            show claire sweater happy at center with dissolve:
                xzoom -1
                xoffset -650
                ypos y_claire

            show claire sweater derp
            
            claire @ say "Aww, I'm jealous you get to sit in [name]'s lap Rori!"

            rori @ say "Ohmygosh[name]whyareyoudoingthis\nthereareotherplacesyoucouldhavesat"

            player "Yeah but I wanted the best seat in the house~"
            
            show rori embarrassed

            n "That only makes him turn more red."

            rori @ say "Aaaaah why would you say it like that?!"

            player "What, isn't this just like one of your Japanese animes?"
            
            show gunner cutie
            show rori yawn blush

            n "The room erupts into laughter, including Rori."
            n "He decides to accept it and leans back into you while Gunner goes to hit play on the movie."

            hide claire
            hide rori
            with dissolve

            show gunner optimistic 
            
            gunner @ say "Alright, now where do I sit?"

            show ava typical excited at center with dissolve:
                xzoom -1
                xoffset -250
                ypos y_ava

            ava @ say "Over here Gunner, there's some room for ya over here!"

            gunner @ say "Don't mind if I do!"

            n "The bird pats the spot on your bed beside her and Gunner pounces on it quite elegantly."

            show gunner neutral at center with move:
                xoffset -470
                ypos y_gunner

            pause .1

            show gunner at flipright
            
            pause .1
            
            pause(.3)

            hide gunner
            hide rori
            hide ava
            with dissolve

            n "The movie starts and it's better than you thought it would be."
            n "Detailed art, fluid animation, and an interesting plot that doesn't make any sense but it's still fun to watch."
            n "Rori fidgets in your lap throughout the movie."
            n "Honestly you're kind of regretting this because he's cutting off blood flow to your legs but it's too late to back out now."
            n "At least he seems to be pretty comfortable."
            n "Whenever you would reach over to grab your drink on the table you would catch a glance of Ava leaning on Gunners shoulder."
            n "You have to admit, they do look pretty cute together."
            n "When the movie's over and everyone gets up to stretch, he's hesitant to leave your lap until you forcefully push him off."
            n "Your party sticks around to banter for a bit before going back home."
            n "Rori even stays behind a little while longer and gives you a hug before leaving."
            n "Overall, you had a pretty good time with everyone. 10/10 would do again."
            n "*Yaaawn*"
            n "You're getting pretty sleepy so you hurry and get ready for bed."
            
    scene bg black with fade
    
    stop music fadeout 2.0

    hide box

    show bg calendar
    show tfriday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7
    
    jump liberation_day