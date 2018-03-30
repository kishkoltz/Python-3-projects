# D:\python3\app\python.exe przygoda.py


import os
import time
import random
import getpass

playerName = 0
zodiac = 0
life = ''
lifeTop = ''
rollValue = ''
equipment = {}
gameOn = True
stat = {'might':0,'nimbleness':0,'endurance':0,'commonSense':0,'slyness':0,'charm':0, 'stomach':0}
finished = False
authorisationPassed = False
gift = {'pinecone':'a pinecone', 'spaceship':'a toy spaceship'}
giftUnwrapped = False

ania = ('''
J  .jYX1u,:          :,           r..Fv     ,r     LB0B@@@B@
 N .   7. Z           :   ; i    .               vrF@B@B@B@B
  i        i     i  .      .   .  .             ,YqZ0@B@B@GE
     :Lr:   v,7  i:         . iXu,72,     ,     r:vvUS@B@B@M
        F::   r   :r:.         ::XLi1uii,  :      ,ivv@MB@B@
         .       .:7Y .:iSq7r0ZX    v:L2    F      :v7JvUNMv
          ,          .  ;70L .YG . juUZ@B1u7Y@7   .ru77iF@rY
           v        ,jE:FFN.i  7GNSJS22X@B@@YS    iJ7:rLjuiX
           i          :u7         r512vJZ@B@B8 :  ::i: iv7J5
                  Y   5.            ,2k1SSqFr   ,, .v:.,,i r
                  Nv:  :jr            :SPj     .:    ;JkMU ,
                     iJX;               .u0Xv  .u:     :0Pv
:X.                    :i                  r77:.:jj7v  2q5jv
,qY                            .:,    .      .: :7Y5qSvvXFEq
    ,.r                  .,,7XZ8N0P5v            7rUUF77vqM@
  .              ij2kqGOBBBMMOG0NXqSk1,           ,YYUPqENXO
rL             v5kFXSqNZZZ0NPXkqSS551F1r        .::vvL1qN80B
 .            1U2uuuUu2u51kkPSXSF1522uujr:         .SUF5FFXE
             Y2uJJJJYuJuu1FXXqXXFk1kF5uuY7:          rL5jUuF
F..r:        7UjjYjYjjuu12F2SFPPNqNPENqFuJu:          jXk15P
: i;         rjuLYYju2uUU2uUu12SXqNZEOMBOGP1       .EGYu5kkG
 v..         rYjUuUu1uUuUJuYuJJJ2FGMMOMMMOMMF       ,F2r2uuS
 .,  :      .7JkNE0EqqkPF1jJLLvJY7.      :uPq5         L2ujk
.  v. j     vLLv,         :rr7Lr           :PGq    urrSS2u2S
Zv,L        u2.  ,         .LJjL            jMBv  :PS2Y125uN
    Jv:     FuL;:         ..L28G.      1kX8BBM@E  rZEuuU1u2X
iU1iir.     uUY7.  .  :Y:iYvLNB@OLLLrrr7uOB@@@BE    v522U1jP
k05.rk1v.   iU11kF5ujLL7jU2Lu8BB@BBMOGMB@@@BMM@U SGu ,XJ1U1k
iY ..2riF    S21UkSS5SFPPkuj7SGMB@B@@@B@B@BBMBBL EU:,F2UU2Uq
iJ:ii0..:    2YYuuFk0NZqPFuYvY0M@B@G8OMOBBBMBM@7 : LP1F21u2X
u1i.L5 ::    7LJJu2SSqPP1J7151q@B@@@.rJ150EG0ZGu7J2SFF155Fuq
iur.JLU      i2Jjjuu125J: jXGXZB@B@@Y :ivvYYuJ510XPFS555X11N
 v:::u        FJLjYuYu7. :i ;Sq0E2   ..:.   .7vkFS1FSkFXSkUE
.::7          qri:ii;,  r1u       ZBNr .:. ,i:uGZPqEZ0G8OZEO
:Ur:          YJ:...  .:L1SF7i.  XNS7  .iYuuirM@M@B8ZMGGZOM@
L5N            Xviirv77:.          .i7uL:7j77.
kX2             UuYYJUL7u2v..i:7UkP0ZZqXJvi7
:5X,             ijJYLYYujujvi;i:.7jFSPNkY7
i:                ,7vLLJJuLLv7i:,:7u2FkN1L
                   :irJjuJuLLLYY2FqXNSSJ:
                     ::iv2u2U15Z0EXS5525
                        .:55F2F1Uj1EMO@B@  M
                           :r: iY0G@PYLSZBM@B
                              UP55SOMuuXL7iJP
                             Mki Ou  YYJv7iSr            r;F
                            @q2i    :Yvi::2O@@@       iir,.r
                            Sur.:L juY;::USLi1@     7uri:,.i
                           .5;,rSXP52LYj5jLri     i5,  .:iiJ
''')

def playerStats():
    print(playerName.center(120))
    print ()
    print (("Your life: " +str(life)).center(120))
    print (("Your might: + " +stat['might']).center(120))
    print (("Your nimbleness: + " +stat['nimbleness']).center(120))
    print (("Your endurance: + " +stat['endurance']).center(120))
    print (("Your common sense: + " +stat['commonSense']).center(120))
    print (("Your slyness: + " +stat['slyness']).center(120))
    print (("Your charm: + " +stat['charm']).center(120))
    print (("Your stomach: + " +stat['stomach']).center(120))

def authorisation():
    global authorisationPassed
    print ("\nAutorisation required.")
    time.sleep(2)
    print ("Did the author receive a kiss? (y//n) ", end = '')
    if "y" in input():
        authorisation = getpass.getpass('Now the author will type the password:')
        if authorisation == 'passw0rd':
            print ("\nPassword correct, authorisation granted.")
            time.sleep(2)
            authorisationPassed = True
        else:
            print ("Sorry, password incorrect.")
            time.sleep(2)
    else:
        print ("Without a kiss override is a no-go.")
        time.sleep(2)
def clear():
    os.system('cls')
clear()

def test():
    global rollValue
    rollValue = random.randint(1, 20)

def cheat():
    global rollValue
    rollValue = 20

def lastRoom():
    print ('Imma load up the last room you were in.')

def gameover():
    clear ()
    print ()
    print ("Y O U  D I E D".center(120))
    print ("Do you want to resurrect? y/n: ", end = '')
    choice = input()
    while choice not in 'yn':
        choice = input ("please type in 'y' or 'n'")
    if choice == 'n':
        mainMenu()
    if choice == 'y':
        resurrect()

def resurrect():
    global life
    life = lifeTop
    lastRoom()

def damage(dmg):
    global life
    life = life - dmg
    print ("You've received %s damage." % str(dmg))
    if life <= 0:
        gameover()
def get(item):
    equipment[item] = 'a ' + item

def lose(item):
    del equipment[item]

def mainMenu():
    global gameOn
    clear()
    print("M A I N  M E N U".center(120))
    print("What would you like to do:".center(120))
    print("1) Continue".center(120))
    print("2) Quit".center(120))
    choice = input()
    while choice not in str(range(1,2)):
        choice = input("Please select, 1 or 2: ", end = '')
    if choice == '1':
        lastRoom()
    if choice == '2':
        gameOn = False

def characterSheet():
    clear()
    playerStats()
    print ("Your equipment:")
    for item in equipment:
        print (equipment[item])
    print()
    choice = input("What would you like to do?\n1) Continue\n2) Quit to main menu\n")
    while choice not in str(range(1,2)):
        choice = input("Please select, 1 or 2: ", end = '')
    if choice == '1':
        lastRoom()
    if choice == "2":
        mainMenu()

