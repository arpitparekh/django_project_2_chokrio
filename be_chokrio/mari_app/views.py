from django.shortcuts import render

# Create your views here.

def showIntro(request):
  data = {
    'title': 'Welcome to my class',
    'content': 'Hello Students! Welcome to my class. I hope you are enjoying your time here.',
    'author': 'Arpit',
    'fruits': ['apple', 'banana', 'cherry', 'dates', 'elderberry','kiwi','mango','orange','pear','pineapple','strawberry','watermelon','grapefruit'],
    'user':{
      'name':'Atul',
      'age': 47,
      'photo':"https://cdn.create.vista.com/api/media/small/250363326/stock-photo-smiling-attractive-woman-white-sweater-looking-camera-isolated-pink",
      'address':{
          'city':'Pune',
          'state':'Maharashtra',
          'country':'India'
        },
      'contact':{
          'phone':'9876543210',
          'email':'atul@gmail.com'
        }
    }
  }
  return render(request, 'intro.html',data)
