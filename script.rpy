################################################################################
#  CHARACTER DEFINITIONS
################################################################################
define jus = Character("Justine", color="#e67e22", who_style="namebox")
define g   = Character("Guard",   color="#3498db", who_style="sec_namebox")
define kim = Character("Kim",     color="#e84393", who_style="sec_namebox")
define c   = Character("Carl",    color="#80c4ff")
define n = Character("Nurse", color="#E9967A")
define m = Character("Mae", color="#E23A32")
define s = Character("Sophie", color="#A23A32")
define l = Character("Lyn", color="#AB3A32" )
define e = Character("Ella", color= "#3A3AB4")
define v = Character("Vidal", color="#3A3AB4")

################################################################################
#  TRANSFORMS
################################################################################
transform justine_bottom_left:
    xalign 0.0        # left edge
    yalign 1.0        # bottom
    anchor (0.0, 1.0) # feet on the floor
    zoom 0.8          # tweak if she’s still too big

transform kim_bottom_right:
    xalign 0.75       # left edge
    yalign 1.05       # bottom
    anchor (0.0, 1.0) # feet on the floor
    zoom 0.8          # tweak if she’s still too big

transform justine_bottom_center:
    xalign 0.3     # left edge
    yalign 0.9       # bottom
    anchor (0.0, 1.0) # feet on the floor
    zoom 0.7          # tweak if she’s still too big

transform kim_bottom_center:
    xalign 0.5
    yalign 1.05
    anchor (0.05, 1.1)
    zoom 0.8

transform kim_bottom_left:
    xalign 0.2
    yalign 1.05
    anchor (0.05, 1.1)
    zoom 0.8

transform guard_bottom_right:
    xalign 0.75       # left edge
    yalign 1.1        # bottom
    anchor (0.0, 1.0) # feet on the floor
    zoom 0.8          # tweak if she’s still too big

transform mae_bottom_center:
    xalign 0.3     # left edge
    yalign 0.9       # bottom
    anchor (0.0, 1.0) # feet on the floor
    zoom 0.7          # tweak if she’s still too big

transform sophie_bottom_center:
    xalign 0.5
    yalign 0.9
    anchor (0.0, 1.0)

transform mae_bottom_left:
    xalign 0.0        # left edge
    yalign 1.0        # bottom
    anchor (0.0, 1.0) # feet on the floor
    zoom 0.7          # tweak if she’s still too big

################################################################################
#  IMAGE_DEFINITIONS+-
################################################################################

#_backgrounds__ (make sure these files exist in /game/images/)
image bg_gate              = "images/bg_gate.jpg"
image bg_after_school_gate = "images/after_school_gate.jpg"
image bg_pub_lib_door      = "images/pub_lib_door.jpg"
image bg_guard_house       = "images/guard_house.jpg"
image bg_room              = "images/bg_room.jpg"
image splash_bg            = "images/splash_bg.png"
image bg_far_view_entrance      = "images/FarViewofEntranceArea.jpg"
image bg_nearing_new_building   = "images/NearingNewBuilding.jpg"
image bg_tambayan_to_entrance   = "images/TambayanAreaGoingtoEntrance.jpg"
image bg_circle_area_lower_view = "images/CircleAreaLowerView.jpg"
image Enter_choice2 = "images/Enter_choice2.jpg"
image bg_entering_hideout      = "images/Entering_hideout.jpg"
image bg_closed_hideout_gate   = "images/Closed_hideout_area_gate.jpg"
image bg_entering_the_school_lobby = "images/entering_the_school_lobby.jpg"
image bg_pup_lobby = "images/pup_lobby.jpg"
image bg_informationdesk = "images/informationdesk.jpg"
image bg_window1 = "images/window1.jpg"
image floor1_hallwayright = "images/floor1_hallwayright.jpg"
image bg_acad = "images/acad.jpg"
image bg_midstair = "images/mid_boys_stairs.jpg"
image bg_lgbt1 = "images/lgbt_cr.jpg"
image bg_lgbt2 = "images/lgbt_door.jpg"
image bg_lgbt3 = "images/lgbt_halfway.jpg"
image bg_stair1 = "images/first_stair1.jpg"  
image bg_stair2= "images/first_stair2.jpg"
image bg_stair3= "images/first_stair3.jpg"
image bg_stair4= "images/first_stair4.jpg"
image floor1_midhallwayleft = "images/floor1_midhallwayleft.jpg"
image floor1_hallwayleft = "images/floor1_hallwayleft.jpg"