def breakfast():
    while gameOn == True:
        global lastRoom
        global life
        lastRoom = breakfast
        clear()
        print("*Cue Grieg - Morning Mood*\nIt's morning. It is cosy and comfortable. \
Before you open your eyes you can smell that a breakfast has been prepared for you. \
What is it?")
        print ("1) Corn flakes and whisky\n2) Fried eggs on bacon\n3) Sweets\n")
        choice = input()
        if choice == "m":
            mainMenu()
            break
        if choice == 'c':
            characterSheet()
            break
        while choice not in ('123'):
            print ("Please select, 1, 2 or 3: ", end = '')
            choice = input()

        if choice == '1':
            print ("\nUgh! Understandably, in order to celebrate this special day you've \
picked the worst dish for breakfast you could. Not only does it harm your liver, but \
also tastes awful.")
            damage(random.randint(0,2))
            stat['stomach'] = str(int(stat['stomach'])-1)
            print ("Your stomach goes down by one point.")
            input()
        if choice == '2':
            print ("\nA sound choice! This classic dish invigorates you with the energy \
required to go through this special day.")
            life = life + 1
            input()
        if choice == '3':
            print ("\nSweet tooth, eh? It was tasty, but at what cost?")
            stat['stomach'] = str(int(stat['stomach'])-1)
            print ("Your stomach goes down by one point.")
            input()
        unwrapGift()
        break

cisowaKomnata = ('''
juvuvr7FLYuuJUkOSkSq2X15XkuPB872k1SX5ULJv7v7,1kvuq52LuFJJFOZri2X7r5EX1v::::,YSXEv7LJrJiru, YqE12i:::.r;,...Lv::i7r,,:ru
FOU522ukjkuJSPS11S7uULJuS0PPEZ5S1XF5u77FLL52Xqj12F5SZJ71v,SG:.;ivL.:;iri,.i1;,kr::,i, :i  .,:riir7:i,,..r2Juj7.Jj:Yvi2u
UMXkPkq5FkZZGk0PXkkPq5kFMEGEMMMMOOE80USSBZMMEGEMOX50M15k511LL7vvF25:vr;ri:1PSi7i:::v7.k7r77;rJiirriir::,,i11F7i:j:7jYL5
18kOZFJJL5qPJuUJvU2US15FkMOP88GOqS2ZSUuvkGE0uPuZGX2FvL77UYLuuU7i:,,:7u,:: i5;..rr,:iru;vJv7rrY:.,ijL.  .uGju7::..:..:,,
P8G0qZBG005uuuU2qESu5jOONEFPMGZZ85PSUuqMOuS0uu5ukNEXLvvrL,:,.,i;i.:LPv:..:rr.  iu:,.,i:rv:::qju, rBYi .2@GYjLi.,:::..:i
FMP220PXZOEjLuk0kE0q25UkUSSEOMSEB0SkJu1Z1rqquUq2rUZZS5Pi ,i.  :7r..jvY:.rSJJr,r7i:...7rii:.ivr7: .7i::.ri..7L:.,::ii.,i
YqFv2SFU1uGujvuYX0P2252EEFEX5uuL1kP22JM05UNULvFEvrkuUS8Y::;,i;. . JuJui.::rv5Sv.. ,.:.:5J:.i::Li,. ii::LS8v:r,.::,:7r.,
vuYLrJLuuuFPX1uF5S5F5UOOJSuS5uvL7vriSYX8S25quX8kiuX7LE0Xr::::N1r.7uuYY7 .2PSL7: :: ..;:i7v:::vu7: .ii:iXrOL...i7i;i77::
Y0ZSL1XLjuYjG08X1q1XS18FJPkUu11uYJuivrJNujJNXu1kv:;:YF127i:,LuPq5L2:,iui2;7ji:riri:i777iiJi ;Yv7v; :;.iBi ,.::iriir7irj
7q5XN51kF1uJLUYu1FU5PqSPvU05FSuULvrr:,rJ::;2uu7Lv,i7rvjJu7r: :7Xjuviiv2Pu7ri,riirrrv,:27:Yi,,7ir7i :i,:@1.:;7r:i:r.:::.
u27uq1XS5uJJvLv72vYv7uuvr5kk2uX5v:ir::v7::777LLLY::7;7FkLi:i0S72EuvLvuJr:iLii:::irii.,ji.:Jv.,.:i7, . .Oj.ii::7 .ii:r7:
uXvLXP5ULLju7uvLYvL27r;:rUJur7FFvuir:iLLiiivjJL1j:,7r7Lr:: ,i:ri7L77UqvL.i:iir.:i;i7r:Li.;v2: . .v:.. .u,,YLvLujJu15u5N
U5Y2U52uu7Lvvvvrjvj2Yvv5E5LJLrv;i77iirUYri;7LX5ji:::i7, ..   :urvNUivv .7v: ,::  :riLv1r.::rr.:.:7r.  ivUUv7NkkqP1UuSk@
LuFP5YvvuLiiiiiLuuL7irSNP5J1jrrv:ir;:7J1rir7vJLr,:;ri7,.:::  rii.LUi.  ... .i:i  Lv7v7LY7:,iri.,.r;: iLuSLiUFNkZvZNL:iu
vYFSJr1LU2viiiJYYLJ;;r7rrvXu2r::::iii:i;::Lrrr7rr::i;vJ7J . .77.iLk,7.      i::, ;r;7r;;LY:.ir:....,:i7XNJLu7:rL:ikujvX
kMFuvv1LYSuYrr7v7L:ii7riiJPJF7:::ri;i..,::v7i;7:.,.:iri:.   :U: .vJ:r:       .      .,:.,i: ..:..:.;:Y5YiruuL:::,:r.rLu
LLv:vLF7L2SFririLUr7ririiivrrii,:;i:.rkuLrvJPFSuuuuu2jLv1F0GEq8EEk0uJ10OGX5uuJL721UJJ5GU2ri r,.,:.:ri.:7S7i:ivj:ri7::rJ
:rru25uu7r7r:ri:i77vri7r:7rL7::i:i:i:k@@vF70O@MOOMOMZkk8ONZM5XGZNZ8OqENBGZ0BMBOk0@@BPMM@@J::....,.,rr .7iri:i:vv.,:i,LL
v1UFuL7J1:::r7:::rr.:r2::7rii.i::ii;:YMZ5GXN0      C I S O W A    K O M N A T A   OO0kZG@L :,...  ,i7.i::::,:.LL::7YrLj
L821Lv7rri:rr;:r:r7.:7riiLrvr7:,ir:i,1B8GO880OMOZZXS5ZMEqM8P0GO0PE8GqOMG8@BOE8O@B@B@BM8M@2 ::i . ..:7. ir;i::,.,,::rSi5
:r:1jiLYvi:irri::71ri::rir;i;ri:iii: 5@M88MB@BqEMMBM8Z8XNNGXqk0P0qGPGqqkENGkOB@80MBMMMMM@J ::i.   .:Jr,i::i::.,::::72LU
ivvFvYY57::ir7..i7L7i:ii:,,:i:::::i.u7,,8F,. r,.  ...  .  .,  ...            .       Ju  ..::::::i;L7LLvvLi::,:vr7jjiPr
FkUv7v7iiiv7rrr:::ii:::i:,:ii,:,.:::u:. MS,  i:.  .,i  ..      .L1:  r,         ...  1M  ,,:i:iuYvLYL77r7i:,. :v7i:::i2
u2JYLr;::r7rr77jvi::::ir:,:::..:.:iiir,,B2  ,7,  ..::  ,.. i:,,:;7r ,X:.    .:,,,,.. XN ,, ...  :L1j7L:::..:,L5Lv::Ui;L
uPSj2Lri7iri7r7;LJ7iiiiii:.,:.,, .,iri, @2 ::7:  ...:.... .:,,,rGBX        .,,::,,   Jq,..    :LSuL7LL7i: .:rFOjSru0UY2
Ukv7:i::iii;r7i7iLUS7i::i:.::,..,:iv::..BS i ... ...,,.,. ..   7k@v       .... ;:  . FB  .  :kMG2UU1Yuv  i.:7Lvv7L7,jYU
:riiiii:;:,ir7r7vLrii,.:i,,.,...i77;:..,@j..  ....:,....,.,:.  ::,. ..,.  :.ur:iY,   2BvEv  .LjXUYYuuYL7:v7;vYi727::Xvu
rJ;;;irv7r,7;7L7;::i:,.r:.,..,..:u7;,,.:@2  . ..   ....:.. :.        ,:,  5B0k77u, .r0Miri .r:  .Li;i;:i,:riiiivLrrvULi
7uri7r7;i7urJrri::ii:.:i:.,..  ,ui;r:,,,@J i: .    ....... :, .  ..    .  G@X10Ev  ,r1@i:1  @Br .Zi:irii:rri,..;77;71iv
.rLv:i.i::i7Yi,::ii:,..r...... iYi:.:i.iBS ..  .   . ....r ::  ..::   .:  r@X:7EL    uB7:.  B@. vr:rr7v7:;ri:,,vvv::7iL
:L7i:,.;i.:i77:.:r;ri:::i....  rr,. ,::i@j    ... ,::... :.:.   ... . ...  7F.     . 5@:. . Mq  5i;iir7vr.iri..rSr;:Uu1
J2:7Yi:Y:.ir:r:.,r:::iiiiriri. :;iiL:i,iBj.:.  . :.,,, ,.:,,    .,.   .. :.  , . .., kB7,   r. :uvu;ivvuUv:i::::i7r;7Uj
uuLYr777,,77i,::..::r:::i:ri;rrri iiv: :@u.,.  .....,.,:..,...  ..    ............,. X@,  ,.. ,:rui:v7YrYrri:.r7riv7L:i
vLri:i:,.i:ri,:v::irii:i:iiii77i. ,,ir :Bu .. .. ..,...:.. ... .       .   . . . .   SB, .....,ii: :i:::,:::i7v;.rLi,.:
v7v::i:::ri:;:L1i:ri:.:i::r7r:i. ::rri::rii,. ......  ,.,...... . ....    ....... .  1@: .,   :ii.i7r7r::ii ivLjF1vr7vL
.:ir:ii;::;r:YLL77rL: ,:,i:::i:: i7i,Li:iiirri..,,.,.... ..,.,...:,,:::..,...:...,.. FBi ....:....:riY7i::i,:iruvL1u11u
:ii7:::,iii:iYLr777Lu::,:ii.::::.iU:.ii.:iiiri:,:,:,,,,..,:::,:::.,,..:.:...,.,....  1B: .,,::. ::::ir7;v::,,,::irkF0vr
:rir::,.:i::.7u:rY:i:i:::iri:::iLYvi:,.ii7:7i,,:::::::::::::::.::,.,::,,::,:,.....,. LB; :,:iri:7ri:iL7:::::,:,:5P22uvL
:7Yi:i:i:::.vkv:iir.::ii,.i:.:U5Pi,.ii:.1Y ,:,:::::::::::::::::,:,:.,.,,,,:,,.:.,... 7@i.,.,i77r::i.::..:,r:,ii5kqNX22P
rr::.:i7i:,,irrriiii:r::..,ijruviLr:,,i:NS .,::::::i:i:i:i:iiiiiiiii::,:.,.i::::.,,. 5Br ...r2ii,7ii,.:i:rrrvU20212Pu5P
:,:.  ,,:,i: .r7r, ::::.:::vuvvi:rJY::,,S5,.,:::i:iii:iiiiii;iiiiii:iii:i::::::::,:. j@: .,:r7v:r7Lvri:,,::jZkYu7r7U1iF
7LrLJ1u1117:,::ri,.:ii;rr7:vrYu;:::v7:.,v2.:;::i;;iiiriririi;rrriiiiir;ri;iiii,:,:i:.LBi :,,,i7:i::::u::,:,FZ7XkS7iYXuL
BB@MBMPX51r.::,,:,.iSuLv::;r:rvii.rLi,..1k.:r:::ii;iirrr7r7r7r7rrrrr7r7rr;7r;irii::,:jB7.;i:i:::7:,:v7r:::ii7.7u11LUSNX
q@OZO1ivvji.::,:.:rYLrrYvL7r  ii..:ii7..JU:::i:iii:rrrr7777v777vvvvv7Lvv7777r7rri;:riu2vvr7v7r:;i;r1riiJr:,:,:::rkEXvuJ
@B@q0L7JLLi.,....:v7:,u;ii:..:i.i::iiiii::rvrr7J7i77v77rvLLYLLjLJYjYJYYYjLYLL7777r77r;;vv7v75u7:;rLv;.:r:,i.:rr:::rri:v
8BM80FriiYi:::.,;rrr:vv,:ir77i,:;i,,:irYiLLv7vv7rvvvYL7LLJJujujUuujUjuJuUuu2u1YLLLLrr7rr7Yri;7vLL;7:;L77:r17::r7i;.:,.r
EB@BBq7L1Uv;vJULu;vjrr7;r,iriii:rr:iL7:ir7;;vvv72uj255FSPSXkqPENE0Eq0X0qqSNN0N0PEPSF1juLPU2;:2XjuLL7FENF5OZEkuLjLiri7iL
@B@O0qXvLr;7L:,,,  .ivjv7iiLL,::riir7i.:iL:.,::,iLr:L7LL77v77;7vvvuvv7LYJLujuJuYjjujUuUYJYuuujuJjJYLYvvv7irr7rvi7Yrv2LL
''')

