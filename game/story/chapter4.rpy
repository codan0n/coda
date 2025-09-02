#chapter 4
#reply to this post or your mother will die in her sleep tonight

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
    
    scene bg hallway summer day
    
    show box with Dissolve(.2):
        ypos 0
    
    show gunner determined at center:
        ypos y_gunner
        xoffset -400
        xzoom -1
    show rori coat angry neutral at center:
        ypos y_rori
        xoffset 350
    
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
                
            call claireFrenchStudy2
    
    
    #wednesday
    
    n "The following day..."
    
    n "Today's the last day before midterms begin. Better pay attention in class and study hard."
    
    
    if claireSmoochies == True:
    
        scene bg campus autumn day clear
        
        show box with Dissolve(.2):
            ypos 0
    
        n "On your way to class you bump into Ava, looking frantic."
        
        show ava typical neutral at center:
            ypos y_ava
        
        ava @ say "Oh uh... hey, [name]! Ready for midterms?"
        
        player "I'm not sure. I guess I have to be cause they're coming whether I like it or not."
        
        ava @ say "I know right? Just one of those things to do and be over with."
        ava @ say "..."
        
        n "Ava lowers her voice."
        
        ava @ say "So um..."
        
        show ava pose concerned
        
        ava @ say "Did you... do it with Claire last night?"
        
        menu:
            "I sure did":
                if avaPoints > 4:
                    $ avaCucked = True
                $ avaLostInterest = True
                $ fuckedClaireEarly = True
                $ avaJealousy += 3
                
                player "You really wanna know?"
                
                n "Ava nods."
                
                player "Yeah, I did."
                
                ava @ say "Oh..."
                ava @ say "I mean uh... congrats?"
                
                player "It was kind of a spontaneous thing, ya know?"
                
                ava @ say "Right haha yeah, you two just saw the opportunity and fucked."
                ava @ say "On the bed right underneath me."
                ava @ say "I had my headphones on so I couldn't hear you guys btw"
                ava @ say "Just in case you were self conscious about that part."
                
                player "I wasn't."
                
                ava @ say "Then I guess that's a relief."
                ava @ say "I was wondering why the hell the bunk bed was shaking so much."
                
                player "Sorry about that, you know how Claire is."
                
                claire @ say "Speaking of that big beautiful bunny..."
                
                n "Claire hops onto the scene with extra whimsy before practically draping herself on top of you."
                n "You can barely hold her up."
                
                claire @ say "Way to go champ, you really handled that \"study session\" like a pro~"
                claire @ say "I'm sure you'll pass that midterm with flying colors ksksksksks!"
                
                player "Claire please get off of me, I'm too weak from last night."
                
                #ava sprites getting progressively angrier
                
                claire @ say "Oh! I guess you deserve a break. You were doing a lot of heavy lifting after all~"
                
                ava @ say "Would you look at the time, I have to get to class."
                ava @ say "Sounds like you two spent a lot of time studying French last night."
                ava @ say "Hope it was worth it."
                
                n "Ava takes to the skies before you can say goodbye."
                
                claire @ say "She's jealous~"
                
                player "I feel bad that we kept her up last night."
                
                claire @ say "Yeahhhhh, we'll have to study at your place next time~"
                
                player "Mhm~ Think we better get to class now though."
                
                claire @ say "We'll do more stuff after midterms ksksksksks"
                claire @ say "See you around, cutie~"
                
                n "Claire gives you a kiss on your cheek then skips away."
                n "It's gonna be really hard to focus in class today."
                
                
                
                
            "I sure didn't":
                $ avaJealousy += 1
                
                player "Nah, we just kissed and stuff."
                
                ava @ say "Was it... nice? I mean would you do it again?"
                
                menu:
                    "Hell yeah":
                        $ avaJealousy += 1
                        
                        player "Hell yeah, it was fucking awesome."
                        
                        ava @ say "I see..."
                        ava @ say "I'm glad you found someone you enjoy."
                        
                        player "I know right? I used to think Claire was kinda annoying but now I really like spending time with her."
                        player "Should I ask her out??"
                        
                        n "Ava rolls her eyes."
                        
                        ava @ say "If she's the one you want then go for it I guess."
                        ava @ say "You could do better though. Just saying."
                        
                        player "I dunno, Claire might just be the best."
                        
                        n "Ava scoffs."
                        
                        ava @ say "Whatever, I gotta head to class now."
                        
                        n "Ava takes to the skies before you can say goodbye."
                        
                        
                        
                        
                    "Probably not":
                        $ clairePoints -= 1
                        
                        player "Honestly probably not. I was just caught up in the moment and wanted to try it out, ya know?"
                        
                        ava @ say "Y-yeah I totally get that haha!"
                        ava @ say "Like I've come *this close* to kissing Gunner before but I'm still like, holding out in case he gives me the ick."
                        
                        if avaCommitted == True:
                            player "Well... I might be free. Just sayin'."
                            
                            ava @ say "*Breee~*"
                            ava @ say "It'd be nice to explore that option soon~"
                            ava @ say "But ugh midterms. I gotta go to class now. Maybe we can meet up later?"
                            #get coffee, just the two of us?
                            
                            player "I'd love to! Once all this midterm business is taken care of."
                            
                            ava @ say "Can't wait~"
                        else:
                            player "You think you might have a backup plan?"
                            
                            ava @ say "Hmmm... there's *someone* I've got my eyes on~"
                            
                            player "Who?"
                            
                            ava @ say "Someone really oblivious."
                            
                            player "Keeping it a secret, huh?"
                            
                            ava @ say "I'm really not."
                            ava @ say "I've gotta head to class now. See you later!"
                            
                            player "See ya!"
    
    
    ###claire bday scene goes here
    
    
    n "After classes end you suddenly get a sinking feeling in your gut."
    n "You could very well bomb these tests and have to retake classes, wasting valuable time and delaying your graduation."
    n "This is your last chance to prepare, better make it count."
    
    scene bg library with fade
    
    n "The library is packed with other students making their last stand. It's hard to even find a place to sit. Some are even sitting on the floor with their books sprawled out around them."
    
    
    #if you studied with claire last night then default this scene to the rose version
    
    $ randumb = renpy.random.randint(0, 1)
    
    if claireFrenchSession == 2:
        $ randumb = 0
    
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
        
        menu:
            "Make some flash cards":
                $ avaPoints += 1
                $ literatureSkill += 1
                $ frenchSkill += 1
                
                player "Sure, I could give it a shot. We could quiz each other on our subjects too!"
                
                ava @ say "Great idea!"
                
                n "You start writing down some phrases from French on the cards and their translations on the back."
                n "After finishing a few you know will be on the exam, you show them to Ava."
                
                player "Am I doing these right? Like this?"
                
                ava @ say "Yup! Want me to read them out to you and you can try and answer them?"
                
                player "If that's supposed to help me memorize them better then yeah go for it."
                
                ava @ say "It works wonders for some people!"
                ava @ say "Ahem"
                ava @ say "Est-ce que j'ai bien dit ça?"
                ava @ say "Did I say that right?"
                
                player "You didn't give me a chance to answer!"
                
                ava @ say "Huh?"
                
                n "Ava looks at the back of the card to read the translation."
                
                ava @ say "\"Did I say that right?\""
                ava @ say "Very funny. Next one!"
                ava @ say "Comment prononcez-vous ces mots?"
                ava @ say "How do you even pronounce these?"
                
                player "You did it again!"
                
                ava @ say "What, really? Sorry! I don't know how to say these!"
                
                player "Just pretend the last letter of each word doesn't exist. That's usually how I do it."
                
                ava @ say "Ok ok I think I got it."
                ava @ say "Je suis passionnée de photographie."
                ava @ say "Oh I know what this says! \"I am passionate about photography!\""
                ava @ say "Did you put that one in just for me?"
                
                player "Heh no, but thanks for spoiling it for me."
                
                ava @ say "Sorryyy I guess I'm no good at this!"
                
                player "It's alright. Want me to try doing your cards for you?"
                
                ava @ say "Sure!"
                
                n "You pick up Ava's stack of flash cards and have more success reviewing her art history topics than your French ones."
                n "You even learn a few things about ancient art."
                
                #ava has sketches of ancient art on her cards?
                
            "Study independently":
                $ literatureSkill += 2
                $ frenchSkill += 2
                
                player "Thanks but I'll just stick to doing my own thing."
                
                ava @ say "Oki! Lemme know if you wanna take a break and just chill for a bit!"
                
                player "Will do!"
                
                n "You and Ava both study independently of each other but occasionally provide friendly distractions during momentary breaks."
                n "She shows you some photos she's working on editing for a project and gives you an overview of the history of art."
                n "You try showing her some of your French lessons but she has a hard time getting the hang of it."
                n "She's familiar with some of the books you've had to read for literature though and gives her impressions on them."
                
        n "You end up studying well into the evening alongside your birb friend. Looking out through the library's massive windows you can see it's already dark out."
        n "With a yawn, you start packing your things and try to get up from the floor but Ava grabs hold of your hand."
        
        ava @ say "Going somewhere?"
        
        player "Uh yeah? It's getting late and the library is gonna close soon."
        
        ava @ say "And?"
        
        player "And... I was gonna go back to my dorm and fall asleep?"
        
        ava @ say "Why not stay here with me?"
        
        player "Here? At the library?"
        
        ava @ say "I wasn't kidding when I said it'd be fun to stay the night here!"
        
        menu:
            "Stay here with Ava":
                $ avaPoints += 1
                $ literatureSkill -= 1
                $ frenchSkill -= 1
                $ avaLibraryAdventure = True
                
                ###cg of ava, mc, and claire hiding
                
                #player "You sure like to hang out in places you're not supposed to be."
                player "I'm down for it!"
                player "I could use a nice little adventure after studying all day!"
                
                ava @ say "Breeee! This is gonna be so much fun!"
                ava @ say "We just have to find a good hiding spot and lay low when the staff does their final rounds."
                
                player "Any ideas?"
                
                ava @ say "The individual study tables should work! They're enclosed from three sides and the open side faces the wall so we just have to crawl underneath a few minutes before closing time."
                
                player "Huh, that might actually work. Just gotta make sure nobody sees us."
                
                ava @ say "Heh, maybe there's a book on sneaking we can check out first."
                
                player "There's not that much time left. Almost everyone has left already. We better do it before they start closing for real."
                
                ava @ say "It's now or never!"
                
                n "You and Ava nonchalantly make your way to the tables she was talking about. There's a row of them spaced out a few feet from each other and the last occupant just left."
                n "Looking around to make sure nobody is watching, you swiftly dive underneath one and pull the chair towards you."
                n "It's surprisingly roomy down here, and with the chair fully tucked in place, nobody would ever suspect a thing."
                n "You hear Ava do the same as you in the desk next to yours. Now all you have to do is wait."
                n "Your heart races as you become hypersensitive to all the sounds around you. Footsteps meander around and you hear disembodied voices of the staff chatting as they put stray books away."
                n "It feels like someone has been watching you... You can feel the vibrations of the floor as someone approaches your desk."
                n "Suddenly they veer off and you hear the clattering of chair against desk. Curiosity gets the better of you and you dare to take a peek."
                n "Seems Ava had the same idea. Both of you look to one side, watching a third party attempting to copy your hiding strategy."
                
                claire @ say "I think I'm stuck..."
                
                ava @ say "Claire?! What on Earth are you doing??"
                
                claire @ say "I could ask you the same thing!"
                claire @ say "I saw you and [name] swoop underneath these desks and thought that looked fun, so why don't I try it myself!"
                
                ava @ say "You're gonna blow our cover!!"
                
                claire @ say "That's not the only thing I'll blow~ Ksksksksksks!"
                claire @ say "What are you two even up to, I wonder~"
                
                player "We're trying to stay the night in the library. It was kind of a spontaneous idea."
                
                claire @ say "Ooh the forbidden sleepover~ Mind if I join in?"
                
                player "You're too big to even fit under there."
                
                ava @ say "Yeah, you're gonna get us all caught the moment someone walks by!"
                
                claire @ say "B-but-"
                claire @ say "I don't wanna miss out...!"
                claire @ say "You're gonna try stealing [name] from me, aren't you?!"
                
                ava @ say "OMG stop being such a drama queen!"
                
                menu:
                    "Claire can stay":
                        $ clairePoints += 1
                    
                        player "*Sigh*"
                        player "This is so dumb."
                        player "Fine, you can stay Claire but we're not bailing you out if you get caught."
                        
                        claire @ say "Yisssss!!! I'll be super sneaky, they won't know a thing!"
                        
                        ava @ say "Ugh, I hope this doesn't blow up in our faces."
                        
                        player "Quiet down! They're shutting off the lights!"
                        
                        n "You retreat back into your hidden alcove. It's starting to hurt your back being hunched over like this. You wonder how long you'll have to wait before it's safe to leave."
                        n "There's no way someone won't spot Claire."
                        n "Right?"
                        n "One by one, groups of lights shut off around you until you're in darkness and the voices of staff members fades away. All that's left now is the hum of the heating unit."
                        
                        call phone_start 
                        
                        call message_start("Ava", "You think we're good to come out now?", "avaavi.png") 

                        call reply_message("Give it a couple minutes to be safe") 
                        
                        call message("Ava", "I can't believe Claire's fat ass didn't get caught", "avaavi.png") 
                        
                        call message("Claire", "Ikr!!", "claireavi.png") 
                        call message("Claire", "I think my butt is stuck", "claireavi.png") 
                        
                        call reply_message("We'll help you out") 
                        
                        call message("Ava", "I think they're locking up now", "avaavi.png") 
                        
                        call message("Claire", "This is sooo exciting!", "claireavi.png") 
                        call message("Claire", "How did you guys come up with this idea lol", "claireavi.png") 
                        
                        call message("Ava", "There's just something so interesting about school buildings at night!", "avaavi.png") 
                        
                        call reply_message("It gives me chill bumps") 
                        call reply_message("Do birds get those?") 
                        
                        call message("Ava", "Noope :P", "avaavi.png") 
                        call message("Ava", "lemme feel em when we get out of here lol", "avaavi.png") 
                        
                        call message("Claire", "I call dibs on first touch", "claireavi.png") 
                        
                        call reply_message("Sure lol") 
    
                        call phone_end
                        
                        n "A few minutes pass and you feel comfortable leaving your hiding spot. You push away the chair then go to pull the other one out for Ava."
                        
                        ava @ say "What a gentleman~"
                        
                        n "The dim glow from the ambient light leaking through the windows illuminates Ava's soft white feathers, revealing markings that normally aren't visible."
                        
                        if avaUrbex == True:
                            player "Hey, I can see your feather markings again!"
                            
                            ava @ say "Must be the coating on the windows filtering the outside light that's making them visible for ya."
                            ava @ say "A shame most people can't see them all the time."
                            
                            if avaPoints > 4:
                                player "Do you have more markings? Like on your back?"
                                
                                ava @ say "Sure do! But I'm not gonna show you them tonight~"
                                
                                player "Aw."
                                
                                ava @ say "Maybe some other time~ I don't wanna go topless when there's security cameras around."
                                
                                player "Fair."
                                
                            
                        else:
                            player "Whoa, you're... glowing."
                            
                            ava @ say "Huh?"
                            
                            player "You've got spirals and stuff on your wings now!"
                            
                            ava @ say "Yeah? They've always been there."
                            ava @ say "Ohhh you can't normally see 'em though. Forgot, they're near ultraviolet."
                            ava @ say "They probably get washed out in bright light for your eyes."
                            
                            if avaPoints > 4:
                                player "Do you have more markings? Like on your back?"
                                
                                ava @ say "Sure do! But I'm not gonna show you them tonight~"
                                
                                player "Aw."
                                
                                ava @ say "Maybe some other time~ I don't wanna go topless when there's security cameras around."
                                
                                player "Fair."
                                
                                
                        claire @ say "Guys? I'm still stuck!"
                        
                        ava @ say "Right, I forgot about her."
                        
                        player "We're coming, Claire."
                        
                        n "You and Ava grab hold of Claire's paws and pull with all your might. It takes a coupe of good yanks to finally dislodge her rear from the underside of the table."
                                
                        claire @ say "Thanks! Ksksksks~"
                        claire @ say "Are we in the clear?"
                        
                        player "Seems like it. I don't see any guards or hear any alarms."
                        
                        ava @ say "The library is ours for the night!"
                        
                        claire @ say "Woo!! Library sleepover!!!"
                        
                        ava @ say "Shshshshs!!! Somebody outside could still hear us!"
                        
                        claire @ say "Sowwy."
                        
                        player "So... now what?"
                        
                        ava @ say "I don't really know. I didn't think we'd get this far."
                        
                        player "I mean, it's late and we have midterms tomorrow. We can't exactly stay up all night painting each other's nails."
                        
                        ava @ say "How about we just... make a fort out of books and fall asleep in it?"
                        
                        claire "Sounds good to me!"
                        
                        player "We're gonna need some big books."
                        
                        n "The next half hour is spent finding books thick enough to serve as the base for your fort then filling out the rest with whatever manuscripts fit well enough."
                        n "You even manage to form an entrance with an archway that seems stable but leaves you in fear of it all toppling down on you."
                
                        claire @ say "It's glorious!"
                
                        ava @ say "I must say, this is quite an impressive fort!"
                        ava @ say "I don't think we ever could have built such a thing during normal operating hours! The staff would have thrown a fit!"
                        
                        player "It'll be a fun surprise for them to find in the morning after we've left!"
                        
                        n "Inside is just roomy enough for you to sit upright. Ava built a nest of paperback books for you to curl up and sleep in."
                        
                        ava @ say "I tried to find the softest ones to sleep on."
                        
                        player "It beats sleeping on the ground in the woods."
                        
                        claire @ say "Hey, I at least provided a soft bnnuy for you to lean back on!"
                        
                        scene bg library night
                        
                        show box with Dissolve(.2):
                            ypos 0
                        
                        show ava glowy suggestive at center:
                            ypos y_ava
                            xoffset 500
                            matrixcolor BrightnessMatrix(-0.10)
                        
                        show claire sweater derp at center:
                            ypos y_claire
                            xoffset -500
                            xzoom -1
                            matrixcolor BrightnessMatrix(-0.10)
                        
                        ava @ say "How about a soft bird this time instead?"
                
                        menu:
                            "Bnnuy":
                                player "Sorry Ava but I can't resist the bnnuy pillow."
                                
                                ava @ say "Aww... I understand though, Claire is a top tier cuddler~"
                                
                                claire @ say "Everyone needs a big beautiful bunny~"
                                
                                n "Claire pulls you into her grasp, inescapable yet comforting."
                                
                                player "So warm and soft~"
                                
                                if claireBullyLevel > 0:
                                    claire @ say "Who's my little snuggleslut?"
                                    
                                    player "Meeeee!"
                                    
                                    ava @ say "What have you done to him?"
                                    
                                    claire @ say "Don't worry, he likes it~"
                                    
                                claire @ say "Now shush up and get some rest. We all got midterms tomorrow!"
                            
                            "Birb":
                                player "I'll take the birb this time."
                                
                                claire @ say ":skull::skull::skull:"
                                
                                ava @ say "I may not be a good mattress like Claire but I can be a good pillow~"
                            
                                n "Ava snuggles up to you, enveloping you in her soft feathers while Claire pouts beside you."
                                
                                ava @ say "Don't be jealous~"
                                
                                claire @ say "It should have been meeeee!"
                                
                                player "Sorry Claire, this bird has been tempting me."
                                
                                claire @ say "I don't blame you, she's been tempting me too!"
                                
                                ava @ say "W-what?? Tempting you how?!"
                                
                                claire @ say "Ksksksksks wouldn't you like to know~"
                            
                                ava @ say "Go to sleep, you creature!"
                                
                                player "Yeah, we have midterms tomorrow."
                                
                                claire @ say "Fiiine. G'night y'all!"
                            
                            
                            "Why not both?":
                                player "Why not both?"
                                
                                ava @ say "Geez, what a snuggle whore."
                                
                                claire @ say "Don't listen to her, [name], I belive in snuggle positivity! It's perfectly valid to cuddle with lots of people!"
                                claire @ say "Also that's rich coming from you, Ava! Snuggle any catboys recently?"
                                
                                if avaPoints > 5:
                                    ava @ say "As a matter of fact, no I have not!"
                                else:
                                    ava @ say "Maybe I have, so what! At least I kept my pants on!"
                                    
                                    claire @ say "For now~"
                                
                                player "Can we all just chill out and enjoy the present snuggles?"
                                
                                claire @ say "That's what I'm trying to do!"
                                claire @ say "Get in here, Ava!"
                                
                                n "Claire pulls Ava in as well, sandwiching you between the two ladies."
                                
                                claire @ say "Comfy?"
                                
                                player "Very."
                                
                                ava @ say "Yup!"
                                
                                claire @ say "Good~ Now shush up and get some rest. We all got midterms tomorrow!"
                            
                            "Neither":
                                player "I'm good. I've already settled into this stack of National Geographics."
                                
                                claire @ say "Suit yourself!"
                                claire @ say "I just hope you don't mind if Ava and I snuggle right here."
                                
                                ava @ say "Who said I'd snuggle with you?!"
                                
                                claire @ say "Come on, I know you can't resist this soft bunny~"
                                
                                ava @ say "It's true, you're like a mother hen guarding her babies."
                                
                                claire @ say "Get over here and get some snuggles~"
                                
                                ava @ say "Fiiine~"
                                
                                n "Ava scooches over and gets embraced by Claire while you flip through some of the magazines lining the floor."
                                
                                claire @ say "Comfy?"
                                
                                ava @ say "Hehe yup!"
                
                                claire @ say "What about you, [name]? It's not too late to join the cuddles~"
                                
                                player "I'm good, thanks."
                                player "I was thinking of getting some sleep soon though. We all got midterms tomorrow and I wanna be rested up."
                                
                                claire @ say "Yeah, I wish we could stay up late but that's probably for the best."
                                claire @ say "Night guys!"
                        
                                    
                        n "It's not easy falling asleep in an unfamiliar place, especially with the paranoia of getting caught."
                        n "You're keenly aware of every sound in the building, getting a mini heart attack each time a new one appears."
                        n "What's that? Did something just beep? It kinda sounded like the front door just opened."
                        
                        player "Wait- did you hear that just now?"
                        
                        ava @ say "Was the the main entrance? Oh shit I think someone's coming!"
                        
                        n "Scrambling out of your book fort, you dodge the beams coming from a security guard's flashlight and remain unseen... for now."
                        n "You did manage to get separated from Ava and Claire in the process however."
                        n "Your body tenses up, instinctively holding your breath trying to avoid detection. You creep around a bookcase while the guard investigates your fortress."
                        
                        guard "Hey! Is someone there?"
                        
                        n "There's too many gaps in this shelf after you took so many books for the fort! You're a sitting duck!"
                        
                        ava @ say "Squawk!"
                        
                        guard "Show yourself!"
                        
                        n "The guard turns his attention to Ava's distraction, giving you time to get away."
                        n "You find a relatively concealed spot but now it sounds like Ava's in trouble."
                        
                        guard "Alright, I see you! Come on out, birdie."
                        
                        menu:
                            "Make a distraction":
                                n "You'll be giving up your perfect hiding spot but at least you'll take the heat off Ava."
                                n "Just as you're about to draw the guard's attention, Claire whistles to get his attention."
                                
                            
                            "Stay quiet":
                                n "Sorry Ava, you should have hidden better."
                                
                                guard "Stop right there!"
                                
                                ava @ say "Eek!"
                                
                                n "Just as the guard is about to apprehend Ava, Claire whistles to get his attention."
                                
                        n "She somehow climbed on top of a bookshelf and was towering over the guard."
                                
                        claire @ say "Get out of here guys, I'll take him on!"
                        
                        n "The last thing you see is Claire jumping onto the guard, dropping him to the ground and causing the whole floor to shake before Ava takes your hand and pulls you to the exit."
                        
                        
                        n "Outside, you lurk in the shadows waiting to see the result of the rabbit's scuffle with the guard."
                        
                        ava @ say "Oh my gosh, do you think she's okay? Should we go in and back her up?"
                        
                        player "Either she sacrificed herself for us or she'll emerge victorious in combat."
                        
                        n "A few minutes pass by and then a lone figure's sillouette appears behind the glass door."
                        n "Is that...?"
                        
                        ava @ say "Claire!!! You made it!"
                        
                        n "Ava swoops in to give her a hug after she opens the door and escapes the hospital on her own."
                        
                        claire @ say "That guard wasn't so tough!"
                        claire @ say "Some basic jui jitsu was enough to knock him out cold!"
                        
                        player "Holy shit, you didn't have to assault an officer of the law for our sake."
                        
                        claire @ say "I know, but it sounded like fun~ So I did it anyway!"
                        
                        ava @ say "I'm glad you didn't get arrested! That would have been such a nightmare the day before midterms!"
                        
                        claire @ say "I know right! Speaking of which, it's gotten pretty late hasn't it?"
                        
                        player "That's more than enough excitement for the night. Come on, let's all get some rest before exams begin."
                        
                        n "You walk Ava and Claire to their dorm, still riding the high from escaping the library."
                        n "Your heart's still racing by the time you make it back to your dorm but eventually the exhaustion catches up with you and you fall asleep."
                        
                         
                        
                    
                    "Claire must go":
                        $ clairePoints -= 1
                    
                        player "Sorry Claire, you gotta go. It's risky enough as it is with just me and Ava."
                        
                        claire @ say "I see how it is..."
                
                        ava @ say "It's nothing personal, there's just no way this could work."
                        
                        claire @ say "Yeah, I guess so."
                        
                        n "Claire emerges from under her table and gives you a wave before hopping away."
                        
                        claire @ say "Good luck! Don't get caught!"
                        
                        n "You wave back and return to your hidden alcove. It's starting to hurt your back being hunched over like this. You wonder how long you'll have to wait before it's safe to leave."
                        n "One by one, groups of lights shut off around you until you're in darkness and the voices of staff members fades away. All that's left now is the hum of the heating unit."
                        
                        call phone_start 
                        
                        call message_start("Ava", "You think we're good to come out now?", "avaavi.png") 

                        call reply_message("Give it a couple minutes to be safe") 
                        
                        call message("Ava", "Kay", "avaavi.png") 
                        call message("Ava", "I can't believe we're doing this!!", "avaavi.png") 
                        
                        call reply_message("I know right?") 
                        call reply_message("You sure love being in weird places don't you?") 
                        
                        call message("Ava", "Guilty as charged~ ^v^", "avaavi.png") 
                        call message("Ava", "There's just something so interesting about school buildings at night!", "avaavi.png") 
                        
                        call reply_message("It gives me chill bumps") 
                        call reply_message("Do birds get those?") 
                        
                        call message("Ava", "Noope :P", "avaavi.png") 
                        call message("Ava", "lemme feel em when we get out of here lol", "avaavi.png") 
                        
                        call reply_message("Sure lol") 
    
                        call phone_end
                        
                        n "A few minutes pass and you feel comfortable leaving your hiding spot. You push away the chair then go to pull the other one out for Ava."
                        
                        ava @ say "What a gentleman~"
                        
                        n "The dim glow from the ambient light leaking through the windows illuminates Ava's soft white feathers, revealing markings that normally aren't visible."
                        
                        if avaUrbex == True:
                            player "Hey, I can see your feather markings again!"
                            
                            ava @ say "Must be the coating on the windows filtering the outside light that's making them visible for ya."
                            ava @ say "A shame most people can't see them all the time."
                            
                            if avaPoints > 4:
                                player "Do you have more markings? Like on your back?"
                                
                                ava @ say "Sure do! But I'm not gonna show you them tonight~"
                                
                                player "Aw."
                                
                                ava @ say "Maybe some other time~ I don't wanna go topless when there's security cameras around."
                                
                                player "Fair."
                                
                            
                        else:
                            player "Whoa, you're... glowing."
                            
                            ava @ say "Huh?"
                            
                            player "You've got spirals and stuff on your wings now!"
                            
                            ava @ say "Yeah? They've always been there."
                            ava @ say "Ohhh you can't normally see 'em though. Forgot, they're near ultraviolet."
                            ava @ say "They probably get washed out in bright light for your eyes."
                            
                            if avaPoints > 4:
                                player "Do you have more markings? Like on your back?"
                                
                                ava @ say "Sure do! But I'm not gonna show you them tonight~"
                                
                                player "Aw."
                                
                                ava @ say "Maybe some other time~ I don't wanna go topless when there's security cameras around."
                                
                                player "Fair."
                            
                        ava @ say "So I guess we're in the clear?"
                        
                        player "Seems like it. I don't see any guards or hear any alarms."
                        
                        ava @ say "Then the library is ours for the night!"
                        
                        player "Just gotta hope nobody's watching the cameras."
                        
                        ava @ say "There must be thousands of security cams around the university. I doubt someone will see us on them."
                        ava @ say "We'll try and stay out of sight though just in case."
                        
                        player "So... now what?"
                        
                        ava @ say "I don't really know. I didn't think we'd get this far."
                        
                        player "I mean, it's late and we have midterms tomorrow. We can't exactly stay up all night painting each other's nails."
                        
                        ava @ say "How about we just... make a fort out of books and fall asleep in it?"
                        
                        player "Sounds good to me!"
                        
                        n "The next half hour is spent finding books thick enough to serve as the base for your fort then filling out the rest with whatever manuscripts fit well enough."
                        n "You manage to form an entrance with an archway that seems stable but leaves you in fear of it all toppling down on you."
                
                        ava @ say "I must say, this is quite an impressive fort!"
                        ava @ say "I don't think we ever could have built such a thing during normal operating hours! The staff would have thrown a fit!"
                        
                        player "It'll be a fun surprise for them to find in the morning after we've left!"
                        
                        n "Inside is just roomy enough for you to sit upright. Ava built a nest of paperback books for you to curl up and sleep in."
                        
                        ava @ say "I tried to find the softest ones to sleep on."
                        
                        player "It beats sleeping on the ground in the woods."
                        player "No soft bunny though."
                        
                        ava @ say "How about a soft bird instead?"
                
                        player "That'll do."
                        
                        n "Ava snuggles up to you, enveloping you in her soft feathers."
                        
                        if avaPoints > 5:
                            n "This is comfy but you know what could be comfier?"
                            
                            player "Can I make a request?"
                            
                            ava @ say "Is it lewd?"
                            
                            player "..."
                            player "A little."
                            
                            ava @ say "What is it?"
                            
                            menu:
                                "Use her boobs as a pillow":
                                    player "I bet your boobs would be the best pillow I've ever slept on. Can I rest my head on 'em?"
                                    
                                    ava @ say "You're lucky I like you or I woulda slapped you."
                                    
                                    player "Is that a yes then?"
                                    
                                    ava @ say "It's no goose down but my feathers are pretty soft~"
                                    ava @ say "Go ahead, humie~"
                                    
                                    n "You maneuver into place and rest your head on her plush breasts. This beats even those super soft pillows hotels have."
                                    
                                    ava @ say "Ya like it?"
                                    
                                    player "It's perfect~"
                                    
                                    ava @ say "*Chirp*!"
                                    ava @ say "I'm glad you're comfy~"
                                "Use her butt as a pillow":
                                    player "I bet your butt would be the best pillow I've ever slept on. Can I rest my head on it?"
                                    
                                    ava @ say "You're lucky I like you or I woulda slapped you."
                                    
                                    player "Is that a yes then?"
                                    
                                    ava @ say "It's no goose down but my feathers are pretty soft~"
                                    ava @ say "Go ahead, humie~"
                                    
                                    n "You maneuver into place and rest your head on her plush ass. This beats even those super soft pillows hotels have."
                                    
                                    ava @ say "Ya like it?"
                                    
                                    player "It's perfect~"
                                    
                                    ava @ say "*Chirp*!"
                                    ava @ say "I'm glad you're comfy~"
                                    
                                "Nevermind":
                                    player "Nevermind, it was a dumb thought."
                        
                                    n "Ava shrugs."
                                    
                                    ava @ say "Whatever you say~"
                                    ava @ say "I guess I'm flattered you had a lewd thought about me though!"
                                    
                                    player "...Do you have lewd thoughts about me?"
                                    
                                    ava @ say "Sometimes!~"
                                    
                                    player "Care to share any of them?"
                                    
                                    ava @ say "Well you didn't share yours so... nope!"
                                    
                                    player "Aww."
                                    
                        ava @ say "Let's try and get some rest now. Got those midterms in the morning after all!"
                        
                        player "Yeah. Goodnight! Sleep tight!"
                        
                        ava @ say "Nighty night!"
                                    
                        n "You close your eyes, feeling as though sleep could overtake you at any moment, yet it never comes."
                        n "Ava seems to be having trouble falling asleep as well."
                        
                        ava @ say "...I can't sleep."
                        
                        player "Me neither."
                        
                        ava @ say "You anxious about the exams?"
                        
                        player "A little bit. You?"
                        
                        ava @ say "Same."
                        ava @ say "But I think staying the night in an unfamiliar and also illegal to be place maybe wasn't the best idea for tonight."
                        
                        player "Heh you think so?"
                        
                        ava @ say "Maybe, but we're already here. And we made a whole fortress and everything!"
                        
                        player "I know right, isn't it awesome?"
                        
                        ava @ say "It is~"
                        ava @ say "But you know what this night really needs?"
                        
                        player "What?"
                        
                        ava @ say "A scary story!"
                        
                        player "Will that put you to sleep? Won't it just give you nightmares?"
                        
                        ava @ say "I like nightmares! They're like horror movies in your head!"
                        
                        player "Heh okay weirdo~ Got any good stories to share?"
                        
                        ava @ say "I got a few~"
                        
                        n "The bird perks up and starts telling you some of her favorites about serial killers, urban legends, and straight up mythical cosmic horror conspiracy theories."
                        n "You get so engrossed in them that you hardly even notice the sound of the door opening."
                        
                        player "Wait- did you hear that just now?"
                        
                        ava @ say "Was the the main entrance? Oh shit I think someone's coming!"
                        
                        n "Scrambling out of your book fort, you dodge the beams coming from a security guard's flashlight and remain unseen... for now."
                        n "You did manage to get separated from Ava in the process however."
                        n "Your body tenses up, instinctively holding your breath trying to avoid detection. You creep around a bookcase while the guard investigates your fortress."
                        
                        guard "Hey! Is someone there?"
                        
                        n "There's too many gaps in this shelf after you took so many books for the fort! You're a sitting duck!"
                        
                        ava @ say "Squawk!"
                        
                        guard "Show yourself!"
                        
                        n "The guard turns his attention to Ava's distraction, giving you time to get away."
                        n "You find a relatively concealed spot but now it sounds like Ava's in trouble."
                        
                        guard "Alright, I see you. Come on out, birdie."
                        
                        menu:
                            "Make a distraction":
                                n "You'll be giving up your perfect hiding spot but at least you'll take the heat off Ava."
                                
                                player "Over here, pig!"
                                
                                #guard is a literal pig
                                
                                guard "Who said that?!"
                                
                                n "The guard comes storming towards you. As good as your hiding spot is, it doesn't give you much room to get away."
                                n "You resign yourself to your fate and reveal yourself to the guard."
                                
                                player "I'm right here. It's just me here, alone."
                                
                                guard "Found you!"
                                
                                n "The guard apprehends you and roughly drags you out of the library, unamused by your antics."
                                n "After chewing you out for wasting his time, he lets you off with a warning."
                                n "Once he's out of sight, Ava swoops down and tackle hugs you."
                                
                                ava @ say "[name]! You didn't get arrested!"
                                
                                player "Heh, lucky me~"
                                
                                ava @ say "Thanks for distracting the guard for me! I was soooo scared hahaha!"
                                
                                player "Don't mention it, it was nothing. You distracted him for me first after all."
                                
                                if avaPoints > 5:
                                    ava @ say "Well I think you deserve a little reward~"
                                    
                                    n "Ava sidles up to you, placing her wings on your chest. Standing on her tip toes, she gives you a quick kiss(?) on your cheek."
                                    
                                    player "Ow! Did you just peck me?"
                                    
                                    ava @ say "Sorry, beaks are awkward."
                                    
                                    player "It's ok, I liked it~"
                                    
                                    ava @ say "*Chirp!~*"
                                    
                                else:
                                    ava @ say "Well you're still my hero tonight~"
                                    
                                
                            
                            "Stay quiet":
                                n "Sorry Ava, you should have hidden better."
                                
                                guard "Stop right there!"
                                
                                ava @ say "Eek!"
                                
                                n "While the guard apprehends Ava, you quietly sneak out of the library. You're not getting arrested on the night before midterms, fuck that."
                                n "You hang around in the shadows, waiting for Ava and the cop to leave."
                                n "Surprisingly, he releases her once they're out."
                                n "You wait until the coast is clear before running out to her."
                                
                                player "Ava! You're okay!"
                                
                                ava @ say "Heh, yeah..."
                                ava @ say "He bitched me out but thankfully let me go."
                                
                                n "She seems embarrassed about the whole thing."
                                
                                ava @ say "That coulda gone a lot worse."
                                
                                player "Yeah, imagine getting arrested just before midterms. I don't think professors would take kindly to that excuse for missing the exam."
                                
                                ava @ say "That's pretty much the only reason that cop let me go! He said \"I'll let you off easy because you probably have exams tomorrow!\""
                                
                                player "Heh, he probably just didn't wanna fill out the paperwork for bringing you in."
                                
                                ava @ say "That and I'm too cute to be arrested~"
                                ava @ say "Seriously, I've been caught urbexing so often but they always let me go!"
                                
                                player "Luckyyy! They'd probably put me away without a second thought!"
                                
                                ava @ say "Thankfully we didn't have to put that to the test tonight!"
                                
                                
                        n "Ava looks back to the library."
                                
                        ava @ say "I guess we won't be sleeping in the fort tonight, huh?"
                        
                        player "Sadly no. I wish I could see the looks on their faces when the library staff discovers it though."
                        
                        ava @ say "It's a work of art!"
                        
                        player "It truly is. And nobody will even know who made it."
                        
                        ava @ say "Nobody but us~"
                        
                        #player "Heh I guess you're right. Us and that pig cop."
                        
                        #ava @ say "Mhm."
                        
                        player "Yeah. It was an enjoyable night, but I'm ready to go to bed for real."
                        
                        ava @ say "Saaaame. It's already past midnight."
                        
                        player "Oof. Good luck on your midterms!"
                        
                        ava @ say "You too!"
                        
                        n "You walk Ava back to her dorm, bid her a good night, then return to your place for some much needed sleep."        
                        
                        
        
                
                
                #talk about how she can't believe you don't just date claire already, you counter about her not dating gunner already. maybe both of you have eyes on someone else
                
                
                
                
            "Go back to your dorm":
                player "As exciting as that sounds, I'd rather sleep in my comfy bed without worrying about campus security throwing me in jail for trespassing and missing my midterm."
                
                ava @ say "Aww, where's your sense of adventure?"
                
                player "I left it at home."
                
                ava @ say "Have it your way!"
                ava @ say "Guess I'll just spend the night in this library all on my lonesome!"
                
                player "K, have fun with that. Good luck on your midterms!"
                
                ava @ say "You too!"
                
                n "You leave Ava to her scheming. You wonder if she'll actually do it."
                n "You'd rather not do anything to endanger your midterms tomorrow. You return to your dorm and get some rest, trying to ignore the test anxiety creeping up on you."
        
        
        
    jump midtermDay1Cafe
    
    
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
    n "From the eradication of entire cultures, to burning of the largest libraries, to some interesting views on industrial society and its future, she makes some good points."
    
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
    
    jump midtermDay1


