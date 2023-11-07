from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


til = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text= "O'zbekcha"),
            KeyboardButton(text="Русский"),
            KeyboardButton(text="English")
        ]
    ],
    resize_keyboard=True
)

lang = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Buyurtma berish"),
        ],
        [
            KeyboardButton(text = "Sozlamalar"),
            KeyboardButton(text = "Biz bilan bog'lanish")
        ]
    ],
    resize_keyboard=True
) 

in_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = 'Lavash', callback_data= 'lavash'),
            InlineKeyboardButton(text= 'Hot dog', callback_data='Hot-dog')
        ],

        [
            InlineKeyboardButton(text = 'Sandwich', callback_data='Sandwich'),
            InlineKeyboardButton(text= 'Shaurma', callback_data= 'Shaurma')
        ],
         [
            InlineKeyboardButton(text = 'Burger', callback_data= 'Burgur'),
            InlineKeyboardButton(text= 'Donar', callback_data='Donar')
        ],
        [
            InlineKeyboardButton(text = 'Gazaklar', callback_data= 'gazak'),
            InlineKeyboardButton(text= 'Ichimliklar', callback_data='drinks')
        ],
        [
            InlineKeyboardButton(text = 'Desertlar', callback_data= 'Desert'),
            InlineKeyboardButton(text= 'Pizza', callback_data='pizza')
        ],
    ]

)

hot_dog_menu = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= "Hot dog baget dabl", callback_data="dabl"),
            InlineKeyboardButton(text= "Classik hot dog", callback_data="clas hot")
        ],
        [
            InlineKeyboardButton(text= "Korolevskiy", callback_data="korol"),
            InlineKeyboardButton(text="Tovuqli hot dog", callback_data="chick-hot")
        ],
        [
            InlineKeyboardButton(text= "Ortga", callback_data="back33")
        ]
    ]
)






dabl_dog = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back26')
        ]
    ]
)

classic_hot_dog = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back27')
        ]
    ]
)


Karol = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back28')
        ]
    ]
)

chick_hor_dog = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back29')
        ]
    ]
)
















sand_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Club Sandwich", callback_data="club"),
            InlineKeyboardButton(text="Classic sandwich", callback_data="clas sand")
        ],
        
        [
            InlineKeyboardButton(text="Ortga",  callback_data="back32")
        ]
    ]
)



classic_sand = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back30')
        ]
    ]
)

chick_sand = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back31')
        ]
    ]
)








###         SHaurma Menulari





shaurma_menu  = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = "Mol go'shtki shaurma", callback_data="besh"),
            InlineKeyboardButton(text="Tovuq shaurma", callback_data="chicksh")
        ],
        [
            InlineKeyboardButton(text="Mol go'shtli (qalampir) shaurma", callback_data="bef-pep"),
            InlineKeyboardButton("Tovuq go'shtli (qalampir) shaurma", callback_data="mix")
        ],
        [
            InlineKeyboardButton(text = "Ortga", callback_data="back7")
        ]
    ]
)

Beef_shaurma = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = 'Mini', callback_data= 'mini5'),
            InlineKeyboardButton(text= 'Classic', callback_data= 'classic5')
        ],
        [
            InlineKeyboardButton(text= 'Ortga', callback_data= 'back1')
        ]
    ]
)

mini_beef_shaurma = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back3')
        ]
    ]
)

classic_beef_shaurma = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back4')
        ]
    ]
)






shaurma_chick = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = 'Mini', callback_data= 'mini8'),
            InlineKeyboardButton(text= 'Classic', callback_data= 'classic8')
        ],
        [
            InlineKeyboardButton(text= 'Ortga', callback_data= 'back19')
        ]
    ]
)

mini_chick_shaurma = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back6')
        ]
    ]
)

classic_chick_shaurma = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back5')
        ]
    ]
)



#####     Beef pepper shaurma




shaurma_beef_pep = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = 'Mini', callback_data= 'mini9'),
            InlineKeyboardButton(text= 'Classic', callback_data= 'classic9')
        ],
        [
            InlineKeyboardButton(text= 'Ortga', callback_data= 'back20')
        ]
    ]
)

mini_beef_pep_shaurma = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back21')
        ]
    ]
)

classic_beef_pep_shaurma = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back22')
        ]
    ]
)





