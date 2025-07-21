#chapter 4

#to do
    #add autumn backgrounds
    #color more backgrounds (add watercolor to lecture hall)
    #revise ch 1-3 to add more contextual stuff and cut out fluff
    #draw teacher and nurse sprites
    #porcupine cameo?
    #add mini scenes like claire's coffee date (she gets honey and salt latte)
    #dean's coffee scene
    
#midterms are on thursday/friday so you have to hunker down on studying, but some distractions are in play
#history exam has an extra credit question about dinosaurs
#miss ellen asks if you're doing anything during the break and might ask you to come over. either way you get her number and start texting (later on you not ellen and miss ellen have the same number)
#after midterms, gunner, ava and claire go home for fall break
#rory taunts rori for not coming home
#can either walk around playing pokemon go with rori or creative writing with mishka
#find out rose lives next door to you
#later get stuck in a power outage in the dorms until you find the breaker and flip it with rose. can't use fire escape or it will set off the sprinklers and ruin everything
#when gunner comes back, he's in shock at all the rats rori has collected in their dorm
#get grades back, see what you need to work on
#chapter ends with skipping class to hang out with ava and claire, then having a medical episode and finding your true diagnosis



label chapter4:
    #monday
    
    rothbauer @ say "...That's the final lesson that will be on the midterm! We'll have a review on Wednesday then you'll be all set for Friday's exam."
    rothbauer @ say "That's all I have for you today. Good luck on your midterms!"
    
    n "The classroom fills with the sounds of papers shuffling and bags being zipped as students begin to file out."
    
    if historySkill < 3:
        n "You have a bad feeling about this history exam. Maybe you should ask someone for help studying."
        n "Rose is definitely the smartest person in this class. She's aced every quiz so far and always has her snout in the books."
        n "As much as you hate to ask, she might be your best bet. You muster up the courage to look over to her and clear your throat."
        
        player "Hey Rose, I-"
        
        rose @ say "Nope. Study on your own."
        
        player "But I-"
        
        rose @ say "Don't care."
        
        n "Without even looking at you, she packs her things and walks away."
        
        
    else:
        n "You feel sufficiently prepared for this exam. A lot of it is stuff you've learned before, just in greater detail."
        n "Still though, if you wanted to ace it you could go for some tutoring."
        
    scene bg hallways
    
    n "On your way to stats, you spot Rori at the vending machine again playing with his rat companion."
    
    rori @ say "Okay... sit! Sit? Please? I'll give you another pretzel if you sit."
    
    n "There's desperation in his voice. He must have been at this for a while but the rat just wants to crawl up and down his sleeves sniffing at every fold in the fabric."
    
    player "Hi Rori. G'day, Guts."
    
    rori @ say "Heya [name]. I'm just trying to teach Guts some tricks. I think he sorta understands what I want him to do but he's... defiant."
    
    player "Must be in his rebellious phase."
    
    n "Guts looks up at you before running down Rori's sleeve and snatching the pretzel out of his hoof."
    
    rori @ say "Hey!"
    
    n "From the corner of your eye you see Gunner striding up to you."
    
    gunner @ say "Sup homos."
    
    menu:
        "How did you know??":
            $ youGay = True
            
            player "H-how did you know I'm a homo?"
            
            gunner @ say "It's shorthand for homo sapien."
            gunner @ say "Wait a minute, are you actually-"
            
        "I'm not a homo":
            $ roriPoints -= 1
            player "Hold up, I ain't no homo!"
            
            gunner @ say "But you are a homo sapien!"
            gunner @ say "You literally cannot deny your homo-ness."
            
        "Respond \"Kill yourself\"":
            $ gunnerPoints -= 1
            
            player "Kill yourself."
            
            gunner @ say "After you."
            
            rori @ say "Guys..."
        
    gunner @ say "Holy shit a rat!!"
    
    n "Gunner pounces in the air, pawing and clawing at Rori's hoodie as Guts scurries around frantically."
    
    rori @ say "Hey! Stop it!"
    
    n "A sound not unlike a baseball being struck by a bat rings out as Rori's horns collide with Gunner's skull."
    n "Gunner falls flat on his back and Rori goes to check on Guts."
    
    rori @ say "There you are! Are you okay?"
    
    n "Guts is still a bit shaken but he seems to find comfort in the Rori's grasp."
    
    player "Dude I think you KO'd Gunner."
    
    rori @ say "Did I? I didn't mean to, I just reacted like any ram would."
    
    menu:
        "Let's steal his wallet":
            $ playerBullyLevel += 1
            
            player "He deserved it. Let's see how much cash he's carrying. I'm sure he won't miss a couple thousand bucks."
            
            rori @ say "Do what you will, I'm just glad Guts isn't hurt."
            
            n "You crouch down to Gunner's limp body and feel around for his wallet but it's not long before his eyes snap open."
            
            gunner @ say "Keep your paws to yourself, mister."
            gunner @ say "Sheesh, I get knocked out for two seconds and you can't help trying to molest me."
            
            player "I was just checking your pulse."
            
            gunner @ say "Yeah yeah I've heard it all before. Trying to see if my cock throbs when you grab it."
            
        "We should see if he's still alive":
            player "We should at least check and see if he's still breathing."
            
            rori @ say "G-good idea."
            rori @ say "I didn't kill him, did I?"
            
            n "You crouch down to Gunner's limp body and poke him on the shoulder."
            n "..."
            n "You poke again."
            n "..."
            n "Gunner starts to stir, groaning in pain. He reaches up to his head where Rori struck him and winces."
            
            gunner @ say "Ughhh..."
            
            player "You okay?"
            
            gunner @ say "It hurts so much..."
            
            player "You're not bleeding but you might have a concussion. We can take you to the hospital if you're gonna cry about it."
            
            gunner @ say "I don't care about that..."
            gunner @ say "I'm more upset that I got knocked out by *Rori* of all people."
            
            rori @ say "Oh, good to see he's still his usual self. I thought I might have given him brain damage."

    n "Gunner rises to his feet, shaking his head."
    
    gunner @ say "Sorry, instincts got a hold of me. I see prey animal, I go for it."
    
    #player "Are secretary birds considered prey animals? Feral ones are pretty aggressive."
    
    rori @ say "Be nice to Guts! He's already crippled!"
    
    player "Yeah, what did he ever do to you?"
    
    gunner @ say "Wait, you named him? Is that the rat from a few weeks ago?"
    
    rori @ say "Yup! I started visiting him regularly and we just sorta became friends."
    
    gunner @ say "Gross."
    
    rori @ say "Rats are actually super smart and learn quickly. I've been teaching him tricks! Watch"
    rori @ say "C'mere Guts, in one sleeve and out the other!"
    
    n "Rori holds open one of his sleeves and Guts crawls inside. A moment later he pops out from his other sleeve."
    
    player "Impressive. I could never do that."
    
    gunner @ say "Yeah cool, just don't bring fleas into our room. The last thing I need is the black plague localized in our dorm during midterms."
    
    rori @ say "Don't worry, he's chill. I gave him a little bath and everything!"
    
    player "Sounds like you're taking great care of him!"
    
    rori @ say "Yeah! I never had a pet before so I did a bunch of research and found out how to best take care of him!"
    
    gunner @ say "I guess if he makes you so happy then I'll try to repress my feline instincts to kill it on sight."
    
    rori @ say "Thanks. And I'll try to repress my sheep instincts to headbutt on reaction."
    
    player "It was a pretty well-timed overhead attack."
    player "I think it's about time we get to class now."
    
    rori @ say "Oki! See you guys later!"
    
    player "Bye Rori! Bye Guts!"
    
    gunner @ say "Later homo. Later rat."
    
    rori @ say "Good luck with midterms!"
    
    player "You too!"
    
    scene bg classroom
    
    herschel @ say "Good afternoon class! The midterm is coming up on Friday but we still have a lot of content to cover so let's jump right in!"
    
    gunner @ say "You mean there's *more* to study?!"
    
    herschel @ say "Yup! The field of mathematics may as well be infinitely spanning, so there's little time to waste!"
    
    gunner @ say "Does that mean we won't even have a review on Wednesday?"
    
    herschel @ say "A review? This is college dear, not daycare."
    herschel @ say "Now then, starting with a Bernoulli distribution, we'll derive a probability mass function over k possible outcomes..."
    
    n "Gunner turns to look at you."
    
    gunner @ say "You and me are going to the library to study after this."
    
    scene bg library
    
    n "After class, Gunner dragged you to the library and found a table for just the two of you."
    
    if statsSkill < 3:
        n "You don't really mind the impropmtu study session, you could use some more practice in statistics."
        
    else:
        n "You're feeling confident in your math abilities to do well on the test, but a little extra practice won't hurt."
        
    gunner @ say "Okay, let's start from the start. What is probability?"
    
    player "You don't know?"
    
    gunner @ say "Obviously I know, but this is gonna be a comprehensive review."
    
    player "There's not enough time in a day to go over half a semester's worth of lessons. Just focus on what you struggle with."
    
    gunner @ say "Ok ok ok I just *cannot* afford to fail this class again."
    gunner @ say "Like I get the basics but when you start throwing in factorials and shit it gets confusing."
    
    player "Yeah, there are a lot of formulas to memorize, and knowing when to use which one."
    
    gunner @ say "Right so like on last week's homework I couldn't figure out which to use..."
    
    n "Gunner opens his textbook and points at a problem. This one gave you some difficulty as well but you managed to solve it correctly."
    n "You work through a few problems with him then start looking over the ones that have stumped you."
    n "At least you try to but Gunner interrupts you every few minutes with another question."
    
    menu:
        "Focus on helping him":
            $ gunnerPoints += 1
            
            n "You'll be nice and help him out since he's so far behind you. You just hope you don't drop a letter grade by neglecting your own studies."
            
            gunner @ say "Thanks for the help bro, it really means a lot!"
        "Focus on your own studies":
            $ statsSkill += 1
    
            player "You gotta try figuring these out on your own. I won't be there to help you during the test."
            
            gunner @ say "We could always cheat :3"
            
            player "Yeah no I'm not copying your wrong answers."
            
            gunner @ say "But can I copy your wrong answers?"
            
            menu:
                "Why not":
                    player "As long as you don't drag me into it when you get caught."
                "Nah":
                    player "Mrs. Herschel will know something is up if we both get the same answers."
                    
                    gunner @ say "I'll take the fall for it if she notices."
                    
                    player "Whatever, it's your grade."
                    
            n "You resume working through problems, occasionally helping your study partner when it's trivial for you."
    
        
    #go to library to study with gunner but he distracts you. claims the concussion rori gave him earlier is messing with his ability to study
    #choose to either focus on your own studies or help him study
    #explain statistics and probability in terms of stock markets and betting


    #tuesday
    
    n "The following day..."
    
    #margaret @ say "That just about sums up our review for Thursday's midterm! Study hard and do your best!"
    
    celestine @ say "Bonjours les étudiants!"
    celestine @ say "We're officially one week away from the midterm! You're all doing well in class so I have no doubt that everyone pass!"
    celestine @ say "N'est-ce pas, [name]?"

    player "Err..."

    menu:
        player "{cps=0}Err...{/cps}"
        "Mais oui!":
            player "Mais oui!"

            celestine @ say "Très bon!"
        "Je ne sais pas...":
            player "Je ne sais pas..."

            celestine @ say "Hmm..."
            celestine @ say "Claire, pourriez-vous donner des cours à [name], s'il vous plaît?"

            show claire sweater happy at center with dissolve:
                xzoom -1
                xpos -300

            claire @ say "Mais oui!"

            celestine @ say "C'est parfait!"

            hide claire with dissolve

    celestine @ say "Let's begin a review of the semester so far, shall we?"
    
    n "Mrs. Celestine goes around the classroom asking questions in French to each student."
    n "Unsurprisingly, Claire has no trouble at all, whereas you have to take a few notes."
    n "After class ends she turns to you with a devious grin."
    
    claire @ say "Heyyyyy [name]~"
    claire @ say "I'm having trouble with a few French words, would you like to come over to my dorm and \"\"\"study\"\"\"?"
    
    menu:
        "No thanks":
            n "You have a feeling this would involve more than just studying."
        
            player "No thanks, I'm good on my own."
            
            claire @ say "Awww..."
            claire @ say "Good luck on your midterms!"
            
            player "You too!"
            
            n "You pack your things and head to the library to cram for the exams."
            
            scene bg library with fade
            
            n "What will you study?"
            
            menu:
                "French":
                    $ frenchSkill += 2
                    n "You pick up your French textbook and practice some lessons."
                "Literature":
                    $ literatureSkill += 2
                    n "You open your totally legally acquired epub of [currentbook] and start reading."
                "History":
                    $ historySkill += 2
                    n "You crack open your History textbook and read up on some ancient cultures."
                "Statistics":
                    $ statsSkill += 2
                    n "You flip open your statistics book and open a calculator app to crunch some numbers."
                    
            n "Without any distractions in place you feel like you learned more than you normally do."
            n "That's about all you can do today. You hope that's enough to pass the midterm."
            
        "Yeah!":
            $ clairePoints += 1
            
            player "Yeah, I could go for a private study session!"
            
            claire @ say "Yay!~"
            
            n "Claire proceeds to grab your hand and drag you to her dorm."
            
            scene bg avadorm
            
            show box with Dissolve(.2):
                ypos 0
                
            if claireFrenchSession == 0:
                call claireFrenchStudy1
            else:
                call claireFrenchStudy2
    
    
    #wednesday
    
    n "You get a sinking feeling in your gut after classes."
    n "These were the last ones before your midterms. All the lessons and reviews do nothing to combat the nerves you get from the impending exams."
    n "What if you missed something? What if you suddenly forget how to write your name?"
    n "This is your last chance to prepare, better make it count."
    
    scene bg library with fade
    
    n "The library is packed with other students making their last stand. It's hard to even find a place to sit. Some are even sitting on the floor with their books sprawled out around them."
    
    
    $ randumb = renpy.random.randint(0, 1)
    
    if randumb == 0:
        $ roseLibraryMidterms = True
        
        n "Every available spot is taken. All except for one table with a single occupant emitting bitch aura so strong it repels all others."
        n "Be brave, [name]. Maybe if you sit at the far end she won't give you rabies."
        n "You try to sneakily pull out the chair and sit down before she notices."
        n "A sudden whizzing sound pierces the air followed by a stinging sensation on your hand, causing you to let go of the chair."
        
        player "Ow! What the fuck?"
        
        n "Looking down, you notice an ink splotch pooled in your fresh wound and a fountain pen lying on the ground."
        
        rose @ say "This table is reserved for God's chosen species. Get lost."
        
        menu:
            "All I see is a filthy raccoon.":
                player "All I see here is a filthy trash panda."
                
                rose @ say "And all I see is a barely evolved monkey taking up space and wasting air!"
                
                player "I can't hear you over the sound of millenia of being the dominant species."
                
                rose @ say "Your time on this planet is long overdue!"
                
                player "And yet I'm still here."
                
                rose @ say "What have I done to deserve this hell?"
                
                menu:
                    "WTF is your problem?":
                        player "What the fuck is your problem? Why are you such a cunt?"
                        
                        rose @ say "Because I like being one."
                        rose @ say "It's a raccoon thing, you wouldn't get it."
                        
                        player "Nah, tons of people are cunts and you're not special."
                        
                        rose @ say "You mean that animalistic sort of reactionary tendency? Please. You can barely see two steps ahead, let alone two hundred."
                        rose @ say "Raccoons have a calculated view of the world and understand our place at the top. It's not our fault we're simply superior."
                        
                        player "So superior you ended up being trash gremlins once humans took over."
                        
                        rose @ say "We're a species of survival! No matter what we always end up on top!"
                        rose @ say "The current age is proof of that! The human menace is nearly wiped out!"
                        rose @ say "The president is a raccoon! The top 10 billionaires are raccoons! The dean of our university is a raccoon!"
                        rose @ say "It's our world and you're just living in it."
                        
                        player "I still don't get why you have to be such a bitch. The dean is a nice guy for a raccoon."
                        
                        rose @ say "He's already peaked, he has it all and there's no more power left for him to seek."
                        rose @ say "It's not like he'd tell you what he had to do to get where he is now."
                        
                        $ suspicionOfDean = True
                        
                        player "Whatever, I get it. Raccoons are simultaneously the most wrongfully persecuted group and the most powerful. Funny how that works."
                        
                        rose @ say "You don't know a damn thing about the world, do you? I'll give you a hint, it's not at all like your cheap public education told you."
                        
                    "Karma for being a bitch":
                        player "Maybe it's just karma for you being such a bitch."
                        
                        rose @ say "Karma is something lesser species made up to feel good about themselves."
                        
                        player "It takes kindess and fairness to build a functioning society."
                        
                        rose @ say "That's what you think."
                        
                    "I'm literally just existing":
                        player "I'm literally just existing here. Is that so bad?"
                        
                        rose @ say "Ugh you don't even realize how terrible you are. It'd be sad if it weren't so disgusting!"
                        
                        player "What is your problem with humans? We basically built civilization from the ground up. You'd still be living in trees if not for us."
                        
                        rose @ say "What an ignorant thing to say! And you genuinely believe it!"
                        
                        player "Uh yeah? Humans invented almost all the useful stuff while everyone else was living like their feral counterparts."
                        
                        rose @ say "This is your brain on human propaganda."
                        
                player "What's that supposed to mean."
                        
                rose @ say "It's not my job to educate you."
                rose @ say "*Sigh*"
                rose @ say "...But I will if you do something for me."
                
                player "What?"
                
                rose @ say "Go get me a coffee. No sugar or milk. I will kill you if you bring me a coffee with that junk in it."
                
                n "She thinks you'll spend your hard earned money buying her an overpriced coffee to listen to her lecture. Will you?"
                
                menu:
                    "Go for it":
                        player "Fine whatever, I wanted to get one for myself anyway. After I listen to your lecture, I want to copy your notes for the midterm."
                        
                        rose @ say "Deal."
                        
                        player "Be right back."
                        
                        call getRoseCoffee
                    "Fuck that":
                        $ frenchSkill += 1
                        $ statsSkill += 1
                        $ literatureSkill += 1
                        
                        player "Screw that, get your own damn coffee. I don't need your raccoonist lecture about how I'm so terrible because of my ancestors."
                        
                        rose @ say "Typical human scum..."
                        
                        n "You drop your backpack down onto the table and pull out your study material."
                        n "Stupid raccoon bitch, who does she think she is?"
                        n "You came here to study history but just looking at it makes you think of her."
                        n "You decide to study everything other than it."
                        n "You're better off in those classes now but you're not so sure you can ace the history test now. You'll just have to wing it cause it's getting late out."
                        n "You pack your things and get ready to leave but Rose looks like she's about to pull an all nighter."
                        
                        jump midtermDay1              
                
            "I belong here then.":
                player "Master species only? Then get out of my seat, trash panda."
                
                rose @ say "How dare you insinuate you're anything more than a barely evolved monkey!"
                
                player "I can't hear you over the sound of millenia of being the dominant species."
                
                rose @ say "Your time on this planet is long overdue!"
                
                player "And yet I'm still here."
                
                rose @ say "What have I done to deserve this hell?"
                
                menu:
                    "WTF is your problem?":
                        player "What the fuck is your problem? Why are you such a cunt?"
                        
                        rose @ say "Because I like being one."
                        rose @ say "It's a raccoon thing, you wouldn't get it."
                        
                        player "Nah, tons of people are cunts and you're not special."
                        
                        rose @ say "You mean that animalistic sort of reactionary tendency? Please. You can barely see two steps ahead, let alone two hundred."
                        rose @ say "Raccoons have a calculated view of the world and understand our place at the top. It's not our fault we're simply superior."
                        
                        player "So superior you ended up being trash gremlins once humans took over."
                        
                        rose @ say "We're a species of survival! No matter what we always end up on top!"
                        rose @ say "The current age is proof of that! The human menace is nearly wiped out!"
                        rose @ say "The president is a raccoon! The top 10 billionaires are raccoons! The dean of our university is a raccoon!"
                        rose @ say "It's our world and you're just living in it."
                        
                        player "I still don't get why you have to be such a bitch. The dean is a nice guy for a raccoon."
                        
                        rose @ say "He's already peaked, he has it all and there's no more power left for him to seek."
                        rose @ say "It's not like he'd tell you what he had to do to get where he is now."
                        
                        $ suspicionOfDean = True
                        
                        player "Whatever, I get it. Raccoons are simultaneously the most wrongfully persecuted group and the most powerful. Funny how that works."
                        
                        rose @ say "You don't know a damn thing about the world, do you? I'll give you a hint, it's not at all like your cheap public education told you."
                        
                    "Karma for being a bitch":
                        player "Maybe it's just karma for you being such a bitch."
                        
                        rose @ say "Karma is something lesser species made up to feel good about themselves."
                        
                        player "It takes kindess and fairness to build a functioning society."
                        
                        rose @ say "That's what you think."
                        
                    "I'm literally just existing":
                        player "I'm literally just existing here. Is that so bad?"
                        
                        rose @ say "Ugh you don't even realize how terrible you are. It'd be sad if it weren't so disgusting!"
                        
                        player "What is your problem with humans? We basically built civilization from the ground up. You'd still be living in trees if not for us."
                        
                        rose @ say "What an ignorant thing to say! And you genuinely believe it!"
                        
                        player "Uh yeah? Humans invented almost all the useful stuff while everyone else was living like their feral counterparts."
                        
                        rose @ say "This is your brain on human propaganda."
                        
                player "What's that supposed to mean."
                        
                rose @ say "It's not my job to educate you."
                rose @ say "*Sigh*"
                rose @ say "...But I will if you do something for me."
                
                player "What?"
                
                rose @ say "Go get me a coffee. No sugar or milk. I will kill you if you bring me a coffee with that junk in it."
                
                n "She thinks you'll spend your hard earned money buying her an overpriced coffee to listen to her lecture. Will you?"
                
                menu:
                    "Go for it":
                        player "Fine whatever, I wanted to get one for myself anyway. After I listen to your lecture, I want to copy your notes for the midterm."
                        
                        rose @ say "Deal."
                        
                        player "Be right back."
                        
                        call getRoseCoffee
                    "Fuck that":
                        $ frenchSkill += 1
                        $ statsSkill += 1
                        $ literatureSkill += 1
                        
                        player "Screw that, get your own damn coffee. I don't need your raccoonist lecture about how I'm so terrible because of my ancestors."
                        
                        rose @ say "Typical human scum..."
                        
                        n "You drop your backpack down onto the table and pull out your study material."
                        n "Stupid raccoon bitch, who does she think she is?"
                        n "You came here to study history but just looking at it makes you think of her."
                        n "You decide to study everything other than it."
                        n "You're better off in those classes now but you're not so sure you can ace the history test now. You'll just have to wing it cause it's getting late out."
                        n "You pack your things and get ready to leave but Rose looks like she's about to pull an all nighter."
                        
                        jump midtermDay1                        
                
                
                
            "My mistake...":
                player "Sorry, my mistake... Here's your fountain pen back please don't stab me with it."
                
                n "She snatches the pen from your hand and returns to writing her notes like nothing ever happened."
                
                rose @ say "...What? Go on, shoo."
                rose @ say "Invasive species..."
                
                n "You look around at the table. It's full of open textbooks with print so tiny it strains your eyes to try reading them."
                
                player "Are you studying for the history midterm?"
                
                rose @ say "You think I need to study for that class?"
                
                n "On the surface she sounds offended but you can sense a hint of pride, scoffing at the notion that she wouldn't be prepared."
                
                rose @ say "I'm doing PhD level independent work, gathering sources and making sense of a very contested point in history."
                
                menu:
                    "Tell me more":
                        $ rosePoints += 1
                        
                        player "Sounds kinda interesting."
                        
                        rose @ say "You wouldn't get it."
                        
                        if historyPoints < 4:
                            player "You're right, I can barely even keep up in class. You're clearly the expert here."
                            
                            rose @ say "At least you acknowledge your inherent ineptitude."
                            
                            player "I still wanna know what it's about though."
                            
                            n "Rose sighs and rolls her eyes."
                            
                        else:
                            player "Maybe not but I bet my ancestors were there. Considering how important humans were to every recorded historical event ever."
                            
                            n "Rose sets down her pen and stands up in her chair to get level with you."
                            
                            rose @ say "Humanist propaganda!"
                            rose @ say "The only reason you egotistical freaks ended up at the forefront of history is because you *burned* everything else to the ground."
                            
                            n "With a 'hmph' she sits back down and resumes her reading, trying to regain her composure."
                            
                            player "Really? First time I've heard of it."
                        
                        rose @ say "Perhaps if you get me a coffee I'll attempt to educate you on how your kind are a blight on civilization."
                        rose @ say "If you can even understand it, that is."
                        
                    "Sounds boring":
                        player "Lame. Are you getting paid for it or something?"
                        
                        rose @ say "I'm doing it out of my own interest. And it'll look good on a resume after I publish my results."
                        
                        player "What's it even about?"
                        
                        rose @ say "You wouldn't get it."
                        
                        if historyPoints < 4:
                            player "You're right, I can barely even keep up in class. You're clearly the expert here."
                            
                            rose @ say "At least you acknowledge your inherent ineptitude."
                            
                            player "I still wanna know what it's about though."
                            
                            n "Rose sighs and rolls her eyes."
                            
                        else:
                            player "Maybe not but I bet my ancestors were there. Considering how important humans were to every recorded historical event ever."
                            
                            n "Rose sets down her pen and stands up in her chair to get level with you."
                            
                            rose @ say "Humanist propaganda!"
                            rose @ say "The only reason you egotistical freaks ended up at the forefront of history is because you *burned* everything else to the ground."
                            
                            n "With a 'hmph' she sits back down and resumes her reading, trying to regain her composure."
                            
                            player "Really? First time I've heard of it."
                        
                        rose @ say "Perhaps if you get me a coffee I'll attempt to educate you on how your kind are a blight on civilization."
                        rose @ say "If you can even understand it, that is."      
                        
                n "She thinks you'll spend your hard earned money buying her an overpriced coffee to listen to her lecture. Will you?"
                
                menu:
                    "Go for it":
                        player "Fine whatever, I wanted to get one for myself anyway. How do you take it? Black like your soul?"
                        
                        rose @ say "Yes."
                        
                        player "Of course. Be right back."
                        
                        call getRoseCoffee
                        
                    "Fuck that":
                        $ frenchSkill += 1
                        $ statsSkill += 1
                        $ literatureSkill += 1
                        
                        player "Screw that, get your own damn coffee."
                        
                        rose @ say "Don't tell me what to do!"
                        
                        player "Shut up and go back to studying! I've got my own studies to take care of."
                        
                        n "The two of you bury your noses in your books and pretend the other doesn't exist."
                        n "Just thinking about history is annoying you because she's such a nerd for it."
                        n "You decide to study everything other than it."
                        n "By the time you leave, Rose is still writing her report."
                        
                        jump midtermDay1
                
            "I'm sitting here regardless":    
                player "I'm sitting here whether you like it or not."
                player "I have a right to be here. It's the school's library, you don't own it."
                
                rose @ say "I kinda do own it actually."
                rose @ say "I can just tell my grandpa you're harassing me and he'll get you expelled, blacklisted, sent to Guantanamo, suicided by two bullets in the back of your head..."
                rose @ say "Whichever I feel like."
                
                $ suspicionOfDean = True
                
                player "Ooh yeah I'm real scared of your kind old grandpa who's friendly to me."
                ###if you've had coffee with him before mention it
                
                rose @ say "Looks can be deceiving. He can be ruthless. You have to be to get to where he is."
                
                player "Well let's just see what happens if I sit down. Oh wow nothing happened!"
                
                rose @ say "Nothing yet. You're wasting my time. You're supposed to shut the fuck up in a library."
                
                player "You're the one who can't resist bitching me out!"
                
                rose @ say "It's the least you deserve!"
                
                player "I deserve a quiet space to study!"
                
                n "You shove Rose's books aside and set down your bag, pulling out your notebooks."
                n "Rose just scoffs and puts in her earbuds, trying to ignore your existence."
                n "About an hour into studying, you start to feel drowsy but you have so much material left to cover."
                n "Fffffuck you need a coffee if you're gonna survive. Luckily the cafe is only a short distance away."
                n "You won't have to worry about someone stealing your spot while you're away with Rose guarding the table, so you take a trip down to Coffee Zone."
                
                scene bg cafe with fade
                
                n "Coffee Zone is busier than you've ever seen it before. All the tables are taken and you have to wait in line before you can even see Mishka on the other side of the counter."
                n "Eventually you get to see the coffee queen rat, rushing to make everyone's orders all on her own."
                
                mishka @ say "[name]!"
                
                player "Hey Mishka! Is now a good time?"
                #Hope you don't mind me coming in on the busiest day of the year
                
                mishka @ say "It gets so busy during exams week... But I will make the best drinks for you as always!"
                
                player "You're the best Mishka."
                player "Take your time, I don't wanna rush you."
                
                mishka @ say "Hah, thanks."
                
                n "After you order, Mishka immediately gets to work on your drink."
                n "Would now be a good time to ask if she wants to hang out later?"
                n "She's pretty overworked but maybe once midterms are over you two will have some free time."
                
                menu:
                    "\"You doing anything this weekend?\"":
                        $ mishkaPoints += 1
                        $ mishkaMidtermWeekendHangout = True
                    
                        player "Hey I was wondering if maybe you'd be free this weekend?"
                        
                        mishka @ say "Sch-scho vy mayesh na-"
                        
                        n "The rat knocks over a ceramic mug, making a loud clattering noise. She hastily uprights the mug and turns to you."
                        
                        mishka @ say "Th-this weekend? I do not really have plans..."
                        
                        player "Great, neither do I! Would you wanna hang out?"
                        
                        mishka @ say "Umm okay! We can do the hanging out!"
                        
                        player "Awesome! I'll figure out the details and let you know later, k?"
                        
                        mishka @ say "Of course, of course!"
                        
                        ###maybe later have an option where mishka's response changes if she likes or dislikes you
                    
                    "Now's not the time":
                        n "Nah, it's rude to ask her at work, especially when she's juggling orders like this."
                        
                n "You step back and let Mishka work on the drink and take more customer orders."
                n "The poor rat is going back and forth nonstop preparing multiple drinks at once yet doesn't miss a beat."
                n "A few minutes later she calls you up to the counter with the drink you asked for."
                
                player "Thanks! I have to get back to studying. Hopefully you find some time to study too!"
                
                mishka @ say "Oh don't worry about me... Dah skorovo!"
                
                player "See you around!"
                
                n "You take the cardboard cup and make your way back to the library."
                
                scene bg library with fade
                
                show box with Dissolve(.2):
                    ypos 0
                    
                n "You return to your seat across from Rose, reinvigorated to knock out this study session."
                n "The raccoon looks up from her book and sniffs the air."
                
                rose @ say "Coffee? Is that... ah it must be Costa Rican. My favorite type. The best type."
                
                player "Yeah? I dunno I just got it from Coffee Zone."
                
                rose @ say "Hm. I guess you're good for something after all. The scent of a hot drink makes reading all the more soothing."
                
                player "Wow is that a genuine compliment coming from you?"
                
                rose @ say "Don't make the mistake of thinking I'm complementing *you.* A broken clock is right twice a day after all."
                rose @ say "You just happened to do something that enhanced my day. You should feel honored."
                
                #player "Riiiiiight."
                
                menu:
                    "Offer her a sip":
                        $ rosePoints += 1
                        $ historySkill += 2
                        
                        player "You want a sip? I haven't taken one yet."
                        
                        rose @ say "Psh, no."
                        
                        n "Rose narrows her eyes."
                        
                        rose @ say "You've only touched the outer sleeve around the cup, yes?"
                        
                        player "Yeah, why?"
                        
                        n "Rose gets up and walks over to you. She has to pull out a nearby chair and stand on top of it to reach the cup."
                        n "She takes hold of it, pulling it up out of the insulating sleeve and takes a long sip."
                        n "Well, chug is a more accurate term. Is she gonna leave any for you?"
                        n "She downs half the cup before setting it down with a satisfied sigh then returns to her seat across from you."
                        
                        player "You're welcome?"
                        
                        rose @ say "I don't recall thanking you."
                        
                        player "Maybe you thought about it?"
                        
                        rose @ say "Certainly not."
                        
                        player "The reward I get for trying to be nice..."
                        
                        rose @ say "Expecting a reward for being nice just means you weren't being nice in the first place."
                        rose @ say "...But you can have my notes for the midterm as a consolation. I don't need them anymore and this saves me the trouble of disposing of them."
                        
                        player "Oh! I wasn't expecting that. Uh thanks."
                        
                        rose @ say "Don't mention it, just bask in the glory of my flawless handwriting and excellent note structure."
                        
                        n "She flicks a sheet of paper toward you, landing perfectly in place for you to read."
                        
                        n "Wow, she wasn't kidding! Rose's notes are incredibly neat and well-organized. Her handwriting consistency rivals that of a printer. Maybe she's onto something about raccoons being superior after all."
                        n "You feel like all the relevant information is laid out in the most straightforward way possible. This will definitely help boost your grade."
                        n "You start going over it and absorbing the knowledge."
                        
                        
                    "Keep it all to yourself":
                        player "You're welcome?"
                        
                        rose @ say "I don't recall thanking you."
                        
                        player "Maybe you thought about it?"
                        
                        rose @ say "Certainly not."
                        
                        n "Fucking bitch."
                        n "Now you're too annoyed by her to even look at your history notes. You'll have to study something else instead."
                        n "You end up briefly going over everything except history. You didn't absorb as much as you had hoped but you'll at least do a little better in your other classes."
                        
                
                
                jump midtermDay1
                
                
                
                
                
        
        
    
    else:
        $ avaLibraryMidterms = True
        
        n "Your only chance to find an open spot is when someone gets up and leaves. You drop down your bag and settle in before anyone else can steal it from you. It's your study spot now."
        n "By sheer coincidence, you find yourself bumping shoulders with a feathered friend."
        
        ava @ say "OMG hi [name]! Fancy seeing you here!"
        
        player "Ava? Sorry, I didn't even see you there!"
        
        ava @ say "This place gets soooo crowded during midterms, huh?"
        
        player "Apparently! Might have to camp out for a spot next time!"
        
        ava @ say "Oooh do you think they'd actually let us do that? Chirp!~"
        
        player "Probably not. We'd have to be sneaky."
        
        ava @ say "Hmmm... I might know a spot."
        ava @ say "But now's not the time! Midterms start tomorrow and I'm so not prepared aaaaaaaaa!!!"
        
        n "You look down at the bird's study materials sprawled out on the carpet."
        n "A notebook with flowery writing and sketches, her laptop plugged into her iconic camera transferring photos, and a stack of flash cards."

        player "I've got literature and French tomorrow. What are you working on?"
        
        ava @ say "I'm mostly worried about art history because I'm so bad at remembering dates!"
        ava @ say "I usually space out in that class because so far it's all been like *ancient* stuff but I'm more of a modern bird ya know?"
        ava @ say "I've been making these flash cards to help me remember."
        
        player "Neat! I don't really do anything special when studying, I just read and pray I remember."
        
        ava @ say "You wanna try making some flash cards of your own? I've got plenty leftover!"
        
        
        
        
        #(you help each other study for your different classes)
        #art history ava? flash cards
        #stay the night in the library with ava
        #
        
        
        jump midtermDay1
    
    
