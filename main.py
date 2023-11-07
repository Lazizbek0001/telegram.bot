import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from buttons import *



bot =Bot(token=API_TOKEN)
dp=Dispatcher(bot)


logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.answer("Hush kelibsiz", reply_markup=til)

    
@dp.message_handler(text= "O'zbekcha")
async def exo(message: types.Message):
    await message.answer("Marhamat", reply_markup = lang)
    
    

text1 = "Marhamat menu tanlang..."
text2 = "✅Marxamat lavashlar menusi!!!"
text3 = "Kategoriyalardan birini tanlang!!!"

text4 = "Marhamat hot doglar menusi!!!"

text5 = "Marhamat sandwichlar menusi!!!"
text6 = "Marhamat shaurmalar menusi!!!"
@dp.message_handler(text= 'Buyurtma berish')
async def exo(message: types.Message):
    await message.answer(text1, reply_markup = in_key)




#####   GAMBURGER

@dp.callback_query_handler(text = 'Burger')
async def exo(call : types.CallbackQuery):
    await call.message.answer("✅Marxamat Burgerlar menusi!!!", reply_markup = Burger)
    
@dp.callback_query_handler(text = 'back34')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = in_key)
    
    
@dp.callback_query_handler(text = 'ham-bur')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 22 000 ming so'm 
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/gamburger", "rb"),caption=text, reply_markup = Gambur)
    
@dp.callback_query_handler(text = 'back35')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = Burger)

@dp.callback_query_handler(text = 'cheese')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 20 000 ming so'm 
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/chizburger", "rb"),caption=text, reply_markup = Cheese_bur)
    
@dp.callback_query_handler(text = 'back36')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = Burger)


########     DONAR


@dp.callback_query_handler(text = 'Donar')
async def exo(call : types.CallbackQuery):
    await call.message.answer("✅Marxamat Donarlar menusi!!!", reply_markup = Donars)
    
@dp.callback_query_handler(text = 'back37')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = in_key)
    
    
@dp.callback_query_handler(text = 'beef-donar')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 23 000 ming so'm 
Tarkib: Kulcha, mol go'sht, pomidor, sous,  piyoz.    
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/donar1.jpg", "rb"),caption=text, reply_markup = donar_beef)
    
@dp.callback_query_handler(text = 'back38')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = Donars)

@dp.callback_query_handler(text = 'cheese')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 23 000 ming so'm 
Tarkib: Kulcha, tovuq go'sht, pomidor, sous, piyoz.     
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/donar2.jpg", "rb"),caption=text, reply_markup = donar_chick)
    
@dp.callback_query_handler(text = 'back39')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = Donars)



###########3         GAZAKLAR



@dp.callback_query_handler(text = 'gazak')
async def exo(call : types.CallbackQuery):
    await call.message.answer("✅Marxamat gazaklar menusi!!!", reply_markup = gazaklar)
    
@dp.callback_query_handler(text = 'back40')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = in_key)
    
    
@dp.callback_query_handler(text = 'free')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 6 000 ming so'm 
Tarkib: kartoshka, sous....   
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/free.jpg", "rb"), caption=text, reply_markup = free)
    
@dp.callback_query_handler(text = 'back41')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = gazaklar)

@dp.callback_query_handler(text = 'kartoshka')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 10 000 ming so'm
Tarkib: kartoshka, sous...      
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/kartoshka.jpg", "rb"), caption= text, reply_markup = potato)
    
@dp.callback_query_handler(text = 'back42')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = gazaklar)


@dp.callback_query_handler(text = 'rici-mi')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 10 000 ming so'm
Tarkib: gurunch, salat bargi, sous...     
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/gurunch1.jpg", "rb"), caption = text, reply_markup = mini_rice)
    
@dp.callback_query_handler(text = 'back43')
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text1, reply_markup = gazaklar)