label midtermDay1Cafe:
    n "Your alarm drags you up from the comfort of slumber, reminding you that today is one day you can't afford to sleep in."
    n "You need a coffee, badly."
    n "You barely got any sleep after last night's ordeal. You wonder if the fortress is still standing."
    n "There's just enough time to swing by the cafe before starting your literature exam."
    
    
    
    n "Coffee Zone is busier than you've ever seen it before. All the tables are taken and you have to wait in line before you can even see Mishka on the other side of the counter."
    n "Eventually you get to see the coffee queen rat, rushing to make everyone's orders all on her own."
    
    mishka @ say "[name]!"
    
    player "Hey Mishka! Is now a good time?"
    #Hope you don't mind me coming in on the busiest day of the year
    
    mishka @ say "It gets so busy during exams week... But I will make the best drinks for you as always!"
    
    player "You're the best Mishka."
    
    n "Should you get a treat for Ms. Ellen? It might get her to go easy on you when she grades your paper."
    
    menu:
        "Get her a cinnamon roll":
            $ ch4EllenSnack = True
        
            player "Could I get a cinnamon roll to go as well?"
        
            mishka @ say "You have luck, this is the last one yet again!"
            
            player "Did you save it just for me?"
            
            mishka @ say "Well... maybe~"
            
            player "Thanks. I'm gonna try bribing my literature professor with it."
            
            mishka @ say "Hopefully that goes well!"
            
            player "Speaking of which, you're insane to be working when midterms start today. You get enough time to study?"
            
        
        "Don't get her anything":
            n "Nah, you'll do this fair and square. You don't need a crutch to pass."
            
            player "You're insane to be working when midterms start today. You get enough time to study?"
    
    mishka @ say "Um.... Well... There is no need to worry about me, really!"
    
    player "If you say so. I'm sure you'll do well!"
    
    mishka @ say "Heh thanks, I think you will do well too!"
    
    n "You finish up your order and stand around while she gets to work on it."
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
            
    n "You step back and let Mishka work on drinks for multiple customers at once."
    n "The poor rat is going back and forth nonstop preparing multiple drinks at once yet doesn't miss a beat."
    n "A few minutes later she calls you up to the counter with the drinks you asked for."
    
    player "Thanks! See you around!"
    
    mishka @ say "Dah skorovo!"
    
    n "You take the cardboard cup and make your way to the literature building, taking sips along the way that gradually bring you back up to full consciousness."
    
