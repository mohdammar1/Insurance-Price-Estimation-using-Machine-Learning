from django.shortcuts import render
import joblib
def ML(arr):
    x=joblib.load("web\MYAI")
    y=x.predict([arr])
    final=abs(y.round(2))
    return final
def home(request):
    if request.method== 'POST':
       age=request.POST.get('age')
       gender=request.POST.get('gender')
       bmi=request.POST.get('bmi')
       kid=request.POST.get('kids')
       smoke=request.POST.get('smoke')
       li= list(map(float,[age,gender,bmi,kid,smoke]))
       new=ML(li)
       return render(request,"home.html",{"lis":new})
    else:
        new=[0]
        return render(request,"home.html",{"lis":new})
    

    