# __GARDEN__ and __EXIT__ (make sure these files exist in /game/imgaes/)
image bg_garden = "images/garden.jpg"
image bg_garden_cat = "images/view_cat.jpg"
image bg_garden1 = "images/garden1.jpg"
image bg_garden2 = "images/garden2.jpg"
image bg_garden3 = "images/garden3.jpg"
image bg_back_garden1 = "images/back_garden1.jpg"
image bg_exit1 = "images/exit1.jpg"
image bg_exit2 = "images/exit2.jpg"
image bg_exit3 = "images/exit3.jpg"
image bg_exit4 = "images/exit4.jpg"
image bg_exit5 = "images/exit5.jpg"
image bg_exit6 = "images/exit6.jpg"
image bg_exit7 = "images/exit7.jpg"
image bg_exit8 = "images/exit8.jpg"
image bg_exit9 = "images/exit9.jpg"
image bg_exit10 = "images/exit10.jpg"
image bg_fire_exit_inside1 = "images/fire_exit_inside1.jpg"
image bg_fire_exit_inside2 = "images/fire_exit_inside2.jpg"
image bg_fire_exit_inside3 = "images/fire_exit_inside3.jpg"
image bg_fire_exit_inside4 = "images/fire_exit_inside4.jpg"
image bg_fire_exit_inside5 = "images/fire_exit_inside5.jpg"


# _Floor 2__ (make sure these files exist in /game/images/)
image bg_floor2_halfwayright = "images/floor2_halfwayright.jpg"

#___DOCUMENTS__ PROCESS___
image doc1 = "images/doc1.jpg"
image doc2 = "images/doc2.jpg"
image doc3 = "images/doc3.jpg"
image doc4 = "images/doc4.jpg"


image bg_admin_office = "images/admin_office.jpg"
image bg_authorized_exit = "images/authorized_personnelonlyareaexit.jpg"
image bg_avr = "images/avr.jpg"
image bg_avr_door = "images/avrdoor.jpg"
image bg_beside_avr = "images/besideavr.jpg"
image bg_beside_faculty_office = "images/besidefacultyoffice.jpg"
image bg_cashier_window = "images/cashierwindow.jpg"
image bg_clinic = "images/clinic.jpg"

image nurse_normal = im.Scale("images/nurse_normal.png", 925, 1200)

#_Carl_
image Carl_normal      = im.Scale("images/Carl_normal.png", 1200, 1350)
image Carl_talking     = im.Scale("images/Carl_talking.png", 1200, 1300)
image Carl_suggesting  = im.Scale("images/Carl_suggesting.png", 1200, 1300)
image Carl_thinking    = im.Scale("images/Carl_thinking.png", 1200, 1300)

#_Justine_ (925×1200, all tags use a single underscore)
image Justine_normal         = im.Scale("images/Justine_normal.png",        925, 1200)
image Justine_talking        = im.Scale("images/Justine_talking.png",       925, 1200)
image Justine_happy          = im.Scale("images/Justine_happy.png",         925, 1200)
image Justine_annoyed        = im.Scale("images/Justine_annoyed.png",       925, 1200)
image Justine_confused       = im.Scale("images/Justine_confused.png",      925, 1200)
image Justine_crying         = im.Scale("images/Justine_crying.png",        925, 1200)
image Justine_holding_id     = im.Scale("images/Justine_holding_id.png",    925, 1200)
image Justine_holding_phone  = im.Scale("images/Justine_holding_phone.png", 925, 1200)
image Justine_sad            = im.Scale("images/Justine_sad.png",           925, 1200)
image Justine_shocked        = im.Scale("images/Justine_shocked.png",       925, 1200)
image Justine_Sighing           = im.Scale("images/Justine_Sighing.png",          925, 1200)
image Justine_smiling          = im.Scale("images/Justine_smiling.png",         925, 1200)
image Justine_surprised      = im.Scale("images/Justine_surprised.png",     925, 1200)
image Justine_tired          = im.Scale("images/Justine_tired.png",         925, 1200)
image Justine_laughing     = im.Scale("images/Justine_laughing.png",         925, 1200)
image Justine_scared    = im.Scale("images/Justine_scared.png",         925, 1200)

#__KIM__
# Assuming Kim's images are in /game/images/ and you want a similar size to Carl (1200x1300)
image Kim_normal       = im.Scale("images/kim_normal.png",       925, 1200)
image Kim_holdingID    = im.Scale("images/kim_holdingID.png",    925, 1200)
image Kim_smiling      = im.Scale("images/kim_smiling.png",      925, 1200)
image Kim_talking      = im.Scale("images/kim_talking.png",      925, 1200)
image Kim_calling      = im.Scale("images/kim_calling.png",      925, 1200)

#_Guard_
image Guard normal   = im.Scale("images/guard_normal.png",          925, 1200)
image Guard happy    = im.Scale("images/guard_happy_talking.png",   925, 1200)
image Guard annoyed  = im.Scale("images/guard_talking_annoyed.png", 925, 1200)


#_LYN_
image Lyn_talking           = im.Scale("images/Lyn_talking.png",        925, 1200)
image Lyn_angry             = im.Scale("images/Lyn_angry.png",        925, 1200)
image Lyn_Anya_smirk        = im.Scale("images/Lyn_Anya_smirk.png",        925, 1200)
image Lyn_disgusted         = im.Scale("images/Lyn_disgusted.png",        925, 1200)
image Lyn_normal            = im.Scale("images/Lyn_normal.png",        925, 1200)
image Lyn_pouting_talking   = im.Scale("images/Lyn_pouting_talking.png",        925, 1200)
image Lyn_pouting           = im.Scale("images/Lyn_pouting.png",        925, 1200)
image Lyn_smug              = im.Scale("images/Lyn_smug.png",        925, 1200)
image Lyn_talking           = im.Scale("images/Lyn_talking.png",        925, 1200)
image Lyn_worried           = im.Scale("images/Lyn_worried.png",        925, 1200)