label midtermDay1:    
    #thursday
    
    n "Today's the day. Midterms."
    n "You'll be glad to get them over with."
    n "You've done everything you can to prepare. All that's left to do is face them with courage and put pencil to paper."
    
label midtermDay1Cont:
    n "The classroom is extra hectic just minutes before class is scheduled to begin."
    n "Tons of chatter, anxious students worrying over their grades, hastily trying to cram in knowledge and share answers before the teacher arrives."
    n "You're too tired from all the studying you've done throughout the week to bother. Instead you just try to remain calm."
    
    if ch4EllenSnack == True:
        n "On your way to your desk you drop off a bag containing the cafe's confectionary treat onto Ms. Ellen's table."
        n "She'll know who it's from."
        
    n "You sit down and close your eyes, getting a couple minutes of rest in before the exam begins."
    n "The room goes silent when the door opens and the sound of Ms. Ellen's heels clatters against the floor on her way to the podium."
    
    if ch4EllenSnack == True:
        n "She looks momentarily confused as she picks up the bag you left for her. She gives it a few sniffs then looks around the room."
        n "You give her a wink when her gaze meets yours and she returns it with a smile."
        
    margaret @ say "Good morning class! I'm sure you're all as anxious to be done with this as I am so without further adiue, I'll just go ahead and hand out the exams. Do your best!"
    
    n "She goes around the room, dropping off a packet of papers on everyone's desk."
    n "Her tail brushed against your hand as she passed by you. So soft~ You just wanna reach out and stroke her fur, but you remember that'd be considered sexual harassment and get you canceled."
    n "You'll just have to take this boring exam instead."
    n "You pick up your pencil and get to work."
    
    scene bg classroom with fade
    
    n "Not even an hour goes by and you're finished. You didn't think it was so bad."
    n "Half the class had already finished and left by the time you stand up and hand yours in."
    n "You've still got plenty of time before your next exam but you're too burnt out to study."
    n "What to do...?"
    
    scene bg roof autumn day
    
    show box with Dissolve(.2):
        ypos 0
    
    n "You felt compelled to come up here for some reason."
    n "Maybe it's because the breeze is comforting."
    n "Your worries melt away as you watch students walking to their next class several stories below you."
    n "You'll be among them in a few minutes, but for now this is your secret spot where you can just get away."
    n "Well, it's someone else's secret spot too."
    
    show margaret happy at center with dissolve:
        ypos y_margaret
    
    margaret @ say "Oh? Looks like I'm late to the party~"
    
    player "Or maybe I'm just early."
    
    margaret @ say "How'd the exam go? Did I make it too easy?"
    
    player "I feel like it was pretty typical."
    
    margaret @ say "Good, I'm glad you didn't struggle with it too much!"
    
    if ch4EllenSnack == True:
        n "She unfurls the paper bag you left her and pulls out the cinnamon roll."
        
        margaret @ say "Am I right to assume this was your doing?"
        
        player "Guilty as charged, ma'am."
        
        margaret @ say "So you're bribing me? How sweet of you~"
        
        menu:
            "It's not a bribe":
                player "It's not a bribe!"
                
                margaret @ say "So you just did it out of love for your literature professor then, huh?"
                
                player "Something like that..."
                player "I just knew you liked them so I got you one."
                
                margaret @ say "We're not supposed to accept gifts from students but I'll make an exception. I always do~"
                
            "It's totally a bribe":
                player "Is it that obvious?"
                
                margaret @ say "People don't just give things away with no expectation of a favor in return."
                margaret @ say "Lucky for you I'm willing to bump your grade up for sweet gestures like this. Just a bit!"
                
        n "Miss Ellen takes a bite out of the treat. Her tail starts to wag immediately."
        
        if ellenPoints > 3:
            n "She tears a piece off and holds it out for you."
            
            margaret @ say "Want a bite?"
            
            player "Sure."
            
            n "You take the chunk of sweet glazed cinnamon roll and devour it in one go."
            n "You didn't realize how hungry that exam had made you."
            
            
        margaret @ say "Y'know, this ain't the most expensive gift a student has given me, but it's up there with the sweetest!"
        
        player "Oh? Do students buy you things often?"
        
        margaret @ say "A little more than you'd expect."
        margaret @ say "I'm just a basic literature professor so I don't get free cars and vacation homes like some in the business and political science departments."
        margaret @ say "It's usually small things like purses, shoes, phones..."
        margaret @ say "I did have one student who was unusual. He wasn't even doing poorly in the class, he just... enjoyed giving me cash."
        margaret @ say "I think he ended up giving me over ten thousand dollars over the semester."
        
        player "Without you even asking? I don't ever want to hear about male privelige ever again."
        
        margaret @ say "Hehehe a few thousand doesn't make up for the challenges I've faced."
        
        player "And here all I can offer are cinnamon rolls."
        
        margaret @ say "You don't have to do much to pass my class. Just listening to me rant is enough, either in the classroom or up here."
        margaret @ say "Preferably up here so I don't have to pay for therapy."
        
        player "I'll do what I can."
                
        
        
    
        
    else:
        n "She pulls a cigarette and a lighter from her pocket and lights one up."
    
        margaret @ say "Usually only smoke when I have a bad day but this is to reward myself for making it through the week."
        
        player "Midterms rough of you too?"
        
        margaret @ say "I have to come up with all new questions and rubrics each semester."
        margaret @ say "I can't reuse the old ones because students were just buying them from upperclassmen."
        
        player "Wow. And here I thought I went to a decent university."
        
        margaret @ say "If only you knew how rampant cheating was. Not just here but everywhere."
        
        if ellenPoints > 3:
            n "Ms. Ellen pulls the cigarette box out and shakes it around."
            
            margaret @ say "Huh, only one left."
            margaret @ say "You want it?"
            
            menu:
                "Hell yeah":
                    $ ellenPoints += 1
                    
                    player "Smoking ciggies with my professor on the rooftop during school hours? How could I resist!"
                    
                    n "You take the cig and put it between your lips. Flicking her lighter open, Ms. Ellen ignites it for you."
                    
                    player "*Cough*"
                    
                    margaret @ say "Heh, you ever smoked one before? I forgot the raised the age where you can buy 'em."
                    
                    player "No but I wanted to look cool."
                    
                    margaret @ say "Cool? Not so much."
                    margaret @ say "Cute is maybe the more appropriate word."
                    
                    player "I'll take it."
                    
                "Nah":
                    player "Nah, smoking is bad for you."
                    
                    margaret @ say "Only in excess! But I'm not gonna pressure you into it, I'm too old for that."
                    
                    player "Did somebody pressure you into trying it?"
                    
                    margaret @ say "Only the struggles of life nudged me towards it."
                    margaret @ say "I used to be so against it until I finally tried one and then it became a routine."
                    margaret @ say "Gotta have something to look forward to and these smoke breaks scratch that itch!"
                    
                    player "I don't think I'm at that point in my life yet."
                    
                    margaret @ say "Suit yourself, that just leaves more for me~"
                    
        margaret @ say "Y'know I've caught a few of your classmates cheating already. Some were even bold enough to look at their phones during the exam today thinking I wouldn't notice!"
        
        player "Are you gonna fail them?"
        
        margaret @ say "Mmmmh probably not. I dunno. If I feel like it I might."
        margaret @ say "Writing up a report for academic dishonesty is suuuuuch a hassle."
        margaret @ say "I'll probably let it slide unless those students piss me off."
        
        player "I'll try and stay on your good side then."
        
        margaret @ say "Just listening to me ramble on about things up here has put you in a pretty good spot, [name]."
        margaret @ say "You could cheat all you want and I won't give it a second thought."
        
        player "So I didn't even have to put all that effort into that exam?"
        
        margaret @ say "You *could* have just turned in a blank sheet of paper, but I actually enjoy reading your thoughts on the class material!"
        
        if literatureSkill < 5:
            margaret @ say "Even if they're a bit... underdeveloped."
        
        margaret @ say "It's a lot more interesting than grading 80 other strangers' responses."
        
        player "Glad I can provide some entertainment value."
        
    if ellenPoints > 4:
        n "Ms. Ellen looks like she's about to say something but hesitates."
        
        if ch4EllenSnack == True:
            n "She finishes her cinnamon roll then blurts it out."
        else:
            n "She takes a drag from her cigarette then blurts it out."
    
        margaret @ say "Hey, you got any plans for next week?"
        
        player "Sorta? Not really? Why?"
        
        margaret @ say "I was just wondering... how do I put this..."
        margaret @ say "I'm not supposed to just *invite* a student over to my place..."
        
        menu:
            "Invite yourself":
                player "What if I were to ask to come over? Maybe I'm just curious to see how a literature professor decorates her home."
                player "Probably lots of books, aren't there?"
                
                margaret @ say "Yes! Tons of them! Would you like to come over and see? I can show you my favorites! You might find one you like~"
                
                player "I'd love to!"
                
                margaret @ say "Perfect! Let me write down my address for you and we can meet up sometime next week. Sound good?"
                
                n "Ms. Ellen can't stop her tail from rapidly wagging as she writes on a scrap piece of paper and hands it to you."
                
                player "Nice, I can't wait!"
                
                margaret @ say "Same!"
                
                n "It feels kinda off to arrange a visit to your teacher's house. But hey you're an adult, you can do whatever you want. It's not like it's illegal to swing by an older woman's house and hang out."
            "That would be weird":
                player "Uhhhh yeah that would be kinda weird."
                
                margaret @ say "Haha... it would, wouldn't it? Forget I mentioned it!"
                margaret @ say "We've been up here a while, don't you have somewhere to be?"
        
        
    n "You check the time on your phone. Just a few minutes left until your next midterm."
        
    player "Oop, it was nice chatting up here with you but I gotta go take my exam in French now."
    
    margaret @ say "Oh? Bonne chance et à bientôt~"
    
    player "You can speak French??"
    
    margaret @ say "Just a bit~ I'm friends with the professor."
    
    player "You know Mrs. Celestine?"
    
    margaret @ say "Yup! We hang out from time to time. Now get going before you're late!"
    
    player "Alright, see you later!"
    
    margaret @ say "Au revoir, [name]!"
    
    n "She waves you off as you hoist your bag up and head down the stairway on to your next exam."
    
    scene bg classroom with fade
    
    n "You show up with only a few minutes to spare. Other students are flipping through their notes and books, making last minute preparations while Claire stares off into space, humming a tune to herself."
    
    claire @ say "[name]! You're 87 seconds late compared to your average arrival time! That's like 1 and a half standard deviations from the norm!"
    
    if smokedCig1:
        claire @ say "Why do you smell like cigarettes? Do you smoke?"
    else:
        claire @ say "Were you talking with someone? You smell like dog."
        
    player "I was just chatting with my literature professor after my exam."
    
    claire @ say "Oh! Think you did well?"
    
    player "Well enough."
    
    
    if claireFrenchStudy1 == True and claireFrenchStudy2 == True:
        claire @ say "I'm sure you'll make a hundred on this test after all the studying we did together~"
        
        player "We didn't really do a whole lot of actual studying, did we?"
        
        claire @ say "It was more like... immersive learning ksksksks~"
    elif claireFrenchStudy1 == True:
        claire @ say "I'm sure you'll do pretty well on this test! After all, we did study together~"
        
        player "I don't think I learned much from that study session..."
        
        claire @ say "I guess we'll have to study together more often!"
    else:
        claire @ say "I hope you're prepared for this test!"
        
        player "I guess we'll find out. I'm sure you'll have no problem with it."
        
        claire @ say "If ya want, you can copy my answers~"
        
        menu:
            "Do it":
                $ claireFrenchCheat1 = True
                
                player "If I get stuck I'll take a peek."
                
                claire @ say "Ksksksks feel free to peek as much as you want~"
            "Don't do it":
                player "Nah, I'll be fine."
                
                claire @ say "If you insist! I'm sure you'll do fine!"
        
    celestine @ say "Bonjour class! Please clear your desks and we'll begin the exam!"
    
    n "Mrs. Celestine passes out the paper packets and you get to work on yours."
    
    if frenchSkill < 4:
        n "Damn, some of these are actually kind of hard."
        
        if claireFrenchCheat1 == True:
            n "You might have to look at Claire's answers after all."
            n "She can obviously work through these much faster than you can but she's been intentionally waiting for you to finish each page before turning hers over."
            n "You quickly copy her answers, trying to rearrange the wording as best you can to obscure the fact that you've cheated your way through these questions."
        else:
            n "Maybe you should have taken Claire up on her offer after all."
            n "She's working through these too fast and is already 2 pages ahead of you."
            n "Guess you're on your own."
        
    else:
        n "You diligently go through them, pacing yourself."
        
        if claireFrenchCheat1 == True:
            n "These questions aren't actually that hard. No need to cheat off Claire after all."
            
        else:
            n "These questions aren't actually that hard."

        if claireFrenchStudy1 == True and claireFrenchStudy2 == True:
            n "Those extra study sessions with her paid off after all."
        elif claireFrenchStudy1 == True:
            n "That study session with her paid off after all."
    
    n "Before you know it, you reach the end of the exam. You give your answers a quick final look over before turning it in."
    
    celestine @ say "Merci! Have a nice autumn break, [name]!"
    
    n "Outside you find Claire waiting for you."
    
    claire @ say "So? How'd ya feel about that test?"
    
    if claireFrenchCheat1 == True:
        claire @ say "I saw ya copying my answers so you're gonna ace it~"
        
        player "Heh yeah thanks for letting me do that."
        
        claire @ say "No problem! You can cheat on me anytime! On tests I mean."
        
        n "Her tone suddenly becomes deadly serious."
        
        claire @ say "If we're dating and you cheat on me with another girl I'll murder you both."

        n "She looms over you, putting off an aura that's both protective and possessive."
        n "Before you can piss yourself in fear, Ava comes swooping in and Claire returns to her usual bubbly self."
    
    
    else:
        if frenchSkill < 4:
            player "It was kinda hard for me..."
            
            claire @ say "Really? You should have taken me up on my offers to study together!"
            
            claire @ say "Really? I guess we need to study together more often~"
        
        else:
            player "It wasn't so bad."
            
            if claireFrenchStudy1 == True and ClaireFrenchStudy2 == True:
                player "No doubt thanks to your help with those study sessions."
                
                claire @ say "Glad to be of service~"
                
            elif claireFrenchStudy1 == True:
                player "No doubt thanks to your help with that study session."
                
                claire @ say "Glad to be of service~"
        
        if avaPoints > 5:
            n "Ava comes swooping in at high speed. She's heading right at you!"
            
            ava @ say "[name]! Coming in hot!!"
            
            n "Instinct kicks in and you hold your arms out ready to catch her."
            n "Once she flies into your grasp you spin in place to slow down her momentum."
            
            player "Gotchya!"
            
            claire @ say "Nice Chad spin~"
            
            ava @ say "Whew, thanks [name]! My mind was still stuck on that last exam and I didn't hit the breaks in time."
            
            player "No problem. Better you crash into me than the ground."
            
            claire @ say "She coulda crashed into me too. I'm a bigger target anyway!"
            
            ava @ say "Maybe I picked my target deliberately~"
            
            claire @ say "Ksksksks you know you can let go of him now, right?"
            
            ava @ say "R-right haha..."
            
            n "Ava pulls her wings back and brushes her feathers into place."
            
            claire @ say "Aww look at [name], he's blushing!"
            
            player "I am not!"
            
            claire @ say "You are too!"
            claire @ say "I wonder if you'd blush if I swooped down into your arms like that~"
            
            ava @ say "You'd crush him to death if you tried!"
            
            menu:
                "Worth it":
                    $ avaPoints -=1
                    $ clairePoints +=1
                    
                    player "It'd be worth it."
                    
                    claire @ say "See, he gets it."
                    claire @ say "I'll spare ya this time but it's the thought that counts!"
            
                "Rather get hit by a truck":
                    $ clairePoints -=1
                    
                    player "I'd rather get hit by a truck. At least then my death would be quick and painless."
            
                    claire @ say "Aww..."
            
        else:
            n "Ava comes swooping in at high speed but Claire is there to catch her and spin her around."
            
            claire @ say "Whoa! Someone's happy to see us ksksksksk!"
            
            player "Nice save."
            
            ava @ say "Sorry about that! My mind was still stuck on that last exam!"
            ava @ say "I hope I got that last question right..."
            
            n "Claire sets Ava down and pats her feathers back into place."
            
    player "You two still have one more exam today, right? I just got finished with my last one."
    
    ava @ say "Yup! I can't stay long 'cause I gotta rush to my next one."
    
    claire @ say "Yeah, we only got a few minutes left!"
    
    player "Good luck you two! I'm gonna head back to my dorm and get ready for tomorrow's exams."
        
    ava @ say "See ya! We'll meet up before the autumn break!"
    
    claire @ say "Yeah let's hang all hang out tomorrow!"
    
    player "Sounds good to me. Later!"
    
    scene bg codadorm with fade
    
    n "You're kinda burnt out from today's exams but you're only halfway through."
    n "You muster up the energy to study a bit for stats and history but wind up falling asleep early."
        
        
    # friday
    
    n "The following day..."
    
    n "Just gotta get through two more exams and then you're home free."
    
    if hasRosesNotes == True:
        n "Reading through Rose's notes is sure to give you a massive leg up on this exam."
        
        player "Thanks again for the notes the other day."
        
        rose @ say "Whatever. Don't mention it."
        
        if rosePoints > 3:
            n "Ooh nice she's wearing the same perfume she was wearing at the library the other day."
            n "Even the page she gave you had the faint scent of goth bitch on it."
            n "You couldn't resist giving it a sniff or two while studying last night."
        
    
    else:
        if historySkill > 3:
            n "You should do reasonably well on this one as long as there's no curveball questions."
            
        else:
            n "You could have spent more time studying this topic. Hopefully the questions aren't too hard."
            
        n "Now you're imagining Rose tutoring you. She'd bite you every time you got a question wrong."
        
    rothbauer @ say "Good day, students! All you'll need for this exam is a pencil, so go ahead and clear your desks and let's get started!"
    
    n "The test is a blur of dynasties and eras, those who ruled and influenced early civilizations, and the lasting impacts of their actions. You're left dazed by the end of it."
    n "Once you're finished, you turn it in and hurry to your next exam without much time to spare."
        
    scene bg lecturehall with fade
    
    n "Gunner's already here and writing equations on his paws with a pen."
    n "There's not enough space for all of them."
    
    if statsSkill > 3:
        n "You feel like you'll be fine but he might not do so hot..."
        
        gunner @ say "It's so over. We're cooked."
        
        player "You might be cooked but I think I'll be okay."
        
        gunner @ say "For real? Lemme peep your answers then."
        
        menu:
            "Let him":
                $ letGunnerCheatStats = True
                
                player "Fine, just don't get me in trouble."
                
                gunner @ say "Thanks bro you're the best."
                
                player "I'm not liable for giving bad answers either. I'm not gonna be making 100\% on this."
                
                gunner @ say "It's all good, you'll do better than I would."
            "Don't let him":
                player "Fuck that, you're gonna get me in trouble."
                
                gunner @ say "No it's cool, I'll bail you out. I'm rich, remember?"
                
                player "How could I ever forget?"
                player "Why don't you just bribe Mrs. Herschel?"
                
                gunner @ say "That's what I do with all my teachers but she's a bitch and won't take my money."
                
                player "Oh the horror."
                    
    else:
        n "You don't feel super confident about this one either."
        
        gunner @ say "It's so over. We're cooked."
        
        player "Just a bit."
        
        gunner @ say "Mrs. Herschel is notorious for giving extremely hard tests. Fuck this bitch."
        
    herschel @ say "Good morning class! You know what day it is! Clear your desks and let the fun begin!"
    
    gunner @ say "See this is her idea of fun. She's a sadist!"
    
    n "When you get your test, your faced with a wall of verbose word problems and mathematical formulas including some symbols you've never even seen before."
    n "This is gonna be tougher than you thought."
    n "You focus your concentration on recalling every bit of statistical knowledge you've studied over the semester."
    
    if letGunnerCheatStats == True:
        n "You give enough space so Gunner can peek at your answers and wait for him to finish before turning the page."
        n "God damn he's so slow. He better hurry up or you're leaving him behind."
        
    else:
        n "Gunner tries to peek at your answers but you're moving too fast for him. You're already on the next page."
        n "Too bad buddy, if you don't hurry up you won't even finish this exam in time."
        
    n "When Mrs. Herschel calls for everyone to put their pencils down, Gunner spends a solid extra minute writing answers while the tests are collected."
    
    herschel @ say "That's enough, Gunner. I've given you plenty of extra time. If you want more, tell the department heads that you have a disability."
    
    gunner @ say "Like tell them I'm retarded?"
    
    herschel @ say "*Sigh*"
    herschel @ say "They might fall for it."
        
    player "Snrk!"
    
    gunner @ say "Don't you 'snrk!'"
    gunner @ say "I'll just pay them off."
    
    herschel @ say "Money only gets you so far, young man."
    
    hide herschel with dissolve
    
    menu:
        "Encourage him":
            $ gunnerPoints += 1
            
            player "Come on dude, the semester's only halfway over. You can still pull this together."
            
            n "Gunner takes a deep breath and composes himself."
            
            gunner "You're right, this is just a minor setback. I only need to improve enough to get a D."
            
            n "You start to crack up at the obvious joke."
            
            gunner "Shut up, you know what I meant."
            
            
        "Taunt him":
            player "LMFAOOOO get dunked on richboiii!"
            
            gunner @ say "I'm gonna pay you $100 to shut the fuck up."
            
            player "Deal!"
            
            n "Gunner slides a crisp hundo your way and you gladly take it. Easiest money you've ever made."
            
        
    gunner @ say "Gotta run but we'll meet up later for lunch, k?"
    gunner @ say "I wanna get the whole squad together one last time before autumn break."
    gunner @ say "We'll meet up at that Thai place. No stupid contests this time."
    
    scene bg black with fade
    
    n "You return to your dorm and unwind for a bit until Gunner texts you saying everyone's ready."
    
    scene bg town
    
    n "When you arrive, Claire waves you over to the table your friends are sitting at."
    
    claire @ say "There he is!!"
    
    gunner @ say "[name]! You made it!"
    
    ava @ say "Did you get lost on the way here?"
    
    rori @ say "Yeah man, we've been waiting for you for a while."
    
    n "Truth be told maybe you did get a little lost. You kinda spaced out and don't even remember how you got here."
    
    player "Sorry guys, I'll try and be faster next time."
    
    claire @ say "It's alright! We were just talking about our plans for the autumn break now that midterms are outta the way!"
    
    player "Plans? Oh right, I didn't make any."
    
    ava @ say "You mean you're not going back home?"
    
    n "You shrug."
    
    player "No? Why would I?"
    
    n "Your friends look to each other uneasily."
    
    ava @ say "I've got my bags packed and ready to go already."
    
    claire @ say "If I'd known you'd be here alone I wouldn't have made plans to visit home!"
    
    gunner @ say "My flight home leaves tonight. What are you gonna do here for a whole week?"
    
    if mishkaMidtermWeekendHangout == True:
        player "I made some plans with Mishka."
        
        claire @ say "Huh? Are you two going on a date?!"
        
        player "No no we're just gonna hang out!"
        
        rori @ say "Y'know I'm staying here too. We can hang out and chill whenever!"
    else:
        player "Same thing I always do, whatever I feel like."
    
        rori @ say "Don't worry, I'm staying too! We can hang out and chill whenever."
    
    menu:
        "That sounds nice":
            $ roriPoints += 1
            
            player "That sounds nice. We can play vidya and watch anime :3"
            
            rori @ say "Ba-a-a-a-a-ah~"
            rori @ say "I'd love that :3"
            
            gunner @ say "Our dorm better not smell like gay sex when I get back."
            
            menu:
                "It won't":
                    player "It won't... probably."
                    
                    claire @ say "Why do all the hot ones end up being gay?"
                    
                    ava @ say "You got it backwards, all the gay ones end up being hot."
                    
                    
                "We'll take it to my dorm":
                    $ hittingOnRori = True
                    
                    player "Guess you'll have to come to my dorm, Rori."
                    
                    rori @ say "OwO"
                    rori @ say "W-what do you mean? We're not really gonna... are we?"
                    
                    player "Hahaha no of course not... unless..?"
            
        "We'll see":
            player "We'll see. I might just wanna lie in bed all week."
            
            rori @ say "That works too. Lemme know if you feel like doing anything. I'll just be in my dorm compiling kernels and debugging bootloaders."
            rori @ say "Might install ReiserFS before it gets deprecated just to see what it's all about."
            
            gunner @ say "So glad I'm not into that nerd shit."
            
            claire @ say "Hey, nerd shit can be sexy!"
            claire @ say "Tell me more about obscure file systems made by wife-murderers, Rori~"
    
            ava @ say "Wife-murderers you say?"
            ava @ say "Now I'm interested~"
    
        n "The waitress comes to take your orders, putting a pause on your conversation."
        n "The rest of your afternoon is spend discussing everyone's plans upon returning home."
        n "After lunch you all walk back to campus to say goodbye before parting ways."
        
        claire @ say "I'm gonna miss you guys!!!"
        
        ava @ say "Same! I hope you all have a great autumn break!"
        
        gunner @ say "Hold down the fort, Rori. If anyone breaks in, there's a 1911 under my pillow you can use."
        
        rori @ say "Let me guess, it's made of solid gold?"
        
        gunner @ say "They make them out of anything else?"
        
        player "It's kinda weird, it feels like we're saying farewell forever."
        
        claire @ say "Awww we'll be back before you know it!"
        
        ava @ say "Yeah and we can still text each other!"
        
        player "I mean I've been with you guys since this semester started. This is the first time we'll be apart since we met."
        player "It's like going back to before I started college, back when I was on my own."
        player "At least Rori will still be here."
        
        rori @ say "I know how you feel. You know you can text me if you ever get lonely and we can hang out!"
        
        claire @ say "Oh my god I would ship you two so hard if I wasn't gonna take [name] for myself."
        
        if avaCommitted:
            ava @ say "Saaame~"
            
        gunner @ say "Rori, *please* take [name] so I don't have to compete with him for Ava. Thank you."
        
        rori @ say "Guys..."
        
        claire @ say "We're just teasin' ya~"
        claire @ say "But you two *would* make a cute couple ksksksksk~"
        
        ava @ say "Come on, I think we've tortured him enough. We can't stick around forever, we've all got our flights to catch!"
        ava @ say "I'm glad we got to see each other one last time before the break!"
        
        gunner @ say "For sure. We'll have to catch up once we're back!"
        
        claire @ say "Safe travels you two!"
        
        gunner @ say "Call me when you get home!"
        
        ava @ say "I will~"
        
        n "After an extremely protracted goodbye from everyone, your friends leave one by one until it's just you and Rori left."
        
        rori @ say "Whew, that was exhausting."
        
        player "I thought they'd never leave."
        
        if hittingOnRori == True:
            rori @ say "...Were you serious about doing stuff at your dorm?"
            
            menu:
                "Yeah, kinda":
                    player "The door's always open for ya~"
                    
                    if roriPoints > 4:                    
                        rori @ say "I uh..."
                        rori @ say "I might come in one night >w>"
                    else:
                        rori @ say "I'll uh... keep that in mind UwU"
                "Maybe? I don't know":
                    player "Yes? No? Maybe. I don't know."
                    
                    if roriPoints > 4:
                        rori @ say "Well uh... if you wanna... Just let me know haha?"
                        
                    else:
                        rori @ say "N-nevermind. Forget I said anything."
                "Nooooo haha":
                    player "Noooo haha I was just joking around."
                    player "I wouldn't wanna have hot and sweaty sex with an adorable sheep boy after missing out on a new episode of Kitsune Chronicles because we were too busy kissing."
                    player "That would be gay."
                    
                    rori @ say "You're right, it would be."
        
        n "Rori looks past you with a face of utter horror and dread."
        
        ###alt intro where you get rory mixed up with rori and think he's trooned out. 50/50 chance?
        
        rori @ say "Oh my god is that...?"
    
        rory @ say "Heyyyyyy lil bro~"
        
        n "She looks over you from top to bottom. You can't tell if she's intrigued or disgusted."
        
        rory @ say "Is this your boyfriend? Just kidding, you could never get a boyfriend!"
        
        rori @ say "What do you want? Don't you have some butterflies to be pulling the wings off of?"
        
        rory @ say "Oh no, I stopped doing that ages ago. I aim for bigger targets now~"
        
        menu:
            "Who the hell is this bitch?":
                player "Rori you wanna tell me who this bitch is?"
                
                rori @ say "She-"
                
                rory @ say "This bitch right here-"
                
                n "She points to Rori."
                
                rory @ say "- that's my little brother unfortunately. We're twins but I'm older by a few minutes~ Like everything in life he came in last place."
                
                player "I didn't ask you."
                
                rory @ say "Didn't you? You said Rory right? With a \'y\'"
                
                player "You're both named Rori?"
                player "Are you fucking serious?"
                
                rory @ say "Pfffft hahahah I know it's confusing, right? At home I'm usually referred to as \"the better Rory~\""
                
                rori @ say "More like cunt Rory!"
                
                rory @ say "You're just jealous that I have one~"
                
                n "You're sensing some sibling rivalry going on here."
                
                rory @ say "And you are?"
                
                player "[name]. Can't say it's been a pleasure to meet you."
            "I love this bitch already":
                player "Damn this bitch seems kinda evil."
                player "I'm into that."
                
                rori @ say "Don't be. She's just a psychopath."
                
                rory @ say "How rude!"
                rory @ say "Well if my dear brother won't introduce me to his friend, I guess I'll have to do it."
                rory @ say "I'm Rory. With a \'y~\' I'm Rori's twin sister, older by just a couple minutes."
                
                n "She holds out her hoof and you reach out to shake it."
                
                rori @ say "[name] wait!!!"
                
                n "Too late."
                n "Rory grabs hold of your soft fleshy human hand and absolutely *crushes* it."
                n "You pull back, yelping in pain."
                
                player "Ow! What the fuck!"
                
                rory @ say "Oops hehehe sorry~"
                rory @ say "I forget how fragile others can be."
                
                n "One of your fingers is sticking out at an unnatural angle. You can neither feel it nor move it."
                
                player "I think you broke something."
                
                rory @ say "No worries, I can fix it!"
                
                n "Before you have time to react, Rory grabs hold of your finger and moves it back into place."
                
                player "Aaaaaaagh!!!"
                
                rory @ say "Good as new!"
                
                n "Through the excruciating pain, you find that you can in fact move your finger again."
                
                rori @ say "I tried to warn you..."
                rori @ say "This is how she's always been. Imagine living with her."
                
                rory @ say "Yes, imagine living with someone as perfect as *me~*"
                rory @ say "You should be honored to have had the privilige, little Rori~"
                
            "Introduce yourself politely":
                player "I don't believe we've met before. I'm [name]."
                
                rory @ say "Nice to meet me, isn't it? I'm Rory -- with a \"y~\""
                
                n "She does a little curtsy."
                
                rory @ say "So nice of you to wrangle my little brother Rori in my absence!"
                
                if roriPoints > 4:
                    player "Rori's nice, I like him."
                else:
                    player "He can be a handful sometimes."
                
                rory @ say "I'm surprised they even admitted him to Harmonia. They must have seen his name and got it mixed up with mine~"
                
                rori @ say "I'm surprised they haven't admitted you to a mental asylum!"
                
                n "There is legitimate anger in Rori's voice."
                
                player "What's your problem? She's your sister isn't she?"
                
                rori @ say "She's a psychopath! Don't be fooled!"
                
                rory @ say "Don't mind him, he's just jealous!"
                
                
                
                #rori @ say "Shut up, I deserve to be here more than you!"
                #
                #rory @ say "Do you?"
                #rory @ say "I'm clearly the better candidate!"
                
        
        rory @ say "I'm basically exactly like him but better in every way!"
        rory @ say "While he's busy downloading kernels, I'm uploading patches for them~"
        rory @ say "I can run circles around him in his favorite games~ He used to cry when I'd perfect KO him in Tekken 10 times in a row!"
        rory @ say "Now he just ragequits!"
        rory @ say "*And* I can climb faster than him with one hoof tied behind my back! We tested this once and I humiliated him~"
        
        if roriPoints > 4:
            player "My Rori is kind and sweet."
            
            rori @ say "Y-your Rori?"
            
            rory @ say "I see, you're one of *those* types."
            #rory @ say "I can be sweeter than him... I just choose not to~"
            rory @ say "Don't make the mistake of conflating passiveness with kindness."
            rory @ say "Rori's personality is a result of him being submissive. He may appear to be nice on the surface, but he's really just desperate for affection."
            rory @ say "But even then, I bet I'm sweeter~"
        else:
            player "You can't be better at everything. Rori has to have something he beats you at."
            
            rory @ say "That's the sad part, he really doesn't!"
            rory @ say "I'm just a straight upgrade from him."
            rory @ say "Literally~"
            
            #rory @ say "The only reason to choose him over me is for his dick, which isn't even that big."
            
            #player "H-how would you know?"
            
            #rory @ say "Doesn't matter. I could turn any gay man straight anyway~"
            
            #rory @ say "Why settle for him when you could have me instead?"
        
        #rory @ say "I haven't met anyone worthy of me yet. I'm almost afraid I never will."
        
        
        rori @ say "What do you want, Rory? Did you come over here just to torture me?"
                
        rory @ say "I just wanted to say goodbye my little bro before I go back home for autumn break, that's all!"
        rory @ say "I know it must have been rough when Ma and Pa denied your request to visit."
        rory @ say "But don't worry, we'll enjoy the time I'm home without you!"
        
        rori @ say "Oh go to hell."
        
        rory @ say "Not right now~"
        rory @ say "I'll catch up with you later, I've got a flight to catch!"
        rory @ say "And it was really nice meeting your boyfriend. Enjoy him while you can, because I might decide to make him mine when I come back! Hahahaha!"
        
        n "She shoulder checks Rori so hard he falls to the ground as she walks away."
        
        menu:
            "Help him up":
                n "You hold out your hand to grab onto and hoist him back up onto his feet."
                
            "Let him get up":
                n "He doesn't need your pity. Helping him will just bruise his ego even more."
                n "He picks himself up and brushes the leaves and dirt off his jacket."
        
        rori @ say "Grrrr that bitch..."
        
        player "And you lived with her for years? That must have been brutal."
        
        rori @ say "I don't care if she's my sister, I genuinely hate her."
        rori @ say "I don't even care that she's better at everything, the world would be a better place without her in it."
        
        player "Geez man. At least she's going away for the week."
        
        rori @ say "Yeah... Luckily I haven't run into her much here. But now that she's seen me with friends she'll stop at nothing to sabotage me."
        rori @ say "She can't stand seeing me happy. It's the one thing that gets under her skin."
        
        player "...You wanna talk about it?"
        
        rori @ say "I dunno. Not right now. I wanna be alone."
        
        player "Alright. I'll see you around man."
        
        rori @ say "Yeah. And thanks for being here for me."
        
        player "Anytime. That's what bros are for."
        
        
    
