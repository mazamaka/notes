---
title: "SQLAdmin -- документация"
description: "Административный интерфейс для SQLAlchemy моделей в Starlette/FastAPI приложениях"
source: "https://aminalaee.github.io/sqladmin/"
---

# SQLAdmin

SQLAlchemy Admin for Starlette/FastAPI

SQLAdmin is a flexible Admin interface for SQLAlchemy models.

Main features include:

- SQLAlchemy sync/async engines
- Starlette integration
- FastAPI integration
- WTForms form building
- SQLModel support
- UI using Tabler

Documentation: https://aminalaee.github.io/sqladmin

Source Code: https://github.com/aminalaee/sqladmin

## Installation

```bash
$ pip install sqladmin
$ pip install sqladmin[full]
```

## Quickstart

Let's define an example SQLAlchemy model:

```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base


Base = declarative_base()
engine = create_engine(
    "sqlite:///example.db",
    connect_args={"check_same_thread": False},
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)


Base.metadata.create_all(engine)  # Create tables
```

If you want to use SQLAdmin with FastAPI:

```python
from fastapi import FastAPI
from sqladmin import Admin, ModelView


app = FastAPI()
admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name]


admin.add_view(UserAdmin)
```

Or if you want to use SQLAdmin with Starlette:

```python
from sqladmin import Admin, ModelView
from starlette.applications import Starlette


app = Starlette()
admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name]


admin.add_view(UserAdmin)
```

Now visiting /admin on your browser you can see the SQLAdmin interface.

## Related projects and inspirations

- Flask-Admin Admin interface for Flask supporting different database backends and ORMs. This project has inspired SQLAdmin extensively and most of the features and configurations are implemented the same.
- FastAPI-Admin Admin interface for FastAPI which works with TortoiseORM.
- Dashboard Admin interface for ASGI frameworks which works with the orm package.

## Configurations

SQLAdmin configuration options are heavily inspired by the Flask-Admin project.

This page will give you a basic introduction and for all the details you can visit API Reference.

Let's say you've defined your SQLAlchemy models like this:

```python
from sqlalchemy import Column, Boolean, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()
engine = create_engine(
    "sqlite:///example.db",
    connect_args={"check_same_thread": False},
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    address = relationship("Address", uselist=False, back_populates="user")

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    user = relationship("User", back_populates="address")
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(Integer)
    is_admin = Column(Boolean, default=False)


Base.metadata.create_all(engine)  # Create tables
```

If you want to integrate SQLAdmin into FastAPI application:

```python
from fastapi import FastAPI
from sqladmin import Admin, ModelView


app = FastAPI()
admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name]


admin.add_view(UserAdmin)
```

As you can see the UserAdmin class inherits from ModelView and accepts some configurations.

### Permissions

You can configure a few general permissions for this model. The following options are available:

- `can_create`: If the model can create new instances via SQLAdmin. Default value is True.
- `can_edit`: If the model instances can be edited via SQLAdmin. Default value is True.
- `can_delete`: If the model instances can be deleted via SQLAdmin. Default value is True.
- `can_view_details`: If the model instance details can be viewed via SQLAdmin. Default value is True.
- `can_export`: If the model data can be exported in the list page. Default value is True.

Example:

```python
class UserAdmin(ModelView, model=User):
    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True
```

### Metadata

The metadata for the model. The options are:

- `name`: Display name for this model. Default value is the class name.
- `name_plural`: Display plural name for this model. Default value is class name + s.
- `icon`: Icon to be displayed for this model in the admin. Only FontAwesome and Tabler names are supported.
- `category`: Category name to display group of ModelView classes together in dropdown.
- `category_icon`: Category icon to display.

Example:

```python
class UserAdmin(ModelView, model=User):
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"
    category = "accounts"
    category_icon = "fa-solid fa-user"
```

### List page

These options allow configurations in the list page, in the case of this example where you can view list of User records.

The options available are:

- `column_list`: List of columns or column names to be displayed in the list page.
- `column_exclude_list`: List of columns or column names to be excluded in the list page.
- `column_formatters`: Dictionary of column formatters in the list page.
- `column_searchable_list`: List of columns or column names to be searchable in the list page.
- `column_sortable_list`: List of columns or column names to be sortable in the list page.
- `column_default_sort`: Default sorting if no sorting is applied, tuple of (column, is_descending) or list of the tuple for multiple columns.
- `list_query`: A method with the signature of (request) -> stmt which can customize the list query.
- `count_query`: A method with the signature of (request) -> stmt which can customize the count query.
- `search_query`: A method with the signature of (stmt, term) -> stmt which can customize the search query.
- `column_filters`: A list of objects that implement the ColumnFilter protocol to be displayed in the list page.
- `details_query`: A method with the signature of (request) -> stmt which can customize the details query.

Example:

```python
class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name, "address.zip_code"]
    column_searchable_list = [User.name]
    column_sortable_list = [User.id]
    column_formatters = {User.name: lambda m, a: m.name[:10]}
    column_default_sort = [(User.email, True), (User.name, False)]
    column_filterable_list = [User.is_admin]
```

> **Tip:** You can use the special keyword `"__all__"` in column_list or column_details_list if you don't want to specify all the columns manually. For example: `column_list = "__all__"`

### ColumnFilter

A ColumnFilter is a class that defines a filter for a column. A few standard filters are implemented in the `sqladmin.filters` module.

```python
class IsAdminFilter:
    title = "Is Admin"
    parameter_name = "is_admin"

    def lookups(self, request, model, run_query) -> list[tuple[str, str]]:
        return [
            ("all", "All"),
            ("true", "Yes"),
            ("false", "No"),
        ]

    def get_filtered_query(self, query, value, model):
        if value == "true":
            return query.filter(model.is_admin == True)
        elif value == "false":
            return query.filter(model.is_admin == False)
        else:
            return query
```

### Built in Column Filters

- `BooleanFilter` - A filter for boolean columns, with the values of Yes (true) and No (false)
- `AllUniqueStringValuesFilter` - A filter for string columns, with the values of all unique values in the column
- `StaticValuesFilter` - A filter for string columns, with the values of a static list of values.
- `ForeignKeyFilter` - A filter for foreign key columns, with the values of all unique values in the foreign key column.
- `OperationColumnFilter` - A flexible filter that automatically detects column types and provides appropriate operations.

Example:

```python
from sqladmin.filters import BooleanFilter, AllUniqueStringValuesFilter, ForeignKeyFilter, OperationColumnFilter

class UserAdmin(ModelView, model=User):
    column_list = ["id", "name", "email", "is_admin", "age"]
    column_filters = [
        BooleanFilter(User.is_admin),
        AllUniqueStringValuesFilter(User.name),
        ForeignKeyFilter(User.site_id, Site.name, title="Site"),
        OperationColumnFilter(User.email),
        OperationColumnFilter(User.age),
    ]
```

`OperationColumnFilter` automatically detects the column type and provides appropriate filtering operations:

- String columns: Contains, Equals, Starts with, Ends with
- Numeric columns: Equals, Greater than, Less than
- UUID columns (SQLAlchemy 2.0+): Contains, Equals, Starts with

### Details page

The options available are:

- `column_details_list`: List of columns or column names to be displayed in the details page.
- `column_details_exclude_list`: List of columns or column names to be excluded in the details page.
- `column_formatters_detail`: Dictionary of column formatters in the details page.

Example:

```python
class UserAdmin(ModelView, model=User):
    column_details_list = [User.id, User.name, "address.zip_code"]
    column_formatters_detail = {User.name: lambda m, a: m.name[:10]}
```

### Pagination options

- `page_size`: Default page size in pagination. Default is 10.
- `page_size_options`: Pagination selector options. Default is [10, 25, 50, 100].

```python
class UserAdmin(ModelView, model=User):
    page_size = 50
    page_size_options = [25, 50, 100, 200]
```