galadriel = ('''
.. . ................,...,.,,::::iiiirii::,ij@@@B@B@B@B@@@@@B@BMEY:::i::::::::::...........,.,...................... ..
... ..................,.,.,,::::::ii;i7L7vO@@BPY1SS8@@uB@B@B@B@@@B@ESuuvr:i:i:::,,........,.,.........................,
 ... ................,.:.,.,,::i:iiiirvu8@B7:,:i::..ir .:7PBB@B@B@B@XYi;L7irii::::,,.....,,,...........................
... . ................:,:::,::::ii;ir7uM0i:.,.. ..,.. ......:i:,7JuX@@Firi;;rii::::,,...:::,..,.....,.................:
 . ..................,.::::::ii;;rirLOM7:::i:i::::::...:.,.::r7j5MMP0@BB1jr;rrii::::,,.:::,,.,.,.,.,...............,,::
  . ............,.,,,.,,::::iiiir;rLMqi:i:iiiii::,:,,.,::.,:i;rrj8@B@@@B@Zqviii:i::::,:::,,.,.,.,.,..............,:,:::
 . . ..........,,,.:,:,:::iiiri;rYkMOr:i:i::,:::::,,,,.::::::i::,,,iLM@@@@BMjr:iii::::::::,:.,.,.,..............,:,:,:,
. . . ..........,,::::::::iirr77SM@Br::irii:iii:i::::::i::ii::iir;ii::i70B@B@B8Pki::iii::::,:.,.,.,,,.,.......,,:,:,,.,
 . . ..........,.:,::::::iirr7rkM@@r.,:L7;rvrriii;irr7r7;rii:,:i::iv7r::i8B@B@OZFv:iiii:::::,,,,.,.,,,.,.,.,,,,:,:.,...
... . ........,.,,:,:::iiirr7rJ2MMu .i7r;7J7:i;;r;777r7r7r7rri::::::r;;ir.:@@BBOMOZNLri:i::::,:,,.,,..,.,,::::::,.,...,
 .   ..  ......,.,,::::iirr77SBBNO:.:ii;rri:ir77r777r7777YLY7riiiri:.::::::@@@MMEkPOP5vr::::::,:,,.,.,.:,::i::::,,.,...
... ..... ......,,::::iirr77LJXE@Fiiii7rr::i7LUukX5u2uuu55Xk5uLr;irr:,i.. .:kB@8MMOqXkSjvri:,,:,:,,.,,:::::::::,,,,.,..
 ..... ........,.,,::iirr77vY10@Zr;rr7iiirr77vuPN0XkFSu51F1k5177;;iriii7i:i  8@MSZM@OFU2uuv7i:,,.,.,,:::::::::::,,.,...
. ... ........,.,,:,:iiir7LuFYMk..i7uvrii;r77rYXO0ZNP5ku1FkkX2vriir;i::iuL7:.G@MMNMOGU1YYvL77;i,,.,,:::::::::::,:,,....
...... ........,,:,::iir;rruXMBi,rvLvrLr:ii77r;28MZGZZXFkEE8XXFviii;r;:ri7r;i@B@BM0E2LYYv777rrii::::::::::::::,,.,.....
..............,,::::::iiri7UPB@iir:ri,u7::7i77rv0MBBMOZqGO@MOM87i:iiriirrr::SB@B@MkYkYv7vr7rrrririi:i:::i::::,:.,......
 ............,,:::::ii;7r72Pk@MrLSi:.ijr.:ii:i:::758BBGEZ@B@Z1i:.,::::i7iv7:Z@B@B@B@M@G177r77v77r77rii::::::::.,.......
............,,:,::iiiiv7ru@M@PiiGG17rrLr::7P@B@BOJrijEEFqEkrii5EGqOv::7r:75:iB@B@BBBB0OB5r7rvLYLJLL7rii::::::,,........
 . ........,,,:::::iir7rLS0qBUi1vu8k17LuYv7;q:  :@BMLY55FjiJBE..:2:;iLv7rvuU:r0@B@GXkUu8FjLLvLLJYJ77rrii:::,,,.,.,.....
..............::::iirr71ZSFM@E1jriOMYj5q8quL@u  F@LN1rLUuirjMY  ,B:7S1j7urv20YFP@B@MMZEX1UFUuYJLL7v77rrii::,:,:,:,,.,,,
 ........:,,.,:::i:irriuZXZMMP1q27PJ,;F0F2SBB@B@BBN5YriLr:iu0@BMBG2u7Lj7S12OL2Z@B@BBB@MX1qF1jJLL777v777rii::::,:,:,,.,,
... ....,,::::::::ii;irukjNuGPkX17kX. kXZE8GBB@BBMMPr:r77::;5kM@BPYr7vu,rU@Bri8B@B@B@BMqqZMMZJ7r7r7r77777riiiii::::::,:
.,.....,.,:::::::iiiiir5U0OO8k2FU5Su1Lv2ZMMMMBMMMB8Firu51i:i7SuU55YJu17i7LXOELP@@@B@MMPPkSUXZM0u7777r7rv7vrr;rrrii:::::
,,......,,:,::::iir;ivZS0B@@BSSkXX57S5v7kZOOBMMBBOO5iiujJi:;FPGS55kFkLLuriuq@BNG@B@B@B@ME52jL75qu77r77vvYLv77rrrri;ii:i
,:,...,,.,,,:::i:i;rv10X@@B@F2kP1kUriSJr72kE8MMBMBki:7uJJv::NO0NFS127ruFrukB@@BPYBB@B@@@BBFYv7;rr7r7r77LLjLjJL77;riiii:
:::.,.:::,::::iii;rLquPkB@@PJU5uuujJi.JJ77L5N0O8MNuj7r151v77NMGPkUjrr7J7vu5M@@@YPB@B@B@Z8qG1LJ7irr777r7r7777LLL77r;:i::
:r:,.:,::::::ii;irru0q5qB@MM5uju77rrriJE1Yvu2kSEqU7u2Uuuvr7LLq0XUJrrvur77ju@B@SLB@B@B@MXU28MUPGur7r77v7v7v7v7v77rr;i::,
ii::,,::::::iiiir;ruFj2q@B@BZFFLr;Lv7;7OGSuJ55XSk15uFXPkXY77YY1uJ7rL0v;LUqUM@BZv@B@B@B@OOBM52jSq17v7v7v7v7v77rri;irii::
:;::,::::::iiiir77rUMMMMB@B@8qFFLjFPuuv58G5UuF5kk8OBMBBMBBqXFSLL7775kii521F8B@BqSMB@BBB@MMF15FYJLLLYvv777777ri:i:::i:::
i;;i:,::::ii;irr7rvSuEMBBB@B8SGjuNOZXuv,U0E221FkEur::::::.::7XSJvrYU5r7iv:iL@@@PPM@B@BOM@OPFXF5ujvLLL77rriri;i::i:i:i::
:rir:::::ii;iri7rr7q0NN@@@q2U0kiv27r:::,i2Y51kqOGq7:,::i:::iLZESLvvXPLi::::7XM1uM@B@B@MBB@OqSX11uuJL7v77rriiiiii:iii:::
rr;ii:::ii;;rr7r7jGZMNUO@M7;jv;:r:i::::.:u7iv1Z8OMBMMB@B@BO8MG02vLqBJiii;iv1X11N@B@B@BBMBOMqXSk52JYLYLLr7rri;iiiiii:i:i
rv;rri:iir;r777LLPkPSX8@B@XYviii:i,irr:.:uJLi;2Z0GZGqS125qqEEZXJi5uL:rir;;7qMMqM@MB@B@B@M88OqqPq1121JuLYLYvvr7iririiiii
7j777rii;irrvLuu2USGOB@BBB@2Lri;iJ:,r;:.LLJk1rrYXNZq000PNk1Sq1LiJ0r:iuMiiirLZMGEMO@@@B@B@B@BMZEN00ZXXS1JYvL7v77;;iri;ii
75vvvvii;rrrrvY1MBGBM@B@M@M5uv;ri1v:ir,7L7ukNZX2uF0OB@@@B@OE2uLvU@G7i70L:::rLSEMZBB@B@B@B@MMMBOO0EEENEXFUUYLYj77r777iii
rLvYJr:::iJuju2u08MPZM@@@B0U27ri75r:r:rL7r7YSPOMMq08MMMOMGZqPXSvNB@B1uSLi:irrYMB@B@B@B@B@B@MBB@BMNP0ZNENPSS12uUJjLv77r7
MZ1@@Bq7j7:ir7;7777LGMB@B05ui::7u7:i:7Yv777vLYu2UqNkuL77vUXOGXvrE@B@EZOq50OEuXMBB@B@@@B@B@B@BBOOOOkXP008EENP5Uu5UUv7r7v
@B@B@B@@@BBEBBMBOESU@OBBM5Uri:;YYi::LjL77vPkX5ui:r7::::iuPG0XL;i7XMBBB@B@B@MM00EGZ@B@B@B@B@B@B@BMMBqEEG0EPk25221qX2LJvj
;qU8BMBZ8@B@@@B@B@B@BBBBMO0MX27vi:iUjL77r7FG8OXr:v;iirv5EBOEurir7L5BB@B@B@BBOG0GGMMM8EOBBMM@@BMMMME011uUu52U2F2221LLLYU
:ri,ru5B8q@B@MBO@B@@BZGEMO@@@BMkqqNYL77rr;7JkO@57UUvvL0O@B@FL7v77;7POO@B@B@B@MMPOMMBBGOOZqB@@B@BZNBB0FSS5uuuSSXFX1uYvru
7Yrr.;S@ZOB@MEO01PX@8NSXBFUOB@@@@M17rrriiiii7SMMUuLv71Z@B@Zkuv7YLvY5N8M@B@B@BBBMMMZBMGkXqkXB0Z0OB@@@B@B@B@0kUjLLLujj77u
rvv7i;7qvriiriuvJrvPkYMZBB8qBB@@BN1v7rr;77YJju0BOUvrLFMB@MMqSU125FPqO88OBB@B@OZMPSBqS1u7uuEZXM@00EZOMM@B@B@B@BM0kukuriL
rv;:irri:i..:7i;r7vJYJk8PBB@MBB@MOXS21U55NGO8G0B@ZFU2Z@@B@BBOGqEEOM@BM8MM@B@BMPEjkF2u0EMXE8M08MMZOZELiLkXOB@B@B@B@@B8ri
::.:ir7i,7i :7rr7i7uuYjL2F8OOMM8ZN0qENqqEGMB@B@B@BMZ8B@B@B@B@BBMBB@B@MBMBMBM8uFFGMqOXSBMOqGG:i@@@ULJ7rvv;ir0kYFLjY0jMBq
...:irri,:i. :i7i:Lurrr7vYkSrv2q0M8MOMOOZOOMB@B@@@B@@@B@@@B@B@B@@@B@B@B@@@B@BBM@8NFurj1PFu7r,BB@@G7rrrr7riir::,..,:r:Y5
...,i:..::::. ii::irii;iri7uP2L7YJPk08MMBM@B@B@B@@@B@@@B@B@B@B@B@B@B@BB8@B@MGujLr;iiiir7r;i.iEBB@B8r;irr7i7i7vriri.ii:r
.:,:.  ,:,,:   :..::.::i,,ii7uvvrrJZ7iru5GMEO@B@B@M@B@B@B@B@B@@MG8855PuqF7ir;rrv;i:r72U7rr:.:rvPZ0S77i:iijP7Yv717i,,r::
,:::  .:..,.   ., ,:.:i::,,.  ::::r2M7iiiii:7uFZ@8MB@B@BMX8kXGu7i;;::iri::Lrv2jri;r7Yvr77L7: :L;iir;;r:.:7L77i7ukir::i,

''')