#_ELLA_
image Ella_grinning         = im.Scale("images/Ella_grinning.png",        925, 1200)
image Ella_normal           = im.Scale("images/Ella_normal.png",        925, 1200)
image Ella_smiling          = im.Scale("images/Ella_smiling.png",        925, 1200)
image Ella_talking          = im.Scale("images/Ella_talking.png",        925, 1200)
image Ella_whispering       = im.Scale("images/Ella_whispering.png",        925, 1200)

#_VIDAL_
image Vidal_angry_talking   = im.Scale("images/Vidal_angry_talking.png",    925, 1200)
image Vidal_angry           = im.Scale("images/Vidal_angry.png",        925, 1200)
image Vidal_normal          = im.Scale("images/Vidal_normal.png",        925, 1200)
image Vidal_smiling         = im.Scale("images/Vidal_smiling.png",        925, 1200)
image Vidal_talking         = im.Scale("images/Vidal_talking.png",        925, 1200)

#_SOPHIE_
image Sophie_normal         = im.Scale("images/Sophie_normal.png",        925, 1200)
image Sophie_smiling        = im.Scale("images/Sophie_smiling.png",        925, 1200)
image Sophie_talkin         = im.Scale("images/Sophie_talking.png",        925, 1200)

#_JORIE_
image Jorie_normal          = im.Scale("images/Jorie_normal.png",        925, 1200)
image Jorie_smiling         = im.Scale("images/Jorie_smiling.png",        925, 1200)
image Jorie_talking         = im.Scale("images/Jorie_talking.png",        925, 1200)

#_MAE_
image Mae_holding_paper     = im.Scale("images/Mae_holding_paper.png",        925, 1200)
image Mae_normal            = im.Scale("images/Mae_normal.png",        925, 1200)
image Mae_smiling           = im.Scale("images/Mae_smiling.png",        925, 1200)
image Mae_talking           = im.Scale("images/Mae_talking.png",        925, 1200)


transform justine_bottom_left:
    xalign 0.0
    yalign 1.0
    zoom 0.6

default visited_library = False
default visited_stone_circle = False
default visited_hideout = False

default visited_cashier      = False
default visited_faculty      = False
default visited_avr          = False
default visited_admin        = False
default visited_sas          = False
default visited_clinic       = False
default view_cat             = False



label before_main_menu:
    $ apply_ui_theme()
    return

$ persistent.ui_theme = "dark"

default persistent.ui_theme = "default"  # This saves the user's selected theme

init python:

    def apply_ui_theme():
        # Use persistent color or default to white
        text_color = persistent.text_color if hasattr(persistent, "text_color") else "#5fa121"

        # Change the say dialogue text color
        style.say_dialogue.color = text_color

        # Optionally, change window background text color or other UI elements here too
        # For example, change textbox window text color or font color if needed

        # To refresh styles immediately, call:
        renpy.restart_interaction()


define c = Character("Carl", color="#80c4ff")

label start:
    stop music fadeout 1.0
    scene bg_room at Transform(xysize=(3280, 3220))

    show Carl_normal at center with dissolve
    c "Hey there."

    show Carl_talking at center with dissolve
    c "Are you new to visual novels?"

    menu:
        "I'm new at this, sorry.":
            jump tutorial
        "I already know, thank you.":
            jump skip_tutorial

label tutorial:

    show Carl_suggesting at center with dissolve
    c "No worries! I'm here to guide you around."

    show Carl_talking at center with dissolve
    c "This box below me? That's the text box."

    show Carl_thinking at center with dissolve
    c "All the story, dialogue, and narration happens here."

    show Carl_suggesting at center with dissolve
    c "Want a cleaner view of the background? Just press the H key on your keyboard to hide the UI."

    show Carl_suggesting at center with dissolve
    c "You can also roll back to dialogue with ease using your scroll wheel in you mouse!"

    show Carl_thinking at center with dissolve
    c "Want a cleaner view of the background? Just press the H key on your keyboard to hide the UI."

    show Carl_talking at center with dissolve
    c "You can press H again to bring everything back."

    show Carl_thinking at center with dissolve
    c "Now if you press the Esc key, you'll open the game menu."

    show Carl_normal at center with dissolve
    c "Let me explain the buttons there real quick!"

    show Carl_talking at center with dissolve
    c "History – lets you view past dialogue in case you missed something."

    show Carl_suggesting at center with dissolve
    c "Save and Load – save your progress or return to a previous point."

    show Carl_thinking at center with dissolve
    c "Preferences – change text speed, music volume, and other settings."

    show Carl_talking at center with dissolve
    c "About – gives info about the game."

    show Carl_normal at center with dissolve
    c "Help – shows all the controls."

    show Carl_thinking at center with dissolve
    c "And Quit – well... exits the game. Careful with that one."

    show Carl_suggesting at center with dissolve
    c "And don't forget the Return button – it brings you right back to the game."

    show Carl_talking at center with dissolve
    c "Got it? Sweet. Let's get started!"

    jump main_game