### General options

- `column_labels`: A mapping of column labels.
- `column_type_formatters`: A mapping of type keys and callable values to format in all places.
- `save_as`: A boolean to enable "save as new" option when editing an object.
- `save_as_continue`: A boolean to control the redirect URL if save_as is enabled.

```python
class UserAdmin(ModelView, model=User):
    def date_format(value):
        return value.strftime("%d.%m.%Y")

    column_labels = {User.mail: "Email"}
    column_type_formatters = dict(ModelView.column_type_formatters, date=date_format)
    save_as = True
```

### Form options

SQLAdmin allows customizing how forms work with your models. The forms are based on WTForms package and include the following options:

- `form`: Default form to be used for creating or editing the model.
- `form_base_class`: Default base class for creating forms. Default value is `wtforms.Form`.
- `form_args`: Dictionary of form field arguments supported by WTForms.
- `form_widget_args`: Dictionary of form widget rendering arguments.
- `form_columns`: List of model columns to be included in the form.
- `form_excluded_columns`: List of model columns to be excluded from the form.
- `form_overrides`: Dictionary of form fields to override.
- `form_include_pk`: Control if primary key column should be included. Default is False.
- `form_ajax_refs`: Use Ajax with Select2 for loading relationship models async.
- `form_converter`: Allow adding custom converters.
- `form_edit_query`: A method with the signature of (request) -> stmt which can customize the edit form data.
- `form_rules`: List of form rules to manage rendering and behaviour of form.
- `form_create_rules`: List of form rules for create page.
- `form_edit_rules`: List of form rules for edit page.

Example:

```python
class UserAdmin(ModelView, model=User):
    form_columns = [User.name]
    form_args = dict(name=dict(label="Full name"))
    form_widget_args = dict(email=dict(readonly=True))
    form_overrides = dict(email=wtforms.EmailField)
    form_include_pk = True
    form_ajax_refs = {
        "address": {
            "fields": ("zip_code", "street"),
            "order_by": ("id",),
        }
    }
    form_create_rules = ["name", "password"]
    form_edit_rules = ["name"]
```

### Export options

- `can_export`: If the model can be exported. Default value is True.
- `column_export_list`: List of columns to include in the export data.
- `column_export_exclude_list`: List of columns to exclude in the export data.
- `export_max_rows`: Maximum number of rows to be exported. Default value is 0 (unlimited).
- `export_types`: List of export types. Default value is `["csv","json"]`.

### Templates

- `list_template`: Template to use for models list page. Default is `sqladmin/list.html`.
- `create_template`: Template to use for model creation page. Default is `sqladmin/create.html`.
- `details_template`: Template to use for model details page. Default is `sqladmin/details.html`.
- `edit_template`: Template to use for model edit page. Default is `sqladmin/edit.html`.

### Events

There are four methods you can override:

- `on_model_change`: Called before a model was created or updated.
- `after_model_change`: Called after a model was created or updated.
- `on_model_delete`: Called before a model was deleted.
- `after_model_delete`: Called after a model was deleted.

```python
class UserAdmin(ModelView, model=User):
    async def on_model_change(self, data, model, is_created, request):
        ...

    async def on_model_delete(self, model, request):
        ...
```

### Custom Action

```python
from sqladmin import BaseView, action
from starlette.responses import RedirectResponse

class UserAdmin(ModelView, model=User):
    @action(
        name="approve_users",
        label="Approve",
        confirmation_message="Are you sure?",
        add_in_detail=True,
        add_in_list=True,
    )
    async def approve_users(self, request: Request):
        pks = request.query_params.get("pks", "").split(",")
        if pks:
            for pk in pks:
                model: User = await self.get_object_for_edit(pk)
                ...

        referer = request.headers.get("Referer")
        if referer:
            return RedirectResponse(referer)
        else:
            return RedirectResponse(request.url_for("admin:list", identity=self.identity))

admin.add_view(UserAdmin)
```