def woods():
    while gameOn == True:
        lastRoom = woods
        clear()
        print ('\n'*15)
        print ('You take the pine cone. You close your eyes as you smell the forest from the little object. \
When you open youe eyes again, you are no longer in your bedroom...', end = '')
        input()
        clear()
        print (cisowaKomnata)
        print ("You can see the entrance to the murky chamber in the woods right before you. Who knows what you \
may find inside... Do you dare step inside? y/n: ", end = '')
        choice = input()
        if choice == "m":
            mainMenu()
            break
        if choice == 'c':
            characterSheet()
            break
        while choice not in ('yn'):
            choice = input("You've got to decide now. y/n")
        if choice == 'y':
            clear()
            print ('\n'*15)
            print("You enter the chamber. It is dark and serene. There is nothing but pristine nature all around you. \
You step further into the chamber...".center(120))
        else:
            clear()
            print ('\n'*15)
            print("You don't dare enter the mysterious space, but you couldn't resist its allure. You step in. It is \
dark and serene. There is nothing but pristine nature all around you. You step further into the chamber...".center(120), end = '')
        input()
        clear()
        print ('\n'*15)
        print ("As you look around, you begin to notice tracks in the undergrowth, traces left by someone else. \
You have a feeling that someone's nearby. You look around anxiously...".center(120))
        time.sleep(1.5)
        clear()
        print (galadriel)
        print (('"%s, you haven\'t watched the Lord of the Rings marathon this year!"' % playerName).center(120))
        input()
        clear()
        print ('\n'*15)
        print ("Took you by surprise, huh? The pointy-eared woman looks crossed, seems that she expects your response.")
        print ("Will you:\n\n1) Apologise and swear to mend your wicked ways\n\n2) \
Ask the woman who the hell is she\n\n") #3) Kiss the woman")
        choice = input()
        while choice not in ('1'): #was supposed to be more :(
            print("Please, make a choice: ", end = '')
            choice = input()
        if choice == '1':
            clear()
            print (ania)
            print ("'I beg for forgiveness, my lady. That will not happen again.'")
            input()
            clear()
            print ('\n'*15)
            print ("Your charm will be put to test now:")
            input()
            test()
            charmRoll = rollValue + int(stat['charm'])
            if charmRoll >=12:
                clear()
                print ('\n'*15)
                print ("SUCCESS")
                print ("The scary-looking woman brightens up. 'All is forgiven, my child. \
After all, how could anyone expect you to sit through a spectacle that lasts for a dozen hours?'")
                print ()
                input()
                unwrapGift()
                break
            if charmRoll <12:
                clear()
                print ('\n'*15)
                print ("FAILURE")
                print ("Since the lady doesn't get any less scary you come to realise that \
your apologies might not be enough for her.")
                input()
                print ("Your might will be put to test")
                test()
                mightRoll = rollValue + int(stat['might'])
                if mightRoll >= 10:
                    print("SUCCESS\nYou managed to stave off the mighty elven woman and \
escape through the portal that must have opened in the aftermath of the magical onslaught.")
                    input()
                    unwrapGift()
                    break
                if mightRoll < 10:
                    print("FAILURE\nYou did you best but the mighty elven lady hits you\
 over the head with her staff. Boink! ")
                    damage(random.randint(1,4))
                    print ("You faint and collapse on the floor.")
                    input()
                    unwrapGift()
                    break

