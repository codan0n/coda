label roriDormIntro:
    $ roriDormIntroSeen = True
    #"this is a description of rori's dorm for when you visit it for the first time"
    
    scene bg roridorm with dissolve
    
    n "Scattered throughout Rori's dorm are various electronics that heat the room to rival a sauna."
    n "The glow of several CRT monitors displaying vintage anime pierces your retinas. Toxic fumes from a soldering iron linger in the air, making you cough. The whirring of fans could drown out the sound of a jet engine."
    
    rori "Sorry about the mess. Housing pays for power so I hooked up a few crypto mining ASICs to generate some passive income."
    
    menu:
        "And kill the environment.":
            player "And destroy the environment in the process."
            
            rori "A few kilowatts is nothing in the grand scheme of things."
            rori "There's a nuclear power plant that generates plenty of electricty nearby."
        "Based electricity thief.":
            player "Based electricity thief."
            
            rori "It's not stealing if they're giving it away for free."
            rori "If they didn't want me using 6000 watts, they shouldn't have given me so many electric sockets."
            
            player "I don't think they accounted for daisy chaining power strips like that. Seems like a fire hazard."
            
            rori "Good thing they have insurance then, and I have remote backups."
    
    return
    
label avaClaireDormIntro:
    $ avaClaireDormIntroSeen = True
    
    "this is a description of Claire and Ava's dorm, to be played the first time you enter it."
    "It's split into two halves with a bed on either end. What must be Ava's side is tidy with photography books and expensive camera gear on the desk."
    "Whereas Claire's side is unkempt and disorganized. She has a tendency to leave her underwear in random places."
    
    
    return