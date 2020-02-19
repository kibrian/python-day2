#this is my story
mystory="""my favorite animal is a {animal y} and loves to eat a lot of {food y}.I have to import food from {city y}"""
def tellstory():
    myfavs =dict()
     addfav('animal','myfavs')
      addfav('food,'myfavs')
       addfav('city','myfavs')
         mystory=format(**myfavs) 
          print('tellstory')

tellstory()


def addfav('mat','myfavs'):
     addfav='''this alloows the user input'''
       prompt=Enter name of + kavar
         response=input(promt).strip() 
          myfavs[mat]=response
            input('press Enter to exit')
tellstory()

