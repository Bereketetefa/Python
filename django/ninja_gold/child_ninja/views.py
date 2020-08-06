[from django.shortcuts import render, redirect
import 

# Create your views here.
def index(request):
    return render(request,'index.html')
    if 'totalgold' not in request.session:
        request.session ['totalgold'] = 0
    if 'activity_log' not in request.session:
        request.session ['activity_log'] = []
    return render(request, 'index.html')

def process(request):
    print(request.POST)
    if request.POST['place'] == 'Farm':
        goldearned = random.randint (10,20)
        request.session['totalgold'] += goldearned
        event = f"went to the farm and earned {goldearned}"
        request.session ['activity_log'].append(event)

        

    if request.POST['place'] == 'Cave':
    goldearned = random.randint (2,5)    
        request.session['totalgold'] += goldearned
        event = f"went to the Cave and earned {goldearned}"
        request.session ['activity_log'].append(event)


    if request.POST['place'] == 'House':
    goldearned = random.randint (5,10)    
        request.session['totalgold'] += goldearned
        event = f"went to the House and earned {goldearned}"
        request.session ['activity_log'].append(event)

    if request.POST['place'] == 'Casino':
    goldearned = random.randint (-50,50)
        request.session['totalgold'] += goldearned
        if goldearned >=0:
            event = f"went to the Casino and earned {goldearned}"
        else:
            event = f'went to the Casino and lost{goldearned}'

        
        request.session ['activity_log'].append(event)

    return redirect ('/')












# def index(request):
#     return render(request,'index.html')
#     if 'Farm' not in request.session:
#         request.session['Farm'] = 0
#         request.session['Cave'] = 0\
#         request.session['House'] = 0\
#         request.session['Casino'] = 0\


#     return render(request.session)
#         request.session['Cave'] = 0\
#         request.session['House'] = 0\
#         request.session['Casino'] = 0\


# def Vote(request):
#     print(request.POST)
#     if request.POST['place'] == 'Farm':
#         request.session['Farm'] +=1
#     if request.POST['place'] == 'Cave':
#         request.session['Cave'] +=1
#     if request.POST['place'] == 'House':
#         request.session['House'] +=1
#     if request.POST['place'] == 'Casino':
#         request.session['Casino'] +=1
#     return redirect('/')]