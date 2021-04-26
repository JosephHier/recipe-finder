from collections import defaultdict
import sqlite3

data = [
      {
            "apple": 1,
            "lemon": 0.1,
            "yt_link": "https://www.youtube.com/watch?v=UnWoAKkDAec",
            "title": "Waldorf Salad",
            "type": "salad",
            "filename": "UnWoAKkDAec"
      },
      {
            "apple": 1,
            "lemon": 0.1,
            "yt_link": "https://www.youtube.com/watch?v=VFQsDAADPLM",
            "title": "Apple Pie",
            "type": "dessert",
            "filename": "VFQsDAADPLM"
      },
      {
            "apple": 1,
            "yt_link": "https://www.youtube.com/watch?v=Ma68BY1a4gg",
            "title": "Cinnamon Apples",
            "type": "dessert",
            "filename": "Ma68BY1a4gg"
      },
      {
            "apple": 1,
            "yt_link": "https://www.youtube.com/watch?v=5xy42zMdpsA",
            "title": "Apple Fritters",
            "type": "dessert",
            "filename": "5xy42zMdpsA"
      },
      {
            "apple": 1,
            "yt_link": "https://www.youtube.com/watch?v=2jnYrZJiam8",
            "title": "Apple Cinnamon Waffles",
            "type": "main",
            "filename": "2jnYrZJiam8"
      },
      {
            "orange": 1,
            "onion": 0.7,
            "yt_link": "https://www.youtube.com/watch?v=kbo-J5vyk8A",
            "title": "Orange Salad",
            "type": "salad",
            "filename": "kbo-J5vyk8A"
      },
      {
            "orange": 1,
            "yt_link": "https://www.youtube.com/watch?v=SJ9ZwFZAwJo",
            "title": "Orange Cake",
            "type": "dessert",
            "filename": "SJ9ZwFZAwJo"
      },
      {
            "orange": 1,
            "yt_link": "https://www.youtube.com/watch?v=voFLQ-mHis0",
            "title": "Orange Chicken",
            "type": "main",
            "filename": "voFLQ-mHis0"
      },
      {
            "orange": 1,
            "yt_link": "https://www.youtube.com/watch?v=sygTw5Sp3Z0",
            "title": "Orange Salmon",
            "type": "main",
            "filename": "sygTw5Sp3Z0"
      },
      {
            "orange": 1,
            "yt_link": "https://www.youtube.com/watch?v=gMt0W3iMqlE",
            "title": "Jelly Squares",
            "type": "dessert",
            "filename": "gMt0W3iMqlE"
      },
      {
            "lemon": 1,
            "yt_link": "https://www.youtube.com/watch?v=ruJJ6nkH6_8",
            "title": "Lemon Poppy-Seed Muffin",
            "type": "dessert",
            "filename": "ruJJ6nkH6_8"
      },
      {
            "lemon": 1,
            "yt_link": "https://www.youtube.com/watch?v=OWO85wlVsjI",
            "title": "Lemon Meringue Pie",
            "type": "dessert",
            "filename": "OWO85wlVsjI"
      },
      {
            "lemon": 1,
            "yt_link": "https://www.youtube.com/watch?v=iK7wG3HIcww",
            "title": "Lemon Chicken",
            "type": "main",
            "filename": "iK7wG3HIcww"
      },
      {
            "lemon": 1,
            "yt_link": "https://www.youtube.com/watch?v=-x2E7T3-r7k",
            "title": "Salmon with Lemon Butter",
            "type": "main",
            "filename": "-x2E7T3-r7k"
      },
      {
            "lemon": 1,
            "yt_link": "https://www.youtube.com/watch?v=b-KU6Koo2xc",
            "title": "Lemon Bars",
            "type": "dessert",
            "filename": "b-KU6Koo2xc"
      },
      {
            "mango": 1,
            "yt_link": "https://www.youtube.com/watch?v=c1uxgJwTREA",
            "title": "Spicy Mango Salad",
            "type": "salad",
            "filename": "c1uxgJwTREA"
      },
      {
            "mango": 1,
            "yt_link": "https://www.youtube.com/watch?v=GTlVDpfKtwE",
            "title": "Mango Shaved Ice",
            "type": "dessert",
            "filename": "GTlVDpfKtwE"
      },
      {
            "mango": 1,
            "yt_link": "https://www.youtube.com/watch?v=SjyiHodj0nM",
            "title": "Mango Mousse",
            "type": "dessert",
            "filename": "SjyiHodj0nM"
      },
      {
            "mango": 1,
            "yt_link": "https://www.youtube.com/watch?v=WoAvXV4lPZ0",
            "title": "Mango Lassi",
            "type": "side",
            "filename": "WoAvXV4lPZ0"
      },
      {
            "mango": 1,
            "yt_link": "https://www.youtube.com/watch?v=G_e8hAu2zPg",
            "title": "Mango Chutney",
            "type": "side",
            "filename": "G_e8hAu2zPg"
      },
      {
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=1qRir364aNk",
            "title": "French Onion Soup",
            "type": "soup",
            "filename": ""
      },
      {
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=dcB5VU93AII",
            "title": "Homemade Onion Rings",
            "type": "side",
            "filename": "dcB5VU93AII"
      },
      {
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=KSIx632mjoU",
            "title": "Onion Dip",
            "type": "side",
            "filename": "KSIx632mjoU"
      },
      {
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=k07vro65OWY",
            "title": "Street Style Samosa",
            "type": "main",
            "filename": "k07vro65OWY"
      },
      {
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=eOgfwLS8EyM",
            "title": "Pollo Encebollado",
            "type": "main",
            "filename": "eOgfwLS8EyM"
      },
      {
            "tomato": 1,
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=RQlp-p_Qcsw",
            "title": "Ratatouille",
            "type": "main",
            "filename": "RQlp-p_Qcsw"
      },
      {
            "tomato": 1,
            "yt_link": "https://www.youtube.com/watch?v=NGFJxkFRcr0",
            "title": "Tomato Soup",
            "type": "soup",
            "filename": "NGFJxkFRcr0"
      },
      {
            "tomato": 1,
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=v2WqcHH65NQ",
            "title": "Spaghetti Bolognese",
            "type": "main",
            "filename": "v2WqcHH65NQ"
      },
      {
            "tomato": 1,
            "yt_link": "https://www.youtube.com/watch?v=gOcfUgd4ekA",
            "title": "Caprese salad",
            "type": "salad",
            "filename": "gOcfUgd4ekA"
      },
      {
            "tomato": 1,
            "yt_link": "https://www.youtube.com/watch?v=vO_0joLyBOY",
            "title": "Gazpacho",
            "type": "soup",
            "filename": "vO_0joLyBOY"
      }
]