@dp.callback_query_handler(text = 'rice-bi')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 8 000 ming so'm
Tarkib: gurunch, salat bargi, sous...     
Miqdorini tanlang..."""
    await call.message.answer_photo(photo= open("Images/gurunch1.jpg", "rb"), caption = text, reply_markup = big_rice)
    
@dp.callback_query_handler(text = 'back44')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = gazaklar)




################            DRinks



@dp.callback_query_handler(text = 'drinks')
async def exo(call : types.CallbackQuery):
    await call.message.answer("Marhamat ichimliklar", reply_markup = drinks)
    
@dp.callback_query_handler(text = 'back45')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = in_key)


@dp.callback_query_handler(text = 'choy-kofe')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = choy_kofe)
    
@dp.callback_query_handler(text = 'back46')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = drinks)


@dp.callback_query_handler(text = 'tea')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = choylar)
    
@dp.callback_query_handler(text = 'back47')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = choy_kofe)
    
    

@dp.callback_query_handler(text = 'blue-tea')
async def exo(call : types.CallbackQuery):
    text = """✅Ko'k choy 
Narxi: 3 000 so'm!"""
    await call.message.answer_photo(photo=open("Images/blue-tea.jpg", "rb"), caption = text, reply_markup = kok_choy)
    
@dp.callback_query_handler(text = 'back48')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = choylar)


@dp.callback_query_handler(text = 'black-tea')
async def exo(call : types.CallbackQuery):
    text = """✅Qora choy 
Narxi: 3 000 so'm!"""
    await call.message.answer_photo(photo=open("Images/blue-tea.jpg", "rb"), caption=text, reply_markup = qora_choy)
    
@dp.callback_query_handler(text = 'back49')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = choylar)


@dp.callback_query_handler(text = 'limon-tea')
async def exo(call : types.CallbackQuery):
    text = """✅Limon choy 
Narxi: 5 000 so'm!"""
    await call.message.answer_photo(photo=open("Images/limon-tea.jpg", "rb"), caption=text, reply_markup = limon_choy)
    
@dp.callback_query_handler(text = 'back50')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = choylar)






@dp.callback_query_handler(text = 'coffee')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = kofelar)
    
@dp.callback_query_handler(text = 'back51')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = choy_kofe)


@dp.callback_query_handler(text = 'america')
async def exo(call : types.CallbackQuery):
    text = """✅Americano 
Narxi: 12 000 so'm!"""
    await call.message.answer_photo(photo=open("Images/americano.jpg", "rb"), caption=text, reply_markup = americano)
    
@dp.callback_query_handler(text = 'back52')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = kofelar)
    
    

@dp.callback_query_handler(text = 'capuc')
async def exo(call : types.CallbackQuery):
    text = """✅Cappuccino 
Narxi: 18 000 so'm!"""
    await call.message.answer_photo(photo=open("cappucino.jpg", "rb"), caption=text, reply_markup = capuccino)
    
@dp.callback_query_handler(text = 'back53')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = kofelar)


@dp.callback_query_handler(text = 'cofe3')
async def exo(call : types.CallbackQuery):
    text = """✅Cofe 3v1 
Narxi: 3 000 so'm!"""
    await call.message.answer_photo(photo=open("Images/cofe.jpg", "rb"), caption=text, reply_markup = cofe3v1)
    
@dp.callback_query_handler(text = 'back54')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = kofelar)


@dp.callback_query_handler(text = 'latte')
async def exo(call : types.CallbackQuery):
    text = """✅Latte big 120g☕️
Narxi: 15 000 so'm!"""
    await call.message.answer_photo(photo=open("Images/latte.jpg"), caption=text, reply_markup = latte)
    
@dp.callback_query_handler(text = 'back55')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = kofelar)







@dp.callback_query_handler(text = 'ice')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = yahna)
    
@dp.callback_query_handler(text = 'back56')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = drinks)


@dp.callback_query_handler(text = 'fanta')
async def exo(call : types.CallbackQuery):
    text = """✅Fanta
Narxi: 11 000 so'm!"""
    await call.message.answer_photo(photo=open("Images/fanta.jpg", "rb"), caption=text, reply_markup = fanta)
    
@dp.callback_query_handler(text = 'back57')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = yahna)
    
    

