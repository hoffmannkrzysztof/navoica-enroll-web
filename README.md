# Formularz Rejestacyjny Navoica

## Wersja automatyczna instalacji:

Ustaw zmienne środowiskowe:

    export ENROLL_DOMAIN = domena.pl

    export ENROLL_EMAIL = adres_do_kontaktu@domena.pl

Uruchom komende:

    make setup

Ostatnim krokiem instalacji będzie ustawienie hasła dla użytkownika `admin`.
Przejdź do sekcji `Konfiguracja Oauth2`


## Wersja ręczna instalacji:

Przejdź do katalogu .envs i skopiuj domyślne ustawienia:


    cd .envs/
    mv .production_example/ .production



Edytuj wg potrzeby. Przykładowe wartości poniżej:

   `.production/.django`

    DJANGO_SECRET_KEY=8zqaTVpMGbAJ6mKdTsdfSDASswwdSfGSZlzAdIpzTYbDXfKw53HVdRCM8n

    DJANGO_ADMIN_URL=admin/

    DJANGO_ALLOWED_HOSTS=enroll.navoica.pl

    DOMAIN=enroll.navoica.pl

    NAVOICA_URL=https://draft.navoica.pl



Zmodyfikuj ustawienia serwera HTTP:

    cd compose/production/traefik/

    mv traefik.yml.example traefik.yml

   `Edytuj plik traefik.yml`

    zmień zmienne __DOMAIN__ i __EMAIL__

Pamiętaj żeby __DOMAIN__ było zgodne z ustawieniami w `.django` z `DOMAIN` i `DJANGO_ALLOWED_HOSTS`

### Budowanie i uruchamianie Dockera

    docker-compose -f production.yml build

    docker-compose -f production.yml up -d

Po uruchomieniu uruchamiamy migracje danych i tworzymy własnego użytkownika admina

    docker-compose -f production.yml exec django python manage.py migrate

    docker-compose -f production.yml exec django python manage.py createsuperuser


## Konfiguracja Oauth2 do komunikacji z navoica.pl

Przechodzimy do panelu administratora (adres może się różnić od wartości `DJANGO_ADMIN_URL`):

    https://enroll-test.navoica.pl/admin/

Uzupełniamy informacje o domenie zgodnie z `DOMAIN`

    https://enroll-test.navoica.pl/admin/sites/site/1/change/

Dodajemy wartości OAUTH2 otrzymane od administratora z navoica.pl, provider EDX

    https://enroll-test.navoica.pl/admin/socialaccount/socialapp/