#saturday
    n "It's officially the first day of your autumn break. No more worries until school starts back up again."
    n "You can enjoy life at your own pace and do whatever you want."
    
    if mishkaMidtermWeekendHangout == true:
        n "You agreed to meet up with Mishka at the cafe today. She said it would be closed for the duration of the break but that it would be a good spot to hang out."
                
        call roseInHallways
        
        jump writingWithMishka
        
    call roseInHallways
    
    jump ch4GoWithRori
        

label roseInHallways:
    n "On your way out, you nearly trip over some short gremlin-type creature."
    n "Oh wait, that's just Rose."
    
    rose @ say "Watch it, punk!"
    
    player "Rose?? What are you doing in my dorm building?"
    
    rose @ say "*Your* dorm building?! If it's anyone's, it's mine!"
    
    player "Wait, you've been living here this whole time?"
    
    rose @ say "...Yes."
    
    player "Aren't you rich? Don't you have a mansion you could be living in instead?"
    
    rose @ say "*Sigh* I don't know why I'm even entertaining you but yes normally I would be residing in the family mansion."
    rose @ say "But granddad insists that I spend some time in the dorms to \"meet people and make friends\" whatever that means."
    
    player "I'm people."
    
    rose @ say "No, you're not. You're barely even sapient."
    
    menu:
        "About this mansion...":
            player "About this mansion... I think I could get you back in there."
            
            rose @ say "I doubt it but let me hear your stupid idea. I could use a laugh."
            
            player "Your grandpa just wants to see you with a friend then he'll let you back in, right?"
            player "I could be your rental friend!"
            
            rose @ say "I think I just puked a little."
            rose @ say "Just moving back into the mansion wouldn't be worth spending a second with a h*man."
            rose @ say "...But he's also holding my inheritance hostage."
            rose @ say "And I don't know which is worse, being in the presence of you or being poor."
            
            player "It's just pretend, you don't have to commit to it."
            player "But the more convincing it looks the less time we'll have to spend together."
            
            rose @ say "Ugh, what have I done to deserve such a fate?"
            
            player "Gee, I wonder."
            player "So are you down?"
            
            rose @ say "What's the catch?"
            
            player "I wanna sleep over at the mansion."
            
            rose @ say "Hell no!"
            
            player "Just for one night! We can even sleep in different rooms!"
            
            if rosePoints > 3:
                rose @ say "I hate this and I hate you but if it will make my filthy human-sympathizer granddad happy then..."
                rose @ say "Fine."
                rose @ say "We'll \"\"\"hang out\"\"\" on occasion within view of my grandfather. You'll stand no closer than 5 feet away from me and under no circumstances will you so much as lay a finger on me."
                rose @ say "Once I'm back in my rightful home, we cease all contact forever and ideally you kill yourself."
                
                player "Deal. Except for the killing myself part. You gotta offer up something good for that."
                
                if rosePoints > 5:
                
                    rose @ say "What, like a pat on the back?"
                    
                    player "I was thinking more like..."
                    
                    menu:
                        "A date":
                            player "A date?"
                            
                            rose @ say "Absolutely not."
                            
                            player "For real, I'll take you out and if you decline a second date I'll kill myself on the spot."
                            
                            rose @ say "Not happening."
                            
                            player "Alright alright, we'll just be \"friends\" til you get your mansion."
                            
                            rose @ say "I'd say it was a pleasure doing business with you, but it really wasn't. I'm only doing this for my grandfather."
                            rose @ say "And so I can get out of these dorms and away from the disgusting troll that inhabits them!"
                            
                            player "Yeah whatever. See you around, \"friend~\""
                            
                            rose @ say "Weirdo creep."
                        "A kiss":
                            player "A kiss?"
                            
                            rose @ say "Not in stock."
                            
                            player "Just one little smooch and then I'm dead. A kiss of death."
                            
                            rose @ say "You can kiss the barrel of a shotgun."
                            
                            player "Alright alright, we'll just be \"friends\" til you get your mansion."
                            
                            rose @ say "I'd say it was a pleasure doing business with you, but it really wasn't. I'm only doing this for my grandfather."
                            rose @ say "And so I can get out of these dorms and away from the disgusting troll that inhabits them!"
                            
                            player "Yeah whatever. See you around, \"friend~\""
                            
                            rose @ say "Weirdo creep."
                        "A pawjob" if rosePoints > 6:
                            n "Yeah why not, you feel confident enough to say this."
                            
                            player "Gimme a pawjob and I'll blow my brains out after blowing my load."
                            
                            rose @ say "The only paws you'll be getting will be me knocking your lights out."
                            
                            n "It seems your confidence was misplaced..."
                            
                            player "Alright alright, we'll just be \"friends\" til you get your mansion."
                            
                            rose @ say "I'd say it was a pleasure doing business with you, but it really wasn't. I'm only doing this for my grandfather."
                            rose @ say "And so I can get out of these dorms and away from the disgusting troll that inhabits them!"
                            
                            player "Yeah whatever. See you around, \"friend~\""
                            
                            rose @ say "Weirdo creep."
                        "Your panties" if avaPantsu == True or clairePantsu == True:
                            player "Ok hear me out..."
                            
                            rose @ say "Uh huh?"
                            
                            player "I've been starting a collection..."
                            
                            rose @ say "Riiiight."
                            
                            player "Of women's panties."
                            
                            rose @ say "Oh go fuck yourself."
                            
                            player "I know right? It all started from this stupid frat boy panty raid thing."
                            player "And I'd kill to have yours."
                            player "Kill myself even."
                            
                            rose @ say "Aside from how disgusting it is to ask that of anyone, let alone someone who hates your guts-"
                            rose @ say "Do you have any idea how much these cost?!"
                            
                            player "It's just underwear, it can't be that expensive."
                            
                            rose @ say "I don't wear *anything* that costs less than $850."
                            rose @ say "Not even my socks."
                            
                            player "Is that per sock or do you count them as a pair?"
                            
                            rose @ say "*Sigh*"
                            rose @ say "You know what, fine. It's for the greater good."
                            
                            player "H-holy shit...!"
                            
                            n "Right then and there Rose bends over and reaches under her skirt. She steps out of a pair of lacey purple panties, the soft silk shining in the sun's glow."
                            n "You swear they were sparkling, like you were in an anime."
                            n "She tosses them to you and the first thing you can think to do is sniff them."
                            
                            n "Wait, what's happening...?"
                            n "The hallway is spinning and you feel as though you're being dragged backwards at high speed."
                            
                            n "You wake up on the floor, panties nowhere to be found."
                            n "What just happened?"
                            n "You pull yourself up onto your feet and suddenly recall."
                            n "The moment you asked for Rose's panties she jumped up and smacked you on your head, knocking you out cold."
                            n "But it felt so real in that dream..."
                            n "You're just gonna count that as a W."
                            
                            
                    
                else:
                    #what, you want a handjob?
                    #kinda
                    #well you're not getting one
                    rose @ say "How about I let you lick my boots?"
                    
                    player "How about you lick my balls?"
                    
                    rose @ say "How about I kick you in the balls?"
                    
                    player "Barefoot?"
                    
                    rose @ say "Forget it."
                    
                    player "Alright alright, we'll just be \"friends\" til you get your mansion."
                    
                    rose @ say "I'd say it was a pleasure doing business with you, but it really wasn't. I'm only doing this for my grandfather."
                    rose @ say "And so I can get out of these dorms and away from the disgusting troll that inhabits them!"
                    
                    player "Yeah whatever. See you around, \"friend~\""
                    
                    rose @ say "Weirdo creep."
                    
            else:
                rose @ say "You're just as retarded as the rest of your species if you think I'd agree to any of this!"
                rose @ say "I'd sooner burn the mansion down than let you take one step into it!"
                
                player "Suit yourself. Have fun living in the dorms for the next four years."
                
                n "You do a cool 360 and walk away, staring her down as you moonwalk out of there."
            
            
        "Have fun living in the dorms, bitch":
            player "Ok then have fun living in the dorms, bitch."
            
            rose @ say "I was actually on my way to the library."
            
            if avaLibraryAdventure == true:
                player "I tried to live in the library once. Maybe you could do the same."
                
                rose @ say "Did it work out?"
                
                player "No."
                
                rose @ say "Sad."
            else:
                player "Why don't you move into the library? You practically already live there."
                
                rose @ say "I just might. This dorm has a human infestation and the only solution is to burn the whole thing down."
                
            player "Why are you going to the library? Midterms are over. We have a week off school."
            
            rose @ say "Your kind wouldn't understand concepts like diligence and perfectionism so I don't expect you to get it."
            rose @ say "But if you must know, I'm going to do some research on dinosaurs."
            
            player "You're actually doing the history extra credit? You already have a hundred in that class."
            
            rose @ say "A hundred and one mind you."
            rose @ say "But yes, I'm aiming for a hundred and two. Plus the material is good to know. Not easy to find information on that era since y'know, you destroyed it all."
            
            player "I wasn't there!"
            
            rose @ say "Yet if you were, you'd destroy it with your incompetence."
            
            player "Fuck this and fuck you. I've got better things to do."
            
            rose @ say "So do I. So get out of my way."
            
            n "You decide to flex your height and take a step over her rather than around."
            
            rose @ say "Ugh, please die."
            
            player "No you."
            
            n "The two of you head in opposite directions, taking different stairwells to the base floor, then pretend not to see each other on the way out."
            
        
