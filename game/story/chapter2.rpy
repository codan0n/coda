label chapter2start:

    ###CHAPTER 2
    ###weather is randomized (starting in week 3?) and affects what you can do after class
    ###once a week you can sleep in and get a chance at a unique night scene?
    ###can also do night scenes on weekends more freely?

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0
    
    play music "audio/ambient/morning birds.ogg" fadein 0.1
    
    n "Farewell sweet weekend, you must return to class for now. Don't worry, you'll be back soon."
    n "You stuff your things into your bag and head out to your first class of the day, History."
    
    scene bg classroom with fade

    play music "audio/music/mere - schooldaze.ogg" fadein 1.0

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
    
    show rose skirt handonhip shy pendant at left:
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
    
    scene bg campus with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Gunner ran off after class, saying something about fraternity obligations."
    n "That leaves you free for the rest of the day."
    
    call afterClassOptions
    
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
    margaret @ say "After Ivan falls and injures his side, he suffers from worsening pain that causes him to become irritable and further destabilize his relationship with his family."
    margaret @ say "His condition eventually leaves him bedridden and unable to work. Faced with both his mortality and the loss of his sense of purpose, he reflects on what it truly means to die."
    margaret @ say "He comes to realize that the perception of death revolves around the fulfillment of life one has made for themself."
    margaret @ say "He had once believed he led a fulfilling life by acquiring prestige and status, but as he lay dying, none of his achievements mattered so much as the sympathy he received from his servant."
    margaret @ say "Moved by its sheer authenticity, Ivan finally understood while on his deathbed that by pursuing his own interests, he had neglected to foster a caring family."
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
    
    show claire sweater happy:
        ypos y_claire
    
    n "Claire waves her paw in the air energetically."
    
    claire @ say "I did!! Lots of food and stuff at cafes and bakeries are French! There's umm cafe au lait which is coffee with milk..."
    claire @ say "And fondant and macrons and brioche and savarin..."
    
    celestine @ say "Oui! France is of course known for its culinary arts! It's only natural that many of their words for cuisine would end up in English."
    celestine @ say "And they sure do love their cafes and bistros! If you go to Paris, you will find one on every corner!"
    celestine @ say "That brings us to today's topic: basic conversation you might experience while out in town shopping."
    
    scene bg campus with fade
    
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
    
    mishka @ say "I could say the same thing about you!"
    
    n "You hadn't considered that before. To you she's the coffee rat but from her point of view, you're just the coffee human."
    
    player "I just got done with class. You going somewhere?"
    
    mishka @ say "Just doing a walk. I'm on my break."
    
    player "Cool, cool."
    
    $ mishkaMall = False
    
    menu:
        "Ask if she wants to hang out":
            $ mishkaMall = True
            
            n "You're not sure how else to ask, so you put it bluntly."
            
            player "You uh... wanna hang out?"
            
            mishka @ say "Hang...out?"
            
            n "She seems confused."
            
            player "Yeah, you know... go somewhere and do something together?"
            
            mishka @ say "Oh!"
            mishka @ say "I'd love to, but I have to get back to work in a minute."
            
            n "Damn, that's code for \'hell no,\' isn't it?"
            
            mishka @ say "But maybe this weekend will work for you?"
            
            n "Maybe it's not! You still have a chance!"
            n "Don't fuck this up."
            
            player "This weekend works! How about..."
            
            n "Your mind races to think of a cool place to take her but comes up blank."
            
            mishka @ say "There's the mall in town if you would like to go."
            mishka @ say "I've never been to it so I don't know what it's like..."
            
            player "Sounds perfect!"
            
            n "You pull out your phone, pretending to pull up your calendar to make sure it's free."
            
            player "Saturday works for me. You got a number so I can text you when I'm there?"
            
            mishka @ say "Hah... I don't actually."
            mishka @ say "Let's just meet there at 3 if that's a good time for you."
            
            player "Yup 3 works."
            
            mishka @ say "Great! See you there~"
            mishka @ say "I have to return to work now but I'm glad I ran into you!"
            
            player "Same! See you at the mall later!"
            
        "Stand around awkwardly":
            n "Nothing comes to mind. No conversation starters, no pickup lines, no funny hypothetical questions."
            n "So you just stand there, looking around aimlessly and giving polite smiles whenever your eyes meet."
            n "To your credit, Mishka also seems to be in the same akward state of not know what to do or say."
            
            mishka @ say "Well it was nice standing here with you."
            mishka @ say "I have to return to work now but maybe we can do this again sometime?"
            
            n "Her statement is totally sincere without a hint of sarcasm."
            
            player "Whenever you're free."
            
            mishka @ say "Hehe see you at the cafe later, [name]!"
            
    hide mishka with dissolve
            
    n "Mishka gives you a wave and heads in the direction of the cafe."
    n "You're feeling tired from classes so you retire to your dorm early."
    
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

    play music "audio/music/mere - schooldaze.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0
        
    show rothbauer at center with dissolve:
        ypos y_roth

    rothbauer @ say "Good morning class! I hope you're prepared for today's quiz!"

    player "Wha-? Quiz?"

    show rose skirt armscrossed shy pendant at center with dissolve:
        xoffset -450
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
            $ rosePoints = rosePoints - 1
            $ badEnd = badEnd + 1
            n "Any way to pass, right? It's not like history is that important anyway."
            n "You sneak a few glances at Rose's sheet until she seems to notice."

            if gaveUmbrella == True:
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

    play music "audio/music/mere - schooldaze faster.ogg" fadein 1.5

    show box with Dissolve(.2):
        ypos 0

    n "For some reason, you can barely concentrate in Statistics today."
    n "Your head is pounding and your vision blurry."
    n "You look down at your notebook and it's all just illegible scribbles and a few drool stains."

    show gunner neutral at center with dissolve:
        ypos y_gunner
    
    gunner @ say "Bro, you still alive? You don't look so good."
    
    player "Ugh, this headache is killing me. I feel like I'm about to throw up."
    
    gunner @ say "Hang in there dude, class'll be over in like five minutes."
    
    n "Somehow you manage to endure five agonizing minutes that seem to last hours."
    n "Once class is over, you try to stand up but it's like your legs are gelatin."
    n "Gunner notices you struggling and comes to help you up."
    
    gunner @ say "How wasted did you get last night to come to class this hungover?"
    
    player "I didn't drink anything last night! I dunno where this is all coming from."
    
    gunner @ say "Maybe you ate something bad? You should take it easy for the rest of the day my guy."
    gunner @ say "C'mon, I'll take you to your dorm."
    
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
    margaret @ say "This is the tale first told by Homer, \"The Odyssey!\""
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
        "Arcoonian book":
            $ rosePoints += 1
            
            n "You take a look at the book Mr. Rothbauer gave you, \"The Rise and Fall of the Arcoonians.\""
            n "Skimming through its pages, you glean some information about their culture and role in ancient North America."
            n "Their society followed the principles of scholarly warriors who loosely ruled the continent."
            n "Honor, self reliance, freedom, sustainability, and harmony with nature were some of their ideals."
            n "Suffering and rising above one's particular life challenges were glamorized as being noble."
            n "Arcoonians fostered a fiercly individualist mindset that idealized liberty and sovereign freedom."
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
    
    
    n "You're starting to feel exhausted, both physicall and mentally."
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

    ##play sound "audio/ambient/morning birds.ogg" fadein 1.0
    play music "audio/music/vylet - yeah i'm ok thanks for asking.ogg" fadein 1.0
    #play music "audio/exports/【Music】こんにちは! ♡ [lQQkCtUahHE].opus"
    
    show box with Dissolve(.2):
        ypos 0

    n "You wake up feeling more tired than when you fell asleep but the bright sunlight streaming through the window urges you to get up."
    n "You reach for your phone and check the time. It's already past noon."
    n "Stats class is ending right about now."
    n "No use going out today. Might as well stay in and recover from this mystery illness that's plaguing you."
    n "You actually don't feel terrible right now but who knows if it will flare up again later."
    
    call phone_start
    
    call message_start("Ava", "Hey [name]! Claire told me you were feeling under the weather", "avaavi.png") 
    call message("Ava", "but if you're feelin better this weekend wanna go somewhere with us?", "avaavi.png") 

    call reply_message("I don't feel so bad today") 
    call reply_message("I think I'll be fine tomorrow")
    call reply_message("Where you going?")
    
    call message("Ava", "I'm not sure!", "avaavi.png") 
    call message("Ava", "Claire says she picked out a spot", "avaavi.png") 
    call message("Ava", "'Somewhere special' she says", "avaavi.png") 
    call message("Ava", "Whatever that means", "avaavi.png") 
    
    call reply_message("Interesting...")
    call reply_message("sure, I'll go")
    
    call message("Ava", "Yay ^v^", "avaavi.png") 
    call message("Ava", "I'll let her know", "avaavi.png") 
    call message("Ava", "meet us tomorrow at around 9 where we usually meet after class", "avaavi.png") 
    
    call reply_message("k")
    
    call phone_end
    
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
    
    $ townEvents.append("avaGarden")
    
    $ avaClaireGarden = True
        
    n "Claire and Ava are already waiting for you at your usual hangout spot."
    
    show ava neutral:
        ypos y_ava
    show claire sweater happy:
        ypos y_claire
    
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

    #play music "audio/music/vylet pony - Reading at Night.ogg" fadein 1.0
    play music "audio/music/vylet - tenderness.ogg" fadein 1.0
    
    if gardenDiscovered == True:
        n "This is the same garden you've visited before, just at one of the other entrances. The area is quite expansive and you haven't been to this part before."

    show ava typical happy at center:
        #xzoom -1
        xoffset 400
        ypos y_ava
    show claire flannel happy at center:
        xzoom -1
        xoffset -400
        ypos y_claire
    with dissolve

    n "Claire hops around whimsically from one plant to another, sniffing the flowers and admiring the multitude of plants."

    claire @ say "It's such a lovely day to go for a walk in the gardens, isn't it?"

    player "Yeah, I guess it's better than being cooped up in my dorm all day."

    ava @ say "Sunlight is good for you. Not just for your skin but also your mental health."

    player "Huh. I didn't know that."

    #n "Maybe that's why you've always been depressed."

    claire @ say "Just be careful not to get a sunburn! And remember to stay hydrated UwU"

    player "What... was that sound you just made?"

    claire @ say "What? UwU?"

    player "Nevermind. Which way should we go? There's like a dozen branching paths."

    claire @ say "Hmm, let's gooooo... this way!"

    n "She seems to pick a direction at random and pulls you and Ava along with her, deep into the garden."
    n "Before long, you're surrounded by a variety of shrubs and flowers to the point where you can't even see any of the university buildings anymore."
    n "Ava managed to escape to take photos of plants, getting particularly excited when she catches a hummingbird or butterfly sipping from a flower, but Claire maintains her death grip on your hand."
    
    ava @ say "Ooh, I have these in my garden back home. It's called a cardinal flower. Can you guess why?"

    player "Cause it's red like cardinals?"
    
    claire @ say "Only the males~"

    ava @ say "Yup! Such a pretty red~"

    claire @ say "She's got a thing for cardinal boys~"

    show ava annoyed

    ava @ say "Shush up, I do not!"

    claire @ say "Ksksksks! Just teasin'!"
    
    show ava typical neutral

    n "Ava and Claire continue to bicker and share fun plant facts as you go along."
    n "After a while, you come to a bench with an arch over it with vines growing all over."

    ava @ say "Whew, it's gettin' kinda hot! Can we take a break?"

    claire @ say "Yeah, my legs are killing me!"

    player "Same."

    n "Claire and Ava sit under the arch and begin reviewing the photos they've taken so far."
    n "There's only room for two so you just lean against a nearby tree, taking sips of water from your bottle and watching the bees zoom around."

    claire @ say "Hey [name], you wanna get a shot of us under the arch?"

    ava @ say "I'll let you use my camera as long as you promise not to drop it. It costs more than a semester's worth of tuition!"

    player "Sure, but I don't really know how to use one of those fancy cameras."

    ava @ say "Don't worry, I'll preset the exposure settings. All you have to do is point and click the button."

    n "Ava flicks some switches and dials on the camera before handing it over to you."
    n "You take a few steps back, compose your shot and press the button with a satisfying shutter sound."
    
    claire @ say "How'd it turn out? Lemme see lemme see lemme see!!"
    
    n "You turn the camera around and show Claire."
    
    show claire flannel laughing
    
    claire @ say "Ohmygosh we look great! This is just the perfect day, isn't it!"

    n "Ava gets up and gestures to the bench."
    
    show claire flannel happy

    ava @ say "Ok now it's your turn, [name]!"

    menu:
        ava "{cps=0}Ok now it's your turn, [name]!{/cps}"
        "I don't like getting my picture taken.":
            player "Sorry, I don't like getting my picture taken."

            ava @ say "I understand. I'm kinda the same way haha! But I've been getting more comfortable with it."
            
            n "Claire lets out a disappointed sigh but doesn't say anything."
        "Okay!":
            $ clairePoints = clairePoints + 1
            
            player "Okay!"

            n "You sit down next to Claire and smile for the camera."
            n "Just before Ava takes the shot, Claire wraps her arm around you, pulling you in close."

            ava @ say "Aww, you two are so cute~"

            claire @ say "Show us the pic!"

            n "Ava comes around and shows you the picture. Your face has a look of surprise mixed with fear as Claire's sudden death grip took hold of you."

            player "Great..."
        "Alright but I'm getting my picture taken with you next.":
            $ clairePoints = clairePoints - 1
            $ avaPoints = avaPoints + 1
            
            player "Alright but I'm getting my picture taken with you next."

            show ava overjoyed

            ava @ say "Who, me??"

            n "She looks to Claire, as if seeking her approval."

            claire @ say "Sure, go for it!"
            
            show ava typical neutral

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
            
            show ava portrait neutral

            claire @ say "One... two... three!"

            n "You smile for the camera and Claire releases the shutter."
            
            claire @ say "Got it!"
            
            show ava typical neutral

            n "Ava excitedly flutters over to see how it turned out."

            ava @ say "Come here [name], check it out!"

            n "You think you both look a little bashful in the shot but you like it more than the other shot."

            player "Aww nice!"

            ava @ say "The sunlight coming from behind really worked in our favor."
            
            player "For sure. It makes your feathers glow so nicely!"
            
            ava @ say "You think so?"
            
            n "Ava shyly smiles, turning away from you."

    claire @ say "Right then, shall we continue our little adventure?"

    ava @ say "Sure! I think I'm all rested up and ready to go!"

    player "Sounds good to me!"

    n "The three of you spend the rest of the day getting lost in the gardens, laughing, and having an all around good time."
    n "Eventually you find your way back to the entrance where you bid adieu and return to your respective dorms for the day."

    hide box

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
            $ goodEnd = goodEnd + 1
            
            n "You might end up regretting this later but you feel bad for making Rose do all the work."
            n "You have to at least put in a minimal effort."
            
            player "You can have them only if you let me write a page of the project."
            
            show rose unimpressed

            rose @ say "Not gonna happen."

            player "I guess you'll never read these rare first hand accounts from..."

            n "You take a look at the pages, unfolding a crease that had formed on one."

            player "The Midwest Arcoonia tribe...?"
            
            show rose angry

            rose @ say "Get your filthy human hands off those!"

            n "She tries to take them but your superior opposable thumbs refuse to let go."

            player "Careful, you don't wanna rip them by accident."
            
            show rose armscrossed furious

            rose @ say "Ugh, fine! ONE page, that's it!"

            n "You let go of the papers with a smirk on your face."

            player "Deal!"
            
            n "Rose snatches the pages and turns away from you."
            
            rose @ say "What the hell is this?!"
            
            n "Rose throws the papers right back into your face."
            n "Crude doodles and barely legible class notes drift past your eyes on their way to the floor."
            
            player "Woops, I guess those weren't pages that fell out of the book after all! Just my history notes~"
            
            rose @ say "Ugh! Go to hell."

            show rose armscrossed neutral at flipleft
                
            pause .25
                
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
            
            show rose angry

            rose @ say "Get your filthy human hands off those!"

            n "She tries to take them but your superior opposable thumbs refuse to let go."

            player "Careful, you don't wanna rip them by accident."
            
            show rose unimpressed

            rose @ say "Ugh, unbelievable."
            rose @ say "..."
            rose @ say "*sigh*"
            
            show rose smug
            
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
            
            show rose unimpressed at center with dissolve:
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
                n "\"Look no further than the humansona workshop every 3th Tuesday after a full moon at 2:14AM where we engage in roleplay with our inner human personas!\""
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

    "The following day..."
    
    show gunner neutral at center with dissolve:
        ypos y_gunner
        xzoom -1
        xoffset -430
    
    gunner "Yeah so then I'm like \"fuck you\" and -- oh hi Rori!"
    
    n "Gunner started following you after class and telling you frat boy stories until you came across Rori sitting on the grass working on something on his laptop."
    
    show rori neutral at center with dissolve:
        ypos y_rori
        xoffset 430
    
    rori @ say "Aaah!"
    
    n "It seems you've startled him."
    
    rori @ say "Oh it's just you."
    rori @ say "I was just really deep into some spaghetti code and so focused on it I didn't see you there!"
    
    gunner @ say "Bruh you are *always* on your laptop fiddling with some command line shit."
    gunner @ say "Why don't you ever I dunno, live your life?"
    
    rori @ say "This *is* my life."
    
    gunner @ say "That is so sad."
    gunner @ say "[name] we gotta intervene. I can't stand to see my roommate like this."
    
    player "What do you propose we do?"
    
    gunner @ say "I dunno, how's that saying go? \"Be a faggot, break the law?\""

    show rori sleepy
    
    rori @ say "I think you mean \"Be gay, do crime.\""
    
    gunner @ say "Exactly! Let's commit a crime!"
    gunner @ say "No homo."
    
    show rori anxious
    
    rori @ say "W-why would I wanna do that?"
    
    gunner @ say "Cause it'll be fun? Back me up, [name]."
    
    menu:
        "Gunner's right, we should all be gay":
            player "Gunner's right, we should all be gay."
            
            gunner @ say "What?! That's not...!"
            
            n "Rori laughs at your response and Gunner's reaction."
            
            rori @ say "Alright I'm in. Can't be gay without a little crime, right?"
            
            player "Only in certain countries!"
            
        "Gunner's right, we should all commit a crime":
            player "Gunner's right, commiting crime is fun."
            
            gunner @ say "Exactly! What better way to bond with the bros than getting into some comic mischief?"
            
            rori @ say "Hm."
            rori @ say "As long as it's not anything extreme, I guess I'll join in."
            
            gunner @ say "Right, no breaking into the White House today."
        "\[Gay\] Maybe we shouldn't become criminals":
            player "Can't we just be gay and not do crime?"
            
            gunner @ say "Where's the fun in that?"
            gunner @ say "You guys are so boooooring!"
            
            rori @ say "H-hey, I'm sure we can find a fun crime to commit!"
            
        "\[Not Gay\] Maybe we shouldn't become criminals":
            player "Maybe we could just do something legal?"
            
            gunner @ say "Where's the fun in that?"
            gunner @ say "You guys are so boooooring!"
            
            rori @ say "H-hey, I'm sure we can find a fun crime to commit!"
            
    player "Hmm... What's a good crime?"
    
    rori @ say "It has to be victimless. Like piracy."
    
    gunner @ say "Bruh have you seen what Somali pirates do?"
    
    rori @ say "No I mean like downloading movies for free."
    
    player "Is there any other way to download them?"
    
    gunner @ say "Can we please not do some made up digital crime? The whole point of this is to get away from that nerdy stuff."
    
    rori @ say "Okay tough guy, what are your ideas?"
    
    gunner @ say "We could rob a bank!"
    gunner @ say "[name] can be our getaway driver!"
    
    player "I thought we *weren't* gonna be harming anyone."
    
    gunner @ say "Bank money is federally insured. Nobody loses a cent!"
    
    rori @ say "What about the taxpayers?"
    
    gunner @ say "The government just reprints what gets stolen. It's like it never even happened."
    
    rori @ say "Still sounds too risky."
    
    player "What if we were vigilantes?"
    
    rori @ say "Like Robinhood, stealing from the rich and giving to the poor?"
    
    gunner @ say "But [name], I am the rich."
    
    rori @ say "Okay then you can be like Catman."
    
    gunner @ say "A loaded superhero who fights crime with crime? You might be onto something."
    
    player "Maybe we should start with something small. Like if we see someone steal a lady's purse we can beat him up and take his wallet."
    
    gunner @ say "That's perfect! Now we just have to wait for some thug to commit a robbery in broad daylight on this wealthy college campus with cops who drive by every 5 minutes."
    
    rori @ say "Keep on the lookout boys, we've got crimes to... wait are we doing crime or stopping it?"
    
    player "Both I think?"
    
    gunner @ say "I say neither at this rate!"
    gunner @ say "Come on, crimes aren't just gonna come to us! We gotta go to the crimes!"
    
    n "Gunner picks a seemingly random direction and confidently marches off. You look to Rori and the two of you wordlessly agree to follow him."
    
    scene bg schoolhallways with fade
    
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
    
    rori @ say "Hmm. That definitely counts as a crime, right?"
    
    gunner @ say "I mean, we'd be liable for any damages to property or personel as a result of giving this bitch a shake, wouldn't we?"
    
    player "Sure sounds like criminal activity to me."
    
    gunner @ say "Gentlemen? Shall we?"
    
    n "With a collective nod, the three of you go on the offensive, kicking, shoving and jostling the machine. The pretzels hang tantalizingly but hold steady through your barrage."
    n "You're all left panting and exhausted, losing the will to continue this fight and slumping against the machine."
    
    gunner @ say "Gah! It's hopeless! It's stuck in there!"
    
    rori @ say "Hold on, I might have a few quarters. We can probably get two bags for the price of one."
    
    player "To hell with that! We didn't come this far just to be law abiding citizens did we?!"
    
    n "You bang your fist against the glass in frustration one last time and that seems to do the trick. Without any fanfare, the bag plops down into the receiving area."
    
    gunner @ say "WE DID IT BOYS!!!!"

    rori @ say "Huzzah!"
    
    n "You reach in and grab your prize."
    
    player "Let us enjoy the spoils of our hardships, lads!"
    
    n "You rip open the top and reach in to grab a salty treat to chomp down on."
    
    player "Aww what the fuck? They're stale."
    
    gunner @ say "No way. Lemme try!"
    gunner @ say "Ugh. Nope. Not worth it."
    
    n "Rori takes the bag and bites into a pretzel as well and gives an unsatisfactory grimace."
    
    rori @ say "Hmm. Just barely inedible."
    
    player "After all that work. Disappointing."
    
    rori @ say "Hey what's that?"
    
    n "You look to where Rori is pointing. In the shadows something skitters across the floor."
    
    gunner @ say "Is that a rat?"
    
    n "Gunner pounces at it but it runs under the vending machine."
    
    rori @ say "Dude cut it out! He's just a little guy."
    rori @ say "He's probably just out looking for food. Here you go, have some pretzels."
    
    n "Rori places the bag on the ground with the open end facing the machine. Lightning quick, the rat comes out and snatches it, dragging it back into its lair."
    n "You, Gunner and Rori crouch down and peek into the gap between the floor and vending machine."
    n "Rori flashes the light from his phone, revealing a ragged grey rat digging through the bag and nibbling on pretzels."
    n "It ravenously chews through them, ignoring your gaze."
    
    rori @ say "Aww. Cute lil' guy."
    
    gunner @ say "Yeesh, I didn't know Harmonia had a rat problem."
    
    rori @ say "He's just trying to survive."
    
    player "Let's leave him to enjoy his feast."
    
    rori @ say "Yeah, I think that's enough crime for one day."
    
    scene bg campus with dissolve
    
    show box with Dissolve(.2):
        ypos 0
        
    show gunner neutral at center with dissolve:
        ypos y_gunner
        xoffset -375
        xzoom -1
    show rori neutral at center with dissolve:
        ypos y_rori
        xoffset 375
    
    gunner @ say "Well this was a waste. I was looking forward to some quality law breaking time with my bros."
    
    player "Eh, I thought it was a fun little sidequest."
    
    rori @ say "Perhaps the real crimes were the friends we made along the way."
    
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
    #play music "audio/music/Evan Schaeffer - React.ogg" fadein 1.0

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
    
    n "Looks like you're early today. So early that the previous class is still in session."
    n "What else is there to do other than loiter around waiting for your class to begin?"
    n "You wander around the halls, reading bulletin boards and mindlessly scrolling back and forth on your phone's home screen."
    n "The vending machine on this floor is out of your preferred snack. Maybe the one on the floor below you has it in stock?"
    n "As you push past the stairwell doors, you catch sight of an orange tail turning the corner on the stairs above."
    n "That's odd, this is the top floor. All thats above here is the rooftop level."
    n "Perhaps the rooftop access is unlocked? This warrants an investigation."
    
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
    
    show margaret smoking laugh

    margaret @ say "Bah, ya got me. I promise not to rat you out if you don't say anything."

    player "Deal."
    
    show margaret smoking neutral

    n "You lean on the wall next to her."

    player "What are you doing up here anyway?"

    margaret @ say "What's it look like? I'm on break."

    player "Didn't think you were the type to smoke."
    
    margaret @ say "I'm not. Or at least I wasn't. I've just got things on my mind."

    player "Such as?"
    
    show margaret sad smoking

    margaret @ say "Private things."

    player "Oh."

    margaret @ say "What about you?"

    show margaret smoking

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
        xpos 300
        ypos y_claire

    claire @ say "Hey [name]! Glad you could make it today!"

    player "Hey Claire! Yeah, I really wasn't feeling too good the other day..."
    
    show claire sweater happy

    claire @ say "Being sick is the wooooorst! I'm happy you're feeling better!"

    player "Tell me about it..."

    hide claire with dissolve

    show celestine happy at center with dissolve:
        ypos y_celestine

    celestine @ say "Good afternoon class! Today we're going to be watching a favorite of mine, Beauty and the Beast!"
    
    show celestine neutral
    
    celestine @ say "I'm sure you're all familiar with the story, so you should be able to follow along and hopefully pick out some of the words they use."
    celestine @ say "It's good you were able to join us today, [name]! It would have been a shame for you to miss such a masterpiece."
    celestine @ say "Oh and it's a wonderful learning opportunity as well! I'm a firm believer that watching movies in another language is extremely helpful for familiarizing yourself with the language!"
    
    show celestine happy
    
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

    celestine @ say "C'est la fin! What did you all think of it?"

    show claire sweater happy at center with dissolve:
        ypos y_claire
        xpos 670

    show celestine at flipright

    claire @ say "I liked it! I picked up a few words they were saying and could infer what they were saying pretty well I think."

    celestine @ say "Tres bon! I may pick a few more movies to show in class in the coming months..."
    celestine @ say "But for now, enjoy your afternoon! You're all dismissed!"

    stop music fadeout 1.0

    scene bg campus with fade
    
    play music "audio/music/Evan Schaeffer - Aqueduct.ogg" fadein .5

    show claire sweater pose suggestive at center with dissolve:
        xzoom -1
        ypos y_claire
        xpos 0

    show box with Dissolve(.2):
        ypos 0
    
    show ava at offscreenright:
        ypos y_ava
        yalign 0

    claire @ say "...That was a pretty good movie, wasn't it? I'm a sucker for any kind of romantic film!"

    player "Yeah, it wasn't bad. I'd sooner re-watch the animated version though."
    
    show claire sweater overjoyed

    claire @ say "The animated version will always hold a special place in my heart ksksksks!"
    gunner "{nw}"

    show ava casual happy at center:
        xpos 320
    show claire:
        xpos -330
    with move

    ava @ say "Hey guys, how was class?"
    
    show claire sweater happy
    
    player "We just got done watching La Belle et la Bête."
    
    show ava casual concerned

    n "Ava looks confused for a bit before figuring it out."
    
    show ava casual daydream

    ava @ say "Ah right, French class."

    claire @ say "How was philosophy?"
    
    show ava casual annoyed

    ava @ say "Boring. It's all stuff I've already learned. I can't believe they didn't take my credits from high school."

    claire @ say "Aww... at least you don't have to worry about your grade if you already know all the material!"
    
    show ava casual unimpressed
    
    ava @ say "Yeah. Honestly I might just start skipping class."
    
    claire @ say "Gasp!"
    
    n "She actually says the word gasp."
    
    claire @ say "What a naughty student you are!"
    
    ava @ say "Meh."
    
    claire @ say "Actually, this gives me an idea..."
    
    n "Suddenly, your head feels so heavy it's going to drag you down to the ground as it painfully pulsates."
    n "You stumble back and take a deep breath."
    
    player "Ugh, I'd love to stay and chat but I've got a killer headache."
    player "I think I'm just gonna go back to my dorm and sleep it off."
    
    ava @ say "Huh? Okay then, hope you feel better!"
    
    claire @ say "Maybe you're still getting over your illness?"
    
    player "Yeah maybe."
    
    claire @ say "Take care [name]!"
    
    ava @ say "See you later!"
    
    player "Later guys."
    
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

    show rori neutral at center with dissolve:
        ypos y_rori

    rori @ say "[name]? You're finally awake!"
    rori @ say "Wait right here, I'll go get the doctor!"
    
    rori "{nw}"
    
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

    kitsuragi @ say "I'd like to perform some tests that will hopefully determine the cause of these dizzy spells."
    kitsuragi @ say "You were unconscious for two whole days and I'm afraid to put you back on your feet."

    menu:
        "Two days?!":
            player "Two days?! There goes my attendance record."
            
            kitsuragi @ say "Your friend here waited by your side the whole time."
            
            player "Aww thanks Rori, you didn't have to do that."
            
            rori @ say "It's alright. I didn't want you to be alone."
            
            kitsuragi @ say "You can get caught up on your studies over the weekend. There are more pressing matters to tend to right now."
        "I can walk fine":
            player "I can walk just fine. See?"
            
            n "You throw the blanket off you and swing your legs over the edge of the bed."
            n "You can already tell this isn't going to end well but you've already committed to the bit."
            n "When your feet touch the cool tile floor, a numb sensation runs across your skin. The muscles that would normally hold your body up simply fail to do anything and you come crumpling down."
            
            rori @ say "[name]!"
            
            n "Rori helps you up and tucks you back into bed like a dumb useless baby."
            
            player "See? Perfectly normal."
            
            kitsuragi @ say "Riiiight..."
            
    kitsuragi @ say "In any case, I would encourage you to return home, Rori. Don't worry, we'll keep a close eye on [name]."

    rori @ say "Aww... Alright."

    n "Rori looks somewhat disappointed but understanding."

    player "Here Rori, lemme give you my phone number so I can update you when they find out what's wrong with me."

    n "Rori immediately brightens up and pulls out his phone."

    rori @ say "Sure! What is it?"

    n "You tell him your number and he types it into his contact list."

    rori @ say "Aaaaand done!"
    rori @ say "See you later [name]. Hope you feel better soon!"

    player "Thanks Rori!"

    n "He grabs his backpack and gives you a fist bump on his way out."

    hide rori with dissolve

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

    #stop music fadeout 1.0

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
    
    call phone_start
    
    call message_start("me", "Hey Rori", "testimage.png")
    call reply_message("Thanks for dragging my ass to the hospital") 
    
    call message("Rori", "Np", "roriavi.png") 
    call message("Rori", "I actually carried you btw", "roriavi.png") 
    
    call reply_message("Oh for real?")
    call reply_message("Damn you must be strong") 
    
    call message("Rori", "It actually wasn't that hard once I got you up on my shoulder", "roriavi.png") 
    call message("Rori", "You alright?", "roriavi.png") 
    
    call reply_message("Myeah probably")
    call reply_message("I'm still at the hospital cause they wanna do more tests")
    
    call message("Rori", "Fug that's a long time", "roriavi.png") 
    call message("Rori", "Hope it's nothing serious", "roriavi.png") 
    
    call reply_message("They just want me to stay here until they're sure I won't randomly pass out in the middle of the street again.") 

    call message("Rori", "Ahh makes sense", "roriavi.png") 
    call message("Rori", "Need me to bring you anything ?", "roriavi.png") 

    call reply_message("Nah I'm good. I got my school books and stuff.") 
    call reply_message("Thanks tho") 
    
    call message("Rori", "Text me if you want anything", "roriavi.png") 
    call message("Rori", "I know hospital food sucks", "roriavi.png") 
    
    call reply_message("Thx will do") 
    
    call phone_end
    
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
                n "{cps=0}{/cps}"
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
                    $ avaPoints = avaPoints + 1
                    
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

    call screen phone_reply("What?","choice3","Thanks?","choice4")

    label choice3:
        $ clairephonewhat = True

        call phone_after_menu from _call_phone_after_menu_2

        call message_start("me", "What?", "testimage.png") from _call_message_start_9

        call message("Claire", "What?", "claireavi.png") from _call_message_46

        call reply_message("...") from _call_reply_message_32
        call reply_message("Idk") from _call_reply_message_33
        call reply_message("Nvm") from _call_reply_message_34

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
        $ clairePoints = clairePoints + 1
        $ clairephonethx = True

        call phone_after_menu from _call_phone_after_menu_3
        call message_start("me", "Thanks?", "testimage.png") from _call_message_start_10

        call message("Claire", "Ur welcome cutie~ ksksksksks ;)", "claireavi.png") from _call_message_55

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
        
        call reply_message("BOOBA")

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
        xpos 0

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
    n "The doctor said to take it easy, so you're just gonna relax in bed all day."
    
    
    
    n "You still have class in a few hours after all."
    n "When it comes time for you to go to bed, you pop another one of those pills, as instructed."
    n "You're already getting sick of them but you gotta do what you gotta do to stay alive you guess."
    n "You rest your head on your pillow and pray nothing bad happens tomorrow as sleep overtakes you."

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

    play music "audio/ambient/morning birds.ogg" fadein 1.5

    show box with Dissolve(.2):
        ypos 0

    n "You wake up and pop one of the pills the doctor gave you."
    n "You're not sure if it's just placebo, but for the first time in nearly a week you don't feel like death which is a good sign."
    n "Returning to class is kind of a drag but it's better than being in that hospital."
    
    stop music fadeout 1.5
    
    scene bg classroom with fade
    
    play music "audio/music/mere - schooldaze.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0
    
    n "You drifted off into a daydream during history class, only returning to reality when you heard your name called."
    
    show rothbauer at center with dissolve:
        xpos 0
        ypos y_roth

    rothbauer @ say "[name], could you tell me why there's no class on Friday?"

    player "Huh? I've been coming in on Fridays for nothing?"

    n "Mr. Rothbauer sighs. You get the feeling that was supposed to be an easy question."

    rothbauer @ say "Must have been a long night studying, eh?"
    rothbauer @ say "*This* Friday is a holiday. Anthromorph's Liberation Day!"
    rothbauer @ say "89 years ago, following the mass reduction in human population, the National Liberties Act was signed which gave anthromorph equal rights to humans."
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
    
    play music "audio/music/mere - schooldaze faster.ogg" fadein 1.5
    
    show box with Dissolve(.2):
        ypos 0
    
    show herschel at center with dissolve:
        xpos 0
        
    herschel @ say "...alright, I think that's enough for today's lesson but we still have a bit of time leftover!"
    
    show gunner neutral at center with dissolve:
        xpos -550
        ypos y_gunner
        xzoom -1
    
    gunner @ say "Does that mean we can go home early?"
    
    herschel @ say "Of course not! Instead what I have in mind is an extra credit opportunity, something you of all students should be particularly interested in."
    
    n "Gunner mutters something under his breath."
    
    gunner @ say "This fucking bitch..."
    
    hide gunner with dissolve
    
    n "Thankfully Mrs. Herschel doesn't seem to have heard his remark."
    
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
                xpos -550
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
            $ goodEnd = goodEnd + 1
            
            n "Before you can say anything, Gunner pipes up."
            
            show gunner neutral at center with dissolve:
                xpos -550
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
            
            gunner @ say "What the fuck kind of reasoning is that..?"
            
            herschel @ say "Very good [name], I'll add one point to your final grade."
            
    stop music fadeout 1.0
    
    scene bg campus with fade
    
    n "Gunner walks with you after class and you once again find Rori on his laptop out on the field."
    
    show rori neutral at center:
        ypos y_rori
        xoffset -450
    show gunner neutral at center:
        ypos y_gunner
        xoffset -450
    with dissolve
    
    rori @ say "Sup. You all done for the day?"
    
    gunner @ say "Yeah. You out here doing your compsci homework again?"
    
    rori @ say "Computer *engineering* not science. There's a difference."
    
    n "Gunner shrugs nonchalantly."
    
    gunner @ say "If you say so. Both look like coding to me."
    
    n "Rori looks up from his screen and seems to just now notice you're there."
    
    rori @ say "Hey [name]! Glad you're out of the hospital!"
    
    player "I know right? About time. They kept me there like a prisoner all weekend."
    
    gunner @ say "Yeah man, what was with that?"
    
    player "I dunno, just been feeling dizzy and stuff lately."
    player "But they gave me some pills and now I feel fine."
    
    rori @ say "Well I'm glad you're okay now. You looked dead when I found you!"
    
    gunner @ say "You still kinda look like it."
    
    player "Gee, thanks..."
    
    gunner @ say "I'm just kiddin!'"
    gunner @ say "Hey, you guys wanna get into some shenanigans today?"
    
    n "Rori raises a brow but doesn't say anything."
    
    player "I dunno, I'm still trying to take it easy, at least for a few days."
    
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
            player "What are you doing here?"
            
            margaret @ say "I've gotta do something to pass the time, don't I?"
            
            player "I just thought you'd be more into reading books or something."
            
            margaret @ say "I've read enough books for one lifetime, I think."
            margaret @ say "The animals around here don't seem to care about my interpretations of Virginia Wolf however."
            
            player "...Well what *are* your interpretations of Virginia Wolf?"
            
            margaret @ say "I'm not fond of her. Her streams of consciousness are a bore and her brand of feminism is too pompous for my tastes."
            margaret @ say "I won't blame you if you just read summaries online instead of reading her books when we go over her."
            
            menu:
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
                    
                    margaret @ say "And where has that taken you?"
                    
                    player "It brought me to this fancy pants university."
                    
                    margaret @ say "Then perhaps you're doing quite well as a jellyfish~"
                    margaret @ say "I suppose I'm more of a wolf. Always chasing after things, relentlessly, until I left my pack behind."
                    
                    player "Why not start a new pack? I was sort of a lone wolf too until I got here and started making friends."
                    
                    margaret @ say "It's far too late for me to start over."
                    margaret @ say "You ought to cherish the time you have with your friends while you're young."
                    
                    player "You make it sound like it's game over once you reach a certain age."
                    
                    margaret @ say "Well, it sort of is if you don't have your life together by a certain time."
                    
                    player "You can't be at that point already. There's still plenty of time."
                    
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
                    margaret @ say "Now I'm just an old lady feeding the birds on my own."
                    
                    n "She looks over to you, then back at the ducks."
                    
                    margaret @ say "Sometimes with a curious student, but not often."
                    
                    player "Come on, you're not that old."
                    
                    margaret @ say "Oh?"
                    
    #margaret @ say "And just how old do you think I am?"    
    
    menu:
        ellen "{cps=0}And just how old do you think I am?{/cps}"
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
            
            margaret @ say "Excuse me???"
            
            player "Mathematically speaking."
            
            margaret @ say "Hm. I suppose it is."
            
            player "Happy birthday by the way."
            
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
    
    scene bg campus with fade
    
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
    
    claire @ say "We sure did~"
    claire @ say "It was Ava's first time drinking!"
    
    ava @ say "Ugh, don't remind me."
    
    claire @ say "I had to drink like an entire keg of beer to even feel anything!"
    
    ava @ say "I don't know how you can stomach it."
    
    claire @ say "I guess I'm just built different!"
    
    n "Ava looks up and down Claire."
    
    ava @ say "Uh huh."
    
    menu:
        claire "{cps=0}I guess I'm just built different!{/cps}"
        "Must be her genes":
            player "Must be your genes."
            
            claire @ say "I know right??"
            
            ava @ say "You're too big for your genes."
            
            claire @ say "Too big for my bras too."
            
            ava @ say "W-where did that come from?!"
            
        "She's FAT!":
            player "It's because you're fat."
            
            claire @ say "Oh? And is that a bad thing?"
            
            ava @ say "Please respond wisely."
            
            menu:
                "{cps=0}Is that a bad thing?{/cps}"
                "Hell no!":
                    $ clairePoints =+ 1
                    
                    player "Hell no! I like chunky bunnies. Thick rabbits are the best."
                    
                    claire @ say "Oh you~"
                    
                    player "You could even stand to put on a few more pounds haha"
                    
                    show claire sweater flustered
                    
                    claire @ say "You think so??"
                    
                    show ava typical annoyed
                    
                    ava @ say "Okay enough with the thinly veiled weight gain fetish talk."
                "Kinda":
                    $ clairePoints =- 1
                    
                    player "N-not at all. You're perfectly friend shaped."
                    
                    claire @ say "Just \"friend\" shaped?"
                    
                    ava @ say "Oof."
                "Yes":
                    player "I'm just saying your should eat a salad every so often."
                    
                    claire @ say "I do!"
                    
                    player "Maybe a smaller one then."
                    
                    claire @ say "Hmph!"
                    claire @ say "I'm not *that* fat, I'm mostly fluff and muscle!"
                    
                    player "Keep telling yourself that."
                    
                    n "Claire pouts and makes a whining sound."
            
        "She's *ahem* high in mass":
            player "More body mass means you need more alcohol to get fucked up."
            
            claire @ say "Well duh!"
            claire @ say "But I ran the numbers for how much a bunny of my size should have to drink and it wasn't even close!"
            
            player "Huh. Maybe you really are built different."
            
            ava @ say "Built like a tank."
            
            claire @ say "Optimized."
    
    n "You chat for a bit longer then remember it's a short week."
    
    player "You guys are alright, dont come to school on Friday."

    claire @ say "Oh yeah! What are y'all's plans for the three way-"
    claire @ say "I mean three day weekend?"
    
    player "I got nothin' so far."
    
    ava @ say "I was thinking of taking some shots on film at this spooky abandoned hospital nearby."
    ava @ say "I could use a partner to make sure I don't get shanked by a crazed hobo if either of you wanna come."
    
    claire @ say "Sorry, I'm gonna be busy with some sorority stuff. Top secret sorority stuff."

    ava @ say "Aww. How about you, [name]?"
    
    menu:
        ava "{cps=0}How about you, [name]?{/cps}"
        "That sounds fun!":
            $ avaPoints += 1
            $ avaUrbex = True
            
            show claire sweater happy
            
            player "That sounds fun! I'd love to go with you!"
            
            show ava casual overjoyed

            ava @ say "Sweet! You don't mind if it's haunted, do you? Cause it's probably haunted."

            player "No, haunted is fine."

            claire @ say "Ksksksks you two are so cute!"

            show ava casual angry

            ava @ say "We are not!"
            
            show claire sweater derp
            
            claire @ say "Girl chill! I'm just joking!"
            
            
        "I'll pass.":
            show claire sweater happy
            
            player "Sounds cool but I'll pass. I'm supposed to go to the parade in town to get extra credit in history."
            
            show ava casual unimpressed

            ava @ say "Aww..."

            
    hide ava
    hide claire
    with dissolve

    hide box

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
    
    scene bg campus with fade
    
    show gunner neutral at center with dissolve:
        ypos y_gunner
    
    gunner @ say "LMAO are you gonna \'study hard\' this weekend, [name]?"
    
    menu:
        "Nope":
            player "Nope. Cool people don't study."
            
            gunner @ say "Right on, brother!"
            
            n "Gunner's fist demands a bump and you do not disappoint."
            
            gunner @ say "So what you got planned?"
            
            if avaUrbex == True:
                player "I'm going urban exploring with some chick."
                
                gunner @ say "Oh so like a date?"
                
                player "Not really."
                
                gunner @ say "You're at least gonna fuck her, right?"
                
                player "I wasn't planning on it."
            else:
                player "Nothing at all."
                
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
            
            gunner @ say "If you can't handle her at her best, you don't deserve her at her worst."
        "Actually yeah":
            player "Yeah actually, I'm really behind on everything."
            
            gunner @ say "That's gay."
            
            player "Maybe so but I still need to pass my classes."
            
    n "Rori sees you two approaching and closes his laptop"
    
    show rori neutral at center with dissolve:
        ypos y_rori
        
    rori @ say "Sup guys."
    
    player "Heya."
    
    gunner @ say "Rori please tell me you've got something good planned for the weekend."
    
    rori @ say "Hmm... Nope, not really."
    rori @ say "Was just gonna work on my projects and maybe torrent a new anime."
    
    gunner @ say "Ugh, don't you guys even celebrate Animorph's Liberation Day?"
    
    rori @ say "Does anyone? It's just a day off from work or school."
    
    player "I'm not even an animorph, so no."
    
    gunner @ say "Oh right, you guys are freshmen so you wouldn't be in the *know.*"
    
    rori @ say "The *know?*"
    
    gunner @ say "Here at Harmonia, we have traditions. Sacred traditions."
    
    n "Gunner gestures for you both to come closer so he can whisper something."
    
    gunner @ say "Every year on Liberation Day, the fraternities conduct a panty raid!"
    
    rori @ say "A what?"
    
    gunner @ say "Oh my God Rori you cannot be this homosexual."
    gunner @ say "It's where you sneak into a girl's room and steal her panties."
    
    rori @ say "That's it? Sounds kinda lame."
    
    player "Panty raids aren't real. It's just some dumb thing Hollywoo came up with for college movies."
    
    gunner @ say "Where do you think they got the idea from?"
    gunner @ say "Me and the boys did it last year. Are you two down to join me this year?"
    
    rori @ say "This sounds like the worst risk versus reward ratio of all time."
    
    gunner @ say "Nah bro, it's like unofficially sanctioned by the university. It's a loooooong time tradition."
    gunner @ say "Nobody's ever gotten in serious trouble for it."
    gunner @ say "But you still need someone to watch your back."
    gunner @ say "Come on, it'll be fun I promise!"
    
    n "Rori lets out a frustrated huff."
    
    rori @ say "Fine, I'll tag along."
    rori @ say "But only to make sure you don't do anything *too* stupid."
    
    gunner @ say "Yes!!!"
    
    n "Gunner looks at you expectantly."
    
    gunner @ say "And what about you?"
    
    if avaUrbex == True:
        player "I already make plans to do some urbex stuff with someone this weekend. Sorry."
        
        gunner @ say "No sweat. Just be sure your schedule's free next year!"
        
        rori @ say "And save me from having to go."
        
        gunner @ say "Do it for Rori."
        
        player "Haha sure."
        player "You two have fun with the panty raid. I gotta run for now."
    else:
        menu:
            "Let's do it":
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
                gunner @ say "You gay or something?"
                gunner @ say "You can ogle Rori's ass while we sneak around if that's the case."
                
                rori @ say "H-hey!"
                
                player "I just have better things to do."
                
                n "Gunner shrugs, pretending like he doesn't care."
                
                gunner @ say "Fine, do what you want. Just don't expect me and Rori to share the spoils from our treasure hunt!"
                
                player "You two have fun with that. I gotta run for now."
                
    gunner @ say "Laters."
    
    rori @ say "Laters."
                
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    