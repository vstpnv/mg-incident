# MG Incident
Magnezio Incident Management — Is Intuitive And Open-Source Customer Support Software.

### Features
* Easy to setup and use for customer and stuff;
* Based on Python 3.5, micro framework Flask and popular Flask extensions (flask-admin, flask-security, flask-sqlalchemy and some more);
*  Minimum settings, maximum productivity – great for small projects;

------------


### Main concepts and entities:
##### Users, Roles and Roles Statuses
- User has a role (**user**, **worker**, **manager** and **admin** roles are already predefined by default, but you can easily identify your custom role).
- Roles can has some Roles Statuses (see below to understand more).

##### Ticket, Ticket Status and Ticket Status Tracking
- Customer (as a rule – user with role ‘user’) add new ticket (for example ticket about something error).
- **Ticket can has a status (new, in progress, pending customer, pending vendor, pending maintenance, transferred, solved, closed already predefined by default, but you can easily identify your custom role).**

Some tickets statuses can be available only for certain roles status.
For example:
- **Customers** can set available for their role status statuses for their tickets.
- **Workers** cat set available for their role status statuses for the tickets they have assigned.
- Managers cat set available for their role status statuses for all tickets.

You can change customer ticket status (for example, new to in progress status) and this changes will be reflected in **Ticket Status Tracking** for history. Also, you can decomposition big ticket to some small tickets too.

------------



### Base deployment
MG Incident works with several open source projects. To get MG Incident up and running you will need to install all of its dependencies. You can see base deployment instruction bellow.

It is understood that you already have Python 3, Docker and Docker Compose installed (Using Docker is not necessary and you can set up database manually (see bellow).

**First of all, clone the project:**

`git clone https://github.com/magnezio/mg-incident.git`

**Configure SMPT server to sending email (for registration and confirmation) in config/production.py:**
```python
MAIL_SERVER = ''
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
SECURITY_EMAIL_SENDER = ''
```
**Make a virtualenv (not necessary if you using pipenv):**

`python3 -m venv env`

**And activate it:**

`. env/bin/activate`

**Install pipenv:**

`pip install pipenv`

**...and project requirements:**

`pipenv install`

**If you prefer using docker-compose for setup database, use (in second terminal window for comfort):**

`docker-compose -f docker/production/docker-compose.yml up`

**Or run postgres db daemon manually.**

**Run sql scripts:**

`psql -U postgres -h localhost < sql/default/create_user.sql`

`psql -U postgres -h localhost < sql/default/create_db.sql`

That created a db user **mgincident_app** with password **masterkey** (configure at  create_user.sql) and database **mgincident** with owner **mgincident_app**.

**In terminal with opened virtualenv run:**

`export MGI_DB_PASSWORD=masterkey`

`export FLASK_APP=run.py`

**Insert predefined roles and ticket statuses:**

`flask insert_predefined_roles_for_users`

`flask insert_predefined_ticket_statuses`

**And run!**

`flask run`