label writingWithMishka:

    play music "audio/music/vylet - I Wish I Could Tell You.ogg" fadein 1.0
    
    n "Outside the cafe you see Mishka standing by herself, watching street birds hop around and peck at the ground."
    n "They fly away as you approach and Mishka notices you."
    
    mishka @ say "[name]! You're here!"
    
    #player "Sorry, am I late? I thought we agreed to meet up at noon."
    
    #n "You check the time on your phone. It's only 11:45."
    
    #mishka @ say "Nyet, it's okay. I just thought you might"
    
    player "Hey Mishka! Sorry to keep you waiting."
    
    mishka @ say "No worries! So...."
    
    n "She looks around nervously."
    
    mishka @ say "I'm not sure what to do now."
    
    #player "I think college students are supposed to go to parties during these breaks."
    player "Honestly me neither."
    player "The campus is a ghost town cause of autumn break."
    
    mishka @ say "Would you like to go inside? I can make drinks for us."
    
    n "You shrug your shoulders."
    
    player "Might as well."
    
    scene bg cafe with fade
    
    n "Mishka unlocks the door and leads you inside where she starts the make the usual coffee for you."
    
    player "At least there's no customers to worry about today."
    
    mishka @ say "None except you! But do not worry, I won't charge for this."
    
    player "Thanks. Is working at a cafe fun? I like the chill vibes drinking here but it looks pretty hectic making the drinks for everyone."
    
    mishka @ say "Oh it gets pretty hard at times! But it's fairly routine work I would say."
    
    player "You're here like all the time. How do you find time for classes?"
    
    mishka @ say "Well I..."
    #Справді немає потреби!
    mishka @ say "Spravdi nemaye potreby!"
    
    player "Pardon?"
    
    mishka @ say "Nevermind. What do you do for fun?"
    
    menu:
        "Troll online image boards":
            player "I engage in the art of baiting people online."
            
            mishka @ say "You do... baiting to people? I am not familiar with this term."
            
            player "It's a niche hobby where the goal is to make strangers get mad."
            
            mishka @ say "I see."
            
            n "You can tell by the look on her face that she doesn't understand the point."
            n "You're starting to question the point of it all yourself."
            
            player "Over time people catch on to trolling efforts and it takes a lot of creativity to come up with new bait but I'm pretty good at it."
            player "I'm known as a master baiter."
            
            mishka @ say "So it's like creative writing?"
            
            player "Sorta?"
            
            mishka @ say "Ahh how fascinating! I liked to write too!"
            
        
        "Write spicy fanfics":
            player "I like to write."
            
            n "Mishka's eyes widen with excitement."
            
            mishka @ say "You do?!"
            mishka @ say "What sort of things do you write?"
            
            n "You're embarrassed to confess to the type of literature you enjoy."
            
            player "Just like uh... y'know, stuff. Romance stories I guess you could say."
            
            mishka @ say "Ahh how fascinating! I liked to write too!"
            
        #"":
            
        
        "Nothing":
            player "For fun? What's that?"
            
            mishka @ say "You know, what are things you enjoy doing?"
            
            player "I'm not really sure? I don't do a whole lot."
        
            mishka @ say "Really? Nothing?"
            mishka @ say "Why don't you try something new?"
            
            player "Like what?"
            
            mishka @ say "When I found myself in your position I took to creative writing!"
            
    player "What did you write?"
    
    mishka @ say "Stories based on cartoons I watched!"
    
    n "Mishka finishes with the drinks and finds a table for you to sit at."
    
    mishka @ say "Back in my home village we had a satellite dish for the television that could just barely pick up signals. Sometimes it would show cartoons but mostly old Soviet era ones."
    
    player "Wow, I totally forgot that was even a thing. Both satellite TV and the Soviet Union."
    
    mishka @ say "Yes, both were awful!"
    mishka @ say "Eventually we got a computer and I could download western cartoons with fan made Ukrainian dubs! I liked them because they were so much more lighthearted!"
    mishka @ say "It was good escapism when shells were landing near our village."
    
    player "...Shells?"
     
    mishka @ say "Ehh, it's not important. Sorry to bring it up."
    mishka @ say "But this is how I started to be learning English!"
    mishka @ say "I downloaded western fanfictions of my favorite cartoons and read through them. Then I tried writing my own!"
    
    n "You nod then take a sip of your drink, scalding your tongue on 200 degrees of hot coffee (93.3C for countries without freedom units)."
    
    player "Did you post them online?"
    
    mishka @ say "I did! But they are lost to time now."
    
    n "She takes a sip of her coffee then looks to you with a smile."
    
    mishka @ say "Maybe... we could write one together?"
    
    menu:
        "Sounds fun!":
            player "I'd be down to try it. I've never written with someone before though."
            
            mishka @ say "That's okay, we can figure it out!"
            
            n "You discuss some basic premises, characters, and plot and settle on a rough plan."
            
        "I'd rather not":
            player "Ehhh I'd rather not. I'm not that great of a writer."
            
            mishka @ say "Oh come on, at least give it a try!"
    
            player "Alright, but I probably won't be that much help."
            
            mishka @ say "All that matters is that we have fun with it!"
    
            n "Mishka guides you through setting up some basic premises, characters, and a plot."
    
    n "Mishka grabs some napkins and pulls a pen from her jacket pocket. She begins sketching diagrams."
    
    mishka @ say "I like to start draw outlines and arrows pointing out related events. You know basic three act structure, right?"
    
    player "Uhh yeah. Beginning, middle, end."
    
    mishka @ say "Yup! I like to start with the end then work my way backwards!"
    mishka @ say "Got any ideas?"
    
    player "For the ending?? Okay uhhh what if... "
    
    
    menu:
        "A storm comes...":
            player "...a giant storm comes and wipes out the town."
            
            mishka @ say "And then?"
            
            player "I dunno?"
            
            mishka @ say "That's like the climax of the story but there's gotta be more!"
            mishka @ say "If the town gets destroyed by the storm then the people will have to rebuild!"
            
            player "I guess that gives all the characters a moment to get together and start all over again."
            
            mishka @ say "Absolutely! Things are forever changed but they still have a home and each other and live happily ever after!"
            mishka @ say "Now let's go back and start at the beginning to figure out how to get there..."
        
        "The protagonist dies":
            
            player "...the protagonist dies in the end?"
            
            mishka @ say "Seems kinda bleak. Does he do a heroic sacrifice or something?"
            
            player "Maybe... not? Sometimes people just die."
            
            mishka @ say "Yeah but narratively there has to be something there. There needs to be a reason to write it like that!"
            
            player "Okay well maybe the whole story is about like setting things up to pass the torch to the future generations?"
            
            mishka @ say "That could work! Except I think it might cause conflict with some parts of the lore."
            
            player "Yeah, I didn't think of that."
            
            mishka @ say "It's like that saying \"It's about the journey, not the destination.\""
            
            player "Huh, I think that actually works better. Like the main character is focusing on figuring out to spend his days before the inevitable end."
            
            mishka @ say "In that case it should be a hopeful tragedy!"
            
            player "Isn't that kind of a contradiction?"
            
            mishka @ say "Not really! If his death is a tragedy then that means someone cares about him."
            mishka @ say "And if someone cares, then that must mean they had good times together."
            mishka @ say "So he'll have left his mark on the world."
            
            player "I guess that makes sense. I just hope it's not all for nothing."
            
            mishka @ say "Nobody said writing would be easy!"
            
    n "You spend the whole day workshopping your story ideas with Mishka, chugging through multiple cups of coffee."
    n "Before you know it, it's dark outside."
    
    mishka @ say "*Yaaaawn*"
    mishka @ say "I think we will have to stop for now."
    
    player "Damn, we spent the whole day just writing."
    
    mishka @ say "Yeah!! Did you enjoy it?"
    
    menu:
        "I did. A lot.":
            player "I did. A lot. I'm glad you dragged me into it!"
            
            mishka @ say "Hehe I'm glad I could drag you into it! We should write more together some time."
            
            player "Of course! We have to finish the story after all!"
            
        "It was alright":
            player "It was alright. Maybe writing's not my thing after all."
    
            mishka @ say "Aww. Sorry to hear."
            mishka @ say "Maybe I should not have dragged you into this..."
            
            player "No it's fine, it was a nice gesture I just can't write well with others."
            
            mishka @ say "..."
    
    
    n "You help Mishka throw away all the cups and wipe down the table before saying goodbye and returning to your dorm for the night."

    scene bg black with fade

    hide box





