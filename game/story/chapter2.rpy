label chapter2start:

    ###CHAPTER 2
    ###weather is randomized (starting in week 3?) and affects what you can do after class
    ###once a week you can sleep in and get a chance at a unique night scene
    ###can also do night scenes on weekends more freely
    ###feel weird wednesday afternoon after giving book to rose at library and go to bed early. change to you go home and give rose the book later. she berates you for taking so long.
    ###pass out in class on thursday and take the next day off

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

    show rothbauer at norm with dissolve

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
    
    show rose neutral at left
    
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
        
    show herschel at norm with dissolve
    
    herschel @ say "Hello class, I hope you all had a pleasant weekend!"
    herschel @ say "Today we'll be going over Bayes' theorem, which is a way of determining probability of a cause from its effect."
    herschel @ say "This is how insurance companies derive your potential risk from factors such as age, previous conditions, and family history."
    herschel @ say "It basically allows you to apply conditions to a set of data and find all sorts of statistical probabilities!"
    herschel @ say "Let's get started with some examples..."
    
    hide herschel with dissolve
    
    n "Mrs. Herschel goes through some problems, starting off with a basic one then adding further complexities to subsequent ones."
    
    scene bg campus with fade
    
    n "Gunner ran off after class, saying something about fraternity obligations."
    n "That leaves you free for the rest of the day."
    
    call afterClassOptions
    
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
    