label getRoseCoffee:
    $ rosePoints += 1
    $ historySkill += 2
    
    n "Coffee Zone is busier than you've ever seen it before. All the tables are taken and you have to wait in line before you can even see Mishka on the other side of the counter."
    n "Eventually you get to see the coffee queen rat, rushing to make everyone's orders all on her own."
    
    mishka @ say "[name]!"
    
    player "Hey Mishka! Is now a good time?"
    #Hope you don't mind me coming in on the busiest day of the year
    
    mishka @ say "It gets so busy during exams week... But I will make the best drinks for you as always!"
    
    player "You're the best Mishka. Can you make one for my.... friend? too?"
    
    mishka @ say "Oh? You have someone special you wish to impress?"
    
    player "N-no nothing like that. If anything I'm being coerced into buying her a drink."
    
    mishka @ say "I see... Well friend or foe I will make it all the same."
    
    player "Take your time, I don't wanna rush you."
    
    mishka @ say "Hah, thanks."
    
    n "You order a drink for yourself and one for Rose. Mishka immediately gets to work on it."
    n "Would now be a good time to ask if she wants to hang out later?"
    n "She's pretty overworked but maybe once midterms are over you two will have some free time."
    
    menu:
        "\"You doing anything this weekend?\"":
            $ mishkaPoints += 1
            $ mishkaMidtermWeekendHangout = True
        
            player "Hey I was wondering if maybe you'd be free this weekend?"
            
            mishka @ say "Sch-scho vy mayesh na-"
            
            n "The rat knocks over a ceramic mug, making a loud clattering noise. She hastily uprights the mug and turns to you."
            
            mishka @ say "Th-this weekend? I do not really have plans..."
            
            player "Great, neither do I! Would you wanna hang out?"
            
            mishka @ say "Umm okay! We can do the hanging out!"
            
            player "Awesome! I'll figure out the details and let you know later, k?"
            
            mishka @ say "Of course, of course!"
            
            ###maybe later have an option where mishka's response changes if she likes or dislikes you
        
        "Now's not the time":
            n "Nah, it's rude to ask her at work, especially when she's juggling orders like this."
            
    n "You step back and let Mishka work on the drinks and take more customer orders."
    n "The poor rat is going back and forth nonstop preparing multiple drinks at once yet doesn't miss a beat."
    n "A few minutes later she calls you up to the counter with the drinks you asked for."
    
    player "Thanks! I have to get back to studying. Hopefully you find some time to study too!"
    
    mishka @ say "Oh don't worry about me... Dah skorovo!"
    
    player "See you around!"
    
    n "You take the cardboard cups and make your way back to the library where Rose awaits."
    
    scene bg library with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "As you're making your way back to Rose, an idea pops into your head."
    n "She's always getting on your case for no good reason. Perhaps it's time to pay her back for it."
    
    menu:
        "Spit in her coffee":
            $ rosePoints -= 1
            $ badEnd += 1
            $ spatInRosesCoffee = True
            
            n "You look around and find a spot where nobody can see you then pop the lid off of Rose's coffee."
            n "There we go, a nice globule of human spit to go on top of her drink. Bon appetit, bitch."
            n "You fix the lid back on top and return to her table."
            
            player "Here you go, the finest coffee in Harmonia."
            
            rose @ say "Set it down there. No not there, away from my notes. No, not on top of that book you drooling neanderthal!"
            
            n "Holy fuck is she picky with the placement of this cup."
            n "You set it down and she adjusts it by half a millimeter."
            
            player "...Aren't you gonna take a sip?"
            
            rose @ say "No."
            
            player "The hell? Why not?"
            
            rose @ say "Because human hands touched it."
            
            player "Then why'd you have me get it in the first place?"
            
            show rose skirt handonhip shy at center:
                ypos y_rose
            
            rose @ say "Because I require the aroma of a hot drink to maximize the efficiency of my studies."
            
            n "So you spat in her drink for nothing."
            
            
        "Don't spit in her coffee":
            n "What's wrong with you? How can you even entertain the notion of tampering with someone's drink like that?"
            
            if drankOliviasCoffee == True:
                n "Even if you're some sick freak who drank that alligator's coffee that surely had a few mililiters of her drool in it."
            
            n "You come back to Rose's table and deliver her drink, untampered with."
            
            player "Here you go, the finest coffee in Harmonia."
            
            rose @ say "Set it down there. No not there, away from my notes. No, not on top of that book you drooling neanderthal!"
            
            n "Holy fuck is she picky with the placement of this cup."
            n "You set it down and she adjusts it by half a millimeter."
            
    rose @ say "Perfect. Now just sit over there while I explain to you why the human race was destined for extinction."
            
    n "Rose lists out a few dozen of humanities great fuck ups, including many you've never heard of and several you've only seen on iceberg conspiracy memes."
    n "Rrom the eradication of entire cultures, to burning of the largest libraries, to some interesting views on industrial society and its future, she makes some good points."
    
    player "Okay but given the opportunity, wouldn't any anthromorph civilization do the same?"
    
    n "She sighs. Somehow you can tell she's had to explain this multiple times in her life, each time growing more and more weary."
    
    rose @ say "No, because most anthromorphs lack any ambition or competence to create the conditions to nearly destroy the world at least four times."
    rose @ say "Only raccoons are above humans in terms of intellect and it takes us ruling the remnants of human-based civilization with an iron paw to keep the world in a peaceful and prosperous state."
    
    player "You haven't even been in power for more than a few decades. You can't say you're better than everyone else!"
    
    rose @ say "Raccoons are literally God's chosen people. Read a book for once."
    
    player "I'm not gonna argue religious bullshit with someone who wears a Satanic pendant. Just give me your notes for the midterm and I'll be on my way."
    
    rose @ say "Take them. I obviously don't need them to ace such an easy class."
    
    n "Wow, Rose's notes are incredibly neat and well-organized. Her handwriting consistency rivals that of a printer. Maybe she's onto something about raccoons being superior after all."
    n "You feel like all the relevant information is laid out in the most straightforward way possible. This will definitely help boost your grade."
    n "You take them back to your dorm and read them in detail, absorbing more information than you could have otherwise."
    
    

label midtermDay1:    
    #thursday
    
    
    
    
    


    
        #visit cafe
        #do lit and french midterm, talk to margaret after class, go home and study for either math or history
        
        
        
        
        
        
    # friday
        #do history and math midterms, meet up with the main group after class to discuss plans for the autumn break