@dp.callback_query_handler(text = 'sprite')
async def exo(call : types.CallbackQuery):
    text = """✅Sprite
Narxi: 13 000 so'm!"""
    await call.message.answer_photo(photo=open("Images/sprite.jpg","rb"),caption=text, reply_markup = sprite)
    
@dp.callback_query_handler(text = 'back58')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = yahna)


@dp.callback_query_handler(text = 'cola')
async def exo(call : types.CallbackQuery):
    text = """✅Coca Cola
Narxi: 12 000 so'm!"""
    await call.message.answer_photo(photo=("Images/cola.jpg", "rb"), caption=text, reply_markup = cola)
    
@dp.callback_query_handler(text = 'back59')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = yahna)


@dp.callback_query_handler(text = 'nestle')
async def exo(call : types.CallbackQuery):
    text = """✅Nestle
Narxi: 4 000 so'm!"""
    await call.message.answer_photo(photo=open("Images/nestale.jpg", "rb"),caption=text, reply_markup = nestle)
    
@dp.callback_query_handler(text = 'back60')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = yahna)






@dp.callback_query_handler(text = 'sok')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = soklar)
    
@dp.callback_query_handler(text = 'back61')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = drinks)


@dp.callback_query_handler(text = 'blis')
async def exo(call : types.CallbackQuery):
    text = """✅Sok Bliss
Narxi: 10 000 so'm!"""
    await call.message.answer_photo(photo=open("Images/blis.jpg", "rb"), caption=text, reply_markup = blis)
    
@dp.callback_query_handler(text = 'back62')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = soklar)
    
    

@dp.callback_query_handler(text = 'fresh')
async def exo(call : types.CallbackQuery):
    text = """✅Fresh sabzi + olma
Narxi: 13 000 so'm!"""
    await call.message.answer_photo(photo=open("Images/fresh.jpg", "rb"), caption=text, reply_markup = fresh)
    
@dp.callback_query_handler(text = 'back63')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = soklar)


#####           Desertlar


@dp.callback_query_handler(text = 'Desert')
async def exo(call : types.CallbackQuery):
    await call.message.answer_photo(photo= open("Images/desert_menu.jpg", "rb"), caption="Marhamat desertlar menusi", reply_markup = desertlar)
    
@dp.callback_query_handler(text = 'back64')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = in_key)



@dp.callback_query_handler(text = 'asal')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 14 000 so'm 
Аnʼnaviy taʼm - asal asosidagi biskvit va krem
Miqdorini tanlang"""
    await call.message.answer_photo(photo=open("Images/asal.jpg", "rb"), caption = text, reply_markup = asal)
    
@dp.callback_query_handler(text = 'back65')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = desertlar)
    
    

@dp.callback_query_handler(text = 'qulubnay')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 15 000 so'm 
Qulupnayli Muss.
Miqdorini tanlang!"""
    await call.message.answer_photo(photo=open("Images/qulup.jpg", "rb"), caption=text, reply_markup = qulupnay)
    
@dp.callback_query_handler(text = 'back66')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = desertlar)

