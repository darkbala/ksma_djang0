
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View, generic
from django.contrib.auth.decorators import login_required
from users.forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm, Form_notes
from .models import AllBooksModel, Model_notes_of_user, Model_footer, PersonModal



class HomeView(generic.ListView):
    template_name = 'users/home.html'
    
    def get_queryset(self):
        books = AllBooksModel.objects.all()[::-1]
        books = books[:9]
        data = PersonModal.objects.all()
        context = {
        'books': books,
        'data':data,
        }
        return context
        

#user_register
class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})


#BOOOOk

def detail(request, book_id):
    book = AllBooksModel.objects.get(id=book_id)
    return render(request, 'mainpage/aboutBook.html', {'book': book})

#NOTES
class View_user_notes(generic.ListView):
    template_name = 'note/notes.html'

    def get_queryset(self):
        return Model_notes_of_user.objects.all()[::-1]


class View_create_note(generic.CreateView):
    template_name = 'note/add_note.html'
    form_class = Form_notes
    success_url = '/notes/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(View_create_note, self).form_valid(form=form)


class View_update_note(generic.UpdateView):
    template_name = 'note/update_note.html'
    form_class = Form_notes
    success_url = '/notes/'

    def get_object(self, **kwargs):
        note_id = self.kwargs.get('id')
        return get_object_or_404(Model_notes_of_user, id=note_id)

    def form_valid(self, form):
        return super(View_update_note, self).form_valid(form=form)


class View_delete_note(generic.DeleteView):
    template_name = 'note/delete_note.html'
    success_url = '/notes/'

    def get_object(self, **kwargs):
        note_id = self.kwargs.get('id')
        return get_object_or_404(Model_notes_of_user, id=note_id)
    
    
#COURSES

class AllBooksView(generic.ListView):
    template_name = 'users/books/all.html'
    paginate_by = 10
        
    def get_queryset(self):
        books = AllBooksModel.objects.all()
        return books
    
class BooksFirstView(generic.ListView):
    template_name = 'users/books/all.html'
        
    def get_queryset(self):
        filt = AllBooksModel.objects.filter(
            course = '1'
        )
        return filt
    
class BooksSecondView(generic.ListView):
    template_name = 'users/books/all.html'
        
    def get_queryset(self):
        filt = AllBooksModel.objects.filter(
            course = '2'
        )
        return filt
    
class BooksThirdView(generic.ListView):
    template_name = 'users/books/all.html'
        
    def get_queryset(self):
        filt = AllBooksModel.objects.filter(
            course = '3'
        )
        return filt
    
class BooksFourthView(generic.ListView):
    template_name = 'users/books/all.html'
        
    def get_queryset(self):
        filt = AllBooksModel.objects.filter(
            course = '4'
        )
        return filt
    
class BooksFifthView(generic.ListView):
    template_name = 'users/books/all.html'
        
    def get_queryset(self):
        filt = AllBooksModel.objects.filter(
            course = '5'
        )
        return filt
    
class BooksSixthView(generic.ListView):
    template_name = 'users/books/all.html'
        
    def get_queryset(self):
        filt = AllBooksModel.objects.filter(
            course = '6'
        )
        return filt
    
#SEARCH

class SearchBookView(generic.ListView):
    model = AllBooksModel
    template_name = "users/search.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = AllBooksModel.objects.filter(
            name_of_book__icontains = query
        )
        return object_list
    
    
#FOOTER

def footer(request):
    data = Model_footer.objects.all()
    return render(request, 'index.html', {'data':data})
