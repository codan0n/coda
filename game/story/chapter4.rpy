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
        
        
        rory @ say "I'm basically exactly like him but better in every way!"
        rory @ say "While he's busy downloading kernels, I'm uploading patches to fix them~"
        rory @ say "I can run circles around him in his favorite games~ He used to get so mad when I'd perfect KO him in Tekken 10 times in a row!"
        
        
        #rory @ say "Why settle for him when you could have me instead?"
    
    
    #after everyone else leaves, rory shows up to taunt rori before she goes home for the break
    
    
        
        
        
        
        
        
        
        
        
        
        
    # saturday and beyond
        #creative writing with mishka
        
        #pokemon go with rori
        
        #sleeping over at ellen's house
        
        #finding out rose lives in your dorm building
            #her grandad doesn't let her stay with him because he wants her to get out more
        
        #power outage in the dorms during a storm
        
        #texting friends
        
        #claire's pinstagram
        
        #skip class with ava and claire. they sleep over
        
        #saturday - gunner finds you in bed with ava and gets mad. Ava and Claire want to go out again today but you faint and they take you to the hospital, where you get your diagnosis. You start a new treatment to mitigate your symptoms.
        
        