from odoo import models, fields, api

class Clientes(models.Model):
    _name = 'tienda.clientes'
    id = fields.Char(string='Identificador', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    dni = fields.Char(string='DNI', required=True)
    poblacion = fields.Char(string='Poblacion')
    direccion = fields.Char(string='Direccion')
    articulo = fields.Many2many('tienda.articulos', string='Articulo')
