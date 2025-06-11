# Estate Property Model

As part of the introduction to Odoo development, the `estate.property` model was created along with is controller for an API: 

- [Estate property](./modules/estate/)


# Odoo Library API Module

This project was created as a learning exercise to explore Odoo's development features, 
particularly the use of models and controllers to build a custom API.

- [Library](./modules/library/)

## Project Overview

The module implements a simple **Library Management System**, including models for:

- Authors
- Books
- Members
- Loans

Once the models were defined, a series of API endpoints were built using **Odoo Controllers**, enabling CRUD operations that were tested with **Postman**.

---

## Features Implemented

### Custom Models

The models that were created:

- `library.author`
- `library.book`
- `library.member`
- `library.loan`

Each model includes logical relationships (e.g., `Many2one`, `One2many`) and business rules to manage data integrity and behavior.

### Decorators Used in Models

To handle computed fields, onchange logic, constraints, and model hooks, the following decorators and methods were used:

```python
@api.depends('loan_ids')
def _compute_loans_count(self):
    for book in self:
        book.loans_count = len(book.loan_ids)

@api.onchange('total_copies')
def _onchange_total_copies(self):
    if self.total_copies and self.copies_available == 0:
        self.copies_available = self.total_copies

@api.constrains('copies_available', 'total_copies')
def _check_copies(self):
    for book in self:
        if book.copies_available > book.total_copies:
            raise ValidationError('Available copies cannot be more than total copies.')

# Note: @api.model is deprecated in the latest versions of Odoo for some use cases
def create(self, vals_list):
    vals_list['created_at'] = fields.Datetime.now()
    vals_list['updated_at'] = fields.Datetime.now()
    return super().create(vals_list)

def write(self, vals):
    vals['updated_at'] = fields.Datetime.now()
    return super().write(vals)
```

# Commands

## Runnig odoo for the first time
```python odoo-bin -r odoo -w 123456789 --addons-path=addons -d odoo -i base```

## Running odoo without initializing the database
```python odoo-bin -r odoo -w 123456789 --addons-path=addons -d odoo```

## Create a new module: scaffold
The first argument after the word scaffold is the module name and the next one is the directory
```python odoo-bin scaffold school modules``` 

## Run odoo when the model has been updated 
```python odoo-bin -r odoo -w 123456789 --addons-path=addons,modules -d odoo -u library```

## Parameters for updating and stablishing the database
This two parameters must always be used together
```-d rd-demo -u library```

## Run odoo when using the odoo.conf file
```python odoo-bin -c odoo.conf -d odoo -i library```

## odoo.conf file structure
This file must be set in the root directory
```
[options]
db_host = localhost
db_port = 5432
db_user = odoo
db_password = 123456789
db_name = odoo
addons_path = modules,addons
admin_passwd = admin
```

## Odoo documentation

- [Odoo orm](https://www.odoo.com/documentation/18.0/developer/reference/backend/orm.html)