label skip_tutorial:

    show Carl_normal at center with dissolve
    c "Ah, a veteran I see. I'll leave you to it then."

    jump main_game

label main_game:

    show Carl_talking at center with dissolve
    c "This is where the real story begins..."

    # Continue your actual visual novel story from here...

    scene bg_gate at Transform(xysize=(2580, 1520)) with fade

    show Justine_normal at justine_bottom_left
    jus "Wow, hindi ako makapaniwala na malapit na akong umalis sa sintang paaralang ‘to."

    # The guard appears
    show Guard normal at guard_bottom_right with dissolve
    g "Good morning, iho. Asan yung I.D mo?"
    
    show Justine_talking at justine_bottom_left
    jus "Sorry po kuya, naiwan ko po yung I.D ko."

    show Guard annoyed at guard_bottom_right with dissolve
    g "Ayy, pasensya na iho pero bawal kang pumasok pag wala kang I.D."

    # CHOICE MENU -------------------------------------------------------------
    menu:
        "Bumalik na lang ako sa bahay":
            jump go_home
        "Tawagan si Kim para kuhanin ang I.D":
            jump call_kim

################################################################################
# CHOICE 1 – GO HOME –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
################################################################################
label go_home:

    show Justine_talking at justine_bottom_left
    jus "Ayy ganon po ba… sige po kuya, uwi na lang po ako."

    show Guard normal
    g "Sa susunod, siguraduhing may I.D ka ha."

    hide Guard normal at guard_bottom_right with dissolve
    show Justine_talking
    $ renpy.pause(0.3)

    # short inner monologue
    window hide
    show Justine_normal at justine_bottom_left
    hide Justine_normal
    with None
    $ renpy.pause(0.2)
    window show

    jus "(Grabe, nakalimutan ko nga na mahigpit talaga si Kuya Guard.)"
    jus "(Pero mabuti na rin ‘yon — mas ligtas kami dito kaysa sa ibang paaralan.)"
    jus "(Hays… kung babalik pa ako ngayon, male-late lang din ako. Bukas na lang ako papasok.)"

    "THE END"
    return

################################################################################
# CHOICE 2 – CALL KIM ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
################################################################################
label call_kim:

    show Justine_talking at justine_bottom_left
    jus "Ayy ganon po ba, wait lang kuya. Papakuha ko lang I.D ko."
    hide Justine_talking
    # phone sprite
    show Justine_holding_phone at justine_bottom_left
    "Tumawag si Justine sa kanyang kaibigan…"
    hide Justine_holding_phone
    jus "Hi Kim, nasaan ka ngayon?"
    kim "Nasa bahay pa. Bakit?"
    jus "Pwede ka bang dumaan sa bahay ko at kunin ang I.D ko? Naiwan ko eh."
    kim "Sakto, may aasikasuhin din ako sa school. Pupuntahan kita."

    "Ilang minuto ang lumipas…"
    hide Guard normal with dissolve
    show Kim_holdingID at kim_bottom_right with dissolve
    kim "Jas! Eto na I.D mo!"
    hide Kim_holdingID with dissolve

    show Justine_holding_id at justine_bottom_left
    show Kim_normal at kim_bottom_left with dissolve
    jus "Ayos! Salamat!"
    hide Kim_normal with dissolve
    hide Justine_holding_id

    

    # show guard happy and let them pass
    show Guard happy at guard_bottom_right with dissolve
    g "Hmm… sige, pwede na kayong pumasok."

    hide Guard happy with dissolve
    hide Justine_holding_phone
    hide Justine_talking
    hide Justine_normal
    show Kim_smiling at kim_bottom_center 
    show Justine_smiling at justine_bottom_center 
    jus "Salamat po, kuya Guard!"
    hide Guard talking
    hide Kim_normal
    

    hide Kim_holdingID with dissolve
    scene bg_guard_house at Transform(xysize=(2580, 1520)) with fade


label hub_room:

    scene bg_after_school_gate at Transform(xysize=(2580, 1720)) with fade 
    show Justine_normal at justine_bottom_left

    jus "Mhmmmm?"

    call screen nav_door_gate
    return

label door_label:

    if visited_library:
        show Justine_Sighing at justine_bottom_left
        jus "Sarado na ang public library. Kanina pa tayo dumaan doon."
        jump hub_room
    else:
        $ visited_library = True

        show Justine_happy at justine_bottom_left
        jus "Ohhh, yung Public Library... ang dami naming alaala dito.…"

        scene bg_pub_lib_door at Transform(xysize=(2580, 1720)) with fade 
        show Justine_smiling at justine_bottom_left
        jus "Dito kami lagi natambay ng mga kaibigan ko sa tuwing may vacant kami."

        show Justine_talking at justine_bottom_left
        jus "Minsan sabay-sabay kaming gumagawa ng homework dito, pero mas madalas puro kwentuhan lang talaga."

        show Justine_laughing at justine_bottom_left
        jus "May isang beses pa nga, napagalitan kami ng librarian kasi masyado kaming maingay!"

        show Justine_Sighing at justine_bottom_left
        jus "Kung tama ang pagka-alala ko... open to every weekdays, 8 AM to 5 PM."
        hide Justine_Sighing

        show Justine_smiling at justine_bottom_left
        jus "Kaya minsan napapaovertime yung mga staff dito kasi di namin namamalayan — 5 na pala."

        show Justine_smiling at justine_bottom_left
        jus "Hay... nami-miss ko ‘yung mga ganung araw. Para bang ang gaan ng lahat."

        jump hub_room