###     Beef pepper shaurma




shaurma_mix = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = 'Mini', callback_data= 'mini10'),
            InlineKeyboardButton(text= 'Classic', callback_data= 'classic10')
        ],
        [
            InlineKeyboardButton(text= 'Ortga', callback_data= 'back23')
        ]
    ]
)

mini_mix_shaurma = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back24')
        ]
    ]
)

classic_mix_shaurma = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back25')
        ]
    ]
)









###              Lavash Menulari



lavash_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = "Mol go'shtli", callback_data = 'Beef-lavash'),
            InlineKeyboardButton(text = "Mol go'shtli (qalampir)", callback_data = 'pepper-lavash')
        ],
        [
            InlineKeyboardButton(text = "Tovuq go'shtlik", callback_data = 'chick-lavash'),
            InlineKeyboardButton(text = "Tovuq go'shtlik (qalampir)", callback_data = 'pep-chick')
        ],
        [
            InlineKeyboardButton(text = "Ortga", callback_data = 'Back')
        ]
    ]
)

###        Pepper Chicken Lavash

pep_lavash_chick = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = 'Mini', callback_data= 'mini6'),
            InlineKeyboardButton(text= 'Classic', callback_data= 'classic6')
        ],
        [
            InlineKeyboardButton(text= 'Ortga', callback_data= 'back16')
        ]
    ]
)

mini_lavash_chick_pep = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back17')
        ]
    ]
)

classic_lavash_chick_pep = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back18')
        ]
    ]
)
######        Chicken Lavash

lavash_chick = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = 'Mini', callback_data= 'mini7'),
            InlineKeyboardButton(text= 'Classic', callback_data= 'classic7')
        ],
        [
            InlineKeyboardButton(text= 'Ortga', callback_data= 'back15')
        ]
    ]
)


mini_lavash_chick = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back8')
        ]
    ]
)

classic_lavash_chick = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back9')
        ]
    ]
)

###     Pepper Lavash

pep_lavash = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = 'Mini', callback_data= 'mini1'),
            InlineKeyboardButton(text= 'Classic', callback_data= 'classic1')
        ],
        [
            InlineKeyboardButton(text= 'Ortga', callback_data= 'back12')
        ]
    ]
)

mini_lavash_pep = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back11')
        ]
    ]
)

classic_lavash_pep = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back10')
        ]
    ]
)

#####        Beef Lavash

beef_lavash = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = 'Mini', callback_data= 'mini3'),
            InlineKeyboardButton(text= 'Classic', callback_data= 'classic3')
        ],
        [
            InlineKeyboardButton(text= 'Ortga', callback_data= 'back13')
        ]
    ]
)

classic_lavash_beef = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back14')
        ]
    ]
)

mini_lavash_beef = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back2')
        ]
    ]
)





#                           Gamburger




Burger = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = 'Gamburger', callback_data= 'ham-bur'),
            InlineKeyboardButton(text= 'Chizburger', callback_data= 'cheese')
        ],
        [
            InlineKeyboardButton(text= 'Ortga', callback_data= 'back34')
        ]
    ]
)

Gambur = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back35')
        ]
    ]
)

Cheese_bur = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back36')
        ]
    ]
)



##############          Donar


Donars = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = "Go'shtli donar", callback_data= 'beef-donar'),
            InlineKeyboardButton(text= 'Tovuqli donar', callback_data= 'chick-donar')
        ],
        [
            InlineKeyboardButton(text= 'Ortga', callback_data= 'back37')
        ]
    ]
)

donar_beef = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back38')
        ]
    ]
)

donar_chick = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back39')
        ]
    ]
)




######          GAZAKLAR




gazaklar = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = "Fries 15 gr", callback_data= 'free'),
            InlineKeyboardButton(text= 'Kartoshka Derevyanski', callback_data= 'kartoshka')
        ],
         [
            InlineKeyboardButton(text = "Gurunch kichik", callback_data= 'rice-mi'),
            InlineKeyboardButton(text= 'Gurunch katta', callback_data= 'rice-bi')
        ],
        [
            InlineKeyboardButton(text= 'Ortga', callback_data= 'back40')
        ]
    ]
)

free = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back41')
        ]
    ]
)

