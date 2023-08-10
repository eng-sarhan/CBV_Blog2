# to activate Virtual Machine  : venv\Scripts\activate
# to upgrade pip : python -m pip install --upgrade pip
# to install django   : pip install django==4.1
# to create django project   : django-admin startproject blog .
# to startapp 'products'  : python manage.py startapp users posts
# to install pillow   : pip install pillow==8
# to create mysql database   : pip install django-mysql==4.2
# to create mysqlclient database   : pip install django mysqlclient
# to create  pymysql database   : pip install pymysql
# to make migrations   : python manage.py makemigrations 
# to migrate   : python manage.py migrate
# to createsuperuser  : python manage.py createsuperuser
# to adding static folders  : python manage.py collectstatic
# pip install django-crispy-forms
# pip install crispy-bootstrap4
# pip install django-allauth
# pip install django-tinymce4-lite
# pip install django-tinymce4-lite==1.7.4

# to run server   : **_**  python manage.py runserver  **_**


# to create requirements  : pip freeze > requirements.txt
# to install requirements  : pip install -r requirements.txt

# sarhan Gamalat@1309@1309
# from mycoffee.wsgi import application
# allowed host = ['mycoffee.engsarhan.com','www.mycoffee.engsarhan.com']

#to create Virtual Machine  : pip install virtualenv enter cd desktop enter virtualenv mysite enter
# from django.conf.urls import url
# D:\PycharmProjects\Mixed_Blog\venv\Lib\site-packages\tinymce\urls.py
# from django.conf.urls import url
# replaced by
# from django.urls import re_path as url
# to adding static folders  : python manage.py collectstatic 
#  :  pip install psycopg2
#   :  pip install psycopg2-binary
#   : pip install pillow
# to rename project : python manage.py renameproject oldname newname

 # to make migrations   : python manage.py migrate --run-syncdb
===========  mysql database  ===================
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'BV_Blog2',
		'USER': 'root',
		'PASSWORD': 'Gamalat@1309@1309',
		'HOST':'localhost',
		'PORT':'3306',
	}
}
=======================
 to create new database:-
from mysql workbench
select schema
create database BV_Blog2;
-----------------------------
to create new database:-
from cmd or Windows shell
mysql --version
mysql -u root -p
password
mysql>show databases;
mysql>create database mycoffee;
mysql>show databases;
-----------------------------------
 


reverse("polls:index", current_app=self.request.resolver_match.namespace)

reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)

from django.core.urlresolvers import reverse
# ...
return HttpResponseRedirect(reverse(index))


def get_absolute_url(self):
    return "/people/%i/" % self.id

                {% load countries %}
                {% get_countries as countries %}
                <select>
                {% for country in countries %}
                    <option value="{{ country.code }}">{{ country.name }}</option>
                {% endfor %}
                </select>

  <select class="selectpicker countrypicker" data-flag="true" ></select>
<select class="selectpicker countrypicker" data-flag="true" ></select>

  <script>
    $('.countrypicker').countrypicker();
  </script>

pip install django-countries==2.0

                 <div class="form-group col-md-4">
                    <label for="inputCountry">Country</label>
                    <input type="text" class="form-control" name="country" id="inputCountry" required value="{{country.name}}">
                </div>

first_name=request.POST.get("first_name", "default value")

<option value="{{ specialization|lower }}" 
    {% if specialization.selected %} selected {% endif %} >
    {{ specialization }}
</option>

<div class="form-group col-md-4">
                    <label for="inputCountry">Country</label>
                    <input type="text" class="form-control" name="country" id="inputCountry" required value="{{country.name}}">
                </div>

[//]: # (<option value="age" {% if sort == 'age' %}selected{% endif %}>age</option>)
{% if country.code =="country" %}
value="country.code" {% if sort == 'country.code' %}selected{% endif %}

    <div class="container mx-auto flex flex-wrap py-6 overflow-hidden">

                   <select id = 'countries' onchange="countrySelected()">
                        <!-- Filled via JS -->
                        <option> Select Country </option>
                        {% for country in country_list%}
                            <option value="{{country.id}}"> {{ country }} </option>
                        {% endfor %}
                   </select>



<!--                <a class="dropdown-item" href="{% url 'posts:post' pro_id=1 %}">Caffè Americano</a>-->
<!--                <a class="dropdown-item" href="{% url 'posts:post' pro_id=2 %}">Café Latte</a>-->
<!--                <a class="dropdown-item" href="{% url 'posts:post' pro_id=3 %}">Cappuccino</a>-->
<!--                <a class="dropdown-item" href="{% url 'posts:post' pro_id=4 %}">Espresso</a>-->
<!--                <a class="dropdown-item"   href="{% url 'posts:posts' %}">All Products</a>-->

<!--              <li class="nav-item">-->
<!--                  <a class="nav-link" href="{% url 'orders:cart' %}">-->
<!--                       <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-cart4" viewBox="0 0 16 16">-->
<!--                      <path fill-rule="evenodd" d="M8 5.754a2.246 2.246 0 100 4.492 2.246 2.246 0 000-4.492zM4.754 8a3.246 3.246 0 116.492 0 3.246 3.246 0 01-6.492 0z" clip-rule="evenodd"/>-->
<!--                      <path d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5zM3.14 5l.5 2H5V5H3.14zM6 5v2h2V5H6zm3 0v2h2V5H9zm3 0v2h1.36l.5-2H12zm1.11 3H12v2h.61l.5-2zM11 8H9v2h2V8zM8 8H6v2h2V8zM5 8H3.89l.5 2H5V8zm0 5a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0zm9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"/>-->
<!--                    </svg>-->
<!--                  </a>-->
<!--              </li>-->

<!--              <li class="nav-item">-->
<!--                  <a  href="{% url 'orders:my_order' %}" class="nav-link border border-light rounded waves-effect" >Orders</a>-->
<!--              </li>-->


              <li class="nav-item">
                  <a  href="{% url 'accounts:show_post_favorite' %}" class="nav-link border border-light rounded waves-effect" >
                   <svg xmlns="http://www.w3.org/2000/svg" width="25" height="35" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                        <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
                    </svg>
                  </a>
              </li>

# from django.urls import re_path as url


            <form action="{% url 'posts:post-list' %}" class="form-inline my-2 my-lg-0">