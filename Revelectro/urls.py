from django.contrib import admin
from django.urls import path, include
from accounts.views import home  # Import the home view from the accounts app

urlpatterns = [
    path('', home, name='home'),  # Define the URL pattern for the home page
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  
    path('ewaste_collection/', include(('ewaste_collection.urls', 'ewaste_collection'), namespace='ewaste_collection')),  
    path('product_selling/', include(('product_selling.urls', 'product_selling'), namespace='product_selling')),
    path('product_rental/', include(('product_rental.urls', 'product_rental'), namespace='product_rental')),
    
# Other URL patterns for your project
]