potato = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back42')
        ]
    ]
)


mini_rice = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back43')
        ]
    ]
)

big_rice = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back44')
        ]
    ]
)


###############    Drinks




drinks = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = "Choy va kofe", callback_data= 'choy-kofe'),
            InlineKeyboardButton(text= 'Yaxna ichimliklar', callback_data= 'ice')
        ],
        [
            InlineKeyboardButton(text= 'Fresh va tabiiy soklar', callback_data= 'sok')
        ],
        [
            InlineKeyboardButton(text= 'Ortga', callback_data= 'back45')
        ]
    ]
)

choy_kofe = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= 'Choylar', callback_data='tea'),
            InlineKeyboardButton(text= 'Kofelar', callback_data='coffee')
        ],
        
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back46')
        ]
    ]
)


choylar = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= "Ko'k choy", callback_data='blue-tea'),
            InlineKeyboardButton(text= 'Qora choy', callback_data='black-tea'),
            InlineKeyboardButton(text= 'Limon choy', callback_data='limon-tea')
        ],
        
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back47')
        ]
    ]
)



kok_choy = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back48')
        ]
    ]
)




qora_choy = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back49')
        ]
    ]
)

limon_choy = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back50')
        ]
    ]
)







kofelar = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= "Americano", callback_data='america'),
            InlineKeyboardButton(text= 'Capuccino', callback_data='capuc')
            
        ],
        [
            InlineKeyboardButton(text= 'Cofe 3v1', callback_data='cofe3'),
            InlineKeyboardButton(text= 'Latte', callback_data='latte')
        ],
        
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back51')
        ]
    ]
)



americano = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back52')
        ]
    ]
)



capuccino = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back53')
        ]
    ]
)

cofe3v1 = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back54')
        ]
    ]
)




latte = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back55')
        ]
    ]
)






yahna = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= "Fanta", callback_data='fanta'),
            InlineKeyboardButton(text= 'Sprite', callback_data='sprite')
            
        ],
        [
            InlineKeyboardButton(text= 'Coca Cola', callback_data='cola'),
            InlineKeyboardButton(text= 'Nestle', callback_data='nestle')
        ],
        
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back56')
        ]
    ]
)



fanta = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back57')
        ]
    ]
)



sprite = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back58')
        ]
    ]
)

cola = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back59')
        ]
    ]
)




nestle = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back60')
        ]
    ]
)






soklar = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= "Blis 1 l", callback_data='blis'),
            InlineKeyboardButton(text= 'Olma va Sabzi fresh', callback_data='fresh')
            
        ],
        
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back61')
        ]
    ]
)



blis = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back62')
        ]
    ]
)



fresh = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back63')
        ]
    ]
)



desertlar = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= "Assalim", callback_data='asal'),
            InlineKeyboardButton(text= 'Qulupnay', callback_data='qulubnay')
            
        ],
        [
            InlineKeyboardButton(text= 'Choko', callback_data='choko')
        ],
        
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back64')
        ]
    ]
)



asal = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back65')
        ]
    ]
)



qulupnay = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back66')
        ]
    ]
)



choko = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back67')
        ]
    ]
)
pizza = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= "Ananaslik", callback_data='ananas'),
            InlineKeyboardButton(text= 'Peperoni', callback_data='peperoni')
            
        ],
        [
            InlineKeyboardButton(text= 'Margaritta', callback_data='margaritta')
        ],
        
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back68')
        ]
    ]
)



ananas = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back69')
        ]
    ]
)



peperoni = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back70')
        ]
    ]
)



margaritta = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text= '1', callback_data='1'),
            InlineKeyboardButton(text= '2', callback_data='2'),
            InlineKeyboardButton(text= '3', callback_data='4')
        ],
        [
            InlineKeyboardButton(text= '4', callback_data='4'),
            InlineKeyboardButton(text= '5', callback_data='5'),
            InlineKeyboardButton(text= '6', callback_data='6')
        ],
        [
            InlineKeyboardButton(text= '7', callback_data='7'),
            InlineKeyboardButton(text= '8', callback_data='8'),
            InlineKeyboardButton(text= '9', callback_data='9')
        ],
        [
            InlineKeyboardButton(text = 'Ortga', callback_data='back71')
        ]
    ]
)