data2 = [
      {
            "apple": 1,
            "yt_link": "https://www.youtube.com/watch?v=sYXJCcvqUVM",
            "title": "Apple Chicken Sausage",
            "type": "main"
      },
      {
            "apple": 1,
            "lemon": 0.1,
            "yt_link": "https://www.youtube.com/watch?v=wnuTYSVG_bw",
            "title": "Apple Crumble",
            "type": "dessert"
      },
      {
            "apple": 1,
            "yt_link": "https://www.youtube.com/watch?v=RT7P0eDhSiM",
            "title": "Apple Cheddar Bacon Sandwich",
            "type": "main"
      },
      {
            "apple": 1,
            "yt_link": "https://youtu.be/CHG0Ie_EXuE",
            "title": "Apple French Toast Roll Ups",
            "type": "main",
            "filename": "CHG0Ie_EXuE"
      },
      {
            "apple": 1,
            "yt_link": "https://www.youtube.com/watch?v=4W58HFh-QXA",
            "title": "Apple Crisp Pancakes",
            "type": "main"
      },
      {
            "apple": 1,
            "yt_link": "https://www.youtube.com/watch?v=i6fw43n_b9I",
            "title": "Apple Donuts",
            "type": "dessert"
      },
      {
            "apple": 1,
            "yt_link": "https://www.youtube.com/watch?v=XH69w6VFPYc",
            "title": "Upside Down Apple Cake",
            "type": "dessert"
      },
      {
            "apple": 1,
            "lemon": 0.1,
            "yt_link": "https://www.youtube.com/watch?v=3c1w2_MQ5D4",
            "title": "Caramel Apple Cheesecake Bars",
            "type": "dessert"
      },
      {
            "apple": 1,
            "yt_link": "https://www.youtube.com/watch?v=-yjrcskGPjs",
            "title": "Pumpkin Apple Smoothie",
            "type": "side"
      },
      {
            "apple": 1,
            "orange": 0.5,
            "yt_link": "https://www.youtube.com/watch?v=scZMJw5GRok",
            "title": "Apple Cider",
            "type": "side"
      },
      {
            "lemon": 0.8,
            "yt_link": "https://www.youtube.com/watch?v=K67xg2TDrK8",
            "title": "Sicilian Cookies",
            "type": "dessert"
      },
      {
            "lemon": 1,
            "yt_link": "https://www.youtube.com/watch?v=YwuxuBmT1OQ",
            "title": "Lemon Cookies",
            "type": "dessert"
      },
      {
            "lemon": 1,
            "yt_link": "https://www.youtube.com/watch?v=lziMy5a16vU",
            "title": "Lemon Jam",
            "type": "side"
      },
      {
            "lemon": 1,
            "yt_link": "https://www.youtube.com/watch?v=7hLzlNzhUIE",
            "title": "Creamy Lemon Chicken",
            "type": "main"
      },
      {
            "lemon": 1,
            "yt_link": "https://www.youtube.com/watch?v=t48bqx1WRN4",
            "title": "Preserved Lemons",
            "type": "side"
      },
      {
            "lemon": 1,
            "yt_link": "https://www.youtube.com/watch?v=4drkNcIHmIs",
            "title": "Greek Lemon Potatoes",
            "type": "side"
      },
      {
            "lemon": 1,
            "yt_link": "https://www.youtube.com/watch?v=nOpQfQNE-_g",
            "title": "Baked Fish with Creamy Lemon Sauce",
            "type": "main"
      },
      {
            "lemon": 1,
            "yt_link": "https://www.youtube.com/watch?v=raYZfPep074",
            "title": "Candied Lemon Slices",
            "type": "dessert"
      },
      {
            "lemon": 1,
            "yt_link": "https://www.youtube.com/watch?v=zzLKoP1SPvU",
            "title": "Lemon Curd",
            "type": "dessert"
      },
      {
            "lemon": 1,
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=r5kJ-NcS-6A",
            "title": "Lemon-Chili Chicken",
            "type": "main"
      },
      {
            "orange": 1,
            "yt_link": "https://www.youtube.com/watch?v=IikOAHUl8J4",
            "title": "Orange Duck",
            "type": "main"
      },
      {
            "orange": 1,
            "onion": 0.5,
            "yt_link": "https://www.youtube.com/watch?v=m2NQkaBwAPg",
            "title": "Maple-Orange Glazed Turkey",
            "type": "main"
      },
      {
            "orange": 1,
            "yt_link": "https://www.youtube.com/watch?v=lOcUKk0QvT4",
            "title": "Carrot Orange Soup",
            "type": "soup"
      },
      {
            "orange": 1,
            "yt_link": "https://www.youtube.com/watch?v=jGMwEGTNVBk",
            "title": "Whole Orange Cake",
            "type": "dessert"
      },
      {
            "orange": 1,
            "yt_link": "https://www.youtube.com/watch?v=M9jEXkwUS4g",
            "title": "Candied Orange Peels",
            "type": "dessert"
      },
      {
            "orange": 1,
            "yt_link": "https://www.youtube.com/watch?v=nji6VDpv_80",
            "title": "Orange Marmalade",
            "type": "side"
      },
      {
            "orange": 1,
            "yt_link": "https://www.youtube.com/watch?v=kzbFdcaL8L0",
            "title": "Orange Vanilla Flan",
            "type": "dessert"
      },
      {
            "orange": 1,
            "yt_link": "https://www.youtube.com/watch?v=TeGD9jWCkF8",
            "title": "Orange Caramel Pudding",
            "type": "dessert"
      },
      {
            "orange": 1,
            "yt_link": "https://www.youtube.com/watch?v=GtngeZpeVyQ",
            "title": "Cranberry Sauce",
            "type": "side"
      },
      {
            "orange": 1,
            "yt_link": "https://www.youtube.com/watch?v=g9-FKIVeIDs",
            "title": "Orange Donuts",
            "type": "dessert"
      },
      {
            "mango": 1,
            "yt_link": "https://www.youtube.com/watch?v=EAK5GfW5q6w",
            "title": "Salmon with Mango Salsa",
            "type": "main"
      },
      {
            "mango": 1,
            "tomato": 0.4,
            "onion": 0.4,
            "yt_link": "https://www.youtube.com/watch?v=Otg1b7SR5x0",
            "title": "Cheeseburger with Mango Relish",
            "type": "main"
      },
      {
            "mango": 1,
            "tomato": 0.4,
            "onion": 0.4,
            "yt_link": "https://www.youtube.com/watch?v=Zsz07voYnX4",
            "title": "Mango Tartar Tilapia Burger",
            "type": "main"
      },
      {
            "mango": 1,
            "lemon": 0.1,
            "yt_link": "https://www.youtube.com/watch?v=U0jcUes66yM",
            "title": "Sweet Chili Mango Sauce",
            "type": "side"
      },
      {
            "mango": 1,
            "yt_link": "https://www.youtube.com/watch?v=osGfh5A7ta0",
            "title": "Thai Sticky Rice",
            "type": "dessert"
      },
      {
            "mango": 1,
            "yt_link": "https://www.youtube.com/watch?v=-CD3QOYul5Y",
            "title": "Raw Mango Rice",
            "type": "side"
      },
      {
            "mango": 1,
            "yt_link": "https://www.youtube.com/watch?v=_oWX0eWwxBE",
            "title": "Tempeh Mango Noodles",
            "type": "main"
      },
      {
            "mango": 1,
            "yt_link": "https://www.youtube.com/watch?v=rzlqkJf0Wus",
            "title": "Chicken Mango and Avocado Salad",
            "type": "salad"
      },
      {
            "mango": 1,
            "yt_link": "https://www.youtube.com/watch?v=JnWx0SZ7Pw0",
            "title": "Mango Cilantro Salad",
            "type": "salad"
      },
      {
            "mango": 1,
            "yt_link": "https://www.youtube.com/watch?v=UiEvNepiPlE",
            "title": "Mango Blueberry Crisp",
            "type": "dessert"
      },
      {
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=TutmnWa6dVo",
            "title": "Slow-Cooked Brisket",
            "type": "main"
      },
      {
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=-GAykN5syNY",
            "title": "One-Pot French Onion Chicken",
            "type": "main"
      },
      {
            "onion": 1,
            "lemon": 0.2,
            "yt_link": "https://www.youtube.com/watch?v=g7tvOFiJ1lI",
            "title": "Laccha Onion Salad",
            "type": "salad"
      },
      {
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=H3HofY85T2w",
            "title": "Onion Creamy Chicken",
            "type": "main"
      },
      {
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=Ninngyd1oVk",
            "title": "Leek and Onion Quiche",
            "type": "main"
      },
      {
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=ExTUH1ASOoU",
            "title": "Onion Rice",
            "type": "side"
      },
      {
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=_d4eTcy052M",
            "title": "Onion Fritters",
            "type": "side"
      },
      {
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=fkSdQovkve0",
            "title": "English Onion and Leek Soup",
            "type": "soup"
      },
      {
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=ToSmAlhNKBw",
            "title": "Italian Wedding Soup",
            "type": "soup"
      },
      {
            "onion": 1,
            "yt_link": "https://www.youtube.com/watch?v=6M4ydW1d86s",
            "title": "Caramelized Onion Bread",
            "type": "side"
      },
      {
            "tomato": 1,
            "yt_link": "https://www.youtube.com/watch?v=86NtXtC8Zbw",
            "title": "Tomato Salad",
            "type": "salad"
      },
      {
            "tomato": 1,
            "onion": 0.5,
            "yt_link": "https://www.youtube.com/watch?v=nVoOz0_zf-Q",
            "title": "Shakshuka",
            "type": "main"
      },
      {
            "tomato": 1,
            "yt_link": "https://www.youtube.com/watch?v=J5XzFtDMHj4",
            "title": "Roasted Tomato Grilled Cheese",
            "type": "main"
      },
      {
            "tomato": 1,
            "yt_link": "https://www.youtube.com/watch?v=S1ec1ESYOD4",
            "title": "Tomato Galette",
            "type": "main"
      },
      {
            "tomato": 1,
            "onion": 0.8,
            "yt_link": "https://www.youtube.com/watch?v=VCor6n3I6_U",
            "title": "Tomato Curry",
            "type": "side"
      },
      {
            "tomato": 1,
            "yt_link": "https://www.youtube.com/watch?v=3WCYisXvMHc",
            "title": "Stuffed Tomatoes",
            "type": "main"
      },
      {
            "tomato": 1,
            "yt_link": "https://www.youtube.com/watch?v=oYo8KlSQYHA",
            "title": "Buffalo Steak",
            "type": "main"
      },
      {
            "tomato": 1,
            "yt_link": "https://www.youtube.com/watch?v=p25A9KTWnzo",
            "title": "Cheddar Tomato Quiche",
            "type": "main"
      },
      {
            "tomato": 1,
            "yt_link": "https://www.youtube.com/watch?v=BM0JyCxVjwc",
            "title": "Pan-Fried Trout with Tomato-Basil Saute",
            "type": "main"
      },
      {
            "tomato": 1,
            "onion": 0.9,
            "yt_link": "https://www.youtube.com/watch?v=pPAGGxpZjxo",
            "title": "Southern Tomato Pie",
            "type": "side"
      }
]

query = """INSERT INTO videos (apple, lemon, mango, onion, orange, tomato, type, title, yt_link, filename)
            VALUES """

for vid_obj in data2:
    v = defaultdict(int, vid_obj)
    query += f'({v["apple"]}, {v["lemon"]}, {v["mango"]}, {v["onion"]}, {v["orange"]}, {v["tomato"]}, \'{v["type"]}\', \'{v["title"]}\', \'{v["yt_link"]}\', \'{v["filename"]}\'),\n'
query = query[:-2]
query += ";"
print(query)

con = sqlite3.connect('video.db')
cur = con.cursor()

cur.execute(query)

con.commit()
con.close()