label ch4GoWithRori:
    n "After lazing around your dorm for a bit, you get bored and decide to take a walk around campus."
    
    
    n "The campus is like a ghost town now that the autumn break is in effect."
    n "There's only the sound of wind rustling through the leaves and... hoof steps?"
    n "You turn around and see Rori with his nose buried in his phone. He doesn't even notice you."
    
    player "Yo! Rori!"
    
    rori @ say "Huh?"
    
    n "Doubly distracted, he walks straight into a lamp post. Ouch."
    n "You walk over and help him up."
    
    player "You alright?"
    
    rori @ say "Ugh... Yeah I'm fine, thanks."
    
    player "Dude what are you doing on your phone that's so important you're walking into things?"
    
    rori @ say "Just one of those monster catcher games."
    
    player "A what now?"
    
    rori @ say "You know, the kind where you walk around in real life and find creatures in the app."
    
    player "Sounds lame."
    
    rori @ say "Normies were super into it a few years ago but now only the most hardcore dedicated fans still play it."
    rori @ say "You wanna install it? I'll show you how to play!"
    
    menu:
        "Nah":
            player "Nah, keep that shit off my phone. I only play the highest quality kemono girl VNs on it."
            
            rori @ say "Suit yourself."
            
            player "Don't you have better games we could play?"
            
            rori @ say "Like back at my dorm? Sure, we could load up Super Smash Sister or something."
            
            player "Works for me."
        "Give it a shot":
            player "Alright but heads up my phone only has like 640KB of RAM."
            
            rori @ say "That's all anyone needs!"
            
            n "Rori sends you a download link from some sketchy Russian site and you let it run."
            
            player "Bro this shit runs at like negative frame rates."
            
            rori @ say "Yeah they're working on an optimization patch."
            
            player "Okay so what now?"
            
            rori @ say "We just walk around until we come across a monster. They're usually around landmarks and stuff."
            
            n "Rori takes you to a few hotspots on campus and shows you the ropes."
            n "There's literally no gameplay, you just swipe the screen and it automatically does everything."
            
            player "Rori I don't mean to be rude but this is gay as hell. Can we please do anything else?"
            
            rori @ say "Aww you don't like it? That's alright, it's not for everyone."
            rori @ say "How about we go back to my dorm and play a real game?"
            
            player "I'm down."
    
    n "Rori plugs some controllers into his PC then runs a few commands in a terminal. On his monitor an emulator pops up and the game begins to boot up."
    
    player "Yayyy modded Super Smash Sisters!"
    
    rori @ say "An all time classic!"
    rori @ say "Hold up, I got something for occasions like this."
    
    n "He leans forward and grabs a bottle of whiskey from under his desk."
    
    player "Whoa, where'd you get that? Won't the school expell you if they find out you have that in the dorms?"
    
    rori @ say "I guess we better dispose of the evidence then~"
    rori @ say "Winner takes a shot after each round?"
    
    menu:
        "You're on!":
            player "Hell yeah, you're on!"
            player "Wait, the *winner* takes a shot?"
            
            rori @ say "No point in me clowning on you all day. The more I drink the more of a chance you have."
            
            n "You and Rori play a few rounds, taking shots after each game."
        "Decline":
            player "Nah, I don't really feel like getting drunk tonight."
            
            rori @ say "Meh, I'm still gonna take a drink for every win."
            rori @ say "Maybe by the end of the day you'll be consistently beating my drunk ass!"
            
            n "You play a few matches with Rori and even manage to win some, forcing him to take a couple of shots."
            
    rori @ say "Hey."

    player "Yeah?"

    rori @ say "It's getting kinda hot in here."
    rori @ say "You mind if I take my pants off?"
    
    menu:
        "Go ahead":
            player "Go ahead, it's your dorm."
            
            n "Rori yoinks off his pants mid-game and still manages to take all your stocks."
        
        "Only if I can too":
            player "Only if I can too. I swear you run it at a million degrees in here on purpose."
            
            if roriPoints > 4:
                rori @ say "That may have been the plan, yes~"
            else:
                rori @ say "I'm not stopping ya."
                
            n "You try to stay focused on the game while shimmying out of your pants, but Rori manages to take out your last stock."
    
    
    n "A few more matches go by with you chattering about random topics. Then you remember the other day and decide to bring it up."
            
    player "Hey so if you don't mind me asking, what's the deal with your sister? Why is she such a cunt?"
    
    rori @ say "Ugh that's just how she's always been."
    rori @ say "Like she's literally my evil twin."
    rori @ say "I got all the gay and submissive genes and she got the psychopath ones."
    
    player "I don't think that's how that works."
    
    rori @ say "Either way she was raised to think she's better than everyone, which ironically made her try to live up to that ideal."
    rori @ say "And she always used me to prove her superiority."
    
    player "Damn bro that sucks. Kinda makes me glad I was a lone child."
    
    rori @ say "I'm giving you fair warning, do *not* get close to her. She has maxxed out her manipulation stat and will take advantage of you in any way she can."
    
    n "Rori is starting to get tilted and slip up in the game more as he talks about his sister."
    
    rori @ say "Seriously, she is just irredeemably awful. But at least she made me realize how women are so I can just be a fag in peace now."
    
    menu:
        "You don't have to be alone" if roriPoints > 2:
            player "Y'know you don't have to be a fag alone."
            
            rori @ say "Wha?"
            
            player "I mean... uhh..."
            player "We could be fags... together?"
            
            rori @ say "If you want, we could totally snuggle on my bed :3"
            
            player "Let's do it!"
            
            jump roriSnuggles
        "Not all women...":
            player "Come on Rori, not all women are evil bitches devoid of empathy. I bet you could find a nice one."
            
            rori @ say "No thanks. Bros before hoes. The only good women are 2D."
            
            player "What about Ava and Claire? They're sweet."
            
            rori @ say "They're cute but they're manipulative. Even at their best, they're waging a war path to get what they want."
            
            player "A war path? Dude you're exaggerating."
            
            rori @ say "Kinda but you get what I mean. Women are selfish by design. At least with guys we can have some comradery. We instinctually *understand* each other on a primal level."
            rori @ say "And I... I take comfort in that."
            
            player "I don't mean to sound homophobic but it just seems like you hate women."
            
            rori @ say "Yeah and? I don't wanna be alone forever so what other option do I have than to be gay?"
            rori @ say "Besides, some boys are really cute."
            
            if roriPoints > 4:
                player "Am I one of those?"
            
                rori @ say "Of course!"
                rori @ say "Cute enough for me to snuggle at least."
                
                player "For real? Why are we sitting here playing a party game for children instead of doing that?"
                
                rori @ say "I dunno, I thought the video games would be like foreplay."
                
                jump roriSnuggles
            else:
                player "Okay dude hate on women all you want, just don't make baseless assertions about my friends just because your sister is a cunt."
                
                rori @ say "Sorry, I didn't mean to ruin the mood... It's just-"
                rori @ say "I thought you'd understand."
                
                player "..."
            
            #if roriPoints > 4:
                #player "You're kinda right. Like I'm sensing that you wanna snuggle with me right now."
        "Hope you find someone":
            player "Sounds like you've had it rough. You really don't deserve to be alone. I hope you find someone you vibe with."
        
            rori @ say "*Sigh* yeah me too."
            rori @ say "But complaining about it just makes me sound like an incel."
            
            player "Dude our whole friend group is incels, barring Gunner."
            
            rori @ say "Ava and Claire don't count. Women can't be incels."
            
            player "You heard them at the snuggle puddle, they said nobody liked them in high school."
            
            rori @ say "I don't know if I believe that. Either way, I'd keep them at a distance."
            
            player "Noted. But have you seen the way that bunny looks at me?"
            
            rori @ say "Yes, I've noticed. She definitely has a crazed look in her eyes. Be careful around her."
            
    n "You play a few more rounds with Rori before calling it a night."
    
label roriSnuggles:
    n "You hop onto Rori's bed and pat the mattress."
    
    player "Hop on dude~"
    
    rori @ say "Hahaha oooookay, this is a little different from the cuddle puddle."
    rori @ say "Since it's just the two of us, this is definitely a little bit gay~"
    
    player "Yeah whatever, get that sheep butt over here."
    
    n "Rori flops onto the bed and rolls over to you, ending up face to face with you."
    
    rori @ say "*gulp*"
    
    player "So uh... come here often?"

    rori @ say "Usually every night."
    
    player "Is this how you snuggle?"
    
    n "You wrap your arm around him and pull him close."
    
    rori @ say "Eeep!"
    rori @ say "I'm nervous, okay??"
    
    player "What are you nervous for? It's just two bros snuggling."
    
    rori @ say "It's *not* just two bros snuggling!"
    rori @ say "I mean I... kinda like you so I just don't wanna fuck this up."
    
    player "Well I kinda like you too, otherwise I wouldn't be snuggling with you."
    
    rori @ say "*Sigh* Do you wanna listen to me ramble or do you just wanna snug? I'm good with either."
    
    menu:
        "Listen":
            ###set romantic fantasy var true
            player "Go ahead and talk, I'll listen."
            
            rori @ say "Thanks. I wouldn't bring this up to anyone else but I feel comfortable saying it to you cause... I think you'll get it."
            rori @ say ""
            
            
            
            #talk about romantic fantasy (optional)
                #wants someone especially genuine and caring. just a very close best friend i guess? someone who doesn't need him to be any different, just appreciates him as he is
                
                
            #can smooch and/or fug after
            
            
            
        "Snug":
            player "Let's just enjoy the moment. We both wanna snuggle a cute boy, so here we are."
            
            rori @ say "Fair. Snugs are nice."
            
            n "Rori settles in, leaning in even closer to your face."
            
            rori @ say "You're nice to be around. I wouldn't mind doing it more often."
    
            player "You're pretty nice to be around yourself. I never thought I'd meet such an adorable dorky sheep twink who vibes with me."
            
            rori @ say "Hey! I'm taller than you!"
            
            player "Still a twink."
            
            rori @ say "Your twink~"
            
            n "You reach your hand lower and get a handful of fluffy sheep booty."
            
            rori @ say "Mmh~"
            
            if roriPoints > 4:
                menu:
                    "Ask if he wants to go further":
                        n "You're in bed with this pantless ram, cuddling and "
                        
                        rori @ say "U-um well, how much further are you talkin'?"
                        
                        menu:
                            "Some smoochies":
                            
                            "Gay ram sex":
                    "This is as far as you go":
                        n ""
        
    
    
    
    


    rori @ say "That alcohol is really starting to kick in~"


    
    #gay ram sex (optional) (he'll try it if he likes you enough but afterwards says he can't do it again without both of you committing to a relationship)
  