label new_building:

    # 1) Far view of entrance, Kim & Justine meet
    scene bg_far_view_entrance at Transform(xysize=(2580, 1520)) with fade 

    show Justine_normal  at justine_bottom_left with dissolve
    jus "Uy, Kim! Saan ka punta?"
    hide Justine_normal with dissolve

    show Kim_talking at kim_bottom_right with dissolve
    kim "May kukunin lang akong papel sa registrar. Ikaw, lakad ka?"
    hide Kim_talking with dissolve

    show Justine_normal  at justine_bottom_left with dissolve
    jus "Titingnan ko nga ulit 'yung bagong building — baka milagro, tapos na!"
    hide Justine_normal with dissolve

    show Kim_talking at kim_bottom_right
    kim "Good luck d'yan! Baka mauna pa tayong mag-retire kaysa matapos ‘yon!"
    hide Kim_talking with dissolve

    show Kim_smiling at kim_bottom_right
    kim "Sige, mauna na 'ko. Kita tayo mamaya."
    hide Kim_smiling with dissolve

    hide Kim_talking with dissolve
    hide Justine_normal with dissolve

    jump callscreen


label explore_new_building:

    if not persistent.visited_explore_new_building:
        $ persistent.visited_explore_new_building = True

        # First time dialogue
        scene bg_nearing_new_building at Transform(xysize=(2580, 1520)) with dissolve
        show Justine_Sighing at justine_bottom_left
        jus "Grabe... matatapos na 'yung school year, pero 'tong building na 'to, hindi pa rin tapos."

        show Justine_Sighing at justine_bottom_left
        jus "Parang hindi rin ako makaka-graduate kung hihintayin ko 'yang matapos."
        jus "I wonder, magkakaroon kaya ng bagong program dito?"

        show Justine_normal at justine_bottom_left
        jus "Hay... sana naman, pagbalik ko next sem, may progreso na."

    else:
        # Alternate one-liner on revisits
        scene bg_nearing_new_building at Transform(xysize=(2580, 1520)) with dissolve
        show Justine_normal at justine_bottom_left
        jus "Gina-gawa parin hanggang ngayon."

    # Return to choice menu after
    scene bg_far_view_entrance at Transform(xysize=(2580, 1520)) with fade 
    jump callscreen


label callscreen:
    scene bg_far_view_entrance at Transform(xysize=(2580, 1520)) with fade 
    call screen custom_choice_menu
    return



label resting_ground:
    scene bg_tambayan_to_entrance at Transform(xysize=(2580, 1520)) with dissolve
    show Justine_happy at justine_bottom_left
    jus "Ang tahimik dito ngayon ha."
    hide Justine_happy

    jump choicethree

label choicethree:
    scene bg_tambayan_to_entrance at Transform(xysize=(2580, 1520)) with fade
    call screen rest_choice_menu
    return

label stone_circle:

    if not visited_stone_circle:
        $ visited_stone_circle = True

        scene bg_tambayan_to_entrance at Transform(xysize=(2580, 1520)) with dissolve
        show Justine_happy at justine_bottom_left
        jus "Ahh, eto lagi pagkatapos ng klase."
        jus "Grabe kami makatakbo kasi inuunahan namin 'yung ibang estudyante—"

        scene bg_circle_area_lower_view at Transform(xysize=(2580, 1520)) with dissolve
        show Justine_laughing at justine_bottom_left
        jus "…baka mawalan kami ng pwesto, kasi dito kami kumakain tuwing lunch time."

    else:
        scene bg_tambayan_to_entrance at Transform(xysize=(2580, 1520)) with dissolve
        show Justine_happy at justine_bottom_left
        jus "Ka-miss magkipag chismis dito haha"
        hide Justine_happy

    jump choicethree

label hideout:

    if not visited_hideout:

        $ visited_hideout = True  # mark as visited on first entry

        scene bg_entering_hideout at Transform(xysize=(2580, 1520)) with fade
        show Justine_happy at justine_bottom_left
        jus "Nandito na ako sa ‘secret’ hideout namin!"

        show Justine_scared at justine_bottom_left
        jus "Dito rin naganap ‘yung infamous open forum namin noon… grabe, riot talaga."

        scene bg_closed_hideout_gate at Transform(xysize=(2580, 1520)) with dissolve
        jus "Lahat ng reklamo, hugot, at ‘crazy sh*t’ binuhos dito—"

        show Justine_Sighing at justine_bottom_left
        jus "may nagsigawan, may nagtampo, may muntik nang magsapakan."

        show Justine_laughing at justine_bottom_left
        jus "Dejoke lang."

        show Justine_Sighing at justine_bottom_left
        jus "Ngayon sarado na. Parang sinelyuhan din ‘yung memories namin dito."

        show Justine_laughing at justine_bottom_left
        jus "Pero kahit ganun, solid pa rin ‘tong lugar—kahit puro kalokohan at drama!"

    else:

        scene bg_closed_hideout_gate at Transform(xysize=(2580, 1520)) with fade
        show Justine_scared at justine_bottom_left
        jus "Nakakatakot rin pala dito pag walang tao."

    jump choicethree