mordin = ('''
               .....                    .          ,ri,:7irvii .:::...,:::::,:,,.,.,,,.,,,,,,:::,,.,.,::,:,:::,:,:,:,::
                      .........        .      .  ..vYv.,7i7J7YL,..:...::i::::::,:,::::::::::ii::::::::i:::::i:::::::::r
:..,.......                      .     : .      rkZ0FU.7r:i:;vvui. . :::,:::,:,,.,,,.:,,,:,:::.::i::::::::::ii:::::i:ir
            . .......                 . :.     71LS5ULr7;:ri7rrrJv. .ir,:::,:,,.,.,,,,,,:,:::.............,,:,::::::::i
     .          .:.:.. .                .     rvJvu5uu;::..i;i::r7v,,7::,:,:.,...,.,,,,,,:,:..::,,.........,::.,...,..,
,,:..:  . .:,...,,,.      . .        ..      ivJ7vP2Lv77::    ::irvLLi.,:::.,.,.,.,,,,,,,.:,.,:::::::,:.,.,.,,,.,.:,::i
:::::,::::,ir;i:..   .   ....      . .      ruFS5O00SqXUir: r    iLLuj: .,.,.,.....,,,.,.,:..r::,:,:,:,,,:,,,,,,.,.....
.::::,::iiiii::,.    .   . ..       .      ik1OF0MBZB@@MXU: ,r    :722Zj. ..,.,...,,,,,,,,: ,:,.............:,....:,::i
       :::i:...:,::,.   .. ...      :     :uFE@@O@B@B@B@ML,:..i:::.:i7kO07 ..,...,.,.,.,.:..,:..............,,.......,:
   :   .,..       ,r:   . . .       ,     :iuOO@@B@B@B@BM1j...YUji..::rqBBZ ..,...,.,,,.,,..,,,...... . . ..,.... ....:
   .   ...         2    ..,:.      :      ..:i5BB@B@@@B@MBu.,r:7Y7ii:,,LM@@L ..,.,.,.,,,,, ..,........ . . ... . .....,
      ,,ii,. ,.   .i   ...::.      ,       .  u@BB@B@B@B@Bu:L. .u: ::vMJFE0B. ,...,,,.,,:............ .     .   . . ..,
     i,,:i      . :.   , .:,      .        .. :5Lrrrr7rrrLii1, ,1F.::7M5   i:......,...,,....,......       ...     ....
    .,,...        ,   ....:.      :       .:::       YY.....i :7vFiYi.i,::  ,...,.,.,.,,, ..... ... . .     .     . . ,
  :riii;:.     ..:,   ...:,      ..        .ri:. iL     :::,.  j757S:  :,@ ,.,...,.,.,,:............ . . . ... .   . ..
.,iirrr:... . .  .,   ,.,:,      :        .  :LPi7SF:    . i.  i0Eki, ,  G..,.,.,.,.,.,,............  . .   .     . . .
 :iiir:.          .  ..,::..     :             k0J;uSNFji:::   rOGS,    :u ,.,...,.,,,,, ,...,...... . . . ... . . ....
:ii;:            .   ..::...    ,               LqSLri7ri..    7@MF   :iXr..,,,.,,:.,,:..,,..,......... ... ... . ....,
ir:i:         i.,.   .,7....    :    .   .    L: :i7irrr:i:,.L:L@@L..  .r:.,,,,,,,,:,::. ,...,...... . ..............,:
i;:::.          .   irvi ..    .,    .        jv.  .,::i7rL:uGiX@Br,r.,ii.:,:,:,:,:,:,:..     .         . . . . . . . .
:ri.           .,.  :i:, ...   :         .   .j;rL7LuJ7r::qXEPv@B8.7v;::,:,:,:,:,:::::: ,;:::i::,:,..,.,,,.,,:.,,,.,.,,
:rv.           .:   ..,....    .        :.:i:rPvu70q0E0r70B8OXGBML:Bv.:,:::::::,:,::::: :::,:::,,,,.........:,......,.:
iY:.   .       ..  .......    ..   .:..:;iir:LPYUYvkZZZXuGBMMOOMqrZO.,::::::::::,:::::, ii::::::,,,....,.,.,,,.,.,,,.,:
iri            .   .......    : ..,,:,::77LLj2XvrPuuGB@MMBBMMBBOqF@1 :::::::::::::::::, ii:::::,:,,...,.,.,,::,.,.,.,,:
:rr7,         .,   :.:....   .:,,..:vqO81u777rr,:PGqO@B@B@@@B@B@M@BM.i:i:i::::::,:.,.:  ::::,::,,:.....,.,.,,:.,.,.,,::
ij;;.     .  .,.  ,,,:,.. 7.J: ::LBB@Bu,...:i:r uuEO@GBB@BZ8@B@B@B@@:.ir7ri::::..:ii7i. ,,:,,,:.,,,...,.,...,,..,.,,,,:
:r::     .   , .  ,,,::. :L,O. ,B@B8:  ..iii:UY OZjkB0irr:riiuLruj7M     ..i:,.iv2FL,S1u:..,.:,,.,...........,.......,:
iri:.   .   .     ,.,:: YFL:M.  LB,  .::::   Mr @MNiL@@BGFuvr:iii7@7       MSi77L7jvrUU5Bi,.,,,.,.....................,
.,,:       :. .  ....: :GuMBG    i .:iii: ,uM@. G@BE:;Z@@@B@B@B@B@M       :2L2vi7L7vJuUF1MF..,,,.,...........,.........
....  .   ri,r.  .,.,: ,8:25q.    i::,:, P@u.    B@@B7:vM@MOBB@0S2::rii, .Z27v;urvY7LFUFjZL:.,,.,.,.,.,...,.,,,.,.,.,.:
 .    ..,1L.::   ,..::  u:LLj;   r:::,, .@B       u@B@vi::::,: Lu..i:iir;;i;72..;vvJvY1X55,,.,,,.,.,.,.,.,...,.,.,.,,,:
..   .::1kY:.    ....,  i:rU57   i::ii: uB@X         .i;.,      7u::i:ii:::,,:r,uvJY1u.LE ..,,:,:.,.,,,.,.,.,,:.:,,,,,:
 . .:7rLLi::     .,:..    .viv   vii::,.8BB@Bj                   B7,:i::i:::::ir:ir77JvY       .
 ,  i7v7j:,  .  :ii.            :r7i;i::@O@B@B@@2r:            :LB7.ii .U;:::::.:rri::. :::,:,:...:.,,,,,,:,:,:::,:,:,:
 ,  :v25L,   .  ..              Jr,iii.1BBB@B@B@@@Z@BOPSj7iJXMB81@u,:;  r7:::::. ,v,,:, .:.,.::   ,,...................
. .:v1Fr.  .:.            .,    ;Br::,uBO5GBBMB@@;  .:7UXF5uL:  ;BO.:i. :v::::i. .Y:iii .....,,   ,...................,
 ..,,,.    .              :. .   MB::OBBO0UuSOM@B@GFj7i:,,.. ivNB@i ::  :Y,::::, .L::ii .,...:     ,...................
                          i         @B@BBB@M0P008M@BPB@i:::,.B@ruBN Gi  ,1:,:,::  vi::i.....,       ,..................
,:........ ...........    i    .   UB@B@B@B@B@B@B .r7kuiiri::ii L@BGO@Y  r,iJLrr..v7:ir: :,:        .,.,.,.,.,.,.,.,..,
''')

