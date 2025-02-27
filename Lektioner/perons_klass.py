import person_klass
import person_klass as p #förkortar namnet till p

#Hämtas från en annan fili

person_obj1 = person_klass.Person('Lisa') # långt att skruva person_klass
print(person_obj1)

#För att inte skriva person_klass varje gång
person_obj2 = p.Person('Anna')
print(person_obj2)

#OM man har flera personer man vill ändra efternamn på så kan man
# 1. Edit > find > Replace