label week2Tuesday:
    scene bg lecturehall with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    show ellen teacher happy at norm with dissolve

    ellen @ say "Good morning everyone. Today we'll be finishing up The Death of Ivan Ilyich. I'll be sad to see him go but we have plenty of other great books to get through and so little time."
    ellen @ say "After Ivan falls and injures his side, he suffers from worsening pain that causes him to become irritable and further destabilize his relationship with his family."
    ellen @ say "His condition eventually leaves him bedridden and unable to work. Faced with both his mortality and the loss of his sense of purpose, he reflects on what it truly means to die."
    ellen @ say "He comes to realize that the perception of death revolves around the fulfillment of life one has made for themself."
    ellen @ say "He had once believed he led a fulfilling life by acquiring prestige and status, but as he lay dying, none of his achievements mattered so much as the sympathy he received from his servant."
    ellen @ say "Moved by its sheer authenticity, Ivan finally understood while on his deathbed that by pursuing his own interests, he had neglected to foster a caring family."
    ellen @ say "Their relationship resembled that of business partners, where one is only good for the convenience and profits they bring in, but by this time Ivan was nothing but dead weight."
    ellen @ say "His existence brought about an impersonal and artificial partnership that could only acknowledge each other as far as how one benefitted the other."
    ellen @ say "And thus his death would be a relief to them."
    
    n "Damn, what a downer."
    n "You suppose that's about as happy an ending as you can get when it comes to Russian literature though."
    n "Mrs. Ellen talks about some interpretations and gets some students' opinions before hinting that an analysis of life and death in Tolstoy's context will be on the test."
    
    scene bg classroom with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    show celestine neutral at norm with dissolve

    celestine @ say "Bonne journée, classe! How was your weekend? Have any of you encountered any French words in your day to day life you never noticed before?"
    
    show claire sweater neutral
    
    n "Claire waves her paw in the air energetically."
    
    claire @ say "I did!! Lots of food and stuff at cafes and bakeries are French! There's umm cafe au lait which is coffee with milk..."
    claire @ say "And fondant and macrons and brioche and savarin..."
    
    celestine @ say "Oui! France is of course known for its culinary arts! It's only natural that many of their words for cuisine would end up in English."
    celestine @ say "And they sure do love their cafes and bistros! If you go to Paris, you will find one on every corner!"
    celestine @ say "That brings us to today's topic: basic conversation you might experience while out in town shopping."
    
    scene bg campus with fade
    
    show claire sweater neutral at center with dissolve
    
    claire @ say "Wish I could stay and chat [name] but I've got sorority duties to take care of today!"
    claire @ say "See you later!"
    
    n "Claire pulls you into one of her signature suffocating hugs before zooming off to do whatever sorority girls do."
    
    hide claire with dissolve 
    
    n "That leaves your schedule free for the day."
    
    call afterClassOptions
    
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
    
    scene bg classroom with fade

    play music "audio/music/mere - schooldaze.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0
        
    show rothbauer at norm with dissolve

    rothbauer @ say "Good morning class! I hope you're prepared for today's quiz!"

    player "Wha-? Quiz?"

    show rose neutral pendant at norm with dissolve:
        xpos -540
        xzoom -1

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
    
    show rothbauer at center with dissolve
    
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

    show gunner neutral at center with dissolve
    
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
    
    n "Gunner practically drags you across campus to your dorm where he tucks you into bed and reads you a bedtime story."
    n "Okay you're pretty sure you hallucinated that last part but the point is you're in bed and rapidly falling asleep."
    
    gunner @ say "Hope you feel better soon. Text me if you need anything!"
    
    player "Thanks. See you in class if I survive."
    
    gunner @ say "Later!"
    
    scene bg black with fade

    hide box

    show bg calendar
    show twednesday at norm
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

    show ellen teacher neutral at norm with dissolve

    ellen @ say "Today we'll be starting a new story, this time originating from ancient Greece in the 5th century BCE."
    ellen @ say "It is the archetypal hero's journey so often found in literature that succeeded it, as well as in our own lives!"
    ellen @ say "This is the tale first told by Homer, \"The Odyssey!\""
    ellen @ say "What's especially interesting about these old poems passed down through oral tradition rather than written word, is that every generation adds their own spin."
    ellen @ say "So the version we'll be reading today is not the same as the original, but is instead an accumulation of the values of various cultures throughout time."
    
    n "Miss Ellen describes some of the historical context and impact of the story but it all blends together into a jumble of incomprehensible words as your brain once again falls into a stupor."

    n "The room starts to spin and you lose your sense of balance."

    stop music fadeout .5

    hide ellen
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
    ellen @ say "[name]! Are you alright?"

    stop music fadeout 1.0

    n "You snap out of your dizzy spell but find that you've fallen out of your seat with the whole class looking at you."
    n "Ellen is looking down at you with a look of genuine concern."

    show ellen teacher sad at norm with dissolve

    play music "audio/ambient/indoors people talking.ogg" fadein .5

    show ellen teacher sad

    ellen @ say "[name]?"
    
    show ellen sad at shudder
    
    ellen @ say "You collapsed all of a sudden..."
    ellen @ say "Do you need a doctor??"

    show ellen teacher sad

    n "You pull yourself back into your seat and shake your head."

    player "N-no, that won't be necessary. I'm fine."

    ellen @ say "Are you sure? It's not every day a student of mine passes out like that."

    player "Y-yeah, I think I'm just dehydrated or something."

    show ellen teacher neutral:
        ypos 10
        linear .1 ypos 0
        
    pause .1

    ellen @ say "Hmm. You better drink more!"
    ellen @ say "And just to be on the safe side, I want you to go home and get some rest. You're excused from class today."

    #n "A day off? Sounds too good to be true. You decide to take her up on the offer before she changes her mind."

    player "Err, thanks."

    n "You pack your things and head out the door, stumbling on the stairs on your way out."

    ellen @ say "Be sure to read the assigned chapters for next time!"

    show ellen

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
    show tthursday at norm
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
    show tfriday at norm
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7
    
    scene bg campus with fade
    
    $ townEvents.append("avaGarden")
    
    $ avaClaireGarden = True
        
    n "Claire and Ava are already waiting for you at your usual hangout spot."
    
    show ava neutral
    show claire sweater neutral
    
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

    show ava normal neutral at norm:
        #xzoom -1
        xpos 375
    show claire outdoors neutral at norm:
        xzoom -1
        xpos -400
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
    
    show ava normal neutral

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
    
    show claire outdoors heyeah
    
    claire @ say "Ohmygosh we look great! This is just the perfect day, isn't it!"

    n "Ava gets up and gestures to the bench."
    
    show claire outdoors neutral

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
            #finished
            $ clairePoints = clairePoints - 1
            $ avaPoints = avaPoints + 1
            
            player "Alright but I'm getting my picture taken with you next."

            show ava overjoyed

            ava @ say "Who, me??"

            n "She looks to Claire, as if seeking her approval."

            claire @ say "Sure, go for it!"
            
            show ava normal neutral

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
            
            show ava normal neutral

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
    show tsaturday at norm
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

    show rose armscrossed neutral at norm with dissolve:
        xzoom -1

    rose @ say "Hm? Oh, it's you. What do you want?"

    n "You pull the tattered book from your bag and hold it out for her."
    
    n "She seems confused at first but quickly snatches it from your grasp and continues on her way."

    player "Not even a 'thank you?'"

    show rose angry -armscrossed

    n "Rose snaps back around and glares at you."

    rose @ say "I told you I don't need your help. Now leave me alone."

    n "You pull a few loose papers from the pocket the book was in."

    player "What about these pages that fell out? Do you want those too?"

    show rose furious

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
            
            show rose unimpressed at norm with dissolve
            
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
    
    show gunner neutral with dissolve
    
    gunner "Yeah so then I'm like \"fuck you\" and oh hi Rori!"
    
    n "Gunner started following you after class and telling you frat boy stories until you came across Rori sitting on the grass working on something on his laptop."
    
    rori @ say "Waaah!"
    
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
    
    rori @ say "I think you mean \"Be gay, do crime.\""
    
    gunner @ say "Exactly! Let's commit a crime!"
    gunner @ say "No homo."
    
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
        "\[Gay\] Maybe we shouldn't become criminals":
            player "Can't we just be gay and not do crime?"
        "\[Not Gay\] Maybe we shouldn't become criminals":
            player "Maybe we could just do something fun and legal?"