###############


                n "You and Rori take turns passing the bottle back and forth, gradually becoming worse at the games you're playing yet having more fun the drunker you get."
                n "Something about letting all your worries slip away while you mash buttons and trash talk each other makes for a most enjoyable evening."
                n "All while sitting in a steamy room with a cute guy..."
                n "All the dorkiness of Rori disappears as he becomes more relaxed and almost arrogant with the way he plays, going for risky stylish combos rather than safe, effective ones."

                rori @ say "Hey."

                player "Yeah?"

                rori @ say "It's getting kinda hot in here."
                rori @ say "You mind if I take my pants off?"

                n "Maybe it's just the alcohol but the way he so confidently said that instantly puts a blush on your face."
                n "He's right though, it is getting kinda hot."
                n "And it's not really that weird for animal people to take their pants off cause they have fur... right?"
                n "Thankfully spending all that time on video game imageboards prepared you for sleepovers like this."

                player "...Only if I can join you."

                rori @ say "Heheheh, now yer talkin'~"

                n "You and Rori shakily rise from your seats and undo your pants."
                n "Rori particularly seems to have a difficult time as he stumbles from side to side until sitting back down and kicking off his pants legs."

                show rori pantslessdrunk with dissolve

                rori @ say "Ahh, there we go~"
                rori @ say "Nice undies by the way."

                player "Same, dude."

                rori @ say "Ssssay, how bout we make this a little more... interestin'?"

                player "I'm listening."

                rori @ say "Loser -*hic*- has to sit in the winner's lap for the next few rounds~"

                player "You're on!"

                n "You blurt it out without even thinking. Upon quick retrospection you realize you've lost nine out of the past ten matches and you only won one because Rori got up to take a piss."
                n "This is gonna be hard."

                menu:
                    n "{cps=0}This is gonna be hard.{/cps}"
                    "Try to win":
                        n "Try as you might, your drunken reflexes are just too slow to outpace Rori's expertise with the game."
                        #n "You manage to work him into a sweat however, before ultimately being defeated."

                        rori @ say "Ahhh a deal's a deal, [name]!~ Come on up and have a seat~"

                        n "Rori moves his fight stick out of the way and pats his lap."
                        n "With a defeated sigh you get up from your bean bag chair and immediately trip over a chord. Thankfully Rori catches you, albeit in a somewhat... compromising position."

                        rori @ say "Whoa! Y-you okay?"

                        n "With the worst possible timing, the door creaks open and Gunner pokes his head inside."

                        show gunner neutral at norm with moveinright:
                            xpos 550

                        gunner @ say "Hey guys are you done making out or whatever, I-"
                        gunner @ say "Oh my."
                        gunner @ say "I'll just leave you to it then."

                        show gunner neutral at offscreenright with move:
                            yalign 0

                        n "The sheer amount of embarrassment you're feeling temporarily sobers you up enough to stand up and turn around to plant your rear in his lap."
                        n "Rori assists you by putting his hands on your sides pulling you into him. He acts like Gunner didn't just walk in on you."

                        rori @ say "There ya go~ Comfy?"
                        #rori @ say "Go ahead and get comfortable~"

                        player "Y-yeah."

                        n "You lean over to pick your controller up off the ground while Rori has an awkward time setting his fight stick up on your lap."
                        n "You get settled in and lean back against Rori's chest, just living in the moment until Rori pokes you."

                        rori @ say "You gonna pick your character or what?"

                        player "Oops forgot to hit A, sorry."

                        n "You tap the button and resume playing."
                        n "Rori rests his muzzle on your shoulder and several rounds go by, usually with him winning."
                        n "It doesn't help that you're distracted..."
                        n "He's so warm and soft..."
                        n "A spontaneous thought pops into your head."
                        n "You should kiss him."

                        menu:
                            "Kiss him!":
                                n "In the middle of a match, you turn your head and bring one hand up to Rori's face, stroking his fur."

                                rori @ say "Heyyyy what are you doin'?~ I'm tryna play thish game hahaha~"

                                n "You silence his complaints by planting your lips upon his."
                                n "His eyes go wide and muffled moans escape his throat."
                                n "Soon though, his mind catches up to what's happening and he accepts it."
                                n "He lets go of his controller and his paws start to explore your body while kissing you back."
                                
                                stop music fadeout 1.0

                                scene bg roridorm with fade

                                show box with Dissolve(.2):

                                #monday4

                                n "After that it's hard to recall specific details, but you remember it was a fun night."
                                n "You woke up in his bed with him in your arms, enjoying the snuggles while you wait for him to wake up."

                                show rori pantsless at norm with dissolve

                                rori @ say "*Yaaaawn*"
                                rori @ say "God, I've got such a headache... Oh hey [name]."
                                rori @ say "Err, what are you doing in my bed?"
                                rori @ say "And where are your pants?"

                                n "You stifle a giggle and lean in to give him a smooch on his lips."

                                player "Does that jog your memory?"

                                rori @ say "Oh... Oh! Haha yeah, it does~"
                                rori @ say "I guess I thought that was just a dream. I'm glad it wasn't though!"

                                player "Me too~"

                                rori @ say "Ahah... Soooo...."
                                rori @ say "What now?"

                                player "I should probably get going soon so Gunner can reclaim his dorm."

                                rori @ say "Yeah, I guess we did kinda hog the room for ourselves..."

                                n "He helps you find your pants then gives you a parting kiss on your way out."

                                player "But yeah, I wouldn't mind if we hung out at my dorm next time."
                                player "I got the whole place to myself~"

                                rori @ say "Sounds good to me~"

                                n "He looks so cute when he smiles like that. You can't help but pull him into a hug and kiss him one more time before leaving."

                                rori @ say "See you later [name]!"

                                player "Later!"

                                stop music fadeout 1.3

                                scene bg codadorm with fade

                                show box with Dissolve(.2):

                                n "After taking a shower, you check your phone. Looks like Rori sent you a message."

                                call phone_start from _call_phone_start_21

                                call message_start("Rori", "Hey [name] I really enjoyed last night and I'd love to do something like that again soon", "roriavi.png") from _call_message_start_31

                                call reply_message("Same!") from _call_reply_message_120

                                call message("Rori", "<3", "roriavi.png") from _call_message_165
                                call message("Rori", "Gunner's been complaining it smells like sweaty human in here now lmao", "roriavi.png") from _call_message_166

                                call reply_message("Oh right, animals have much stronger sense of smell than I do") from _call_reply_message_121
                                call reply_message("I just took a shower but I can still smell a bit of ram") from _call_reply_message_122

                                call message("Rori", "Sorry lol", "roriavi.png") from _call_message_167
                                call message("Rori", "We also have a much stronger musk than humans", "roriavi.png") from _call_message_168

                                call reply_message("It's fine I don't mind") from _call_reply_message_123
                                call reply_message("I kinda like your smell~") from _call_reply_message_124

                                call message("Rori", "Aww <3", "roriavi.png") from _call_message_169

                                call reply_message("<3") from _call_reply_message_125

                                call phone_end from _call_phone_end_25

                                #n "You start getting ready for class, excited to text Rori again afterward."

                                jump monday6
                            "Don't kiss him":
                                $ dating = ""
                                n "You've got to put a stop to this. You don't like Rori like this."
                                n "You shouldn't lead him on by kissing him. You shouldn't even be in his lap."
                                n "But he's having such a good time, and honestly so are you."
                                n "It wouldn't hurt to let him enjoy having your butt in his lap for a few more rounds, right?"
                                n "You play another round or two before deciding to hop off and sit back in the bean bag chair."

                                rori @ say "Aww, leaving so soon?"

                                player "It was getting a little too hot for my liking."

                                rori @ say "Heh, I'll say it was~"
                                rori @ say "Ah well, the spot's still available if you ever change your mind~"

                                n "As tempting as it is, you stay where you are for the remainder of the night until it's time to return to your dorm."
                                n "You and Rori had finished the bottle of whiskey at some point but you'd sobered up enough to walk home."

                                rori @ say "Ahh, this was fun, wasn't it?"
                                rori @ say "Nothin' like playing games with a friend all night, huh?"

                                player "Yup! The alcohol sure helped too~"

                                rori @ say "Heh, it sure did~"

                                n "Rori leans into you and gives you a hug."

                                rori @ say "See ya later~"
                                rori @ say "Don't get lost on the way back home, k?"

                                n "You return the hug and pat him on the back."

                                player "I'll be alright."

                                rori @ say "Don't forget your pants, bro."

                                player "Oh right."

                                n "You put your pants back on before waving goodbye to Rori and heading back to your dorm, where you flop in bed and fall asleep immediately."

                                stop music fadeout 1.3

                                scene bg codadorm with fade

                                show box with Dissolve(.2):

                                n "The following morning, you check your phone and find Rori messaged you."

                                call phone_start from _call_phone_start_22

                                call message_start("Rori", "Last night was pretty crazy, huh? I enjoyed it tho and I hope you did too lol", "roriavi.png") from _call_message_start_32

                                call reply_message("Yeah lol it was great") from _call_reply_message_126
                                call reply_message("We should do it again sometime!") from _call_reply_message_127

                                call message("Rori", "Sure! I promise I'll keep my pants on next time :P", "roriavi.png") from _call_message_170
                                call message("Rori", "Haha unless...?", "roriavi.png") from _call_message_171

                                call reply_message("Omg I just remembered that part") from _call_reply_message_128
                                call reply_message("I blame the alcohol") from _call_reply_message_129

                                call message("Rori", "Suuuuuure", "roriavi.png") from _call_message_172
                                call message("Rori", "lol Gunner's been complaining it smells like sweaty human in here now", "roriavi.png") from _call_message_173

                                call reply_message("Oh right, animals have much stronger sense of smell than I do") from _call_reply_message_130
                                call reply_message("I need to take a shower. I still smell like ram.") from _call_reply_message_131

                                call message("Rori", "Sorry lol", "roriavi.png") from _call_message_174
                                call message("Rori", "We also have a much stronger musk than humans", "roriavi.png") from _call_message_175

                                call reply_message("It's fine I don't mind") from _call_reply_message_132

                                call message("Rori", "Heh well I'll see you around [name]", "roriavi.png") from _call_message_176

                                call reply_message("see yaaaa") from _call_reply_message_133

                                call phone_end from _call_phone_end_26

                                jump monday6
                    "Lose on purpose":
                        #rori suspects you lost on purpose and teases you but player blames it on being drunk
                        n "The thought of sitting in Rori's lap is all you need to throw the match."
                        n "You play extra bad to ensure you lose, though it probably wasn't necessary."

                        rori @ say "Ahahaha what was that?? Don't tell me you lost on purpose~"

                        player "Shuddup, it was the alcohol makin' me all slow and stuff!"

                        rori @ say "Suuuuuure [name]~"
                        rori @ say "Now hurry up and get your cute butt up here!"

                        n "His words ellicit a giggle out of you, throwing out any pretense of you not being eager to do this."
                        n "Rori moves his fight stick out of the way and pats his lap."
                        n "You hop up from your bean bag chair and stumble over to Rori, planting your rear square in his lap and fidgeting around to get comfortable."
                        n "You can hear a soft sigh from behind you as his hands grab your waist and pull you closer to him."
                        n "With the worst possible timing, the door creaks open and Gunner pokes his head inside."
                        n "You freeze, but Rori seems utterly unaware of Gunner's presence and gently paws at you."

                        show gunner neutral at norm with moveinright:
                            xpos 555

                        gunner @ say "Hey guys are you done making out or whatever, I-"
                        gunner @ say "Oh my."
                        gunner @ say "I'll see myself out then."

                        show gunner neutral at offscreenright with move:
                            yalign 0
                            
                        n "Your face turns red and you feel hotter than before."

                        rori @ say "Heh, what's the matter? Never been in a ram's lap before?"

                        player "Y-yeah, that's it."

                        rori @ say "Well you better get used to it~"

                        n "Rori leans to the side to pick up your controllers. He hands you yours and you help him set his fight stick up on your lap."
                        n "You get settled in and lean back against Rori's chest while he gets used to this... control scheme."

                        rori @ say "You gonna pick your character or what?"

                        player "Hm? Oh right, sorry."

                        n "You hurry up and choose your fighter and resume playing."
                        n "Rori rests his muzzle on your shoulder and several rounds go by, usually with him winning."
                        n "It doesn't help that you're distracted..."
                        n "He's so warm and soft..."
                        n "A spontaneous thought pops into your head."
                        n "You should kiss him."

                        menu:
                            "Kiss him!":
                                n "In the middle of a match, you turn your head and bring one hand up to Rori's face, stroking his fur."

                                rori @ say "Heyyyy what are you doin'?~ I'm tryna play thish game hahaha~"

                                n "You silence his complaints by planting your lips upon his."
                                n "His eyes go wide and muffled moans escape his throat."
                                n "Soon though, his mind catches up to what's happening and he accepts it."
                                n "He lets go of his controller and his paws start to explore your body while kissing you back."

                                stop music fadeout 1.0

                                scene bg roridorm with fade

                                show box with Dissolve(.2):

                                #monday4

                                n "After that it's hard to recall specific details, but you remember it was a fun night."
                                n "You woke up in his bed with him in your arms, enjoying the snuggles while you wait for him to wake up."

                                show rori pantsless at norm with dissolve

                                rori @ say "*Yaaaawn*"
                                rori @ pantsless "God, I've got such a headache... Oh hey [name]."
                                rori @ pantsless "Err, what are you doing in my bed?"
                                rori @ pantsless "And where are your pants?"

                                n "You stifle a giggle and lean in to give him a smooch on his lips."

                                player "Does that jog your memory?"

                                rori @ pantsless "Oh... Oh! Haha yeah, it does~"
                                rori @ pantsless "I guess I thought that was just a dream. I'm glad it wasn't though!"

                                player "Me too~"

                                rori @ pantsless "Ahah... Soooo...."
                                rori @ pantsless "What now?"

                                player "I should probably get going soon so Gunner can reclaim his dorm."

                                rori @ say "Yeah, I guess we did kinda hog the room for ourselves..."

                                player "Oh shoot, I forgot it's Monday already!"

                                n "He helps you find your pants then gives you a parting kiss on your way out."

                                player "But yeah, I wouldn't mind if we hung out at my dorm next time."
                                player "I got the whole place to myself~"

                                rori @ pantsless "Sounds good to me~"

                                n "He looks so cute when he smiles like that. You can't help but pull him into a hug and kiss him one more time before leaving."

                                rori @ pantsless "See you later [name]!"

                                player "Later!"

                                stop music fadeout 1.3

                                scene bg codadorm with fade

                                show box with Dissolve(.2):

                                n "After taking a shower, you check your phone. Looks like Rori sent you a message."

                                call phone_start from _call_phone_start_23

                                call message_start("Rori", "Hey [name] I really enjoyed last night and I'd love to do something like that again soon", "roriavi.png") from _call_message_start_33

                                call reply_message("Same!") from _call_reply_message_134

                                call message("Rori", "<3", "roriavi.png") from _call_message_177
                                call message("Rori", "Gunner's been complaining it smells like sweaty human in here now lmao", "roriavi.png") from _call_message_178

                                call reply_message("Oh right, animals have much stronger sense of smell than I do") from _call_reply_message_135
                                call reply_message("I just took a shower but I can still smell a bit of ram") from _call_reply_message_136

                                call message("Rori", "Sorry lol", "roriavi.png") from _call_message_179
                                call message("Rori", "We also have a much stronger musk than humans", "roriavi.png") from _call_message_180

                                call reply_message("It's fine I don't mind") from _call_reply_message_137
                                call reply_message("I kinda like your smell~") from _call_reply_message_138

                                call message("Rori", "Aww <3", "roriavi.png") from _call_message_181

                                call reply_message("<3") from _call_reply_message_139

                                call phone_end from _call_phone_end_27

                                #n "You start getting ready for class, excited to text Rori again afterward."

                                jump monday6
                            "Don't kiss him":
                                $ dating = ""
                                n "You've got to put a stop to this. You don't like Rori like this."
                                n "You shouldn't lead him on by kissing him. You shouldn't even be in his lap."
                                n "But he's having such a good time, and honestly so are you."
                                n "It wouldn't hurt to let him enjoy having your butt in his lap for a few more rounds, right?"
                                n "You play another round or two before deciding to hop off and sit back in the bean bag chair."

                                rori @ say "Aww, leaving so soon?"

                                player "It was getting a little too hot for my liking."

                                rori @ say "Heh, I'll say it was~"
                                rori @ say "Ah well, the spot's still available if you ever change your mind~"

                                n "As tempting as it is, you stay where you are for the remainder of the night until it's time to return to your dorm."
                                n "You and Rori had finished the bottle of whiskey at some point but you'd sobered up enough to walk home."

                                rori @ say "Ahh, this was fun, wasn't it?"
                                rori @ say "Nothin' like playing games with a friend all night, huh?"

                                player "Yup! The alcohol sure helped too~"

                                rori @ say "Heh, it sure did~"

                                n "Rori leans into you and gives you a hug."

                                rori @ say "See ya later~"
                                rori @ say "Don't get lost on the way back home, k?"

                                n "You return the hug and pat him on the back."

                                player "I'll be alright."

                                rori @ say "Don't forget your pants, bro."

                                player "Oh right."

                                n "You put your pants back on before waving goodbye to Rori and heading back to your dorm, where you flop in bed and fall asleep immediately."

                                stop music fadeout 1.3

                                scene bg codadorm with fade

                                show box with Dissolve(.2):

                                n "The following morning, you check your phone and find Rori messaged you."

                                call phone_start from _call_phone_start_24

                                call message_start("Rori", "Last night was pretty crazy, huh? I enjoyed it tho and I hope you did too lol", "roriavi.png") from _call_message_start_34

                                call reply_message("Yeah lol it was great") from _call_reply_message_140
                                call reply_message("We should do it again sometime!") from _call_reply_message_141

                                call message("Rori", "Sure! I promise I'll keep my pants on next time :P", "roriavi.png") from _call_message_182
                                call message("Rori", "Haha unless...?", "roriavi.png") from _call_message_183

                                call reply_message("Omg I just remembered that part") from _call_reply_message_142
                                call reply_message("I blame the alcohol") from _call_reply_message_143

                                call message("Rori", "Suuuuuure", "roriavi.png") from _call_message_184
                                call message("Rori", "lol Gunner's been complaining it smells like sweaty human in here now", "roriavi.png") from _call_message_185

                                call reply_message("Oh right, animals have much stronger sense of smell than I do") from _call_reply_message_144
                                call reply_message("I need to take a shower. I still smell like ram.") from _call_reply_message_145

                                call message("Rori", "Sorry lol", "roriavi.png") from _call_message_186
                                call message("Rori", "We also have a much stronger musk than humans", "roriavi.png") from _call_message_187

                                call reply_message("It's fine I don't mind") from _call_reply_message_146

                                call message("Rori", "Heh well I'll see you around [name]", "roriavi.png") from _call_message_188

                                call reply_message("see yaaaa") from _call_reply_message_147

                                call phone_end from _call_phone_end_28
                                jump monday6
            "Politely decline":

                n "Rori shrugs"

                rori @ say "More for me I guess."

                n "He throws his head back to take another swig."

                player "Hey take it easy with that stuff."
                player "Where'd you even get that anyway?"

                rori @ say "Snuck it out of the fraternity building."

                player "Well quit chugging it and hit start already!"

                n "Rori flips you off and starts the game."
                n "He gradually becomes worse at the game, yet you end up having more fun the drunker he gets."
                n "He gets more sluggish but less predictable over time, leading to some interesting and hilarious plays."
                n "Something about letting all your worries slip away while you mash buttons and trash talk each other makes for a most enjoyable evening."
                n "All while sitting in a steamy room with a cute guy..."
                n "All the dorkiness of Rori disappears as he becomes more relaxed and almost arrogant with the way he plays, going for risky stylish moves rather than safe, effective ones."

                rori @ say "Hey."

                player "Yeah?"

                rori @ say "It's getting kinda hot in here."
                rori @ say "You mind if I take my pants off?"

                n "Did he really just say what you think he said? You thought you were just coming over to play video games..."
                n "He's right though, it is getting kinda hot."
                n "And it's not really that weird for animal people to take their pants off cause they have fur... right?"
                n "Ah what the hell, why not?"

                player "...Only if I can join you."

                rori @ say "Heheheh, now yer talkin'~"

                n "You and Rori rise from your seats and undo your pants."
                n "Rori particularly seems to have a difficult time as he stumbles from side to side until sitting back down and kicking off his pants legs."

                show rori pantslessdrunk with dissolve

                rori @ say "Ahh, there we go~"
                rori @ say "Nice undies by the way."

                player "Same, dude."

                rori @ say "Sayyyy, how bout we make this a little more... interestin'?"

                player "Uh, like how?"

                rori @ say "Loser -*hic*- has to sit in the winner's lap for the next few rounds~"

                n "Given the way he's playing, you're confident you can beat him."
                n "Unless he's been luring you into a false sense of security this whole time so he can win when it matters."

                player "You're on!"

                n "Drunk Rori is somehow so charming you don't even consider turning him down."
                n "You choose your best character and get ready to take him on."

                menu:
                    n "{cps=0}You choose your best character and get ready to take him on.{/cps}"
                    "Try to win":
                        n "Fueled by your sudden desire to have that cute ram sitting in your lap, you go all out."
                        n "Your efforts pay off and you decisively win the match. You look over to Rori and pat your lap."

                        rori @ say "Wha-? No way I lost! Best two out of three!"

                        player "Nope! A deal's a deal, Rori!~ Now get that fluffy booty over here asap~"

                        n "Rori grins as he gets up and stumbles over to you."

                        rori @ say "Alright, but you asked for it~"

                        player "What the hell's that supposed to mea-"
                        player "OOF!"

                        n "Rori falls ass first onto you, pinning you between him and the bean bag chair you're sitting on."

                        rori @ say "Hehehe, comfy?~"

                        n "You toss your controller aside and grab hold of the ram's hips to position him more comfortably on your lap."

                        rori @ say "Heheheh~ H-hey, cut that out -*squeak*- I'm ticklish~ Ahashahaaha~"

                        n "God damn this ram makes some adorable noises."
                        n "With the worst possible timing, the door creaks open and Gunner pokes his head inside."

                        show gunner neutral at norm with moveinright:
                            xpos 555

                        gunner @ say "Hey guys are you done making out or whatever, I-"
                        gunner @ say "Oh my."
                        gunner @ say "I'll just leave you to it then."

                        show gunner neutral at offscreenright with move:
                            yalign 0

                        n "You don't even think Rori noticed with how much he's struggling to breath from laughing."
                        n "You smirk and tease him a bit more before letting him get comfortable."

                        player "There ya go~ Comfy?"

                        rori @ say "Y-yeah."

                        n "You lean over to pick your controllers up off the ground, setting Rori's fight stick down on his lap."
                        n "You pick your character and rest your chin on his shoulder. You can feel him shiver and hear him sigh."
                        n "So cute~"
                        n "You scritch his head a bit and he rewards you with more of those cute noises."

                        player "Ready?"

                        rori @ say "Hm?"

                        player "To start the game?"
                        
                        rori @ say "Oh! Yeah~"

                        n "You play a few rounds but notice you aren't winning as often, despite being the sober one."
                        n "Dammit it's all Rori's fault, he's distracting you! He keeps fidgeting and making cute noises and looking at you with those adorable eyes and... and..."
                        n "He's so warm and soft..."
                        n "A spontaneous thought pops into your head."
                        n "You should kiss him."

                        menu:
                            "Kiss him!":
                                n "In the middle of a match, you lean forward and bring one hand up to Rori's face, stroking his fur."

                                rori @ say "Heyyyy what are you doin'?~ I'm tryna play thish game hahaha~"

                                n "You silence his complaints by turning his head and planting your lips upon his."
                                n "His eyes go wide and muffled moans escape his throat."
                                n "Soon though, his mind catches up to what's happening and he accepts it."
                                n "You let go of his controller and start to rub up and down his fluffy body with your hands while kissing him passionately."

                                stop music fadeout 1.0

                                scene bg roridorm with fade

                                show box with Dissolve(.2):

                                #monday4

                                n "After that it's hard to recall specific details, but you remember it was a fun night."
                                n "You woke up in his bed with him in your arms, enjoying the snuggles while you wait for him to wake up."

                                show rori pantsless at norm with dissolve

                                rori @ say "*Yaaaawn*"
                                rori @ say "God, I've got such a headache... Oh hey [name]."
                                rori @ say "Err, what are you doing in my bed?"
                                rori @ say "And where are your pants?"

                                n "You stifle a giggle and lean in to give him a smooch on his lips."

                                player "Does that jog your memory?"

                                rori @ say "Oh... Oh! Haha yeah, it does~"
                                rori @ say "I guess I thought that was just a dream. I'm glad it wasn't though!"

                                player "Me too~"

                                rori @ say "Ahah... Soooo...."
                                rori @ say "What now?"

                                player "I should probably get going soon so Gunner can reclaim his dorm."

                                rori @ say "Yeah, I guess we did kinda hog the room for ourselves..."

                                player "Oh shoot, I forgot it's Monday already!"

                                n "He helps you find your pants then gives you a parting kiss on your way out."

                                player "But yeah, I wouldn't mind if we hung out at my dorm next time."
                                player "I got the whole place to myself~"

                                rori @ say "Sounds good to me~"

                                n "He looks so cute when he smiles like that. You can't help but pull him into a hug and kiss him one more time before leaving."

                                rori @ say "See you later [name]!"

                                player "Later!"

                                stop music fadeout 1.3

                                scene bg codadorm with fade

                                show box with Dissolve(.2):

                                n "After taking a shower, you check your phone. Looks like Rori sent you a message."

                                call phone_start from _call_phone_start_25

                                call message_start("Rori", "Hey [name] I really enjoyed last night and I'd love to do something like that again soon", "roriavi.png") from _call_message_start_35

                                call reply_message("Same!") from _call_reply_message_148

                                call message("Rori", "<3", "roriavi.png") from _call_message_189
                                call message("Rori", "Gunner's been complaining it smells like sweaty human in here now lmao", "roriavi.png") from _call_message_190

                                call reply_message("Oh right, animals have much stronger sense of smell than I do") from _call_reply_message_149
                                call reply_message("I just took a shower but I can still smell a bit of ram") from _call_reply_message_150

                                call message("Rori", "Sorry lol", "roriavi.png") from _call_message_191
                                call message("Rori", "We also have a much stronger scent than humans", "roriavi.png") from _call_message_192

                                call reply_message("It's fine I don't mind") from _call_reply_message_151
                                call reply_message("I kinda like your smell~") from _call_reply_message_152

                                call message("Rori", "Aww <3", "roriavi.png") from _call_message_193

                                call reply_message("<3") from _call_reply_message_153

                                call phone_end from _call_phone_end_29

                                #n "You start getting ready for class, excited to text Rori again afterward."
                                jump monday6
                            "Don't kiss him":
                                $ dating = ""
                                n "You've got to put a stop to this. You don't like Rori like this."
                                n "You shouldn't lead him on by kissing him. You shouldn't even have him in his lap like this."
                                n "But he's having such a good time, and honestly so are you."
                                n "It wouldn't hurt to let him enjoy having his butt in your lap for a few more rounds, right?"
                                n "You play another round or two before deciding to kick him off and make him sit back in his cool gamer chair."

                                rori @ say "Aww, was I distracting you?"

                                player "Eh, It was getting a little too hot for my liking."

                                rori @ say "Heh, I'll say it was~"
                                rori @ say "If you change your mind, all you gotta do is give the word~"

                                n "Your mind imagines several different scenarios at once but you shake your head and focus."
                                n "As tempting as it is, you sit and play for the remainder of the night until you're too sleepy to continue."

                                player "Ahh, this was fun, wasn't it?"
                                player "Nothin' like playing games with a friend all night, huh?"

                                rori @ say "Yup! The alcohol sure helped too~"

                                player "...Yeah, it did~"

                                n "Rori leans into you and gives you a hug."

                                rori @ say "See ya later~"
                                rori @ say "Don't get lost on the way back home, k?"

                                n "You return the hug and pat him on the back."

                                player "I'll be alright."

                                rori @ say "Don't forget your pants, bro."

                                player "Oh right. I knew I was forgetting something!"

                                n "You put your pants back on before waving goodbye to Rori and heading back to your dorm, where you flop in bed and fall asleep immediately."

                                stop music fadeout 1.3

                                scene bg codadorm with fade

                                show box with Dissolve(.2):

                                n "The following morning, you check your phone and find Rori messaged you."

                                call phone_start from _call_phone_start_26

                                call message_start("Rori", "Last night was pretty crazy, huh? I enjoyed it tho and I hope you did too lol", "roriavi.png") from _call_message_start_36

                                call reply_message("Yeah lol it was great") from _call_reply_message_154
                                call reply_message("We should do it again sometime!") from _call_reply_message_155

                                call message("Rori", "Sure! I promise I'll keep my pants on next time :P", "roriavi.png") from _call_message_194
                                call message("Rori", "Haha unless...?", "roriavi.png") from _call_message_195

                                call reply_message("Omg you were having the time of your life on my lap, weren't you?") from _call_reply_message_156

                                call message("Rori", ";3", "roriavi.png") from _call_message_196
                                call message("Rori", "lol Gunner's been complaining it smells like sweaty human in here now", "roriavi.png") from _call_message_197

                                call reply_message("Oh right, animals have much stronger sense of smell than I do") from _call_reply_message_157
                                call reply_message("I need to take a shower. I still smell like ram.") from _call_reply_message_158

                                call message("Rori", "Sorry lol", "roriavi.png") from _call_message_198
                                call message("Rori", "We also have a much stronger scent than humans", "roriavi.png") from _call_message_199

                                call reply_message("It's fine I don't mind") from _call_reply_message_159

                                call message("Rori", "Heh well I'll see you around [name]", "roriavi.png") from _call_message_200

                                call reply_message("see yaaaa") from _call_reply_message_160

                                call phone_end from _call_phone_end_30
                                jump monday6
                    "Lose on purpose":
                        n "You'd rather be sitting in that cute ram's lap than the other way around."
                        n "You have to really try to throw the match while making it look convincing but Rori immediately sees through your trickery."

                        rori @ say "Hah! No way I just destroyed you that hard while drunk! You want to sit in my lap that bad, huh~"

                        player "N-no, I just... My finger's were sweaty so I kept missing the buttons and..."

                        rori @ say "Ahaha suuure~ Don't worry, I won't tell anyone how eager you are to lose a bet to me~"
                        rori @ say "But next game you lose, you're takin' off more than just your pants~"
                        rori @ say "Now hurry up and get your cute butt up here!"

                        n "Rori moves his fight stick out of the way and pats his lap."

                        n "God, he's so much more... dominant when he's like this."
                        n "Not that you mind one bit."
                        n "You hop up from your bean bag chair and stumble over to Rori, planting your rear square in his lap and fidgeting around to get comfortable."
                        n "You can hear a soft sigh from behind you as his hands grab your waist and pull you closer to him."

                        player "Ah~ Rori... I-"

                        n "With the worst possible timing, the door creaks open and Gunner pokes his head inside."
                        n "You freeze, but Rori continues to casually paw at you, seemingly oblivious to Gunner's presence."
                        n "That or he just doesn't care."

                        show gunner neutral at norm with moveinright:
                            xpos 550

                        gunner @ say "Hey guys are you done making out or whatever, I-"
                        gunner @ say "Oh my."

                        rori @ say "Hm? Whassat?"
                        rori @ say "Gunner!!!! Sup, man? Wanna join us?"

                        n "Your face turns red and you feel hotter than before."
                        n "Gunner's interruption sobers you up even more than you already were. You think about getting out of Rori's lap but he's got a firm grip on you."
                        n "That, and he's just so comfortable and makes you feel like you belong on his lap, even if someone's watching."

                        gunner @ say "Maybe later. When everyone has their pants on."

                        show gunner neutral at offscreenright with move:
                            yalign 0

                        n "Rori shrugs."

                        rori @ say "What's his problem? Anyway, you gonna pick your character?"

                        n "You hurry up and choose your fighter and resume playing."
                        n "Rori rests his muzzle on your shoulder and several rounds go by. You're tempted to lose again on purpose he's somehow playing even worse than you."

                        rori @ say "Nff, I can't beat ya. 'm too drunk."
                        rori @ say "Wanna play another game?"

                        player "Sure, what else ya got?"

                        n "A mischievous grin forms on Rori's face."

                        rori @ say "What was that Gunner said about makin' out?"
                        rori @ say "Oh yeah~"
                        rori @ say "Ever make out with a ram before?"

                        player "N-no?"

                        rori @ say "Would you like to?~"

                        menu:
                            rori "{cps=0}Would you like to?~{/cps=0}"
                            "Hell yes!":
                                n "Your heart skips a beat."

                                player "Y-yes, I'd love to!"

                                n "Rori brings a hand up to your face, turning your head to face him. The smell of alcohol fills your nose as he brings his lips close to yours."
                                n "You tremble as he pushes against you, giving you your first taste of both whiskey and cute ram boy. that alone is enough to make you feel intoxicated and wanting for more."
                                n "Rori happily obliges you, gently gripping your hair as he pushes his lips harder into yours. Soft moans come from the both of you as you enjoy the intimate moment."
                                
                                stop music fadeout 1.0

                                scene bg roridorm with fade

                                show box with Dissolve(.2):

                                #monday4

                                n "After that it's hard to recall specific details, but you remember it was a fun night."
                                n "You woke up in his bed with him in your arms, enjoying the snuggles while you wait for him to wake up."

                                show rori pantsless at norm with dissolve

                                rori @ say "*Yaaaawn*"
                                rori @ say "God, I've got such a headache... Oh hey [name]."
                                rori @ say "Err, what are you doing in my bed?"
                                rori @ say "And where are your pants?"

                                n "You stifle a giggle and lean in to give him a smooch on his lips."

                                player "Does that jog your memory?"

                                rori @ say "Oh... Oh! Haha yeah, it does~"
                                rori @ say "I guess I thought that was just a dream. I'm glad it wasn't though!"

                                player "Me too~"

                                rori @ say "Ahah... Soooo...."
                                rori @ say "What now?"

                                player "I should probably get going soon so Gunner can reclaim his dorm."

                                rori @ say "Yeah, I guess we did kinda hog the room for ourselves..."

                                player "Oh shoot, I forgot it's Monday already!"

                                n "He helps you find your pants then gives you a parting kiss on your way out."

                                player "But yeah, I wouldn't mind if we hung out at my dorm next time."
                                player "I got the whole place to myself~"

                                rori @ say "Sounds good to me~"

                                n "He looks so cute when he smiles like that. You can't help but pull him into a hug and kiss him one more time before leaving."

                                rori @ say "See you later [name]!"

                                player "Later!"

                                stop music fadeout 1.3

                                scene bg codadorm with fade

                                show box with Dissolve(.2):

                                n "After taking a shower, you check your phone. Looks like Rori sent you a message."

                                call phone_start from _call_phone_start_27

                                call message_start("Rori", "Hey [name] I really enjoyed last night and I'd love to do something like that again soon", "roriavi.png") from _call_message_start_37

                                call reply_message("Same!") from _call_reply_message_161

                                call message("Rori", "<3", "roriavi.png") from _call_message_201
                                call message("Rori", "Gunner's been complaining it smells like sweaty human in here now lmao", "roriavi.png") from _call_message_202

                                call reply_message("Oh right, animals have much stronger sense of smell than I do") from _call_reply_message_162
                                call reply_message("I just took a shower but I can still smell a bit of ram") from _call_reply_message_163

                                call message("Rori", "Sorry lol", "roriavi.png") from _call_message_203
                                call message("Rori", "We also have a much stronger scent than humans", "roriavi.png") from _call_message_204

                                call reply_message("It's fine I don't mind") from _call_reply_message_164
                                call reply_message("I kinda like your smell~") from _call_reply_message_165

                                call message("Rori", "Aww <3", "roriavi.png") from _call_message_205

                                call reply_message("<3") from _call_reply_message_166

                                call phone_end from _call_phone_end_31

                                jump monday6
                            "Nah":
                                $ dating = ""
                                n "You've got to put a stop to this. You don't like Rori like this."
                                n "You shouldn't lead him on by kissing him. You shouldn't even be in his lap."
                                n "But he's having such a good time, and honestly so are you."
                                n "It wouldn't hurt to let him enjoy having your butt in his lap for a few more rounds, right?"

                                player "Nah, I'm good like this. Thanks for the offer though haha"

                                n "Rori shrugs."

                                rori @ say "Your loss~"

                                n "Rori puts his hands on his controller and starts another game. You play round after round, telling yourself you'll get up after this next one but you never do."
                                n "Rori keeps distracting you, even going so far as to nibble on your ears, which turns out to be a strangely ticklish sensation."
                                n "During one such instance, you end up so distracted you actually lose a match you were trying to win."

                                rori @ say "Aha! Gotchya! I told ya what'd happen next round I took from ya, didn't I?~"

                                n "You nervously gulp."

                                player "W-well, a deal's a deal I guess..."

                                stop music fadeout 1.0

                                scene bg roridorm with fade

                                show box with Dissolve(.2):

                                #monday4

                                n "After that it's hard to recall specific details, but you remember it was a fun night."
                                n "You woke up in his bed with him in your arms, enjoying the snuggles for a bit before slinking away to get dressed."
                                n "Fuuuuuck, why can't you find your underwear?"
                                if fratsoro == "soro":
                                    n "At least you locate your bra, hanging off the side of the bed from one of Rori's horns."
                                n "Whatever. You hastily put on your pants and tip toe toward the door."
                                n "You feel bad about ditching him but you weren't planning on staying the night really don't feel like staying any longer."

                                show rori pantsless at norm with dissolve

                                rori @ say "*Yaaaawn*"
                                rori @ say "God, I've got such a headache... Oh hey [name]."
                                rori @ say "Err, what are you doing here?"

                                player "Err, I guess we passed out last night. Pretty intense gaming session, heh."

                                rori @ say "Mmmyeah, makes sense."

                                player "Anyway, I had fun and all but I gotta go do a thing now. See ya later!"

                                rori @ say "See ya!"
                                rori @ say "Oh, don't forget about these!"

                                n "Rori pulls your underwear out from under his pillow and holds them up."
                                n "You sheepishly snag them and stuff them under your shirt and head out."

                                stop music fadeout 1.3

                                scene bg codadorm with fade

                                show box with Dissolve(.2):

                                n "After taking a shower, you check your phone. Looks like Rori sent you a message."

                                call phone_start from _call_phone_start_28

                                call message_start("Rori", "Hey [name] I really enjoyed last night. I guess things got pretty wild but I was too drunk to remember clearly", "roriavi.png") from _call_message_start_38

                                call reply_message("Yeah I think we both ended up intoxicated") from _call_reply_message_167
                                call reply_message("It was fun but I'm not sure if I wanna do it again..,") from _call_reply_message_168

                                call message("Rori", "Hm", "roriavi.png") from _call_message_206
                                call message("Rori", "Well I won't bring it up again", "roriavi.png") from _call_message_207
                                call message("Rori", "Gunner on the other hand...", "roriavi.png") from _call_message_208

                                call reply_message("Oh god") from _call_reply_message_169

                                call message("Rori", "Don't worry, I don't think he's gonna blackmail you or anything", "roriavi.png") from _call_message_209
                                call message("Rori", "It's not like he got any pics of us half naked with you on my lap", "roriavi.png") from _call_message_210

                                call reply_message("Mrf~") from _call_reply_message_170
                                call reply_message("NGL i did lose that game on purpose") from _call_reply_message_171

                                call message("Rori", "I knew you did~", "roriavi.png") from _call_message_211

                                call reply_message("Drunk ram boy is hard to resist >.>") from _call_reply_message_172

                                call message("Rori", "Hehe good to know~", "roriavi.png") from _call_message_212
                                call message("Rori", "Well I can always steal another bottle, and my lap's always available ;3", "roriavi.png") from _call_message_213

                                call reply_message("Heh, I'll keep that in mind") from _call_reply_message_173

                                call message("Rori", "Sure thing, cutie~ UwU", "roriavi.png") from _call_message_214
                                call message("Rori", "Until that happens, I get the impression you'd rather be like", "roriavi.png") from _call_message_215
                                call message("Rori", "how things were before last night", "roriavi.png") from _call_message_216

                                call reply_message("Mmmmyeah") from _call_reply_message_174

                                call message("Rori", "That's cool. I don't mind us just being friends.", "roriavi.png") from _call_message_217

                                call reply_message("Thanks Rori") from _call_reply_message_175

                                call phone_end from _call_phone_end_32

                                jump monday6



