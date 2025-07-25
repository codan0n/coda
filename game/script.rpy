init python:

    def claire_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sound effects/clairevoice.wav")
        elif event == "slow_done":
            renpy.sound.stop()
    
    def mere_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sound effects/clairevoice.wav")
        elif event == "slow_done":
            renpy.sound.stop()

    def herschel_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sound effects/herschel.wav")
        elif event == "slow_done":
            renpy.sound.stop()

    def celeste_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sound effects/celeste.wav")
        elif event == "slow_done":
            renpy.sound.stop()

    def roth_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sound effects/roth.wav")
        elif event == "slow_done":
            renpy.sound.stop()

    def kitsuragi_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sound effects/kitsuragi.wav")
        elif event == "slow_done":
            renpy.sound.stop()


    def rose_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sound effects/rose.wav")
        elif event == "slow_done":
            renpy.sound.stop()

    def player_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sound effects/player.wav")
        elif event == "slow_done":
            renpy.sound.stop()


    def narrator_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sound effects/narrator.wav")
        elif event == "slow_done":
            renpy.sound.stop()


    def gunner_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sound effects/gunner.wav")
        elif event == "slow_done":
            renpy.sound.stop()


    def mishka_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sound effects/mishka.wav")
        elif event == "slow_done":
            renpy.sound.stop()

    def ellen_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sound effects/ellen.wav")
        elif event == "slow_done":
            renpy.sound.stop()

    def ava_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sound effects/ava/ava.wav")
        elif event == "slow_done":
            renpy.sound.stop()

    def rori_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/sound effects/rori.wav")
        elif event == "slow_done":
            renpy.sound.stop()



    #def character_callback(event, **kwargs):
     #   if event == "end":
      #      renpy.sound.play("audio/next.wav", channel="audio")

    #config.all_character_callbacks.append(character_callback)


