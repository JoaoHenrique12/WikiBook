# WikiBook

![apresentacao](presentation.gif)

## Sobre

A ideia inicial era construir uma rede social para pessoas que liam artigos da wikipédia.
O 'algoritmo' juntaria pessoas que gostassem de artigos semelhantes.
Sendo assim, dentro da pasta [web_crawler](web_crawler/) deveria haver o programa para 
extrair os metadados de uma série de páginas da wikipédia. Metadados estes que auxiliariam
na junção dos usuários da rede social.

WikiBook é um projeto inacabado, mas possui alguns pontos interessantes a serem observados.

### Autenticação de usuários

A autenticação de usuários com Django é baseada em 2 pontos principais:

- Na model User.

[models.py](WikiBook/social_media/models.py)

```python3
from django.contrib.auth.models import User
```

- No decorator @login_required() ou na classe LoginRequiredMixin

Que são usados nas views.

[views.py](WikiBook/social_media/views.py)

```python3
@login_required
def password_change_done(request):
    return render(request, 'registration/password_change_done.html',
                  {'information_updated': True})

...

# LoginRequiredMixin, must be the first class in inheritance.
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'social_media/profile.html'

...
```


### Django signals

Funcionam como se fossem procedures de bancos de dados.

Este signal foi implementado para assegurar a criação de um **Profile** toda vez que um **User** fosse
criado.

Para observar a implementação destes signals vá aos arquivos:
- [ signals.py ](WikiBook/social_media/signals.py)
- [ apps.py ](WikiBook/social_media/apps.py)


### Selenium e Factory Boy com Django 

Foi criado apenas um teste no arquivo [tests.py](WikiBook/social_media/tests.py),
o objetivo principal era observar como o Selenium seria integrado com o Django.

Além disto também foi pesquisado sobre a criação de fake objects com
[Factory Boy](https://factoryboy.readthedocs.io/en/stable/).
Um exemplo pode ser observado neste outro repositorio:
[LINK](https://github.com/JoaoHenrique12/django_junk/blob/master/FactoryBoy/social_media/tests/fake_objects.py)