The available options for action are:

- `name`: A string name to be used in URL for this action.
- `label`: A string for describing this action.
- `add_in_list`: A boolean indicating if this action should be available in list page.
- `add_in_detail`: A boolean indicating if this action should be available in detail page.
- `confirmation_message`: A string message for confirmation modal.

## Authentication

SQLAdmin provides an optional `AuthenticationBackend`.

The class has three methods you need to override:

- `authenticate`: Will be called for validating each incoming request.
- `login`: Will be called only in the login page to validate username/password.
- `logout`: Will be called only for the logout.

```python
from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]
        request.session.update({"token": "..."})
        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        if not token:
            return False
        return True


authentication_backend = AdminAuth(secret_key="...")
admin = Admin(app=..., authentication_backend=authentication_backend)
```

> **Note:** In order to use AuthenticationBackend you need to install the `itsdangerous` package.

### Permissions (is_visible / is_accessible)

```python
class UserAdmin(ModelView, model=User):
    def is_accessible(self, request: Request) -> bool:
        return True

    def is_visible(self, request: Request) -> bool:
        return True
```

## Working with Templates

Since Jinja2 is modular, you can override your specific template file:

```html
{% extends "sqladmin/details.html" %}
{% block content %}
    {{ super() }}
    <p>Custom HTML</p>
{% endblock %}
```

```python
class UserAdmin(ModelView, model=User):
    details_template = "custom_details.html"
```

### Adding filters

```python
def datetime_format(value, format="%H:%M %d-%m-%y"):
    return value.strftime(format)

admin.templates.env.filters["datetime_format"] = datetime_format
```

### Adding globals

```python
def value_is_filepath(value: Any) -> bool:
    return isinstance(value, str) and os.path.isfile(value)

admin.templates.env.globals["value_is_filepath"] = value_is_filepath
```

## Working with Custom Views

```python
from sqladmin import BaseView, expose

class ReportView(BaseView):
    name = "Report Page"
    icon = "fa-solid fa-chart-line"

    @expose("/report", methods=["GET"])
    async def report_page(self, request):
        return await self.templates.TemplateResponse(request, "report.html")

admin.add_view(ReportView)
```

### Database access

```python
from sqlalchemy import select, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

Session = sessionmaker(bind=engine, class_=AsyncSession)

class ReportView(BaseView):
    name = "Report Page"
    icon = "fa-solid fa-chart-line"

    @expose("/report", methods=["GET"])
    async def report_page(self, request):
        async with Session(expire_on_commit=False) as session:
            stmt = select(func.count(User.id))
            result = await session.execute(stmt)
            users_count = result.scalar_one()

        return await self.templates.TemplateResponse(
            request,
            "report.html",
            context={"users_count": users_count},
        )

admin.add_view(ReportView)
```

## Working with Files and Images

Use `fastapi-storages` package:

```python
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType

storage = FileSystemStorage(path="/tmp")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    file = Column(FileType(storage=storage))
```

## Model Converters

```python
from sqladmin import ModelConverter

class CustomModelConverter(ModelConverter):
    @converts("JSON", "JSONB")
    def conv_json(self, model, prop, kwargs):
        return CustomJSONField(**kwargs)

class BaseAdmin(ModelView):
    form_converter = CustomModelConverter
```

## Deployment with HTTPS

For Uvicorn behind reverse proxy:

```bash
uvicorn <module>:<app> --forwarded-allow-ips='*' --proxy-headers
```

## Optimize relationship loading

### Using form_ajax_refs

```python
class ParentAdmin(ModelView, model=Parent):
    form_ajax_refs = {
        "children": {
            "fields": ("id",),
            "order_by": "id",
        }
    }
```

### Using form_excluded_columns

```python
class ParentAdmin(ModelView, model=Parent):
    form_excluded_columns = [Parent.children]
```

## Display custom attributes

