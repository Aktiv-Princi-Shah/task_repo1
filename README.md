# task_repo1
----------------------------------
# -*- coding: utf-8 -*-

# Technical Implementation: One2many Relationship Between Library and Books
# Author: Your Name
# Website: https://www.aktivsoftware.com

# __manifest__.py
{
    "name": "Library One2Many Management",
    "version": "18.0.1.0.0",
    "author": "Your Name",
    "website": "https://www.aktivsoftware.com",
    "category": "Tools",
    "depends": ["base", "web"],
    "data": [
        "views/library_views.xml",
        "views/menu_views.xml",
        "security/ir.model.access.csv"
    ],
    "installable": True,
    "application": True,
    "auto_install": False
}

# models/__init__.py
# -*- coding: utf-8 -*-

from . import library
from . import book


# models/library.py
# -*- coding: utf-8 -*-

from odoo import models, fields

class Library(models.Model):
    """
    Library model holds information about a physical library.
    One library can have multiple books (One2Many relationship).
    """
    _name = 'library.library'
    _description = 'Library'

    name = fields.Char(string='Library Name', required=True)
    location = fields.Char(string='Location')
    capacity = fields.Integer(string='Capacity (Number of People)')
    notes = fields.Text(string='Additional Notes')

    # One2Many: One Library has many Books
    book_ids = fields.One2many(
        comodel_name='library.book',     # Related model
        inverse_name='library_id',       # Field in the related model
        string='Books in Library'        # Label
    )


# models/book.py
# -*- coding: utf-8 -*-

from odoo import models, fields

class Book(models.Model):
    """
    Book model stores details of each book.
    Each book belongs to one library (Many2One relationship).
    """
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Book Title', required=True)
    author = fields.Char(string='Author')
    isbn = fields.Char(string='ISBN Number')
    state = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed')
    ], string='Status', default='available')

    # Many2One: Many Books belong to One Library
    library_id = fields.Many2one(
        comodel_name='library.library',  # Parent model
        string='Library'
    )


# views/library_views.xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Form View for Library with Notebook Tab for Books -->
    <record id="view_library_form" model="ir.ui.view">
        <field name="name">library.library.form</field>
        <field name="model">library.library</field>
        <field name="arch" type="xml">
            <form string="Library">
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="location"/>
                        <field name="capacity"/>
                        <field name="notes"/>
                    </group>
                    <notebook>
                        <page string="Books">
                            <!-- Show all related books in a One2many tab -->
                            <field name="book_ids">
                                <tree editable="bottom">
                                    <field name="name"/>
                                    <field name="author"/>
                                    <field name="isbn"/>
                                    <field name="state"/>
                                </tree>
                            </field>
                        </page>
                    </notebook>
                </sheet>
            </form>
        </field>
    </record>

    <!-- Tree View for Libraries -->
    <record id="view_library_tree" model="ir.ui.view">
        <field name="name">library.library.tree</field>
        <field name="model">library.library</field>
        <field name="arch" type="xml">
            <tree>
                <field name="name"/>
                <field name="location"/>
                <field name="capacity"/>
            </tree>
        </field>
    </record>

    <!-- Tree View for Books -->
    <record id="view_book_tree" model="ir.ui.view">
        <field name="name">library.book.tree</field>
        <field name="model">library.book</field>
        <field name="arch" type="xml">
            <tree>
                <field name="name"/>
                <field name="author"/>
                <field name="isbn"/>
                <field name="library_id"/>
            </tree>
        </field>
    </record>

    <!-- Form View for Books -->
    <record id="view_book_form" model="ir.ui.view">
        <field name="name">library.book.form</field>
        <field name="model">library.book</field>
        <field name="arch" type="xml">
            <form string="Book">
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="author"/>
                        <field name="isbn"/>
                        <field name="state"/>
                        <field name="library_id"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>
</odoo>


# views/menu_views.xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Main Menu for Library -->
    <menuitem id="menu_main_library" name="Library" sequence="10"/>

    <!-- Submenu for Libraries -->
    <menuitem id="menu_libraries" name="Libraries" parent="menu_main_library"/>
    <act_window id="action_library"
                name="Libraries"
                res_model="library.library"
                view_mode="tree,form"
                menu_id="menu_libraries"/>

    <!-- Submenu for Books -->
    <menuitem id="menu_books" name="Books" parent="menu_main_library"/>
    <act_window id="action_books"
                name="Books"
                res_model="library.book"
                view_mode="tree,form"
                menu_id="menu_books"/>
</odoo>


# security/ir.model.access.csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_library_model,library.library,model_library_library,base.group_user,1,1,1,1
access_book_model,library.book,model_library_book,base.group_user,1,1,1,1


# Summary for Non-Coders:
# - One2many means: one library has many books.
# - You create a library, then inside it you can add books in a tab.
# - Each book is automatically linked to the library.
# - You can view all books directly too from the menu.
# - Each view lets you create, read, update, or delete records.
# - Code is structured so even beginners can follow.

# 🎯 Test Steps:
# 1. Go to "Library" Menu → Libraries → Create
# 2. Fill library details and add books in the "Books" tab
# 3. Go to "Books" menu and confirm linkage
# ✅ One2Many setup is complete.
