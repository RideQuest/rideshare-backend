# Ridequest
[![Build Status](https://travis-ci.org/RideQuest/rideshare-backend.svg?branch=master)](https://travis-ci.org/RideQuest/rideshare-backend)
## In city carpool app. Less Trafic, better city.
   Coproduction of Codefellows Python401 and Javascript401.
### Authors

    Jared Scarr
    Lisa Wenke
    Rick Tesmond
    Sawako Ishida
    Wenjing Qiang


## Endpoints
   The Rideshare Api features restful endpoints that can be accessed by a front end application. Most require authorization and authentication in order to access the data.
   
#### Signup - Allows a user to register.
    
      entered URL: /users/signup
      returns:

        HTTP/1.0 200 OK
        Allow: POST, HEAD, OPTIONS
        Content-Type: application/json
        Vary: Accept, Cookie

        [
            {
                "email": "rider@example.com",
                "id": 1,
                "password": "pbkdf2_sha256$24000$840UJfb2V0WH$T1Ra98hPO//va52p3ICuU7HofVrFUgFkaasoCZVrjfo=",
                "username": "example_rider"
            }
        ]
        
#### Login - Allows a user to register.
    
      entered URL: /auth-token/
      returns:

        HTTP/1.0 200 OK
        Allow: POST, OPTIONS
        Content-Type: application/json
        Vary: Accept, Cookie

        [
            {
               "profile_id": null,
               "token": "1fb4170f3d112d5983ce4856b9b5477400386784",
               "user_id": 12
            }
        ]
   
#### Get/Modify User.
    
      entered URL: /users/1/
      returns:

        HTTP/1.0 200 OK
        Allow: GET, POST, HEAD, OPTIONS
        Content-Type: application/json
        Vary: Accept, Cookie

        [
            {
                "email": "rider@example.com",
                "id": 1,
                "password": "pbkdf2_sha256$24000$840UJfb2V0WH$T1Ra98hPO//va52p3ICuU7HofVrFUgFkaasoCZVrjfo=",
                "username": "example_rider"
            }
        ]
        
#### Add Profile

      entered URL: /profiles/add
      returns:

        HTTP/1.0 200 OK
        Allow: PUT, POST, PATCH, DELETE, HEAD, OPTIONS
        Content-Type: application/json
        Vary: Accept

        {
            "carbrand": "Jaguar",
            "carseat": 3,
            "email": "rider@example.com",
            "firstname": "Ride",
            "lastname": "Share-er",
            "petsallowed": true,
            "phonenumber": "+41524204242"
        }

#### Get/Modify Profile

      entered URL: /profiles/<user pk>/
      returns:

        HTTP/1.0 200 OK
        Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
        Content-Type: application/json
        Vary: Accept

        {
            "carbrand": "Jaguar",
            "carseat": 3,
            "email": "rider@example.com",
            "firstname": "Ride",
            "lastname": "Share-er",
            "petsallowed": true,
            "phonenumber": "+41524204242"
        }

#### Add Route - Add a route associated with a user.
    
      entered URL: /routes/add
      returns:

        HTTP/1.0 200 OK
        Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
        Content-Type: application/json
        Vary: Accept

        {
            "id": 1,
            "start_point": "SRID=4326;POINT (-122.3372268676900063 47.5948333740239988)",
            "user": 1
        }
    
#### Get/Modify Routes - Returns list of routes associtated with a specified user.
    
      entered URL: /routes/<user pk>/
      returns:

        HTTP/1.0 200 OK
        Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
        Content-Type: application/json
        Vary: Accept

        {
            "id": 1,
            "start_point": "SRID=4326;POINT (-122.3372268676900063 47.5948333740239988)",
            "user": 1
        }
    
#### Query - Returns all possible rideshares within a radius of a starting point.
    
      entered URL: /query/
      returns:
      
        HTTP/1.0 200 OK
        Allow: GET, POST, HEAD, OPTIONS
        Content-Type: application/json
        Vary: Accept, Cookie

        {
            "id": 10,
            "start_point": "SRID=4326;POINT (-122.3372268676900063 47.5948333740239988)",
            "user": 10
        },
        {
            "id": 11,
            "start_point": "SRID=4326;POINT (-122.3372268676900063 47.5948333740239988)",
            "user": 11
        }
    

### Storage
    
We utilized Ansible, Amazon Web Service EC2, and an RDS instance for deployment. The app requires a Postgresql database with a PostGis extension to store geographic information.
    

### Dependency Requirements
    
    Django==1.9.5
    django-cors-headers==1.1.0
    django-phonenumber-field==1.1.0
    djangorestframework==3.3.3
    dj-database-url==0.4.1
    factory-boy==2.7.0
    fake-factory==0.5.7
    geojson==1.3.2
    Pygments==2.1.3
    psycopg==2.6.1
    requests==2.9.1
    

