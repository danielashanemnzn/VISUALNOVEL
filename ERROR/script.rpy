#The script of the game goes in this file.
# The script of the game goes in this file.
image 1 = "images/1.jpg" 
image 3 = "images/3.jpg"
image 4 = "images/4.jpg"
image 5 = "images/5.jpg"
image 6 = "images/6.jpg"
image 7 = "images/7.jpg"
image 8 = "images/8.jpg"
image 9 = "images/9.jpg"    
image 10 = "images/10.jpg"
image 11 = "images/11.jpg"
image 12 = "images/12.jpg"
image 13 = "images/13.jpg"
image 14 = "images/14.jpg"
image 15 = "images/15.jpg"

label splashscreen:
    scene black
    play music "audio/splash_music.mp3" fadein 1.0
    #show first image
    show 1 with fade
    pause 3.0
    hide 1 with dissolve

    #show second image
    show 2 with fade
    pause 3.0
    hide 2 with dissolve

    #show third image
    show 3 with fade
    pause 3.0
    hide 3 with dissolve

    #show fourth image
    show 4 with fade
    pause 3.0
    hide 4 with dissolve

    #show fifth image
    show 5 with fade
    pause 3.0
    hide 5 with dissolve

    #Show sixth image
    show 6 with fade
    pause 3.0
    hide 6 with dissolve

    #Show seventh image
    show 7 with fade
    pause 3.0
    hide 7 with dissolve

    #Show seventh image
    show 8 with fade
    pause 3.0
    hide 8 with dissolve

    #Show seventh image
    show 9 with fade
    pause 3.0
    hide 9 with dissolve

    #Show seventh image
    show 10 with fade
    pause 3.0
    hide 10 with dissolve

    # Show seventh image
    show 11 with fade
    pause 3.0
    hide 11 with dissolve

    #Show seventh image
    show 12 with fade
    pause 3.0
    hide 12 with dissolve

    # Show seventh image
    show 13 with fade
    pause 3.0
    hide 13 with dissolve

    # Show seventh image
    show 14 with fade
    pause 3.0
    hide 14 with dissolve

    # Show seventh image
    show 15 with fade
    pause 3.0
    hide 15 with dissolve
    
    #Fiction Disclaimer
    pause 1.0

    show text "They say school is just a chapter in life." with fade
    pause 4.0
    hide text with fade
    
    show text "But no one tells you how much living actually happens here—how the little moments slowly become the ones you’ll remember most." with fade
    pause 4.0
    hide text with fade
  
    show text "The first hellos. The awkward silences. The late-night cramming. The inside jokes that never made sense to anyone else." with fade
    pause 4.0
    hide text with fade

    show text "This campus, these hallways... they’re more than just a backdrop. They're where I laughed, struggled, grew—and became someone new." with fade
    pause 4.0
    hide text with fade
    
    show text "And while I don’t know where this story will take me, I know it starts here." with fade
    pause 4.0
    hide text with fade
   
    show text "Right now." with fade
    pause 4.0
    hide text with fade
  
    show text "So, let's begin—from the first step, to the final goodbye." with fade
    pause 4.0
    hide text with fade

    stop music fadeout 1.0
    return
# Declare characters used by this game. The color argument colorizes the
# name of the character.
default cool_mode_enabled = False

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