################################################################################
#  ENTER BUILDING – Lobby hub
################################################################################
label enter_buildingcampus:

    scene bg_entering_the_school_lobby at Transform(xysize=(2580,1520)) with fade
    show Justine_normal at justine_bottom_left
    jus "Pasok tayo sa main building. Saan kaya pupunta ngayon?"
    scene bg_informationdesk at Transform(xysize=(2580,1520)) with fade
    show Justine_normal at justine_bottom_left
    scene bg_pup_lobby at Transform(xysize=(2580,1520)) with fade 
    
    jump inside_building

label inside_building:
    scene bg_window1 at Transform(xysize=(2580,1520)) with fade 
    call screen inside_choice_menu
    call screen information_desk
    return

label cashier:

    scene bg_cashier_window at Transform(xysize=(2580, 1520)) with fade
    show Justine_smiling at justine_bottom_left
    
    jus "Cashier… mabuti na wala ako kailangan na bayarin"

    jus "Tinamad pa kasi sa ibang subjects and yan tuloy bumayad pa siya ng tuition para sa tatlong semesters…"

    show Justine_talking at justine_bottom_left
    "Hello, may babayaran pa ba kayo ngayon?"

    show Justine_smiling at justine_bottom_left
    jus "Ay wala naman, pasensya na sa pagabala."

    show Justine_happy at justine_bottom_left
    "Okay lang po. Kung may transaction kayo na gagawin, pwede po kayo magbayad online sa PUP SIS..."
    "...o dalhin mo nalang ID mo dito para ma-verify ang transaction niyo po."

    show Justine_laughing at justine_bottom_left
    jus "Ayos! Buti nalang wala akong utang!"

    jump inside_building

label right_hall:
    scene floor1_hallwayright at Transform(xysize=(2580, 1520)) with fade
    show Justine_Sighing at justine_bottom_left
    jus "grabe walang katao tao himala?"
    hide Justine_Sighing

label floor1_right_hall:
    scene floor1_hallwayright at Transform(xysize=(2580, 1520)) with fade 
    call screen right_hall_menu
    return

label show_three_images:
    scene floor1_hallwayright at Transform(xysize=(2580, 1520))

    show doc1 at Position(xysize=(50, 100), xpos=0.1, yalign=0.5)
    show doc2 at Position(xysize=(59, 100), xpos=0.5, yalign=0.5)
    show doc3 at Position(xysize=(50, 199), xpos=0.5, yalign=0.5)
    show doc3 at Position(xysize=(50, 100), xpos=0.75, yalign=0.5)
    pause 

    jump right_hall_forward2
label clinic_room:

    scene bg_clinic at Transform(xysize=(2580, 1520)) with fade
    show Justine_talking at justine_bottom_left

    jus "Clinic… ayan, tahimik pero dito sikat ang lahat ng drama sa buhay."

    show Justine_normal at justine_bottom_left
    jus "Dito ako tumatambay minsan dahil sa sakit ng ulo, pati na din dahil sa minsan na pasakit ng loob."

    show Justine_Sighing at justine_bottom_left
    jus "Minsang umupo ako d’yan, hindi dahil sa masamang pakiramdam kundi dahil gusto ko lang ng pahinga."
    jus "At ang Nurse? Parang naging nanay ko pa."

    show Justine_smiling at justine_bottom_left
    jus "Palagi niya akong tinatanong, ‘Okay ka lang ba talaga?’ Nakakamiss toh talaga."

    # Start of flashback sequence
    scene bg_clinic at Transform(xysize=(2580, 1520)) with fade
    show nurse_normal at right
    show Justine_normal at justine_bottom_left

    n "Ay dios mio, tambay ka nanaman dito uli? Ano nanaman pakiramdam mo mijo."

    show Justine_talking at justine_bottom_left
    jus "Wala po ma'am, unting sakit lang ng ulo po."

    
    n "Wag mo kalimutan na alagaan mo sarili mo mijo."

    # End of flashback
    scene bg_clinic at Transform(xysize=(2580, 1520)) with fade
    show Justine_happy at justine_bottom_left

    jus "Ang bait talaga ni ma'am. Sana makadalaw ako ulit dito."

    jump right_hall_forward
label right_hall_forward:
    scene bg_acad at Transform(xysize=(2580, 1520)) with fade 
    show Justine_talking at justine_bottom_left
    jus "Tuloy lang… baka may bukas na classroom sa dulo."

    jump right_hall_forward2

label right_hall_forward2:
    scene bg_acad at Transform(xysize=(2580, 1520)) 
    call screen right_hall_menu1
    return
    # Move to a NEW hallway, not back to right_hall
    # or create another label like "deeper_hallway"

