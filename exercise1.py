#this is my story
mystory="""my favorite animal is a {animal y} and loves to eat a lot of {food y}.I have to import food from {city y}""
def tellstory:
myfavs=dict()
addfav('animal',myfavs)
addfav('food',myfavs)
addfav('city',myfavs)
mystory=format(**myfavs) 
print(story) 
def addfav(mat,myfavs):
'''this alloows the user input'''
prompt='Enter name of' + kavar
response=input(promt).strip() 
myfavs[mat]=response
tellstory()
input('press Enter to exit')