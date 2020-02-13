### Social-login using django-allauth

##### Installation:
* *pip install django-allauth*

* edit some settings as shown:
https://django-allauth.readthedocs.io/en/latest/installation.html



### for using google login

In setting.py :

INSTALLED_APPS = (

.......
            'allauth.socialaccount.providers.google',

            )


The Google provider is OAuth2 based.

#### App registration

Create a google app to obtain a key and secret through the developer console.



##### Google Developer Console
    https://console.developers.google.com/ 
 * create project
 * go to OAuth consent screen and fill it
 * go to credentials and create oAuth Client Id
 *  you'll get client_id and secret key
 * use it in django


#### for facebook login

In setting.py :

INSTALLED_APPS = (

.......
            'allauth.socialaccount.providers.facebook',
            )

* create secret key and client id by visiting:
 developers.facebook.com





 references:
  https://django-allauth.readthedocs.io/en/latest/installation.html
 https://django-allauth.readthedocs.io/en/latest/providers.html#google
 https://django-allauth.readthedocs.io/en/latest/providers.html#facebook