@dp.callback_query_handler(text = 'choko')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 17 000 ming so'm 
Аnʼnaviy taʼm - shokolat asosidagi biskvit va krem.
Miqdorini tanlangg"""
    await call.message.answer_photo(photo=open("Images/choko.jpg", "rb"), caption=text, reply_markup = choko)
    
@dp.callback_query_handler(text = 'back67')
async def exo(call : types.CallbackQuery):
    await call.message.answer_photo(photo=open("Images/desert_mneu.jpg", "rb"), caption="""Marhamat desertlar menusi""", reply_markup = desertlar)


###############       Pizzas



@dp.callback_query_handler(text = 'pizza')
async def exo(call : types.CallbackQuery):
    await call.message.answer("Marhamat pizza menusi", reply_markup = pizza)
    
@dp.callback_query_handler(text = 'back68')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = in_key)



@dp.callback_query_handler(text = 'ananas')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 65 000 so'm 
Пицца с Ананасом.
Пицца с Колбасой     33см.
Соус Томатный Для Пиццы
3 вида колбас 130гр.
Тонкое тесто
Кукуруза
Сыр 100гр.
ГрибыMiqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/pizza1.jpg", "rb"), caption = text, reply_markup = ananas)
    
@dp.callback_query_handler(text = 'back69')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = pizza)
    
    

@dp.callback_query_handler(text = 'peperoni')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 75 000 ming so'm 
Пицца Пепперони
Пицца Пепперони     33см.
Соус Томатный Для Пиццы
Тонкое тесто.
Сыр 110 гр.
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/pizza2.jpg", "rb"), caption=text, reply_markup = peperoni)
    
@dp.callback_query_handler(text = 'back70')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = pizza)

@dp.callback_query_handler(text = 'margaritta')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 60 000 ming so'm 
Пицца Маргарита
Пицца Маргарита  33см.
Соус Томатный Для Пиццы 
Тонкое тесто 
Сыр 100гр.
Помидоры
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/pizza3.jpg", "rb"), caption=text, reply_markup = margaritta)
    
@dp.callback_query_handler(text = 'back71')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = pizza)




















@dp.callback_query_handler(text = 'lavash')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text2, reply_markup = lavash_menu)
    
@dp.callback_query_handler(text = 'Back')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = in_key)





@dp.callback_query_handler(text = "Shaurma")
async def exo(call : types.CallbackQuery):
    await call.message.answer_photo(photo=open("Images/shaurma_menu.jpg", "rb"),caption=text6, reply_markup=shaurma_menu)

@dp.callback_query_handler(text = "back7")
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup=in_key)
    
    
    

@dp.callback_query_handler(text = 'Sandwich')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text2, reply_markup = sand_menu)
    
    
@dp.callback_query_handler(text = 'club')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 22 000 ming so'm 
Tarkibi: Kulcha, tovuq go'shti, pomidor, sous,  piyoz.
Miqdorini tanlang..."""
    await call.message.answer_photo(photo= open("Images/sandwich1.jpg", "rb"),caption=text, reply_markup = chick_sand)
    
    
  
@dp.callback_query_handler(text = 'clas sand')
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 24 000 ming so'm 
Tarkibi: Kulcha, tovuq go'shti, pomidor, sous,  piyoz.
Miqdorini tanlang.."""
    await call.message.answer_photo(photo=open("Images/sandwich1.jpg", "rb"),caption=text, reply_markup = classic_sand)
      

@dp.callback_query_handler(text = 'back31')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text5, reply_markup = sand_menu)
 
 

@dp.callback_query_handler(text = 'back30')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text5, reply_markup = sand_menu)


@dp.callback_query_handler(text = 'back32')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text1, reply_markup = in_key)
    
    

    
    
    
    
####     Beef  Shaurma

@dp.callback_query_handler(text = "besh")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text3, reply_markup=Beef_shaurma)
    
    
@dp.callback_query_handler(text = "mini5")
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 18 000 ming so'm
Kulcha, mol go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/shaurma1.jpg", "rb"),caption=text, reply_markup=mini_beef_shaurma)
    
    
@dp.callback_query_handler(text = "classic5")
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 22 000 ming so'm
Kulcha, mol go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/shaurma1.jpg", "rb"),caption=text, reply_markup=classic_beef_shaurma)
    

@dp.callback_query_handler(text = "back3")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text3, reply_markup=Beef_shaurma) 
    
@dp.callback_query_handler(text = "back4")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text3, reply_markup=Beef_shaurma)
    
@dp.callback_query_handler(text = "back1")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text6, reply_markup=shaurma_menu)
    


###    Chicken Shaurma
    
@dp.callback_query_handler(text = "chicksh")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text3, reply_markup=shaurma_chick)
    
    

@dp.callback_query_handler(text = "mini8")
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 17 000 ming so'm
Kulcha, tovuq go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/shaurma2.jpg", "rb"),caption=text, reply_markup=mini_chick_shaurma)

@dp.callback_query_handler(text = "classic8")
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 20 000 ming so'm
Kulcha, tovuq go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/shaurma2.jpg", "rb"),caption=text, reply_markup=classic_chick_shaurma)
    

@dp.callback_query_handler(text = "back19")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text6, reply_markup=shaurma_menu)

@dp.callback_query_handler(text = "back5")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text3, reply_markup=shaurma_chick)

@dp.callback_query_handler(text = "back6")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text3, reply_markup=shaurma_chick)



###      beef pep shaurma

@dp.callback_query_handler(text = "bef-pep")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text3, reply_markup=shaurma_beef_pep)
    
    
    

@dp.callback_query_handler(text = "mini9")
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 23 000 ming so'm
Kulcha, mol go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/shaurma3.jpg", "rb"),caption=text, reply_markup=mini_beef_pep_shaurma)

@dp.callback_query_handler(text = "classic9")
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 25 000 ming so'm
Kulcha, mol go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/shaurma3.jpg", "rb"),caption=text, reply_markup=classic_beef_pep_shaurma)
    

@dp.callback_query_handler(text = "back20")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text6, reply_markup=shaurma_menu)

@dp.callback_query_handler(text = "back21")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text3, reply_markup=shaurma_beef_pep)

@dp.callback_query_handler(text = "back22")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text3, reply_markup=shaurma_beef_pep)



@dp.callback_query_handler(text = "mix")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text3, reply_markup=shaurma_mix)
    

@dp.callback_query_handler(text = "mini10")
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 20 000 ming so'm
Kulcha, tovuq go'sht, garimdori, pomidor, sous,  piyoz. 
Miqdorini tanlang."""
    await call.message.answer_photo(photo=open("Images/shaurma4.jpg", "rb"),caption=text, reply_markup=mini_mix_shaurma)

