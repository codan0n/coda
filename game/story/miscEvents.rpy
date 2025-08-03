label claireFrenchStudy1:
    #add minor variations if you do this after claire tells you she likes you
    #add bullyclaire if flag is true

    if avaClaireDormIntroSeen == True:
        scene bg avadorm with fade

        play music "audio/music/vylet - I Wish I Could Tell You.ogg" fadein .4
        
        show box with Dissolve(.2):
            ypos 0
            
    else:
        call avaClaireDormIntro from _call_avaClaireDormIntro
    
    n "Ava is lying on her bed reading a magazine while listening to headphones."
    n "She turned her eyes over to you when when Claire crashed through the doorway."            
    
    show ava reaching concerned at center with dissolve:
        ypos y_ava
        xoffset -600
        xzoom -1
    
    ava @ say "Heya Claire. You alright?"
    
    show claire sweater happy at center with dissolve:
        ypos y_claire
        xoffset 500
    
    claire @ say "Ava, get out."
    
    show claire sweater leaning suggestive
    
    claire @ say "...unless you wanna join in on this 'study session' [name] and I are about to have."
    
    show ava reaching embarrassed
    
    ava @ say "I'll just uh, give you two some privacy."
    ava "{nw}"
    
    pause .1
    
    show ava with move:
        xoffset 2400
    
    n "Ava grabs her bag and flutters out of the room."
    n "Without hesitation, Claire pins you between her warm soft body and the cold hard wall. She has a crazed look in her eyes and all you've got is your textbook to protect you."
    
    claire @ say "So~ Where did you want to begin~"
    
    player "Um well..."
    player "Chapter 2-2 was giving me some trouble. I can't tell how to pronounce some of these French words that are a jumble of vowels."
    
    claire @ say "Ksksksks you're so adorable, acting committed to the role~"
    
    n "Role?"
    n "Claire seems to think you're roleplaying like the textbook suggests."
    n "You recall a scenario where one of you acts as a tourist in France needing help with the language. You guess you'll play along."
    
    claire @ say "Laisse-moi t'apprendre~"
    
    n "Claire lifts you off your feet and sets you down in a chair. She brushes aside a pair of panties on the desk and slams your textbook down where it was."
    n "You feel something heavy and squishy rest atop your head as she leans over you."
    
    claire @ say "Il fait chaud ici, n'est-ce pas?"
    
    n "You think she's saying something about it being hot? You flip open your book and look around for an appropriate response."
    
    player "Uhh... oui assez chaud."
    
    show claire pose suggestive earsup
    
    claire @ say "Ça te dérange si j'enlève mon pull?"
    
    n "She tugs at the bottom of her sweater, airing out the heat beneath the fabric."
    n "It's becoming difficult to keep track of the conversation as she uses more words you don't know."
    n "She must have been reading ahead."
    n "All you can offer is a basic observation about the sweater."
    ###in later scenes if you've studied more you can say better things
    
    player "C'est un beau pull. Ça te va bien."
    
    show claire flustered
    
    claire @ say "Hrmm..."
    
    n "Claire racks her claws against the table impatiently while thinking."
    
    claire @ say "Il fait tellement chaud que je pourrais m'évanouir! Allons au lit!~"
    
    n "Before you have time to translate, you're hoisted out of the chair and thrown onto Claire's bed, face up."
    
    scene claire pov edited with fade
    
    show box:
        ypos 0
    
    n "In the blink of an eye, the bunny pounces on top of you, thankfully propping herself up on her paws so as to not crush your frail human body."
    n "Without your textbook to protect you, you'll have an even harder time navigating this strange conversation. You're still unfamiliar with the customs of France but Claire seems to be guiding you."
    n "Perhap if you study more in your free time you'll have a better grasp on things."
    
    player "Is this how people normally talk in France?"
    
    claire "...From what I've read, yes."
    claire "Maintenant, ne sois pas si timide~"
    
    scene bg black with dissolve
    
    stop music fadeout 2.0
    
    pause .8
    
    scene bg avadorm with fade
    
    play music "audio/music/vylet - blockhead.ogg" fadein .4
    
    show box with Dissolve(.2):
        ypos 0
    
    n "An eternity passes with you and your study partner frequently changing position and whispering broken French to each other in this hot and sweaty room."
    n "Though the odd body language still confuses you, you feel like you've learned a few new words and grammatical rules."
    n "You've ended up lying on your back with your head in Claire's lap while she strokes your hair."
    n "It's an incredibly soothing feeling. You could fall asleep right here."
    n "You let out a yawn and check the time on your phone."
    
    show claire sweater happy at center with dissolve:
        ypos y_claire

    player "Man, it's getting late. I should get back to my dorm and get ready for tomorrow."
    
    n "You sit up, roll out of bed, and begin collecting your belongings."
    
    player "This was actually kinda fun. Like the whole 'roleplaying in French' thing. And I learned a lot!"
    player "We should do this again sometime!"
    
    show claire sad
    
    claire @ say "...Seriously?"
    
    player "What?"
    
    claire @ say "Nothing... I had fun too."
    
    n "She seems disappointed. Was there something else she wanted to do?"
    
    show claire sweater pose suggestive
    
    claire @ say "Maybe next time we can do something... more fun than studying?~"
    
    n "Ohh she probably means playing video games."
    ###download some french translated games for next time
    
    player "Sure, we can play around next time."
    
    claire @ say "Okay <3"
    claire @ say "Yay <3"
    
    player "See you in class!"
    
    claire @ say "À un de ces quatre!"
    
    hide claire with dissolve
    
    stop music fadeout 2.0
    
    return