label admin:
    
    scene bg_clinic at Transform(xysize=(2580, 1520)) with fade
    show Justine_talking at justine_bottom_left

    jus "Na-alala ko nung gumawa kami ng system para sa finals namin sa comprog"
    jus "pumunta kami dito para humingi ng permiso na mag-ikot sa campus at mag-picture"

    show Justine_Sighing at justine_bottom_left
    jus "naka-ilang balik kami dahil may proper procedure pala bago pumunta dito."

    # Start of flashback sequence
    scene bg_clinic at Transform(xysize=(2580, 1520)) with fade
    show Mae_talking at center
    "Kaming dalawa nalang ni Sophie yung papasok sa loob para ipasa yung letter"

    # 1st Attempt
    scene bg_admin_office at Transform(xysize=(2580, 1520)) with fade
    show Mae_smiling at left with dissolve
    show Sophie_smiling at right with dissolve
    "(Left the office after a few minutes)"
    hide Mae_smiling with dissolve
    hide Sophie_smiling 

    scene bg_admin_office at Transform(xysize=(2580, 1520)) with fade
    show Sophie_talking at right with dissolve
    s "Guys ulitin daw mali raw yung format ng letter"
    hide Sophie_talking with dissolve

    show Mae_talking at left with dissolve 
    m "Ganito raw yung proper format"
    show Mae_holding_paper at left with dissolve

    # 2nd Attempt
    scene bg_admin_office at Transform(xysize=(2580, 1520)) with fade
    show Sophie_talking at right with dissolve
    show Mae_normal at left with dissolve
    "left the office after a few minutes"

    scene floor1_hallwayleft at Transform(xysize=(2580, 1520)) with fade
    show Mae_talking at left with dissolve
    m "need naman daw ng appointment sa sinta"

    # 3rd Attempt
    scene bg_admin_office at Transform(xysize=(2580, 1520)) with fade
    show Sophie_talking at right with dissolve
    s "Manifesting ma-approve na to"
    show Mae_normal at left with dissolve
    "left the office after a few minutes"

    scene floor1_hallwayleft at Transform(xysize=(2580, 1520)) with fade
    show Mae_talking at mae_bottom_center with dissolve
    m "Finally! na-approve na rin HAHAHAHA"
    hide Mae_talking at mae_bottom_center with dissolve
    # End of Flashback
    show Justine_laughing at justine_bottom_left with dissolve
    jus "Haha... naaawa ako sa kanila"
    hide Justine_laughing at Justine_bottom_left with dissolve
    
    # ____CHOICES_____
    menu:
        "knock and enter the admin office":
            jump adm_office1
        "Just enter the door":
            jump adm_office2


label adm_office1:
    scene bg_admin_office 
    show Justine_talking at justine_bottom_left
    jus "Hello po ma'am vidal"

    show Vidal_talking at right with dissolve
    v "And you are..?"

    show Justine_talking at justine_bottom_left
    jus "Justine po ma’am from BSIT 4-1"

    show Vidal_talking at right with dissolve
    v "Oh why hello Justine, what can I do for you?"

    show Justine_talking at justine_bottom_left
    jus  " nag-iikot Ikot lang po para sa huling sandali ko as a student of this sintang paaralan"

    show Vidal_talking at right with dissolve
    v "Kung ganon din ay, enjoyin mo na habang nandito ka"

    show Justine_talking at justine_bottom_left
    jus "Maraming salamat po"

    return

    jump right_hall_forward2 

label adm_office2:

    scene bg_admin_office 
    show Vidal_talking at right with dissolve
    v "Sino ka at bakit ka pumapasok lang ng basta basta?"
    show Justine_talking at justine_bottom_left
    jus "uhmmm... Justine ma’am from BSIT 4-1 po"
    show Vidal_angry_talking at right with dissolve
    v "Justine!!! Ilang taon ka nang nag-aaral dito pero hindi mo man lang alam ang tamang proseso bago pumasok?"
    show Justine_scared at justine_bottom_left
    jus "Sorry po Ma'am Vidal, hindi na po mau-ulit"

    show Vidal_angry_talking at right with dissolve
    v "Kakatok ka lang ng 3 beses and give your greetings, ganoon ba kahirap yon?"

    show Justine_scared at left with dissolve
    jus "Maraming salamat po"
    hide Justine_scared with dissolve

    show Vidal_angry_talking at right with dissolve
    v "Labas!, marmai pa kaming ginagawa at dadagdag ka pa!!!"

    "Justine was forced out"
    return 

    jump right_hall_forward2 

    



label mid:
    scene bg_midstair at Transform(xysize=(2580, 1520)) with fade
    show Justine_Sighing at justine_bottom_left
    jus "grabe walang katao tao himala?"
    hide Justine_Sighing

label right_hall_forward3:
    scene bg_midstair at Transform(xysize=(2580, 1520))
    call screen right_hall_menu2

label lgbt_cr:
    scene bg_lgbt3 at Transform(xysize=(2580, 1520)) with fade
    scene bg_lgbt2 at Transform (xysize=(2580, 1520)) with fade
    scene bg_lgbt1 at Transform (xysize=(2580, 1520)) with fade
    show Justine_normal at justine_bottom_left
    jus "Sana mayroon kang makita"
    hide Justine_normal