@dp.callback_query_handler(text = "classic10")
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 24 000 ming so'm
Kulcha, tovuq go'sht,garimdori, pomidor, sous,  piyoz. 
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/shaurma4.jpg", "rb"), caption=text, reply_markup=classic_mix_shaurma)
    

@dp.callback_query_handler(text = "back23")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text6, reply_markup=shaurma_menu)

@dp.callback_query_handler(text = "back24")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text3, reply_markup=shaurma_mix)

@dp.callback_query_handler(text = "back25")
async def exo(call : types.CallbackQuery):
    
    await call.message.answer(text3, reply_markup=shaurma_mix)

    
    

@dp.callback_query_handler(text = 'Hot-dog')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text4, reply_markup = hot_dog_menu)
    

@dp.callback_query_handler(text = "chick-hot")
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 17 000 ming so'm 
Tarkibi: Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/hotdog4.jpg","rb"),caption=text, reply_markup = chick_hor_dog)
    
    
@dp.callback_query_handler(text = "clas hot")
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 8 000 ming so'm 
Tarkibi: Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang.."""
    await call.message.answer_photo(photo=open("Images/hotdog2.jpg", "rb"),caption=text, reply_markup = classic_hot_dog)
    


@dp.callback_query_handler(text = "dabl")
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 18 000 ming so'm 
Tarkibi: Kulcha,sosiska 2x,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/hotdog1.jpg", "rb"),caption=text, reply_markup = dabl_dog)
    
    
    
@dp.callback_query_handler(text = "korol")
async def exo(call : types.CallbackQuery):
    text = """✅Narxi: 15 000 ming so'm 
Tarkibi Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/hotdog3.jpg"),caption=text, reply_markup = Karol)
    
    
@dp.callback_query_handler(text = 'back26')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text4, reply_markup=hot_dog_menu)

@dp.callback_query_handler(text = 'back27')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text4, reply_markup=hot_dog_menu)
    
@dp.callback_query_handler(text = 'back28')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text4, reply_markup=hot_dog_menu)
    
@dp.callback_query_handler(text = 'back29')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text4, reply_markup=hot_dog_menu)
    
@dp.callback_query_handler(text = 'back33')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text4, reply_markup=in_key)
    
    

##### Chicken lavash

