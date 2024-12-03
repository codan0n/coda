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
define mere = Character("Mere", image="mere", color="#eeb1da", what_color="#d0dbff", callback=name_callback, cb_name = "mere", what_font="dudu.ttf")
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
define lina = Character("lina", image="lina", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define waitress = Character("waitress", image="lina", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define nicodemus = Character("Nicodemus", image="nicodemus", what_color="d0dbff", callback=name_callback, cb_name = "nicodemus", what_font="dudu.ttf")

define y_olivia = 1500
define y_margaret = 1570
define y_rori = 1565
define y_rose = 1400
define y_gunner = 1595
define y_mere = 1250
define y_herschel = 1515
define y_celestine = 1600
define y_claire = 1825
define y_kitsuragi = 1500
define y_lina = 1570
define y_ava = 1465
define y_mishka = 1550
define y_roth = 1750
define y_nicodemus = 1550
define y_trish = 1550


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
        'images/characters/nicodemus neutral.png'
    group saying:
        #xysize(1920,1080)
        xzoom .9
        yzoom .90
        pos (600,156)
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
layeredimage margaret smoking laugh:
    at sprite_highlight('margaret')
    always:
        'images/characters/margaret/margaret smoking laugh.png'
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
            

layeredimage lina:
    at sprite_highlight('lina')
    always:
        'images/characters/lina.png'
    group saying:
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
        'images/characters/kitsuragi.png'
    group saying:
        attribute say:
            "images/bubble.png"


layeredimage olivia neutral:
    at sprite_highlight('olivia')
    always:
        'images/characters/olivia neutral.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage olivia looking:
    at sprite_highlight('olivia')
    always:
        'images/characters/olivia looking.png'
    group saying:
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
            
layeredimage trish neutral:
    at sprite_highlight('trish')
    always:
        'images/characters/trish neutral.png'
    group saying:
        attribute say:
            "images/bubble.png"

layeredimage volginova neutral:
    at sprite_highlight('volginova')
    always:
        'images/characters/volginova neutral.png'
    group saying:
        attribute say:
            "images/bubble.png"
   

label start:
    # variables
    $ dating = ""
    $ currentWeather = "sunny"
    $ daysSinceRain = 1
    $ avaClaireGarden = False
    $ avaUrbex = False
    $ gunnerRaid = False
    $ gaveCinRoll = False
    $ studied = ""
    $ fratsoro = ""
    $ heshe = ""
    $ heher = ""
    $ hisher = ""
    $ himher = ""
    
    $ forestDiscovered = False
    $ libraryDiscovered = False
    $ gardenDiscovered = False
    $ trackDiscovered = False
    $ townDiscovered = False
    $ avaClaireLunch = False
    $ clairephonewhat = False
    $ clairephonethx = False
    $ statsSkill = 0
    $ frenchSkill = 0
    $ historySkill = 0
    $ literatureSkill = 0
    $ roriPoints = 0
    $ ellenPoints = 0
    $ rosePoints = 0
    $ avaPoints = 0
    $ clairePoints = 0
    
    $ currentbook = "The Death of Ivan Ilyich"
    $ nightWalkIndex = 0
    $ roseNightWalkActive = False
    $ claireNightWalkActive = False
    $ roriNightWalkActive = False
    $ avaNightWalkActive = False
    $ gunnerNightWalkActive = False
    $ ellenNightWalkActive = False
    $ mishkaNightWalkActive = False
    
    $ afterClassExploration = ["mainStreetIntro", "gardenIntro", "forestIntro", "runningTrackIntro"]
    $ townEvents = ["celestineTown", "linaTown"]
    $ trackEvents = ["gunnerTrack", "roriTrack"]
    $ forestEvents = ["roseForest" "claireForest"]
    $ gardenEvents = ["mishkaGarden"]
    $ cafeEvents = ["oliviaCafe"]
    $ nightEvents = ["gunnerNight", "avaNight", "claireNight", "mishkaNight", "roseNight", "avaGunnerNight", "roriNight"]
    #$ locationsAvailable = ["forestLocation", "gardenLocation", "townLocation", "trackLocation"]
    
    $ clairepath = False
    $ avapath = False
    $ roripath = False
    $ ellenpath = False
    $ rosepath = False
    $ mishkapath = False
    $ gaveUmbrella = False
    $ badEnd = 0
    $ goodEnd = 0
    $ boygirlfriend = ""
    $ roseTrade = False
    $ roseBias = False
    $ claireBias = False
    $ roriDormIntroSeen = False
    $ avaClaireDormIntroSeen = False

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

call chapter1
    


label ending:

    scene bg black with fade

    ###
    n "Thanks for playing!"
    n "More to come in a future update!"
    n "Credits in the \"About\" section on the main menu."
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
