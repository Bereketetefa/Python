from django.urls import path, datetime
from datetime import date 

def main(request):
    date = date.today()
    print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

    currenttime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    context = {
        'time': currenttime
    }

    return render(request, "time_display.hmtl", context)














