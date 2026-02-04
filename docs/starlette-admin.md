---
title: "Starlette-Admin -- документация"
description: "Административный интерфейс для Starlette и FastAPI приложений"
source: "https://jowilf.github.io/starlette-admin/"
---

# Starlette-Admin

*Fast, beautiful, and extensible administrative interface framework for Starlette & FastApi applications*

![Preview image](https://raw.githubusercontent.com/jowilf/starlette-admin/main/docs/images/preview.jpg)

## why starlette-admin?

FastAPI has emerged as a popular web framework for building APIs in Python. However, it lacks a mature admin interface
solution like Flask-Admin to quickly manage your data through a user-friendly interface. Although
solutions like Sqladmin and Fastapi-Admin exist, they only work with specific ORMs such as SQLAlchemy and Tortoise ORM.

Starlette-admin was born from the need for a FastAPI admin interface that works with various data layer. It aims
to provide a complete solution for CRUD interfaces regardless of the database backend. Starlette-admin works out of the
box with multiple ORM/ODMs and can also be used with a custom data layer.

## Getting started

* Check out [the documentation](https://jowilf.github.io/starlette-admin).
* Try the [live demo](https://starlette-admin-demo.jowilf.com/). ([Source code](https://github.com/jowilf/starlette-admin-demo))
* Follow the [tutorials](https://jowilf.github.io/starlette-admin/tutorials/)
* Try the several usage examples included in the [/examples](https://github.com/jowilf/starlette-admin/tree/main/examples) folder
* If you find this project helpful or interesting, please consider giving it a star ⭐️

## Features

- CRUD any data with ease
- Automatic form validation
- Advanced table widget with [Datatables](https://datatables.net/)
- Search and filtering
- Search highlighting
- Multi-column ordering
- Export data to CSV/EXCEL/PDF and Browser Print
- Authentication
- Authorization
- Manage Files
- Custom views
- Custom batch actions
- Supported ORMs
    * [SQLAlchemy](https://www.sqlalchemy.org/)
    * [SQLModel](https://sqlmodel.tiangolo.com/)
    * [MongoEngine](http://mongoengine.org/)
    * [ODMantic](https://github.com/art049/odmantic/)
    * Custom backend ([doc](https://jowilf.github.io/starlette-admin/advanced/base-model-view/), [example](https://github.com/jowilf/starlette-admin/tree/main/examples/custom-backend))
- Internationalization

## Installation

### PIP

shell
$ pip install starlette-admin

### Poetry

shell
$ poetry add starlette-admin

## Example

This is a simple example with SQLAlchemy model

python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from starlette.applications import Starlette

from starlette_admin.contrib.sqla import Admin, ModelView

Base = declarative_base()
engine = create_engine("sqlite:///test.db", connect_args={"check_same_thread": False})

# Define your model
class Post(Base):
  __tablename__ = "posts"

  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str]

Base.metadata.create_all(engine)

app = Starlette()  # FastAPI()

# Create admin
admin = Admin(engine, title="Example: SQLAlchemy")

# Add view
admin.add_view(ModelView(Post))

# Mount admin to your app
admin.mount_to(app)

Access your admin interface in your browser at [http://localhost:8000/admin](http://localhost:8000/admin)

## Third party

*starlette-admin* is built with other open source projects:

- [Tabler](https://tabler.io/)
- [Datatables](https://datatables.net/)
- [jquery](https://jquery.com/)
- [Select2](https://select2.org/)
- [flatpickr](https://flatpickr.js.org/)
- [moment](http://momentjs.com/)
- [jsoneditor](https://github.com/josdejong/jsoneditor)
- [fontawesome](https://fontawesome.com/)
- [TinyMCE](https://www.tiny.cloud/)

## Contributing

Contributions are welcome and greatly appreciated! Before getting started, please read
[our contribution guidelines](https://github.com/jowilf/starlette-admin/blob/main/CONTRIBUTING.md)

# Introduction

The tutorials will introduce you to a series of hands-on exercises designed to help you master the various features of
Starlette-Admin. Each tutorial guides you through practical steps, allowing you to learn by doing.

## Prerequisites

Before diving into the tutorials, ensure you meet the following prerequisites:

- Understand the basics of [FastAPI](https://fastapi.tiangolo.com/) or [Starlette](https://www.starlette.io/)
- Familiarize yourself with at least one of the following ORM/ODMs:
    * [SQLAlchemy](https://www.sqlalchemy.org/)
    * [SQLModel](https://sqlmodel.tiangolo.com/)
    * [MongoEngine](http://mongoengine.org/)
    * [ODMantic](https://github.com/art049/odmantic/)

# Building your first admin panel

The goal of this tutorial is to guide you through the process of creating an admin panel to manage a simple Todo model
using Starlette-Admin.

By the end of this tutorial, you will have a user-friendly admin interface to perform CRUD (Create, Read, Update,
Delete) operations on Todo items without the need for writing any front-end code or complex database queries.

!!! quote "What you will learn"

    - How to generate a basic admin panel for your models
    - Familiarize yourself with the generated admin panel
    - Basic concepts of Starlette-Admin

## Project Setup

### Installation

* Create a virtual environment and activate it

=== "macOS/Linux"

    shell
    python -m venv env
    source env/bin/activate
    

=== "Windows"

    shell
    python -m venv env
    env\Scripts\activate
    

* Create a 'requirements.txt' file with the following content

=== "SQLAlchemy"

    requirements
    starlette-admin
    sqlalchemy
    uvicorn
    

=== "SQLModel"

    requirements
    starlette-admin
    sqlmodel
    uvicorn
    

=== "MongoEngine"

    requirements
    starlette-admin
    mongoengine
    uvicorn
    

=== "ODMantic"

    requirements
    starlette-admin
    odmantic
    uvicorn
    

??? note

    If you prefer to setup a FastAPI project, add 'fastapi' in your requirements file. For example,

    requirements
    fastapi
    starlette-admin
    sqlalchemy
    uvicorn
    

* Install the dependencies

shell
pip install -r requirements.txt

### Project structure

    .
    │
    ├── env/                # Virtual environment directory
    ├── main.py             # Main tutorial file
    └── requirements.txt    # File specifying tutorial dependencies

In this tutorial, all code will be contained within the 'main.py' file for simplicity. As you progress to real-world
applications, consider organizing your code into modular structures.

## Define the model

Now that our project is ready, let's write the Todo model, on which we will perform the CRUD Operations

=== "SQLAlchemy"

    python
    from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

    class Base(DeclarativeBase):
        pass

    class Todo(Base):
        __tablename__ = "todo"

        id: Mapped[int] = mapped_column(primary_key=True)
        title: Mapped[str]
        done: Mapped[bool]
    

=== "SQLModel"

    python
    from typing import Optional

    from sqlmodel import Field, SQLModel

    class Todo(SQLModel, table=True):
        id: Optional[int] = Field(default=None, primary_key=True)
        title: str
        done: bool
    

=== "MongoEngine"

    python
    import mongoengine as db

    class Todo(db.Document):
        title = db.StringField()
        done = db.BooleanField()

    

=== "ODMantic"

    python
    from odmantic import Model

    class Todo(Model):
        title: str
        done: bool
    

Let's take a closer look at the attributes:

- 'id (int)': A unique identifier for each Todo item.
- 'title (str)': The title or description of the Todo item.
- 'done (bool)': A boolean value indicating whether the Todo item is marked as done.

??? note

    For **MongoEngine** and **ODMantic**, the 'id' field is added automatically and serves as the unique identifier.
    You don't need to explicitly define it in the model.

## Configure the admin panel

### Initialization

To begin, we'll set up an empty admin interface:

=== "SQLAlchemy"

    python hl_lines="1 3 5 21"
    from sqlalchemy import create_engine
    from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
    from starlette_admin.contrib.sqla import Admin

    engine = create_engine("sqlite:///basic.db", connect_args={"check_same_thread": False})

    class Base(DeclarativeBase):
        pass

    class Todo(Base):
        __tablename__ = "todo"

        id: Mapped[int] = mapped_column(primary_key=True)
        title: Mapped[str]
        done: Mapped[bool]

    # Create an empty admin interface
    admin = Admin(engine, title="Tutorials: Basic")
    

=== "SQLModel"

    python hl_lines="5 7 17"
    from typing import Optional

    from sqlalchemy import create_engine
    from sqlmodel import Field, SQLModel
    from starlette_admin.contrib.sqlmodel import Admin

    engine = create_engine("sqlite:///basic.db", connect_args={"check_same_thread": False})

    class Todo(SQLModel, table=True):
        id: Optional[int] = Field(default=None, primary_key=True)
        title: str
        done: bool

    # Create an empty admin interface
    admin = Admin(engine, title="Tutorials: Basic")
    

=== "MongoEngine"

    python hl_lines="2 11"
    import mongoengine as db
    from starlette_admin.contrib.mongoengine import Admin

    class Todo(db.Document):
        title = db.StringField()
        done = db.BooleanField()

    # Create an empty admin interface
    admin = Admin(title="Tutorials: Basic")
    

=== "ODMantic"

    python hl_lines="2 13"
    from odmantic import AIOEngine, Model
    from starlette_admin.contrib.odmantic import Admin

    engine = AIOEngine()

    class Todo(Model):
        title: str
        done: bool

    # Create an empty admin interface
    admin = Admin(engine, title="Tutorials: Basic")
    

### Adding a view for the Todo model

Now that the admin interface is initialized, the next step is to add a view for managing the 'Todo' model.

python
admin.add_view(ModelView(Todo))

In the code above, we use the function [add_view][starlette_admin.base.BaseAdmin.add_view] of
the [Admin][starlette_admin.base.BaseAdmin] class to include a view for
the 'Todo' model within the admin interface.

The [ModelView][starlette_admin.base.BaseAdmin.add_view] class allow you to add a dedicated set of admin pages for
managing any model.

!!! important

    Ensure to import 'ModelView' from the same package as the 'Admin' class, which varies based on the ORM/ODM you are
    using. For instance, if you are using SQLAlchemy, the import statement is as follows:

    python
    from starlette_admin.contrib.sqla import Admin, ModelView
    

## Mount 'admin' to your application

We can mount the 'admin' on a Starlette or FastAPI application by using
the [mount_to][starlette_admin.base.BaseAdmin.mount_to] function and passing the app instance:

=== "Starlette"

    python
    from starlette.applications import Starlette

    app = Startette()

    # Mount admin to your app
    admin.mount_to(app)
    

=== "FastAPI"

    python
    from fastapi import FastAPI

    app = FastAPI()

    # Mount admin to your app
    admin.mount_to(app)
    

## Full Code

Below is the complete code for the tutorial:

=== "SQLAlchemy"

    python
    from sqlalchemy import create_engine
    from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
    from starlette.applications import Starlette
    from starlette_admin.contrib.sqla import Admin, ModelView

    engine = create_engine("sqlite:///basic.db", connect_args={"check_same_thread": False})

    class Base(DeclarativeBase):
        pass

    class Todo(Base):
        __tablename__ = "todo"

        id: Mapped[int] = mapped_column(primary_key=True)
        title: Mapped[str]
        done: Mapped[bool]

    Base.metadata.create_all(engine)

    app = Starlette()  # or app = FastAPI()

    # Create an empty admin interface
    admin = Admin(engine, title="Tutorials: Basic")

    # Add view
    admin.add_view(ModelView(Todo, icon="fas fa-list"))

    # Mount admin to your app
    admin.mount_to(app)

    

=== "SQLModel"

    python
    from typing import Optional

    from sqlalchemy import create_engine
    from sqlmodel import Field, SQLModel
    from starlette.applications import Starlette
    from starlette_admin.contrib.sqlmodel import Admin, ModelView

    engine = create_engine("sqlite:///basic.db", connect_args={"check_same_thread": False})

    class Todo(SQLModel, table=True):
        id: Optional[int] = Field(default=None, primary_key=True)
        title: str
        done: bool

    SQLModel.metadata.create_all(engine)

    app = Starlette()  # or app = FastAPI()

    # Create an empty admin interface
    admin = Admin(engine, title="Tutorials: Basic")

    # Add view
    admin.add_view(ModelView(Todo, icon="fas fa-list"))

    # Mount admin to your app
    admin.mount_to(app)

    

=== "MongoEngine"

    python
    import mongoengine as db
    from mongoengine import connect, disconnect
    from starlette.applications import Starlette

    from starlette_admin.contrib.mongoengine import Admin, ModelView

    class Todo(db.Document):
        title = db.StringField()
        done = db.BooleanField()

    app = Starlette(
        on_startup=[lambda: connect("basic")],
        on_shutdown=[disconnect],
    )

    # Create an empty admin interface
    admin = Admin(title="Tutorials: Basic")

    # Add view
    admin.add_view(ModelView(Todo, icon="fas fa-list"))

    # Mount admin to your app
    admin.mount_to(app)

    

=== "ODMantic"

    python
    from odmantic import AIOEngine, Model
    from starlette.applications import Starlette
    from starlette_admin.contrib.odmantic import Admin, ModelView

    engine = AIOEngine()

    class Todo(Model):
        title: str
        done: bool

    app = Starlette()

    # Create an empty admin interface
    admin = Admin(engine, title="Tutorials: Basic")

    # Add views
    admin.add_view(ModelView(Todo, icon="fas fa-list"))

    # Mount app
    admin.mount_to(app)

    

## Run the server

We can now launch the server to make the admin interface available. This is done using the 'uvicorn' command:

shell
uvicorn main:app

The admin dashboard will be available at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

## Exploring the Admin interface

Let's take a tour of the admin interface autogenerated by Starlette-Admin and see it in action.

### Home Page

Navigate to the admin home page at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin). It should look something
like this:

![Home Page](../../assets/images/tutorials/basic/home_page.png)

The home page is empty right now except for the menu on the left. The menu has a single item called "Todos" that links
to the CRUD pages we generated for the Todo model.

!!! note

    We'll learn how to customize and add content to the home page later on.

### CRUD Pages

If you click on "Todos" in the menu, you'll be taken to the auto-generated CRUD pages for managing todo records.

#### Listing Page

This page lists the todo records

![List View](../../assets/images/tutorials/basic/list_full.png)

Let's go through some of the built-in functionality:

- **Search**

Type into the search box to filter records.

![Search](../../assets/images/tutorials/basic/fulltext_search.png)

- **Filter**

Click the button to filter by column values.

![Search Builder](../../assets/images/tutorials/basic/search_builder.png)

!!! warning

    Make sure to reset the filters when you are done

- **Show/Hide Columns**

Customize visible columns

![Show/Hide Columns](../../assets/images/tutorials/basic/show_hide_columns.png)

- **Delete**

Click the trash icon to delete a record.

![Delete](../../assets/images/tutorials/basic/delete.png)

- **Export**

Click Export and choose CSV or Excel.

![Export](../../assets/images/tutorials/basic/export.png)

#### Create a new todo item

From the listing page click on the button **New Todo** to navigate to the creation page

Fill the form and click **Save**. You'll be back on the list with the new Todo added.

![Create view](../../assets/images/tutorials/basic/create.png)

#### Edit an item

From the listing page click on the **Edit (pencil) icon** on an existing Todo.
Change the title and save. You'll see the updated title in the list.

![Edit view](../../assets/images/tutorials/basic/edit.png)

## Next Steps

You now have a basic admin interface for your Todo app.

Some next tutorials to continue learning:

- To be continued...

The final source code is available [on GitHub](https://github.com/jowilf/starlette-admin/tree/main/examples/tutorials/basic)

# Getting started

## Initialization

The first step is to initialize an empty admin interface for your app:

=== "SQLAlchemy"
    python
    from sqlalchemy import create_engine
    from starlette_admin.contrib.sqla import Admin

    engine = create_engine("sqlite:///test.db", connect_args={"check_same_thread": False})

    admin = Admin(engine)
    
=== "SQLModel"
    python
    from sqlalchemy import create_engine
    from starlette_admin.contrib.sqlmodel import Admin

    engine = create_engine("sqlite:///test.db", connect_args={"check_same_thread": False})

    admin = Admin(engine)
    
=== "MongoEngine"
    python
    from starlette_admin.contrib.mongoengine import Admin

    admin = Admin()
    
=== "ODMantic"
    python
    from odmantic import AIOEngine
    from starlette_admin.contrib.odmantic import Admin

    engine = AIOEngine()

    admin = Admin(engine)
    

## Adding Views

### ModelView

Model views allow you to add a dedicated set of admin pages for managing any model.

=== "SQLAlchemy"
    python hl_lines="2 10-11"
    from sqlalchemy import create_engine
    from starlette_admin.contrib.sqla import Admin, ModelView

    from .models import User, Post

    engine = create_engine("sqlite:///test.db", connect_args={"check_same_thread": False})

    admin = Admin(engine)

    admin.add_view(ModelView(User))
    admin.add_view(ModelView(Post))

    
=== "SQLModel"
    python hl_lines="2 10-11"
    from sqlalchemy import create_engine
    from starlette_admin.contrib.sqlmodel import Admin, ModelView

    from .models import User, Post

    engine = create_engine("sqlite:///test.db", connect_args={"check_same_thread": False})

    admin = Admin(engine)

    admin.add_view(ModelView(User))
    admin.add_view(ModelView(Post))

    
=== "MongoEngine"
    python hl_lines="1 7-8"
    from starlette_admin.contrib.mongoengine import Admin, ModelView

    from .models import Post, User

    admin = Admin()

    admin.add_view(ModelView(User))
    admin.add_view(ModelView(Post))

    
=== "ODMantic"
    python hl_lines="2 10-11"
    from odmantic import AIOEngine
    from starlette_admin.contrib.odmantic import Admin, ModelView

    from .models import Post, User

    engine = AIOEngine()

    admin = Admin(engine)

    admin.add_view(ModelView(User))
    admin.add_view(ModelView(Post))

    
This gives you a set of fully featured CRUD views for your model:

- A *list view*, with support for searching, sorting, filtering, and deleting records.
- A *create view* for adding new records.
- An *edit view* for updating existing records.
- A read-only *details view*.

### CustomView

With [CustomView][starlette_admin.views.CustomView] you can add your own views (not tied to any particular model). For example,
a custom home page that displays some analytics data.

python
from starlette_admin import CustomView

admin.add_view(CustomView(label="Home", icon="fa fa-home", path="/home", template_path="home.html"))

To have a full control of the rendering, override the 'render' methods

python
from starlette.requests import Request
from starlette.responses import Response
from starlette.templating import Jinja2Templates
from starlette_admin import CustomView

class HomeView(CustomView):
    async def render(self, request: Request, templates: Jinja2Templates) -> Response:
        return templates.TemplateResponse(
            request,
            name="home.html",
            context={"latest_posts": ..., "top_users": ...},
        )

admin.add_view(HomeView(label="Home", icon="fa fa-home", path="/home"))

### Link

Use [Link][starlette_admin.views.Link] to add arbitrary hyperlinks to the menu

python
from starlette_admin.views import Link

admin.add_view(Link(label="Home Page", icon="fa fa-link", url="/"))

### DropDown

Use [DropDown][starlette_admin.views.DropDown] to group views together in menu structure

python
from starlette_admin import CustomView, DropDown
from starlette_admin.contrib.sqla import ModelView
from starlette_admin.views import Link

from .models import User

admin.add_view(
    DropDown(
        "Resources",
        icon="fa fa-list",
        views=[
            ModelView(User),
            Link(label="Home Page", url="/"),
            CustomView(label="Dashboard", path="/dashboard", template_path="dashboard.html"),
        ],
    )
)

## Mount admin to your app

The last step is to mount the admin interfaces to your app

=== "SQLAlchemy"
    python hl_lines="2 9 16"
    from sqlalchemy import create_engine
    from starlette.applications import Starlette
    from starlette_admin.contrib.sqla import Admin, ModelView

    from .models import Post, User

    engine = create_engine("sqlite:///test.db", connect_args={"check_same_thread": False})

    app = Starlette() # FastAPI()

    admin = Admin(engine)

    admin.add_view(ModelView(User))
    admin.add_view(ModelView(Post))

    admin.mount_to(app)

    
=== "SQLModel"
    python hl_lines="2 9 16"
    from sqlalchemy import create_engine
    from starlette.applications import Starlette
    from starlette_admin.contrib.sqlmodel import Admin, ModelView

    from .models import Post, User

    engine = create_engine("sqlite:///test.db", connect_args={"check_same_thread": False})

    app = Starlette()  # FastAPI()

    admin = Admin(engine)

    admin.add_view(ModelView(User))
    admin.add_view(ModelView(Post))

    admin.mount_to(app)

    
=== "MongoEngine"
    python hl_lines="1 6 13"
    from starlette.applications import Starlette
    from starlette_admin.contrib.mongoengine import Admin, ModelView

    from .models import Post, User

    app = Starlette()  # FastAPI()

    admin = Admin()

    admin.add_view(ModelView(User))
    admin.add_view(ModelView(Post))

    admin.mount_to(app)
    
=== "ODMantic"
    python hl_lines="2 9 16"
    from odmantic import AIOEngine
    from starlette.applications import Starlette
    from starlette_admin.contrib.odmantic import Admin, ModelView

    from .models import Post, User

    engine = AIOEngine()

    app = Starlette()  # FastAPI()

    admin = Admin(engine)

    admin.add_view(ModelView(User))
    admin.add_view(ModelView(Post))

    admin.mount_to(app)
    

You can now access your admin interfaces in your browser at [http://localhost:8000/admin](http://localhost:8000/admin)

# Admin Configurations

Multiple options are available to customize your admin interface

python
admin = Admin(
    title="SQLModel Admin",
    base_url="/admin",
    route_name="admin",
    statics_dir="statics/admin",
    templates_dir="templates/admin",
    logo_url="'https'://preview.tabler.io/static/logo-white.svg",
    login_logo_url="'https'://preview.tabler.io/static/logo.svg",
    index_view=CustomView(label="Home", icon="fa fa-home", path="/home", template_path="home.html"),
    auth_provider=MyAuthProvider(login_path="/sign-in", logout_path="/sign-out"),
    middlewares=[],
    debug=False,
    i18n_config = I18nConfig(default_locale="en")
)

## Parameters

* 'title': Admin title.
* 'base_url': Base URL for Admin interface.
* 'route_name': Mounted Admin name
* 'logo_url': URL of logo to be displayed instead of title.
* 'login_logo_url': If set, it will be used for login interface instead of logo_url.
* 'statics_dir': Templates dir for static files customisation
* 'templates_dir': Templates dir for customisation
* 'index_view': CustomView to use for index page.
* 'auth_provider': Authentication Provider
* 'middlewares': Starlette middlewares
* 'i18n_config': i18n config for your admin interface

# ModelView Configurations

There are multiple options available to customize your ModelView. For a complete list, please refer to the API
documentation for [BaseModelView()][starlette_admin.views.BaseModelView].

Here are some of the most commonly used options:

## Fields

You can use the 'fields' property of the ModelView class to customize which fields are included in the admin view.

python hl_lines="21"
from sqlalchemy import JSON, Column, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from starlette.applications import Starlette
from starlette_admin import TagsField
from starlette_admin.contrib.sqla import Admin, ModelView

Base = declarative_base()
engine = create_engine("sqlite:///test.db", connect_args={"check_same_thread": False})

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    tags = Column(JSON)
    content = Column(Text)

class PostView(ModelView):
    fields = ["id", "title", Post.content, TagsField("tags", label="Tags")]

app = Starlette()

admin = Admin(engine)
admin.add_view(PostView(Post, icon="fa fa-blog"))
admin.mount_to(app)

## Exclusions

There are several options available for customizing which fields are displayed in different parts of the admin
view. These options include:

* 'exclude_fields_from_list': List of fields to exclude from the List page.
* 'exclude_fields_from_detail': List of fields to exclude from the Detail page.
* 'exclude_fields_from_create': List of fields to exclude from the creation page.
* 'exclude_fields_from_edit': List of fields to exclude from the editing page.\

python
class PostView(ModelView):
    exclude_fields_from_list = [Post.content, Post.tags]

!!! note

    For more advanced use cases, you can override
    the [ModelView.get_fields_list()][starlette_admin.views.BaseModelView.get_fields_list] function.

## Searching & Sorting

Several options are available to specify which fields can be sorted or searched.

* 'searchable_fields' for list of searchable fields
* 'sortable_fields' for list of orderable fields
* 'fields_default_sort' for initial order (sort) to apply to the table

!!! Usage

    python
    class PostView(ModelView):
        sortable_fields = [Post.id, "title"]
        searchable_fields = [Post.id, Post.title, "tags"]
        fields_default_sort = ["title", ("price", True)]
    

## Exporting

One of the powerful features of Starlette-admin is the ability to export data from the list page.

You can specify the export options for each ModelView using the following attributes:

* 'export_fields':  List of fields to include in the export.
* 'export_types': A list of available export filetypes. Available
  exports are '['csv', 'excel', 'pdf', 'print']'. By default, only 'pdf' is disabled.

!!! Example

    python
    from starlette_admin import ExportType

    class PostView(ModelView):
        export_fields = [Post.id, Post.content, Post.tags]
        export_types = [ExportType.CSV, ExportType.EXCEL]
    

## Pagination

The pagination options in the list page can be configured. The available options are:

* 'page_size': Default number of items to display in List page pagination.
            Default value is set to '10'.
* 'page_size_options': Pagination choices displayed in List page.  Default value is set to '[10, 25, 50, 100]'.
     Use '-1'to display All

!!! Example

    python
    class PostView(ModelView):
        page_size = 5
        page_size_options = [5, 10, 25, 50, -1]
    

## Templates
The template files are built using Jinja2 and can be completely overridden in the configurations. The pages available are:

* 'list_template': List view template. Default is 'list.html'.
* 'detail_template': Details view template. Default is 'detail.html'.
* 'create_template': Edit view template. Default is 'create.html'.
* 'edit_template': Edit view template. Default is 'edit.html'.

!!! Example

    python
    class PostView(ModelView):
        detail_template = "post_detail.html"
    

## Datatables Extensions

*starlette-admin* includes some datatable extensions by default. You can disable any of these extensions
in your 'ModelView' by overridden following options:

* 'column_visibility': Enable/Disable [column visibility](https://datatables.net/extensions/buttons/built-in#Column-visibility) extension
* 'search_builder': Enable/Disable [search builder](https://datatables.net/extensions/searchbuilder/) extension
* 'responsive_table': Enable/Disable [responsive](https://datatables.net/extensions/responsive/) extension
* 'save_state': Enable/Disable [state saving](https://datatables.net/examples/basic_init/state_save.html)

!!! Example

    python
    class PostView(ModelView):
        column_visibility = False
        search_builder = False
        responsive_table = True
        save_state = True
    

## Object Representation

*starlette-admin* provides two methods for customizing how objects are represented in the admin interface:

### '__admin_repr__'

It is a special method that can be defined in a model class to customize the object representation in the admin
interface. By default, only the value of the object's primary key attribute is displayed. However, by implementing
'__admin_repr__', you can return a string that better represents the object in the admin interface.

!!! Example

    For example, the following implementation for a 'User' model will display the user's full name instead of their primary
    key in the admin interface:

    python
    class User:
        id: int
        first_name: str
        last_name: str

        async def __admin_repr__(self, request: Request):
            return f"{self.last_name} {self.first_name}"
    

    ![Custom Object representation](../../../images/tutorial/configurations/modelview/object_text_representation.png){ width="200" }

### '__admin_select2_repr__'

This method is similar to '__admin_repr__', but it returns an HTML string that is used to display the object in
a 'select2' widget. By default, all the object's attributes allowed for detail page are used except relation and file
fields.

!!! note

    The returned value should be valid HTML.

!!! danger

    Escape your database value to avoid Cross-Site Scripting (XSS) attack.
    You can use Jinja2 Template render with 'autoescape=True'.
    For more information, visit [OWASP website](https://owasp.org/www-community/attacks/xss/)
    python
    from jinja2 import Template
    Template("Hello {{name}}", autoescape=True).render(name=name)
    

!!! Example

    Here is an example implementation for a 'User' model that includes the user's name and photo:

    python
    class User:
        id: int
        name: str
        photo_url: str

        async def __admin_select2_repr__(self, request: Request) -> str:
            return f''
    

    ![Custom Select2 rendering](../../../images/tutorial/configurations/modelview/select2_customization.png){ width="300" }

## Hooks

Hooks are callback functions that give you an easy way to customize and extend the default CRUD functions. You can use
hooks to perform actions before or after specific operations such as item creation, editing, or deletion.

The following hooks are available:

- [before_create(request, data, obj)][starlette_admin.views.BaseModelView.before_create]: Called before a new object is
  created

- [after_create(request, obj)][starlette_admin.views.BaseModelView.after_create]: Called after a new object is created

- [before_edit(request, data, obj)][starlette_admin.views.BaseModelView.before_edit]: Called before an existing object is
  updated

- [after_edit(request, obj)][starlette_admin.views.BaseModelView.after_edit]: Called after an existing object is updated

- [before_delete(request, obj)][starlette_admin.views.BaseModelView.before_delete]:  Called before an object is deleted

- [after_delete(request, obj)][starlette_admin.views.BaseModelView.after_delete]: Called after an object is deleted

### Example

python
class OrderView(ModelView):
    async def after_create(self, request: Request, order: Order):
        analytics.track_order_created(order)

# Forms Validations

Starlette-admin is designed to be flexible and agnostic to your specific database backend. Therefore, it doesn't include
built-in data validation capabilities. Instead, data validation will depend on the validation mechanisms provided by
your chosen database backend.

## SQLAlchemy

There are several options available for validating your data:

### Pydantic

[Pydantic](https://github.com/pydantic/pydantic) is a widely used Python library that provides data validation
capabilities using Python's type hints.

To automatically validate submitted data with Pydantic, you only need to define a Pydantic model and
use 'starlette_admin.contrib.sqla.ext.pydantic.ModelView'

!!! Example

    python
    from starlette_admin.contrib.sqla.ext.pydantic import ModelView

    class Post(Base):
        __tablename__ = "posts"

        id = Column(Integer, primary_key=True)
        title = Column(String)
        content = Column(Text)
        views = Column(Integer)

    class PostIn(BaseModel):
        id: Optional[int] = Field(primary_key=True)
        title: str = Field(min_length=3)
        content: str = Field(min_length=10)
        views: int = Field(multiple_of=4)

        @validator("title")
        def title_must_contain_space(cls, v):
            if " " not in v.strip():
                raise ValueError("title must contain a space")
            return v.title()

    # Add view
    admin.add_view(ModelView(Post, pydantic_model=PostIn))

    

### Custom Validation

You can also create your own validation functions to enforce specific data requirements.

!!! Example

    python
    from starlette_admin.contrib.sqla import ModelView
    from starlette_admin.exceptions import FormValidationError

    class PostView(ModelView):

        async def validate(self, request: Request, data: Dict[str, Any]) -> None:
            """Raise FormValidationError to display error in forms"""
            errors: Dict[str, str] = dict()
            _2day_from_today = date.today() + timedelta(days=2)
            if data["title"] is None or len(data["title"]) < 3:
                errors["title"] = "Ensure this value has at least 03 characters"
            if data["text"] is None or len(data["text"]) < 10:
                errors["text"] = "Ensure this value has at least 10 characters"
            if data["date"] is None or data["date"] < _2day_from_today:
                errors["date"] = "We need at least one day to verify your post"
            if data["publisher"] is None:
                errors["publisher"] = "Publisher is required"
            if data["tags"] is None or len(data["tags"]) < 1:
                errors["tags"] = "At least one tag is required"
            if len(errors) > 0:
                raise FormValidationError(errors)
            return await super().validate(request, data)
    

    ![SQLAlchemy Form Validations](../../images/validations/sqla.png)

??? info

    Full example available [here](https://github.com/jowilf/starlette-admin/tree/main/examples/sqla)

## SQLModel

With SQLModel, validating your data is made easy. Once you've defined your model, any data submitted to it will be
automatically validated.

!!! Example

    python
    from sqlmodel import SQLModel, Field
    from pydantic import validator

    class Post(SQLModel, table=True):
        id: Optional[int] = Field(primary_key=True)
        title: str = Field()
        content: str = Field(min_length=10)
        views: int = Field(multiple_of=4)

        @validator('title')
        def title_must_contain_space(cls, v):
            if ' ' not in v:
                raise ValueError('title must contain a space')
            return v.title()
    

    ![SQLModel Form Validations](../../images/validations/sqlmodel.png)

??? info

    Full example available [here](https://github.com/jowilf/starlette-admin/tree/main/examples/sqlmodel)

## Odmantic

Validation of submitted data is handled seamlessly by Odmantic. Any data that you submit to your defined model will be
validated automatically.

!!! Example

    python
    from typing import List, Optional

    from odmantic import EmbeddedModel, Field, Model
    from pydantic import EmailStr

    class Address(EmbeddedModel):
        street: str = Field(min_length=3)
        city: str = Field(min_length=3)
        state: Optional[str]
        zipcode: Optional[str]

    class Author(Model):
        first_name: str = Field(min_length=3)
        last_name: str = Field(min_length=3)
        email: Optional[EmailStr]
        addresses: List[Address] = Field(default_factory=list)

    

    ![SQLModel Form Validations](../../images/validations/odmantic.png)

??? info

    Full example available [here](https://github.com/jowilf/starlette-admin/tree/main/examples/odmantic)

## MongoEngine

The submitted data will be automatically validated according to your model definition.

!!! Example

    python
    import mongoengine as db

    class Comment(db.EmbeddedDocument):
        name = db.StringField(min_length=3, max_length=20, required=True)
        value = db.StringField(max_length=20)

    class Post(db.Document):
        name = db.StringField(max_length=20, required=True)
        value = db.StringField(max_length=20)
        inner = db.ListField(db.EmbeddedDocumentField(Comment))
        lols = db.ListField(db.StringField(max_length=20))
    

    ![SQLModel Form Validations](../../images/validations/mongoengine.png)

??? info

    Full example available [here](https://github.com/jowilf/starlette-admin/tree/main/examples/mongoengine)

# Authentication & Authorization

To protect your admin interface from unwanted users, you can create an Authentication Provider by extending
the [AuthProvider][starlette_admin.auth.AuthProvider] class and set 'auth_provider' when declaring your admin app

## Username and Password Authentication

By default, [AuthProvider][starlette_admin.auth.AuthProvider] provides a login form with 'username' and 'password'
fields for basic username and password authentication. To fully support this authentication method, you need to
implement the following methods in your custom Authentication Provider:

* [is_authenticated][starlette_admin.auth.BaseAuthProvider.is_authenticated]: This method will be called to validate
  each incoming request.
* [get_admin_user][starlette_admin.auth.BaseAuthProvider.get_admin_user]: Return connected user 'name' and/or 'avatar'
* [get_admin_config][starlette_admin.auth.BaseAuthProvider.get_admin_config]: Return 'logo_url' or 'app_title' according to connected user or any other condition.
* [login][starlette_admin.auth.AuthProvider.login]: will be called to validate user credentials.
* [logout][starlette_admin.auth.AuthProvider.logout]: Will be called to logout (clear sessions, cookies, ...)

python
from starlette.requests import Request
from starlette.responses import Response
from starlette_admin.auth import AdminConfig, AdminUser, AuthProvider
from starlette_admin.exceptions import FormValidationError, LoginFailed

users = {
    "admin": {
        "name": "Admin",
        "avatar": "admin.png",
        "company_logo_url": "admin.png",
        "roles": ["read", "create", "edit", "delete", "action_make_published"],
    },
    "johndoe": {
        "name": "John Doe",
        "avatar": None, # user avatar is optional
        "roles": ["read", "create", "edit", "action_make_published"],
    },
    "viewer": {"name": "Viewer", "avatar": "guest.png", "roles": ["read"]},
}

class UsernameAndPasswordProvider(AuthProvider):
    """
    This is only for demo purpose, it's not a better
    way to save and validate user credentials
    """

    async def login(
        self,
        username: str,
        password: str,
        remember_me: bool,
        request: Request,
        response: Response,
    ) -> Response:
        if len(username) < 3:
            """Form data validation"""
            raise FormValidationError(
                {"username": "Ensure username has at least 03 characters"}
            )

        if username in users and password == "password":
            """Save 'username' in session"""
            request.session.update({"username": username})
            return response

        raise LoginFailed("Invalid username or password")

    async def is_authenticated(self, request) -> bool:
        if request.session.get("username", None) in users:
            """
            Save current 'user' object in the request state. Can be used later
            to restrict access to connected user.
            """
            request.state.user = users.get(request.session["username"])
            return True

        return False

    def get_admin_config(self, request: Request) -> AdminConfig:
        user = request.state.user  # Retrieve current user
        # Update app title according to current_user
        custom_app_title = "Hello, " + user["name"] + "!"
        # Update logo url according to current_user
        custom_logo_url = None
        if user.get("company_logo_url", None):
            custom_logo_url = request.url_for("static", path=user["company_logo_url"])
        return AdminConfig(
            app_title=custom_app_title,
            logo_url=custom_logo_url,
        )

    def get_admin_user(self, request: Request) -> AdminUser:
        user = request.state.user  # Retrieve current user
        photo_url = None
        if user["avatar"] is not None:
            photo_url = request.url_for("static", path=user["avatar"])
        return AdminUser(username=user["name"], photo_url=photo_url)

    async def logout(self, request: Request, response: Response) -> Response:
        request.session.clear()
        return response

For a working example, have a look
at ['https://github.com/jowilf/starlette-admin/tree/main/examples/auth'](https://github.com/jowilf/starlette-admin/tree/main/examples/auth)

## Custom Authentication flow (OAuth2/OIDC, ...)

If you prefer to use a custom authentication flow, such as OAuth2 or OIDC, you can implement the following methods in
your custom Authentication Provider:

* [is_authenticated][starlette_admin.auth.BaseAuthProvider.is_authenticated]: This method will be called to validate each incoming request.
* [get_admin_user][starlette_admin.auth.BaseAuthProvider.get_admin_user]: Return connected user 'name' and/or 'profile'
* [render_login][starlette_admin.auth.AuthProvider.render_login]: Override the default behavior to render a custom login page.
* [render_logout][starlette_admin.auth.AuthProvider.render_logout]: Implement the custom logout logic.

Additionally, you can override these methods depending on your needs:

* [get_middleware][starlette_admin.auth.BaseAuthProvider.get_middleware]: To provide a custom authentication middleware
  for the admin interface
* [setup_admin][starlette_admin.auth.BaseAuthProvider.setup_admin]: This method is called during the setup process of
  the admin interface and allows for custom configuration and setup.

python
from typing import Optional

from starlette.datastructures import URL
from starlette.requests import Request
from starlette.responses import RedirectResponse, Response
from starlette.routing import Route
from starlette_admin import BaseAdmin
from starlette_admin.auth import (
    AdminUser,
    AuthProvider,
    login_not_required,
)

from authlib.integrations.starlette_client import OAuth

from .config import AUTH0_CLIENT_ID, AUTH0_CLIENT_SECRET, AUTH0_DOMAIN

oauth = OAuth()
oauth.register(
    "auth0",
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{AUTH0_DOMAIN}/.well-known/openid-configuration",
)

class MyAuthProvider(AuthProvider):
    async def is_authenticated(self, request: Request) -> bool:
        if request.session.get("user", None) is not None:
            request.state.user = request.session.get("user")
            return True
        return False

    def get_admin_user(self, request: Request) -> Optional[AdminUser]:
        user = request.state.user
        return AdminUser(
            username=user["name"],
            photo_url=user["picture"],
        )

    async def render_login(self, request: Request, admin: BaseAdmin):
        """Override the default login behavior to implement custom logic."""
        auth0 = oauth.create_client("auth0")
        redirect_uri = request.url_for(
            admin.route_name + ":authorize_auth0"
        ).include_query_params(next=request.query_params.get("next"))
        return await auth0.authorize_redirect(request, str(redirect_uri))

    async def render_logout(self, request: Request, admin: BaseAdmin) -> Response:
        """Override the default logout to implement custom logic"""
        request.session.clear()
        return RedirectResponse(
            url=URL(f"https://{AUTH0_DOMAIN}/v2/logout").include_query_params(
                returnTo=request.url_for(admin.route_name + ":index"),
                client_id=AUTH0_CLIENT_ID,
            )
        )

    @login_not_required
    async def handle_auth_callback(self, request: Request):
        auth0 = oauth.create_client("auth0")
        token = await auth0.authorize_access_token(request)
        request.session.update({"user": token["userinfo"]})
        return RedirectResponse(request.query_params.get("next"))

    def setup_admin(self, admin: "BaseAdmin"):
        super().setup_admin(admin)
        """add custom authentication callback route"""
        admin.routes.append(
            Route(
                "/auth0/authorize",
                self.handle_auth_callback,
                methods=["GET"],
                name="authorize_auth0",
            )
        )

For a working example, have a look
at ['https://github.com/jowilf/starlette-admin/tree/main/examples/authlib'](https://github.com/jowilf/starlette-admin/tree/main/examples/authlib)

The AuthProvider can be added at your admin interface as follows:

python
admin = Admin(
    engine,
    title="Example: Authentication",
    auth_provider=MyAuthProvider(),
    middlewares=[Middleware(SessionMiddleware, secret_key=SECRET)],
)

## Authorization

### For all views

Each [view][starlette_admin.views.BaseView] implement [is_accessible][starlette_admin.views.BaseView.is_accessible] method which can be used to restrict access
to current user.

python
from starlette_admin import CustomView
from starlette.requests import Request

class ReportView(CustomView):

    def is_accessible(self, request: Request) -> bool:
        return "admin" in request.state.user["roles"]

!!! important

    When view is inaccessible, it does not appear in menu structure

### For [ModelView][starlette_admin.views.BaseModelView]

In [ModelView][starlette_admin.views.BaseModelView], you can override the following methods to restrict access to
the current connected user.

* 'can_view_details': Permission for viewing full details of Items
* 'can_create': Permission for creating new Items
* 'can_edit': Permission for editing Items
* 'can_delete': Permission for deleting Items
* 'is_action_allowed':  verify if the action with 'name' is allowed.
* 'is_row_action_allowed':  verify if the row action with 'name' is allowed.

python
from starlette_admin.contrib.sqla import ModelView
from starlette.requests import Request
from starlette_admin import action, row_action

class ArticleView(ModelView):
    exclude_fields_from_list = [Article.body]

    def can_view_details(self, request: Request) -> bool:
        return "read" in request.state.user["roles"]

    def can_create(self, request: Request) -> bool:
        return "create" in request.state.user["roles"]

    def can_edit(self, request: Request) -> bool:
        return "edit" in request.state.user["roles"]

    def can_delete(self, request: Request) -> bool:
        return "delete" in request.state.user["roles"]

    async def is_action_allowed(self, request: Request, name: str) -> bool:
        if name == "make_published":
            return "action_make_published" in request.state.user["roles"]
        return await super().is_action_allowed(request, name)

    async def is_row_action_allowed(self, request: Request, name: str) -> bool:
        if name == "make_published":
            return "row_action_make_published" in request.state.user["roles"]
        return await super().is_row_action_allowed(request, name)

    @action(
        name="make_published",
        text="Mark selected articles as published",
        confirmation="Are you sure you want to mark selected articles as published ?",
        submit_btn_text="Yes, proceed",
        submit_btn_class="btn-success",
    )
    async def make_published_action(self, request: Request, pks: List[Any]) -> str:
        ...
        return "{} articles were successfully marked as published".format(len(pks))

    @row_action(
        name="make_published",
        text="Mark as published",
        confirmation="Are you sure you want to mark this article as published ?",
        icon_class="fas fa-check-circle",
        submit_btn_text="Yes, proceed",
        submit_btn_class="btn-success",
        action_btn_class="btn-info",
    )
    async def make_published_row_action(self, request: Request, pk: Any) -> str:
        ...
        return "The article was successfully marked as published"

# Managing files

*Starlette-Admin* has out-of-the-box support for [SQLAlchemy-file](https://github.com/jowilf/sqlalchemy-file) and Gridfs through Mongoengine FileField & ImageField

## SQLAlchemy & SQLModel

All you need is to add ImageField or FileField from [SQLAlchemy-file](https://github.com/jowilf/sqlalchemy-file) to your model

python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy_file import FileField, ImageField
from starlette_admin.contrib.sqla import ModelView

Base = declarative_base()

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(50), unique=True)
    cover = Column(ImageField(thumbnail_size=(128, 128)))
    content = Column(FileField)

class BookView(ModelView):
    pass

admin.add_view(BookView(Book))

!!! note

    You can also use 'multiple=True' to save multiple files.

## MongoEngine

*Starlette-Admin* support ImageField and FileField

python
from mongoengine import Document, FileField, ImageField, StringField
from starlette_admin.contrib.mongoengine import ModelView

class Book(Document):
    title = StringField(max_length=50)
    cover = ImageField(thumbnail_size=(128, 128))
    content = FileField()

class BookView(ModelView):
    pass

admin.add_view(BookView(Book))

# Actions

In starlette-admin, actions provide an easy way to interact with your database records and
perform various operations such as mass delete, special mass updates, sending emails, etc.

## Batch Actions

By default, to update an object, you must select it in the list page and update it. This works well for a majority of
use cases. However, if you need to make the same change to many objects at once, this workflow can be quite tedious.

In these cases, you can write a *custom batch action* to bulk update many objects at once.

!!! note

    *starlette-admin* add by default an action named 'delete' to delete many object at once

To add other batch actions to your [ModelView][starlette_admin.views.BaseModelView], besides the default delete action,
you can define a
function that implements the desired logic and wrap it with the [@action][starlette_admin.actions.action] decorator (
Heavily inspired by Flask-Admin).

!!! warning

    The batch action name should be unique within a ModelView.

### Example

python
from typing import List, Any

from starlette.datastructures import FormData
from starlette.requests import Request
from starlette.responses import RedirectResponse, Response

from starlette_admin import action
from starlette_admin.contrib.sqla import ModelView
from starlette_admin.exceptions import ActionFailed

class ArticleView(ModelView):
    actions = ["make_published", "redirect", "delete"]  # 'delete' function is added by default

    @action(
        name="make_published",
        text="Mark selected articles as published",
        confirmation="Are you sure you want to mark selected articles as published ?",
        submit_btn_text="Yes, proceed",
        submit_btn_class="btn-success",
        form="""
        <form>
            
        </form>
        """,
    )
    async def make_published_action(self, request: Request, pks: List[Any]) -> str:
        # Write your logic here

        data: FormData = await request.form()
        user_input = data.get("example-text-input")

        if ...:
            # Display meaningfully error
            raise ActionFailed("Sorry, We can't proceed this action now.")
        # Display successfully message
        return "{} articles were successfully marked as published".format(len(pks))

    # For custom response
    @action(
        name="redirect",
        text="Redirect",
        custom_response=True,
        confirmation="Fill the form",
        form='''
        <form>
            
        </form>
        '''
    )
    async def redirect_action(self, request: Request, pks: List[Any]) -> Response:
        data = await request.form()
        return RedirectResponse(f"https://example.com/?value={data['value']}")

## Row actions

Row actions allow you to perform actions on individual items within a list view.

!!! note

    By default, starlette-admin includes three (03) row actions

    - 'view': redirects to the item's detail page
    - 'edit': redirects to the item's edit page
    - 'delete': deletes the selected item

To add other row actions to your [ModelView][starlette_admin.views.BaseModelView], besides the default ones, you can
define a function that implements the desired logic and wrap it with
the [@row_action][starlette_admin.actions.row_action] decorator

For cases where a row action should simply navigate users to a website or internal page, it is preferable to
use the [@link_row_action][starlette_admin.actions.link_row_action] decorator. The key difference is
that 'link_row_action'
eliminates the need to call the action API. Instead, the link is included directly in the href attribute of the
generated html element (e.g. '<a href='https://example.com/?pk=4' ...>').

!!! warning

    The row actions (both [@row_action][starlette_admin.actions.row_action]
    and [@link_row_action][starlette_admin.actions.link_row_action]) name should be unique within a ModelView.

### Example

python
from typing import Any

from starlette.datastructures import FormData
from starlette.requests import Request

from starlette_admin._types import RowActionsDisplayType
from starlette_admin.actions import link_row_action, row_action
from starlette_admin.contrib.sqla import ModelView
from starlette_admin.exceptions import ActionFailed

class ArticleView(ModelView):
    ...
    row_actions = ["view", "edit", "go_to_example", "make_published",
                   "delete"]  # edit, view and delete are provided by default
    row_actions_display_type = RowActionsDisplayType.ICON_LIST  # RowActionsDisplayType.DROPDOWN

    @row_action(
        name="make_published",
        text="Mark as published",
        confirmation="Are you sure you want to mark this article as published ?",
        icon_class="fas fa-check-circle",
        submit_btn_text="Yes, proceed",
        submit_btn_class="btn-success",
        action_btn_class="btn-info",
        form="""
        <form>
            
        </form>
        """,
    )
    async def make_published_row_action(self, request: Request, pk: Any) -> str:
        # Write your logic here

        data: FormData = await request.form()
        user_input = data.get("example-text-input")

        if ...:
            # Display meaningfully error
            raise ActionFailed("Sorry, We can't proceed this action now.")
        # Display successfully message
        return "The article was successfully marked as published"

    @link_row_action(
        name="go_to_example",
        text="Go to example.com",
        icon_class="fas fa-arrow-up-right-from-square",
    )
    def go_to_example_row_action(self, request: Request, pk: Any) -> str:
        return f"https://example.com/?pk={pk}"

### List rendering

The 'RowActionsDisplayType' enum provides options for customizing how row actions are displayed in the list view.

#### RowActionsDisplayType.ICON_LIST

python hl_lines="5"
from starlette_admin._types import RowActionsDisplayType

class ArticleView(ModelView):
    row_actions_display_type = RowActionsDisplayType.ICON_LIST

#### RowActionsDisplayType.DROPDOWN

python hl_lines="5"
from starlette_admin._types import RowActionsDisplayType

class ArticleView(ModelView):
    row_actions_display_type = RowActionsDisplayType.DROPDOWN

# Multiple Admin

You can add multiple admin to your app with different or same views. To manage this, simply use different 'base_url'
and 'route_name'

python
from starlette.applications import Starlette
from starlette_admin import BaseAdmin as Admin
from starlette_admin.contrib.sqla import ModelView

app = Starlette()

admin1 = Admin(
    "Admin1", base_url="/admin1", route_name="admin1", templates_dir="templates/admin1"
)
admin1.add_view(ModelView(Report))
admin1.add_view(ModelView(Post))
admin1.mount_to(app)

admin2 = Admin(
    "Admin2", base_url="/admin2", route_name="admin2", templates_dir="templates/admin2"
)
admin2.add_view(ModelView(Post))
admin2.add_view(ModelView(User))
admin2.mount_to(app)

assert app.url_path_for("admin1:index") == "/admin1/"
assert app.url_path_for("admin2:index") == "/admin2/"

# Custom Field

*Starlette-Admin* has a lot of built-in [fields][starlette_admin.fields.BaseField] available. But you can override or create your own field
according to your need.

!!! important

    Before creating a new field, try first to extend the existing ones. They are flexible enough to fit most use cases.

The first step is to define a new class, which derives from [BaseField][starlette_admin.fields.BaseField] or any others fields to customize it

python
from starlette_admin import BaseField
from dataclasses import dataclass

@dataclass
class CustomField(BaseField):
    pass

## List Rendering

*Starlette-Admin* use [Datatables](https://datatables.net/) to render list. By default all fields will be render as text field.
To customize this behavior you need to write a javascript function to
render your column inside datatable instance. For more information on how to write your function
read [Datatables documentation](https://datatables.net/reference/option/columns.render).

* First, you need to provide a link to your custom javascript file in which you add additional render function, by overriding
the admin class

!!! Example

    This is simple example with SQLAlchemy backend

    python
    from starlette_admin.contrib.sqla import Admin as BaseAdmin

    class Admin(BaseAdmin):
        def custom_render_js(self, request: Request) -> Optional[str]:
            return request.url_for("statics", path="js/custom_render.js")

    admin = Admin(engine)
    admin.add_view(...)
    

    js title="statics/js/custom_render.js"
    Object.assign(render, {
      mycustomkey: function render(data, type, full, meta, fieldOptions) {
            ...
      },
    });
    

!!! note

    'fieldOptions' is your field as javascript object. Your field attributes is serialized into
    javascript object by using dataclass 'asdict' function.

* Then, set 'render_function_key' value

python
from starlette_admin import BaseField
from dataclasses import dataclass

@dataclass
class CustomField(BaseField):
    render_function_key: str = "mycustomkey"

## Form

For form rendering, you should create a new html file under the directory 'forms' in your templates dir.

These jinja2 variables are available:

* 'field': Your field instance
* 'error': Error message coming from 'FormValidationError'
* 'data': current value. Will be available if it is edit or when validation error occur
* 'action': 'EDIT' or 'CREATE'

!!! Example

    html title="forms/custom.html"
    
    {%if error %}
    
    {%endif%}
    

python
from starlette_admin import BaseField
from dataclasses import dataclass

@dataclass
class CustomField(BaseField):
    render_function_key: str = "mycustomkey"
    form_template: str = "forms/custom.html"

## Detail Page

To render your field on detail page, you should create a new html file under the directory 'displays' in your template dir.

These jinja2 variables are available:

* 'field': Your field instance
* 'data': value to display

!!! Example

    html title="displays/custom.html"
    <span>Hello {{data}}</span>
    

python
from starlette_admin import BaseField
from dataclasses import dataclass

@dataclass
class CustomField(BaseField):
    render_function_key: str = "mycustomkey"
    form_template: str = "forms/custom.html"
    display_template: str = "displays/custom.html"

## Data processing

For data processing you will need to override two functions:

* 'process_form_data':  Will be call when converting field value into python dict object
* 'serialize_field_value': Will be call when serializing value to send through the API. This is the same data
you will get in your *render* function

python
from dataclasses import dataclass
from typing import Any, Dict

from requests import Request
from starlette.datastructures import FormData
from starlette_admin import BaseField

@dataclass
class CustomField(BaseField):
    render_function_key: str = "mycustomkey"
    form_template: str = "forms/custom.html"
    display_template: str = "displays/custom.html"

    async def parse_form_data(self, request: Request, form_data: FormData) -> Any:
        return form_data.get(self.name)

    async def serialize_value(self, request: Request, value: Any, action: RequestAction) -> Any:
        return value

    def dict(self) -> Dict[str, Any]:
        return super().dict()

!!! important
    Override 'dict' function to get control of the options which is available in javascript.

# Extending BaseModelView

*Starlette-Admin*  makes a few assumptions about the database models that it works with. If you want to implement your
own database backend, and still have *Starlette-Admin*’s model views work as expected, then you should take note of the
following:

1. Each model must have one field which acts as a primary key to uniquely identify instances of that model. However,
   there are no restriction on the data type or the field name of the primary key field.
2. Models must make their data accessible as python properties.

If that is the case, then you can implement your own database backend by extending the
[BaseModelView][starlette_admin.BaseModelView] class, and implementing the set of methods listed below.

Let's say you've defined your models like this:

python
from dataclasses import dataclass
from typing import List

@dataclass
class Post:
    id: int
    title: str
    content: str
    tags: List[str]

First you need to define a new class, which derives from [BaseModelView][starlette_admin.views.BaseModelView].

python
from starlette_admin import BaseModelView

class PostView(BaseModelView):
    pass

## Metadata

Set the 'identity', 'name' and 'label' for the new class

python
from starlette_admin import BaseModelView

class PostView(BaseModelView):
    identity = "post"
    name = "Post"
    label = "Blog Posts"
    icon = "fa fa-blog"

!!! important

     'identity' is used to identify the model associated to this view and should be unique.

## Primary key

Set the 'pk_attr' value which is primary key attribute name

python
from starlette_admin import BaseModelView

class PostView(BaseModelView):
    pk_attr = "id"

## Fields

Internally, *Starlette-Admin*  uses custom fields all inherit from [BaseField][starlette_admin.fields.BaseField] to
represent each attribute. So, you need to choose the right field for each attribute or create a new field if needed.
See [API Reference][starlette_admin.fields.BaseField] for full list of default fields.

python
from starlette_admin import BaseModelView
from starlette_admin import IntegerField, StringField, TagsField, TextAreaField

class PostView(BaseModelView):
    fields = [
        IntegerField("id"),
        StringField("title"),
        TextAreaField("content"),
        TagsField("tags"),
    ]

## CRUD methods

Finally, you need to implement these CRUD methods:

* [count()][starlette_admin.BaseModelView.count]
* [find_all()][starlette_admin.BaseModelView.find_all]
* [create()][starlette_admin.BaseModelView.create]
* [edit()][starlette_admin.BaseModelView.edit]
* [delete()][starlette_admin.BaseModelView.delete]

## Full example

python
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Union

from starlette.requests import Request
from starlette_admin import IntegerField, StringField, TagsField, TextAreaField
from starlette_admin.exceptions import FormValidationError
from starlette_admin.views import BaseModelView

@dataclass
class Post:
    id: int
    title: str
    content: str
    tags: List[str]

    def is_valid_for_term(self, term):
        return (
            str(term).lower() in self.title.lower()
            or str(term).lower() in self.content.lower()
            or any([str(term).lower() in tag.lower() for tag in self.tags])
        )

    def update(self, data: Dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

db: Dict[int, Post] = dict()
next_id = 1

def filter_values(values: Iterable[Post], term):
    filtered_values = []
    for value in values:
        if value.is_valid_for_term(term):
            filtered_values.append(value)
    return filtered_values

class PostView(BaseModelView):
    identity = "post"
    name = "Post"
    label = "Blog Posts"
    icon = "fa fa-blog"
    pk_attr = "id"
    fields = [
        IntegerField("id"),
        StringField("title"),
        TextAreaField("content"),
        TagsField("tags"),
    ]
    sortable_fields = ("id", "title", "content")
    search_builder = False

    async def count(
        self,
        request: Request,
        where: Union[Dict[str, Any], str, None] = None,
    ) -> int:
        values = list(db.values())
        if where is not None:
            values = filter_values(values, where)
        return len(values)

    async def find_all(
        self,
        request: Request,
        skip: int = 0,
        limit: int = 100,
        where: Union[Dict[str, Any], str, None] = None,
        order_by: Optional[List[str]] = None,
    ) -> List[Any]:
        values = list(db.values())
        if order_by is not None:
            assert len(order_by) < 2, "Not supported"
            if len(order_by) == 1:
                key, dir = order_by[0].split(maxsplit=1)
                values.sort(key=lambda v: getattr(v, key), reverse=(dir == "desc"))

        if where is not None and isinstance(where, (str, int)):
            values = filter_values(values, where)
        if limit > 0:
            return values[skip : skip + limit]
        return values[skip:]

    async def find_by_pk(self, request: Request, pk):
        return db.get(int(pk), None)

    async def find_by_pks(self, request: Request, pks):
        return [db.get(int(pk)) for pk in pks]

    async def validate_data(self, data: Dict):
        errors = {}
        if data["title"] is None or len(data["title"]) < 3:
            errors["title"] = "Ensure title has at least 03 characters"
        if data["tags"] is None or len(data["tags"]) < 1:
            errors["tags"] = "You need at least one tag"
        if len(errors) > 0:
            raise FormValidationError(errors)

    async def create(self, request: Request, data: Dict):
        await self.validate_data(data)
        global next_id
        obj = Post(id=next_id, **data)
        db[next_id] = obj
        next_id += 1
        return obj

    async def edit(self, request: Request, pk, data: Dict):
        await self.validate_data(data)
        db[int(pk)].update(data)
        return db[int(pk)]

    async def delete(self, request: Request, pks: List[Any]) -> Optional[int]:
        cnt = 0
        for pk in pks:
            value = await self.find_by_pk(request, pk)
            if value is not None:
                del db[int(pk)]
                cnt += 1
        return cnt

# Deployment

Whether you're using Starlette-Admin with FastAPI or Starlette, there are already well-documented resources to guide you
through the deployment process. It is strongly recommended to refer to these resources as they offer detailed
information and best practices:

* [FastAPI Deployment Documentation](https://fastapi.tiangolo.com/deployment/)
* [Uvicorn Deployment Documentation](https://www.uvicorn.org/deployment)

However, When running your application behind a proxy server such as Traefik or Nginx, you may encounter an
issue where static files are not rendered as HTTPS links.
To address this issue, follow the steps below:

1. Ensure that your proxy server is properly configured to handle HTTPS traffic.
2. When starting your application with Uvicorn, include the '--forwarded-allow-ips' and '--proxy-headers' options.
   These options enable Uvicorn to correctly handle forwarded headers from the proxy server.

shell title="Example"
uvicorn app.main:app --forwarded-allow-ips='*' --proxy-headers

# Alternatives, Inspiration and Comparisons

* [Flask-Admin:](https://github.com/flask-admin/flask-admin) Simple and extensible administrative interface framework for Flask. The main goal of this project is to provide similar tool for Starlette/FastApi.
* [FastApi-Admin:](https://github.com/fastapi-admin/fastapi-admin) A fast admin dashboard based on FastAPI and TortoiseORM.
* [sqladmin:](https://github.com/aminalaee/sqladmin) SQLAlchemy Admin for FastAPI and Starlette

ModelView

Bases: BaseModelView

A view for managing SQLAlchemy models.
Source code in starlette_admin/contrib/sqla/view.py

class ModelView(BaseModelView):
    """A view for managing SQLAlchemy models."""

    sortable_field_mapping: ClassVar[Dict[str, InstrumentedAttribute]] = {}
    """A dictionary for overriding the default model attribute used for sorting.

    Example:
        python
        class Post(Base):
            __tablename__ = "post"

            id: Mapped[int] = mapped_column(primary_key=True)
            title: Mapped[str] = mapped_column()
            user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
            user: Mapped[User] = relationship(back_populates="posts")

        class PostView(ModelView):
            sortable_field = ["id", "title", "user"]
            sortable_field_mapping = {
                "user": User.age,  # Sort by the age of the related user
            }
        
    """

    def __init__(
        self,
        model: Type[Any],
        icon: Optional[str] = None,
        name: Optional[str] = None,
        label: Optional[str] = None,
        identity: Optional[str] = None,
        converter: Optional[BaseSQLAModelConverter] = None,
    ):
        try:
            mapper: Mapper = inspect(model)  # type: ignore
        except NoInspectionAvailable:
            raise InvalidModelError(  # noqa B904
                f"Class {model.__name__} is not a SQLAlchemy model."
            )
        self.model = model
        self.identity = (
            identity or self.identity or slugify_class_name(self.model.__name__)
        )
        self.label = (
            label or self.label or prettify_class_name(self.model.__name__) + "s"
        )
        self.name = name or self.name or prettify_class_name(self.model.__name__)
        self.icon = icon
        if self.fields is None or len(self.fields) == 0:
            self.fields = [
                self.model.__dict__[f].key
                for f in list(self.model.__dict__.keys())
                if type(self.model.__dict__[f]) is InstrumentedAttribute
            ]
        self.fields = (converter or ModelConverter()).convert_fields_list(
            fields=self.fields, model=self.model, mapper=mapper
        )
        self._setup_primary_key()
        self.exclude_fields_from_list = normalize_list(self.exclude_fields_from_list)  # type: ignore
        self.exclude_fields_from_detail = normalize_list(self.exclude_fields_from_detail)  # type: ignore
        self.exclude_fields_from_create = normalize_list(self.exclude_fields_from_create)  # type: ignore
        self.exclude_fields_from_edit = normalize_list(self.exclude_fields_from_edit)  # type: ignore
        _default_list = [
            field.name
            for field in self.fields
            if not isinstance(field, (RelationField, FileField))
        ]
        self.searchable_fields = normalize_list(
            self.searchable_fields
            if (self.searchable_fields is not None)
            else _default_list
        )
        self.sortable_fields = normalize_list(
            self.sortable_fields
            if (self.sortable_fields is not None)
            else _default_list
        )
        self.export_fields = normalize_list(self.export_fields)
        self.fields_default_sort = normalize_list(
            self.fields_default_sort, is_default_sort_list=True
        )
        super().__init__()

    def _setup_primary_key(self) -> None:
        # Detect the primary key attribute(s) of the model
        _pk_attrs = []
        self._pk_column: Union[
            Tuple[InstrumentedAttribute, ...], InstrumentedAttribute
        ] = ()
        self._pk_coerce: Union[Tuple[type, ...], type] = ()
        for key in list(self.model.__dict__.keys()):
            attr = getattr(self.model, key)
            if isinstance(attr, InstrumentedAttribute) and getattr(
                attr, "primary_key", False
            ):
                _pk_attrs.append(key)
        if len(_pk_attrs) > 1:
            self._pk_column = tuple(getattr(self.model, attr) for attr in _pk_attrs)
            self._pk_coerce = tuple(
                extract_column_python_type(c) for c in self._pk_column
            )
            self.pk_field: BaseField = MultiplePKField(_pk_attrs)
        else:
            assert (
                len(_pk_attrs) == 1
            ), f"No primary key found in model {self.model.__name__}"
            self._pk_column = getattr(self.model, _pk_attrs[0])
            self._pk_coerce = extract_column_python_type(self._pk_column)  # type: ignore[arg-type]
            try:
                # Try to find the primary key field among the fields
                self.pk_field = next(f for f in self.fields if f.name == _pk_attrs[0])
            except StopIteration:
                # If the primary key is not among the fields, treat its value as a string
                self.pk_field = StringField(_pk_attrs[0])
        self.pk_attr = self.pk_field.name

    async def handle_action(
        self, request: Request, pks: List[Any], name: str
    ) -> Union[str, Response]:
        try:
            return await super().handle_action(request, pks, name)
        except SQLAlchemyError as exc:
            raise ActionFailed(str(exc)) from exc

    async def handle_row_action(
        self, request: Request, pk: Any, name: str
    ) -> Union[str, Response]:
        try:
            return await super().handle_row_action(request, pk, name)
        except SQLAlchemyError as exc:
            raise ActionFailed(str(exc)) from exc

    def get_details_query(self, request: Request) -> Select:
        """
        Return a Select expression which is used as base statement for
        [find_by_pk][starlette_admin.views.BaseModelView.find_by_pk] and
        [find_by_pks][starlette_admin.views.BaseModelView.find_by_pks] methods.

        Examples:
            python  hl_lines="3-4"
            class PostView(ModelView):

                    def get_details_query(self, request: Request):
                        return super().get_details_query().options(selectinload(Post.author))
            
        """
        return select(self.model)

    def get_list_query(self, request: Request) -> Select:
        """
        Return a Select expression which is used as base statement for
        [find_all][starlette_admin.views.BaseModelView.find_all] method.

        Examples:
            python  hl_lines="3-4"
            class PostView(ModelView):

                    def get_list_query(self, request: Request):
                        return super().get_list_query().where(Post.published == true())

                    def get_count_query(self, request: Request):
                        return super().get_count_query().where(Post.published == true())
            

        If you override this method, don't forget to also override
        [get_count_query][starlette_admin.contrib.sqla.ModelView.get_count_query],
        for displaying the correct item count in the list view.
        """
        return select(self.model)

    def get_count_query(self, request: Request) -> Select:
        """
        Return a Select expression which is used as base statement for
        [count][starlette_admin.views.BaseModelView.count] method.

        Examples:
            python hl_lines="6-7"
            class PostView(ModelView):

                    def get_list_query(self, request: Request):
                        return super().get_list_query().where(Post.published == true())

                    def get_count_query(self, request: Request):
                        return super().get_count_query().where(Post.published == true())
            
        """
        return select(func.count()).select_from(self.model)

    def get_search_query(self, request: Request, term: str) -> Any:
        """
        Return SQLAlchemy whereclause to use for full text search

        Args:
           request: Starlette request
           term: Filtering term

        Examples:
           python
           class PostView(ModelView):

                def get_search_query(self, request: Request, term: str):
                    return Post.title.contains(term)
           
        """
        clauses = []
        for field in self.get_fields_list(request):
            if field.searchable and type(field) in [
                StringField,
                TextAreaField,
                EmailField,
                URLField,
                PhoneField,
                ColorField,
            ]:
                attr = getattr(self.model, field.name)
                clauses.append(cast(attr, String).ilike(f"%{term}%"))
        return or_(*clauses)

    async def count(
        self,
        request: Request,
        where: Union[Dict[str, Any], str, None] = None,
    ) -> int:
        session: Union[Session, AsyncSession] = request.state.session
        stmt = self.get_count_query(request)
        if where is not None:
            if isinstance(where, dict):
                where = build_query(where, self.model)
            else:
                where = await self.build_full_text_search_query(
                    request, where, self.model
                )
            stmt = stmt.where(where)  # type: ignore
        if isinstance(session, AsyncSession):
            return (await session.execute(stmt)).scalar_one()
        return (await anyio.to_thread.run_sync(session.execute, stmt)).scalar_one()  # type: ignore[arg-type]

    async def find_all(
        self,
        request: Request,
        skip: int = 0,
        limit: int = 100,
        where: Union[Dict[str, Any], str, None] = None,
        order_by: Optional[List[str]] = None,
    ) -> Sequence[Any]:
        session: Union[Session, AsyncSession] = request.state.session
        stmt = self.get_list_query(request).offset(skip)
        if limit > 0:
            stmt = stmt.limit(limit)
        if where is not None:
            if isinstance(where, dict):
                where = build_query(where, self.model)
            else:
                where = await self.build_full_text_search_query(
                    request, where, self.model
                )
            stmt = stmt.where(where)  # type: ignore
        stmt = self.build_order_clauses(request, order_by or [], stmt)
        for field in self.get_fields_list(request, RequestAction.LIST):
            if isinstance(field, RelationField):
                stmt = stmt.options(joinedload(getattr(self.model, field.name)))
        if isinstance(session, AsyncSession):
            return (await session.execute(stmt)).scalars().unique().all()
        return (
            (await anyio.to_thread.run_sync(session.execute, stmt))  # type: ignore[arg-type]
            .scalars()
            .unique()
            .all()
        )

    async def find_by_pk(self, request: Request, pk: Any) -> Any:
        session: Union[Session, AsyncSession] = request.state.session
        if isinstance(self._pk_column, tuple):
            """
            For composite primary keys, the pk parameter is a comma-separated string
            representing the values of each primary key attribute.

            For example, if the model has two primary keys (id1, id2):
            - the 'pk' will be: "val1,val2"
            - the generated query: (id1 == val1 AND id2 == val2)
            """
            assert isinstance(self._pk_coerce, tuple)
            clause = and_(
                (
                    _pk_col == _coerce(_pk)
                    if _coerce is not bool
                    else _pk_col
                    == (_pk == "True")  # to avoid bool("False") which is True
                )
                for _pk_col, _coerce, _pk in zip(
                    self._pk_column, self._pk_coerce, iterdecode(pk)  # type: ignore[type-var,arg-type]
                )
            )
        else:
            assert isinstance(self._pk_coerce, type)
            clause = self._pk_column == self._pk_coerce(pk)
        stmt = self.get_details_query(request).where(clause)
        for field in self.get_fields_list(request, request.state.action):
            if isinstance(field, RelationField):
                stmt = stmt.options(joinedload(getattr(self.model, field.name)))
        if isinstance(session, AsyncSession):
            return (await session.execute(stmt)).scalars().unique().one_or_none()
        return (
            (await anyio.to_thread.run_sync(session.execute, stmt))  # type: ignore[arg-type]
            .scalars()
            .unique()
            .one_or_none()
        )

    async def find_by_pks(self, request: Request, pks: List[Any]) -> Sequence[Any]:
        has_multiple_pks = isinstance(self._pk_column, tuple)
        try:
            return await self._exec_find_by_pks(request, pks)
        except DBAPIError:  # pragma: no cover
            if has_multiple_pks:
                # Retry for multiple primary keys in case of an error related to the composite IN construct
                # This section is intentionally not covered by the test suite because SQLite, MySQL, and
                # PostgreSQL support composite IN construct.
                return await self._exec_find_by_pks(request, pks, False)
            raise

    async def _exec_find_by_pks(
        self, request: Request, pks: List[Any], use_composite_in: bool = True
    ) -> Sequence[Any]:
        session: Union[Session, AsyncSession] = request.state.session
        has_multiple_pks = isinstance(self._pk_column, tuple)

        if has_multiple_pks:
            """Handle composite primary keys"""
            clause = await self._get_multiple_pks_in_clause(pks, use_composite_in)
        else:
            clause = self._pk_column.in_(map(self._pk_coerce, pks))  # type: ignore
        stmt = self.get_details_query(request).where(clause)
        for field in self.get_fields_list(request, request.state.action):
            if isinstance(field, RelationField):
                stmt = stmt.options(joinedload(getattr(self.model, field.name)))
        if isinstance(session, AsyncSession):
            return (await session.execute(stmt)).scalars().unique().all()
        return (
            (await anyio.to_thread.run_sync(session.execute, stmt))  # type: ignore[arg-type]
            .scalars()
            .unique()
            .all()
        )

    async def _get_multiple_pks_in_clause(
        self, pks: List[Any], use_composite_in: bool
    ) -> Any:
        """
        Constructs the WHERE clause for models with multiple primary keys.

        Args:
            pks: A list of comma-separated values
                Example: ["val1,val2", "val3,val4"]
            use_composite_in: A flag indicating whether to use the composite IN construct.

        The generated query depends on the value of 'use_composite_in':

        - When 'use_composite_in' is True:
            WHERE (id1, id2) IN ((val1, val2), (val3, val4))

            Note: The composite IN construct may not be supported by all database backends.
                Read https://docs.sqlalchemy.org/en/latest/core/sqlelement.html#sqlalchemy.sql.expression.tuple_

        - When 'use_composite_in' is False:
            WHERE (id1 == val1 AND id2 == val2) OR (id1 == val3 AND id2 == val4)
        """
        assert isinstance(self._pk_coerce, tuple)
        decoded_pks = tuple(iterdecode(pk) for pk in pks)
        if use_composite_in:
            return tuple_(*self._pk_column).in_(
                tuple(
                    (_coerce(_pk) if _coerce is not bool else _pk == "True")
                    for _coerce, _pk in zip(
                        self._pk_coerce, decoded_pk  # type: ignore[type-var,arg-type]
                    )
                )
                for decoded_pk in decoded_pks
            )
        else:  # noqa: RET505, pragma: no cover
            clauses = []
            for decoded_pk in decoded_pks:
                clauses.append(
                    and_(
                        (
                            _pk_col == _coerce(_pk)
                            if _coerce is not bool
                            else (_pk_col == (_pk == "True"))
                        )  # to avoid bool("False") which is True
                        for _pk_col, _coerce, _pk in zip(
                            self._pk_column, self._pk_coerce, decoded_pk  # type: ignore[type-var,arg-type]
                        )
                    )
                )
            return or_(*clauses)

    async def validate(self, request: Request, data: Dict[str, Any]) -> None:
        """
        Inherit this method to validate your data.

        Args:
            request: Starlette request
            data: Submitted data

        Raises:
            FormValidationError: to display errors to users

        Examples:
            python
            from starlette_admin.contrib.sqla import ModelView
            from starlette_admin.exceptions import FormValidationError

            class Post(Base):
                __tablename__ = "post"

                id = Column(Integer, primary_key=True)
                title = Column(String(100), nullable=False)
                text = Column(Text, nullable=False)
                date = Column(Date)

            class PostView(ModelView):

                async def validate(self, request: Request, data: Dict[str, Any]) -> None:
                    errors: Dict[str, str] = dict()
                    _2day_from_today = date.today() + timedelta(days=2)
                    if data["title"] is None or len(data["title"]) < 3:
                        errors["title"] = "Ensure this value has at least 03 characters"
                    if data["text"] is None or len(data["text"]) < 10:
                        errors["text"] = "Ensure this value has at least 10 characters"
                    if data["date"] is None or data["date"] < _2day_from_today:
                        errors["date"] = "We need at least one day to verify your post"
                    if len(errors) > 0:
                        raise FormValidationError(errors)
                    return await super().validate(request, data)
            

        """

    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        try:
            data = await self._arrange_data(request, data)
            await self.validate(request, data)
            session: Union[Session, AsyncSession] = request.state.session
            obj = await self._populate_obj(request, self.model(), data)
            session.add(obj)
            await self.before_create(request, data, obj)
            if isinstance(session, AsyncSession):
                await session.commit()
                await session.refresh(obj)
            else:
                await anyio.to_thread.run_sync(session.commit)  # type: ignore[arg-type]
                await anyio.to_thread.run_sync(session.refresh, obj)  # type: ignore[arg-type]
            await self.after_create(request, obj)
            return obj
        except Exception as e:
            return self.handle_exception(e)

    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        try:
            data = await self._arrange_data(request, data, True)
            await self.validate(request, data)
            session: Union[Session, AsyncSession] = request.state.session
            obj = await self.find_by_pk(request, pk)
            await self._populate_obj(request, obj, data, True)
            session.add(obj)
            await self.before_edit(request, data, obj)
            if isinstance(session, AsyncSession):
                await session.commit()
                await session.refresh(obj)
            else:
                await anyio.to_thread.run_sync(session.commit)  # type: ignore[arg-type]
                await anyio.to_thread.run_sync(session.refresh, obj)  # type: ignore[arg-type]
            await self.after_edit(request, obj)
            return obj
        except Exception as e:
            self.handle_exception(e)

    async def _arrange_data(
        self,
        request: Request,
        data: Dict[str, Any],
        is_edit: bool = False,
    ) -> Dict[str, Any]:
        """
        This function will return a new dict with relationships loaded from
        database.
        """
        arranged_data: Dict[str, Any] = {}
        for field in self.get_fields_list(request, request.state.action):
            if isinstance(field, RelationField) and data[field.name] is not None:
                foreign_model = self._find_foreign_model(field.identity)  # type: ignore
                if isinstance(field, HasMany):
                    arranged_data[field.name] = field.collection_class(await foreign_model.find_by_pks(request, data[field.name]))  # type: ignore[call-arg]
                else:
                    arranged_data[field.name] = await foreign_model.find_by_pk(
                        request, data[field.name]
                    )
            else:
                arranged_data[field.name] = data[field.name]
        return arranged_data

    async def _populate_obj(
        self,
        request: Request,
        obj: Any,
        data: Dict[str, Any],
        is_edit: bool = False,
    ) -> Any:
        for field in self.get_fields_list(request, request.state.action):
            name, value = field.name, data.get(field.name, None)
            if isinstance(field, FileField):
                value, should_be_deleted = value
                if should_be_deleted:
                    setattr(obj, name, None)
                elif (not field.multiple and value is not None) or (
                    field.multiple and isinstance(value, list) and len(value) > 0
                ):
                    setattr(obj, name, value)
            else:
                setattr(obj, name, value)
        return obj

    async def delete(self, request: Request, pks: List[Any]) -> Optional[int]:
        session: Union[Session, AsyncSession] = request.state.session
        objs = await self.find_by_pks(request, pks)
        if isinstance(session, AsyncSession):
            for obj in objs:
                await self.before_delete(request, obj)
                await session.delete(obj)
            await session.commit()
        else:
            for obj in objs:
                await self.before_delete(request, obj)
                await anyio.to_thread.run_sync(session.delete, obj)  # type: ignore[arg-type]
            await anyio.to_thread.run_sync(session.commit)  # type: ignore[arg-type]
        for obj in objs:
            await self.after_delete(request, obj)
        return len(objs)

    async def build_full_text_search_query(
        self, request: Request, term: str, model: Any
    ) -> Any:
        return self.get_search_query(request, term)

    def build_order_clauses(
        self, request: Request, order_list: List[str], stmt: Select
    ) -> Select:
        for value in order_list:
            attr_key, order = value.strip().split(maxsplit=1)
            model_attr = getattr(self.model, attr_key, None)
            if model_attr is not None and isinstance(
                model_attr.property, RelationshipProperty
            ):
                stmt = stmt.outerjoin(model_attr)
            sorting_attr = self.sortable_field_mapping.get(attr_key, model_attr)
            stmt = stmt.order_by(
                not_none(sorting_attr).desc()
                if order.lower() == "desc"
                else sorting_attr
            )
        return stmt

    async def get_pk_value(self, request: Request, obj: Any) -> Any:
        return await self.pk_field.parse_obj(request, obj)

    async def get_serialized_pk_value(self, request: Request, obj: Any) -> Any:
        value = await self.get_pk_value(request, obj)
        return await self.pk_field.serialize_value(request, value, request.state.action)

    def handle_exception(self, exc: Exception) -> None:
        try:
            """Automatically handle sqlalchemy_file error"""
            from sqlalchemy_file.exceptions import ValidationError

            if isinstance(exc, ValidationError):
                raise FormValidationError({exc.key: exc.msg})
        except ImportError:  # pragma: no cover
            pass
        raise exc  # pragma: no cover

Source code in starlette_admin/contrib/sqla/view.py

class ModelView(BaseModelView):
    """A view for managing SQLAlchemy models."""

    sortable_field_mapping: ClassVar[Dict[str, InstrumentedAttribute]] = {}
    """A dictionary for overriding the default model attribute used for sorting.

    Example:
        python
        class Post(Base):
            __tablename__ = "post"

            id: Mapped[int] = mapped_column(primary_key=True)
            title: Mapped[str] = mapped_column()
            user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
            user: Mapped[User] = relationship(back_populates="posts")

        class PostView(ModelView):
            sortable_field = ["id", "title", "user"]
            sortable_field_mapping = {
                "user": User.age,  # Sort by the age of the related user
            }
        
    """

    def __init__(
        self,
        model: Type[Any],
        icon: Optional[str] = None,
        name: Optional[str] = None,
        label: Optional[str] = None,
        identity: Optional[str] = None,
        converter: Optional[BaseSQLAModelConverter] = None,
    ):
        try:
            mapper: Mapper = inspect(model)  # type: ignore
        except NoInspectionAvailable:
            raise InvalidModelError(  # noqa B904
                f"Class {model.__name__} is not a SQLAlchemy model."
            )
        self.model = model
        self.identity = (
            identity or self.identity or slugify_class_name(self.model.__name__)
        )
        self.label = (
            label or self.label or prettify_class_name(self.model.__name__) + "s"
        )
        self.name = name or self.name or prettify_class_name(self.model.__name__)
        self.icon = icon
        if self.fields is None or len(self.fields) == 0:
            self.fields = [
                self.model.__dict__[f].key
                for f in list(self.model.__dict__.keys())
                if type(self.model.__dict__[f]) is InstrumentedAttribute
            ]
        self.fields = (converter or ModelConverter()).convert_fields_list(
            fields=self.fields, model=self.model, mapper=mapper
        )
        self._setup_primary_key()
        self.exclude_fields_from_list = normalize_list(self.exclude_fields_from_list)  # type: ignore
        self.exclude_fields_from_detail = normalize_list(self.exclude_fields_from_detail)  # type: ignore
        self.exclude_fields_from_create = normalize_list(self.exclude_fields_from_create)  # type: ignore
        self.exclude_fields_from_edit = normalize_list(self.exclude_fields_from_edit)  # type: ignore
        _default_list = [
            field.name
            for field in self.fields
            if not isinstance(field, (RelationField, FileField))
        ]
        self.searchable_fields = normalize_list(
            self.searchable_fields
            if (self.searchable_fields is not None)
            else _default_list
        )
        self.sortable_fields = normalize_list(
            self.sortable_fields
            if (self.sortable_fields is not None)
            else _default_list
        )
        self.export_fields = normalize_list(self.export_fields)
        self.fields_default_sort = normalize_list(
            self.fields_default_sort, is_default_sort_list=True
        )
        super().__init__()

    def _setup_primary_key(self) -> None:
        # Detect the primary key attribute(s) of the model
        _pk_attrs = []
        self._pk_column: Union[
            Tuple[InstrumentedAttribute, ...], InstrumentedAttribute
        ] = ()
        self._pk_coerce: Union[Tuple[type, ...], type] = ()
        for key in list(self.model.__dict__.keys()):
            attr = getattr(self.model, key)
            if isinstance(attr, InstrumentedAttribute) and getattr(
                attr, "primary_key", False
            ):
                _pk_attrs.append(key)
        if len(_pk_attrs) > 1:
            self._pk_column = tuple(getattr(self.model, attr) for attr in _pk_attrs)
            self._pk_coerce = tuple(
                extract_column_python_type(c) for c in self._pk_column
            )
            self.pk_field: BaseField = MultiplePKField(_pk_attrs)
        else:
            assert (
                len(_pk_attrs) == 1
            ), f"No primary key found in model {self.model.__name__}"
            self._pk_column = getattr(self.model, _pk_attrs[0])
            self._pk_coerce = extract_column_python_type(self._pk_column)  # type: ignore[arg-type]
            try:
                # Try to find the primary key field among the fields
                self.pk_field = next(f for f in self.fields if f.name == _pk_attrs[0])
            except StopIteration:
                # If the primary key is not among the fields, treat its value as a string
                self.pk_field = StringField(_pk_attrs[0])
        self.pk_attr = self.pk_field.name

    async def handle_action(
        self, request: Request, pks: List[Any], name: str
    ) -> Union[str, Response]:
        try:
            return await super().handle_action(request, pks, name)
        except SQLAlchemyError as exc:
            raise ActionFailed(str(exc)) from exc

    async def handle_row_action(
        self, request: Request, pk: Any, name: str
    ) -> Union[str, Response]:
        try:
            return await super().handle_row_action(request, pk, name)
        except SQLAlchemyError as exc:
            raise ActionFailed(str(exc)) from exc

    def get_details_query(self, request: Request) -> Select:
        """
        Return a Select expression which is used as base statement for
        [find_by_pk][starlette_admin.views.BaseModelView.find_by_pk] and
        [find_by_pks][starlette_admin.views.BaseModelView.find_by_pks] methods.

        Examples:
            python  hl_lines="3-4"
            class PostView(ModelView):

                    def get_details_query(self, request: Request):
                        return super().get_details_query().options(selectinload(Post.author))
            
        """
        return select(self.model)

    def get_list_query(self, request: Request) -> Select:
        """
        Return a Select expression which is used as base statement for
        [find_all][starlette_admin.views.BaseModelView.find_all] method.

        Examples:
            python  hl_lines="3-4"
            class PostView(ModelView):

                    def get_list_query(self, request: Request):
                        return super().get_list_query().where(Post.published == true())

                    def get_count_query(self, request: Request):
                        return super().get_count_query().where(Post.published == true())
            

        If you override this method, don't forget to also override
        [get_count_query][starlette_admin.contrib.sqla.ModelView.get_count_query],
        for displaying the correct item count in the list view.
        """
        return select(self.model)

    def get_count_query(self, request: Request) -> Select:
        """
        Return a Select expression which is used as base statement for
        [count][starlette_admin.views.BaseModelView.count] method.

        Examples:
            python hl_lines="6-7"
            class PostView(ModelView):

                    def get_list_query(self, request: Request):
                        return super().get_list_query().where(Post.published == true())

                    def get_count_query(self, request: Request):
                        return super().get_count_query().where(Post.published == true())
            
        """
        return select(func.count()).select_from(self.model)

    def get_search_query(self, request: Request, term: str) -> Any:
        """
        Return SQLAlchemy whereclause to use for full text search

        Args:
           request: Starlette request
           term: Filtering term

        Examples:
           python
           class PostView(ModelView):

                def get_search_query(self, request: Request, term: str):
                    return Post.title.contains(term)
           
        """
        clauses = []
        for field in self.get_fields_list(request):
            if field.searchable and type(field) in [
                StringField,
                TextAreaField,
                EmailField,
                URLField,
                PhoneField,
                ColorField,
            ]:
                attr = getattr(self.model, field.name)
                clauses.append(cast(attr, String).ilike(f"%{term}%"))
        return or_(*clauses)

    async def count(
        self,
        request: Request,
        where: Union[Dict[str, Any], str, None] = None,
    ) -> int:
        session: Union[Session, AsyncSession] = request.state.session
        stmt = self.get_count_query(request)
        if where is not None:
            if isinstance(where, dict):
                where = build_query(where, self.model)
            else:
                where = await self.build_full_text_search_query(
                    request, where, self.model
                )
            stmt = stmt.where(where)  # type: ignore
        if isinstance(session, AsyncSession):
            return (await session.execute(stmt)).scalar_one()
        return (await anyio.to_thread.run_sync(session.execute, stmt)).scalar_one()  # type: ignore[arg-type]

    async def find_all(
        self,
        request: Request,
        skip: int = 0,
        limit: int = 100,
        where: Union[Dict[str, Any], str, None] = None,
        order_by: Optional[List[str]] = None,
    ) -> Sequence[Any]:
        session: Union[Session, AsyncSession] = request.state.session
        stmt = self.get_list_query(request).offset(skip)
        if limit > 0:
            stmt = stmt.limit(limit)
        if where is not None:
            if isinstance(where, dict):
                where = build_query(where, self.model)
            else:
                where = await self.build_full_text_search_query(
                    request, where, self.model
                )
            stmt = stmt.where(where)  # type: ignore
        stmt = self.build_order_clauses(request, order_by or [], stmt)
        for field in self.get_fields_list(request, RequestAction.LIST):
            if isinstance(field, RelationField):
                stmt = stmt.options(joinedload(getattr(self.model, field.name)))
        if isinstance(session, AsyncSession):
            return (await session.execute(stmt)).scalars().unique().all()
        return (
            (await anyio.to_thread.run_sync(session.execute, stmt))  # type: ignore[arg-type]
            .scalars()
            .unique()
            .all()
        )

    async def find_by_pk(self, request: Request, pk: Any) -> Any:
        session: Union[Session, AsyncSession] = request.state.session
        if isinstance(self._pk_column, tuple):
            """
            For composite primary keys, the pk parameter is a comma-separated string
            representing the values of each primary key attribute.

            For example, if the model has two primary keys (id1, id2):
            - the 'pk' will be: "val1,val2"
            - the generated query: (id1 == val1 AND id2 == val2)
            """
            assert isinstance(self._pk_coerce, tuple)
            clause = and_(
                (
                    _pk_col == _coerce(_pk)
                    if _coerce is not bool
                    else _pk_col
                    == (_pk == "True")  # to avoid bool("False") which is True
                )
                for _pk_col, _coerce, _pk in zip(
                    self._pk_column, self._pk_coerce, iterdecode(pk)  # type: ignore[type-var,arg-type]
                )
            )
        else:
            assert isinstance(self._pk_coerce, type)
            clause = self._pk_column == self._pk_coerce(pk)
        stmt = self.get_details_query(request).where(clause)
        for field in self.get_fields_list(request, request.state.action):
            if isinstance(field, RelationField):
                stmt = stmt.options(joinedload(getattr(self.model, field.name)))
        if isinstance(session, AsyncSession):
            return (await session.execute(stmt)).scalars().unique().one_or_none()
        return (
            (await anyio.to_thread.run_sync(session.execute, stmt))  # type: ignore[arg-type]
            .scalars()
            .unique()
            .one_or_none()
        )

    async def find_by_pks(self, request: Request, pks: List[Any]) -> Sequence[Any]:
        has_multiple_pks = isinstance(self._pk_column, tuple)
        try:
            return await self._exec_find_by_pks(request, pks)
        except DBAPIError:  # pragma: no cover
            if has_multiple_pks:
                # Retry for multiple primary keys in case of an error related to the composite IN construct
                # This section is intentionally not covered by the test suite because SQLite, MySQL, and
                # PostgreSQL support composite IN construct.
                return await self._exec_find_by_pks(request, pks, False)
            raise

    async def _exec_find_by_pks(
        self, request: Request, pks: List[Any], use_composite_in: bool = True
    ) -> Sequence[Any]:
        session: Union[Session, AsyncSession] = request.state.session
        has_multiple_pks = isinstance(self._pk_column, tuple)

        if has_multiple_pks:
            """Handle composite primary keys"""
            clause = await self._get_multiple_pks_in_clause(pks, use_composite_in)
        else:
            clause = self._pk_column.in_(map(self._pk_coerce, pks))  # type: ignore
        stmt = self.get_details_query(request).where(clause)
        for field in self.get_fields_list(request, request.state.action):
            if isinstance(field, RelationField):
                stmt = stmt.options(joinedload(getattr(self.model, field.name)))
        if isinstance(session, AsyncSession):
            return (await session.execute(stmt)).scalars().unique().all()
        return (
            (await anyio.to_thread.run_sync(session.execute, stmt))  # type: ignore[arg-type]
            .scalars()
            .unique()
            .all()
        )

    async def _get_multiple_pks_in_clause(
        self, pks: List[Any], use_composite_in: bool
    ) -> Any:
        """
        Constructs the WHERE clause for models with multiple primary keys.

        Args:
            pks: A list of comma-separated values
                Example: ["val1,val2", "val3,val4"]
            use_composite_in: A flag indicating whether to use the composite IN construct.

        The generated query depends on the value of 'use_composite_in':

        - When 'use_composite_in' is True:
            WHERE (id1, id2) IN ((val1, val2), (val3, val4))

            Note: The composite IN construct may not be supported by all database backends.
                Read https://docs.sqlalchemy.org/en/latest/core/sqlelement.html#sqlalchemy.sql.expression.tuple_

        - When 'use_composite_in' is False:
            WHERE (id1 == val1 AND id2 == val2) OR (id1 == val3 AND id2 == val4)
        """
        assert isinstance(self._pk_coerce, tuple)
        decoded_pks = tuple(iterdecode(pk) for pk in pks)
        if use_composite_in:
            return tuple_(*self._pk_column).in_(
                tuple(
                    (_coerce(_pk) if _coerce is not bool else _pk == "True")
                    for _coerce, _pk in zip(
                        self._pk_coerce, decoded_pk  # type: ignore[type-var,arg-type]
                    )
                )
                for decoded_pk in decoded_pks
            )
        else:  # noqa: RET505, pragma: no cover
            clauses = []
            for decoded_pk in decoded_pks:
                clauses.append(
                    and_(
                        (
                            _pk_col == _coerce(_pk)
                            if _coerce is not bool
                            else (_pk_col == (_pk == "True"))
                        )  # to avoid bool("False") which is True
                        for _pk_col, _coerce, _pk in zip(
                            self._pk_column, self._pk_coerce, decoded_pk  # type: ignore[type-var,arg-type]
                        )
                    )
                )
            return or_(*clauses)

    async def validate(self, request: Request, data: Dict[str, Any]) -> None:
        """
        Inherit this method to validate your data.

        Args:
            request: Starlette request
            data: Submitted data

        Raises:
            FormValidationError: to display errors to users

        Examples:
            python
            from starlette_admin.contrib.sqla import ModelView
            from starlette_admin.exceptions import FormValidationError

            class Post(Base):
                __tablename__ = "post"

                id = Column(Integer, primary_key=True)
                title = Column(String(100), nullable=False)
                text = Column(Text, nullable=False)
                date = Column(Date)

            class PostView(ModelView):

                async def validate(self, request: Request, data: Dict[str, Any]) -> None:
                    errors: Dict[str, str] = dict()
                    _2day_from_today = date.today() + timedelta(days=2)
                    if data["title"] is None or len(data["title"]) < 3:
                        errors["title"] = "Ensure this value has at least 03 characters"
                    if data["text"] is None or len(data["text"]) < 10:
                        errors["text"] = "Ensure this value has at least 10 characters"
                    if data["date"] is None or data["date"] < _2day_from_today:
                        errors["date"] = "We need at least one day to verify your post"
                    if len(errors) > 0:
                        raise FormValidationError(errors)
                    return await super().validate(request, data)
            

        """

    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        try:
            data = await self._arrange_data(request, data)
            await self.validate(request, data)
            session: Union[Session, AsyncSession] = request.state.session
            obj = await self._populate_obj(request, self.model(), data)
            session.add(obj)
            await self.before_create(request, data, obj)
            if isinstance(session, AsyncSession):
                await session.commit()
                await session.refresh(obj)
            else:
                await anyio.to_thread.run_sync(session.commit)  # type: ignore[arg-type]
                await anyio.to_thread.run_sync(session.refresh, obj)  # type: ignore[arg-type]
            await self.after_create(request, obj)
            return obj
        except Exception as e:
            return self.handle_exception(e)

    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        try:
            data = await self._arrange_data(request, data, True)
            await self.validate(request, data)
            session: Union[Session, AsyncSession] = request.state.session
            obj = await self.find_by_pk(request, pk)
            await self._populate_obj(request, obj, data, True)
            session.add(obj)
            await self.before_edit(request, data, obj)
            if isinstance(session, AsyncSession):
                await session.commit()
                await session.refresh(obj)
            else:
                await anyio.to_thread.run_sync(session.commit)  # type: ignore[arg-type]
                await anyio.to_thread.run_sync(session.refresh, obj)  # type: ignore[arg-type]
            await self.after_edit(request, obj)
            return obj
        except Exception as e:
            self.handle_exception(e)

    async def _arrange_data(
        self,
        request: Request,
        data: Dict[str, Any],
        is_edit: bool = False,
    ) -> Dict[str, Any]:
        """
        This function will return a new dict with relationships loaded from
        database.
        """
        arranged_data: Dict[str, Any] = {}
        for field in self.get_fields_list(request, request.state.action):
            if isinstance(field, RelationField) and data[field.name] is not None:
                foreign_model = self._find_foreign_model(field.identity)  # type: ignore
                if isinstance(field, HasMany):
                    arranged_data[field.name] = field.collection_class(await foreign_model.find_by_pks(request, data[field.name]))  # type: ignore[call-arg]
                else:
                    arranged_data[field.name] = await foreign_model.find_by_pk(
                        request, data[field.name]
                    )
            else:
                arranged_data[field.name] = data[field.name]
        return arranged_data

    async def _populate_obj(
        self,
        request: Request,
        obj: Any,
        data: Dict[str, Any],
        is_edit: bool = False,
    ) -> Any:
        for field in self.get_fields_list(request, request.state.action):
            name, value = field.name, data.get(field.name, None)
            if isinstance(field, FileField):
                value, should_be_deleted = value
                if should_be_deleted:
                    setattr(obj, name, None)
                elif (not field.multiple and value is not None) or (
                    field.multiple and isinstance(value, list) and len(value) > 0
                ):
                    setattr(obj, name, value)
            else:
                setattr(obj, name, value)
        return obj

    async def delete(self, request: Request, pks: List[Any]) -> Optional[int]:
        session: Union[Session, AsyncSession] = request.state.session
        objs = await self.find_by_pks(request, pks)
        if isinstance(session, AsyncSession):
            for obj in objs:
                await self.before_delete(request, obj)
                await session.delete(obj)
            await session.commit()
        else:
            for obj in objs:
                await self.before_delete(request, obj)
                await anyio.to_thread.run_sync(session.delete, obj)  # type: ignore[arg-type]
            await anyio.to_thread.run_sync(session.commit)  # type: ignore[arg-type]
        for obj in objs:
            await self.after_delete(request, obj)
        return len(objs)

    async def build_full_text_search_query(
        self, request: Request, term: str, model: Any
    ) -> Any:
        return self.get_search_query(request, term)

    def build_order_clauses(
        self, request: Request, order_list: List[str], stmt: Select
    ) -> Select:
        for value in order_list:
            attr_key, order = value.strip().split(maxsplit=1)
            model_attr = getattr(self.model, attr_key, None)
            if model_attr is not None and isinstance(
                model_attr.property, RelationshipProperty
            ):
                stmt = stmt.outerjoin(model_attr)
            sorting_attr = self.sortable_field_mapping.get(attr_key, model_attr)
            stmt = stmt.order_by(
                not_none(sorting_attr).desc()
                if order.lower() == "desc"
                else sorting_attr
            )
        return stmt

    async def get_pk_value(self, request: Request, obj: Any) -> Any:
        return await self.pk_field.parse_obj(request, obj)

    async def get_serialized_pk_value(self, request: Request, obj: Any) -> Any:
        value = await self.get_pk_value(request, obj)
        return await self.pk_field.serialize_value(request, value, request.state.action)

    def handle_exception(self, exc: Exception) -> None:
        try:
            """Automatically handle sqlalchemy_file error"""
            from sqlalchemy_file.exceptions import ValidationError

            if isinstance(exc, ValidationError):
                raise FormValidationError({exc.key: exc.msg})
        except ImportError:  # pragma: no cover
            pass
        raise exc  # pragma: no cover

sortable_field_mapping = {} class-attribute

A dictionary for overriding the default model attribute used for sorting.
Example

class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped[User] = relationship(back_populates="posts")

class PostView(ModelView):
    sortable_field = ["id", "title", "user"]
    sortable_field_mapping = {
        "user": User.age,  # Sort by the age of the related user
    }

Example

class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped[User] = relationship(back_populates="posts")

class PostView(ModelView):
    sortable_field = ["id", "title", "user"]
    sortable_field_mapping = {
        "user": User.age,  # Sort by the age of the related user
    }

get_count_query(request)

Return a Select expression which is used as base statement for count method.

Examples:

class PostView(ModelView):

        def get_list_query(self, request: Request):
            return super().get_list_query().where(Post.published == true())

        def get_count_query(self, request: Request):
            return super().get_count_query().where(Post.published == true())

Source code in starlette_admin/contrib/sqla/view.py

def get_count_query(self, request: Request) -> Select:
    """
    Return a Select expression which is used as base statement for
    [count][starlette_admin.views.BaseModelView.count] method.

    Examples:
        python hl_lines="6-7"
        class PostView(ModelView):

                def get_list_query(self, request: Request):
                    return super().get_list_query().where(Post.published == true())

                def get_count_query(self, request: Request):
                    return super().get_count_query().where(Post.published == true())
        
    """
    return select(func.count()).select_from(self.model)

Source code in starlette_admin/contrib/sqla/view.py

def get_count_query(self, request: Request) -> Select:
    """
    Return a Select expression which is used as base statement for
    [count][starlette_admin.views.BaseModelView.count] method.

    Examples:
        python hl_lines="6-7"
        class PostView(ModelView):

                def get_list_query(self, request: Request):
                    return super().get_list_query().where(Post.published == true())

                def get_count_query(self, request: Request):
                    return super().get_count_query().where(Post.published == true())
        
    """
    return select(func.count()).select_from(self.model)

get_details_query(request)

Return a Select expression which is used as base statement for find_by_pk and find_by_pks methods.

Examples:

class PostView(ModelView):

        def get_details_query(self, request: Request):
            return super().get_details_query().options(selectinload(Post.author))

Source code in starlette_admin/contrib/sqla/view.py

def get_details_query(self, request: Request) -> Select:
    """
    Return a Select expression which is used as base statement for
    [find_by_pk][starlette_admin.views.BaseModelView.find_by_pk] and
    [find_by_pks][starlette_admin.views.BaseModelView.find_by_pks] methods.

    Examples:
        python  hl_lines="3-4"
        class PostView(ModelView):

                def get_details_query(self, request: Request):
                    return super().get_details_query().options(selectinload(Post.author))
        
    """
    return select(self.model)

Source code in starlette_admin/contrib/sqla/view.py

def get_details_query(self, request: Request) -> Select:
    """
    Return a Select expression which is used as base statement for
    [find_by_pk][starlette_admin.views.BaseModelView.find_by_pk] and
    [find_by_pks][starlette_admin.views.BaseModelView.find_by_pks] methods.

    Examples:
        python  hl_lines="3-4"
        class PostView(ModelView):

                def get_details_query(self, request: Request):
                    return super().get_details_query().options(selectinload(Post.author))
        
    """
    return select(self.model)

get_list_query(request)

Return a Select expression which is used as base statement for find_all method.

Examples:

class PostView(ModelView):

        def get_list_query(self, request: Request):
            return super().get_list_query().where(Post.published == true())

        def get_count_query(self, request: Request):
            return super().get_count_query().where(Post.published == true())

If you override this method, don't forget to also override get_count_query, for displaying the correct item count in the list view.
Source code in starlette_admin/contrib/sqla/view.py

def get_list_query(self, request: Request) -> Select:
    """
    Return a Select expression which is used as base statement for
    [find_all][starlette_admin.views.BaseModelView.find_all] method.

    Examples:
        python  hl_lines="3-4"
        class PostView(ModelView):

                def get_list_query(self, request: Request):
                    return super().get_list_query().where(Post.published == true())

                def get_count_query(self, request: Request):
                    return super().get_count_query().where(Post.published == true())
        

    If you override this method, don't forget to also override
    [get_count_query][starlette_admin.contrib.sqla.ModelView.get_count_query],
    for displaying the correct item count in the list view.
    """
    return select(self.model)

Source code in starlette_admin/contrib/sqla/view.py

def get_list_query(self, request: Request) -> Select:
    """
    Return a Select expression which is used as base statement for
    [find_all][starlette_admin.views.BaseModelView.find_all] method.

    Examples:
        python  hl_lines="3-4"
        class PostView(ModelView):

                def get_list_query(self, request: Request):
                    return super().get_list_query().where(Post.published == true())

                def get_count_query(self, request: Request):
                    return super().get_count_query().where(Post.published == true())
        

    If you override this method, don't forget to also override
    [get_count_query][starlette_admin.contrib.sqla.ModelView.get_count_query],
    for displaying the correct item count in the list view.
    """
    return select(self.model)

get_search_query(request, term)

Return SQLAlchemy whereclause to use for full text search

Parameters:
Name 	Type 	Description 	Default
request 	Request 	

Starlette request
	required
term 	str 	

Filtering term
	required

Examples:

class PostView(ModelView):

     def get_search_query(self, request: Request, term: str):
         return Post.title.contains(term)

Source code in starlette_admin/contrib/sqla/view.py

def get_search_query(self, request: Request, term: str) -> Any:
    """
    Return SQLAlchemy whereclause to use for full text search

    Args:
       request: Starlette request
       term: Filtering term

    Examples:
       python
       class PostView(ModelView):

            def get_search_query(self, request: Request, term: str):
                return Post.title.contains(term)
       
    """
    clauses = []
    for field in self.get_fields_list(request):
        if field.searchable and type(field) in [
            StringField,
            TextAreaField,
            EmailField,
            URLField,
            PhoneField,
            ColorField,
        ]:
            attr = getattr(self.model, field.name)
            clauses.append(cast(attr, String).ilike(f"%{term}%"))
    return or_(*clauses)

Source code in starlette_admin/contrib/sqla/view.py

def get_search_query(self, request: Request, term: str) -> Any:
    """
    Return SQLAlchemy whereclause to use for full text search

    Args:
       request: Starlette request
       term: Filtering term

    Examples:
       python
       class PostView(ModelView):

            def get_search_query(self, request: Request, term: str):
                return Post.title.contains(term)
       
    """
    clauses = []
    for field in self.get_fields_list(request):
        if field.searchable and type(field) in [
            StringField,
            TextAreaField,
            EmailField,
            URLField,
            PhoneField,
            ColorField,
        ]:
            attr = getattr(self.model, field.name)
            clauses.append(cast(attr, String).ilike(f"%{term}%"))
    return or_(*clauses)

validate(request, data) async

Inherit this method to validate your data.

Parameters:
Name 	Type 	Description 	Default
request 	Request 	

Starlette request
	required
data 	Dict[str, Any] 	

Submitted data
	required

Raises:
Type 	Description
FormValidationError 	

to display errors to users

Examples:

from starlette_admin.contrib.sqla import ModelView
from starlette_admin.exceptions import FormValidationError

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    text = Column(Text, nullable=False)
    date = Column(Date)

class PostView(ModelView):

    async def validate(self, request: Request, data: Dict[str, Any]) -> None:
        errors: Dict[str, str] = dict()
        _2day_from_today = date.today() + timedelta(days=2)
        if data["title"] is None or len(data["title"]) < 3:
            errors["title"] = "Ensure this value has at least 03 characters"
        if data["text"] is None or len(data["text"]) < 10:
            errors["text"] = "Ensure this value has at least 10 characters"
        if data["date"] is None or data["date"] < _2day_from_today:
            errors["date"] = "We need at least one day to verify your post"
        if len(errors) > 0:
            raise FormValidationError(errors)
        return await super().validate(request, data)

Source code in starlette_admin/contrib/sqla/view.py

async def validate(self, request: Request, data: Dict[str, Any]) -> None:
    """
    Inherit this method to validate your data.

    Args:
        request: Starlette request
        data: Submitted data

    Raises:
        FormValidationError: to display errors to users

    Examples:
        python
        from starlette_admin.contrib.sqla import ModelView
        from starlette_admin.exceptions import FormValidationError

        class Post(Base):
            __tablename__ = "post"

            id = Column(Integer, primary_key=True)
            title = Column(String(100), nullable=False)
            text = Column(Text, nullable=False)
            date = Column(Date)

        class PostView(ModelView):

            async def validate(self, request: Request, data: Dict[str, Any]) -> None:
                errors: Dict[str, str] = dict()
                _2day_from_today = date.today() + timedelta(days=2)
                if data["title"] is None or len(data["title"]) < 3:
                    errors["title"] = "Ensure this value has at least 03 characters"
                if data["text"] is None or len(data["text"]) < 10:
                    errors["text"] = "Ensure this value has at least 10 characters"
                if data["date"] is None or data["date"] < _2day_from_today:
                    errors["date"] = "We need at least one day to verify your post"
                if len(errors) > 0:
                    raise FormValidationError(errors)
                return await super().validate(request, data)
        

    """

async def validate(self, request: Request, data: Dict[str, Any]) -> None:
    """
    Inherit this method to validate your data.

    Args:
        request: Starlette request
        data: Submitted data

    Raises:
        FormValidationError: to display errors to users

    Examples:
        python
        from starlette_admin.contrib.sqla import ModelView
        from starlette_admin.exceptions import FormValidationError

        class Post(Base):
            __tablename__ = "post"

            id = Column(Integer, primary_key=True)
            title = Column(String(100), nullable=False)
            text = Column(Text, nullable=False)
            date = Column(Date)

        class PostView(ModelView):

            async def validate(self, request: Request, data: Dict[str, Any]) -> None:
                errors: Dict[str, str] = dict()
                _2day_from_today = date.today() + timedelta(days=2)
                if data["title"] is None or len(data["title"]) < 3:
                    errors["title"] = "Ensure this value has at least 03 characters"
                if data["text"] is None or len(data["text"]) < 10:
                    errors["text"] = "Ensure this value has at least 10 characters"
                if data["date"] is None or data["date"] < _2day_from_today:
                    errors["date"] = "We need at least one day to verify your post"
                if len(errors) > 0:
                    raise FormValidationError(errors)
                return await super().validate(request, data)
        

    """

Fields
starlette_admin.fields
BaseField dataclass

Base class for fields

Parameters:
Name 	Type 	Description 	Default
name 	str 	

Field name, same as attribute name in your model
	required
label 	Optional[str] 	

Field label
	None
help_text 	Optional[str] 	

Hint message to display in forms
	None
type 	Optional[str] 	

Field type, unique key used to define the field
	None
disabled 	Optional[bool] 	

Disabled in forms
	False
read_only 	Optional[bool] 	

Read only in forms
	False
id 	str 	

Unique id, used to represent field instance
	''
search_builder_type 	Optional[str] 	

datatable columns.searchBuilderType, For more information click here
	'default'
required 	Optional[bool] 	

Indicate if the fields is required
	False
exclude_from_list 	Optional[bool] 	

Control field visibility in list page
	False
exclude_from_detail 	Optional[bool] 	

Control field visibility in detail page
	False
exclude_from_create 	Optional[bool] 	

Control field visibility in create page
	False
exclude_from_edit 	Optional[bool] 	

Control field visibility in edit page
	False
searchable 	Optional[bool] 	

Indicate if the fields is searchable
	True
orderable 	Optional[bool] 	

Indicate if the fields is orderable
	True
render_function_key 	str 	

Render function key inside the global render variable in javascript
	'text'
form_template 	str 	

template for rendering this field in creation and edit page
	'forms/input.html'
display_template 	str 	

template for displaying this field in detail page
	'displays/text.html'
Source code in starlette_admin/fields.py

@dataclass
class BaseField:
    """
    Base class for fields

    Parameters:
        name: Field name, same as attribute name in your model
        label: Field label
        help_text: Hint message to display in forms
        type: Field type, unique key used to define the field
        disabled: Disabled in forms
        read_only: Read only in forms
        id: Unique id, used to represent field instance
        search_builder_type: datatable columns.searchBuilderType, For more information
            [click here](https://datatables.net/reference/option/columns.searchBuilderType)
        required: Indicate if the fields is required
        exclude_from_list: Control field visibility in list page
        exclude_from_detail: Control field visibility in detail page
        exclude_from_create: Control field visibility in create page
        exclude_from_edit: Control field visibility in edit page
        searchable: Indicate if the fields is searchable
        orderable: Indicate if the fields is orderable
        render_function_key: Render function key inside the global 'render' variable in javascript
        form_template: template for rendering this field in creation and edit page
        display_template: template for displaying this field in detail page
    """

    name: str
    label: Optional[str] = None
    type: Optional[str] = None
    help_text: Optional[str] = None
    disabled: Optional[bool] = False
    read_only: Optional[bool] = False
    id: str = ""
    search_builder_type: Optional[str] = "default"
    required: Optional[bool] = False
    exclude_from_list: Optional[bool] = False
    exclude_from_detail: Optional[bool] = False
    exclude_from_create: Optional[bool] = False
    exclude_from_edit: Optional[bool] = False
    searchable: Optional[bool] = True
    orderable: Optional[bool] = True
    render_function_key: str = "text"
    form_template: str = "forms/input.html"
    label_template: str = "forms/_label.html"
    display_template: str = "displays/text.html"
    error_class = "is-invalid"

    def __post_init__(self) -> None:
        if self.label is None:
            self.label = self.name.replace("_", " ").capitalize()
        if self.type is None:
            self.type = type(self).__name__
        self.id = self.name

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        """
        Extracts the value of this field from submitted form data.
        """
        return form_data.get(self.id)

    async def parse_obj(self, request: Request, obj: Any) -> Any:
        """Extracts the value of this field from a model instance.

        By default, this function returns the value of the attribute with the name 'self.name' from 'obj'.
        However, this function can be overridden to provide custom logic for computing the value of a field.

        ??? Example

            py
            # Suppose we have a 'User' model with 'id', 'first_name', and 'last_name' fields.
            # We define a custom field called 'MyCustomField' to compute the full name of the user:

            class MyCustomField(StringField):
                async def parse_obj(self, request: Request, obj: Any) -> Any:
                    return f"{obj.first_name} {obj.last_name}"  # Returns the full name of the user

            # Then, We can define our view as follows

            class UserView(ModelView):
                fields = ["id", MyCustomField("full_name")]
            
        """
        return getattr(obj, self.name, None)

    async def serialize_none_value(
        self, request: Request, action: RequestAction
    ) -> Any:
        """Formats a None value for sending to the frontend.

        Args:
            request: The current request object.
            action: The current request action.

        Returns:
            Any: The formatted None value.
        """
        return None

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> Any:
        """Formats a value for sending to the frontend based on the current request action.

        !!! important

            Make sure this value is JSON Serializable for RequestAction.LIST and RequestAction.API

        Args:
            request: The current request object.
            value: The value to format.
            action: The current request action.

        Returns:
            Any: The formatted value.
        """
        return value

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        """Returns a list of CSS file URLs to include for the current request action."""
        return []

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        """Returns a list of JavaScript file URLs to include for the current request action."""
        return []

    def dict(self) -> Dict[str, Any]:
        """Return the dataclass instance as a dictionary."""
        return asdict(self)

    def input_params(self) -> str:
        """Return HTML input parameters as a string."""
        return html_params(
            {
                "disabled": self.disabled,
                "readonly": self.read_only,
            }
        )

Source code in starlette_admin/fields.py

@dataclass
class BaseField:
    """
    Base class for fields

    Parameters:
        name: Field name, same as attribute name in your model
        label: Field label
        help_text: Hint message to display in forms
        type: Field type, unique key used to define the field
        disabled: Disabled in forms
        read_only: Read only in forms
        id: Unique id, used to represent field instance
        search_builder_type: datatable columns.searchBuilderType, For more information
            [click here](https://datatables.net/reference/option/columns.searchBuilderType)
        required: Indicate if the fields is required
        exclude_from_list: Control field visibility in list page
        exclude_from_detail: Control field visibility in detail page
        exclude_from_create: Control field visibility in create page
        exclude_from_edit: Control field visibility in edit page
        searchable: Indicate if the fields is searchable
        orderable: Indicate if the fields is orderable
        render_function_key: Render function key inside the global 'render' variable in javascript
        form_template: template for rendering this field in creation and edit page
        display_template: template for displaying this field in detail page
    """

    name: str
    label: Optional[str] = None
    type: Optional[str] = None
    help_text: Optional[str] = None
    disabled: Optional[bool] = False
    read_only: Optional[bool] = False
    id: str = ""
    search_builder_type: Optional[str] = "default"
    required: Optional[bool] = False
    exclude_from_list: Optional[bool] = False
    exclude_from_detail: Optional[bool] = False
    exclude_from_create: Optional[bool] = False
    exclude_from_edit: Optional[bool] = False
    searchable: Optional[bool] = True
    orderable: Optional[bool] = True
    render_function_key: str = "text"
    form_template: str = "forms/input.html"
    label_template: str = "forms/_label.html"
    display_template: str = "displays/text.html"
    error_class = "is-invalid"

    def __post_init__(self) -> None:
        if self.label is None:
            self.label = self.name.replace("_", " ").capitalize()
        if self.type is None:
            self.type = type(self).__name__
        self.id = self.name

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        """
        Extracts the value of this field from submitted form data.
        """
        return form_data.get(self.id)

    async def parse_obj(self, request: Request, obj: Any) -> Any:
        """Extracts the value of this field from a model instance.

        By default, this function returns the value of the attribute with the name 'self.name' from 'obj'.
        However, this function can be overridden to provide custom logic for computing the value of a field.

        ??? Example

            py
            # Suppose we have a 'User' model with 'id', 'first_name', and 'last_name' fields.
            # We define a custom field called 'MyCustomField' to compute the full name of the user:

            class MyCustomField(StringField):
                async def parse_obj(self, request: Request, obj: Any) -> Any:
                    return f"{obj.first_name} {obj.last_name}"  # Returns the full name of the user

            # Then, We can define our view as follows

            class UserView(ModelView):
                fields = ["id", MyCustomField("full_name")]
            
        """
        return getattr(obj, self.name, None)

    async def serialize_none_value(
        self, request: Request, action: RequestAction
    ) -> Any:
        """Formats a None value for sending to the frontend.

        Args:
            request: The current request object.
            action: The current request action.

        Returns:
            Any: The formatted None value.
        """
        return None

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> Any:
        """Formats a value for sending to the frontend based on the current request action.

        !!! important

            Make sure this value is JSON Serializable for RequestAction.LIST and RequestAction.API

        Args:
            request: The current request object.
            value: The value to format.
            action: The current request action.

        Returns:
            Any: The formatted value.
        """
        return value

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        """Returns a list of CSS file URLs to include for the current request action."""
        return []

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        """Returns a list of JavaScript file URLs to include for the current request action."""
        return []

    def dict(self) -> Dict[str, Any]:
        """Return the dataclass instance as a dictionary."""
        return asdict(self)

    def input_params(self) -> str:
        """Return HTML input parameters as a string."""
        return html_params(
            {
                "disabled": self.disabled,
                "readonly": self.read_only,
            }
        )

additional_css_links(request, action)

Returns a list of CSS file URLs to include for the current request action.
Source code in starlette_admin/fields.py

def additional_css_links(
    self, request: Request, action: RequestAction
) -> List[str]:
    """Returns a list of CSS file URLs to include for the current request action."""
    return []

Source code in starlette_admin/fields.py

def additional_css_links(
    self, request: Request, action: RequestAction
) -> List[str]:
    """Returns a list of CSS file URLs to include for the current request action."""
    return []

additional_js_links(request, action)

Returns a list of JavaScript file URLs to include for the current request action.
Source code in starlette_admin/fields.py

def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
    """Returns a list of JavaScript file URLs to include for the current request action."""
    return []

Source code in starlette_admin/fields.py

def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
    """Returns a list of JavaScript file URLs to include for the current request action."""
    return []

dict()

Return the dataclass instance as a dictionary.
Source code in starlette_admin/fields.py

def dict(self) -> Dict[str, Any]:
    """Return the dataclass instance as a dictionary."""
    return asdict(self)

Source code in starlette_admin/fields.py

def dict(self) -> Dict[str, Any]:
    """Return the dataclass instance as a dictionary."""
    return asdict(self)

input_params()

Return HTML input parameters as a string.
Source code in starlette_admin/fields.py

def input_params(self) -> str:
    """Return HTML input parameters as a string."""
    return html_params(
        {
            "disabled": self.disabled,
            "readonly": self.read_only,
        }
    )

Source code in starlette_admin/fields.py

def input_params(self) -> str:
    """Return HTML input parameters as a string."""
    return html_params(
        {
            "disabled": self.disabled,
            "readonly": self.read_only,
        }
    )

parse_form_data(request, form_data, action) async

Extracts the value of this field from submitted form data.
Source code in starlette_admin/fields.py

async def parse_form_data(
    self, request: Request, form_data: FormData, action: RequestAction
) -> Any:
    """
    Extracts the value of this field from submitted form data.
    """
    return form_data.get(self.id)

Source code in starlette_admin/fields.py

async def parse_form_data(
    self, request: Request, form_data: FormData, action: RequestAction
) -> Any:
    """
    Extracts the value of this field from submitted form data.
    """
    return form_data.get(self.id)

parse_obj(request, obj) async

Extracts the value of this field from a model instance.

By default, this function returns the value of the attribute with the name self.name from obj. However, this function can be overridden to provide custom logic for computing the value of a field.
Example

Example

Source code in starlette_admin/fields.py

async def parse_obj(self, request: Request, obj: Any) -> Any:
    """Extracts the value of this field from a model instance.

    By default, this function returns the value of the attribute with the name 'self.name' from 'obj'.
    However, this function can be overridden to provide custom logic for computing the value of a field.

    ??? Example

        py
        # Suppose we have a 'User' model with 'id', 'first_name', and 'last_name' fields.
        # We define a custom field called 'MyCustomField' to compute the full name of the user:

        class MyCustomField(StringField):
            async def parse_obj(self, request: Request, obj: Any) -> Any:
                return f"{obj.first_name} {obj.last_name}"  # Returns the full name of the user

        # Then, We can define our view as follows

        class UserView(ModelView):
            fields = ["id", MyCustomField("full_name")]
        
    """
    return getattr(obj, self.name, None)

Source code in starlette_admin/fields.py

async def parse_obj(self, request: Request, obj: Any) -> Any:
    """Extracts the value of this field from a model instance.

    By default, this function returns the value of the attribute with the name 'self.name' from 'obj'.
    However, this function can be overridden to provide custom logic for computing the value of a field.

    ??? Example

        py
        # Suppose we have a 'User' model with 'id', 'first_name', and 'last_name' fields.
        # We define a custom field called 'MyCustomField' to compute the full name of the user:

        class MyCustomField(StringField):
            async def parse_obj(self, request: Request, obj: Any) -> Any:
                return f"{obj.first_name} {obj.last_name}"  # Returns the full name of the user

        # Then, We can define our view as follows

        class UserView(ModelView):
            fields = ["id", MyCustomField("full_name")]
        
    """
    return getattr(obj, self.name, None)

serialize_none_value(request, action) async

Formats a None value for sending to the frontend.

Parameters:
Name 	Type 	Description 	Default
request 	Request 	

The current request object.
	required
action 	RequestAction 	

The current request action.
	required

Returns:
Name 	Type 	Description
Any 	Any 	

The formatted None value.
Source code in starlette_admin/fields.py

async def serialize_none_value(
    self, request: Request, action: RequestAction
) -> Any:
    """Formats a None value for sending to the frontend.

    Args:
        request: The current request object.
        action: The current request action.

    Returns:
        Any: The formatted None value.
    """
    return None

Source code in starlette_admin/fields.py

async def serialize_none_value(
    self, request: Request, action: RequestAction
) -> Any:
    """Formats a None value for sending to the frontend.

    Args:
        request: The current request object.
        action: The current request action.

    Returns:
        Any: The formatted None value.
    """
    return None

serialize_value(request, value, action) async

Formats a value for sending to the frontend based on the current request action.

Important

Make sure this value is JSON Serializable for RequestAction.LIST and RequestAction.API

Parameters:
Name 	Type 	Description 	Default
request 	Request 	

The current request object.
	required
value 	Any 	

The value to format.
	required
action 	RequestAction 	

The current request action.
	required

Returns:
Name 	Type 	Description
Any 	Any 	

The formatted value.
Source code in starlette_admin/fields.py

async def serialize_value(
    self, request: Request, value: Any, action: RequestAction
) -> Any:
    """Formats a value for sending to the frontend based on the current request action.

    !!! important

        Make sure this value is JSON Serializable for RequestAction.LIST and RequestAction.API

    Args:
        request: The current request object.
        value: The value to format.
        action: The current request action.

    Returns:
        Any: The formatted value.
    """
    return value

Source code in starlette_admin/fields.py

async def serialize_value(
    self, request: Request, value: Any, action: RequestAction
) -> Any:
    """Formats a value for sending to the frontend based on the current request action.

    !!! important

        Make sure this value is JSON Serializable for RequestAction.LIST and RequestAction.API

    Args:
        request: The current request object.
        value: The value to format.
        action: The current request action.

    Returns:
        Any: The formatted value.
    """
    return value

BooleanField dataclass

Bases: BaseField

This field displays the true/false value of a boolean property.
Source code in starlette_admin/fields.py

@dataclass
class BooleanField(BaseField):
    """This field displays the 'true/false' value of a boolean property."""

    search_builder_type: Optional[str] = "bool"
    render_function_key: str = "boolean"
    form_template: str = "forms/boolean.html"
    display_template: str = "displays/boolean.html"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> bool:
        return form_data.get(self.id) == "on"

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> bool:
        return bool(value)

Source code in starlette_admin/fields.py

@dataclass
class BooleanField(BaseField):
    """This field displays the 'true/false' value of a boolean property."""

    search_builder_type: Optional[str] = "bool"
    render_function_key: str = "boolean"
    form_template: str = "forms/boolean.html"
    display_template: str = "displays/boolean.html"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> bool:
        return form_data.get(self.id) == "on"

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> bool:
        return bool(value)

IntegerField dataclass

Bases: NumberField

This field is used to represent the value of properties that store integer numbers. Erroneous input is ignored and will not be accepted as a value.
Source code in starlette_admin/fields.py

@dataclass
class IntegerField(NumberField):
    """
    This field is used to represent the value of properties that store integer numbers.
    Erroneous input is ignored and will not be accepted as a value."""

    class_: str = "field-integer form-control"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Optional[int]:
        try:
            return int(form_data.get(self.id))  # type: ignore
        except (ValueError, TypeError):
            return None

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> Any:
        return int(value)

Source code in starlette_admin/fields.py

@dataclass
class IntegerField(NumberField):
    """
    This field is used to represent the value of properties that store integer numbers.
    Erroneous input is ignored and will not be accepted as a value."""

    class_: str = "field-integer form-control"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Optional[int]:
        try:
            return int(form_data.get(self.id))  # type: ignore
        except (ValueError, TypeError):
            return None

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> Any:
        return int(value)

DecimalField dataclass

Bases: NumberField

This field is used to represent the value of properties that store decimal numbers. Erroneous input is ignored and will not be accepted as a value.
Source code in starlette_admin/fields.py

@dataclass
class DecimalField(NumberField):
    """
    This field is used to represent the value of properties that store decimal numbers.
    Erroneous input is ignored and will not be accepted as a value.
    """

    step: str = "any"
    class_: str = "field-decimal form-control"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Optional[decimal.Decimal]:
        try:
            return decimal.Decimal(form_data.get(self.id))  # type: ignore
        except (decimal.InvalidOperation, ValueError):
            return None

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> str:
        return str(value)

Source code in starlette_admin/fields.py

@dataclass
class DecimalField(NumberField):
    """
    This field is used to represent the value of properties that store decimal numbers.
    Erroneous input is ignored and will not be accepted as a value.
    """

    step: str = "any"
    class_: str = "field-decimal form-control"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Optional[decimal.Decimal]:
        try:
            return decimal.Decimal(form_data.get(self.id))  # type: ignore
        except (decimal.InvalidOperation, ValueError):
            return None

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> str:
        return str(value)

FloatField dataclass

Bases: StringField

A text field, except all input is coerced to an float. Erroneous input is ignored and will not be accepted as a value.
Source code in starlette_admin/fields.py

@dataclass
class FloatField(StringField):
    """
    A text field, except all input is coerced to an float.
     Erroneous input is ignored and will not be accepted as a value.
    """

    class_: str = "field-float form-control"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Optional[float]:
        try:
            return float(form_data.get(self.id))  # type: ignore
        except ValueError:
            return None

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> float:
        return float(value)

Source code in starlette_admin/fields.py

@dataclass
class FloatField(StringField):
    """
    A text field, except all input is coerced to an float.
     Erroneous input is ignored and will not be accepted as a value.
    """

    class_: str = "field-float form-control"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Optional[float]:
        try:
            return float(form_data.get(self.id))  # type: ignore
        except ValueError:
            return None

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> float:
        return float(value)

StringField dataclass

Bases: BaseField

This field is used to represent any kind of short text content.
Source code in starlette_admin/fields.py

@dataclass
class StringField(BaseField):
    """This field is used to represent any kind of short text content."""

    maxlength: Optional[int] = None
    minlength: Optional[int] = None
    search_builder_type: Optional[str] = "string"
    input_type: str = "text"
    class_: str = "field-string form-control"
    placeholder: Optional[str] = None

    def input_params(self) -> str:
        return html_params(
            {
                "type": self.input_type,
                "minlength": self.minlength,
                "maxlength": self.maxlength,
                "placeholder": self.placeholder,
                "required": self.required,
                "disabled": self.disabled,
                "readonly": self.read_only,
            }
        )

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> Any:
        return str(value)

Source code in starlette_admin/fields.py

@dataclass
class StringField(BaseField):
    """This field is used to represent any kind of short text content."""

    maxlength: Optional[int] = None
    minlength: Optional[int] = None
    search_builder_type: Optional[str] = "string"
    input_type: str = "text"
    class_: str = "field-string form-control"
    placeholder: Optional[str] = None

    def input_params(self) -> str:
        return html_params(
            {
                "type": self.input_type,
                "minlength": self.minlength,
                "maxlength": self.maxlength,
                "placeholder": self.placeholder,
                "required": self.required,
                "disabled": self.disabled,
                "readonly": self.read_only,
            }
        )

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> Any:
        return str(value)

TextAreaField dataclass

Bases: StringField

This field is used to represent any kind of long text content. For short text contents, use StringField
Source code in starlette_admin/fields.py

@dataclass
class TextAreaField(StringField):
    """This field is used to represent any kind of long text content.
    For short text contents, use [StringField][starlette_admin.fields.StringField]"""

    rows: int = 6
    class_: str = "field-textarea form-control"
    form_template: str = "forms/textarea.html"
    display_template: str = "displays/textarea.html"

    def input_params(self) -> str:
        return html_params(
            {
                "rows": self.rows,
                "minlength": self.minlength,
                "maxlength": self.maxlength,
                "placeholder": self.placeholder,
                "required": self.required,
                "disabled": self.disabled,
                "readonly": self.read_only,
            }
        )

Source code in starlette_admin/fields.py

@dataclass
class TextAreaField(StringField):
    """This field is used to represent any kind of long text content.
    For short text contents, use [StringField][starlette_admin.fields.StringField]"""

    rows: int = 6
    class_: str = "field-textarea form-control"
    form_template: str = "forms/textarea.html"
    display_template: str = "displays/textarea.html"

    def input_params(self) -> str:
        return html_params(
            {
                "rows": self.rows,
                "minlength": self.minlength,
                "maxlength": self.maxlength,
                "placeholder": self.placeholder,
                "required": self.required,
                "disabled": self.disabled,
                "readonly": self.read_only,
            }
        )

TinyMCEEditorField dataclass

Bases: TextAreaField

A field that provides a WYSIWYG editor for long text content using the TinyMCE library.

This field can be used as an alternative to the TextAreaField to provide a more sophisticated editor for user input.

Parameters:
Name 	Type 	Description 	Default
version_tinymce 	str 	

TinyMCE version
	'6.4'
version_tinymce_jquery 	str 	

TinyMCE jQuery version
	'2.0'
height 	int 	

Height of the editor
	300
menubar 	Union[bool, str] 	

Show/hide the menubar in the editor
	False
statusbar 	bool 	

Show/hide the statusbar in the editor
	False
toolbar 	str 	

Toolbar options to show in the editor
	'undo redo | formatselect | bold italic backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat'
content_style 	str 	

CSS style to apply to the editor content
	'body { font-family: -apple-system, BlinkMacSystemFont, San Francisco, Segoe UI, Roboto, Helvetica Neue, sans-serif; font-size: 14px; -webkit-font-smoothing: antialiased; }'
extra_options 	Dict[str, Any] 	

Other options to pass to TinyMCE
	dict()
Source code in starlette_admin/fields.py

@dataclass
class TinyMCEEditorField(TextAreaField):
    """A field that provides a WYSIWYG editor for long text content using the
     [TinyMCE](https://www.tiny.cloud/) library.

    This field can be used as an alternative to the [TextAreaField][starlette_admin.fields.TextAreaField]
    to provide a more sophisticated editor for user input.

    Parameters:
        version_tinymce: TinyMCE version
        version_tinymce_jquery: TinyMCE jQuery version
        height: Height of the editor
        menubar: Show/hide the menubar in the editor
        statusbar: Show/hide the statusbar in the editor
        toolbar: Toolbar options to show in the editor
        content_style: CSS style to apply to the editor content
        extra_options: Other options to pass to TinyMCE
    """

    class_: str = "field-tinymce-editor form-control"
    display_template: str = "displays/tinymce.html"
    version_tinymce: str = "6.4"
    version_tinymce_jquery: str = "2.0"
    height: int = 300
    menubar: Union[bool, str] = False
    statusbar: bool = False
    toolbar: str = (
        "undo redo | formatselect | bold italic backcolor | alignleft aligncenter"
        " alignright alignjustify | bullist numlist outdent indent | removeformat"
    )
    content_style: str = (
        "body { font-family: -apple-system, BlinkMacSystemFont, San Francisco, Segoe"
        " UI, Roboto, Helvetica Neue, sans-serif; font-size: 14px;"
        " -webkit-font-smoothing: antialiased; }"
    )
    extra_options: Dict[str, Any] = dc_field(default_factory=dict)
    """For more options, see the [TinyMCE | Documentation](https://www.tiny.cloud/docs/tinymce/6/)"""

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        if action.is_form():
            return [
                f"https://cdn.jsdelivr.net/npm/tinymce@{self.version_tinymce}/tinymce.min.js",
                f"https://cdn.jsdelivr.net/npm/@tinymce/tinymce-jquery@{self.version_tinymce_jquery}/dist/tinymce-jquery.min.js",
            ]
        return []

    def input_params(self) -> str:
        _options = {
            "height": self.height,
            "menubar": self.menubar,
            "statusbar": self.statusbar,
            "toolbar": self.toolbar,
            "content_style": self.content_style,
            **self.extra_options,
        }

        return (
            super().input_params()
            + " "
            + html_params({"data-options": json.dumps(_options)})
        )

Source code in starlette_admin/fields.py

@dataclass
class TinyMCEEditorField(TextAreaField):
    """A field that provides a WYSIWYG editor for long text content using the
     [TinyMCE](https://www.tiny.cloud/) library.

    This field can be used as an alternative to the [TextAreaField][starlette_admin.fields.TextAreaField]
    to provide a more sophisticated editor for user input.

    Parameters:
        version_tinymce: TinyMCE version
        version_tinymce_jquery: TinyMCE jQuery version
        height: Height of the editor
        menubar: Show/hide the menubar in the editor
        statusbar: Show/hide the statusbar in the editor
        toolbar: Toolbar options to show in the editor
        content_style: CSS style to apply to the editor content
        extra_options: Other options to pass to TinyMCE
    """

    class_: str = "field-tinymce-editor form-control"
    display_template: str = "displays/tinymce.html"
    version_tinymce: str = "6.4"
    version_tinymce_jquery: str = "2.0"
    height: int = 300
    menubar: Union[bool, str] = False
    statusbar: bool = False
    toolbar: str = (
        "undo redo | formatselect | bold italic backcolor | alignleft aligncenter"
        " alignright alignjustify | bullist numlist outdent indent | removeformat"
    )
    content_style: str = (
        "body { font-family: -apple-system, BlinkMacSystemFont, San Francisco, Segoe"
        " UI, Roboto, Helvetica Neue, sans-serif; font-size: 14px;"
        " -webkit-font-smoothing: antialiased; }"
    )
    extra_options: Dict[str, Any] = dc_field(default_factory=dict)
    """For more options, see the [TinyMCE | Documentation](https://www.tiny.cloud/docs/tinymce/6/)"""

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        if action.is_form():
            return [
                f"https://cdn.jsdelivr.net/npm/tinymce@{self.version_tinymce}/tinymce.min.js",
                f"https://cdn.jsdelivr.net/npm/@tinymce/tinymce-jquery@{self.version_tinymce_jquery}/dist/tinymce-jquery.min.js",
            ]
        return []

    def input_params(self) -> str:
        _options = {
            "height": self.height,
            "menubar": self.menubar,
            "statusbar": self.statusbar,
            "toolbar": self.toolbar,
            "content_style": self.content_style,
            **self.extra_options,
        }

        return (
            super().input_params()
            + " "
            + html_params({"data-options": json.dumps(_options)})
        )

extra_options = dc_field(default_factory=dict) class-attribute instance-attribute

For more options, see the TinyMCE | Documentation
TagsField dataclass

Bases: BaseField

This field is used to represent the value of properties that store a list of string values. Render as select2 tags input.
Source code in starlette_admin/fields.py

@dataclass
class TagsField(BaseField):
    """
    This field is used to represent the value of properties that store a list of
    string values. Render as 'select2' tags input.
    """

    form_template: str = "forms/tags.html"
    form_js: str = "js/field/forms/tags.js"
    class_: str = "field-tags form-control form-select"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> List[str]:
        return form_data.getlist(self.id)  # type: ignore

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        if action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="css/select2.min.css",
                    )
                )
            ]
        return []

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        if action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="js/vendor/select2.min.js",
                    )
                )
            ]
        return []

Source code in starlette_admin/fields.py

@dataclass
class TagsField(BaseField):
    """
    This field is used to represent the value of properties that store a list of
    string values. Render as 'select2' tags input.
    """

    form_template: str = "forms/tags.html"
    form_js: str = "js/field/forms/tags.js"
    class_: str = "field-tags form-control form-select"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> List[str]:
        return form_data.getlist(self.id)  # type: ignore

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        if action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="css/select2.min.css",
                    )
                )
            ]
        return []

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        if action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="js/vendor/select2.min.js",
                    )
                )
            ]
        return []

EmailField dataclass

Bases: StringField

This field is used to represent a text content that stores a single email address.
Source code in starlette_admin/fields.py

@dataclass
class EmailField(StringField):
    """This field is used to represent a text content
    that stores a single email address."""

    input_type: str = "email"
    render_function_key: str = "email"
    class_: str = "field-email form-control"
    display_template: str = "displays/email.html"

Source code in starlette_admin/fields.py

@dataclass
class EmailField(StringField):
    """This field is used to represent a text content
    that stores a single email address."""

    input_type: str = "email"
    render_function_key: str = "email"
    class_: str = "field-email form-control"
    display_template: str = "displays/email.html"

URLField dataclass

Bases: StringField

This field is used to represent a text content that stores a single URL.
Source code in starlette_admin/fields.py

@dataclass
class URLField(StringField):
    """This field is used to represent a text content that stores a single URL."""

    input_type: str = "url"
    render_function_key: str = "url"
    class_: str = "field-url form-control"
    display_template: str = "displays/url.html"

Source code in starlette_admin/fields.py

@dataclass
class URLField(StringField):
    """This field is used to represent a text content that stores a single URL."""

    input_type: str = "url"
    render_function_key: str = "url"
    class_: str = "field-url form-control"
    display_template: str = "displays/url.html"

PhoneField dataclass

Bases: StringField

A StringField, except renders an <input type="phone">.
Source code in starlette_admin/fields.py

@dataclass
class PhoneField(StringField):
    """A StringField, except renders an '<input type="phone">'."""

    input_type: str = "phone"
    class_: str = "field-phone form-control"

Source code in starlette_admin/fields.py

@dataclass
class PhoneField(StringField):
    """A StringField, except renders an '<input type="phone">'."""

    input_type: str = "phone"
    class_: str = "field-phone form-control"

ColorField dataclass

Bases: StringField

A StringField, except renders an <input type="color">.
Source code in starlette_admin/fields.py

@dataclass
class ColorField(StringField):
    """A StringField, except renders an '<input type="color">'."""

    input_type: str = "color"
    class_: str = "field-color form-control form-control-color"

Source code in starlette_admin/fields.py

@dataclass
class ColorField(StringField):
    """A StringField, except renders an '<input type="color">'."""

    input_type: str = "color"
    class_: str = "field-color form-control form-control-color"

PasswordField dataclass

Bases: StringField

A StringField, except renders an <input type="password">.
Source code in starlette_admin/fields.py

@dataclass
class PasswordField(StringField):
    """A StringField, except renders an '<input type="password">'."""

    input_type: str = "password"
    class_: str = "field-password form-control"

Source code in starlette_admin/fields.py

@dataclass
class PasswordField(StringField):
    """A StringField, except renders an '<input type="password">'."""

    input_type: str = "password"
    class_: str = "field-password form-control"

EnumField dataclass

Bases: StringField

Enumeration Field. It takes a python enum.Enum class or a list of (value, label) pairs. It can also be a list of only values, in which case the value is used as the label. Example:

class Status(str, enum.Enum):
    NEW = "new"
    ONGOING = "ongoing"
    DONE = "done"

class MyModel:
    status: Optional[Status] = None

class MyModelView(ModelView):
    fields = [EnumField("status", enum=Status)]

python
class MyModel:
    language: str

class MyModelView(ModelView):
    fields = [
        EnumField(
            "language",
            choices=[("cpp", "C++"), ("py", "Python"), ("text", "Plain Text")],
        )
    ]

Source code in starlette_admin/fields.py

@dataclass
class EnumField(StringField):
    """
    Enumeration Field.
    It takes a python 'enum.Enum' class or a list of *(value, label)* pairs.
    It can also be a list of only values, in which case the value is used as the label.
    Example:
        python
        class Status(str, enum.Enum):
            NEW = "new"
            ONGOING = "ongoing"
            DONE = "done"

        class MyModel:
            status: Optional[Status] = None

        class MyModelView(ModelView):
            fields = [EnumField("status", enum=Status)]
        

        python
        class MyModel:
            language: str

        class MyModelView(ModelView):
            fields = [
                EnumField(
                    "language",
                    choices=[("cpp", "C++"), ("py", "Python"), ("text", "Plain Text")],
                )
            ]
        
    """

    multiple: bool = False
    enum: Optional[Type[Enum]] = None
    choices: Union[Sequence[str], Sequence[Tuple[Any, str]], None] = None
    choices_loader: Optional[
        Callable[[Request], Union[Sequence[str], Sequence[Tuple[Any, str]]]]
    ] = dc_field(default=None, compare=False)
    form_template: str = "forms/enum.html"
    class_: str = "field-enum form-control form-select"
    coerce: Callable[[Any], Any] = str
    select2: bool = True

    def __post_init__(self) -> None:
        if self.choices and not isinstance(self.choices[0], (list, tuple)):
            self.choices = list(zip(self.choices, self.choices))  # type: ignore
        elif self.enum:
            self.choices = [(e.value, e.name.replace("_", " ")) for e in self.enum]
            self.coerce = int if issubclass(self.enum, IntEnum) else str
        elif not self.choices and self.choices_loader is None:
            raise ValueError(
                "EnumField required a list of choices, enum class or a choices_loader for dynamic choices"
            )
        super().__post_init__()

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        return (
            list(map(self.coerce, form_data.getlist(self.id)))
            if self.multiple
            else (
                self.coerce(form_data.get(self.id)) if form_data.get(self.id) else None
            )
        )

    def _get_choices(self, request: Request) -> Any:
        return (
            self.choices
            if self.choices_loader is None
            else self.choices_loader(request)
        )

    def _get_label(self, value: Any, request: Request) -> Any:
        for v, label in self._get_choices(request):
            if value == v:
                return label
        raise ValueError(f"Invalid choice value: {value}")

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> Any:
        if isinstance(value, Enum):
            value = value.value
        labels = [
            (self._get_label(v, request) if action != RequestAction.EDIT else v)
            for v in (value if self.multiple else [value])
        ]
        return labels if self.multiple else labels[0]

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        if self.select2 and action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="css/select2.min.css",
                    )
                )
            ]
        return []

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        if self.select2 and action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="js/vendor/select2.min.js",
                    )
                )
            ]
        return []

    @classmethod
    def from_enum(
        cls,
        name: str,
        enum_type: Type[Enum],
        multiple: bool = False,
        **kwargs: Dict[str, Any],
    ) -> "EnumField":
        warnings.warn(
            f'This method is deprecated. Use EnumField("name", enum={enum_type.__name__}) instead.',
            DeprecationWarning,
            stacklevel=1,
        )
        return cls(name, enum=enum_type, multiple=multiple, **kwargs)  # type: ignore

    @classmethod
    def from_choices(
        cls,
        name: str,
        choices: Union[Sequence[str], Sequence[Tuple[str, str]], None],
        multiple: bool = False,
        **kwargs: Dict[str, Any],
    ) -> "EnumField":
        warnings.warn(
            f'This method is deprecated. Use EnumField("name", choices={choices}) instead.',
            DeprecationWarning,
            stacklevel=1,
        )
        return cls(name, choices=choices, multiple=multiple, **kwargs)  # type: ignore

Source code in starlette_admin/fields.py

@dataclass
class EnumField(StringField):
    """
    Enumeration Field.
    It takes a python 'enum.Enum' class or a list of *(value, label)* pairs.
    It can also be a list of only values, in which case the value is used as the label.
    Example:
        python
        class Status(str, enum.Enum):
            NEW = "new"
            ONGOING = "ongoing"
            DONE = "done"

        class MyModel:
            status: Optional[Status] = None

        class MyModelView(ModelView):
            fields = [EnumField("status", enum=Status)]
        

        python
        class MyModel:
            language: str

        class MyModelView(ModelView):
            fields = [
                EnumField(
                    "language",
                    choices=[("cpp", "C++"), ("py", "Python"), ("text", "Plain Text")],
                )
            ]
        
    """

    multiple: bool = False
    enum: Optional[Type[Enum]] = None
    choices: Union[Sequence[str], Sequence[Tuple[Any, str]], None] = None
    choices_loader: Optional[
        Callable[[Request], Union[Sequence[str], Sequence[Tuple[Any, str]]]]
    ] = dc_field(default=None, compare=False)
    form_template: str = "forms/enum.html"
    class_: str = "field-enum form-control form-select"
    coerce: Callable[[Any], Any] = str
    select2: bool = True

    def __post_init__(self) -> None:
        if self.choices and not isinstance(self.choices[0], (list, tuple)):
            self.choices = list(zip(self.choices, self.choices))  # type: ignore
        elif self.enum:
            self.choices = [(e.value, e.name.replace("_", " ")) for e in self.enum]
            self.coerce = int if issubclass(self.enum, IntEnum) else str
        elif not self.choices and self.choices_loader is None:
            raise ValueError(
                "EnumField required a list of choices, enum class or a choices_loader for dynamic choices"
            )
        super().__post_init__()

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        return (
            list(map(self.coerce, form_data.getlist(self.id)))
            if self.multiple
            else (
                self.coerce(form_data.get(self.id)) if form_data.get(self.id) else None
            )
        )

    def _get_choices(self, request: Request) -> Any:
        return (
            self.choices
            if self.choices_loader is None
            else self.choices_loader(request)
        )

    def _get_label(self, value: Any, request: Request) -> Any:
        for v, label in self._get_choices(request):
            if value == v:
                return label
        raise ValueError(f"Invalid choice value: {value}")

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> Any:
        if isinstance(value, Enum):
            value = value.value
        labels = [
            (self._get_label(v, request) if action != RequestAction.EDIT else v)
            for v in (value if self.multiple else [value])
        ]
        return labels if self.multiple else labels[0]

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        if self.select2 and action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="css/select2.min.css",
                    )
                )
            ]
        return []

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        if self.select2 and action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="js/vendor/select2.min.js",
                    )
                )
            ]
        return []

    @classmethod
    def from_enum(
        cls,
        name: str,
        enum_type: Type[Enum],
        multiple: bool = False,
        **kwargs: Dict[str, Any],
    ) -> "EnumField":
        warnings.warn(
            f'This method is deprecated. Use EnumField("name", enum={enum_type.__name__}) instead.',
            DeprecationWarning,
            stacklevel=1,
        )
        return cls(name, enum=enum_type, multiple=multiple, **kwargs)  # type: ignore

    @classmethod
    def from_choices(
        cls,
        name: str,
        choices: Union[Sequence[str], Sequence[Tuple[str, str]], None],
        multiple: bool = False,
        **kwargs: Dict[str, Any],
    ) -> "EnumField":
        warnings.warn(
            f'This method is deprecated. Use EnumField("name", choices={choices}) instead.',
            DeprecationWarning,
            stacklevel=1,
        )
        return cls(name, choices=choices, multiple=multiple, **kwargs)  # type: ignore

TimeZoneField dataclass

Bases: EnumField

This field is used to represent the name of a timezone (eg. Africa/Porto-Novo)
Source code in starlette_admin/fields.py

@dataclass
class TimeZoneField(EnumField):
    """This field is used to represent the name of a timezone (eg. Africa/Porto-Novo)"""

    def __post_init__(self) -> None:
        if self.choices is None:
            self.choices = [
                (self.coerce(x), x.replace("_", " ")) for x in common_timezones
            ]
        super().__post_init__()

Source code in starlette_admin/fields.py

@dataclass
class TimeZoneField(EnumField):
    """This field is used to represent the name of a timezone (eg. Africa/Porto-Novo)"""

    def __post_init__(self) -> None:
        if self.choices is None:
            self.choices = [
                (self.coerce(x), x.replace("_", " ")) for x in common_timezones
            ]
        super().__post_init__()

CountryField dataclass

Bases: EnumField

This field is used to represent the name that corresponds to the country code stored in your database
Source code in starlette_admin/fields.py

@dataclass
class CountryField(EnumField):
    """This field is used to represent the name that corresponds to the country code stored in your database"""

    def __post_init__(self) -> None:
        try:
            import babel  # noqa
        except ImportError as err:
            raise ImportError(
                "'babel' package is required to use 'CountryField'. Install it with 'pip install starlette-admin[i18n]'"
            ) from err
        self.choices_loader = lambda request: get_countries_list()
        super().__post_init__()

Source code in starlette_admin/fields.py

@dataclass
class CountryField(EnumField):
    """This field is used to represent the name that corresponds to the country code stored in your database"""

    def __post_init__(self) -> None:
        try:
            import babel  # noqa
        except ImportError as err:
            raise ImportError(
                "'babel' package is required to use 'CountryField'. Install it with 'pip install starlette-admin[i18n]'"
            ) from err
        self.choices_loader = lambda request: get_countries_list()
        super().__post_init__()

CurrencyField dataclass

Bases: EnumField

This field is used to represent a value that stores the 3-letter ISO 4217 code of currency
Source code in starlette_admin/fields.py

@dataclass
class CurrencyField(EnumField):
    """
    This field is used to represent a value that stores the
    [3-letter ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code of currency
    """

    def __post_init__(self) -> None:
        try:
            import babel  # noqa
        except ImportError as err:
            raise ImportError(
                "'babel' package is required to use 'CurrencyField'. Install it with 'pip install starlette-admin[i18n]'"
            ) from err
        self.choices_loader = lambda request: get_currencies_list()
        super().__post_init__()

Source code in starlette_admin/fields.py

@dataclass
class CurrencyField(EnumField):
    """
    This field is used to represent a value that stores the
    [3-letter ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code of currency
    """

    def __post_init__(self) -> None:
        try:
            import babel  # noqa
        except ImportError as err:
            raise ImportError(
                "'babel' package is required to use 'CurrencyField'. Install it with 'pip install starlette-admin[i18n]'"
            ) from err
        self.choices_loader = lambda request: get_currencies_list()
        super().__post_init__()

DateTimeField dataclass

Bases: NumberField

This field is used to represent a value that stores a python datetime.datetime object Parameters: search_format: moment.js format to send for searching. Use None for iso Format output_format: display output format
Source code in starlette_admin/fields.py

@dataclass
class DateTimeField(NumberField):
    """
    This field is used to represent a value that stores a python datetime.datetime object
    Parameters:
        search_format: moment.js format to send for searching. Use None for iso Format
        output_format: display output format
    """

    input_type: str = "datetime-local"
    class_: str = "field-datetime form-control"
    search_builder_type: str = "moment-LL LT"
    output_format: Optional[str] = None
    search_format: Optional[str] = None
    form_alt_format: Optional[str] = "F j, Y  H:i:S"

    def input_params(self) -> str:
        return html_params(
            {
                "type": self.input_type,
                "min": self.min,
                "max": self.max,
                "step": self.step,
                "data_alt_format": self.form_alt_format,
                "data_locale": get_locale(),
                "placeholder": self.placeholder,
                "required": self.required,
                "disabled": self.disabled,
                "readonly": self.read_only,
            }
        )

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Union[datetime, None]:
        try:
            dt = datetime.fromisoformat(form_data.get(self.id))  # type: ignore
        except (TypeError, ValueError):
            return None

        # Preserve pre-timezone conversion behaviour
        if not is_timezone_conversion_enabled():
            return dt

        if dt.tzinfo is not None:
            database_tz = get_database_tzinfo()
            return dt.astimezone(database_tz).replace(tzinfo=None)

        # Native datetime, assume it's in the user's timezone
        user_tz = get_tzinfo()
        database_tz = get_database_tzinfo()

        return dt.replace(tzinfo=user_tz).astimezone(database_tz).replace(tzinfo=None)

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> str:
        assert isinstance(value, datetime), f"Expected datetime, got {type(value)}"

        # Preserve pre-timezone conversion behaviour
        if not is_timezone_conversion_enabled():
            if action != RequestAction.EDIT:
                return format_datetime(value, self.output_format)
            return value.isoformat()

        user_tz = get_tzinfo()

        if value.tzinfo is None:
            # native datetime from db, assume it's in database timezone
            database_tz = get_database_tzinfo()
            value = value.replace(tzinfo=database_tz)

        if action != RequestAction.EDIT:
            return format_datetime(value, self.output_format, user_tz)

        # For EDIT action, convert to user timezone and return as naive datetime for datetime-local input
        converted_value = value.astimezone(user_tz)
        return converted_value.replace(tzinfo=None).isoformat()

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        if action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="css/flatpickr.min.css",
                    )
                )
            ]
        return []

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        _links = [
            str(
                request.url_for(
                    f"{request.app.state.ROUTE_NAME}:statics",
                    path="js/vendor/flatpickr.min.js",
                )
            )
        ]
        if get_locale() != "en":
            _links.append(
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path=f"i18n/flatpickr/{get_locale()}.js",
                    )
                )
            )
        if action.is_form():
            return _links
        return []

Source code in starlette_admin/fields.py

@dataclass
class DateTimeField(NumberField):
    """
    This field is used to represent a value that stores a python datetime.datetime object
    Parameters:
        search_format: moment.js format to send for searching. Use None for iso Format
        output_format: display output format
    """

    input_type: str = "datetime-local"
    class_: str = "field-datetime form-control"
    search_builder_type: str = "moment-LL LT"
    output_format: Optional[str] = None
    search_format: Optional[str] = None
    form_alt_format: Optional[str] = "F j, Y  H:i:S"

    def input_params(self) -> str:
        return html_params(
            {
                "type": self.input_type,
                "min": self.min,
                "max": self.max,
                "step": self.step,
                "data_alt_format": self.form_alt_format,
                "data_locale": get_locale(),
                "placeholder": self.placeholder,
                "required": self.required,
                "disabled": self.disabled,
                "readonly": self.read_only,
            }
        )

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Union[datetime, None]:
        try:
            dt = datetime.fromisoformat(form_data.get(self.id))  # type: ignore
        except (TypeError, ValueError):
            return None

        # Preserve pre-timezone conversion behaviour
        if not is_timezone_conversion_enabled():
            return dt

        if dt.tzinfo is not None:
            database_tz = get_database_tzinfo()
            return dt.astimezone(database_tz).replace(tzinfo=None)

        # Native datetime, assume it's in the user's timezone
        user_tz = get_tzinfo()
        database_tz = get_database_tzinfo()

        return dt.replace(tzinfo=user_tz).astimezone(database_tz).replace(tzinfo=None)

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> str:
        assert isinstance(value, datetime), f"Expected datetime, got {type(value)}"

        # Preserve pre-timezone conversion behaviour
        if not is_timezone_conversion_enabled():
            if action != RequestAction.EDIT:
                return format_datetime(value, self.output_format)
            return value.isoformat()

        user_tz = get_tzinfo()

        if value.tzinfo is None:
            # native datetime from db, assume it's in database timezone
            database_tz = get_database_tzinfo()
            value = value.replace(tzinfo=database_tz)

        if action != RequestAction.EDIT:
            return format_datetime(value, self.output_format, user_tz)

        # For EDIT action, convert to user timezone and return as naive datetime for datetime-local input
        converted_value = value.astimezone(user_tz)
        return converted_value.replace(tzinfo=None).isoformat()

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        if action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="css/flatpickr.min.css",
                    )
                )
            ]
        return []

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        _links = [
            str(
                request.url_for(
                    f"{request.app.state.ROUTE_NAME}:statics",
                    path="js/vendor/flatpickr.min.js",
                )
            )
        ]
        if get_locale() != "en":
            _links.append(
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path=f"i18n/flatpickr/{get_locale()}.js",
                    )
                )
            )
        if action.is_form():
            return _links
        return []

DateField dataclass

Bases: DateTimeField

This field is used to represent a value that stores a python datetime.date object Parameters: search_format: moment.js format to send for searching. Use None for iso Format output_format: Set display output format
Source code in starlette_admin/fields.py

@dataclass
class DateField(DateTimeField):
    """
    This field is used to represent a value that stores a python datetime.date object
    Parameters:
        search_format: moment.js format to send for searching. Use None for iso Format
        output_format: Set display output format
    """

    input_type: str = "date"
    class_: str = "field-date form-control"
    output_format: Optional[str] = None
    search_format: str = "YYYY-MM-DD"
    search_builder_type: str = "moment-LL"
    form_alt_format: Optional[str] = "F j, Y"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        try:
            return date.fromisoformat(form_data.get(self.id))  # type: ignore
        except (TypeError, ValueError):
            return None

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> str:
        assert isinstance(value, date), f"Expect date, got  {type(value)}"
        if action != RequestAction.EDIT:
            return format_date(value, self.output_format)
        return value.isoformat()

Source code in starlette_admin/fields.py

@dataclass
class DateField(DateTimeField):
    """
    This field is used to represent a value that stores a python datetime.date object
    Parameters:
        search_format: moment.js format to send for searching. Use None for iso Format
        output_format: Set display output format
    """

    input_type: str = "date"
    class_: str = "field-date form-control"
    output_format: Optional[str] = None
    search_format: str = "YYYY-MM-DD"
    search_builder_type: str = "moment-LL"
    form_alt_format: Optional[str] = "F j, Y"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        try:
            return date.fromisoformat(form_data.get(self.id))  # type: ignore
        except (TypeError, ValueError):
            return None

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> str:
        assert isinstance(value, date), f"Expect date, got  {type(value)}"
        if action != RequestAction.EDIT:
            return format_date(value, self.output_format)
        return value.isoformat()

TimeField dataclass

Bases: DateTimeField

This field is used to represent a value that stores a python datetime.time object Parameters: search_format: Format to send for search. Use None for iso Format output_format: Set display output format
Source code in starlette_admin/fields.py

@dataclass
class TimeField(DateTimeField):
    """
    This field is used to represent a value that stores a python datetime.time object
    Parameters:
        search_format: Format to send for search. Use None for iso Format
        output_format: Set display output format
    """

    input_type: str = "time"
    class_: str = "field-time form-control"
    search_builder_type: str = "moment-LTS"
    output_format: Optional[str] = None
    search_format: str = "HH:mm:ss"
    form_alt_format: Optional[str] = "H:i:S"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        try:
            return time.fromisoformat(form_data.get(self.id))  # type: ignore
        except (TypeError, ValueError):
            return None

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> str:
        assert isinstance(value, time), f"Expect time, got  {type(value)}"
        if action != RequestAction.EDIT:
            return format_time(value, self.output_format)
        return value.isoformat()

Source code in starlette_admin/fields.py

@dataclass
class TimeField(DateTimeField):
    """
    This field is used to represent a value that stores a python datetime.time object
    Parameters:
        search_format: Format to send for search. Use None for iso Format
        output_format: Set display output format
    """

    input_type: str = "time"
    class_: str = "field-time form-control"
    search_builder_type: str = "moment-LTS"
    output_format: Optional[str] = None
    search_format: str = "HH:mm:ss"
    form_alt_format: Optional[str] = "H:i:S"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        try:
            return time.fromisoformat(form_data.get(self.id))  # type: ignore
        except (TypeError, ValueError):
            return None

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> str:
        assert isinstance(value, time), f"Expect time, got  {type(value)}"
        if action != RequestAction.EDIT:
            return format_time(value, self.output_format)
        return value.isoformat()

ArrowField dataclass

Bases: DateTimeField

This field is used to represent sqlalchemy_utils.types.arrow.ArrowType
Source code in starlette_admin/fields.py

@dataclass
class ArrowField(DateTimeField):
    """
    This field is used to represent sqlalchemy_utils.types.arrow.ArrowType
    """

    def __post_init__(self) -> None:
        if not arrow:  # pragma: no cover
            raise ImportError("'arrow' package is required to use 'ArrowField'")
        super().__post_init__()

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        # Preserve pre-timezone conversion behaviour
        if not is_timezone_conversion_enabled():
            try:
                return arrow.get(form_data.get(self.id))  # type: ignore
            except (TypeError, arrow.parser.ParserError):  # pragma: no cover
                return None

        dt = await super().parse_form_data(request, form_data, action)
        if dt is None:
            return None

        return arrow.get(dt)

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> str:
        assert isinstance(value, arrow.Arrow), f"Expected Arrow, got  {type(value)}"

        # Preserve pre-timezone conversion behaviour
        if not is_timezone_conversion_enabled():
            if action != RequestAction.EDIT:
                return value.humanize(locale=get_locale())

            return value.isoformat()

        if action != RequestAction.EDIT:
            user_tz = get_tzinfo()
            return value.to(user_tz).humanize(locale=get_locale())

        return await super().serialize_value(request, value.datetime, action)

Source code in starlette_admin/fields.py

@dataclass
class ArrowField(DateTimeField):
    """
    This field is used to represent sqlalchemy_utils.types.arrow.ArrowType
    """

    def __post_init__(self) -> None:
        if not arrow:  # pragma: no cover
            raise ImportError("'arrow' package is required to use 'ArrowField'")
        super().__post_init__()

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        # Preserve pre-timezone conversion behaviour
        if not is_timezone_conversion_enabled():
            try:
                return arrow.get(form_data.get(self.id))  # type: ignore
            except (TypeError, arrow.parser.ParserError):  # pragma: no cover
                return None

        dt = await super().parse_form_data(request, form_data, action)
        if dt is None:
            return None

        return arrow.get(dt)

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> str:
        assert isinstance(value, arrow.Arrow), f"Expected Arrow, got  {type(value)}"

        # Preserve pre-timezone conversion behaviour
        if not is_timezone_conversion_enabled():
            if action != RequestAction.EDIT:
                return value.humanize(locale=get_locale())

            return value.isoformat()

        if action != RequestAction.EDIT:
            user_tz = get_tzinfo()
            return value.to(user_tz).humanize(locale=get_locale())

        return await super().serialize_value(request, value.datetime, action)

JSONField dataclass

Bases: BaseField

This field render jsoneditor and represent a value that stores python dict object. Erroneous input is ignored and will not be accepted as a value.
Source code in starlette_admin/fields.py

@dataclass
class JSONField(BaseField):
    """
    This field render jsoneditor and represent a value that stores python dict object.
    Erroneous input is ignored and will not be accepted as a value."""

    height: str = "20em"
    modes: Optional[Sequence[str]] = None
    render_function_key: str = "json"
    form_template: str = "forms/json.html"
    display_template: str = "displays/json.html"

    def __post_init__(self) -> None:
        if self.modes is None:
            self.modes = ["view"] if self.read_only else ["tree", "code"]
        super().__post_init__()

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Optional[Dict[str, Any]]:
        try:
            value = form_data.get(self.id)
            return json.loads(value) if value is not None else None  # type: ignore
        except JSONDecodeError:
            return None

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        if action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="css/jsoneditor.min.css",
                    )
                )
            ]
        return []

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        if action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="js/vendor/jsoneditor.min.js",
                    )
                )
            ]
        return []

Source code in starlette_admin/fields.py

@dataclass
class JSONField(BaseField):
    """
    This field render jsoneditor and represent a value that stores python dict object.
    Erroneous input is ignored and will not be accepted as a value."""

    height: str = "20em"
    modes: Optional[Sequence[str]] = None
    render_function_key: str = "json"
    form_template: str = "forms/json.html"
    display_template: str = "displays/json.html"

    def __post_init__(self) -> None:
        if self.modes is None:
            self.modes = ["view"] if self.read_only else ["tree", "code"]
        super().__post_init__()

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Optional[Dict[str, Any]]:
        try:
            value = form_data.get(self.id)
            return json.loads(value) if value is not None else None  # type: ignore
        except JSONDecodeError:
            return None

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        if action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="css/jsoneditor.min.css",
                    )
                )
            ]
        return []

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        if action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="js/vendor/jsoneditor.min.js",
                    )
                )
            ]
        return []

FileField dataclass

Bases: BaseField

Renders a file upload field. This field is used to represent a value that stores starlette UploadFile object. For displaying value, this field wait for three properties which is filename, content-type and url. Use multiple=True for multiple file upload When user ask for delete on editing page, the second part of the returned tuple is True.
Source code in starlette_admin/fields.py

@dataclass
class FileField(BaseField):
    """
    Renders a file upload field.
    This field is used to represent a value that stores starlette UploadFile object.
    For displaying value, this field wait for three properties which is 'filename',
    'content-type' and 'url'. Use 'multiple=True' for multiple file upload
    When user ask for delete on editing page, the second part of the returned tuple is True.
    """

    accept: Optional[str] = None
    multiple: bool = False
    render_function_key: str = "file"
    form_template: str = "forms/file.html"
    display_template: str = "displays/file.html"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Tuple[Union[UploadFile, List[UploadFile], None], bool]:
        should_be_deleted = form_data.get(f"_{self.id}-delete") == "on"
        if self.multiple:
            files = form_data.getlist(self.id)
            return [f for f in files if not is_empty_file(f.file)], should_be_deleted  # type: ignore
        file = form_data.get(self.id)
        return (
            None if (file and is_empty_file(file.file)) else file  # type: ignore
        ), should_be_deleted

    def _isvalid_value(self, value: Any) -> bool:
        return value is not None and all(
            (
                hasattr(v, "url")
                or (isinstance(v, dict) and v.get("url", None) is not None)
            )
            for v in (value if self.multiple else [value])
        )

    def input_params(self) -> str:
        return html_params(
            {
                "accept": self.accept,
                "disabled": self.disabled,
                "readonly": self.read_only,
                "multiple": self.multiple,
            }
        )

Source code in starlette_admin/fields.py

@dataclass
class FileField(BaseField):
    """
    Renders a file upload field.
    This field is used to represent a value that stores starlette UploadFile object.
    For displaying value, this field wait for three properties which is 'filename',
    'content-type' and 'url'. Use 'multiple=True' for multiple file upload
    When user ask for delete on editing page, the second part of the returned tuple is True.
    """

    accept: Optional[str] = None
    multiple: bool = False
    render_function_key: str = "file"
    form_template: str = "forms/file.html"
    display_template: str = "displays/file.html"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Tuple[Union[UploadFile, List[UploadFile], None], bool]:
        should_be_deleted = form_data.get(f"_{self.id}-delete") == "on"
        if self.multiple:
            files = form_data.getlist(self.id)
            return [f for f in files if not is_empty_file(f.file)], should_be_deleted  # type: ignore
        file = form_data.get(self.id)
        return (
            None if (file and is_empty_file(file.file)) else file  # type: ignore
        ), should_be_deleted

    def _isvalid_value(self, value: Any) -> bool:
        return value is not None and all(
            (
                hasattr(v, "url")
                or (isinstance(v, dict) and v.get("url", None) is not None)
            )
            for v in (value if self.multiple else [value])
        )

    def input_params(self) -> str:
        return html_params(
            {
                "accept": self.accept,
                "disabled": self.disabled,
                "readonly": self.read_only,
                "multiple": self.multiple,
            }
        )

ImageField dataclass

Bases: FileField

FileField with accept="image/*".
Source code in starlette_admin/fields.py

@dataclass
class ImageField(FileField):
    """
    FileField with 'accept="image/*"'.
    """

    accept: Optional[str] = "image/*"
    render_function_key: str = "image"
    form_template: str = "forms/image.html"
    display_template: str = "displays/image.html"

Source code in starlette_admin/fields.py

@dataclass
class ImageField(FileField):
    """
    FileField with 'accept="image/*"'.
    """

    accept: Optional[str] = "image/*"
    render_function_key: str = "image"
    form_template: str = "forms/image.html"
    display_template: str = "displays/image.html"

RelationField dataclass

Bases: BaseField

A field representing a relation between two data models.

This field should not be used directly; instead, use either the HasOne or HasMany fields to specify a relation between your models.

Important

It is important to add both models in your admin interface.

Parameters:
Name 	Type 	Description 	Default
identity 	Optional[str] 	

Foreign ModelView identity
	None
Example

class Author:
    id: Optional[int]
    name: str
    books: List["Book"]

class Book:
    id: Optional[int]
    title: str
    author: Optional["Author"]

class AuthorView(ModelView):
    fields = [
        IntegerField("id"),
        StringField("name"),
        HasMany("books", identity="book"),
    ]

class BookView(ModelView):
    fields = [
        IntegerField("id"),
        StringField("title"),
        HasOne("author", identity="author"),
    ]
...
admin.add_view(AuthorView(Author, identity="author"))
admin.add_view(BookView(Book, identity="book"))
...

Example

class Author:
    id: Optional[int]
    name: str
    books: List["Book"]

class Book:
    id: Optional[int]
    title: str
    author: Optional["Author"]

class AuthorView(ModelView):
    fields = [
        IntegerField("id"),
        StringField("name"),
        HasMany("books", identity="book"),
    ]

class BookView(ModelView):
    fields = [
        IntegerField("id"),
        StringField("title"),
        HasOne("author", identity="author"),
    ]
...
admin.add_view(AuthorView(Author, identity="author"))
admin.add_view(BookView(Book, identity="book"))
...

Source code in starlette_admin/fields.py

@dataclass
class RelationField(BaseField):
    """
    A field representing a relation between two data models.

    This field should not be used directly; instead, use either the [HasOne][starlette_admin.fields.HasOne]
    or [HasMany][starlette_admin.fields.HasMany] fields to specify a relation
    between your models.

    !!! important

        It is important to add both models in your admin interface.

    Parameters:
        identity: Foreign ModelView identity

    ??? Example

        py
        class Author:
            id: Optional[int]
            name: str
            books: List["Book"]

        class Book:
            id: Optional[int]
            title: str
            author: Optional["Author"]

        class AuthorView(ModelView):
            fields = [
                IntegerField("id"),
                StringField("name"),
                HasMany("books", identity="book"),
            ]

        class BookView(ModelView):
            fields = [
                IntegerField("id"),
                StringField("title"),
                HasOne("author", identity="author"),
            ]
        ...
        admin.add_view(AuthorView(Author, identity="author"))
        admin.add_view(BookView(Book, identity="book"))
        ...
        
    """

    identity: Optional[str] = None
    multiple: bool = False
    render_function_key: str = "relation"
    form_template: str = "forms/relation.html"
    display_template: str = "displays/relation.html"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        if self.multiple:
            return form_data.getlist(self.id)
        return form_data.get(self.id)

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        if action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="css/select2.min.css",
                    )
                )
            ]
        return []

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        if action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="js/vendor/select2.min.js",
                    )
                )
            ]
        return []

Source code in starlette_admin/fields.py

@dataclass
class RelationField(BaseField):
    """
    A field representing a relation between two data models.

    This field should not be used directly; instead, use either the [HasOne][starlette_admin.fields.HasOne]
    or [HasMany][starlette_admin.fields.HasMany] fields to specify a relation
    between your models.

    !!! important

        It is important to add both models in your admin interface.

    Parameters:
        identity: Foreign ModelView identity

    ??? Example

        py
        class Author:
            id: Optional[int]
            name: str
            books: List["Book"]

        class Book:
            id: Optional[int]
            title: str
            author: Optional["Author"]

        class AuthorView(ModelView):
            fields = [
                IntegerField("id"),
                StringField("name"),
                HasMany("books", identity="book"),
            ]

        class BookView(ModelView):
            fields = [
                IntegerField("id"),
                StringField("title"),
                HasOne("author", identity="author"),
            ]
        ...
        admin.add_view(AuthorView(Author, identity="author"))
        admin.add_view(BookView(Book, identity="book"))
        ...
        
    """

    identity: Optional[str] = None
    multiple: bool = False
    render_function_key: str = "relation"
    form_template: str = "forms/relation.html"
    display_template: str = "displays/relation.html"

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        if self.multiple:
            return form_data.getlist(self.id)
        return form_data.get(self.id)

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        if action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="css/select2.min.css",
                    )
                )
            ]
        return []

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        if action.is_form():
            return [
                str(
                    request.url_for(
                        f"{request.app.state.ROUTE_NAME}:statics",
                        path="js/vendor/select2.min.js",
                    )
                )
            ]
        return []

HasOne dataclass

Bases: RelationField

A field representing a "has-one" relation between two models.
Source code in starlette_admin/fields.py

@dataclass
class HasOne(RelationField):
    """
    A field representing a "has-one" relation between two models.
    """

Source code in starlette_admin/fields.py

@dataclass
class HasOne(RelationField):
    """
    A field representing a "has-one" relation between two models.
    """

HasMany dataclass

Bases: RelationField

A field representing a "has-many" relationship between two models.
Source code in starlette_admin/fields.py

@dataclass
class HasMany(RelationField):
    """A field representing a "has-many" relationship between two models."""

    multiple: bool = True
    collection_class: Union[Type[Collection[Any]], Callable[[], Collection[Any]]] = list

Source code in starlette_admin/fields.py

@dataclass
class HasMany(RelationField):
    """A field representing a "has-many" relationship between two models."""

    multiple: bool = True
    collection_class: Union[Type[Collection[Any]], Callable[[], Collection[Any]]] = list

ListField dataclass

Bases: BaseField

Encapsulate an ordered list of multiple instances of the same field type, keeping data as a list.

Usage

class MyModel:
    id: Optional[int]
    values: List[str]

class ModelView(BaseModelView):
    fields = [IntegerField("id"), ListField(StringField("values")]

Source code in starlette_admin/fields.py

@dataclass(init=False)
class ListField(BaseField):
    """
    Encapsulate an ordered list of multiple instances of the same field type,
    keeping data as a list.

    !!! usage

        python
        class MyModel:
            id: Optional[int]
            values: List[str]

        class ModelView(BaseModelView):
            fields = [IntegerField("id"), ListField(StringField("values")]
        
    """

    form_template: str = "forms/list.html"
    display_template: str = "displays/list.html"
    search_builder_type: str = "array"
    field: BaseField = dc_field(default_factory=lambda: BaseField(""))

    def __init__(self, field: BaseField, required: bool = False) -> None:
        self.field = field
        self.name = field.name
        self.required = required
        self.__post_init__()

    def __post_init__(self) -> None:
        super().__post_init__()
        self.field.id = ""
        if isinstance(self.field, CollectionField):
            self.field._propagate_id()

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        indices = self._extra_indices(form_data)
        value = []
        for index in indices:
            self.field.id = f"{self.id}.{index}"
            if isinstance(self.field, CollectionField):
                self.field._propagate_id()
            value.append(await self.field.parse_form_data(request, form_data, action))
        return value

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> Any:
        serialized_value = []
        for item in value:
            serialized_item_value = None
            if item is not None:
                serialized_item_value = await self.field.serialize_value(
                    request, item, action
                )
            serialized_value.append(serialized_item_value)
        return serialized_value

    def _extra_indices(self, form_data: FormData) -> List[int]:
        """
        Return list of all indices.  For example, if field id is 'foo' and
        form_data contains following keys ['foo.0.bar', 'foo.1.baz'], then the indices are [0,1].
        Note that some numbers can be skipped. For example, you may have [0,1,3,8]
        as indices.
        """
        indices = set()
        for name in form_data:
            if name.startswith(self.id):
                idx = name[len(self.id) + 1 :].split(".", maxsplit=1)[0]
                if idx.isdigit():
                    indices.add(int(idx))
        return sorted(indices)

    def _field_at(self, idx: Optional[int] = None) -> BaseField:
        if idx is not None:
            self.field.id = self.id + "." + str(idx)
        else:
            """To generate template string to be used in javascript"""
            self.field.id = ""
        if isinstance(self.field, CollectionField):
            self.field._propagate_id()
        return self.field

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        return self.field.additional_css_links(request, action)

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        return self.field.additional_js_links(request, action)

Source code in starlette_admin/fields.py

@dataclass(init=False)
class ListField(BaseField):
    """
    Encapsulate an ordered list of multiple instances of the same field type,
    keeping data as a list.

    !!! usage

        python
        class MyModel:
            id: Optional[int]
            values: List[str]

        class ModelView(BaseModelView):
            fields = [IntegerField("id"), ListField(StringField("values")]
        
    """

    form_template: str = "forms/list.html"
    display_template: str = "displays/list.html"
    search_builder_type: str = "array"
    field: BaseField = dc_field(default_factory=lambda: BaseField(""))

    def __init__(self, field: BaseField, required: bool = False) -> None:
        self.field = field
        self.name = field.name
        self.required = required
        self.__post_init__()

    def __post_init__(self) -> None:
        super().__post_init__()
        self.field.id = ""
        if isinstance(self.field, CollectionField):
            self.field._propagate_id()

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        indices = self._extra_indices(form_data)
        value = []
        for index in indices:
            self.field.id = f"{self.id}.{index}"
            if isinstance(self.field, CollectionField):
                self.field._propagate_id()
            value.append(await self.field.parse_form_data(request, form_data, action))
        return value

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> Any:
        serialized_value = []
        for item in value:
            serialized_item_value = None
            if item is not None:
                serialized_item_value = await self.field.serialize_value(
                    request, item, action
                )
            serialized_value.append(serialized_item_value)
        return serialized_value

    def _extra_indices(self, form_data: FormData) -> List[int]:
        """
        Return list of all indices.  For example, if field id is 'foo' and
        form_data contains following keys ['foo.0.bar', 'foo.1.baz'], then the indices are [0,1].
        Note that some numbers can be skipped. For example, you may have [0,1,3,8]
        as indices.
        """
        indices = set()
        for name in form_data:
            if name.startswith(self.id):
                idx = name[len(self.id) + 1 :].split(".", maxsplit=1)[0]
                if idx.isdigit():
                    indices.add(int(idx))
        return sorted(indices)

    def _field_at(self, idx: Optional[int] = None) -> BaseField:
        if idx is not None:
            self.field.id = self.id + "." + str(idx)
        else:
            """To generate template string to be used in javascript"""
            self.field.id = ""
        if isinstance(self.field, CollectionField):
            self.field._propagate_id()
        return self.field

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        return self.field.additional_css_links(request, action)

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        return self.field.additional_js_links(request, action)

CollectionField dataclass

Bases: BaseField

This field represents a collection of others fields. Can be used to represent embedded mongodb document.

Usage

 CollectionField("config", fields=[StringField("key"), IntegerField("value", help_text="multiple of 5")]),

Source code in starlette_admin/fields.py

@dataclass(init=False)
class CollectionField(BaseField):
    """
    This field represents a collection of others fields. Can be used to represent embedded mongodb document.
    !!! usage

    python
     CollectionField("config", fields=[StringField("key"), IntegerField("value", help_text="multiple of 5")]),
    
    """

    fields: Sequence[BaseField] = dc_field(default_factory=list)
    render_function_key: str = "json"
    form_template: str = "forms/collection.html"
    display_template: str = "displays/collection.html"

    def __init__(
        self, name: str, fields: Sequence[BaseField], required: bool = False
    ) -> None:
        self.name = name
        self.fields = fields
        self.required = required
        super().__post_init__()
        self._propagate_id()

    def get_fields_list(
        self,
        request: Request,
        action: RequestAction = RequestAction.LIST,
    ) -> Sequence[BaseField]:
        return extract_fields(self.fields, action)

    def _propagate_id(self) -> None:
        """Will update fields id by adding his id as prefix (ex: category.name)"""
        for field in self.fields:
            field.id = self.id + ("." if self.id else "") + field.name
            if isinstance(field, type(self)):
                field._propagate_id()

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        value = {}
        for field in self.get_fields_list(request, action):
            value[field.name] = await field.parse_form_data(request, form_data, action)
        return value

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> Any:
        serialized_value: Dict[str, Any] = {}
        for field in self.get_fields_list(request, action):
            name = field.name
            serialized_value[name] = None
            if hasattr(value, name) or (isinstance(value, dict) and name in value):
                field_value = (
                    getattr(value, name) if hasattr(value, name) else value[name]
                )
                if field_value is not None:
                    serialized_value[name] = await field.serialize_value(
                        request, field_value, action
                    )
        return serialized_value

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        _links = []
        for f in self.get_fields_list(request, action):
            _links.extend(f.additional_css_links(request, action))
        return _links

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        _links = []
        for f in self.get_fields_list(request, action):
            _links.extend(f.additional_js_links(request, action))
        return _links

@dataclass(init=False)
class CollectionField(BaseField):
    """
    This field represents a collection of others fields. Can be used to represent embedded mongodb document.
    !!! usage

    python
     CollectionField("config", fields=[StringField("key"), IntegerField("value", help_text="multiple of 5")]),
    
    """

    fields: Sequence[BaseField] = dc_field(default_factory=list)
    render_function_key: str = "json"
    form_template: str = "forms/collection.html"
    display_template: str = "displays/collection.html"

    def __init__(
        self, name: str, fields: Sequence[BaseField], required: bool = False
    ) -> None:
        self.name = name
        self.fields = fields
        self.required = required
        super().__post_init__()
        self._propagate_id()

    def get_fields_list(
        self,
        request: Request,
        action: RequestAction = RequestAction.LIST,
    ) -> Sequence[BaseField]:
        return extract_fields(self.fields, action)

    def _propagate_id(self) -> None:
        """Will update fields id by adding his id as prefix (ex: category.name)"""
        for field in self.fields:
            field.id = self.id + ("." if self.id else "") + field.name
            if isinstance(field, type(self)):
                field._propagate_id()

    async def parse_form_data(
        self, request: Request, form_data: FormData, action: RequestAction
    ) -> Any:
        value = {}
        for field in self.get_fields_list(request, action):
            value[field.name] = await field.parse_form_data(request, form_data, action)
        return value

    async def serialize_value(
        self, request: Request, value: Any, action: RequestAction
    ) -> Any:
        serialized_value: Dict[str, Any] = {}
        for field in self.get_fields_list(request, action):
            name = field.name
            serialized_value[name] = None
            if hasattr(value, name) or (isinstance(value, dict) and name in value):
                field_value = (
                    getattr(value, name) if hasattr(value, name) else value[name]
                )
                if field_value is not None:
                    serialized_value[name] = await field.serialize_value(
                        request, field_value, action
                    )
        return serialized_value

    def additional_css_links(
        self, request: Request, action: RequestAction
    ) -> List[str]:
        _links = []
        for f in self.get_fields_list(request, action):
            _links.extend(f.additional_css_links(request, action))
        return _links

    def additional_js_links(self, request: Request, action: RequestAction) -> List[str]:
        _links = []
        for f in self.get_fields_list(request, action):
            _links.extend(f.additional_js_links(request, action))
        return _links

Views
starlette_admin.views
BaseView

Base class for all views

Attributes:
Name 	Type 	Description
label 	str 	

Label of the view to be displayed.
icon 	Optional[str] 	

Icon to be displayed for this model in the admin. Only FontAwesome names are supported.
Source code in starlette_admin/views.py

class BaseView:
    """
    Base class for all views

    Attributes:
        label: Label of the view to be displayed.
        icon: Icon to be displayed for this model in the admin. Only FontAwesome names are supported.
    """

    label: str = ""
    icon: Optional[str] = None

    def title(self, request: Request) -> str:
        """Return the title of the view to be displayed in the browser tab"""
        return self.label

    def is_active(self, request: Request) -> bool:
        """Return true if the current view is active"""
        return False

    def is_accessible(self, request: Request) -> bool:
        """
        Override this method to add permission checks.
        Return True if current user can access this view
        """
        return True

Source code in starlette_admin/views.py

class BaseView:
    """
    Base class for all views

    Attributes:
        label: Label of the view to be displayed.
        icon: Icon to be displayed for this model in the admin. Only FontAwesome names are supported.
    """

    label: str = ""
    icon: Optional[str] = None

    def title(self, request: Request) -> str:
        """Return the title of the view to be displayed in the browser tab"""
        return self.label

    def is_active(self, request: Request) -> bool:
        """Return true if the current view is active"""
        return False

    def is_accessible(self, request: Request) -> bool:
        """
        Override this method to add permission checks.
        Return True if current user can access this view
        """
        return True

is_accessible(request)

Override this method to add permission checks. Return True if current user can access this view
Source code in starlette_admin/views.py

def is_accessible(self, request: Request) -> bool:
    """
    Override this method to add permission checks.
    Return True if current user can access this view
    """
    return True

Source code in starlette_admin/views.py

def is_accessible(self, request: Request) -> bool:
    """
    Override this method to add permission checks.
    Return True if current user can access this view
    """
    return True

is_active(request)

Return true if the current view is active
Source code in starlette_admin/views.py

def is_active(self, request: Request) -> bool:
    """Return true if the current view is active"""
    return False

Source code in starlette_admin/views.py

def is_active(self, request: Request) -> bool:
    """Return true if the current view is active"""
    return False

title(request)

Return the title of the view to be displayed in the browser tab
Source code in starlette_admin/views.py

def title(self, request: Request) -> str:
    """Return the title of the view to be displayed in the browser tab"""
    return self.label

Source code in starlette_admin/views.py

def title(self, request: Request) -> str:
    """Return the title of the view to be displayed in the browser tab"""
    return self.label

DropDown

Bases: BaseView

Group views inside a dropdown
Example

admin.add_view(
    DropDown(
        "Resources",
        icon="fa fa-list",
        views=[
            ModelView(User),
            Link(label="Home Page", url="/"),
            CustomView(label="Dashboard", path="/dashboard", template_path="dashboard.html"),
        ],
    )
)

Example

admin.add_view(
    DropDown(
        "Resources",
        icon="fa fa-list",
        views=[
            ModelView(User),
            Link(label="Home Page", url="/"),
            CustomView(label="Dashboard", path="/dashboard", template_path="dashboard.html"),
        ],
    )
)

Source code in starlette_admin/views.py

class DropDown(BaseView):
    """
    Group views inside a dropdown

    Example:
        python
        admin.add_view(
            DropDown(
                "Resources",
                icon="fa fa-list",
                views=[
                    ModelView(User),
                    Link(label="Home Page", url="/"),
                    CustomView(label="Dashboard", path="/dashboard", template_path="dashboard.html"),
                ],
            )
        )
        
    """

    def __init__(
        self,
        label: str,
        views: List[Union[Type[BaseView], BaseView]],
        icon: Optional[str] = None,
        always_open: bool = True,
    ) -> None:
        self.label = label
        self.icon = icon
        self.always_open = always_open
        self.views: List[BaseView] = [
            (v if isinstance(v, BaseView) else v()) for v in views
        ]

    def is_active(self, request: Request) -> bool:
        return any(v.is_active(request) for v in self.views)

    def is_accessible(self, request: Request) -> bool:
        return any(v.is_accessible(request) for v in self.views)

Source code in starlette_admin/views.py

class DropDown(BaseView):
    """
    Group views inside a dropdown

    Example:
        python
        admin.add_view(
            DropDown(
                "Resources",
                icon="fa fa-list",
                views=[
                    ModelView(User),
                    Link(label="Home Page", url="/"),
                    CustomView(label="Dashboard", path="/dashboard", template_path="dashboard.html"),
                ],
            )
        )
        
    """

    def __init__(
        self,
        label: str,
        views: List[Union[Type[BaseView], BaseView]],
        icon: Optional[str] = None,
        always_open: bool = True,
    ) -> None:
        self.label = label
        self.icon = icon
        self.always_open = always_open
        self.views: List[BaseView] = [
            (v if isinstance(v, BaseView) else v()) for v in views
        ]

    def is_active(self, request: Request) -> bool:
        return any(v.is_active(request) for v in self.views)

    def is_accessible(self, request: Request) -> bool:
        return any(v.is_accessible(request) for v in self.views)

Link

Bases: BaseView

Add arbitrary hyperlinks to the menu
Example

admin.add_view(Link(label="Home Page", icon="fa fa-link", url="/"))

Example

admin.add_view(Link(label="Home Page", icon="fa fa-link", url="/"))

Source code in starlette_admin/views.py

class Link(BaseView):
    """
    Add arbitrary hyperlinks to the menu

    Example:
        python
        admin.add_view(Link(label="Home Page", icon="fa fa-link", url="/"))
        
    """

    def __init__(
        self,
        label: str = "",
        icon: Optional[str] = None,
        url: str = "/",
        target: Optional[str] = "_self",
    ):
        self.label = label
        self.icon = icon
        self.url = url
        self.target = target

Source code in starlette_admin/views.py

class Link(BaseView):
    """
    Add arbitrary hyperlinks to the menu

    Example:
        python
        admin.add_view(Link(label="Home Page", icon="fa fa-link", url="/"))
        
    """

    def __init__(
        self,
        label: str = "",
        icon: Optional[str] = None,
        url: str = "/",
        target: Optional[str] = "_self",
    ):
        self.label = label
        self.icon = icon
        self.url = url
        self.target = target

CustomView

Bases: BaseView

Add your own views (not tied to any particular model). For example, a custom home page that displays some analytics data.

Attributes:
Name 	Type 	Description
path 		

Route path
template_path 		

Path to template file
methods 		

HTTP methods
name 		

Route name
add_to_menu 		

Display to menu or not
Example

admin.add_view(CustomView(label="Home", icon="fa fa-home", path="/home", template_path="home.html"))

Example

admin.add_view(CustomView(label="Home", icon="fa fa-home", path="/home", template_path="home.html"))

Source code in starlette_admin/views.py

class CustomView(BaseView):
    """
    Add your own views (not tied to any particular model). For example,
    a custom home page that displays some analytics data.

    Attributes:
        path: Route path
        template_path: Path to template file
        methods: HTTP methods
        name: Route name
        add_to_menu: Display to menu or not

    Example:
        python
        admin.add_view(CustomView(label="Home", icon="fa fa-home", path="/home", template_path="home.html"))
        
    """

    def __init__(
        self,
        label: str,
        icon: Optional[str] = None,
        path: str = "/",
        template_path: str = "index.html",
        name: Optional[str] = None,
        methods: Optional[List[str]] = None,
        add_to_menu: bool = True,
    ):
        self.label = label
        self.icon = icon
        self.path = path
        self.template_path = template_path
        self.name = name
        self.methods = methods
        self.add_to_menu = add_to_menu

    async def render(self, request: Request, templates: Jinja2Templates) -> Response:
        """Default methods to render view. Override this methods to add your custom logic."""
        return templates.TemplateResponse(
            request=request,
            name=self.template_path,
            context={"title": self.title(request)},
        )

    def is_active(self, request: Request) -> bool:
        return request.scope["path"] == self.path

Source code in starlette_admin/views.py

class CustomView(BaseView):
    """
    Add your own views (not tied to any particular model). For example,
    a custom home page that displays some analytics data.

    Attributes:
        path: Route path
        template_path: Path to template file
        methods: HTTP methods
        name: Route name
        add_to_menu: Display to menu or not

    Example:
        python
        admin.add_view(CustomView(label="Home", icon="fa fa-home", path="/home", template_path="home.html"))
        
    """

    def __init__(
        self,
        label: str,
        icon: Optional[str] = None,
        path: str = "/",
        template_path: str = "index.html",
        name: Optional[str] = None,
        methods: Optional[List[str]] = None,
        add_to_menu: bool = True,
    ):
        self.label = label
        self.icon = icon
        self.path = path
        self.template_path = template_path
        self.name = name
        self.methods = methods
        self.add_to_menu = add_to_menu

    async def render(self, request: Request, templates: Jinja2Templates) -> Response:
        """Default methods to render view. Override this methods to add your custom logic."""
        return templates.TemplateResponse(
            request=request,
            name=self.template_path,
            context={"title": self.title(request)},
        )

    def is_active(self, request: Request) -> bool:
        return request.scope["path"] == self.path

render(request, templates) async

Default methods to render view. Override this methods to add your custom logic.
Source code in starlette_admin/views.py

async def render(self, request: Request, templates: Jinja2Templates) -> Response:
    """Default methods to render view. Override this methods to add your custom logic."""
    return templates.TemplateResponse(
        request=request,
        name=self.template_path,
        context={"title": self.title(request)},
    )

Source code in starlette_admin/views.py

async def render(self, request: Request, templates: Jinja2Templates) -> Response:
    """Default methods to render view. Override this methods to add your custom logic."""
    return templates.TemplateResponse(
        request=request,
        name=self.template_path,
        context={"title": self.title(request)},
    )

BaseModelView

Bases: BaseView

Base administrative view. Derive from this class to implement your administrative interface piece.

Attributes:
Name 	Type 	Description
identity 	Optional[str] 	

Unique identity to identify the model associated to this view. Will be used for URL of the endpoints.
name 	Optional[str] 	

Name of the view to be displayed
fields 	Sequence[BaseField] 	

List of fields
pk_attr 	Optional[str] 	

Primary key field name
form_include_pk 	bool 	

Indicates whether the primary key should be included in create and edit forms. Default to False.
exclude_fields_from_list 	Sequence[str] 	

List of fields to exclude in List page.
exclude_fields_from_detail 	Sequence[str] 	

List of fields to exclude in Detail page.
exclude_fields_from_create 	Sequence[str] 	

List of fields to exclude from creation page.
exclude_fields_from_edit 	Sequence[str] 	

List of fields to exclude from editing page.
searchable_fields 	Optional[Sequence[str]] 	

List of searchable fields.
sortable_fields 	Optional[Sequence[str]] 	

List of sortable fields.
export_fields 	Optional[Sequence[str]] 	

List of fields to include in exports.
fields_default_sort 	Optional[Sequence[Union[Tuple[str, bool], str]]] 	

Initial order (sort) to apply to the table. Should be a sequence of field names or a tuple of (field name, True/False to indicate the sort direction). For example: ["title", ("created_at", False), ("price", True)] will sort by title ascending, created_at ascending and price descending.
export_types 	Sequence[ExportType] 	

A list of available export filetypes. Available exports are ['csv', 'excel', 'pdf', 'print']. Only pdf is disabled by default.
column_visibility 	bool 	

Enable/Disable column visibility extension
search_builder 	bool 	

Enable/Disable search builder extension
page_size 	int 	

Default number of items to display in List page pagination. Default value is set to 10.
page_size_options 	Sequence[int] 	

Pagination choices displayed in List page. Default value is set to [10, 25, 50, 100]. Use -1to display All
responsive_table 	bool 	

Enable/Disable responsive extension
save_state 	bool 	

Enable/Disable state saving
datatables_options 	Dict[str, Any] 	

Dict of Datatables options. These will overwrite any default options set for the datatable.
list_template 	str 	

List view template. Default is list.html.
detail_template 	str 	

Details view template. Default is detail.html.
create_template 	str 	

Edit view template. Default is create.html.
edit_template 	str 	

Edit view template. Default is edit.html.
actions 	Optional[Sequence[str]] 	

List of actions
additional_js_links 	Optional[List[str]] 	

A list of additional JavaScript files to include.
additional_css_links 	Optional[List[str]] 	

A list of additional CSS files to include.
Source code in starlette_admin/views.py

class BaseModelView(BaseView):
    """
    Base administrative view.
    Derive from this class to implement your administrative interface piece.

    Attributes:
        identity: Unique identity to identify the model associated to this view.
            Will be used for URL of the endpoints.
        name: Name of the view to be displayed
        fields: List of fields
        pk_attr: Primary key field name
        form_include_pk (bool): Indicates whether the primary key should be
            included in create and edit forms. Default to False.
        exclude_fields_from_list: List of fields to exclude in List page.
        exclude_fields_from_detail: List of fields to exclude in Detail page.
        exclude_fields_from_create: List of fields to exclude from creation page.
        exclude_fields_from_edit: List of fields to exclude from editing page.
        searchable_fields: List of searchable fields.
        sortable_fields: List of sortable fields.
        export_fields: List of fields to include in exports.
        fields_default_sort: Initial order (sort) to apply to the table.
            Should be a sequence of field names or a tuple of
            (field name, True/False to indicate the sort direction).
            For example:
            '["title",  ("created_at", False), ("price", True)]' will sort
             by 'title' ascending, 'created_at' ascending and 'price' descending.
        export_types: A list of available export filetypes. Available
            exports are '['csv', 'excel', 'pdf', 'print']'. Only 'pdf' is
            disabled by default.
        column_visibility: Enable/Disable
            [column visibility](https://datatables.net/extensions/buttons/built-in#Column-visibility)
            extension
        search_builder: Enable/Disable [search builder](https://datatables.net/extensions/searchbuilder/)
            extension
        page_size: Default number of items to display in List page pagination.
            Default value is set to '10'.
        page_size_options: Pagination choices displayed in List page.
            Default value is set to '[10, 25, 50, 100]'. Use '-1'to display All
        responsive_table: Enable/Disable [responsive](https://datatables.net/extensions/responsive/)
            extension
        save_state: Enable/Disable [state saving](https://datatables.net/examples/basic_init/state_save.html)
        datatables_options: Dict of [Datatables options](https://datatables.net/reference/option/).
            These will overwrite any default options set for the datatable.
        list_template: List view template. Default is 'list.html'.
        detail_template: Details view template. Default is 'detail.html'.
        create_template: Edit view template. Default is 'create.html'.
        edit_template: Edit view template. Default is 'edit.html'.
        actions: List of actions
        additional_js_links: A list of additional JavaScript files to include.
        additional_css_links: A list of additional CSS files to include.

    """

    identity: Optional[str] = None
    name: Optional[str] = None
    fields: Sequence[BaseField] = []
    pk_attr: Optional[str] = None
    form_include_pk: bool = False
    exclude_fields_from_list: Sequence[str] = []
    exclude_fields_from_detail: Sequence[str] = []
    exclude_fields_from_create: Sequence[str] = []
    exclude_fields_from_edit: Sequence[str] = []
    searchable_fields: Optional[Sequence[str]] = None
    sortable_fields: Optional[Sequence[str]] = None
    fields_default_sort: Optional[Sequence[Union[Tuple[str, bool], str]]] = None
    export_types: Sequence[ExportType] = [
        ExportType.CSV,
        ExportType.EXCEL,
        ExportType.PRINT,
    ]
    export_fields: Optional[Sequence[str]] = None
    column_visibility: bool = True
    search_builder: bool = True
    page_size: int = 10
    page_size_options: Sequence[int] = [10, 25, 50, 100]
    responsive_table: bool = False
    save_state: bool = True
    datatables_options: ClassVar[Dict[str, Any]] = {}
    list_template: str = "list.html"
    detail_template: str = "detail.html"
    create_template: str = "create.html"
    edit_template: str = "edit.html"
    actions: Optional[Sequence[str]] = None
    row_actions: Optional[Sequence[str]] = None
    additional_js_links: Optional[List[str]] = None
    additional_css_links: Optional[List[str]] = None
    row_actions_display_type: RowActionsDisplayType = RowActionsDisplayType.ICON_LIST

    _find_foreign_model: Callable[[str], "BaseModelView"]

    def __init__(self) -> None:  # noqa: C901
        fringe = list(self.fields)
        all_field_names = []
        while len(fringe) > 0:
            field = fringe.pop(0)
            if not hasattr(field, "_name"):
                field._name = field.name  # type: ignore
            if isinstance(field, CollectionField):
                for f in field.fields:
                    f._name = f"{field._name}.{f.name}"  # type: ignore
                fringe.extend(field.fields)
            name = field._name  # type: ignore
            if name == self.pk_attr and not self.form_include_pk:
                field.exclude_from_create = True
                field.exclude_from_edit = True
            if name in self.exclude_fields_from_list:
                field.exclude_from_list = True
            if name in self.exclude_fields_from_detail:
                field.exclude_from_detail = True
            if name in self.exclude_fields_from_create:
                field.exclude_from_create = True
            if name in self.exclude_fields_from_edit:
                field.exclude_from_edit = True
            if not isinstance(field, CollectionField):
                all_field_names.append(name)
                field.searchable = (self.searchable_fields is None) or (
                    name in self.searchable_fields
                )
                field.orderable = (self.sortable_fields is None) or (
                    name in self.sortable_fields
                )
        if self.searchable_fields is None:
            self.searchable_fields = all_field_names[:]
        if self.sortable_fields is None:
            self.sortable_fields = all_field_names[:]
        if self.export_fields is None:
            self.export_fields = all_field_names[:]
        if self.fields_default_sort is None:
            self.fields_default_sort = [self.pk_attr]  # type: ignore[list-item]

        # Actions
        self._actions: Dict[str, Dict[str, str]] = OrderedDict()
        self._row_actions: Dict[str, Dict[str, str]] = OrderedDict()
        self._actions_handlers: Dict[
            str, Callable[[Request, Sequence[Any]], Awaitable]
        ] = OrderedDict()
        self._row_actions_handlers: Dict[str, Callable[[Request, Any], Awaitable]] = (
            OrderedDict()
        )
        self._init_actions()

    def is_active(self, request: Request) -> bool:
        return request.path_params.get("identity", None) == self.identity

    def _init_actions(self) -> None:
        self._init_batch_actions()
        self._init_row_actions()
        self._validate_actions()

    def _init_batch_actions(self) -> None:
        """
        This method initializes batch and row actions, collects their handlers,
        and validates that all specified actions exist.
        """
        for _method_name, method in inspect.getmembers(
            self, predicate=inspect.ismethod
        ):
            if hasattr(method, "_action"):
                name = method._action.get("name")
                self._actions[name] = method._action
                self._actions_handlers[name] = method

        if self.actions is None:
            self.actions = list(self._actions_handlers.keys())

    def _init_row_actions(self) -> None:
        for _method_name, method in inspect.getmembers(
            self, predicate=inspect.ismethod
        ):
            if hasattr(method, "_row_action"):
                name = method._row_action.get("name")
                self._row_actions[name] = method._row_action
                self._row_actions_handlers[name] = method

        if self.row_actions is None:
            self.row_actions = list(self._row_actions_handlers.keys())

    def _validate_actions(self) -> None:
        for action_name in not_none(self.actions):
            if action_name not in self._actions:
                raise ValueError(f"Unknown action with name '{action_name}'")
        for action_name in not_none(self.row_actions):
            if action_name not in self._row_actions:
                raise ValueError(f"Unknown row action with name '{action_name}'")

    async def is_action_allowed(self, request: Request, name: str) -> bool:
        """
        Verify if action with 'name' is allowed.
        Override this method to allow or disallow actions based
        on some condition.

        Args:
            name: Action name
            request: Starlette request
        """
        if name == "delete":
            return self.can_delete(request)
        return True

    async def is_row_action_allowed(self, request: Request, name: str) -> bool:
        """
        Verify if the row action with 'name' is allowed.
        Override this method to allow or disallow row actions based
        on some condition.

        Args:
            name: Row action name
            request: Starlette request
        """
        if name == "delete":
            return self.can_delete(request)
        if name == "edit":
            return self.can_edit(request)
        if name == "view":
            return self.can_view_details(request)
        return True

    async def get_all_actions(self, request: Request) -> List[Dict[str, Any]]:
        """Return a list of allowed batch actions"""
        actions = []
        for action_name in not_none(self.actions):
            if await self.is_action_allowed(request, action_name):
                actions.append(self._actions.get(action_name, {}))
        return actions

    async def get_all_row_actions(self, request: Request) -> List[Dict[str, Any]]:
        """Return a list of allowed row actions"""
        row_actions = []
        for row_action_name in not_none(self.row_actions):
            if await self.is_row_action_allowed(request, row_action_name):
                _row_action = self._row_actions.get(row_action_name, {})
                if (
                    request.state.action == RequestAction.LIST
                    and not _row_action.get("exclude_from_list")
                ) or (
                    request.state.action == RequestAction.DETAIL
                    and not _row_action.get("exclude_from_detail")
                ):
                    row_actions.append(_row_action)
        return row_actions

    async def handle_action(
        self, request: Request, pks: List[Any], name: str
    ) -> Union[str, Response]:
        """
        Handle action with 'name'.
        Raises:
            ActionFailed: to display meaningfully error
        """
        handler = self._actions_handlers.get(name, None)
        if handler is None:
            raise ActionFailed("Invalid action")
        if not await self.is_action_allowed(request, name):
            raise ActionFailed("Forbidden")
        handler_return = await handler(request, pks)
        custom_response = self._actions[name]["custom_response"]
        if isinstance(handler_return, Response) and not custom_response:
            raise ActionFailed(
                "Set custom_response to true, to be able to return custom response"
            )
        return handler_return

    async def handle_row_action(
        self, request: Request, pk: Any, name: str
    ) -> Union[str, Response]:
        """
        Handle row action with 'name'.
        Raises:
            ActionFailed: to display meaningfully error
        """
        handler = self._row_actions_handlers.get(name, None)
        if handler is None:
            raise ActionFailed("Invalid row action")
        if not await self.is_row_action_allowed(request, name):
            raise ActionFailed("Forbidden")
        handler_return = await handler(request, pk)
        custom_response = self._row_actions[name]["custom_response"]
        if isinstance(handler_return, Response) and not custom_response:
            raise ActionFailed(
                "Set custom_response to true, to be able to return custom response"
            )
        return handler_return

    @action(
        name="delete",
        text=_("Delete"),
        confirmation=_("Are you sure you want to delete selected items?"),
        submit_btn_text=_("Yes, delete all"),
        submit_btn_class="btn-danger",
    )
    async def delete_action(self, request: Request, pks: List[Any]) -> str:
        affected_rows = await self.delete(request, pks)
        return ngettext(
            "Item was successfully deleted",
            "%(count)d items were successfully deleted",
            affected_rows or 0,
        ) % {"count": affected_rows}

    @link_row_action(
        name="view",
        text=_("View"),
        icon_class="fa-solid fa-eye",
        exclude_from_detail=True,
    )
    def row_action_1_view(self, request: Request, pk: Any) -> str:
        route_name = request.app.state.ROUTE_NAME
        return str(
            request.url_for(route_name + ":detail", identity=self.identity, pk=pk)
        )

    @link_row_action(
        name="edit",
        text=_("Edit"),
        icon_class="fa-solid fa-edit",
        action_btn_class="btn-primary",
    )
    def row_action_2_edit(self, request: Request, pk: Any) -> str:
        route_name = request.app.state.ROUTE_NAME
        return str(request.url_for(route_name + ":edit", identity=self.identity, pk=pk))

    @row_action(
        name="delete",
        text=_("Delete"),
        confirmation=_("Are you sure you want to delete this item?"),
        icon_class="fa-solid fa-trash",
        submit_btn_text="Yes, delete",
        submit_btn_class="btn-danger",
        action_btn_class="btn-danger",
    )
    async def row_action_3_delete(self, request: Request, pk: Any) -> str:
        await self.delete(request, [pk])
        return gettext("Item was successfully deleted")

    @abstractmethod
    async def find_all(
        self,
        request: Request,
        skip: int = 0,
        limit: int = 100,
        where: Union[Dict[str, Any], str, None] = None,
        order_by: Optional[List[str]] = None,
    ) -> Sequence[Any]:
        """
        Find all items
        Parameters:
            request: The request being processed
            where: Can be dict for complex query
                json
                 {"and":[{"id": {"gt": 5}},{"name": {"startsWith": "ban"}}]}
                
                or plain text for full search
            skip: should return values start from position skip+1
            limit: number of maximum items to return
            order_by: order data clauses in form '["id asc", "name desc"]'
        """
        raise NotImplementedError()

    @abstractmethod
    async def count(
        self,
        request: Request,
        where: Union[Dict[str, Any], str, None] = None,
    ) -> int:
        """
        Count items
        Parameters:
            request: The request being processed
            where: Can be dict for complex query
                json
                 {"and":[{"id": {"gt": 5}},{"name": {"startsWith": "ban"}}]}
                
                or plain text for full search
        """
        raise NotImplementedError()

    @abstractmethod
    async def find_by_pk(self, request: Request, pk: Any) -> Any:
        """
        Find one item
        Parameters:
            request: The request being processed
            pk: Primary key
        """
        raise NotImplementedError()

    @abstractmethod
    async def find_by_pks(self, request: Request, pks: List[Any]) -> Sequence[Any]:
        """
        Find many items
        Parameters:
            request: The request being processed
            pks: List of Primary key
        """
        raise NotImplementedError()

    async def before_create(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        """
        This hook is called before a new item is created.

        Args:
            request: The request being processed.
            data: Dict values contained converted form data.
            obj: The object about to be created.
        """

    @abstractmethod
    async def create(self, request: Request, data: Dict) -> Any:
        """
        Create item
        Parameters:
            request: The request being processed
            data: Dict values contained converted form data
        Returns:
            Any: Created Item
        """
        raise NotImplementedError()

    async def after_create(self, request: Request, obj: Any) -> None:
        """
        This hook is called after a new item is successfully created.

        Args:
            request: The request being processed.
            obj: The newly created object.
        """

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        """
        This hook is called before an item is edited.

        Args:
            request: The request being processed.
            data: Dict values contained converted form data
            obj: The object about to be edited.
        """

    @abstractmethod
    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        """
        Edit item
        Parameters:
            request: The request being processed
            pk: Primary key
            data: Dict values contained converted form data
        Returns:
            Any: Edited Item
        """
        raise NotImplementedError()

    async def after_edit(self, request: Request, obj: Any) -> None:
        """
        This hook is called after an item is successfully edited.

        Args:
            request: The request being processed.
            obj: The edited object.
        """

    async def before_delete(self, request: Request, obj: Any) -> None:
        """
        This hook is called before an item is deleted.

        Args:
            request: The request being processed.
            obj: The object about to be deleted.
        """

    @abstractmethod
    async def delete(self, request: Request, pks: List[Any]) -> Optional[int]:
        """
        Bulk delete items
        Parameters:
            request: The request being processed
            pks: List of primary keys
        """
        raise NotImplementedError()

    async def after_delete(self, request: Request, obj: Any) -> None:
        """
        This hook is called after an item is successfully deleted.

        Args:
            request: The request being processed.
            obj: The deleted object.
        """

    def can_view_details(self, request: Request) -> bool:
        """Permission for viewing full details of Item. Return True by default"""
        return True

    def can_create(self, request: Request) -> bool:
        """Permission for creating new Items. Return True by default"""
        return True

    def can_edit(self, request: Request) -> bool:
        """Permission for editing Items. Return True by default"""
        return True

    def can_delete(self, request: Request) -> bool:
        """Permission for deleting Items. Return True by default"""
        return True

    async def serialize_field_value(
        self, value: Any, field: BaseField, action: RequestAction, request: Request
    ) -> Any:
        """
        Format output value for each field.

        !!! important

            The returned value should be json serializable

        Parameters:
            value: attribute of item returned by 'find_all' or 'find_by_pk'
            field: Starlette Admin field for this attribute
            action: Specify where the data will be used. Possible values are
                'VIEW' for detail page, 'EDIT' for editing page and 'API'
                for listing page and select2 data.
            request: The request being processed
        """
        if value is None:
            return await field.serialize_none_value(request, action)
        return await field.serialize_value(request, value, action)

    async def serialize(
        self,
        obj: Any,
        request: Request,
        action: RequestAction,
        include_relationships: bool = True,
        include_select2: bool = False,
    ) -> Dict[str, Any]:
        obj_serialized: Dict[str, Any] = {}
        obj_meta: Dict[str, Any] = {}
        for field in self.get_fields_list(request, action):
            if isinstance(field, RelationField) and include_relationships:
                value = getattr(obj, field.name, None)
                foreign_model = self._find_foreign_model(field.identity)  # type: ignore
                if value is None:
                    obj_serialized[field.name] = None
                elif isinstance(field, HasOne):
                    if action == RequestAction.EDIT:
                        obj_serialized[field.name] = (
                            await foreign_model.get_serialized_pk_value(request, value)
                        )
                    else:
                        obj_serialized[field.name] = await foreign_model.serialize(
                            value, request, action, include_relationships=False
                        )
                else:
                    if action == RequestAction.EDIT:
                        obj_serialized[field.name] = [
                            (await foreign_model.get_serialized_pk_value(request, obj))
                            for obj in value
                        ]
                    else:
                        obj_serialized[field.name] = [
                            await foreign_model.serialize(
                                v, request, action, include_relationships=False
                            )
                            for v in value
                        ]
            elif not isinstance(field, RelationField):
                value = await field.parse_obj(request, obj)
                obj_serialized[field.name] = await self.serialize_field_value(
                    value, field, action, request
                )
        if include_select2:
            obj_meta["select2"] = {
                "selection": await self.select2_selection(obj, request),
                "result": await self.select2_result(obj, request),
            }
        obj_meta["repr"] = await self.repr(obj, request)

        # Make sure the primary key is always available
        pk_attr = not_none(self.pk_attr)
        if pk_attr not in obj_serialized:
            pk_value = await self.get_serialized_pk_value(request, obj)
            obj_serialized[pk_attr] = pk_value

        pk = await self.get_pk_value(request, obj)
        route_name = request.app.state.ROUTE_NAME
        obj_meta["detailUrl"] = str(
            request.url_for(route_name + ":detail", identity=self.identity, pk=pk)
        )
        obj_serialized["_meta"] = obj_meta
        return obj_serialized

    async def repr(self, obj: Any, request: Request) -> str:
        """Return a string representation of the given object that can be displayed in the admin interface.

        If the object has a custom representation method '__admin_repr__', it is used to generate the string. Otherwise,
        the value of the object's primary key attribute is used.

        Args:
            obj: The object to represent.
            request: The request being processed

        Example:
            For example, the following implementation for a 'User' model will display
            the user's full name instead of their primary key in the admin interface:

            python
            class User:
                id: int
                first_name: str
                last_name: str

                def __admin_repr__(self, request: Request):
                    return f"{self.last_name} {self.first_name}"
            
        """
        repr_method = getattr(obj, "__admin_repr__", None)
        if repr_method is None:
            return str(await self.get_pk_value(request, obj))
        if inspect.iscoroutinefunction(repr_method):
            return await repr_method(request)
        return repr_method(request)

    async def select2_result(self, obj: Any, request: Request) -> str:
        """Returns an HTML-formatted string that represents the search results for a Select2 search box.

        By default, this method returns a string that contains all the object's attributes in a list except
        relation and file attributes.

        If the object has a custom representation method '__admin_select2_repr__', it is used to generate the
        HTML-formatted string.

        !!! note

            The returned value should be valid HTML.

        !!! danger

            Escape your database value to avoid Cross-Site Scripting (XSS) attack.
            You can use Jinja2 Template render with 'autoescape=True'.
            For more information [click here](https://owasp.org/www-community/attacks/xss/)

        Parameters:
            obj: The object returned by the 'find_all' or 'find_by_pk' method.
            request: The request being processed

        Example:
            Here is an example implementation for a 'User' model
            that includes the user's name and photo:

            python
            class User:
                id: int
                name: str
                photo_url: str

                def __admin_select2_repr__(self, request: Request) -> str:
                    return f''
            

        """
        template_str = (
            "<span>{%for col in fields %}{%if obj[col]%}<strong>{{col}}:"
            " </strong>{{obj[col]}} {%endif%}{%endfor%}</span>"
        )
        fields = [
            field.name
            for field in self.get_fields_list(request)
            if (
                not isinstance(field, (RelationField, FileField))
                and not field.exclude_from_detail
            )
        ]
        html_repr_method = getattr(
            obj,
            "__admin_select2_repr__",
            lambda request: Template(template_str, autoescape=True).render(
                obj=obj, fields=fields
            ),
        )
        if inspect.iscoroutinefunction(html_repr_method):
            return await html_repr_method(request)
        return html_repr_method(request)

    async def select2_selection(self, obj: Any, request: Request) -> str:
        """
        Returns the HTML representation of an item selected by a user in a Select2 component.
        By default, it simply calls 'select2_result()'.

        !!! note

            The returned value should be valid HTML.

        !!! danger

            Escape your database value to avoid Cross-Site Scripting (XSS) attack.
            You can use Jinja2 Template render with 'autoescape=True'.
            For more information [click here](https://owasp.org/www-community/attacks/xss/)

        Parameters:
            obj: item returned by 'find_all' or 'find_by_pk'
            request: The request being processed

        """
        return await self.select2_result(obj, request)

    async def get_pk_value(self, request: Request, obj: Any) -> Any:
        return getattr(obj, not_none(self.pk_attr))

    async def get_serialized_pk_value(self, request: Request, obj: Any) -> Any:
        """
        Return serialized value of the primary key.

        !!! note

            The returned value should be JSON-serializable.

        Parameters:
            request: The request being processed
            obj: object to get primary key of

        Returns:
            Any: Serialized value of a PK.
        """
        return await self.get_pk_value(request, obj)

    def _length_menu(self) -> Any:
        return [
            self.page_size_options,
            [(_("All") if i < 0 else i) for i in self.page_size_options],
        ]

    def _search_columns_selector(self) -> List[str]:
        return [f"{name}:name" for name in self.searchable_fields]  # type: ignore

    def _export_columns_selector(self) -> List[str]:
        return [f"{name}:name" for name in self.export_fields]  # type: ignore

    def get_fields_list(
        self,
        request: Request,
        action: RequestAction = RequestAction.LIST,
    ) -> Sequence[BaseField]:
        """Return a list of field instances to display in the specified view action.
        This function excludes fields with corresponding exclude flags, which are
        determined by the 'exclude_fields_from_*' attributes.

        Parameters:
             request: The request being processed.
             action: The type of action being performed on the view.
        """
        return extract_fields(self.fields, action)

    def _additional_css_links(
        self, request: Request, action: RequestAction
    ) -> Sequence[str]:
        links = self.additional_css_links or []
        for field in self.get_fields_list(request, action):
            for link in field.additional_css_links(request, action) or []:
                if link not in links:
                    links.append(link)
        return links

    def _additional_js_links(
        self, request: Request, action: RequestAction
    ) -> Sequence[str]:
        links = self.additional_js_links or []
        for field in self.get_fields_list(request, action):
            for link in field.additional_js_links(request, action) or []:
                if link not in links:
                    links.append(link)
        return links

    async def _configs(self, request: Request) -> Dict[str, Any]:
        locale = get_locale()
        return {
            "label": self.label,
            "pageSize": self.page_size,
            "lengthMenu": self._length_menu(),
            "searchColumns": self._search_columns_selector(),
            "exportColumns": self._export_columns_selector(),
            "fieldsDefaultSort": dict(
                (it, False) if isinstance(it, str) else it
                for it in self.fields_default_sort  # type: ignore[union-attr]
            ),
            "exportTypes": self.export_types,
            "columnVisibility": self.column_visibility,
            "searchBuilder": self.search_builder,
            "responsiveTable": self.responsive_table,
            "stateSave": self.save_state,
            "fields": [f.dict() for f in self.get_fields_list(request)],
            "pk": self.pk_attr,
            "locale": locale,
            "apiUrl": request.url_for(
                f"{request.app.state.ROUTE_NAME}:api", identity=self.identity
            ),
            "actionUrl": request.url_for(
                f"{request.app.state.ROUTE_NAME}:action", identity=self.identity
            ),
            "rowActionUrl": request.url_for(
                f"{request.app.state.ROUTE_NAME}:row-action", identity=self.identity
            ),
            "dt_i18n_url": request.url_for(
                f"{request.app.state.ROUTE_NAME}:statics", path=f"i18n/dt/{locale}.json"
            ),
            "datatablesOptions": self.datatables_options,
        }

Source code in starlette_admin/views.py

class BaseModelView(BaseView):
    """
    Base administrative view.
    Derive from this class to implement your administrative interface piece.

    Attributes:
        identity: Unique identity to identify the model associated to this view.
            Will be used for URL of the endpoints.
        name: Name of the view to be displayed
        fields: List of fields
        pk_attr: Primary key field name
        form_include_pk (bool): Indicates whether the primary key should be
            included in create and edit forms. Default to False.
        exclude_fields_from_list: List of fields to exclude in List page.
        exclude_fields_from_detail: List of fields to exclude in Detail page.
        exclude_fields_from_create: List of fields to exclude from creation page.
        exclude_fields_from_edit: List of fields to exclude from editing page.
        searchable_fields: List of searchable fields.
        sortable_fields: List of sortable fields.
        export_fields: List of fields to include in exports.
        fields_default_sort: Initial order (sort) to apply to the table.
            Should be a sequence of field names or a tuple of
            (field name, True/False to indicate the sort direction).
            For example:
            '["title",  ("created_at", False), ("price", True)]' will sort
             by 'title' ascending, 'created_at' ascending and 'price' descending.
        export_types: A list of available export filetypes. Available
            exports are '['csv', 'excel', 'pdf', 'print']'. Only 'pdf' is
            disabled by default.
        column_visibility: Enable/Disable
            [column visibility](https://datatables.net/extensions/buttons/built-in#Column-visibility)
            extension
        search_builder: Enable/Disable [search builder](https://datatables.net/extensions/searchbuilder/)
            extension
        page_size: Default number of items to display in List page pagination.
            Default value is set to '10'.
        page_size_options: Pagination choices displayed in List page.
            Default value is set to '[10, 25, 50, 100]'. Use '-1'to display All
        responsive_table: Enable/Disable [responsive](https://datatables.net/extensions/responsive/)
            extension
        save_state: Enable/Disable [state saving](https://datatables.net/examples/basic_init/state_save.html)
        datatables_options: Dict of [Datatables options](https://datatables.net/reference/option/).
            These will overwrite any default options set for the datatable.
        list_template: List view template. Default is 'list.html'.
        detail_template: Details view template. Default is 'detail.html'.
        create_template: Edit view template. Default is 'create.html'.
        edit_template: Edit view template. Default is 'edit.html'.
        actions: List of actions
        additional_js_links: A list of additional JavaScript files to include.
        additional_css_links: A list of additional CSS files to include.

    """

    identity: Optional[str] = None
    name: Optional[str] = None
    fields: Sequence[BaseField] = []
    pk_attr: Optional[str] = None
    form_include_pk: bool = False
    exclude_fields_from_list: Sequence[str] = []
    exclude_fields_from_detail: Sequence[str] = []
    exclude_fields_from_create: Sequence[str] = []
    exclude_fields_from_edit: Sequence[str] = []
    searchable_fields: Optional[Sequence[str]] = None
    sortable_fields: Optional[Sequence[str]] = None
    fields_default_sort: Optional[Sequence[Union[Tuple[str, bool], str]]] = None
    export_types: Sequence[ExportType] = [
        ExportType.CSV,
        ExportType.EXCEL,
        ExportType.PRINT,
    ]
    export_fields: Optional[Sequence[str]] = None
    column_visibility: bool = True
    search_builder: bool = True
    page_size: int = 10
    page_size_options: Sequence[int] = [10, 25, 50, 100]
    responsive_table: bool = False
    save_state: bool = True
    datatables_options: ClassVar[Dict[str, Any]] = {}
    list_template: str = "list.html"
    detail_template: str = "detail.html"
    create_template: str = "create.html"
    edit_template: str = "edit.html"
    actions: Optional[Sequence[str]] = None
    row_actions: Optional[Sequence[str]] = None
    additional_js_links: Optional[List[str]] = None
    additional_css_links: Optional[List[str]] = None
    row_actions_display_type: RowActionsDisplayType = RowActionsDisplayType.ICON_LIST

    _find_foreign_model: Callable[[str], "BaseModelView"]

    def __init__(self) -> None:  # noqa: C901
        fringe = list(self.fields)
        all_field_names = []
        while len(fringe) > 0:
            field = fringe.pop(0)
            if not hasattr(field, "_name"):
                field._name = field.name  # type: ignore
            if isinstance(field, CollectionField):
                for f in field.fields:
                    f._name = f"{field._name}.{f.name}"  # type: ignore
                fringe.extend(field.fields)
            name = field._name  # type: ignore
            if name == self.pk_attr and not self.form_include_pk:
                field.exclude_from_create = True
                field.exclude_from_edit = True
            if name in self.exclude_fields_from_list:
                field.exclude_from_list = True
            if name in self.exclude_fields_from_detail:
                field.exclude_from_detail = True
            if name in self.exclude_fields_from_create:
                field.exclude_from_create = True
            if name in self.exclude_fields_from_edit:
                field.exclude_from_edit = True
            if not isinstance(field, CollectionField):
                all_field_names.append(name)
                field.searchable = (self.searchable_fields is None) or (
                    name in self.searchable_fields
                )
                field.orderable = (self.sortable_fields is None) or (
                    name in self.sortable_fields
                )
        if self.searchable_fields is None:
            self.searchable_fields = all_field_names[:]
        if self.sortable_fields is None:
            self.sortable_fields = all_field_names[:]
        if self.export_fields is None:
            self.export_fields = all_field_names[:]
        if self.fields_default_sort is None:
            self.fields_default_sort = [self.pk_attr]  # type: ignore[list-item]

        # Actions
        self._actions: Dict[str, Dict[str, str]] = OrderedDict()
        self._row_actions: Dict[str, Dict[str, str]] = OrderedDict()
        self._actions_handlers: Dict[
            str, Callable[[Request, Sequence[Any]], Awaitable]
        ] = OrderedDict()
        self._row_actions_handlers: Dict[str, Callable[[Request, Any], Awaitable]] = (
            OrderedDict()
        )
        self._init_actions()

    def is_active(self, request: Request) -> bool:
        return request.path_params.get("identity", None) == self.identity

    def _init_actions(self) -> None:
        self._init_batch_actions()
        self._init_row_actions()
        self._validate_actions()

    def _init_batch_actions(self) -> None:
        """
        This method initializes batch and row actions, collects their handlers,
        and validates that all specified actions exist.
        """
        for _method_name, method in inspect.getmembers(
            self, predicate=inspect.ismethod
        ):
            if hasattr(method, "_action"):
                name = method._action.get("name")
                self._actions[name] = method._action
                self._actions_handlers[name] = method

        if self.actions is None:
            self.actions = list(self._actions_handlers.keys())

    def _init_row_actions(self) -> None:
        for _method_name, method in inspect.getmembers(
            self, predicate=inspect.ismethod
        ):
            if hasattr(method, "_row_action"):
                name = method._row_action.get("name")
                self._row_actions[name] = method._row_action
                self._row_actions_handlers[name] = method

        if self.row_actions is None:
            self.row_actions = list(self._row_actions_handlers.keys())

    def _validate_actions(self) -> None:
        for action_name in not_none(self.actions):
            if action_name not in self._actions:
                raise ValueError(f"Unknown action with name '{action_name}'")
        for action_name in not_none(self.row_actions):
            if action_name not in self._row_actions:
                raise ValueError(f"Unknown row action with name '{action_name}'")

    async def is_action_allowed(self, request: Request, name: str) -> bool:
        """
        Verify if action with 'name' is allowed.
        Override this method to allow or disallow actions based
        on some condition.

        Args:
            name: Action name
            request: Starlette request
        """
        if name == "delete":
            return self.can_delete(request)
        return True

    async def is_row_action_allowed(self, request: Request, name: str) -> bool:
        """
        Verify if the row action with 'name' is allowed.
        Override this method to allow or disallow row actions based
        on some condition.

        Args:
            name: Row action name
            request: Starlette request
        """
        if name == "delete":
            return self.can_delete(request)
        if name == "edit":
            return self.can_edit(request)
        if name == "view":
            return self.can_view_details(request)
        return True

    async def get_all_actions(self, request: Request) -> List[Dict[str, Any]]:
        """Return a list of allowed batch actions"""
        actions = []
        for action_name in not_none(self.actions):
            if await self.is_action_allowed(request, action_name):
                actions.append(self._actions.get(action_name, {}))
        return actions

    async def get_all_row_actions(self, request: Request) -> List[Dict[str, Any]]:
        """Return a list of allowed row actions"""
        row_actions = []
        for row_action_name in not_none(self.row_actions):
            if await self.is_row_action_allowed(request, row_action_name):
                _row_action = self._row_actions.get(row_action_name, {})
                if (
                    request.state.action == RequestAction.LIST
                    and not _row_action.get("exclude_from_list")
                ) or (
                    request.state.action == RequestAction.DETAIL
                    and not _row_action.get("exclude_from_detail")
                ):
                    row_actions.append(_row_action)
        return row_actions

    async def handle_action(
        self, request: Request, pks: List[Any], name: str
    ) -> Union[str, Response]:
        """
        Handle action with 'name'.
        Raises:
            ActionFailed: to display meaningfully error
        """
        handler = self._actions_handlers.get(name, None)
        if handler is None:
            raise ActionFailed("Invalid action")
        if not await self.is_action_allowed(request, name):
            raise ActionFailed("Forbidden")
        handler_return = await handler(request, pks)
        custom_response = self._actions[name]["custom_response"]
        if isinstance(handler_return, Response) and not custom_response:
            raise ActionFailed(
                "Set custom_response to true, to be able to return custom response"
            )
        return handler_return

    async def handle_row_action(
        self, request: Request, pk: Any, name: str
    ) -> Union[str, Response]:
        """
        Handle row action with 'name'.
        Raises:
            ActionFailed: to display meaningfully error
        """
        handler = self._row_actions_handlers.get(name, None)
        if handler is None:
            raise ActionFailed("Invalid row action")
        if not await self.is_row_action_allowed(request, name):
            raise ActionFailed("Forbidden")
        handler_return = await handler(request, pk)
        custom_response = self._row_actions[name]["custom_response"]
        if isinstance(handler_return, Response) and not custom_response:
            raise ActionFailed(
                "Set custom_response to true, to be able to return custom response"
            )
        return handler_return

    @action(
        name="delete",
        text=_("Delete"),
        confirmation=_("Are you sure you want to delete selected items?"),
        submit_btn_text=_("Yes, delete all"),
        submit_btn_class="btn-danger",
    )
    async def delete_action(self, request: Request, pks: List[Any]) -> str:
        affected_rows = await self.delete(request, pks)
        return ngettext(
            "Item was successfully deleted",
            "%(count)d items were successfully deleted",
            affected_rows or 0,
        ) % {"count": affected_rows}

    @link_row_action(
        name="view",
        text=_("View"),
        icon_class="fa-solid fa-eye",
        exclude_from_detail=True,
    )
    def row_action_1_view(self, request: Request, pk: Any) -> str:
        route_name = request.app.state.ROUTE_NAME
        return str(
            request.url_for(route_name + ":detail", identity=self.identity, pk=pk)
        )

    @link_row_action(
        name="edit",
        text=_("Edit"),
        icon_class="fa-solid fa-edit",
        action_btn_class="btn-primary",
    )
    def row_action_2_edit(self, request: Request, pk: Any) -> str:
        route_name = request.app.state.ROUTE_NAME
        return str(request.url_for(route_name + ":edit", identity=self.identity, pk=pk))

    @row_action(
        name="delete",
        text=_("Delete"),
        confirmation=_("Are you sure you want to delete this item?"),
        icon_class="fa-solid fa-trash",
        submit_btn_text="Yes, delete",
        submit_btn_class="btn-danger",
        action_btn_class="btn-danger",
    )
    async def row_action_3_delete(self, request: Request, pk: Any) -> str:
        await self.delete(request, [pk])
        return gettext("Item was successfully deleted")

    @abstractmethod
    async def find_all(
        self,
        request: Request,
        skip: int = 0,
        limit: int = 100,
        where: Union[Dict[str, Any], str, None] = None,
        order_by: Optional[List[str]] = None,
    ) -> Sequence[Any]:
        """
        Find all items
        Parameters:
            request: The request being processed
            where: Can be dict for complex query
                json
                 {"and":[{"id": {"gt": 5}},{"name": {"startsWith": "ban"}}]}
                
                or plain text for full search
            skip: should return values start from position skip+1
            limit: number of maximum items to return
            order_by: order data clauses in form '["id asc", "name desc"]'
        """
        raise NotImplementedError()

    @abstractmethod
    async def count(
        self,
        request: Request,
        where: Union[Dict[str, Any], str, None] = None,
    ) -> int:
        """
        Count items
        Parameters:
            request: The request being processed
            where: Can be dict for complex query
                json
                 {"and":[{"id": {"gt": 5}},{"name": {"startsWith": "ban"}}]}
                
                or plain text for full search
        """
        raise NotImplementedError()

    @abstractmethod
    async def find_by_pk(self, request: Request, pk: Any) -> Any:
        """
        Find one item
        Parameters:
            request: The request being processed
            pk: Primary key
        """
        raise NotImplementedError()

    @abstractmethod
    async def find_by_pks(self, request: Request, pks: List[Any]) -> Sequence[Any]:
        """
        Find many items
        Parameters:
            request: The request being processed
            pks: List of Primary key
        """
        raise NotImplementedError()

    async def before_create(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        """
        This hook is called before a new item is created.

        Args:
            request: The request being processed.
            data: Dict values contained converted form data.
            obj: The object about to be created.
        """

    @abstractmethod
    async def create(self, request: Request, data: Dict) -> Any:
        """
        Create item
        Parameters:
            request: The request being processed
            data: Dict values contained converted form data
        Returns:
            Any: Created Item
        """
        raise NotImplementedError()

    async def after_create(self, request: Request, obj: Any) -> None:
        """
        This hook is called after a new item is successfully created.

        Args:
            request: The request being processed.
            obj: The newly created object.
        """

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        """
        This hook is called before an item is edited.

        Args:
            request: The request being processed.
            data: Dict values contained converted form data
            obj: The object about to be edited.
        """

    @abstractmethod
    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        """
        Edit item
        Parameters:
            request: The request being processed
            pk: Primary key
            data: Dict values contained converted form data
        Returns:
            Any: Edited Item
        """
        raise NotImplementedError()

    async def after_edit(self, request: Request, obj: Any) -> None:
        """
        This hook is called after an item is successfully edited.

        Args:
            request: The request being processed.
            obj: The edited object.
        """

    async def before_delete(self, request: Request, obj: Any) -> None:
        """
        This hook is called before an item is deleted.

        Args:
            request: The request being processed.
            obj: The object about to be deleted.
        """

    @abstractmethod
    async def delete(self, request: Request, pks: List[Any]) -> Optional[int]:
        """
        Bulk delete items
        Parameters:
            request: The request being processed
            pks: List of primary keys
        """
        raise NotImplementedError()

    async def after_delete(self, request: Request, obj: Any) -> None:
        """
        This hook is called after an item is successfully deleted.

        Args:
            request: The request being processed.
            obj: The deleted object.
        """

    def can_view_details(self, request: Request) -> bool:
        """Permission for viewing full details of Item. Return True by default"""
        return True

    def can_create(self, request: Request) -> bool:
        """Permission for creating new Items. Return True by default"""
        return True

    def can_edit(self, request: Request) -> bool:
        """Permission for editing Items. Return True by default"""
        return True

    def can_delete(self, request: Request) -> bool:
        """Permission for deleting Items. Return True by default"""
        return True

    async def serialize_field_value(
        self, value: Any, field: BaseField, action: RequestAction, request: Request
    ) -> Any:
        """
        Format output value for each field.

        !!! important

            The returned value should be json serializable

        Parameters:
            value: attribute of item returned by 'find_all' or 'find_by_pk'
            field: Starlette Admin field for this attribute
            action: Specify where the data will be used. Possible values are
                'VIEW' for detail page, 'EDIT' for editing page and 'API'
                for listing page and select2 data.
            request: The request being processed
        """
        if value is None:
            return await field.serialize_none_value(request, action)
        return await field.serialize_value(request, value, action)

    async def serialize(
        self,
        obj: Any,
        request: Request,
        action: RequestAction,
        include_relationships: bool = True,
        include_select2: bool = False,
    ) -> Dict[str, Any]:
        obj_serialized: Dict[str, Any] = {}
        obj_meta: Dict[str, Any] = {}
        for field in self.get_fields_list(request, action):
            if isinstance(field, RelationField) and include_relationships:
                value = getattr(obj, field.name, None)
                foreign_model = self._find_foreign_model(field.identity)  # type: ignore
                if value is None:
                    obj_serialized[field.name] = None
                elif isinstance(field, HasOne):
                    if action == RequestAction.EDIT:
                        obj_serialized[field.name] = (
                            await foreign_model.get_serialized_pk_value(request, value)
                        )
                    else:
                        obj_serialized[field.name] = await foreign_model.serialize(
                            value, request, action, include_relationships=False
                        )
                else:
                    if action == RequestAction.EDIT:
                        obj_serialized[field.name] = [
                            (await foreign_model.get_serialized_pk_value(request, obj))
                            for obj in value
                        ]
                    else:
                        obj_serialized[field.name] = [
                            await foreign_model.serialize(
                                v, request, action, include_relationships=False
                            )
                            for v in value
                        ]
            elif not isinstance(field, RelationField):
                value = await field.parse_obj(request, obj)
                obj_serialized[field.name] = await self.serialize_field_value(
                    value, field, action, request
                )
        if include_select2:
            obj_meta["select2"] = {
                "selection": await self.select2_selection(obj, request),
                "result": await self.select2_result(obj, request),
            }
        obj_meta["repr"] = await self.repr(obj, request)

        # Make sure the primary key is always available
        pk_attr = not_none(self.pk_attr)
        if pk_attr not in obj_serialized:
            pk_value = await self.get_serialized_pk_value(request, obj)
            obj_serialized[pk_attr] = pk_value

        pk = await self.get_pk_value(request, obj)
        route_name = request.app.state.ROUTE_NAME
        obj_meta["detailUrl"] = str(
            request.url_for(route_name + ":detail", identity=self.identity, pk=pk)
        )
        obj_serialized["_meta"] = obj_meta
        return obj_serialized

    async def repr(self, obj: Any, request: Request) -> str:
        """Return a string representation of the given object that can be displayed in the admin interface.

        If the object has a custom representation method '__admin_repr__', it is used to generate the string. Otherwise,
        the value of the object's primary key attribute is used.

        Args:
            obj: The object to represent.
            request: The request being processed

        Example:
            For example, the following implementation for a 'User' model will display
            the user's full name instead of their primary key in the admin interface:

            python
            class User:
                id: int
                first_name: str
                last_name: str

                def __admin_repr__(self, request: Request):
                    return f"{self.last_name} {self.first_name}"
            
        """
        repr_method = getattr(obj, "__admin_repr__", None)
        if repr_method is None:
            return str(await self.get_pk_value(request, obj))
        if inspect.iscoroutinefunction(repr_method):
            return await repr_method(request)
        return repr_method(request)

    async def select2_result(self, obj: Any, request: Request) -> str:
        """Returns an HTML-formatted string that represents the search results for a Select2 search box.

        By default, this method returns a string that contains all the object's attributes in a list except
        relation and file attributes.

        If the object has a custom representation method '__admin_select2_repr__', it is used to generate the
        HTML-formatted string.

        !!! note

            The returned value should be valid HTML.

        !!! danger

            Escape your database value to avoid Cross-Site Scripting (XSS) attack.
            You can use Jinja2 Template render with 'autoescape=True'.
            For more information [click here](https://owasp.org/www-community/attacks/xss/)

        Parameters:
            obj: The object returned by the 'find_all' or 'find_by_pk' method.
            request: The request being processed

        Example:
            Here is an example implementation for a 'User' model
            that includes the user's name and photo:

            python
            class User:
                id: int
                name: str
                photo_url: str

                def __admin_select2_repr__(self, request: Request) -> str:
                    return f''
            

        """
        template_str = (
            "<span>{%for col in fields %}{%if obj[col]%}<strong>{{col}}:"
            " </strong>{{obj[col]}} {%endif%}{%endfor%}</span>"
        )
        fields = [
            field.name
            for field in self.get_fields_list(request)
            if (
                not isinstance(field, (RelationField, FileField))
                and not field.exclude_from_detail
            )
        ]
        html_repr_method = getattr(
            obj,
            "__admin_select2_repr__",
            lambda request: Template(template_str, autoescape=True).render(
                obj=obj, fields=fields
            ),
        )
        if inspect.iscoroutinefunction(html_repr_method):
            return await html_repr_method(request)
        return html_repr_method(request)

    async def select2_selection(self, obj: Any, request: Request) -> str:
        """
        Returns the HTML representation of an item selected by a user in a Select2 component.
        By default, it simply calls 'select2_result()'.

        !!! note

            The returned value should be valid HTML.

        !!! danger

            Escape your database value to avoid Cross-Site Scripting (XSS) attack.
            You can use Jinja2 Template render with 'autoescape=True'.
            For more information [click here](https://owasp.org/www-community/attacks/xss/)

        Parameters:
            obj: item returned by 'find_all' or 'find_by_pk'
            request: The request being processed

        """
        return await self.select2_result(obj, request)

    async def get_pk_value(self, request: Request, obj: Any) -> Any:
        return getattr(obj, not_none(self.pk_attr))

    async def get_serialized_pk_value(self, request: Request, obj: Any) -> Any:
        """
        Return serialized value of the primary key.

        !!! note

            The returned value should be JSON-serializable.

        Parameters:
            request: The request being processed
            obj: object to get primary key of

        Returns:
            Any: Serialized value of a PK.
        """
        return await self.get_pk_value(request, obj)

    def _length_menu(self) -> Any:
        return [
            self.page_size_options,
            [(_("All") if i < 0 else i) for i in self.page_size_options],
        ]

    def _search_columns_selector(self) -> List[str]:
        return [f"{name}:name" for name in self.searchable_fields]  # type: ignore

    def _export_columns_selector(self) -> List[str]:
        return [f"{name}:name" for name in self.export_fields]  # type: ignore

    def get_fields_list(
        self,
        request: Request,
        action: RequestAction = RequestAction.LIST,
    ) -> Sequence[BaseField]:
        """Return a list of field instances to display in the specified view action.
        This function excludes fields with corresponding exclude flags, which are
        determined by the 'exclude_fields_from_*' attributes.

        Parameters:
             request: The request being processed.
             action: The type of action being performed on the view.
        """
        return extract_fields(self.fields, action)

    def _additional_css_links(
        self, request: Request, action: RequestAction
    ) -> Sequence[str]:
        links = self.additional_css_links or []
        for field in self.get_fields_list(request, action):
            for link in field.additional_css_links(request, action) or []:
                if link not in links:
                    links.append(link)
        return links

    def _additional_js_links(
        self, request: Request, action: RequestAction
    ) -> Sequence[str]:
        links = self.additional_js_links or []
        for field in self.get_fields_list(request, action):
            for link in field.additional_js_links(request, action) or []:
                if link not in links:
                    links.append(link)
        return links

    async def _configs(self, request: Request) -> Dict[str, Any]:
        locale = get_locale()
        return {
            "label": self.label,
            "pageSize": self.page_size,
            "lengthMenu": self._length_menu(),
            "searchColumns": self._search_columns_selector(),
            "exportColumns": self._export_columns_selector(),
            "fieldsDefaultSort": dict(
                (it, False) if isinstance(it, str) else it
                for it in self.fields_default_sort  # type: ignore[union-attr]
            ),
            "exportTypes": self.export_types,
            "columnVisibility": self.column_visibility,
            "searchBuilder": self.search_builder,
            "responsiveTable": self.responsive_table,
            "stateSave": self.save_state,
            "fields": [f.dict() for f in self.get_fields_list(request)],
            "pk": self.pk_attr,
            "locale": locale,
            "apiUrl": request.url_for(
                f"{request.app.state.ROUTE_NAME}:api", identity=self.identity
            ),
            "actionUrl": request.url_for(
                f"{request.app.state.ROUTE_NAME}:action", identity=self.identity
            ),
            "rowActionUrl": request.url_for(
                f"{request.app.state.ROUTE_NAME}:row-action", identity=self.identity
            ),
            "dt_i18n_url": request.url_for(
                f"{request.app.state.ROUTE_NAME}:statics", path=f"i18n/dt/{locale}.json"
            ),
            "datatablesOptions": self.datatables_options,
        }

after_create(request, obj) async

This hook is called after a new item is successfully created.

Parameters:
Name 	Type 	Description 	Default
request 	Request 	

The request being processed.
	required
obj 	Any 	

The newly created object.
	required
Source code in starlette_admin/views.py

async def after_create(self, request: Request, obj: Any) -> None:
    """
    This hook is called after a new item is successfully created.

    Args:
        request: The request being processed.
        obj: The newly created object.
    """

Source code in starlette_admin/views.py

async def after_create(self, request: Request, obj: Any) -> None:
    """
    This hook is called after a new item is successfully created.

    Args:
        request: The request being processed.
        obj: The newly created object.
    """

after_delete(request, obj) async

This hook is called after an item is successfully deleted.

Parameters:
Name 	Type 	Description 	Default
request 	Request 	

The request being processed.
	required
obj 	Any 	

The deleted object.
	required
Source code in starlette_admin/views.py

async def after_delete(self, request: Request, obj: Any) -> None:
    """
    This hook is called after an item is successfully deleted.

    Args:
        request: The request being processed.
        obj: The deleted object.
    """

Source code in starlette_admin/views.py

async def after_delete(self, request: Request, obj: Any) -> None:
    """
    This hook is called after an item is successfully deleted.

    Args:
        request: The request being processed.
        obj: The deleted object.
    """

after_edit(request, obj) async

This hook is called after an item is successfully edited.

Parameters:
Name 	Type 	Description 	Default
request 	Request 	

The request being processed.
	required
obj 	Any 	

The edited object.
	required
Source code in starlette_admin/views.py

async def after_edit(self, request: Request, obj: Any) -> None:
    """
    This hook is called after an item is successfully edited.

    Args:
        request: The request being processed.
        obj: The edited object.
    """

Source code in starlette_admin/views.py

async def after_edit(self, request: Request, obj: Any) -> None:
    """
    This hook is called after an item is successfully edited.

    Args:
        request: The request being processed.
        obj: The edited object.
    """

before_create(request, data, obj) async

This hook is called before a new item is created.

Parameters:
Name 	Type 	Description 	Default
request 	Request 	

The request being processed.
	required
data 	Dict[str, Any] 	

Dict values contained converted form data.
	required
obj 	Any 	

The object about to be created.
	required
Source code in starlette_admin/views.py

async def before_create(
    self, request: Request, data: Dict[str, Any], obj: Any
) -> None:
    """
    This hook is called before a new item is created.

    Args:
        request: The request being processed.
        data: Dict values contained converted form data.
        obj: The object about to be created.
    """

Source code in starlette_admin/views.py

async def before_create(
    self, request: Request, data: Dict[str, Any], obj: Any
) -> None:
    """
    This hook is called before a new item is created.

    Args:
        request: The request being processed.
        data: Dict values contained converted form data.
        obj: The object about to be created.
    """

before_delete(request, obj) async

This hook is called before an item is deleted.

Parameters:
Name 	Type 	Description 	Default
request 	Request 	

The request being processed.
	required
obj 	Any 	

The object about to be deleted.
	required
Source code in starlette_admin/views.py

async def before_delete(self, request: Request, obj: Any) -> None:
    """
    This hook is called before an item is deleted.

    Args:
        request: The request being processed.
        obj: The object about to be deleted.
    """

Source code in starlette_admin/views.py

async def before_delete(self, request: Request, obj: Any) -> None:
    """
    This hook is called before an item is deleted.

    Args:
        request: The request being processed.
        obj: The object about to be deleted.
    """

before_edit(request, data, obj) async

This hook is called before an item is edited.

Parameters:
Name 	Type 	Description 	Default
request 	Request 	

The request being processed.
	required
data 	Dict[str, Any] 	

Dict values contained converted form data
	required
obj 	Any 	

The object about to be edited.
	required
Source code in starlette_admin/views.py

async def before_edit(
    self, request: Request, data: Dict[str, Any], obj: Any
) -> None:
    """
    This hook is called before an item is edited.

    Args:
        request: The request being processed.
        data: Dict values contained converted form data
        obj: The object about to be edited.
    """

Source code in starlette_admin/views.py

async def before_edit(
    self, request: Request, data: Dict[str, Any], obj: Any
) -> None:
    """
    This hook is called before an item is edited.

    Args:
        request: The request being processed.
        data: Dict values contained converted form data
        obj: The object about to be edited.
    """

can_create(request)

Permission for creating new Items. Return True by default
Source code in starlette_admin/views.py

def can_create(self, request: Request) -> bool:
    """Permission for creating new Items. Return True by default"""
    return True

Source code in starlette_admin/views.py

def can_create(self, request: Request) -> bool:
    """Permission for creating new Items. Return True by default"""
    return True

can_delete(request)

Permission for deleting Items. Return True by default
Source code in starlette_admin/views.py

def can_delete(self, request: Request) -> bool:
    """Permission for deleting Items. Return True by default"""
    return True

Source code in starlette_admin/views.py

def can_delete(self, request: Request) -> bool:
    """Permission for deleting Items. Return True by default"""
    return True

can_edit(request)

Permission for editing Items. Return True by default
Source code in starlette_admin/views.py

def can_edit(self, request: Request) -> bool:
    """Permission for editing Items. Return True by default"""
    return True

Source code in starlette_admin/views.py

def can_edit(self, request: Request) -> bool:
    """Permission for editing Items. Return True by default"""
    return True

can_view_details(request)

Permission for viewing full details of Item. Return True by default
Source code in starlette_admin/views.py

def can_view_details(self, request: Request) -> bool:
    """Permission for viewing full details of Item. Return True by default"""
    return True

Source code in starlette_admin/views.py

def can_view_details(self, request: Request) -> bool:
    """Permission for viewing full details of Item. Return True by default"""
    return True

count(request, where=None) abstractmethod async

Count items Parameters: request: The request being processed where: Can be dict for complex query

 {"and":[{"id": {"gt": 5}},{"name": {"startsWith": "ban"}}]}

or plain text for full search

Source code in starlette_admin/views.py

@abstractmethod
async def count(
    self,
    request: Request,
    where: Union[Dict[str, Any], str, None] = None,
) -> int:
    """
    Count items
    Parameters:
        request: The request being processed
        where: Can be dict for complex query
            json
             {"and":[{"id": {"gt": 5}},{"name": {"startsWith": "ban"}}]}
            
            or plain text for full search
    """
    raise NotImplementedError()

Source code in starlette_admin/views.py

@abstractmethod
async def count(
    self,
    request: Request,
    where: Union[Dict[str, Any], str, None] = None,
) -> int:
    """
    Count items
    Parameters:
        request: The request being processed
        where: Can be dict for complex query
            json
             {"and":[{"id": {"gt": 5}},{"name": {"startsWith": "ban"}}]}
            
            or plain text for full search
    """
    raise NotImplementedError()

create(request, data) abstractmethod async

Create item Parameters: request: The request being processed data: Dict values contained converted form data Returns: Any: Created Item
Source code in starlette_admin/views.py

@abstractmethod
async def create(self, request: Request, data: Dict) -> Any:
    """
    Create item
    Parameters:
        request: The request being processed
        data: Dict values contained converted form data
    Returns:
        Any: Created Item
    """
    raise NotImplementedError()

Source code in starlette_admin/views.py

@abstractmethod
async def create(self, request: Request, data: Dict) -> Any:
    """
    Create item
    Parameters:
        request: The request being processed
        data: Dict values contained converted form data
    Returns:
        Any: Created Item
    """
    raise NotImplementedError()

delete(request, pks) abstractmethod async

Bulk delete items Parameters: request: The request being processed pks: List of primary keys
Source code in starlette_admin/views.py

@abstractmethod
async def delete(self, request: Request, pks: List[Any]) -> Optional[int]:
    """
    Bulk delete items
    Parameters:
        request: The request being processed
        pks: List of primary keys
    """
    raise NotImplementedError()

Source code in starlette_admin/views.py

@abstractmethod
async def delete(self, request: Request, pks: List[Any]) -> Optional[int]:
    """
    Bulk delete items
    Parameters:
        request: The request being processed
        pks: List of primary keys
    """
    raise NotImplementedError()

edit(request, pk, data) abstractmethod async

Edit item Parameters: request: The request being processed pk: Primary key data: Dict values contained converted form data Returns: Any: Edited Item
Source code in starlette_admin/views.py

@abstractmethod
async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
    """
    Edit item
    Parameters:
        request: The request being processed
        pk: Primary key
        data: Dict values contained converted form data
    Returns:
        Any: Edited Item
    """
    raise NotImplementedError()

Source code in starlette_admin/views.py

@abstractmethod
async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
    """
    Edit item
    Parameters:
        request: The request being processed
        pk: Primary key
        data: Dict values contained converted form data
    Returns:
        Any: Edited Item
    """
    raise NotImplementedError()

find_all(request, skip=0, limit=100, where=None, order_by=None) abstractmethod async

Find all items Parameters: request: The request being processed where: Can be dict for complex query

 {"and":[{"id": {"gt": 5}},{"name": {"startsWith": "ban"}}]}

or plain text for full search skip: should return values start from position skip+1 limit: number of maximum items to return order_by: order data clauses in form ["id asc", "name desc"]

Source code in starlette_admin/views.py

@abstractmethod
async def find_all(
    self,
    request: Request,
    skip: int = 0,
    limit: int = 100,
    where: Union[Dict[str, Any], str, None] = None,
    order_by: Optional[List[str]] = None,
) -> Sequence[Any]:
    """
    Find all items
    Parameters:
        request: The request being processed
        where: Can be dict for complex query
            json
             {"and":[{"id": {"gt": 5}},{"name": {"startsWith": "ban"}}]}
            
            or plain text for full search
        skip: should return values start from position skip+1
        limit: number of maximum items to return
        order_by: order data clauses in form '["id asc", "name desc"]'
    """
    raise NotImplementedError()

Source code in starlette_admin/views.py

@abstractmethod
async def find_all(
    self,
    request: Request,
    skip: int = 0,
    limit: int = 100,
    where: Union[Dict[str, Any], str, None] = None,
    order_by: Optional[List[str]] = None,
) -> Sequence[Any]:
    """
    Find all items
    Parameters:
        request: The request being processed
        where: Can be dict for complex query
            json
             {"and":[{"id": {"gt": 5}},{"name": {"startsWith": "ban"}}]}
            
            or plain text for full search
        skip: should return values start from position skip+1
        limit: number of maximum items to return
        order_by: order data clauses in form '["id asc", "name desc"]'
    """
    raise NotImplementedError()

find_by_pk(request, pk) abstractmethod async

Find one item Parameters: request: The request being processed pk: Primary key
Source code in starlette_admin/views.py

@abstractmethod
async def find_by_pk(self, request: Request, pk: Any) -> Any:
    """
    Find one item
    Parameters:
        request: The request being processed
        pk: Primary key
    """
    raise NotImplementedError()

Source code in starlette_admin/views.py

@abstractmethod
async def find_by_pk(self, request: Request, pk: Any) -> Any:
    """
    Find one item
    Parameters:
        request: The request being processed
        pk: Primary key
    """
    raise NotImplementedError()

find_by_pks(request, pks) abstractmethod async

Find many items Parameters: request: The request being processed pks: List of Primary key
Source code in starlette_admin/views.py

@abstractmethod
async def find_by_pks(self, request: Request, pks: List[Any]) -> Sequence[Any]:
    """
    Find many items
    Parameters:
        request: The request being processed
        pks: List of Primary key
    """
    raise NotImplementedError()

Source code in starlette_admin/views.py

@abstractmethod
async def find_by_pks(self, request: Request, pks: List[Any]) -> Sequence[Any]:
    """
    Find many items
    Parameters:
        request: The request being processed
        pks: List of Primary key
    """
    raise NotImplementedError()

get_all_actions(request) async

Return a list of allowed batch actions
Source code in starlette_admin/views.py

async def get_all_actions(self, request: Request) -> List[Dict[str, Any]]:
    """Return a list of allowed batch actions"""
    actions = []
    for action_name in not_none(self.actions):
        if await self.is_action_allowed(request, action_name):
            actions.append(self._actions.get(action_name, {}))
    return actions

Source code in starlette_admin/views.py

async def get_all_actions(self, request: Request) -> List[Dict[str, Any]]:
    """Return a list of allowed batch actions"""
    actions = []
    for action_name in not_none(self.actions):
        if await self.is_action_allowed(request, action_name):
            actions.append(self._actions.get(action_name, {}))
    return actions

get_all_row_actions(request) async

Return a list of allowed row actions
Source code in starlette_admin/views.py

async def get_all_row_actions(self, request: Request) -> List[Dict[str, Any]]:
    """Return a list of allowed row actions"""
    row_actions = []
    for row_action_name in not_none(self.row_actions):
        if await self.is_row_action_allowed(request, row_action_name):
            _row_action = self._row_actions.get(row_action_name, {})
            if (
                request.state.action == RequestAction.LIST
                and not _row_action.get("exclude_from_list")
            ) or (
                request.state.action == RequestAction.DETAIL
                and not _row_action.get("exclude_from_detail")
            ):
                row_actions.append(_row_action)
    return row_actions

Source code in starlette_admin/views.py

async def get_all_row_actions(self, request: Request) -> List[Dict[str, Any]]:
    """Return a list of allowed row actions"""
    row_actions = []
    for row_action_name in not_none(self.row_actions):
        if await self.is_row_action_allowed(request, row_action_name):
            _row_action = self._row_actions.get(row_action_name, {})
            if (
                request.state.action == RequestAction.LIST
                and not _row_action.get("exclude_from_list")
            ) or (
                request.state.action == RequestAction.DETAIL
                and not _row_action.get("exclude_from_detail")
            ):
                row_actions.append(_row_action)
    return row_actions

get_fields_list(request, action=RequestAction.LIST)

Return a list of field instances to display in the specified view action. This function excludes fields with corresponding exclude flags, which are determined by the exclude_fields_from_* attributes.

Parameters:
Name 	Type 	Description 	Default
request 	Request 	

The request being processed.
	required
action 	RequestAction 	

The type of action being performed on the view.
	LIST
Source code in starlette_admin/views.py

def get_fields_list(
    self,
    request: Request,
    action: RequestAction = RequestAction.LIST,
) -> Sequence[BaseField]:
    """Return a list of field instances to display in the specified view action.
    This function excludes fields with corresponding exclude flags, which are
    determined by the 'exclude_fields_from_*' attributes.

    Parameters:
         request: The request being processed.
         action: The type of action being performed on the view.
    """
    return extract_fields(self.fields, action)

Source code in starlette_admin/views.py

def get_fields_list(
    self,
    request: Request,
    action: RequestAction = RequestAction.LIST,
) -> Sequence[BaseField]:
    """Return a list of field instances to display in the specified view action.
    This function excludes fields with corresponding exclude flags, which are
    determined by the 'exclude_fields_from_*' attributes.

    Parameters:
         request: The request being processed.
         action: The type of action being performed on the view.
    """
    return extract_fields(self.fields, action)

get_serialized_pk_value(request, obj) async

Return serialized value of the primary key.

Note

The returned value should be JSON-serializable.

Parameters:
Name 	Type 	Description 	Default
request 	Request 	

The request being processed
	required
obj 	Any 	

object to get primary key of
	required

Returns:
Name 	Type 	Description
Any 	Any 	

Serialized value of a PK.
Source code in starlette_admin/views.py

async def get_serialized_pk_value(self, request: Request, obj: Any) -> Any:
    """
    Return serialized value of the primary key.

    !!! note

        The returned value should be JSON-serializable.

    Parameters:
        request: The request being processed
        obj: object to get primary key of

    Returns:
        Any: Serialized value of a PK.
    """
    return await self.get_pk_value(request, obj)

Source code in starlette_admin/views.py

async def get_serialized_pk_value(self, request: Request, obj: Any) -> Any:
    """
    Return serialized value of the primary key.

    !!! note

        The returned value should be JSON-serializable.

    Parameters:
        request: The request being processed
        obj: object to get primary key of

    Returns:
        Any: Serialized value of a PK.
    """
    return await self.get_pk_value(request, obj)

handle_action(request, pks, name) async

Handle action with name. Raises: ActionFailed: to display meaningfully error
Source code in starlette_admin/views.py

async def handle_action(
    self, request: Request, pks: List[Any], name: str
) -> Union[str, Response]:
    """
    Handle action with 'name'.
    Raises:
        ActionFailed: to display meaningfully error
    """
    handler = self._actions_handlers.get(name, None)
    if handler is None:
        raise ActionFailed("Invalid action")
    if not await self.is_action_allowed(request, name):
        raise ActionFailed("Forbidden")
    handler_return = await handler(request, pks)
    custom_response = self._actions[name]["custom_response"]
    if isinstance(handler_return, Response) and not custom_response:
        raise ActionFailed(
            "Set custom_response to true, to be able to return custom response"
        )
    return handler_return

Source code in starlette_admin/views.py

async def handle_action(
    self, request: Request, pks: List[Any], name: str
) -> Union[str, Response]:
    """
    Handle action with 'name'.
    Raises:
        ActionFailed: to display meaningfully error
    """
    handler = self._actions_handlers.get(name, None)
    if handler is None:
        raise ActionFailed("Invalid action")
    if not await self.is_action_allowed(request, name):
        raise ActionFailed("Forbidden")
    handler_return = await handler(request, pks)
    custom_response = self._actions[name]["custom_response"]
    if isinstance(handler_return, Response) and not custom_response:
        raise ActionFailed(
            "Set custom_response to true, to be able to return custom response"
        )
    return handler_return

handle_row_action(request, pk, name) async

Handle row action with name. Raises: ActionFailed: to display meaningfully error
Source code in starlette_admin/views.py

async def handle_row_action(
    self, request: Request, pk: Any, name: str
) -> Union[str, Response]:
    """
    Handle row action with 'name'.
    Raises:
        ActionFailed: to display meaningfully error
    """
    handler = self._row_actions_handlers.get(name, None)
    if handler is None:
        raise ActionFailed("Invalid row action")
    if not await self.is_row_action_allowed(request, name):
        raise ActionFailed("Forbidden")
    handler_return = await handler(request, pk)
    custom_response = self._row_actions[name]["custom_response"]
    if isinstance(handler_return, Response) and not custom_response:
        raise ActionFailed(
            "Set custom_response to true, to be able to return custom response"
        )
    return handler_return

Source code in starlette_admin/views.py

async def handle_row_action(
    self, request: Request, pk: Any, name: str
) -> Union[str, Response]:
    """
    Handle row action with 'name'.
    Raises:
        ActionFailed: to display meaningfully error
    """
    handler = self._row_actions_handlers.get(name, None)
    if handler is None:
        raise ActionFailed("Invalid row action")
    if not await self.is_row_action_allowed(request, name):
        raise ActionFailed("Forbidden")
    handler_return = await handler(request, pk)
    custom_response = self._row_actions[name]["custom_response"]
    if isinstance(handler_return, Response) and not custom_response:
        raise ActionFailed(
            "Set custom_response to true, to be able to return custom response"
        )
    return handler_return

is_action_allowed(request, name) async

Verify if action with name is allowed. Override this method to allow or disallow actions based on some condition.

Parameters:
Name 	Type 	Description 	Default
name 	str 	

Action name
	required
request 	Request 	

Starlette request
	required
Source code in starlette_admin/views.py

async def is_action_allowed(self, request: Request, name: str) -> bool:
    """
    Verify if action with 'name' is allowed.
    Override this method to allow or disallow actions based
    on some condition.

    Args:
        name: Action name
        request: Starlette request
    """
    if name == "delete":
        return self.can_delete(request)
    return True

Source code in starlette_admin/views.py

async def is_action_allowed(self, request: Request, name: str) -> bool:
    """
    Verify if action with 'name' is allowed.
    Override this method to allow or disallow actions based
    on some condition.

    Args:
        name: Action name
        request: Starlette request
    """
    if name == "delete":
        return self.can_delete(request)
    return True

is_row_action_allowed(request, name) async

Verify if the row action with name is allowed. Override this method to allow or disallow row actions based on some condition.

Parameters:
Name 	Type 	Description 	Default
name 	str 	

Row action name
	required
request 	Request 	

Starlette request
	required
Source code in starlette_admin/views.py

async def is_row_action_allowed(self, request: Request, name: str) -> bool:
    """
    Verify if the row action with 'name' is allowed.
    Override this method to allow or disallow row actions based
    on some condition.

    Args:
        name: Row action name
        request: Starlette request
    """
    if name == "delete":
        return self.can_delete(request)
    if name == "edit":
        return self.can_edit(request)
    if name == "view":
        return self.can_view_details(request)
    return True

Source code in starlette_admin/views.py

async def is_row_action_allowed(self, request: Request, name: str) -> bool:
    """
    Verify if the row action with 'name' is allowed.
    Override this method to allow or disallow row actions based
    on some condition.

    Args:
        name: Row action name
        request: Starlette request
    """
    if name == "delete":
        return self.can_delete(request)
    if name == "edit":
        return self.can_edit(request)
    if name == "view":
        return self.can_view_details(request)
    return True

repr(obj, request) async

Return a string representation of the given object that can be displayed in the admin interface.

If the object has a custom representation method __admin_repr__, it is used to generate the string. Otherwise, the value of the object's primary key attribute is used.

Parameters:
Name 	Type 	Description 	Default
obj 	Any 	

The object to represent.
	required
request 	Request 	

The request being processed
	required
Example

For example, the following implementation for a User model will display the user's full name instead of their primary key in the admin interface:

class User:
    id: int
    first_name: str
    last_name: str

    def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}"

Example

For example, the following implementation for a User model will display the user's full name instead of their primary key in the admin interface:

class User:
    id: int
    first_name: str
    last_name: str

    def __admin_repr__(self, request: Request):
        return f"{self.last_name} {self.first_name}"

Source code in starlette_admin/views.py

async def repr(self, obj: Any, request: Request) -> str:
    """Return a string representation of the given object that can be displayed in the admin interface.

    If the object has a custom representation method '__admin_repr__', it is used to generate the string. Otherwise,
    the value of the object's primary key attribute is used.

    Args:
        obj: The object to represent.
        request: The request being processed

    Example:
        For example, the following implementation for a 'User' model will display
        the user's full name instead of their primary key in the admin interface:

        python
        class User:
            id: int
            first_name: str
            last_name: str

            def __admin_repr__(self, request: Request):
                return f"{self.last_name} {self.first_name}"
        
    """
    repr_method = getattr(obj, "__admin_repr__", None)
    if repr_method is None:
        return str(await self.get_pk_value(request, obj))
    if inspect.iscoroutinefunction(repr_method):
        return await repr_method(request)
    return repr_method(request)

Source code in starlette_admin/views.py

async def repr(self, obj: Any, request: Request) -> str:
    """Return a string representation of the given object that can be displayed in the admin interface.

    If the object has a custom representation method '__admin_repr__', it is used to generate the string. Otherwise,
    the value of the object's primary key attribute is used.

    Args:
        obj: The object to represent.
        request: The request being processed

    Example:
        For example, the following implementation for a 'User' model will display
        the user's full name instead of their primary key in the admin interface:

        python
        class User:
            id: int
            first_name: str
            last_name: str

            def __admin_repr__(self, request: Request):
                return f"{self.last_name} {self.first_name}"
        
    """
    repr_method = getattr(obj, "__admin_repr__", None)
    if repr_method is None:
        return str(await self.get_pk_value(request, obj))
    if inspect.iscoroutinefunction(repr_method):
        return await repr_method(request)
    return repr_method(request)

select2_result(obj, request) async

Returns an HTML-formatted string that represents the search results for a Select2 search box.

By default, this method returns a string that contains all the object's attributes in a list except relation and file attributes.

If the object has a custom representation method __admin_select2_repr__, it is used to generate the HTML-formatted string.

Note

The returned value should be valid HTML.

Danger

Escape your database value to avoid Cross-Site Scripting (XSS) attack. You can use Jinja2 Template render with autoescape=True. For more information click here

Parameters:
Name 	Type 	Description 	Default
obj 	Any 	

The object returned by the find_all or find_by_pk method.
	required
request 	Request 	

The request being processed
	required
Example

Here is an example implementation for a User model that includes the user's name and photo:

class User:
    id: int
    name: str
    photo_url: str

    def __admin_select2_repr__(self, request: Request) -> str:
        return f''

Example

Here is an example implementation for a User model that includes the user's name and photo:

class User:
    id: int
    name: str
    photo_url: str

    def __admin_select2_repr__(self, request: Request) -> str:
        return f''

Source code in starlette_admin/views.py

async def select2_result(self, obj: Any, request: Request) -> str:
    """Returns an HTML-formatted string that represents the search results for a Select2 search box.

    By default, this method returns a string that contains all the object's attributes in a list except
    relation and file attributes.

    If the object has a custom representation method '__admin_select2_repr__', it is used to generate the
    HTML-formatted string.

    !!! note

        The returned value should be valid HTML.

    !!! danger

        Escape your database value to avoid Cross-Site Scripting (XSS) attack.
        You can use Jinja2 Template render with 'autoescape=True'.
        For more information [click here](https://owasp.org/www-community/attacks/xss/)

    Parameters:
        obj: The object returned by the 'find_all' or 'find_by_pk' method.
        request: The request being processed

    Example:
        Here is an example implementation for a 'User' model
        that includes the user's name and photo:

        python
        class User:
            id: int
            name: str
            photo_url: str

            def __admin_select2_repr__(self, request: Request) -> str:
                return f''
        

    """
    template_str = (
        "<span>{%for col in fields %}{%if obj[col]%}<strong>{{col}}:"
        " </strong>{{obj[col]}} {%endif%}{%endfor%}</span>"
    )
    fields = [
        field.name
        for field in self.get_fields_list(request)
        if (
            not isinstance(field, (RelationField, FileField))
            and not field.exclude_from_detail
        )
    ]
    html_repr_method = getattr(
        obj,
        "__admin_select2_repr__",
        lambda request: Template(template_str, autoescape=True).render(
            obj=obj, fields=fields
        ),
    )
    if inspect.iscoroutinefunction(html_repr_method):
        return await html_repr_method(request)
    return html_repr_method(request)

Source code in starlette_admin/views.py

async def select2_result(self, obj: Any, request: Request) -> str:
    """Returns an HTML-formatted string that represents the search results for a Select2 search box.

    By default, this method returns a string that contains all the object's attributes in a list except
    relation and file attributes.

    If the object has a custom representation method '__admin_select2_repr__', it is used to generate the
    HTML-formatted string.

    !!! note

        The returned value should be valid HTML.

    !!! danger

        Escape your database value to avoid Cross-Site Scripting (XSS) attack.
        You can use Jinja2 Template render with 'autoescape=True'.
        For more information [click here](https://owasp.org/www-community/attacks/xss/)

    Parameters:
        obj: The object returned by the 'find_all' or 'find_by_pk' method.
        request: The request being processed

    Example:
        Here is an example implementation for a 'User' model
        that includes the user's name and photo:

        python
        class User:
            id: int
            name: str
            photo_url: str

            def __admin_select2_repr__(self, request: Request) -> str:
                return f''
        

    """
    template_str = (
        "<span>{%for col in fields %}{%if obj[col]%}<strong>{{col}}:"
        " </strong>{{obj[col]}} {%endif%}{%endfor%}</span>"
    )
    fields = [
        field.name
        for field in self.get_fields_list(request)
        if (
            not isinstance(field, (RelationField, FileField))
            and not field.exclude_from_detail
        )
    ]
    html_repr_method = getattr(
        obj,
        "__admin_select2_repr__",
        lambda request: Template(template_str, autoescape=True).render(
            obj=obj, fields=fields
        ),
    )
    if inspect.iscoroutinefunction(html_repr_method):
        return await html_repr_method(request)
    return html_repr_method(request)

select2_selection(obj, request) async

Returns the HTML representation of an item selected by a user in a Select2 component. By default, it simply calls select2_result().

Note

The returned value should be valid HTML.

Danger

Escape your database value to avoid Cross-Site Scripting (XSS) attack. You can use Jinja2 Template render with autoescape=True. For more information click here

Parameters:
Name 	Type 	Description 	Default
obj 	Any 	

item returned by find_all or find_by_pk
	required
request 	Request 	

The request being processed
	required
Source code in starlette_admin/views.py

async def select2_selection(self, obj: Any, request: Request) -> str:
    """
    Returns the HTML representation of an item selected by a user in a Select2 component.
    By default, it simply calls 'select2_result()'.

    !!! note

        The returned value should be valid HTML.

    !!! danger

        Escape your database value to avoid Cross-Site Scripting (XSS) attack.
        You can use Jinja2 Template render with 'autoescape=True'.
        For more information [click here](https://owasp.org/www-community/attacks/xss/)

    Parameters:
        obj: item returned by 'find_all' or 'find_by_pk'
        request: The request being processed

    """
    return await self.select2_result(obj, request)

Source code in starlette_admin/views.py

async def select2_selection(self, obj: Any, request: Request) -> str:
    """
    Returns the HTML representation of an item selected by a user in a Select2 component.
    By default, it simply calls 'select2_result()'.

    !!! note

        The returned value should be valid HTML.

    !!! danger

        Escape your database value to avoid Cross-Site Scripting (XSS) attack.
        You can use Jinja2 Template render with 'autoescape=True'.
        For more information [click here](https://owasp.org/www-community/attacks/xss/)

    Parameters:
        obj: item returned by 'find_all' or 'find_by_pk'
        request: The request being processed

    """
    return await self.select2_result(obj, request)

serialize_field_value(value, field, action, request) async

Format output value for each field.

Important

The returned value should be json serializable

Parameters:
Name 	Type 	Description 	Default
value 	Any 	

attribute of item returned by find_all or find_by_pk
	required
field 	BaseField 	

Starlette Admin field for this attribute
	required
action 	RequestAction 	

Specify where the data will be used. Possible values are VIEW for detail page, EDIT for editing page and API for listing page and select2 data.
	required
request 	Request 	

The request being processed
	required
Source code in starlette_admin/views.py

async def serialize_field_value(
    self, value: Any, field: BaseField, action: RequestAction, request: Request
) -> Any:
    """
    Format output value for each field.

    !!! important

        The returned value should be json serializable

    Parameters:
        value: attribute of item returned by 'find_all' or 'find_by_pk'
        field: Starlette Admin field for this attribute
        action: Specify where the data will be used. Possible values are
            'VIEW' for detail page, 'EDIT' for editing page and 'API'
            for listing page and select2 data.
        request: The request being processed
    """
    if value is None:
        return await field.serialize_none_value(request, action)
    return await field.serialize_value(request, value, action)

async def serialize_field_value(
    self, value: Any, field: BaseField, action: RequestAction, request: Request
) -> Any:
    """
    Format output value for each field.

    !!! important

        The returned value should be json serializable

    Parameters:
        value: attribute of item returned by 'find_all' or 'find_by_pk'
        field: Starlette Admin field for this attribute
        action: Specify where the data will be used. Possible values are
            'VIEW' for detail page, 'EDIT' for editing page and 'API'
            for listing page and select2 data.
        request: The request being processed
    """
    if value is None:
        return await field.serialize_none_value(request, action)
    return await field.serialize_value(request, value, action)

BaseAdmin

Base class for implementing Admin interface.
Source code in starlette_admin/base.py

class BaseAdmin:
    """Base class for implementing Admin interface."""

    def __init__(
        self,
        title: str = _("Admin"),
        base_url: str = "/admin",
        route_name: str = "admin",
        logo_url: Optional[str] = None,
        login_logo_url: Optional[str] = None,
        templates_dir: str = "templates",
        statics_dir: Optional[str] = None,
        index_view: Optional[CustomView] = None,
        auth_provider: Optional[BaseAuthProvider] = None,
        middlewares: Optional[Sequence[Middleware]] = None,
        debug: bool = False,
        i18n_config: Optional[I18nConfig] = None,
        timezone_config: Optional[TimezoneConfig] = None,
        favicon_url: Optional[str] = None,
    ):
        """
        Parameters:
            title: Admin title.
            base_url: Base URL for Admin interface.
            route_name: Mounted Admin name
            logo_url: URL of logo to be displayed instead of title.
            login_logo_url: If set, it will be used for login interface instead of logo_url.
            templates_dir: Templates dir for customisation
            statics_dir: Statics dir for customisation
            index_view: CustomView to use for index page.
            auth_provider: Authentication Provider
            middlewares: Starlette middlewares
            i18n_config: i18n configuration
            timezone_config: timezone configuration
            favicon_url: URL of favicon.
        """
        self.title = title
        self.base_url = base_url
        self.route_name = route_name
        self.logo_url = logo_url
        self.login_logo_url = login_logo_url
        self.favicon_url = favicon_url
        self.templates_dir = templates_dir
        self.statics_dir = statics_dir
        self.auth_provider = auth_provider
        self.middlewares = list(middlewares) if middlewares is not None else []
        self.index_view = (
            index_view
            if (index_view is not None)
            else CustomView("", add_to_menu=False)
        )
        self._views: List[BaseView] = []
        self._models: List[BaseModelView] = []
        self.routes: List[Union[Route, Mount]] = []
        self.debug = debug
        self.i18n_config = i18n_config
        self.timezone_config = timezone_config
        self._setup_templates()
        self.init_locale()
        self.init_auth()
        self.init_routes()

    def add_view(self, view: Union[Type[BaseView], BaseView]) -> None:
        """
        Add View to the Admin interface.
        """
        view_instance = view if isinstance(view, BaseView) else view()
        self._views.append(view_instance)
        self.setup_view(view_instance)

    def custom_render_js(self, request: Request) -> Optional[str]:
        """
        Override this function to provide a link to custom js to override the
        global 'render' object in javascript which is use to render fields in
        list page.

        Args:
            request: Starlette Request
        """
        return None

    def init_locale(self) -> None:
        if self.i18n_config is not None:
            try:
                import babel  # noqa
            except ImportError as err:
                raise ImportError(
                    "'babel' package is required to use i18n features."
                    "Install it with 'pip install starlette-admin[i18n]'"
                ) from err
            self.middlewares.insert(
                0, Middleware(LocaleMiddleware, i18n_config=self.i18n_config)
            )

        if self.timezone_config is not None:
            self.middlewares.insert(
                0, Middleware(TimezoneMiddleware, timezone_config=self.timezone_config)
            )

    def init_auth(self) -> None:
        if self.auth_provider is not None:
            self.auth_provider.setup_admin(self)

    def init_routes(self) -> None:
        statics = StaticFiles(directory=self.statics_dir, packages=["starlette_admin"])
        self.routes.extend(
            [
                Mount("/statics", app=statics, name="statics"),
                Route(
                    self.index_view.path,
                    self._render_custom_view(self.index_view),
                    methods=self.index_view.methods,
                    name="index",
                ),
                Route(
                    "/api/{identity}",
                    self._render_api,
                    methods=["GET"],
                    name="api",
                ),
                Route(
                    "/api/{identity}/action",
                    self.handle_action,
                    methods=["GET", "POST"],
                    name="action",
                ),
                Route(
                    "/api/{identity}/row-action",
                    self.handle_row_action,
                    methods=["GET", "POST"],
                    name="row-action",
                ),
                Route(
                    "/{identity}/list",
                    self._render_list,
                    methods=["GET"],
                    name="list",
                ),
                Route(
                    "/{identity}/detail/{pk}",
                    self._render_detail,
                    methods=["GET"],
                    name="detail",
                ),
                Route(
                    "/{identity}/create",
                    self._render_create,
                    methods=["GET", "POST"],
                    name="create",
                ),
                Route(
                    "/{identity}/edit/{pk}",
                    self._render_edit,
                    methods=["GET", "POST"],
                    name="edit",
                ),
            ]
        )
        if self.index_view.add_to_menu:
            self._views.append(self.index_view)

    def _setup_templates(self) -> None:
        env = Environment(
            loader=ChoiceLoader(
                [
                    FileSystemLoader(self.templates_dir),
                    PackageLoader("starlette_admin", "templates"),
                    PrefixLoader(
                        {
                            "@starlette-admin": PackageLoader(
                                "starlette_admin", "templates"
                            ),
                        }
                    ),
                ]
            ),
            extensions=["jinja2.ext.i18n"],
            autoescape=True,
        )
        templates = Jinja2Templates(env=env)

        # globals
        templates.env.globals["views"] = self._views
        templates.env.globals["app_title"] = self.title
        templates.env.globals["is_auth_enabled"] = self.auth_provider is not None
        templates.env.globals["__name__"] = self.route_name
        templates.env.globals["logo_url"] = self.logo_url
        templates.env.globals["login_logo_url"] = self.login_logo_url
        templates.env.globals["favicon_url"] = self.favicon_url
        templates.env.globals["custom_render_js"] = lambda r: self.custom_render_js(r)
        templates.env.globals["get_locale"] = get_locale
        templates.env.globals["get_locale_display_name"] = get_locale_display_name
        templates.env.globals["i18n_config"] = self.i18n_config or I18nConfig()
        templates.env.globals["get_timezone"] = get_timezone
        templates.env.globals["get_timezone_display_name"] = get_timezone_display_name
        templates.env.globals["timezone_config"] = self.timezone_config
        # filters
        templates.env.filters["is_custom_view"] = lambda r: isinstance(r, CustomView)
        templates.env.filters["is_link"] = lambda res: isinstance(res, Link)
        templates.env.filters["is_model"] = lambda res: isinstance(res, BaseModelView)
        templates.env.filters["is_dropdown"] = lambda res: isinstance(res, DropDown)
        templates.env.filters["get_admin_user"] = (
            self.auth_provider.get_admin_user if self.auth_provider else None
        )
        templates.env.filters["get_admin_config"] = (
            self.auth_provider.get_admin_config if self.auth_provider else None
        )
        templates.env.filters["tojson"] = lambda data: json.dumps(data, default=str)
        templates.env.filters["file_icon"] = get_file_icon
        templates.env.filters["to_model"] = (
            lambda identity: self._find_model_from_identity(identity)
        )
        templates.env.filters["is_iter"] = lambda v: isinstance(v, (list, tuple))
        templates.env.filters["is_str"] = lambda v: isinstance(v, str)
        templates.env.filters["is_dict"] = lambda v: isinstance(v, dict)
        templates.env.filters["ra"] = lambda a: RequestAction(a)
        # install i18n
        templates.env.install_gettext_callables(gettext, ngettext, True)  # type: ignore
        self.templates = templates

    def setup_view(self, view: BaseView) -> None:
        if isinstance(view, DropDown):
            for sub_view in view.views:
                self.setup_view(sub_view)
        elif isinstance(view, CustomView):
            self.routes.insert(
                0,
                Route(
                    view.path,
                    endpoint=self._render_custom_view(view),
                    methods=view.methods,
                    name=view.name,
                ),
            )
        elif isinstance(view, BaseModelView):
            view._find_foreign_model = self._find_model_from_identity
            self._models.append(view)

    def _find_model_from_identity(self, identity: Optional[str]) -> BaseModelView:
        if identity is not None:
            for model in self._models:
                if model.identity == identity:
                    return model
        raise HTTPException(
            HTTP_404_NOT_FOUND,
            _("Model with identity %(identity)s not found") % {"identity": identity},
        )

    def _render_custom_view(
        self, custom_view: CustomView
    ) -> Callable[[Request], Awaitable[Response]]:
        async def wrapper(request: Request) -> Response:
            if not custom_view.is_accessible(request):
                raise HTTPException(HTTP_403_FORBIDDEN)
            return await custom_view.render(request, self.templates)

        return wrapper

    async def _render_api(self, request: Request) -> Response:
        identity = request.path_params.get("identity")
        model = self._find_model_from_identity(identity)
        if not model.is_accessible(request):
            return JSONResponse(None, status_code=HTTP_403_FORBIDDEN)
        skip = int(request.query_params.get("skip") or "0")
        limit = int(request.query_params.get("limit") or "100")
        order_by = request.query_params.getlist("order_by")
        where = request.query_params.get("where")
        pks = request.query_params.getlist("pks")
        select2 = "select2" in request.query_params
        request.state.action = RequestAction.API if select2 else RequestAction.LIST
        if len(pks) > 0:
            items = await model.find_by_pks(request, pks)
            total = len(items)
        else:
            if where is not None:
                try:
                    where = json.loads(where)
                except JSONDecodeError:
                    where = str(where)
            items = await model.find_all(
                request=request,
                skip=skip,
                limit=limit,
                where=where,
                order_by=order_by,
            )
            total = await model.count(request=request, where=where)
        serialized_items = [
            (
                await model.serialize(
                    item,
                    request,
                    RequestAction.API if select2 else RequestAction.LIST,
                    include_relationships=not select2,
                    include_select2=select2,
                )
            )
            for item in items
        ]

        if not select2:
            # Add row actions for datatables
            row_actions = await model.get_all_row_actions(request)
            assert model.pk_attr
            for serialized_item in serialized_items:
                serialized_item["_meta"]["rowActions"] = self.templates.get_template(
                    "row-actions.html"
                ).render(
                    _actions=row_actions,
                    display_type=model.row_actions_display_type,
                    pk=serialized_item[model.pk_attr],
                    request=request,
                    model=model,
                )

        return JSONResponse(
            {
                "items": serialized_items,
                "total": total,
            }
        )

    async def handle_action(self, request: Request) -> Response:
        request.state.action = RequestAction.ACTION
        try:
            identity = request.path_params.get("identity")
            pks = request.query_params.getlist("pks")
            name = not_none(request.query_params.get("name"))
            model = self._find_model_from_identity(identity)
            if not model.is_accessible(request):
                raise ActionFailed("Forbidden")
            handler_return = await model.handle_action(request, pks, name)
            if isinstance(handler_return, Response):
                return handler_return
            return JSONResponse({"msg": handler_return})
        except ActionFailed as exc:
            return JSONResponse({"msg": exc.msg}, status_code=HTTP_400_BAD_REQUEST)

    async def handle_row_action(self, request: Request) -> Response:
        request.state.action = RequestAction.ROW_ACTION
        try:
            identity = request.path_params.get("identity")
            pk = request.query_params.get("pk")
            name = not_none(request.query_params.get("name"))
            model = self._find_model_from_identity(identity)
            if not model.is_accessible(request):
                raise ActionFailed("Forbidden")
            handler_return = await model.handle_row_action(request, pk, name)
            if isinstance(handler_return, Response):
                return handler_return
            return JSONResponse({"msg": handler_return})
        except ActionFailed as exc:
            return JSONResponse({"msg": exc.msg}, status_code=HTTP_400_BAD_REQUEST)

    async def _render_list(self, request: Request) -> Response:
        request.state.action = RequestAction.LIST
        identity = request.path_params.get("identity")
        model = self._find_model_from_identity(identity)
        if not model.is_accessible(request):
            raise HTTPException(HTTP_403_FORBIDDEN)
        return self.templates.TemplateResponse(
            request=request,
            name=model.list_template,
            context={
                "model": model,
                "title": model.title(request),
                "_actions": await model.get_all_actions(request),
                "__js_model__": await model._configs(request),
            },
        )

    async def _render_detail(self, request: Request) -> Response:
        request.state.action = RequestAction.DETAIL
        identity = request.path_params.get("identity")
        model = self._find_model_from_identity(identity)
        if not model.is_accessible(request) or not model.can_view_details(request):
            raise HTTPException(HTTP_403_FORBIDDEN)
        pk = request.path_params.get("pk")
        obj = await model.find_by_pk(request, pk)
        if obj is None:
            raise HTTPException(HTTP_404_NOT_FOUND)
        return self.templates.TemplateResponse(
            request=request,
            name=model.detail_template,
            context={
                "title": model.title(request),
                "model": model,
                "raw_obj": obj,
                "_actions": await model.get_all_row_actions(request),
                "obj": await model.serialize(obj, request, RequestAction.DETAIL),
            },
        )

    async def _render_create(self, request: Request) -> Response:
        request.state.action = RequestAction.CREATE
        identity = request.path_params.get("identity")
        model = self._find_model_from_identity(identity)
        config = {"title": model.title(request), "model": model}
        if not model.is_accessible(request) or not model.can_create(request):
            raise HTTPException(HTTP_403_FORBIDDEN)
        if request.method == "GET":
            return self.templates.TemplateResponse(
                request=request,
                name=model.create_template,
                context=config,
            )
        form = await request.form()
        dict_obj = await self.form_to_dict(request, form, model, RequestAction.CREATE)
        try:
            obj = await model.create(request, dict_obj)
        except FormValidationError as exc:
            config.update(
                {
                    "errors": exc.errors,
                    "obj": dict_obj,
                }
            )
            return self.templates.TemplateResponse(
                request=request,
                name=model.create_template,
                context=config,
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            )
        pk = await model.get_pk_value(request, obj)
        url = request.url_for(self.route_name + ":list", identity=model.identity)
        if form.get("_continue_editing", None) is not None:
            url = request.url_for(
                self.route_name + ":edit", identity=model.identity, pk=pk
            )
        elif form.get("_add_another", None) is not None:
            url = request.url
        return RedirectResponse(url, status_code=HTTP_303_SEE_OTHER)

    async def _render_edit(self, request: Request) -> Response:
        request.state.action = RequestAction.EDIT
        identity = request.path_params.get("identity")
        model = self._find_model_from_identity(identity)
        if not model.is_accessible(request) or not model.can_edit(request):
            raise HTTPException(HTTP_403_FORBIDDEN)
        pk = request.path_params.get("pk")
        obj = await model.find_by_pk(request, pk)
        if obj is None:
            raise HTTPException(HTTP_404_NOT_FOUND)
        config = {
            "title": model.title(request),
            "model": model,
            "raw_obj": obj,
            "obj": await model.serialize(obj, request, RequestAction.EDIT),
        }
        if request.method == "GET":
            return self.templates.TemplateResponse(
                request=request,
                name=model.edit_template,
                context=config,
            )
        form = await request.form()
        dict_obj = await self.form_to_dict(request, form, model, RequestAction.EDIT)
        try:
            obj = await model.edit(request, pk, dict_obj)
        except FormValidationError as exc:
            config.update(
                {
                    "errors": exc.errors,
                    "obj": dict_obj,
                }
            )
            return self.templates.TemplateResponse(
                request=request,
                name=model.edit_template,
                context=config,
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            )
        pk = await model.get_pk_value(request, obj)
        url = request.url_for(self.route_name + ":list", identity=model.identity)
        if form.get("_continue_editing", None) is not None:
            url = request.url_for(
                self.route_name + ":edit", identity=model.identity, pk=pk
            )
        elif form.get("_add_another", None) is not None:
            url = request.url_for(self.route_name + ":create", identity=model.identity)
        return RedirectResponse(url, status_code=HTTP_303_SEE_OTHER)

    async def _render_error(
        self,
        request: Request,
        exc: Exception = HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR),
    ) -> Response:
        assert isinstance(exc, HTTPException)
        return self.templates.TemplateResponse(
            request=request,
            name="error.html",
            context={"exc": exc},
            status_code=exc.status_code,
        )

    async def form_to_dict(
        self,
        request: Request,
        form_data: FormData,
        model: BaseModelView,
        action: RequestAction,
    ) -> Dict[str, Any]:
        data = {}
        for field in model.get_fields_list(request, action):
            data[field.name] = await field.parse_form_data(request, form_data, action)
        return data

    def mount_to(
        self,
        app: Starlette,
        redirect_slashes: bool = True,
    ) -> None:
        admin_app = Starlette(
            routes=self.routes,
            middleware=self.middlewares,
            debug=self.debug,
            exception_handlers={HTTPException: self._render_error},
        )
        admin_app.state.ROUTE_NAME = self.route_name
        app.mount(
            self.base_url,
            app=admin_app,
            name=self.route_name,
        )
        admin_app.router.redirect_slashes = redirect_slashes

Source code in starlette_admin/base.py

class BaseAdmin:
    """Base class for implementing Admin interface."""

    def __init__(
        self,
        title: str = _("Admin"),
        base_url: str = "/admin",
        route_name: str = "admin",
        logo_url: Optional[str] = None,
        login_logo_url: Optional[str] = None,
        templates_dir: str = "templates",
        statics_dir: Optional[str] = None,
        index_view: Optional[CustomView] = None,
        auth_provider: Optional[BaseAuthProvider] = None,
        middlewares: Optional[Sequence[Middleware]] = None,
        debug: bool = False,
        i18n_config: Optional[I18nConfig] = None,
        timezone_config: Optional[TimezoneConfig] = None,
        favicon_url: Optional[str] = None,
    ):
        """
        Parameters:
            title: Admin title.
            base_url: Base URL for Admin interface.
            route_name: Mounted Admin name
            logo_url: URL of logo to be displayed instead of title.
            login_logo_url: If set, it will be used for login interface instead of logo_url.
            templates_dir: Templates dir for customisation
            statics_dir: Statics dir for customisation
            index_view: CustomView to use for index page.
            auth_provider: Authentication Provider
            middlewares: Starlette middlewares
            i18n_config: i18n configuration
            timezone_config: timezone configuration
            favicon_url: URL of favicon.
        """
        self.title = title
        self.base_url = base_url
        self.route_name = route_name
        self.logo_url = logo_url
        self.login_logo_url = login_logo_url
        self.favicon_url = favicon_url
        self.templates_dir = templates_dir
        self.statics_dir = statics_dir
        self.auth_provider = auth_provider
        self.middlewares = list(middlewares) if middlewares is not None else []
        self.index_view = (
            index_view
            if (index_view is not None)
            else CustomView("", add_to_menu=False)
        )
        self._views: List[BaseView] = []
        self._models: List[BaseModelView] = []
        self.routes: List[Union[Route, Mount]] = []
        self.debug = debug
        self.i18n_config = i18n_config
        self.timezone_config = timezone_config
        self._setup_templates()
        self.init_locale()
        self.init_auth()
        self.init_routes()

    def add_view(self, view: Union[Type[BaseView], BaseView]) -> None:
        """
        Add View to the Admin interface.
        """
        view_instance = view if isinstance(view, BaseView) else view()
        self._views.append(view_instance)
        self.setup_view(view_instance)

    def custom_render_js(self, request: Request) -> Optional[str]:
        """
        Override this function to provide a link to custom js to override the
        global 'render' object in javascript which is use to render fields in
        list page.

        Args:
            request: Starlette Request
        """
        return None

    def init_locale(self) -> None:
        if self.i18n_config is not None:
            try:
                import babel  # noqa
            except ImportError as err:
                raise ImportError(
                    "'babel' package is required to use i18n features."
                    "Install it with 'pip install starlette-admin[i18n]'"
                ) from err
            self.middlewares.insert(
                0, Middleware(LocaleMiddleware, i18n_config=self.i18n_config)
            )

        if self.timezone_config is not None:
            self.middlewares.insert(
                0, Middleware(TimezoneMiddleware, timezone_config=self.timezone_config)
            )

    def init_auth(self) -> None:
        if self.auth_provider is not None:
            self.auth_provider.setup_admin(self)

    def init_routes(self) -> None:
        statics = StaticFiles(directory=self.statics_dir, packages=["starlette_admin"])
        self.routes.extend(
            [
                Mount("/statics", app=statics, name="statics"),
                Route(
                    self.index_view.path,
                    self._render_custom_view(self.index_view),
                    methods=self.index_view.methods,
                    name="index",
                ),
                Route(
                    "/api/{identity}",
                    self._render_api,
                    methods=["GET"],
                    name="api",
                ),
                Route(
                    "/api/{identity}/action",
                    self.handle_action,
                    methods=["GET", "POST"],
                    name="action",
                ),
                Route(
                    "/api/{identity}/row-action",
                    self.handle_row_action,
                    methods=["GET", "POST"],
                    name="row-action",
                ),
                Route(
                    "/{identity}/list",
                    self._render_list,
                    methods=["GET"],
                    name="list",
                ),
                Route(
                    "/{identity}/detail/{pk}",
                    self._render_detail,
                    methods=["GET"],
                    name="detail",
                ),
                Route(
                    "/{identity}/create",
                    self._render_create,
                    methods=["GET", "POST"],
                    name="create",
                ),
                Route(
                    "/{identity}/edit/{pk}",
                    self._render_edit,
                    methods=["GET", "POST"],
                    name="edit",
                ),
            ]
        )
        if self.index_view.add_to_menu:
            self._views.append(self.index_view)

    def _setup_templates(self) -> None:
        env = Environment(
            loader=ChoiceLoader(
                [
                    FileSystemLoader(self.templates_dir),
                    PackageLoader("starlette_admin", "templates"),
                    PrefixLoader(
                        {
                            "@starlette-admin": PackageLoader(
                                "starlette_admin", "templates"
                            ),
                        }
                    ),
                ]
            ),
            extensions=["jinja2.ext.i18n"],
            autoescape=True,
        )
        templates = Jinja2Templates(env=env)

        # globals
        templates.env.globals["views"] = self._views
        templates.env.globals["app_title"] = self.title
        templates.env.globals["is_auth_enabled"] = self.auth_provider is not None
        templates.env.globals["__name__"] = self.route_name
        templates.env.globals["logo_url"] = self.logo_url
        templates.env.globals["login_logo_url"] = self.login_logo_url
        templates.env.globals["favicon_url"] = self.favicon_url
        templates.env.globals["custom_render_js"] = lambda r: self.custom_render_js(r)
        templates.env.globals["get_locale"] = get_locale
        templates.env.globals["get_locale_display_name"] = get_locale_display_name
        templates.env.globals["i18n_config"] = self.i18n_config or I18nConfig()
        templates.env.globals["get_timezone"] = get_timezone
        templates.env.globals["get_timezone_display_name"] = get_timezone_display_name
        templates.env.globals["timezone_config"] = self.timezone_config
        # filters
        templates.env.filters["is_custom_view"] = lambda r: isinstance(r, CustomView)
        templates.env.filters["is_link"] = lambda res: isinstance(res, Link)
        templates.env.filters["is_model"] = lambda res: isinstance(res, BaseModelView)
        templates.env.filters["is_dropdown"] = lambda res: isinstance(res, DropDown)
        templates.env.filters["get_admin_user"] = (
            self.auth_provider.get_admin_user if self.auth_provider else None
        )
        templates.env.filters["get_admin_config"] = (
            self.auth_provider.get_admin_config if self.auth_provider else None
        )
        templates.env.filters["tojson"] = lambda data: json.dumps(data, default=str)
        templates.env.filters["file_icon"] = get_file_icon
        templates.env.filters["to_model"] = (
            lambda identity: self._find_model_from_identity(identity)
        )
        templates.env.filters["is_iter"] = lambda v: isinstance(v, (list, tuple))
        templates.env.filters["is_str"] = lambda v: isinstance(v, str)
        templates.env.filters["is_dict"] = lambda v: isinstance(v, dict)
        templates.env.filters["ra"] = lambda a: RequestAction(a)
        # install i18n
        templates.env.install_gettext_callables(gettext, ngettext, True)  # type: ignore
        self.templates = templates

    def setup_view(self, view: BaseView) -> None:
        if isinstance(view, DropDown):
            for sub_view in view.views:
                self.setup_view(sub_view)
        elif isinstance(view, CustomView):
            self.routes.insert(
                0,
                Route(
                    view.path,
                    endpoint=self._render_custom_view(view),
                    methods=view.methods,
                    name=view.name,
                ),
            )
        elif isinstance(view, BaseModelView):
            view._find_foreign_model = self._find_model_from_identity
            self._models.append(view)

    def _find_model_from_identity(self, identity: Optional[str]) -> BaseModelView:
        if identity is not None:
            for model in self._models:
                if model.identity == identity:
                    return model
        raise HTTPException(
            HTTP_404_NOT_FOUND,
            _("Model with identity %(identity)s not found") % {"identity": identity},
        )

    def _render_custom_view(
        self, custom_view: CustomView
    ) -> Callable[[Request], Awaitable[Response]]:
        async def wrapper(request: Request) -> Response:
            if not custom_view.is_accessible(request):
                raise HTTPException(HTTP_403_FORBIDDEN)
            return await custom_view.render(request, self.templates)

        return wrapper

    async def _render_api(self, request: Request) -> Response:
        identity = request.path_params.get("identity")
        model = self._find_model_from_identity(identity)
        if not model.is_accessible(request):
            return JSONResponse(None, status_code=HTTP_403_FORBIDDEN)
        skip = int(request.query_params.get("skip") or "0")
        limit = int(request.query_params.get("limit") or "100")
        order_by = request.query_params.getlist("order_by")
        where = request.query_params.get("where")
        pks = request.query_params.getlist("pks")
        select2 = "select2" in request.query_params
        request.state.action = RequestAction.API if select2 else RequestAction.LIST
        if len(pks) > 0:
            items = await model.find_by_pks(request, pks)
            total = len(items)
        else:
            if where is not None:
                try:
                    where = json.loads(where)
                except JSONDecodeError:
                    where = str(where)
            items = await model.find_all(
                request=request,
                skip=skip,
                limit=limit,
                where=where,
                order_by=order_by,
            )
            total = await model.count(request=request, where=where)
        serialized_items = [
            (
                await model.serialize(
                    item,
                    request,
                    RequestAction.API if select2 else RequestAction.LIST,
                    include_relationships=not select2,
                    include_select2=select2,
                )
            )
            for item in items
        ]

        if not select2:
            # Add row actions for datatables
            row_actions = await model.get_all_row_actions(request)
            assert model.pk_attr
            for serialized_item in serialized_items:
                serialized_item["_meta"]["rowActions"] = self.templates.get_template(
                    "row-actions.html"
                ).render(
                    _actions=row_actions,
                    display_type=model.row_actions_display_type,
                    pk=serialized_item[model.pk_attr],
                    request=request,
                    model=model,
                )

        return JSONResponse(
            {
                "items": serialized_items,
                "total": total,
            }
        )

    async def handle_action(self, request: Request) -> Response:
        request.state.action = RequestAction.ACTION
        try:
            identity = request.path_params.get("identity")
            pks = request.query_params.getlist("pks")
            name = not_none(request.query_params.get("name"))
            model = self._find_model_from_identity(identity)
            if not model.is_accessible(request):
                raise ActionFailed("Forbidden")
            handler_return = await model.handle_action(request, pks, name)
            if isinstance(handler_return, Response):
                return handler_return
            return JSONResponse({"msg": handler_return})
        except ActionFailed as exc:
            return JSONResponse({"msg": exc.msg}, status_code=HTTP_400_BAD_REQUEST)

    async def handle_row_action(self, request: Request) -> Response:
        request.state.action = RequestAction.ROW_ACTION
        try:
            identity = request.path_params.get("identity")
            pk = request.query_params.get("pk")
            name = not_none(request.query_params.get("name"))
            model = self._find_model_from_identity(identity)
            if not model.is_accessible(request):
                raise ActionFailed("Forbidden")
            handler_return = await model.handle_row_action(request, pk, name)
            if isinstance(handler_return, Response):
                return handler_return
            return JSONResponse({"msg": handler_return})
        except ActionFailed as exc:
            return JSONResponse({"msg": exc.msg}, status_code=HTTP_400_BAD_REQUEST)

    async def _render_list(self, request: Request) -> Response:
        request.state.action = RequestAction.LIST
        identity = request.path_params.get("identity")
        model = self._find_model_from_identity(identity)
        if not model.is_accessible(request):
            raise HTTPException(HTTP_403_FORBIDDEN)
        return self.templates.TemplateResponse(
            request=request,
            name=model.list_template,
            context={
                "model": model,
                "title": model.title(request),
                "_actions": await model.get_all_actions(request),
                "__js_model__": await model._configs(request),
            },
        )

    async def _render_detail(self, request: Request) -> Response:
        request.state.action = RequestAction.DETAIL
        identity = request.path_params.get("identity")
        model = self._find_model_from_identity(identity)
        if not model.is_accessible(request) or not model.can_view_details(request):
            raise HTTPException(HTTP_403_FORBIDDEN)
        pk = request.path_params.get("pk")
        obj = await model.find_by_pk(request, pk)
        if obj is None:
            raise HTTPException(HTTP_404_NOT_FOUND)
        return self.templates.TemplateResponse(
            request=request,
            name=model.detail_template,
            context={
                "title": model.title(request),
                "model": model,
                "raw_obj": obj,
                "_actions": await model.get_all_row_actions(request),
                "obj": await model.serialize(obj, request, RequestAction.DETAIL),
            },
        )

    async def _render_create(self, request: Request) -> Response:
        request.state.action = RequestAction.CREATE
        identity = request.path_params.get("identity")
        model = self._find_model_from_identity(identity)
        config = {"title": model.title(request), "model": model}
        if not model.is_accessible(request) or not model.can_create(request):
            raise HTTPException(HTTP_403_FORBIDDEN)
        if request.method == "GET":
            return self.templates.TemplateResponse(
                request=request,
                name=model.create_template,
                context=config,
            )
        form = await request.form()
        dict_obj = await self.form_to_dict(request, form, model, RequestAction.CREATE)
        try:
            obj = await model.create(request, dict_obj)
        except FormValidationError as exc:
            config.update(
                {
                    "errors": exc.errors,
                    "obj": dict_obj,
                }
            )
            return self.templates.TemplateResponse(
                request=request,
                name=model.create_template,
                context=config,
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            )
        pk = await model.get_pk_value(request, obj)
        url = request.url_for(self.route_name + ":list", identity=model.identity)
        if form.get("_continue_editing", None) is not None:
            url = request.url_for(
                self.route_name + ":edit", identity=model.identity, pk=pk
            )
        elif form.get("_add_another", None) is not None:
            url = request.url
        return RedirectResponse(url, status_code=HTTP_303_SEE_OTHER)

    async def _render_edit(self, request: Request) -> Response:
        request.state.action = RequestAction.EDIT
        identity = request.path_params.get("identity")
        model = self._find_model_from_identity(identity)
        if not model.is_accessible(request) or not model.can_edit(request):
            raise HTTPException(HTTP_403_FORBIDDEN)
        pk = request.path_params.get("pk")
        obj = await model.find_by_pk(request, pk)
        if obj is None:
            raise HTTPException(HTTP_404_NOT_FOUND)
        config = {
            "title": model.title(request),
            "model": model,
            "raw_obj": obj,
            "obj": await model.serialize(obj, request, RequestAction.EDIT),
        }
        if request.method == "GET":
            return self.templates.TemplateResponse(
                request=request,
                name=model.edit_template,
                context=config,
            )
        form = await request.form()
        dict_obj = await self.form_to_dict(request, form, model, RequestAction.EDIT)
        try:
            obj = await model.edit(request, pk, dict_obj)
        except FormValidationError as exc:
            config.update(
                {
                    "errors": exc.errors,
                    "obj": dict_obj,
                }
            )
            return self.templates.TemplateResponse(
                request=request,
                name=model.edit_template,
                context=config,
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            )
        pk = await model.get_pk_value(request, obj)
        url = request.url_for(self.route_name + ":list", identity=model.identity)
        if form.get("_continue_editing", None) is not None:
            url = request.url_for(
                self.route_name + ":edit", identity=model.identity, pk=pk
            )
        elif form.get("_add_another", None) is not None:
            url = request.url_for(self.route_name + ":create", identity=model.identity)
        return RedirectResponse(url, status_code=HTTP_303_SEE_OTHER)

    async def _render_error(
        self,
        request: Request,
        exc: Exception = HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR),
    ) -> Response:
        assert isinstance(exc, HTTPException)
        return self.templates.TemplateResponse(
            request=request,
            name="error.html",
            context={"exc": exc},
            status_code=exc.status_code,
        )

    async def form_to_dict(
        self,
        request: Request,
        form_data: FormData,
        model: BaseModelView,
        action: RequestAction,
    ) -> Dict[str, Any]:
        data = {}
        for field in model.get_fields_list(request, action):
            data[field.name] = await field.parse_form_data(request, form_data, action)
        return data

    def mount_to(
        self,
        app: Starlette,
        redirect_slashes: bool = True,
    ) -> None:
        admin_app = Starlette(
            routes=self.routes,
            middleware=self.middlewares,
            debug=self.debug,
            exception_handlers={HTTPException: self._render_error},
        )
        admin_app.state.ROUTE_NAME = self.route_name
        app.mount(
            self.base_url,
            app=admin_app,
            name=self.route_name,
        )
        admin_app.router.redirect_slashes = redirect_slashes

__init__(title=_('Admin'), base_url='/admin', route_name='admin', logo_url=None, login_logo_url=None, templates_dir='templates', statics_dir=None, index_view=None, auth_provider=None, middlewares=None, debug=False, i18n_config=None, timezone_config=None, favicon_url=None)

Parameters:
Name 	Type 	Description 	Default
title 	str 	

Admin title.
	lazy_gettext('Admin')
base_url 	str 	

Base URL for Admin interface.
	'/admin'
route_name 	str 	

Mounted Admin name
	'admin'
logo_url 	Optional[str] 	

URL of logo to be displayed instead of title.
	None
login_logo_url 	Optional[str] 	

If set, it will be used for login interface instead of logo_url.
	None
templates_dir 	str 	

Templates dir for customisation
	'templates'
statics_dir 	Optional[str] 	

Statics dir for customisation
	None
index_view 	Optional[CustomView] 	

CustomView to use for index page.
	None
auth_provider 	Optional[BaseAuthProvider] 	

Authentication Provider
	None
middlewares 	Optional[Sequence[Middleware]] 	

Starlette middlewares
	None
i18n_config 	Optional[I18nConfig] 	

i18n configuration
	None
timezone_config 	Optional[TimezoneConfig] 	

timezone configuration
	None
favicon_url 	Optional[str] 	

URL of favicon.
	None
Source code in starlette_admin/base.py

def __init__(
    self,
    title: str = _("Admin"),
    base_url: str = "/admin",
    route_name: str = "admin",
    logo_url: Optional[str] = None,
    login_logo_url: Optional[str] = None,
    templates_dir: str = "templates",
    statics_dir: Optional[str] = None,
    index_view: Optional[CustomView] = None,
    auth_provider: Optional[BaseAuthProvider] = None,
    middlewares: Optional[Sequence[Middleware]] = None,
    debug: bool = False,
    i18n_config: Optional[I18nConfig] = None,
    timezone_config: Optional[TimezoneConfig] = None,
    favicon_url: Optional[str] = None,
):
    """
    Parameters:
        title: Admin title.
        base_url: Base URL for Admin interface.
        route_name: Mounted Admin name
        logo_url: URL of logo to be displayed instead of title.
        login_logo_url: If set, it will be used for login interface instead of logo_url.
        templates_dir: Templates dir for customisation
        statics_dir: Statics dir for customisation
        index_view: CustomView to use for index page.
        auth_provider: Authentication Provider
        middlewares: Starlette middlewares
        i18n_config: i18n configuration
        timezone_config: timezone configuration
        favicon_url: URL of favicon.
    """
    self.title = title
    self.base_url = base_url
    self.route_name = route_name
    self.logo_url = logo_url
    self.login_logo_url = login_logo_url
    self.favicon_url = favicon_url
    self.templates_dir = templates_dir
    self.statics_dir = statics_dir
    self.auth_provider = auth_provider
    self.middlewares = list(middlewares) if middlewares is not None else []
    self.index_view = (
        index_view
        if (index_view is not None)
        else CustomView("", add_to_menu=False)
    )
    self._views: List[BaseView] = []
    self._models: List[BaseModelView] = []
    self.routes: List[Union[Route, Mount]] = []
    self.debug = debug
    self.i18n_config = i18n_config
    self.timezone_config = timezone_config
    self._setup_templates()
    self.init_locale()
    self.init_auth()
    self.init_routes()

Source code in starlette_admin/base.py

def __init__(
    self,
    title: str = _("Admin"),
    base_url: str = "/admin",
    route_name: str = "admin",
    logo_url: Optional[str] = None,
    login_logo_url: Optional[str] = None,
    templates_dir: str = "templates",
    statics_dir: Optional[str] = None,
    index_view: Optional[CustomView] = None,
    auth_provider: Optional[BaseAuthProvider] = None,
    middlewares: Optional[Sequence[Middleware]] = None,
    debug: bool = False,
    i18n_config: Optional[I18nConfig] = None,
    timezone_config: Optional[TimezoneConfig] = None,
    favicon_url: Optional[str] = None,
):
    """
    Parameters:
        title: Admin title.
        base_url: Base URL for Admin interface.
        route_name: Mounted Admin name
        logo_url: URL of logo to be displayed instead of title.
        login_logo_url: If set, it will be used for login interface instead of logo_url.
        templates_dir: Templates dir for customisation
        statics_dir: Statics dir for customisation
        index_view: CustomView to use for index page.
        auth_provider: Authentication Provider
        middlewares: Starlette middlewares
        i18n_config: i18n configuration
        timezone_config: timezone configuration
        favicon_url: URL of favicon.
    """
    self.title = title
    self.base_url = base_url
    self.route_name = route_name
    self.logo_url = logo_url
    self.login_logo_url = login_logo_url
    self.favicon_url = favicon_url
    self.templates_dir = templates_dir
    self.statics_dir = statics_dir
    self.auth_provider = auth_provider
    self.middlewares = list(middlewares) if middlewares is not None else []
    self.index_view = (
        index_view
        if (index_view is not None)
        else CustomView("", add_to_menu=False)
    )
    self._views: List[BaseView] = []
    self._models: List[BaseModelView] = []
    self.routes: List[Union[Route, Mount]] = []
    self.debug = debug
    self.i18n_config = i18n_config
    self.timezone_config = timezone_config
    self._setup_templates()
    self.init_locale()
    self.init_auth()
    self.init_routes()

add_view(view)

Add View to the Admin interface.
Source code in starlette_admin/base.py

def add_view(self, view: Union[Type[BaseView], BaseView]) -> None:
    """
    Add View to the Admin interface.
    """
    view_instance = view if isinstance(view, BaseView) else view()
    self._views.append(view_instance)
    self.setup_view(view_instance)

Source code in starlette_admin/base.py

def add_view(self, view: Union[Type[BaseView], BaseView]) -> None:
    """
    Add View to the Admin interface.
    """
    view_instance = view if isinstance(view, BaseView) else view()
    self._views.append(view_instance)
    self.setup_view(view_instance)

custom_render_js(request)

Override this function to provide a link to custom js to override the global render object in javascript which is use to render fields in list page.

Parameters:
Name 	Type 	Description 	Default
request 	Request 	

Starlette Request
	required
Source code in starlette_admin/base.py

def custom_render_js(self, request: Request) -> Optional[str]:
    """
    Override this function to provide a link to custom js to override the
    global 'render' object in javascript which is use to render fields in
    list page.

    Args:
        request: Starlette Request
    """
    return None

def custom_render_js(self, request: Request) -> Optional[str]:
    """
    Override this function to provide a link to custom js to override the
    global 'render' object in javascript which is use to render fields in
    list page.

    Args:
        request: Starlette Request
    """
    return None

Auth
starlette_admin.auth
BaseAuthProvider

Bases: ABC

Base class for implementing the Authentication into your admin interface

Parameters:
Name 	Type 	Description 	Default
login_path 	str 	

The path for the login page.
	'/login'
logout_path 	str 	

The path for the logout page.
	'/logout'
allow_paths 	Optional[Sequence[str]] 	

A list of paths that are allowed without authentication.
	None
allow_routes 	Optional[Sequence[str]] 	

A list of route names that are allowed without authentication.
	None
Warning

    The usage of allow_paths is deprecated. It is recommended to use allow_routes that specifies the route names instead.

Source code in starlette_admin/auth.py

class BaseAuthProvider(ABC):
    """
    Base class for implementing the Authentication into your admin interface

    Args:
        login_path: The path for the login page.
        logout_path: The path for the logout page.
        allow_paths: A list of paths that are allowed without authentication.
        allow_routes: A list of route names that are allowed without authentication.

    Warning:
        - The usage of 'allow_paths' is deprecated. It is recommended to use 'allow_routes'
          that specifies the route names instead.

    """

    def __init__(
        self,
        login_path: str = "/login",
        logout_path: str = "/logout",
        allow_paths: Optional[Sequence[str]] = None,
        allow_routes: Optional[Sequence[str]] = None,
    ) -> None:
        self.login_path = login_path
        self.logout_path = logout_path
        self.allow_paths = allow_paths
        self.allow_routes = allow_routes

        if allow_paths:
            warnings.warn(
                "'allow_paths' is deprecated. Use 'allow_routes' instead.",
                DeprecationWarning,
                stacklevel=2,
            )

    @abstractmethod
    def setup_admin(self, admin: "BaseAdmin") -> None:
        """
        This method is an abstract method that must be implemented in subclasses.
        It allows custom configuration and setup of the admin interface
        related to authentication and authorization.
        """
        raise NotImplementedError()

    def get_middleware(self, admin: "BaseAdmin") -> Middleware:
        """
        This method returns the authentication middleware required for the admin interface
        to enable authentication
        """
        return Middleware(AuthMiddleware, provider=self)

    async def is_authenticated(self, request: Request) -> bool:
        """
        This method will be called to validate each incoming request.
        You can also save the connected user information into the
        request state and use it later to restrict access to some part
        of your admin interface

        Returns:
            True: to accept the request
            False: to redirect to login page

        Examples:
            python
            async def is_authenticated(self, request: Request) -> bool:
                if request.session.get("username", None) in users:
                    # Save user object in state
                    request.state.user = my_users_db.get(request.session["username"])
                    return True
                return False
            
        """
        return False

    def get_admin_config(self, request: Request) -> Optional[AdminConfig]:
        """
        Override this method to display custom 'logo_url' and/or 'app_title'

        Returns:
            AdminConfig: The admin interface config

        Examples:
            python
            def get_admin_config(self, request: Request) -> AdminConfig:
                user = request.state.user  # Retrieve current user (previously saved in the request state)
                return AdminConfig(
                    logo_url=request.url_for("static", path=user["company_logo_url"]),
                )
            

            python
            def get_admin_config(self, request: Request) -> AdminConfig:
                user = request.state.user  # Retrieve current user (previously saved in the request state)
                return AdminConfig(
                    app_title="Hello, " + user["name"] + "!",
                )
            
        """
        return None  # pragma: no cover

    def get_admin_user(self, request: Request) -> Optional[AdminUser]:
        """
        Override this method to display connected user 'name' and/or 'profile'

        Returns:
            AdminUser: The connected user info

        Examples:
            python
            def get_admin_user(self, request: Request) -> AdminUser:
                user = request.state.user  # Retrieve current user (previously saved in the request state)
                return AdminUser(username=user["name"], photo_url=user["photo_url"])
            
        """
        return None  # pragma: no cover

Source code in starlette_admin/auth.py

class BaseAuthProvider(ABC):
    """
    Base class for implementing the Authentication into your admin interface

    Args:
        login_path: The path for the login page.
        logout_path: The path for the logout page.
        allow_paths: A list of paths that are allowed without authentication.
        allow_routes: A list of route names that are allowed without authentication.

    Warning:
        - The usage of 'allow_paths' is deprecated. It is recommended to use 'allow_routes'
          that specifies the route names instead.

    """

    def __init__(
        self,
        login_path: str = "/login",
        logout_path: str = "/logout",
        allow_paths: Optional[Sequence[str]] = None,
        allow_routes: Optional[Sequence[str]] = None,
    ) -> None:
        self.login_path = login_path
        self.logout_path = logout_path
        self.allow_paths = allow_paths
        self.allow_routes = allow_routes

        if allow_paths:
            warnings.warn(
                "'allow_paths' is deprecated. Use 'allow_routes' instead.",
                DeprecationWarning,
                stacklevel=2,
            )

    @abstractmethod
    def setup_admin(self, admin: "BaseAdmin") -> None:
        """
        This method is an abstract method that must be implemented in subclasses.
        It allows custom configuration and setup of the admin interface
        related to authentication and authorization.
        """
        raise NotImplementedError()

    def get_middleware(self, admin: "BaseAdmin") -> Middleware:
        """
        This method returns the authentication middleware required for the admin interface
        to enable authentication
        """
        return Middleware(AuthMiddleware, provider=self)

    async def is_authenticated(self, request: Request) -> bool:
        """
        This method will be called to validate each incoming request.
        You can also save the connected user information into the
        request state and use it later to restrict access to some part
        of your admin interface

        Returns:
            True: to accept the request
            False: to redirect to login page

        Examples:
            python
            async def is_authenticated(self, request: Request) -> bool:
                if request.session.get("username", None) in users:
                    # Save user object in state
                    request.state.user = my_users_db.get(request.session["username"])
                    return True
                return False
            
        """
        return False

    def get_admin_config(self, request: Request) -> Optional[AdminConfig]:
        """
        Override this method to display custom 'logo_url' and/or 'app_title'

        Returns:
            AdminConfig: The admin interface config

        Examples:
            python
            def get_admin_config(self, request: Request) -> AdminConfig:
                user = request.state.user  # Retrieve current user (previously saved in the request state)
                return AdminConfig(
                    logo_url=request.url_for("static", path=user["company_logo_url"]),
                )
            

            python
            def get_admin_config(self, request: Request) -> AdminConfig:
                user = request.state.user  # Retrieve current user (previously saved in the request state)
                return AdminConfig(
                    app_title="Hello, " + user["name"] + "!",
                )
            
        """
        return None  # pragma: no cover

    def get_admin_user(self, request: Request) -> Optional[AdminUser]:
        """
        Override this method to display connected user 'name' and/or 'profile'

        Returns:
            AdminUser: The connected user info

        Examples:
            python
            def get_admin_user(self, request: Request) -> AdminUser:
                user = request.state.user  # Retrieve current user (previously saved in the request state)
                return AdminUser(username=user["name"], photo_url=user["photo_url"])
            
        """
        return None  # pragma: no cover

get_admin_config(request)

Override this method to display custom logo_url and/or app_title

Returns:
Name 	Type 	Description
AdminConfig 	Optional[AdminConfig] 	

The admin interface config

Examples:

def get_admin_config(self, request: Request) -> AdminConfig:
    user = request.state.user  # Retrieve current user (previously saved in the request state)
    return AdminConfig(
        logo_url=request.url_for("static", path=user["company_logo_url"]),
    )

def get_admin_config(self, request: Request) -> AdminConfig:
    user = request.state.user  # Retrieve current user (previously saved in the request state)
    return AdminConfig(
        app_title="Hello, " + user["name"] + "!",
    )

Source code in starlette_admin/auth.py

def get_admin_config(self, request: Request) -> Optional[AdminConfig]:
    """
    Override this method to display custom 'logo_url' and/or 'app_title'

    Returns:
        AdminConfig: The admin interface config

    Examples:
        python
        def get_admin_config(self, request: Request) -> AdminConfig:
            user = request.state.user  # Retrieve current user (previously saved in the request state)
            return AdminConfig(
                logo_url=request.url_for("static", path=user["company_logo_url"]),
            )
        

        python
        def get_admin_config(self, request: Request) -> AdminConfig:
            user = request.state.user  # Retrieve current user (previously saved in the request state)
            return AdminConfig(
                app_title="Hello, " + user["name"] + "!",
            )
        
    """
    return None  # pragma: no cover

Source code in starlette_admin/auth.py

def get_admin_config(self, request: Request) -> Optional[AdminConfig]:
    """
    Override this method to display custom 'logo_url' and/or 'app_title'

    Returns:
        AdminConfig: The admin interface config

    Examples:
        python
        def get_admin_config(self, request: Request) -> AdminConfig:
            user = request.state.user  # Retrieve current user (previously saved in the request state)
            return AdminConfig(
                logo_url=request.url_for("static", path=user["company_logo_url"]),
            )
        

        python
        def get_admin_config(self, request: Request) -> AdminConfig:
            user = request.state.user  # Retrieve current user (previously saved in the request state)
            return AdminConfig(
                app_title="Hello, " + user["name"] + "!",
            )
        
    """
    return None  # pragma: no cover

get_admin_user(request)

Override this method to display connected user name and/or profile

Returns:
Name 	Type 	Description
AdminUser 	Optional[AdminUser] 	

The connected user info

Examples:

def get_admin_user(self, request: Request) -> AdminUser:
    user = request.state.user  # Retrieve current user (previously saved in the request state)
    return AdminUser(username=user["name"], photo_url=user["photo_url"])

Source code in starlette_admin/auth.py

def get_admin_user(self, request: Request) -> Optional[AdminUser]:
    """
    Override this method to display connected user 'name' and/or 'profile'

    Returns:
        AdminUser: The connected user info

    Examples:
        python
        def get_admin_user(self, request: Request) -> AdminUser:
            user = request.state.user  # Retrieve current user (previously saved in the request state)
            return AdminUser(username=user["name"], photo_url=user["photo_url"])
        
    """
    return None  # pragma: no cover

Source code in starlette_admin/auth.py

def get_admin_user(self, request: Request) -> Optional[AdminUser]:
    """
    Override this method to display connected user 'name' and/or 'profile'

    Returns:
        AdminUser: The connected user info

    Examples:
        python
        def get_admin_user(self, request: Request) -> AdminUser:
            user = request.state.user  # Retrieve current user (previously saved in the request state)
            return AdminUser(username=user["name"], photo_url=user["photo_url"])
        
    """
    return None  # pragma: no cover

get_middleware(admin)

This method returns the authentication middleware required for the admin interface to enable authentication
Source code in starlette_admin/auth.py

def get_middleware(self, admin: "BaseAdmin") -> Middleware:
    """
    This method returns the authentication middleware required for the admin interface
    to enable authentication
    """
    return Middleware(AuthMiddleware, provider=self)

Source code in starlette_admin/auth.py

def get_middleware(self, admin: "BaseAdmin") -> Middleware:
    """
    This method returns the authentication middleware required for the admin interface
    to enable authentication
    """
    return Middleware(AuthMiddleware, provider=self)

is_authenticated(request) async

This method will be called to validate each incoming request. You can also save the connected user information into the request state and use it later to restrict access to some part of your admin interface

Returns:
Name 	Type 	Description
True 	bool 	

to accept the request
False 	bool 	

to redirect to login page

Examples:

async def is_authenticated(self, request: Request) -> bool:
    if request.session.get("username", None) in users:
        # Save user object in state
        request.state.user = my_users_db.get(request.session["username"])
        return True
    return False

Source code in starlette_admin/auth.py

async def is_authenticated(self, request: Request) -> bool:
    """
    This method will be called to validate each incoming request.
    You can also save the connected user information into the
    request state and use it later to restrict access to some part
    of your admin interface

    Returns:
        True: to accept the request
        False: to redirect to login page

    Examples:
        python
        async def is_authenticated(self, request: Request) -> bool:
            if request.session.get("username", None) in users:
                # Save user object in state
                request.state.user = my_users_db.get(request.session["username"])
                return True
            return False
        
    """
    return False

Source code in starlette_admin/auth.py

async def is_authenticated(self, request: Request) -> bool:
    """
    This method will be called to validate each incoming request.
    You can also save the connected user information into the
    request state and use it later to restrict access to some part
    of your admin interface

    Returns:
        True: to accept the request
        False: to redirect to login page

    Examples:
        python
        async def is_authenticated(self, request: Request) -> bool:
            if request.session.get("username", None) in users:
                # Save user object in state
                request.state.user = my_users_db.get(request.session["username"])
                return True
            return False
        
    """
    return False

setup_admin(admin) abstractmethod

This method is an abstract method that must be implemented in subclasses. It allows custom configuration and setup of the admin interface related to authentication and authorization.
Source code in starlette_admin/auth.py

@abstractmethod
def setup_admin(self, admin: "BaseAdmin") -> None:
    """
    This method is an abstract method that must be implemented in subclasses.
    It allows custom configuration and setup of the admin interface
    related to authentication and authorization.
    """
    raise NotImplementedError()

Source code in starlette_admin/auth.py

@abstractmethod
def setup_admin(self, admin: "BaseAdmin") -> None:
    """
    This method is an abstract method that must be implemented in subclasses.
    It allows custom configuration and setup of the admin interface
    related to authentication and authorization.
    """
    raise NotImplementedError()

AuthProvider

Bases: BaseAuthProvider
Source code in starlette_admin/auth.py

class AuthProvider(BaseAuthProvider):
    async def login(
        self,
        username: str,
        password: str,
        remember_me: bool,
        request: Request,
        response: Response,
    ) -> Response:
        """
        This method will be called to validate user credentials

        Returns:
            response: return the response back

        Raises:
            FormValidationError: when form values is not valid
            LoginFailed: to display general error

        Examples:
            python
            async def login(
                self,
                username: str,
                password: str,
                remember_me: bool,
                request: Request,
                response: Response,
            ) -> Response:
                if len(username) < 3:
                    # Form data validation
                    raise FormValidationError(
                        {"username": "Ensure username has at least 03 characters"}
                    )

                if username in my_users_db and password == "password":
                    # Save username in session
                    request.session.update({"username": username})
                    return response

                raise LoginFailed("Invalid username or password")
            
        """
        raise LoginFailed("Not Implemented")

    async def logout(self, request: Request, response: Response) -> Response:
        """
        Implement logout logic (clear sessions, cookies, ...) here
        and return the response back

        Returns:
            response: return the response back

        Examples:
            python
            async def logout(self, request: Request, response: Response) -> Response:
                request.session.clear()
                return response
            
        """
        raise NotImplementedError()

    async def render_login(self, request: Request, admin: "BaseAdmin") -> Response:
        """Render the default login page for username & password authentication."""
        if request.method == "GET":
            return admin.templates.TemplateResponse(
                request=request,
                name="login.html",
                context={"_is_login_path": True},
            )
        form = await request.form()
        try:
            return await self.login(
                form.get("username"),  # type: ignore
                form.get("password"),  # type: ignore
                form.get("remember_me") == "on",
                request,
                RedirectResponse(
                    request.query_params.get("next")
                    or request.url_for(admin.route_name + ":index"),
                    status_code=HTTP_303_SEE_OTHER,
                ),
            )
        except FormValidationError as errors:
            return admin.templates.TemplateResponse(
                request=request,
                name="login.html",
                context={"form_errors": errors, "_is_login_path": True},
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            )
        except LoginFailed as error:
            return admin.templates.TemplateResponse(
                request=request,
                name="login.html",
                context={"error": error.msg, "_is_login_path": True},
                status_code=HTTP_400_BAD_REQUEST,
            )

    async def render_logout(self, request: Request, admin: "BaseAdmin") -> Response:
        """Render the default logout page."""
        return await self.logout(
            request,
            RedirectResponse(
                request.url_for(admin.route_name + ":index"),
                status_code=HTTP_303_SEE_OTHER,
            ),
        )

    def get_login_route(self, admin: "BaseAdmin") -> Route:
        """
        Get the login route for the admin interface.
        """
        return Route(
            self.login_path,
            wrap_endpoint_with_kwargs(self.render_login, admin=admin),
            methods=["GET", "POST"],
        )

    def get_logout_route(self, admin: "BaseAdmin") -> Route:
        """
        Get the logout route for the admin interface.
        """
        return Route(
            self.logout_path,
            wrap_endpoint_with_kwargs(self.render_logout, admin=admin),
            methods=["GET"],
        )

    def setup_admin(self, admin: "BaseAdmin") -> None:
        """
        Set up the admin interface by adding necessary middleware and routes.
        """
        admin.middlewares.append(self.get_middleware(admin=admin))
        login_route = self.get_login_route(admin=admin)
        logout_route = self.get_logout_route(admin=admin)
        login_route.name = "login"
        logout_route.name = "logout"
        admin.routes.extend([login_route, logout_route])

Source code in starlette_admin/auth.py

class AuthProvider(BaseAuthProvider):
    async def login(
        self,
        username: str,
        password: str,
        remember_me: bool,
        request: Request,
        response: Response,
    ) -> Response:
        """
        This method will be called to validate user credentials

        Returns:
            response: return the response back

        Raises:
            FormValidationError: when form values is not valid
            LoginFailed: to display general error

        Examples:
            python
            async def login(
                self,
                username: str,
                password: str,
                remember_me: bool,
                request: Request,
                response: Response,
            ) -> Response:
                if len(username) < 3:
                    # Form data validation
                    raise FormValidationError(
                        {"username": "Ensure username has at least 03 characters"}
                    )

                if username in my_users_db and password == "password":
                    # Save username in session
                    request.session.update({"username": username})
                    return response

                raise LoginFailed("Invalid username or password")
            
        """
        raise LoginFailed("Not Implemented")

    async def logout(self, request: Request, response: Response) -> Response:
        """
        Implement logout logic (clear sessions, cookies, ...) here
        and return the response back

        Returns:
            response: return the response back

        Examples:
            python
            async def logout(self, request: Request, response: Response) -> Response:
                request.session.clear()
                return response
            
        """
        raise NotImplementedError()

    async def render_login(self, request: Request, admin: "BaseAdmin") -> Response:
        """Render the default login page for username & password authentication."""
        if request.method == "GET":
            return admin.templates.TemplateResponse(
                request=request,
                name="login.html",
                context={"_is_login_path": True},
            )
        form = await request.form()
        try:
            return await self.login(
                form.get("username"),  # type: ignore
                form.get("password"),  # type: ignore
                form.get("remember_me") == "on",
                request,
                RedirectResponse(
                    request.query_params.get("next")
                    or request.url_for(admin.route_name + ":index"),
                    status_code=HTTP_303_SEE_OTHER,
                ),
            )
        except FormValidationError as errors:
            return admin.templates.TemplateResponse(
                request=request,
                name="login.html",
                context={"form_errors": errors, "_is_login_path": True},
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            )
        except LoginFailed as error:
            return admin.templates.TemplateResponse(
                request=request,
                name="login.html",
                context={"error": error.msg, "_is_login_path": True},
                status_code=HTTP_400_BAD_REQUEST,
            )

    async def render_logout(self, request: Request, admin: "BaseAdmin") -> Response:
        """Render the default logout page."""
        return await self.logout(
            request,
            RedirectResponse(
                request.url_for(admin.route_name + ":index"),
                status_code=HTTP_303_SEE_OTHER,
            ),
        )

    def get_login_route(self, admin: "BaseAdmin") -> Route:
        """
        Get the login route for the admin interface.
        """
        return Route(
            self.login_path,
            wrap_endpoint_with_kwargs(self.render_login, admin=admin),
            methods=["GET", "POST"],
        )

    def get_logout_route(self, admin: "BaseAdmin") -> Route:
        """
        Get the logout route for the admin interface.
        """
        return Route(
            self.logout_path,
            wrap_endpoint_with_kwargs(self.render_logout, admin=admin),
            methods=["GET"],
        )

    def setup_admin(self, admin: "BaseAdmin") -> None:
        """
        Set up the admin interface by adding necessary middleware and routes.
        """
        admin.middlewares.append(self.get_middleware(admin=admin))
        login_route = self.get_login_route(admin=admin)
        logout_route = self.get_logout_route(admin=admin)
        login_route.name = "login"
        logout_route.name = "logout"
        admin.routes.extend([login_route, logout_route])

get_login_route(admin)

Get the login route for the admin interface.
Source code in starlette_admin/auth.py

def get_login_route(self, admin: "BaseAdmin") -> Route:
    """
    Get the login route for the admin interface.
    """
    return Route(
        self.login_path,
        wrap_endpoint_with_kwargs(self.render_login, admin=admin),
        methods=["GET", "POST"],
    )

Source code in starlette_admin/auth.py

def get_login_route(self, admin: "BaseAdmin") -> Route:
    """
    Get the login route for the admin interface.
    """
    return Route(
        self.login_path,
        wrap_endpoint_with_kwargs(self.render_login, admin=admin),
        methods=["GET", "POST"],
    )

get_logout_route(admin)

Get the logout route for the admin interface.
Source code in starlette_admin/auth.py

def get_logout_route(self, admin: "BaseAdmin") -> Route:
    """
    Get the logout route for the admin interface.
    """
    return Route(
        self.logout_path,
        wrap_endpoint_with_kwargs(self.render_logout, admin=admin),
        methods=["GET"],
    )

Source code in starlette_admin/auth.py

def get_logout_route(self, admin: "BaseAdmin") -> Route:
    """
    Get the logout route for the admin interface.
    """
    return Route(
        self.logout_path,
        wrap_endpoint_with_kwargs(self.render_logout, admin=admin),
        methods=["GET"],
    )

login(username, password, remember_me, request, response) async

This method will be called to validate user credentials

Returns:
Name 	Type 	Description
response 	Response 	

return the response back

Raises:
Type 	Description
FormValidationError 	

when form values is not valid
LoginFailed 	

to display general error

Examples:

async def login(
    self,
    username: str,
    password: str,
    remember_me: bool,
    request: Request,
    response: Response,
) -> Response:
    if len(username) < 3:
        # Form data validation
        raise FormValidationError(
            {"username": "Ensure username has at least 03 characters"}
        )

    if username in my_users_db and password == "password":
        # Save username in session
        request.session.update({"username": username})
        return response

    raise LoginFailed("Invalid username or password")

Source code in starlette_admin/auth.py

async def login(
    self,
    username: str,
    password: str,
    remember_me: bool,
    request: Request,
    response: Response,
) -> Response:
    """
    This method will be called to validate user credentials

    Returns:
        response: return the response back

    Raises:
        FormValidationError: when form values is not valid
        LoginFailed: to display general error

    Examples:
        python
        async def login(
            self,
            username: str,
            password: str,
            remember_me: bool,
            request: Request,
            response: Response,
        ) -> Response:
            if len(username) < 3:
                # Form data validation
                raise FormValidationError(
                    {"username": "Ensure username has at least 03 characters"}
                )

            if username in my_users_db and password == "password":
                # Save username in session
                request.session.update({"username": username})
                return response

            raise LoginFailed("Invalid username or password")
        
    """
    raise LoginFailed("Not Implemented")

Source code in starlette_admin/auth.py

async def login(
    self,
    username: str,
    password: str,
    remember_me: bool,
    request: Request,
    response: Response,
) -> Response:
    """
    This method will be called to validate user credentials

    Returns:
        response: return the response back

    Raises:
        FormValidationError: when form values is not valid
        LoginFailed: to display general error

    Examples:
        python
        async def login(
            self,
            username: str,
            password: str,
            remember_me: bool,
            request: Request,
            response: Response,
        ) -> Response:
            if len(username) < 3:
                # Form data validation
                raise FormValidationError(
                    {"username": "Ensure username has at least 03 characters"}
                )

            if username in my_users_db and password == "password":
                # Save username in session
                request.session.update({"username": username})
                return response

            raise LoginFailed("Invalid username or password")
        
    """
    raise LoginFailed("Not Implemented")

logout(request, response) async

Implement logout logic (clear sessions, cookies, ...) here and return the response back

Returns:
Name 	Type 	Description
response 	Response 	

return the response back

Examples:

async def logout(self, request: Request, response: Response) -> Response:
    request.session.clear()
    return response

Source code in starlette_admin/auth.py

async def logout(self, request: Request, response: Response) -> Response:
    """
    Implement logout logic (clear sessions, cookies, ...) here
    and return the response back

    Returns:
        response: return the response back

    Examples:
        python
        async def logout(self, request: Request, response: Response) -> Response:
            request.session.clear()
            return response
        
    """
    raise NotImplementedError()

Source code in starlette_admin/auth.py

async def logout(self, request: Request, response: Response) -> Response:
    """
    Implement logout logic (clear sessions, cookies, ...) here
    and return the response back

    Returns:
        response: return the response back

    Examples:
        python
        async def logout(self, request: Request, response: Response) -> Response:
            request.session.clear()
            return response
        
    """
    raise NotImplementedError()

render_login(request, admin) async

Render the default login page for username & password authentication.
Source code in starlette_admin/auth.py

async def render_login(self, request: Request, admin: "BaseAdmin") -> Response:
    """Render the default login page for username & password authentication."""
    if request.method == "GET":
        return admin.templates.TemplateResponse(
            request=request,
            name="login.html",
            context={"_is_login_path": True},
        )
    form = await request.form()
    try:
        return await self.login(
            form.get("username"),  # type: ignore
            form.get("password"),  # type: ignore
            form.get("remember_me") == "on",
            request,
            RedirectResponse(
                request.query_params.get("next")
                or request.url_for(admin.route_name + ":index"),
                status_code=HTTP_303_SEE_OTHER,
            ),
        )
    except FormValidationError as errors:
        return admin.templates.TemplateResponse(
            request=request,
            name="login.html",
            context={"form_errors": errors, "_is_login_path": True},
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        )
    except LoginFailed as error:
        return admin.templates.TemplateResponse(
            request=request,
            name="login.html",
            context={"error": error.msg, "_is_login_path": True},
            status_code=HTTP_400_BAD_REQUEST,
        )

Source code in starlette_admin/auth.py

async def render_login(self, request: Request, admin: "BaseAdmin") -> Response:
    """Render the default login page for username & password authentication."""
    if request.method == "GET":
        return admin.templates.TemplateResponse(
            request=request,
            name="login.html",
            context={"_is_login_path": True},
        )
    form = await request.form()
    try:
        return await self.login(
            form.get("username"),  # type: ignore
            form.get("password"),  # type: ignore
            form.get("remember_me") == "on",
            request,
            RedirectResponse(
                request.query_params.get("next")
                or request.url_for(admin.route_name + ":index"),
                status_code=HTTP_303_SEE_OTHER,
            ),
        )
    except FormValidationError as errors:
        return admin.templates.TemplateResponse(
            request=request,
            name="login.html",
            context={"form_errors": errors, "_is_login_path": True},
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        )
    except LoginFailed as error:
        return admin.templates.TemplateResponse(
            request=request,
            name="login.html",
            context={"error": error.msg, "_is_login_path": True},
            status_code=HTTP_400_BAD_REQUEST,
        )

render_logout(request, admin) async

Render the default logout page.
Source code in starlette_admin/auth.py

async def render_logout(self, request: Request, admin: "BaseAdmin") -> Response:
    """Render the default logout page."""
    return await self.logout(
        request,
        RedirectResponse(
            request.url_for(admin.route_name + ":index"),
            status_code=HTTP_303_SEE_OTHER,
        ),
    )

Source code in starlette_admin/auth.py

async def render_logout(self, request: Request, admin: "BaseAdmin") -> Response:
    """Render the default logout page."""
    return await self.logout(
        request,
        RedirectResponse(
            request.url_for(admin.route_name + ":index"),
            status_code=HTTP_303_SEE_OTHER,
        ),
    )

setup_admin(admin)

Set up the admin interface by adding necessary middleware and routes.
Source code in starlette_admin/auth.py

def setup_admin(self, admin: "BaseAdmin") -> None:
    """
    Set up the admin interface by adding necessary middleware and routes.
    """
    admin.middlewares.append(self.get_middleware(admin=admin))
    login_route = self.get_login_route(admin=admin)
    logout_route = self.get_logout_route(admin=admin)
    login_route.name = "login"
    logout_route.name = "logout"
    admin.routes.extend([login_route, logout_route])

Source code in starlette_admin/auth.py

def setup_admin(self, admin: "BaseAdmin") -> None:
    """
    Set up the admin interface by adding necessary middleware and routes.
    """
    admin.middlewares.append(self.get_middleware(admin=admin))
    login_route = self.get_login_route(admin=admin)
    logout_route = self.get_logout_route(admin=admin)
    login_route.name = "login"
    logout_route.name = "logout"
    admin.routes.extend([login_route, logout_route])

login_not_required(endpoint)

Decorators for endpoints that do not require login.
Source code in starlette_admin/auth.py

def login_not_required(
    endpoint: Callable[..., Any],
) -> Callable[..., Any]:
    """Decorators for endpoints that do not require login."""

    endpoint._login_not_required = True  # type: ignore[attr-defined]

    return endpoint

def login_not_required(
    endpoint: Callable[..., Any],
) -> Callable[..., Any]:
    """Decorators for endpoints that do not require login."""

    endpoint._login_not_required = True  # type: ignore[attr-defined]

    return endpoint

Actions
starlette_admin.actions
action(name, text, confirmation=None, submit_btn_class='btn-primary', submit_btn_text=_('Yes, Proceed'), icon_class=None, form=None, custom_response=False)

Decorator to add custom batch actions to your ModelView

Parameters:
Name 	Type 	Description 	Default
name 	str 	

unique action name for your ModelView
	required
text 	str 	

Action text
	required
confirmation 	Optional[str] 	

Confirmation text. If not provided, action will be executed unconditionally.
	None
submit_btn_text 	Optional[str] 	

Submit button text
	lazy_gettext('Yes, Proceed')
submit_btn_class 	Optional[str] 	

Submit button variant (ex. btn-primary, btn-ghost-info, btn-outline-danger, ...)
	'btn-primary'
icon_class 	Optional[str] 	

Icon class (ex. fa-lite fa-folder, fa-duotone fa-circle-right, ...)
	None
form 	Optional[str] 	

Custom form to collect data from user
	None
custom_response 	Optional[bool] 	

Set to True when you want to return a custom Starlette response from your action instead of a string.
	False

Usage

class ArticleView(ModelView):
    actions = ['make_published', 'redirect']

    @action(
        name="make_published",
        text="Mark selected articles as published",
        confirmation="Are you sure you want to mark selected articles as published ?",
        submit_btn_text="Yes, proceed",
        submit_btn_class="btn-success",
        form='''
        <form>
            
        </form>
        '''
    )
    async def make_published_action(self, request: Request, pks: List[Any]) -> str:
        # Write your logic here

        data: FormData =  await request.form()
        user_input = data.get("example-text-input")

        if ... :
            # Display meaningfully error
            raise ActionFailed("Sorry, We can't proceed this action now.")
        # Display successfully message
        return "{} articles were successfully marked as published".format(len(pks))

    # For custom response
    @action(
        name="redirect",
        text="Redirect",
        custom_response=True,
        confirmation="Fill the form",
        form='''
        <form>
            
        </form>
        '''
     )
    async def redirect_action(self, request: Request, pks: List[Any]) -> Response:
        data = await request.form()
        return RedirectResponse(f"https://example.com/?value={data['value']}")

Source code in starlette_admin/actions.py

def action(
    name: str,
    text: str,
    confirmation: Optional[str] = None,
    submit_btn_class: Optional[str] = "btn-primary",
    submit_btn_text: Optional[str] = _("Yes, Proceed"),
    icon_class: Optional[str] = None,
    form: Optional[str] = None,
    custom_response: Optional[bool] = False,
) -> Callable[[Callable[..., Awaitable[str]]], Any]:
    """
    Decorator to add custom batch actions to your [ModelView][starlette_admin.views.BaseModelView]

    Args:
        name: unique action name for your ModelView
        text: Action text
        confirmation: Confirmation text. If not provided, action will be executed
                      unconditionally.
        submit_btn_text: Submit button text
        submit_btn_class: Submit button variant (ex. 'btn-primary', 'btn-ghost-info',
                'btn-outline-danger', ...)
        icon_class: Icon class (ex. 'fa-lite fa-folder', 'fa-duotone fa-circle-right', ...)
        form: Custom form to collect data from user
        custom_response: Set to True when you want to return a custom Starlette response
            from your action instead of a string.

    !!! usage

        python
        class ArticleView(ModelView):
            actions = ['make_published', 'redirect']

            @action(
                name="make_published",
                text="Mark selected articles as published",
                confirmation="Are you sure you want to mark selected articles as published ?",
                submit_btn_text="Yes, proceed",
                submit_btn_class="btn-success",
                form='''
                <form>
                    
                </form>
                '''
            )
            async def make_published_action(self, request: Request, pks: List[Any]) -> str:
                # Write your logic here

                data: FormData =  await request.form()
                user_input = data.get("example-text-input")

                if ... :
                    # Display meaningfully error
                    raise ActionFailed("Sorry, We can't proceed this action now.")
                # Display successfully message
                return "{} articles were successfully marked as published".format(len(pks))

            # For custom response
            @action(
                name="redirect",
                text="Redirect",
                custom_response=True,
                confirmation="Fill the form",
                form='''
                <form>
                    
                </form>
                '''
             )
            async def redirect_action(self, request: Request, pks: List[Any]) -> Response:
                data = await request.form()
                return RedirectResponse(f"https://example.com/?value={data['value']}")
        
    """

    def wrap(f: Callable[..., Awaitable[str]]) -> Callable[..., Awaitable[str]]:
        f._action = {  # type: ignore
            "name": name,
            "text": text,
            "confirmation": confirmation,
            "submit_btn_text": submit_btn_text,
            "submit_btn_class": submit_btn_class,
            "icon_class": icon_class,
            "form": form if form is not None else "",
            "custom_response": custom_response,
        }
        return f

    return wrap

Source code in starlette_admin/actions.py

def action(
    name: str,
    text: str,
    confirmation: Optional[str] = None,
    submit_btn_class: Optional[str] = "btn-primary",
    submit_btn_text: Optional[str] = _("Yes, Proceed"),
    icon_class: Optional[str] = None,
    form: Optional[str] = None,
    custom_response: Optional[bool] = False,
) -> Callable[[Callable[..., Awaitable[str]]], Any]:
    """
    Decorator to add custom batch actions to your [ModelView][starlette_admin.views.BaseModelView]

    Args:
        name: unique action name for your ModelView
        text: Action text
        confirmation: Confirmation text. If not provided, action will be executed
                      unconditionally.
        submit_btn_text: Submit button text
        submit_btn_class: Submit button variant (ex. 'btn-primary', 'btn-ghost-info',
                'btn-outline-danger', ...)
        icon_class: Icon class (ex. 'fa-lite fa-folder', 'fa-duotone fa-circle-right', ...)
        form: Custom form to collect data from user
        custom_response: Set to True when you want to return a custom Starlette response
            from your action instead of a string.

    !!! usage

        python
        class ArticleView(ModelView):
            actions = ['make_published', 'redirect']

            @action(
                name="make_published",
                text="Mark selected articles as published",
                confirmation="Are you sure you want to mark selected articles as published ?",
                submit_btn_text="Yes, proceed",
                submit_btn_class="btn-success",
                form='''
                <form>
                    
                </form>
                '''
            )
            async def make_published_action(self, request: Request, pks: List[Any]) -> str:
                # Write your logic here

                data: FormData =  await request.form()
                user_input = data.get("example-text-input")

                if ... :
                    # Display meaningfully error
                    raise ActionFailed("Sorry, We can't proceed this action now.")
                # Display successfully message
                return "{} articles were successfully marked as published".format(len(pks))

            # For custom response
            @action(
                name="redirect",
                text="Redirect",
                custom_response=True,
                confirmation="Fill the form",
                form='''
                <form>
                    
                </form>
                '''
             )
            async def redirect_action(self, request: Request, pks: List[Any]) -> Response:
                data = await request.form()
                return RedirectResponse(f"https://example.com/?value={data['value']}")
        
    """

    def wrap(f: Callable[..., Awaitable[str]]) -> Callable[..., Awaitable[str]]:
        f._action = {  # type: ignore
            "name": name,
            "text": text,
            "confirmation": confirmation,
            "submit_btn_text": submit_btn_text,
            "submit_btn_class": submit_btn_class,
            "icon_class": icon_class,
            "form": form if form is not None else "",
            "custom_response": custom_response,
        }
        return f

    return wrap

row_action(name, text, confirmation=None, action_btn_class=None, submit_btn_class='btn-primary', submit_btn_text=_('Yes, Proceed'), icon_class=None, form=None, custom_response=False, exclude_from_list=False, exclude_from_detail=False)

Decorator to add custom row actions to your ModelView

Parameters:
Name 	Type 	Description 	Default
name 	str 	

Unique row action name for the ModelView.
	required
text 	str 	

Action text displayed to users.
	required
confirmation 	Optional[str] 	

Confirmation text; if provided, the action will require confirmation.
	None
action_btn_class 	Optional[str] 	

Action button variant for detail page (ex. btn-success, btn-outline, ...)
	None
submit_btn_class 	Optional[str] 	

Submit button variant (ex. btn-primary, btn-ghost-info, btn-outline-danger, ...)
	'btn-primary'
submit_btn_text 	Optional[str] 	

Text for the submit button.
	lazy_gettext('Yes, Proceed')
icon_class 	Optional[str] 	

Icon class (ex. fa-lite fa-folder, fa-duotone fa-circle-right, ...)
	None
form 	Optional[str] 	

Custom HTML to collect data from the user.
	None
custom_response 	Optional[bool] 	

Set to True when you want to return a custom Starlette response from your action instead of a string.
	False
exclude_from_list 	bool 	

Set to True to exclude the action from the list view.
	False
exclude_from_detail 	bool 	

Set to True to exclude the action from the detail view.
	False

Usage

@row_action(
    name="make_published",
    text="Mark as published",
    confirmation="Are you sure you want to mark this article as published ?",
    icon_class="fas fa-check-circle",
    submit_btn_text="Yes, proceed",
    submit_btn_class="btn-success",
    action_btn_class="btn-info",
)
async def make_published_row_action(self, request: Request, pk: Any) -> str:
    session: Session = request.state.session
    article = await self.find_by_pk(request, pk)
    if article.status == Status.Published:
        raise ActionFailed("The article is already marked as published.")
    article.status = Status.Published
    session.add(article)
    session.commit()
    return f"The article was successfully marked as published."

Source code in starlette_admin/actions.py

def row_action(
    name: str,
    text: str,
    confirmation: Optional[str] = None,
    action_btn_class: Optional[str] = None,
    submit_btn_class: Optional[str] = "btn-primary",
    submit_btn_text: Optional[str] = _("Yes, Proceed"),
    icon_class: Optional[str] = None,
    form: Optional[str] = None,
    custom_response: Optional[bool] = False,
    exclude_from_list: bool = False,
    exclude_from_detail: bool = False,
) -> Callable[[Callable[..., Awaitable[str]]], Any]:
    """
    Decorator to add custom row actions to your [ModelView][starlette_admin.views.BaseModelView]

    Args:
        name: Unique row action name for the ModelView.
        text: Action text displayed to users.
        confirmation: Confirmation text; if provided, the action will require confirmation.
        action_btn_class: Action button variant for detail page (ex. 'btn-success', 'btn-outline', ...)
        submit_btn_class: Submit button variant (ex. 'btn-primary', 'btn-ghost-info', 'btn-outline-danger', ...)
        submit_btn_text: Text for the submit button.
        icon_class: Icon class (ex. 'fa-lite fa-folder', 'fa-duotone fa-circle-right', ...)
        form: Custom HTML to collect data from the user.
        custom_response: Set to True when you want to return a custom Starlette response
            from your action instead of a string.
        exclude_from_list: Set to True to exclude the action from the list view.
        exclude_from_detail: Set to True to exclude the action from the detail view.

    !!! usage

        python
        @row_action(
            name="make_published",
            text="Mark as published",
            confirmation="Are you sure you want to mark this article as published ?",
            icon_class="fas fa-check-circle",
            submit_btn_text="Yes, proceed",
            submit_btn_class="btn-success",
            action_btn_class="btn-info",
        )
        async def make_published_row_action(self, request: Request, pk: Any) -> str:
            session: Session = request.state.session
            article = await self.find_by_pk(request, pk)
            if article.status == Status.Published:
                raise ActionFailed("The article is already marked as published.")
            article.status = Status.Published
            session.add(article)
            session.commit()
            return f"The article was successfully marked as published."
        
    """

    def wrap(f: Callable[..., Awaitable[str]]) -> Callable[..., Awaitable[str]]:
        f._row_action = {  # type: ignore
            "name": name,
            "text": text,
            "confirmation": confirmation,
            "action_btn_class": action_btn_class,
            "submit_btn_text": submit_btn_text,
            "submit_btn_class": submit_btn_class,
            "icon_class": icon_class,
            "form": form if form is not None else "",
            "custom_response": custom_response,
            "exclude_from_list": exclude_from_list,
            "exclude_from_detail": exclude_from_detail,
        }
        return f

    return wrap

Source code in starlette_admin/actions.py

def row_action(
    name: str,
    text: str,
    confirmation: Optional[str] = None,
    action_btn_class: Optional[str] = None,
    submit_btn_class: Optional[str] = "btn-primary",
    submit_btn_text: Optional[str] = _("Yes, Proceed"),
    icon_class: Optional[str] = None,
    form: Optional[str] = None,
    custom_response: Optional[bool] = False,
    exclude_from_list: bool = False,
    exclude_from_detail: bool = False,
) -> Callable[[Callable[..., Awaitable[str]]], Any]:
    """
    Decorator to add custom row actions to your [ModelView][starlette_admin.views.BaseModelView]

    Args:
        name: Unique row action name for the ModelView.
        text: Action text displayed to users.
        confirmation: Confirmation text; if provided, the action will require confirmation.
        action_btn_class: Action button variant for detail page (ex. 'btn-success', 'btn-outline', ...)
        submit_btn_class: Submit button variant (ex. 'btn-primary', 'btn-ghost-info', 'btn-outline-danger', ...)
        submit_btn_text: Text for the submit button.
        icon_class: Icon class (ex. 'fa-lite fa-folder', 'fa-duotone fa-circle-right', ...)
        form: Custom HTML to collect data from the user.
        custom_response: Set to True when you want to return a custom Starlette response
            from your action instead of a string.
        exclude_from_list: Set to True to exclude the action from the list view.
        exclude_from_detail: Set to True to exclude the action from the detail view.

    !!! usage

        python
        @row_action(
            name="make_published",
            text="Mark as published",
            confirmation="Are you sure you want to mark this article as published ?",
            icon_class="fas fa-check-circle",
            submit_btn_text="Yes, proceed",
            submit_btn_class="btn-success",
            action_btn_class="btn-info",
        )
        async def make_published_row_action(self, request: Request, pk: Any) -> str:
            session: Session = request.state.session
            article = await self.find_by_pk(request, pk)
            if article.status == Status.Published:
                raise ActionFailed("The article is already marked as published.")
            article.status = Status.Published
            session.add(article)
            session.commit()
            return f"The article was successfully marked as published."
        
    """

    def wrap(f: Callable[..., Awaitable[str]]) -> Callable[..., Awaitable[str]]:
        f._row_action = {  # type: ignore
            "name": name,
            "text": text,
            "confirmation": confirmation,
            "action_btn_class": action_btn_class,
            "submit_btn_text": submit_btn_text,
            "submit_btn_class": submit_btn_class,
            "icon_class": icon_class,
            "form": form if form is not None else "",
            "custom_response": custom_response,
            "exclude_from_list": exclude_from_list,
            "exclude_from_detail": exclude_from_detail,
        }
        return f

    return wrap

link_row_action(name, text, action_btn_class=None, icon_class=None, exclude_from_list=False, exclude_from_detail=False)

Decorator to add custom row link actions to a ModelView for URL redirection.

Note

This decorator is designed to create row actions that redirect to a URL, making it ideal for cases where a row action should simply navigate users to a website or internal page.

Parameters:
Name 	Type 	Description 	Default
name 	str 	

Unique row action name for the ModelView.
	required
text 	str 	

Action text displayed to users.
	required
action_btn_class 	Optional[str] 	

Action button variant for detail page (ex. btn-success, btn-outline, ...)
	None
icon_class 	Optional[str] 	

Icon class (ex. fa-lite fa-folder, fa-duotone fa-circle-right, ...)
	None
exclude_from_list 	bool 	

Set to True to exclude the action from the list view.
	False
exclude_from_detail 	bool 	

Set to True to exclude the action from the detail view.
	False

Usage

@link_row_action(
    name="go_to_example",
    text="Go to example.com",
    icon_class="fas fa-arrow-up-right-from-square",
)
def go_to_example_row_action(self, request: Request, pk: Any) -> str:
    return f"https://example.com/?pk={pk}"

Source code in starlette_admin/actions.py

def link_row_action(
    name: str,
    text: str,
    action_btn_class: Optional[str] = None,
    icon_class: Optional[str] = None,
    exclude_from_list: bool = False,
    exclude_from_detail: bool = False,
) -> Callable[[Callable[..., str]], Any]:
    """
    Decorator to add custom row link actions to a ModelView for URL redirection.

    !!! note

        This decorator is designed to create row actions that redirect to a URL, making it ideal for cases where a
        row action should simply navigate users to a website or internal page.

    Args:
        name: Unique row action name for the ModelView.
        text: Action text displayed to users.
        action_btn_class: Action button variant for detail page (ex. 'btn-success', 'btn-outline', ...)
        icon_class: Icon class (ex. 'fa-lite fa-folder', 'fa-duotone fa-circle-right', ...)
        exclude_from_list: Set to True to exclude the action from the list view.
        exclude_from_detail: Set to True to exclude the action from the detail view.

    !!! usage

        python
        @link_row_action(
            name="go_to_example",
            text="Go to example.com",
            icon_class="fas fa-arrow-up-right-from-square",
        )
        def go_to_example_row_action(self, request: Request, pk: Any) -> str:
            return f"https://example.com/?pk={pk}"
        

    """

    def wrap(f: Callable[..., str]) -> Callable[..., str]:
        f._row_action = {  # type: ignore
            "name": name,
            "text": text,
            "action_btn_class": action_btn_class,
            "icon_class": icon_class,
            "is_link": True,
            "exclude_from_list": exclude_from_list,
            "exclude_from_detail": exclude_from_detail,
        }
        return f

    return wrap

def link_row_action(
    name: str,
    text: str,
    action_btn_class: Optional[str] = None,
    icon_class: Optional[str] = None,
    exclude_from_list: bool = False,
    exclude_from_detail: bool = False,
) -> Callable[[Callable[..., str]], Any]:
    """
    Decorator to add custom row link actions to a ModelView for URL redirection.

    !!! note

        This decorator is designed to create row actions that redirect to a URL, making it ideal for cases where a
        row action should simply navigate users to a website or internal page.

    Args:
        name: Unique row action name for the ModelView.
        text: Action text displayed to users.
        action_btn_class: Action button variant for detail page (ex. 'btn-success', 'btn-outline', ...)
        icon_class: Icon class (ex. 'fa-lite fa-folder', 'fa-duotone fa-circle-right', ...)
        exclude_from_list: Set to True to exclude the action from the list view.
        exclude_from_detail: Set to True to exclude the action from the detail view.

    !!! usage

        python
        @link_row_action(
            name="go_to_example",
            text="Go to example.com",
            icon_class="fas fa-arrow-up-right-from-square",
        )
        def go_to_example_row_action(self, request: Request, pk: Any) -> str:
            return f"https://example.com/?pk={pk}"
        

    """

    def wrap(f: Callable[..., str]) -> Callable[..., str]:
        f._row_action = {  # type: ignore
            "name": name,
            "text": text,
            "action_btn_class": action_btn_class,
            "icon_class": icon_class,
            "is_link": True,
            "exclude_from_list": exclude_from_list,
            "exclude_from_detail": exclude_from_detail,
        }
        return f

    return wrap

========================

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.15.1] - 2025-05-26

### Fixed

- Reenable autoescaping in template rendering by [@jowilf](https://github.com/jowilf)
  in [#662](https://github.com/jowilf/starlette-admin/pull/662)

## [0.15.0] - 2025-05-21

### Breaking Changes

#### Updated Method Signatures in 'ModelView' Class

The following methods in the 'ModelView' class now require an additional 'request' parameter:

1. **'get_list_query'**
    - **Old Signature:** 'def get_list_query(self) -> Select'
    - **New Signature:** 'def get_list_query(self, request: Request) -> Select'

2. **'get_count_query'**
    - **Old Signature:** 'def get_count_query(self) -> Select'
    - **New Signature:** 'def get_count_query(self, request: Request) -> Select'

#### Impact on Custom Implementations

If you have extended or overridden the 'get_list_query' or 'get_count_query' methods in your custom views, you **must
update** their definitions to include the 'request' parameter.

#### Example Update

=== "Before"

    python
    def get_list_query(self) -> Select:
        return super().get_list_query().where(Post.published == true())
    

=== "After"

    python
    def get_list_query(self, request: Request) -> Select:
      return super().get_list_query(request).where(Post.published == true())
    

### Added

* Implement Beanie ODM Support by [@alexdlukens](https://github.com/alexdlukens)
  in [#656](https://github.com/jowilf/starlette-admin/pull/656)
* Add zh_Hant (Traditional Chinese) translation by [@limouren](https://github.com/limouren)
  in [#646](https://github.com/jowilf/starlette-admin/pull/646)
* Add 'get_details_query' to SQLAlchemy ModelView. by [@nimaxin](https://github.com/nimaxin)
  in [#643](https://github.com/jowilf/starlette-admin/pull/643)
* feat(sqla): add support for joined table polymorphic inheritance by [@noamsto](https://github.com/noamsto)
  in [#633](https://github.com/jowilf/starlette-admin/pull/633)
* Improve JsonField form template by [@jowilf](https://github.com/jowilf)
  in [#639](https://github.com/jowilf/starlette-admin/pull/639)
* bump httpx test dependency by [@pbsds](https://github.com/pbsds)
  in [#630](https://github.com/jowilf/starlette-admin/pull/630)
* Allow overriding the default templates by [@jowilf](https://github.com/jowilf)
  in [#636](https://github.com/jowilf/starlette-admin/pull/636)
* upgrade tabler to 1.1.0 by [@jowilf](https://github.com/jowilf)
  in [#637](https://github.com/jowilf/starlette-admin/pull/637)
* Add support for sqlalchemy 'collection_class' property by [@jowilf](https://github.com/jowilf)
  in [#625](https://github.com/jowilf/starlette-admin/pull/625)
* feat(base): add redirect_slashes option to mount_to method by [@noamsto](https://github.com/noamsto)
  in [#618](https://github.com/jowilf/starlette-admin/pull/618)
* escape row and bulk actions form value in template by [@jowilf](https://github.com/jowilf)
  in [#615](https://github.com/jowilf/starlette-admin/pull/615)
* upgrade tabler to beta21 by [@jowilf](https://github.com/jowilf)
  in [#599](https://github.com/jowilf/starlette-admin/pull/599)
* Upgrade Odmantic support to v1.0+ by [@jowilf](https://github.com/jowilf)
  in [#594](https://github.com/jowilf/starlette-admin/pull/594)
* Add Portuguese translation by [@abnerjacobsen](https://github.com/abnerjacobsen)
  in [#480](https://github.com/jowilf/starlette-admin/pull/480)

### Fixed

* Fix dictionary size change exception when using SQLAlchemy 'association_proxy' by [@jowilf](https://github.com/jowilf)
  in [#624](https://github.com/jowilf/starlette-admin/pull/624)
* Update enum rendering to ensure 'selected' state is applied for data value of 0
  by [@tomopy03](https://github.com/tomopy03) in [#621](https://github.com/jowilf/starlette-admin/pull/621)
* escape json value in relation template by [@jowilf](https://github.com/jowilf)
  in [#598](https://github.com/jowilf/starlette-admin/pull/598)
* Fix Deprecation Warnings for TemplateResponse and Jinja2Templates by [@ptrstn](https://github.com/ptrstn)
  in [#575](https://github.com/jowilf/starlette-admin/pull/575)

## [0.14.1] - 2024-07-12

### Fixed

* Fix JSON serialization error for UUID primary keys when excluded from list by [@alg](https://github.com/alg)
  in [#553](https://github.com/jowilf/starlette-admin/pull/553)

## [0.14.0] - 2024-05-28

### Added

* Add German translation
  by [@disrupted](https://github.com/disrupted)
  in [#523](https://github.com/jowilf/starlette-admin/pull/523)
* Add Support for favicon customization
  by [@omarmoo5](https://github.com/omarmoo5)
  in [#520](https://github.com/jowilf/starlette-admin/pull/520)

## [0.13.2] - 2024-02-04

### Fixed

* Remove extra whitespaces from TextAreaField form template (0.13.0 regression) by [@jowilf](https://github.com/jowilf)
  in [#494](https://github.com/jowilf/starlette-admin/pull/494)

## [0.13.1] - 2024-01-21

### Fixed

* Fixed the StopIteration exception raised in Sqlalchemy ModelView when the primary key is not included in the field
  list by [@jowilf](https://github.com/jowilf) in [#482](https://github.com/jowilf/starlette-admin/pull/482)

## [0.13.0] - 2024-01-16

### Added

* Enhance AuthMiddleware, introduce '@login_not_required' decorator and 'allow_routes', deprecate 'allow_paths'
  by [@jowilf](https://github.com/jowilf)
  in [#474](https://github.com/jowilf/starlette-admin/pull/474)
* Add a search bar on detail page to search by attributes or values
  by [@hasansezertasan](https://github.com/hasansezertasan)
  in [#461](https://github.com/jowilf/starlette-admin/pull/461)
* Refactor TinyMCEEditorField: support custom TinyMCE configuration
  by [@hasansezertasan](https://github.com/hasansezertasan)
  in [#380](https://github.com/jowilf/starlette-admin/pull/380)
* Add support for SQLAlchemy 'column_property' by [@jowilf](https://github.com/jowilf)
  in [#408](https://github.com/jowilf/starlette-admin/pull/408)
* Add support for SQLAlchemy Models with Multiple Primary Keys by [@jowilf](https://github.com/jowilf)
  in [#402](https://github.com/jowilf/starlette-admin/pull/402)
* Adds 'AdminConfig' to override 'app_title' and 'logo_url' in the templates
  by [@hasansezertasan](https://github.com/hasansezertasan)
  in [#374](https://github.com/jowilf/starlette-admin/pull/374)

### Fixed

* Support translation for login form placeholders by [@hasansezertasan](https://github.com/hasansezertasan)
  in [#425](https://github.com/jowilf/starlette-admin/pull/425)
* Fixes actions docstrings
  by [@mrharpo](https://github.com/mrharpo)
  in [#401](https://github.com/jowilf/starlette-admin/pull/401)

## [0.12.2] - 2023-11-13

* Fixed issue where "Empty" and "Not Empty" filters raised NotImplementedError on SQLAlchemy relationship attributes
  by [@whchi](https://github.com/whchi) in [#394](https://github.com/jowilf/starlette-admin/pull/394)

## [0.12.1] - 2023-11-07

* Fixed a regression caused by [#361](https://github.com/jowilf/starlette-admin/pull/361) where SQLAlchemy models with
  Mixin Classes raises AttributeError by [@hasansezertasan](https://github.com/hasansezertasan)
  in [#385](https://github.com/jowilf/starlette-admin/pull/385)

## [0.12.0] - 2023-11-07

### Added

* Add Before and After Hooks for Create, Edit, and Delete Operations by [@jowilf](https://github.com/jowilf)
  in [#327](https://github.com/jowilf/starlette-admin/pull/327)
* Feature: Row actions by [@jowilf](https://github.com/jowilf) & [@mrharpo](https://github.com/mrharpo)
  in [#348](https://github.com/jowilf/starlette-admin/pull/348)
  and [#302](https://github.com/jowilf/starlette-admin/pull/302)
* Add Support for Custom Sortable Field Mapping in SQLAlchemy ModelView by [@jowilf](https://github.com/jowilf)
  in [#328](https://github.com/jowilf/starlette-admin/pull/328)

???+ usage

    python hl_lines="12"
    class Post(Base):
        __tablename__ = "post"

        id: Mapped[int] = mapped_column(primary_key=True)
        title: Mapped[str] = mapped_column()
        user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
        user: Mapped[User] = relationship(back_populates="posts")

    class PostView(ModelView):
        sortable_field = ["id", "title", "user"]
        sortable_field_mapping = {
            "user": User.age,  # Sort by the age of the related user
        }
    

* Add support for Turkish language by [@hasansezertasan](https://github.com/hasansezertasan)
  in [#330](https://github.com/jowilf/starlette-admin/pull/330) & [#377](https://github.com/jowilf/starlette-admin/pull/377).
* Allow the page title customization from the ModelView by [@mrharpo](https://github.com/mrharpo)
  in [#311](https://github.com/jowilf/starlette-admin/pull/311)
* Add support for custom DataTables options by [@mrharpo](https://github.com/mrharpo)
  in [#308](https://github.com/jowilf/starlette-admin/pull/308)
* Add support for datatables [state saving](https://datatables.net/examples/basic_init/state_save.html)

???+ usage

    python
    class MyModelView(ModelView):
        save_state = True
    

### Fixed

* Fix [#347](https://github.com/jowilf/starlette-admin/issues/347): Detect SQLAlchemy primary key with custom column
  name by [@jowilf](https://github.com/jowilf)
  in [#361](https://github.com/jowilf/starlette-admin/pull/361)

* Fixed a bug with field access authorization where restricted users could not modify a partial list of fields in an
  entity by [@jowilf](https://github.com/jowilf) in [#360](https://github.com/jowilf/starlette-admin/pull/360)

### Internals

* Explicitly export all public functions and classes by [@jowilf](https://github.com/jowilf)
  in [#362](https://github.com/jowilf/starlette-admin/pull/362)

## [0.11.2] - 2023-08-31

### Fixed

* Bug Fix: Current Enum Value Not Pre-Selected on Edit by [@jowilf](https://github.com/jowilf)
  in [#273](https://github.com/jowilf/starlette-admin/pull/273)

## [0.11.1] - 2023-07-29

### Fixed

* Bug Fix: Ensure Excluded fields from a RequestAction are not treated by [@jowilf](https://github.com/jowilf)
  in [#251](https://github.com/jowilf/starlette-admin/pull/251)

## [0.11.0] - 2023-07-26

### Added

* Improve the Authentication Provider to support custom flow such as oauth2/OIDC by [@jowilf](https://github.com/jowilf)
  in [#221](https://github.com/jowilf/starlette-admin/pull/221).

### Internals

* Drop python 3.7 support by [@jowilf](https://github.com/jowilf)
  in [#248](https://github.com/jowilf/starlette-admin/pull/248)

## [0.10.1] - 2023-07-22

### Fixed

* Fix [#224](https://github.com/jowilf/starlette-admin/issues/224) by [@jowilf](https://github.com/jowilf)
  in [#227](https://github.com/jowilf/starlette-admin/pull/227)
* Fix [#239](https://github.com/jowilf/starlette-admin/issues/239): Order Select2 data by primary key during fetching by
  [@jowilf](https://github.com/jowilf) in [#241](https://github.com/jowilf/starlette-admin/issues/241)

## [0.10.0] - 2023-06-26

### Added

* Added support for Russian language in the web interface by [@nessshon](https://github.com/nessshon)
  in [#201](https://github.com/jowilf/starlette-admin/pull/201)
* i18n: Update message catalogs by [@jowilf](https://github.com/jowilf)
  in [#202](https://github.com/jowilf/starlette-admin/pull/202)
* Support custom response for batch actions by [@jowilf](https://github.com/jowilf)
  in [#212](https://github.com/jowilf/starlette-admin/pull/212)

### Fixed

* Fixed [#206](https://github.com/jowilf/starlette-admin/issues/206): Setting 'add_to_menu=False' in CustomView still
  results in the view being displayed in the menu

## [0.9.0] - 2023-05-25

### Added

* Enhance fields conversion logic to support custom converters
  by [@jowilf](https://github.com/jowilf) in [#191](https://github.com/jowilf/starlette-admin/pull/191)
* Add deployment section to documentation by [@jowilf](https://github.com/jowilf)
  in [#195](https://github.com/jowilf/starlette-admin/pull/195)

### Fixed

* Blank Edit Form Displayed for IntegerField with Value 0 by [@jowilf](https://github.com/jowilf)
  in [#194](https://github.com/jowilf/starlette-admin/pull/194)

## [0.8.2] - 2023-05-12

### Added

* Add 'allow_paths' parameter to AuthProvider to allow unauthenticated access to specific paths
  by [@jowilf](https://github.com/jowilf)
  in [#187](https://github.com/jowilf/starlette-admin/pull/187)
* Allow Unauthenticated Access to 'js.cookie.min.js' by [@mixartemev](https://github.com/mixartemev)
  in [#183](https://github.com/jowilf/starlette-admin/pull/183)

## [0.8.1] - 2023-04-30

### Added

* Update fontawesome to 6.4.0 & add missings webfonts by [@jowilf](https://github.com/jowilf)
  in [#176](https://github.com/jowilf/starlette-admin/pull/176)
* Allow class level configuration for ModelView identity, name & label by [@jowilf](https://github.com/jowilf)
  in [#178](https://github.com/jowilf/starlette-admin/pull/178)

## [0.8.0] - 2023-04-09

### Added

* Add extension to autovalidate SQLAlchemy data with pydantic by [@jowilf](https://github.com/jowilf)
  in [#144](https://github.com/jowilf/starlette-admin/pull/144)
* Make '_extract_fields()' method in BaseModelView public and renamed
  to [get_fields_list()][starlette_admin.views.BaseModelView.get_fields_list] by [@jowilf](https://github.com/jowilf)
  in [#148](https://github.com/jowilf/starlette-admin/pull/148)
* Add support for custom object representations in the admin interface with '__admin_repr__'
  and '__admin_select2_repr__'  by [@jowilf](https://github.com/jowilf)
  in [#152](https://github.com/jowilf/starlette-admin/pull/152). The documentation can be
  found [here](../user-guide/configurations/modelview/#object-representation)

### Internals

* Enhance code quality with additional ruff rules by [@jowilf](https://github.com/jowilf)
  in [#159](https://github.com/jowilf/starlette-admin/pull/159)

## [0.7.0] - 2023-03-24

### Added

* Allow custom form for batch actions by [@giaptx](https://github.com/giaptx) and [@jowilf](https://github.com/jowilf)
  in [#61](https://github.com/jowilf/starlette-admin/pull/61)
* Add [TinyMCEEditorField][starlette_admin.fields.TinyMCEEditorField] by [@sinisaos](https://github.com/sinisaos)
  and [@jowilf](https://github.com/jowilf)
  in [#131](https://github.com/jowilf/starlette-admin/pull/131)

### Internals

* Add SQLAlchemy model with Pydantic validation example [@jowilf](https://github.com/jowilf)
  in [#125](https://github.com/jowilf/starlette-admin/pull/125)
* Refactor and format HTML files for better readability by [@jowilf](https://github.com/jowilf)
  in [#136](https://github.com/jowilf/starlette-admin/pull/136)

## [0.6.0] - 2023-03-12

### Added

* Setup i18n and Add French translations by [@jowilf](https://github.com/jowilf)
  in [#74](https://github.com/jowilf/starlette-admin/pull/74)
*

Add [TimeZoneField][starlette_admin.fields.TimeZoneField], [CountryField][starlette_admin.fields.CountryField], [CurrencyField][starlette_admin.fields.CurrencyField] & [ArrowField][starlette_admin.fields.ArrowField]

* Add support for [sqlalchemy_utils](https://github.com/kvesteri/sqlalchemy-utils) data types
* Add SQLAlchemy 2 support by  [@jowilf](https://github.com/jowilf)
  in [#113](https://github.com/jowilf/starlette-admin/pull/113)
* Add support for initial order (sort) to apply to the table by [@jowilf](https://github.com/jowilf)
  in [#115](https://github.com/jowilf/starlette-admin/pull/115)

!!! usage

    python
    class User:
        id: int
        last_name: str
        first_name: str

    class UserView(ModelView):
        fields_default_sort = ["last_name", ("first_name", True)]

    admin.add_view(UserView(User))
    

### Fixed

* Fix [#69](https://github.com/jowilf/starlette-admin/issues/69) : Return 'HTTP_422_UNPROCESSABLE_ENTITY' when form data
  is not valid

### Deprecated

* 'EnumField.from_enum("status", Status)' is deprecated. Use 'EnumField("status", enum=Status)' instead.
* 'EnumField.from_choices("language", [('cpp', 'C++'), ('py', 'Python')])' is deprecated.
  Use 'EnumField("name", choices=[('cpp', 'C++'), ('py', 'Python')])' instead.

## [0.5.5] - 2023-03-06

### Fixed

* Fix [#116](https://github.com/jowilf/starlette-admin/issues/116) : Internal Server Error when login credentials are
  wrong by [@jowilf](https://github.com/jowilf) in [#117](https://github.com/jowilf/starlette-admin/pull/117)

## [0.5.4] - 2023-03-03

### Fixed

* Fix [#99](https://github.com/jowilf/starlette-admin/issues/99) : Show error message when an error occur on 'delete'
  action (detail view).

### Added

* Display meaningfully error message when SQLAlchemyError occur during action execution
  by [@jowilf](https://github.com/jowilf) and [@dolamroth](https://github.com/dolamroth)
  in [#105](https://github.com/jowilf/starlette-admin/pull/105)

## [0.5.3] - 2023-02-25

### Fixed

* Fix Bug with SQLAlchemy column converters by [@jowilf](https://github.com/jowilf)
  in [#103](https://github.com/jowilf/starlette-admin/pull/103)

## [0.5.2] - 2022-12-29

### Fixed

* Fix Bug with 'search_format' params for [DateField][starlette_admin.fields.DateField]
  and [TimeField][starlette_admin.fields.TimeField]
  by [@jowilf](https://github.com/jowilf) & [@ihuro](https://github.com/ihuro)
  in [#68](https://github.com/jowilf/starlette-admin/pull/68) & [#71](https://github.com/jowilf/starlette-admin/pull/71)

## [0.5.1] - 2022-12-27

### Fixed

* Fix Bug with 'sqlalchemy.dialects.postgresql.base.UUID' column by [@jowilf](https://github.com/jowilf)
  in [#65](https://github.com/jowilf/starlette-admin/pull/65)

## [0.5.0] - 2022-12-17

### Added

* Introduce ['AdminUser'][starlette_admin.auth.AuthProvider.get_admin_user] and add navbar to show the
  current ['AdminUser'][starlette_admin.auth.AuthProvider.get_admin_user] information ('username' and 'photo')
  by [@jowilf](https://github.com/jowilf) in [#49](https://github.com/jowilf/starlette-admin/pull/49)

### Internals

* Add auth example by [@jowilf](https://github.com/jowilf) in [#51](https://github.com/jowilf/starlette-admin/pull/51)

## [0.4.0] - 2022-12-07

---

### Added

* Custom batch actions by [@jowilf](https://github.com/jowilf)
  in [#44](https://github.com/jowilf/starlette-admin/pull/44)
* Add 'get_list_query', 'get_count_query' and 'get_search_query' methods to SQLAlchemy backend that can be inherited for
  customization by [@jowilf](https://github.com/jowilf) in [#47](https://github.com/jowilf/starlette-admin/pull/47)

### Internals

* Update datatables to '1.13.1'
* Update Search builder UI to fit tabler design

## [0.3.2] - 2022-12-02

---

### Fixed

* Fix Datatables warning when primary key is not included in 'fields' by [@jowilf](https://github.com/jowilf)
  in [#23](https://github.com/jowilf/starlette-admin/issues/23)

### Docs

* Add spanish translation for 'docs/index.md' by [@rafnixg](https://github.com/rafnixg)
  in [#35](https://github.com/jowilf/starlette-admin/pull/35)

### Internals

* Use Ruff for linting by [@jowilf](https://github.com/jowilf)
  in [#29](https://github.com/jowilf/starlette-admin/pull/29)
* Migrate to Hatch by [@jowilf](https://github.com/jowilf) in [#30](https://github.com/jowilf/starlette-admin/pull/30)
* Setup pre-commit by [@jowilf](https://github.com/jowilf) in [#33](https://github.com/jowilf/starlette-admin/pull/33)
* Add support for Python 3.11 in test suite by [@jowilf](https://github.com/jowilf)
  in [#34](https://github.com/jowilf/starlette-admin/pull/34)

## [0.3.1] - 2022-11-22

---

### Fixed

* Fix Regression on SQLModel backend: Duplicate instances when creating or updating a model with relationships
  in [#23](https://github.com/jowilf/starlette-admin/issues/23)

## [0.3.0] - 2022-11-21

---

### Breaking Changes

* Changes in 'ModelView' definition

=== "Now"

    python
    class Post:
        id: int
        title: str

    admin.add_view(ModelView(Post, icon="fa fa-blog", label = "Blog Posts"))
    

=== "Before"

    python
    class Post:
        id: int
        title: str

    class PostView(ModelView, model=Post):
        icon = "fa fa-blog"
        label = "Blog Posts"

    admin.add_view(PostView)
    

* Changes in 'CustomView' definition

=== "Now"

    python
    admin.add_view(CustomView(label="Home", icon="fa fa-home", path="/home", template_path="home.html"))
    

=== "Before"

    python
    class HomeView(CustomView):
        label = "Home"
        icon = "fa fa-home"
        path = "/home"
        template_path = "home.html"

    admin.add_view(HomeView)
    

* Changes in 'Link' definition

=== "Now"

    python
    admin.add_view(Link(label="Back to Home", icon="fa fa-home", url="/", target = "_blank"))
    

=== "Before"

    python
    class BackToHome(Link):
        label = "Back to Home"
        icon = "fa fa-home"
        url = "/"
        target = "_blank"
    

These changes are inspired from *Flask-admin* and are introduced to help reduce code size and keep it simple.

### Added

* Add 'CollectionField'
* Add 'ListField'
* Add support for [Odmantic](https://art049.github.io/odmantic/)
* Add support for datatables [responsive extensions](https://datatables.net/extensions/responsive/)

!!! usage

    python
    class MyModelView(ModelView):
        responsive_table = True
    

### Changed

* Move 'SQLModel' to it own contrib package
* MongoEngine 'EmbeddedDocumentField' is now converted into 'CollectionField'

### Removed

* Remove PDF from default 'export_types'

## [0.2.2] - 2022-09-20

---

### Fixed

* Null support for EnumField in [#17](https://github.com/jowilf/starlette-admin/pull/17)

## [0.2.1] - 2022-09-19

---

### Fixed

* Fix SearchBuilder not working with dates (SQLAlchemy) in [#15](https://github.com/jowilf/starlette-admin/pull/15)

## [0.2.0] - 2022-09-14

---

### Changed

* Date & Time input now use Flatpickr in [#10](https://github.com/jowilf/starlette-admin/pull/10)

## [0.1.1] - 2022-09-09

---

### Added

- Add 'ColorField' in [#7](https://github.com/jowilf/starlette-admin/pull/7)
- AsyncEngine support for SQLAlchemy in [#8](https://github.com/jowilf/starlette-admin/pull/8)