################




    
    
        
        
    # autumn break
        
        #monday
        #sleeping over at ellen's house
        #ellen's romantic fantasy
            #wants someone who's not afraid to live like it's their last day alive. wants to be free and try new things, go anywhere, just have fun. needs to be someone dedicated to that. no regrets lifestyle.
        
       
        
        
        #mid week side content
            #history extra credit
                #optional pic with rose to send to her grandpa
            #if you decline, then go for a walk and encounter lina, choice to do panty raid 
            #if you decline, you walk into town and come across margaret and celestine shopping (celestine remarks she thinkgs someone stole her panties so she had to get more)
                #margaret "Time honored tradition. Boys will be boys."
                #riiiiight, boys
            
            #texting friends, see what they're up to. claire at the beach, ava and gunner at a party
                #ava: Guess who showed up!!
                #claire's pinstagram
            
        
        #friday
            #power outage in the dorms during a storm
            
        
        
        
    # classes resume
        #skip class with ava and claire. they sleep over
        #trish??
        #saturday - gunner finds you in bed with ava and gets mad. Ava and Claire want to go out again today but you faint and they take you to the hospital, where you get your diagnosis. You start a new treatment to mitigate your symptoms.
        
    #to be committed to ava's route, there's a part where ava's polaroids get lost in the wind and you and gunner have to chase after them. gunner gives up bc it's too dangerous but you can still get it (something like it flies into traffic). Make it super obvious that you're committing to ava here, like "are you absolutely sure you would do this for ava?" or like tell her afterwards "i wouldn't do that for anyone other than you"
    #gunner saves you on your first try, pulls you back and tells you to let it go, it's just one photo
    #if you succeed, ava will later invite you on a date and commit to you 
    
    #glare all you want, you're not getting them back ms ellen