define spotlightimage = Character("spotlightimage", image="spotlightimage")
define n = Character("", what_color="EEEEEE", callback=name_callback, cb_name = "n", what_italic=True, what_size=37, what_font="Comfortaa-Regular.ttf")
#define player = Character("", color="#a4cffc", what_color="#a4cffc", callback=name_callback, cb_name = "player", what_font="dudu.ttf")
define player = Character("testname", color="#95d29d", what_color="#a5ac61", callback=name_callback, cb_name = "player", what_font="dudu.ttf")
define claire = Character("Claire", image="claire", color="#eeb1da", what_color="#ffd9f0", callback=name_callback, cb_name = "claire", what_font="dudu.ttf")
define guard = Character("Guard", image="guard", color="#eeb1da", what_color="#d0dbff", callback=name_callback, cb_name = "mere", what_font="dudu.ttf")
define ava = Character("Ava", image="ava", color="#fbffc8", what_color="#c8f8ff", callback=name_callback, cb_name = "ava", what_font="dudu.ttf")
define ellen = Character("Ellen", image="ellen", color="#b6e4d6", what_color="#ffe8b7", callback=name_callback, cb_name = "ellen", what_font="dudu.ttf")
define margaret = Character("Margaret", image="margaret", color="#b6e4d6", what_color="#ffe8b7", callback=name_callback, cb_name = "margaret", what_font="dudu.ttf")
define mishka = Character("Mishka", image="mishka", color="#a4cffc", what_color="#dbc9f3", callback=name_callback, cb_name = "mishka", what_font="dudu.ttf")
define rose = Character("Rose", image="rose", color="#dbb0ff", what_color="#b3a6ff", callback=name_callback, cb_name = "rose", what_font="dudu.ttf")
define rori = Character("Rori", image="rori", color="#b5d0ff", what_color="#ddd4ac", callback=name_callback, cb_name = "rori", what_font="dudu.ttf")
define gunner = Character("Gunner", image="gunner", color="#f7d2ae", what_color="#ff5497", callback=name_callback, cb_name = "gunner", what_font="dudu.ttf")
define rothbauer = Character("Mr. Rothbauer", image="rothbauer", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define herschel = Character("Mrs. Herschel", image="herschel", what_color="d0dbff", callback=name_callback, cb_name = "herschel", what_font="dudu.ttf")
define celestine = Character("Mrs. Celestine", image="celestine", what_color="d0dbff", callback=name_callback, cb_name = "celestine", what_font="dudu.ttf")
define kitsuragi = Character("kitsuragi", image="kitsuragi", what_color="d0dbff", callback=name_callback, cb_name = "kitsuragi", what_font="dudu.ttf")
define volginova = Character("Volginova", image="volginova", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define adam = Character("Adam", image="adam", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define attendant = Character("Attendant", image="attendant", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define trish = Character("Trish", image="trish", what_color="d0dbff", callback=name_callback, cb_name = "trish", what_font="dudu.ttf")
define olivia = Character("Olivia", image="olivia", what_color="d0dbff", callback=name_callback, cb_name = "olivia", what_font="dudu.ttf")
define fortune = Character("Fortune", image="fortune", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define creature = Character("Creature", image="fortune", what_color="d0dbff", what_font="dudu.ttf")
define lina = Character("lina", image="lina", what_color="d0dbff", callback=name_callback, cb_name = "lina", what_font="dudu.ttf")
define waitress = Character("waitress", image="lina", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define nicodemus = Character("Nicodemus", image="nicodemus", what_color="d0dbff", callback=name_callback, cb_name = "nicodemus", what_font="dudu.ttf")

define y_olivia = 1150
define y_margaret = 1570
define y_rori = 1565
define y_rose = 1400
define y_gunner = 1595
define y_mere = 1250
define y_herschel = 1515
define y_celestine = 1600
define y_claire = 1825
define y_kitsuragi = 1430
define y_lina = 1470
define y_ava = 1465
define y_mishka = 1550
define y_roth = 1750
define y_nicodemus = 1400
define y_trish = 1300
define y_fortune = 1100


#old mishka text color a4cffc
#old gunner color #ffb7d3, reuse for lina?
#ff0063
#old rori color  c9ddac
#old rose color dbb0ff 
#other npc color d0dbff

###thanks to https://github.com/SoDaRa/Auto-Highlight for this

define config.say_attribute_transition = Dissolve(0.07, alpha=True)

define config.say_attribute_transition_layer = "master"

#layeredimage n:
#    at sprite_highlight('n')
#    always:
#        'testimage'

#layeredimage player:
#    at sprite_highlight('player')
#    always:
#        'testimage'

layeredimage nicodemus neutral:
    at sprite_highlight('nicodemus')
    always:
        'images/characters/nicodemus/nicodemus neutral.png'
#    group lighting:
#        xzoom .9
#        yzoom .90
#        pos (600,156)
#        attribute light:
#            'images/characters/rose/rose athletic dismissive.png'
    group saying:
        #xysize(1920,1080)
        xzoom -.9
        yzoom .90
        pos (670,-83)
        attribute say:
            "images/bubble.png"
            
layeredimage ava casual excited:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava casual excited.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy angry:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy angry.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy concerned:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy concerned.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy embarrassed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy embarrassed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy excited:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy excited.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy flattered:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy flattered.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy grouchy browless:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy grouchy browless.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy grouchy:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy grouchy.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy neutral:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy neutral.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy smug:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy smug.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy suggestive:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy suggestive.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy unamused:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy unamused.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava profile overjoyed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava profile overjoyed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava casual whimsical:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava casual whimsical.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy unsure:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy unsure.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy waitwhat:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy waitwhat.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava casual unamused:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava casual unamused.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy whimsical:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy whimsical.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical neutral:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical neutral.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical shy:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical shy.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical whimsical:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical whimsical.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical suggestive:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical suggestive.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical smug:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical smug.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical concerned:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical concerned.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical enamored:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical enamored.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical motivated:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical motivated.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical unamused:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical unamused.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava pose whimsical:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava pose whimsical.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava pose smug:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava pose smug.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava pose shy:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava pose shy.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical agitated:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical agitated.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical unamused:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical unamused.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical unimpressed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical unimpressed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical shocked:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical shocked.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical happy:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical happy.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava twopiece pants unimpressed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava twopiece pants unimpressed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava twopiece pants smile:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava twopiece pants smile.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava twopiece smile:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava twopiece smile.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava twopiece flattered:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava twopiece flattered.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava portrait overjoyed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava portrait overjoyed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava suggestive:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava suggestive.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava portrait smile:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava portrait smile.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava portrait concerned:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava portrait concerned.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava casual flattered:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava casual flattered.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava glowy unimpressed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava glowy unimpressed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava unimpressedbrowless:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava unimpressedbrowless.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava reaching concerned:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava reaching concerned.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava pose unimpressed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava pose unimpressed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava flattered:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava flattered.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava embarassed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava embarassed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava smile:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava smile.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava unimpressed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava unimpressed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava reaching concerned:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava reaching concerned.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava reaching embarrassed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava reaching embarrassed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava motivated:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava motivated.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava casual happy:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava casual happy.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava seriously:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava seriously.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava pose happy:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava pose happy.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava profile embarrassed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava profile embarrassed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-135,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava reaching concerned shirtopen:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava reaching concerned shirtopen.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-135,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava profile annoyed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava profile annoyed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-135,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava profile angry:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava profile angry.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-135,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava profile whimsical:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava profile whimsical.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-135,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava profile smug:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava profile smug.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-135,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava profile happy:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava profile happy.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava casual smile:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava casual smile.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava casual angry:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava casual angry.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava casual overjoyed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava casual overjoyed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava casual unimpressed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava casual unimpressed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava casual annoyed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava casual annoyed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava casual concerned:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava casual concerned.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava casual daydream:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava casual daydream.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava unsure:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava unsure.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava concerned:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava concerned.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava waitwhat:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava waitwhat.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava pose flattered:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava pose flattered.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava pose happy:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava pose happy.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava pose ohyou:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava pose ohyou.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical glowy agitated:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical glowy agitated.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava profile shy:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava profile shy.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical embarrassed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical embarrassed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-130,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava profile concerned:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava profile concerned.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-130,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava pose angry:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava pose angry.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava pose concerned:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava pose concerned.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava pose annoyed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava pose annoyed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava bored:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava bored.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical excited:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical excited.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical angry:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical angry.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical annoyed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical annoyed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical neutral:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical neutral.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava portrait neutral:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava portrait neutral.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava typical overjoyed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava typical overjoyed.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"
layeredimage ava tipsy:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava tipsy.png'
    group saying:
        xzoom .9
        yzoom 1.0
        pos (-80,-30)
        attribute say:
            "images/bubble.png"


layeredimage celestine neutral:
    at sprite_highlight('celestine')
    always:
        'images/characters/celestine/celestine neutral.png'
    group saying:
        xzoom .7
        yzoom .60
        pos (145,106)
        attribute say:
            "images/bubble.png"
layeredimage celestine confident:
    at sprite_highlight('celestine')
    always:
        'images/characters/celestine/celestine confident.png'
    group saying:
        xzoom .7
        yzoom .60
        pos (145,106)
        attribute say:
            "images/bubble.png"
layeredimage celestine explaining:
    at sprite_highlight('celestine')
    always:
        'images/characters/celestine/celestine explaining.png'
    group saying:
        xzoom .7
        yzoom .60
        pos (145,106)
        attribute say:
            "images/bubble.png"
layeredimage celestine excited:
    at sprite_highlight('celestine')
    always:
        'images/characters/celestine/celestine excited.png'
    group saying:
        xzoom .7
        yzoom .60
        pos (145,106)
        attribute say:
            "images/bubble.png"

layeredimage claire topless surprised earsup:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire topless surprised earsup.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater happy:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater happy.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater derp:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater derp.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater flustered:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater flustered.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater giggle:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater giggle.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater happy earsup:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater happy earsup.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater hot:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater hot.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater hot earsup:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater hot earsup.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater laughing:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater laughing.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater leaning suggestive:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater leaning suggestive.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater overjoyed:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater overjoyed.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater pose happy:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater pose happy.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater pose laughing:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater pose laughing.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater pose suggestive:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater pose suggestive.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater pose suggestive earsup:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater pose suggestive earsup.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater sad:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater sad.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater suggestive:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater suggestive.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater suggestive earsup:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater suggestive earsup.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater surprised earsup:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater surprised earsup.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire sweater wave happy:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater wave happy.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
            
layeredimage claire swimsuit flannel happy:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit flannel happy.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit gasp1:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit gasp1.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit gasp2:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater swimsuit gasp2.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit happy:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit happy.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit hot:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit hot.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit laugh:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit laugh.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit leaning:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit leaning.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit leaning hot:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit leaning hot.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit leaning wink:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit leaning wink.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit sad:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit sad.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit suggestive:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit suggestive.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit suggestive earsup:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit suggestive earsup.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit surprised earsup:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit surprised earsup.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
            
layeredimage claire flannel derp:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire flannel derp.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire flannel :
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire flannel .png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire flannel flustered:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire flannel flustered.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire flannel happy:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire flannel happy.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire flannel laughing:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire flannel laughing.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire flannel sad:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire flannel sad.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire flannel suggestive:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire flannel suggestive.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire flannel surprised earsup:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire flannel surprised earsup.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"
layeredimage claire flannel wink:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire flannel wink.png'
    group saying:
        xzoom .85
        yzoom .63
        pos (150,126)
        attribute say:
            "images/bubble.png"

layeredimage margaret neutral:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret neutral.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret smoking melancholy shocked:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret smoking melancholy shocked.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret smoking intrigued shocked:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret smoking intrigued shocked.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret smoking intrigued:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret smoking intrigued.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret smoking sad shocked:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret smoking sad shocked.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret shocked leaningback:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret shocked leaningback.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret sad shocked:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret sad shocked.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret tailwag flattered:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret tailwag flattered.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret tailwag happy:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret tailwag happy.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret smoking melancholy:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret smoking melancholy.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret sad smoking:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret sad smoking.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret smoking sad shocked:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret smoking sad shocked.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret smoking intrigued:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret smoking intrigued.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret smoking happy:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret smoking happy.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret flattered:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret flattered.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret tailwag neutral:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret tailwag neutral.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret tailwag flattered:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret tailwag flattered.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret tailwag happy:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret tailwag happy.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret intrigued:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret intrigued.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret melancholy:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret melancholy.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret happy:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret happy.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret sad:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret sad.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret smoking neutral:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret smoking neutral.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"
layeredimage margaret sadsmoking:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret sad smoking.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
        attribute say:
            "images/bubble.png"

layeredimage ellen neutral:
    at sprite_highlight('ellen')
    always:
        'images/characters/ellen/ellen neutral.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage ellen happy:
    at sprite_highlight('ellen')
    always:
        'images/characters/ellen/ellen happy.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage ellen proud:
    at sprite_highlight('ellen')
    always:
        'images/characters/ellen/ellen proud.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage ellen smug:
    at sprite_highlight('ellen')
    always:
        'images/characters/ellen/ellen smug.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage ellen overjoyed:
    at sprite_highlight('ellen')
    always:
        'images/characters/ellen/ellen overjoyed.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage ellen skates:
    at sprite_highlight('ellen')
    always:
        'images/characters/ellen/ellen skates.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage ellen annoyed:
    at sprite_highlight('ellen')
    always:
        'images/characters/ellen/ellen annoyed.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage ellen laugh:
    at sprite_highlight('ellen')
    always:
        'images/characters/ellen/ellen laugh.png'
    group saying:
        attribute say:
            "images/bubble.png"
            
            
layeredimage fortune:
    at sprite_highlight('fortune')
    always:
        'images/characters/fortune.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,69)
        attribute say:
            "images/bubble.png"
            
            
layeredimage gunner neutral:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner neutral.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner annoyed:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner annoyed.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner charming:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner charming.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner cheeky1:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner cheeky1.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner cutie:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner cutie.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner determined:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner determined.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner disgusted:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner disgusted.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner displeased:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner displeased.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner eyesclosed catface:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner eyesclosed catface.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner eyesclosed smile:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner eyesclosed smile.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner frown1:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner frown1.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner gruff:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner gruff.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner hissing:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner hissing.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner itsover:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner itsover.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner mischief:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner mischief.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner motivated:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner motivated.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner optimistic:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner optimistic.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner pissed:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner pissed.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner snoring:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner snoring.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner uncomfy:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner uncomfy.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner wink catface:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner wink catface.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
layeredimage gunner wink frown:
    at sprite_highlight('gunner')
    always:
        'images/characters/gunner/gunner wink frown.png'
    group saying:
        xzoom .8
        yzoom .72
        pos (105,57)
        attribute say:
            "images/bubble.png"
        

layeredimage herschel:
    at sprite_highlight('herschel')
    always:
        'images/characters/herschel/herschel neutral.png'
    group saying:
        xzoom .85
        yzoom .72
        pos (70,29)
        attribute say:
            "images/bubble.png"
            

layeredimage lina neutral:
    at sprite_highlight('lina')
    always:
        'images/characters/lina/lina neutral.png'
    group saying:
        xzoom .95
        yzoom .95
        pos (50,-10)
        attribute say:
            "images/bubble.png"
layeredimage lina sax neutral:
    at sprite_highlight('lina')
    always:
        'images/characters/lina/lina sax neutral.png'
    group saying:
        xzoom .95
        yzoom .95
        pos (50,-10)
        attribute say:
            "images/bubble.png"


            
layeredimage mere neutral:
    at sprite_highlight('mere')
    always:
        'images/characters/mere/mere.png'
    group saying:
        xzoom .9
        yzoom .95
        pos (-120,7)
        attribute say:
            "images/bubble.png"




layeredimage mishka jacketless frown:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless frown.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless nervous anxious:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless nervous anxious.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless nervous sad:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless nervous sad.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless nervous sleep:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless nervous sleep.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless nervous tongueout 2:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless nervous tongueout 2.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless nervous tongueout:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless nervous tongueout.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless nervous wink 2 tongueout:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless nervous wink 2 tongueout.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless nervous wink:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless nervous wink.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless nervous:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless nervous.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless neutral:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless neutral.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless overjoyed:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless overjoyed.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless sad2 nervous:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless sad2 nervous.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless sleep:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless sleep.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless tongueout:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless tongueout.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless wink 1:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless wink 1.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless wink 2 tongueout:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless wink 2 tongueout.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless wink tongueout:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless wink tongueout.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka jacketless wink:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka jacketless wink.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka neutral standing:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka neutral standing.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka standing frown:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka standing frown.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka standing overjoyed:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka standing overjoyed.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka standing sleep:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka standing sleep.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka standing tongueout:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka standing tongueout.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka standing wink 1 tongueout:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka standing wink 1 tongueout.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka standing wink 1:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka standing wink 1 tongueout.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka standing wink 2 tongueout:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka standing wink 2 tongueout.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka standing wink 2:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka standing wink 2.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka anxious sad:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka anxious sad.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka anxious smile:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka anxious smile.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka tired happy:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka tired happy.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka nervous sad:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka nervous sad.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka nervous2:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka nervous 2.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka anxious tongueout wink left:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka anxious tongueout wink left.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka asleep:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka asleep.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka anxious neutral:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka anxious neutral.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka neutral wink right:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka neutral wink right.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka neutral wink left:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka neutral wink left.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka neutral tongueout wink right:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka neutral tongueout wink right.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka anxious wink right:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka anxious wink right.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka neutral:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka neutral.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka nervous:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka nervous.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka teasing:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka teasing.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka saddest:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka saddest.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka shy:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka shy.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka shy smile:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka shy smile.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka cute:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka cute.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka nya:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka nya.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka despondent:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka despondent.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka hopeful:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka hopeful.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka happy wink:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka happy wink.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka winki:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka winki.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka anxious:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka anxious.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka anxious grin:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka anxious grin.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka shy grin:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka shy grin.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka shy:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka shy.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka silly wink:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka silly wink.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka wave sad:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka wave sad.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka happy:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka happy.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka wincing2:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka wincing 2.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka mousey wink right:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka mousey wink right.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka ceremonial neutral:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka ceremonial.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka derp:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka derp.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"    
layeredimage mishka ceremonial happy:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka hap ceremonial.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka hat neutral:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka hat neutral.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka hat happy:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka hat happy.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka hat sad:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka hat sad.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka hat depressed:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka hat depressed.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka sad:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka sad.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka depressed:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka depressed.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka shy sad:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka shy sad.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka neutral eyesclosed:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka neutral eyesclosed.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
layeredimage mishka neutral eyesclosed tongueout:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka neutral eyesclosed tongueout.png'
    group saying:
        xzoom .95
        yzoom 1
        pos (-70,-7)
        attribute say:
            "images/bubble.png"
            
            
layeredimage kitsuragi:
    at sprite_highlight('kitsuragi')
    always:
        'images/characters/kitsuragi/kitsuragi.png'
    group saying:
        xzoom .8
        yzoom .7
        pos (80,-22)
        attribute say:
            "images/bubble.png"


layeredimage olivia neutral:
    at sprite_highlight('olivia')
    always:
        'images/characters/olivia/olivia neutral.png'
    group saying:
        xzoom 1.1
        yzoom 1.1
        pos (-20,-88)
        attribute say:
            "images/bubble.png"
layeredimage olivia looking:
    at sprite_highlight('olivia')
    always:
        'images/characters/olivia/olivia looking.png'
    group saying:
        xzoom 1.1
        yzoom 1.1
        pos (-20,-88)
        attribute say:
            "images/bubble.png"
    
    
    
    
layeredimage rori furious:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori furious.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori angry neutral:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori angry neutral.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori angry rat:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori angry rat.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori angry:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori angry.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed angry:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed angry.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed anxious:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed anxious.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed asleep:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed asleep.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed cheery blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed cheery blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed cheery:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed cheery.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed concerned blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed concerned blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed concerned:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed concerned.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed drunk:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed drunk.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed embarrassed:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed embarrassed.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed embarrassed2:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed embarrassed2.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed flattered:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed flattered.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed happy lookingaway blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed happy lookingaway blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed laugh eyeopen:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed laugh eyeopen.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed laugh:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed laugh eyeopen.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed neutral lookingaway:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed neutral lookingaway.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed neutral:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed neutral.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed silly:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed silly.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed sleepy blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed sleepy blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed sleepy:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed sleepy.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed smile blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed smile blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed smile:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed smile.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed supersmug blushing lookingaway:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed supersmug blushing lookingaway.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed supersmug:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed supersmug.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed surprised eyesclosed:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed surprised eyesclosed.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed surprised:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed surprised.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed worried:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed worried.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed worried2:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed worried2.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed yawn lookingaway blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed yawn lookingaway blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori armscrossed:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori armscrossed.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori drunk alert armscrossed:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori drunk alert armscrossed.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat anxious:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat anxious.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat anxious2:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat anxious2.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat asleep:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat asleep.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat blushing:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat blushing.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat cheery blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat cheery blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat concerned blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat concerned blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat concerned:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat concerned.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat drunk alert:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat drunk alert.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat drunk:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat drunk.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat embarrassed:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat embarrassed.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat embarrassed2:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat embarrassed2.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat flattered blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat flattered blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat laugh eyeopen:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat laugh eyeopen.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat laugh:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat laugh.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat neutral:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat neutral.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat sassy:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat sassy.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat silly:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat silly.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat sleepy blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat sleepy blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat sleepy:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat sleepy.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat smile:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat smile.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat supersmug blushing lookingaway:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat supersmug blushing lookingaway.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat supersmug:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat supersmug.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat surprised:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat surprised.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat worried:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat worried.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat worried2:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat worried2.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat yawn lookingaway blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat yawn lookingaway blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori sassy:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori sassy.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori neutral:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori neutral.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori rat neutral:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori rat neutral.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori embarrassed:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori embarrassed.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori concerned blushing:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori concerned blushing.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori surprised:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori surprised.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori neutral lookingaway:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori neutral lookingaway.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori sleepy blushing:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori sleepy blushing.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori concerned:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori concerned.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori worried:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori worried.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori smug:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori smug.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori supersmug blushing:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori supersmug blushing.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori supersmug:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori supersmug.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori asleep:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori asleep.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori worried noblush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori worried noblush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori cheery blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori cheery blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori smirk lookingaway:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori smirk lookingaway.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori smirk blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori smirk blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori smirk:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori smirk.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori soyface smug:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori soyface smug.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori soyface:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori soyface.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori drunk alert:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori drunk alert.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori cheery:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori cheery.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori flattered blushing:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori flattered blushing.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori happy:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori happy.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori sleepy:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori sleepy.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori smile lookingaway:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori smile lookingaway.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori smile lookingaway blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori smile lookingaway blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori yawn blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori yawn blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori yawn lookingaway blush:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori yawn lookingaway blush.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori sleepy:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori sleepy.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori concerned:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori concerned.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori neutral blushing:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori neutral blushing.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori anxious:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori anxious.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"
layeredimage rori drunk:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori drunk.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"            
layeredimage rori pantslessdrunk:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori pantslessdrunk.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"            
layeredimage rori laugh:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori laugh.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"            
layeredimage rori pantsless:
    at sprite_highlight('rori')
    always:
        'images/characters/rori/rori pantsless.png'
    group saying:
        xzoom .75
        yzoom .6
        pos (4,33)
        attribute say:
            "images/bubble.png"



layeredimage rose jacket fistsclenched angry:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose jacket fistsclenched angry.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose jacket handonhip furious:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose jacket handonhip furious.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose jacket fistsclenched angry knife:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose jacket fistsclenched angry knife.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose jacket handonhip dismissive:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose jacket handonhip dismissive.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose jacket fistsclenched annoyed:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose jacket fistsclenched annoyed.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose jacket handonhip shy:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose jacket handonhip shy.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose jacket handonhip annoyed:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose jacket handonhip annoyed.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose jacket armscrossed dismissive:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose jacket armscrossed dismissive.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose jacket armscrossed furious:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose jacket armscrossed furious.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose jacket handonhip growling:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose jacket handonhip growling.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt handonhip dismissive pendant:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt handonhip dismissive pendant.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose athletic irritated:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose athletic irritated.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose athletic dismissive lookingaway:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose athletic dismissive lookingaway.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose athletic dismissive:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose athletic dismissive.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose athletic furious:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose athletic furious.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt armscrossed shy pendant:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt armscrossed shy pendant.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt furiouspose pendant:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt furiouspose pendant.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt armscrossed furious pendant:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt armscrossed furious pendant.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt fistsclenched angry pendant:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt fistsclenched angry pendant.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt armscrossed dismissive:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose armscrossed dismissive.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose armscrossed dismissive pendant:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt armscrossed dismissive pendant.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt handonhip smug pendant:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt handonhip smug pendant.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt fistsclenched angry:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt fistsclenched angry.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt armscrossed annoyed pendant:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt armscrossed annoyed pendant.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt armscrossed annoyed:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt armscrossed annoyed.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt handonhip annoyed:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt handonhip annoyed.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt handonhip annoyed pendant:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt handonhip annoyed pendant.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt armscrossed dismissive pendant:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt armscrossed dismissive pendant.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt armscrossed dismissive:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt armscrossed dismissive.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt handonhip shy pendant:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt handonhip shy pendant.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt handonhip dismissive:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt handonhip dismissive.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt handonhip smug:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt handonhip smug.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt handonhip shy:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt handonhip shy.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt armscrossed unsure:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt armscrossed unsure.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt furiouspose:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt furiouspose.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"
layeredimage rose skirt furiouspose pendant:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt furiouspose pendant.png'
    group saying:
        xzoom -.9
        yzoom .9
        pos (625,-62)
        attribute say:
            "images/bubble.png"

    
layeredimage rothbauer:
    at sprite_highlight('rothbauer')
    always:
        'images/characters/rothbauer.png'
    group saying:
        xzoom .9
        yzoom .8
        pos (220,147)
        attribute say:
            "images/bubble.png"
            
layeredimage trish notext neutral:
    at sprite_highlight('trish')
    always:
        'images/characters/trish/trish notext neutral.png'
    group saying:
        xzoom .65
        yzoom .68
        pos (160,121)
        attribute say:
            "images/bubble.png"

layeredimage volginova neutral:
    at sprite_highlight('volginova')
    always:
        'images/characters/volginova neutral.png'
    group saying:
        attribute say:
            "images/bubble.png"
   




# variables

default dating = ""
default currentWeather = "sunny"
default daysSinceRain = 1
default currentbook = "The Death of Ivan Ilyich"


#need to order these approximately chronologically
default currentSeason = "summer"
default calledRoriNerd = False
default metGunner = False
default metClaire = False
default metAva = False
default signedUpForSorority = False
default signedUpForFraternity = False
default avaClaireLunch = False
default cafeLightsOn = False
default acceptedGunnersMoney = False
default wantToTravel = False
default claireFrenchSession = 0
default trolledAva = False
default mishkaMall = False
default mishkaMallSpecialActive = False
default mishkaMallSpecialPlayed = False
default calledClaireFat = 0
default chosenHobby = "none"
default gaveUmbrella = False
default historyCheated = False
default readArcoonianBook = False
default avaClaireGarden = False
default roseTrade = False
default photoWithClaire = False
default photoWithAva = False
default writingHistoryPaper = False
default guessEllensAge = 0
default intoFatChicks = True
default reallyIntoFatChicks = False
default clairephonewhat = False
default clairephonethx = False
default avaUrbex = False
default gunnerRaid = False
default avaPantsu = False
default clairePantsu = False
default roseNicodemusCampusScene = False
default gnugift = False
default stayedInHospitalWithGunner = False
default snuggledWithAva = False
default avaSnugglePlus = False
default metFortune = False
default heardFortune = False
default money = 0
default moneySpent = 0
default gaveCinRoll = False
default spicyVictory = False
default rejectedAvasproposal = False
default beakOrTailfeathers = ""
default fixedRosesCassette = False
default claireBullyLevel = 0
default playerBullyLevel = 0
default youGay = False
default foughtGunner = False
default claireCommitted = False
default avaCommitted = False
default roriCommitted = False
default stayedUpWithClaire = False
default romanticFantasy = False
default celestineHot = False
default almostKissedClaire = False
default roseLibraryMidterms = False
default avaLibraryMidterms = False
default suspicionOfDean = False
default mishkaMidtermWeekendHangout = False
default spatInRosesCoffee = False
default drankOliviasCoffee = False
default avaLibraryAdventure = False

default roseNightWalkLvl = 1
default gunnerNightWalkLvl = 1
default roriNightWalkLvl = 1
default avaNightWalkLvl = 1
default claireNightWalkLvl = 1
default ellenNightWalkLvl = 1
default mishkaNightWalkLvl = 1

default statsSkill = 0
default frenchSkill = 0
default historySkill = 0
default literatureSkill = 0

default roryPoints = 0
default roriPoints = 0
default gunnerPoints = 0
default ellenPoints = 0
default rosePoints = 0
default avaPoints = 0
default mishkaPoints = 0
default clairePoints = 0
default badEnd = 0
default goodEnd = 0
default roseBias = 0
default claireBias = 0

default nightWalkIndex = 0
default roseNightWalkActive = False
default claireNightWalkActive = False
default roriNightWalkActive = False
default avaNightWalkActive = False
default gunnerNightWalkActive = False
default ellenNightWalkActive = False
default mishkaNightWalkActive = False

default forestDiscovered = False
default libraryDiscovered = False
default gardenDiscovered = False
default trackDiscovered = False
default townDiscovered = False

default afterClassExploration = ["mainStreetIntro", "gardenIntro", "forestIntro", "runningTrackIntro"]
default townEvents = []#"linaTown", "celestineTown"]
default trackEvents = ["gunnerTrack"]#, "roriTrack"]
default forestEvents = [] #["roseForest", "claireForest"]
default gardenEvents = ["mishkaGarden"]
default cafeEvents = ["oliviaCafe"]
default libraryEvents = []
default nightEvents = ["avaNight", "claireNight", "mishkaNight", "roseNight", "roriNight"] #re-add gunnerNight when it's ready
default locationsAvailable = ["forestLocation", "gardenLocation", "townLocation", "trackLocation"]

default clairepath = False
default avapath = False
default roripath = False
default ellenpath = False
default rosepath = False
default mishkapath = False

default roriDormIntroSeen = False
default avaClaireDormIntroSeen = False


label start:
    
    #places characters centered
    transform norm:
        yalign 0
        
    transform slowhop:
        linear .19 ypos 18
        linear .19 ypos 0

    transform hop:
        yoffset 15
        linear .18 yoffset 0
        #linear .05 yalign 1.1
        #linear .1 yalign 1.0

    transform hopaway:
        linear .15 xpos -400 ypos -30
        linear .08 xpos -500 ypos 0
        pause .08
        linear .15 xpos -600 ypos -30
        linear .08 xpos -700 ypos 0
        pause .08
        linear .15 xpos -800 ypos -30
        linear .08 xpos -900 ypos 0
        pause .08
        linear .15 xpos -1000 ypos -30
        linear .08 xpos -1100 ypos 0
        linear .15 xpos -1400
        pause .08
        linear .15 xpos -1400
    
    transform hopback:
        xpos -1400 ypos 0
        linear .15 xpos -1200 ypos -30
        linear .08 xpos -1000 ypos 0
        pause .08
        linear .15 xpos -800 ypos -30
        linear .08 xpos -600 ypos 0
        pause .08
        linear .15 xpos -400 ypos -30
        linear .08 xpos -400 ypos 0
        
        

    transform flipright:
        yoffset 14
        xzoom -1
        linear .17 yoffset 0
    transform flipleft:
        yoffset 14
        xzoom 1
        linear .17 yoffset 0
    transform fliphop:
        yalign 1.1
        xzoom -1
        linear .25 yalign 0
    transform fliphop2:
        ypos 1095
        xzoom 1
        linear .05 ypos 1080


    transform shudder:
        xoffset 5
        pause .021
        xoffset 0
        pause .021
        xoffset -5
        pause .021
        xoffset 0
        pause .021
        xoffset 5
        pause .021
        xoffset 0
        pause .021
        xoffset -5
        pause .021
        xoffset 0
        pause .021
        xoffset 5
        pause .021
        xoffset 0
        xoffset -5
        pause .021
        xoffset 0
        pause .021
        xoffset 5
        pause .021
        xoffset 0
        xoffset -5
        pause .021
        xoffset 0

    transform righter:
        xalign 1.0
    transform lefter:
        xalign 0.0


    
###testing
    
    #scene bg campus
    #show box with Dissolve(.2):
    #    ypos 0
    #n "welcome"
    #n "This is claire"
    
    
    
    #show claire sw neu at center:
    #    xpos -175
    #    xzoom -1
    #show ellen neutral at center:
    #    xpos -460
    #    xzoom -1
    #show rose neutral at center:
    #    xpos -670
    #    xzoom -1
    #show mishka neutraltral at center:
    #    xpos 220
    #show rori neutraltral at center:
    #    xpos 585
    #show ava typical neutraltral at center:
    #    xpos 810
    
    #n "Choose your waifu"

####end testing
#
#python:
#    from enum import Enum
#    
#    #slot = Enum('A', 'B', 'C', 'D', 'E')
#
#    class Weekday(Enum):
#
#        MONDAY = 1
#
#        TUESDAY = 2
#
#        WEDNESDAY = 3
#
#        THURSDAY = 4
#
#        FRIDAY = 5
#
#        SATURDAY = 6
#
#        SUNDAY = 7
#    
#    n(str(Weekday.WEDNESDAY.name))
#    
#    n(str(Weekday(1).name))
#    
#    i = 2
#    
#    if i == 1:
#        n(str(Weekday(i).name))
#    elif i == 2:
#        n(str(Weekday(i).name))
#        
#        
#    pastryenum = Enum('pastryenum', [muffin, cupcake, croissant])
#        
#    #later
#    n "later..."
#    
#    menu:
#        "What pastry do you want?"
#            "muffin":
#                "you have chosen your pastry"
#                pastry = MUFFIN
#            "cupcake":
#                "you have chosen your pastry"
#                pastry = CUPCAKE
#            "croissant":
#                "you have chosen your pastry"
#                pastry = CROISSANT
#    
#    if pastry = MUFFIN:
#        n "ya got a muffin"
#    elif pastry = CUPCAKE:
#        n "ya got a cupcake"
#    elif pastry = CROISSANT:
#        n "ya got a croissant"
#    else:
#        n "code ain't working"
#        
#    n "fin"

call chapter1 from _call_chapter1
    
label nothinglol:
    scene bg black
    
    n "Thanks for playing!"
    n "More to come in future updates!"
    
    return

label ending:

    scene bg black with fade

    ###
    n "Thanks for playing!"
    n "More to come in future updates!"
    ###n "Credits in the \"About\" section on the main menu."
    #n "sprite highlighting code: Sodora"
#    n "Writing: - Codanon, anonymous"
#
#    n "Art: anonymous, @birdsarealright, @lizardsart89, @_zokhan, @_ronvi/@wiskors, @majisuta022, @rexhastala, @spakka5, @baronboar, machapigeon, Mono/Proton, Loanshark, @videobun_art, @PennsArtStudio, @ljesak, @Katnay3, @BaronBoar, Nevrax Design Team"
#
#    n "Music: Mere Notilde, Vylet Pony ({a=https://www.youtube.com/@VyletPony/videos}Check her out omg she's amazing{/a}), Evan Schaeffer"
#
#    n "Misc: Phone UI: Nadianova"
#    #https://nadianova.itch.io/phone-message-system-for-renpy
#    #https://lemmasoft.renai.us/forums/viewtopic.php?t=40245
#
#    #n "Dangerously based: @spakka5, @rexhastala"
#    #for doing free art
#    n "Notably based: @spakka5, @rexhastala, Mono, machapigeon, @lizardsart89, Loanshark, Vylet"

    n "twitter.com/codavn"

    return