def space():
    while gameOn == True:
        global lastRoom
        lastRoom = space
        clear()
        print ('\n'*15)
        print ("Your eyes are closed. You feel a slight sensation of weightlessness. \
You try to keep the breakfast you consumed not so long ago in your stomach.")
        print ("Your endurance will be put to test.")
        input()
        test()
        enduranceRoll = rollValue + int(stat['endurance'])
        if enduranceRoll >= 12:
            print ("SUCCESS\nYou managed to keep the content of your stomach where it was supposed to be.")
            input()
        if enduranceRoll < 11:
            print ("FAILURE\nYou cannot hold the breakfast in the low gravity conditions.")
            input()
        print ("'Oh, hello %s. I see you're awake now." % playerName, end = '')
        input()
        clear()
        print (mordin)
        print ("The voice you heard belongs to an unimposing, friendly-looking alien.")
        input()
        clear()
        print ('\n'*15)
        print ("Would you like to:\n1) Shoot him in the back\n2) Ask him why are you \
on a space ship")
        choice = input()
        if choice == "m":
            mainMenu()
            break
        if choice == 'c':
            characterSheet()
            break
        while choice not in ('12'):
            choice = input("You've got to decide now. y/n")
        if choice == '1':
            print ("You don't have a gun. Yet.")
            input()
            clear()
            print (mordin)
            print ("'In case you forgot out mission, we are on our way to save the Krogans \
from the genophage! Exciting, isn't it? By the way, here's your weapon.")
            get('laser pistol')
            input()
        if choice == '2':
            clear()
            print (ania)
            print ("'Uh, hello. What am I doing in the outer space with you guys?'")
            input()
            clear()
            print (mordin)
            print ("'I am glad you asked. We are on our way to save the Krogans \
from the genophage! Exciting, isn't it? By the way, here's your weapon.")
            get('laser pistol')
            input()
        clear()
        print ("It sure is exciting. On your way to your destination you mow down \
legions of nasty looking aliens until you reach the slowly crumbling tower.")
        input()
        clear()
        print (mordin)
        print ("That's it. Now I need to climb the tower and sacrifice myself \
to save the Krogans and redeem myself.")
        clear()
        print ('\n'*15)
        print ("Would you like to:\n1) Shoot him in the back\n2) Let him go")
        choice = input()
        if choice == "m":
            mainMenu()
            break
        if choice == 'c':
            characterSheet()
            break
        while choice not in ('12'):
            choice = input("You've got to decide now. y/n")
        if choice == '1':
            print ("You shot the friendly alien dead. I hope you are happy. \
You use the space ship to get back to your bed.")
            input()
            unwrapGift()
            break
        if choice == '2':
            print ("This choice stand against your nature. Authorisation is required.")
            authorisation
            if authorisationPassed == True:
                print ("You let the friendly looking alien get into the tower. When \
all is done you get back to the space ship so that you can return to your bed.")
                input()
                unwrapGift()
                break
            else:
                print ("You couldn't overcome your predatory nature. You shot the \
friendly alien dead. You use the space ship to get back to your bed.")
                input()
                unwrapGift()
                break

