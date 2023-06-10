########-----------------------------------------------------------------------#######
########                     project setup script for django                   #######
########-----------------------------------------------------------------------#######

import os, json, requests
from pathlib import Path



def file_opener(name, mode, content=[]):
    if mode == 'r':
        with open(name, mode) as f:
            return f.readlines()
    elif mode == 'w':
        with open(name, mode) as f:
            f.writelines(content)
    elif mode == 'json':
        with open(name, 'w') as f:
            json.dump(content, f, indent=4, sort_keys=True)

def array2str(arr):
    str = ''
    for item in arr:
        str += item + '\n'
    return str  
    
def array2file(content:list()):
    arr = []
    for item in content:
        arr.append(item+'\n')
    return arr

def projectsetup():

    new_file = []
    
    string = file_opener(f'{project}/{project}/settings.py', 'r')[12:]
    
    # creating .ENV file value
    def create_env(name, value='', file=''):
        with open(f'{project}/.env', 'a+') as f:
            f.writelines(f"{name} = {value}\n")
            if name == "SECRET_KEY":
                new_file.append( f'{name} = os.getenv("{name}")\n')
            else:
                new_file.append( f'{name}{" "*((18 - len(name)))} = os.getenv("{name}")\n')

    #project/settings.py        
    for index in range(len(string)):
        if string[index][0] != "#":
            if string[index] != "\n" and  string[index].split()[0] == file['project']['settings']['secret'] :
                name = file['project']['settings']['secret']
                value = string[index].split()[-1]
                # .ENV file
                create_env(name, value)
                
            elif string[index] != "\n" and  string[index].split()[0] == 'INSTALLED_APPS':
                new_file.append(string[index])
                new_file.insert(index+1, array2str(file['project']['settings']['install_app']))
                
            elif string[index] != "\n" and  string[index].split()[0].strip(":") == "'DIRS'":
                template = "os.path.join(BASE_DIR, 'Templates')"
                new_file.append(f"\t\t'DIRS' : [{template}],\n")
                
            elif string[index] != "\n" and  string[index].split()[0] == "STATIC_URL":
                new_file.append(string[index])
                new_file.append(array2str(file["project"]["settings"]["path"]))
                
            elif string[index] != "\n" and  string[index].split()[0] == "DEFAULT_AUTO_FIELD":
                new_file.append(string[index])
                new_file.append(array2str(file["project"]["settings"]["email_backend"]))
                
                for name in file["project"]["settings"]["email_secret"]:
                    create_env(name)
                new_file.append(array2str(file["project"]["settings"]["email_protocol"]))
                
            else:
                new_file.append(string[index])
                
    # import module in settings.py
    new_file.insert(1, array2str(file['project']['settings']['import']))
    
    # project/settings.py
    file_opener(f'{project}/{project}/settings.py', 'w', new_file)
    
    # project/urls.py
    file_opener(f'{project}/{project}/urls.py', 'w', array2file(file['project']['urls']))
    
def appsetup():
    file_opener(f'{project}/{app}/urls.py', 'w', array2file(file["app"]['urls']))
    file_opener(f'{project}/{app}/views.py', 'w', array2file(file["app"]['views']))

def createsuperuser():
    file_opener(f'{project}/{project}/wsgi.py', 'w', file_opener(f'{project}/{project}/wsgi.py', 'r')[9:] + array2file(file['project']['wsgi']))

def system(project, app):
    venv = project + '-venv'
    # os.system(f"python -m venv {venv}")
    # os.system(f'"D:\Python\DevOps\ProjectSetup\{venv}\Scripts\python.exe -m pip install --upgrade pip"')
    # os.system(f'"D:\Python\DevOps\ProjectSetup\{venv}\Scripts\pip3.11.exe install django python-dotenv requests"')
    os.system(f'"D:\Python\DevOps\ProjectSetup\{venv}\Scripts\django-admin.exe  startproject {project}"')

    os.system(f'"cd {project} && D:\Python\DevOps\ProjectSetup\{venv}\Scripts\django-admin.exe  startapp {app} && echo #> {app}/urls.py"')

    os.system(f"D:\Python\DevOps\ProjectSetup\{venv}\Scripts\pip3.11.exe freeze > {project}/requirements.txt")
    
