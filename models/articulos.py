from odoo import models, fields, api

class Articulos(models.Model):
    _name = 'tienda.articulos'
    codigo = fields.Char(string='Codigo', required=True)
    marca = fields.Char(string='Marca', required=True)
    descripcion = fields.Char(string='Descripcion', required=True)
    stock = fields.Integer(string='Stock', required=True)
    precio = fields.Integer(string='Precio', required=True)