krzys = ('''
 ,   . .      .:..   .                         ,.,.,...,...,
.,. ..,.  , ,,,..   . .                     .  ::,,.,,,,..,,
.:   ...  ..   ...   .                       . :,,.,.,.,,,.:
,,  ...   . ..,.,                              .,.,.,...,.,.
.:  .,.. ..,.:,.         .               .   . ,,,.,.,.,.,.,
,,. ,.,.,....            .                     ,:.,.,.,.,,,,
,;  ,,.,.,,:,              ,.,:.               :,,,,.,.,.,.:
:;  ;,,.,,:.    ..        ,:L;:.:,.             ,.,.,.,.,.,,
,L  ::.,,..   ,irLi:.,:;:::rLv,,     ..:,.      .,.,.,.,,,.:
:i  r,:.     .::iivvTvTvTLvryvYLv;iivTCyyr,      ...,...,.,,
,L .i::,    .,,;:iivrvLvLTvUThCE0EkPyhUFUhc:    ,. ....,.,.,
:r .v:i.    ..:,::iiLrl7lvYvct0CPkEPkcyTuYhu,    :L::.. ...,
:l ,i:,    ..,,:,:,;rLrvLlLTYhFCtCFkcuTUvcvhr.   i::::::,,.,
;r..L:i     ,,:,:,::i;LivrvvcYuTucuYcvcvYLTYY.   ;Y;i::,::::
:u ,i7:    ..,:;:;;i:iiv7L7tUyctTTvcvUlUYYvUL:   .TlvlLL;;,:
ir  ,,    ....::;;vrLivLviYTychUyTyYyTulcvTvc:   .uvvrLrv7LL
:l .vY   . ,,,,::;rl7lLcLlYclUUFthcFUtYUvYLUv;    cl7LiLiL;l
vU.,y,     .,,;:i:YYviTcyctlUtCtkUFTUYcvTLTvY:    Fvl7vrLiLL
LT ;c             .i:;;cYuvTvcLcYyuhyCuFuuvlLL   vUTLlLv7Lil
iY.iC                   :LU7iivvlLvvlLlvvlhUtU, ,FuYcLYLviLv
7t Y,                                      ,;c. .TLL7viLivic
Yl i.                                           :LviLiviLivL
Ly LT                                           ;uirr7;vrr:T
cU ;0                  iy0;                     : .;iiL;Lirv
YF ihL .               rrFh                  L,,L:,L;rrv:Lil
Tc ryu,u              ,;ccC;              , .F. c;7;7rr;L;LL
ly LYt v.          . ,ivUPch            ,v. T7:,,iiL:7;7ir;l
cU Lcv:,, ,.. . .il .7TLSBycL   ........:  ruLviL:rr7:viiirL
Ly YLv7,,  .,;;Luc   rUtuSyky; .,, ... ..:cU;iiu;L;iiL;7;r;v
TY Lvil ,..,iivvL     :iL,. :L, ..,.,.;tkcYivvyLi;L;7;L;7;rr
rl YrLL  : .,iiL,        ,.,ikPSTuvlLUUTLviiLcrirri7iri7;7;v
lL.vviv ,:. ,,,.,     .;.,:,;iuTFcuTtYcrLi7:i:r:7iv;r;7;r;iL
Lv ciLr .i.. .     .,LtU.      ,,L7YvYiLiL;i;LiiiL;Lr7;LiLiY
T;.vLiL .i, .         ;7v,.   .   ;7viL7vir:riL;riL;ri7;Lirv
7i.Y;7i .l:.., . ,.... . .., .,   .TrLivili:;7r7;rr7;iir:L;v
L:.vrir ,;;:... .,::;,::i:iiTlt7. :7viLiLlr:i;7ir;i;L;7;i:Lv
L: c;L; .r:;,.    ....     .:7il;:;LrLr7vT:iiLii7Lii:L;r;7:Y
Y..l7ii :;: ..  ,  .:,,. ...::;;7:7iL7LLtv;;Li7:i7v;r:L;r;i7
Y, c:7: ,r,.    ,:,:illviYct7r:;:riL7LvuYl:i;vrr;;7v;7ir;r:Y
c,,Li;: :;:      .:,:7uYUlTlUvU::;Lr7vyYtvr:::vrL:i7L;r;r;i7
v,.Y:L: ,L;. .     . ,,i:;:7rl;, :iivhTulULr:;,iiL;;;v;r;L;v
Y.,L;i: :::               . .     :iyctTUlUlYvv;7;i:,:L:iirL
T..l:r, ,,.:,                    .lYYyctYUTyTtTtYtvlr::7:;:7
y .Li::.7ri:,                  .,Y0UyctlUTytCuyTtcyUCUtlYrrr
T .L:;:uvT;,                 .,vLkuFctTuTtchuhuycuTyUyUFuyYk
F ,i;::r;.      . . . . . . .:cTFttctYtcyThuCttvTvTvTvcvcvTU
Y ,L:i:,     .     ..,.::;:;vCuFYcTtTtUFUhuyvviv7vLTYtcycuvF
Y ,i;::.,.,,:,:,:,. ,,;rcYyFCUtYYlFUyuuTuvYrv7TYtTtUhtCtCUUF
''')

def endGame():
    global gameOn
    while gameOn == True:
        global lastRoom
        lastRoom = endGame
        clear()
        print ('\n'*15)
        print ("The box now is empty. You raise your eyes and look around the room. \
The room you're in belongs to a house from a countryside. Also, there is another \
person in the room.")
        input()
        print (krzys)
        print ("'Well, well, well. You've finished your adventure and reached my lair.'".center(120))
        print ("'Did you enjoy?'".center(120), end = '')
        input()
        print ('\n'*15)
        print ("So, did you enjoy this little adventure?\na) Yes ^_^\nb) no :C")
        choice = input()
        while choice not in ('ab'):
            choice = input("Please answer the question")
        if choice == 'a':
            print ("Well, I am glad that despite many shortcomings the game managed to raise your mood.")
            input()
            gameOn = False
            mainMenu()
            break
        if choice == 'b':
            print ("IMPOSSIBIRU!")
            input()
            gameOn = False
            mainMenu()
            break
