label roriDormIntro:
    $ roriDormIntroSeen = True
    #"this is a description of rori's dorm for when you visit it for the first time"
    
    scene bg roridorm with dissolve
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Scattered throughout Rori's dorm are various electronics that heat the room to rival a sauna."
    n "The glow of several CRT monitors displaying vintage anime pierces your retinas. Toxic fumes from a soldering iron linger in the air, making you cough. The whirring of fans could drown out the sound of a jet engine."
    
    show rori neutral at norm with dissolve
    
    rori "Sorry about the mess. The university pays for power so I hooked up a few crypto mining ASICs to generate some passive income."
    
    menu:
        "And kill the environment.":
            player "And destroy the environment in the process."
            
            rori "A few kilowatts is nothing in the grand scheme of things."
            rori "There's a nuclear power plant that generates plenty of electricty nearby."
        "Based electricity thief.":
            player "Based electricity thief."
            
            rori "It's not stealing if they're giving it away for free."
            rori "If they didn't want me using 11000 watts, they shouldn't have given me so many electric sockets."
            
            player "I don't think they accounted for daisy chaining power strips like that. Seems like a fire hazard."
            
            rori "Good thing they have insurance then, and I have remote backups."
    
    return
    
label avaClaireDormIntro:
    #"this is a description of Claire and Ava's dorm, to be played the first time you enter it."
    $ avaClaireDormIntroSeen = True
    
    scene bg avadorm with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    n "This is the first time you've ever been in a girl's room. This one being shared between Ava and Claire, their lifestyles are reflected in the stark contrast in their respective sides of the room."
    n "Ava's side is tidy and clean with art books neatly stacked on the desk alongside expensive camera gear whereas Claire's half of the room is unkempt and disorganized."
    n "She also has a tendency to leave her underwear in random places."
    n "The duality of woman."
    
    return
    

label sleepingIn:
    #scene plays the first time you sleep in and skip class
    
    $ bedpilled = True
            
    #results in you skipping class but having more time to do stuff after class
    
    n "Without a doubt, the best thing you can do is take care of yourself."
    n "And taking care of yourself means hitting the snooze button from time to time."
    n "By your calculations, five more minutes of shuteye translates to at least an hour of alertness and productivity in the day."
    n "Can you really refuse such a lucrative offer? That's more than a 10x return on investment!"
    n "Yes, it's best to return to your comfy fortress underneath those blankets."
    n "It would be foolish to fall for the sunk cost fallacy line of thinking that you *must* continue your day right now just because you've already gotten out of bed."
    n "You crawl into the cotton's warm embrace and go for round two in the ring of slumber."
    
    scene bg black with fade
    
    pause 0.9
    
    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0
    
    n "Five minutes turned into an hour in the snap of your fingers."
    n "Time's imperceptibly slow march suddenly lurched forward while you were asleep to stab you in the back when you were at your most vulnerable."
    n "Your eyes open and focus in on your clock. Your first class of the day is halfway over by now but you might make it to the second one."
    n "Although you do feel slightly more energized, you forgot to account for diminishing returns."
    n "Plus you now have to pay back your debt to the sleep economy by getting less than an optimal amount of sleep later."
    n "Or you could go to bed earlier, but then you'd miss out on... {i}activities.{/i}"
    n "Just something to consider. For now, you need to get ready and go to class."

    return
    
    

label runningTrackIntro:
    $ trackDiscovered = True
    $ afterClassExploration.remove("runningTrackIntro")
    
    "Before you lies a grassy field encircled by an elliptical ring made of some synthetic material. Bleachers stand tall parallel to the long axis of the ring."
    "Soccer goals rest on the ends of the field, though no game is being played at the moment. Runners jog along the ellipse, speeding past those on their cool down laps walking along the outer edge."
    "Off to the side is a section where various exercise machines and equipment are being used by athletic students. There's even a rock climbing wall over there."
    "You must have wandered into the sports side of campus."
    "Maybe you should start that fitness arc you've been postponing."
    "But where do you even start? You didn't bring clothes to run in today but you could at least take a look at the machines and figure out how they work, right?"
    "You hesitantly approach the workout area and walk past some folk who are stretching."
    "It feels like they're staring out you. You must look so out of place. Everyone here is lean or muscular or both."
    "You just try to ignore everything around you and get to an available machine."
    "Ah, here's one."
    "...Now how the hell does it work?"
    "So you sit on the bench and... your arms go... here?"
    "Wait no, you think it's actually for your legs."
    "It's not moving. How do you get it to move? Does it go the other way?"
    "Fffffuck, that cute girl over there is definitely getting weirded out from watching you."
    "Mission abort, you repeat, mission abort. You can't do this. You need a buddy to teach you how not to embarrass yourself here."
    "You dismount the machine and retreat in shame."
    
    return
    
label forestIntro:
    $ forestDiscovered = True
    $ afterClassExploration.remove("forestIntro")
    
    "At the edge of campus lies a forest with an inviting dirt trail leading into it."
    "Might as well see where it goes."
    "It goes... into the woods."
    "You don't know what you expected."
    "Every now and then you come across a fellow student walking along the trail, but it's otherwise a quiet and serene experience."
    "The sounds of nature echo in the distance from wild birds bickering among themselves to squirrels skittering along branches."
    "You occasionally catch sight of deer grazing among the grass but they vanish into the trees upon spotting you."
    "After walking for about a mile, the path ends, having looped back to the university campus."
    "Such a peaceful walk has left you feeling rejuvinated yet calm at the same time."
    
    return
    

label gardenIntro:
    $ gardenDiscovered = True
    $ afterClassExploration.remove("gardenIntro")
    
    n "Along one edge of campus lies a botanical garden where a variety of flowers, bushes and trees surround the intertwining paths like a labrynth."
    
    if avaClaireGarden == True:
        n "This is where you spent a lovely day with Ava and Claire, though you must have taken a different trail that time."
    
    n "Plaques mark the plants with their scientific names and some information about them, providing insight to their life cycles and uses."
    n "It's a pleasant walk, watching bees and butterflies fly around collecting nectar and pollen, attracted by the sweet aromas."
    n "The path goes on for a while, and it feels like you'll never escape."
    n "At some point you crossed a bridge overlooking a stream, and later come across the pond it feeds into."
    n "You watched the fish and turtles from a dock, then continued your journey through the flora while passing by greenhouses and gazebos."
    n "Surprisingly there aren't many others walking these paths. It's a nice place to get away from everything and enjoy some peace and quiet among nature."
    n "Eventually you make it out of the maze, though you're pretty sure you didn't see everything the garden has to offer."
    n "It'll have to wait for another day."

    return
    
label mainStreetIntro:
    $ townDiscovered = True
    $ afterClassExploration.remove("mainStreetIntro")
    #$ locationsAvailable.remove("townLocation")

    "A short walk off campus brings you to a commercial area. The streets are lined with restaurants and a variety of shops ranging from fashion to books, gift shops, electronics, art stores, antiques, and more."
    "It gets overwhelming quickly and you can hardly decide which shops to stop at."
    "Just doing some window shopping is enough to satisfy your curiosity for the most part."
    "You hate it when you walk into what appears to be a general clothing store, only for it to be entirely women's clothing except for a small men's section in the back."
    "You guess it's for husbands when they bring their wives shopping but since you're alone it just makes everything awkward when you have to walk past women's undergarments to get to some boring shirt."
    "Then you have to pretend to be interested then hurry out of the store before the attendant can say \"Thanks for stopping by!\""
    "Around the fifth time it happens, you decide to cut your losses and go back to your dorm."
    
    return