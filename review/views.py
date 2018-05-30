from django.shortcuts import render,redirect
# Create your views here.
def reviewindex(request):
    return render(request,'review/ReviewHome.html',locals())
def reviewcomment(request):
    if request.method== 'POST':

        t = request.POST['score']
        print(t)
        return redirect("/")
    return render(request,'review/ReviewComment.html',locals())