def unwrapGift():
    while gameOn == True:
        global lastRoom
        lastRoom = unwrapGift
        clear()
        numerals = ('none', 'one', 'two', 'three')
        giftsintheBox = numerals[len(gift)]
        if len(gift) == 3:
            print ("It's time to unpack the present you've noticed in the foot of your bed. It's \
a box tied with a red lace. Do you want to loosen the lace? ", end = '')
            choice = input('y/n: ')
            if choice == "m":
                mainMenu()
                break
            if choice == 'c':
                characterSheet()
                break
            while choice not in ('yn'):
                choice = input("You've got to decide now. y/n")
            if choice == 'y':
                print("\nThat's the spirit! You untie the lace and take it off. Do you want to unwrap \
the packing paper now?")
            else:
                print("\nThat's not an option. Your hands untie the lace and take it off before you \
can order otherwise. Perhaps you'll be more willing to unwrap the packing paper?")
            choice = input('y/n: ')
            if choice == "m":
                mainMenu()
                break
            if choice == 'c':
                characterSheet()
                break
            while choice not in ('yn'):
                choice = input("You've got to decide now. y/n")
            if choice == 'y':
                print("\nWe're getting closer! You tear the paper with excitement! The last \
thing remaining is to open the box. Are you ready?")
            else:
                print("\nWell, now that the paper isn't held by the lace it peels away off the \
gift on its own. The only thing you have to do now is to open the box. Are you ready?")
            choice = input('y/n: ')
            if choice == "m":
                mainMenu()
                break
            if choice == 'c':
                characterSheet()
                break
            while choice not in ('yn'):
                choice = input("You've got to decide now. y/n")
            if choice == 'y':
                print("\nYou open the box with anticipation.")
            else:
                print("\nRegardless of your readiness, the box opens up like a beautiful \
flower you didn't care to open.")
        if len(gift) == 0:
            endGame()
            break
        else:
            print ("You're back on your bed with the box wide open on your lap.")

        if giftsintheBox == 'one':
            print ("One last gift remains in the box:")
        else:
            print ("There are %s gifts in the box:" % str(giftsintheBox))
        if 'pinecone' in gift:
            print ("p) a pine cone?")
        if 'spaceship' in gift:
            print ("s) a toy space ship")
        if 'watch' in gift:
            print ('w) a hand watch')
        choice = input ("The choice is yours: ")
        if choice == "m":
            mainMenu()
            break
        if choice == 'c':
            characterSheet()
            break
        while choice not in ("psw"):
            choice = input ("Please, make a choice: ")
            if choice == "m":
                mainMenu()
                break
            if choice == 'c':
                characterSheet()
                break
        if choice == 'p':
            del gift['pinecone']
            get('pinecone')
            woods()
            break
        if choice == 's':
            del gift['spaceship']
            get('spaceship')
            space()
            break
        if choice == 'w':
            del gift['watch']
            get('watch')
            prague()
            break

if playerName == 0:
    print ('Hello! What is your name?'.center(120))
    playerName = input (' '*58)
if zodiac == 0:
    clear()
    print ('Please select your zodiac sign:'.center(120))
    print ('''
             .5ku   uS1.               N@2         v@O.                                                   .
            O@175@P@F72@8             :@LBB.      B@v@v             .OXU7i77rLuEB:                  :OBuq11M7
            @.   :@:   .@.                P@:   .@@                  iriBBi.@B...                 i@@F.B,   @7
                  B                        vB@@@BX                      J@  k@                   5B:   @k   BM
                  @                        Mq:.,1B.                     uB  ZB                  7B      SZqj@v
                 iBr                      BG     LB                     7@  E@                  B@2EM2     7B
                 O@M                      8X     2@                     JB  NB                  @;   @5   PB
                 :2:                       MZurYM@.                  vriM@i:B@:r7,              NZ   EkLB@q
                                             7J7,                    F2vri77rivuk:               7YLurL0i

                  1                           2                           3                           4
                Aries                       Taurus                      Gemini                      Cancer

                .752r
               @BM5SO@M
              S@      @M                ZB.5@ XBBMMBN                                           ;  :, .:..
              r@,     j@                :@ ,B. @B5i8B@                                         7B@ @B:L@B:
             7G@@u    OB                 B  @  u@   @B                  :uPSY                   MB .@  B@
            BM   0B   BP                 @  B  F@   BF                i@BFvYE@G                 GB .B  @B
            @,    @   M@                .B  @  u@ iB2            LP51q@i      @B2UFSU           GO  @  B@
            7@r:Y@u   .@B               1@7vBi PBO5              5OZ0E7        XPqPOX           GM  B  @B    F,
              rr7.                       v, iFOB@                FXXXFNN@B@B@B@MMMM@M           @B P@2 B@  L@B
                                            vS 1B                :i;:;:ii7rrrr;rirr7r           ii  v  rBBvuX7
                                            :  i,                                                        ,,

                  5                           6                           7                           8
                 Leo                        Virgo                       Libra                      Scorpio

                        :             FL.   i7i
                      5@@:           .MBB. NBOB                                                 7@B       i@B:
                     N@:8               kG:@  @i                                                 :@B7    O@N,
                   YB0                   @B.  BO                  .FNv     i,   .i   ,.            7BL  @@
                 .@B.                    B@   @@  uSFY           rBkFB@2vS@B@@JXZB@1GO              iB r@
            :.  0@2                      @B   7@k@7..LB:               iLi   :8;  .1L              rq@M@B0B.
            rS@BMkX:                     .     P@:    @Y         r@B@M,  .ZBF  :BF  :r              uB Y@
            :@M                                @0MMZG@Z         :j.  ;2ZGML,1@Bu 5B@B              ,@1  @@
            Lv                             r.:M8  ,;i                                            .1BS    B@7
                                          j@B@7                                                 ,7j.      rFi

                 9                            10                          11                          12
            Saggitaurus                    Capricorn                   Aquarius                     Pisces
''')
    zodiac = input(' '*59)
    if zodiac == '7':
        print ("That is correct, you were born under the zodiac sign of Libra, which ruling planet is Venus.".center(120))
        time.sleep(2)
        print ("That means that today is your birthday.".center(120), end = '')
        input()
    else:
        print ("Ah, you cannot cheat the all knowing stars! You were born under the zodiac sign of Libra, \
which ruling planet is Venus.".center(120))
        time.sleep(2)
        print ("That means that today is your birthday.".center(120), end = '')
        input()
clear()
print ("")
print ("Dear " +playerName+ ", since birthdays are all about gifts, we are about to make use of\
 the gift that you've had with you for quite a while now. The gift of imagination.")
print ("")
print ("Before we let you stride the imaginary realms we will have to establish your physical and mental faculties\
 that will\nrepresent you in this world. We will let fate decide:")
input()
clear()
print (playerName.center(120))
print()
lifeTop = random.randint(10,15)
life = lifeTop
print (("Your life: " +str(life)).center(120))
time.sleep(1)
stat['might'] = str(random.randint(0,5))
print (("Your might: + " +stat['might']).center(120))
time.sleep(1)
stat['nimbleness'] = str(random.randint(0,5))
print (("Your nimbleness: + " +stat['nimbleness']).center(120))
time.sleep(1)
stat['endurance'] = str(random.randint(0,5))
print (("Your endurance: + " +stat['endurance']).center(120))
time.sleep(1)
stat['commonSense'] = str(random.randint(0,5))
print (("Your common sense: + " +stat['commonSense']).center(120))
time.sleep(1)
stat['slyness'] = str(random.randint(0,5))
print (("Your slyness: + " +stat['slyness']).center(120))
time.sleep(1)
stat['charm'] = str(random.randint(0,5))
print (("Your charm: + " +stat['charm']).center(120))
time.sleep(1)
stat['stomach'] = str(random.randint(0,5))
print (("Your stomach: + " +stat['stomach']).center(120))
while finished == False:
    clear()
    playerStats()
    choice = input ("What would you like to do?\n\
1) Continue\n2) Change the fate, pump up one of your faculties.\n")
    if choice == '1':
        print ("\nVery well, let's proceed.")
        time.sleep(2)
        choice = ''
        finished = True
        lastRoom = breakfast
    if choice == '2':
        authorisation()
        if authorisationPassed == True:
                print ("\nVery well. Please provide the new value:")
                stat[input('Trait: ')] = input('Value: ')
                choice = ''
                authorisationPassed = False

while gameOn == True:
    lastRoom()
