label chapter1:
    stop music fadeout .5
    
    #scene bg letter

    "You got a letter."
    "The name on the envelope said \"Harmonia University.\""
    "It's rediculous... Could it really be true?"
    "Such a prestegious university wants you...?"
    "You never even applied."
    "Did they send this by mistake?"
    "But it's signed by the dean himself."
    
    "\"Congratulations! You have been admitted to Harmonia University for Fall 2021. We invite you to one of the highest ranked learning institutions in the world to experience a plethora of exciting opportunities!\""
    "\"Our passionate staff will prepare you for a lifetime of success. Join us as you step into the next chapter of your life!\""
    
    "It goes on for a while, full of marketing buzzwords and diversity statistics."
    "There's a note at the bottom."
    
    "\"Given your situation, I would like to personally welcome you and offer you a tour of the campus myself. It would be an honor to have you among us.\""
    "\"I have arranged comfortable living accomodations for you, so that you may focus on getting the most out of your education. Your scholarship will cover all your necessities and then some.\""
    "\"On behalf of Harmonia University, we eagerly await your arrival.\""
    "\"Nicodemus Kaczynski\nDean of Harmonia University\""
    
    "It's strange, but can you really say no?"
    "Might as well go for it. There's nothing left for you at home anymore."
    #there's no reason to stay home anymore
    "Your parents died of that damn disease three years ago. Since then you haven't really done anything."
    "This could be a good opportunity to start fresh."
    
    #your parents died of that damn disease three years ago.
    #yes this bit is just a silent hill 2 reference
    
    scene bg black with fade
    
    "A few weeks later"
    
    ########
    
    scene bg campus_sunny_day with dissolve
    #background names can't have capital letters
    
    show box with Dissolve(.2):
        ypos 0
    
    nicodemus "...that about concludes our tour of Harmonia's campus. What did you think? Not too pretentious, I hope! Bahahaha!"
    nicodemus "I'm reminded of when I was a new student here myself. A bit nervous but so full of wonder and excitement! It felt like anything was possible!"
    nicodemus "Forging lifelong friendships! Making a name for myself in the academic community! Joining clubs and causing a ruckus! Why, I even found love sitting under that cedar tree over there."
    nicodemus "My point is, anybody can blow through four years of university, get their diploma and proceed with their life like it never even happened."
    nicodemus "But I implore you to really make the most of what you've been given!"
    nicodemus "Study hard but take some time to search for something that makes you happy, whether that's being with friends or making your mark on society or just living in the moment!"
    nicodemus "Find what's important to you!"
    nicodemus "Now then, do you have any questions, young lad?"
    
    "To be honest, you weren't really paying attention for the past hour until now."
    "The dean is a short raccoon who wears an old timey but distinguished suit. A pair of small spectacles rests at the edge of his snout. He carries a cane but doesn't lean on it too much."
    "He's like a caricature of a kind old grandpa who tells war stories but leaves the gorey parts out."
    "He seems like a nice guy and all, but you just can't escape the feeling like you don't belong here."
    
    $ name = "player"
    define player = Character("name", color="#2a2a2a", what_color="#9af3a8", callback=name_callback, cb_name = "player")
    
    $ questionInvite = False
    $ questionFitIn = False
    $ questionTour = False
    $ questionAsked = False

label nicodemusQuestions:
    menu:
        "Why did you invite me here?" if questionInvite == False:
            $ questionInvite = True
            
            player "I'm grateful to be here, but I don't understand *why* I'm even here."
            player "I never submitted an application."
            
            nicodemus "We keep tabs on \'persons of interest.\' You know, brilliant young students with bright futures to send ads in the mail to. They make for great alumni."
            
            player "So I'm just here for the optics? For your marketing team to brag about how the college is so diverse it has a human?"
            
            nicodemus "Precisely."
            nicodemus "That is, at least on paper, the official reason for how I brought you on board."
            nicodemus "The actual reason has more to do with..."
            
            "He hesitates, seemingly unsure of what words to use."
            
            nicodemus "You see, your predicament reminded me of an old friend of mine. Are you familiar with the Tasmanian tiger?"
            
            "The dean reaches into his coat pocket and pulls out a photograph."
            
            scene bg tasmaniantiger with dissolve
            
            pause 2.3
            
            menu:
                "What about them?":
                    show box with Dissolve(.2):
                        ypos 0
                
                    "You shake your head."
                    
                    player "Never seen them before."
                    
                    nicodemus "No one has, not for a few decades. At least, not a living specimen."
                    nicodemus "I'm afraid they've gone extinct."
                "They're gone, aren't they?":
                    show box with Dissolve(.2):
                        ypos 0
        
                    player "They're not around anymore, right?"
                    
                    nicodemus "Yes, they went exctinct decades ago. There's not even a color photograph of one."
                    
            "\"Extinct.\""
            "The word sends chills down your spine."
            "You've been trying not to think about it, but that's what your species will be once you die."
            "All that will be left of you are stories and photographs."
            
            scene bg campus_sunny_day with dissolve    
            
            show box with Dissolve(.2):
                ypos 0                
            
            nicodemus "He was a dear friend, someone you could always count on. But as time went on, the burden of being the last of his kind got to him."
            nicodemus "He withdrew himself from everyone and eventually withered away, like some forgotten flower. I'd hate for you to suffer the same fate."
            nicodemus "You see what I'm getting at, don't you?"
            
            "You give a somber nod."
        "Will I fit in?" if questionFitIn == False:
            $ questionFitIn = True
            
            player "I'm not sure I fit in here. This seems like the kind of university you only get into if you come from old money."
            
            #nicodemus says the times are changing and so is the demographic, but also says you'll be surprised about how you can find your niche
        "What's with the tour?" if questionTour == False:
            $ questionTour = True
            
            player "A dean like you must be pretty busy. Why'd you take the time out of your day to personally give *me* a tour of the campus?"
            
            nicodemus "Less busy than you'd imagine! I may run the show around here but the show mostly takes care of itself."
        "That's all" if questionAsked == True:
            player "That's all."
            
            jump movingOn
    
    $ questionAsked = True
        
    nicodemus "Was that all you wanted to ask?"
        
    jump nicodemusQuestions
        
        
label movingOn:
    
    
    
    
    
    
    
    
    return
