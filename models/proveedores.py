from odoo import models, fields, api

class Proveedores(models.Model):
    _name = 'tienda.proveedores'
    id = fields.Char(string='Identificador', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    dni = fields.Char(string='Direccion', required=True)
    telefono = fields.Integer(string='Telefono', required=True)
    anticulo = fields.Many2many('tienda.articulos', string='Articulo')