@dp.callback_query_handler(text = 'chick-lavash')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup=lavash_chick)


@dp.callback_query_handler(text = 'classic7')
async def exo(call: types.CallbackQuery):
    text = """✅Narxi: 22 000 ming so'm 
Tarkibi: Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/lavash3.jpg", "rb"),caption=text, reply_markup = classic_lavash_chick)
    

@dp.callback_query_handler(text = 'mini7')
async def exo(call: types.CallbackQuery):
    text = """✅Narxi: 19 000 ming so'm 
Tarkibi: Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/lavash3.jpg", "rb"),caption=text, reply_markup = mini_lavash_chick) 
    

@dp.callback_query_handler(text = 'back15')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup=lavash_menu)
    

@dp.callback_query_handler(text = 'back8')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup=lavash_chick)
    

@dp.callback_query_handler(text = 'back9')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup=lavash_chick)







###      pep Chick lavash

@dp.callback_query_handler(text='pep-chick')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup=pep_lavash_chick)
    


@dp.callback_query_handler(text = 'classic6')
async def exo(call: types.CallbackQuery):
    text = """✅Narxi: 20 000 ming so'm 
Tarkibi:Xamir,garimdori tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/lavash4.jpg", 'rb'),caption =text, reply_markup = classic_lavash_chick_pep)
    

@dp.callback_query_handler(text = 'mini6')
async def exo(call: types.CallbackQuery):
    text = """✅Narxi: 17 000 ming so'm 
Tarkibi: Xamir,garimdori,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/lavash4.jpg", 'rb'),caption=text, reply_markup = mini_lavash_chick_pep)   



@dp.callback_query_handler(text = 'back17')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = pep_lavash_chick)
    

@dp.callback_query_handler(text = 'back18')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = pep_lavash_chick)
    

@dp.callback_query_handler(text = 'back16')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text2, reply_markup = lavash_menu)






### pep - Lavash

@dp.callback_query_handler(text = 'pepper-lavash')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup=pep_lavash)
    

@dp.callback_query_handler(text = 'classic1')
async def exo(call: types.CallbackQuery):
    text = """Narxi: 20 000 ming so'm 
Tarkibi: Xamir,garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open("Images/lavash2.jpg"),caption=text, reply_markup = classic_lavash_pep)
    

@dp.callback_query_handler(text = 'back10')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = pep_lavash)


@dp.callback_query_handler(text = 'back11')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = pep_lavash)


@dp.callback_query_handler(text = 'back12')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text2, reply_markup = lavash_menu)    


@dp.callback_query_handler(text = 'mini1')
async def exo(call:types.CallbackQuery):
    text = """✅Narxi: 18 000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open('Images/lavash2.jpg','rb'),caption=text, reply_markup=mini_lavash_pep)
    






#####                   Beef Lavash
    
@dp.callback_query_handler(text = 'Beef-lavash')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup=beef_lavash)
    


@dp.callback_query_handler(text = 'back13')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text2, reply_markup = lavash_menu)    


@dp.callback_query_handler(text = 'classic3')
async def exo(call:types.CallbackQuery):
    text = """Narxi: 20 000 ming so'm 
Tarkibi: Xamir,garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang..."""
    await call.message.answer_photo(photo=open('Images/lavash1.jpg','rb'),caption=text, reply_markup=classic_lavash_beef)



@dp.callback_query_handler(text = 'back14')
async def exo(call : types.CallbackQuery):
    await call.message.answer("Kategoriyalardan birini tanlang!!!", reply_markup = beef_lavash)


    
    
@dp.callback_query_handler(text = 'mini3')
async def exo(call:types.CallbackQuery):
    text = """✅Narxi: 18 000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang..."""
    await call.message.answer_photo(photo= open('Images/lavash1.jpg','rb'),caption=text, reply_markup=mini_lavash_beef)
    
    
    
    
@dp.callback_query_handler(text = 'back2')
async def exo(call : types.CallbackQuery):
    await call.message.answer(text3, reply_markup = beef_lavash)

















if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)