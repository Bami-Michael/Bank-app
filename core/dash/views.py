from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Transaction, Member,Guest,Idme,Bank
from .forms import transferform,profileform,settingsform,MyPasswordChangeForm,guestform,idme_field,Contact_form
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt




def home(request):
    return render(request, 'index.html', {} )



def aboutus(request):
    return render(request, 'aboutus.html', {} )



def contact2(request):
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Message Sent! We will get back to you as soon as possible!')
            return redirect(contact2)
    form = Contact_form()
    return render(request, 'contact2.html', {"Contact_form":Contact_form} )



@login_required(login_url="logger")
def contact(request):
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Message Sent! We will get back to you as soon as possible!')
            return redirect(dash)
    form = Contact_form()
    return render(request, 'contact.html', {"Contact_form":Contact_form} )





@login_required(login_url="logger")
def idme_page(request):   
    if request.method == 'POST':
        form = idme_field(request.POST)
        if form.is_valid():
            presave = form.save(commit=False)
            presave.idm = request.user
            presave.save() 
            messages.success(request, 'Your ID.me Account will be Verified!')
            return redirect(userprofile)
        else:
            messages.error(request, 'Invalid Logging  !!!')
            return redirect(idme_page)
    form = idme_field()
    return render(request, 'Idme.html', {'form': form})



@login_required(login_url="logger")
def portfolio(request):
    messages.info(request, 'You currently have no Investment Portfolio !')
    return redirect(dash)



@login_required(login_url="logger")
def faq(request):
    #history = Transaction.objects.all().filter(user = request.user).order_by('-id')[:8]
    return render(request, 'faq.html', {} )

    
    


@never_cache 
@login_required(login_url="logger")
def userprofile(request):
    currentUser = Member.objects.get(user = request.user)
    form1 = profileform(
    data=(request.POST or None),
    files=(request.FILES or None),
    instance=currentUser)
    if "prof" in request.POST and form1.is_valid():
        form1.save()    
        messages.success(request, 'Profile Updated!')   
        return redirect(userprofile)    
    
    form2 = settingsform(request.POST or None,instance=currentUser)
    if "set" in request.POST and form2.is_valid():
        form2.save() 
        messages.success(request, 'Settings Updated!')       
        return redirect(userprofile) 

    if "guest" in request.POST:
        form = guestform(request.POST,request.FILES)
        if form.is_valid():
            presave = form.save(commit=False)
            presave.Guest = request.user
            presave.save() 
            messages.success(request, 'Guest Account Created Successfully')
            return redirect(userprofile)
        else:
            messages.info(request, 'Error Creating Quest Account !')
            return redirect(userprofile) 
    

    form = form = MyPasswordChangeForm(request.user, request.POST)
    form3 = guestform()
    
    
    return render(request, 'userprofile.html', {"form1":form1,"form2":form2,'form': form,"form3":form3, })




@login_required(login_url="logger")
def change_password(request):
    if request.method == 'POST':
        form = MyPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect(userprofile)
        else:
            messages.error(request, 'Invalid Password Change !!!')
            return redirect(userprofile)
    else:
        form = MyPasswordChangeForm(request.user)
    return render(request, 'userprofile.html', {'form': form })







@login_required(login_url="logger")
def transfer(request):
    banks = Bank.objects.all
    context ={"banks":banks}
    form = transferform(request.POST or None, request.FILES or None)
    #bform = bank_form(request.POST or None, request.FILES or None)
    if form.is_valid():        
        transaction = form.save(commit=False)
        transaction.user = request.user
        #transaction.bank = request.POST['bank']
        transaction.save() 
        newprice = Transaction.objects.all().filter(user = request.user)
        oldprice = Member.objects.all().filter(user = request.user)
        z = 0
        for x in oldprice:
            z = x.checkings
        a = 0
        for x in newprice:
            a = x.amount           
        Member.objects.filter(user = request.user).update(checkings = z-a)
        messages.success(request, 'Your money transfer is now processing...')
        return  redirect(dash)

    context['form']= form 
    return render(request, "transfer.html", context)

    


@login_required(login_url="logger")
def dash(request):
    user = Member.objects.get(user = request.user)
    if user.status == "locked":
        logout(request)    
        return render(request, 'locked.html', {} )
    history = Transaction.objects.all().filter(user = request.user).order_by('-timestamp')[:8]
    return render(request, 'dash.html', {'history': history} )



@login_required(login_url="logger")
def historyview(request):
    #history = Transaction.objects.all().filter(user = request.user)
    #return render(request, 'history.html', {'history': history} )
    posts = Transaction.objects.all().filter(user = request.user).order_by('-timestamp')  # fetching all post objects from database
    p = Paginator(posts, 12)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    st = "${:.2f}"
    context = {'page_obj': page_obj, "st":st}
    # sending the page object to index.html
    return render(request, 'history.html', context)


@csrf_exempt
def logger(request):   
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session.set_expiry(3000)
            login(request, user)
            return  redirect(dash)
        else:
            messages.success(request, ("Invalid Login Credentials, Try Again..."))
            return  redirect(logger)
    else:
        return render(request, 'login.html', {} )


def logout_user(request):
    logout(request)    
    return redirect("home")


