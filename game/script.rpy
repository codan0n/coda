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
define mere = Character("Mere", image="mere", color="#eeb1da", what_color="#d0dbff", callback=name_callback, cb_name = "other", what_font="dudu.ttf")
define ava = Character("Ava", image="ava", color="#fbffc8", what_color="#c8f8ff", callback=name_callback, cb_name = "ava", what_font="dudu.ttf")
define ellen = Character("Ellen", image="ellen", color="#b6e4d6", what_color="#ffe8b7", callback=name_callback, cb_name = "ellen", what_font="dudu.ttf")
define margaret = Character("Margaret", image="margaret", color="#b6e4d6", what_color="#ffe8b7", callback=name_callback, cb_name = "margaret", what_font="dudu.ttf")
define mishka = Character("Mishka", image="mishka", color="#a4cffc", what_color="#dbc9f3", callback=name_callback, cb_name = "mishka", what_font="dudu.ttf")
define rose = Character("Rose", image="rose", color="#dbb0ff", what_color="#b3a6ff", callback=name_callback, cb_name = "rose", what_font="dudu.ttf")
define rori = Character("Rori", image="rori", color="#b5d0ff", what_color="#ddd4ac", callback=name_callback, cb_name = "rori", what_font="dudu.ttf")
define gunner = Character("Gunner", image="gunner", color="#f7d2ae", what_color="#ff5497", callback=name_callback, cb_name = "gunner", what_font="dudu.ttf")
define rothbauer = Character("Mr. Rothbauer", image="rothbauer", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define herschel = Character("Mrs. Herschel", image="herschel", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define celestine = Character("Mrs. Celestine", image="celestine", what_color="d0dbff", callback=name_callback, cb_name = "celestine", what_font="dudu.ttf")
define kitsuragi = Character("kitsuragi", image="kitsuragi", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define volginova = Character("Volginova", image="volginova", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define adam = Character("Adam", image="adam", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define attendant = Character("Attendant", image="attendant", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define trish = Character("Trish", image="trish", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define olivia = Character("Olivia", image="olivia", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define fortune = Character("Fortune", image="fortune", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define creature = Character("Creature", image="fortune", what_color="d0dbff", what_font="dudu.ttf")
define lina = Character("lina", image="lina", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define waitress = Character("waitress", image="lina", what_color="d0dbff", callback=name_callback, cb_name = "other1", what_font="dudu.ttf")
define nicodemus = Character("Nicodemus", image="nicodemus", what_color="d0dbff", callback=name_callback, cb_name = "nicodemus", what_font="dudu.ttf")

define y_margaret = 1570
define y_rori = 1565
define y_rose = 1400
define y_gunner = 1485
define y_herschel = 1485
define y_celestine = 1600
define y_claire = 1570
define y_ava = 1465
define y_mishka = 1550
define y_roth = 1550
define y_nicodemus = 1550


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
layeredimage ava reaching embarassed:
    at sprite_highlight('ava')
    always:
        'images/characters/ava/ava reaching embarassed.png'
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
        attribute say:
            "images/bubble.png"
layeredimage celestine happy:
    at sprite_highlight('celestine')
    always:
        'images/characters/celestine/celestine neutral.png'
    group saying:
        attribute say:
            "images/bubble.png"

layeredimage claire sweater neutral:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater neutral.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit sad:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit sad.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire sweater pose neutral:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater pose neutral.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire outdoors derp:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire outdoors derp.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit lusty:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit lusty.png'
    group saying:
        attribute say:
            "images/bubble.png"

layeredimage claire swimsuit flannel neutral:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit flannel neutral.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire sweater pose lusty:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater pose lusty.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire sweater pose lusty alert:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater pose lusty alert.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire outdoors lusty:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire outdoors lusty.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire outdoors embarassed:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire outdoors embarassed.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire outdoors horny:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire outdoors horny.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire outdoors derp:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire outdoors derp.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire outdoors heyeah:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire heyeah.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire outdoors sad:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire outdoors sad.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire sweater wave lusty alert:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater wave lusty alert.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire sweater neutral alert:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater neutral alert.png'
    group saying:
        attribute say:
            "images/bubble.png"

layeredimage claire sweater pose laugh:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater pose laugh.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire sweater pose lusty alert:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater pose lusty alert.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire sweater lusty alert:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater lusty alert.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire sweater lusty:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater lusty.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire sweater cry:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater cry.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire sweater derp:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater derp.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire sweater embarassed:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater embarassed.png'
    group saying:
        attribute say:
            "images/bubble.png"            
layeredimage claire sweater giggle:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater giggle.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire sweater heyeah:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater heyeah.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire sweater leaning:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater leaning.png'
    group saying:
        attribute say:
            "images/bubble.png"            
layeredimage claire sweater overjoyed:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater overjoyed.png'
    group saying:
        attribute say:
            "images/bubble.png"            
layeredimage claire sweater surprised:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater surprised.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire sweater wave:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire sweater wave.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire outdoors neutral:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire outdoors neutral.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire outdoors surprised:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire outdoors surprised.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire outdoors heyeah:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire outdoors heyeah.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit neutral:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit neutral.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit surprised:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit surprised.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit heyeah:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit heyeah.png'
    group saying:
        attribute say:
            "images/bubble.png"
layeredimage claire swimsuit leaning:
    at sprite_highlight('claire')
    always:
        'images/characters/claire/claire swimsuit leaning.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (0,88)
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
        'images/characters/gunner neutral.png'
    group saying:
        xzoom .9
        yzoom .75
        pos (545,223)
        attribute say:
            "images/bubble.png"
        

layeredimage herschel:
    at sprite_highlight('herschel')
    always:
        'images/characters/herschel.png'
    group saying:
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
layeredimage mishka sad wave:
    at sprite_highlight('mishka')
    always:
        'images/characters/mishka/mishka sad wave.png'
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



layeredimage rose skirt handonhip annoyed:
    at sprite_highlight('rose')
    always:
        'images/characters/rose/rose skirt handonhip annoyed.png'
        xzoom -1
    group saying:
        xzoom .9
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
    $ dndnight = False
    $ gaveCinRoll = False
    $ studied = ""
    $ fratsoro = ""
    $ heshe = ""
    $ heher = ""
    $ hisher = ""
    $ himher = ""
    
    $ forestDiscovered = False
    $ gardenDiscovered = False
    $ trackDiscovered = False
    $ townDiscovered = False
    $ avaClaireLunch = False
    $ clairephonewhat = ""
    $ clairephonethx = ""
    $ roriparty = ""
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
    
label gunner_rage:
    n "Wait, how did you get here again?"
    
    play music "audio/music/mere - schooldaze.ogg" fadein 1.0

    show rose neutral pendant at center with moveinright

    rose @ say "Are you gonna move or what? You're blocking the doorway."

    player "Huh? Oh, sorry."

    n "You step forward into the classroom and take your seat with Rose following behind you."

    show rose neutral at offscreenleft with move:
        yalign 0

    n "Shortly afterward, Mr. Rothbauer comes in and begins the lesson for the day."

    show rothbauer at center with dissolve

    rothbauer @ say "Good morning, class!"
    rothbauer @ say "Today we'll be going over"

    show bg static1
    pause .02
    show bg static3
    pause .04
    show bg static2
    pause .03
    show bg classroom

   
    scene bg lecturehall

    play music "audio/music/mere - schooldaze faster.ogg" fadein 1.5

    show box:
        ypos 0

    show gunner neutral at center:
        xzoom -1
        xpos -475

    show herschel at center

    herschel @ say "Ahem! Gunner!"

    n "You look over to Gunner, who's banging his head to the beat of whatever he's listening to on his headphones."
    n "You reach out and tap his shoulder and he opens his eyes."

    gunner @ say "Huh? What's up?"

    #show gunner

    herschel @ say "It's time for class to begin, dear."

    n "He seems to realize where he is and sheepishly takes off his headphones."
    
    herschel @ say "Maybe if you spent a little less time listening to music and more time studying, you'd have passed this class last time."

    gunner @ say "Mmh..."

    n "Ouch."
    n "What a mean thing to say."
    n "Aren't teachers supposed to be kind and uplifting?"
    #n "Wait no, where'd you get that crazy idea lol"
    n "You feel for Gunner. Dude just wanted to relax before class started."

    hide gunner with dissolve

    herschel @ say "Now that I have everyone's attention, please open your books to page 43."
    
    n "You pick up your pencil and prepare to take notes."
    n "Mrs. Herschel ends up going too fast for you to keep up but you write down what you can."

    stop music fadeout 1.0

    scene bg campus with fade

    play music "audio/ambient/outdoors people talking.ogg" fadein .5

    show gunner neutral at center with dissolve:
        xzoom -1

    show box:
        ypos 0

    n "Gunner sulks next to you quietly as the two you walk away from the math building."

    gunner @ say "..."
    gunner @ say "GOD FUCKING DAMMIT I HATE THAT BITCH"

    #show gunner angry

    player "Whoa what?"

    gunner @ say "Earlier when Mrs. Herschel got onto me!"
    gunner @ say "Fucking boomers."
    gunner @ say "She's probably just mad music wasn't invented yet back when she was a student!"

    n "Gunner punches the brick wall of a building you were passing by."

    player "Holy shit that looked like it hurt! You alright bro?"

    n "Gunner takes a few breaths and recomposes himself."

    show gunner neutral

    gunner @ say "Sorry, I'm just pissed off all because of this stupid math class."

    player "You just don't have the mind for this kind of stuff. Not everyone does. You're good at other things."

    gunner @ say "If only schools saw it that way."
    gunner @ say "I hate how I'm getting stuck on this *one* class!"

    player "Don't worry bro, you'll pass this semester and then you'll never have to worry about it ever again."

    gunner @ say "Heh, yeah..."

    n "Gunner seems to relax a little."

    gunner @ say "Hey, you wanna go get lunch together? I know a good place a short walk off campus. It's my treat!"

    player "Yeah man, lunch sounds good right about now."

    gunner @ say "Sweet! They say a good meal can turn a bad day around, y'know!"

    player "Then what are we waiting for? Let's go!"

    hide gunner with dissolve

    stop music fadeout 1.0

    n "Gunner returns to his usual cheerful self as you walk to the restaurant."
    n "The food ended up being really good too."
    n "Just... expensive."
    n "You're glad Gunner offered to pay."

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show tmonday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7


    #___tuesday2
label ellen_rage:
    scene bg codadorm with fade

    play music "audio/ambient/morning birds.ogg" fadein .5

    show box:
        ypos 0

    n "Mornings are already starting to blend together. It's all the same, you wake up, get ready for class and head out."
    n "Not much room for variation other than which dinosaurs you get in your dino egg oatmeal."
    n "You loved those sugary \"eggs\" as a kid, but tragically you went through an edgy teen phase where you refused to eat such a silly meal."
    n "Now that you're an adult you've come to the conclusion that dinosaur egg oatmeal is based as fuck."
    n "That satisfying crunch and blast of flavor puts it well in the god tiers of breakfasts."
    #n "You usually end up eating most of the sugary \"eggs\" before they hatch"
    n "You got a lot of stegosauruses today."
    n "There's probably like a horoscope or something for this."
    n "You look it up and bookmark the page on your phone for later reading. You've got to focus on literature for now."

    stop music fadeout .9


    
    scene bg codadorm with fade

    show box:
        ypos 0

    n "Man, why do you feel so sleepy all of a sudden? You felt fine just a few minutes ago."
    n "Luckily you made it through class. Your future self is gonna hate you for not doing the homework you planned to do tonight though."
    n "You kick off your shoes and crawl into bed, not even bothering to feed your online addiction before closing your eyes and falling asleep."

    #___wednesday2
label passout:

    play music "audio/ambient/morning birds.ogg" fadein .5

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    n "When you wake up the following morning, you feel a bit groggy but still functional."
    #n "You roll out of bed without a problem. Maybe yesterday was just a fluke. Maybe something you ate didn't set well with you?"
    n "You perform your usual morning routine and prepare to head out."

    #show bg static3
    #pause .02

    #show bg codadorm

    stop music fadeout .5

    scene bg campus with fade

    play music "audio/ambient/outdoors people talking.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "It's a lovely day out. Sun shines through the clouds and a light breeze rustles the leaves in the trees."
    n "You make it about halfway to the history building when you start to feel strange again."

    show bg static2
    pause .02
    show bg campus

    n "It becomes difficult to breathe and you feel a sharp pain in your head."
    n "Your vision begins to fade as you drop down to your hands and knees."

    show bg static1
    pause .02
    show bg static2
    pause .02
    show bg campus

    n "The last thing you recall is slumping to the ground and hearing someone call your name."

    rori @ say "[name]!!"

    stop music fadeout .5

    hide box


    #___thursday2
label hospital_bound:

    scene bg black with fade

    n "..."
    n "....."
    n "......."

    scene bg hospital with fade

    show box with Dissolve(.2):
        ypos 0

    play music "audio/music/Mere Notilde - Empty Room.ogg" 

    show box with Dissolve(.2):
        ypos 0

    n "...Huh?"
    n "Where are you?"
    n "You hear beeps from a heart monitor."
    n "You try to look around but your whole body is aching."

    show rori neutral at center with dissolve

    rori @ say "[name]? You're finally awake!"
    rori @ say "Wait right here, I'll go get the kitsuragi!"
    
    gunner "{nw}"
    show rori at offscreenleft with move:
        yalign 0

    n "Before you can even respond, he runs out of the room."
    n "Did he bring you here? How long have you been out?"

    show kitsuragi at offscreenright:
        yalign 0

    n "He returns a few minutes later with a kitsuragi."

    show rori neutral at center:
        xzoom -1
        xpos 1400
    show kitsuragi at center:
        xpos 450
    with move

    kitsuragi @ say "Hello, [name]. First thing's first, how are you feeling? You seem to have taken a nasty fall but I'm more concerned about what may have caused it in the first place."

    player "Well... my body feels pretty sore in general and I feel exhausted and dehydrated."

    rori @ say "Oh, I've got a bottle of water if you need it!"

    n "Rori digs around in his backpack and hands you the bottle."
    n "You can barely reach your arm up to grasp it and opening the lid proves to be a challenge."
    n "The kitsuragi writes something on her clipboard."

    kitsuragi @ say "Have you been experiencing these symptoms or any other strange sensations lately?"

    player "Err kinda? I've been having dizzy spells since the other day and I passed out in class yesterday."
    player "And I've been feeling really thirsty all the time, even though I've been drinking a lot of water."
    
    show rori anxious

    rori @ say "Y-you passed out in class?!"

    kitsuragi @ say "You realize that's a bit out of the ordinary, don't you?"

    player "I guess I figured it would just sorta fix itself if I ignored it..."

    kitsuragi @ say "Well I'm sorry to say that we're not gonna be able to release you in this condition. We'll need to take all sorts of tests to determine the cause of these dizzy spells."

    player "Oh..."

    kitsuragi @ say "You should thank your friend here. Not only did he carry you here, but he stayed overnight waiting for you to wake up."

    player "I guess that is a lot to do for someone you barely know... Thanks Rori."
    
    show rori neutral

    rori @ say "Oh it was nothing, really! If anything, you saved me from going to class!"

    player "Heh. Yeah."
    #player "Wait did you say you've been here since yesterday?"

    #rori @ say "Yeah! I was starting to wonder if you'd ever wake up!"

    kitsuragi @ say "In any case, I would encourage you to return home, Rori. We'll keep a close eye on [name]."

    rori @ say "Hmm... Alright."

    n "Rori looks somewhat disappointed but understanding."

    player "Here Rori, lemme give you my phone number so I can update you when they find out what's wrong with me."

    n "Rori immediately brightens up and pulls out his phone."

    rori @ say "Sure! What is it?"

    n "You tell him your number and he types it into his contact list."

    rori @ say "Aaaaand done!"
    rori @ say "Well, I'll let you get some rest now. Hope you feel better soon!"

    player "Thanks Rori!"

    n "He grabs his backpack and gives you a fist bump on his way out."

    hide rori with dissolve

    n "The kitsuragi waits for Rori to be out of earshot before sighing and turning to you."

    kitsuragi @ say "Given your... situation..."
    kitsuragi @ say "I don't want to jump to conclusions, but you know what these symptoms remind me of?"

    player "Yeah... I figured it was only a matter of time but I never expected it to happen so soon."

    kitsuragi @ say "Hey, we still don't know it's that for sure. It could be anything."
    kitsuragi @ say "We'll get started on some tests soon. There's no point in worrying until we have a proper diagnosis."
    kitsuragi @ say "I'll be back in a little bit."

    hide kitsuragi with dissolve

    n "The disease that took your parents' lives, as well as the lives of billions of humans... could you be experiencing its effects?"
    n "Nihil syndrome... Not much is even known about it. Nobody knows where it came from, how it's contracted, or how to cure it."
    n "It just showed up one day and only affects humans. Even people who were completely isolated somehow got infected."
    n "Evidence suggests it's a flaw in your DNA, like a ticking time bomb for humanity but some claim it's alien in origin."
    n "Others believe it's a government conspiracy to wipe out humanity. Or maybe it's retribution from God."
    n "You don't really know what to believe."
    n "Maybe you are just jumping to conclusions. There's still no confirmation you have it. For now."

    #stop music fadeout 1.0

    hide box

    scene bg black with fade

    hide box


    #___friday2

    scene bg hospital with fade

    #play music "audio/music/Evan Schaeffer - Encomium.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "After several hours worth of tests, they made you stay the night here."
    n "You're already tired of this place. You hate being here."
    n "But they insist that you stay at least until they can get the dizzy spells under control."
    n "At least now you have a convenient excuse for falling behind in class."

    play audio "audio/sound effects/vibrate.ogg"

    n "Huh? Sounds like you got a text. You reach for your phone."

    call phone_start from _call_phone_start_3

    call message_start("Gunner", "Why did you skip stats lol", "gunneravi.png") from _call_message_start_3

    call reply_message("Wasn't feeling well, went to the doctor.") from _call_reply_message_11

    call message("Gunner", "Oh shit for real??? Are you ok", "gunneravi.png") from _call_message_10

    call reply_message("Yeah just fell down and stuff.") from _call_reply_message_12

    call message("Gunner", "Alright well I hope you feel better soon", "gunneravi.png") from _call_message_11
    call message("Gunner", "BTW herschel said to do the homework problems for lesson 2-3", "gunneravi.png") from _call_message_12

    call reply_message("Thanks") from _call_reply_message_13

    call message("Gunner", "See you on Monday!", "gunneravi.png") from _call_message_13

    call phone_end from _call_phone_end_3

    n "Gunner is probably still lost in that class. Maybe you should work on the homework so you don't fall too far behind."
    n "..."
    n "Or you could feed your addiction to trolling on Sudanese ceremonial rug weaving image boards."

    show phonechan1 at center with dissolve:
        xpos 700
        ypos 200

    n "You could spend hours doing this."
    n "In fact, you used to waste your life away on this god forsaken site every day."
    n "You can't count the number of times you've been banned, but no bioluminescent government officials have shown up at your doorstep so you must be doing something right."
    #n "As you scroll through, looking for (you)s, something catches your eye."
    #n "Is that... fanart? Of that story you started writing and posting online in freshman year of high school?"
    #n "Yup, it's unmistakable, that is definitely your ponysona you made for it. Hey, they were in style at the time."
    #show ms paint pony on the chan
    #n "But why would Anonymouse just randomly post that image? It has nothing to do with their post."
    #n "Maybe they clicked it by accident."
    #n "Why would they even have it on their hard drive?"
    #n "Maybe they were a fan? But after all these years, it's hard to imagine someone still cares about that old thing, especially when you can barely remember it."
    #n "You do remember abandoning it right after posting a gigantic cliffhanger though."
    #n "Your fans are probably pissed about that lol"
    #n "Life got in the way though."
    #n "You got pretty far into development but like everything you've done, it's half baked and left to rot."
    #n "All the ideas you had for the next update start to trickle back into your head."
    #n "Maybe once you get out of this hellhole you'll search for that flash drive that had the latest draft on it."
    #n "You spend a while reminiscing about the times you were semi-internet popular back in the days before you could become a millionaire making reaction videos to projects like this."
    #n "Oh well. It's getting late. You should try and get some sleep."
    n "Time flies by and it starts getting late. You should try and get some sleep."

    hide phonechan1 with dissolve

    n "You put away your phone and make yourself as comfortable as you can in your dumb little hospital bed and close your eyes."
    
    stop music fadeout 1.0

    hide box

    scene bg black with fade

    hide box


    #___saturday3

    scene bg hospital with fade

    #play music "audio/ai8.ogg" fadein 1.0
    #play music "audio/music/Evan Schaeffer - React.ogg" fadein 1.0
    
    show box with Dissolve(.2):
        ypos 0
    
    play music "audio/music/Evan Schaeffer - Encomium.ogg" fadein .5

    n "What a waste of a weekend."
    n "It's already Saturday evening and still no word of when you'll be able to leave this place."
    n "You should just get up and walk away. What are they gonna do, call the police and arrest you?"

    play audio "audio/sound effects/vibrate.ogg"
    
    n "Hm?"

    call phone_start from _call_phone_start_4

    call message_start("Ava", "Hey [name] I heard you weren't feeling well so I just wanted to check in on you.", "avaavi.png") from _call_message_start_4

    call reply_message("Hey Ava. Yeah everything's fine, just feeling a little under the weather.") from _call_reply_message_14

    call message("Ava", "Oh nooo ;^;", "avaavi.png") from _call_message_14
    call message("Ava", "Hopefully nothing serious?", "avaavi.png") from _call_message_15

    call reply_message("Nah but I'm confined to bed unfortunately.") from _call_reply_message_15

    call message("Ava", "Dang, I was gonna see if you wanted to come to this party with me and Claire..", "avaavi.png") from _call_message_16

    call reply_message("Sorry, I would totally go if I could :/") from _call_reply_message_16

    call message("Ava", "That's fine, there will be plenty more parties I'm sure! ^v^", "avaavi.png") from _call_message_17
    call message("Ava", "Get well soon~", "avaavi.png") from _call_message_18

    call reply_message("Thank") from _call_reply_message_17

    call phone_end from _call_phone_end_4
    
    pause .2

    n "God."
    n "DAMMIT"
    n "Not only is this bullshit mystery disease possibly threatening your life, it's destroying your social life as well."
    n "This is not the college experience you were promised by those Hollywoof movies."
    n "You sit and wallow in your frustration until you get yet another text."

    call phone_start from _call_phone_start_5

    call message_start("Rori", "Hey you never texted me back after the other day. Did they let you go?", "roriavi.png") from _call_message_start_5

    call reply_message("No, they want me to stay here until they're sure I won't randomly pass out in the middle of the street again.") from _call_reply_message_18

    call message("Rori", "Oh hecc", "roriavi.png") from _call_message_19
    call message("Rori", "Need me to bring you anything ?", "roriavi.png") from _call_message_20

    call reply_message("Nah I'm good. I got my school books and stuff.") from _call_reply_message_19
    call reply_message("Thanks tho") from _call_reply_message_20

    call message("Rori", "Ah alright", "roriavi.png") from _call_message_21
    call message("Rori", "Hey uh can I get your input on something?", "roriavi.png") from _call_message_22

    call reply_message("?") from _call_reply_message_21

    call message("Rori", "So there's this party going on tonight... do you think I should go to it??", "roriavi.png") from _call_message_23

    call reply_message("Why wouldn't you?") from _call_reply_message_22

    call message("Rori", "I dunno", "roriavi.png") from _call_message_24
    call message("Rori", "Parties make me anxious", "roriavi.png") from _call_message_25
    call message("Rori", "I mean that thing on the rooftop was fun but idk", "roriavi.png") from _call_message_331

    call screen phone_reply("Yeah go for it","choice1","If you don't wanna go, don't go","choice2")

    label choice1:
        #finished
        $ roriPoints = roriPoints + 1
        $ roriparty = True
        call phone_after_menu from _call_phone_after_menu

        call message_start("me", "Yeah go for it", "testimage.png") from _call_message_start_6
        call reply_message("It'll be fine") from _call_reply_message_23

        call message("Rori", "Hmmmm", "roriavi.png") from _call_message_27
        call message("Rori", "Ok!", "roriavi.png") from _call_message_28
        call message("Rori", "If I don't enjoy it I can just leave lol", "roriavi.png") from _call_message_29
        call message("Rori", "Thanks [name]!", "roriavi.png") from _call_message_30
        call message("Rori", "I'll text you later!", "roriavi.png") from _call_message_31

        call reply_message("Have fun") from _call_reply_message_24

        jump aftermenu

    label choice2:
        #untested
        call phone_after_menu from _call_phone_after_menu_1
        call message_start("me", "If you don't wanna go, don't go", "testimage.png") from _call_message_start_7

        call message("Rori", "Yeah but...", "roriavi.png") from _call_message_32
        call message("Rori", "Nah you're right. I'm no party animal.", "roriavi.png") from _call_message_33
        call message("Rori", "I have better things to do with my time anyway.", "roriavi.png") from _call_message_34
        call message("Rori", "Talk to you later [name]", "roriavi.png") from _call_message_35

        call reply_message("Later") from _call_reply_message_25

        jump aftermenu


label aftermenu:
    call phone_end from _call_phone_end_5

    n "Dammit, why did Rori have to remind you of that party you're missing out on?"
    n "You've got nothing to do here but play with your phone and study."
    n "Speaking of which, you have some reading to catch up on for literature class."
    n "Then there's the math problems Gunner told you about."
    n "Wouldn't be a bad idea to study history either."
    n "Or you could say screw that and go back to the internet."

    menu:
        n "{cps=0}You can either do that or work on the math problems Gunner told you about.{/cps}"
        "Read for literature":
            #finished
            $ ellenPoints = ellenPoints + 1
            $ studied = "lit"
            n "You lean over and reach into your backpack to pull out your copy of \"The Death of Ivan Ilyich.\""
            n "Luckily you had your headphones in your bag as well. You put them on and get to reading."
            n "\"The past history of Ivan Ilyich's life was most simple and ordinary and most terrible...\""
        "Work on stats homework":
            #finished
            $ roriPoints = roriPoints + 1
            $ studied = "stats"
            n "You lean over and reach into your backpack to pull out your stats textbook."
            n "Luckily you had your headphones in your bag as well. You put them on and get to studying."
            n "\"Given the rarity of a particular disease .02 and the chance of a false negative .08, find the probability that a patient actually has the disease if the test yields a positive result...\""
        "Study history":
            #finished
            $ rosePoints = rosePoints + 1
            $ studied = "history"
            n "You don't have any homework in history but it would still do you some good to crack open the textbook and do a bit of studying for the test."
            n "Luckily you had your headphones in your bag as well. You put them on and start reading."
            n "You don't remember where class left off so you flip to a random page."
            n "In his final moments before his execution, the leader of the expedition famously said to the Arcoonian tribe..."
        "Browse pinstagram":
            #finished
            $ avaPoints = avaPoints + 1
            n "You know what, you really don't feel like doing homework right now."
            n "Instead, you'd like to indulge in the finer arts society has to offer."
            n "You tap the pinstagram app on your phone and instantly receive a dopamine rush as dozens of random images crowd your screen."
            n "After a bit of scrolling, you stumble upon Ava's profile."
            n "The software must have automatically detected you have her number in your contacts and added her to your news feed."
            n "Sometimes the FBI agent monitoring your internet connections is pretty cool like that."
            n "Ava's got some nice pics on here. Just like she said, she's really into landscape shots."
            n "Some of these look like they're taken from high up. She's probably perched in a tree judging by the looks of it."
            n "Kinda makes you wanna go out and explore. If only you weren't basically held prisoner here."

    scene bg black with fade

    play audio "audio/sound effects/vibrate.ogg"

    n "*Buzz buzz*"

    scene bg hospital with fade

    show box with Dissolve(.2):
        ypos 0

    n "You look around as your brain scrambles to recall where you are."
    n "Oh right, you're still in this dreadful hospital."
    n "You must have fallen asleep while you were studying."
    n "You check your phone and see you just received a new message from Claire."

    hide box

    call phone_start from _call_phone_start_6

    call message_start("Claire", "Heyyyyyyy [name] c:", "claireavi.png") from _call_message_start_8

    call reply_message("Hey?") from _call_reply_message_26

    call message("Claire", "I mnt to text u earlrie but got distractedddddddd sorry", "claireavi.png") from _call_message_36

    call reply_message("It's ok") from _call_reply_message_27

    call message("Claire", "Wishj u werehere w tih us", "claireavi.png") from _call_message_37

    call reply_message("?") from _call_reply_message_28

    call message("Claire", "Me an d ava", "claireavi.png") from _call_message_38
    call message("Claire", "We 're at pqrty", "claireavi.png") from _call_message_39
    call message("Claire", "Partyr", "claireavi.png") from _call_message_40
    call message("Claire", "Panties", "claireavi.png") from _call_message_41
    call message("Claire", "Party", "claireavi.png") from _call_message_42

    call reply_message("Oh") from _call_reply_message_29
    call reply_message("How is it") from _call_reply_message_30

    call message("Claire", "Im drunk olo", "claireavi.png") from _call_message_43
    call message("Claire", "Lol", "claireavi.png") from _call_message_44

    call reply_message("Cool") from _call_reply_message_31

    call message("Claire", "Ur cute btw", "claireavi.png") from _call_message_45

    call screen phone_reply("What?","choice3","Thanks?","choice4")

    label choice3:
        #finished
        $ clairephonewhat = True

        call phone_after_menu from _call_phone_after_menu_2

        call message_start("me", "What?", "testimage.png") from _call_message_start_9

        call message("Claire", "What?", "claireavi.png") from _call_message_46

        call reply_message("...") from _call_reply_message_32
        call reply_message("Idk") from _call_reply_message_33
        call reply_message("Nvm") from _call_reply_message_34

        call message("Claire", "Wait", "claireavi.png") from _call_message_47

        call reply_message("?") from _call_reply_message_35

        call message("Claire", "Nvm", "claireavi.png") from _call_message_48

        call reply_message("aargh") from _call_reply_message_36

        call message("Claire", "Aav advised me to 'shut the hell up oh my god'", "claireavi.png") from _call_message_49

        call reply_message("Maybe you should take her advice") from _call_reply_message_37

        call message("Claire", "Idc if I regert th is later but fuck it", "claireavi.png") from _call_message_50
        call message("Claire", "Srsly I think your cute and I wann a kiss youre face", "claireavi.png") from _call_message_51
        call message("Claire", "Ok wow rude", "claireavi.png") from _call_message_52

        call reply_message("Sorry, I'm just frustrated cause I'm stuck in this hospital potentially dying and can't party with you") from _call_reply_message_38

        call message("Claire", "...", "claireavi.png") from _call_message_53
        call message("Claire", "Are you being sarcasm ?", "claireavi.png") from _call_message_54

        call reply_message("maybe idk") from _call_reply_message_39
        call reply_message("fuk") from _call_reply_message_40

        call phone_end from _call_phone_end_6

        show bg static1
        pause .05
        show bg hospital

        stop music fadeout 2.0

        show box with Dissolve(.2):
            ypos 0

        n "The headache returns with a vengeance and your phone drops to the floor."

        show bg static2
        pause .05

        show bg hospital

        n "Your head hurts so much."

        show bg static1
        pause .05
        show bg static3
        pause .05
        show bg static1
        pause .05
        show bg static2
        pause .05

        show bg hospital

        n "You shut your eyes tight and before you even realize it, you're out cold."

        hide box

        show bg static2
        pause .1
        show bg static1
        pause .1
        show bg static3
        pause .1
        show bg static2
        pause .1
        show bg static3
        pause .1
        show bg static2
        pause .1
        show bg static1
        pause .1
        show bg static3
        pause .1
        show bg static2
        pause .1
        show bg static3
        pause .1

        jump aftermenu2

    label choice4:
        #untested
        $ clairePoints = clairePoints + 1
        $ clairephonethx = True

        call phone_after_menu from _call_phone_after_menu_3
        call message_start("me", "Thanks?", "testimage.png") from _call_message_start_10

        call message("Claire", "Ur welcome cutie~ ksksksksks ;)", "claireavi.png") from _call_message_55

        call reply_message("Ok i think you've had too much to drink") from _call_reply_message_41

        call message("Claire", "Naaaaahhhhh you should see Ava tho omg", "claireavi.png") from _call_message_56
        call message("Claire", "Literal featherweight", "claireavi.png") from _call_message_57

        call reply_message("Sounds like a good time") from _call_reply_message_42
        call reply_message("Wish I wasn't stuck in this stupid hospital") from _call_reply_message_43

        call message("Claire", "Yeah ;(", "claireavi.png") from _call_message_58
        call message("Claire", "Hold on", "claireavi.png") from _call_message_59
        call message("Claire", "I got smth thatll cheer u up", "claireavi.png") from _call_message_60

        call reply_message("What is it") from _call_reply_message_44
        call reply_message("????") from _call_reply_message_45

        call message("Claire", "Sry keep u waiiting, took a bit to conmvince ava", "claireavi.png") from _call_message_61
        call message_img("Claire", "Enjoy~", "pic1.png") from _call_message_img
        #claire sends pic of her and ava lifting their shirts, claire sticking out her tongue seductively, ava winking and throwing peace sign

        call reply_message("BOOBA") from _call_reply_message_46

        call phone_end from _call_phone_end_7

        show bg static2
        pause .05

        show bg hospital

        stop music fadeout 2.0

        show box with Dissolve(.2):
            ypos 0

        n "Your phone slips out of your hand and falls to the floor as an immense headache washes over you."

        show bg static1
        pause .05
        show bg static3
        pause .05
        show bg static1
        pause .05
        show bg static2
        pause .05


        show bg hospital

        n "Your head hurts so much."

        n "You shut your eyes tight and before you even realize it, you're out cold."

        hide box

        show bg static2
        pause .1
        show bg static1
        pause .1
        show bg static3
        pause .1
        show bg static2
        pause .1
        show bg static3
        pause .1
        show bg static2
        pause .1
        show bg static1
        pause .1
        show bg static3
        pause .1
        show bg static2
        pause .1
        show bg static3
        pause .1


        jump aftermenu2


label aftermenu2:

    stop music fadeout 1.0

    scene bg black with fade

    n "..."

    #___sunday3
label leaving_hospital:

    scene bg hospital with fade

    play music "audio/ambient/morning birds.ogg" fadein 0.1

    show box with Dissolve(.2):
        ypos 0

    n "Morning light shines through the window."
    n "What day is it?"
    n "How much longer are you gonna be stuck here?"
    n "You reach over to the nightstand for your phone."
    n "Wait a second, didn't you drop it last night? How'd it end up back here?"

    show kitsuragi at center with dissolve:
        xpos 0

    kitsuragi @ say "Good morning, [name]. How are you feeling?"

    player "Better than last night. Had another one of those migraines but I'm fine now."

    kitsuragi @ say "Well I have some good news for you."
    kitsuragi @ say "While we don't know for certain what's causing these migraines and dizzy spells, we managed to get ahold of something that should reduce their intensity."

    n "The kitsuragi tosses a bottle of pills at you."

    kitsuragi @ say "Read the instructions carefully otherwise ya might die."
    kitsuragi @ say "...I'm kidding! Well, kinda. Seriously, read the instructions. Two a day. Any more than that and you're bound to experience some strange side effects."
    kitsuragi @ say "Contact us immediately if you experience another one of these incidents."

    player "You mean I'm free to go?"

    kitsuragi @ say "That's correct. We ask that you take it easy though since we don't know what exactly triggers the symptoms you've been experiencing."
    kitsuragi @ say "In the mean time, we'll continue our tests and we'll let you know as soon as we know anything."

    player "So you still don't know if I have nihil syndrome? Like, when would the tests show if I have it or not?"

    kitsuragi @ say "It's hard to say. We don't have all the equipment here to test for it so we had to send your blood across the country to find out."
    kitsuragi @ say "From what we can tell here though, you appear to be fine. I actually really doubt it's nihil. You said you started experiencing symptoms shortly after you moved here, right?"
    kitsuragi @ say "Well, city water isn't as pure as they'd like you to believe. If you can, try drinking bottled water or get one of those fancy filters."

    player "Damn government putting chemicals in the water."

    kitsuragi @ say "Haha yeah."

    n "She helps you out of bed and makes sure you can walk before letting you loose."

    kitsuragi @ say "Stay safe, kid. Don't hesitate to call us with any questions you may have!"

    player "Thanks. I'll let you know if anything comes up."

    kitsuragi @ say "You better!"

    hide kitsuragi with dissolve

    n "The kitsuragi accompanies you to the lobby and sees you out."

    n "From there, you decide to head back to your dorm and chill in the comfort of your own home, away from that gross hospital."

    stop music fadeout 1.0

    scene bg codadorm with fade

    #play music "audio/ai3.ogg" fadein 1.0
    #play music "audio/music/Evan Schaeffer - Bonita.ogg" fadein 1.0
    play music "audio/music/vylet pony - Reading at Night.ogg"

    show box with Dissolve(.2):
        ypos 0

    n "After taking a shower and fixing yourself a bowl of cereal, you nestle up in bed and check on your texts."

    if clairephonethx == True:

        call phone_start from _call_phone_start_7

        call message_start("Claire", "Ahahahah I k new youd like tht~", "claireavi.png") from _call_message_start_11
        call message("Claire", "Plenty more where that came from~", "claireavi.png") from _call_message_62
        call message("Claire", "...", "claireavi.png") from _call_message_63
        call message("Claire", "[name]?", "claireavi.png") from _call_message_64
        call message("Claire", "Hellooooooo ?", "claireavi.png") from _call_message_65

        call reply_message("Hey sorry I fell asleep") from _call_reply_message_47
        call reply_message("I think that pic you sent almost killed me lmao") from _call_reply_message_48

        call message("Claire", "Rly?? Lmao", "claireavi.png") from _call_message_66
        call message("Claire", "Man last night was wild. You shoulda been there!", "claireavi.png") from _call_message_67

        call reply_message("Believe me, there's no other place I would have rather been.") from _call_reply_message_49
        call reply_message("Oh I'm free from the hospital btw!") from _call_reply_message_50

        call message("Claire", "No way! We should celebrate!", "claireavi.png") from _call_message_68

        call reply_message("Yeah lol I'm interested in what that 'plenty more where that came from' really meant") from _call_reply_message_51

        call message("Claire", "OMG ksksksksks", "claireavi.png") from _call_message_69
        call message("Claire", "You'll have to buy me a few drinks first ;)", "claireavi.png") from _call_message_70

        call reply_message("That, I can do.") from _call_reply_message_52

        call message("Claire", "Mmmmaybe wait til next weekend when I'm not hungover lol", "claireavi.png") from _call_message_71
        call message("Claire", ":P", "claireavi.png") from _call_message_72
        call message("Claire", "Ava says hi btw", "claireavi.png") from _call_message_73

        call reply_message("Tell her I said hi") from _call_reply_message_53
        call reply_message("Also thx for the pic last night >:3") from _call_reply_message_54

        call message("Claire", "Ksksksksks she says she'll kill you if you show anyone that pic!", "claireavi.png") from _call_message_74

        call reply_message("Never would have thought she'd be camera shy~") from _call_reply_message_55

        call message("Claire", "She'd really kill you if you said that to her LOL", "claireavi.png") from _call_message_75

        call reply_message("Heh") from _call_reply_message_56
        call reply_message("Well I'll let you get back to your hangover. I'll see you in French tomorrow!") from _call_reply_message_57

        call message("Claire", "See yaaaaaa!!!!", "claireavi.png") from _call_message_76
        call message("Claire", "Cutie~ :3", "claireavi.png") from _call_message_77

        call phone_end from _call_phone_end_8

    elif clairephonewhat == True:
        call phone_start from _call_phone_start_8

        call message_start("Claire", "Uhh ok?????", "claireavi.png") from _call_message_start_12
        call message("Claire", "I mean I just gace y ou a conplimemt nd u kinda just blew up on me so", "claireavi.png") from _call_message_78
        call message("Claire", "Whatevr", "claireavi.png") from _call_message_79
        call message("Claire", "[name]?", "claireavi.png") from _call_message_80
        call message("Claire", "Hellooooooo ?", "claireavi.png") from _call_message_81

        call reply_message("Hey sorry I fell asleep") from _call_reply_message_58
        call reply_message("Again, sorry about last night. I wasn't feeling well.") from _call_reply_message_59
        call reply_message("Good news is that I'm out of the hospital now and they gave me some pills that may or may not help with that.") from _call_reply_message_60

        call message("Claire", "Ohmygosh I'm sooooo sorry about all that!", "claireavi.png") from _call_message_82
        call message("Claire", "I was being so cringe Dx", "claireavi.png") from _call_message_83

        call reply_message("What no, I was being cringey") from _call_reply_message_61

        call message("Claire", "Lol let's just say we both were", "claireavi.png") from _call_message_84
        call message("Claire", "And let's agree never to speak of it again, k?", "claireavi.png") from _call_message_85

        call reply_message("Lmao k") from _call_reply_message_62
        call reply_message("How was the party?") from _call_reply_message_63

        call message("Claire", "It was fun! Me and Ava had a great time!", "claireavi.png") from _call_message_86
        call message("Claire", "Hangovers are a biiiitch tho", "claireavi.png") from _call_message_87

        call reply_message("I can imagine.") from _call_reply_message_64

        call message("Claire", "I hope you're feeling better than us lol", "claireavi.png") from _call_message_88

        call reply_message("I'm feeling alright") from _call_reply_message_65
        call reply_message("For now") from _call_reply_message_66

        call message("Claire", "Das gud", "claireavi.png") from _call_message_89
        call message("Claire", "I got worried when you said you were in the hospital,", "claireavi.png") from _call_message_90

        call reply_message("Meh, it's nothing serious.") from _call_reply_message_67
        call reply_message("These pills should help") from _call_reply_message_68

        call message("Claire", "Hope so!", "claireavi.png") from _call_message_91

        call reply_message("Lol") from _call_reply_message_69
        call reply_message("Well I'll let you get back to your hangover. I'll see you in French tomorrow!") from _call_reply_message_70

        call message("Claire", "See yaaaaaa!!!!", "claireavi.png") from _call_message_92

        call phone_end from _call_phone_end_9

    n "You eat your cereal while watching videos, remembering to take one of your pills."
    n "The kitsuragi said to take it easy, so you're just gonna relax in bed all day."
    n "You should probably text Rori and let him know you're out of the hospital."
    n "It's literally the least you could do considering he took you there in the first place."
    n "How he even managed to carry you all the way there is pretty impressive."
    n "You guess it's those gains finally paying off from hitting up the gym with Gunner."

    if roriparty == True:
        call phone_start from _call_phone_start_9

        call message_start("me", "Hey Rori", "testimage.png") from _call_message_start_13
        call reply_message("I made it out of the hospital alive") from _call_reply_message_71

        call message("Rori", "Sup [name]", "roriavi.png") from _call_message_93
        call message("Rori", "Nice! Did they find out what was wrong with you?", "roriavi.png") from _call_message_94

        call reply_message("Nope!") from _call_reply_message_72
        call reply_message("They gave me some pills tho") from _call_reply_message_73

        call message("Rori", "That's something at least.", "roriavi.png") from _call_message_95
        call message("Rori", "I hope it's nothing serious.", "roriavi.png") from _call_message_96

        call reply_message("Nah don't worry about it.") from _call_reply_message_74
        call reply_message("How was the party last night?") from _call_reply_message_75

        call message("Rori", "It was pretty crazy! I had a few beers and talked to people and did stuff", "roriavi.png") from _call_message_97

        call reply_message("A few beers and talking to people is what you consider crazy?") from _call_reply_message_76

        call message("Rori", "I mean for me yes that is pretty crazy!", "roriavi.png") from _call_message_98
        call message("Rori", "Gunner was there too", "roriavi.png") from _call_message_332 
        call message("Rori", "He dared me to send you a dick pic", "roriavi.png") from _call_message_333 
        call message("Rori", "I was so drunk I almost did!", "roriavi.png") from _call_message_334 
        
        call screen phone_reply("You should have","roripicyes","lmao that's so wacky","roripicno")
        
        label roripicyes:
            #finished
            $ roriPoints = roriPoints + 1
            
            call phone_after_menu from _call_phone_after_menu_14 

            call message_start("me", "You should have", "testimage.png") from _call_message_start_42 

            call message("Rori", "OWO", "roriavi.png") from _call_message_335 
            call message("Rori", "Haha quit joking around [name]", "roriavi.png") from _call_message_336 

            call reply_message("It would have been super funny") from _call_reply_message_247 
                
            call message("Rori", "Oh yeah? Well maybe next time I'm drunk then :P", "roriavi.png") from _call_message_337 
        
        label roripicno:
            #finished
            call phone_after_menu from _call_phone_after_menu_15 

            call message_start("me", "lmao that's so wacky", "testimage.png") from _call_message_start_43 

            call message("Rori", "Ikr? Can you imagine me ever doing that?", "roriavi.png") from _call_message_338 
            
            call reply_message("Still sounds like you had a wild time") from _call_reply_message_248 
        
        call reply_message("Fuck I wish I could have gone to the party") from _call_reply_message_78

        #call message("Rori", "Heheh thanks ^^;", "roriavi.png") from _call_message_100
        call message("Rori", "To think I never would have gone if you hadn't told me to lol", "roriavi.png") from _call_message_101
        call message("Rori", "There will be other parties tho", "roriavi.png") from _call_message_102

        call reply_message("Yeah") from _call_reply_message_79

        #call message("Rori", "I'm actually pretty excited now!", "roriavi.png") from _call_message_103

        #call reply_message("Attaboy") from _call_reply_message_80

        call message("Rori", "You doin anything for the rest of today", "roriavi.png") from _call_message_104
        call message("Rori", "?", "roriavi.png") from _call_message_105

        call reply_message("I gotta chill in bed. Doctor's orders.") from _call_reply_message_81

        call message("Rori", "Ah makes sense", "roriavi.png") from _call_message_339 
        call message("Rori", "Let me know if you need anything!", "roriavi.png") from _call_message_340 

        call reply_message("Anything?") from _call_reply_message_249

        call message("Rori", "Within reason!", "roriavi.png") from _call_message_341 

        call reply_message("Like goat boi dick pics?") from _call_reply_message_250
        
        call message("Rori", "Bahhh! >.<", "roriavi.png") from _call_message_342 
        
        call reply_message("Hehehe just teasin'") from _call_reply_message_251

        call phone_end from _call_phone_end_10
    else:
        call phone_start from _call_phone_start_10

        call message_start("me", "Hey Rori", "testimage.png") from _call_message_start_14
        call reply_message("I made it out of the hospital alive") from _call_reply_message_83

        call message("Rori", "Sup [name]", "roriavi.png") from _call_message_109
        call message("Rori", "Nice! Did they find out what was wrong with you?", "roriavi.png") from _call_message_110

        call reply_message("Nope!") from _call_reply_message_84
        call reply_message("They gave me some pills tho") from _call_reply_message_85

        call message("Rori", "That's something at least.", "roriavi.png") from _call_message_111
        call message("Rori", "I hope it's nothing serious.", "roriavi.png") from _call_message_112

        call reply_message("Nah don't worry about it.") from _call_reply_message_86
        call reply_message("What did you end up doing last night?") from _call_reply_message_87

        call message("Rori", "Well I was working on fixing a bug in a program and I got frustrated so I left and went for a walk to clear my mind", "roriavi.png") from _call_message_113
        call message("Rori", "And I ended up bumping into this girl and we chatted for a while", "roriavi.png") from _call_message_114
        #it's rose

        call reply_message("Niiice") from _call_reply_message_252
        call reply_message("You get her number?") from _call_reply_message_253 

        call message("Rori", "I did!", "roriavi.png") from _call_message_343 
        call message("Rori", "I'm way too nervous about texting her though", "roriavi.png") from _call_message_344 
        
        call reply_message("Why?") from _call_reply_message_254
        
        call message("Rori", "Idk she's just... kinda intimidating?", "roriavi.png") from _call_message_345 
        call message("Rori", "Goth girl vibes and such", "roriavi.png") from _call_message_346 
        
        call reply_message("Jackpot") from _call_reply_message_255
        
        call message("Rori", "lol i know", "roriavi.png") from _call_message_347 
        call message("Rori", "What you doin", "roriavi.png") from _call_message_348 
        call message("Rori", "?", "roriavi.png") from _call_message_349 
        
        #call message("Rori", "We got along pretty well and I was thinking of asking if she'd like to do something with me this weekend", "roriavi.png") from _call_message_116

        #call reply_message("I guess it turned out for the better that you didn't go to that party after all.") from _call_reply_message_89

        #call message("Rori", "Yup!", "roriavi.png") from _call_message_117
        #call message("Rori", "Thanks for telling me not to go lol", "roriavi.png") from _call_message_118

        #call reply_message("Hey it was entirely your choice") from _call_reply_message_90

        #call message("Rori", "Yeah but you helped influence it", "roriavi.png") from _call_message_119

        #call reply_message("If you say so") from _call_reply_message_91

        #call message("Rori", "You doin anything for the rest of today", "roriavi.png") from _call_message_120
        #call message("Rori", "?", "roriavi.png") from _call_message_121

        call reply_message("I gotta chill in bed all day. Doctor's orders.") from _call_reply_message_92

        call message("Rori", "Ah makes sense", "roriavi.png") from _call_message_122
        call message("Rori", "I gotta work on some homework", "roriavi.png") from _call_message_123
        call message("Rori", "Let me know if you need anything!", "roriavi.png") from _call_message_350 

        call reply_message("Thx lol. Text you later") from _call_reply_message_93

        call phone_end from _call_phone_end_11

    n "Sounds like everyone else had a fun weekend."
    n "You feel like you were robbed of yours."
    n "At least you're no longer trapped in that hospital. It was starting to feel like you were being held prisoner there."
    n "You can relax."
    n "For now."
    n "You still have class in a few hours after all."
    n "When it comes time for you to go to bed, you pop another one of those pills, as instructed."
    n "You're already getting sick of them but you gotta do what you gotta do to stay alive you guess."
    n "You rest your head on your pillow and pray nothing bad happens tomorrow as sleep overtakes you."

    stop music fadeout 1.0

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show tsunday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    #___monday3
label monty_hall:

    scene bg codadorm with fade

    play music "audio/ambient/morning birds.ogg" fadein 1.5

    show box with Dissolve(.2):
        ypos 0

    n "Those pills must be working since you don't feel like death when you wake up."
    n "It might just be placebo but damn if it's not effective."
    n "Regardless, you decide to take another one just in case and hope you don't pass out in history class."

    stop music fadeout 1.5
    
    scene bg classroom with fade
    
    play music "audio/music/mere - schooldaze.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0
    
    n "You drifted off into a daydream during class that was dispelled when you heard your name called."
    
    show rothbauer at center with dissolve:
        xpos 0

    rothbauer @ say "[name], could you tell me why there's no class this Friday?"

    player "Huh? There's no class on Friday?"

    n "Mr. Rothbauer sighs. You get the feeling that was supposed to be an easy question."

    rothbauer @ say "Must have been a long night studying, eh?"
    rothbauer @ say "Friday is Anthromorphs's Liberation Day! The day when us anthromorphs were granted equal rights to our human counterparts who had ruled society for so long."
    rothbauer @ say "It took several rebellions, riots, and even wars to reach this point."
    rothbauer @ say "Prior to this historic day, we had no right to vote, own land, hold position in government, and were generally treated as second class citizens."
    rothbauer @ say "Though many were opposed to this notion, it would hardly matter in the end, as the human population had been on the decline..."
    rothbauer @ say "...and would soon be outnumbered by the anthromorphs who could set aside their own differences to become allied in this cause."
    rothbauer @ say "Anyway, that's all I have for you today."
    rothbauer @ say "Oh wait, there's still one more thing!"
    rothbauer @ say "There will be a parade in town to celebrate the holiday. I'll add 2 percent to your final grade if you show up and prove you were there by taking a selfie haha!"
    rothbauer @ say "You kids all love taking those funny little self portraits, don't you? Well this will be a good opportunity for you take another one while going out gaining an appreciation for historical events!"
    rothbauer @ say "Why, back in my day when I was the director of Harmonia's Anthromorphs Liberation Day committee I..."

    n "As he goes on with his rant, students start leaving. It's 5 minutes past the end of class after all. You decide to join them."
    
    stop music fadeout 1.0

    scene bg lecturehall with fade
    
    play music "audio/music/mere - schooldaze faster.ogg" fadein 1.5
    
    show box with Dissolve(.2):
        ypos 0
    
    show herschel at center with dissolve:
        xpos 0
        
    herschel @ say "...alright, I think that's enough for today's lesson but we still have a bit of time leftover!"
    
    show gunner neutral at center with dissolve:
        xpos -550
        xzoom -1
    
    gunner @ say "Does that mean we can go home early?"
    
    herschel @ say "Of course not! Instead what I have in mind is an extra credit opportunity, something you of all students should be particularly interested in."
    
    n "Gunner mutters something under his breath."
    
    gunner @ say "Fucking bitch..."
    
    hide gunner with dissolve
    
    n "Thankfully Mrs. Herschel doesn't seem to have heard it."
    
    herschel @ say "I have something of a math riddle for you to solve!"
    herschel @ say "Say you have three doors to choose from and behind one of them lies a prize."
    herschel @ say "After making your selection, someone comes along and opens one of the doors you did not choose and contains no prize."
    herschel @ say "You're given a choice to change your selection to the remaining door. Should you do it?"
    
    n "As usual the class is dead silent and Mrs. Herschel has infinite patience for someone to speak up."
    n "Gunner is engrossed in his notebook, drawing diagrams and writing out formulas in an attempt to find the solution."
    n "He's clearly failing to find one, meaning you're gonna have to take one for the team and come up with an answer."
    
    menu:
        n "{cps=0}He's clearly failing to find one, meaning you're gonna have to take one for the team and come up with an answer.{/cps=0}"
        "Keep your initial choice":
            n "You raise your hand and the pine marten calls on you."
            
            player "Um, I guess I'd keep my initial choice. At this point it's a 50/50 chance so either door is equally likely to be a winner, right?"
            
            herschel @ say "A 50/50 shot you say? Ah, that's where you're wrong."
            herschel @ say "Are the chances really as equal as they seem?"
            
            n "Gunner circles something and puts down his pencil."
            
            show gunner neutral at center with dissolve:
                xpos -550
                xzoom -1
            
            gunner @ say "Would you be twice as likely to win if you choose the other door?"
            
            herschel @ say "Precisely! Very good Gunner! Tell us how you came to that conclusion, won't you?"
            
            gunner @ say "Well uh, I'm not really sure to be honest. But like in the beginning you have a 1 in 3 chance right?"
            gunner @ say "Then you get rid of one door but that can't possibly affect the chances of your decision in the past can it?"
            gunner @ say "So all that chance of winning from the two doors you didn't choose is set in stone. All the other guy did was get rid of a losing option."
            
            herschel @ say "Correct! Your initial choice has a 1/3 chance, so recall that what you don't choose is 1 minus your chance."
            herschel @ say "You wind up with the other two doors combined having a 2/3 chance of having a prize behind one of them."
            herschel @ say "It may help to think in terms of quantities rather than chance. Imagine you know your door has 1/3 of the prize, so then the doors you didn't choose have a combined 2/3 of the prize."
            herschel @ say "Then someone opens of of them and reveals nothing behind it, so they remaining door you didn't choose must contain the larger prize!"
            herschel @ say "Very good Gunner, I'll add a point to your final grade."
            
        "Change your selection":
            $ goodEnd = goodEnd + 1
            
            n "Before you can say anything, Gunner pipes up."
            
            show gunner neutral at center with dissolve:
                xpos -550
                xzoom -1
            
            gunner @ say "What difference does it make? It's a 50/50 chance at that point... isn't it?"
            
            herschel @ say "Is that your final choice? Perhaps someone else would choose otherwise..?"
            
            n "She's making it sound like Gunner is wrong. You should go for the opposite answer."
            
            player "I'd change my decision."
            
            herschel @ say "And you'd be right to! You'd enjoy a 2/3 chance of success if you switch to the other door."
            
            gunner @ say "How the hell...? That can't be right, how does a door suddenly gain a higher chance without doing anything?"
            
            herschel @ say "I told you it was a riddle, so the answer could never be obvious!"
            herschel @ say "The trick lies in eliminating a losing option after making your choice."
            herschel @ say "Your door has a 1/3 chance of winning, right? So that means the other two doors have a combined 2/3 chance of winning, at least in the beginning."
            herschel @ say "When you remove one of those doors, where does that extra chance go? Nowhere! It stays right where it was!"
            herschel @ say "It's just that where it was is where you're not. Which is why you should change your choice."
            
            n "Gunner mutters something again."
            
            gunner @ say "What the fuck kind of reasoning is that..?"
            
            herschel @ say "Very good [name], I'll add one point to your final grade."
            
    stop music fadeout 1.0
            
    scene bg black with fade
    
    show bg calendar
    show tmonday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    #___tuesday3

    scene bg cafe with fade

    play music "audio/music/mere - coffeeLoveLoopInstrumental.exe.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0

    n "You decide to make a stop at the cafe on your way to class. They must have updated their menu because you can smell cinnamon and pumpkin spice in the air."

    show mishka neutral at center with dissolve:
        xzoom -1
        #xpos -440
        xpos 0

    mishka @ say "Hello [name]! Would you like to try the spice of pumpkin latte? It's part of our fall menu thing."

    player "Actually I was eyeing that cinnamon roll."

    mishka @ say "Oh lucky you, it's our last one! They sell out very quickly!"

    player "They must be good then."
    
    show mishka overjoyed

    mishka @ say "Yes, fully of sugar and sweetness! When I first came to America I had no concept of a 'cinnamon roll' but it soon became a favorite of mine hehe!"
    
    show mishka neutral

    player "I'll take it to go please. I have to be in class in a few minutes."

    mishka @ say "Gotchya!"

    n "Mishka places the pastry in a bag and slides it over to you as you swipe your card through the machine."
    
    show mishka winki

    mishka @ say "Spasibah! Have great day!"
    
    show mishka neutral
    
    show margaret neutral at offscreenright:
        yalign 0
    
    #hide mishka with dissolve

    #add sound effect of bell as anyone enters the cafe
    
    pause .2

    show margaret neutral:
        xpos 350
    show mishka:
        xpos -440
    with move

    ellen @ say "Oh hello there, [name]. I didn't expect to see one of my students here just before class. Are you feeling any better?"

    player "Yes ma'am. I ended up going to the hospital and they gave me some pills so I won't pass out in your class anymore."
    
    show margaret happy

    ellen @ say "That's good to hear! I'd certainly hope you're feeling well today since we're having a quiz!"

    player "Err, quiz?"

    show margaret sad

    ellen @ say "Oh didn't anybody let you know?"
    
    show margaret neutral
    
    ellen @ say "You should be fine though, as long as you've been keeping up with your reading."
    
    show margaret happy
    
    ellen @ say "Now if you'll excuse me, I'm going to get one of those delicious cinnamon buns. What better way to start autumn, right?"
    #ellen @ say "Why, I'd kill for them! Figuratively, of course!"
    
    show mishka sad

    mishka @ say "Sorry ma'am, I just sold the last one to [name] here..."

    show ellen sad

    ellen @ say "Seriously?"
    ellen @ say "Damn, I was really counting on that cinnamon bun to get me through today..."

    menu:
        ellen "{cps=0}Damn, I was really counting on that cinnamon bun to get me through today...{/cps=0}"
        "Offer Miss Ellen your cinnamon roll":
            #finished
            $ ellenPoints = ellenPoints + 1
            $ gaveCinRoll = True
            $ badEnd = badEnd + 1
            player "Well... I could give you mine. I don't really mind."
            
            show mishka happy

            show margaret neutral
            
            mishka @ say "Aww how sweet of you!"

            ellen @ say "Oh my goodness, I'm flattered but a teacher could never accept such a gift from a student!"
            
            show mishka neutral

            player "No really, I just remembered I'm not supposed to eat sugary things when I'm on these pills so..."

            show margaret intrigued 
            
            ellen @ say "Hmm..."

            n "Miss Ellen looks around."
            
            show margaret melancholy

            ellen @ say "Well, I suppose I could, just this once..."

            player "Don't worry, I'm not gonna tell on you or anything."
            player "Here you go."

            n "You hand over the bag."
            
            show margaret neutral

            ellen @ say "Aww, thanks [name]!"

            n "Miss Ellen gives you a warm smile and leans in close enough to whisper into your ear."

            ellen @ say "Don't worry about the quiz today~"

            n "Miss Ellen waves to you as she takes a bite of the cinnamon roll."

            ellen @ say "See you in class!"

            hide ellen with dissolve

            player "Yeah, I guess I should get going too. Later, Mishka!"

            mishka @ say "Dah skorovuh!"

            stop music fadeout 1.3

            scene bg lecturehall with fade

            #play music "audio/ai21.ogg" fadein .5
            play music "audio/music/mere - retrograde.ogg" fadein .5

            show box with Dissolve(.2):
                ypos 0

            show margaret neutral at center with dissolve

            ellen @ say "Good morning class! I hope you studied well for today's quiz!"

            n "Ellen hands out papers to everyone, giving you a warm smile as she hands you yours."

            if studied == "lit":
                #finished
                n "You probably could have aced this quiz anyway. You had plenty of time to read over it during your stay at the hospital after all."
                n "But the extra assurance certainly doesn't hurt."
                n "You work through the quiz normally in case she decides to go back on her word."
                n "When you're finished you walk up and turn it in."
            else:
                #finished
                n "It's a good thing you bribed her with that cinnamon roll, otherwise you'd fail this quiz for sure."
                n "Feels a bit dishonest though..."
                n "Looking over the questions, you have no idea how to answer most of them."
                n "You just write something that kinda makes sense and turn it in when you're done."


        "Don't offer Miss Ellen your cinnamon roll":
            #untested
            show mishka neutral
            
            player "Better luck next time."

            n "You take a bite out of your cinnamon roll while Miss Ellen glares at you."

            ellen @ say "Yes well... I'll see you in class, [name]."

            hide ellen with dissolve

            n "She storms out of the cafe."
            
            #show mishka hopeful
            
            n "You glance at Mishka who just shrugs."

            player "Guess I better go too. Later, Mishka!"
            
            show mishka happy

            mishka @ say "Dah skorovuh!"
            
            stop music fadeout 1.0

            scene bg lecturehall with fade
            
            play music "audio/music/mere - retrograde.ogg" fadein .5

            show margaret neutral at center with dissolve

            show box with Dissolve(.2):
                ypos 0

            ellen @ say "Good morning class! I hope you studied well for today's quiz!"

            n "Ellen hands out papers to everyone, glaring at you as she hands you yours."
            n "She isn't still mad about the cinnamon roll thing, is she?"
            n "Hopefully she doesn't take it out on your grades."

            if studied == "lit":
                n "The answers come to you fairly quickly as you go through the quiz, thanks to the time you spent studying while bedridden."
                n "You feel confident as you walk up and hand in your quiz."
            else:
                n "After looking over the quiz and realizing you're not prepared to answer any of these questions, you begin to regret not giving up your cinnamon roll this morning."
                n "You do the best you can and sheepishly turn it in."
            

    ellen @ say "...Is that everyone's?"
    
    show margaret melancholy
    
    ellen @ say "Very good, what do you say we call it a day?"
    
    show margaret neutral
    
    ellen @ say "I don't want to overload your brains with too much stress. If you felt like this quiz was difficult, take this opportunity to reassess how you study."
    ellen @ say "And be sure to read every page assigned to you! There are no shortcuts when it comes to literature!"
    ellen @ say "That's all I have for you. Class dismissed!"

    scene bg classroom with fade
    
    player "At least it's a short week this week."
    
    claire @ say "Oh yeah!"
    
    show claire sweater giggle
    
    claire @ say "What are y'all's plans for the three way- I mean three day weekend?"
    #claire @ say "Y'all excited for the three way- I mean three day weekend?"
    
    #player "You guys are alright, dont come to school on friday"
    
#later ava complains her philosophy prof told her to stop skipping
    ava @ say "I was thinking of filming at this old abandoned hospital nearby. I could use a partner to make sure I don't get shanked by a crazed hobo if you wanna come, [name]."

    $ avahangout1 = False

    menu:
        ava "{cps=0}I was thinking of filming at this old abandoned hospital nearby. I could use a partner to make sure I don't get shanked by a crazed hobo if you wanna come, [name].{/cps}"
        "That sounds fun!":
            #finished
            $ avaPoints += 1
            $ avahangout1 = True
            
            show claire sweater neutral
            
            player "That sounds fun! I'd love to go with you!"
            
            show ava casual overjoyed

            ava @ say "Sweet! You don't mind if it's haunted, do you? Cause it's probably haunted."

            player "No, haunted is fine."

            claire @ say "Ksksksks you two are so cute!"

            show ava casual angry

            ava @ say "We are not!"
            
            show claire sweater derp
            
            claire @ say "Ksksksks chill! I'm just joking!"
            
            player "What about you Claire? Got any epic plans?"
            
            show ava casual happy
            show claire neutral

            claire @ say "Nothing too exciting, just going back home to visit family and stuff."

            player "Couldn't wait until Thanksgiving or Christmas to go back?"

            claire @ say "I only live a couple hours away and my siblings are actors in the play they have going on at my old middle school."
            
            show claire overjoyed
            
            claire @ say "It's actually the same play I performed in when I was their age so I'll be glad to cheer them on!"
            
            show ava casual smile

            ava @ say "Aww, now you're the one being cute!"
            
            show claire sweater giggle

            claire @ say "Ksksks I guess we're all just a bunch of cuties on duty~"

            n "Your swear you can feel your brain physically cringe."
            #n "Deer god you really can't stand being near women sometimes."
            n "Out of the corner of your eye you see Gunner approaching."

            show claire sweater neutral:
                xpos -600
            show ava casual happy:
                xpos 600
            with move

            show gunner neutral at center with dissolve:
                xzoom -1
                
            show gunner:
                xpos 0
                ypos 15
                xzoom 1
                linear .15 yalign 0
            
            pause .6
            
            show gunner at fliphop2:
                xpos 0
                ypos 15
                xzoom -1
                linear .15 yalign 0
            

            gunner @ say "Sup guys! What's a bunch of cuties like you doing out here in the open?"

            ava @ say "Hiii~"
            
            claire @ say "Heyo!"

            player "We're just discussing our plans for Friday."

            gunner @ say "Nice, I'm going on this fishing trip thing with Rori and the other Alphas!"
            ###option to go fishing with rori if you decline ava's invitation. end up with rose if you decline both

            player "Whoa, Rori's an official Alpha male now?"

            gunner @ say "Yup!"

            player "Based. Good for him!"
            
            claire @ say "Who's Rori? He sounds hot."
            
            player "He's the goat."

            gunner @ say "Anyway what are your plans?"

            player "Me and Ava are going to an abandoned hospital to take photos and stuff."

            gunner @ say "Oh... That sounds fun."

            ava @ say "I shoot pretty much every day. Maybe you can come next time!"

            gunner @ say "Yeah... next time..."

            n "He looks so sad that you stole his chance to hang out with Ava."
            n "Sorry Gunner."

            gunner @ say "Well, I have a lot of homework to get started on so I'll see you all later!"

            ava @ say "See ya! Good luck!"

            player "Laters."

            claire @ say "Byeeeee!"

            hide gunner with dissolve

            n "Gunner walks off with an obviously fake smile. Damn, you're starting to feel bad about cucking him out of some alone time with Ava."
            n "You spend a little more time chatting with the girls before heading home yourself."
        "I'll pass.":
            #untested
            $ rosePoints += 1
            show claire sweater neutral
            
            player "Sounds cool but I'll pass. I'm supposed to go to the parade in town to get extra credit in history."
            
            show ava casual unimpressed

            ava @ say "Aww..."

            player "Can't Claire go with you?"
            
            show ava casual happy

            claire @ say "I would but I'm going back home for the weekend."
            claire @ say "My siblings are actors in the play they have going on at my old middle school. It's only a few hours away so I figured I'd go cheer them on!"

            ava @ say "Dang, guess I'll just have to go on my own."

            n "As if on cue, Gunner approaches."

            show claire sweater neutral:
                xpos -600
            show ava casual happy:
                xpos 600
            with move

            show gunner neutral at center with dissolve:
                xzoom -1
                
            show gunner:
                xpos 0
                ypos 15
                xzoom 1
                linear .15 yalign 0
            
            pause .6
            
            show gunner at fliphop2:
                xpos 0
                ypos 15
                xzoom -1
                linear .15 yalign 0

            gunner @ say "Sup guys! What's a bunch of cuties like you doing out here in the open?"            

            ava @ say "Gunner! Would you happen to be busy this Friday?"

            gunner @ say "Nope! Why?"

            ava @ say "So you wouldn't mind coming along with me to an abandoned and possibly haunted hospital for a photo project, would you?"

            gunner @ say "Not at all! That sounds pretty awesome actually!"
            
            show ava casual overjoyed

            ava @ say "DidImentionI'mgonnabealoneinmydormallweekend?"

            gunner @ say "What was that?"
            
            show ava casual flattered

            ava @ say "Nothing! Nevermind!"
            
            show claire derp

            claire @ say "Ksksksksks~"
            claire @ say "Sounds like you two will have a fun little date together~"
            
            show claire neutral

            gunner @ say "Wait, this is a date?"
            
            show ava casual concerned

            ava @ say "No! I mean-"
            ava @ say "It's a uh..."

            gunner @ say "No yeah, it's cool haha. What's a date, am I right?"
            
            show ava casual daydream

            ava @ say "Haha exactly!"
            ava @ say "I mean, an abandoned hospital full of rusty nails is far from the most romantic place I could take someone out to!"
            
            show ava casual happy

            n "There's a sudden awkward silence."
            n "Okay you can't take it anymore, you need to execute your exit strategy now."

            player "Well I have a lot of homework to get started on so I'll see you all later! Have fun on your date!"
            
            show ava annoyed

            ava @ say "It's not a date!!!"

            gunner @ say "Later, [name]!"

            claire @ say "Byeeeee!"

    hide ava
    hide claire
    hide gunner
    with dissolve

    hide box

    scene bg black with fade

    #show bg static3
    #pause .02
    #show bg static2
    #pause .02
    #show bg static3
    #pause .02
    #show bg black
    #pause .04
    #show bg static1
    #pause .02
    #hide ava
    #hide claire
    #show bg static2
    #pause .02
    #show bg black
    #pause .08
    #show bg static3
    #pause .02
    #show bg static1
    #pause .03
    #show bg black

    stop music fadeout 1.3

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show ttuesday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    #___wednesday3
label history_quiz:

    scene bg codadorm with fade

    pause .6

    show bg classroom

    #play music "audio/ai1.ogg" fadein 1.0
    play music "audio/music/mere - schooldaze.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0

    n "Once again, you can't for the life of you remember the hours leading up to how you got to class."
    n "It's like your brain has just stopped recording everything."
    n "At least you hope you haven't been forgetting anything super important."

    

    stop music fadeout 1.3

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    n "What an exhausting day."
    n "You can't even remember what happened in stats class. Your brain is fried but you still need to read for tomorrow."
    #n "You got your quiz back in stats and you didn't do nearly as well as you thought you did. These professors really need to chill."
    n "You sit at your desk and open your copy of 'Bartleby, the Scrivener,' a short story Mrs. Ellen assigned for the class."
    n "You end up relating a lot to this Bartleby guy. The dude just wants to get paid for sitting around doing nothing all day."
    n "\"I would prefer not to\" is gonna be your new motto."
    #bartleby the scrivener (42 pages, a 2 day affair), about preferring not to change, not accepting change, wasting your life and becoming a burden on others

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show twednesday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    #___thursday3
label liberation_eve:

    scene bg lecturehall with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    show margaret neutral at center with dissolve

    ellen @ say "Good morning class!"
    
    show margaret happy
    
    ellen @ say "I'm sure you're all as excited about the long weekend as I am so how does a short day sound?"
    
    show margaret melancholy

    n "The class erupts into a half-hearted cheer followed by a dull murmur that takes a while for Ms. Ellen to calm down."

    ellen @ say "Alright alright, the sooner you all shut up the sooner you can go home."

    n "She rubs her temples like she has a migraine until the class quiets down."

    show margaret sad

    ellen @ say "Ugh..."
    ellen @ say "Let's get this over with..."

    n "Ms. Ellen sluggishly gives her lesson but cuts it off after 15 minutes."
    
    show margaret neutral

    ellen @ say "You know what? I think that's enough for today. Enjoy your weekend, everybody!"

    hide ellen with dissolve

    n "Usually she waits until everyone has left, but today she hastily grabs her purse and rushes out the door before anyone else."
    n "Strange, but you can't complain about having an early start to your weekend."
    n "Well, almost an early start. You still have to get through French first."

    scene bg classroom with fade

    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    show celestine neutral at center with dissolve

    celestine @ say "Hello class! Happy Anthromorphs's Liberation Day Eve!!"
    celestine @ say "Obviously this is an American holiday but I wanted to go over related holidays other countries celebrate!"
    celestine @ say "France is actually credited with kickstarting the push for us animal folk to have equal rights in this era!"
    celestine @ say "It sure sends a message when the human elites get brutally murdered and eaten by commoners, huh?"
    celestine @ say "Sometimes that's what it takes to change the world!"
    celestine @ say "I highly recommend visiting France during the week long celebration they have! It's like Mardis Gras on crack! Heehee~"
    celestine @ say "Though France didn't see a long-standing animal leader for a while, Britain had one the next decade! To this day, Queen Mary is celebrated by having her portrait on their currency!"

    n "Mrs. Celestine rambles on and on about other countries and their various transitions from human dominated society to the gradual rise of animal people."
    n "Maybe one day you'll get your face on the dollar bill as a memory of the last human."
    n "Either that or they'll talk shit about you in textbooks for being an evil human who oppressed every other species for millenia."
    n "So much for an extra long weekend. If someone hadn't interrupted her, she probably would have ranted well into the evening."

    celestine @ say "Oop! Seems I got a bit too excited! Class is dismissed! Enjoy your weekend!"

    hide celestine with dissolve

    n "You grab your bag and prepare to head out, do your usual chat with Ava and Claire and then go home."
    
    stop music fadeout 1.0

    show bg calendar
    show tthursday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    #___friday3
label liberation_day:
    
    scene bg codadorm with fade

    show box:
        ypos 0
    
    play music "audio/ambient/morning birds.ogg" fadein 0.1

    n "Today is Anthromorphs' Liberation Day."
    n "You've always felt awkward about this holiday."
    n "Like it's not for you or something."
    n "Maybe a hundred years ago it was about the alliance between humans and anthromorphs."
    n "But nowadays it's been recontextualized as the rise of animal people after your kind died off."
    n "It's a really strange feeling. The world you inhabit was shaped by humans who are just gone now, aside from you."
    n "Your great grandpa would have been horrified to see you hanging out with your current friends."
    n "He claimed he was allergic to any kind of fur but he always looked so smug when detailing the battles he had fought in where he killed anthromorphs."
    n "And now he's dead and your only friends are animal people."
    n "The age of humans is over and a new generation has inherited the world."

    if avahangout1 == True:
        n "*sigh*"
        n "At least you get to hang out with a cute bird (who might be into you??) today."

        hide box

        call phone_start from _call_phone_start_29

        call message_start("me", "Hey", "testimage.png") from _call_message_start_63

        call message("Ava", "Hi!!!", "avaavi.png") from _call_message_352

        call reply_message("So we're going to this old hospital today?") from _call_reply_message_256

        call message("Ava", "Yup! I'm ready whenever you are ^v^", "avaavi.png") from _call_message_353

        call reply_message("Where exactly is it?") from _call_reply_message_257

        call message("Ava", "Hang on lemme get the coordinates", "avaavi.png") from _call_message_354

        call phone_end from _call_phone_end_55

        show box:
            ypos 0

        n "She sends you the coordinates which open in your map app when you tap on them."
        n "You can barely tell there's a building there from the satellite images since it's so overgrown with trees and bushes."
        n "Ava sends you a text telling you to meet her there in half an hour."
        n "You prepare your backpack, stuffing it with a couple water bottles and snacks, then proceed to head out."

        scene bg oldhospital foyer with fade
        
        show box:
            ypos 0

        #play music "audio/ambient/spooky.ogg" fadein 1.0
        #play music "audio/music/vylet - Cavern Lurker.ogg" fadein 1.0

        show box with Dissolve(.2):
            ypos 0

        n "Ava wasn't kidding when she said this place was abandoned."
        n "Graffiti lines the walls and weeds grow out of cracks in the concrete. You'd be afraid to enter a place like this alone, but luckily you have a dainty liberal arts student to protect you."

        show ava typical neutral at center with dissolve

        #ava @ say "Hey [name]! Glad you could make it!"

        #player "It took a while to find it! There's no trail or signs or anything."

        #ava @ say "I know, right? It's so exciting! It's probably been years since anyone has last stepped foot here."
        ava @ say "It's probably been years since anyone has last stepped foot here."
        
        player "Any functioning member of society at least."
        
        show ava excited
        
        ava @ say "Come on, let's get exploring!"
        
        scene bg oldhospital hall1 with dissolve
        
        show box:
            ypos 0

        n "Ava leads the way as you go deeper inside, pulling away some boarding planks and debris along the way."
        n "She looks around before deciding on a place to compose a shot and snapping a picture."

        player "That's not your usual camera, is it?"
        
        show ava typical neutral at center with dissolve:
            xzoom -1

        ava @ say "Hm? Oh this?"
        ava @ say "I brought one of my old film cameras along. Thought some vintage black and white film would fit the mood of the place, y'know?"
        
        player "It's not because ghosts can only be recorded on analogue, is it?"
        
        show ava pose smile
        
        ava @ say "Well, that too."

        n "She pulls a lever on the camera, loading the next frame."
        
        show ava typical neutral

        #ava @ say "But I also wanted to capture the feeling of those old historical photos with the inky blacks and softness to the frame."
        
        #player "Black and white means it's art, right?"

        #ava @ say "Hey, I like black and white for portraits!"
        ava @ say "And it just wouldn't feel right shooting this place in color."
        ava @ say "I don't even think color film was invented yet when they built this place."

        player "What about lead paint and asbestos?"
        
        show ava at flipleft
        
        pause .8
        
        show ava at flipright
        
        pause .4

        ava @ say "Hehe, I dunno! Try not to lick the walls just in case."

        n "You make your way through the building slowly, being careful not to step on any rusty nails or fall through any floorboards."
        n "Dust kicks up as you explore, mixing with the smell of mildew in the humid air. Every now and then you hear creaks and pops from other rooms echoing throughout the building."
        n "Water drips down from the ceiling into little puddles full of moss and weird sludge you don't dare touch."
        n "Luckily the holes in the walls provide enough light for you to navigate."
        
        show ava waitwhat
        
        ava @ say "Whoa, check this out!"
        
        scene bg oldhospital room with dissolve
        
        show box:
            ypos 0

        n "Ava motions for you to look through a crack in the wall. When you bend over to peer inside all you see is a seemingly ordinary waiting room."

        player "I don't get it, what's so special about this?"
        
        show ava unsure at center with dissolve

        ava @ say "Oh right, I guess you wouldn't be able to see it with your weak human eyes."
        
        player "Hey! My eyes are optimized for tracking movement and identifying photoshopped pixels!"
        
        show ava seriously
        
        ava @ say "Hmm okay how do I describe this..."
        ava @ say "You know how in those crime shows they shine a blacklight and they can see bloodstains and stuff? It's like that."
        
        player "Whoa really? So this room was covered in blood at some point?"

        ava @ say "Err... actually blood doesn't glow like in the movies and stuff."
        ava @ say "Other bodily fluids will though."

        player "Gross!"
        
        show ava pose overjoyed

        ava @ say "That doesn't mean this building didn't see its fair share of blood though!"
        
        show ava ohyou
        
        ava @ say "The doctors at this hospital was known for their eagerness to amputate limbs."
        ava @ say "Like, if you came in with a cold they'd amputate your leg."

        player "Wow, that's uh..."
        
        show ava pose smile

        ava @ say "There's even a \'cemetary\' for all the disembodied limbs out back!"

        player "How do you know all this?"
        
        show ava pose happy

        ava @ say "I saw a video on it."
        ava @ say "Whenever I can't sleep I put on morbid videos."

        player "Doesn't that give you nightmares?"

        ava @ say "Not really? I don't dream much."
        ava @ say "Do you?"

        player "Sometimes."

        ava @ say "About what?"

        player "Usually something completely random and unnoteworthy."
        player "But sometimes they feel real and can make me anxious."

        n "Ava pokes her camera through the crack and adjusts the dials and rings on the camera."

        ava @ say "Sometimes I daydream. Whatever I'm doing, my brain just goes on autopilot while I think about things I wanna shoot."

        player "Shoot as in with your camera, right?"
        
        ava @ say "Hm? Yeah."
        
        player "Like spooky hospitals?"

        ava @ say "Actually yeah, this is the sort of things I imagine, but more abstract."
        
        hide ava with dissolve

        n "Ava clicks the shutter button and takes a photo."

        #player "What are you doing?"

        #ava @ say "Rewinding the film."

        #player "Oh."
        #player "...Why?"

        #ava @ say "Oh sorry, I should have explained."
        #ava @ say "I wanted to try taking some double exposures, y'know, where you take a shot on top of an already exposed piece of film."
        #ava @ say "It's a technique that I've thought about using more but the results can look kinda random so it's hard to imagine how it'll turn out."
        
        n "You and Ava make your way to the end of the hall where a staircase lies, the steps covered in rubble from the crumbling walls and steps above."
        n "Ava crouches down and turns her camera 90 degrees to take a shot of it."
        n "Her feathers stick up and you jump a little when a loud noise comes from behind, echoing throughout the hall."
        
        show ava pose concerned at center with dissolve
        
        n "You speak in a hushed tone."

        player "...Did you hear that?"

        ava @ say "Yeah... is someone here?"
        
        n "As if to answer her question, the sound of stone clattering onto the floorboards reaches you."
        
        player "M-must have been the wind?"
        
        ava @ say "I don't think we're alone. Come on, let's go up the stairs, quick!"
        
        n "Ava goes first, lightly stepping between the larger piles of debris while you struggle with these non-OSHA compliant stair sizes."
        n "She flutters over a precarious gap in the steps that you unfortunately end up getting your foot stuck in."
        
        player "Agh! My foot!"
        
        show ava unsure
        
        ava @ say "[name]!"
        
        n "Ava doubles back and helps pull you out, oblivious to the pain shooting through your ankle. You try to hold your tongue to not reveal your position to the other intrudor."
        n "You hobble up the remaining stairs and into a room, closing the door behind you, bracing it with your body in case they try breaking in."
        
        scene bg oldhospital darkroom with fade
        
        show box:
            ypos 0
        
        n "For a few moments it's just you and Ava in a dark room trying not to breath heavily after the scare and rapid ascent so you can listen."
        n "With your back against the door, you hold onto Ava. She's got both her wings wrapped around you."
        n "Her camera is jabbing into your side uncomfortably but you can feel her heartbeat against your chest, which is oddly calming."
        n "You guess if you're gonna get stabbed by a hobo, this would be a nice final memory. Cute bird in your arms. Maybe someone will find the film and develop it."
        n "Maybe someone will make a documentary about you."
        n "'Two dumbasses go venturing in dangerous hobotopia, shockingly get murdered in most gruesome way possible.'"
        #player "I wonder who they'd get to reenact me in the documentary? Maybe they'd shave a chimpanzee for it?"
        n "After a few minutes, Ava speaks up, still in a hushed tone."
        
        show ava typical neutral at center with dissolve
        
        ava @ say "I think whoever that was is gone. Or at least they didn't follow us."
        
        player "Yeah. We probably scared them off with the noise we made climbing up the stairs."
        player "Hopefully it was just a wild animal and not like a psycho stalker serial killer."
        
        ava @ say "Ugh you just reminded me of something."
        
        player "What?"
        
        ava @ say "Promise you won't cringe."
        
        player "Oh please, whatever it is, I guarantee I've done worse."
        
        ava @ say "I had blocked this memory out for so long but... in freshman year of high school I would actually send letters to serial killers who were in jail that I thought were cool."
        
        show ava angry
        
        ava @ say "I was confused at the time okay???"
        
        menu:
            ava "{cps=0}I was confused at the time okay???{/cps}"
            "What was the appeal?":
                player "That's uh... quite unexpected. What's the appeal?"
                
                show ava typical neutral
                
                ava @ say "I dunno, I guess the forbidden nature of it combined with the gruesomeness?"
                ava @ say "A murderer is just an interesting type of person!"
                ava @ say "You just wanna know \'What made you do it?\'"
                ava @ say "Cause you have to wonder if you could become a murderer too if you grew up just a little differently."
                ava @ say "You'd know you're not just with any regular shmuck if he had the guts to kill somebody!"        
            "Nah, I get it.":
                player "I completely understand."
                
                show ava typical neutral
                
                player "There's something sexy about someone who can straight up murder in cold blood."
                player "That sort of evil is mesmerizing, isn't it?"
                
                ava @ say "I know right??"
                ava @ say "Maybe it's like a primal instinct thing. Like wanting a brutish man who can protect you."
                ava @ say "By violently murdering your enemies."
                ava @ say "I mean, uh, that's probably what I was thinking back then."
                ava @ say "You don't have to murder anyone for me to like you."
                
                player "Noted."
        
        player "Did any of them ever write you back?"
        
        ava @ say "I dunno. My parents probably would have shredded the letters if we got any before I'd ever gotten a chance to see them."

        n "You feel Ava pull away from you."
        
        show ava with move:
            xpos -300
        
        player "Careful, it's dark and I don't know if this is the rusty nail room."
        
        n "*Crck*"
        n "A dim purplish glow gradually fills the room."
        
        show ava glowy unimpressed with dissolve
        
        ava @ say "I brought some glowsticks. Good to have in case your batteries run out. Or for creating ambiance."
        ava @ say "And they're my favorite color."
        
        player "Whoa! Ava, your feathers..!"
        
        show ava at flipright
        
        ava @ say "Hm? What about them?"
        
        player "They're all pretty and stuff!"
        
        ava @ say "Oh my gosh thanks? I didn't really do anything special with them today though."
        
        player "But you have patterns on them now!"
        
        ava @ say "I always have patterns on them. That's just how they are."
        ava @ say "Wait, you mean the spirals?"
        
        player "Yeah those."
        
        ava @ say "You're just now noticing them? Those have always been there."
        ava @ say "Hmm, okay I think I know what's going on."
        
        n "She waves a glowstick over her wing feathers and the patterns become more visible the closer they are to the light."
        
        ava @ say "Just like what I was saying before. The glowstick must be acting like a blacklight."
        ava @ say "With these you can see what I see all the time."
        
        player "Wow. Do all birds have patterns on their feathers?"
        
        #show ava portrait neutral
        
        ava @ say "Just the pretty ones~"
        
        #show ava typical neutral
        
        #player "You'd be fun at one of those glowstick raves"
        
        #player "It certainly makes the thought of getting stabbed by a crackhead here more palatable."
        
        #ava @ say "Haha I was thinking the same thing!"
        
        n "Ava breaks another glowstick and wanders further into the room."
        
        #ava @ say "If I was a serial killer on the run from the police, this is the type of place I'd hang around in."
        
        show ava:
            ypos 15
            xzoom -1
            linear .15 ypos 0
            
        #show ava pose concerned
            
        ava @ say "You comin- oh god [name]! What's with your foot?"
        
        player "Huh?"
        
        n "You look down to see your foot bent at an unnatural angle."
        
        player "Oh. FUck."
        
        ava @ say "Holy Hoole that looks bad... Stay right there, I'll- I dunno, I'll figure something out."
        
        n "Ava looks around and finds an old wooden cane for you to lean on."
        
        ava @ say "Lucky we're in a hospital right? Haha..."
        
        n "Her attempt at making light of the situation is appreciated but now that the adrenaline is wearing off, you're starting to feel excruciating pain."
        
        player "Where's a kitsuragi when you need one?"
        
        ava @ say "Can you walk? We should get you to a real hospital asap."
        
        n "Ava lets you lean on her as the two of you exit the room and head back down the stairway."
        n "It takes a long time but you eventually make it back to the ground floor."
        
        scene bg oldhospital hall2 with fade
        
        show box:
            ypos 0
        
        show box with Dissolve(.2):
            ypos 0
        
        n "As you're trying to figure out which direction you came from, you notice Ava seems preoccupied with a corridor you hadn't explored."
        
        show ava concerned at center with dissolve:
            xpos 0
        
        ava @ say "..."
        
        player "Go ahead, I can tell you've got a photo in mind."
        
        show ava excited
        
        ava @ say "Whew thanks! I'll be just a second, alright?"
        
        hide ava with dissolve
        
        n "You lean on your cane while she flutters up to a high perch and lines up a shot."
        n "Suddenly a loud crashing noise startles both of you and Ava comes crashing down."
        
        
        show ava reaching concerned:
            ypos -3000
            
        show ava with move:
            ypos 1080
            
        pause .2
            
        show ava with move:
                ypos 0
                
        show ava at shudder
        
        show ava unsure
        
        
        
        
        #show ava unsure at center:
        #    ypos -3080
            
        #pause .1
        
        #show ava:
        #    ypos 1080
        #with move
        
        #pause .2
        
        #show ava:
        #    ypos 0
        #with move
        
        
        player "Ava!"
        
        ava @ say "I'm okay!"
        
        player "What the fuck was that?"
        
        ava @ say "I dunno but we better get out of here now before we get murdered."
        
        player "Don't you wanna meet your serial killer husbando?"
        
        show ava angry
        
        ava @ say "Shut up or I'll leave you here without your crutch."
        
        ### ava flying up to higher floors and helping you up, more gunner stalking, he gets caught in the end, 
        
        #n "As Ava lines up another shot, the two of you are startled by a sudden loud noise that echoes throughout the building."
        
        player "Okay okay, let's just get out of here. Which is... that way I think? I'm not sure, this place is like a maze."
        
        show ava typical neutral

        n "You poke your heads out of the room you're in."

        player "Do you see anything?"

        ava @ say "Nada."
        ava @ say "Wait."

        n "You turn your head to the direction she's facing."

        ava @ say "Wasn't that window boarded up earlier?"

        player "I don't remember, there's a lot of boarded up windows."

        ava @ say "It looks like it leads outside. I'll help you through it."
        
        hide ava with dissolve

        n "Ava puts forth her best effort in pushing you through the window, though a petite bird lass like her is unable to offer much help."
        n "You basically get your upper body onto the windowsill and then roll over the edge."
        
        stop music fadeout 1.0
        
        scene bg oldhospital exterior with fade
        
        show box:
            ypos 0
        
        play music "audio/ambient/outdoors night crickets.ogg" fadein 1.0
        
        n "With the last bit of sunlight fading from the sky, it was hard to see exactly where you were crashing. And Ava wasn't waiting around to get murdered just cause your foot hurts."
        n "Fortunately you only feel nice soft grass on the ground and not broken glass."
        n "Any minute vibration in your foot still hurts like hell though."
        
        player "Ow."
        
        show ava typical neutral at center with dissolve:
            xpos 300
            yalign 0
        
        ava @ say "You alright there? Here's your cane."
        
        n "As you stand back up you swear you can hear footsteps in the grass."
        n "And yup that is definitely a pair of eyes staring at you."
        
        show gunner neutral at left with dissolve:
            yalign 0
            xzoom -1
            xpos -300
        
        gunner @ say "[name]! Ava! Sup?"
        
        show ava concerned
        
        ava @ say "Gunner? What the hell are you doing here?!"
        
        #gunner @ say "Oh y'know, just some urban exploration. Urbex as they say. Which I'm totally into by the way."
        
        #ava @ say "Dammit Gunner, [name] got hurt cause you scared us!"        
        
        gunner @ say "Oh y'know, just some urban exploration. Urbex as they say. Which I'm totally into by the way."
        
        ava @ say "I thought you had fishing trip with your frat today?"
        
        gunner @ say "Oh, that? Uhh, we decided not to, due to concerns. Ethical concerns. About fishing."
        gunner @ say "Did you know the yellowtail population has decreased by 81 percent since 1913? I just thought that was interesting."
        gunner @ say "Hey is your foot alright, [name]? I'm no expert in human anatomy but I don't think you can twist yours back 180 degrees normally."
        
        player "Yeah it's def sprained or something."
        
        show ava angry
        
        ava @ say "Dammit Gunner we thought you were a stalker and [name] got injured because of you!"
        
        gunner @ say "Hey, don't blame me because [name] clumsily tripped over their own feet!"
        
        #ava @ say "Says the scaredy cat afraid of ghosts!"
        
        #gunner @ say "Now those are actually scary!"
        #gunner @ say "I just wanted to have a nice relaxing stroll through this abandoned hospital, and by coincidence you happened to show up at the same time and [name] had an unfortunate accident."
        gunner @ say "It's not like I pushed them down the stairs or anything."
        #gunner @ say "It's your own fault for rushing."
        
        show ava annoyed
        
        ava @ say "Ugh, whatever. Let's just get [name] to a doctor. You can carry them since you're the most responsible for them getting hurt in the first place."
        
        gunner @ say "Hmph. Fine."
        
        n "You kinda tuned out of the conversation. This hospital sucks. Can you go home now? Your feet hurt."
        n "Gunner gingerly picks you up in a bridal carry. Oh god this feels so nice what the fuck."
        
        gunner @ say "Sorry about all this, buddy. I really did just wanna hang out and stuff."
        
        n "The trip to the hospital is quiet and tense."
        
        stop music fadeout 1.0
        
        scene bg hospital with fade
        
        show box with Dissolve(.2):
            ypos 0
        
        play music "audio/music/Vylet Pony - lemonade.ogg" fadein 0.1
        
        show kitsuragi at center:
            xpos -500
            xzoom -1
        show gunner neutral at center:
            xpos 350
        show ava typical neutral at center:
            xpos 533
        with dissolve
        
        kitsuragi @ say "Welp. I expected to see you again soon but not for something like this."
        kitsuragi @ say "You're lucky you have friends to drag your ass here all the time."
        
        player "It's a bonding experience."
        
        gunner @ say "Again, super sorry this happened, [name]! I'll make it up to you, I promise."
        
        show ava angry
        
        ava @ say "You better!"
        
        gunner @ say "You played your part in this happening too! I reckon you owe [name] something too!"
        
        kitsuragi @ say "I'll leave you all to figure that out on your own."
        kitsuragi @ say "[name], you're free to go whenever. Or you can stay the night, I don't care."
        
        n "You sip on the complimentary juice box she gave you for being brave while she twisted your foot back into place and nod."
        
        hide kitsuragi with dissolve
        
        show gunner with move:
            xpos 0
        
        n "Gunner and Ava awkwardly stand around, looking at the ground in opposite directions."
        n "You cough to break the silence."
        
        player "Sooooo..."
        
        show ava pose concerned
        
        ava @ say "Soooo...?"
        
        #gunner @ say "....Yeah."
        
        player "This was a fun day. If I wasn't already traumatized by hospitals, I sure will be now."
        
        show ava pose flattered
        
        ava @ say "Heh yeah... This place is even spookier than the old abandoned one, huh?"
        
        show ava typical neutral
        
        gunner @ say "You gonna stay the night here or go back to your dorm?"
        
        menu:
            gunner "{cps=0}You gonna stay the night here or go back to your dorm?{/cps}"
            "I'll stay here.":
                #finished
                player "I don't really feel like moving. I'll wait and see if my foot is better in the morning."
                
                gunner @ say "I'll stay here with you then. I don't want you to be alone in this shitty place."
                
                player "Aww, how sweet of you."
                
                ava @ say "I'll stay too!"
                
                show gunner:
                    xzoom -1
                
                player "Nah, one is enough to suffer here with me. Thanks though."
                
                show ava concerned
                
                n "Ava looks slightly disappointed but nods."
                
                ava @ say "Alright then..."
                
                show ava motivated
                
                ava @ say "I'll go but if Gunner tries to break your other leg, gimme a call and I'll come flying!"
                
                player "Heh will do~"
                
                show ava typical neutral
                
                ava @ say "Take care, [name]. I'll see you later, k?"
                
                player "For sure. Later birdy~"
                
                ava @ say "Later, human~"
                
                hide ava with dissolve
                
                gunner @ say "Cute."
                
                n "Gunner plops down in the chair across from you."
                
                player "Is this how you imagined today would go?"
                
                gunner @ say "No. I dunno how I thought it would go. I just kinda went for... *something* and hoped it would work out okay."
                
                player "Mhhm. I know how that feels."
                player "Maybe you just have to do nothing and things work out better that way."
                
                gunner @ say "You think so?"
                
                player "Sometimes. It's more uhh, natural that way?"
                player "If you try to force something to happen, it won't go the way you want it to."
                
                gunner @ say "But if I don't try, I won't get what I want. I'll just be at the mercy of whatever life throws at me."
                gunner @ say "It's not fucking fair. You don't even try and girls practically throw themselves at you."
                
                player "They do? I never noticed."
                
                gunner @ say "Wait..."
                
                n "Gunner looks like he just realized something."
                
                gunner @ say "You don't even have a scheme to get with Ava, do you?"
                
                player "A scheme? No, she just keeps inviting me to stuff and I keep going."
                
                gunner @ say "Unbelievable! Hah!"
                gunner @ say "It must be a plot to make me jealous, is that it?!"
                
                player "No dude, we just naturally get along I guess??"
                player "It's just fate that she happened to ask me to hang out first."
                player "You can't really plan for that."
                
                gunner @ say "So you're telling me to quit trying?"
                
                player "Sort of. It seems to be working for me pretty well."
                player "I think you'll reach a better outcome if you just be yourself instead of trying to manipulate events in your favor."
                
                gunner @ say "You must not know many cats."
                gunner @ say "Manipulating fate in our favor *is* our nature."
                #gunner @ say "They say every time a cat does something, Ecaflip rolls a nine sided die to determine our success."
                gunner @ say "They say our lord and savior Ecaflip gave us nine lives so we can fail and learn from our mistakes in eight of them, then succeed in our nineth."
                gunner @ say "I believe there's always a path to victory, it's just a matter of finding it and doing what you need to do to get there."
                
                menu:
                    gunner "{cps=0}I believe there's always a path to victory, it's just a matter of finding it and doing what you need to do to get there.{/cps}"
                    "Good luck with that":
                        #finished
                        player "I don't know what to say to that other than good luck."
                
                        gunner @ say "I don't need your luck. I make my own luck."
                        
                        n "Gunner's tone had become more standoffish. There's a tense moment of silence. You guess neither of you have anything left to add to the conversation."
                        n "Gunner pulls out his phone and doesn't say anything to you for the rest of the night."
                        
                        stop music fadeout 1.0
                        
                        hide box

                        scene bg black with fade

                        hide box    

                        show bg calendar
                        show tfriday at center
                        with Dissolve(.5)

                        pause .6
                        show tforwardslash
                        pause .2
                        show tbackslash

                        pause .7
                        
                        scene bg codadorm with fade
                        
                        show box with Dissolve(.2):
                            ypos 0
                        
                        n "Gunner was still a little bitter this morning, but at least he walked you home."
                    "I guess we have different ideas of fate":
                        #finished
                        player "I guess we have different ideas of fate then."
                        player "I always saw it as something you can't change. Like me being the last human and ending up in this hospital tonight with an injured ankle was unavoidable despite our illusions of choice."
                        
                        gunner @ say "Maybe it is that way for you."
                        gunner @ say "But we felines define our own fate! It is our destiny to defy the chains of uhh... destiny!"
                        
                        player "Nice self fulfilling prophecy you got there. What if your fate is to get with Ava and you're unknowingly working against it?"
                        
                        gunner @ say "Oh shit could that really happen?"
                        
                        player "You're the one who believes in real life RNG manipulation, not me."
                        
                        #gunner @ say "Just you wait, I just have to figure out the right order of steps to take and dust clouds to kick up and I'll win the lottery!"
                        gunner @ say "It's a cat exclusive ability."
                        
                        player "If you say so. I don't want us to fight over some girl though."
                        player "Bros before hoes and such."
                        
                        gunner @ say "Ay, true."
                        gunner @ say "But don't call my crush a hoe."
                        
                        player "Oh sorry."
                        player "But for real, I'm not even actively pursing anyone, I don't think? If Ava wants to go out with me or you or whoever, that's her choice."
                        #I'm just gonna let Ava decide who she wants."
                        
                        gunner @ say "I guess that's... fair?"
                        
                        player "Cool, I'm glad you're not mad at me."
                        
                        gunner @ say "Same."
                        gunner @ say "Don't expect me to hold back though. I'm gonna end up with Ava no matter what."
                        
                        player "We'll see about that."
                        
                        stop music fadeout 1.0
                        
                        hide box

                        scene bg black with fade

                        hide box    

                        show bg calendar
                        show tfriday at center
                        with Dissolve(.5)

                        pause .6
                        show tforwardslash
                        pause .2
                        show tbackslash

                        pause .7

                        #___saturday4
                        
                        scene bg codadorm with fade
                        
                        show box with Dissolve(.2):
                            ypos 0
                        
                        n "After talking with Gunner a bit more last night you both fell asleep. When you woke up you felt good enough to walk back to your dorm."
                        n "Gunner made sure you got here fine then went back to his dorm."
                        
                
                
            "Screw this place.":
                player "Yeah no, screw this place, I'm going home."
                
                n "Gunner hands you your crutch as you get into a sitting position and begin to stand up."
                
                gunner @ say "I can carry you back if you want."
                
                player "That won't be necessary."
                
                show gunner:
                    xzoom -1
                
                show ava portrait concerned
                
                ava @ say "You gonna be okay?"
                
                player "I think so, aside from the nightmares of getting stalked by hobos."
                
                show ava portrait smile
                
                ava @ say "Aww, want me to snuggle you tonight and protect you?~"

                menu:
                    ava "{cps=0}Aww, want me to snuggle you tonight and protect you?~{/cps}"
                    "Yes please":
                        $ avaPoints = avaPoints + 1
                        player "That would be delightful."
                        
                        show ava embarassed

                        n "Ava looks caught off guard, like she didn't expect that response."

                        ava @ say "I-I was just joking you know!"
                        
                        show ava at flipright

                        n "She looks away but can't hide her blush."
                        
                        show ava annoyed
                        
                        show ava at flipleft

                        ava @ say "F-f-fine! Just for tonight though!"
                        
                        player "Good enough for me!"
                        
                        hide ava
                        hide gunner
                        with dissolve
                        
                        n "Gunner quietly seethes in the corner."
                        #n "Too bad buddy, should have broken your ankle if you wanted bird snuggles."
                        n "Too bad buddy, shouldn't have gotten my ankle broken."
                        
                        #ava @ say "And you have to be the little spoon."
                        
                        n "Gunner walks you back to your dorm, being unusually quiet and ocassionally glaring at you while you joke about the day's events with Ava."
                        n "After what you've been through, it's nice to lighten up a little."
                        n "Gunner can be pissy if he wants, you're gonna enjoy some birdy snuggles tonight."
                        
                        stop music fadeout 1.0
                        
                        scene bg codadorm with fade
                        
                        #play music "audio/exports/【Music】こんにちは! ♡ [lQQkCtUahHE].opus" fadeout 1.0
                        play music "audio/music/vylet - yeah i'm ok thanks for asking.ogg" fadein 1.0

                        show box:
                            ypos 0

                        n "You made it back to your dorm in one piece."
                        n "Gunner went back to his own dorm and you left Ava to her own devices while you took a quick shower."
                        n "You step out of the steamy bathroom wearing some ultra comfy pajamas to cuddle up in. You turn your head and catch Ava preening her feathers on your bed."
                        
                        show ava reaching embarassed at center
                        
                        ava @ say "Aaa! [name], don't look!"
                        
                        player "S-sorry."
                        
                        n "She turns away from you and quickly buttons up her shirt."
                        
                        show ava annoyed at center:
                            xpos 0
                        with dissolve
                        
                        ava @ say "You should knock first!"
                        
                        player "It's my room."
                        
                        #show ava angry
                        
                        ava @ say "Still! I could have been nude!"
                        
                        player "Is that foreshadowing?"
                        
                        show ava angry
                        
                        ava @ say "No!"
                        
                        player "Dang."
                        
                        show ava typical neutral
                        
                        ava @ say "I came here for friendly clothes-on cuddling, nothing more."
                        
                        player "Well then, shall we get to business?"
                        
                        n "You crawl into bed and Ava lies down next to you, seemingly unsure of what to do next."
                        
                        ava @ say "I've never done this before..."
                        
                        player "Really? Me neither."
                        
                        ava @ say "I guess I'm supposed to..."
                        
                        n "She tries wrapping her wings around you but she struggles getting the one between the mattress and your body."
                        
                        ava @ say "God dammit why is this so difficult."
                        
                        player "Here, lemme just..."
                        
                        n "You try holding onto her but run into the same issue. Once you get your arms around her, the one pinned between her body and the mattress loses bloodflow."
                        
                        show ava bored
                        
                        ava @ say "...This isn't very comfortable is it?"
                        
                        player "Not really."
                        
                        show ava concerned
                        
                        ava @ say "We can just sleep next to each other if you want."
                        
                        show ava typical neutral
                        
                        player "Deal. Now gimme back my arm before it needs to be amputated."
                        
                        n "You eventually find a comfortable position facing away from each other but at least you can feel her soft feathers against your skin, which feels nice."
                        n "Soon you both fall asleep. Maybe it's because of your bird guardian but you don't have any nightmares."
                        
                        stop music fadeout 1.0
                        
                        hide box

                        scene bg black with fade

                        hide box    

                        show bg calendar
                        show tfriday at center
                        with Dissolve(.5)

                        pause .6
                        show tforwardslash
                        pause .2
                        show tbackslash

                        pause .7

                        #___saturday4
                        

                        scene bg codadorm with fade

                        show box with Dissolve(.2):
                            ypos 0

                        play music "audio/ambient/morning birds.ogg" fadein 1.0
                        
                        if avaPoints >= 3:
                            n "You're woken up earlier than usual by Ava's stirring."
                            n "It's not even daylight out and she's stretching and chirping and tweeting."
                            n "She rolls over and rests a wing on you."
                            
                            show ava typical neutral at center:
                                yalign 0
                                xzoom -1
                                xpos -175
                            
                            ava @ say "Morning~"
                            
                            n "You make an unsatisfied caveman grunt as your natural desire is to sleep in."
                            
                            ava @ say "I don't know why but I'm feeling really refreshed!"
                            
                            show ava overjoyed
                            
                            ava @ say "Perhaps that's the power of snuggles?"
                            
                            player "We weren't even really snuggling."
                            
                            show ava typical neutral
                            
                            ava @ say "Yeah but our bodies don't know that! It's the proximity that counts!"
                            
                            player "Next time can we at least be nude?"
                            
                            ava @ say "Hmm..."
                            ava @ say "Sure!"
                            
                            show ava portrait neutral
                            
                            ava @ say "*If* there's a next time hehe~"
                            
                            player "Wow, you really are in a great mood today."
                            
                            show ava overjoyed
                            
                            ava @ say "Breeee~"
                            ava @ say "I guess I am! Very unusual, isn't it?"
                            
                            player "Must be the endorphins."
                            
                            show ava typical neutral
                            
                            #ava @ say "?"
                            #ava @ say "Oh, endorphins. Maybe!"
                            ava @ say "Maybe!"
                            ava @ say "Nothing gets me more excited than adventure and yesterday sure was one!"
                            
                            n "Ava hops out of bed and unlocks your window."
                            
                            player "Hey, where are you going?"
                            
                            show ava typical neutral
                            
                            ava @ say "Got a busy day of shooting ahead of me!"
                            
                            player "With your camera, right?"
                            
                            ava @ say "Of course!"
                            
                            n "She takes a dive through the window. A moment later you see her swoop up into the sky."
                            
                            hide ava with dissolve
                            
                            n "Just like that, she's gone."
                            n "The cuddles were pretty disappointing but the way she smiled at you made your heart skip a beat."
                            n "You flop out of bed and pace around the room a few times."
                        else:
                            n "You're woken up earlier than usual by Ava's stirring."
                            n "It's not even daylight out and she's stretching and chirping and tweeting."
                            
                            show ava typical neutral at center:
                                yalign 0
                                xzoom -1
                                xpos -175
                            
                            ava @ say "Morning."
                            
                            n "You make an unsatisfied caveman grunt as your natural desire is to sleep in."
                            n "Ava gets up and awkwardly wanders around the room, yawning."
                            
                            ava @ say "Did you... enjoy the snuggles?"
                            
                            player "Mhm."
                            
                            ava @ say "How's your ankle?"
                            
                            player "Hurts less today."
                            
                            ava @ say "That's good. You just gonna stay in bed all day?"
                            
                            n "You take a look at the clock on your phone."
                            
                            player "Only probably for another 4 hours or so."
                            
                            show ava annoyed
                            
                            ava @ say "Well I'm gonna go out and find a good place to take some shots before the sun comes up."
                            
                            player "Have fun with that!"
                            
                            hide ava with dissolve
                            
                            n "You roll over and bury your face in your pillow."
                            n "Wait, is she mad at you or something?"
                            n "Your sleepy brain is too slow to react. She already opened the window and flew out, leaving a cool draft to chill your bones."
                            n "Too tired to get up and close the window, you pull up your blanket over your head and fall back to sleep for a few hours."
                            
                            scene bg black with dissolve
                            
                            pause .8
                            
                            scene bg codadorm with dissolve
                            
                            show box:
                                ypos 0
                            
                            n "The sun has come up and you're fully- er, mostly rested." 
                            
                        jump dayafterurbexcont
                        
                    "We can all snuggle together at my place":
                        player "Hey that's a great idea! We can all snuggle at my dorm."
                        
                        show ava waitwhat
                        
                        ava @ say "A-all three of us??"
                        ava @ say "Uhh you sure that's a good idea?"
                        
                        n "Gunner shrugs."
                        
                        gunner @ say "Eh, I'll take what I can get. I'm game."
                        
                        show ava angry
                        
                        ava @ say "W-well I'm not gonna just let you and Gunner have all the fun! I'm going too!"
                        
                        player "That settles it then! Snuggle party at my dorm!"
                        
                        show ava concerned
                        
                        n "Ava and Gunner look at each other with a uncertain expressions."
                        
                        scene bg codadorm with fade
                        
                        show box with Dissolve(.2):
                            ypos 0
                        
                        show gunner neutral at center:
                            xpos 300
                            xzoom -1
                        show ava typical neutral at center:
                            xpos -300
                        with dissolve
                        
                        gunner @ say "So...."
                        
                        show ava bored
                        
                        ava @ say "How are we gonna do this?"
                        
                        player "Good question. I'm not a pro at this by any means."
                        
                        show ava typical neutral
                        
                        n "You sit on your bed and try to recall just what you were thinking when you invited the whole love triangle to cuddle together."
                        n "Lost in thought, you don't notice your two snuggle buddies hopping onto the bed on either side of you."
                        
                        show ava at flipright
                        show gunner at flipleft
                        
                        show ava smile
                        
                        ava @ say "Let's try this. Just lie down and relax~"
                        
                        n "Ava gently pushes you onto your back and wraps her soft feathery wings around you."
                        n "A moment later, you feel Gunner's fur brushing against you from the other side."
                        
                        gunner @ say "You alright? You're shaking."
                        
                        player "Yeah, j-just cold is all..."
                        
                        n "You've never been so nervous before. You can't even think straight. Was it a mistake to bring Gunner here? Oh god what's he doing?"
                        n "You feel his scratchy tongue combing your hair like your some sort of stupid baby kitten who is too dumb to groom yourself." 
                        n "Gunner is literally grooming you."
                        
                        gunner @ say "Purrrr~"
                        gunner @ say "Calm down bro, we'll warm ya up~"
                        
                        n "This is a classic power play by felines."
                        n "First they play nice and cuddly to lower your guard, then they start licking you to assert dominance, next he's gonna try and fuck the bird in your bed."
                        
                        show ava suggestive
                        
                        ava @ say "Everything alright, [name]?"
                        
                        show ava smile
                        
                        player "Y-yeah, I just need to-"
                        
                        menu:
                            player "{cps=0}Y-yeah, I just need to-{/cps}"
                            "Turn towards Ava":
                                $ avaPoints += 1
                                n "You adjust yourself and turn to face Ava, leaving you backside to Gunner."
                                n "A risky move, as it puts you in a position of vulnerability, but it also blocks Gunner's path to Ava."
                                n "You hold onto Ava tightly, face buried in her plumage."
                                
                                player "That's better."
                                
                                show ava flattered
                                
                                ava @ say "Breee~ This works too~"
                                
                                n "You can feel Gunner staring daggers at the back of your head."
                                n "It doesn't matter though, the bird is in your arms, not his."
                                n "In retaliation, he doubles down on brushing your hair with his scratchy cat tongue, purring ever louder and even pulling your hips closer to him."
                                n "The prices you pay for love."
                                n "And you *know* neither of you are enjoying this, but Ava seems to be all for it."
                                
                                show ava portrait overjoyed
                                
                                ava @ say "Heeheehee~ You two are so cute~ *chirp!*"
                                
                                gunner @ say "*Purrpurrpurrpurrpurrpurr~*"
                                
                                show ava portrait happy
                                
                                n "Gunner's going for the humiliation tactic but as long as his paws and tongue are on you, they're not on Ava and that's the best available outcome."
                                n "You close your eyes and mentally prepare for an awkward morning."
                                n "Somehow you manage to fall asleep amidst the tension running so high."
                            "Turn towards Gunner":
                                n "It's said that to emerge victorious in war, you must be unpredictable, and that's precisely what you're going for."
                                n "You roll onto your side facing Gunner and wrap him in your arms."
                                n "Got you now, you son of a bitch!"
                                
                                gunner @ say "Oh? Whatchya doin' there, bud?"
                                
                                show ava portrait overjoyed
                                
                                ava @ say "Ohmygosh this is so hot!"
                                
                                show ava portrait concerned
                                
                                ava @ say "I mean, it's so hot in here, right?"
                                
                                show ava portrait smile
                                
                                player "Just snuggling with my bro. Nothing wrong with that, is there?"
                                
                                n "You pull him in so tight he won't even think about escaping."
                                
                                gunner @ say "N-no, of course not!"
                                
                                n "He gives you a lick with his rough tongue on your face and digs his claws into your side."
                                n "Better you than Ava you suppose."
                                n "At least she's enjoying the show."
                                
                                ava @ say "You two are so cute~"
                                
                                n "You feel her nuzzle the back of your head and lay her wing on top of you. You make sure Gunner's paw gets nowhere near it."
                                n "You close your eyes and mentally prepare for an awkward morning."
                                n "Somehow you manage to fall asleep amidst the tension running so high."
                                
                        stop music fadeout .7
                                
                        scene bg codadorm with fade
                        
                        show box with Dissolve(.2):
                            ypos 0
                        
                        play music "audio/ambient/morning birds.ogg" fadein 1.5
                        
                        n "When your consciousness begins to reboot the following day, you question whether yesterday's events were just a dream until you realize you have a bird in your arms."
                        n "And then comes the nightmarish reality that is a snoozing Gunner inches from your face."
                        n "Somehow in the middle of the night you and Ava switched position so that she was in the middle of you two."
                        n "You guess this round of flirting with Ava ended up being a draw."
                        
                        show ava typical neutral at center:
                            xpos -200
                            xzoom -1
                        with dissolve
                        
                        ava @ say "*Yaaawn~*"
                        ava @ say "Morning~"
                        
                        player "Sleep well?"
                        
                        show ava overjoyed
                        
                        ava @ say "Amazingly well!"
                        
                        show ava typical neutral
                        
                        ava @ say "How's your ankle?"
                        
                        player "Fine, I think."
                        
                        n "You pull the blanket away and set foot on the floor."
                        n "It's still painful but you can deal with it."
                        n "Gunner begins to stir, stetching out his arms and yawning."
                        
                        show gunner neutral at center:
                            xpos 200
                        with dissolve
                        
                        gunner @ say "Morning cutie~"
                        gunner @ say "Oh hey [name], didn't see ya there."
                        gunner @ say "Man, they really hooked you up with the best everything in here huh? Your bed is so much softer than the one in my dorm."
                        
                        player "Yeah well don't get used to sleeping in it. My ankle's all better so you can go home now."
                        
                        gunner @ say "Oof, kicking us out so soon? Was I not a good snuggler?"
                        
                        ava @ say "You were pretty good! Both of you were!"
                        
                        player "Sorry, I've just got a busy day ahead of me."
                        
                        gunner @ say "That's alright, we'll head out soon. Thanks for having us over~"
                        
                        n "Gunner purrs and gives you a playful lick, surely an attempt to intimidate you, as he gets out of bed."
                        
                        gunner @ say "If either of you need top tier snuggles again, you know where to find me~"
                        
                        ava @ say "I'll keep both of you in mind~"
                        
                        player "See you two later."
                        
                        hide gunner
                        hide ava
                        with dissolve
                        
                        jump dayafterurbexcont
                                
                                
                        
                        #"gunner snuggles behind you. you're starting to regret this"
                    
                    
                        #gunner licks ava and you
                        
                    "Spill your spaghetti":
                        player "N-no thanks, that's what my tulpa waifu is for."
                        
                        #ava @ say "Do you wanna snuggle Gunner instead?"
                        
                        show ava waitwhat

                        ava @ say "You have a tulpa?"

                        n "Fuck, why did you say that?"

                        ava @ say "That's so cool!"

                        player "Really?"
                        
                        show ava overjoyed
                        
                        ava @ say "You should tell me about her!"
                        
                        player "M-maybe later..."
                        
                        n "Great, now you have to make up a schizo imaginary girlfriend to impress Ava."
                        n "Or make her jealous."
                        
                        show ava typical neutral
                        
                        player "Let's get out of this hospital first. I'm already sick of being here."
                        
                        gunner @ say "Agreed."
                        
                        hide gunner
                        hide ava
                        with dissolve
                        
                        n "Ava and Gunner walk you back to your dorm. Ava asks if you're sure you don't need a snuggle buddy but you're still too ashamed from before to take her up on the offer."
                        n "That and you don't want Gunner to break your other ankle tonight."
                        n "Thankfully he acts pretty chill on the way back, and you all make light of the events of the day."
                        n "After what you've been through, it's nice to ease up a little."
                        n "Your ankle still kinda hurts but you make it back to your dorm and get into bed, texting your friends until you fall into slumber."
                        
                        stop music fadeout 1.0
                        
                        scene bg black with fade

                        hide box    

                        show bg calendar
                        show tfriday at center
                        with Dissolve(.5)

                        pause .6
                        show tforwardslash
                        pause .2
                        show tbackslash

                        pause .7

                        #___saturday4

                        scene bg codadorm with fade

                        show box with Dissolve(.2):
                            ypos 0

                        play music "audio/ambient/morning birds.ogg" fadein 1.0

                        jump dayafterurbexcont
        
    else:
        n "At least you can get some extra credit by going to that parade today."
        n "That way you'll be able to work 2\% less hard and still pass your history class, which sounds like a fair tradeoff."

        scene bg town with fade
        
        play music "audio/music/vylet - manehattan's finest.ogg" fadein .5

        show box with Dissolve(.2):
            ypos 0

        n "As you've come to expect, your sense of timing as well as your sense of direction have failed you yet again."
        n "It's way past when the parade was scheduled and you're still stuck on some backroads looking over your shoulder wondering when you'll get shanked."
        n "Maybe you should just call it quits and try going back home, if you can find it that is."
        n "For the nth time, your map app has you pointed in the exact opposite direction you're facing and is telling you to walk in circles for the next two hours."
        n "You have to mentally figure out where you are and plot your own course like it's the fucking 1800s."
        n "Ok, you think you just have to cross this street here then round that corner and it's mostly a straight shot to-"

        rose "What the hell are you doing?!"

        n "You feel someone grab onto the back of your shirt and pull you onto the sidewalk."
        
        player "Hey, get your paws off me!"
        
        n "A moment later a semi truck speeds through the street, right where you had stepped foot a mere fraction of a second ago."
        
        show rose angry at center with dissolve

        rose @ say "How dumb are you? You would have been dead if I didn't just save your ass!"

        player "Wha?"

        n "You blink, dumbstruck as your brain replays everything that just happened in slow motion."

        rose @ say "Didn't you ever learn to look both ways before crossing?"

        player "I did! The light even said to cross!"

        n "You point to the crosswalk sign, but to your surprise it says \"DO NOT CROSS\""
        n "It turns to white and says to cross a second later."

        player "How the...? I was sure I looked before I crossed! There weren't any cars!"

        show rose unimpressed

        rose @ say "Ugh, where's your wrangler when you need them?"

        n "There's no way to respond to that without sounding mad so you just keep quiet."

        rose @ say "Where are you trying to get to anyway? Everywhere is closed for the holiday."

        player "The parade?"

        rose @ say "Ended an hour ago."

        player "I figured. I just wanna go home now."

        rose @ say "*sigh*"
        rose @ say "I know natural selection wants you dead, but letting my project partner die on the streets might affect my grade so..."
        rose @ say "I guess I'm walking you home."

        player "I can walk myself home."

        rose @ say "You sure? Cause you were going the wrong way."

        player "Fine, if you really wanna take me home so bad you can."

        show rose armscrossed angry

        rose @ say "I don't want to walk you home but you obviously can't be trusted to do anything on your own!"

        player "Whatever, just lead the way."

        hide rose with dissolve

        n "Rose scowls and heads in the opposite direction, taking you down streets and alleyways that start to look more familiar as you get closer to campus."
        n "For someone so short she walks pretty quick. You can barely keep up."
        n "She only slows down when a large crowd blocks her way."
        n "When the crowd disperses a lone figure in robes stands in the middle of the sidewalk."
        n "He turns around and looks down at you and Rose."

        show fortune at center with dissolve:
            xpos 300

        fortune @ say "I've been expecting you."

        player "Huh? Who are you?"

        show rose neutral at center with dissolve:
            xzoom -1
            xpos -300

        rose @ say "He's just some homeless guy."
        rose @ say "Move. You're in the way."
        
        show rose:
            linear .5 xpos -150    
        pause .1
        show fortune with move:
            xpos 450

        n "Rose tries to walk around him but he steps in her path."

        fortune @ say "Homeless I am not. The world is my home."
        
        show rose unimpressed

        rose @ say "Even worse than homeless, this guy's a hippie."
        #Oh he's worse than I thought, he's a hippie."

        n "Rose tries once more to manuever around him, but it's almost like he knows which direction she'll go before she does."
        
        show rose:
            linear .4 xpos -250    
        pause .1
        show fortune with move:
            xpos 350
            
        pause .3
        
        show rose:
            linear .5 xpos -100    
        pause .1
        show fortune with move:
            xpos 500
        
        show rose angry

        rose @ say "Get out of the way!"

        #rose @ say "You're starting to piss me off. Move or you'll regret it!"
        
        show rose roseknife
        
        show rose:
            ypos 15
            linear .15 ypos 0

        n "Rose pulls something out from her pocket out of view of the hobo and holds it concealed in her clenched fist."
        n "Is that a... knife?"

        fortune @ say "Your blade does not deter me. I have seen the future. You are harmless."

        n "Rose grips her knife tighter."

        rose @ say "What do you want? Money? Nobody carries cash anymore."
        
        #fortune "I have no need for money, everything I work with is free."
        fortune @ say "I am merely one of fate's messengers."
        fortune @ say "You may decline to hear your fortune if you wish, but it will reach you one way or another, sooner or later."
        #fortune teller gives rose a false fortune, knowing that she doesn't pay?
        
        show rose unimpressed

        rose @ say "Good to know. I'll decline your \'fortune\' thank you."

        show rose neutral

        rose @ say "Come on, [name], I'm not sticking around."
        
        show rose:
            ypos 15
            xzoom 1
            linear .15 ypos 0
        
        pause .33
        
        show rose with move:
            xpos -450

        n "Rose starts to walk across the street to the other sidewalk."

        $ gnugift = False

        menu:
            n "{cps=0}Rose starts to walk across the street to the other sidewalk.{/cps}"
            "Aw come on, I wanna hear my fortune!":
                player "Aw come on, I at least wanna hear my fortune!"
                
                show rose:
                    ypos 15
                    xzoom -1
                    linear .15 ypos 0

                rose @ say "Why? He's just gonna make up some bullshit."
                rose @ say "Here's my fortune: I'm gonna walk back to campus without you and you'll get hit by a car and die."

                fortune @ say "Wrong."

                #rose @ say "What did you say?"

                fortune @ say "[name] will not perish today. Nor tomorrow, nor the next day."
                fortune @ say "There is something special about you. Your fate diverges. It is not yet sealed."
                fortune @ say "It seems you have a mission in life to be completed before you pass away."

                player "Wait, so I'm not dying?"

                fortune @ say "Not yet."

                rose @ say "Could you be any more vague?"

                player "Rose, this guy might be legit! He knew my name and I didn't even tell him!"

                rose @ say "He probably just overheard me saying it!"

                fortune @ say "Your fate is also divergent, Rose."

                player "See, he even knows your name too!"

                show rose angry

                rose @ say "Because you just said it!"

                fortune @ say "Perhaps your destiny is related to [name]'s? Unfortunately, I cannot give definitive answers for such people."

                show rose neutral

                rose @ say "What a great fortune teller you are."
                rose @ say "Now if you're done, we'll be on our way."

                fortune @ say "There is more. I can see several potential destinies and the paths you may take to reach them."
                fortune @ say "For a small donation I will-"

                rose @ say "Forget it. Like I said, nobody carries cash anymore, boomer."
                
                fortune @ say "I take etherium. My wallet address is 0x1AF7aD03CbB3e40a55392D518D585eA3EBB8F4B8."
                
                rose @ say "Cryptocurrency is fake and- "
                
                n "A nearby truck drives by and honks it's horn, cutting off the end of Rose's sentence before she walks off."
                
                show rose:
                    ypos 15
                    xzoom 1
                    linear .15 ypos 0
                    
                pause .2

                show rose with move:
                    xpos -1500

                #n "Rose waits for an opening in traffic and crosses the street."

                fortune @ say "Ah of course. You zoomers will donate to millionaire streamers and girls taking photos of their hooves in bad lighting online but won't even consider giving to the needy?"

                player "Sorry, I don't have any cash either."
                
                fortune @ say "What about that bill you're carrying in your back pocket?"

                player "What? I don't have a-"

                n "You reach into your pocket and to your surprise pull out a five dollar bill."

                fortune @ say "You have history with that young lady, don't you?"

                player "Not really? I only just met her recently and- oh you mean history class?"

                n "The fortune teller smiles and winks."

                fortune @ say "I think I know how you can have a future with her as well."

                n "Give money to the fortune teller?"

                menu:
                    n "{cps=0}Give money to the fortune teller?{/cps}"
                    "Yes":
                        $ gnugift = True
                        n "You won't be any poorer for giving him the money since you didn't realize you had it in the first place."
                        n "You hand over the crumpled bill and await the wisdom of the gnu."
                        n "He leans over and takes it with his teeth and begins chewing on it."
                        n "With your hand still extended, he grabs hold of it and places something in your palm and wrapping your fingers around it."

                        fortune @ say "Carry that with you. You'll need it someday soon."

                        n "With that, the gnu steps back and into the shadows."

                        hide fortune with dissolve

                        n "You unclench your fist and look down at what he gave you."
                        n "It's a short cable with a USB C connector at one end and a headphone jack input on the other."
                        n "What the hell kind of puzzle game bullshit is this?"
                        n "You look up with a confused expression, ready to ask what this is for but the fortune teller is nowhere to be found."
                    "No":
                        player "Thanks but I'd rather let it come as a surprise."

                        fortune @ say "Fair enough. I won't keep you any longer."

                        n "The gnu steps back and into the shadows."

                        hide fortune with dissolve

                        n "Man, that was weird."
                        n "But at least you came out five dollars richer than you thought you were."

                n "You look around for Rose and see her among a crowd of people waiting for the next crosswalk light."

                player "Hey, wait up!"

                n "You chase after her, narrowly avoiding getting hit by a car as you jog across the street."
                n "Rose glares at you and shakes her head."
                
            "Yeah, let's bail":
                player "Yeah, let's get away from this weirdo."

                fortune @ say "As you wish. I won't keep you from your fate any longer."

                n "The gnu steps back and into the shadows."

                hide fortune with dissolve

                n "You follow Rose, looking over your shoulder."
                n "Luckily that creepy gnu isn't following you."
                n "In fact, it's like he vanished into thin air."

        n "When you get close to the campus, Rose chases you away with some colorful vocabulary and you hurry back to your dorm, ready for a nice long sleep."

        #meet fortune tellers. Rose is skeptical and gets angry when teller says they will end up together, refuses to pay
        #teller mentions coda has a terrible fate coming but warns not to worry about it
        
        stop music fadeout 1.0

        scene bg codadorm with fade

        show box:
            ypos 0

        n "Drained from today's excursion, you flop onto your bed and pull up the covers, falling asleep quickly."

        hide box

        scene bg black with fade

        hide box    

        show bg calendar
        show tfriday at center
        with Dissolve(.5)

        pause .6
        show tforwardslash
        pause .2
        show tbackslash

        pause .7

        #___saturday4

        scene bg codadorm with fade

        show box with Dissolve(.2):
            ypos 0

        play music "audio/ambient/morning birds.ogg" fadein 1.0


label dayafterurbexcont:
    ###with the removal of the story, this part needs tweaking. just make it a one off urge to write
    n "Yesterday was a bit much. You need to relax and recover today."
    n "You suddenly recall something you had started to do to pass the time in recent years."
    n "You didn't have much else to do at home so you began writing."
    n "Just writing whatever kind of stories popped into your head. It was therapeutic in a way."
    #n "You suddenly recall the urge you had to continue work on your story last week."
    n "That sounds like a nice way to spend the day."
    #n "Beats studying and doing homework, and you're not quite energized enough to hang out with anyone at the moment."
    #n "You search around for your old flash drive with all your notes on it."
    #n "When you find it, you plug it in to make sure it's the right one and not the one full of obscene images."
    #n "Yup, this is it."
    n "You stuff your laptop into your bag and sling it over your shoulder before heading out."

    stop music fadeout 1.0

    scene bg cafe with fade

    show box:
        ypos 0

    #play music "audio/coffeeLoveInstrumentalEditexe.ogg" fadein 1.0
    play music "audio/music/vylet - I Wish I Could Tell You.ogg" fadein 1.0

    n "What better place to write than a cafe?"
    n "You step up to the counter to order your required caffeinated beverage."

    show mishka neutral at center with dissolve:
        xzoom -1
        
    mishka @ say "Hello [name]! What it is I can get for you today?"
    
    n "You place your order and she gets started on it while you find a place to set up your laptop."
    
    show mishka at flipleft
        
    pause .3

    show mishka neutral at offscreenleft with move:
        yalign 0
        
        
    #n "You order the usual and find a place to set up your laptop."
    n "As you're catching up on your insane writings, Mishka walks up to you with two drinks in her hands."

    show mishka anxious grin at center with move:
        xzoom -1
        xpos 1750

    mishka @ say "Here's your drink~"

    player "Thanks."

    n "Mishka continues to hover over you as you scald your tongue on 200 degrees of hot coffee."
    
    show mishka shy grin

    mishka @ say "..."

    player "...?"

    mishka @ say "What your working on?"

    player "Just a story thing."
    
    show mishka shy -grin

    mishka @ say "Oh? For class or for a fun?"

    player "Just something to pass the time I guess. I used to be really into writing but just kinda stopped at some point."
    
    show mishka happy

    mishka @ say "Ah, that is so cool!"
    
    show mishka neutral
    
    mishka @ say "I once wrote little stories but now I'm content to only read them."

    player "Really? What kind of stories do you like?"

    mishka @ say "I read much of medieval fantasy stuff!"
    mishka @ say "I also liked the slavic fan fictions of western media."

    player "Really? That's a thing?"

    mishka @ say "Oh yes, there is big community for it! I would even download fan dubs of your cartoons to watch. They are so much more lighthearted compared to old Soviet reruns!"
    mishka @ say "It was good escapism when shells were landing near village."

    player "...Shells?"
    
    show mishka depressed

    mishka @ say "Ehh, it's not important. Sorry to bring it up."
    
    show mishka happy
    
    mishka @ say "But this is how I started to be learning English!"
    
    show mishka neutral 
    
    mishka @ say "I could hardly get enough of reading the stories!"
    
    #mishka @ say "I often would have no familiarity with the source material while reading the fanfics so it was always a surprise finally to see the originals!"
    
    $ mishkaWriting = False

    menu:
        mishka "{cps=0}I could hardly get enough of reading the stories!{/cps=0}"
        "Would you like to know what this one's about?":
            #finished
            $ mishkaWriting = True
            
            n "You're hesitant to reveal your writing to anyone you personally know, but Mishka seems pretty open to this kind of thing so maybe she won't make fun of you?"

            player "Would you like to know what this one's about?"
            
            show mishka overjoyed

            mishka @ say "Zvichayno!!!"

            player "Heheh I'll take that as a yes."
            
            show mishka shy grin

            mishka @ say "Xaxa yes, of course of course!"

            n "Mishka sits down across from you and you explain the plot so far. She nods and seems to not only understand your overly convoluted lore but enjoy it as well."
            
            show mishka neutral

            mishka @ say "Wow [name], that sounds pretty neat!"

            player "Really? You think so? I was afraid it would sound lame when I said it aloud."

            mishka @ say "No no no, you clearly put a lot of effort into this!"
            mishka @ say "Is there somewhere I can read the whole thing?"

            n "You tell her the name and site it's uploaded on and she types it into her phone."

            mishka @ say "Oorah! I'll check it out when I have a chance!"

            hide mishka with dissolve

            n "Mishka continues to sit with you and chat while you work on your story. The cafe is empty so it's not like she has to go back to work anyway."
            n "She even moved her seat right next to your so she could read your screen. You've never really been this close to her before since she's always been behind a table."
            n "She smells like lavender."
            n "You bounce a few ideas off her and she gives some good feedback as well as a few ideas of her own."
            n "After you've spent a few hours at the cafe, you've got a near-final draft ready and your table is littered with empty coffee cups."

            show mishka neutral at center with dissolve:
                xzoom -1

            mishka @ say "*Yaaaawn*"
            mishka @ say "Welp, it's about time to close down."

            player "Damn, did I really spend all day here?"

            mishka @ say "You did!"
            mishka @ say "Not that I mind though!"
            
            show mishka happy
                        
            mishka @ say "It was good to help you with your writings!"

            player "Haha I appreciate the help! I'll go over this one more time before posting it online."
            
            show mishka neutral

            mishka @ say "I can't wait to read it!"

            hide mishka with dissolve

            n "You help Mishka throw away all the cups and wipe down the table before saying goodbye and returning to your dorm for the night."

        "I should really get back to work":
            #finished
            #+1 point for everyone else
            $ roriPoints += 1
            $ ellenPoints += 1
            $ rosePoints += 1
            $ avaPoints += 1
            $ clairePoints += 1
            player "Nice!"
            player "I should get back to work on mine though. Thanks for the coffee!"
            
            show mishka sad

            n "Mishka looks slightly taken aback."

            mishka @ say "O-oh, right of course. I should get back to work too..."
            mishka @ say "Well I'll let you alone for now."
            
            #show mishka despondent 
            show mishka anxious
            
            mishka @ say "Uhh let me know if you need more coffee!"

            hide mishka with dissolve

            n "She awkwardly walks back to the counter and pulls out a book."
            n "It dawns on you that she probably wanted to sit with you and hear about your story."
            n "Well dang, now you feel bad."
            n "It's too late to invite her back over so you might as well actually get started writing this next chapter."
            #n "You quickly review your wikiped page to refamiliarize yourself with the plot."
            n "The more you write, the more you get into it"
            n "You had forgotten how much you really enjoyed this."
            n "After you've spent a few hours at the cafe, you've got a near-final draft ready and your table is littered with empty coffee cups."

            show mishka despondent at center with dissolve:
                xzoom -1

            mishka @ say "*Yaaaawn*"
            mishka @ say "Welp, it's about time to close down."

            player "Damn, did I really spend all day here?"

            mishka @ say "Yup."
            mishka @ say "Time flies when you're busy I suppose."
            mishka @ say "I hope you got a lot done."

            player "Yeah, I think I'll post this chapter tonight."
            
            show mishka neutral

            mishka @ say "Oh?"
            mishka @ say "Well good luck [name]!"
            mishka @ say "I hope people enjoy to read it!"

            player "Thanks!"

            hide mishka with dissolve

            n "You help Mishka throw away all the cups and wipe down the table before saying goodbye and returning to your dorm for the night."
            n "You wonder if you should have told her what you were writing or if she would have thought it was lame."
            n "You've never told somebody you personally know about it before. You prefer to post anonymously."
            n "If someone in irl found out you were responsible for this dumb indulgent fanfiction..."
            n "You shudder to imagine how your friends would view you afterwards."
            n "But after spending all day writing, you remember what drew you into this in the first place."
            n "The waifus."
            n "It's always been about the waifus."

    hide box

    stop music fadeout 1.0

    scene bg black with fade

    hide box

    show bg calendar
    show tsaturday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    #___sunday4
label movienight:
    
    scene bg campus with fade

    play music "audio/ambient/outdoors people talking.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0

    #n "The next couple of days passed by so uneventfully you can hardly even recall what happened."

    #n "After going back to your dorm, you posted your writings then closed your laptop, not wanting to think about how people will react to it."
    #n "You had fun writing it but that doesn't mean others will enjoy reading your trash."
    n "The following day, you find yourself wandering aimlessly around the campus, alone with your thoughts."
    n "A dangerous game."
    n "As you pass by the cafe, you caught a glimpse of Rori and Gunner inside sitting by a window."
    n "Too late to turn away now, they already saw you and are waving for you to come inside."
    n "You had wanted to be mysterious and broody today but you guess your friends had other plans."
    
    scene bg cafe with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    play music "audio/music/mere - coffeeLove.exe.ogg" fadein 1.0
    #play music "audio/music/vylet - Catching On.ogg" fadein 1.0
    
    show gunner neutral at offscreenleft:
        yalign 0
    show rori neutral at offscreenleft:
        yalign 0
    
    pause .1

    show gunner neutral at center:
        xzoom -1
        xpos 1550
    show rori neutral at center:
        xpos 1270
        xzoom -1
    with move

    gunner @ say "Sup [name]!"

    rori @ say "Hi there!"

    player "Hey guys. I'm not interrupting anything, am I?"

    gunner @ say "Nah, Rori was just showing me some math stuff."

    player "How's that going?"

    rori @ say "It's... not."

    show ava typical neutral at offscreenright:
        yalign 0
    show claire sweater neutral at offscreenright:
        yalign 0

    n "You turn your head as you hear the door open behind you and a familiar bird and bunny walk in."

    show ava typical neutral at center:
        xpos 275
    show claire sweater neutral at center:
        xpos 650
    with move

    ava @ say "Well look who it is~"
    
    show claire sweater overjoyed
    
    claire @ say "Oh my gosh [name]! What a coincidence meeting you here!~"

    player "It's not much of a coincidence. It feels like I'm here whenever I've got free time."
    
    show claire sweater leaning

    claire @ say "Is that so? I'll have to start coming here more often then~"
    
    #claire @ say "Ooh, are these your friends?"
    
    n "Claire turns to Rori with a friendly grin."
    
    show claire sweater wave
    
    claire @ say "Hiya! I don't think we've met! I'm Claire and this is Ava!"
    
    show rori anxious
    show claire sweater neutral

    #ava @ say "Oh right! I remember seeing you with him before! Gunner was it?"

    #gunner @ say "Yup, that's me."

    #claire @ say "And who might you be?"

    #rori @ say "M-me? My name's Rori. Nice to meet you."
    
    n "Rori looks kinda nervous. You're not sure if it's because he's shy or if it's just Claire intimidating him."
    
    rori @ say "Nice to meet you. My name's Rori."
    
    if roriparty == True:

        claire @ say "OMG I remember seeing you at that party the other week! I can't believe you did that thing!"
        
        show rori at shudder

        rori @ say "O-oh yeah?"

        player "What thing?"

        rori @ say "N-nothing!"
        
        show ava portrait neutral
        
        ava @ say "We'll just be moving along now. Don't mind us!"
        
        n "Ava drags Claire away from the blushing ram to avoid further embarassing him."
        
        gunner @ say "Bye guys! Talk to you later!"
        
    else:
        claire @ say "I like your horns~"
        
        show rori neutral

        rori @ say "I- my... horns? Thanks? I don't really do anything too fancy with 'em."

        show ava annoyed

        ava @ say "Claire can you please stop flirting with every boy you meet"

        claire @ say "Hey I hit on girls too."
        
        show ava typical neutral

        ava @ say "This is why I'm embarassed to go out in public with you."

        claire @ say "Ksksksks love you too Ava <3"
        
        show ava portrait neutral

        ava @ say "We'll just be moving along now. Don't mind us!"

        gunner @ say "Hey it's no problem, awkward flirting is infinitely more fun than doing math problems."

        ava @ say "See you around, guys!"
        
        show claire sweater leaning

        claire @ say "À un de ces quatre! Ksksksksk!"

        player "Later guys. And good luck with the homework."

    hide gunner
    hide rori
    hide ava
    hide claire
    with dissolve

    n "You walk up to the counter with Ava and Claire at your side."
    #n "As usual, Mishka is there to greet you with a smile... or half of one. Maybe a third."
    n "As usual, Mishka is there to greet you."

    show mishka shy at center with dissolve:
        xzoom -1
        xpos -400

    mishka @ say "Hello again [name]! What for you can I get?"

    player "The usual please."

    n "You scan your card and step off to the side."
    
    show mishka neutral

    mishka @ say "And for you two?"

    show ava typical neutral at center:
        xpos 225
    show claire sweater neutral at center:
        xpos 600
    with dissolve

    claire @ say "Can I get a large chai tea latte, hot, with almond milk and extra honey and salt aaaaaand three cinnamon buns?"
    
    #player "You don't have to get me anything lol"
    player "Oh nice you're getting a cinnamon bun for everyone?"
    
    show claire sweater surprised
    
    claire @ say "Huh? No I'm not?"
    
    n "Oh god they're all for her, aren't they?"
    
    #show claire sweater neutral
    show ava pose ohyou
    
    ava @ say "Cinnamon buns for the bun~"
    
    show claire sweater embarassed
    
    claire @ say "I gotta maintain my figure somehow!"
    
    show ava typical neutral
    
    ava @ say "I'll just have a mocha please!"
    
    show claire sweater neutral
    
    mishka @ say "Konyechnya! I'll have that ready for you all shortly!"

    hide mishka with dissolve

    n "While Mishka starts work on your orders, you hang off to the side with Ava and Claire."

    claire @ say "So, got any plans for the rest of today, [name]?"

    player "Hmm... Not really. Pretty lazy day honestly."

    ava @ say "A lazy day every now and then is nice."
    
    show claire sweater heyeah

    claire @ say "I looooove staying in bed all day, wrapped up in a nice warm blanket and watching movies."
    
    show claire sweater giggle
    
    claire @ say "*Gasp*"
    
    show claire sweater overjoyed
    
    claire @ say "[name] we should have a movie night!"
    
    show ava overjoyed

    ava @ say "Ooh, that sounds fun~"
    
    player "I dunno, my dorm is kind of a wreck and I don't have anything to watch and"
    
    show claire sweater neutral
    show ava typical neutral

    claire @ say "Come on, you promised!"

    player "I did? I don't remember that..."
    
    show ava smile
    
    ava @ say "Yeah, I'm pretty sure we talked about this before."
    
    player "Am I being gaslit right now?"
    
    #show ava annoyed
    show ava typical neutral
    
    ava @ say "No, you definitely promised us a movie night at some point."

    claire @ say "Perfect! We'll meet at your dorm at 7 then!"
    claire @ say "You better pick out some good movies~"

    n "In that case you'll have to dust off your old pirate hat and update your torrent client when you get back to your dorm."
    #n "What kind of movies do normies like again?"
    if mishkaWriting == True:
        n "Maybe you should invite Mishka over as well. She's always had your back even though you hardly know her."
    else:
        n "Maybe you should invite Mishka over as well. She's always had your back even though you've never even hung out with her."
    n "She walks over with your drinks right at the perfect time."

    show mishka neutral at center with dissolve:
        xzoom -1
        xpos -350

    mishka @ say "Here's your drinks and cinnamon buns! Enjoy!"

    player "Thanks!"
    player "Hey uh Mishka, I was wondering if you'd wanna come hang out with us later today. We're gonna be watching some movies at my dorm."

    show mishka sad
    
    mishka @ say "Oh? I'd love to, but unfortunately I am having a busy today..."
    mishka @ say "Perhaps another day?"

    claire @ say "Aww... Don't worry Mishka, we'll find a day where we can all hang out together!"
    
    show mishka happy

    #mishka @ say "Hehe thanks! I'm usually very busy though but I appreciate the gesture!"
    mishka @ say "Really..? I would very appreciate that!"
    
    show mishka neutral

    ava @ say "Yeah, you're really cool! You must be really busy though having to work here all the time on top of going to class."

    show mishka depressed

    mishka @ say "Heh, yeah... class and work all of the time..."
    
    show mishka despondent
    
    mishka @ say "Well uh, here your foods and drinks. Be careful, they are hot!"

    player "Thanks again Mishka! We'll see you later!"

    hide mishka with dissolve
    
    pause .1
    
    show ava:
        xpos -100
    show claire:
        xpos 400
    with move

    n "On your way out, Ava stops you."
    
    show ava excited

    ava @ say "Why don't we invite them to come along too? They seem pretty cool."
    
    show claire sweater leaning

    claire @ say "Ah I see how it is. You wanna spend some time with that Gunner boy, donchya?~"
    
    show ava annoyed at flipright

    ava @ say "You're the one who was into that cute ram!"
    
    show ava angry 
    show claire sweater heyeah

    claire @ say "Ksksksks so now you think Rori's cute too?"

    ava @ say "Claire I swear on my tyrannosaurus ancestors-"

    n "You let them continue bickering while you approach Gunner and Rori."

    hide ava
    hide claire
    with dissolve

    show gunner neutral at center:
        xzoom -1
        xpos -300
    show rori neutral at center:
        xpos 400
    with dissolve

    player "Hey guys. Apparently I'm hosting a movie night tonight. Wanna come with so I'm not stuck listening to these two bicker for hours all on my lonesome?"

    gunner @ say "Oh hell yes."

    rori @ say "W-well, I guess I could skip tonight's raid and join you. What are you all watching?"

    player "To be honest I have no idea. I was just gonna download whatever comes up when I search 'guns cars explosions movie'"
    
    show rori laugh

    rori @ say "I've got a flash drive with a bunch of kinos we could watch!"

    player "Sweet, that works! See ya at my dorm at around 7!"
    
    show rori neutral

    gunner @ say "We'll be there!"

    n "You give a thumbs up then turn back to Ava and Claire."

    hide gunner
    hide rori
    with dissolve

    show ava typical neutral at center:
        xpos -350
        xzoom -1
    show claire sweater neutral at center:
        xpos 350
        #xzoom -1
    with dissolve

    player "They're on board."
    
    show ava overjoyed

    ava @ say "Awesome! We'll see ya later tonight [name]!"
    
    show claire heyeah

    claire @ say "Yeah, thanks for hosting! I can't wait~"

    stop music fadeout 1.3

    scene bg codadorm with fade

    ##play sound "ambient/outdoors night crickets.ogg"

    show box with Dissolve(.2):
        ypos 0

    n "Later that evening..."
    
    play music "audio/ambient/outdoors night crickets.ogg" fadein 1.5

    player "Gosh darn dangit raptor jesus god gosh darn dammit goshhhh"
    player "Where the heck is Rori???"

    n "It's a bit past 7 o'clock and he's still not here and your backup movie you began torrenting stalled."
    n "You hear some noise outside your door followed by knocking."
    n "Please let that be Rori."

    show rori neutral at center with dissolve
    
    play music "audio/music/Vylet Pony - Cozy Pone.ogg" fadein .5
    #play music "audio/music/vylet - リラックス.ogg" fadein .5

    rori @ say "Hi! Sorry I'm late."

    player "It's fine. Did you bring the movies? And where's Gunner?"
    
    rori @ say "He's running a little late but he'll be here. And yeah I got 'em right here."

    n "He whips out a flash drive."

    player "Cool, let's see what you got."

    n "You plug the drive into your laptop and browse the files on it."
    n "Deer god..."
    n "Why are half of these file names in Japanese?"
    n "Rori, you didn't..."
    n "You open one and skip to the middle and are greeted with a barrage of bright colors and a high pitched \"ONI-CHAAAAAAN!~\""
    n "You immediately slam the laptop lid shut."
    n "What the fuck Rori"

    player "I thought you said you had some good movies..."

    show rori laugh

    rori @ say "These *are* good."

    player "How am I supposed to explain this weeb shit to a normie like Ava?"
    
    hide rori with dissolve

    n "Before you can come up with a backup movie, you hear another knocking at your door."
    ###hotline miami door sound effect
    n "As you turn the knob, Claire's fat bunny ass bursts through the doorway, knocking you onto the ground, semi-conscious."

    show ava typical neutral at center:
        xpos 50
        xzoom -1
    show claire sweater wave at center:
        xpos -450
        xzoom -1
    show gunner neutral at center:
        xpos 650
    with dissolve

    claire @ say "Heyyyy~"
    
    show ava pose ohyou
    show claire sweater neutral

    ava @ say "I hope you didn't start without us haha"
    
    show ava pose happy

    gunner @ say "Heya [name]. I see Rori made it here in one piece."

    n "Yeah not to mention he brought 12 gigabytes of One Peace."
    n "You pick yourself off the ground and welcome everyone in."
    
    player "Come on in guys, I'm glad you could make it!"
    player "Help yourself to some snacks. I have some sodas in the mini fridge too if you want any."

    ###if gunner was in your dorm before
        #gunner @ say "Daaaamn, I didn't notice it before but your dorm came with a mini fridge?"

    gunner @ say "Daaaamn, your dorm came with a mini fridge?"
    
    n "Gunner picks up the empty box of dino nuggies you left beside your microwave."
    
    gunner @ say "You even have a microwave! They don't allow us peasants to have these cause someone managed to burn down a whole dorm building with one."

    show claire sweater lusty alert

    claire @ say "Pretty swanky place you got here~"
    
    show claire sweater neutral -alert

    player "Thanks. Go ahead and have a seat wherever and we'll start watching something."
    
    show ava -pose overjoyed

    ava @ say "Hey Rori! Was that Boku no Doki Doki Phantasm Gx; R-EVerSe?"
    
    show ava typical neutral
    show rori neutral at center:
        xpos 2000

    n "To your surprise, Ava is leaning over Rori, who is busy connecting the laptop to the television and has his anime folder open in clear view on the laptop screen."
    
    show claire:
        xpos -725
    show ava:
        xpos -375
    show rori neutral at center:
        xpos 150
    with move

    rori @ say "Yeah! Have you been keeping up with season 15?"
    
    show ava motivated

    ava @ say "I have! It looks like they're hyping up Golden Stardust to go Requiem Mode: Super Blue Évolution for the fight against Diamond Moonlight!"

    show claire sweater heyeah

    claire @ say "I can't wait to see her final Perfect Vampire form!"

    gunner @ say "I just hope they don't stray too far from the manga version."
    
    show ava angry

    ava @ say "Don't spoil it!"

    gunner @ say "I won't, I won't!"

    n "Apparently everyone is a weeb."
    n "Maybe tonight won't be a disaster after all."

    hide ava
    hide claire
    hide rori
    hide gunner
    with dissolve

    n "Once everybody gets situated and Rori picks out a film, you're faced with a predicament."
    n "A life altering decision presents itself."
    n "Who do you sit next to?"
    n "This room wasn't meant to accomodate five people so there's not a lot of places to sit."
    n "Everyone but you and Gunner has snagged a seat and he's distracted by his phone, so now's your chance." 

    ###maybe extend the scene after the credits roll and you're alone with whoever you sat with after the others leave
    menu:
        n "{cps=0}Everyone but you and Gunner has snagged a seat and he's distracted by his phone, so now's your chance.{/cps=0}"
        "Sit next to Claire":
            #finished
            $ clairePoints = clairePoints + 1
            n "Surprisingly, Claire has not occupied your bed and has instead opted recline against it whilst sitting on the floor, her arm elbow deep in a bag of chips."
            n "You decide to join her down there and grab a handful of chips when she takes her paw out."

            show claire sweater neutral at center with dissolve

            claire @ say "Sup."

            #player "Enjoying the snacks?"
            player "There's room on the bed you know."

            claire @ say "I didn't wanna get crumbs in your sheets."

            player "How thoughtful."

            hide claire with dissolve

            n "Gunner looks up from his phone as Rori hits the play button."

            show ava typical neutral at offscreenleft
            show gunner neutral at center with dissolve:
                xpos -300
                xzoom -1

            gunner @ say "Hmm, where to sit...?"

            show ava overjoyed at center with dissolve:
                xalign 0 
                xpos 300
                xzoom 1

            ava @ say "You can come sit next to me!"

            n "Ava pats the space beside her on the bed."
            n "Gunner climbs onto your bed, sitting next to Ava with their backs propped up against the wall."
            
            #show ava excited
            
            show gunner:
                xzoom -1
                
            pause .2

            show gunner neutral at center with move:
                xpos 470
                
            pause .1
            
            show gunner at flipleft
                #xzoom 1
                
            pause .3

            hide gunner
            hide ava
            with dissolve

            #show gunner neutral at center with dissolve:
            #    xpos -180
            #    xzoom -1

            #n "He quickly leans over and whispers something into your ear."

            #gunner @ say "Based. Thank you [name]."

            show claire sweater neutral alert at center with dissolve

            claire @ say "...and I figured those two would wanna sit together~"

            show claire -alert
            
            player "Aww."
            
            player "Well I don't mind sitting down here if it's next to you."
            player "Even if the hard bedframe is killing my back."
            
            show claire sweater lusty

            #claire @ say "Hehe I guess next time we'll just have to take the bed~"
            claire @ say "You can always lay on me you know~"

            player "...I wouldn't mind that either."

            show ava annoyed at center with dissolve:
                xpos 525

            ava @ say "Shh! The movie's starting!"

            hide ava
            hide claire
            with dissolve

            n "Claire wraps an arm around you and pulls you in close as the movie begins to play."
            #n "Your conversation will have to continue later, since the opening credits have rolled and the movie starts to play."
            n "You have to admit, it's a pretty good movie. The voicework is good, the animation's fluid, and the plot is interesting enough even if it doesn't make any sense whatsoever."
            n "Claire's constant munching was kind of distracting but it was kinda cute how she looked over to you and smiled when both of you reached into the chip bag at the same time."
            #n "At some point the discomfort from the bed frame digging into your spine was too much to ignore so you took up the bun's offer and decided to use her gut as a backrest."
            n "She's so soft and warm... You almost want to fall asleep like this."
            n "Oh god she's even stroking your hair"
            n "You're in heaven right now."
            n "Unfortunately the movie must end sometime and when it does, everyone gets up to stretch and banter a bit before heading home for the night."
            n "Claire however stays behind a little while longer and gives you a hug before leaving."
            n "Overall, you had a pretty good time with everyone. 10/10 would do again."
            n "*Yaaawn*"
            n "You're getting pretty sleepy though so you hurry and get ready for bed."

        "Sit next to Ava":
            #untested
            #gunner complains about there not being enough chairs and sits next to claire
            $ avaPoints = avaPoints + 1
            n "Ava had decided to occupy your bed, which is fine because it's the most comfortable spot and you wanted to sit next to her anyway."
            n "You plop down on it, bouncing her up into the air."
            
            show ava reaching concerned:
                ypos -3000
            
            n "She glides back down with her wings outstretched."

            #show ava typical neutral at center with move:
                #xzoom -1
            show ava with move:
                ypos 50
                
            #pause .01
            
            show ava with MoveTransition(delay=.05):
                ypos 0
                
            show ava at shudder

            ava @ say "Brreeee! Easy there, [name]!"

            player "Sorry, forgot birds have hollow bones."
            
            ava @ say "They're actually denser to account for that, so they're not any lighter than your mammal bones."
            ava @ say "I'm just small and dainty."
            ava @ say "A strong breeze is enough to knock me over haha."
            
            show claire sweater giggle:
                xzoom -1
                xpos -550
                
            claire @ say "Ksksksksks"
            claire @ say "[name] knocked you up so hard your shirt started taking itself off!~"
            
            ava @ say "?"
            
            show ava reaching embarassed
            
            ava @ say "Wha-!"
            
            n "Ava quicky buttons up her shirt."
            
            show ava unimpressed
            
            ava @ say "Just pretend that didn't happen."
            
            n "Gunner looks up from his phone."
            
            show gunner neutral at center with dissolve:
                xpos 475
            
            gunner @ say "Damn, what did I miss?"
                
            show ava pose concerned at flipright
            
            ava @ say "Nothing!"

            #player "I'll be more careful around you then lol"
            
            hide ava with dissolve

            gunner @ say "Hrm..."
            gunner @ say "[name], you got any more chairs around here?"

            show claire sweater neutral alert at center:
                xzoom -1
                xpos -550

            claire @ say "Come sit next to me!"

            n "Claire pats the space beside her on the floor."

            #pause .1

            show gunner at flipright
                
            pause .5
            
            show gunner at flipleft
            
            pause .5
            
            show gunner at flipright
                
            pause .2
            
            show gunner at flipleft
            
            pause .3
            
            show gunner at flipright
                
            pause .2
            
            show gunner at flipleft
            
            pause .1

            n "Gunner grimaces and looks around for any alternatives."
            
            show gunner neutral at center with move:
                xpos -200
                
            pause .01
            
            show gunner at flipright            
                
            n "Alas, with nowhere else to sit, he's forced to plop down next to her."
            
            show claire sweater lusty alert
            
            n "Claire wraps an arm around him and he disappears into her floof."
            
            show gunner with MoveTransition(delay=.4):
                xpos -310
            
            n "RIP"
            
            show rori neutral with dissolve:
                xpos 385
                
            rori @ say "Shshshsh! The movie's starting!"

            hide gunner
            hide claire
            hide rori
            hide ava
            with dissolve

            n "As the opening credits play, Ava scoots closer to you, her feathers brushing up against your skin."
            n "The movie goes on and it's better than you thought it would be."
            n "Detailed art, fluid animation, and an interesting plot that doesn't make any sense but it's still fun to watch."
            n "Before you realize it, Ava is full-on clinging to you."
            n "Not that you mind. She's really soft. No wonder they used to make pillow stuffing out of feathers."
            n "You can't resist wrapping an arm around her which only entices her to snuggle you closer."
            n "When the movie ends, everyone gets up to stretch and banter a bit before heading home for the night."
            n "Ava even stays behind a little while longer and gives you a hug before leaving."
            n "Overall, you had a pretty good time with everyone. 10/10 would do again."
            n "*Yaaawn*"
            n "You're getting pretty sleepy so you hurry and get ready for bed."

        "Sit next to Rori":
            #untested
            $ roriPoints = roriPoints + 1

            n "You approach Rori, who is sitting in your desk chair."

            show rori neutral at center with dissolve

            rori @ say "Oh, am I in your spot?"

            player "Yeah but it's no big deal."

            show rori anxious

            rori @ say "Wh-whoa what are you-"

            n "You simply lift Rori up and take your seat back before lowering him onto your lap."
            
            rori @ say "*Bleat!*"
            
            n "The others stare and laugh as Rori tries to cover his blushing face."
            
            show ava typical neutral at offscreenright

            show gunner neutral at center with dissolve:
                xpos 450

            n "Gunner nods to you."

            gunner @ say "Establishing dominance in your home. A real alpha move, [name]."

            show claire sweater neutral at center with dissolve:
                xzoom -1
                xpos -500

            show claire sweater derp
            
            claire @ say "Aww, I'm jealous you get to sit in [name]'s lap Rori!"

            rori @ say "Ohmygosh[name]whyareyoudoingthis\nthereareotherplacesyoucouldhavesat"

            player "Yeah but I wanted the best seat in the house~"

            n "That only makes him turn more red."

            rori @ say "Aaaaah why would you say it like that?!"

            player "What, isn't this just like one of your Japanese animes?"

            n "The room erupts into laughter, including Rori."
            n "He decides to accept it and leans back into you while Gunner goes to hit play on the movie."

            hide claire
            hide rori
            with dissolve

            gunner @ say "Alright, now where do I sit?"

            show ava typical neutral at center with dissolve:
                xzoom -1
                xpos -100

            ava @ say "Over here Gunner, there's some room for ya over here!"

            gunner @ say "Don't mind if I do!"

            n "The bird pats the spot on your bed beside her and Gunner pounces on it quite elegantly."

            show gunner neutral at center with move:
                xpos -270

            pause .1

            show gunner at flipright
            
            pause .1
            

            pause(.3)

            hide gunner
            hide rori
            hide ava
            with dissolve

            n "The movie starts and it's better than you thought it would be."
            n "Detailed art, fluid animation, and an interesting plot that doesn't make any sense but it's still fun to watch."
            n "Rori fidgets in your lap throughout the movie."
            n "Honestly you're kind of regretting this because he's cutting off blood flow to your legs but it's too late to back out now."
            n "At least he seems to be pretty comfortable."
            n "Whenever you would reach over to grab your drink on the table you would catch a glance of Ava leaning on Gunners shoulder."
            n "You have to admit, they do look pretty cute together."
            n "When the movie's over and everyone gets up to stretch, he's hesitant to leave your lap until you forcefully push him off."
            n "Your party sticks around to banter for a bit before going back home."
            n "Rori even stays behind a little while longer and gives you a hug before leaving."
            n "Overall, you had a pretty good time with everyone. 10/10 would do again."
            n "*Yaaawn*"
            n "You're getting pretty sleepy so you hurry and get ready for bed."

    stop music fadeout 1.5

    hide box

    scene bg black with fade

    hide box
    
    
    stop music fadeout 1.0

    hide box
    
    scene bg black with fade

    hide box

    show bg calendar
    show tsunday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    #___monday4
label ellen_feeding_ducks:
    scene bg codadorm with fade
    
    play music "audio/ambient/morning birds.ogg" fadein 0.1
    
    show box with Dissolve(.2):
        ypos 0
    
    n "The weekend sure left you pretty tired. Maybe social interaction isn't such a good idea after all."

    player "ACHOO!"

    n "...Especially when it leaves your room littered with enough fur and feathers to make you sneeze constantly."
    #n "It's too early to vacuum but you don't want to stay here either where it smells like a zoo."
    n "It's still too early to vacuum but at least you can wash your bed linens. You bunch them up and throw them in your laundry hamper."
    n "You'll get around to that later."
    n "Maybe."
    #n "Maybe it's for the best you don't have a roommate, lest you be allergic to them."
    n "*sniffle*"
    n "Gah, you really need to get out of this room for a bit. It smells like a zoo in here."
    
    scene bg campus with fade
    
    play music "audio/music/vylet - Tranquility and Happiness.ogg" 
    
    show box with Dissolve(.2):
        ypos 0
    
    n "Amid the myriad of fuzzy animals passing by on their way to class, you spot a glum looking doggo on a bench overlooking the pond they have in the middle of campus for some reason."
    n "Wild ducks and squirrels surround her, feeding on the bits of bread and seeds she scatters about."
    n "Upon closer inspection, it turns out to be Ms. Ellen!"
    n "Without thinking, you decide to sit next to her. All the animals scatter as you approach and Ms. Ellen raises her head."
    
    show margaret sad at center with dissolve
    
    ellen @ say "Hm? Oh it's you."
    
    player "Yup."
    
    n "An uncomfortable silence passes."
    
    menu:
        n "{cps=0}An uncomfortable silence passes.{/cps}"
        "What are you doing here?":
            #finished
            player "What are you doing here?"
            
            ellen @ say "I've gotta do something to pass the time, don't I?"
            
            player "I just thought you'd be more into reading books or something."
            
            ellen @ say "I've read enough books for one lifetime, I think."
            ellen @ say "The animals around here don't care to hear my interpretations of Virginia Wolf however."
            
            player "...Well what *are* your interpretations of Virginia Wolf?"
            
            ellen @ say "I'm not fond of her. Her streams of consciousness are a bore and her brand of feminism is too pompous for my tastes."
            ellen @ say "I won't blame you if you just read summaries online instead of reading her books when we go over her."
            
            if gaveCinRoll == True:
                #finished
                player "Wow, you're really lax on the whole teaching thing, aren't you?"
                
                ellen @ say "I didn't used to be. I used to try really hard."
                ellen @ say "But after teaching here... I've seen so many cheaters graduate. So many people dumber than a rock get by on their rich parents and end up in important jobs."
                ellen @ say "That's just the path in life they've had given to them."
                ellen @ say "The dean pressures us to just shut up and take the bribes. Not little things like cinnamon rolls, I'm talking cars and vacation homes."
                
                player "How many vacation homes does a professor need??"
                
                ellen @ say "I wish I had one. They only offer those to smooth things over when senator So-and-So's dipshit son gets in trouble with the law for assaulting some poor sorority girl."
                ellen @ say "The most I've ever got was a strange case where I think the student enjoyed giving me money?"
                ellen @ say "I suckered him out of nearly twenty grand over a couple semesters."
                
                player "You lucky dog."
                
                show margaret happy
                
                ellen @ say "Hehehehe~"
                
                show margaret neutral
                
                ellen @ say "You won't have to do that much to pass my class. Just listening to me rant is enough for me. It's a lot cheaper than therapy, that's for sure."
                
                n "Ms. Ellen sighs."
                
                show margaret sad
                
                ellen @ say "I like to think I make my own paths in life, for better or worse."
                ellen @ say "Though I can't help but feel I've been on a streak of bad decisions for quite a long time."
            
                player "Same, but... I think I'm making the most of it?"
                player "I always felt like I'm mindlessly drifting through life like a jellyfish in the sea but at least now I have friends."
                
                ellen @ say "Cherish them."
                
                player "Huh?"
                
                ellen @ say "You're only an undergraduate once. Things will change when you get older. Enjoy your life now while you can."
                
                player "I'll try."
            
            else:
                #untested
                player "Wow, a professor openly telling me to be academically dishonest?"
                
                show margaret happy
                
                ellen @ say "It's more likely than you think."
                
                player "And here I thought you hated me cause I poached your cinnamon roll."
                
                ellen @ say "Do it again and I'll fail you."
                
                show margaret melancholy
                
                ellen @ say "It's true though, I've long since lost the passion for teaching, if it ever existed in the first place. My knowledge of literature has never gotten anyone anywhere."
                
                show margaret sad 
                
                ellen @ say "Every English major I taught ended up killing themselves or wanting to."
                
                player "That's not really your fault."
                
                ellen @ say "I know. I still consider my job to be rather worthless though."
                
                player "Why not quit?"
                
                ellen @ say "And do what? I'm too old to find a new career I enjoy, and the pay is good here."
                
                player "Is money everything? I've never had much so I dunno if it's worth working for. And you're not that old."
                
                #ellen @ say "Interesting. I forgot who wrote it but some philosopher once said there's nothing more indignant than being poor. Er, no offense."
                #ellen @ say "I've never been rich, but I come from a well off family"
                
                ellen @ say "You get used to a certain amount and then you can never go back."
                
                show margaret neutral
                
                ellen @ say "And just how old do you think I am?"
                ###make this scene happen on ellen's birthday
                
                menu:
                    ellen "{cps=0}And just how old do you think I am?{/cps}"
                    "20s":
                        $ ellenPoints += 1
                        #later student ellen comments "you said so yourself, I could pass for being in my 20s!"
                        player "I dunno, late 20s?"
                        
                        n "Miss Ellen snickers."
                        
                        show margaret happy
                        
                        ellen @ say "Either you're flattering me or you don't know what a woman in her late 20s looks like."
                        
                        player "Hey, I'm pretty sure I've seen students who look older than you!"
                        
                        show margaret neutral
                        
                        ellen @ say "Those are graduate students, dear. It's not enough to get a Bachelor's degree these days, you need at least a Master's if you want a good job."
                        
                        show margaret melancholy
                        
                        ellen @ say "There's something comedically tragic to see one of my undergrads return after a couple of years to get another fancy piece of paper."
                        #ellen @ say "And this may come as a surprise, but not everybody starts college the moment they graduate from high school."
                        #ellen @ say "Or losers who joined the military at a late age 'for the benefits' when really it was because they could never get a job beyond stocking shelves."
                        
                        player "Aww, wouldn't you be glad to see me again?"
                        
                        show margaret happy
                        
                        ellen @ say "Not if you keep snatching my cinnamon rolls!"
                        
                        player "You're gonna hold that over me forever, aren't you?"
                        
                        show margaret neutral
                        
                        ellen @ say "Maybe!"
                        ellen @ say "Hehehehe!"
                        ellen @ say "What about you? Would you want to see me again?"
                        
                        player "Only if you're still as beautiful."
                        
                        show margaret intrigued
                        
                        ellen @ say "..."
                        
                        show margaret happy 
                        
                        ellen @ say "Oh psh! Hehehehe you're really quite a joker, aren't you?"
                        ellen @ say "Smart move. Only the fool can be spared the queen's wrath after all~"
                        
                        player "Hahaha really though, I think it would be cool to see you again after this semester. Maybe we could get coffee or something?"
                        
                        show margaret neutral
                        
                        ellen @ say "Careful [name], it almost sounds like you're flirting with your professor!~"
                        
                        player "I swear I'm not, I don't even know how to flirt."
                        
                        ellen @ say "So this is just you being your sweet normal self, huh?"
                        
                        player "I guess?"
                        
                        ellen @ say "Well it is pretty cute. Just don't expect me to boost your grade for it.... at least not by much~"
                    "30s":
                        player "Early 30s I guess?"
                        
                        show margaret melancholy
                        
                        ellen @ say "Try 41, dear."
                        ###37
                        ###hey, that's still prime
                        ###mathematically speaking at least
                        ellen @ say "Obviously you weren't paying attention when I mentioned how long I'd been teaching here."
                        
                        player "No way. I'm gonna need to see your ID, miss."
                        
                        show margaret happy
                        
                        ellen @ say "Hehehehe I can't remember the last time I got carded buying wine."
                        
                        show margaret tailwag flattered
                        
                        ellen @ say "I appreciate the compliment though~"
                        
                        n "You can hear her tail brushing against the back of the bench as it wags happily."
                        
                        player "It's the least I could do after snatching your cinnamon roll. You were right, they're to die for."
                        
                        show margaret neutral -tailwag
                        
                        ellen @ say "Or to kill for!"
                        
                        #show margaret experimental wip
                        
                        n "She playfully bares her teeth and growls."
                        
                        show margaret happy
                        
                        ellen @ say "Hehehe I'm just kidding. You're too cute to kill."
                        
                        player "Me? Cute? And here I thought I was ghastly and ragged."
                        
                        show margaret sad
                        
                        ellen @ say "Woops, did that really slip out of my mouth? I meant cute like uhh..."
                        
                        show margaret melancholy
                        
                        ellen @ say  "Like one of these baby ducks!"
                        
                        player "Thanks? I think?"
                        
                        show margaret neutral
                        
                        ellen @ say "Don't think too much about it."
                        
                        n "Ellen reclines against the bench and sighs."
                        
                        show margaret melancholy
                        
                        ellen @ say "It's nice to get to talk to one of my students like this."
                        ellen @ say "Most are either intimidated by me or just see me as an obstacle to their degree."
                        
                        player "Yeah I'm not really too into the whole college thing."
                        player "I just come to class out of habit and sometimes I learn interesting things."
                        player "I like hearing your rants about authors' beliefs."
                        
                        show margaret flattered
                        
                        ellen @ say "Oh really? I always feel so embarrassed after those little tirades! I suppose I just can't help myself."
                        
                        #player "Your personality comes through your teaching. I guess all teachers are like that but usually it comes across as 'wow this lady is a huge bitch.'"
                        player "I guess literature would lend itself most to expression. Not much room for interpretation in statistics or French."
                        
                        show margaret neutral
                        
                        ellen @ say "Au contraire, le langage limite nos pensées."
                        
                        player "What??"
                        
                        ellen @ say "There's certain things you can't express in one language alone."
                        ellen @ say "Even if you mastered English, which very few people have done, other languages open your mind up to new thoughts."
                        #ellen @ say "That's what Celestine taught me. You know her, right?"
                        ellen @ say "That's what Sera taught me. You might know her as Mrs. Celestine."
                        
                        player "Yeah, she's my French teacher."
                        
                        ellen @ say "I thought so. She's nice. And wise. You should listen to her."
                        ellen @ say "And she's your \'professor,\' not teacher. You're in college, hun."
                        
                        player "Well excuuuse me, I didn't realize there was a huge difference!"
                        
                        ellen @ say "A lot of people think professors are just here to read aloud from a textbook and take your money but we can be so much more than that!"
                        ellen @ say "We're here because we have an interest in gaining and imparting knowledge that helps you grow as a person."
                        ellen @ say "Literature has helped me understand myself better and I hope it can do the same to you!"
                        
                        #ellen @ say "We're supposed to be like mentors, setting expectations for how to behave like an adult."
                        #ellen @ say "A common teacher is little more than a glorified babysitter, but a true professor exists to guide students to a higher level of maturity."
                        #ellen @ say "A teacher is there to get you through mandatory schooling. Our job is to help you reach a higher level of critical thinking."
                        #ellen @ say "It's assumed you have a vested interest in learning and the opportunities that come with knowledge. You're here willingly after all~"
                        # it's funny. I've studied all this literature and I still don't have the words to express myself. Perhaps the words don't exist.
                        
                        player "This might be a dumb question but... how so?"
                        player "Are you just destined to fall into one interest, or do you choose it or what?"
                        
                        ellen @ say "How can I put it... Ah!"
                        ellen @ say "Think of the knowledge you've accumulated throughout your life like a pair of glasses."
                        ellen @ say "Your vision is still kinda blurry with these glasses but every time you learn something new things become a little more clear."
                        ellen @ say "Eventually you find the pair of glasses that are right for you."
                        ellen @ say "For me, reading stories and trying to understand the feelings behind the authors made my world view the clearest so I specialized in that!"
                        
                        show margaret happy
                        
                        ellen @ say "There's so much you can feel without having the words to express it. And if you don't have the words, you can get stuck not understanding what you're feeling!"
                        #ellen @ say "A professor is more dignified and deserves greater respect!"
                            #more like a mentor if you let them
                            #a teacher helps you grow into an adult, a professor helps you mature
                            #a teacher is a glorified babysitter, a professor sets expectations for how to act like an adult
                        #ellen @ say "You might wanna read that essay by George Orwell on how your thoughts are limited by your language."
                        
                        show margaret neutral
                        
                        ellen @ say "There's a fascinating essay by George Orwell you might consider reading on how your thoughts are limited by your language."
                        
                        player "Maybe I'll read it someday when I'm not studying four different subjects at once."
                        
                        show margaret happy
                        
                        ellen @ say "Perhaps I'll just have to assign it to you then~"
                    "40s":
                        player "You're not old until you're like, grandma age."
                        
                        show margaret sad
                        
                        n "Miss Ellen sighs."
                        
                        ellen @ say "I suppose I could be a grandmother at my age. If I had any children of my own, that is."
                        
                        show ellen at shudder
                        
                        ellen @ say "Sorry, I didn't mean to make things awkward."
                        
                        player "It's fine. I mean, isn't it awkward of me to walk up to my literature professor and while she's feeding ducks?"
                        
                        show margaret neutral
                        
                        ellen @ say "Not really! This is how people made friends before we had technology to enslave our minds after all."
                        
                        #player "I'm glad I'm not the only one who finds the internet to be an impressively lonely place. I always preferred to "
                        #player "I think it's also how serial killers got into their careers"
                        player "Hahaha do you think you and I could be friends if you weren't my professor?"
                        
                        ellen @ say "Of course!"
                        ellen @ say "I think we could be friends even with you as my student. People forget that such things were common a hundred years ago. It still happens in a lot of other countries!"
                        ellen @ say "A community can be composed of anyone who enjoys each other's company, regardless of status."
                        
                        show margaret melancholy
                        
                        ellen @ say "You're quite an interesting person and can make good conversation. That's really all I need."
                        
                        player "Wow, that's kinda sweet of you to say! I guess you kinda are like a kind old grandma hahah!"
                        
                        show margaret flattered
                        
                        ellen @ say "Well, let's not say that..."
                        
                        show margaret neutral
                        
                        ellen @ say "But don't be afraid to say hi whenever you see me~"
                        
                        player "Same goes to you! I'd love to sit and chat with you over a coffee sometime."
                        #If we cross paths at the coffee shop again, I'd love to sit and have a chat with you!"
                        #ellen "Deal!"
                        #ellen "If I see you at the cafe again, I certainly will!"
                        
                        ellen @ say "I'm sure that can be arranged~"
                
                
                #ellen "How else will I afford my precious cinnamon rolls?"
            
            
        "Everything okay?":
            player "Is everything okay? You look kinda sad."
            
            ellen @ say "Can't a lady feed the local wildlife without being judged?"
            
            n "The pond animals have started to make their way back and Ms. Ellen tosses them some bread crusts."
            
            ellen @ say "Honestly, I don't know why I even bother. What have ducks ever done for me?"
            
            menu:
                ellen "{cps=0}Honestly, I don't know why I even bother. What have ducks ever done for me?{/cps}"
                "They're a part of nature.":
                    player "They don't have to do anything, they're ducks."
                    player "They're a part of nature, so perhaps they're inherently, I don't know, beautiful or something?"
                    player "And we're technically a part of that nature so they're like our siblings. Little duck siblings."
                    
                    show margaret neutral
                    
                    n "You catch Ms. Ellen smirking."
                    
                    show margaret happy
                    
                    ellen @ say "Do yourself a favor and drop philosophy class."
                    
                    player "I'm not even taking philosophy!"
                    
                    show margaret neutral
                    
                    ellen @ say "In that case, consider trying it out next semester~"
                    ellen @ say "You might learn a thing or two hehehe."
                    
                    player "Maybe I'll major in it out of spite."
                    
                    ellen @ say "And end up being a teacher like me."
                    
                    player "That doesn't sound too bad."
                    
                    ellen @ say "Trust me, it is."
                    ellen @ say "Maybe some people are content to waste their lives away but it eats at me knowing I could have done something else."
                    
                    player "What else would you have done?"
                    
                    ellen @ say "Honestly, any other path would have been better for me."
                    
                    #player "Hey don't say that, you could have ended up being a stripper or something"
                    
                    #ellen @ say "Now at least that sounds exciting~"
                    #ellen @ say "Hehehe I'm just kidding~"
                    
                    show margaret sad
                    
                    ellen @ say "But now I'm old and stuck on this path."
                    
                    player "You're only what, like 30? You've got time."
                    
                    show margaret neutral
                    
                    ellen @ say "Try 41, dear."
                    
                    show margaret tailwag flattered
                    
                    ellen @ say "I appreciate the compliment though~"
                    
                    n "You can hear her tail brushing against the back of the bench as it wags happily."
                    
                    show margaret sad
                    
                    ellen @ say "Oh, if only I could go back in time, but with all the wisdom I've accumulated over the years..."
                    
                "Then don't bother?":
                    player "Then don't bother? I mean, you're the one who made the conscious decision to come sit out here with a bag of bread instead of playing on your phone like everyone else does."
                    
                    ellen @ say "I suppose it's out of habit."
                    ellen @ say "It's just something my hus-- ex husband and I did a lot."
                    
                    player "Oh."
                    player "..."
                    
                    show margaret neutral
                    
                    ellen "You wanna try?"
                    
                    n "She nudges the bread bag closer to you."
                    n "You grab a few slices and start tearing off pieces."
                    
                    player "Oh gross, there's mold on it."
                    
                    ellen @ say "Why do you think I've been giving it to the ducks for free?"
                    
                    player "Won't they get sick?"
                    
                    ellen @ say "They've never complained before."
                    
                    n "You toss a few pieces and the ducks come running with their wings outstretched."
                    n "One gives you an appreciative quack."
                    n "Meanwhile, Ms. Ellen takes a pawful of seeds and soon attracts a squirrel to perch on her arm."
                    
                    ellen @ say "They are rather cute, aren't they?"
                    
                    player "Yeah, like a scene out of Cinderella. Or was it Sleeping Beauty?"
                    
                    n "Ellen looks confused."
                    
                    ellen @ say "I think you mean Snow White, dear."
                    
                    player "I think all those classics had a scene where the main girl interacts with wild animals to show how pure and in tune with nature she is."
                    
                    ellen @ say "Did you see they're remaking those old films in live action now? Bambi's played by a pit bull in the new one."
                    #They're quick to point out how specist they were but they're quicker to make a buck off them."
                    #They made Alice in Wonderland a rabbit in the new one."
                    #ellen @ say "And now it's some kind of commentary on classism, brought to you by huge corporation."
                    #they turned the little mermaid into a - oh I'm not gonna say it
                    
                    #player "Yeah, I guess her black fur was supposed to contrast with the white rabbit now?"
                    player "Huh. I could see why they'd replace the human characters but isn't Bambi supposed to be a deer?"
                    
                    ellen @ say "I guess anybody can be Bambi these days."

    n "You sit with Ellen for a few more minutes, making idle talk and feeding ducks until you run out of bread."
    
    show margaret melancholy
            
    ellen @ say "Thanks for sitting and talking with me. It really made my day worthwhile."
    ellen @ say "There's more to you that makes you special than just being the last human."        

    player "I don't know about that. I'm just like anyone else. Just doing whatever society expects me to do. Go to school. Pay taxes. That sort of thing."
    
    ellen @ say "You're very kind and have your own unique perspective. You can uplift people without realizing it."
    
    player "I'm glad you think so. I try. Well no, I don't really try. I just want to live a comfortable life and be happy with others."

    show margaret neutral
    
    ellen @ say "Perhaps that's all you need to do."
    
    n "Miss Ellen stands up."
    

    
    ellen @ say "I have to go now. Again, thanks for talking with me. Take care, alright?"
    
    player "Yeah. You too."
    
    #hang out with ellen feeding squirrels, she wonders if this is the best thing she's done in her life providing sustenance for wild animals who otherwise might not survive, the squirrels at least seem to be grateful, , talks about autumn and some things she likes
    
label rose_book:
    scene bg classroom with fade
    play music "audio/music/mere - schooldaze.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0

    show rothbauer at center with dissolve

    rothbauer @ say "...and that's ultimately how the Shang dynasty shaped ancient China and how a humble panda prevented a full scale civil war."
    rothbauer @ say "Class dismissed! Have a nice rest of your day!"

    hide rothbauer with dissolve

    n "You shove your books into your bag and get up with the rest of the class to leave but Mr. Rothbauer stops you."

    show rothbauer at center with dissolve

    rothbauer @ say "Oh [name], do you have a moment?"
    rothbauer @ say "On Friday I mentioned a book that might help you and Rose with your project. It's quite rare and I'm pretty sure you won't find it in the library."
    rothbauer @ say "I managed to locate my copy back at home, but it seems Rose had other things to do today than come to class."
    rothbauer @ say "Would you mind sharing this with her? It gives some very good insight on the early civilizations in America before European settlers arrived."

    player "Sure, I'll give it a look and let Rose know about it."

    rothbauer @ say "Thanks! I'm looking forward to hearing your presentation the most!"

    hide rothbauer with dissolve

    n "So Rose decided your project is on ancient America, huh?"
    n "That's interesting. Being from the land of burgers, all your history classes have focused on America more than anything so you're familiar with the basic stuff."
    n "It was almost like a reversal of the rest of the world where anthromorphs were usually slaves or lower class."
    n "During ancient times in America, they lived more in harmony with humans."
    n "Then after the Americas were colonized, anthromorphs didn't really have equal rights until humans started dying off."
    n "Maybe nihil syndrome is like, karma for centuries of subjugation or something."
    n "Oops, no time to consider the philosophical side of your species going extinct, you have to get to statistics!"

    scene bg lecturehall with fade

    play music "audio/music/mere - schooldaze faster.ogg" fadein 1.5

    show herschel at center with dissolve

    show box with Dissolve(.2):
        ypos 0

    herschel @ say "Good afternoon class! I hope you're all prepared for today's quiz!"
    herschel @ say "Gunner, you told [name] which topics to study, right?"

    show gunner neutral at center with dissolve:
        xzoom -1
        xpos -400

    gunner @ say "Er, yes ma'am!"

    n "Gunner has his head buried in his notes, frantically cramming in last minute knowledge on theorems and principles as Mrs. Herschel passes out quizzes."

    herschel @ say "Good, now put away your notes. This is not an open book quiz. If you studied at all prior to today it should be fairly easy!"

    gunner @ say "*Gulp*"

    hide gunner with dissolve

    n "Mrs. Herschel places a piece of paper on yours and Gunner's desks."

    herschel @ say "You may begin as soon as you get your quiz."

    hide herschel with dissolve

    n "You pick up your pencil and begin working on problems."

    if studied == "stats":
        #untested
        #gunner will come to you for studying later, will help you later by giving +1 point to anyone you're interested in if you tell him
        n "Some of them are really similar to the ones from the homework."
        n "Overall it's not too hard, but Gunner seems to still be on the front side of the sheet by the time you've finished."
    else:
        #finished
        #Gunner feels better bc you thought it was hard, but doesn't come to you for studying
        n "You have absolutely no idea how to begin solving some of these."
        n "You can only remember what she taught when you were in class but that doesn't help when half the problems are from the homework you didn't do."
        n "You can only do your best and hope you pass."

    show herschel at center with dissolve

    herschel @ say "Time!"
    herschel @ say "Gunner, that means pencils down."

    hide herschel with dissolve

    n "Gunner lets out a frustrated sigh and slams his pencil down as Mrs. Herschel comes to collect everyone's papers."

    show gunner neutral at center with dissolve:
        xzoom -1
        xpos -400

    gunner @ say "Psst, [name], is it me or was that quiz stupid hard?"


    if studied == "stats":
        player "I didn't have too much trouble with it. Did you do the homework?"

        gunner @ say "Yeah but I didn't get the right answers on them."

        player "Well there's your problem..."
    else:
        player "Yeah I don't think I did too well..."

        gunner @ say "This is so unfair. Not everyone is a math major!"

    show herschel at center with dissolve

    herschel @ say "Is that everybody's? Very good, I'll have these back to you and graded next class. For now let's go over cumulative distribution functions!"

    n "Gunner puts a finger to the side of his head and gestures like he's blowing his brains out."
    n "Poor guy. He's trying his best."

    stop music fadeout 1.3

    scene bg campus with fade

    #play music "audio/ai21.ogg" fadein 1.0
    #play music "audio/music/Evan Schaeffer - Aqueduct.ogg" fadein .7
    play music "audio/ambient/outdoors people talking.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "After class you decide to stop by the cafe for some sweet delicious coffee and a sandwich for lunch."
    
    n "Back at your dorm, you get ready for bed, almost forgetting to take your stupid pill."
    n "As much as you hate taking these, they really do seem to work. You have a lot more energy now and you don't have random migraines throughout the day."
    n "Let's hope it stays that way."

    stop music fadeout 1.0
    hide box

    scene bg black with fade
    
    show bg calendar
    show tmonday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    #___tuesday4
label vacation_planning1:
    
    scene bg campus with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    play music "audio/music/vylet - Ordinarily.ogg" fadein .5
    
    show claire outdoors heyeah at center with dissolve:
        xpos 500
    show ava annoyed at offscreenleft:
        yalign 0
        
    claire @ say "...and I'm like \"nooo, you didn't!\" and then she's like \"but I diiiiid\" and so I'm like-"
    
    show ava annoyed at center with move:
        xpos 1500
        xzoom -1
        
    show claire outdoors surprised
    
    claire @ say "Oh hai Ava!"
        
    n "Ava's appearance has spared you from listening to the rest of Claire's wacky and definitely very interesting dream she had last night."
    
    show claire outdoors neutral
    
    player "Get any good shots lately?"
    
    ava @ say "No, because I had to cancel my plans for today!"
    ava @ say "My philosophy professor emailed me saying that I'd missed too many classes and he was threatening to fail me if I didn't show up."
    
    player "What, really?"
    
    show claire outdoors sad
    
    claire @ say "OMG no wayyy ;^;"
    
    ava @ say "Apparently it's Harmonia policy to automatically fail students who accumulate too many absences, regardless of their actual grades."
    
    claire @ say "That is so lame."
    
    show ava angry
    
    ava @ say "I know, right?!"
    ava @ say "So now I can't miss any more philosophy classes, even though I already went through it in high school!"
    
    show claire outdoors neutral
    
    player "In that case, why haven't I been expelled yet? I'm pretty sure I've missed more days than you."
    
    show ava unimpressed
    
    ava @ say "It's based on how frequently you're absent over a period of time. So missing a class here and there doesn't matter unless you start to be absent more often than not."
    #ava @ say "I think it's tracked on a per class basis? So you can miss x number of classes per subject."
    
    player "I guess that makes sense. And they're probably more lenient on me because I had a note from my doctor."
    
    ava @ say "Yeah, that'll do it."
    
    show claire outdoors lusty
    
    n "Claire gets a scheming look in her eyes."
    
    claire @ say "In that case, if you can't afford to skip philosophy, why not skip another class?"
    
    show ava overjoyed
    
    ava @ say "That's not a bad idea!"
    ava @ say "I can distribute my absences among all my classes so I always have free time to go shooting!"
    
    show claire outdoors heyeah
    
    claire @ say "Ksksksks I was thinking we could all take a vacation day together~"
    
    show ava typical neutral
    
    player "Like a half-weekend in the middle of the week? What would we even do?"
    
    stop music fadeout 1.0
    
    #this is about the point where we should jump forward in time. play the rest of this scene at a later point when the player remembers.

    #wednesday 4
label rori_belltower:

    scene bg campus with fade
    
    show box:
        ypos 0
    
    play music "audio/ambient/outdoors people talking.ogg" fadein .5
    
    n "Whoa, you totally spaced out... for an entire day according to the date on your phone."
    n "It's already afternoon. You don't even remember going to class today."
    n "Must be one of those 'grab your backpack and walk around campus aimlessly' days."
    #n "Any point in worrying about this is quickly dispelled when you spot what appears to be someone standing on the roof of the bell tower."
    n "What's that in the distance? Looks like someone standing at the edge of one of the rooftops on top of the guard rail."
    n "Are they... gonna jump?!"
    n "Why else would someone stand ominously on the edge of a tall building like that??"
    n "You squint your eyes against the harsh sunlight to see who it might be."
    
    player "Deer god..."
    
    #n "You sprint to the tower, hoping you'll make it in time."
    n "You sprint to the building, hoping you'll make it in time."
    
    stop music fadeout 1.0
    
    #scene bg campus with fade
    
    #show box
    
    #n "You arrive at the base of the tower but the entrance is sealed shut. You pull on the door handle in vain."
    
    #player "What the fuck, let me in!"
    
    #n "You're clearly not getting in this way. How did he get to the top?"
    #n "You take a step back and look along the outer wall of the tower. There are enough ledges and stones jutting out for you to maybe climb up."
    #n "With no other options, you begin your ascent. Brick by brick, you pull yourself up to a new ledge, taking only as much time as you need to catch your breath and reach for the next height."
    #n "Sweating and panting, you eventually make it to a platform about halfway up the tower. Your arms have just about given up on you."
    #n "You have to keep on going but..."
    
    #scene bg static1
    #pause .02
    #show bg static2
    #pause .02
    
    scene bg roof with fade
    
    show box:
        ypos 0
    
    n "After running up several flights of stairs, you're left panting and sweating. Thankfully you made it in time."
    
    player "Rori!!"
    
    #n "You open your eyes, feeling faint as if you just blacked out for a moment."
    #n "Standing over you is the one you were trying to reach, having descended to your elevation."
    
    show rori neutral at center
    
    play music "audio/music/vylet - yeah i'm ok thanks for asking.ogg"
    
    rori @ say "Sup dude."
    rori @ say "You alright?"
    
    player "What the hell are you doing? Get down from there!"
    
    #player "Rori?"
    #player "What are you doing up here?"
    
    n "Rori hops down from the guard rail and walks over to you."
    
    rori @ say "I was just chillin.'"
    rori @ say "I saw you running down there and waved."
    
    player "You looked like you were about to jump!"
    
    #player "Not planning on killing yourself?"
    
    show rori anxious
    
    rori @ say "W-what? No! Why would I do that?"
    
    player "Why else would you be up there like that?"
    
    #player "You were standing on the edge of a tall building alone!"
    
    show rori laugh
    
    #rori @ say "So? That doesn't mean I'm gonna jump!"
    
    rori @ say "I just like climbing stuff."
    
    show rori neutral
    
    rori @ say "It's relaxing."
    
    player "Scaring me half to death-"
    player "*wheeeeeze*"
    player "...is your idea of relaxing?"
    
    #player "You call this-"
    #player "*wheeeeeze*"
    #player "...relaxing?"
    
    rori @ say "Very!"
    
    show rori laugh
    
    rori @ say "Baaaaah~"
    
    show rori neutral:
        xzoom -1
    
    n "Rori turns toward the setting sun."
    
    rori @ say "The higher you go, the better the view."
    
    n "Rori climbs onto the guard rail once again and sits on top."
    
    #n "You try to sit up but something about being up high causes you to become dizzy."
    #n "Rori helps you upright and you both sit on the ledge looking outward at the twilight sun and surrounding campus and town."
    
    #rori @ say "It's even better at the top."
    
    player "I don't think I could manage to get up there."
    
    rori @ say "It's not hard. You just put your foot up and pull your body up with your arms."
    
    n "You hesitate before giving it a try. On your first attempt your foot slips and you narrowly avoid slamming your face into the brick wall."
    n "This wall isn't gonna get the best of you. Fueled by your anger, you jump up and grab the horizontal bar and pull yourself to the top."
    n "It's terrifying to sit up here but if Rori can do it so can you."
    
    show rori laugh
    
    rori @ say "Hey, you did it!"
    
    show rori neutral
    
    rori @ say "Wanna juice box?"
    
    #rori @ say "That's alright, we can chill here."
    
    #n "You just sit back and admire the view for a while in silence."
    #n "You don't really have anything to say, but is there anything that needs to be said?"
    #n "Can't it just be two bros hanging out precariously on the edge of a building in quiet recognition for each other?"
    #n "Your pondering is interrupted by the annoying sound of a juice box being slurped on loudly."
    n "You look over and see Rori sucking on the straw of a now empty carton of apple juice."
    
    #rori @ say "Hm?"
    #rori @ say "You want some?"
    
    n "He pulls another carton out from his hoodie pocket and hands it to you."
    
    player "Uh sure. Thanks."
    
    n "You jab the straw through it, nearly falling off your perch from the motion."
    n "You grip the bar you're sitting on with all your strength and take a sip of your juice."
    
    player "This feels like a dream."
    
    rori @ say "How so?"
    
    player "It's all so surreal. I never would have imagined I'd be here, like this."
    
    rori @ say "It's nice though, isn't it?"
    
    player "Yeah."
    
    rori @ say "..."
    
    hide rori with dissolve
    
    n "You enjoy the apple juice and sunset, unsure of what else to say but feeling like you understand Rori a little better."
    n "He's been staring off in the distance with a look of contemplation. He appears... oddly confident. Like he's in his element here."
    n "Like you, he spends way too much time glued to a screen, but he seems to accept reality for what it is."
    n "He just chooses to stay in his comfort zones, whether it's online chatrooms or lonely clock towers."
    n "He's a solitary creature but he's willing to share his lonesome spaces, which is maybe what everyone needs every now and then."
    n "Being lonely together isn't so bad, is it?"
    n "Or maybe you're just looking way too deep into it and Rori just likes climbing stuff because he's a ram."
    n "In any case, the sun is going down and you'd rather get down from here before it gets dark."
    #n "Rori helps you make your way down, as he effortlessly gets a foothold in the smallest of crevices and slightest of angles."
    #n "It's just as hard climbing down for you but he guides you to safety."
    
    show rori neutral at center with dissolve
    
    rori @ say "Thanks for sitting with me."
    rori @ say "I usually do it alone but it's nice to have someone to drink juice with and watch the sun set."
    
    player "Yeah, it did turn out to be relaxing, aside from whenever the wind was trying to push me off the edge."
    
    rori @ say "Yeah it does that lol"
    rori @ say "I have to get back home and work on some stuff."
    rori @ say "I'll see you around, k?"
    #player "Thanks. I really should have stretched beforehand, but y'know. Thought you were gonna kill yourself so I just jumped right in."
    
    #rori @ say "I get it lol. I'll see you later, k?"
    rori @ say "And if you see me on the tower again, feel free to say hi and climb up if you want."
    
    player "Sure thing."
    
    n "You and Rori give each other a nod of understanding and head back to ground level before parting ways back to your dorms."
    #n "If he's anything like you, he's gonna masturbate then go to bed."
    
    
    
    
    #add a choice
    
    #becomes a regular hangout spot for everyone, kinda like the clock tower scenes in kh2
    
    
    stop music fadeout .5

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show twednesday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7
    
    
    
    
    

    #hide box
    
    #scene bg classroom with fade

    #show rothbauer at center with dissolve

    #scene bg campus with fade

    #show box

    #n "It was another rough day in statistics. Poor Gunner had to stay behind and try justifying his homework answers to Mrs. Herschel in hopes of getting a passing grade."
    #n "As you step into the courtyard you bump into your beloved bunny buddy and feathered friend."

    #show claire sweater neutral at center
    #show ava typical neutral at center:
    #    xzoom -1
    #with dissolve

    
    #___thursday4

    

    #___friday4

    #___saturday5
label hiking:
    
    scene bg codadorm with fade
    
    play music "audio/music/vylet - Destiny Station.ogg" 
    
    call phone_start from _call_phone_start_32 

    call message_start("Ava", "Hiya [name]! You busy today?", "avaavi.png") from _call_message_start_64 

    call reply_message("Not really, why what's up?") from _call_reply_message_258 

    call message("Ava", "I was just wondering if you'd wanna come hiking in the mountains with Gunner and me ^v^", "avaavi.png") from _call_message_355 

    call reply_message("Like today?") from _call_reply_message_259 

    call message("Ava", "Yeah!", "avaavi.png") from _call_message_356 

    call reply_message("Kinda short notice don't you think? Is there even enough daylight left in the day for that?") from _call_reply_message_260 

    call message("Ava", "It'll be fine! Sunset is one of the best times to take photos anyway!", "avaavi.png") from _call_message_357 
    
    call phone_end from _call_phone_end_56 
    
    show box with Dissolve(.2):
        ypos 0
    
    n "As you're considering Ava's offer, Gunner sends you a text."
    
    call phone_start from _call_phone_start_33 
    
    call message_start("Gunner", "Dude say no to Ava", "gunneravi.png") from _call_message_start_65 

    call reply_message("What? Why?") from _call_reply_message_261 

    call message("Gunner", "Cause I wanna hang out with her alone", "gunneravi.png") from _call_message_358
    call message("Gunner", "Get to know her and stuff yknow", "gunneravi.png") from _call_message_359
    
    call reply_message("Hmm") from _call_reply_message_262
    
    call message("Gunner", "I'll give you 100$ if you do this for me", "gunneravi.png") from _call_message_360
    
    call screen phone_reply("Accept Gunner's offer","gunneraccept","Decline Gunner's offer","gunnerdecline")
    #,"Offer to be Gunner's wingman","gunnerwingman")
    
    label gunneraccept:
        #finished
        $ avaPoints =- 1
        call phone_after_menu from _call_phone_after_menu_16
        
        call message_start("me", "K", "testimage.png") from _call_message_start_66 
        call reply_message("I'll send you my paypossum account") from _call_reply_message_263 

        call message("Gunner", "Thanks man you're a lifesaver!", "gunneravi.png") from _call_message_361 
        
        call reply_message("Lol np") from _call_reply_message_264 
        call reply_message("Have fun with Ava") from _call_reply_message_265 
        
        call message("Gunner", "That's the plan!", "gunneravi.png") from _call_message_362 
        
        call message("Ava", "Well? We're about to head out soon.", "avaavi.png") from _call_message_363
        
        call reply_message("Oh sorry I just remembered I have something else I was gonna do today") from _call_reply_message_266
        
        call message("Ava", "Aww oki then", "avaavi.png") from _call_message_364
        
        call reply_message("Hope you have fun with Gunner tho!") from _call_reply_message_267
        
        call phone_end from _call_phone_end_57
        
        n "Hopefully Gunner can play his cards right and catch that bird."
        #n "You're feeling pretty bored of writing though. You kind of regret not going with them on their little adventure."
        
        call phone_start from _call_phone_start_51 

        call message_start("Rori", "Hey [name], you doing anything tonight?", "roriavi.png") from _call_message_start_67 

        call reply_message("Not a thing") from _call_reply_message_268 

        call message("Rori", "Would you like to come along with me and Claire? She's dragging me out into the woods to teach me outdoorsy stuff", "roriavi.png") from _call_message_365 
        
        call reply_message("That doesn't sound like a thing you would enjoy") from _call_reply_message_269
        
        call message("Rori", "It's not! But she talked me into it and now I'm all nervous and I'm gonna hate this and I get shy around bunnies and", "roriavi.png") from _call_message_366 
        
        call reply_message("Say no more, I'm on my way") from _call_reply_message_270
        
        call message("Rori", "Thx so much ^w^", "roriavi.png") from _call_message_367 
        
        call phone_end from _call_phone_end_58
        
        n "Sounds similar to what Ava wanted to do but this way you're helping two friends in need."
        n "You grab your jacket and prepare to head out."
        
        scene bg waterfall with fade
        
        play music "audio/music/Evan Schaeffer - Whigg Meadow.ogg" fadein 0.1
        #play music "audio/music/vylet - Oak Library.ogg" fadein 1.0
        
        
        show claire outdoors neutral at center:
            xpos -500
            xzoom -1
        show rori neutral at center:
            xpos 500
        with dissolve
        
        show box with Dissolve(.2):
            ypos 0
        
        claire @ say "...and that one that just flew by is a house sparrow! They originated from Europe and are kind of an invasive species but their population has been on the decline for the past fifty years."
        
        n "Claire had decided to take Rori deep into the woods to teach him about the outdoors and you got caught up in it."
        n "She's been banging out facts about random plants and animals the whole way."
        n "She's also been grabbing dry grass and small twigs and putting them in her pocket."
        
        rori @ say "Can we take a break? My hooves hurt from all this walking."
        
        player "Yeah and it's getting dark. Shouldn't we turn back?"
        
        claire @ say "Hmm... Alright, fine. But first I wanna show you something!"
        
        n "You and Rori sit down on a nearby fallen log while the bunny drags her boot over the ground repeatedly, kicking away leaves and debris until there's nothing but dirt."
        
        claire @ say "Have either of you made a fire before?"
        
        n "You and Rori shake your heads."
        
        show claire outdoors heyeah
        
        claire @ say "Well y'all're about to learn!"
        
        show claire outdoors neutral
        
        claire @ say "I like to start by doing this so the surrounding leaves won't catch on fire and potentially spread beyond a little area."
        #claire @ say "Also if the ground is damp you can sometimes get a dry patch of ground to work with."
        #claire @ say "Alternatively you can make a bed of sticks or logs to start your fire on top of!"
        
        n "You look over to Rori who oddly seems to be paying close attention to everything Claire is saying."
        
        claire @ say "We'll need to find some dry, dead wood to burn. If it's just lying on the ground it'll probably be damp or soaked, so try and find stuff that's propped up on top of something."
        
        n "Claire gestures for you to follow her off the trail and into the thicket."
        
        show claire outdoors surprised
        
        claire @ say "Ah here we go! A nice cedar branch! The oils in this will burn easily!"
        
        show claire outdoors neutral
        
        n "You and Rori look around for suitable branches."
        n "The ram grabs a random stick hanging off a tree."
        
        rori @ say "What about this one?"
        
        claire @ say "Not so ideal. You can see it still has green leaves on it so it probably was alive recently and just fell off the tree."
        claire @ say "Try breaking it in half."
        
        n "Rori stuggles to bend it but it keeps bouncing back to its original shape."
        n "He hands it to you but you can't get it to break even when using your knee."
        
        claire @ say "A pretty good indicator of how well it will burn is how easy it is to break."
        claire @ say "Old dry sticks break easy but greener stuff is full of water and is kinda elastic like that one."
        
        n "Claire helps you find suitable sticks until you've got a nicely sized bundle, which you deposit at the fire pit she dug."
        
        claire @ say "Great! We've got a good mix of branches and sticks of various sizes! Now comes the hard part!"
        
        n "Rori sighs, winded from collecting all that wood."
        
        rori @ say "You mean that was the *easy* part?"
        
        claire @ say "Yup! By far the hardest part is starting a fire and keeping it alive!"
        claire @ say "That's why I've been collecting this along the way!"
        
        n "She sticks her paws into her pockets and pulls out the stuff she'd been gathering."
        
        claire @ say "When you start a fire you have to build your way up from the easiest to burn stuff to the hardest."
        claire @ say "Dead brown grasses are common everywhere all year round and make great kindling!"
        
        n "You pick up a branch with a thick bundle of brown pine needles on the end."
        
        player "What about this? Will this work?"
        
        claire @ say "Nope! Leaves, including pine needles, don't make for great fire starters. They just don't burn easily or long enough."
        claire @ say "Try that thing right next to you though!"
        
        n "She points to a tall shoot sprouting from the ground. It's brown and has some kind of soft cotton-y seeds on the end."
        
        claire @ say "Cattail seeds will ignite if you just look at them wrong! Great mix of fiberous material but also being airy for the fire to breathe."
        
        n "Rori picks a similarly fluffy plant and begins to chew on it."
        
        show claire outdoors surprised
        
        claire @ say "Hey! Don't eat our tinder!"
        
        show rori anxious
        
        rori @ say "Sorry! I'm just hungry from all this walking!"
        
        show claire outdoors neutral
        
        claire @ say "Would you rather be hungry or cold?"
        
        rori @ say "...Hungry I guess."
        
        show rori neutral
        
        claire @ say "Having enough material to start the fire is crucial!"
        claire @ say "You always need at least twice as much tinder and kindling as you think you need so go ahead and look for more dry straw-like stuff and the smallest twigs you can find."
        
        n "As tiring as this is, you have to admit it's kinda fun. This sort of thing is in your blood after all."
        n "Your caveman instincts call to you to build fire and make sharp stick to kill mammoths and to reject the enslavement of the modern world."
        n "Rori seems to be getting into it too. Maybe because of all that time behind a computer screen, this stuff seems novel and interesting to the both of you."
        n "You both return to Claire with big handfuls of grass, seeds, reeds and sticks."
        
        claire @ say "Perfect! Let's just arrange these sticks by size here..." 
        
        n "Rori quickly sorts the sticks in neat bundles from smallest to largest."
        
        claire @ say "And now we just grab our grass, mix in a few of our tiniest twigs and shape it into a bird's nest like so."
        
        n "The bunny bends the material into a tight circle."
        
        claire @ say "And now we're ready to go!"
        claire @ say "Rori, would you do the honors? I got a lighter in one of my pockets."
        
        show rori anxious
        
        n "Rori blushes like mad as he digs around Claire's pockets trying to find her lighter while she holds the bird's nest."
        n "You're not sure if you should be jealous."
        
        show rori neutral
        
        rori @ say "Found it! Finally..."
        
        claire @ say "Nice! Go ahead and hold it under the nest and light it up!"
        
        n "The fluffy bundle catches flame within a few seconds. Claire holds onto it, tilting it so the rising flames encompass the whole thing before setting it down on top of some sticks."
        
        claire @ say "And now we just gradually stack sticks on top!"
        claire @ say "Do the smallest ones first and only go up in size once the previous ones catch on fire."
        
        n "Claire fans the flame with her paw while you pile sticks onto it."
        n "The tinder burns quickly, and after a few seconds it turns to ash, leaving mostly only embers left."
        
        player "Damn, it went out so fast..."
        
        rori @ say "Yeah, I thought we had a good little flame going on there."
        
        claire @ say "Not to worry! Check this out~"
        
        show claire outdoors horny
        
        n "Claire gets on all fours and sticks her face close to the smoldering remains. She takes a deep breath and blows on it, making it glow red hot in the dwindling sunlight."
        n "...Does she have to make that face?"
        n "A few more breaths and the remaining kindling reignites."
        
        show claire outdoors neutral
        
        claire @ say "You kinda have to baby the fire until it can sustain itself."
        claire @ say "Now that the smaller twigs are hot they should light up when the kindling flames surround them."
        
        n "You and Rori watch in awe as what she said comes true. She starts to arrange slightly larger sticks around the little flame and in time those burn too."
        n "Soon enough you have a fire reaching up almost as tall as you are just from gradually piling on more sticks, being careful not to smother the flame."
        
        claire @ say "See? It's not so hard!"
        
        rori @ say "Yeah, that was actually pretty cool! I wanna build more fires now!"
        
        n "Claire roughly pulls the ram into a side hug."
        
        show claire with move:
            xpos 310
            
        pause .1
        
        show claire:
            xzoom 1
        
        rori @ say "Ack!"
        
        claire @ say "That's the spirit! You two can come camping with me and we'll make all the fires we want ksksksks!"
        
        n "Thankfully you managed not to be victim to Claire's bone breaking grasp."
        n "But the thought of camping with your friends does sound nice. Could invite Gunner and Ava, maybe even Mishka."
        n "The three of you continue to feed the fire while sitting and telling stories. Claire even brought snacks."
        
        stop music fadeout 1.3
        
        n "Suddenly you hear a rustling in the woods."
        
        show claire outdoors surprised
        
        n "Both Claire's and Rori's ears perk up but in the darkness you can't see a thing."
        n "The sound of frantic footsteps crunching leaves and snapping twigs gets closer until two familiar faces show up in the light of the fire."
        
        
        show ava unsure at center:
            xpos -350
            xzoom -1
        show gunner neutral at center:
            xpos -600
            xzoom -1
        with dissolve
        
        ava @ say "Aaaah! Claire?! What are you doing here??"
        
        claire @ say "I could ask you the same thing!"
        
        show claire outdoors neutral
        
        gunner @ say "Heyyy Rori and [name]! The gang's all here!"
        
        rori @ say "Why were you two running through the woods?"
        
        gunner @ say "We're being hunted by a skinwalker, man!"
        
        n "Rori rolls his eyes and sighs."
        
        rori @ say "Ava, what's the real reason?"
        
        show ava seriously
        
        ava @ say "Well I don't think it was a skinwalker but maybe more like a wendigo or something."
        
        show claire outdoors heyeah
        
        claire @ say "They probably got caught having sex in the woods by a creepy old redneck ksksksksksk!"
        
        show ava pose angry
        
        ava @ say "Uh, no!"
        
        show ava pose concerned
        show claire outdoors surprised
        
        ava @ say "Look, I even have proof! I took a photo of the creature!"
        
        n "Ava holds up her camera and switches it on."
        n "Everyone gathers around her as it boots up and she navigates to the photo library."
        n "The shots are dark and you can make out what appears to be fresh blood on the trees but other than that there's no creature to be seen."
        
        show ava concerned -pose
        show claire outdoors neutral
        
        ava @ say "What? But I know it was there! Gunner you saw it too!"
        
        gunner @ say "Yeah, it was right there with its back to us right next to that tree right there!"
        
        show rori anxious
        
        rori @ say "I mean, it was probably a mountain lion or something and you just missed it? Still pretty spooky."
        
        show rori neutral
        show ava annoyed
        
        ava @ say "No, I know I had it in frame, I could see it through the viewfinder when I took the shots!"
        
        show ava concerned
        
        ava @ say "Unless..."
        
        n "Ava switches off her camera."
        
        show ava typical neutral
        
        ava @ say "Of course! Anything supernatural can't be recorded digitally."
        ava @ say "I knew I should have brought my film camera today..."
        ava @ say "I'll get a shot of it next time."
        
        gunner @ say "Next time? I'm not coming back here again, that's for sure! That thing was totally gonna eat us! I could see it in its eyes!"
        
        show ava annoyed
        
        ava @ say "Well not everyone is a scaredy cat!"
        
        gunner @ say "Yeah, and not everyone has wings to get away!"
        
        player "Whatever it was, we should be safe here. Wild animals fear the fire."
        
        n "Claire throws another couple of sticks onto the flames."
        
        show ava typical neutral
        
        claire @ say "Might as well get cozy if we're gonna stay here a while!"
        
        rori @ say "We're not gonna stay here all night are we? I still have homework to finish."
        
        claire @ say "Just until these two calm down."
        claire @ say "Until then, you are all cordially invited to join the cuddle puddle!"
        
        player "The what"
        
        #play sound "ambient/outdoors night crickets.ogg" fadein 1.0
        #play music "audio/music/vylet pony - Reading at Night.ogg" fadein 1.5
        play music "audio/music/vylet - Over Equestria.ogg" fadein 1.0
        
        n "You are soon encompassed by soft bunny fluff, followed shortly by coarse ram fur."
        
        player "Oof!"
        
        if heshe == "he":
            gunner @ say "Sorry bro, didn't mean to step on your balls."
        else:
            gunner @ say "Sorry, didn't mean to step on your tits."
            
        player "It's k."
        
        n "Typical cat behavior, stepping all over you."
        n "At least Ava doesn't weigh much as she crawls over you to snuggle with Gunner."
        
        ava @ say "'Scuse me!"
        
        claire @ say "Everyone comfy?"
        
        rori @ say "Yup! I can't remember the last time I was a part of something like this."
        
        n "You settle in to the warm fur and feathers surrounding you, which is admittedly probably the comfiest feeling you've ever experienced."
        
        player "Claire, you are the softest mattress I've ever laid on."
        
        claire @ say "Thanks!"
        
        show claire outdoors surprised
        
        claire @ say "Hey! Ava, no making out in the cuddle puddle unless you brought smooches for everyone!"
        
        show ava unimpressed
        
        ava @ say "Oh my gosh Claire I'm nottt!"
        
        gunner @ say "Not yet~"
        
        show ava embarassed
        
        ava @ say "SHush!"
        
        n "Gunner pulls Ava closer and tickles her. At least that's what you think is happening. It's hard to tell from where you are."
        
        show ava flattered
        
        ava @ say "Hehehehe ahhh stoppit!!"
        
        rori @ say "Get a room you two!"
        
        show ava typical neutral
        show claire outdoors neutral
        
        gunner @ say "Says the guy with his head resting on the biggest tits in Harmonia."
        
        rori @ say "Wha? I'm not..!"
        
        show claire outdoors embarassed
        
        claire @ say "You're on my boobs, dude."
        
        rori @ say "Oh heck I'm so sorry!"
        
        show claire outdoors derp
        
        claire @ say "Nah, go ahead and motorboat 'em, I don't care."
        
        show ava waitwhat
        
        ava @ say "Claire!"
        
        claire @ say "What?"
        
        show ava annoyed
        
        ava @ say "Did *you* bring enough for the class?"
        
        show claire outdoors lusty
        
        claire @ say "It was an open invitation."
        
        gunner @ say "Snrk!"
        
        show ava angry
        
        ava @ say "Why are you so lewd!"
        
        show claire outdoors derp
        
        claire @ say "Cause I wanna know who has a crush on me!"
        
        show ava unimpressed
        
        ava @ say "And you do that by acting like a slut?"
        ava @ say "You're probably just making someone who does like you jealous!"
        
        claire @ say "You're one to talk!"
        
        ava @ say "W-what?!"
        
        gunner @ say "She's bluffing! She knows there's no way Rori would try anything."
        
        #show ava typical neutral
        
        claire @ say "You never know! Somebody might take up the offer!"
        
        show claire outdoors lusty
        
        n "Claire suddenly glares in your direction."
        
        claire @ say "Isn't that right, [name]?"
        
        menu:
            claire "{cps=0}Isn't that right, [name]?{/cps}"
            "Let Rori keep his pillow":
                #finished
                $ clairePoints -= 1
                n "You turn away from that dreadful stare. It frightens you."
                
                player "Th-that's alright, Rori can keep his uh 'pillows.'"
                
                claire @ say "Suit yourself! Not everyone can handle such great tits~"
                
                n "The bunny pulls Rori in closer. You can hear his bones cracking and the air leaving his lungs."
                n "Poor guy. It was nice knowing him."
                n "Amidst the endless bickering and sexual innuendos, you nestle in and close your eyes."
                n "You're cozy, next to a fire, with your friends... what more could you want?"
                n "This is good, isn't it?"
                
                
                #ava @ say "Oh my gosh Claire, can you leave the poor ram alone for 5 seconds?"
                
                #claire @ say "Suit yourself! I better not catch you trying to motorboat ava's tiny tits though!"
                #horny ramblings of a madman
                #mad ramblings of a hornyman
                #claire "Oh? Perhaps you'd prefer to rest your head on Ava's birdy butt then~"
                #ava "Aww, now you're left out! I'll let you rest your head on my ass if you want!"
            "Move aside, Rori":
                #finished
                player "Move aside Rori, you're hogging the pillows!"
                
                show rori with move:
                    xpos 600
                    
                n "You switch places with Rori and get comfy with your head in between Claire's breasts."
                
                claire @ say "See? It worked!!"
                
                show ava angry
                
                ava @ say "This proves nothing! Seduction has nothing to do with romance!"
                
                claire @ say "Sorry Ava, [name] can't hear you with their ears covered by my massive titties~"
                    
                player "I fall asleep face down and end my turn."
                #btw i sleep face down
                
                n "You roll over and close your eyes, ignoring the brewing storm around you."
                n "Ava is seething but she's not entirely wrong. Bunny boobs are nice regardless of whether or not you'd go out with Claire."
                n "But now that you're thinking of it, is Claire actually interested in you??"
                n "That would explain why she's always been flirty with you... But doesn't she do that with everyone?"
                n "Or does she try extra hard with you?"
                n "The more you think about it, the further you drift into slumber..."
            #alternatively you static out and pass out
        
        #claire @ say "Maybe you should try it sometime?"
        
        #claire @ say "Sorry I have correct opinions and great tits~"
        
        #claire @ say "Um it's called having fun? Maybe try it sometime?"
        
        #ava @ say "Hmph!"
        
        #n "Even in the cuddle puddle those two can't help but argue."
        
        
        
        #ava @ say "..."
        #ava @ say "Well to whom it may concern, my ass has a special one time offer! One free spank for anyone who's interested!"        
        
        #rori @ say "OWO"
        
        #claire @ say "See? That's what I'm talkin' about!"
        #claire @ say "Now that's more like it!"
        #that's the spirit!
        
        #n "You may never get a chance like this again. Should you go for it?"
        
        #menu:
        #    "Just one couldn't hurt, right?":
        #        n "Your hand winds up and comes down with the force of a thousand virgins."
                
        #        show ava overjoyed
                
        #        ava @ say "SQUAWK!"
                
        #        n "Two slaps echo through the forest in quick succession."
        #        n "You look Gunner in the eye, both of your hands on Ava's cheeks."
        #        n "The genie has been let out of the bottle now. War has officially been declared."
                
         #   "Nope, too risky":
         #       n "You can't. Raptor Jesus can judge you all he wants but you don't want to piss off the bird gods too."
         #       n "Gunner however has no such inhibitions and winds up for a smack that's sure to feel like slapping the a pillow from a 5 star hotel."
         #       n "To everyone's shock, not just one but two soft slaps ring out, echoing through the forest."
         #       n "You look down and see both Gunner and Rori's hands on Ava's ass."
                
         #       gunner @ say "You son of a bitch, I'll kill you!"
                
         #       n "Just as Gunner pounces, claws ready to tear out Rori's neck, you feel the familiar sensation of being abruptly pulled out of a dream."
                
        ###fade to white, fade back in 
        scene bg black with fade
        
        pause .7
        
        scene bg waterfall with fade
        
        show box with Dissolve(.2):
            ypos 0

        show claire outdoors neutral:
            xpos 310        
        show rori neutral:
            xpos 600
        show ava typical neutral at center:
            xpos -350
            xzoom -1
        show gunner neutral at center:
            xpos -600
            xzoom -1
        with dissolve
        
        claire @ say "[name]! Time to wake up, sleepyhead!"
        
        n "You blink a few times, trying to recall where you are."
        #n "You're surrounded by warmth and floof and everyone is staring at you."
        n "That's right, you were forcefully indoctrinated into the cuddle cult and then you fell asleep."
        
        claire @ say "Did you have a nice nap?"
        
        player "Mhm~"
        
        show ava excited
        
        ava @ say "Nothing like a nice cuddle to bring one's spirits up~"
        
        show ava typical neutral
        
        rori @ say "Yeah, this was quite a novel experience!"
        
        gunner @ say "Hopefully whatever was chasing us has gotten bored and fucked off by now."
        
        #claire @ say "Ksksksks you sure fall asleep quick! Did you know you talk in your sleep?"
        
        #player "Wha? What did I say??"
        
        #ava @ say "Something about my ass???"
        
        #n "Gunner busts out laughing."
        
        #gunner @ say "Pffftahahahahahaa! You're a hoot and a half, you know that [name]?"
        
        #ava @ say "Hmph!"
        
        #claire @ say "Aww don't be mad, Ava. You should be honored [name] has dreams about your feathery butt!"
        
        #n "Ava tries to maintain her composure but even she starts to crack up."
        
        #ava @ say "Kshh, okay maybe it was a little funny hehehe~"
        
        #n "Claire pulls everyone together for a tight hug."
        
        #claire @ say "I'm so glad I met you all <3"
        
        #rori @ say "*wheeze* I'm... glad... too..."
        
        #claire @ say "You all ready to go back into town?"
        
        show ava pose ohyou
        
        ava @ say "Hah, yeah... I already forgot we were being hunted by a mythological creature."
        
        claire @ say "I'd say it's about time we get out of here."
        
        show ava typical neutral
        
        gunner @ say "We should be fine with the five of us travelling together."
        gunner @ say "Just have to make sure nobody gets picked off and skinwalkered."
        
        player "If it's a skinwalker versus Claire, my money's on the 300 pound 7 foot tall bunny."
        
        gunner @ say "For sure. Lanky cryptids BTFO."
        
        show claire outdoors embarassed
        
        claire @ say "350 pounds but who's keeping track am I right?"
        
        rori @ say "We're like a Dragons and Dungeons party transported into the real world."
        
        show claire outdoors derp
        
        claire @ say "Hah! Tonight has been way more fun than any LARP club I've been to!"
        
        rori @ say "Now I wanna write a campaign based on this trip. I think I'll call it Cryptids and Crypts."
        
        show claire outdoors surprised
        
        claire @ say "I'd play it!"
        
        n "Your party stamps out the dying campfire and covers it with dirt in preparation for finally leaving the woods behind and returning to your comfy dorms."
        #n "Claire invites everyone to continue the cuddle puddle at her dorm next weekend"
        
        stop sound fadeout 1.0
        stop music fadeout 1.0
        
        jump aftercuddlepuddle
        
    label gunnerdecline:
        #untested
        call phone_after_menu from _call_phone_after_menu_17
        
        call message_start("me", "Nah", "testimage.png") from _call_message_start_68
        call reply_message("I wanna hang out with Ava too lmao") from _call_reply_message_271
        
        call message("Gunner", "WTF", "gunneravi.png") from _call_message_368
        call message("Gunner", "I thought we were bros", "gunneravi.png") from _call_message_369
        
        call reply_message("Ya we are but I don't think she's into you") from _call_reply_message_272 
        call reply_message("I think she's more into humans :/") from _call_reply_message_273
        
        call message("Gunner", "Oh fuck off", "gunneravi.png") from _call_message_370
        
        call reply_message("Dude chill") from _call_reply_message_274
        call reply_message("If she likes you she'd let you know") from _call_reply_message_275
        call reply_message("Til then, I'm gonna shoot my shot with her") from _call_reply_message_276
        
        call message("Gunner", "...", "gunneravi.png") from _call_message_371
        
        call message("Ava", "Well? We're about to head out soon.", "avaavi.png") from _call_message_372
        
        call reply_message("Hey yeah that sounds like a great time!") from _call_reply_message_277
        
        call message("Ava", "Great! We'll come get you right now!", "avaavi.png") from _call_message_373 

        call reply_message("k, see you in a bit") from _call_reply_message_278 

        call message("Ava", ":>", "avaavi.png") from _call_message_374 
        
        call phone_end from _call_phone_end_59
        
        scene bg waterfall with fade
        
        play music "audio/music/Evan Schaeffer - Whigg Meadow.ogg" fadein 0.1
        
        show box with Dissolve(.2):
            ypos 0
        
        show gunner neutral at center:
            xzoom -1
            xpos -400
        with dissolve
        
        player "Is she done yet? She said we'd be done before sundown."
        
        gunner @ say "Huh? What's the matter, you afraid of the dark or something?"
        
        player "I can't see anything!"
        
        gunner @ say "Oh right. Human eyes. Lmao."
        
        #ava swoops down animation
        
        n "You hear a rustling of leaves high above in the tree beside you. Shortly after, Ava swoops down and perches lightly on the ground."
        
        show ava portrait neutral at center with dissolve:
            xpos 300
        
        ava @ say "All done! I got some decent shots of the city lights from up there."
        
        player "Great. Can we go home now?"
        
        show ava typical neutral
        
        ava @ say "Sure thing! Wait a sec, has anyone seen my lens cap?"
        
        gunner @ say "I thought you had it on you when you flew up?"
        
        show ava concerned
        
        ava @ say "Uhh no? I thought I gave it to you?"
        
        player "I don't remember seeing a lens cap."
        
        stop music fadeout .5
        
        pause .2
        
        #play sound "audio/vyletcreatureaudio/vy_creature01_misc_06.opus"
        
        play sound "audio/sound effects/monster roar 1.wav"
        
        creature "RRRRRAAAWWWRRRRRR"
        
        pause 1
        
        gunner @ say "What the hell was that?!"
        
        player "Uhh mountain lion maybe? I've heard tales of strange noises coming from them."
        
        #play sound "audio/vyletcreatureaudio/vy_creature01_misc_07.opus"
        
        creature "RRREEEEEEEEEEEEEeeeeeeeeee..."
        
        pause 1
        
        gunner @ say "What about that?!"
        
        #replace with wind in trees sfx
        play music "audio/ambient/outdoors night crickets.ogg" fadein 1.5
        
        ava @ say "A chupacabra? Maybe some sort of sasquatch?"
        
        player "Sounded more like a skinwalker to me."
        
        show gunner at shudder
        
        n "Gunner shudders."
        
        gunner @ say "Don't even joke about that!"
        
        show ava overjoyed
        
        ava @ say "Wouldn't it be awesome if it was a spirit of the forest?"
        
        ###if player talked about ghosts during the old hospital thing, have them talk about it more here
        
        show ava typical neutral
        
        gunner @ say "Whatever it is, it sounds like it's pissed."
        gunner @ say "We should leave before we get mauled, eaten, seduced or any combination of those by whatever lurks these woods at night!"
        
        n "Gunner starts down the trail back to where you came from."
        
        show ava annoyed
        
        ava @ say "Wait, what about my lens cap?"
        
        gunner @ say "Forget about the 2 cents worth of plastic, I'll buy you a new one when we get back!"
        
        #play sound "audio/vyletcreatureaudio/vy_creature01_misc_17.ogg"
        
        creature "HHHHHHHHHssssssss"
        
        pause 1
        
        player "Ok what the fuck that is not a natural cry."
        
        ava @ say "It sounded more distant that time..."
        
        gunner @ say "Good! Now can we please get a move on?"
        
        n "Gunner grabs Ava's wing, dragging her down the slope with him."
        
        ava @ say "Hold up! There's still some light out!"
        
        gunner @ say "So?"
        
        ava @ say "So I wanna get a photo of this mysterious creature!"
        ava @ say "This could be a once in a lifetime opportunity!"
        
        gunner @ say "Are you out of your mind? It's just a mountian lion or something. There's probably a billion photos of them on the internet."
        gunner @ say "It's not worth sticking around for."
        gunner @ say "Not to mention people get mauled by them all the time!"
        
        ava @ say "Mmh..."
        ava @ say "Maybe it is just a regular wild animal but I feel like this is happening for a reason."
        ava @ say "I have to see for myself if this is a worthwhile shot or not. And if it's a little dangerous then so be it!"
        ava @ say "Nobody ever won an award taking photos in their back yard. This art is all about the adventure, bringing out the mystique of the world!"
        
        stop music fadeout 2.0
        
        play music "audio/music/vylet - dance of the macabre.ogg" fadein 1.0
        
        #play sound "audio/vyletcreatureaudio/vy_creature01_misc_12.opus"
        creature "CCCCCLLLLOOOOOSSSSSSEEEEERRRRRRR....."
        
        show gunner at hop
        
        pause .1
        
        show gunner at flipleft
        
        pause .3
        
        show gunner at flipright
        
        pause .3
        
        show gunner at shudder
        
        n "Gunner jumps, startled by the noise."
        
        gunner @ say "Did you just hear that?"
        
        ava @ say "It sounded like it was telling us to come closer."
        
        player "Generally a bad idea, based on every horror movie ever."
        
        gunner @ say "That's it, I'm out."
        
        hide gunner with dissolve
        
        ava @ say "Jeez, what a pussy."
        ava @ say "Come on [name], you'll come with me right?"

        menu:
            ava "{cps=0}Come on [name], you'll come with me right?{/cps}"
            "Sure, I ain't afraid of no ghosts.":
                $ avaPoints += 1
                player  "Sure, I ain't afraid of no ghosts."
                
                show ava overjoyed
                
                ava @ say "I knew I could count on you~"
                
                show ava typical neutral
                
                ava @ say "Come on, the sound was coming from that direction."
                
                n "You and Ava quickly make your way through the woods. She holds onto your hand, guiding you through the darkness."
                n "The further you go, the more you start to regret your decision."
                n "Your caveman instincts are telling you that whatever is out there has a clear advantage over you and could kill you without a second thought."
                
                ava @ say "Wait! There!"
                
                n "Ava stops behind a tree and pokes her head out from around it."
                
                ava @ say "Hold this."
                
                n "She unscrews the lens from her camera and passes it to you."
                n "You can only just see her outline in the minimal light offered by the fallen sun as she attaches a telephoto lens onto her camera."
                n "The bird takes aim at something in the distance you can't possibly hope to see."
                n "You squint your eyes and notice some rustling brush amidst the darkness."
                n "*click click click click*"
                n "Ava takes several shots in quick succession, masking the soft footsteps as something approaches from behind."
                
                show gunner neutral at center with dissolve:
                    xpos -300
                    xzoom -1
                
                gunner @ say "Holy shit, what the fuck is that thing??"
                
                n "You turn around to see a wide eyed Gunner standing behind you, staring in despair at the apparent abyss."
                
                show ava annoyed
                
                ava @ say "Shh!"
                
                show ava typical neutral
                
                n "Ava looks down at her camera for a moment to adjust some settings."
                n "When she puts the viewfinder back up to her face she seems to look around, confused."
                
                show ava unsure
                
                ava @ say "Huh? Where'd it go? It was right there just a second ago!"
                
                player "Uhh Ava, I can't see much but it looks like the rustling grass is getting closer."
                
                gunner @ say "It must have smelled us! Come on, you got your shots, let's get out of here!"
                
                n "Gunner grabs both you and Ava by your shirt collars and hustles back to the trail."
                
                show ava pose annoyed
                
                ava @ say "Hey let go! Just one more shot!"
                
                hide gunner
                hide ava
                with dissolve
                
                n "The smell of blood and rot wafts past your nose. You chance a look behind you and feel a chill run down your spine when you see two glowing orbs staring at you."
                n "Gunner lets go of you as you overtake him and make it down the mountian even faster than him."
                n "The haunting scent only dissipates when you spot a warm glow between the leaves in the distance. Your caveman instincts tell you that must be a safe place."
                
                stop music fadeout 1.5
                
                n "Out of breath and fueled solely be adrenaline, you double time it to what ends up being a campfire way out here of all places."
                n "The smokey air and comforting heat are all you need to feel safe again."
                n "You don't even notice the campers until you hear their voices."
                
                play music "audio/music/vylet - Over Equestria.ogg" fadein 1.0
                
                show claire outdoors neutral at center:
                    xpos 700
                show rori neutral at center:
                    xpos 300
                show ava typical neutral:
                    xpos -300
                    xzoom -1
                show gunner neutral: 
                    xpos -600
                    xzoom -1
                with dissolve
                
                claire @ say "Ava?"
                
                rori @ say "Gunner? And [name]! What are you guys doing here?"
                
                player "Getting chased by skinwalkers apparently!"
                
                claire @ say "Lmao did you three get caught fuckin' in the woods?"
                
                gunner @ say "We definitely would have gotten horrifically murdered if we were."
                gunner @ say "That's how it always goes in like every horror film. The poor college students just trying to get laid always meet a gruesome end."
                
                n "Rori rolls his eyes and sighs."
                
                rori @ say "Ava, what happened out there?"
                
                ava @ say "Well I don't think it was a skinwalker but maybe more like a wendigo or something."
        
                rori @ say "Pics or it didn't happen."
                
                ava @ say "Don't give me that look! I have proof! I do have pics!"
        
                n "Ava holds up her camera and switches it on."
                n "Everyone gathers around her as it boots up and she navigates to the photo library."
                n "The shots are dark and you can make out what appears to be fresh blood on the trees but other than that there's no creature to be seen."
                
                show ava concerned -pose
                show claire outdoors neutral
                
                ava @ say "What? But I know it was there! Gunner you saw it too!"
                
                gunner @ say "Yeah, it was right there with its back to us right next to that tree right there!"
                
                show rori anxious
                
                rori @ say "I mean, it was probably a mountain lion or something and you just missed it? Still pretty spooky."
                
                show rori neutral
                show ava annoyed
                
                ava @ say "No, I know I had it in frame, I could see it through the viewfinder when I took the shots!"
                
                show ava concerned
                
                ava @ say "Unless..."
                
                n "Ava switches off her camera."
                
                show ava typical neutral
                
                ava @ say "Of course! Anything supernatural can't be recorded digitally."
                ava @ say "I knew I should have brought my film camera today..."
                ava @ say "I'll get a shot of it next time."
                
                gunner @ say "Next time? I'm not coming back here again, that's for sure! That thing was totally gonna eat us! I could see it in its eyes!"
                
                show ava annoyed
                
                ava @ say "Well not everyone is a scaredy cat!"
                
                gunner @ say "Yeah, and not everyone has wings to get away!"
                
                player "Whatever it was, we should be safe here. Wild animals fear the fire."
                
                n "Claire throws another couple of sticks onto the flames."
                
                show ava typical neutral
                
                claire @ say "Might as well get cozy if we're gonna stay here a while!"
                
                rori @ say "We're not gonna stay here all night are we? I still have homework to finish."
                
                claire @ say "Just until these two calm down."
                claire @ say "Until then, you are all cordially invited to join the cuddle puddle!"
                
                player "The what"
                
                pause .1
                
                show claire:
                    xpos 550
                show rori:
                    xpos 250
                show ava:
                    xpos -250
                show gunner:
                    xpos -500
                with move
                
                n "You are soon encompassed by soft bunny fluff, followed shortly by coarse ram fur."
                
                #play sound "ambient/outdoors night crickets.ogg" fadein 1.0
                #play music "audio/music/vylet pony - Reading at Night.ogg" fadein 1.5
                play music "audio/music/vylet - Over Equestria.ogg" fadein 1.0
                
                player "Oof!"
                
                if heshe == "he":
                    gunner @ say "Sorry bro, didn't mean to step on your balls."
                else:
                    gunner @ say "Sorry, didn't mean to step on your tits."
                    
                player "It's k."
                
                n "Typical cat behavior, stepping all over you."
                n "At least Ava doesn't weigh much as she crawls over you to snuggle in between you and Gunner."
                        
                ava @ say "'Scuse me!"
                
                claire @ say "Everyone comfy?"
                
                n "You settle in to the warm fur and feathers surrounding you, which is admittedly probably the comfiest feeling you've ever experienced."
                
                rori @ say "Yup!"

                player "Claire, you are the softest mattress I've ever laid on."
                
                show claire outdoors derp

                claire @ say "Thanks!"
                
                show claire outdoors surprised

                claire @ say "Whoa now Ava, I know you're excited to be snuggling your crushes but keep your pants on."
                
                show ava waitwhat
                
                ava @ say "What?! You're the one with Rori's head between your tits!"
                
                show claire outdoors neutral                
                show rori laugh
                
                rori @ say "\[*Happy ram noises*\]"
                
                show rori neutral
                
                #claire @ say "Don't be jealous, you get two cuties all for yourself~"
                #claire @ say "Wanna trade?"
                
                show claire outdoors lusty
                
                claire @ say "And *you're* the one sandwiched between two cuties~"
                
                show ava annoyed
                
                ava @ say "Y-you engineered it to happen like this!"
                
                show claire outdoors embarassed
                
                claire @ say "You're welcome~"
                claire @ say "Ksksksks~"
                
                n "Even in the cuddle puddle those two can't stop arguing."
                
                ava @ say "Huff!"
                
                show claire outdoors derp
                
                claire @ say "My paw can't reach. Someone spank Ava for being ungrateful."
                #claire @ say "It's up to you rori"
                #rori @ say "Who, me??"
                
                show ava annoyed
                
                ava @ say "Oh my gosh, don't you dare!"
                
                show claire outdoors embarassed
                
                claire @ say "What, you told me you were into that!"
                
                show ava embarassed
                
                ava @ say "Shshshshhhh!!!"
                ava @ say "I did not!"
                
                show claire outdoors lusty
                
                claire @ say "Twenty bucks says you'll squawk~"
                
                show ava angry
                
                ava @ say "SHut"
                
                n "You may never get a chance like this again. Should you go for it?"
                
                menu:
                    n "{cps=0}You may never get a chance like this again. Should you go for it?{/cps}"
                    "Just one couldn't hurt, right?":
                        n "It'll be funny, right?"
                        n "She's vaguely into you so she'll allow it, right?"
                        n "Your hand winds up and comes down with the force of a thousand virgins."
                        
                        show ava overjoyed
                        
                        ava @ say "Squawk~"
                        
                        show gunner at hop
                        
                        gunner @ say "Hey, paws off my bird!"
                        
                        n "Gunner hisses and attacks with his claws, digging them into your neck."
                        
                        player "AAAAAAH OH FUCK GET HIM OFF ME!"
                        
                        #n "Two slaps echo through the forest in quick succession."
                        
                        #n "You look Gunner in the eye, both of your hands on Ava's cheeks."
                        #n "The genie has been let out of the bottle now. War has officially been declared."
                        
                    "Nope, too risky":
                        #n "You can't. Raptor Jesus can judge you all he wants but you don't want to piss off the bird gods too."
                        n "You can't do it. What would she think? What would everyone else think?"
                        n "Gunner however has no such inhibitions and winds up for a smack that's sure to feel like slapping the a pillow from a 5 star hotel."
                        #n "To everyone's shock, not just one but two soft slaps ring out, echoing through the forest."
                        
                        show ava overjoyed
                        
                        ava @ say "Squawk~"
                        
                        #n "You look down and see both Gunner and Rori's hands on Ava's ass."
                        
                        #gunner @ say "You son of a bitch, I'll kill you!"
                        
                        #n "Just as Gunner pounces, claws ready to tear out Rori's neck, you feel the familiar sensation of being abruptly pulled out of a dream."
                        
                ###fade to white, fade back in 
                scene bg white 
                
                pause .1
                
                scene bg waterfall with dissolve
                
                show box:
                    ypos 0
                
                claire @ say "[name]! Wake up, sleepyhead!"
                
                n "You blink a few times, trying to recall where you are."
                
                show claire outdoors neutral:
                    xpos 550
                show rori neutral:
                    xpos 250
                show ava typical neutral:
                    xpos -250
                    xzoom -1
                show gunner neutral:
                    xpos -500
                    xzoom -1
                with dissolve
                
                
                n "You're surrounded by warmth and floof and everyone is staring at you."
                n "That's right, you were forcefully indoctrinated into the cuddle cult and then..."
                
                show claire outdoors embarassed
                
                claire @ say "Ksksksks you sure fall asleep quick! Did you know you talk in your sleep?"
                
                player "Wha? What did I say??"
                
                show ava embarassed
                
                ava @ say "Something about my 'feathery booty'???"
                
                n "Gunner busts out laughing."
                
                gunner @ say "Pffftahahahahahaa! You're a hoot and a half, you know that [name]?"
                
                show ava angry
                
                ava @ say "Hmph!"
                
                show claire outdoors derp
                
                claire @ say "Aww don't be mad, Ava. You should be honored [name] has dreams about your feathery butt!"
                
                n "Ava tries to maintain her composure but even she starts to crack up."
                
                show ava flattered
                
                ava @ say "Kshh, okay maybe it was a little funny hehehe~"
                
                show claire outdoors neutral
                
                n "Claire pulls everyone together for a tight hug."
                
                #show ava typical neutral
                
                claire @ say "I'm so glad I met you all <3"
                
                rori @ say "*wheeze* I'm... glad... too..."
                
                claire @ say "You all ready to go back into town?"
                        
                show ava portrait neutral
                
                ava @ say "Hah, yeah... I already forgot we were being hunted by a mythological creature."
                
                claire @ say "I'd say it's about time we get out of here."
                
                show ava typical neutral
                
                gunner @ say "We should be fine with the five of us travelling together."
                gunner @ say "Just have to make sure nobody gets picked off and skinwalkered."
                
                player "If it's a skinwalker versus Claire, my money's on the 300 pound 7 foot tall bunny."
                
                gunner @ say "For sure. Lanky cryptids BTFO."
                
                show claire outdoors embarassed
                
                claire @ say "350 pounds but who's keeping track am I right?"
                
                rori @ say "We're like a Dragons and Dungeons party transported into the real world."
                
                show claire outdoors derp
                
                claire @ say "Hah! Tonight has been way more fun than any LARP club I've been to!"
                
                rori @ say "Now I wanna write a campaign based on this trip. I think I'll call it Cryptids and Crypts."
                
                show claire outdoors surprised
                
                claire @ say "I'd play it!"
                
                n "Your party stamps out the dying campfire and covers it with dirt in preparation for finally leaving the woods behind and returning to your comfy dorms."
                #n "Claire invites everyone to continue the cuddle puddle at her dorm next weekend"
                
                stop sound fadeout 1.0
                stop music fadeout 1.0
                
                jump aftercuddlepuddle
                
                
            "Nah, I'm a pussy like Gunner, let's get out of here.":
                player "Nah, I'm a pussy like Gunner, let's get out of here."
                
                show ava angry
                
                ava @ say "Ugh, you cowards!"
                ava @ say "Fine, you two can run away but I'm going after it!"
                
                n "Ava turns around and takes flight in the direction of the noises."
                
                hide ava with dissolve
                
                show gunner neutral with dissolve:
                    xpos -300
                    xzoom -1
                
                gunner @ say "Aww hell. It's too dangerous to leave her alone. We better go after her."
                
                player "Y-yeah. You lead the way."
                
                hide gunner with dissolve
                
                n "It's so dark you can't see past your nose. You have to hold onto Gunner's tail otherwise you'd get lost in seconds."
                n "The further you go, the more you start to regret your decision."
                n "Your caveman instincts are telling you that whatever is out there has a clear advantage over you and could kill you without a second thought."
                n "After what feels like an eternity, you come across Ava perched in a low branch with her camera pointed at something."
                
                show ava annoyed with dissolve:
                    yalign 0
                    xpos 300
                
                ava @ say "Shh!"
                
                show ava concerned
                ava @ say "Almosssst..."
                
                n "You can only just see her outline in the dim light offered by the dusk sky as she slowly adjusts the focus ring on a chunky telephoto lens."
                n "The bird takes aim at something in the distance you can't possibly hope to see."
                n "Ava takes several shots in quick succession."
                n "*click click click click*"
                n "You squint your eyes and notice some rustling brush amidst the darkness."
                n "Gunner stealthily claws his way up the tree to Ava's height and manages to catch sight of what she's shooting."
                
                show gunner neutral at center:
                    xpos -600
                    xzoom -1
                
                gunner @ say "Holy shit, what the fuck is that thing??"
                
                player "What's going on? I can't see anything but I hear leaves rustling and it sounds like it's getting closer?"
                
                gunner @ say "It must have smelled us! Come on, you got your shots, let's get out of here!"
                
                n "Gunner grabs Ava and hops down from the tree, pulling you by your shirt collar away from there."
                
                show ava pose annoyed
                
                ava @ say "Hey let go! Lemme get just one more shot!"
                
                hide gunner
                hide ava
                with dissolve
                
                n "The smell of blood and rot wafts past your nose. You chance a look behind you and feel a chill run down your spine when you see two glowing orbs staring at you."
                n "Gunner lets go of you as you overtake him and make it down the mountian even faster than him."
                n "The haunting scent only dissipates when you spot a warm glow between the leaves in the distance. Your caveman instincts tell you that must be a safe place."
                
                stop music fadeout 1.5
                
                n "Out of breath and fueled solely be adrenaline, you double time it to what ends up being a campfire way out here of all places."
                n "The smokey air and comforting heat are all you need to feel safe again."
                n "You don't even notice the campers until you hear their voices."
                
                play music "audio/music/vylet - Over Equestria.ogg" fadein 1.0
                

                show claire outdoors neutral at center:
                    xpos 700
                show rori neutral at center:
                    xpos 300
                show ava typical neutral:
                    xpos -300
                    xzoom -1
                show gunner neutral: 
                    xpos -600
                    xzoom -1
                with dissolve
                
                claire @ say "Ava?"
                
                rori @ say "Gunner? And [name]! What are you guys doing here?"
                
                player "Getting chased by skinwalkers apparently!"
                
                claire @ say "Lmao did you three get caught fuckin' in the woods?"
                
                gunner @ say "If we were, we definitely would have gotten slashered! Like in every horror the movie with college characters!"
                
                rori @ say "Ava, what happened out there?"
                
                ava @ say "Well I don't think it was a skinwalker but maybe more like a wendigo or something."
        
                n "Rori sighs and rolls his eyes."
                
                rori @ say "Pics or it didn't happen."
                
                ava @ say "Don't give me that look! I have proof! I took photos!"
        
                n "Ava holds up her camera and switches it on."
                n "Everyone gathers around her as it boots up and she navigates to the photo library."
                n "The shots are dark and you can make out what appears to be fresh blood on the trees but other than that there's no creature to be seen."
        
                show ava concerned -pose
                show claire outdoors neutral
                
                ava @ say "What? But I know it was there! Gunner you saw it too!"
                
                gunner @ say "Yeah, it was right there with its back to us right next to that tree right there!"
                
                show rori anxious
                
                rori @ say "I mean, it was probably a mountain lion or something and you just missed it? Still pretty spooky."
                
                show rori neutral
                show ava annoyed
                
                ava @ say "No, I know I had it in frame, I could see it through the viewfinder when I took the shots!"
                
                show ava concerned
                
                ava @ say "Unless..."
                
                n "Ava switches off her camera."
                
                show ava typical neutral
                
                ava @ say "Of course! Anything supernatural can't be recorded digitally."
                ava @ say "I knew I should have brought my film camera today..."
                ava @ say "I'll get a shot of it next time."
                
                gunner @ say "Next time? I'm not coming back here again, that's for sure! That thing was totally gonna eat us! I could see it in its eyes!"
                
                show ava annoyed
                
                ava @ say "Well not everyone is a scaredy cat!"
                
                gunner @ say "Yeah, and not everyone has wings to get away!"
                
                player "Whatever it was, we should be safe here. Wild animals fear the fire."
                
                n "Claire throws another couple of sticks onto the flames."
                
                show ava typical neutral
                show claire outdoors heyeah
                
                claire @ say "Might as well get cozy if we're gonna stay here a while!"
                
                rori @ say "We're not gonna stay here all night are we? I still have homework to finish."
                
                show claire outdoors neutral
                
                claire @ say "Just until these two calm down."
                claire @ say "Until then, you are all cordially invited to join the cuddle puddle!"
                
                #this is the pussy out route, has some stuff you don't see in brave route

                player "The what"
                
                pause .1
                
                show claire:
                    xpos 550
                show rori:
                    xpos 250
                show ava:
                    xpos -250
                show gunner:
                    xpos -500
                with move
                
                n "You are soon encompassed by soft bunny fluff, followed shortly by coarse ram fur."
                
                #play sound "ambient/outdoors night crickets.ogg" fadein 1.0
                #play music "audio/music/vylet pony - Reading at Night.ogg" fadein 1.5
                play music "audio/music/vylet - Over Equestria.ogg" fadein 1.0
                
                player "Oof!"
                
                if heshe == "he":
                    gunner @ say "Sorry bro, didn't mean to step on your balls."
                else:
                    gunner @ say "Sorry, didn't mean to step on your tits."
                    
                player "It's k."
                
                n "Typical cat behavior, stepping all over you."

                ava @ say "'Scuse me!"
                
                n "Ava flutters past you to perch upon Gunner."
                
                claire @ say "Everyone comfy?"
                
                rori @ say "Yup!"
                
                n "You settle in to the warm fur and feathers surrounding you, which is admittedly probably the comfiest feeling you've ever experienced."
                
                player "Claire, you are the softest mattress I've ever laid on."
                
                show claire outdoors derp
        
                claire @ say "Thanks!"
                
                show claire outdoors embarassed
                
                claire @ say "You should try using Ava's butt as a pillow sometime!"
                
                show ava angry
                
                ava @ say "Shshshs don't say that!"
                
                show claire outdoors neutral
                
                claire @ say "What, it's true! At least your feathery butt is the softest pillow I've ever used."
                
                rori @ say "...I wanna hear the story of how that happened."
                
                show ava embarassed
                
                ava @ say "D-don't worry about it! Besides, *you're* the one with the softest pillows in Harmonia right now."
                
                rori @ say "Huh? What do you mean?"
                
                show claire outdoors derp
                
                claire @ say "Your head's on my tits dude."
                
                show rori anxious
                
                rori @ say "Wha? Oh my gosh, I didn't even mean to...!"
                
                show claire outdoors embarassed
                
                claire @ say "Ksksksks it's fine!"
                
                show rori neutral
                
                n "Claire wraps her arms around Rori's body, preventing him from escaping."
                
                show claire outdoors neutral
                
                claire @ say "Poor [name] though isn't snuggling anyone in particular!"
                
                show ava excited
                
                ava @ say "Yeah [name], hurry up and choose your threesome hehehe!"
                
                show claire outdoors lusty
                
                claire @ say "Wow I didn't expect you of all people to say that Ava."
                
                show ava embarassed
                
                ava @ say "I didn't mean like-"
                
                show claire outdoors derp
                
                claire @ say "Ksksks yes you did!"
                
                menu:
                    claire "{cps=0}Ksksks yes you did!{/cps}"
                    "Choose Rori and Claire.":
                        $ roriPoints += 1
                        $ clairePoints += 1
                        player "Well I wouldn't mind sharing a pillow with Rori."
                        
                        show claire outdoors lusty
                        
                        claire @ say "Go ahead!~ That's why I got two of 'em!"
                        
                        n "Claire grabs hold of you and pulls you in right next to Rori."
                        
                        rori @ say "Oh hi."
                        
                        player "Sup."
                        player "Come here often?"
                        
                        rori @ say "Not really."
                        
                        player "It's nice isn't it?"
                        
                        rori @ say "Yeah it's not bad."
                        
                        show claire outdoors neutral
                        
                        claire @ say "Ava please tell me you and Gunner are having a less awkward flirting experience than these two."
                        
                        n "Claire looks over to them."
                        
                        claire @ say "Oh. He's got his paws on her ass. He must be doin' something right."
                        
                        ava @ say "He's uhh, just testing that theory you proposed!"
                        
                        gunner @ say "About her soft feathery ass."
                        
                        claire @ say "You're welcome~"
                        
                        gunner @ say "Thank you based bunny!"
                        
                        claire @ say "Heh. They make a cute couple, don't you think?"
                        
                        #rori @ say ""
                        
                        menu:
                            claire "{cps=0}Heh. They make a cute couple, don't you think?{/cps}"
                            "Yeah I guess.":
                                player "Yeah I guess"
                            "...":
                                player "..."
                            
                            "Sure do!":
                                $ avaPoints =- 1
                                player "They sure do!"
                            
                        show claire outdoors lusty
                        
                        claire @ say "But we make a cuter trio~"
                        
                        rori @ say "To be fair, you two are doing all the heavy lifting."
                        
                        show claire outdoors derp
                        
                        claire @ say "Aww don't be so humble!"
                        
                        if roriPoints >= clairePoints:
                            show claire outdoors neutral
                            
                            claire @ say "I know for a fact [name] thinks you're cuter than me~"
                            
                            rori @ say "That can't possibly be true!!"
                            
                            player "...Well it is."
                            
                            rori @ say "!"
                            rori @ say "Why is it everytime I'm with you all you try to make me blush?!"
                            
                        else:
                            show claire outdoors neutral
                            
                            claire @ say "You and [name] would be just as cute as Ava and Gunner!"
                            
                            show ava concerned
                            
                            ava @ say "Wow, for once she's not making herself the center of attention. She must really mean that!"
                            
                            claire @ say "It's true!"
                            claire @ say "...But me and [name] would be the cutest couple. Just sayin'."
                            
                            show ava angry
                            
                            ava @ say "Oh there it is! I knew you couldn't go more than half a second without making things it about you!"
                            
                            show claire outdoors lusty
                            
                            claire @ say "Ksksksks shush and enjoy your catboy~"
                            
                            show ava waitwhat
                            
                            ava @ say "Don't tell me what to- *SQUAWK!*"
                            
                            claire @ say "Look at her, always scolding me for being too sexy when she lets Gunner get away with lewding her up in the cuddle puddle, a place for wholesome snuggles!"
                            claire @ say "Well, if they're going that far we might as well go all the way, right Rori? [name]?"
                            ###
                            n "unfinished"
                            
                            #pantsless rori
                            #wake up from dream
                        
                    
                    "Choose Ava and Gunner.":
                        $ avaPoints += 1
                        player "I volunteer to test the theory that Ava is softer than Claire."
                        
                        show ava waitwhat
                        
                        ava @ say "...I guess I brought this upon myself, didn't I?"
                        
                        show claire outdoors lusty
                        
                        claire @ say "You sure did~"
                        
                        n "You roll over onto Ava, who is lying on Gunner. Who is lying on Claire."
                        n "It's more like a cuddle tower than a puddle at this point but you're not complaining."
                        ###
                        n "unfinished"
        
                        #lie on top of ava, bird sandwich
        
                stop music fadeout 2.0
        

    ###
    #label gunnerwingman:
        #call phone_after_menu
        
        #call message_start("me", "How about", "testimage.png")
        #call reply_message("I come and be your wingman?")
        
        #call message("Gunner", "You'd do that?", "gunneravi.png")
        
        #call reply_message("Sure!")
        #call reply_message("I know you like Ava so I don't mind helping you out")
        
        #call message("Gunner", "Aw thanks so much!", "gunneravi.png")
        #call message("Gunner", "Back in high school random girls would usually ask me out so I have no idea how to approach a girl I actually like, y'know?", "gunneravi.png")
        
        #call reply_message("Yeah bro it's all good don't worry I got your back")
        
        #call message("Ava", "Well? We're about to head out soon.", "avaavi.png")
        
        #call reply_message("Hey yeah that sounds like a great time!")
        
        #call message("Ava", "Great! We'll come get you right now!", "avaavi.png") 

        #call reply_message("k, see you in a bit") 

        #call message("Ava", ":>", "avaavi.png") 
        
        
label aftercuddlepuddle:
    #n "As usual you can't just have a relaxing day, your friends always have some adventure they want to drag you out on."
    
    #scene bg codadorm with fade

    #show box

    #n "With nothing else to do today, you decide to man up and check up on how people are reacting to your story update."
    #n "It's been about a week so that should be plenty of time for shitposters, trolls and fans alike to post their comments."
    #n "Looking back on last week, you kinda overreacted. It's just text on a screen after all."
    #n "You log into your laptop and prepare for the worst as you scroll down to the comments section under your latest chapter."
    #n "\"Cool\" - cooldude438"
    #n "\"gay.\" - Xx_fanglover_xX"
    #n "The duality of man."
    #n "\"wow this really made my day blah blah blah I used to read your stories way back in the day blah blah blah you're so amazing and I want to blah blah blah\" - d1ck_suck3r_562"
    #n "There's always that one guy who will treat every post you make as the second coming of raptor Jesus."
    #n "\"Absolutely haram\" - deanon42"
    #n "Okay, reasonable."
    #n "\"Kill yourself\" - milkies69"
    #n "Fair enough."
    #n "\"Plebbit as fuck\" - smugpeppe55"
    #n "THAT'S IT YOU CROSSED THE FUCKING LINE."
    #n "You have to engage this troll with facts and logic and utterly annihilate him."
    #n "Your pride is at sake."
    #n "You click on the reply box and begin thinking out how you want to structure this post."
    #n "After 30 minutes of typing up a storm, you hit send."
    #n "Aaaaand the tab crashed. Great."
    #n "When you reload it your 5 page essay on why you're so great is gone."
    #n "Fuck it, you'll just reply \"no u\" and continue about your day."
    #n "Satisfied in destroying this room temperature IQ individual, you get back to work on your story."
    #n "It's become something of an obssession of yours lately. You don't know why you ever quit working on it. It's so much fun to write these characters you've come to love."


    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show tsaturday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7


    #___sunday5
    #tuesday5
label vacationday:
    #finished
    
    #wednesday5
    
    #booba tea

    scene bg codadorm with fade
    
    play music "audio/ambient/morning birds.ogg" fadein .5

    show box:
        ypos 0

    n "*knock knock knock*"

    claire @ say "[name]!!! Wake up! We've got a long day ahead of us!"

    n "You jolt awake and slowly piece together where you are."
    n "It kinda feels like the past couple weeks have been a dream. Or perhaps a nightmare."

    n "*KNOCK KNOCK KNOCK KNOCK*"
    n "You groan and roll out of bed."

    player "One second! Lemme put some pants on, jeez..."

    ava @ say "Take your time [name], we'll wait!"

    claire @ say "Or you could just open the door as you are right now :3"

    show ava typical neutral at offscreenleft:
        yalign 0
    show claire sweater neutral at offscreenright:
        yalign 0

    n "You throw on some clothes and open the door."

    play music "audio/music/vylet - Oak Library.ogg" fadein 1.0

    show ava typical neutral at center:
        xzoom -1
        xpos 1440
    show claire sweater neutral at center:
        xpos 460
    with move

    claire @ say "Heyyyyy! What's up? Why haven't you been responding to our texts??"

    player "Huh? Oh sorry, I forgot to put my phone on the charger before falling asleep."

    ava @ say "It's cool. It's not like we were about to just abandon you today!"

    claire @ say "Yeah!! We've got a busy schedule today and it wouldn't be the same without you!"

    player "Remind me again what we're doing? I have to go to class in like two hours."
    
    show ava bored

    ava @ say "You already forgot?"
    
    show claire sweater overjoyed
    
    claire @ say "We're skipping class today to go on an adventure!"
    
    show ava overjoyed
    
    ava @ say "We're gonna get some boba tea and go out shopping and get massages at the spa and and and"
    
    show claire sweater neutral
    
    player "Did you just wake up and decide to do this?"
    
    show ava typical neutral
    show claire sweater surprised

    claire @ say "Oh my gosh do you really not remember?"

    ava @ say "Yeah, we had a whole conversation about this last week! Did you hit your head or something??"

    player "Now that you mention it, it rings a bell. But it feels more like it happened in a dream."
    
    show claire sweater leaning

    claire @ say "Well we better make sure today's unforgettable then, huh?"
    
    show claire sweater neutral
    
    claire @ say "Come on, let's go get coffee first to wake you up, sleepyhead~"

    player "*Yaaaaawn*"
    player "Sounds good to me!"

    scene bg town with fade
    
    show box with Dissolve(.2):
        ypos 0

    ###bump into ellen and celestine in town

    n "After grabbing breakfast at Coffee Zone, you, Claire and Ava roamed the streets off campus."
    #n "With it being a weekday, it almost felt like a ghost town. Everyone was at work or school. It was nice to have the town practically all to yourself though."
    n "The three of you walked through main street and explored the various antique shops, boutiques, and other stores without a care in the world."
    n "Getting pampered at the spa was obviously the highlight of the day."
    n "Relaxing and listening to Ava and Claire gossip about cute boys and petty girl drama while getting a massage was definitely worth letting your classwork pile up."
    n "They barely even argued!"
    n "Not to mention your nails have never looked better."
    n "They even had a sauna, though apparently they aren't as popular among your anthro friends. Probably because it causes their fur and feathers to get heavy with dampness and smothers them."
    n "But as someone with based human skin, it really opened up your pores and relieved all the tension in your body, melting away all your worries."
    n "Ava had to drag you out, otherwise you never would have left."
    n "You suspect Claire let her towel slip on purpose when you were looking in her direction even though she swears it was an accident."
    n "Then there was the incident at the tea shop where she kept referring to your drinks as 'booba tea.'"
    n "With the sun starting to set, you make your way back to the dorms."
    n "Overall it was quite a pleasant day, but apparently the bird and bunny weren't done with you yet."

    show ava typical neutral at center:
        xpos 500
    show claire sweater neutral at center:
        xzoom -1
        xpos -400
    with dissolve

    #play music "audio/music/Evan Schaeffer - React.ogg" fadein .5

    player "This was awesome, we should do this again sometime."
    
    show claire sweater neutral alert

    claire @ say "Hey today's not over yet! The night's still young, you know~"
    
    show ava unsure

    ava @ say "Yeah, don't tell me you forgot our sleepover plans too!"

    player "Huh? I'm sleeping over at your place tonight?"

    show claire sweater leaning

    claire @ say "Other way around, silly~"
    
    show ava overjoyed

    ava @ say "Your dorm is so much nicer than ours! They gave you more room even though it's just you in here."
    
    show ava typical neutral

    player "Yeah but where are you two gonna sleep? I only have one bed."
    
    show claire sweater giggle

    claire @ say "Oh I'm sure we can make that work~"
    
    show ava pose ohyou

    ava @ say "Hehehe, hope ya don't mind getting cozy with us~"

    player "Well if you insist..."
    
    scene bg codadorm with fade
    
    #play music "audio/music/Vylet Pony - lemonade.ogg" fadein .5
    play music "audio/music/vylet pony - Reading at Night.ogg"
    
    show box:
        ypos 0

    show ava typical neutral at center:
        xpos 500
    show claire sweater neutral at center:
        xzoom -1
        xpos -400
    with dissolve

    n "Claire flops on your bed and Ava flutters over."

    claire @ say "Go ahead and put some flixnet on the TV, [name]!"

    n "Aw hell, you always knew this day would come."
    n "The day you'd have to admit you don't have a flixnet subscription and that you just pirate TV shows from streaming sites."
    n "At least last time you had Rori as a scapegoat since he had all those obscure shows on his flash drive."

    player "Err about that..."

    show bg static2
    pause .02
    show bg static3
    pause .02
    show bg codadorm
    
    show ava concerned

    ava @ say "What's wrong? You *do* have a streaming service, don't you?"
    # I mean, how much of a virgin would you have to be to not have one in current year?"
    
    show claire sweater surprised

    claire @ say "Are you okay? You're doing that human thing where water comes out of your skin."

    n "Fuck fuck fuck fuck fuck they know."
    n "You carefully weigh your options."
    n "The window is a mere 2 meters to your left, you could jump out and the fall would likely kill you immediately but you just remembered you haven't cleared your browser history yet."
    n "Then it hits you."
    n "Rori left his flash drive here!"
    n "You can load up one of his animes and just say it's not on any American streaming services so Rori downloaded it for you."
    n "Of course, that means you'll have to deal with the obnoxious noises and annoying anime tropes but it's better than your friends thinking you're a virgin."

    player "A-actually, why don't I put on some anime? There's this one Rori downloaded for me that I've been wanting to watch and it's not on flixnet..."
    
    show claire sweater neutral

    claire @ say "Sounds good to me!"
    
    show ava excited

    ava @ say "Go for it!"
    
    show ava typical neutral

    n "Whew, they fell for it. Now you just have to plug your laptop in and pick a normal anime..."
    n "Dammit Rori, why are all your file names in Japanese??"
    n "You double click one at random and the video opens. After a few seconds the subtitles show up, revealing the name of this series to be \"Monster Girl Adventure\""
    n "Oh deer lord no, not this..."
    
    show ava overjoyed

    ava @ say "Ooh, this looks interesting!"
    
    show claire sweater surprised

    claire @ say "Hey I've heard of this one!"
    
    show claire sweater leaning
    
    claire @ say "Interesting choice~ Hurry up and fullscreen it, [name]~"
    
    show ava typical neutral

    n "It's too late now, the die has been cast and your fate is sealed."
    n "All you can do is sit on the bed between your friends and prepare for an awkward night."
    n "Distracted by all your worrying and overthinking, you're caught off guard when the pungent odor of alcohol wafts through the air and Claire nudges you."

    claire @ say "Hey, you got any soda? Or am I gonna have to chug this raw?"

    n "Claire waves a bottle in front of your face."

    player "What the..? Where'd you get that?"
    
    show claire sweater -leaning pose lusty

    claire @ say "I told you I was bringing alcohol, duh. I managed to get my paws on a full bottle of vodka! Pretty sweet, huh?~"

    n "She says with a wink as she licks the bottle."
    
    show ava pose unimpressed

    ava @ say "I'd say it's the opposite of sweet tasting. Just smelling it from over here is making me sick..."
    
    show claire sweater embarassed

    claire @ say "Aww, don't worry I'll mix it with somethin' to make it more palatable for ya!"

    player "I think I have some sodas in the fridge."

    n "You move to get up and grab some but Claire puts her paw on your shoulder and forces you back onto the bed."
    
    show claire sweater derp

    claire @ say "I got it~"
    
    show claire sweater neutral

    n "The big bunny blocks your view of the TV as she walks over to the fridge, swaying her hips."
    n "She opens the door and bends down, taking her time grabbing the drinks with her ass in the air and her little tail wagging."
    n "She somehow manages to be more lewd than this literal porn anime on the screen right now."
    n "She even looks behind her to make sure you're watching, though it's not like you could avoid having the thicc bun in your field of vision no matter which direction you're facing."
    n "You look over to Ava who's stifling a giggle."

    player "Was this part of the plans we made earlier too?"
    
    show ava portrait neutral

    ava @ say "Hehehe no, this is just how she is~"
    
    show ava typical neutral

    n "Claire plops down on the bed with a pack of soda and some plastic cups you had lying around, knocking both you and Ava into the air."
    n "When you come back down, the bunny wraps her arms around both you and Ava, the two of you on each side of her."
    
    show claire sweater pose lusty alert

    claire @ say "Trust me, once you get a little alcohol in this bird, she'll be the same way~"

    show ava unimpressed

    ava @ say "Psh, not true!"

    n "Claire pours everyone a round of drinks, mixing extra pop in with Ava's to dilute the nail polish taste and smell."

    claire @ say "You're right, you could never match how sexy I am~"
    
    show ava annoyed

    ava @ say "More like how slutty you are!"
    
    show claire sweater leaning -lusty

    n "Claire sticks our her tongue."

    claire @ say "Try not to be so jealous~"
    
    show ava angry

    ava @ say "Hmph!"

    n "Once again you find yourself in the middle of one of their bickering sessions. At least you have some booze to sip on while they go at it."
    n "They continue to argue while you watch the show. It's actually pretty good. The story has you engaged and the monster girls are cute."
    
    show ava tipsy
    show claire sweater lusty alert

    ava @ say "...and bigger ishn't always better! Small, perky tits are serper... suprer... serprerior! More gooder than your big dumb cow udders!"

    claire @ say "At leasht my titties are fuggable! *hic* Who would ever wanna feel up a flat board like your chesht?"

    ava @ say "Better to get a pawfuls of shoft feathery boobas than flabby floppy fatty fat fat fat!"

    n "High school did not prepare you for this."

    claire @ say "Let'sh ssssettle this right now! [name]! If you had to pick one us... *hic* for the tiddies! Who would you pick?"

    menu:
        claire "{cps=0}Let'sh ssssettle this right now! [name]! If you had to pick one us... *hic* for the tiddies! Who would you pick?{/cps}"
        "Claire":
            $ ellenPoints = ellenPoints + 1
            $ avaPoints = avaPoints - 1
            n "You hesitate, preparing yourself for Ava's wrath."

            player "...Claire."
            
            show claire sweater leaning -lusty

            claire @ say "Hah! I told ya! Humans looooooove bigger~"

            n "The bunny pulls you in for a hug, pressing her massive pillowy chest into your face while Ava glares at you."

            #ava @ say "I'll strangle you with your own bra!"
            
            #claire "You hear that, [name]? Ava wants to take off my bra ksksksksks!"
            
            
            #claire "You'll have to get it off first~"
            
            #ava says something about strangling claire with her own bra, claire counters saying it's not big enough

            #claire @ say "What bra?~"

            #ava @ say "Grrr... Fffffine you win thiss battle, but a nice toned aaaasssssss ish what everyone wants!"
            
            ava @ say "Grrr... Who needfsdfsa tits when -hic- when I've got an ass like this!"

            #claire @ say "Sorry, [name] can't hear you over the sound of my massive titties covering [hisher] ears!"

            n "The two move onto arguing about butts. Once Claire lets you go, you take another drink and the rest of the night becomes a blur."
        "Ava":
            $ rosePoints = rosePoints + 1
            $ roriPoints = roriPoints + 1
            $ clairePoints = clairePoints - 1
            n "You hesitate, preparing yourself for Claire's wrath."
            
            player "...Ava."

            ava @ say "Hah! I was right! [name] has a more refined taste in breasts~"

            n "The bird pulls you in for a hug, rubbing your face between her petite breasts while Claire glares at you."

            claire @ say "You can't even smother [name] with those tiny tits of yours!"
            claire @ say "At least I've got the better ass~"

            ava @ say "What makes you think someone would prepfer your fat butt in favor of a nice toned ass like mine?"
            
            show claire sweater leaning -lusty

            claire @ say "You saw how [name] was staring when I was bent overr earlierrrr!"

            ava @ say "That's only cause your ass is bigger than the broad side of a barnnn!"

            claire @ say "I'll take that as a compliment~"

            n "The two move onto arguing about asses. Once Ava lets you go, you take another drink and the rest of the night becomes a blur."
        "Both":
            $ avaPoints = avaPoints + 1
            $ clairePoints = clairePoints + 1
            player "Both are great."

            n "Both Claire and Ava instantly shift from being catty to being flattered. They both hug and nuzzle you tight, pressing their chests against you."

            ava @ say "Ohmygosh [name] you're soooooooo sweet!!! I'm so sorry for calling your tits flabby Claire!"

            claire @ say "[name] you're the beshtttt!! I'm sorry for calling you flat Ava!"

            n "You can't breathe but that's alright. This is a good way to die."
            n "The rest of the night is a blur, but you recall Ava and Claire moving on to arguing about who has the better ass next."


    stop music fadeout 1.0

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show tmonday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    #___thursday5
    #finished
    #note, have alternative scene depending on previous gunner/ava choices and their affinity
    scene bg codadorm with fade

    #play music "audio/ai21.ogg" fadein .5
    play music "audio/ambient/morning birds.ogg" fadein .5

    show box:
        ypos 0
    
    n "You wake up to the sound of banging on your door."
    n "Each knock feels like they're hitting your head directly."
    n "Fuuuuuuck you're so hungover. You forgot to drink any water last night."
    n "You clumsily roll over Claire's body on your way out of bed. She's sound asleep and doesn't notice you, even as you trip over the blanket and hit the ground."
    n "You slowly open the door, just a crack."

    show gunner neutral at center with dissolve:
        xzoom -1

    gunner @ say "Morning, [name]. You didn't show up to class last night so Mrs. Herschel wanted me to give you this homework-"

    n "Gunner's eyes suddenly go wide."

    gunner @ say "Yo, is that Claire in your bed? Holy shit dude! I knew she was into you!"

    n "You hear rummaging behind you. You take a peek and see Ava's head pop up from behind Claire's body."

    show ava waitwhat at center with dissolve:
        xpos 500

    show gunner neutral

    ava @ say "Gunner...? Oh uh, hey!!!"

    n "Grimacing, you slowly turn back to Gunner."

    #show gunner angry
    ###show gunner yiik pose
    gunner @ say "How could you-"
    gunner @ say "What the hell is going on??"

    player "It's not what you think, we were just..."

    gunner @ say "Ugh, whatever. Forget it."
    gunner @ say "Here, just take this. I gotta go. Later."

    hide gunner with dissolve

    n "He hands you a packet full of math problems and immediately turns away and leaves."
    
    show ava reaching concerned

    ava @ say "..."

    ###if you have a certain number of avapoints, do this alt route instead
    #ava @ say "Who was that?"

    #player "...Nobody. Just a classmate dropping off some homework."

    #ava @ say "Mmh... What happened last night?"

    show claire sweater embarassed at center:
        xpos -350
        xzoom -1
    with dissolve

    claire @ say "*YAAAAAAAWN*"
    claire @ say "Mornin'~"
    claire @ say "Last night sure was fun, huh?~"
    
    show ava unimpressedbrowless

    ava @ say "Ugh, maybe if I could remember it..."
    
    show claire sweater derp

    claire @ say "Aw, don't tell me you caught [name]'s amnesia too!"
    
    show ava flattered

    ava @ say "Heheh... Yeah, I think that's enough drinking for me for a while..."
    
    show ava overjoyed
    
    ava @ say "Anyway, I'm sure I had a good time with you [name]!"
    
    show ava typical neutral
    
    ava @ say "But me and Claire should really get back to our dorm and get ready for class."
    
    show claire sweater neutral

    claire @ say "As much as I'd like to stay, she's right. Can't afford to skip too many classes but I'm sure we'll be able to do this once more before the semester's up~"

    player "Heh, we'll see~"
    player "I had a great time with you guys but it's about time we went back to being full time students."

    n "You help Ava and Claire collect their things and they head out."
    
    show claire sweater lusty

    claire @ say "See you in French later~"
    
    show ava excited

    ava @ say "And I'm sure I'll see you right after!"

    player "Later!"

    hide claire
    hide ava
    with dissolve

    n "Whew. What a day."
    n "Hopefully class is easy today cause you and your hangover are in no mood to learn."
    n "You make yourself presentable and walk out, head still throbbing."

    show bg campus

    show bg calendar
    show ttuesday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    scene bg black with fade

    #n "A few days later..."
    
label hospital_revisit:
    #finished
    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    play music "audio/music/vylet - wish.ogg" fadein 1.5

    #n "You pour some milk into a bowl of cereal and start to eat at your desk while reading through your favorite Bulgarian right wing Neonpets blog."
    n "When you get back from class, you make a bowl of cereal and take your pills between bites of corn syrup enriched corn flakes."

    #show bg static1
    #pause .02
    #show bg codadorm
    
    #n "Once you're finished, you throw out the styrofoam bowl and plastic spoon and throw your bag over your shoulder."
    #n "Woops, almost forgot to take one of your pills."
    n "You can't say you like the idea of being dependent on pills to survive, but life could certainly be a lot worse."
    n "You're in one of the most prestigious universities in the world, you've made friends, and a big sexy bunny might be into you."
    n "For the first time since you can remember, you feel pretty content."
    n "Maybe you should be grateful for what you have."
    #n "As you're about to step out the door and head to class, your phone rings."
    n "*Bzzzz*"
    n "Oh that's your phone. Who could be calling you now?"

    show phonecall at center with dissolve:
        #ypos 1280
        xpos 700
        ypos 200
    
    kitsuragi @ say "Hello, I'm with Harmonia Medical Center. Is this [name]?"

    n "You recognize that voice. It's the kitsuragi who was taking care of you."
    n "Suddenly you don't feel so good anymore..."

    player "Er, yes. This is [name] speaking."

    kitsuragi @ say "Would you be available to come in and talk about your condition? The sooner the better."

    player "Um sure. Were you hoping for like, today?"

    kitsuragi @ say "Like now would be best."

    player "Okay... I'll be there in half an hour."

    kitsuragi @ say "Thank you. I'll see you soon."

    n "{i}Click.{/i}"

    hide phonecall with dissolve

    n "Your heart sinks in your chest."
    n "From the tone of her voice you can tell this isn't going to be a fun visit."

    stop music fadeout 1.0

    scene bg campus with fade

    play music "audio/ambient/indoors people talking.ogg" fadein 1.5

    show box with Dissolve(.2):
        ypos 0

    n "Anxiety wells up inside you as you walk to the medical center."
    n "You can't stop your brain from automatically assuming the worst."
    n "You barely pay attention to your surroundings while you walk."
    n "Before you know it, you're outside the hospital."
    n "You spot the kitsuragi smoking a cigarette at the side of the building."

    show kitsuragi at center with dissolve

    kitsuragi @ say "Oh, you're earlier than I expected."

    player "Yeah... Can we get this over with?"

    kitsuragi @ say "Of course. Come with me please."

    stop music fadeout 1.0

    scene bg hospital with fade

    #play music "audio/ai6.ogg" fadein 1.0
    play music "audio/music/vylet - the child who dreamt it all.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0

    show kitsuragi at center with dissolve

    n "The kitsuragi brings you inside and into a room similar to the one you stayed in over the weekend."

    kitsuragi @ say "I'm just gonna get the routine checkup bullshit out of the way quickly cause I'm sure you don't have time for this sort of thing."

    n "She wraps something around your arm and connects it to a machine that slowly inflates it."
    n "She takes a reading from the machine and writes it down before deflating the armband and removing it."

    kitsuragi @ say "Blood pressure's a bit high but that's expected."
    kitsuragi @ say "Any headaches, drowsiness, or nausea since Monday?"

    player "No. If anything I've felt great these past few days."

    kitsuragi @ say "Well, at least those pills are working."

    player "I noticed I've been forgetting things more often though."
    player "Like, I literally won't know how I got to class sometimes."
    player "And occasionally I'll see static? And get that feeling like when you get up too fast after lying down for a while."

    n "The kitsuragi writes that down in a notepad then looks away and sighs."

    kitsuragi @ say "Look, there's no easy way to tell you this but the blood tests came back and..."
    kitsuragi @ say "And we can say with confidence that you do in fact have nihil syndrome."

    n "You feel your heart sink to the bottom of your stomach."

    #player "What?! No, redo the test! It was probably just a false positive!"
    player "What?! You said I was fine last time I was here!"

    kitsuragi @ say "I'm afraid we already ran tests multiple blood samples using different methods and they consistently tested positive."

    n "You slump in your seat, feeling like this is some sort of bad dream."

    player "So this means I'm gonna die soon, right?"

    n "The kitsuragi avoids eye contact, gesturing with her hands as she tries to come up with an answer for you."

    kitsuragi @ say "Well... since we caught it early... and there have been advancements in medicine... experimental technology could..."

    player "Just- how long do you think I have?"

    kitsuragi @ say "...Five years? Maybe more, maybe less. I don't know. This disease isn't easy to predict."

    player "So just enough time to graduate college and keel over. Great."

    kitsuragi @ say "Hey, I'm not saying for sure you'll pass away anytime soon, that was just an estimate based on average cases."
    kitsuragi @ say "Some people went ten, fifteen, almost twenty years before it was their time."
    kitsuragi @ say "You may not be around for as long as you'd like but you can do a lot in the time you have left."
    
    player "Even if I do stay around longer than expected, it'll be a miserable existence."
    player "I've seen how the affected get. They're practically zombies. No more energy, fading memory, totally apathetic."
    
    kitsuragi @ say "My advice to you is to take advantage of every single day. Don't let any time go to waste. Enjoy your time here while it lasts."
    kitsuragi @ say "I guess that advice goes to everyone, but moreso in your case."

    player "So... that's it? \"You're dying, but make sure you spend your time wisely. Bye!\""

    kitsuragi @ say "Pretty much."
    kitsuragi @ say "My boss initially wanted to put you back in one of these beds so we could run more tests on you but I convinced him it would be pointless."
    kitsuragi @ say "You've got a life to live, a destiny to fulfill and such. No need to waste it in here. Do whatever you wanted to do."

    n "You look down, unsure of what do say or do."

    kitsuragi @ say "..."
    kitsuragi @ say "Look, I have a confession to make."
    kitsuragi @ say "I could see the signs from the first tests we ran on you."
    kitsuragi @ say "I intentionally mislead you and told you you probably didn't have the disease because I knew it would only depress you."
    kitsuragi @ say "And when you're running out of time, the last thing you need is depression."
    kitsuragi @ say "You've had nihil syndrome for who knows how long, but you could very well have lived the rest of your life without knowing."
    kitsuragi @ say "Don't let this drag you down. Just use this knowledge to prepare and do whatever you always wanted to do before the end of your life."
    kitsuragi @ say "I'm truly sorry, but that's the best advice I can give you."

    n "You want to argue but she's got a point."
    n "And besides, you really want to get out of this place as soon as possible."

    player "Fine. If that's all you have for me, then I'll be leaving. Thanks for the heads up."

    kitsuragi @ say "We'll continue to monitor your case and provide as much support as we can. Don't hesitate to call us if you feel strange in the slightest."
    kitsuragi @ say "Here's my card. Call me whenever you feel like, even if you just wanna talk or whatever."

    player "...Thanks."

    n "You take her card and hurry out of the room."

    stop music fadeout 1.3

    scene bg campus with fade
    
    play music "audio/ambient/indoors people talking.ogg" fadein 1.5

    show box with Dissolve(.2):
        ypos 0

    n "You don't even know where you're going right now, just as long as it's away from that hospital."
    n "The sound of people around you talking, yelling, being happy drives into your head like a jackhammer."
    n "Goddammit why can't they just shut up?"
    n "You need some peace and quiet and to be alone."
    n "But it's just so loud and crowded everywhere on campus!"
    
    stop music fadeout 1.0

    ###choice to either visit cafe or go to dorm?

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    n "You stormed back to your dorm and have been lying in bed for the past hour, breathing heavily while your brain tries to make sense of the situation."
    n "What are you even supposed to do now?"
    n "Everything is so pointless."
    n "Even if you graduate from this stupid university, you'd hardly have enough time to do anything after."

    show bg static2
    pause .02
    show bg static1
    pause .02
    show bg codadorm

    n "But what else are you going to do?"
    n "Get some awful wageslave job until you die?"
    n "Hold that thought, your phone is buzzing."

    call phone_start from _call_phone_start_12

    call message_start("Gunner", "Where were u today?", "gunneravi.png") from _call_message_start_16

    call phone_end from _call_phone_end_13

    n "Screw this, you don't feel like talking to anyone, let alone explaining your absence."
    n "You're just gonna..."

    show bg static1
    pause .05
    show bg static2
    pause .05
    show bg static1
    pause .05
    show bg static3
    pause .05

    show bg codadorm

    n "*Yawn*"

    show bg static3
    pause .05
    show bg static2
    pause .05
    show bg static1
    pause .05
    show bg static3
    pause .05
    show bg static2
    pause .05
    show bg static2
    pause .05
    show bg static3
    pause .05
    show bg static1
    pause .05

    show bg codadorm

    n "Just gonna... fall asleep right now..."

    hide box

    show bg static1
    pause .05
    show bg static2
    pause .05
    show bg static1

    show bg codadorm

    pause .05
    show bg static3
    pause .05
    show bg static1
    pause .05
    show bg static3
    pause .05
    show bg static2

    show bg codadorm

    pause .05
    show bg static3
    pause .05
    show bg static1
    pause .05
    show bg static2
    pause .05
    show bg static2
    pause .05
    show bg static3
    pause .05
    show bg static1
    pause .05
    show bg static1
    pause .05
    show bg static2
    show bg static1
    pause .05
    show bg static2


    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show tfriday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

label cafe_comfort:
    #finished
    #it's night
    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    n "..."
    #n "Today you wake up feeling like crap, and not just because you forgot to take your pills last night."
    n "You lie in bed staring at the ceiling wondering what to do next."
    n "You can't really come up with anything but your patience is wearing thin."
    n "You need to get out and do something, anything."
    n "Hopping out of bed, you put on a coat and head outside."

    scene bg cafe with fade

    play music "audio/music/mere - coffeeLoveLoopInstrumental.exe.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0

    n "Somehow you always end up at the cafe. Surprisingly it's still open at this hour."
    n "As usual, Mishka is there behind the counter ready to greet you and take your order."

    show mishka neutral at center with dissolve

    mishka @ say "Hello [name]!"
    
    show mishka saddest
    
    mishka @ say " ...Vsyoh horosho? You look sort of out of it today."

    player "Eh, going through some personal stuff. Wouldn't wanna bother you with the details."
    
    show mishka depressed

    mishka @ say "I understand. Life can be like that sometimes. I can only hope some of coffee will make things better, maybe?"
    
    show mishka neutral
    
    mishka @ say "The usual?"

    player "Yeah, that'd be great."

    mishka @ say "Don't worry about paying, it's on house."
    #it's on the mouse!

    player "Thanks, Mishka."

    n "You hang around the counter while Mishka prepares your coffee."
    n "Thankfully no one else is around to witness your miserable face."

    mishka @ say "There you go! Enjoy!"

    n "Feeling the warmth through the paper cup and smelling the fresh roasted coffee somehow makes you feel a little more alive."
    n "It's hard to describe but in a small sense you almost seem to forget about your problems and just live in this very moment."

    player "Thanks. I uh, needed this."
    
    show mishka happy

    mishka @ say "Always a pleasure to be of helping people!"

    n "Mishka grins at you. You can't tell if she's just being polite or if she genuinely means it."
    n "But you'd rather choose to believe she cares on some level."
    n "Not necessarily about you since you're just another customer, but about helping people and making the world a better place."
    n "Or at least a more tolerable one. Just a bit of kindness goes a long way."
    #n "Huh... Making the world a better place?"
    #n "..."
    #n "Where were you going with that train of thought?"
    #n "You've had so much on your mind lately you can hardly keep up with your own thoughts."
    #n "Whatever, if it's important you'll remember it later."
    #n "For now, you give Mishka an appreciative nod and head outside."
    n "You give Mishka an appreciative nod and head outside."

    stop music fadeout 1.3

    scene bg campus with fade

    show box with Dissolve(.2):
        ypos 0

    n "It's pretty chilly out tonight. Good thing you brought a coat."
    n "The coffee helps to warm you up as well."
    # n "Feels like a storm's about to come in."
    n "You just wander aimlessly for a while, wondering what you're going to do now."
    #n "before realizing you have class today but you quickly dismiss the idea of attending."
    n "There doesn't seem to be any point in going to class anymore, considering your circumstances."
    n "And besides, you just really really don't feel like going."
    n "And who could blame you? People take days off for lesser problems than literally dying."
    n "It's kinda funny. You feel like you've skipped class more than you've attended them."
    n "Hey, it's not like you asked to be put into a pointless school system that consumes what little life you've got left."
    n "You need to figure out what you're gonna put the rest of your life towards. Something worthwhile."
    #n "You spend the rest of the day just wondering around town aimlessly, not really knowing what to do or what to feel."
    #n "You've sort of calmed down but you're still not happy and you doubt you will be anytime soon."

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show tfriday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    #___saturday5
label friendly_hangout:

    #scene bg codadorm with fade

    #show box

    #n "You wake up sometime in the afternoon. No point in going to class anymore. No point in anything really."
    #n "You reach over to your sidetable and grab your pill bottle."
    #n "You've got a headache but these are usually pretty good at clearing that up."
    #n "Rolling out of bed, you go to the sink to get a glass of water."

    #show bg static1
    #pause .02
    #show bg codadorm

    #n "Huh? You were already at the sink."
    #n "Your glass is overflowing with water as the faucet continues to pour into it."
    #n "You shake your head and turn off the faucet before popping some pills and taking a sip."

    #show bg static1
    #pause .02
    #show bg static2
    #pause .02
    #show bg static3
    #pause .02
    #show bg static1
    #pause .02
    #show bg codadorm

    #n "Huh? You were already at the sink."
    #n "Your glass is overflowing with water as the faucet continues to pour into it."
    #n "You shake your head and turn off the faucet before popping some pills and taking a sip."
    #n "Ahh, much better."



    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0
    
    play music "audio/music/vylet - yeah i'm ok thanks for asking.ogg" fadein 1.5

    #claire comments on player skipping class so often?

    n "Another sunrise, another day closer to death."
    n "Screw this, you're getting sick of moping around. It feels like such a waste."
    n "Everything feels like a waste but walking around doing nothing seems especially useless."
    n "You've got to start living your life without regrets."
    n "Do something worthwhile with your time."
    n "Suddenly your phone buzzes, pulling you out of your current thoughts."
    n "Looks like you have a few messages from yesterday."

    call phone_start from _call_phone_start_13

    call message_start("Gunner", "Hey Rori's gonna show me how to play this dragons and dungeons game on saturday, you wanna come?", "gunneravi.png") from _call_message_start_17

    call message("Claire", "Hiiii <: me and ava are going to the botanical gardens on saturday if you wanna join us~~", "avaavi.png") from _call_message_132

    call phone_end from _call_phone_end_14

    n "Maybe what you need right now is a distraction and both of those options sound good."


    if roriPoints <= (avaPoints + clairePoints - 5):
        #untested
        $ dndnight = True
        
        n "Gunner has always been a bro to you, despite your differences. You should hang out with him more."
        n "You feel like you don't hang out with Rori enough though. He's always been kind to you but he's always just kinda... in the background."
        n "He's probably a really cool guy once you get to know him more."
        
        call phone_start from _call_phone_start_14

        call message_start("me", "You still need a player? Sorry for not getting back to you sooner.", "testimage.png") from _call_message_start_18

        call message("Gunner", "It's all good.", "gunneravi.png") from _call_message_133
        call message("Gunner", "And yeah, we could always use one more!", "gunneravi.png") from _call_message_134
        call message("Gunner", "We're getting things set up if you wanna come over now. You know where our dorm is?", "gunneravi.png") from _call_message_135

        call reply_message("Yeah I'll be right over") from _call_reply_message_102

        call phone_end from _call_phone_end_15

        n "Not wanting to keep them waiting, you rush to get ready and head out to Edgar Hall."

        scene bg roridorm with fade

        show box with Dissolve(.2):
            ypos 0

        #play music "audio/exports/Feather [653254166].opus" fadein 1.0
        play music "audio/music/vylet - Oak Library.ogg" fadein 1.0

        show rori neutral at center:
            xpos 450
        show gunner neutral at center:
            xzoom -1
            xpos -450
        with dissolve

        rori @ say "...so that about covers the basic rules. Did you get all that?"

        gunner @ say "Uhh..."
        gunner @ say "What was that part about calculating how to do... damage and evasion and stuff?"
        gunner @ say "Eh, nevermind. I'll figure it out as I go along."

        rori @ say "Don't worry about calculations, I'll handle all that stuff."
        rori @ say "Just focus on roleplaying as your character and I'll guide you along."
        rori @ say "[name], Adam, you two ready?"

        n "A voice comes from Rori's laptop."

        show adam at center with dissolve

        adam @ say "Yup. I've been working on my wizard's stats all day."

        player "Who the hell is Adam?"

        rori @ say "Oh, I forgot to mention that to [name]. Adam is with us through the power of the internet."

        adam @ say "I'm out of town at my grandmother's funeral but I *never* miss a DnD session."

        player "Wait, are you at your grandma's funeral *right now?*"

        adam @ say "..."

        n "His voice becomes garbled and incomprehensible over the next few seconds."

        adam @ say "...Sorry, lag."
        adam @ say "Are we all ready to play now?"

        player "I've never really played these kinds of games but I'll manage."

        rori @ say "I guess it can be intimidating with all the numbers and rules and stuff but it'll be fun, trust me."
        rori @ say "For context, this campaign takes place in the Republic of Lunaria, a powerful nation thanks to its natural resources and strong army."
        rori @ say "Guards regularly patrol towns and roads, ever vigilant of criminals so be on your best behavior when eyes are on you or you might get to take part in a public execution."
        rori @ say "Okay, let's begin with some character back stories!"
        rori @ say "Adam, why don't you start us off?"

        adam @ say "Alright, my character is an arrogant wizard named Edor, known for his many tricks and spectacles."
        adam @ say "He's currently on the run from the law after accidentally burning down a circus tent during a performance and killing dozens of guests."
        adam @ say "Although he travels disguised, he has a bad habit of revealing his true identity when someone badmouths Edor for the circus incident."
        adam @ say "He's currently searching for a way to become a hero and cleanse his reputation."

        rori @ say "Nice! How about you Gunner?"

        gunner @ say "I'm a warrior named Vodstock. I made a living selling pelts from bears I killed with my bare hands but business has dried up after I wiped out the local feral bear population."
        gunner @ say "So I've decided to journey the lands in search of new challenges."
        gunner @ say "Vodstock is a firm believer that every problem can be solved using his fists."

        rori @ say "Interesting... Your turn, [name]!"

        player "Err..."

        n "You didn't really come prepared so you have to make up a character on the spot."

        menu:
            n "{cps=0}You didn't really come prepared so you have to make up a character on the spot.{/cps}"
            "I'm a bard":
                player "I'm a travelling bard named Wilden who got separated from his caravan and is now wandering the country alone."
                player "During my travels, I came across a smoldering crater in the middle of a field and among the ashes I found a mysterious device that produces music on its own."
                player "I use it in conjunction with my own instruments to create musical genres that have never before been heard..."
                player "...which grant me strange abilities like being able to jump higher, run faster, and swing a sword harder."
                player "It usually draws quite a crowd and has been my main source of income lately."

                rori @ say "Haha okay, we'll go along with that."
                rori @ say "Alright, are we all ready to begin?"
                rori @ say "Let's see... Okay, I've got it!"
                rori @ say "During his travels, Vodstock came across a village having a bit of a bear problem eating the locals' livestock and even attacking some villagers."
                rori @ say "Vodstock put his expertise in hunting bears to use and took on a contract to track down and kill the terrorizing bear."
                rori @ say "Coincidentally, a travelling bard happened to be in the area and believes he can pacify the bear using his musical talents."
                rori @ say "He decides to join Vodstock in hunting down the bear and hopefully taming it."
                rori @ say "Meanwhile, a certain wizard tries to escape from some guards who caught wind that he was in the area after he drunkenly boasted about his glory days as a stage magician."
                rori @ say "He's cutting through a forest when he encounters two strangers struggling against a massive wild bear! I'll let you all take it from here."

                adam @ say "Being the arrogant wizard I am, I rush in to help these fellows against this bear. Who knows, I might even be regarded as a hero for my actions!"

                gunner @ say "I've got the bear in a headlock and say to the stranger..."
                gunner @ say "\"Hark! Who goes there? Stand back, I don't want you to get hurt, bystander! I might accidentally swing at you and break your nose with my pinkie finger!\""

                rori @ say "..."

                player "Oh uh, \"yeah don't worry, we got everything under control!\""
                player "That's what I yell out to the wizard, while clinging to the bear's back and fiddling with my music box."
                player "\"Dammit, that tune only seemed to make him angrier...\""

                rori @ say "Okay, go ahead and everyone roll for initiative."

                n "Adam picks up a die and rolls it."
                n "You and Gunner look at each other before rolling your own die as well."

                rori @ say "The bear flings Wilden off and knocks him against a tree, causing him to drop his music box. The beast also escapes Vodstock's headlock and puts him in one of his own."

                adam @ say "I clear my throat and raise my hands in a position to cast some motherfuckin' magic."
                adam @ say "\"Leave this to me.\""
                adam @ say "Lighting begins to crackle at my fingertips and I point at the bear."

                player "\"Wait! Don't kill him! He's just misunderstood!\""

                adam @ say "I scoff at the notion but decide to play along."
                adam @ say "\"Fiiiine, I'll just use an electrified net to immobilize him.\""

                n "Adam rolls a 20 sided die and it lands on 4."

                rori @ say "Oof. Not quite powerful enough to trap this enemy. Static electricity escapes from your fingers but it's hardly more than an uncomfortable shock."
                rori @ say "It's enough to get him to stop mauling Vodstock, though now Edor has an angry bear charging toward him."

                player "What if I boost the spell with some music?"

                rori @ say "That could work!"
                rori @ say "If you roll high enough that is."

                n "You pick up the die and roll it."
                n "It lands on 12."

                rori @ say "That'll do it!"

                player "I press a button on the box and it plays a new song, a rapid, thumping beat that sounds like distant thunder."
                
                rori @ say "Success! The bear is now ensnared in a cage of electricity!"
                
                gunner @ say "Holding onto my shoulder which had sustained a swipe of the bear's claws, I wander up to the others."
                gunner @ say "\"Whew, that bear sure was tougher than the ones back home! I reckon he'd be a powerful ally if you manage to tame him.\""

                player "I play around with the knobs and buttons on the music box, testing different melodies until I find one that seems to soothe the bear."
                player "\"Alright I think I found one that works! Lower the lightning, but be prepared to raise it just in case!\""

                adam @ say "I lower the electric field but keep my hands poised to fry the bear if it tries anything."

                rori @ say "The bear slowly walks up to Wilden and sniffs his face before giving him a lick."

                player "\"Ew.\""

                gunner @ say "\"Success!\""

                player "\"Thanks for your help, kind wizard! I wish I could repay you but I don't have any money at the moment.\""

                adam @ say "\"That's quite alright, being a hero is its own reward.\""
                adam @ say "\"Though, that's quite an interesting contraption you've got there. It seems to possess some magical qualities. I'd love to take a look at it sometime.\""

                player "\"Sure, but it doesn't really work for anyone other than me.\""
                player "I hand Edor the box, but it only responds with static when he messes with it."

                adam @ say "\"Ah, it must have chosen you to be its master then. Nothing I can do about that.\""
                adam @ say "\"However, they say that wielders of magical items like these have a grand destiny awaiting them.\""
                adam @ say "\"If you don't mind, I'd like to journey with you to see what fate has in store for you.\""

                player "I shrug."
                player "\"Sure I guess.\""

                gunner @ say "\"And I'd like to study this bear you've made friends with. I never would have believed such a thing if I hadn't seen it with my own one eye.\""
                gunner @ say "By the way I just decided my character has an eyepatch."

                rori @ say "Uh... sure, alright."

                gunner @ say "\"What are you going to call him?\""

                player "\"I was thinking...\""

                menu:
                    "Truffles":
                        $ bearname = "Truffles"
                        player "...Truffles."
                    "Bon Bon":
                        $ bearname = "Bon Bon"
                        player "...Bon Bon."

                gunner @ say "\"Haha, how d'you like the sound of that, [bearname]? I think it suits you well!\""

                rori @ say "[bearname] snorts and licks Vodstock's face."

                adam @ say "\"By the way, I never caught your names.\""

                gunner @ say "\"Name's Vodstock the bear hunter.\""

                player "\"And I'm Wilden the bard. I studied music at the college down in Southsand.\""

                gunner @ say "\"What about you? You must be an experienced wizard to be able to pull off lightning spells without electrocuting yourself.\""

                adam @ say "\"Damn straight! I am Edor the great and powerful wizard of sparks and spectacles!\""
                adam @ say "\"Perhaps you've heard of me?\""

                n "You and Gunner shrug."

                adam @ say "\"Ah well... Perhaps that's for the best... Anyway, lead the way to your cabin, Wilden.\""

            "I'm an alchemist":
                player "I'm an alchemist named Wilden who has lost his alchemy license due to malpractice."
                player "Reluctant to give up potion making after spending so much time and money at the college of concoctions, I've secluded myself and experimented with fantastic revolutionary potions."
                player "However, they always come with a downside. Drinking a potion that grants you the ability to see through walls may later give you cancer for example."

                rori @ say "Haha okay, we'll go along with that."
                rori @ say "Alright, are we all ready to begin?"
                rori @ say "Let's see... Okay, I've got it!"
                rori @ say "During his travels, Vodstock came across a village having a bit of a bear problem eating the locals' livestock and even attacking some villagers."
                rori @ say "Vodstock put his expertise in hunting bears to use and took on a contract to track down and kill the terrorizing bear. However, a local potion brewer had other plans..."
                rori @ say "Wilden, certain that all his new potion needed was some feral bear saliva, asked to tag along with Vodstock in order to collect the ingredient to ensure freshness."
                rori @ say "Meanwhile, a certain wizard tries to escape from some guards who caught wind that he was in the area after he drunkenly boasted about his glory days as a stage magician."
                rori @ say "He's cutting through a forest when he encounters two strangers struggling against a massive wild bear! I'll let you all take it from here."

                adam @ say "Being the arrogant wizard I am, I rush in to help these fellows against this bear. Who knows, I might even be regarded as a hero for my actions!"
                
                gunner @ say "I've got the bear in a headlock and say to the stranger..."
                gunner @ say "\"Hark! Who goes there? Stand back, I don't want you to get hurt, bystander! I might accidentally swing at you and break your nose with my pinkie finger!\""

                rori @ say "..."

                player "Oh uh, \"yeah don't worry, we got everything under control!\""
                player "That's what I yell out to the wizard, holding a jar under the bear's mouth while clinging to its back."
                
                rori @ say "Okay, go ahead and everyone roll for initiative."

                n "Adam picks up a die and rolls it."
                n "You and Gunner look at each other before rolling your own die as well."

                rori @ say "The bear flings Wilden off and knocks him against a tree, causing him to drop his jar. The beast also escapes Vodstock's headlock and puts him in one of his own."
                
                adam @ say "I clear my throat and raise my hands in a position to cast some motherfuckin' magic."
                adam @ say "\"Leave this to me.\""
                adam @ say "Lighting begins to crackle at my fingertips and I point at the bear."

                player "\"Wait! I need the bear alive! At least until I can get a sample of its saliva!\""

                adam @ say "\"What on earth do you need bear drool for?! Ah no matter, I'll simply make a lightning cage to ensnare the bear!\""

                n "Adam rolls a 20 sided die and it lands on 4."

                rori @ say "Oof. Not quite powerful enough to trap this enemy. Static electricity escapes from your fingers but it's hardly more than an uncomfortable shock."
                rori @ say "It's enough to get him to stop mauling Vodstock, though now Edor has an angry bear charging toward him."

                player "Oh, I think I have a potion that boosts magic prowess in my satchel..."

                rori @ say "That'll work!"

                player "I dig the bottle out from my bag and toss it to Edor."

                adam @ say "I immediately chug the potion and prepare the spell again."

                rori @ say "Success! The bear is now immobilized in a cage of electricity!"

                adam @ say "\"Hurry up and collect your stupid sample, I can't keep this up for long!\""

                player "\"R-right.\""
                player "I hesitantly walk up to the bear as it glares down at me with a hungry look in its eyes."

                rori @ say "The jar fills up quickly due to how much it's drooling."

                adam @ say "Ok, now what?"

                gunner @ say "Holding onto my shoulder which had sustained a swipe of the bear's claws, I wander up to the others."
                gunner @ say "\"Whew, that bear sure was tougher than the ones back home! It's almost a shame to have to kill it.\""
                gunner @ say "\"Say, Wilden, you don't happen to have a potion that'll turn him tame for a while do you? At least until I can tame him myself?\""

                player "\"I think I have something like that, hold on...\""
                player "I dig a potion out of my bag and hand it to Vodstock."
                player "\"Good luck administering it...\""

                gunner @ say "I just pry open its jaws and pour it inside its maw."

                rori @ say "Roll the die."

                n "Gunner picks up the die and rolls a 14."

                rori @ say "Success! The bear swallows the potion and after a few seconds, he becomes visibly becomes relaxed and no longer has a thirst for murder."

                adam @ say "\"Nice work! I'm a bit rusty on that spell. Back in the day it would be no problem to hold it up for hours.\""
                adam @ say "I lower the electric barrier, ready to raise it again if the bear attacks."

                player "\"Thanks for your help, kind wizard! If you'd like, I can repay you with a sample of my newest potion once it's done brewing.\""

                adam @ say "\"Ah, that must be why you needed bear drool. Tell me, what does this potion aim to do?\""

                player "\"If my hypothesis is correct, it will render you invisible for quite some time. Be warned though, I cannot predict the consequences.\""

                adam @ say "\"Interesting... I'm sure that will come in handy at some point.\""

                player "\"My shack isn't too far from here. The potion should be done by tea time. You can stay a while and rest if you'd like.\""

                gunner @ say "\"Do you mind if I tag along? I don't really want to show up in town with the bear, lest I scare off the lasses.\""
                gunner @ say "\"Speaking of which, what should I call him? I was thinking something along the lines of Truffles or Bon Bon.\""

                menu:
                    "Truffles":
                        $ bearname = "Truffles"
                        player "\"Truffles sounds sweet.\""
                    "Bon Bon":
                        $ bearname = "Bon Bon"
                        player "\"Bon Bon sounds cute.\""

                gunner @ say "\"Haha, how d'you like the sound of that, [bearname]? I think it suits you well!\""
                
                rori @ say "[bearname] snorts and licks Vodstock's face."

                adam @ say "\"By the way, I never caught your names.\""

                gunner @ say "\"Name's Vodstock the bear hunter.\""

                player "\"And I'm Wilden, graduate of the school of alchemy up in uh... Norskton.\""

                gunner @ say "\"What about you? You must be an experienced wizard to be able to pull off lightning spells without electrocuting yourself.\""

                adam @ say "\"Damn straight! I am Edor the great and powerful wizard of sparks and spectacles!\""
                adam @ say "\"Perhaps you've heard of me?\""

                n "You and Gunner shrug."

                adam @ say "\"Ah well... Perhaps that's for the best... Anyway, lead the way to your cabin, Wilden.\""

        rori @ say "And thus begins the journey of Edor, Vodstock, Wilden and [bearname]. Will they become heroes of Lunaria or be the catalyst for its destruction?"
        rori @ say "Don't worry, that's not all we're doing today, we're just gonna take a quick break."
        rori @ say "How do you like it so far?"
        
        gunner @ say "It's pretty cool! It's a lot less nerdy than I thought it was gonna be."

        player "Yeah, I like how it forces you to get creative and stuff."

        adam @ say "I think our party is shaping up quite nicely. I like the addition of a wild bear companion named [bearname]."

        rori @ say "I'm glad you're all enjoying it! I'm having a great time too!"
        rori @ say "Imma grab some snacks and sodas. You guys want anything?"

        hide rori
        hide gunner
        hide adam
        with dissolve

        n "Hanging out with Rori and the others really lightened your mood. You totally forgot about everything going south in your life for a while."
        n "Only when it's time to leave do you start to feel sad again but even then something's changed."
        n "You realize you have a group of friends to enjoy spending time with. It doesn't even feel like a waste of time, rather it's probably the most worthwhile thing you can do."
        
        stop music fadeout 1.0

        scene bg codadorm with fade

        show box with Dissolve(.2):
            ypos 0

        n "Overall today was pretty good but you're feeling a bit drained."
        n "You crawl into bed and close your eyes, reflecting on the day with nary an intrusive thought until you fall asleep."

        stop music fadeout 1.3

    else:
        ""
        

        stop music fadeout 1.3

        scene bg codadorm with fade

        show box with Dissolve(.2):
            ypos 0

        n "Overall today was pretty good but you're feeling a bit drained."
        n "You crawl into bed and close your eyes, reflecting on the day with nary an intrusive thought until you fall asleep."

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show tsaturday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    #___sunday6
    #rose workout scene

    #___monday6

    ###
    #time skips around
    #rose asks if you're okay
    #you must look like shit if even rose is asking that
    #can say yeah or not really
    #time skip to gunner in math class when you answer


    #___thursday6
label ellen_rooftop1:
    #finished

    scene bg schoolhallways with fade

    show box with Dissolve(.2):
        ypos 0
    
    play music "audio/ambient/indoors people talking.ogg" fadein 1.0
    
    #faced with expulsion if you don't go back to class but was given some extra days off for condition
    #n "You check your phone."
    #n "It's already Thursday. You can hardly even remember the past few days."
    
    #change it so you find yourself in the literature building, not knowing why. you sure as hell aren't going back to class, but then you see ms ellen
    
    
    #n "It kinda feels like you're still in a dream. One of those nightmarish ones where you feel like you're waking up and going to school."
    #n "But this is no dream. At least you're pretty sure it's not."
    #n "You really are dying and you're wasting your time going to school."
    #n "At first you thought \"What's the point of going to school?\""
    #n "But then you thought \"What's the point of anything?\""
    #n "You won't live long enough to make much of an impact in the world, and you're certainly never going to do everything you always wanted to do."
    #n "But after some contemplation, you decided you can at least get your degree. That way you can die knowing you accomplished *something.*"
    #n "Honestly, you're just so used to the school lifestyle, you're kinda afraid to try anything else."
    #n "You could drop out today but what would you even do? Go back home and play video games? Pathetic..."
    #n "Maybe you could commit a federal crime and go out in a blaze of glory?"
    #n "Or just travel the world until you can't physically continue?"
    #n "Backup plans are nice to have but for now you're going to focus on trying to get through this semester."
    ##don't say it now but later on the protag realizes the real important thing was making an impact on their friends' lives
    #n "Having to study can be a drag but at least you're suffering together with your friends in that regard."
    #n "And going to class just lets you see them more often."
    #n "...Man, what a cope, but it's all you've got."
    #n "That and a copy of Bartleby the Scrivener."
    #n "It's about time to go to literature. You toss the book in your bag and zip it up before slinging it over your shoulder and heading out."
    #n "You wish you had a friend in that class but at least Miss Ellen is nice to you."
    
    n "Huh? What are you doing here? You sure as hell aren't planning on going back to class now, but for some reason you have your backpack on and are wandering the halls of the literature building."
    #n "You check your phone. It's about 15 minutes before you're supposed to have literature."
    

    n "What was that all about?"
    n "You absentmindedly make your way to class, forgetting that you had planned on skipping."

    stop music fadeout 1.3

    scene bg classroom with fade
    
    play music "audio/music/mere - retrograde.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    n "Miss Ellen hardly seemed to acknowledge your conversation during or after class but you're still left thinking about it."

    show celestine neutral at center with dissolve

    celestine @ say "[name]? [name] are you paying attention?"

    player "Huh? Oh, yeah."

    celestine @ say "How do you say 'I forgot my homework' in French?"

    player "Err..."

    show claire sweater surprised at center with dissolve:
        xpos 500

    claire @ say "J'ai oublié mes devoirs."

    celestine @ say "Very good Claire. Next time let [name] figure it out on their own."
    
    show claire sweater heyeah

    claire @ say "Don't worry, I'll make sure [heshe] studies over the weekend~"

    celestine @ say "Très bon!"
    celestine @ say "Now please turn to page 134 in your textbooks!~"

    stop music fadeout 1.3

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show tmonday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    #___friday6
label spicy_restaurant:
    #finished
    scene bg campus with fade
    
    show box with Dissolve(.2):
        ypos 0
    
    play music "audio/music/vylet - Pancake.ogg" fadein 1.0
    
    n "You really weren't planning on returning to class but it's become a habit."
    n "And Gunner had asked for your help in stats but you couldn't offer much assistance in your deteriorated state of mind."
    n "You really need a nap. These social obligations are killing you."
    #n "You were kinda zonked out during class but at least you survived the week. Now you can go home and relax and not have to worry about social obligations for another few days."
    
    
    show ava casual happy at center:
        xpos 400
    show claire outdoors neutral at center:
        xzoom -1
        xpos -400
    with dissolve
    
    n "Oh god dammit."
    
    claire @ say "Hiiiii [name]!!!"
    
    show ava casual concerned
    
    ava @ say "Wow, you look like death. You alright?"
    
    player "I'm fine, just tired is all."
    
    show claire outdoors surprised
    
    claire @ say "Dang, are classes really that tough on you? How much sleep are you getting?"
    
    player "Uhh between 12 and 16 hours I think?"
    
    show ava casual unimpressed
    
    ava @ say "That is like, the opposite of how much sleep you're supposed to get."
    
    claire @ say "Yeah, maybe you should see a doctor about that...."
    
    player "It's fine, I can manage."
    
    show claire outdoors neutral
    
    claire @ say "Well if you can stay up long enough, we were gonna check out this new restaurant tonight!"
    
    player "What kind of restaurant is it?"
    
    claire @ say "Thai! Or wait, was it Korean? Actually I think it's Japanese?"
    
    show ava casual smile
    
    ava @ say "It's some sort of Asian food. Apparently they have this super spicy noodle bowl challenge where if you finish it without throwing up, your meal is free!"
    
    claire @ say "I can't really handle spicy food so count me out!"
    
    #ava @ say "Same!"
    
    player "Well, I don't think I'd ever pass up the opportunity for free food. Just tell me when and where."
    
    claire @ say "We're still figuring it out but I'll text ya the details later!"
    
    show ava casual happy
    
    ava @ say "Yeah, this is kinda a last minute thing and it's already a super busy Friday! We gotta run now but we'll see ya in a few hours, k?"
    
    player "Sure. See you two later at this restaurant."
    
    claire @ say "Byeeee~"
    
    #show ava casual excited
    
    ava @ say "Laters~"
    
    n "Ava gives you a wave and the two run off, giggling."
    
    hide claire
    hide ava
    with dissolve
    
    n "Well that gives you something to do tonight."
    #n "Better hurry to your dorm to get in a few hours of relaxation before hanging out with your friends."
    
    scene bg town with fade
    
    #play music "audio/music/Evan Schaeffer - Aqueduct.ogg" fadein .5
    play music "audio/music/vylet - Our Light and After (ft. Pepper Mei).ogg" fadein .5
    
    show box with Dissolve(.2):
        ypos 0
    
    n "You ended up just taking a nap once you got home. You forgot to set an alarm but thankfully Claire spamming your phone woke you up."
    n "As usual, you're late but hey that just means you won't be waiting on anyone."
    n "You spot your friends sitting around a table in an outdoors dining area and make your way towards them."
    
    show gunner neutral:
        xpos -325
        xzoom -1
    show rori neutral at center:
        xpos -675
        xzoom -1
    show claire outdoors neutral:
        xpos 520
    show ava casual happy:
        xpos 800
    with dissolve
    
    ##shows everyone
    #show rose neutral at center:
    #    xpos 100
    #show margaret neutral at center:
    #    xzoom -1
    #    xpos -300
    #show ellen neutral at center:
    #    xzoom -1
    #    xpos -220
    #show gunner neutral:
    #    xpos -525
    #    xzoom -1
    #show rori neutral at center:
    #    xpos -800
    #    xzoom -1
    #show claire sweater neutral:
    #    xpos 570
    #show ava typical neutral:
    #    xpos 850
    #show mishka neutral at center:
    #    xpos 350
    #with dissolve
    
    hide box
    
    show box:
        ypos 0
    
    show claire outdoors derp
    
    claire @ say "Heyyyy you made it, sleepyhead!~"
    
    show claire outdoors neutral
    
    player "Kept ya waiting, huh? Sorry about that. I see you invited my bros to join us too!"
    
    n "You give Gunner and Rori fist bumps as you sit down."
    
    gunner @ say "Heyyy, wassup [name]!"
    
    rori @ say "Glad you could join us!"
    
    show ava casual daydream
    
    ava @ say "You took so long we decided to go ahead and order for you."
    
    player "Really? Nothing too expensive I hope..."
    
    show ava casual smile
    
    ava @ say "Quite the contrary! ...If you can finish it, that is."
    
    n "You raise a brow and are about to ask what she meant when the waitress arrives and sets everyone's meals on the table."
    
    #show waitress at center with dissolve
    
    waitress "Aaaand for you the spicy ramen bowl challenge! Please sign here so we're not liable for any damages to your short term or long term health. Good luck!"
    
    n "She hands you a pen and paper, which you absentmindedly sign, confused as to why you have to sign something just to have hot sauce in your pasta."
    
    waitress "Thank you~ And here's the one for you too!"
    
    n "The waitress hands over the pen and a similar paper to Gunner before setting down his bowl."
    
    waitress "Try not to die!"
    
    n "She does a little bow and heads back inside."
    
    hide waitress with dissolve
    
    rori @ say "Yeesh, it's making my eyes water already. I can even taste it from all the way over here!"
    
    gunner @ say "Hahaha sorry [name] but I swear it wasn't my idea! Ava thought it would be funny to order it for you and well, I didn't want you to suffer alone!"
    
    show ava casual unimpressed
    
    ava @ say "I was only half serious!"
    #ava @ say "Hehehehe *chirp~*"
    
    claire @ say "You can have some of what I got if it's too spicy for you [name]."
    
    #player "It's fine. I mean, how spicy can it be? It smells pretty good in fact."
    player "It's fine. Humans evolved to eat this kinda stuff. It smells pretty good in fact!"
    
    show ava casual happy
    
    ava @ say "You sure? I don't wanna be responsible for killing ya."
    
    player "Yeah! I mean, I didn't have any restaurants like this where I grew up but I always enjoyed spicy food. They probably just hype it up for marketing. How hot could this be?"
    
    gunner @ say "I guess we're about to find out!"
    
    n "Gunner grabs his chopsticks, fumbling with them for a bit trying to grab a slice of beef on top of the noodles."
    
    gunner @ say "Goddammit... fuck... almost... dangit... Where's a fork when you need one? Ah screw it."
    
    n "He stabs the meat with a chopstick and puts it in his mouth while the whole squad watches with curiosity and anticipation."
    
    rori @ say "Well. He's not dead yet."
    
    n "Gunner finishes chewing and swallows."
    
    gunner @ say "Huh. That was... not so ba-"
    
    n "He suddenly wheezes and reaches for his drink, downing half the cup before setting it down."
    
    gunner @ say "Okay it doesn't hit you at first but when it does it's like getting hot brass down your shirt."
    gunner @ say "Still not the spiciest I ever had."
    
    ava @ say "I think it's supposed to get spicier the further down you go."
    
    player "A real 9 circles of hell, I'm sure."
    
    show claire outdoors derp
    
    claire @ say "Alright [name], your turn!"
    
    show claire outdoors neutral
    
    n "Unlike Gunner, you actually know how to use chopsticks and pick up a clump of noodles to slurp. It doesn't taste any different than the generic spicy ramen you could find at any grocery store."
    
    player "Heh, easy."
    
    n "And then it hits you. You cough uncontrollably for a few seconds as you frantically reach for your drink, taking a few sips until the fire in your mouth has been extinguished."
    
    player "Ack! You were right, it does have a delayed kick to it."
    
    gunner @ say "I told you! Here Rori, have some of this."
    
    rori @ say "What? No way! Keep your peppers off my lemongrass tofu!"
    
    show ava casual smile
    
    ava @ say "What's the matter, don't think you can finish it all on your own?"
    
    gunner @ say "I'm sure I could, I just dunno if the discount is gonna be worth being bathroom-bound all day tomorrow."
    
    n "You silently take another, smaller bite. You're already sweating."
    
    show ava casual overjoyed
    
    ava @ say "Look, [name] can do it just fine!"
    
    gunner @ say "Yeah but look how much [heshe]'s sweating though!"
    
    player "We humans evolved to eat food like this not out of necessity but out of pure dumbfuckery and stubbornness."
    
    show ava casual flattered
    
    #n "The group snickers at your self-deprecating joke."
    n "As Ava takes a bite out of her meal, Claire leans in and whispers something to her, causing her feathers to floof up and almost makes her choke on her food."
    
    ava @ say "Whaaaat? Claire oh my gosh no!"
    
    gunner @ say "What? What did she say?"
    
    ava @ say "Nothing hahaha nothing!"
    
    show claire outdoors embarassed
    
    claire @ say "All I'm sayin' is, he's competitive! He'd totally be down for it!"
    
    gunner @ say "What???"
    
    show claire outdoors derp
    
    claire @ say "I just said there should be a prize for whoever finishes their spicy bowl first!"
    
    show ava casual annoyed
    
    ava @ say "Claire shush!"
    
    n "Gunner's ears perk up. If you had fluffy adjustable ears, they'd be perked too."
    
    player "What sort of prize?"
    
    show claire outdoors lusty
    
    n "Claire giggles and winks at you."
    
    claire @ say "Whatever you want bby~"
    
    gunner @ say "I'd finish this thing right now if I could get a lapdance."
    
    show claire outdoors embarassed
    
    claire @ say "That's it? I was gonna suggest something... spicier ksksksksks!"
    
    show ava casual angry
    
    ava @ say "Oh quiet you! I'm not just gonna hand out lapdances to anyone who can eat spicy food!"
    
    claire @ say "I would."
    
    player "Okay how about just sitting in the winner's lap?"
    
    show ava casual concerned
    
    ava @ say "Hrm..."
    
    show claire outdoors lusty
    
    claire @ say "Come onnnnn, I know you wanna do it! Have some fun every once in a while!"
    
    n "Everyone stares at Ava expectantly."

    show ava casual annoyed
    
    ava @ say "...Alright fine! I'll do it, but this is just a one time offer!"
    
    show claire outdoors heyeah
    
    claire @ say "I call dibs on the loser's lap!"
    
    show ava casual happy
    
    n "Gunner grimaces at the thought."
    
    show claire outdoors neutral
    
    gunner @ say "Well, I can't say no to the chance to have a pretty bird in my lap. I just hope Claire's ass doesn't crush you when you lose, [name]!"
    
    player "Nah, Ava's cute butt is gonna be perched right here."
    
    n "You pat your thigh."
    n "Ava hides her face behind a wing, too embarassed to face anyone."
    
    show ava casual unimpressed
    
    ava @ say "Guyyysss!"
    
    rori @ say "For the record, I had nothing to do with this."
    
    show ava casual smile
    
    gunner @ say "Enough talk! Our duel for soft feathery cheeks begins now!"
    
    n "You and Gunner dig into your bowls, haphazardously taking large bites to get through it quicker."
    n "Gunner is getting better at using the chopsticks, grabbing whole clumps of noodles at once."
    n "Your tongue stings and you soon run out of water, taking to chewing on ice cubes to dull the pain."
    n "Your mouth is on fire but you can't rest for even a moment if you want to beat Gunner when he's this determined."
    n "He's panting like a dog and his eyes are sweating but he's not slowing down."
    n "The pain is unbearable at this point. You haven't taken a bite in a few seconds but the feeling is getting exponentially worse every second."
    n "You're feeling woozy. Should you press on?"
    
    menu:
        n "{cps=0}You're feeling woozy. Should you press on?{/cps}"
        "Keep going":
            #finished
            $ avaPoints += 1
            n "No, you're not giving up. You can do this. You will assert your dominance!"
            n "You're nearing the bottom of the bowl now. Gunner is struggling with his last few bites."
            n "You grab the bowl and vaccuum the rest down into your stomach."
            n "It's finished. You won. You close your eyes and revel in your victory."
            
            stop music fadeout 1.0
            
            scene bg black with fade

            #hide box

            #show bg calendar
            #show tfriday at center
            #with Dissolve(.5)

            #pause .6
            #show tforwardslash
            #pause .2
            #show tbackslash

            pause .65
            
            scene bg hospital with fade
            
            show box with Dissolve(.2):
                ypos 0
            
            #play music "audio/music/vylet - tenderness.ogg" fadein 1.5
            
            n "Urgh... you feel like death. Every breath you take hurts. You can't feel your tongue but you can feel your intestines are punishing you for your hubris."
            n "You can't remember a thing after winning your little contest last night. You must have passed out."
            
            show kitsuragi at center with dissolve
            
            kitsuragi "Hello again [name]. I wish I could say it's nice to see you again, but the story your friends told me when they dragged you here has left me appalled by your stupidity."
            
            player "It was worth it."
            
            kitsuragi "I'm sure it was."
            kitsuragi "Anyway, you may be dying but you could at least try not to reduce your lifespan any further."
            
            player "How long am I gonna be stuck here this time?"
            
            kitsuragi "Now that you're awake you're free to go. I'm not gonna bother writing up a prescription but you can pick up some pills at the pharmacy. Just tell them I gave you the diagnosis 'butthurt.'"
            kitsuragi "Now get out of my hospital."
            
            hide kitsuragi with dissolve
            
            n "The kitsuragi leaves the room, leaving you to ponder your life decisions and muster the energy to get up, trying not to put undue stress on your abdomen on the way home."
            
            scene bg codadorm with fade
            
            play music "audio/music/vylet - リラックス.ogg" fadein 1.0
            
            show box with Dissolve(.2):
                ypos 0
            
            n "You collapse onto your bed as soon as you make it back to your dorm."
            n "Your phone buzzing is the only thing stopping you from falling back to sleep."
            
            call phone_start from _call_phone_start_52 

            call message_start("Ava", "Hey [name]! You doing alright?", "avaavi.png") from _call_message_start_69 
            call message("Ava", "Sorry we just kinda dumped you at the hospital :/", "avaavi.png") from _call_message_375 

            call reply_message("Yeah.") from _call_reply_message_279 
            call reply_message("wtf happened last night") from _call_reply_message_280

            call message("Ava", "You passed out literally as soon as you finished your bowl", "avaavi.png") from _call_message_376 
            call message("Ava", "But hey at least you won the contest!", "avaavi.png") from _call_message_377 
            
            call reply_message("Woo") from _call_reply_message_281
            call reply_message("My stomach will never be the same") from _call_reply_message_282

            call message("Ava", "RIP", "avaavi.png") from _call_message_378 
            call message("Ava", "I'm glad you're okay though", "avaavi.png") from _call_message_379 
            call message("Ava", "I was kinda rooting for you lol", "avaavi.png") from _call_message_380 
            
            call reply_message("Oh?") from _call_reply_message_283
            call reply_message("You didn't wanna sit in Gunner's lap?") from _call_reply_message_284
            
            if avaPoints >= 4:
                #untested
                #need to determine if points requirement is too high
                call message("Ava", "I'd rather sit in yours :P", "avaavi.png") from _call_message_381 
                
                call reply_message("It's free anytime") from _call_reply_message_285
                
                #call message("Ava", "Noted~", "avaavi.png") 
                #call message("Ava", "Maybe I'll swing by later to \'study\' OvO", "avaavi.png") 
                call message("Ava", "OvO", "avaavi.png") from _call_message_382 
                call message("Ava", "I've got a busy schedule but I'll try to squeeze you in~", "avaavi.png") from _call_message_383 
                
                call reply_message("Lookin forward to it UwU") from _call_reply_message_286
                
                call message("Ava", "Hehe same~", "avaavi.png") from _call_message_384 
                
                call phone_end from _call_phone_end_60         
                
                #call message("Ava", "Allow me to see what my consultant says", "avaavi.png") 
                
                #call message("Claire", "This is Ava's consultant.", "claireavi.png") 
                #call message("Claire", "As a result of unfortunately landing you in the hospital last night, I would like to offer you compensation in the form of a makeout session", "claireavi.png") 
                #call message("Claire", "administered by my client Ava Montblanc at a time of your choosing", "claireavi.png") 
                #call message("Claire", "you can also totally feel her up and stuff lol", "claireavi.png") 
                #call message("Claire", "no bra too", "claireavi.png") 
                
                #call message("Ava", "AAAA WHAT NO I DID NOT AGREE TO THIS", "avaavi.png") 
                
                #call message("Claire", "Too late, the offer's been sent :P", "claireavi.png") 
                
                #call screen phone_reply("Accept offer","avaaccept","Decline offer","avadecline")
                
                #label avaaccept:
                    #call phone_after_menu
                    
                    #call message_start("me", "Deal", "testimage.png") 
                    
                    #call message("Ava", "Oh my gosh Claire whyyyy ;-;", "avaavi.png") 
                    
                    #call message("Claire", "she's acting hard to get but i know she wants it :P", "claireavi.png") 
                    
                    #call reply_message("Claire's influence is truly limitless")
                    
                    #call message("Claire", "just wait until our next sleepover >:3", "claireavi.png") 
                    
                    #call message("Ava", "You guys are so lewd >.>", "avaavi.png") 
                    
                    #call message("Claire", "i am literally handing you a once in a lifetime opportunity to get with a human on a silver platter", "claireavi.png") 
                    #call message("Claire", "you should be more thankful", "claireavi.png") 
                    
                    #call message("Ava", "Hmph!", "avaavi.png") 
                    
                    #call message("Ava", "Hey WTF!", "avaavi.png") 
                    
                    #call message("Claire", "I just put a lock on her underwear drawer", "claireavi.png") 
                    #call message("Claire", "no bra for you until you uphold your end of the deal with [name]!", "claireavi.png") 
                    
                    #call message("Ava", "My panties were in there too!", "avaavi.png") 
                    
                    #call message("Claire", "I guess that sweetens the deal even more :P", "claireavi.png") 
                    
                    #call reply_message("")
                    #ava says she was planning on hanging out with gunner today, player can come with if they want. she says if you play your cards right you'll get your prize
                    #player teases she better hope that thin shirt of hers doesn't get wet, it's supposed to rain tomorrow
                    
                    
                    #grind session at party
                    #negotiating my bird butt
                    
                    #may i spank it
                    
                    #once
                    
                    #good deal

                    #call phone_end
                
                #label avadecline:
                    #$ avaPoints += 1
                    #call phone_after_menu
                    
                    #call message_start("me", "Nah don't worry about it", "testimage.png") 
                    
                    #call message("Claire", "are you sure? i know she's playin hard to get but she's thiiiis close to doin it", "claireavi.png") 
                    
                    #call message("Ava", "I am not!", "avaavi.png") 
                    
                    #call reply_message("Yeah it's fine. I just wanted the glory of beating Gunner last night.")
                    
                    #call message("Claire", "awwww so humble <3", "claireavi.png") 
                    #call message("Claire", "well if you change your mind, I'll be your consolation prize~", "claireavi.png") 
                    
                    #call message("Ava", "Hrmph!", "avaavi.png") 
                    #call message("Ava", "And I guesssss I can give you a smooch on the cheek or something", "avaavi.png") 
                    
                    #call message("Claire", "See! I told you she'd come around! Just needed some jealousy as motivation~", "claireavi.png") 
                    
                    #call reply_message("you're too kind, both of you~")
                    
                    #call message("Claire", "That reminds me!", "claireavi.png") 
                    #call message("Claire", "I'm going fishing with that ram boi if you wanna come~", "claireavi.png") 
                    
                    #call reply_message("Wow, you're really pushing him to get outdoors more huh")
                    #call reply_message("Around what time? I'm feeling kinda beat today")
                    
                    #call message("Claire", "We can go tomorrow but it's gotta be bright and early!", "claireavi.png") 
                    
                    #call reply_message("You coming, Ava?")
                    
                    #call message("Ava", "I would but I already made plans with Gunner", "avaavi.png") 
                    #call message("Ava", "We're going urban exploring again, this time at the old train station", "avaavi.png") 
                    
                    #call screen phone_reply("Go fishing","claireaccept","Ask to join Ava","clairedecline")
                    
                    #label claireaccept:
                        #$ clairePoints += 1
                        #$ roriPoints += 1
                        #call phone_after_menu
                        
                        #call message_start("me", "Ah damn enjoy your adventure. Watch out for hobos.", "testimage.png") 
                        #call reply_message("I'm gonna catch a big fish with Claire and Rori lol")
                        
                        
                    
                    
                    
                    
                    
                    #move the talk about fishing trip/urbex to sunday morning
                    
                    
                    
                
                    #label clairedecline:
                        #$ avaPoints += 1
                        #call phone_after_menu
                        
                        #call reply_message("Is this an Ava x Gunner exclusive or do you have room for one more?")
                        
                        #call message("Ava", "I was hoping you'd ask to join~", "avaavi.png") 
                        #call message("Ava", "As much as I like Gunner, he's kinda.... ", "avaavi.png") 
                        #call message("Ava", "Uhhhh", "avaavi.png") 
                        #call message("Ava", "Well you know how he is", "avaavi.png") 
                        
                        #call reply_message("I get what you mean")
                        
                        #call message("Claire", "I sense a love triangle~", "claireavi.png") 
                        #call message("Claire", "Or perhaps a love quadrilateral if I'm involved idk if I am or not", "claireavi.png") 
                        
                        #call message("Ava", "Shush, the adults are talking", "avaavi.png") 
                        
                        #call message("Claire", "Don't silence me!", "claireavi.png") 
                        #call message("Claire", "Like it or not, you'll have to choose one way or another eventually!", "claireavi.png") 
                        #call message("Claire", "Or a three way if you're so inclined uwu", "claireavi.png") 
                        
                        #call message("Ava", "Blocked", "avaavi.png") 
                        
                        #call message("Claire", "Hey! Rude!", "claireavi.png") 
                        #call message("Claire", "[name] call Ava a whore for me, thx", "claireavi.png") 
                        
                        #you live in the same room, you do it
                        
                        #claire "oh yeah"
                        #claire "Ow! She threw a textbook at me"
                        #claire "And now she's trying to strangle me with a bra"
                        
                        #n "god you wish you could see that"
                        #call reply_message("Claire says you're a slut, Ava")
                        
                        #call message("Ava", "Well it takes one to know one!", "avaavi.png") 
                        
                        #call phone_end
            else:
                #finished
                call message("Ava", "I was leaving it to chance really", "avaavi.png") from _call_message_385 
                call message("Ava", "Or rather, whoever was most determined", "avaavi.png") from _call_message_386 
                call message("Ava", "Which ended up being you! ^v^~", "avaavi.png") from _call_message_387 
                
                call reply_message("Cool so where's my lapdance?") from _call_reply_message_287
                
                call message("Ava", "Hey, I only said I'd sit in the victor's lap!", "avaavi.png") from _call_message_388 
                
                call reply_message("And yet my lap remains empty") from _call_reply_message_288    
                
                call message("Ava", "Can we continue this conversation later? Something just came up.", "avaavi.png") from _call_message_389 
                
                call reply_message("fffffine but don't think i'll just forget about it!") from _call_reply_message_289    
                
                call message("Ava", "Of course not~ I'm excited to see where this goes myself~", "avaavi.png") from _call_message_390 
            
                call phone_end from _call_phone_end_61
                
            #n "That's enough texting for today."
            n "It's a beautiful day out but your stomach still hurts from yesterday, so you resign yourself to catching up on some classwork between watching videos online."
                    
        "Concede":
            #untested
            n "It would be wise to admit defeat. There's no point in hurting yourself over this."
            
            player "No more. I can't go any further."
            
            n "You sit there, brain fried from the traumatic spices, suckling on an ice cube as Gunner finishes his bowl and claims victory."
            
            show ava casual overjoyed
            
            gunner @ say "THROUGH THE FIRE AND FLAMES, I EMERGE VICTORIOUS! *inhale* AAAAAAAAAAAAAAAAAAA"
            
            n "He sits panting for a while before trying to take a sip of water."
            
            gunner @ say "EVEN THE WATER BURNS!!!"
            
            show ava casual happy
            
            ava @ say "You alright, big guy?"
            
            gunner @ say "No"
            gunner @ say "I need"
            gunner @ say "I need your avian ass right here on my lap cause I just owned [name] and brought glory to all of catkind."
            
            show ava casual daydream
            
            n "Ava stifles a giggle."
            
            ava @ say "Oh pft. Fine. I said I would, and I guess you do kinda deserve it."
            
            show ava:
                xpos -150
            with move
            
            pause .1
            
            show ava casual concerned
            
            n "Ava stands up and walks over, visibly hesitant, but a thumbs up from Claire is enough to convince her to go with it."
            
            show ava casual flattered at flipright
            
            n "She pushes out her rear, flaunting her tail feathers and sits down on Gunner's lap."
            n "She lets out a surprised chirp as he grabs her by the waist and pulls her closer."
            n "Feels bad man."
            
            show claire outdoors lusty
            
            claire @ say "Alright, your turn [name]!"
            
            player "Wha"
            
            n "You were too busy chugging water and sulking to notice Claire's giant ass looming over you."
            n "You have no time to prepare as it comes crashing down, making the seat you're sitting in groan and creak as 300 pounds of bunny crushes your legs."
            n "You can't even see over her when she leans back and settles in."
            
            player "This is fine."
            
            n "However, even being pinned between an uncomfortable chair and a BBW (big beautiful waifu) is nothing compared to the smoldering spice lingering in your mouth."
            n "You probably made the right choice in not continuing, even if you do have to pay for the meal now."
            
            show ava casual smile
            
            ava @ say "You comfy, Claire?"
            
            show claire outdoors embarassed
            
            claire @ say "Yup! Ksksksks!"
            
            show ava casual overjoyed
            
            ava @ say "Same~"
            ava @ say "*Chirp*~"
            
            show claire outdoors neutral
            
            claire @ say "I just feel bad cause now Rori's left out!"
            
            rori @ say "O-oh that's quite alright..! I wouldn't want to uh, steal the glory from [name] so you can stay over there with [himher]."
            
            n "You catch a glance at Gunner. The bastard shoots you a smug grin and wraps his arms around the bird sitting in his lap."
            n "Fuck, why did you even suggest this silly contest in the first place?"
            
            show ava casual happy
            
            ava @ say "Mind if I try a bite, [name]?"
            
            player "Wha? Are you sure? I'm literally dying over here."
            
            show ava casual smile
            
            ava @ say "I'm sure I'll be fine~"
            
            n "Ava reacher over with her fork and takes a stab at your red hot molten lava in a bowl."
            n "You watch in horror as she takes a big bite and swallows it."
            
            show ava casual daydream
            
            ava @ say "Hmm. Kinda bland if you ask me."
            
            gunner @ say "Whoaaaa!!! How can you eat something like that so casually?"
            
            show ava casual smile
            
            ava @ say "Hehe~ It's a secret~"
            
            rori @ say "Ohh I think I know! I read that birds don't have receptors for capsaicin, the thing that makes things spicy."
            
            show ava casual overjoyed
            
            ava @ say "Breeee~ Ya got me! It was fun watching you guys suffer from something so mild!"
            
            show ava casual happy
            
            n "Ava pulls your bowl closer to her and continues eating it like it's nothing."
            
            ###if you had ava sit by you during the movie night, comment on how he's getting his revenge
            
            n "The night goes on and eventually Claire gives you a break when you all decide to head back home."
            n "Ava and Gunner sure seemed to have a good time, and even though Rori was maidenless he still seemed to enjoy spending time with everyone."
            n "Even you had a few laughs once you no longer felt like death was preferable to your situation."
            n "Still, losing the contest kinda bummed you out more than expected."
            
            stop music fadeout 1.0
        
            scene bg black with fade

            hide box

            show bg calendar
            show tfriday at center
            with Dissolve(.5)

            pause .6
            show tforwardslash
            pause .2
            show tbackslash

            pause .7
            
            scene bg codadorm with fade
            
            n "You wake up feeling dizzy, almost kinda hungover."
            n "Your poor intestines are still groaning in pain even after you made several trips to the bathroom."
            n "Last night was not worth the trouble, just to lose."
            
            call phone_start from _call_phone_start_53 

            call message_start("Ava", "Hey [name]! You doing alright?", "avaavi.png") from _call_message_start_70 
            call message("Ava", "Thought I'd check in on you", "avaavi.png") from _call_message_391 

            call reply_message("Yeah, jsut hating every moment of existence.") from _call_reply_message_290 
            
            call message("Ava", "Oof, sorry about last night", "avaavi.png") from _call_message_392 
            call message("Ava", "I thought for sure you'd win!", "avaavi.png") from _call_message_393 
            
            call reply_message("Really? I guess we both underestimated Gunner") from _call_reply_message_291 
            
            call message("Ava", "He's pretty determined, you gotta give him that!", "avaavi.png") from _call_message_394 
            call message("Ava", "Better luck next time~", "avaavi.png") from _call_message_395 
            
            call reply_message("yeah lol") from _call_reply_message_292 
            
            call phone_end from _call_phone_end_62
            
            n "You're getting pretty tired of this love triangle bullshit. Sooner or later she's gonna have to pick a side."
            n "It's a beautiful day out but your stomach still hurts from yesterday, so you resign yourself to catching up on some classwork between watching videos online."
            
    

    #you're not serious are you?
    #maybe I am~
    
    
    scene bg black with fade
    

    #___saturday7
    
    #get texts from friends talking about last night
    #if you didn't go to hospital, do something with mishka/rose/ellen. too exhausted to do anything today

    #___sunday7
    #fishing with rori and claire or urbex with gunner and ava

    #___monday7

    #___tuesday7

    #___wednesday7
label history_reenactment:
    #finished (more or less. needs adjustments if the player studied this history chapter earlier (in the hospital I think?))
    #reenact a scene from history with rose

    scene bg classroom with fade

    play music "audio/music/mere - schooldaze.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0    
    n "A few days later..."

    show rothbauer at center with dissolve

    rothbauer @ say "Good morning class!"
    rothbauer @ say "I don't want to run out of time like last class so we'll get right into group B's presentation today."

    n "Several students around you get up and walk to the front of the classroom."

    show rose furious at center with dissolve:
        xpos -500
        xzoom -1

    rose @ say "That's us! Get up you idiot!"

    player "Huh? I don't remember a presentation due today..."

    hide rose with dissolve

    n "You better not piss Rose off any more than you already have. You walk up with everyone else, utterly clueless as to what you're doing."

    rothbauer @ say "You may begin as soon as you're ready!"

    hide rothbauer with dissolve

    n "Thankfully one of your classmates begins. Apparently you're doing some sort of reenactment of a period in history."
    n "Only thing is, you have no idea what part of history you're supposed to be in."
    n "All you know is that you're a human in a strange land and your execution is scheduled for right now o'clock."

    show rose neutral at center with dissolve

    rose @ say "You, ambassador for the humans from far beyond the great sea, have poisoned our water, burned our crops, murdered our people and stolen our knowledge!"
    rose @ say "For your crimes against the Arcoonia tribe, you shall be sentenced to death."
    rose @ say "Any last words, vile creature?"

    menu:
        rose "{cps=0}Any last words, vile creature?{/cps}" 
        "Can we talk this over a cup of tea?":
            player "Can we talk this over a cup of tea?"

            rose @ say "Wha-?"
            
            show rose angry
            
            rose @ say "Stick to the script, idiot!"

            n "Rose hesitates before pretending to bring down a wooden play sword over your neck, killing you instantly."
        "I regret nothing!":
            player "I regret nothing!"
            
            show rose angry
            
            rose @ say "I'll drink from your skull!"

            n "Rose stares daggers at you and pretends to bring down a wooden play sword over your neck, killing you instantly."
        "It was worth it!":
            player "It was worth it!"
            
            rose @ say "Wha-?"
            
            show rose angry
            
            rose @ say "Stick to the script, idiot!"

            #n "Rose looks at you with a bit of confusion and irritation before pretending to bring down a wooden play sword over your neck, killing you instantly."
            n "Rose pretends to bring down a wooden play sword over your neck, killing you instantly."

    hide rose with dissolve

    n "That's your version of how this particular moment in history went down, at least."
    n "You don't know, you didn't read this chapter."
    n "The rest of the class awkwardly claps as you and your group take a bow and returns to their seats."

    show rothbauer at center with dissolve

    rothbauer @ say "Very good! I'm not sure as to the historical accuracy of the ambassador's final words, but I'm quite pleased with how this little presentation turned out!"
    rothbauer @ say "Indeed, when European settlers arrived in America, the existing societal structure was shaken up."
    rothbauer @ say "Animals like the Arcoonians that were once worshipped were conquered and enslaved for centuries."
    rothbauer @ say "Rather than have their knowledge turned against them, the Arcoonians opted to destroy their advanced technology and blueprints."
    rothbauer @ say "Which is truly a shame. Centuries of knowledge, scientific progress and art was lost. Some sources say this loss was more impactful than the burning of the Library of Alexandria."
    rothbauer @ say "Ah, but we'll have to talk more about that later. I'll see you all next class!"

    stop music fadeout .9

    #___thursday7

    #___friday7
label main_date:

    hide box

    scene bg black with fade

    hide box

    show bg calendar
    show tthursday at center
    with Dissolve(.5)

    pause .6
    show tforwardslash
    pause .2
    show tbackslash

    pause .7

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    n "The next few days pass by relatively uneventfully until Friday evening rolls around."
    n "Classwork has been pretty effective in keeping your mind off your illness, and you've started helping Gunner study more just to spend more time with him and Rori."
    n "Same thing with Claire, but she's the one helping you study in that case."
    n "*buzz buzz*"
    n "Your heart skips a beat every time you hear your phone go off."
    n "You never got so many texts before coming here so it's kind of a nice surprise."
    n "You finally feel like you're getting your money's worth out of your phone plan."
    #n "clairepoints is [clairePoints]"

    # get texts from date candidate/gunner
    #n "The rest of the day goes by uneventfully until that night when you get a text."
    
    if roriPoints >= 3:
        $ roripath = True
        
    if avaPoints >= 5:
        $ avapath = True

    if clairePoints >= 4:
        $ clairepath = True
    if claireBias == True and clairePoints < 4:
        $ clairePath = True

    if clairepath == True:
        if claireBias == True:
            #modify scene where the player can't reject claire
                        
            $ dating = "claire"
            
            call phone_start from _call_phone_start_54 

            call message_start("Claire", "Heyyyy c:", "claireavi.png") from _call_message_start_71 

            call reply_message("What's up?") from _call_reply_message_293 

            call message("Claire", "So I was thinking....", "claireavi.png") from _call_message_396 

            call reply_message("?") from _call_reply_message_294 

            call message("Claire", "You and I should go out sometime!", "claireavi.png") from _call_message_397 
            call message("Claire", "Like just us", "claireavi.png") from _call_message_398 

            call reply_message("Like a date?") from _call_reply_message_295 

            call message("Claire", "I mean, if you want it to be ;3", "claireavi.png") from _call_message_399 

            call reply_message("Heck yeah, I was waiting for you to ask me out!") from _call_reply_message_296 
            
            call message("Claire", "OMG RLY??!", "claireavi.png") from _call_message_400 
            call message("Claire", "Meet me tomorrow at noon at the quad", "claireavi.png") from _call_message_401 
            call message("Claire", "And bring your swimsuit~", "claireavi.png") from _call_message_402 
            
            call reply_message("Can't wait!") from _call_reply_message_297 

            call phone_end from _call_phone_end_63 

            jump saturday8
            

        else:
            call phone_start from _call_phone_start_16

            call message_start("Claire", "Heyyyy c:", "claireavi.png") from _call_message_start_20

            call reply_message("What's up?") from _call_reply_message_104

            call message("Claire", "So I was thinking....", "claireavi.png") from _call_message_137

            call reply_message("?") from _call_reply_message_105

            call message("Claire", "You and I should go out sometime!", "claireavi.png") from _call_message_138
            call message("Claire", "Like just us", "claireavi.png") from _call_message_139

            call reply_message("Like a date?") from _call_reply_message_106

            call message("Claire", "I mean, if you want it to be ;3", "claireavi.png") from _call_message_140

            call screen phone_reply("Sure!","clairedateaccept","Umm...","clairedatereject")

            label clairedateaccept:
                $ dating = "claire"
                call phone_after_menu from _call_phone_after_menu_4

                call message_start("me", "Sure! That sounds great!", "testimage.png") from _call_message_start_21

                call message("Claire", "OMG yeeeeee", "claireavi.png") from _call_message_141
                call message("Claire", "Meet me tomorrow at noon at the quad", "claireavi.png") from _call_message_142
                call message("Claire", "And bring your swimsuit~", "claireavi.png") from _call_message_143

                call reply_message("Can't wait!") from _call_reply_message_107

                call phone_end from _call_phone_end_17

                jump saturday8

            label clairedatereject:
                $ clairepath = False
                call phone_after_menu from _call_phone_after_menu_5

                call message_start("me", "Umm... Maybe another time", "testimage.png") from _call_message_start_22

                call message("Claire", "Oh", "claireavi.png") from _call_message_144
                call message("Claire", "Ok yeah", "claireavi.png") from _call_message_145
                call message("Claire", "I'll just uh talk to you later I guess", "claireavi.png") from _call_message_146

                call phone_end from _call_phone_end_18


    if avapath == True:
        call phone_start from _call_phone_start_55 
        ###change this to her simply inviting you to go shooting with her. maybe skip ahead to developing her film photos

        #call message_start("Ava", "Hey [name] I was wondering if you wanted to come with me to this party thing on the literature building roof", "avaavi.png") from _call_message_start_23
        call message_start("Ava", "Hey [name] I was wondering if you wanted to come shooting with me tomorrow! ^v^", "avaavi.png") from _call_message_start_72 
        #call message("Ava", "Just you and me", "avaavi.png") 

        #call reply_message("Oh the thing gunner goes to") from _call_reply_message_108
        call reply_message("Just you and me?") from _call_reply_message_298 
        
        call message("Ava", "Yup!", "avaavi.png") from _call_message_403 

        #call message("Ava", "?", "avaavi.png") from _call_message_147
        #call message("Ava", "How'd you know?", "avaavi.png") from _call_message_148
        
        #call reply_message("He invited me to one before") 
        #call reply_message("Weird that he didn't invite me this time") 
        
        #call message("Ava", "huh", "avaavi.png") 
        #call message("Ava", "Well I just wanted to see if you'd come along wiht me", "avaavi.png") 
        #call message("Ava", "We can dance and stuff", "avaavi.png") 
        #call message("Ava", "there will be beer if you're into that", "avaavi.png") 
        
        call screen phone_reply("Sure!","avadateaccept","Hmm...","avadatereject")

        label avadateaccept:
            $ dating = "ava"
            call phone_after_menu from _call_phone_after_menu_18 

            call message_start("me", "Sure! Where and when?", "testimage.png") from _call_message_start_73 

            call message("Ava", "I was thinking I'd meet with you right after class", "avaavi.png") from _call_message_404 
            
            call reply_message("Works for me lol") from _call_reply_message_299 
            
            call message("Ava", "Yay!~ I promise it's gonna be a lot of fun OvO", "avaavi.png") from _call_message_405 

            call reply_message("Cant wait!") from _call_reply_message_300 

            call phone_end from _call_phone_end_64 

            jump saturday8

        label avadatereject:
            $ avapath = False

            call phone_after_menu from _call_phone_after_menu_7

            call message_start("me", "Hmm... idk I'm not feelin it today sorry", "testimage.png") from _call_message_start_74 

            call message("Ava", "Oh... That's fine, just thought I'd offer", "avaavi.png") from _call_message_406 

            call phone_end from _call_phone_end_20

    if roripath == True:
        call phone_start from _call_phone_start_18

        call message_start("Rori", "Hey [name]", "roriavi.png") from _call_message_start_26

        call reply_message("What's up?") from _call_reply_message_111

        call message("Rori", "I was just wondering...", "roriavi.png") from _call_message_151
        call message("Rori", "If you'd maybe want to come over and play some video gaems or something sometime", "roriavi.png") from _call_message_152

        call screen phone_reply("Sure!","roridateaccept","Err...","roridatereject")

        label roridateaccept:
            $ dating = "rori"
            call phone_after_menu from _call_phone_after_menu_8

            call message_start("me", "Sure! Did you have a time in mind?", "testimage.png") from _call_message_start_27

            call message("Rori", "Awesome! Anytime tomorrow's good! Swing by my dorm whenever you feel like it ^^", "roriavi.png") from _call_message_155

            call phone_end from _call_phone_end_21

            jump saturday8
        label roridatereject:
            $ roripath = False

            call phone_after_menu from _call_phone_after_menu_9

            call message_start("me", "Err... I'm kinda busy", "testimage.png") from _call_message_start_28

            call message("Rori", "Aw... that's alright", "roriavi.png") from _call_message_156
            call message("Rori", "Just thought I'd offer", "roriavi.png") from _call_message_157

            call reply_message("Appreciate it") from _call_reply_message_112

            call phone_end from _call_phone_end_22

            jump saturday8

    call phone_start from _call_phone_start_19

    call message_start("Gunner", "Sup [name]", "gunneravi.png") from _call_message_start_29

    call reply_message("Yo") from _call_reply_message_113

    call message("Gunner", "You doing anything tomorrow?", "gunneravi.png") from _call_message_158

    call reply_message("Nope") from _call_reply_message_114
    call reply_message("Why?") from _call_reply_message_115

    call message("Gunner", "Great so you're free to be our goalie then!", "gunneravi.png") from _call_message_159

    call reply_message("Your what?") from _call_reply_message_116

    call message("Gunner", "Soccer", "gunneravi.png") from _call_message_160

    call reply_message("Oh sports") from _call_reply_message_117

    call message("Gunner", "Yeah sports", "gunneravi.png") from _call_message_161

    call reply_message("ok fine") from _call_reply_message_118

    call message("Gunner", "Sweet! Thanks1", "gunneravi.png") from _call_message_162
    call message("Gunner", "We'll be at the field by the running track at like 2", "gunneravi.png") from _call_message_163

    call phone_end from _call_phone_end_23

    jump saturday8

label saturday8:

    # saturday8

    # at this point, the player is either locked into ava, claire or rori's path or they are eligable for rose, ellen's or mishka's path. Mishka's path is only available if the player declines rose and ellen

    scene bg campus with fade

    show box with Dissolve(.2):
        ypos 0
    
    play music "audio/music/vylet - there.ogg" 

    n "It's a bright and sunny day today. Puddles from last night's storm are strewn about and the air is heavy with humidity."

    if dating == "rori":
        n "You better let Rori know you're on your way."

        call phone_start from _call_phone_start_20

        call message_start("me", "Hey I'm heading over there now", "testimage.png") from _call_message_start_30

        call message("Rori", "Cool! I'm just finishing getting things set up over here. Should be done by the time you get here!", "roriavi.png") from _call_message_164

        call reply_message("Aight I'll be there in like 10 minutes") from _call_reply_message_119

        call phone_end from _call_phone_end_24

        n "A short walk later you find yourself at Rori's dorm building."
        n "Gunner just happens to be walking out the door as you're about to head inside."

        show gunner neutral at center with dissolve

        gunner @ say "Sup [name]. Where you goin'?"

        player "Gonna play some vidya with Rori."

        gunner @ say "Oh yeah, he mentioned something like that. I can't really stand staying inside for too long so I'm going out to kick some balls."

        n "He gestures to the soccer ball under his foot."

        player "I'm more into pressing buttons and melting my eyes in the glow of a TV screen in a dark room."

        gunner @ say "Haha have fun with that. I'll stay out late so you and Rori can have some time alone together ahahaha!"

        n "You laugh along with him but you might actually end up being thankful for that depending on how things go."
        n "As you wave goodbye to Gunner and head inside you wonder if Rori really just wants to hang out or if there's something more to it."

        stop music fadeout 1.3

        scene bg roridorm with fade

        play music "audio/music/vylet - wish.ogg"

        show box with Dissolve(.2):
            ypos 0

        show rori neutral at center with dissolve

        rori @ say "Hey [name]! Come on in! I just got my computer hooked up to the TV and all the emulators configured."
        rori @ say "We can play pretty much any game you want!"

        n "You plop down in a bean bag chair and grab a controller."

        player "Sounds good. Wanna smash?"

        show rori anxious

        rori @ say "Wh-what?"

        player "You have Super Smash Sisters on here don't you?"

        show rori laugh

        rori @ say "Oh... Oh right! Yeah haha!"
        
        show rori neutral

        n "He goes over to the computer and loads up the game."

        rori @ say "Do you mind setting up a match? I gotta take care of something real quick."

        player "Sure, no problem."

        show rori neutral at offscreenleft with move:
            yalign 0

        n "You set up the rules and choose your character while Rori steps out of view."
        n "He returns a minute later and sits in his epic gamer chair with a fight stick on his lap."

        show rori neutral at center with move:
            xzoom -1
            xpos 1800

        #rori @ say "Alright, ready to get your ass kicked?"

        player "Hahaha a fight stick? Really?"
        
        rori @ say "Yeah, I go to tournaments and stuff. Wanted to have good competing gear."
        
        player "Well go easy on me, I'm not a pro gamer I don't even have a rainbow keyboard."

        show rori laugh

        rori @ say "Don't worry, my reflexes are gonna be slow tonight! Heh!"

        player "Why's that?"

        show rori neutral
        
        n "Rori turns to you and pulls a bottle of whiskey out from his hoodie."

        rori @ say "I've already been sipping on this. Just a little something to calm the nerves, you know?"

        player "Woah nice. Can't you get in huge trouble for bringing that into the dorms though? Especially since you're underaged?"

        n "Rori hiccups."

        show rori drunk with dissolve

        rori @ say "I guess we better get rid of the evidence then, huh?~"

        n "He grabs the bottle and holds it out for you to take."

        menu:
            n "{cps=0}He grabs the bottle and holds it out for you to take.{/cps=0}"
            "Take a swig":
                n "Hell yeah."
                n "You grab of the bottle and take a swig. The potent whiskey burns your throat and fills your stomach with warmth. The odor is enough to make you wince, let alone the taste."

                player "Gah!"

                rori @ say "Hahahaha that was my same reaction my first time too!"

                player "Aw shuddup and hit start!"

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

                        show gunner neutral at center with moveinright:
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
                                    ypos 0

                                #monday4

                                n "After that it's hard to recall specific details, but you remember it was a fun night."
                                n "You woke up in his bed with him in your arms, enjoying the snuggles while you wait for him to wake up."

                                show rori pantsless at center with dissolve

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
                                    ypos 0

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
                                    ypos 0

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

                        show gunner neutral at center with moveinright:
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
                                    ypos 0

                                #monday4

                                n "After that it's hard to recall specific details, but you remember it was a fun night."
                                n "You woke up in his bed with him in your arms, enjoying the snuggles while you wait for him to wake up."

                                show rori pantsless at center with dissolve

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
                                    ypos 0

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
                                    ypos 0

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

                        show gunner neutral at center with moveinright:
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
                                    ypos 0

                                #monday4

                                n "After that it's hard to recall specific details, but you remember it was a fun night."
                                n "You woke up in his bed with him in your arms, enjoying the snuggles while you wait for him to wake up."

                                show rori pantsless at center with dissolve

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
                                    ypos 0

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
                                    ypos 0

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

                        show gunner neutral at center with moveinright:
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
                                    ypos 0

                                #monday4

                                n "After that it's hard to recall specific details, but you remember it was a fun night."
                                n "You woke up in his bed with him in your arms, enjoying the snuggles while you wait for him to wake up."

                                show rori pantsless at center with dissolve

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
                                    ypos 0

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
                                    ypos 0

                                #monday4

                                n "After that it's hard to recall specific details, but you remember it was a fun night."
                                n "You woke up in his bed with him in your arms, enjoying the snuggles for a bit before slinking away to get dressed."
                                n "Fuuuuuck, why can't you find your underwear?"
                                if fratsoro == "soro":
                                    n "At least you locate your bra, hanging off the side of the bed from one of Rori's horns."
                                n "Whatever. You hastily put on your pants and tip toe toward the door."
                                n "You feel bad about ditching him but you weren't planning on staying the night really don't feel like staying any longer."

                                show rori pantsless at center with dissolve

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
                                    ypos 0

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


        # cant drink alcohol with pills? also forgot pills at home? Feel like utter shit for the next few days but rori takes care of you



    if dating == "ava":
        ###hospital scene 2
        ###if skipped first scene, ava mentions coming here with gunner before
        #n "You better let Ava know you're on your way."
        # ava explains history of abandoned hospital, tells some spooky rumors, she's shooting on film today, invites you to help her develop it in darkroom, can let her kiss you
        #choices: asks if you believe in supernatural (I always have my camera around in case I see a UFO or something haha),

        #call phone_start from _call_phone_start_29

        #call message_start("me", "Hey I'm heading to the party now", "testimage.png") from _call_message_start_39

        #call message("Ava", "Perfect! I'll meet you there!", "avaavi.png") from _call_message_218

        #call phone_end from _call_phone_end_33

        #stop music fadeout 1.3
        
        

        #n "You and Ava spent another hour or two looking around, snapping photos and exploring this dilapidated building until she runs out of film."
        #n "Ava flaps up to the second floor but you can't reach due to stairs being out"

        #ava @ say "Welp, I'm outta film. Wanna help me develop it?"
        
        #n "very unfinished. basically you hang out with ava at the party but leave early cause gunner is being a dick."
        
        
        #n "After the party..."
        
        show ava typical neutral at center with dissolve
        
        ava @ say "Whew! I think we got some great shots today!"
        
        player "Man, you do this like everyday? It's exhausting..."
        
        show ava excited
        
        ava @ say "Yup! I think it's fun! Breeee~"
        
        show ava typical neutral
        
        player "You gonna post some of your shots on pinsta tonight?"
        
        ava @ say "Actually, I was gonna develop the roll of film I finished off today."
        
        show ava overjoyed
        
        ava @ say "Hey if you wanna lend me a hand I'd be happy to show you how it's done!"
        
        n "You're not doing anything else today so you figure why not."
        
        player "Sure, lead the way."
        
        scene bg avadorm with fade
        
        show box with Dissolve(.2):
            ypos 0
        
        #play music "audio/exports/【Music】Over Equestria [ZFgFqPKimPc].opus"
        play music "audio/music/vylet - Takamine.ogg" fadein 1.0
        
        #n "After shooting with Ava, she invited you to her dorm to help develop her film shots."
        
        show ava typical neutral at center
        
        ava @ say "Okay so developing film at home is sort of a tricky process."
        ava @ say "We'll be submerging the film in chemical baths for a while without any light so I hope you're not afraid of the dark!"

        player "What, you mean like a darkroom?"
        
        show ava excited

        ava @ say "Exactly!"
        
        show ava typical neutral
        
        ava @ say "It has to be absolutely pitch black for this to work."
        ava @ say "I have the chemicals and stuff ready to go. We can draw the curtains and turn the lights off and go in the closet to develop these shots!"

        player "As long as you know what you're doing..."

        ava @ say "Don't worry, it's not as hard as it sounds!"
        ava @ say "Just need to heat up some water first to a precise temperature..."
        
        n "Ava flips a switch on an electric kettle. It begins to hiss as she flutters around the room, gathering jars of liquid."
        n "You do your part in darkening the room. She insisted there not be any light leaking inside."
        n "Ava lays out all the tools and materials on her desk and gives a brief overview of what you're doing."
        
        show ava at hop
        
        ava @ say "Alright, water's hot! You ready to start this?"
        
        player "I think so?"
        
        show ava motivated
        
        ava @ say "Then I'm turning out the lights in 3... 2... 1..."
        
        #change so it doesn't take place in the closet, is a mystery how claire got in, or she was here all along

        scene bg black with fade

        ava @ say "Alright, I'm gonna crack open the film now. No matter what, you can't let any light in or it'll ruin the shots."
        ava @ say "You know where everything is, right?"

        #player "Er, yeah. It's kinda cramped in here though..."
        player "Er, yeah. It's kinda hard to tell where I am though..."

        ava @ say "This should only take about 30 minutes."
        ava @ say "Hand me the can opener please."

        n "You grab the can opener and feel around for any feathers to get your bearing in the dark."

        ava @ say "Hey! Watch where you're poking that thing!"

        player "Sorry! I don't know which direction you're facing."

        ava @ say "*Huff*"
        ava @ say "I'm facing towards the desk."

        n "She snatches the tool and you can hear her peeling the lid off the film canister."
        
        ava @ say "There we go..."
        ava @ say "I'm putting it in the first chemical bath now."

        n "You hear a bit of splashing as she submerges the film."

        player "Okay... now what?"

        ava @ say "Now we wait for a couple minutes!"

        player "That's it?"

        ava @ say "Also have to stir the chemicals every 45 seconds."
        ava @ say "Like I said, it's not that hard. It's more monotonous than anything."

        player "Oh."

        n "You feel Ava's feathers brush up against you as you hear her stirring the chemicals."
        n "A few seconds go by then you hear Ava shuffling around."

        ava @ say "Here, you stir."

        n "She hands you a stick and guides you to the chemical tank, holding onto your arm to make sure you're at the right one."

        ava @ say "Yup, this is the one. Go ahead and stir it. Gently."

        n "Ava leans on you while you stir. The chemicals smell pretty awful and the room is starting to feel like a sauna after you stuffed a towel under the door to prevent light from coming in."
        n "It doesn't help that Ava is so close to you, warming you up even more."
        n "You spent the next few minutes making idle chit chat with Ava and stirring the tank until enough time has passed."

        ava @ say "That should be good. Scooch over, I need to transfer the film to the next tank."
        ava @ say "This one takes about twice as long as the other one."

        n "You move aside while Ava transfers the film and stirs the new tank."

        ava @ say "Having fun?"

        player "Err... yeah?"

        ava @ say "Haha like I said, it's pretty boring."
        
        n "Ava bumps into you and steps on your foot as she reaches over to the tank to stir."
        
        ava @ say "Oh, sorry!"
        
        player "It's fine."

        #n "Ava leans even closer to you. You can feel her beak nudging against your cheek."

        ava @ say "Know any ways to pass the time?~"

        player "Well I..."

        ava @ say "Hm? Yes?"

        n "I-is she coming onto you?!"
        n "That tone of voice, her brushing up against you, the fact she invited you into a dark cramped space alone like this..."

        menu:
            n "{cps=0}That tone of voice, her brushing up against you, the fact she invited you into a dark cramped space alone like this...{/cps}"
            "Kiss her.":
                n "Aw fuck it. You're 80 percent sure she wants you to kiss her."
                n "You wrap your arm around her and nuzzle her face, elliciting a small gasp from her."

                ava @ say "[name]~"

                n "You pull her in even closer and realize kissing a beak is just as hard as it sounds, moreso in the dark."
                n "Ava wraps her wings around you and helps you figure it out though."
                n "For the next several minutes, you softly kiss each other while she idly stirs the chemical tank from time to time."
                n "Suddenly she stops and pushes you away."

                ava @ say "Ahh, time out!!"
                ava @ say "I need to transfer the film!"

                n "You laugh to yourself as she turns and reaches over to handle the film."
                n "While she's busy moving the film while you stand behind her, her tail feathers tickling your face."
                #n "Thanks to the cramped space, you're now pressed between the wall and Ava's backside, her tail feathers tickling your face."
                n "In the non-existant visibility, your hands begin to wander, giving you a pretty good image of how she's positioned."
                n "She's bent over as she works on the film, cooing softly and grinding back against you as you feel her up."
                #n "This goes on for a while as she works with the chemicals."

                ava @ say "Ah~ [name]~ I-I think the f-film is good now."
                ava @ say "We can turn on the lights and see how it turned out!"

                n "You feel around for the lightswitch and turn on the lights."
                #n "Ava follows behind you with the film and turns on the lights."

                scene bg avadorm with fade

                #play music "audio/exports/01 - Takamine.opus" fadein 1.0
                #play music "audio/exports/04 - tenderness.opus" fadein 1.0

                show box with Dissolve(.2):
                    ypos 0

                show ava typical neutral at center with moveinleft:
                    xzoom -1

                ava @ say "Check it out! It turned out pretty good, I'd say!"

                n "She holds up the negatives in the light, showing the shots she took earlier."
                n "It's hard to make out all the details on such a small strip, and the colors are inverted but from what you can tell they look good."
                #n "It's hard to make out all the details on such a small strip but you can recognize some of the places from the hospital."

                player "Nice!"

                ava @ say "I'll scan and edit these later and send 'em to you~"
                
                show ava bored
                
                ava @ say "Unfortunately scanning is ten times more dull and frustrating than developing, so I won't make you sit through that."

                show ava with move:
                    xpos -200

                show claire sweater neutral at center with dissolve:
                    xpos 600

                claire @ say "Get any interesting shots, Ava?~"
                
                show ava portrait concerned

                ava @ say "Aaah! Claire!!! How long have you been here?!"

                claire @ say "Long enough to hear you and [name] having fun 'developing film'~"
                claire @ say "Next time don't forget to invite this bunny to join in~"
                
                show ava annoyed -portrait

                ava @ say "Oh pshh, like your fat butt could fit in the closet with me and [name]~"

                claire @ say "Don't forget my fat tits too~"
                
                show ava angry -portrait

                ava @ say "And your fat head~"

                claire @ say "Ksksksks! Don't talk bad about my head with that beak of yours~"

                ava @ say "Oh-"
                ava @ say "My gosh!"

                n "Ava and Claire continue teasing each other while you stand by awkwardly. You can feel yourself blushing which just makes you feel even more uncomfortable."
                n "It almost feels like they're fighting over you."
                n "But they're still doing it in a friendly way."

                claire @ say "Alright alright, you can enjoy your new [boygirlfriend]~"
                
                show claire lusty
                
                claire @ say "All I'm sayin' is you don't have to be alone together if ya get what I mean~"

                n "Claire looks over and winks at you."
                
                show ava waitwhat

                ava @ say "Oh my goshhh go to horny jail already Claire~"
                
                show claire embarassed

                n "The bunny pulls Ava into a side hug and smooches her on the side of her beak before whispering into her ear."

                claire @ say "I'll meet you there~"
                
                show ava smile
                show claire sweater derp

                n "Ava giggles and pushes her away so she can come lean on you."

                ava @ say "Ignore her, she puts the 'dummy' in 'dummy thicc~'"

                player "What the hell have I stumbled into I thought I was just gonna be helping shoot some photos today."
                
                show claire sweater neutral

                claire @ say "Well I guess you got more than you bargained for~"
                
                show ava flattered

                ava @ say "Oh shush you!"
                
                show ava typical neutral
                
                ava @ say "Anyway, it's getting kinda late so I'll see you tomorrow, k?"

                player "Sure~"

                n "Ava's feathers poof up and she gives you a parting kiss."
                n "As you leave the room you hear the two roommates resume their bickering."

                stop music fadeout 1.3

                scene bg codadorm with fade

                show box with Dissolve(.2):
                    ypos 0

                n "Whew, you made it back to your dorm without getting mauled by an aggressively horny rabbit or her protective secretary bird bestie."
                n "What a strange day."
                n "You're not sure what you did to deserve all that but hey at least you got a cute bird gf now."
                n "Speaking of which, it sounds like you just got a text from her."

                call phone_start from _call_phone_start_30

                call message_start("Ava", "Heyyyy I hope you had a good time today c:", "avaavi.png") from _call_message_start_40
                call message("Ava", "Even with Claire's weirdness haha", "avaavi.png") from _call_message_219

                call reply_message("Yeah today was great! I really enjoyed the part with the thing and the stuff") from _call_reply_message_176

                call message("Ava", "Hopefully we can finish what we started soon~", "avaavi.png") from _call_message_220

                call message("Claire", "Same", "claireavi.png") from _call_message_221

                call message("Ava", "OMG stop eavesdropping on my conversations claire!!!", "avaavi.png") from _call_message_222

                call message("Claire", "Ksksksks ilu <333", "claireavi.png") from _call_message_223

                call message("Ava", "Don't worry about her, she's harmless XvX", "avaavi.png") from _call_message_224

                call reply_message("We might have to find a more secluded place lol") from _call_reply_message_177

                call message("Ava", "Yeah, I'll come over to your dorm this weekend~", "avaavi.png") from _call_message_225

                call reply_message("Sounds good") from _call_reply_message_178

                call message("Ava", "<3 OvO", "avaavi.png") from _call_message_226

                call phone_end from _call_phone_end_34

                n "You plug your phone into its charger and turn in for the night, excited to wake up tomorrow and see Ava again."

                jump monday6
            "Don't kiss her.":
                #get a bad end point
                $ dating = ""
                n "Maybe it's all just in your head. You don't even want to kiss her."
                n "But... the way those feathers brush against your skin as she softly sighs..."
                n "Maybe it's the fumes from these chemicals clouding your mind but you suddenly have a strong urge to do something... risque."
                n "She gasps as you feel up her body, grinding back against you while soft chirps escape her beak."

                ava @ say "Nnh~ [name]... Keep going~"

                n "You happily oblige her, getting even more frisky until she remembers what you originally came here to do."

                ava @ say "Aack! The film!"
                ava @ say "I left it in that chem bath for too long!"

                n "She hurriedly begins transferring it into the next tank."

                ava @ say "B-but don't stop, I-I-I can fix this..."

                n "You shrug and continue what you were doing while she desperately stirs."
                n "The air in the room becomes hotter over the next several minutes while you and Ava get more intimate than you ever imagined."

                n "In the end you're both left panting messes and need a good long moment to recover."
                #n "Eventually you both put your clothes back on without a word."

                ava @ say "...The film should be ready now. We can turn on the lights."

                n "You turn on the dorm lights and Ava holds the film up to it."

                stop music fadeout 1.3

                scene bg avadorm with fade

                #play music "audio/ai12.ogg" fadein 1.0

                show box with Dissolve(.2):
                    ypos 0

                show ava concerned at center with dissolve:
                    xzoom -1

                ava @ say "Oh noooo! They turned out wayyyy too exposed from being in the second chem bath too long!"

                show ava with move:
                    xpos -200
                    
                show claire sweater cry at center with dissolve:
                    xpos 600

                claire @ say "Aww, sorry to hear that..."
                
                show claire sweater derp at center
                
                claire @ say "But at least you two still had fun by the sound of it~"
                
                show ava embarassed

                ava @ say "Aaah! Claire!!! How long have you been here?!"
                
                show claire embarassed

                claire @ say "Long enough to hear you and [name] having fun 'developing film'~"
                
                show claire lusty
                
                claire @ say "Next time don't forget to invite this bunny to join in~"
                
                show ava flattered

                ava @ say "Hah... was it that obvious?"
                
                show claire alert

                claire @ say "I could hear everything~"
                
                show claire neutral -alert
                
                claire @ say "So? How was it?~"

                n "Ava giggles and sticks her tongue out."
                
                show ava smile

                ava @ say "Better than you~"
                
                show claire surprised

                claire @ say "What?! I don't believe you!"
                
                show ava overjoyed

                ava @ say "It's true!"

                n "The bunny turns to you with a menacing grin."
                
                show claire sweater leaning

                claire @ say "Then show me~"

                n "You gulp and look to Ava for support but she's busy locking the door and unbuttoning her shirt."

                stop music fadeout 1.3

                scene bg codadorm with fade

                show box with Dissolve(.2):
                    ypos 0

                n "You got back to your dorm late last night so naturally you wake up tired."

                n "Seems you got a few text messages while you were out."

                call phone_start from _call_phone_start_31

                call message_start("Ava", "Heyyyy yesterday was pretty wild, huh <3", "avaavi.png") from _call_message_start_41
                call message("Claire", "it was just an ordinary weekend for me~", "claireavi.png") from _call_message_227

                call message("Ava", "omg shush up you slut~", "avaavi.png") from _call_message_228

                call message("Claire", "<3", "claireavi.png") from _call_message_229

                call message("Ava", "Anyway yeah all that was kinda spontaneous and unplanned...", "avaavi.png") from _call_message_230

                call message("Claire", "And *I'm* the slutty one?", "claireavi.png") from _call_message_231
                call message("Claire", "Ow!", "claireavi.png") from _call_message_232

                call message("Ava", "What I'm tryin to get at if this hoe will shut up", "avaavi.png") from _call_message_233
                call message("Ava", "Jk claire ilu <333", "avaavi.png") from _call_message_234

                call message("Claire", "C:", "claireavi.png") from _call_message_235

                call message("Ava", "Is like I had a lot of fun with you [name] but idk if I'm really feeling it with you", "avaavi.png") from _call_message_236
                call message("Ava", "you know", "avaavi.png") from _call_message_407 

                call reply_message("Oh") from _call_reply_message_179
                call reply_message("Yeah that's cool. I get it. I wasn't really interested in a relationship either. I just think you;'re hot") from _call_reply_message_180

                call message("Claire", "Same", "claireavi.png") from _call_message_237

                call message("Ava", "Cool, good to know we're on the same page then", "avaavi.png") from _call_message_238
                call message("Ava", "...And yeah if you ever wanna do what we did in the closet again just let me know~ <3", "avaavi.png") from _call_message_239

                call message("Claire", "Let me know as well~", "claireavi.png") from _call_message_240

                call reply_message("Lol ok") from _call_reply_message_181
                call reply_message("Does that apply to what we did on Claire's bed too?") from _call_reply_message_182

                call message("Claire", "Yes", "claireavi.png") from _call_message_241

                call message("Ava", "...Yes", "avaavi.png") from _call_message_242

                call phone_end from _call_phone_end_35

                n "Wow. Those two are really something."
                n "You thought as much of Claire but Ava's like that too?"
                n "That bunny must have corrupted her."

                scene bg codadorm with fade

                show box with Dissolve(.2):
                    ypos 0

                jump monday6


    if dating == "claire":
        #n "You better let Claire know you're on your way."

        #call phone_start from _call_phone_start_32

        #call message_start("me", "Hey I'm heading over now", "testimage.png") from _call_message_start_42

        #call message("Claire", "Perfect! I'll meet you there~", "claireavi.png") from _call_message_243

        #call phone_end from _call_phone_end_36

        #scene bg campus with fade

        #play music "audio/music/Evan Schaeffer - Encomium.ogg" fadein 1.0

        #show box with Dissolve(.2):
        #ypos 0

        claire @ say "[name]! Over here!"

        n "You turn your head and see Claire waving to you."

        show claire outdoors neutral at center with dissolve:
            xzoom -1

        claire @ say "Ready to go?"

        player "Go where exactly?"

        claire @ say "Ksksks you'll find out!"

        n "Claire takes your hand and guides you away from campus to a nearby trail through the woods."

        scene bg waterfall with fade
        
        play music "audio/music/vylet - Tranquility and Happiness.ogg" fadein 1.0

        show box with Dissolve(.2):
            ypos 0

        n "After a decent hike, you wind up at a pond at the base of a waterfall."

        show claire outdoors derp at center with dissolve

        claire @ say "Here we are!~"
        
        show claire outdoors neutral
        
        claire @ say "I heard it's a common dating spot around here so of course I just had to take you!"

        #n "You have to admit, it is some pretty scenery."
        player "It is pretty serene. And I could go for a dip in some cool water after that long ass hike."

        #player "Yeah, this is pretty nice. I was wondering where you were taking me haha."
        
        show claire outdoors lusty

        claire @ say "Ksksksks I was hoping you'd say that!"

        #n "Claire slips out of her cardigan and starts to lift her shirt over her head, revealing her swimsuit top underneath."
        
        show claire swimsuit flannel neutral
        
        n "Claire slips out of her flannel and starts to lift her shirt over her head, revealing her swimsuit top underneath."

        menu:
            n "{cps=0}Claire slips out of her flannel and starts to lift her shirt over her head, revealing her swimsuit top underneath.{/cps}"
            "Stare":
                #finished
                n "Your eyes gravitate toward her as she undresses, unable to look away."
                
                hide claire with dissolve
                
                n "She notices your staring and, with a smirk, she makes a show of sticking out her rear as she takes off her pants."

                show claire swimsuit leaning at center with dissolve

                claire @ say "Now it's your turn to get changed~"
                claire @ say "You did bring a swimsuit, yeah? Unless you were planning on skinny dipping ksksksks~"

                player "...Huh? Oh yeah, it's in my bag."
            "Look away as she undresses":
                #finished
                n "You feel the need to give her some privacy as she undresses, so you avert your gaze."
                
                hide claire with dissolve
                
                n "However, that only ellicits a giggle from the bunny."
                
                claire @ say "You can stare, you know~ I know you want to~"

                n "Well if she's inviting you to, it can't hurt to take a quick peek..."

                show claire swimsuit leaning at center with dissolve

                n "She strikes a pose as you look over to her."
                n "Sweet raptor jesus does she rock that swimsuit."

                claire @ say "Okay, your turn~"

        n "You dig your swimsuit out of your bag and change into it while Claire not-so-subtley watches."
        n "She's got a crazed look in her eyes, like a feral wolf hungrily watching an unguarded lamb out in the open."
        n "It's a good thing you're into that, otherwise you'd feel really uncomfortable right now."
        
        show claire swimsuit neutral

        claire @ say "Alright! Ready to get wet?~"

        n "Claire grabs your hand and takes you to the edge of the pool where she starts stepping in without hesitation."
        n "You however tense up as your foot touches the water."

        claire @ say "Hm? What's the matter?"

        player "Ah! N-nothing, the water's just really cold..."

        n "Claire giggles and drags you deeper into the water."
        
        claire @ say "You'll get used to it~"

        n "You're powerless to escape from her death grip as she pulls you further in."
        n "In retaliation, you playfully splash some water at her. She covers her face with her arm."
        n "When she lowers it, she has a sinister look on her face."
        
        show claire swimsuit lusty

        #player "Hah! Not so floofy anymore, now are ya?"
        player "Oh no..."

        n "Claire releases her hold on you and uses both her paws to rapidly strike the surface of the pond, pelting you with water droplets."
        #n "Claire winds up her paw and shoves a deluge of water in your direction, utterly soaking you."

        player "Aaaah! You're gonna pay for that!"

        claire @ say "Ksksksks catch me if you can!~"

        n "Even though it's cold enough to make you shiver, you give chase to Claire as she retreats further into the pool."
        n "She attacks with more splashes until you catch up to her and tackle her, bringing you both down under the water."        
        n "You both emerge completely soaked and laughing hysterically."
        
        show claire swimsuit heyeah

        claire @ say "Okay okay! Truce?~"

        player "Hahaha sure, for now~"
        
        show claire swimsuit neutral

        n "Claire wades over to you and nuzzles your cheek."
        n "You hold her close and look into her eyes."
        n "Her stunning eyes."
        n "That look she's giving you... You can't recall a time someone has looked at you like this."
        n "Those adorable puppy-dog eyes... err, rabbit eyes, combined with that genuine smile... Just makes you want to kiss her."
        
        if claireBias == True:
            #finished
            n "Ever so slowly, you lean in closer to her and she mirrors your movement."
            n "Time seems to slip away as you close your eyes and gently press your lips against hers."
            n "She's surprisingly tender with you, caressing you in a way that gives you goosebumps and melts your heart."
            n "The way she looks at you after your first kiss is the most reassuring look you've seen in your life."
            
            show claire swimsuit lusty

            claire @ say "[name]..."
            
            show claire swimsuit surprised

            n "You're about to lean in for another kiss when Claire's ears perk up."

            claire @ say "Dammit, somebody's coming. A bunch of frat bros and their dumb hoes judging by the sound of it..."

            n "You don't hear a thing but then again, you don't have massive ears."
            
            show claire swimsuit leaning

            claire @ say "Come on, I know somewhere we can have a little privacy~"

            n "Claire guides you to the waterfall and she disappears behind it."
            n "Really? A hidden cave behind the waterfall? What, is there a treasure chest back there too?"

            scene bg black with dissolve

            n "You pass through the waterfall and can hardly see anything in the darkness. Almost immediately you get pounced on by Claire."
            n "She pins you to the wall and begins assaulting you with kisses and little nibbles."

            player "A-ah, Claire~"

            claire @ say "Hehe, don't be afraid to make some noise~ The waterfall will cover it up~"

            n "Pleasured gasps escape your lips as she toys with you. Her paws guide your hands, placing them on something extraordinarily soft."

            claire @ say "Go ahead and play with 'em~ I know you've been wanting to~"

            n "Your eyes go wide as you realize you don't feel a swimsuit anywhere on her body."
            n "You're rewarded with soft nuzzles and cute moans as you explore her body, feeling around everywhere in the dark and finding her favorite spots to be touched."

            claire @ say "Mmf, [name]~"
            claire @ say "We got a few hours til sundown~ Wanna make the most of it?~"

            player "Y-yeah, I'd love to~"

            n "You suddenly feel the bunny's lips against yours as she starts undoing your swimsuit..."

            stop music fadeout 1.3

            scene bg codadorm with fade
            
            play music "audio/ambient/outdoors night crickets.ogg" fadein 1.0

            show box with Dissolve(.2):
                ypos 0

            n "After a lovely day with Claire at the waterfall, you arrive home after dark and check your phone."

            call phone_start from _call_phone_start_56 

            call message_start("Claire", "OMG today was the best <333", "claireavi.png") from _call_message_start_75 

            call reply_message("Yeah <3") from _call_reply_message_301 
            call reply_message("I didn't know what to expect for our date but I'd say it turned out the best possible way") from _call_reply_message_302 

            call message("Claire", "Agreed~", "claireavi.png") from _call_message_408 
            call message("Claire", "The hike was longer than I thought it would be tho", "claireavi.png") from _call_message_409 
            call message("Claire", "Next time let's just meet at my dorm~", "claireavi.png") from _call_message_410 

            call reply_message("lol is Ava ok with that?") from _call_reply_message_303 

            call message("Claire", "Nobody said she can't join in on the fun~", "claireavi.png") from _call_message_411 

            call message("Ava", "*bonk*", "avaavi.png") from _call_message_412 

            call message("Claire", "Ow!", "claireavi.png") from _call_message_413 

            call message("Ava", "Don't invite me to 3somes without my knowledge!", "avaavi.png") from _call_message_414 

            call message("Claire", "Fffffffine <3", "claireavi.png") from _call_message_415 

            call reply_message("I didn't wanna share anyway") from _call_reply_message_304 

            call message("Claire", "Awwww <34333333", "claireavi.png") from _call_message_416 
            call message("Claire", "Your so adorable [name] x3", "claireavi.png") from _call_message_417 

            call reply_message("Let's give Ava a break and just meet up at my dorm next time, k?") from _call_reply_message_305 
            call reply_message("I'm all alone in here anyway") from _call_reply_message_306 

            call message("Claire", "Ohh yeahhhh", "claireavi.png") from _call_message_418 
            call message("Claire", "Gonna have to take advantage of that >:3", "claireavi.png") from _call_message_419 

            call reply_message("lol") from _call_reply_message_307 
            call reply_message("This weekend for sure") from _call_reply_message_308 
            call reply_message("But right now I'm pretty worn out and need a big sleep") from _call_reply_message_309 

            call message("Claire", "Kk", "claireavi.png") from _call_message_420 
            call message("Claire", "Good niiiiiiiite <3", "claireavi.png") from _call_message_421 

            call reply_message("Nite <3") from _call_reply_message_310 

            call phone_end from _call_phone_end_65 

            n "You plug your phone into its charger and turn in for the night, excited to wake up tomorrow and see Claire again."

            stop music fadeout 1.0

            jump monday6
        

        menu:
            n "{cps=0}Those adorable puppy-dog eyes... err, rabbit eyes, combined with that genuine smile... Just makes you want to kiss her.{/cps=0}"
            "Kiss her.":
                #finished
                ###ending is too rushed
                n "Ever so slowly, you lean in closer to her and she mirrors your movement."
                n "Time seems to slip away as you close your eyes and gently press your lips against hers."
                n "She's surprisingly tender with you, caressing you in a way that gives you goosebumps and melts your heart."
                n "The way she looks at you after your first kiss is the most reassuring look you've seen in your life."

                show claire swimsuit lusty
                
                claire @ say "[name]..."
                
                show claire swimsuit surprised

                n "You're about to lean in for another kiss when Claire's ears perk up."

                claire @ say "Dammit, somebody's coming. A bunch of frat bros and their dumb hoes judging by the sound of it..."

                n "You don't hear a thing but then again, you don't have massive ears."
                
                show claire swimsuit leaning

                claire @ say "Come on, I know somewhere we can have a little privacy~"

                n "Claire guides you to the waterfall and she disappears behind it."
                n "Really? A hidden cave behind the waterfall? What, is there a treasure chest back there too?"

                scene bg black with dissolve

                n "You pass through the waterfall and can hardly see anything in the darkness. Almost immediately you get pounced on by Claire."
                n "She pins you to the wall and begins assaulting you with kisses and little nibbles."

                player "A-ah, Claire~"

                claire @ say "Hehe, don't be afraid to make some noise~ The waterfall will cover it up~"

                n "Pleasured gasps escape your lips as she toys with you. Her paws guide your hands, placing them on something extraordinarily soft."

                claire @ say "Go ahead and play with 'em~ I know you've been wanting to~"

                n "Your eyes go wide as you realize you don't feel a swimsuit anywhere on her body."
                n "You're rewarded with soft nuzzles and cute moans as you explore her body, feeling around everywhere in the dark and finding her favorite spots to be touched."

                claire @ say "Mmf, [name]~"
                claire @ say "We got a few hours til sundown~ Wanna make the most of it?~"

                player "Y-yeah, I'd love to~"

                n "You suddenly feel the bunny's lips against yours as she starts undoing your swimsuit..."

                stop music fadeout 1.3

                scene bg codadorm with fade
                
                play music "audio/ambient/outdoors night crickets.ogg" fadein 1.0

                show box with Dissolve(.2):
                    ypos 0

                n "After a lovely day with Claire at the waterfall, you arrive home after dark and check your phone."

                call phone_start from _call_phone_start_57 

                call message_start("Claire", "OMG today was the best <333", "claireavi.png") from _call_message_start_76 

                call reply_message("Yeah <3") from _call_reply_message_311 
                call reply_message("I didn't know what to expect for our date but I'd say it turned out the best possible way") from _call_reply_message_312 

                call message("Claire", "Agreed~", "claireavi.png") from _call_message_422 
                call message("Claire", "The hike was longer than I thought it would be tho", "claireavi.png") from _call_message_423 
                call message("Claire", "Next time let's just meet at my dorm~", "claireavi.png") from _call_message_424 

                call reply_message("lol is Ava ok with that?") from _call_reply_message_313 

                call message("Claire", "Nobody said she can't join in on the fun~", "claireavi.png") from _call_message_425 

                call message("Ava", "*bonk*", "avaavi.png") from _call_message_426 

                call message("Claire", "Ow!", "claireavi.png") from _call_message_427 

                call message("Ava", "Don't invite me to 3somes without my knowledge!", "avaavi.png") from _call_message_428 

                call message("Claire", "Fffffffine <3", "claireavi.png") from _call_message_429 

                call reply_message("I didn't wanna share anyway") from _call_reply_message_314 

                call message("Claire", "Awwww <34333333", "claireavi.png") from _call_message_430 
                call message("Claire", "Your so adorable [name] x3", "claireavi.png") from _call_message_431 

                call reply_message("Let's give Ava a break and just meet up at my dorm next time, k?") from _call_reply_message_315 
                call reply_message("I'm all alone in here anyway") from _call_reply_message_316 

                call message("Claire", "Ohh yeahhhh", "claireavi.png") from _call_message_432 
                call message("Claire", "Gonna have to take advantage of that >:3", "claireavi.png") from _call_message_433 

                call reply_message("lol") from _call_reply_message_317 
                call reply_message("This weekend for sure") from _call_reply_message_318 
                call reply_message("But right now I'm pretty worn out and need a big sleep") from _call_reply_message_319 

                call message("Claire", "Kk", "claireavi.png") from _call_message_434 
                call message("Claire", "Good niiiiiiiite <3", "claireavi.png") from _call_message_435 

                call reply_message("Nite <3") from _call_reply_message_320 

                call phone_end from _call_phone_end_66 

                n "You plug your phone into its charger and turn in for the night, excited to wake up tomorrow and see Claire again."

                stop music fadeout 1.0

                jump monday6


            "Don't kiss her.":
                #finished
                $ dating = ""
                n "Hold on, this isn't right... Something feels wrong."
                n "Do you really want to kiss her or are you just caught up in the moment?"
                n "You're not sure you actually have feelings for Claire."
                n "You turn your head away and Claire seems to sense your feelings right away."
                
                show claire swimsuit surprised

                claire @ say "Oh... Did I do something wrong?"

                player "N-no, of course not! I just..."
                player "I dunno, I guess I just don't really feel it..."
                
                show claire swimsuit sad

                n "Claire looks down, disappointed, and steps away."

                claire @ say "Oh..."
                claire @ say "I see."
                claire @ say "It's alright. Sorry for not making sure everything was ok with you first."

                player "Don't apologize, you didn't do anything wrong. Everything's still good."
                
                show claire swimsuit neutral

                n "Claire smiles at you and half-heartedly splashes you again."

                claire @ say "You sure?"

                n "You splash her back."

                player "Yeah! I'm really flattered you asked me out on a date and it's been really fun."
                player "And I'd love to hang out with you more, but just... as friends, ok?"

                show claire swimsuit sad

                n "Claire rubs her eyes as they start to water up."
                n "She pulls you into a hug and holds you there for an uncomfortable amount of time before letting go."

                claire @ say "Y-yeah, friends~"

                n "You splash around in the pool for a bit longer until some frat bros come and ruin the already ruined mood."

                claire @ say "...How bout we call it a day?"

                player "Yeah..."

                stop music fadeout 1.3

                scene bg codadorm with fade
                
                play music "audio/ambient/outdoors night crickets.ogg" fadein 1.0

                show box with Dissolve(.2):
                    ypos 0

                call phone_start from _call_phone_start_34

                call message_start("Claire", "Hey... Today was... interesting.", "claireavi.png") from _call_message_start_44

                call reply_message("Yeah") from _call_reply_message_193
                call reply_message("I had fun though") from _call_reply_message_194

                call message("Claire", "Me too", "claireavi.png") from _call_message_257

                call reply_message("Sorry things didn't go how you wanted them to") from _call_reply_message_195

                call message("Claire", "It's alright. I'm glad we can still be friends at least", "claireavi.png") from _call_message_258

                call reply_message("Same! You're a really cool and nice person!") from _call_reply_message_196

                call message("Claire", "Thanks c:", "claireavi.png") from _call_message_259
                call message("Claire", "I'll see you around~", "claireavi.png") from _call_message_260

                call reply_message("Ya. Gnight") from _call_reply_message_197

                call message("Claire", "Nini", "claireavi.png") from _call_message_261

                call phone_end from _call_phone_end_38

                n "You turn out the lights and climb into bed, wondering what tomorrow will bring."
                
                stop music fadeout 1.0
                
                jump monday6


    if dating == "":
        n "Playing soccer with Gunner and his pals was pretty fun, even if the grass was all wet and gross."
        n "After a couple hours you all decided to call it quits but Gunner said he had something to talk to you about."
        n "You stroll through the campus streets on your way back to your dorm with Gunner beside you."

        show gunner neutral at center with dissolve

        gunner @ say "...Sooooo."

        player "...Yeah?"

        gunner @ say "If you could date anyone at Harmonia, who would it be?"

        player "Wha-? Where did that come from?"

        n "Is he hitting on you?!"

        gunner @ say "N-nowhere, it's just..."
        gunner @ say "You know that Ava chick?"

        player "What about her?"

        gunner @ say "Ah well, I was just wondering... you don't really have a thing for her do you?"

        player "Uhh not that I know of?"

        #gunner @ say "Really? Whew! I always see you two hanging out so I was kinda worried you might be a thing!"
        #gunner @ say "So you don't mind if I ask her out then, right?"
        gunner @ say "Okay good. Well I was thinking of finally asking her out. I think I've flirted enough and I've grown on her."

        player "Good for you dude! Good luck!"

        gunner @ say "Thanks!"
        gunner @ say "But that's got me wondering..."
        gunner @ say "If you're not into Ava, then who *are* you into?"

        player "What?! What makes you so sure I'm interested in anybody?"

        gunner @ say "Come on, everyone has their eye on someone! You don't have to give me any names, just tell me what sort of person you like!"

        menu:
            gunner "{cps=0}Come on, everyone has their eye on someone! You don't have to give me any names, just tell me what sort of person you like!{/cps}"
            "Someone gothy":
                $ rosePoints = rosePoints + 1
                player "Hmm... I guess someone gothy? Yeah, goth really scratches my itch."
            "Someone mature":
                $ ellenPoints = ellenPoints + 1
                player "Hmm... I guess someone mature? Maybe someone a little older?"
            "Someone shy":
                $ rosePoints = rosePoints - 1
                $ ellenPoints = ellenPoints - 1
                player "Hmm... I guess someone shy? I think those kinds of people are cute."

        gunner @ say "Ahh, I see then..."
        gunner @ say "I think I have an idea of who you're thinking of~"
        gunner @ say "Just leave everything to me!"
        gunner @ say "See ya later!"
        #gunner @ say "Well good luck finding that kind of person!"
        #gunner @ say "Thanks for the little chat!"

        hide gunner with dissolve

        n "Gunner runs off before you can say anything."

        #player "No problem."
        player "What did he mean by this?"

        #gunner @ say "Now if you'll excuse me, I'm gonna try and court that secretary bird."

        #player "Haha you go get 'em, tiger."

        stop music fadeout 1.3

        scene bg codadorm with fade

        show box with Dissolve(.2):
            ypos 0

#label post_main_date:

label monday6:
    # monday6

    if dating == "rori":
        jump posttimeskip
    if dating == "ava":
        jump posttimeskip
    if dating == "claire":
        jump posttimeskip
    else:
        #saturday8-2
        
        if roseBias == True:
            scene bg library with fade

            #play music "audio/ai9.ogg" fadein 1.0
            play music "audio/music/vylet - That Feeling I Get in my Heart" fadein 1.0

            show box with Dissolve(.2):
                ypos 0
        
            n "You find yourself at the library searching for the next book you need for your literature class."
            n "By some massive failure of the piracy community, the book isn't available on any websites that don't look like foreign malware requiring you to sign up."
            n "How dare they not track down this book, scan it, and upload it for free just for you."
            n "And to hell with paying for an overpriced copy at the local book store. You probably aren't even going to read it anyway."
            n "Now that you're actually here looking around, you realize how insanely massive Harmonia's library is. It's a nine story building where each floor is bigger than your old school."
            n "On top of that, many of the shelves are so high you'd need a ladder to get to the top."
            n "You could probably get lost in here and die of starvation before someone found you."
            
            player "You must have stumbled into the history section because you've spotted a certain bitchy raccoon in one of the aisles."
            
            n "Wait, did you just say that out loud?"

            show rose unimpressed at center with dissolve

            rose @ say "Ugh, what are you doing here?"
            rose @ say "Can't I have one place where you'll leave me alone?"

            player "I'm just passing through."
            player "If anything it feels like *you're* the one stalking *me*."
            
            show rose angry
            
            rose @ say "In your dreams, creep!"
            
            player "More like in my nightmares!"
            
            rose @ say "I could make your life a nightmare if you want."
            
            player "Tempting but I'm just looking for a copy of \"Romaunt of the Rose\". You wouldn't happen to have seen it, would you?"
            
            rose @ say "Seriously?"
            
            player "What?"
            
            rose @ say "Is this a joke?"
            
            player "No, it's really called that! I need it for literature!"
            
            rose @ say "Well I haven't seen it. So go away."
            rose @ say "Actually, before you do, you might as well make yourself useful."
            rose @ say "Grab that book on the top shelf for me."
            
            player "And why would I do that?"
            
            rose @ say "Because if I don't get a perfect score on this history project, I'm tanking your grade along with mine."
            
            player "Okay jeez fine. Which book?"
            
            rose @ say "That one."
            
            n "She points to a thick tome that looks like it will crumble into dust the moment you touch it."
            n "You stretch your arms up to it but it's just out of reach."
            
            player "Damn, isn't there a stepping stool or a ladder or something?"
            
            rose @ say "Hold on, stay right there."
            
            player "Hey, what are you-"
            
            n "You feel Rose's claws dig into your side as she climbs onto you."
            
            player "That hurts you know!"
            
            rose @ say "Don't be such a baby. And stand still!"
            
            n "Rose makes her way up onto your shoulders which puts her at just the right height to pull the book off the shelf."
            
            rose @ say "Ugh, it's stuck!"
            
            n "She tugs on it a few times, throwing off your balance."
            
            rose @ say "Got it!"
            rose @ say "W-whoa!"
            
            n "Your loss of balance combined with the added weight causes you to stumble and trip over your own feet."
            n "Rose jumps to safety while you crash to the ground."
            
            player "*THUD!!!*"
            
            rose @ say "Shh! This is a library you know!"
            
            player "Ow..."
            
            rose @ say "Hehehehe!"
            
            player "Did you just laugh? I didn't think it was possible. Have I died and gone to hell?"
            
            rose @ say "Unfortunately no, you're still alive."
            
            n "You get up with a groan. You feel a sharp pain in your spine."
            
            rose @ say "You ok?"
            
            menu:
                "Yeah":
                    player "Yeah, perfectly fine."
                    
                    rose @ say "Damn."
                    
                    n "She says and begins to walk off."
                "No":
                    player "No."
                    
                    rose @ say "Good."
                    
            player "Wow, not even a 'thanks' for getting that super important book, huh?"
            
            rose @ say "What do you expect, a medal?"
            
            #player "A blowjob would do."
            
            #rose @ say "I bite."
            
            player "That would be nice."
            
            rose @ say "How about this: I'll help you find the book *you're* looking for. I could use a break from this history paper anyway."
            
            player "Deal. You can check the lower shelves while I look high."
            
            rose @ say "Or I can ride on your shoulders again and look high while you search low."
            
            player "Wow first a giggle and now a joke. You must be warming up to me."
            player "...that was a joke, right?"
            
            rose @ say "Heh. Maybe~"
            
            n "Despite using you as a stepping stool, Rose is actually not being a bitch to you today."
            n "You must be doing something right."
            n "You begin scouring the library for your book with Rose."
            n "It feels like hours have gone by but surprisingly Rose sticks by your side, quietly whispering some small talk and banter."
            n "Today must be your lucky day because Rose finds your book on the bottom shelf."

            rose @ say "Is this it? You said it was called \"Romaunt of the Rose\" right?"
            
            player "No way, you actually found it! I was starting to worry I'd have to pay for a copy!"
            
            rose @ say "You went through all this trouble to avoid buying your own copy? You should just pirate it."
            
            player "I tried but I couldn't find it."
            player "And I'm not paying for overpriced sheets of paper from a dead author!"
            
            rose @ say "Well have fun reading old English. I'm gonna get back to my- I mean \"our\" history project."
            
            player "Thanks for the help."
            
            n "As she turns around and begins to walk away, an impulsive thought suddenly forms in your mind and you blurt it out without thinking."
            
            player "Hey wait! You wanna grab a coffee together or something?"
            
            rose @ say "Only if you're paying."
            
            player "I mean, you did just save me like 50 bucks."
            
            n "Rose sighs."
            
            rose @ say "Fiiiine, I suppose I can spare a couple minutes for some caffeine."
            
            player "Coffee Zone?"
            
            rose @ say "Hell yeah."
            
            $ dating = "rose"
            
            scene bg black with fade
            
            jump posttimeskip
            
        
        else: 
            n "Another week goes by and you find yourself wondering what to do with your weekend."
            n "Miss Ellen mentioned a seminar on modern women writers that's supposed to be happening today."
            n "You don't really care to do school related things on a weekend but she promised extra credit just for attending."
            n "Besides that you've still got to do your part for the history project. If you should even bother with it, that is."
            n "You could also just stay in your dorm and catch up on some homework."
            
        
            menu:
                n "{cps=0}You could also just stay in your dorm and catch up on some homework.{/cps}"
                "Do history project":
                    n "Better to get it over with than continue procrastinating."
                    n "You grab your backpack and prepare to head out to the library for some research."

                    scene bg library with fade

                    play music "audio/music/vylet - sleepless.ogg"

                    show box with Dissolve(.2):
                        ypos 0

                    n "Now that you're actually here looking around, you not that Harmonia's library is absolutely massive. It's a nine story building where each floor is bigger than your old school."
                    n "On top of that, many of the shelves are so high you'd need a ladder to get to the top."
                    n "You could probably get lost in here and die of starvation before someone found you."
                    n "After scouring the shelves, you finally come across the history section."
                    n "You guess you really shouldn't be surprised to see Rose here, but the sight of her still startles you."

                    show rose unimpressed at center with dissolve

                    rose @ say "Ugh, what are you doing here?"
                    rose @ say "Can't I have one place where you'll leave me alone?"

                    player "Jeez sorry for wanting to get my part of the history paper done."
                    
                    show rose angry
                    
                    rose @ say "You're the one who weaseled your way into helping in the first place!"

                    player "Yeah, so I wouldn't just be dead weight."

                    show rose neutral
                    rose @ say "I guarantee we'd get a better score if you just let me handle everything."
                    rose @ say "Why don't you just run along and let me work on the project myself?"
                    rose @ say "It's less work for you *and* I'll even let you copy off my homework for the rest of the semester."

                    menu:
                        rose "{cps=0}It's less work for you *and* I'll even let you copy off my homework for the rest of the semester.{/cps}"
                        "Deal":
                            n "It seems she really doesn't want you hanging around."
                            n "You guess it's a win-win where you basically don't have to try to pass your history class outside of tests."
                            n "And Rose doesn't have to be bothered by your mere presence anymore."

                            player "Fine. Sorry to be a nuisance."

                            rose @ say "Hmph."

                            hide rose with dissolve

                            n "Rose turns back to her books as you walk away."

                            stop music fadeout 1.3

                            jump mishkasunday
                        "No deal":
                            player "Nope."
                            
                            show rose furious
                            
                            rose @ say "Ugh, what is your problem?!"
                            rose @ say "Just take what I'm offering and leave me alone!"

                            player "I've already decided I'm going to write my one page and that's that."
                            player "Now can I please see what you've done so I can make sure I'm not repeating information you already wrote?"

                            n "Rose grinds her teeth and looks like she's about to kill you, but instead she just opens her notebook and pulls out her project draft papers, handing them to you."

                            hide rose with dissolve

                            n "It looks like she's already close to being finished with the paper, but there are a few corrections to be made that she's noted on here."
                            n "You sit there in awkward silence reading this densely-packed paper that makes reading your textbook sound fun while Rose has her nose shoved in a book."
                            n "That's not to say there isn't any interesting information to be found here though."
                            n "Like the bit about the raccoon tribe that attempted to mimic European cultures after the settlers arrived to the point where they had a king and queen and attempted to migrate to England."
                            n "As you're reading through it, Rose gets up and walks away but left her books and bag behind."
                            n "Leaning back in your chair you see her in one of the aisles looking up at one of the books on the top shelf with a more frustrated than usual expression on her face."
                            n "It doesn't look like there's a ladder available."
                            n "With a sigh you decide to help out, even if she'll hate you more for it. You set aside the paper for now and walk over."

                            show rose neutral at center with dissolve

                            rose @ say "Dammit, they just had to put it all the way at the top!"

                            player "Which one?"

                            rose @ say "That one."

                            n "She points at a rather hefty looking tome on the top shelf."

                            player "Isn't there supposed to be a ladder for those?"

                            rose @ say "All they have is this stupid step stool."

                            n "Even on your tip toes on top of the step stool, you can't reach it."

                            rose @ say "Here, get down."

                            player "What the-"

                            n "Rose starts climbing onto your shoulders, yanking and pulling on your clothes and hair."

                            player "Ow!"

                            rose @ say "Shut up."
                            rose @ say "Okay now stand back up on the stool."

                            n "With Rose standing on your shoulders, you carefully climb back onto the stepping stool."

                            rose @ say "If you look up, you're literally dead."

                            menu:
                                rose "{cps=0}If you look up, you're literally dead.{/cps}"
                                "Don't look up.":
                                    $ goodEnd = goodEnd + 1
                                    n "Rose takes her sweet time grabbing the book, her boots digging into your shoulders."

                                    player "Any day now..."

                                    rose @ say "It's... urgh... stuck in there tight!"
                                    rose @ say "Ah, there we go!"

                                    n "The weight on your shoulders suddenly increases as Rose takes hold of the oversized book."
                                    n "You grit your teeth as she climbs down off of you, bumping your head with the corner of the book on accident."
                                    n "Or at least you think it was an accident."

                                    if rosePoints >= 2:
                                        $ dating = "rose"
                                        
                                        show rose smug
                                        
                                        rose @ say "Hmph. Thanks for the help. I guess you're not completely dead weight after all."
                                        
                                        hide rose with dissolve

                                        n "You spend the rest of the day running errands for Rose in between trying to figure out how you're gonna write a page that fits in with what she's already written."
                                        n "But at the end of the day, it all feels worth it cause you saw her smile."
                                        n "It was just for a brief moment but you definitely saw her smile at some point when you got her on a tangent about humans losing the Great Emu War."

                                        stop music fadeout 1.3

                                        jump posttimeskip
                                    else:
                                        rose @ say "Hmph."

                                        n "You spend the rest of the day running errands for Rose in between trying to figure out how you're gonna write a page that fits in with what she's already written."
                                        n "She doesn't speak to you much and at some point she packs her things up and leaves without a word."

                                        stop music fadeout 1.3

                                        jump mishkasunday

                                "...Maybe just a quick peek":
                                    n "The instant your head moves one degree upward, you get a boot to the face."
                                    n "You tumble to the ground and everything goes black."

                                    scene library with fade

                                    show box with Dissolve(.2):
                                        ypos 0

                                    n "When you come to, Rose is nowhere to be found and her belongings are gone."
                                    n "Can't say she didn't warn you."
                                    n "It was a calculated risk but man are you bad at math."
                                    n "Welp, your work here is done. You pack your things and head back to your dorm."

                                    stop music fadeout 1.3

                                    scene bg codadorm with fade

                                    show box with Dissolve(.2):
                                        ypos 0

                                    n "Checking the mirror when you get back to your dorm, you've got an outline of Rose's boot marked onto your face."
                                    n "Damn, it hurts like hell and stings when you touch it."
                                    n "You get the feeling you should avoid Rose from now on if you don't want to have an even earlier death."

                                    jump mishkasunday


                "Do homework":
                    $ goodEnd = goodEnd + 1
                    n "You stay in your dorm and do homework."
                    n "It's boring, but at least you understand the material better now."
                "Go to literature seminar":
                    $ goodEnd = goodEnd + 1
                    if rosekiss == False:
                        n "All you have to do is show up and pretend to pay attention, which seems like less work than researching and writing for the history project."
                    else:
                        n "All you have to do is show up and pretend to pay attention. Seems easy enough."
                    n "You grab your backpack and prepare to head out."

                    scene bg lecturehall with fade

                    play music "audio/music/mere - retrograde.ogg" fadein .5

                    show box with Dissolve(.2):
                        ypos 0

                    n "That seminar dragged on forever. They had like four different guest speakers trying to sell their book about how hard it is making a living writing books as a woman etc."
                    n "You zoned out of it pretty early on and hardly noticed when it was finished."
                    n "A few people are staying behind to talk to the writers but you're more interested in going about the rest of your day."
                    n "Your plans come to a screeching halt when Miss Ellen stops you near the exit."

                    show margaret neutral at center with dissolve

                    ellen @ say "[name]! I'm so glad you could make it! What did you think? Quite inspirational, wouldn't you agree?"

                    player "Yeah, it was good. Very informative."

                    ellen @ say "Thanks for coming! If you have any comments, feel free to write them on the feedback form over there."

                    player "Sure."

                    ellen @ say "See you in class!"

                    if ellenPoints >= 3:
                        menu:
                            ellen "{cps=0}See you in class!{/cps=0}"
                            "See ya.":
                                player "See ya."

                                n "You wave goodbye and head back to your dorm for the day."

                                jump mishkasunday
                            "Stay behind and talk more":
                                player "Actually, I wanted to talk more... about what you said up on the rooftop the other day."

                                ellen @ say "Is that so?"
                                ellen @ say "Hmm..."
                                ellen @ say "I've got to finish up here first but would you mind meeting me up there in 20 minutes?"

                                player "Sure."

                                scene bg roof with fade

                                play music "audio/music/vylet - Evening Trot.ogg" fadein 1.0

                                show box with Dissolve(.2):
                                    ypos 0

                                n "Half an hour has passed and Miss Ellen is nowhere to be seen."
                                n "Did she just forget about you?"
                                n "Just as you're considering going home, Miss Ellen comes up the stairs and pulls out a cigarette carton."

                                show margaret neutral at center with dissolve

                                ellen @ say "Want one?"

                                player "I'm good."

                                show margaret smoking neutral

                                n "She lights one up and blows out a cloud of smoke."

                                ellen @ say "So what was it you wanted to talk about?"

                                player "I dunno."
                                player "..."
                                #player "You said you were going through a mid life crisis? What's that all about?"
                                #ellen @ say "Oh it's nothing for you to worry about."
                                #player "..."
                                #player "I'll tell you my story if you tell me yours first."
                                #ellen @ say "..."
                                #ellen @ say "Alright, fine."

                                ellen @ say "..."

                                player "..."

                                ellen @ say "Huh."
                                ellen @ say "Well, why don't I tell you my troubles, then you can decide if you wanna talk about yours."

                                player "That works for me."

                                n "Miss Ellen takes another drag from her cigarette."

                                show ellen sad

                                ellen @ say "Where to start..."
                                ellen @ say "Y'know I never wanted to be a teacher."

                                player "Then why'd you become one?"

                                ellen @ say "Dunno. I wasn't sure what else to do and nothing else was working either."
                                ellen @ say "My ex-husband convinced me to try it."
                                ellen @ say "I wanted to be a writer but to be honest, I hate my writing."
                                ellen @ say "Not just the end result but the whole process involved."
                                ellen @ say "It's frustrating and it never feels good enough and hardly anybody appreciates the work you put into it."

                                show ellen smoking

                                ellen @ say "I just liked the idea of being a best-selling author like those other women."
                                ellen @ say "But now I'm well past my prime, stuck in a job I hate with no accomplishments, no goals, not even a family..."
                                ellen @ say "I guess that's why I picked up smoking."

                                player "Wow uh"
                                player "Dang."
                                player "I didn't realize you had it so rough."

                                ellen @ say "That's what happens when you get old and can't find anything that makes you happy."
                                ellen @ say "Alright, I've offloaded some of my pain, now it's your turn."

                                player "Right so I found out a few weeks ago I'm gonna go extinct in a few years so now everything seems pointless."
                                player "But I've sorta found some distraction from that in hanging out with friends and stuff."
                                player "But then sometimes I can't stop myself from thinking about how meaningless my life is and how I'll be gone before I've even had a chance to feel alive."

                                ellen @ say "I see."

                                n "Ellen finishes off her cigarette and pauses for a minute."

                                ellen @ say "I guess we have more in common than I thought."

                                player "Yeah."

                                ellen @ say "I wish I could offer some wisdom but all I have is Tolstoy's bullshit."

                                player "Hah. Y'know, you're the most real literature teacher I've had."

                                ellen @ say "Oh I'm pretty sure all us literature folks are depressed in some way, some are just better at hiding it."

                                n "Miss Ellen grins as she pulls a flask from her jacket."

                                ellen @ say "Truth be told, nothin' gets me through the day quite like a few sips of vodka."

                                player "Holy shit, you get drunk at work?"

                                ellen @ say "Just a little."
                                ellen @ say "I like to live a little dangerously~"

                                n "She holds the flask out to you."

                                ellen @ say "Wanna sip?"

                                menu:
                                    ellen "{cps=0}Wanna sip?{/cps=0}"
                                    "Accept":
                                        $ dating = "ellen"
                                        player "Ah fuck it. How can I say no?"

                                        n "You take hold of the flask and down a sip."

                                        player "Gah, that taste..."

                                        ellen @ say "You become numb to it eventually."

                                        player "I can't believe I'm trespassing on a university rooftop and drinking underaged with my literature professor."

                                        ellen @ say "Wild, isn't it?"
                                        ellen @ say "Well sometimes life is wild. And sometimes you have to make it wild."
                                        ellen @ say "Cause otherwise you're not even living. You're just letting life happen to you."

                                        player "I'll drink to that, Miss Ellen."

                                        n "Miss Ellen giggles as you take another swig."

                                        ellen @ say "Oh please, there's no need to be so formal you know!"
                                        
                                        show margaret smoking neutral
                                        
                                        ellen @ say "Just call me Ellen from now on when it's just the two of us~"
                                        ellen @ say "Unless you *prefer* to call me Miss hehehe~"

                                        player "There's a time and place for everything."

                                        ellen @ say "Good answer~"

                                        n "You spend a while longer up on the rooftop, chatting and emptying a good portion of her flask."
                                        n "You might have had a bit too much because you end up having some difficulty walking down the stairs but Miss Ellen holds onto you on the way down."
                                        n "In the hall she looks around to make sure no one's watching before pulling you into a tight hug."

                                        ellen @ say "If you ever want to talk again, I'm always available~"

                                        hide ellen with dissolve

                                        n "Your mind, still sluggish from the booze, struggles to catch up to what's happening."

                                        player "Y-you too."

                                        n "She's already halfway down the hall by the time you respond, her tail wagging as she walks away."
                                        n "You try not to stare but it's just so mesmerizing..."
                                        n "After she rounds a corner, you head in the opposite direction and return to your dorm for the night, thinking about everything you two talked about on the roof."

                                        stop music fadeout 1.0

                                        jump posttimeskip
                                    "Decline":
                                        #ellen seems a little disappointed if you say no but player reassures her they won't say anything
                                        player "No thanks."

                                        show ellen sadsmoking

                                        n "Miss Ellen seems to deflate a little, almost like she's disappointed."

                                        ellen @ say "Oh... that's fair."

                                        player "Don't worry, I won't tell anyone."

                                        ellen @ say "To be honest, I don't really care if you do or don't."
                                        ellen @ say "I'm just living passively at this point. Whatever happens to me happens. I don't care anymore."
                                        ellen @ say "..."
                                        ellen @ say "My life's a wreck."
                                        ellen @ say "I thought maybe I could become like a cautionary tale on how not to end up like me to you."
                                        ellen @ say "But I guess it doesn't really matter, does it?"

                                        n "You wish you could console her but you can't think of anything to say."
                                        n "After a while she takes a sip from her flask."

                                        ellen @ say "I'm sorry I couldn't be more helpful, [name]."

                                        player "It's alright. You're doing what you can."
                                        player "Maybe it's better to just, understand that others are suffering too than to try and fix things you know you can't fix."

                                        show ellen smoking

                                        ellen @ say "Heh. You sound pretty wise for your age, kid."

                                        hide ellen with dissolve

                                        n "You hang out with Miss Ellen on the roof for a while longer before parting ways."
                                        n "Man, now you just feel even more depressed after seeing a grown lady as miserable as her."
                                        n "You have a feeling you'd end up just like her if you were to reach that age."

                                        stop music fadeout 1.0

                                        jump mishkasunday
                    else:
                        player "See ya."

                        n "You wave goodbye and head back to your dorm for the day."

                        stop music fadeout 1.0

                        jump mishkasunday



label mishkasunday:
    # sunday8-2

    $ dating = "mishka"

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    n "Sunday mornings always feel like your weekend is already over."
    n "It's not like you've even accomplished much this weekend either..."
    n "But sometimes you need a weekend just to rest and recover. Honestly they should give you a pre-weekend to prepare you for a more productive weekend."
    n "You'll have to petition society about that later, cause you haven't been to the cafe lately and you've got a need for some bitterly delicious coffee."

    scene bg campus with fade

    play music "audio/music/vylet - Takamine.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0

    n "What the-? The door to the cafe is locked! Who could have done such a thing?!"

    mishka @ say "[name]?"

    show mishka despondent at center with dissolve:
        xzoom -1

    n "Oh thank God."
    n "Mishka shows up seemingly out of nowhere to open the cafe for you. She truly is the best."
    
    show mishka cute

    mishka @ say "Sorry, the cafe is closed today. No coffee for you hehe!"

    n "You've never felt more betrayed."

    player "Well damn. There go my entire plans for the day."
    player "...What are you doing out here by the cafe if you're off work today then?"
    
    show mishka happy

    mishka @ say "I was just on my way back to home from church when I saw you attempting to break in."
    mishka @ say "I was going to call police but then I saw it was just you."

    n "You laugh nervously, not really able to tell if she's joking about calling the police on you."

    player "Ahah...hah... Well... Got any other plans?"
    
    show mishka overjoyed

    mishka @ say "Mmmmnope!"
    mishka @ say "I'll probably just read a book or browse pinstagram til it's time to get dinner!"
    
    show mishka shy
    
    mishka @ say "*Gasp!*"
    
    show mishka happy
    
    mishka @ say "Would you like to come along to dinner with me?"
    mishka @ say "I know a place that serves authentic food from my motherland!"
    
    show mishka shy smile
    
    mishka @ say "The owner is so nice and she always says things like \"Mishka, why don't you find yourself a cute special somebody to come here with so you aren't always eat alone?\""
    
    show mishka overjoyed
    
    mishka @ say "Yes yes, very good [name], you will be happy to come along with me to eat good food and have good time!"

    n "Mishka's usual subdued tone becomes bubbly and excited as she practically decides for you that you're going on a date with her."
    #n "Not that you mind. It's something to do, and if you were gonna go out with anybody it'd have to be Mishka. She's so kind and the way she talks is charming."
    n "Not that you mind. It's something to do, and if you were gonna go out with anybody it'd have to be Mishka. She's so kind and the way she talks is funny and cute."
    
    stop music fadeout 1.0

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    n "After deciding upon a time and exchanging phone numbers, you and Mishka parted ways until evening would arrive."
    n "You decided to break out some nicer clothes than usual for your date tonight. Nothing too fancy, just something less casual than jeans and a milsurp jacket."
    n "Even if Mishka was totally checking out your glorious flecktarn parka earlier."
    #n "Mishka's words echoed through your mind 'Heheh death to russian invaders, free ukraine!'"
    n "Welp, time to find out what Ukrainian tastes like."
    n "Ukrainian food, you mean."
    #n "Ukrainian food, that is."
    #n "Ukrainian food, to clarify."

    scene bg restoran with fade

    show box with Dissolve(.2):
        ypos 0

    play music "audio/music/russianeaster.ogg" fadein 1.0

    n "You arrive at the place Mishka described and you're inclined to believe you found the right place judging by the abundant eastern European decor and the fact the menu is in cyrillic."
    n "You let the hostess know that you're waiting for a friend and she said something in Russian and sat you at a table."
    n "You think she was happy but it's hard to tell."
    n "You tried to order a water but she just said \"Nyet, vih pyote eto\" and poured you a glass of straight vodka without even carding you."
    n "After a few minutes, Mishka finally arrives. She's greeted with a warm hug by the hostess who directs her over to you."

    show mishka happy at center with dissolve

    mishka @ say "[name]! I'm so happy you made it!"

    player "I think that lady's just as happy as you are that I showed up."
    
    show mishka anxious grin

    mishka @ say "Who, tovarisch Volginova? She's who I mentioned ealier! She's the owner!"
    
    show mishka neutral
    
    mishka @ say "I think she's a retired colonel or something like that. I dunno, she's very secretive about her past!"

    n "You chance a glance over to her and she gestures that she has her eye on you before walking up to the table with another glass."

    show volginova neutral at center with dissolve:
        xzoom -1
        xpos -500

    volginova @ say "Here you go, dear~"

    mishka @ say "Spasibuh!"

    volginova @ say "Do you need a minute to decide?"

    n "Mishka looks up at you inquisitively."

    player "Err, why don't you order for me Mishka? I'm sure it's all good."
    
    show mishka teasing

    mishka @ say "Sure! I'll have kruchenyky eeeee... kotleta po-kyivsky would be good introduction for [name], ya dumayu."
    
    show mishka shy
    
    mishka @ say "Ah and could we get varenyky please?"

    volginova @ say "Zvychayno! I'll have those varenyky out for you in a few minutes."

    hide volginova with dissolve

    n "Volginova disappears behind a curtain, leaving you and Mishka alone in the restaurant with some kind of russian classical music playing in the background."
    #n "Mishka mentions something about Volginova being in the KGB "
    n "You and Mishka idly chat and sip on your drinks for a few minutes until Mishka excuses herself to the restroom."

    hide mishka with dissolve

    n "A short while later, Volginova shows up with the appetizer Mishka ordered and places them on the table, then she just sort of... stands there intimidatingly."

    show volginova neutral at center with dissolve

    volginova @ say "   ...   "

    n "It's starting to freak you out so you try to say something."

    player "Umm, Mishka just went to the restroom but she should be back any-"

    #volginova has an eyepatch
    #volginova @ say "Break her heart and I promise you I will break every bone in your body in half... twice!"

    volginova @ say "You seem like nice girl."

    if fratsoro == "frat":
        player "Oh actually I'm a b-"

    volginova @ say "If you break her heart, I promise you I will break every bone in your body in half... twice!"

    n "That's all she says before turning around and walking back into the kitchen."

    show volginova neutral at offscreenleft with move:
        yalign 0

    n "A moment later Mishka reappears, her cheery mood completely contrasting with Volginova."

    show mishka saddest at center with dissolve

    mishka @ say "Huh? What's wrong, [name]? Are you not having good time?"

    player "I-it's nothing. Just hungry is all."
    
    show mishka happy

    mishka @ say "Aww, you didn't have to wait for me to come back before trying the varenyky!"

    n "You have to admit, they smell really good."
    n "Mishka grabs one and takes a bite out of it."

    player "What are they anyway?"
    
    show mishka shy

    mishka @ say "They are like umm... I think you call them dumplings? Is just cheese and stuff inside a bread thing."
    mishka @ say "You will find many Ukrainian dishes can be described as 'thing inside a bread thing' haha!"

    n "You take one and pop it into your mouth."
    n "Ow fuck, it's hot!"
    n "Trying not to look like a total idiot in front of your date, you try to cool your mouth with a nice big sip of Ukrainian water."
    n "Hoo boy this is already turning out to be a fun night."
    n "Mishka giggles and sips her drink. You wonder if Volginova gave her vodka as well."
    n "Some time later, Volginova arrives with your main course."
    n "It appears to be some breaded chicken for you and a... meat roll thing for Mishka."
    n "You silently thank Mishka for ordering you something that looks normal to you."

    mishka @ say "Ah, want a bite of mine? It's got mushroom and carrots and beets inside!"
    
    n "You don't want to hurt her feelings so you go for it."
    
    player "Uhm, sure!"

    n "You hesitantly cut a slice from Mishka's plate and dump it onto your own."
    n "She's looking at you expectantly, so you quickly look away from it and put it in your mouth."
    n "To your surprise, it actually doesn't taste that bad. It's like the dumpling but instead of a bread shell it's a... meat shell."
    n "Not exactly the most appetizing thought but sometimes food tastes better than it looks."
    n "You give Mishka a nod of approval and wash it down with a sip of vodka."
    
    show mishka anxious grin

    mishka @ say "So? What you think?"

    player "I liked it! Buuuuut I think I'll stick to my... kotlet of... uh po-kyifz...fzky... thing. God why do eastern european languages have so many consonants right next to each other all the time?"
    
    show mishka happy

    n "Mishka giggles at your struggle to speak her language."

    mishka @ say "Oh believe me, I have many complaints about English language! So many useless letters and redundant words! Why make it so complicated?"

    player "You haven't seen useless letters until you've read French."

    n "You and Mishka have a nice time bashing different countries and cultures until you've finished your meals and Volginova comes with a mint for the both of you."

    show volginova neutral at center with dissolve:
        xzoom -1
        xpos 1200
        
    show mishka neutral

    volginova @ say "Well? How did you enjoy it?"

    player "It was very nice, thank you!"

    n "Skeptical of your words, she looks to Mishka."

    mishka @ say "We loved it, blagodaryu vas!"

    volginova @ say "Otlichna! Do not worry about paying for the meal, though I will expect you to pay for my dearest Mishka's meal next time, young lady!"

    n "She points at you and stares directly into your soul but Mishka just laughs it off."

    mishka @ say "Haha don't be so old fashioned, we can split it next time, right [name]?~"

    n "Given how well this date went, your heart skips a beat when you realize Mishka enjoyed it as well and is already asking to go on another one."

    player "Of course! I'd love to do this again sometime!"

    n "Mishka wraps her little arms around your body, giving you the tightest hug you've ever experienced from someone shorter than you."

    mishka @ say "Uraaa!~ Thank you [name]!"

    n "Volginova gives you a pat on the back."

    volginova @ say "Horosho! Have good night you two."

    mishka @ say "Goodnight tovarisch Volginova!"

    player "Thank you for the meal!"

    hide volginova with dissolve

    n "You walk Mishka home underneath the stars in the cool autumn air, wondering what could be more perfect than this?"

    stop music fadeout 1.3

    scene bg black with fade

    n "The next few days pass by surprisingly quick. You spend a lot of time hanging out with and texting Mishka before and after class."
    n "Before you know it, the next weekend is here, giving you another opportunity to go out."


label mishka_rain_date:
    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    n "You wake up to the sounds of rain against your window."
    n "As peaceful as it sounds, this is gonna throw a wrench into your plans with Mishka today."
    n "You were supposed to go for a picnic with her today..."

    call phone_start from _call_phone_start_50

    call message_start("Mishka", "Allo [name]! Ready for todays date??", "mishkaavi.png") from _call_message_start_62

    call reply_message("Yeah but it doesn't look like this rain plans on letting up anytime soon and I don't wanna eat soggy sandwiches...") from _call_reply_message_227

    call message("Mishka", "That's okay! We can still go for walk like planned!", "mishkaavi.png") from _call_message_322

    call reply_message("Hmm... Alright. I'll meet you outside the cafe, k?") from _call_reply_message_228

    call message("Mishka", "Oki! c:", "mishkaavi.png") from _call_message_323
    call message("Mishka", "See you soon <3", "mishkaavi.png") from _call_message_324

    call reply_message("See ya <3") from _call_reply_message_229

    call phone_end from _call_phone_end_54

    n "You don your finest milsurp parka and head out."

    scene bg campus with fade

    show box with Dissolve(.2):
        ypos 0

    #play music "audio/music/Jazz Piano Bar - Doug Maxwell, Media Right Productions (No Copyright Music).mp3" fadein .5
    play music "audio/music/vylet - Rarity Dozing in a Coffee Shop at 1AM.opus" fadein .5

    n "The rain was cold and relentless, already soaking through the supposedly water resistant threads of your jacket."
    n "Worth it to see Mishka though."
    n "You wait under the awning outside the cafe, mindlessly re-reading your texts."
    n "The smell of ozone and lavender fills your nose and you hear something scuttling near you."
    n "Before you can look over your shoulder, you feel a pair of petite arms wrap around your waist from behind."

    show mishka hat happy at center with dissolve

    mishka @ say "Gotchya! Heehee~"

    player "Heh, I didn't know rats were predatory animals~"
    
    show mishka hat neutral

    mishka "We're opportunistic~"

    n "Mishka lets go and walks around in front of you."

    menu:
        n "{cps=0}Mishka lets go and walks around in front of you.{/cps}"
        "Is that a new perfume? I like it.":
            player "Is that a new perfume? I like it."

            mishka @ say "It is! It's supposed to smell like stormy weather so I thought it would be a good fit for today."

            player "You should wear it more often."

            mishka @ say "Maybe I will~"
        "I like your hat.":
            player "I like your hat."

            mishka @ say "Dyakuyu! It's an ushanka."
            mishka @ say "You humans invented them to keep your ears warm."
            mishka @ say "But I don't like not being able to hear so I cut holes in mine for my ears."

            player "Don't they get cold?"

            mishka @ say "In this weather? Nyet, this is like Ukrainian summer."

    player "So what are we gonna do since our picnic is ruined?"

    mishka @ say "I figured we could just walk around and enjoy the rain."

    player "Sounds good to me!"

    n "You hold your hand out and Mishka takes a hold of it as you walk back out into the increasing downpour."

    hide mishka with dissolve

    show bg streets with dissolve

    n "As boring as it sounds, you end up having a fun time just walking around town in the rain with your rat girlfriend."
    n "She tells you stories about her life in Ukraine and how she had trouble adjusting to American lifestyle."
    n "In a way you can kind of relate, being from a small town yourself and having to get used to living in a populated area like Harmonia."

    show mishka neutral hat at center with dissolve

    mishka @ say "Incoming!"

    n "Mishka jumps into a large puddle, stomping her boots just as she hits the water, causing it to splash all over you."

    player "Hey!"

    n "You reciprocate by stomping into the puddle and splashing her back."

    mishka @ say "Aaaaah! Hahahahaha I love days like these!"
    mishka @ say "Americans are allergic to water or something so nobody ever goes out during a storm so I can be by myself..."

    ###thunder sound effect
    show bg lightning1
    pause .03
    show bg streets

    mishka @ say "...or with someone I like."
    mishka @ say "And feel like I'm home..."

    ###thunder sound effect
    show bg lightning1
    pause .02
    show bg lightning2
    pause .02
    show bg streets with dissolve

    player "Uhh, Mishka? You think maybe we should go inside? That lightning is getting pretty close."
    
    show mishka happy hat

    mishka @ say "Ahahahahaha! Isn't this great?!"

    ###thunder sound effect x2
    show bg lightning1
    pause .02
    show bg lightning2
    pause .02
    show bg lightning1
    show bg streets with dissolve
    pause .06
    show bg lightning1
    pause .02
    show bg lightning2
    pause .02
    show bg streets with dissolve
    
    show mishka neutral hat

    mishka @ say "Who's afraid of a little lightning?"

    n "Even with her fur damp from the rain, you can see the tips of her fur start to stand up."
    n "Wait, doesn't that mean..."

    player "Oh shit! Mishka!"

    n "You grab hold of Mishka and hold her tight, pulling her back just before a bolt of lightning crashes down right in front of you."

    hide mishka
    show bg lightning1
    pause .02
    show bg lightning2
    pause .02
    show bg lightning1
    pause .6
    show bg streets with dissolve

    player "Mishka?"

    n "When your hearing and vision return, you're still holding onto Mishka and she's still laughing maniacally."

    player "Mishka! Are you alright?"

    show mishka happy hat at center with dissolve

    mishka @ say "Ahah... Ahhh... ahahahaha..."
    
    show mishka hat sad
    mishka @ say "Hhhhh..."
    
    mishka @ say "Y-yeah, I'm okay..."

    n "You look back to where the lightning struck."
    n "There's a tree split in half and glowing red hot about 30 feet away."
    n "It wasn't as close as you thought but still pretty close."

    mishka @ say "We'd probably be dead if it was any closer."

    player "Yeah... I think that's enough walking around in the storm for today."
    
    show mishka hat depressed

    mishka @ say "My place isn't far from here. We can stay there if you want."

    player "Yeah, that's a good idea."

    scene bg black with fade

    n "You hurried back to Mishka's apartment and got out of your soaking wet jackets, shivering."
    n "You were shivering from the cold but you think Mishka was still shaken up by the lightning strike."
    n "She became a lot quieter and less responsive."
    n "You made some coffee that went untouched as the two of you fell asleep in each other's arms."

    stop music fadeout 1

    jump posttimeskip

    ######add another minidate before time skip
    #another abandoned hospital scene with ava
    #rori
    #claire


label posttimeskip:
    #ACT 2
    ### include some more scenes between your date and this time skip
    ###make a background that says 1 month later, hold on it for a second
    #month long time skip
    #sunday10/tuesday10

    scene bg codadorm with fade
    
    play music "audio/ambient/morning birds.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    if dating == "rori":
        n "It's been about a month since you started dating Rori."
        n "You've made it a weekly thing to play video games, usually at your place."
        n "Today however, you're going to be playing at a local tournament."
        n "More specifically, you're gonna be cheering Rori on as he competes in some fighting games there."
        n "You didn't even recognize some of the more obscure Japanese fighting games on the list but he seemed really excited about it."

        scene bg tournament with fade

        show box with Dissolve(.2):
            ypos 0
        
        play music "audio/music/vylet - Spark.ogg" fadein .5

        #note the venue is actually just a classroom?
        n "Wow, there sure are a lot more people here than you thought there would be."
        n "It smells worse than a zoo in here. Especially near the Smash players."
        n "You watch as Rori's down to his last guy in Dragon Fighterz. He doesn't seem to be doing too well against his opponent."
        n "He's stuck blocking in the corner but his attempt to reverse the situation gets countered and ends with him getting knocked out."
        n "He sighs and sits back in his chair before giving his opponent a fist bump and unplugging his fight stick."

        show rori neutral at center with dissolve

        rori @ say "Welp. I'm out of the tournament."

        player "Aww, too bad."

        rori @ say "It's fine. There's a lot of really good players here! It's a lot different from the locals I played at back home."

        player "Well as long as you're having fun."

        show rori laugh
        
        rori @ say "I am!"
        
        show rori neutral
        
        rori @ say "Apparently the Melted Blood finals are already happening so I'm gonna go wanna watch that, then I'll help get Smash Sisters set up."

        n "Rori guides you to a small crowd formed around a laptop that's been broken in half sitting on top of a trash bin."
        n "Two guys are sitting on the floor with their fight sticks in their lap."

        player "This is the finals..?"

        rori @ say "Yup! The semi-finals were hosted in the restroom cause there wasn't enough space."

        n "You're suddenly glad you're not a Melted Blood player."
        n "You don't even understand what's happening on the screen and can barely hear the audio over the sound of the players mashing buttons."
        n "Rori seems to enjoy watching it though. You've noticed his cute little tail wags as he gets excited."
        n "Enticed by his tail wagging, you can't resist staring at his butt."
        n "You're too busy staring to notice when the match ends though."

        show rori at hop
        
        show rori laugh
        
        rori @ say "OOOOOOOHHHH!!!!"
        rori @ say "Did you see that?!"
        
        show rori neutral

        player "Huh? Oh uh yeah! Really nice Z-cancel into 4D counterair half super!"

        rori @ say "Were you even watching? It was obviously a three eighths super..."

        player "Nah, I was staring at your ass."
        
        show rori anxious

        rori @ say "Oh... my gosh [name]!"

        player "What? It was more interesting than the game!"
        
        show rori laugh

        rori @ say "Pfft haha okay whatever you say~"
        
        show rori neutral
        
        rori @ say "Just try to pay attention to the game when I'm winning the finals for Smash Sisters, okay?~"

        player "No promises~"

        rori @ say "Speaking of which, I'm gonna go help set that up now. Lot of heavy lifting CRTs."
        rori @ say "Why don't you grab some snacks for us before we start playing doubles?"

        player "Sure! See you in a bit!"

        n "Rori gives you a smooch before walking off to lift some ancient televisions while you wander off in search of food."
        
        stop music fadeout 1.0

        scene bg tournament with fade

        show box with Dissolve(.2):
            ypos 0
        
        play music "audio/music/vylet - the magic show hype part muffled.ogg"

        n "You manage to flag down Rori, who's worked up a sweat from moving those heavy old box TVs."
        n "You had snagged some chips and sodas from a vending machine and brought them over."
        n "You toss him a bag of pretzels and a can of bepis."

        show rori neutral at center with dissolve

        rori @ say "Thanks!"

        n "You crack open your sodas and snacks and sit back, relaxing until the tournament starts."

        rori @ say "You ready?"

        player "I think so? I've never really played on a competitive level so I'm not sure what to expect."

        rori @ say "Ah don't worry, doubles is a meme category anyway."
        rori @ say "I'll do all the heavy lifting. Just try not to hit me, cause friendly fire is enabled."
        rori @ say "Just try and have fun!"

        hide rori with dissolve

        n "Reassured by Rori's words, you proceed to your designated setup and plug in your controllers."
        n "Soon enough, two other guys come sit down next to you and start up the game."
        n "These sweaty tryhards pick up on the fact you're a filthy casual and absolutely thrash you, taking out all your lives early on and leaving Rori to fend for himself."
        n "He takes out a few of their lives on his own but it's really just unfair for him to go two vs one like this and even he can't last long on his own."

        show rori neutral at center with dissolve

        rori @ say "Pah... That was rough..."

        player "Sorry, I shouldn't have died so quickly."

        rori @ say "Nah, it's fine. I'm still havin' fun. Hopefully you are too!"

        player "Yeah! It's nice getting to play with you! I just hate that I'm dragging you down..."

        rori @ say "Don't even worry about it! Like I said, doubles is just for fun. I'll get a chance to kick some butt in singles."

        hide rori with dissolve

        n "You get to play one more game before losing and getting knocked out of the doubles tournament but Rori doesn't seem to mind."
        n "You stick around to watch the rest of the matches until it's time for singles to start."
        n "Rori convinced you to try competing in this bracket as well, even though you know you won't get far."
        n "As you predicted, you get knocked out two games in."
        n "Oh well, at least now you can go cheer Rori on without the stress of competing."
        n "You look around for his horns and waggly tail and spot him playing on a setup connected to the projector screen."

        player "Woo!! Go Rori!!!"

        n "Your cheers are for naught however, as he ultimately loses the match."
        n "He gives his opponent a fist bump then walks over to you."

        show rori neutral at center with dissolve

        rori @ say "Sup. Of course you start watching as soon as I start losing haha"

        player "Eh, I lost my first two games and now I'm out of the tournament. It's a lot harder when I don't have you to save my ass haha"

        rori @ say "Yeah, I guess we both have some training to do then, don't we!"

        player "I'd rather just go home and play something easy like Meinkraft."

        rori @ say "You know what, that sounds pretty good right about now!"

        hide rori with dissolve
        
        stop music fadeout 1.0

        n "You and Rori stick around to watch the rest of the tournament before heading back to his dorm and snuggling in bed while playing comfy games."

        scene bg black with fade

        hide box

        show bg calendar
        show tsunday at center
        with Dissolve(.5)

        pause .6
        show tforwardslash
        pause .2
        show tbackslash

        pause .7


    if dating == "claire":
        n "It's been about a month since you started dating Claire."
        n "She's a bit clingy and wants to spend time with you at every available opportunity, but she's also very sweet and you genuinely enjoy her company."
        n "Today she wants to go to the mall with you."
        n "You didn't really have a mall where you grew up so you're interested in seeing what it's like."
        n "When you were younger, TV shows always made them out to be the cool hangout spot for high schoolers."
        n "But then you got to high school and only the rich kids could afford to go anywhere other than the local convenience store."
        #n "You're excited to see what all the hype is about, but you're no stranger to disappointment so you keep your expectations low."
        n "So you're excited to see what all the hype is about."
        
        stop music fadeout 1.0

        scene bg mall with fade

        #play music "audio/music/ai7.ogg" fadein 1.0
        #change to rarity 3am? or manehattens finest
        #play music "audio/exports/Rarity Sipping A Capuccino At Some 24 Hour Coffee Shop At 3am.opus"
        play music "audio/music/vylet - manehattan's finest.ogg" fadein 1.5

        show box with Dissolve(.2):
            ypos 0

        #n "Claire gave you a quick walkthrough of the place and you have to admit you're just as disappointed as you expected to be."
        n "When you arrive, it feels like you've stepped into some sort of corporate cemetary full of zombies trudging from shop to shop to look at cheaply made goods."
        n "It's not at all like how TV shows portrayed it."

        show claire outdoors neutral at center with dissolve

        claire @ say "You said this is the first time you've ever been to a mall, right?"
        claire @ say "Well, what do you think??"

        player "It's, uh... nice."
        
        show claire outdoors derp

        claire @ say "I know, it kinda sucks. They aren't what they used to be."

        player "I haven't seen a single person who looks happy to be here."

        #where's the carousel? claire wants to ride it but it's broken down?
        
        show claire outdoors sad

        claire @ say "I remember them being so lively..."
        claire @ say "I guess online shopping kind of killed the sense of wonder of going to the store and seeing what they had."
        claire @ say "Now you can easily find whatever you want on the internet for cheaper than they have it here."
        
        show claire at shudder
        
        claire @ say "Ohmygosh[name]I'msooooooosorrythisdatesucks!!!"

        n "Claire looks like she's about to cry. You need to defuse this before she causes a scene."

        player "Hey, it's not that bad! There's some neat shops I wanted to check out?"
        
        show claire outdoors surprised

        claire @ say "O-oh yeah?"

        player "Yeah, there's umm..."

        menu:
            player "{cps=0}Yeah, there's umm...{/cps=0}"
            "Thot Topic":
                player "There's that goth store."

                claire @ say "You mean Thot Topic?"

                player "Yeah, that's the one! I saw some shirts in the window that looked kinda cool."
                
                show claire outdoors heyeah

                claire @ say "Ohmygosh let's go then!!!"

                hide claire with dissolve

                n "Claire drags you up the escalator to the second floor and into the shop, where some edgy teens are loitering around."
                n "It smells like cheap goth perfume in here."

                show claire outdoors neutral at center with dissolve

                claire @ say "I remember buying so many hoodies from here in middle school!"

                player "Really? You had an edgy phase?"

                claire @ say "Yup! All throughout middle school and even a little during high school!"
                
                show claire outdoors embarassed
                
                claire @ say "I wanted to dye my fur all black but my parents wouldn't let me."
                
                show claire outdoors sad
                
                claire @ say "Ah, all those emo rock anime AMVs, lost like tears in the rain..."
                #claire @ say "I spent hours blasting Lincoln Park AMVs at max volume after school every day ahahaha!"

                player "Wow. I never would have expected you to be that type."
                
                show claire outdoors derp
                
                claire @ say "Everybody has their dark secrets, [name]."
                
                show claire outdoors lusty
                
                claire @ say "I wonder what yours are~"

                player "U-um well, we don't really have to talk about middle school..."
                
                show claire outdoors derp

                claire @ say "Ksksksks alright, if you insist~"
                
                show claire outdoors lusty
                
                claire @ say "But I'll find out, someday!~"

                n "You spend some time flipping through shirts with enough pop culture references to make you physically cringe before settling on just buying some pockey to snack on with Claire."

            "The arcade":
                player "Did I see an actual arcade back there? I thought those went extinct."
                
                show claire outdoors embarassed

                claire @ say "Oh yeah, I used to love going to those! I was a beast at Dance Dance Rebellion!"

                player "I've never played it. I never had an arcade where I grew up even though I thought they were the coolest shit."
                
                show claire outdoors heyeah

                claire @ say "Let's go see if it's still open then!"

                hide claire with dissolve

                n "Claire grabs your hand and drags you across the mall to the dark arcade tucked away in the corner."
                
                play music "audio/music/Vylet Pony - ANTONYMPH (Instrumental) muffled.ogg"
                
                n "It looks abandoned save for the lone clerk at the counter exchanging money for tokens."
                n "You slide a twenty dollar bill his way and get a stack of tokens in return."
                n "Claire wants to hop on the DDR machine first and tries putting in the tokens so hastily she drops some."

                show claire outdoors neutral at center with dissolve

                claire @ say "Woops! Don't worry, I'll pick those up in a minute."
                claire @ say "Which song do you wanna play?"

                n "You obviously don't recognize any of them so you scroll through the list at random, tapping your foot on the dance pad until you find one that sounds catchy."
                n "You set your game to easy mode while Claire has hers on insane."

                claire @ say "Come on [name], at least pick normal mode! Don't ya wanna impress your girlfriend with your dance moves?"

                player "Hey wait, I've never played this game before!"

                n "Claire steps on your mat and selects normal mode for you and hits start."
                n "Almost immediately you're hit with a barrage of arrows that you have difficulty even hitting a fair rank on."
                #n "WTF this is harder than those videos make it seem"
                
                show claire at flipright
                
                pause .25
                
                show claire at flipleft
                
                pause .25
                
                show claire with MoveTransition(.15):
                    xpos -50
                
                pause .25
                
                show claire at shudder
                
                pause .15
                
                show claire at flipright
                
                pause .25
                
                show claire at flipleft
                
                pause .25
                
                show claire at flipright
                
                pause .25
                
                show claire with MoveTransition(.15):
                    xpos 25
                    
                pause .25
                    
                show claire at flipleft
                
                pause .25
                
                show claire at flipright
                
                pause .25
                
                n "You look over to Claire's side and her screen is covered in arrows but she seems to have no problem, lightly tapping her feet to each one as she holds herself up by the bar on the back of the machine."
                
                show claire outdoors embarassed

                claire @ say "What's the matter [name]? Can't dance?"

                n "She's panting hard but clearly having a blast. You get the feeling she's even showing off a little when she starts tapping the notes on your dance pad for you."
                #n "By the end of the first song, you're both panting."

                claire @ say "Hah... whew... I haven't had a workout like that in a while!"

                player "Yeah that was more fun and more exercise I've had in years!"
                
                show claire outdoors neutral

                claire @ say "...Wanna play another song?"

                player "Heck yes!"

                hide claire with dissolve

                n "You and Claire don't even play the other arcade machines, you just play DDR until you're out of tokens."
                
                stop music fadeout 1.0
                
                n "By the end of it, you're too exhausted to want to play the other games anyway."
                
                #play music "audio/exports/Rarity Sipping A Capuccino At Some 24 Hour Coffee Shop At 3am.opus"
                play music "audio/music/vylet - manehattan's finest.ogg" fadein 1.5

            #"Build a Bunny Workshop:"



        show claire outdoors neutral at center with dissolve

        claire @ say "Alright, we went somewhere you wanted to go, now it's my turn to pick a store!"

        n "You gulp, fearing you may have to stand around in a candle shop for the next couple of hours."

        player "I don't remember agreeing to that, but okay."

        claire @ say "Trust me, you'll enjoy it~"

        if fratsoro == "frat":
            n "Claire drags you off into a store you feel has no place in a mall where anybody can see you: the lingerie store."

            show claire outdoors neutral at center with dissolve

            claire @ say "What's wrong [name]? Why are you blushing so hard? It's just a clothing store."

            player "It's not just any clothing! It's... It's... sexy clothing!"
            player "I was raised with good Christian values! I can't even pass by the ladies' underwear section at Wallyworld without feeling awkward!"
            player "Where am I supposed to look without being accused of being a pervert?"

            n "You can see some of your classmates strolling outside the store through the window. You instantly dive behind a rack of panties to conceal yourself."
            n "Claire picks out a particularly skimpy pair from the stand and holds them up to your face."
            
            show claire outdoors lusty

            claire @ say "What do you think of these? Wouldn't I look cute in them? I don't think they have my size though ksksksks"

            n "She's clearly enjoying your suffering."

            n "Your bunny gf drags you throughout the store, holding up various frilly lingerie to her body and getting your input while you try not to get spotted by your classmates."

            hide claire with dissolve

        else:
            n "Claire drags you off into a type of store you thought was just a myth: the lingerie store."

            show claire outdoors neutral at center with dissolve
                #xzoom -1

            claire @ say "Hm? You alright?"

            player "Oh, it's just... I've never been in a store like this before. I didn't even know they existed really."
            
            show claire outdoors derp

            claire @ say "Ohhhh my gosh [name] we need to get you some cute lingerie today for sure!"

            n "She finds a lacey black pair of panties and proudly holds them up to you."
            
            show claire outdoors lusty

            claire @ say "What do you think of these?"

            player "For me or for you...?"
            
            show claire outdoors heyeah

            claire @ say "Girl, you think I could fit in these?"

            n "She hands them to you and they're surprisingly soft. You could get used to wearing somethign like this..."
            n "Claire then picks out a frilly deep purple bra and holds it up to her chest."
            
            show claire outdoors lusty

            claire @ say "How about this?"

            player "What? That won't fit me at all!"
            
            show claire outdoors heyeah

            claire @ say "For meeee, dummy!"

            player "Oh. Oh, yeah that'd look cute on you!"
            
            show claire outdoors embarassed

            claire @ say "I don't wanna look cute, I wanna look sexy for you!"

            player "You already look sexy!"

            claire @ say "Then I wanna look cute!"

            player "Oh my god, bitch make up your mind!"
            
            show claire outdoors lusty

            claire @ say "Ksksksks why don't you pick something out for me then~"

            hide claire with dissolve

            n "The two of you end up picking out underwear for each other, racking up quite a large bill."
            n "Claire insists on paying for it all. Probably to assert dominance."

        n "You hit up a few more stores while you're there before returning to campus and to your respective dorms."

        scene bg black with fade
        
        stop music fadeout 1.0

        hide box

        show bg calendar
        show tsunday at center
        with Dissolve(.5)

        pause .6
        show tforwardslash
        pause .2
        show tbackslash

        pause .7

        scene bg codadorm with fade

        show box with Dissolve(.2):
            ypos 0

        #n "###unfinished"

        ### claire tries sending you a pic of her in lingerie but it won't load. She says she'll just have to show you in person next time



    if dating == "ava":
        n "It's been about a month since you started dating Ava."
        n "You've begun hanging around campus more often, waiting for her to be done with class for the day instead of going straight home."
        n "You have to admit, it's pretty relaxing just sitting on a park bench and talking about how your day went with her."
        n "Some days you go on walks all over town and she takes a lot of selfies with you to post on pinstagram."
        n "It gets kind of tiring but it makes her happy so you go along with it."
        n "At least you've visited some pretty interesting places you otherwise never would have seen while she gets her photography practice in."
        n "Yesterday she invited you to go on yet another excursion with her today but she promises this one will be special."
        n "You wonder what she has in mind..."

        scene bg waterfall with fade

        play music "audio/music/vylet - Evening Trot.ogg" fadein 1.0

        show box with Dissolve(.2):
            ypos 0

        n "Ava insisted that you come with her so early in the morning the sun wasn't even up."
        n "She mentioned something about a 'golden hour' as the sun rises being the ideal time for photography."
        n "You weren't in any state to pay much attention to it, especially since you had to skip your morning coffee."
        n "But she did bring you out here to teach you how to use a camera so you try to memorize the basic functions of the device and noob shooting techniques she shows you."

        show ava typical neutral at center with dissolve

        ava @ say "...and if you want more of the image in focus, you have to stop down the aperture, but remember to adjust the shutter speed or ISO to compensate for the loss of light!"

        player "Uh... huh. And how do I do that again?"

        n "Ava presses a button and the screen turns on, showing a live view of what the lens sees."
        n "She then flicks a dial and the image becomes brighter or darker."

        ava @ say "See? Easy, right?"
        ava @ say "You're basically just balancing the amount of light you get against motion blur, depth of field, and noise."

        n "This seems a lot more complicated than just clicking a button like you thought it would be but you just nod your head like you know what she's saying."

        ava @ say "Go ahead and try taking some shots!"
        ava @ say "Remember to zoom with your feet, compose an interesting frame, adjust exposure and be very still when you press the shutter release button!"

        hide ava with dissolve

        n "You put your eye to the viewfinder and look around for something to shoot."
        n "Trying to remember all the steps at once while also trying to be creative in your shot is harder than it sounds."
        n "You end up settling for a boring shot of the waterfall with some rocks in the foreground."

        show ava typical neutral at center with dissolve

        player "How's this?"

        ava @ say "Lemme see."

        n "You hand the camera over to Ava and she checks out your shot on the screen."

        ava @ say "Not bad! It's exposed decently and it shows you put some thought into your composition."
        ava @ say "But let me show you a trick!"
        ava @ say "Try setting the shutter speed really low, to like a full second and take that same shot."
        ava @ say "You can close down the aperture to make up for the increased light while getting everything in focus too!"
        ava @ say "And remember you'll have to be *very* still cause every movement you make will just shake the frame."
        #  with Dissolve(.2)

        hide ava with dissolve

        n "You take back the camera and follow Ava's advice, holding your breath as you take the shot"
        n "The one second the shutter is open feels like ten as you try your best not to move."
        n "*Ka-chunk*"
        n "The shutter finally returns to its closed position and you can review your photo."
        n "The long exposure time blended the movement of the waterfall into long streaks of light. It looks like something you'd see on a calendar."

        show ava typical neutral at center with dissolve

        player "Huh. So that's how those pics are taken."

        ava @ say "Yup! Pretty neat, huh?"

        n "Ava shows you a few more tricks as you play around with her camera and you take some more shots of the surroundings until she suggests something else."
        
        show ava flattered

        ava @ say "Wanna take a few pics of me?"
        ava @ say "Usually I'm the one shooting others, but I've picked up a few poses I could try."

        player "Oh, sure!"
        
        show ava smile

        ava @ say "Sweet!"

        hide ava with dissolve

        n "Ava guides you along, doing most of the work in positioning herself, choosing where to stand relative to the available light and scenery."
        n "It starts out pretty tame, just her doing some midly artsy tasteful poses you might find on any art hoe's pinstagram."
        n "But then she kicks off her shoes and socks and flaps over to the big rock jutting out from the pond."

        show ava typical neutral at center with dissolve

        ava @ say "Hey, get a few shots of me up on this rock with the waterfall in the background!"
        ava @ say "That lens doesn't zoom very far so you'll have to get your feet wet!"

        hide ava with dissolve

        n "As you're carefully stepping into the freezing water, trying not to step on any pointy rocks, you suddenly feel something land on top of your head, obstructing your vision."
        
        scene bg black with dissolve
        
        n "You pull it away from your eyes."
        
        scene bg waterfall with dissolve
        
        show box with Dissolve(.2):
            ypos 0
        
        n "It's... Ava's shirt?"
        
        show ava twopiece pants smile at center with dissolve
        
        #n "You pull it off and look up to see your bird gf posing topless (in an artsy way of course) with a blush on her face."
        #she's turned away from you, covers her breasts with her wing
        
        #n "(((author's note, this scene needs to be rewritten. also just imagine ava is nude here because the art isn't done yet.)))"

        #show ava topless at center with dissolve

        ava @ say "Well? You gonna just stare or take some shots?"

        n "You pick your jaw up from off the ground and raise the camera to your eye, rapidly clicking the shutter button."
        n "Ava smirks, as you take dozens of pics of her from several angles."
        
        ava @ say "Easy there, don't fill up the SD card just yet!"
        
        player "I won't! Hold on..."
        
        n "The camera stopped responding. You look down to see if you maybe flipped a wrong switch or something."
        
        hide ava with dissolve
        
        n "Dammit why do they make these things so complicated? You just wanna press button and get picture of sexy bird."
        n "*Click*"
        n "Aha!"
        
        player "Fixed it!"
        player "Huh?"
        
        scene bg black with dissolve
        
        n "Once again your vision goes dark."
        
        scene bg waterfall with dissolve
        
        show box with Dissolve(.2):
            ypos 0
        
        n "You shake the fabric off your head, this time it was Ava's pants."
        
        show ava twopiece flattered at center with dissolve:
            xzoom -1
        
        ava @ say "Well? What do you think?"
        
        player "You're stunning~"
        
        show ava twopiece smile
        
        ava @ say "Breeeee~ Thanks~"
        ava @ say "Feel free to pose me any way you want~"
        
        n "You didn't bring a swimsuit but you wade into the water to get closer regardless as you have fun taking various shots."
        n "Ava assures you her camera is splashproof but you try not to get it too wet."
        n "After a while, Ava suggests something new."
        
        ava @ say "Hey..."
        ava @ say "I never thought I'd say this but"
        ava @ say "Wanna try some... nude photography?"
        
        player "Huh? Does me being nude help with my composition technique or something?"
        
        ava @ say "Hehe no, silly! I meant if *I* was nude!~"
        ava @ say "But you do have a point, perhaps it's only fair if we're both unclothed~"
        
        n "You can't believe your ears. How did you go from an internet-addicted shut-in loser to having girls eager to off their clothes in your presence in half a semester?"
        
        player "Aren't you afraid someone else will come and see you like this?"
        
        ava @ say "Oh I don't think anybody's coming out here this early in the morning. I'll know if anyone's coming from a mile away with my bird senses anyway!"
        ava @ say "We should have plenty of time to have some fun~"
        
        player "You mean, take artistic shots of natural beauty, right?"
        
        ava @ say "Of course!~"
        
        player "Well in that case..."
        
        n "You begin to strip out of your clothes, with Ava following suit."        

        scene bg waterfall with fade

        show box with Dissolve(.2):
            ypos 0

        n "Ava was a bit camera shy at first but you managed to get some interesting shots of her in between some lewd touching."
        n "Honestly you're surprised a slasher villain didn't come and ruin the fun by brutally murdering you."
        #if you did the old hospital thing
        #n "Wait, would Ava be into that?"
        n "You ended up filling Ava's 64GB SD card with shots, prompting you both to put your clothes back on and call it a day."

        show ava smile at center with dissolve

        ava @ say "Whew! I've never managed to fill up that card in a single outing before!"
        
        show ava suggestive
        
        ava @ say "Did you learn a thing or two about photography?"
        
        show ava smile

        player "I think so! It's a lot of fun when you have a pretty subject to shoot!"
        
        show ava flattered

        ava @ say "Heheh, and I guess it can be pretty fun to be on the other side of the lens sometimes too!"

        n "You and Ava begin the hike back to campus, chatting about future photo session ideas along the way."

        stop music fadeout 1.3

        scene bg black with fade

        hide box

        show bg calendar
        show tsunday at center
        with Dissolve(.5)

        pause .6
        show tforwardslash
        pause .2
        show tbackslash

        pause .7

        scene bg codadorm with fade

        show box with Dissolve(.2):
            ypos 0



    if dating == "rose":
        n "It's been a few weeks since you first started seeing Rose."
        n "You're not really sure if you're officially dating at this point but she's certainly warmed up to you by now."
        #n "And maybe that's all you need."
        #n "Is this what dating a goth is like?"
        n "At least now she doesn't always talk down on you and you've gotten her to smile a few more times."
        n "Twice a week you've been going to the library to work on your history project or to just study and do homework in her company."
        n "She makes you run around and do errands for her but sometimes she rewards you for your efforts and that's enough to keep you crawling back."
        n "First it started off with answers to the homework but last week she changed it up a bit."
        n "That moment has been stuck in your head since, playing on repeat."
        
        stop music fadeout 1.0

        scene bg library with fade
        
        #play music "audio/exports/【Music】That Feeling I Get in my Heart (ft. Namii) [GGCqMucK1Eo].opus"
        play music "audio/music/vylet - sleepless.ogg"

        show box with Dissolve(.2):
            ypos 0

        n "You're in the middle of reading a page long paragraph in your textbook over and over because you keep spacing out when Rose tugs on the earphone in your ear."
        n "She was generous enough to share them with you, one in your ear, the other in hers on the condition that she controlled the music."
        n "Which turned out to be a win-win for you because she's introduced you to some really interesting metal bands this way."
        n "You look up and take the earbud out to see what she has to say."

        show rose neutral at center with dissolve

        rose @ say "Hey. Go buy me a coffee."

        player "Buy your own damn coffee."
        
        show rose armscrossed smug

        rose @ say "Come on, I'll make it worth your while."

        player "You can't bribe me, I already have the answers for next week's homework."
        
        show rose armscrossed grin

        rose @ say "Is that so?"

        n "Rose gets up from her chair and leans in toward you."
        n "That devilish smirk on her face... She's up to something."
        n "Intrigued, but also terrified, you freeze up as she gently strokes your face with those claws of hers."
        n "How this tiny little raccoon can activate your fight or flight response so hard is impressive."
        n "You can feel her hot breath on your neck as her muzzle gets closer..."
        n "You nervously look around to see if anyone's watching as she tilts her head upward to plant her lips on your own."
        n "Your heart is pounding so goddamn fast right now, you lose all sense of time and forget about your surroundings."
        n "It literally feels like a dream, like your body is floating and nothing matters outside of this one thing."
        n "Reality comes rushing back to you hard once she pulls back though."

        rose @ say "How about now?"

        player "Y-yeah..."

        hide rose with dissolve

        n "You don't even consider refusing her now. You've learned what kind of coffee she likes at this point and you eagerly go to fetch a cup from the cafe for her."
        n "When you return, she acts like nothing even happened. She doesn't even thank you for buying her a drink."
        n "She just continues reading her book without looking up at you, occasionally taking sips."
        n "...You think you're in love."
        
        stop music fadeout 1.0

        scene bg codadorm with fade

        show box with Dissolve(.2):
            ypos 0

        n "Today's a bit special. Instead of going to the library like usual, Rose has invited you to tour the local history museum with her."
        n "You better leave soon, you don't wanna risk being late and pissing her off."

        scene bg museum with fade

        show box with Dissolve(.2):
            ypos 0

        show rose neutral at center with dissolve

        play music "audio/music/vylet - That Feeling I Get in my Heart.ogg" fadein 1.0

        rose @ say "Took you long enough."

        player "I'm ten minutes early!"

        rose @ say "Be twenty minutes early next time."

        n "You're not sure if she's joking. You shrug and get in line to buy admission tickets."

        player "So, I have a question."

        rose @ say "Shoot."

        player "Is this like a date?"

        show rose angry
        
        rose @ say "What? No!"

        player "I dunno, this kind of feels like a date to me."

        rose @ say "Well it's not!"

        #player "In that case, I'm only buying my own ticket."
        player "Why are we here then?"
        
        show rose neutral

        rose @ say "Because history is interesting and you should know more about it."

        player "Oh I get it, you want your [boygirlfriend] to be as knowledgable about the past as you."
        
        show rose furious

        rose @ say "That's not-!"
        
        hide rose with dissolve

        n "The line moves forward and it's your turn to buy tickets, interrupting Rose."

        #attendant is a monitor lizard lady

        attendant "Welcome to Harmonia's Museum of History!"
        attendant "We're currently running a special where couples get in for the price of one!"
        
        show rose neutral at center with dissolve

        rose @ say "We're not a coup-"

        n "You pull Rose into a side hug and hold her tight as she tries to escape."

        player "Yup! We're a couple! Here you go, keep the change!"

        n "You hand the attendant a bill and she hands back two tickets."

        attendant "Thank you and enjoy the museum!"

        player "Thanks!"

        n "You feign a smile and walk into the museum, gritting your teeth as Rose sinks her claws into your arm."
        n "When you're far enough away you release the rabid raccoon and hold her ticket out for her."
        
        show rose unimpressed

        rose @ say "NEVER do that again!"

        player "You're welcome. I just saved you twenty bucks!"
        
        show rose smug

        rose @ say "I would have made you pay it anyway."

        player "What, in exchange for another kiss? You're doing a pretty bad job of convincing me this isn't a date~"
        
        show rose armscrossed furious

        rose @ say "Hmph."

        n "Rose growls at you and turns her head away but continues walking alongside you."
        
        show rose armscrossed neutral
        
        n "Eventually she cools off enough to start pointing out things and explaining the history behind them."

        rose @ say "...You know what that thing is?"

        player "Uhh... A giant bell?"

        rose @ say "Yeah. You know why this town is called Harmonia?"

        player "Nope. Why?"

        rose @ say "Bells like those used to ring every day at noon here and play a little song."
        rose @ say "Travellers claimed they could always hear the town song before they could see the town, even if it wasn't around noon time."

        player "That's... kinda spooky."

        rose @ say "Well, there are tales of ghosts ringing the bells at night."

        player "Yeah, I can see why they took the bells down."

        rose @ say "That was actually because they were starting to get damaged and nobody bothered to put up new ones because of noise complaints."
        rose @ say "So now this one sits in this museum, gathering dust."
        
        player "What happened to the others?"
        
        rose @ say "Nobody knows. Probably got melted down or some private collector snatched them up."
        rose @ say "Well, we know one got lost in the river when they were transporting it."
        rose @ say "But nobody's been able to locate it."
        
        hide rose with dissolve

        n "Rose guides you around the rest of the museum, offering explanations and trivia for just about everything here."
        n "Of course a place as old and populated as Harmonia has a lot of history. You end up spending nearly the whole day touring the place with Rose."
        n "Her nerding out over historical artifacts overrides her need to be a bitch so it ends up being a rather pleasant experience."
        n "The sun is starting to go down by the time you finish covering everything."
        n "As you're on your way out, Rose grabs your arm."
        
        show rose flustered at center with dissolve

        rose @ say "Hey... Thanks for coming here with me."
        rose @ say "I don't really have anyone else who'd wanna join me for something like this and I didn't wanna come alone like some kind of loser."

        player "Oh it's no problem. I enjoyed it a lot actually."
        player "And what's wrong with going places by yourself? That doesn't make you a loser."

        n "Oh god, does it?"
        
        show rose grin

        rose @ say "I mean- I don't have a lot of friends so this kinda meant something to me."

        player "I get what you mean. I didn't have any friends before moving here."
        player "I was actually really excited to come here with you today. I hope we can do something like this again soon."

        rose @ say "Heh well... today doesn't have to end just yet you know."

        player "What do you mean?"

        #show rose unimpressed

        #rose @ say "*Sigh*"
        rose @ say "I can't believe I'm saying this..."
        
        show rose smug
        
        rose @ say "Wanna go back to your dorm and make out?"

        player "Did I hear that right? Am I dreaming?"
        
        show rose angry

        rose @ say "Don't make it weird! It's a simple yes or no question!"

        player "Hell yes! What are we waiting around here for? Let's go!"

        n "You grab hold of Rose's paw and speedwalk out of there back to your dorm while she pretends she doesn't actually like you."

        stop music fadeout 1.3

        scene bg codadorm with fade
        
        play music "audio/music/vylet - Rarity Dozing in a Coffee Shop at 1AM.opus"
        #play music "audio/exports/im sorry (apathy).opus"

        show box with Dissolve(.2):
            ypos 0

        n "You barely step foot in your dorm when Rose assaults you, climbing onto you with her sharp claws and kissing all over your neck and face."
        n "You hold her close to your body and make your way to your bed, falling onto your back."
        n "You stroke her soft fur while kissing her lips. Once again, time and space disappear and all that matters is here and now and her."
        n "Your heart feels like it's about to burst out of your chest and yet you're entirely calm."
        n "The two of you softly sigh and moan as you explore each others' bodies until she suddenly stops you."

        show rose neutral at center with dissolve

        rose @ say "Wait, there's something I should..."

        player "...?"

        rose @ say "Nevermind. It's not important."
        rose @ say "..."
        rose @ say "...Are you really into me?"

        player "I mean, yeah? You're the type of girl I've been fantasizing about for years."
        player "A dominant shortstack goth nerd... what's not to love?"

        show rose smug

        rose @ say "Psh."
        rose @ say "Well, if that's how you feel..."

        hide rose with dissolve

        n "Rose suddenly lunges for your throat, biting into it just enough to leave a mark."
        n "You gasp, freezing up as she nibbles your neck, leaving you feeling more vulnerable than you've ever felt in your life."
        n "And yet it feels amazing."
        n "...You're almost certain you're in love."
        
        stop music fadeout 1.0

        scene bg codadorm with fade

        show box with Dissolve(.2):
            ypos 0

        n "You're not sure how much time passed but you don't care. You had an incredible time with Rose up until the second she had to leave."
        n "You're pretty confident you'll have a chance to do this again soon though."
        n "...Is it morning already?!"
        n "You perform your usual morning routine but stop to check out the marks Rose left on your neck."
        n "Yeah, she's definitely a biter."
        n "Hopefully today will be cold enough so you can get by with a scarf..."

        scene bg black with fade

        hide box

        show bg calendar
        show tsunday at center
        with Dissolve(.5)

        pause .6
        show tforwardslash
        pause .2
        show tbackslash

        pause .7


    if dating == "mishka":
        n "It's been a few weeks since you started dating Mishka."
        n "You make a point to visit the cafe nearly every day and usually spend a couple hours there, studying and chatting."
        n "It's sort of become your second home."
        n "Oftentimes, you help Mishka clean up and close down the shop, then walk her to her apartment while holding hands."
        n "Right outside her apartment is where you kissed her the first time."
        n "It was a cold night, but you really didn't want to part ways just yet so you both stood out there talking until you ran out of things to say."
        n "That's when she suddenly stood on her tip toes and gave you a kiss on the lips before quickly saying goodbye and running into her apartment."
        n "For a rat, she sure is pretty mousey."
        n "You like that about her though."
        n "She's cute, modest, chill, and likes spending time with you without being clingy about it."
        n "And that's why you're excited to go to a local fair with her tonight."
        n "You're pretty sure she's excited too, but when you brought it up to her she started rambling in Ukrainian."
        n "Nevertheless you managed to arrange meeting her there tonight."

        scene bg fair with fade

        #play music "audio/ai13.ogg" fadein 1.0
        #play music "audio/music/vylet - Tranquility and Happiness.ogg" fadein 1.0
        play music "audio/music/vylet - Colourless.ogg" fadein 1.0
        #cozy pone

        show box with Dissolve(.2):
            ypos 0

        n "You made sure to arrive an hour early so you wouldn't keep her waiting, but it seems she had the same idea."

        show mishka ceremonial neutral at center with dissolve

        #n "It looks nice but it clashes pretty hard with the American styled fair."
        #n "Not to mention she's making you feel underdressed compared to her more formal attire."

        mishka @ say "[name]!!! Over here!"

        player "Hey Mishka! You look very nice!"
        #player "Hey Mishka! I like your hat! What is that style of hat called again?"

        mishka @ say "Thanks! I don't get many opportunities to put this on!"
        mishka @ say "But... now that I'm here... maybe it is I am overdressed?"
        #mishka @ say "Thanks! It's an ushanka. It keeps my ears nice and warm!"

        #player "Nah, don't worry about it. That just makes you the prettiest one here"
        #player "Nah, don't worry about it. That just makes you the fanciest one here"
        player "Nah, don't worry about it. That just means everyone else is a pleb."
        #player "Whatever it is, it looks cute on you."

        mishka @ say "Aww, you're so sweet [name]! You look nice too!"

        #mishka @ say "I'm not sure what that means but I'll take it as a compliment!"

        n "Mishka holds her paw out for you to grab as you walk over to the ticket station."
        n "As Volginova would want, you pay for both tickets."

        mishka @ say "I've never been to an American festival before... What is it you do here?"

        player "Well, this is more like a county fair than a festival."
        player "There's food and rides and games with prizes."

        mishka @ say "Ooh, that sounds nice!"

        player "Ever had fried orios before?"

        mishka @ say "Goodness, no! Who would do such a thing to a poor cookie?"

        player "Never underestimate American ingenuity, arrogance and ignorance."

        mishka @ say "Ah, damn you Americans and your obsession with to fry foods!"
        #mishka @ say "Hehe!"

        player "Ya wanna try some?"

        mishka @ say "Sure!"

        n "You track down a vendor and order a heart attack for the both of you."
        n "Mishka eyes the cookies with a mix of fascination and horror."
        n "She hesitantly grabs one and takes a bite."
        
        show mishka ceremonial happy

        mishka @ say "Aak! It's so sweet!"
        mishka @ say "I love it!"
        
        show mishka ceremonial neutral

        player "I know, right?"

        n "You walk around the fair while snacking on the calorie equivalent of a feast back in Mishka's home village until you come across a game with a prize Mishka is enamoured by."

        mishka @ say "Ohh, look at that! It's so adorable!"

        n "It's a plushie of a heart with an eye and arms and hands."
        n "It actually looks a little creepy but who are you to judge?"

        player "Want me to win it for you?"

        mishka @ say "Oh my gosh you can do that???"

        player "Heh, just watch!"

        n "You walk up to the booth and slide the attendant five bucks."
        n "That gets you three chances to try and shoot a target with a little pellet gun."
        n "Should be easy, right?"
        n "Mishka cheers you on as you shoulder the rifle and brace the stock against your cheek."

        mishka @ say "Good luck [name]! You can do it!!!"

        n "You take a deep breath and take aim. Slowly, you squeeze the trigger until it fires off the pellet."
        n "Miss!"
        n "That's ok, you've still got two more tries left, and now you know how this thing shoots. You'll get it this time."
        n "*Bang*"
        n "Another miss!"

        mishka @ say "You have to aim a little more upward, [name]."

        n "You adjust your aim and watch as the flimsy pellet flies in a random direction once you fire it."
        n "It's those damn fans beside the targets throwing off your shot! How are you supposed to land a hit with the wind pushing your pellet around like that?!"
        n "Determined to win a prize for Mishka, you pay another five dollars for another three shots and promptly miss the first two."

        mishka @ say "I wanna try! Let me have that!"

        n "With a defeated sigh you hand the rifle over to Mishka and try to guide her on how to hold it but she quickly shoulders it and fires off a shot."
        n "She actually hit the target!"

        player "Whoa! How'd you do that?"

        mishka @ say "I have some practice shooting from when I used to hunt back in my home country."

        player "What did you hunt?"

        mishka @ say "Bears mostly. I was on night duty to protect village."
        #mishka @ say "And every night someone was on duty to shoot bear from entering village."
        #I had to protect village from bear

        n "Mishka proudly accepts her prize and shows it off to you."

        mishka @ say "Look! Isn't it cute?"

        $ givePlushie = False

        menu:
            "Yeah!":
                $ givePlushie = True
                #she gives it to you in the end
                player "Yeah! I'm glad you were able to win it otherwise I might have been here all night trying to shoot that target haha!"

                n "Mishka surprises you with a sudden hug."

                mishka @ say "I'm glad you tried though!"
            "It's kinda creepy haha":
                #she keeps it
                player "It's kinda creepy looking haha..."

                mishka @ say "I like creepy things!"

                n "Mishka surprises you with a sudden hug."

                mishka @ say "Thank you so much for trying to win it for me!"

                player "Anytime~"

        n "You hug her back, reflecting on how lucky you are to be here with your affectionate rat girlfriend right now."

        hide mishka with dissolve

        n "You spend the rest of the evening trying out a few rides, getting lost in the hedge maze, and decided to end the night with a trip through the tunnel of love."
        n "Neither of you really know what to expect as you board the swan shaped boat thing."
        n "The cool water rapidly moves around it, spraying you with a light mist."

        player "Huh. I wonder why that sign says not to ride if you have heart problems."

        n "Slowly, the boat carries you into a pitch black tunnel..."

        stop music fadeout 1.3

        scene bg black with fade
        
        #play music "audio/exports/【Music】Kid ｜ Read Description [8AjuGs59A5k].opus" fadein 6.0
        #play music "audio/ambient/spooky.ogg" fadein 1.0

        n "You feel Mishka leaning on you as you're plunged into darkness."
        n "You wrap an arm around her and rest your head on top of hers, relaxing after a few hours of walking around."
        n "You stroke her cheek with your hand, gently pulling her in for a kiss when a wicked scream echoes throughout the tunnel."

        player "What the hell was that?"

        n "Suddenly lights flicker on and off, revealing short glimpses of strange and horrific creatures looming around you."
        n "They even threw in a few animatronics that appear to pounce at you, causing you to recoil and shrink in your seat, clinging to Mishka."
        n "She seems to be having a good time, giggling at everything while every other jumpscare gets a shriek out of you."
        #flicker spooky imagery on screen
        n "Eventually the horror ends and the tunnel goes back to being a calm ride in the dark."
        n "You sigh and finally relax, letting go of Mishka."

        mishka @ say "Hahaha did you have fun?"

        player "That... was not what I was expecting."

        mishka @ say "It was great! I wanna ride again!"

        player "It almost gave me a heart attack!"

        mishka @ say "Aww, you poor thing!"

        n "Mishka pulls you into a hug and kisses your cheek, making the ride worth it in the end."
        n "Soon though, you see a light at the end of the tunnel, indicating the ride is about to end."
        n "You stay prepared for any last minute jumpscares though."
        
        stop music fadeout 1.0

        scene bg fair with fade

        show box with Dissolve(.2):
            ypos 0

        n "You ended up going on the ride again, though Mishka practically had to beg you to get on it."
        n "Thankfully it's less scary the second time and you got more time to smooch on your rat gf."
        n "As the night comes to a close, you walk Mishka back to her apartment."

        stop music fadeout 1.3

        scene bg streets with fade

        show box with Dissolve(.2):
            ypos 0

        play music "audio/music/gymnopedies.ogg" 

        show mishka ceremonial neutral at center with dissolve

        mishka @ say "I had a wonderful night with you [name]!"

        player "So did I! I haven't been to a fair since like, middle school."
        
        show mishka ceremonial happy

        mishka @ say "I've never been to one at all before tonight!"
        
        show mishka ceremonial neutral

        player "I'm glad you enjoyed it! I've never had so much fun at one!"

        n "You continue chatting with her until you get to her apartment."

        if givePlushie == True:
            mishka @ say "Here! I want you to have this!"

            n "She holds out the heart plushie she won."

            player "Aww, you don't have to do that! You're the one who won it after all."

            mishka @ say "Yes but I wanted to give you something for giving me such a lovely night!"

            n "You take hold of the plushie."

            player "Well, if you insist~"

            mishka @ say "I've also got something else for you!"

            player "Hm? What's that?"

            n "Mishka takes hold of both of your hands and looks up at you with the starlight glimmering in her eyes."
            n "With a cute blush on her cheeks and an adorable little smile, she leans in and gives you a kiss that feels like it lasts forever."
            n "You close your eyes and kiss her back, wishing this moment would never end."
            n "All good things must come to an end however, and after a few seconds she stops standing on her tip toes, breaking the kiss."

            mishka @ say "[name]?"

            player "Yeah?"

            mishka @ say "I love you."

            player "I love you too!"

            n "You might have said that a bit too eagerly, because she breaks into a giggle fit."

            mishka @ say "I'll see you tomorrow at the cafe, ok?"

            player "Definitely!"

            mishka @ say "Goodnight!"

            player "Goodnight!"
            
            hide mishka with dissolve

            n "She turns and goes into her apartment, waving to you as she closes the door."
            n "You head back to your dorm, happier than you've ever been in your life."

            stop music fadeout 1.3

        else:
            n "When you reach the door, takes hold of both of your hands and looks up at you with the starlight glimmering in her eyes."
            n "With a cute blush on her cheeks and an adorable little smile, she leans in and gives you a kiss that feels like it lasts forever."
            n "You close your eyes and kiss her back, wishing this moment would never end."
            n "All good things must come to an end however, and after a few seconds she stops standing on her tip toes, breaking the kiss."

            mishka @ say "[name]?"

            player "Yeah?"

            mishka @ say "I love you."

            player "I love you too, Mishka."

            n "Mishka giggles and gives you another hug."

            mishka @ say "*Yaaaaawn*"
            mishka @ say "I wish this night wouldn't end, but I'm getting pretty sleepy..."

            n "Her yawn causes you to yawn as well. Come to think of it, it's been a long day and you're exhausted."

            player "Yeah... that'd be nice..."

            mishka @ say "Oh [name], you're sleepy too? Can you make it back to your dorm alright?"

            player "Huh? Oh yeah, I'll be fine, I- *yaaaaaawn*"

            mishka @ say "No no, this won't do, you'll never make it back! Why don't you spend the night here!"

            player "Mishka, that's the best idea ever. How did you get so smart?"

            mishka @ say "Hehehe come on [name], let's get you in bed."

            n "She takes your hand, leading you inside where you proceed to cuddle and have the best sleep of your life."

            stop music fadeout 1.3

            scene bg black with fade

            hide box

            show bg calendar
            show tsunday at center
            with Dissolve(.5)

            pause .6
            show tforwardslash
            pause .2
            show tbackslash

            pause .7

            #monday10

    scene bg classroom with fade

    #play music "audio/ai1.ogg" fadein 1.0
    play music "audio/music/mere - schooldaze.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0

    show rothbauer at center with dissolve


    if dating == "rose":
        rothbauer @ say "The class average on the last test was a 69."

        n "You hear a student on the other side of the room snicker."

        rothbauer @ say "Now, I'm not the kind of professor who enjoys failing students, but such a low average frightens me and should be a wake up call to some of you!"
        rothbauer @ say "However, two students did make a hundred! Good work, [name] and Rose!"
        rothbauer @ say "I'm especially impressed with your improvement, [name]! Did you hire a tutor by any chance?"

        n "The only reason you even passed was because of Rose's help."
        n "You look to her. She looks so proud she taught an idiot like you so well."
        
        show rose smug at center with dissolve:
            xpos -500
            xzoom -1

        rose @ say "[name] has been hitting the books at the library every week and that seems to help."
        #player "Well, I've been hitting the books at the library with Rose every week and that seems to help."
        
        show rose grin

        rothbauer @ say "Ah, I remember back in the day before we had television and internet to entertain ourselves, my friends and I practically lived at the library!"
        rothbauer @ say "It brings me joy to see students like you taking your studies seriously! Could I ask you two to consider joining the tutorship program?"

        #show rose neutral at center with dissolve:
            #xzoom -1
            #xpos -350
            
        show rose neutral

        rose @ say "Sorry, I'm too busy for that."

        rothbauer @ say "Ah, of course! I know you treat your studies like a full time job, Rose!"

        hide rose with dissolve

        rothbauer @ say "What about you, [name]? You had a pretty nasty quiz grade early in the semester."
        rothbauer @ say "I'd be happy to drop it if you helped improve the average score of this class with some good old fashioned tutoring sessions!"

        menu:
            rothbauer "{cps=0}I'd be happy to drop it if you helped improve the average score of this class with some good old fashioned tutoring sessions!{/cps}"
            "Sure":
                n "Ehh, you really don't wanna do this but you could bump your B average to an A this way which might impress Rose enough for her to..."

                player "Sure, I'll do it."

                rothbauer @ say "Excellent! Class, please work with [name] to organize a time and place to have a study session!"
                rothbauer @ say "This will be very helpful for the upcoming midterm. Thank you [name]!"
                rothbauer @ say "Now then... let's begin today's lesson, shall we?"

                n "You feel like you just got suckered into doing his job for him..."
                n "At the end of class, you get a bunch of people you've never talked to trying to get your phone number and saying when they're available like you'll remember."
            "lmao no":
                n "LOL you're not gonna do this boomer's job for him."
                n "These other students can sink or swim for all you care."
                n "Just get a cute raccoon gf who enjoys history more than she enjoys you, it's easy."

                player "Ehh, I think I'm busy as well. Sorry."

                rothbauer @ say "I see... In that case I guess the others will have to find a way to pick up the slack on their own."
                rothbauer @ say "Remember, the midterm is approaching and it will not go easy on you!"

                rothbauer @ say "Now then... let's begin today's lesson, shall we?"
    else:
        rothbauer @ say "Your tests results... leave much to be desired, class."
        rothbauer @ say "If you need me to slow down during lectures, please let me know. But you should also be reading the assigned chapters."
        rothbauer @ say "I'll give you a little tip, some of the questions are lifted directly from the book."

        n "Rothbauer hands back the tests from like a month ago."
        n "How long does it take to grade a multiple choice test?"
        n "He drops your packet down on your desk facing down. That's not a good sign."
        n "You lift the corner and peek at your grade."
        n "...Well, at least it's passing. Barely."

        rothbauer @ say "Good work as always Rose. Keep it up!"
        rothbauer @ say "Have you considered joining the tutorship program?"
        rothbauer @ say "It would be an excellent experience for you if you're aiming to be a history professor, and some of the other students could really use the help."

        n "Did he just glance your way?"

        show rose neutral at center with dissolve:
            xzoom -1
            xpos -550

        rose @ say "Sorry, I'm too busy for that."

        rothbauer @ say "Ah, of course! My star student must spend most of the day studying after all."
        rothbauer @ say "Oh well, I guess the others will have to find a way to pick up the slack on their own."
        rothbauer @ say "Now then... let's begin today's lesson, shall we?"

    scene bg lecturehall

    play music "audio/music/mere - schooldaze faster.ogg" fadein 1.5

    show herschel at center with dissolve

    show box with Dissolve(.2):
        ypos 0

    herschel @ say "Good day, class!"
    herschel @ say "I noticed the majority of you had some difficulty with last week's homework!"
    herschel @ say "So I decided to drop them from your grade and we'll be going over those lessons again today!"

    n "You can hear Gunner breathe a sigh of relief."

    herschel @ say "I really want you all to understand this chapter because if you don't, I can guarantee you'll fail this upcoming midterm!"
    herschel @ say "Now then, let's begin reviewing Bernoulli distributions..."

    show bg static2
    pause .02
    show bg lecturehall

    n "Yeah, you're gonna need to pay more attention in class from now on."

    stop music fadeout 1.3

    scene bg campus with fade

    play music "audio/ambient/outdoors people talking.ogg" fadein .5

    show box with Dissolve(.2):
        ypos 0

    show gunner neutral at center with dissolve

    player "At first I didn't think this class was too hard but now I completely empathize with you."

    gunner @ say "It's all cool, brah. At least I'm not the only one who thinks this stuff is hard."

    if dating == "ava":
        player "I was getting it for a while but then it just got too complicated and kept piling on more stuff."

        gunner @ say "Yeah... you wanna study together today?"

        player "Sorry, I'm kinda busy tonight... I'm supposed to help Ava with a photography thing."

        gunner @ say "Oh... that's cool. I'll get Rori to help me then. Hopefully you can find a tutor as well."

        player "Thanks but at the end of the day I'm not too worried about all these tests and shit."

        gunner @ say "That's a good attitude to have. Fuck midterms!"
        gunner @ say "We should build our own university with blackjack and hookers!"

        player "You might be onto something. You could probably learn probability by playing blackjack better than listening to Mrs. Herschel."

        gunner @ say "Hahaha ya think so?"
        gunner @ say "Anyway I gotta jet. See you later!"

        player "Later."

        gunner @ say "And good luck on these midterms, bro!"

        player "Same to you!"
    else:
        player "Yeah, you wanna study together today?"

        gunner @ say "Ooh, sorry I can't. I kinda have a date with Ava tonight."

        player "Is a date with Ava worth failing again?"

        gunner @ say "..."
        gunner @ say "......"
        gunner @ say "........."
        gunner @ say "Yes."

        player "Fair enough."

        gunner @ say "Don't worry though, I'll find time to study."

        n "Gunner's phone buzzes and he pulls it out to check it."

        gunner @ say "Oh that's her!"
        gunner @ say "I'll catch ya later [name], I gotta go meet up with Ava."

        player "Laters! Have fun!"

        stop music fadeout 1.3

    scene bg codadorm with fade

    if dating == "ellen":
        #tuesday10
        show box with Dissolve(.2):
            ypos 0

        n "It's been a few weeks since you first started regularly hanging out with Miss Ellen."
        n "Every now and then you see her up on the roof drinking or smoking and you join her to rant about life and stuff."
        n "Sometimes she straight up invites you to come with her after class."
        n "It's like therapy but cheaper and more fun."
        n "Today however, she surprised you with a visit at the cafe..."

        scene bg cafe with fade

        play music "audio/music/mere - coffeeLove.exe.ogg" fadein 1.0

        show box with Dissolve(.2):
            ypos 0

        show mishka teasing at center with dissolve

        mishka @ say "I'll have that ready for you shortly, [name]!"

        show mishka neutral at flipright

        mishka @ say "And what can I get for you, miss?"

        n "You step aside from the ordering counter and pull out your phone."

        ellen @ say "I'll have a cinnamon roll and a honey almond latte. Hot please~"

        mishka @ say "Sure thing!"

        hide mishka with dissolve

        n "Wait a minute, you recognize that voice! And that scent!"
        n "You turn to face who you thought was Miss Ellen but..."

        n "Is this just some student who happens to look, sound, and smell similar?"
        n "She notices you staring and grins."

        show ellen smug at center with dissolve

        ellen @ say "Heheheh"
        
        show ellen neutral
        
        ellen @ say "Hi there!"

        player "Do I know you?"
        
        show ellen laugh

        ellen @ say "Maybe~ I recently transferred here!"

        player "...How recently exactly?"
        
        show ellen smug
        
        ellen @ say "Hehehehe!"
        
        show ellen happy
        
        ellen @ say "Hey, you're pretty cute~ Wanna sit with me?"

        n "This is all too bizarre. It feels like a setup but you're intrigued enough to go along with it."

        player "Er, sure."

        n "You grab your drink from the pickup counter and find a table to sit at."
        
        show ellen neutral

        ellen @ say "Oh, I think you grabbed my drink by mistake, [name]."

        player "Huh. I don't recall giving you my name."

        ellen @ say "Ah, well I... overheard the barista say it~"

        player "Riiiight. And what did you say your name was again?"
        
        show ellen laugh

        ellen @ say "Ellen~"
        
        show ellen neutral

        player "..."
        player "Okay what the hell is going on?"

        #n "The girl giggles and takes off her hat for a moment to show you the hair bun done up under it."
        #she giggles and lifts the brim of her hat to show her eyes
        n "The girl giggles and lowers her rose tinted glasses for a moment."

        ellen @ say "It's me! Miss Ellen!"

        player "I knew it! Why are you dressed like a student??"
        
        show ellen annoyed

        ellen @ say "Keep your voice down! It's a disguise!"

        player "Why would you need a disguise?"

        show ellen proud

        ellen @ say "So I can do this without getting fired~"

        n "Miss Ellen leans across the table and plants a smooch right on your lips."

        show bg static3
        pause .02
        show bg cafe
        n "You're so shocked you don't know how to respond."
        n "Miss Ellen casually sits back down and takes a sip from her latte with a smirk."

        player "Miss Ellen, I don't-"
        
        show ellen neutral

        ellen @ say "It's just Ellen, hun~"

        player "*Ellen* I don't know if it' such a good idea for you to pose as a student and go around kissing other students."
        
        show ellen annoyed

        ellen @ say "Hey, don't act like I'm smooching just any students! This getup is just for you!"
        
        show ellen neutral
        
        ellen @ say "And why shouldn't I have some fun? I'm well into my 40s and so far today's been the most exhilerating day of my life!"
        ellen @ say "Why should I abide by society's rules? They're just holding me back. It's not like I'm hurting anyone."

        player "Are you high right now?"

        show ellen laugh

        ellen @ say "I don't think so."
        
        show ellen overjoyed
        
        ellen @ say "Why, you wanna skip class and smoke some weed?"

        n "This is horrifying. This lady has clearly lost her mind and is trying to relive some twisted idea of a college freshman's wild party life."
        n "Did you cause this? She wasn't acting like this a month ago and she seems to have developed a thing for you."
        
        show ellen neutral

        ellen @ say "Hey, come on, chill out. What's the worst that could happen?"

        player "Uh, you could get fired and I could get expelled?"

        ellen @ say "And?"

        player "And... uh..."

        ellen @ say "Exactly! Hun, who cares if that happens? I mean don't get me wrong, I'm not actively *trying* to get fired."
        ellen @ say "But it's not like I'm in love with my job either."
        ellen @ say "And you're gonna be dead soon anyway so I don't see why you bother coming to class in the first place unless you had a thing for one of your professors."

        player "I-"

        n "You can't even argue against that."

        player "There's no way that flimsy disguise is gonna work for more than a day."

        show ellen laugh

        ellen @ say "It worked on you, didn't it?"
        ellen @ say "If anyone asks, I'm Miss Ellen's neice."

        player "...Who happens to be named Ellen."

        show ellen smug

        ellen @ say "Yes."

        player "...This is just crazy enough to work."
        player "But what even is your end goal? Like, why are you doing this?"
        
        show ellen neutral

        ellen @ say "Cause I wanna relive my life the way I want to! I don't wanna be the old Miss Ellen who's too scared to live on the edge, just hiding on the sidelines wallowing in depression."
        ellen @ say "I wanna feel young and fresh again! Like the world is full of opportunities and all I have to do is reach out and grab onto them!"

        player "I thought you said all that was bullshit."
        
        show ellen proud

        ellen @ say "It is! But when you're young and confident you can make things happen!"
        ellen @ say "Plus, I've got the advantage of years of experience on my side~"

        player "So you're just gonna fake being young until you make it?"

        ellen @ say "Pretty much! Life gets real boring when you're old."
        ellen @ say "You can't go to wild parties anymore, people are too busy trying to climb the social ladder and spending time with their families instead of chasing their own dreams!"
        ellen @ say "And once I've had my fun, I can go back to being *Miss* Ellen like nothing ever happened and write a book about it."
        ellen @ say "So what do ya say? Wanna help an old girl out?"

        n "You sigh, knowing this is a horrendous idea."
        n "But she does kind of have a point. Your life is way too short to worry about the consequences of this."
        n "You suppose it's not any worse than getting drunk with your literature professor on the rooftop."
        n "And if she does decide to do something too wild, you'll be there to stop her."

        player "...Alright, fine. I'll play along. But I'm not gonna do anything with you that'll get me arrested."
        player "They said I only have about five years left in me. I ain't about to spend them rotting in jail."

        show ellen laugh

        ellen @ say "Deal! Thank you soooooo much [name]!"
        ellen @ say "I promise this'll be fun, for the both of us!"
        
        show ellen neutral

        n "Ellen's phone buzzes."

        ellen @ say "Oop, gotta go! I have to back to teaching in half an hour!"

        n "She stands up and grabs her backpack, bending over to give you a kiss on the cheek on her way out."

        hide ellen with dissolve

        n "This is definitely the strangest thing to have ever happened to you."
        n "As you go to throw away your cup, Mishka speaks up."

        show mishka nya at center with dissolve:
            xzoom -1

        mishka @ say "Who was that? Perhaps someone you know..?"

        player "Um, just someone from my high school."
        
        show mishka happy

        mishka @ say "Ooh, a girlfriend?~"

        player "Er, yeah, something like that. I guess."

        mishka @ say "Oh my gosh, how fortunate she transferred here then!"

        player "Yup, just my luck."

        stop music fadeout 1.3

        scene bg codadorm with fade

        show box with Dissolve(.2):
            ypos 0

        n "You could hardly focus in class, seeing Miss Ellen back to her normal self after posing as a student just half an hour earlier."
        n "Not that you really need to pay attention in literature anymore, since you've noticed her marking up your grades higher than you deserve."
        n "You have a feeling this won't end well."

        scene bg black with fade

        hide box

        show bg calendar
        show ttuesday at center
        with Dissolve(.5)

        pause .6
        show tforwardslash
        pause .2
        show tbackslash

        pause .7

        scene bg campus with fade
        
        play music "audio/music/vylet - Catching On.ogg" fadein 1.0

        show ellen neutral at offscreenright:
            yalign 0

        show box with Dissolve(.2):
            ypos 0

        #n "On your way to class you're stopped by a mysterious figure rolling past you on a skateboard."
        n "On your way to class you hear the sound of a skateboard rolling on the pavement approaching."

        ellen @ say "[name]!! Wait up!!!"

        show ellen neutral at offscreenleft with move:
            yalign 0

        #show text "{color=b6e4d6}[name]!! Wait up!!!{/color}":
            #ypos 46
            #xpos 900

        #show ellensay at offscreenleft with MoveTransition(delay=1.5)

        #hide text

        ellen @ say "How do I control this thing?!"
        gunner "{nw}"

        show ellen at offscreenright with move:
            xzoom -1
            yalign 0

        n "Ellen zooms past you and promptly falls off her skateboard."

        show ellen laugh at center with dissolve:
            xpos 50

        ellen @ say "I'm alright!"
        
        show ellen neutral

        player "Ellen? What are you doing? Don't you have a class to teach?"

        ellen @ say "I took the day off to learn how to skateboard!"

        player "...Why?"

        ellen @ say "Cause that's what young folks do, right? Skip class and shred some asphalt!"

        player "Maybe if you're in middle or high school..."
        
        show ellen annoyed

        ellen @ say "Oh don't be such a stick in the mud! Come teach me how to board!"

        player "What makes you think I know how to skateboard?"

        show ellen laugh

        ellen @ say "In that case we can learn together!"

        player "Can't we do this later? I have classes to attend."

        show ellen proud

        ellen @ say "You'd rather sit in some stuffy classroom learning useless bullshit than have fun with me? Come on, we ain't gettin' any younger!"

        menu:
            ellen "{cps=0}You'd rather sit in some stuffy classroom learning useless bullshit than have fun with me? Come on, we ain't gettin' any younger!{/cps}"
            "I'm running low on sick days":
                player "I've skipped enough class and I'm kinda running low on sick days. I'll get expelled before my first semester is up at this rate."

                ellen @ say "Okay and?"
                ellen @ say "I fail to see the issue here."

                n "Ellen shoves the skateboard into your hands."

                show ellen laugh

                ellen @ say "Now take off that heavy backpack and do a kickflip for me!"

                n "Looks like she's not giving you any choice in the matter. You play along and set your bag down and place the board on the ground before stepping on it."
            "Fine, let's do this":
                player "Fine, let's do this."

                show ellen laugh

                ellen @ say "That's the spirit!"

                n "You set your bag down and place the board on the ground before stepping on it."

        show ellen neutral

        n "You struggle to maintain your balance but you manage to stay on."

        player "I've never really ridden one of these things before..."

        ellen @ say "You're doing great! Lemme just give ya a push!"

        player "Miss Ellen wait!"

        hide ellen with dissolve

        n "She places her paws on your back and gives you a rough push, sending you rolling down the street before crashing into a trash can and being flung off onto the grass."
        n "You see stars for a while. When you come to, Ellen is standing over you."

        show ellen laugh at center with dissolve

        ellen @ say "Whoa! That was totally gnarly dude!"
        
        show ellen happy

        n "You're starting to regret this."
        n "But you have to admit, this skateboarding this is more exhilerating than anything else you've done at Harmonia."

        player "Where's the board? I wanna give it another shot."

        show ellen laugh

        ellen @ say "Haha no way, it's my turn! Now on your feet, soldier, and check this out!"

        show ellen neutral

        n "Ellen helps you up before grabbing the board and standing on it. She moves one foot to the back edge of the board and stomps down, sending it and herself a few inches into the air."

        ellen @ say "Pretty sweet, huh?"

        player "Hell yeah! Show me how you did that!"

        show ellen laugh

        ellen @ say "Hahaha sure thing!"

        hide ellen with dissolve

        n "You and Ellen practice skateboarding until the sun starts to go down. Some students gave you strange looks but it doesn't matter cause you had fun."
        n "You even got to walk Ellen back to her car where you chatted some more before she gave you a parting smooch on the cheek."
        n "She even let you hold onto the skateboard for her until next time."

        show ellen laugh at center with dissolve

        ellen @ say "You better impress me next time I see you on that board!"

        player "No promises but I'll try!"

        ellen @ say "Hahaha alright then, see you in class tomorrow, cutie~"

        hide ellen with dissolve

        n "You wave as she drives away."
        n "Welp, nowhere to go now other than back to your dorm."
        
        stop music fadeout 1.0

        jump next01

    #wednesday10


    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0
    ###have a different scene if dating ellen?
    ###show her how to skateboard
    #skip class with her, choice to be hesitant or go for it
    #she asks if you've ever ridden a skateboard before, can say once, a few times or never
    #learn more about her during/after boarding
    n "You spent a few hours hanging out with [dating] after class before returning to your dorm for the day."

label next01:

    show bg static1
    pause .02
    show bg codadorm
    n "Dammit, you're tired but you have so much homework to do."
    n "You crack open a textbook and sit at your desk, trying to find where you left off while fishing through your bag for your pills."
    n "You forgot to take one earlier, so that's probably why you're not feeling too great."
    n "You throw your head back and swallow it dry."
    #n "Bartleby the scrivener was blah blah blah blah"
    show bg static3
    pause .02
    show bg codadorm
    pause .03
    show bg static1
    pause .02
    show bg static2
    pause .02
    show bg codadorm
    n "After studying for a while you realize you never actually took your pill. Damn, with all these midterms you almost forgot you're dying."
    show bg static1
    pause .02
    show bg codadorm
    n "You fill up a glass of water and swallow it."
    n "Fuck it, you'll take another one to make up for the one you missed earlier. That's how that works, right?"
    show bg static1
    pause .02
    show bg codadorm
    show bg static1
    pause .02
    show bg static2
    pause .02
    show bg static3
    pause .02
    show bg codadorm
    pause .05
    show bg static1
    pause .02
    show bg codadorm
    pause .04
    show bg static3
    pause .02
    show bg static1
    pause .02
    show bg static2
    pause .02
    show bg codadorm
    n "...the summation of a Fibonnaci sequence of arbitrary length blah blah blah... "
    n "Why is your skin so itchy? Allergies? Wait did you take your pills today?"
    n "Your body is probably just going through withdrawal or something since you've become so dependent on them, it expects one every few hours."
    n "You twist open the cap on the bottle and knock one back, chasing it down with a sip of water."


    show bg codadorm


    n "Ahh, much better."



    show bg codadorm

    n "Circa 400 AD, the Roman Empire saw bloody conflict as the subjugated classes, mostly comprised of anthromorphs though aided considerably by human benefactors..."

    show bg codadorm

    n "Goddammit you forgot to take your pills, didn't you? That's why you can't focus. Your hands are jittery and you knock over your water all over your textbooks as you reach for your pill bottle."
    n "You manage to get it open and down one without any water."
    n "Whew, that was a close one. Now you can get back to studying in peace. Where did you leave off?"

    show bg static3
    pause .03
    show bg static2
    pause .02
    show bg codadorm

    n "Parlais vous francais?"


    #sudden cut to codadorm night version
    show bg codadorm

    n "What the...?"
    n "It's as if time suddenly lunged forward a few hours."
    n "You feel strange... You're breathing heavily and you're sweating and you simultaneously feel beaten and more full of energy than you ever have before."
    n "Glancing down at your desk, you notice you have a book you don't even recognize open on it along with some gibberish scrawled in the margins."
    n "What happened and... and... what is... going... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on...? on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on...? on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on...? on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on...
    on... on... on... on... on... on... on......on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on... on..."
    #n "It's as if time has become heavy and is crushing you from all sides."

    #thursday10


    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    n "You wake up in bed feeling perfectly normal."
    n "What the hell happened last night? Was that all just a dream?"
    n "If it was, then why is your homework that you don't remember doing finished?"
    n "Could it be..."
    n "..."
    n "...ghosts?"
    n "Or aliens?"
    n "Or alien ghosts?"
    n "Maybe your phone could give you some hint."

    if dating == "mishka":
        n "You whip it out and see you've got some unread texts from Mishka."

        call phone_start from _call_phone_start_35

        call message_start("Mishka", "?", "mishkaavi.png") from _call_message_start_45

        call message("Mishka", "I don't understand ?", "mishkaavi.png") from _call_message_154
        call message("Mishka", "Is this some kind of american humors?", "mishkaavi.png") from _call_message_262
        call message("Mishka", "Haha", "mishkaavi.png") from _call_message_263
        call message("Mishka", "?", "mishkaavi.png") from _call_message_264

        call phone_end from _call_phone_end_39

        n "You hesitantly scroll up to see what it is you sent her."
        n "Oh god what is this"
        n "Several walls of text sent from you clutter the screen."
        n "As you rapidly scroll through it, you glean that it's some schizo rant about the Earth being flat, complete with sources."
        #n "Judging by the typos, you apparently typed this by hand."
        n "What the fuck is wrong with your brain?"
        n "You've never felt more embarrased in your life."
        n "You feel so bad for subjecting Mishka to this."
    if dating == "rose":
        n "You whip it out and check through your conversation history with Rose."
        n "Oh god what is this"
        n "Several walls of text sent from you clutter the screen."
        n "As you rapidly scroll through it, you glean that it's some schizo rant about the Earth being flat, complete with sources."
        #n "Judging by the typos, you apparently typed this by hand."
        n "What the fuck is wrong with your brain?"
        n "Your text bubbles are occasionally interrupted by replies from Rose."

        call phone_start from _call_phone_start_36

        call message_start("Rose", "?", "roseavi.png") from _call_message_start_46

        call message("Rose", "wtf", "roseavi.png") from _call_message_265
        call message("Rose", "stop", "roseavi.png") from _call_message_266
        call message("Rose", "stfu already", "roseavi.png") from _call_message_267
        call message("Rose", "doggammit I'm muting my phone for the night", "roseavi.png") from _call_message_268
        call message("Rose", "fuck you", "roseavi.png") from _call_message_269

        call phone_end from _call_phone_end_40

        n "You've never felt more embarrased in your life."
        n "You feel so bad for subjecting Rose to this."

    if dating == "claire":
        n "You whip it out and check through your conversation history with Claire."
        n "Oh god what is this"
        n "Several walls of text sent from you clutter the screen."
        n "As you rapidly scroll through it, you glean that it's some schizo rant about the Earth being flat, complete with sources."
        #n "Judging by the typos, you apparently typed this by hand."
        n "What the fuck is wrong with your brain?"
        n "Your text bubbles are occasionally interrupted by replies from Claire."

        call phone_start from _call_phone_start_37

        call message_start("Claire", "Uhh", "claireavi.png") from _call_message_start_47

        call message("Claire", "Lol?", "claireavi.png") from _call_message_270
        call message("Claire", "ok you can stop now", "claireavi.png") from _call_message_272
        call message("Claire", "please stop", "claireavi.png") from _call_message_273
        call message("Claire", ":C", "claireavi.png") from _call_message_274
        call message("Claire", "OMG shut up already!!!", "claireavi.png") from _call_message_275
        call message("Claire", "Earth is round!!!", "claireavi.png") from _call_message_436 
        call message("Claire", "Rounder than my boobs!!!!!", "claireavi.png") from _call_message_437 

        call phone_end from _call_phone_end_41

        n "You've never felt more embarrased in your life."
        n "You feel so bad for subjecting Claire to this."
    if dating == "ava":
        n "You whip it out and check through your conversation history with Ava."
        n "Oh god what is this"
        n "Several walls of text sent from you clutter the screen."
        n "As you rapidly scroll through it, you glean that it's some schizo rant about the Earth being flat, complete with sources."
        #n "Judging by the typos, you apparently typed this by hand."
        n "What the fuck is wrong with your brain?"

        call phone_start from _call_phone_start_38

        call message_start("Ava", "Uhh", "avaavi.png") from _call_message_start_48

        call message("Ava", "Wut", "avaavi.png") from _call_message_276
        call message("Ava", "is this a meme?", "avaavi.png") from _call_message_277
        call message("Ava", "am i getting epicly trolled?", "avaavi.png") from _call_message_278
        call message("Ava", "why are you so weird :v", "avaavi.png") from _call_message_279
        call message("Ava", "OMG shut up already!!!", "avaavi.png") from _call_message_280

        call phone_end from _call_phone_end_42

        n "You've never felt more embarrased in your life."
        n "You feel so bad for subjecting Ava to this."
    if dating == "ellen":
        n "You whip it out and check through your conversation history with Ava."

        call phone_start from _call_phone_start_39

        call message_start("Ellen", "WTF are you high right now", "ellenavi.png") from _call_message_start_49
        call message("Ellen", "without me??!", "ellenavi.png") from _call_message_281
        call message("Ellen", "...", "ellenavi.png") from _call_message_282
        call message("Ellen", "no, if you were high you'd be more intelligable than this", "ellenavi.png") from _call_message_283
        call message("Ellen", "I am so disappointed in you", "ellenavi.png") from _call_message_284
        call message("Ellen", "I'm tempted to fail you right now", "ellenavi.png") from _call_message_285
        call message("Ellen", "please never do that ever again", "ellenavi.png") from _call_message_286

        call phone_end from _call_phone_end_43

        n "You hesitantly scroll up to see what it is you sent her."
        n "Oh god what is this"
        n "Several walls of text sent from you clutter the screen."
        n "As you rapidly scroll through it, you glean that it's some schizo rant about the Earth being flat, complete with sources."
        #n "Judging by the typos, you apparently typed this by hand."
        n "What the fuck is wrong with your brain?"
        n "You've never felt more embarrased in your life."
        n "You feel so bad for subjecting Miss Ellen to this."
    if dating == "rori":
        n "You whip it out and check through your conversation history with Rori."
        n "Oh god what is this"
        n "Several walls of text sent from you clutter the screen."
        n "As you rapidly scroll through it, you glean that it's some schizo rant about the Earth being flat, complete with sources."
        #n "Judging by the typos, you apparently typed this by hand."
        n "What the fuck is wrong with your brain?"

        call phone_start from _call_phone_start_40

        call message_start("Rori", "k", "roriavi.png") from _call_message_start_50

        call phone_end from _call_phone_end_44

        n "Thankfully Rori seems to be immune to your psychotic trolling attempt."
        n "You've never felt more embarrased in your life."
        n "You feel so bad for subjecting Rori to this."

    n "That was so unlike you."
    n "You look over at your pill bottle and notice it's completely empty."
    n "Sweet raptor jesus, how many of those did you take last night?"
    n "It's not like you had many left but how are you not dead right now?"
    n "You're left with more questions than answers and no time to ponder them since class starts in fifteen minutes."
    n "You send a text saying you're sorry and were drunk and you'll never do it again before heading to class."

    scene bg lecturehall with fade

    show box with Dissolve(.2):
        ypos 0

    #play music "audio/ai21.ogg" fadein .5
    play music "audio/music/mere - retrograde.ogg" fadein .5

    show margaret neutral at center with dissolve

    ellen @ say "...and that about covers the review for Tuesday's midterm!"
    ellen @ say "Study hard and do your best! I wish you all good luck!"

    hide ellen with dissolve

    n "The other students pack their things and file out of the room, but as usual you stay behind to talk to Miss Ellen."

    show margaret neutral at center with dissolve

    n "Miss Ellen looks around to make sure there aren't any other students nearby."

    show margaret at flipright
    pause .8
    show margaret at flipleft:
        xzoom 1
    pause .5

    ellen @ say "Hey there [name]. I'm gonna be up on the roof in a minute if you wanna join me."

    player "I have to go to French next but I can be up there right after."

    show margaret sad

    ellen @ say "Aww, don't you wanna skip class to hang out with me?~"

    menu:
        ellen "{cps=0}Aww, don't you wanna skip class to hang out with me?~{/cps=0}"
        "I could do that":
            player "I could do that."
            
            show margaret neutral

            ellen @ say "Ya sure?"

            player "Yeah, that class isn't too hard. I can afford to miss a few days."

            show margaret neutral
            pause .1

            ellen @ say "In that case, what are we waiting for?"
            ellen @ say "Go ahead and get up there first so people don't see us walking in the hall together."

            player "Sure thing. See ya there, Ellen."

            n "She giggles every time you omit the \"Miss.\""

            if dating == "ellen":
                n "Sometimes you call her just Ellen during class just to fluster her."
                n "It works and it's cute."

            ellen @ say "Later~"

            scene bg roof with fade

            #play music "audio/ai20.ogg" fadein 1.0
            play music "audio/music/vylet - Evening Trot.ogg" fadein 1.0

            show box with Dissolve(.2):
                ypos 0

            n "You wait around for a few minutes, texting Claire with an excuse for missing class before Ellen shows up."
            n "Before even saying anything she pulls out her cigarettes and lights one up."

            show margaret smoking neutral at center with dissolve

            ellen @ say "Want one?"

        "I shouldn't...":
            player "I mean yeah but..."
            
            show margaret neutral

            ###change this, since now ellen and celestine are friends
            #ellen @ say "Ahh, I get it, you wouldn't wanna miss out on seeing... Mrs. Celestine, was it?"
            ellen @ say "Ahh I get it, you wouldn't wanna miss out on seeing Mrs. Celestine, huh?"
            ellen @ say "I saw her at Victorya's Secret the other day. She's got good taste in lingerie."

            player "Wh-what?! No, that's not what I-"

            show margaret neutral at hop

            pause .1
            
            show margaret happy

            #ellen @ say "No worries! I'll save ya a spot~"
            ellen @ say "Hehe I'm just teasin'! Don't worry, I'll stick around a while~"
            
            show margaret neutral
            
            ellen @ say "Go ahead and learn some French before coming up to the roof."
            ellen @ say "Just don't keep me waiting too long~"

            player "Sure thing. See ya there, Ellen."

            n "She giggles every time you omit the \"Miss.\""

            if dating == "ellen":
                n "Sometimes you call her just Ellen during class just to fluster her."
                n "It works and it's cute."

            ellen @ say "Later~"

            scene bg classroom with fade

            play music "audio/music/mere - retrograde.ogg" fadein .5

            show celestine neutral at center with dissolve

            show box with Dissolve(.2):
                ypos 0

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

                    show claire sweater neutral at center with dissolve:
                        xzoom -1
                        xpos -300

                    claire @ say "Mais oui!"

                    celestine @ say "C'est parfait!"

                    hide claire with dissolve

            celestine @ say "Let's begin a review of the semester so far, shall we?"

            hide celestine with dissolve

            if dating == "Claire":
                n "Claire's been helping you learn French \"in preparation for visiting France\" one day."
                n "You have to admit, you've started to enjoy hearing her speak French. It is the so-called language of love, after all."
                n "That and it can be incredibly sexy."
                ###in bad end, you visit france on your travels. when you come back to harmonia you can say if it was good or overrated

            n "Mrs. Celestine goes around the classroom asking questions in French to each student."
            n "Unsurprisingly, Claire has no trouble at all, whereas you have to take a few notes."

            stop music fadeout 1.3

            scene bg roof with fade

            #play music "audio/ai10.ogg" fadein 1.0
            play music "audio/music/Evan Schaeffer - Katje's Song.ogg" fadein 1.0

            show box with Dissolve(.2):
                ypos 0

            n "After class, you make your way back to the literature building to meet with Miss Ellen."
            n "You could already smell her cigarette smoke as you came up the stairway."

            show margaret smoking neutral at center with dissolve

            ellen @ say "Sup."

            player "Salut."
            player "I mean hey."
            player "Sorry, I guess I still have French on my mind."

            ellen @ say "It's cool. Want a cig?"

    player "Nah, I'm good. What's new?"

    ellen @ say "Getting ready for midterms is always a fun time."
    ellen @ say "I have to come up with new prompts every semester because we had a problem with students buying old essays."

    player "Wow, and here I thought I attended a nice university."

    ellen @ say "Don't be fooled, cheating is more commonplace than you'd think."
    ellen @ say "I've caught a few of your classmates cheating already."
    ellen @ say "I usually let it slide because it's too much work to do anything about it."
    ellen @ say "I'll make sure a student gets expelled if they so much as fail to cite a source correctly if I don't like them though."

    player "Huh, that's... scary."

    ellen @ say "I do always get excited to read students' essays though cause most of them are hilariously trash."

    player "Really? They're that bad?"

    ellen @ say "Oh they're awful! Most students fall into one of two categories."
    ellen @ say "There are the ones who can't construct an analysis to save their lives and usually miss the point of the prompt."
    ellen @ say "Then you've got the tryhards who bury their essay in so much academic fluff that they think I want to read. Those are even worse than the former."

    player "Which one am I?"

    ellen @ say "I don't know, I just pick a random number between 85 and 100 and write it on your papers without reading them."

    player "Are they that boring to you?"

    ellen @ say "You try grading 60 papers in a night."
    ellen @ say "Besides, I'm way more interested in our little conversations up here on the roof."
    ellen @ say "So how's your life been going?"

    player "Well, I'm not dead yet so that's a good sign."

    n "Ellen inhales the last bit from her cigarrete before throwing it to the ground and nodding."
    
    show margaret neutral -smoking

    ellen @ say "Yup. Same."

    player "Something weird happened last night though and I'm not sure if I should be concerned."
    player "I think I overdosed on these pills I'm taking to stay alive or something."

    ellen @ say "What? Why?"

    player "I dunno, I sat down to study and somehow lost consciousness while staying awake and time seemed to melt away and like..."
    player "It all feels like a dream now and I can barely remember it."

    show margaret sad

    ellen @ say "Hmm."
    ellen @ say "That is actually concerning."
    ellen @ say "Have you talked to your doctor about it?"

    player "Not yet."
    player "Honestly, I hate just the thought of talking to doctors."
    player "It's not like they're gonna magically cure me."
    player "If I have a choice between rotting away in a hospital bed hooked up to life support or just trying to live a normal life that'll be cut short whenever, I'd choose the latter."

    show margaret neutral

    ellen @ say "Yeah."
    ellen @ say "I don't blame you, if those doctors graduated from here they're probably full of shit."
    ellen @ say "Still though, you should get that checked out."
    #ellen @ say "You don't *always* have to suffer you know."
    ellen @ say "You can live your life without constant suffering you know."
    ellen @ say "Or at least try to."
    ellen @ say "You don't have to always let shit happen to you. Sometimes you can do something about it."

    player "I guess."

    n "You and Miss Ellen stand around silently for a while, just enjoying the scenery in each others' company until you decide to check your phone."

    player "Hey I've gotta go. I'm supposed to meet up with some friends at Coffee Zone in a bit."
    
    show margaret melancholy

    ellen @ say "Is that so?"
    
    show margaret happy
    
    ellen @ say "Well don't let me keep you!"
    
    show margaret neutral 
    
    ellen @ say "I'm gonna hang around up here for a while longer."

    player "See you later Ellen."
    player "And thanks for... well, you know."

    ellen @ say "Of course, hun."
    
    show margaret sad 
    
    ellen @ say "I'm a pretty lousy professor but at least I can make a difference to one of my students."
    ellen @ say "Even if it is just unlicensed therapy sessions on the roof."
    ellen @ say "And thank you for listening and being so open with me."

    hide ellen with dissolve

    n "You give her a hug before heading down the stairs."

    scene bg campus with dissolve

    show box with Dissolve(.2):
        ypos 0

    n "Back on the ground, you look up and see her on the edge of the roof waving down to you."
    n "You wave back and start making your way to the cafe."

    stop music fadeout 1.3

    scene bg cafe with fade

    play music "audio/music/mere - coffeeLove.exe.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0

    n "You show up to the cafe and see your friends already sitting at a table."

    if dating == "ellen":
        ##farleft with Dissolve(.2)
        gunner @ say "Hey [name]! Over here!"
        # farleft with Dissolve(.2)

        n "You wave and walk over. Looks like everone already bought drinks."

        show ava typical neutral at center:
            xzoom -1
            xpos -520
        show gunner neutral at center:
            xzoom -1
            xpos -700
        show claire sweater neutral at center:
            xpos 500
        show rori neutral at center:
            xpos 700
        with dissolve

        player "Hey guys, what's up?"

        claire @ say "Just waiting for you~"

        player "Ahh, sorry I'm late. Had to talk to my literature teacher about something."

        ava @ say "Well go ahead and order a drink [name]! We'll still be here!"

        player "Alright, be right back!"

        hide gunner
        hide ava
        hide rori
        hide claire
        with dissolve

        n "You walk up to the counter and see a familiar smiling face."

        show mishka neutral at center with dissolve

        mishka @ say "Vitannya [name]! I see you brought a lot of friends with you today!"

        player "Heh, yeah. They all barely fit on screen at once."

        mishka @ say "What can I get for you?"

        player "The usual."

        mishka @ say "Of course! I'll have that ready for you in just a minute!"

        player "Thanks!"

        hide mishka with dissolve

        n "You chat with your friends for a bit until Mishka calls your name."
        n "As you're carrying your drink back to the table, you see that somebody has taken your seat."

        show ellen laugh at center with dissolve

        ellen @ say "[name]! Hey! Fancy meeting you here!"
        
        show ellen neutral

        n "Before you can respond, she stands up and gives you a kiss on the cheek and steals your drink."

        player "Uh. Right. What a coincidence."

        show ava typical neutral at center:
            xzoom -1
            xpos -520
        show gunner neutral at center:
            xzoom -1
            xpos -700
        show claire sweater neutral at center:
            xpos 500
        show rori neutral at center:
            xpos 700
        with dissolve

        rori @ say "And who might this be, [name]? Your girlfriend?"

        ellen @ say "Yup! [name] and I went to high school together! I had no idea [heshe] was even attending Harmonia until I saw them a few days ago!"

        claire @ say "Wow, it must have been fate that you two would meet up again!"

        ellen @ say "Hehe, I know right?"

        n "She takes a sip of your coffee and looks back at you with a smirk."
        n "You pull up another seat and sit down."

        ava @ say "How come you never mentioned her to us, [name]! She's really cool!"

        gunner @ say "I don't think I've seen you around campus but... you do seem kinda familiar. Have we met before?"
        
        show ellen happy

        ellen @ say "O-oh umm... Probably not haha! I really don't go out that much and I'm usually the quiet kid in class!"

        gunner @ say "Oh... I could have sworn we had a class together last semester. Was it literature?"
        
        show ellen proud

        ellen @ say "Nope! This is my first semester here!"
        ellen @ say "Isn't that right, [name]?"

        n "Miss Ellen wraps an arm around you."

        player "Yeah."

        gunner @ say "Hmm. Well okay. I must just be misremembering. I did get a concussion from playing football last semester after all and sometimes I get deja vu."

        ellen @ say "Oh no! How did that happen?"

        gunner @ say "Well the grass was kinda wet cause it had been raining earlier that day and this big dude named Jeremy was on the other team and..."

        n "Gunner tells his story while Miss Ellen sips on your coffee and leans against you."
        n "Eventually you lighten up as everyone tells random stories and to your surprise everyone falls for Miss Ellen's student act."
        n "They actually seem to get along quite nicely."
        n "Maybe this isn't such a bad thing after all?"
        n "There really doesn't seem to be any harm in it. And it does kinda warm your heart whenever Miss Ellen rests her head on you."
        n "When it comes time to go back home, you wave goodbye to everyone except Miss Ellen who walks you back to your dorm."

        stop music fadeout 1.3

        #scene bg codadorm with fade

        #show box with Dissolve(.2):
        #ypos 0

        #n "###unfinished"

        # walks you back to your dorm, thanks you for letting her do this, whines she isn't ready to go back to teaching, asks if she can enjoy being a student for a while longer, if you say yes you get a bad end point (good miss ellen point) and sleep with her
    if dating == "mishka":
        player "Hey guys!"

        show ava typical neutral at center:
            xzoom -1
            xpos -520
        show gunner neutral at center:
            xzoom -1
            xpos -700
        show claire sweater neutral at center:
            xpos 500
        show rori neutral at center:
            xpos 700
        with dissolve
        
        gunner @ say "Sup [name]!"

        player "Hopefully I didn't keep you waiting too long."

        ava @ say "Nah we just got here a minute ago."

        claire @ say "We did order drinks without you though."

        player "I take it you didn't get me anything?"

        claire @ say "Nope! Sorry!"

        player "It's alright. Be right back."

        hide claire
        hide gunner
        hide ava
        hide rori
        with dissolve

        n "You walk over to the counter where Mishka is hard at work making drinks."

        show mishka neutral at center with dissolve

        player "Hey cutie. Come here often?"
        
        show mishka happy

        mishka @ say "Ohmygosh [name]! You startled me! Hahaha!"

        player "Heh sorry. How are things going?"
        
        show mishka neutral

        mishka @ say "Busier than normal!"
        
        show mishka nya
        
        mishka @ say "It always gets this way before midterms and finals though."

        player "Ah, would you hate me if I added one more order to the list?"
        
        show mishka silly wink

        mishka @ say "Of course not!"
        mishka @ say "Will it be the usual then?"

        player "As always."

        mishka @ say "No problem~"

        hide mishka with dissolve

        n "You hang around the counter chatting with Mishka as she finishes up everyone's drinks."
        n "When she's done, you and her grab hold of them all and carry them over to the table your friends are sitting at."

        show ava typical neutral at center:
            xzoom -1
            xpos -520
        show gunner neutral at center:
            xzoom -1
            xpos -700
        show claire sweater neutral at center:
            xpos 500
        show rori neutral at center:
            xpos 700
        show mishka neutral at center:
            xzoom -1
        with dissolve

        mishka @ say "Pryvit! Do you mind if I sit with you all?"

        ava @ say "Of course not!"

        mishka @ say "Dyakuyu!"

        n "Mishka passes out drinks before getting settled in a seat center next to yours."

        claire @ say "[name], aren't you two like, dating??"

        player "Yup!"
        
        show mishka silly wink

        n "You wrap an arm around your tiny rat gf and pull her in close."
        n "She responds by nuzzling your neck, her whiskers tickling you."
        
        show mishka neutral

        claire @ say "You're so cute together!"

        mishka @ say "Aww thanks~"

        n "You and Mishka take turns sipping from your coffee cup while just chatting with your friends and having a good time."
        n "Mishka's always been super friendly so it's no surprise everyone gets along with her."
        n "When it comes time to go back home, you wave goodbye to everyone except Mishka who walks you back to your dorm."

        stop music fadeout 1.0

        #scene bg codadorm with fade

        #show box with Dissolve(.2):
        #ypos 0

        #n "###unfinished"


        # Walk back to your dorm with her, invite her to sleep over (non sexually)
    if dating == "rose":
        player "Hey guys."

        show ava typical neutral at center:
            xzoom -1
            xpos -525
        show gunner neutral at center:
            xzoom -1
            xpos -725
        show rori neutral at center:
            xpos 450
        show claire sweater neutral at center:
            xpos 750
        with dissolve

        gunner @ say "Hey [name]! I thought you said you were gonna bring your gee eff?"

        n "Right on time, the door opens and Rose walks in. She looks around for you and hesitantly comes closer as she spots you and your group of friends."

        show rose neutral at center with dissolve:
            xzoom -1

        rose @ say "..."

        n "You smile and wrap an arm around her."

        player "Everyone, this is my girlfriend, Rose!"

        gunner @ say "Nice to meet you!"

        player "Go on, don't be shy."

        rose @ say "..."

        player "I promise she's not a feral raccoon I dressed up in a skirt, she's just shy."
        
        show rose angry

        rose @ say "I will bite your face off, [name]."

        player "Do it."

        n "Rose sighs and turns to your friends."
        
        show rose neutral at flipleft

        rose @ say "...Hey."
        
        show claire overjoyed

        claire @ say "Ohmygosh [name] your girlfriend is soooooo cute!!!"
        
        show rose flustered

        rose @ say "Wh-what?!"
        
        show claire sweater neutral
        
        show ava at hop

        ava @ say "Hi Rose! We're glad you could join us!"

        rori @ say "Heya! [name] told us all about you!"
        
        show rose neutral

        n "Rose narrows her eyes."

        rose @ say "What exactly did [heher] tell you?"

        player "Just that you're a huge history nerd and that you're into humans."

        show rose furious
        
        rose @ say "H-hey! Only one of those is true!"
        
        show claire derp

        claire @ say "Oh my goshhhhh you're so lucky Rose! You get to date the rarest species."
        
        show ava portrait neutral

        ava @ say "Sounds like someone's jealous~"
        
        show claire embarassed

        claire @ say "You bet I am!"

        player "Anyway, how about we go ahead and order some drinks?"

        hide rose
        hide ava
        hide claire
        hide rori
        hide gunner
        with dissolve

        n "Well, this is going better than you expected."
        n "You herd your friends over to the counter where Mishka greets you with a smile."

        show mishka neutral at center with dissolve:
            xzoom -1
            xpos -575

        mishka @ say "Vitannya [name]! My, you've got a large group with you today!"

        player "Heh, yeah. They all barely fit on screen at once."

        mishka @ say "What can I get for you?"

        player "The usual."

        show rose neutral at center with dissolve:
            xpos -150

        rose "Coffee as black as my soul."

        show claire sweater neutral at center with dissolve:
            xpos 225

        claire @ say "A pumpkin spice latte for me please! And could you put honey and salt on it too?"

        show ava typical neutral at center with dissolve:
            xpos 380

        ava @ say "I'll have a hazlenut cappucinno with whipped cream. Thanks!"

        show gunner neutral at center with dissolve:
            xpos 555

        gunner @ say "Can I get the mango passionfruit tea?"

        show rori neutral at center with dissolve:
            xpos 800

        rori @ say "Uhh... I'll take a hot cocoa please."

        player "Wha-? I'm not paying for all of you you know!"

        n "You stand there with your credit card crowded by all your friends, just trying to pay for your own drink."
        
        show claire sweater cry

        claire @ say "Aww..."

        show ava portrait neutral

        ava @ say "Oh! Haha woops!"

        gunner @ say "Fug, I don't get paid til next week."

        show rori anxious

        rori @ say "Ah dang, I left my wallet at home."
        
        show rose unimpressed
        
        rose @ say "You're at least paying for mine."

        n "Oh you know what, screw it. Your life's too short to worry about finances."

        player "Ughhhh fiiiine. Put it all on my bill."
        
        show claire sweater heyeah
        show rori laugh
        show ava overjoyed
        
        claire @ say "Yayyy!!!"

        n "Everyone (except Rose) thanks you and wanders back to the table to wait for their orders."

        hide ava
        hide claire
        hide gunner
        hide rori
        with dissolve
        
        show mishka overjoyed

        mishka @ say "Haha I guess your friends really rely on you, huh?"
        
        show mishka neutral
        show rose armscrossed neutral

        rose @ say "Seems more like they're taking advantage of you but whatever."

        player "It's cool. I really don't mind."

        rose @ say "Hmph. As long as you have enough for me I guess it doesn't matter."
        
        show rose armscrossed furious

        n "You pull Rose in close and give her a smooch on her furry head, to which she responds with trying to bite your nose off."

        player "Hey! Is that any way to thank someone who just bought you coffee?"
        
        show rose armscrossed smug

        rose @ say "Yes."
        
        show mishka silly wink

        n "You can see Mishka stifling a giggle while she works on your drinks."

        hide mishka
        hide rose
        with dissolve

        n "You and Rose head back to your table and hang out with the others, spending the next couple hours talking, joking, and hearing what's new in everyone's lives."
        n "Thankfully Rose restrains herself from assaulting you and it even looks like she has a good time."
        n "Your friends seem to enjoy her company as well and agree that you all should do this again sometime."
        n "When it comes time to go back home, you wave goodbye to everyone except Rose who walks you back to your dorm."

        stop music fadeout 1.0
        
        #scene bg codadorm with fade

        #show box with Dissolve(.2):
        #ypos 0

        #n "###unfinished"
        ###short rose conversation, she spends the night


    if dating == "rori":
        n "You wave and walk over. Looks like everone already bought drinks."

        show ava casual happy at center:
            xzoom -1
            xpos -520
        show gunner neutral at center:
            xzoom -1
            xpos -700
        show claire sweater neutral at center:
            xpos 500
        show rori neutral at center:
            xpos 700
        with dissolve

        hide box
        show box with Dissolve(.2):
            ypos 0
        
        player "Hey guys, what's up?"

        rori @ say "Hey [name]! Come have a seat! I already got you a drink."

        player "Thanks!"

        n "You give him a smooch on the cheek before sitting down and taking a sip."

        rori @ say "Aaaaaack hey!!!"

        player "Hey yourself, cutie."

        show claire sweater overjoyed

        claire @ say "Ohmygosh you two are so adorable!~"

        rori @ say "We are not!!"
        
        show claire sweater neutral

        player "Yes we are~"

        rori @ say "Ava and Gunner are the cuter couple! Go harass them about it!"

        n "All eyes turn toward the bird and cat."
        
        show ava casual concerned

        ava @ say "Wh-what?"

        claire @ say "What did I say! I knew you were into him ever since you first laid eyes on him!"
        
        show ava casual annoyed

        ava @ say "Oh shush up, you!"

        gunner @ say "No keep going, I wanna hear more."

        claire @ say "The first time we saw you she said you were cute~"

        ava @ say "You tricked me into saying that!"

        claire @ say "And then she was soooo checking you out at that party!"

        ava @ say "Claire I swear I will knock you out right here and now!"

        claire @ say "Ksksksks!~"

        n "As usual, Ava and Claire argue back and forth, much to your entertainment."
        n "Rori shows you memes on his phone while you sit back and enjoy the show."
        n "You could get used to hangouts like these happening more often."
        n "When it comes time to go back home, you wave goodbye to everyone except Rori who walks you back to your dorm."
        
        stop music fadeout 1.0

        #scene bg codadorm with fade

        #show box with Dissolve(.2):
        #ypos 0

        #n "###unfinished"


    if dating == "ava":
        n "You wave and walk over. Looks like everone already bought drinks."

        show rori neutral at center:
            xzoom -1
            xpos -400
        show gunner neutral at center:
            xzoom -1
            xpos -625
        show claire sweater neutral at center:
            xpos 700
        show ava casual happy at center:
            xpos 433
        with dissolve

        player "Hey guys, what's up?"
        
        show ava overjoyed

        ava @ say "Hey [name]! Come have a seat! I already got you a drink."
        
        show ava casual happy

        player "Thanks!"

        n "You give her a smooch on the cheek before sitting down and taking a sip."
        n "Her feathers puff up and she wraps a wing around you."

        claire @ say "Ohmygosh you two are so adorable together!~"

        #ava @ say "I know~"

        player "Ava's the cute one. I'm the uhh..."
        
        #show ava excited

        ava @ say "The cuter one!"
        
        show ava casual happy

        player "What? No!"
        
        show ava annoyed

        ava @ say "What? Yes!"

        player "Let's settle this with a vote. Who's cuter?"
        
        show ava casual happy

        claire @ say "You are, [name]!"

        gunner @ say "...Ava."

        rori @ say "I can't pick a side so I'm staying out of this!"
        
        show ava smile

        ava @ say "I guess it's a draw~"

        player "If you insist, but I still think you're cuter."
        
        show ava casual flattered
        
        ava @ say "Aww~"

        n "You and your newfound group of friends spend the next hour or so just chilling and talking about recent going ons in your lives."
        n "When it comes time to go back home, you wave goodbye to everyone except Ava who walks you back to your dorm."
        
        stop music fadeout 1.0

        #scene bg codadorm with fade

        #show box with Dissolve(.2):
        #ypos 0

        #n "###unfinished"

    if dating == "claire":
        ##farleft with Dissolve(.2)
        gunner @ say "Hey [name]! Over here!"
        # farleft with Dissolve(.2)

        n "You wave and walk over. Looks like everone already bought drinks."

        show ava typical neutral at center:
            xzoom -1
            xpos -500
        show gunner neutral at center:
            xzoom -1
            xpos -700
        show rori neutral at center:
            xpos 600
        with dissolve

        player "Hey guys."
        player "Where's Claire?"

        claire @ say "Right here!"

        show claire sweater neutral at center with dissolve

        n "Claire walks up from behind you and surprises you with a hug."
        n "Ava giggles and quickly snaps a photo of you, trapped in Claire's fluffy clutches."

        claire @ say "What's up y'all?"

        rori @ say "Just chillin' and sippin'~"

        claire @ say "[name]!! Let's get some drinks too!"

        player "Sure, just let me go first please."
        
        n "Claire releases you and you can finally breathe again."
        
        claire @ say "BRB right back~"

        #claire @ say "Only if you pay for mine~"

        #player "Deal."

        hide ava
        hide gunner
        hide rori
        hide claire
        with dissolve
        
        pause .25

        show claire sweater neutral at center:
            xpos 400
        show mishka neutral at center:
            xzoom -1
            xpos -400
        with dissolve

        mishka @ say "Vitannya, human! It looks like you've brought your bunny dyevushka with you today! How are you all?"

        player "We're doing well, how bout you?"
        
        show mishka cute

        mishka @ say "It gets a little busier here than normal when big tests are coming up, but I'm doing alright."

        claire @ say "Aww, hang in there!"
        
        show mishka happy

        mishka @ say "Hehe I will try! Anyway what can I get for you two lovelies?"
        
        show mishka neutral
        
        #claire @ say "An iced pumpkin spice caramel cappuccino with retrograde please~"
        claire @ say "I'll have an extra large oat milk mocha frappe with extra honey and salt please~"
        
        mishka @ say "And for you?"

        player "The usual."
        
        mishka @ say "Gotchya! I'll have it ready in just a minute!"

        player "Thanks Mishka!"
        
        show claire heyeah

        claire @ say "Yeah, you're the beeeeeeesssst!~ Ksksksks!"
        
        show mishka happy

        mishka @ say "Oh haha it's nothing, really! But thank you though~"

        hide mishka
        hide claire
        with dissolve

        n "You swipe your credit card through the machine and chat with Mishka while she makes your drinks."
        n "When you head back to your table, Claire snags the only remaining seat."

        show ava typical neutral at center:
            xzoom -1
            xpos -500
        show gunner neutral at center:
            xzoom -1
            xpos -700
        show rori neutral at center:
            xpos 600
        show claire sweater neutral at center
        with dissolve

        claire @ say "Oh noooo, where will you sit, [name]?"

        n "Your bunny gf snatches her drink from your hand, sipping on it with a smug expression while patting her lap."
        
        player "This again? How many lap sitting moments are we gonna have?"
        
        n "You roll your eyes and sit down in her lap like the sub that you are while the others snicker."

        player "Shut up, you're all just jealous you don't have a big booba blonde bunny gf!"

        gunner @ say "Yeah nah, I'm pretty happy with my petite qt art hoe bird gf."
        
        show ava annoyed

        ava @ say "Hey! I'm not an art hoe!"
        
        claire @ say "Yeah she's not freaky enough to be one."
        
        show ava unimpressedbrowless

        ava @ say "Huff. Anyway, what about you, Rori? Don't you have someone you're into?"

        rori @ say "Well uhh... no not really..."

        show claire sweater overjoyed at flipright

        claire @ say "Why don't you ask out Mishka!"
        
        rori @ say "Wh-what? Why her?"
        
        show claire sweater derp

        claire @ say "Cause you're both kinda quiet and shy but nice!"
        
        show claire neutral

        rori @ say "Y-yeah but... I don't even know her that well and I'm probably not her type!"

        gunner @ say "You never know if you don't try, bro!"

        n "You and your group of friends spend the next hour trying to convince Rori to ask Mishka out but in the end he chickens out."
        n "Oh well, maybe next time."

        n "When it comes time to go back home, you wave goodbye to everyone except Claire who walks you back to your dorm."

        stop music fadeout 1.3

        scene bg codadorm with fade

        show box with Dissolve(.2):
            ypos 0

        #n "###unfinished"

    #saturday11

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    if dating == "rori":
        n "A couple days later..."

        call phone_start from _call_phone_start_41

        call message_start("Rori", "Sup [name]! You ready for our date today?", "roriavi.png") from _call_message_start_51

        call reply_message("Yup! I'm just about to head out right now.") from _call_reply_message_110

        call message("Rori", "Sweet! See you in a little bit!", "roriavi.png") from _call_message_287

        call phone_end from _call_phone_end_45
    if dating == "rose":
        n "A couple days later..."

        call phone_start from _call_phone_start_42

        call message_start("Rose", "You ready for our date today?", "roseavi.png") from _call_message_start_52

        call reply_message("Yup! I'm just about to head out right now.") from _call_reply_message_198

        call message("Rose", "Well hurry up. I don't like being kept waiting.", "roseavi.png") from _call_message_288

        call phone_end from _call_phone_end_46
    if dating == "ava":
        n "A couple days later..."

        call phone_start from _call_phone_start_43

        call message_start("Ava", "Hii :> You ready for our date today?", "avaavi.png") from _call_message_start_53

        call reply_message("Yup! I'm just about to head out right now.") from _call_reply_message_199

        call message("Ava", "Don't keep me waiting!~", "avaavi.png") from _call_message_289

        call phone_end from _call_phone_end_47
    if dating == "claire":
        n "A couple days later..."

        call phone_start from _call_phone_start_44

        call message_start("Claire", "Hai!!!You ready for our date today?", "claireavi.png") from _call_message_start_54

        call reply_message("Yup! I'm just about to head out right now.") from _call_reply_message_200

        call message("Claire", "Sweet! See you there~", "claireavi.png") from _call_message_290

        call phone_end from _call_phone_end_48
    if dating == "ellen":
        n "A couple days later..."

        call phone_start from _call_phone_start_45

        call message_start("Ellen", "You ready for our date today?", "ellenavi.png") from _call_message_start_55

        call reply_message("I'm just about to head out right now.") from _call_reply_message_201

        call message("Ellen", "Don't be late!", "ellenavi.png") from _call_message_291

        call phone_end from _call_phone_end_49
    if dating == "mishka":
        n "A couple days later..."

        call phone_start from _call_phone_start_46

        call message_start("Mishka", "Hellooo ! Are you ready for our date today?", "mishkaavi.png") from _call_message_start_56

        call reply_message("Yup! I'm just about to head out right now.") from _call_reply_message_202

        call message("Mishka", "Yay! I'll meet you there <3", "mishkaavi.png") from _call_message_292

        call phone_end from _call_phone_end_50

        n "She sends you another message composed of a bunch of cyrillic characters, most of which your phone can't even render."

    n "You grab your jacket and speedwalk out the door, eager for your date."

    scene bg campus with fade

    play music "audio/music/vylet pony - aura.ogg" fadein 1.0

    show box with Dissolve(.2):
        ypos 0

    n "In your haste, you turn a corner and bump into someone, knocking you onto the ground."

    player "Oof!"

    show bg static1
    pause .03
    show bg static2
    pause .03
    show bg campus
    pause .05
    show bg static1
    pause .03
    show bg static2
    pause .03
    show bg campus with dissolve

    #jump credits

    jump trish1
    
    
label trish1:
    #show sayfarleft with Dissolve(.2)
    trish @ say "Oh my gosh are you okay???"
    #hide sayfarleft with Dissolve(.2)
    
    show trish neutral at center with dissolve:
        xzoom -1
    
    n "Standing over you is the fattest possum you've seen in your life."
    n "Even fatter than the one your cousin caught in his garage and kept as a pet."
    n "And she smells more like trash than your cousin's possum ever did."
    
    #menu:
        #"Tis nothing but a flesh wound.":
            #n "Before you can say something witty (or dumb), the possum pulls you up to your feet."
        #"Just a minor case of serious brain damage.":
            #n "Before you can say something witty (or dumb), the possum pulls you up to your feet."
    
    player "Uhh, sorry about that."
    
    n "You do a 360 and start to walk away but just end up bumping into her again."
    
    trish @ say "You alright there? Did you bump your head or something?"
    trish @ say "I bumped my head once really hard when I was little and since then I don't remember things too good anymore."
    trish @ say "Then again, I don't remember if I had good memory when I was little so maybe I was always like this."
    trish @ say "What did you say your name was again?"
    
    player "[name]. I'm a freshman here. I don't recall ever seeing you around."
    
    trish @ say "Hehe I guess you don't remember things either! We have so much in common!"
    trish @ say "My name's uhh...."
    trish @ say "Ummmmmm....."
    trish @ say "Oh yeah, it's Trish! Trish de la {a=https://4chan.org/trash/}Trash{/a}!"
    
    player "Well it was nice meeting you Trish but I really have to get going now so if you'll excuse me..."
    
    trish @ say "Wait a minute!!!"
    trish @ say "Are you sure you're okay?"
    
    player "Uhh yeah? I didn't hit the ground that hard."
    
    trish @ say "No, I mean you kinda have a sad aura around you."
    
    player "A sad aura?"
    
    trish @ say "Yeah! You look like you've got something weighing on you!"
    
    player "It's none of your business."
    
    trish @ say "Fine, keep your secrets hehe. Just know that things will get worse before they get better!"
    trish @ say "But in the end it's up to you to decide whether or not you'll come out stronger for it or be crushed."
    
    player "Uh sure, I'll keep that in mind."
    
    trish @ say "Do you believe people decide to hate you as soon as they meet you?"
    
    menu:
        trish "{cps=0}Do you believe people decide to hate you as soon as they meet you?{/cps}"
        "What?":
            player "What?"
            player "Where did that come from?"
            
            trish @ say "Sorry, it's a weird question, I know."
            trish @ say "I just meant like do you think you'll end up alone?"
            
            player "I've kinda always been alone until recently."
            
            trish @ say "Do you think it will last?"
            
            player "..."
            player "I'm not really sure."
            
            trish @ say "I'm a loner too!"
            trish @ say "I'm not sure why but people usually seem repulsed by me."
            trish @ say "I think people can sense auras. Y'know, like subconciously. And their subcon tells them to stay away from me."
            trish @ say "And when I bumped into you I read your aura and could tell you were a little different too."
            
            player "I guess I just give off doomer vibes."
            player "It's kind of a miracle I managed to find friends here at all."
            
            trish @ say "Are they really your friends?"
            
            player "What do you mean?"
            
            trish @ say "I thought I had friends once but it turned out that once I stopped being entertaining to them they turned on me."
            
            player "I'm sorry that happened to you."
            
            trish @ say "It's alright. I got really good at reading people afterward."
            trish @ say "I sense that you're a kindhearted person but you've got some darkness within that makes it difficult for others to connect with you."
            trish @ say "Not necessarily dark as in evil, just something holding you back."
            trish @ say "Hopefully you can tame it or conquer it or learn to live with it!"
            
            player "What a-"
            
            trish @ say "I know what you're gonna say. \'What a strange thing to say.\'"
            trish @ say "It doesn't matter if you believe me or not. I'm just saying what's on my mind."
            trish @ say "I'll let you go now. Enjoy your date!"
            
            #n "Trish waves goodbye to you and starts to walk away."
            
            player "See you around I guess."
    
            trish @ say "Byeeee!!!"
            
            n "She gives you a tight squeeze, no doubt rubbing her trashy smell off on you."
            n "Just what you needed before your date."
            n "As soon as she lets go, you hurry on out of there."
            #n "That possum was starting to creep you out."
            
            hide trish with dissolve
            
        
        "Yes":
            player "Yes? I mean, kinda?"
            player "What a strange thing to ask a stranger."
            
            trish @ say "There are strange people in this world. I guess I'm one of them. You appear to be one too!"
            
            player "How so?"
            
            trish @ say "You just said you think people hate you before getting to know you. That's not really a normal thought, now is it?"
            
            player "It's normal to me."
            player "But I guess I see your point. Normies don't really think about this sort of thing."
            
            trish @ say "It seems we have similar thoughts! I'm still investigating auras but I think people with alike thoughts will have comparable auras."
            trish @ say "Or perhaps it's the other way around. Maybe two people with the same aura will have the same thoughts."
            
            player "What the heck even is an aura?"
            
            trish @ say "It's kinda hard to define. It's a metaphysical property all sentient beings possess that influences your connections and pathways in life."
            trish @ say "I believe it's an evolved social mechanism."
            
            player "Sounds like something a schizophrenic would come up with."
            player "Tell me more."
            
            show trish at hop
            
            pause .15
            
            show trish at hop
            
            pause .25
            
            show trish at shudder
            
            trish @ say "Ohmygosh okay! *huff huff* Sorry I'm just getting really excited, not many people care to hear about my aura theories!"
            trish @ say "In fact, you're the first person I've talked to for this long at Harmonia!"
            trish @ say "Though I did kinda have to knock you out for this to happen."
            
            player "I forgive you."
            player "So what do you think my aura say about me?"
            
            trish @ say "I suspect you have an aura that repels most people but allows a few select ones through."
            trish @ say "You're like a black coffee! Bitter tasting and intolerable for most unless you dress it up with cream and sugar, but some people really prefer the bitterness!"
            
            player "I can be pretty bitter."
            player "So auras are like inherent personal biases we have towards types of people?"
            
            trish @ say "Yisssss!!!"
            trish @ say "Now you're getting it!"
            trish @ say "You might get along with another bitter aura because you're the same, or you might get along with a creamy aura because you pair well together!"
            trish @ say "But oftentimes the requirements are highly specific. You need a certain type of additive to go with a certain roast."
            
            player "That just sounds like a measure of how well people get along based on their personality."
            
            trish @ say "It does! But it's deeper than that."
            trish @ say "Now consider that someone doesn't have to taste a coffee to tell it's bitter. It's already in the air. They can smell it."
            trish @ say "They can smell your aura too. Not literally, this is just a metaphor."
            trish @ say "Your aura permeates into all aspects of your existence. Through walls, space, time, information systems like internets, possibly even across people you encounter..."
            trish @ say "The point is, someone can read your aura without ever knowing your personality."
            trish @ say "In fact your personality, or the one you present to others, doesn't have to match your aura!"
            trish @ say "You can have a sour aura and be a sweet person."
            
            player "That's... huh. So how are auras consciously perceived?"
            
            trish @ say "They're not!"
            trish @ say "At least not normally."
            trish @ say "I'm training to be proficient in reading auras but I still get them wrong all the time. I may even be completely wrong about you!"
            trish @ say "It's an underdeveloped scientific field of study that has been suppressed by governments because it has dangerous implications so I'm like a pioneer in researching this kinda stuff."
            
            player "Wow and it's totally not made up bullshit?"
            
            trish @ say "Nope! It's as real as the simulation we're living in!"
            trish @ say "That is to say, it's \'canon,\' whatever that means."
            
            player "And what exactly are the implications of auras being real?"
            
            trish @ say "It's tied to fate. Everyone has a fate but your aura determines how you reach it. It can even affect the final outcome to some degree!"
            trish @ say "It's true! I've seen it before!!!"
            trish @ say "I'm so excited to observe and research this phenomenon more! I'm collecting all my notes and working on a paper to publish once I have sufficient evidence."
            
            player "So it's all unproven theory as of now?"
            
            trish @ say "*Huff huff* sort of? Metaphysical interactions are kinda hard to prove real. It's like a black hole of information that has to be deduced."
            trish @ say "I'm getting a *strong* sense that your aura will be crucial for my research so I'm gonna start stalking you, k? Hope you don't mind!"
            
            player "Not at all."
            
            trish @ say "Hehehe see? Would you have said that to anybody else? I suspect our aura fields are operating in parallel, which tends to make the parties involved agree with each other."
            trish @ say "Almost hypnotically so, but that's another field of study I could go on all day about."
            
            player "Holy shit, you're right! It's almost like I had no choice but to agree. Like I was forced to and I had no say in the matter."
            
            trish @ say "Oh but you did! At one point in the past you could have nudged the timeline so we'd end up someplace else."
            trish @ say "But personally I believe our meeting was fated to happen regardless of circumstances."
            trish @ say "I'm sorry I took up so much of your time, I was just excited to talk about auras with someone who would listen."
            
            player "It's fine, it was really interesting to hear about!"
            
            #trish @ say "Hehe I'm glad! I have a feeling this won't be the last time we meet"
            trish @ say "Hehe I'm glad! I'll let you go for now, but I'll be keeping my eye on you."
            
            player "Thanks? I suppose it's fine if you observe me for your research. I'd like to see your findings on that."
            
            trish @ say "Thank you so much!! It's gonna be revolutionary!"
            
            n "Trish smiles gleefully and walks past you, drooling in excitement."
            
            show trish at offscreenright with move:
                yalign 0
            
            n "You hear her shouting to you after she's a few meters away."
            
            trish @ say "By the way, looking sharp. Have fun on your date!"
            
            player "Thanks!"
            
            n "Wait, how did she know about that?"
    
    #player "You sure it isn't just your sense of smell?"
    
    
    #later, rose talks about how she believes that given enough time, anybody would backstab her
    #the more you seclude yourself, the less people will sypathize with you
    
    jump cont1
    
label cont1:

    stop music fadeout 1.0

    play audio "audio/sound effects/vibrate.ogg"

    n "Goddammit what now"
    n "You dig your phone out of your pocket and feel your heart sink as you see who's calling."

    show phonecall at center with dissolve:
        xpos 700
        ypos 200

    n "Why now of all times?"

    stop music fadeout .5

    #menu:
        #"Answer phone":
    n "Hesitantly, you move your thumb over the answer button and tap it."

    player "Hello?"

    kitsuragi @ say "Hello, [name]?"

    player "Y-yes?"

    kitsuragi @ say "We've got the results back from some additional tests we've been running and..."

    player "And?"

    kitsuragi @ say "It's better to talk about it in person. Do you have a moment? It's pretty urgent."

    n "You let out a long sigh."

    player "I'll be right over."

    hide phonecall with dissolve

    n "You hang up and send your date a text saying you have to cancel your plans before changing direction toward the hospital."

    scene bg hospital with fade

    show kitsuragi at center with dissolve

    show box with Dissolve(.2):
        ypos 0

    play music "audio/music/gnossienne.ogg" fadein .5

    kitsuragi @ say "Thanks for coming in on such short notice. How are you feeling?"

    player "Honestly fed up with this bullshit."

    kitsuragi @ say "That's understandable. I hate interrupting your life like this but I wouldn't do it if it wasn't important."
    kitsuragi @ say "The field of medicine is constantly changing as we learn new things and I'm afraid a recent discovery will have to change the way we treat you."

    player "So you've been treating me wrong this whole time?"

    n "The kitsuragi sighs."

    kitsuragi @ say "Unfortunately, yes."
    kitsuragi @ say "Did you bring that pill bottle I gave you last time?"

    player "No, it's in my dorm."

    kitsuragi @ say "Well throw it out when you get back. There's evidence suggesting taking those will shorten your lifespan."

    player "What."
    player "The hell."

    kitsuragi @ say "Basically, the agreed upon theory is that the reason patients suffer from exhaustion is because their bodies are exerting themselves to stay alive for however long they've got left."
    kitsuragi @ say "The body only allocates enough resources for you to just stay awake, causing the drowsiness you felt."
    kitsuragi @ say "The pills we gave you overrode that, forcing your body to shift resources away from fighting the disease."

    player "Okay, so I've been killing myself faster for the past month. Great."
    player "So what have you got for me now?"

    kitsuragi @ say "Nothing."
    kitsuragi @ say "At this point we don't really have anything that can help you in any way. I'm sorry."

    player "So that's it, huh?"
    player "You come into my life to tell me I've got an incurable disease, then sell me a pill so I'm not a walking corpse, only to take it away because it turned out to be poison?!"
    player "You're lucky I don't have any family to sue you bastards into oblivion once I'm gone."
    player "Y'know I would have preferred not knowing I was gonna die like this. It would have been a nice little surprise just after finishing my degree, but at least I could have enjoyed the time I had."

    n "You're left out of breath by the time you're done ranting."
    n "The kitsuragi just stands there, her expression unchanging."
    n "Eventually she inhales to say something but you cut her off."

    player "Just shut up. Don't call me again unless you have a real cure."

    hide kitsuragi with dissolve

    n "You get up and leave the room. As you walk past the kitsuragi, you can see a hint of sympathy and regret in her eyes."
    n "Not that it matters."

    scene bg codadorm with fade

    show box with Dissolve(.2):
        ypos 0

    n "You stormed back to your dorm, ignoring the barrage of texts making your phone buzz every few minutes."
    n "This is unbelievable."
    n "Not only are you dying, but now you're doomed to be miserable fighting off the symptoms for the next few years."
    n "You recall the pathetic state your parents were in before they passed away. It was painful to watch, and it only got worse over time."
    n "What an undignified way to die. Not with a bang but the softest whimper you can imagine."
    n "Why did you ever think you could escape that fate?"
    n "You flump down in your bed and take a deep breath."
    n "That helped clear your mind a bit."
    n "You feel bad for blowing up on the kitsuragi earlier. Obviously none of this is her fault and it's not like she can even do anything. She's just the messenger relaying the terrible news."
    n "That reminds you, you owe your date an explanation for cancelling at the last second."
    n "Wait, this doesn't feel right."
    n "All of this doesn't feel right."
    n "Going to school, making friends, going out with [dating]..."
    n "It's all so pointless when you think about it."
    n "School is just wasting your time, and getting close to anybody when you don't have a potential future together is just cruel."
    n "And now that you're off those pills, you won't be pleasant to be around, even if you're in a good mood."
    n "You almost certainly would have broken up and moved on long before you're set to die, but you can't bring yourself to justify continuing a dead-end relationship."
    n "You're gonna call them and let them know it's over between you."
    n "Aaaargh god dammit fuck fuck fuck this so much"
    n "You don't wanna break up just as soon as you've started dating someone who actually means something to you!"
    n "But what choice do you have?"

    menu:
        n "{cps=0}But what choice do you have?{/cps}"
        "Break up":
            hide box
            show bg static1
            pause .03
            show bg static2
            pause .02
            show bg static3
            pause .03
            show bg codadorm
            pause .08
            show bg static1
            pause .03
            show bg static2
            pause .02
            show bg static3
            pause .03
            show bg static1
            pause .03
            show bg static2
            pause .02
            show bg static3
            pause .03
            show bg static1
            pause .03
            show bg static2
            pause .02
            show bg static3
            pause .03
        "Break up":
            hide box
            show bg static1
            pause .03
            show bg static2
            pause .02
            show bg static3
            pause .03
            show bg codadorm
            pause .08
            show bg static1
            pause .03
            show bg static2
            pause .02
            show bg static3
            pause .03
            show bg static1
            pause .03
            show bg static2
            pause .02
            show bg static3
            pause .03
            show bg static1
            pause .03
            show bg static2
            pause .02
            show bg static3
            pause .03

    jump ending

label ending:

    scene bg black with fade

    ###
    n "Thanks for playing!"
    n "More to come in a future update!"
    n "Credits in the about section on the main menu."
    n "sprite highlighting code: Sodora"
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