label claireFrenchStudy2:
    $ claireFrenchSession = 2
    
    if avaClaireDormIntroSeen == False:
        call avaClaireDormIntro
    
    n "At least Ava isn't here this time."
    n "Claire wastes no time in removing her sweater."
    
    claire @ say "What? It's hot in here."
    
    player "Whatever helps you study!"
    
    claire @ say "Ksksksks so dedicated to the role, I love it~"
    claire @ say "Puis-je prendre ta veste?"
    
    player "Uhh..."
    
    n "Before you can mentally translate the sentence, Claire tears your jacket from your body and gives it a good sniff."
    
    claire @ say "Ahhh, boysmell~ That's the good stuff~"
    claire @ say "Especially *human* boysmell~"
    
    player "Merci!"
    
    claire @ say "Ksksksks so cute~"
    claire @ say "I guess we should begin studyin', huh?"
    claire @ say "Well go ahead, court me like you would a French girl!"
    
    n "There actually was a section in the book about flirting. You try and recall some French pick up lines."
    
    if frenchSkill < 4:
        player "Uhh comment ça va?"
        
        claire @ say "Comment ça va? *Comment ça va?!*"
        claire @ say "Bien, je suppose. Pourquoi demandez-vous?"
        
        show claire topless surprised earsup at center:
            ypos y_claire
        
        menu:
            claire "{cps=0}Bien, je suppose. Pourquoi demandez-vous?{/cps}"
            "Just wanted to get to know you":
                player "Je voulais juste te connaître."
                
                claire @ say "Pourquoi ne m'emmènes-tu pas à un rendez-vous alors?"
                
                player "A date? Wait are we still roleplaying or not?"
                
                claire @ say "Ksksksks do you want us to be?"
                
                player "I guess we could roleplay a date in Paris. For studying purposes that is."
                
                claire @ say "And nothing more?"
                
                player "...Maybe a bit more."
                
                claire @ say "Sounds lovely~ Take me to the Louvre~"
                
            "You look like you fuck human men":
                player "Parce que tu as l'air de baiser des hommes humains."
                
                claire @ say "I never actually have!"
                claire @ say "Mais il y a une première fois à tout."
                
                player "This is just part of the roleplay by the way."
                
                claire @ say "Aww..."
                claire @ say "We could turn this into an erotic roleplay >:3"
                
                player "Will that help me pass the exam?"
                
                claire @ say "Perhaps."
                
                player "We didn't have a lesson on bedroom talk..."
                player "But I think there was a section in the book about going out on dates."
                
                claire @ say "We could do a roleplay date! Pretend we're in Paris!"
                
                player "I guess we could give it a shot. Lemme pull up some pics of Paris landmarks on my phone."
                
                claire @ say "Eeeeeee, I'm so excited!~"
        
    else:
        player "Qui est cette mignonne toute seule?"
        
        claire @ say "Q-qui, moi?"
        claire @ say "You really think I'm cute?"
        claire @ say "I mean... tu penses vraiment que je suis mignon?"
        
        menu:
            "The cutest!":
                $ clairePoints += 1
                
                player "Oui!"
                player "Don't tell the others but I think you're the cutest in the friend group~"
                
                claire @ say "Oh my gosh really????"
                claire @ say "I knew you had the hots for me~"
                claire @ say "I think my relentless flirting is starting to pay off!"
                
                player "Heh, maybe a little..."
                
                claire @ say "So how about we go on a date?"
                
                player "A real one? Or just like a French study date?"
                
                claire @ say "Yes!"
                
                player "That doesn't... okay whatever. How about we finish up our roleplay like we're going on a date in Paris?"
                
                claire @ say "Works for me!"
                
            "You're pretty cute for a 400 pound bunny":
                player "Tu es plutôt mignon pour un lapin de 400 livres."
                
                if intoFatChicks == True:
                    claire @ say "Ksksksks knowing you, you're into that sort of thing~"
                    
                    player "Guilty as charged~"
                    
                    claire @ say "Well if you even wanted to date a big beautiful bunny, here's your chance~"
                    
                    player "A date? Wait are we still roleplaying or not?"
                    
                    claire @ say "Ksksksks do you want us to be?"
                    
                    player "I guess we could roleplay a date in Paris. For studying purposes that is."
                    
                    claire @ say "And nothing more?"
                    
                    player "...Maybe a bit more."
                    
                    claire @ say "Sounds lovely~ Take me to the Louvre!~"
                        
                else:
                    claire @ say "H-hey, I'm only 350 pounds..."
                    claire @ say "And I'm actually pretty muscular under all this cushion!"
                    
                    player "I guess you have to be to constantly be lifting all that mass."
                    
                    claire @ say "Is this really your idea of flirting?"
                    
                    player "Uhh... am I supposed to be flirting?"
                    
                    claire @ say "I thought that was the whole point of this exercise."
                    
                    player "Right, sorry. I don't even know how to flirt in English, let alone French."
                    
                    claire @ say "Ksksksks that's okay~ You can take me out on a date to make up for it!"
                    
                    player "A date?! During midterms week?"
                    
                    claire @ say "Just a mock date will do~ We can pretend we're in Paris!"
                    
                    player "I guess there was that section in the book about dating. Je viendrai te chercher à sept heures."
                    
                    claire @ say "That's the spirit!"
                    
    
    n "You go on a virtual tour of Paris with Claire, visiting famous places like the Louvre and Eiffel Tower through the power of the internet."
    n "At some point you moved to her bed and she's been unable to keep her paws off you."
    n "Her distraction makes it difficult to continue your study/roleplay session."
    
    ###art of claire sitting on bed with player in her lap but obscured by open textbook claire is holding
    
    menu:
        "Get flirty":
            $ clairePoints += 1
            $ almostKissedClaire = True
            
            n "Newsflash buddy, this rabbit is down to fuck and you've just been friendzoning yourself all this time."
            n "When are you going to man up and dick her down?"
            
            player "Do you think any of this will actually be on the midterm?"
            
            claire @ say "Probably not, but you've been getting more fluent in French!"
            
            player "Yeah, I think I'm good on the exam. How about we take a break from studying?"
            player "Like a break to make out or something."
            
            claire @ say "Sounds good to me!"
            claire @ say "Get on up here!"
            
            n "Claire pulls you in close. Whatever bravado you had moments ago melts into nervousness."
            n "Are you really about to go through with this?"
            n "Inching closer, you close your eyes, waiting for the moment your lips make contact with hers."
            n "Before it ever happens, you hear the door knob rotate and your eyes shoot open."
            
            ava @ say "Hey Claire... Oh! Am I interrupting something?"
            
            n "Claire opens her eyes to glare daggers at her roommate."
            
            claire @ say "Ava! You ruined the moment!!"
            
            ava @ say "OMG were you two about to kiss??"
            
            if avaCommitted == True:
                ava @ say "Were you really just gonna steal him away from me like that?!"
                
                show claire topless surprised earsup at center:
                    ypos y_claire
                    xoffset 500
                show ava pose annoyed at center:
                    ypos y_ava
                    xoffset -500
                    xzoom -1
                
                claire @ say "Don't you have your own boytoy to play with? Can't you let me have this human male all for myself?"
                
                ava @ say "Bitch, you know I have feelings for [name] too!"
                
                claire @ say "I can't help it if he falls for *my* charm instead!~"
                
                menu:
                    "We were just acting out a scene":
                        $ clairePoints -= 1
                        
                        player "We were just acting out a scene from our French textbook."
                        player "Claire invited me over to study for our midterm on Thursday."
                        player "I guess we got a little too in character."
                    
                        claire @ say "Oh!"
                        claire @ say "Y-yeah, I guess so..."
                        
                        ava @ say "Was being topless necessary for your studying too?"
                        
                        claire @ say "Nah, I was just hot."
                        
                        ava @ say "It is pretty hot in here."
                        
                        n "Ava nonchalantly unbuttons her top and takes it off."
                        
                        ava @ say "What? If you two are gonna be topless then so am I."
                        
                        player "Do you two walk around in your dorm half naked often?"
                        
                        claire @ say "All the time."
                        
                        ava @ say "Claire goes full nude most of the time."
                        
                        claire @ say "I can't help it! My body's a furnace and they always crank up the heat in here!"
                        
                        player "You should come to my dorm."
                        
                        claire @ say "Is that an invitation to walk around your dorm naked?"
                        
                        player "What? No, I meant I have air conditioning."
                        
                        claire @ say "Oh."
                        
                        ava @ say "We should hang out at your dorm more often though."
                        
                        claire @ say "Agreed~"
                        
                        player "Do I get a say in this matter?"
                        
                        ava @ say "Hm. No~"
                        
                        n "Ava sidles up beside you and wraps her wing around you. Claire pulls her in closer."
                        
                        claire @ say "The mini cuddle puddle is always open if ya want it, [name]~"
                        
                        player "I'm surprised you two get along so well considering how much you argue."
                        
                        ava @ say "That's just how girls are. The more we bicker, the stronger our friendship!"
                        
                        claire @ say "This bird always comes down to my bunk to snuggle at night after we get in a huge fight~"
                        
                        #ava @ say "Oh shush, [name] doesn't need to know that!"
                        ava @ say "Do guys not do that?"
                        
                        player "Nah, we just call each other homophobic slurs."
                        
                    "Claire is pretty irresistable...":
                        $ avaPoints -= 2
                        
                        player "Turns out Claire is pretty irresistable."
                        player "We were just trying some stuff, nothing too serious."
                        
                        ava @ say "Hmph, then I hope you don't mind me 'just trying some stuff' with Gunner!"
                        
                        player "Go right ahead. You can have catboy cock as long as I get bunny boobs."
                    
                        ava @ say "Maybe I will! Just don't come crawling back to me when you get tired of this oversized rabbit!"
                    
                        n "Ava storms out of the room, slamming the door on her way out."
                        
                        claire @ say "Geez what a drama queen. It was just a near smooch event, it's not like I was bouncing on your dick."
                        
                        player "Myeah. I kinda feel bad though. She did admit she liked me last week."
                        
                        claire @ say "That's for her to work through. I like ya just as much, if not more!"
                        
                        player "I guess if she wants me that bad she'll have to get past you first."
                        
                        claire @ say "Probably! I just hope we can all stay friends no matter what happens."
                        
                        player "Yeah. I'd hate to lose you guys over some romantic feelings."
                        
                        claire @ say "I have a feeling we'll all be together for a long time~"
                    
                    "If you can like 2 boys I can like 2 girls" if avaPoints > 5:
                        player "Hey if you like two boys, why can't I like two girls?"
                        
                        claire @ say "Yeah Ava, it's only fair if you don't pick a side that you let [name] be flirty with other girls too!"
                        
                        ava @ say "Ugh...! Fine, but you're not stealing that first human smooch from me!"
                        
                        claire @ say "Try and take it, I dare ya~"
                        
                        player "Ladies, please. Quit fighting and I'll give you both a smooch."
                        
                        claire @ say "Vraiment?"
                        
                        ava @ say "Really?"
                        
                        n "Ava flutters closer. You pull her in and plant a kiss on her forehead then do the same for Claire."
                        
                        player "There, happy now?"
                        
                        claire @ say "Yasss~"
                        
                        ava @ say "It's a start."
                        
                        n "Gee why do you get two girls flocking to you?"
                        n "It feels less like a chad power fantasy and more like you're working to wrangle them in."
                        n "Twice the women, twice the problems."
                        
                        
                
            else:
                menu:
                    "Yeah, kinda":
                        player "Yeah, kinda. Until you barged in uninvited."
                        
                        ava @ say "Excuse me, it's *my* dorm as well!"
                        
                        claire @ say "Can't a girl get some privacy with her human?"
                        
                        ava @ say "Oh? Are you two a couple now?"
                        
                        player "No."
                        
                        claire @ say "Not yet~"
                        
                        ava @ say "Don't you have your own dorm to yourself? You can have your fun over there."
                        
                        claire @ say "Great idea! Next time I'm coming over to your place [name]~"
                        claire @ say "That way Ava can bring Gunner over here and it'll all work out!"
                        
                        ava @ say "Hey, who said I'm doing anything with Gunner?"
                        
                        claire @ say "Oh please, if you had a moment alone with him in private you'd be doing more than what [name] and I were about to do!"
                        
                        ava @ say "Not true! I'm still waiting to determine my feelings for him!"
                        
                        claire @ say "Well if you wait too long then your other options are gonna be taken!"
                        
                        ava @ say "I'll get with one of them when I'm good and ready!"
                        
                        menu:
                            "Claire's right":
                                player "Claire's right, Gunner seems like the boy for you."
                                
                                ava @ say "Ugh I knowwww but I still have feelings for someone else too..!"
                                
                                player "Who?"
                                
                                claire @ say "Should I tell him?"
                                
                                ava @ say "*sigh* No, he'll figure it out if it's meant to be."
                            "You should wait and see":
                                player "Yeah no need to rush, you'll find the true one for you when the time is right."
                                
                                ava @ say "See, [name] knows what it's all about. Romance is a delicate thing, you can't just bumrush your way in... *Claire*!"
                                
                                claire @ say "What? Boys are dense, you gotta let them know directly you want them, and even then they're still too stupid to get it half the time!"
                                
                                ava @ say "Ugh, I don't need this kind of stress during midterms week."
                    "We were just acting out a scene":
                        $ clairePoints -= 1
                        
                        player "We were just acting out a scene from our French textbook."
                        player "Claire invited me over to study for our midterm on Thursday."
                        player "I guess we got a little too in character."
                    
                        claire @ say "Oh!"
                        claire @ say "Y-yeah, I guess so..."
                        
                        ava @ say "Was being topless necessary for your studying too?"
                        
                        claire @ say "Nah, I was just hot."
                        
                        ava @ say "It *is* pretty hot in here."
                        
                        
                        
                        
                        
                        
                        
                        
                    
                    #ava @ say "How go the studies?"
                    
                    # claire @ say "Tres bien!"
                
                
                
            
            
            
            
            
            
        
        "Focus on studying":
            $ frenchSkill += 1


    return