def staticsetup():
    dirs = ['Templates', 'media']
    for dir in dirs:
        Path(f'{project}/{dir}').mkdir(parents=True, exist_ok=True)
    
    #for index.html
    r = requests.get('https://raw.githubusercontent.com/IshuSinghSE/scripts/master/index.html')
    with open(f'{project}/{dirs[0]}/index.html', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

    #for .gitignore
    r = requests.get('https://raw.githubusercontent.com/IshuSinghSE/scripts/master/gitignore')
    with open('.gitignore', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    
    # for README.md        
    r = requests.get('https://raw.githubusercontent.com/IshuSinghSE/scripts/master/README.md')
    with open('README.md', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    

def main(project, app):
    venv = project + '-venv'
    staticsetup()
    # system(project, app)
    # projectsetup()
    # appsetup()
    # # file_opener('config.json', 'json', file)
    # createsuperuser()
    # os.system(f'"D:\Python\DevOps\ProjectSetup\{venv}\Scripts\python.exe {project}\manage.py makemigrations"')
    # os.system(f'"D:\Python\DevOps\ProjectSetup\{venv}\Scripts\python.exe {project}\manage.py migrate"')
    # os.system(f'"D:\Python\DevOps\ProjectSetup\{venv}\Scripts\pip3.11.exe uninstall  requests"')
    
    # os.system(f'start "C:\Program Files\Google\Chrome\Application\chrome.exe"  http://127.0.0.1:8000/')
    # os.system(f"D:\Python\DevOps\ProjectSetup\{venv}\Scripts\python.exe {project}\manage.py runserver")
    
# if __name__ == "__main__":
project = 'temp'#input('Project name : ')
app = 'demo'#input('App name : ')

file = {    
        "project":{
                "urls":[
                    "from django.contrib import admin",
                        "from django.urls import path, include",
                        "from django.conf import settings",
                        "from django.conf.urls.static import static\n",
                        "urlpatterns = [",
                        "\tpath('admin/', admin.site.urls),",
                        f"\tpath('',include('{app}.urls')),",
                        "]",
                        "urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)",],    
                "settings":{
                        "import":[
                            "from dotenv import load_dotenv",
                            "import os\n",
                            "load_dotenv()",],
                        "secret":
                            "SECRET_KEY",
                        "install_app":
                        [f"\t'{app}.apps.{app.capitalize()}Config',",],
                        "path":[
                            "STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]",
                            "STATIC_ROOT = os.path.join(BASE_DIR,'assets')\n",
                            "MEDIA_URL  = '/media/'",
                            "MEDIA_ROOT = os.path.join(BASE_DIR,'media')",],
                        "email_backend":[
                            "\n\n### Email Configuration ###",
                            "EMAIL_BACKEND   = 'django.core.mail.backends.smtp.EmailBackend'",
                            "EMAIL_HOST      = 'smtp.mail.yahoo.com'",],
                        "email_secret":
                            ["EMAIL_USER" ,"EMAIL_PASSWORD" ,"DEFAULT_FROM_EMAIL" ,"RECIPIENT_ADDRESS",],
                        "email_protocol":[
                            "EMAIL_PORT    = 587",
                            "EMAIL_USE_TLS = True",
                            "EMAIL_USE_SSL = False",
                            "EMAIL_TIMEOUT = 30",],
                        },
                "wsgi":[
                        "from django.contrib.auth.models import User",
                        "users = User.objects.all()",
                        "if not users:",
                        "\tUser.objects.create_superuser(username='admin', email='user@example.com', password='admin', is_active=True, is_staff=True)",
                    ],
                    },
        
        "app":{ 
                "urls": ["from django.urls import path, include",
                        "from .views import index\n",
                        "urlpatterns = [",
                        "\tpath('',index, name='index'),",
                        "\n]",
                        ],
                "views":["from django.conf import settings",
                        "from django.shortcuts import render\n",
                        "def index(request):",
                        "\treturn render(request, 'index.html',{})",
                        ],     
                },
        }

if app == '':
    main(project, project)
else:
    main(project, app)