```python
class User(Base):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True)
    first_name = mapped_column(String)
    last_name = mapped_column(String)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

class UserAdmin(ModelView, model=User):
    column_list = [User.id, "full_name"]
    column_details_list = [User.id, "full_name"]
```

## Using a request object

```python
class PostAdmin(ModelView, model=Post):
    async def insert_model(self, request, data):
        data["author_id"] = request.user.id
        return await super().insert_model(request, data)
```

## Multiple databases

```python
Session = sessionmaker()
Session.configure(binds={User: engine1, Account: engine2})

admin = Admin(app=app, session_maker=Session)
```

## Working with Passwords

```python
class UserAdmin(ModelView, model=User):
    column_labels = {"hashed_password": "password"}
    form_create_rules = ["name", "hashed_password"]
    form_edit_rules = ["name"]

    async def on_model_change(self, data, model, is_created, request) -> None:
        if is_created:
            data["hashed_password"] = data["hashed_password"] + "_hashed"
```

## API Reference

### Admin

```python
Admin(
    app,
    engine=None,
    session_maker=None,
    base_url='/admin',
    title='Admin',
    logo_url=None,
    favicon_url=None,
    middlewares=None,
    debug=False,
    templates_dir='templates',
    authentication_backend=None
)
```

### ModelView class-attributes

| Attribute | Default | Description |
|-----------|---------|-------------|
| `can_create` | True | Permission for creating new Models |
| `can_edit` | True | Permission for editing Models |
| `can_delete` | True | Permission for deleting Models |
| `can_view_details` | True | Permission for viewing details |
| `can_export` | True | Permission for exporting lists |
| `column_list` | [] | Columns to display in List page |
| `column_exclude_list` | [] | Columns to exclude in List page |
| `column_details_list` | [] | Columns to display in Detail page |
| `column_details_exclude_list` | [] | Columns to exclude in Detail page |
| `page_size` | 10 | Default pagination size |
| `page_size_options` | [10, 25, 50, 100] | Pagination choices |
| `column_searchable_list` | [] | Searchable columns |
| `column_sortable_list` | [] | Sortable columns |
| `column_default_sort` | [] | Default sort column |
| `form` | None | Custom form class |
| `form_columns` | [] | Columns in the form |
| `form_excluded_columns` | [] | Columns excluded from form |
| `form_include_pk` | False | Include PK in form |
| `form_ajax_refs` | {} | Ajax refs for relationships |
| `export_types` | ['csv', 'json'] | Export filetypes |
| `export_max_rows` | 0 | Max export rows (0=unlimited) |
| `save_as` | False | Enable "save as new" |
| `save_as_continue` | True | Redirect after save_as |

### ModelView methods

| Method | Description |
|--------|-------------|
| `on_model_change(data, model, is_created, request)` | Before create/update |
| `after_model_change(data, model, is_created, request)` | After create/update |
| `on_model_delete(model, request)` | Before delete |
| `after_model_delete(model, request)` | After delete |
| `list_query(request)` | Customize list query |
| `count_query(request)` | Customize count query |
| `search_query(stmt, term)` | Customize search query |
| `sort_query(stmt, request)` | Customize sort query |
| `details_query(request)` | Customize details query |
| `form_edit_query(request)` | Customize edit form data |
| `insert_model(request, data)` | Custom create logic |
| `update_model(request, pk, data)` | Custom update logic |
| `delete_model(request, pk)` | Custom delete logic |

### BaseView

```python
from sqladmin import BaseView, expose

class CustomAdmin(BaseView):
    name = "Custom Page"
    icon = "fa-solid fa-chart-line"

    @expose("/custom", methods=["GET"])
    async def test_page(self, request: Request):
        return await self.templates.TemplateResponse(request, "custom.html")

admin.add_base_view(CustomAdmin)
```

### AuthenticationBackend

```python
from sqladmin.authentication import AuthenticationBackend

class AdminAuth(AuthenticationBackend):
    async def authenticate(self, request) -> bool: ...
    async def login(self, request) -> bool: ...
    async def logout(self, request) -> bool: ...
```
