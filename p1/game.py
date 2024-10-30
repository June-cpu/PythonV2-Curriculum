import random
from riddles import riddles

def intro():
    description = r"""
    
     :
                       :
                       :
                       :
        .              :
         '.            :           .'
           '.          :         .'
             '.   .-" .  -.   .'                                   .'':
               '."          ".'                               .-""-.'         .---.          .----.        .-""-.
                :            :                _    _        ."     .' ".    ..."     "...    ."      ".    ."       ".
        .........            .........    o  (_)  (_)  ()   :    .'    :   '..:.......:..'   :        :    :         :   o
                :            :                              :  .'      :       '.....'       '.      .'    '.       .'
                 :          :                             .'.'.      .'                        `''''`        `'''''`
                  '........'                              ''   ``
                 .'    :   '.
               .'      :     '.
             .'        :       '.
           .'          :         '.
                       :
                       :
                       :
                       :
    
    
    """
    intro_text = (
        "Welcome to 'Astra Lost in Space'!\n"
        "In this text-based adventure game, you will join a group of friends stranded in space after a mysterious incident.\n"
        "You must explore various planets, solve riddles, and gather resources to survive and find a way back home.\n\n"
        "About the Anime:\n"
        "Astra Lost in Space follows a group of high school students who go on a camping trip in space.\n"
        "After an unexpected event, they find themselves on a journey across uncharted planets, facing numerous challenges.\n"
        "As they navigate through these strange worlds, they must rely on each other and their wits to survive.\n\n"
        "Are you ready to embark on this adventure? Let's begin!\n"
    )
    print(intro_text)

def ilavurs():
    
    description = (
        "Ilavurs is a lush, tropical planet filled with giant vegetation and diverse animal life. "
        "After being stranded, the crew lands here seeking shelter and resources. "
        "They explore the vibrant ecosystem but must also be cautious of the wildlife and potential dangers lurking within the dense foliage."
    )
    return description, random.choice(riddles["easy"])

def shummoor():
   
    description = (
        "Shummoor is a harsh desert planet characterized by extreme temperatures and dangerous sandstorms. "
        "The crew faces difficulties finding water and shelter as they navigate the vast dunes. "
        "They must work together to survive the relentless environment and avoid getting lost in the storms."
    )
    return description, random.choice(riddles["easy"])

def lulucia():
    description = (
        "Lulucia is an ice-covered planet with sub-zero temperatures and limited resources. "
        "The crew struggles to find warmth and sustenance in the freezing conditions. "
        "They must use their ingenuity and teamwork to survive while searching for a way to leave the icy wasteland."
    )
    return description, random.choice(riddles["easy"])

def vixia():
    description = (
        "Vixia is a seemingly peaceful, forested planet rich with a variety of life forms. "
        "The crew initially finds it inviting, but they soon realize that the planet hides dangers among its lush landscapes. "
        "They must navigate the complex ecosystem while being mindful of the unknown threats that lurk in the shadows."
    )
    return description, random.choice(riddles["normal"])

def arispade():
    description = (
        "Arispade is a mysterious planet with peculiar atmospheric effects that disrupt communication and navigation. "
        "The crew faces confusion and disorientation as they attempt to explore the planet. "
        "They must rely on their instincts and work closely together to overcome the challenges presented by the strange environment."
    )
    return description, random.choice(riddles["normal"])

def icriss():
    description = (
        "Icriss is a volcanic planet known for its hazardous lava flows and frequent seismic activity. "
        "The crew must tread carefully to avoid the dangerous eruptions and navigate through the treacherous terrain. "
        "Their survival depends on quick thinking and effective communication to stay safe amid the planet's volatility."
    )
    return description, random.choice(riddles["normal"])

def galem():
    description = (
        

        "Galem is a gas giant featuring floating land masses, making it challenging for the crew to find stable ground. "
        "As they explore, they encounter unique phenomena and must be cautious of the unpredictable weather patterns. "
        "The crew's ability to adapt and think creatively is put to the test as they navigate the obstacles of this unusual world."
    )
    return description, random.choice(riddles["hard"])

def earth():
    description = (
        
		r"""

				_-o#&&*''''?d:>b\_
          _o/"`''  '',, dMF9MMMMMHo_
       .o&#'        `"MbHMMMMMMMMMMMHo.
     .o"" '         vodM*$&&HMMMMMMMMMM?.
    ,'              $M&ood,~'`(&##MMMMMMH\
   /               ,MMMMMMM#b?#bobMMMMHMMML
  &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk
 ?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L
|               |MMMMMMMMMMMMMMMMMMMMbMH'   T,
$H#:            `*MMMMMMMMMMMMMMMMMMMMb#}'  `?
]MMH#             ""*""*#MMMMMMMMMMMMM'    -
MMMMMb_                   |MMMMMMMMMMMP'     :
HMMMMMMMHo                 `MMMMMMMMMT       .
?MMMMMMMMP                  9MMMMMMMM}       -
-?MMMMMMM                  |MMMMMMMMM?,d-    '
 :|MMMMMM-                 `MMMMMMMT .M|.   :
  .9MMM[                    &MMMMM*' `'    .
   :9MMk                    `MMM#"        -
     &M}                     `          .-
      `&.                             .
        `~,   .                     ./
            . _                  .-
              '`--._,dd###pp='

		
		"""
        "Earth is the final destination for the crew, a place of familiarity and comfort. "
        "After their long journey, they are finally home. "
    )
    return description, "Congrats, You won!"