label lgbt_cr_menu:
    scene bg_lgbt1 at Transform(xysize=(2580, 1520)) 
    call screen lgbt_cr

label garden:
    scene bg_garden at Transform(xysize=(2580, 1520)) with fade 
    show Justine_normal at justine_bottom_left
    jus "Sana makita ko siya ulit"
    hide Justine_normal 
    
label garden_view_menu:
    scene bg_garden at Transform(xysize=(2580, 1520))
    call screen garden_view

label garden_view1:

    scene bg_garden1 at Transform(xysize=(2500, 1520)) with fade
    show Justine_happy at justine_bottom_left
    jus "Wow! lagi talaga andito tong pusa nato e"
    jus "Andaming umaamo lagi sa pusa na to"

label garden_view_menu1:
    scene bg_garden1 at Transform(xysize=(2580, 1520))
    call screen cat
label garden_view2:

    scene bg_garden2 at Transform(xysize=(2500, 1520)) with fade
    pause 1.0
    scene bg_garden3 at Transform(xysize=(2500, 1520)) with fade
    pause 1.0
         
    jump back_garden_view

label back_garden_view:
    scene bg_garden3 at Transform(xysize=(2500, 1520))
    call screen back_garden

label back_garden1:
    scene bg_back_garden1 at Transform(xysize=(2580, 1520))
    call screen back_garden_menu1
    
label right_exit:
    scene bg_exit1 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_exit2 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_exit3 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_exit4 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_exit5 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_exit6 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_exit7 at Transform(xysize=(2580, 1520)) with fade
    jump right_exit_menu

label right_exit_menu:
    scene bg_exit7 at Transform(xysize=(2580, 1520))
    call screen right_exit_menu1

label outside_exit:    
    scene bg_exit8 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_exit9 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_exit10 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    jump outside_exit_menu

label fire_exit_inside1:
    scene bg_fire_exit_inside1 at Transform(xysize=(2580, 1520)) with fade
    scene bg_fire_exit_inside2 at Transform(xysize=(2580, 1520)) with fade
    scene bg_fire_exit_inside3 at Transform(xysize=(2580, 1520)) with fade
    scene bg_fire_exit_inside4 at Transform(xysize=(2580, 1520)) with fade
    scene bg_fire_exit_inside5 at Transform(xysize=(2580, 1520)) with fade

label fire_exit_inside_menu:
    scene bg_fire_exit_inside5 at Transform(xysize=(2580, 1520)) with fade
    call screen fire_exit_inside_menu1


label outside_exit_menu:
    scene bg_after_school_gate at Transform(xysize=(2580, 1520)) with fade
    call screen nav_door_gate
    

label upstairs:
    scene bg_stair1 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_stair2 at Transform(xysize=(2580, 1520)) with fade
    pause 1.0
    scene bg_stair3 at Transform(xysize=(2580, 1520)) with fade
    show Justine_Sighing at justine_bottom_left
    jus "Ba yan! Wait nga!"
    
    hide Justine_Sighing

    jump second_floor_stair

label second_floor_stair:
    scene bg_stair4 at Transform(xysize=(2580, 1520)) with fade
    show Justine_Sighing at justine_bottom_left
    jus "Teka! nakakapagod"

    jump second_floor_stair1

label second_floor_stair1:
    scene bg_floor2_halfwayright at Transform(xysize=(2580, 1520)) with fade
    show Justine_laughing at justine_bottom_left
    jus "Haha! Nakakatawa naman!"

label male_bathroom:


label right_hall_forward4:
    scene bg_floor2_halfwayright at Transform(xysize=(2500, 1520))
    call screen right_hall_menu3


label second_floor:
    scene bg_second_floor at Transform(xysize=(2580, 1520)) 
    call screen second_floor_menu

label left_hall:
    scene floor1_midhallwayleft at Transform(xysize=(2580, 1520)) with fade
    scene floor1_hallwayleft at Transform(xysize=(2580, 1520)) with fade
    show Justine_Sighing at justine_bottom_left
    jus "Liwanag ngayon ha?"
    hide Justine_Sighing

label floor1_left_hall:
    scene floor1_hallwayleft at Transform(xysize=(2580, 1520))
    call screen left_hall_menu
    return


    jump inside_building

label avrhall:
    scene bg_beside_avr at Transform(xysize=(2580, 1520)) with fade
    call screen left_hallcorner_menu
    return

label avrdor:
    scene bg_avr_door at Transform(xysize=(2580, 1520)) with fade
    show Justine_talking at justine_bottom_left

    jus "Ah, yung AVR... Naalala ko si Sophie tuloy. Na high blood pa siya noon dahil pinalinis pa siya nung nakalat namin yung AVR..."

    # Start of flashback
    scene bg_avr with fade
    show Sophie_angry at right
    show Justine_shocked at justine_bottom_left

    soph "Ano ba yan, itatapon nalang eto! Mas lalo na ikaw Justin! Lagot ka sa akin mamaya!"

    # End of flashback
    scene bg_avr with fade
    show Justine_shivering at justine_bottom_left

    jus "Inabangan niya pa ako sa gate nung uwian... Nakakaiba talaga yung galit netong babae na 'to…"

    jump inside_building