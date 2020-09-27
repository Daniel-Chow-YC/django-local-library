from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic # for class based views

# Create your views here.

# ---------------------index page view function -----------------------

def index(request):
    """View function for home page of site."""

    # if request.method == 'GET':

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    # Get a session value, setting a default value of 0 if it is not present 
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# ---------------------all books page class view -----------------------
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

# ---------------------book detail view -----------------------
class BookDetailView(generic.DetailView):
    model = Book

# --------------------all authors page view -----------------------
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

# ---------------------author detail view -----------------------
class AuthorDetailView(generic.DetailView):
    model = Author

# ---------------------on loan view -----------------------
from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

# --------------------- all loaned books view ---------------------
from django.contrib.auth.mixins import PermissionRequiredMixin

class LoanedBooksAllBooksListView(PermissionRequiredMixin,generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
    permission_required = 'catalog.can_mark_returned'
    model = BookInstance
    template_name ='catalog/bookinstance_list_all_loaned_books.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


# ## for function based view:
# from django.contrib.auth.decorators import permission_required

# @permission_required('catalog.can_mark_returned')
# def my_view(request):
#     ...


# ---------------------Testing against authenticated users---------------------
## for function-based views, the easiest way to restrict access to your functions is to apply the login_required decorator to your view function

# from django.contrib.auth.decorators import login_required

# @login_required
# def my_view(request):
#     ...


## the easiest way to restrict access to logged-in users in your class-based views is to derive from LoginRequiredMixin. You need to declare this mixin first in the superclass (parent class) list, before the main view class.

# from django.contrib.auth.mixins import LoginRequiredMixin

# class MyView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'