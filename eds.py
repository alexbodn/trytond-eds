# -*- coding: utf-8 -*-
"""
    eds.py

    :copyright: (c) 2017 by Alex Bodnaru
    :license: see LICENSE for more details.
"""
from trytond.model import ModelView, ModelSQL, fields, Unique, Check
from trytond.ir import Model, ModelField


class EDSSource(ModelSQL, ModelView):
    "EDSSource"
    __name__ = 'eds.source'
    name = fields.Char('Name', required=True)
    description = fields.Char('Description', required=True)
    models = fields.One2Many('eds.model', 'source', 'EDSModel')


class EDSModelActions(ModelSQL, ModelView):
    'EDSModelActions'
    __name__ = 'eds.model.actions'

    name = fields.Char('Name', required=True)

    on_source_create = fields.Char('On Source Create', required=False)
    on_source_update = fields.Char('On Source Update', required=False)
    on_source_delete = fields.Char('On Source Delete', required=False)


class EDSModel(ModelSQL, ModelView):
    'EDSModel'
    __name__ = 'eds.model'
    source = fields.Many2One('eds.eds', 'EDSSource', ondelete='RESTRICT',)
    model = fields.Many2One('ir.model', 'Model', ondelete='RESTRICT',)
    fields = fields.One2Many('eds.model.field', 'model', 'EDSField')
    action_class = fields.Many2One(
        'eds.model.actions', 'EDSModelActions', ondelete='RESTRICT',)


class EDSModelField(ModelSQL, ModelView):
    'EDSModelField'
    __name__ = 'eds.model.field'
    model = fields.Many2One('eds.model', 'EDSModel', ondelete='CASCADE',)
    field = fields.Many2One('ir.model.field', 'ModelField', ondelete='CASCADE',)
    eds_query = fields.Char('EDS Query', required=True)
    action_class = fields.Many2One(
        'eds.model.actions', 'EDSModelActions', ondelete='RESTRICT',)


class EDSRelation(ModelSQL, ModelView):
    'EDSRelation'
    __name__ = 'eds.relation'
    model = fields.Many2One('eds.model', 'EDSModel', ondelete='CASCADE',)
    tryton_id = fields.Integer('ID', readonly=True)
    eds_query = fields.Char('EDS Query', required=False)


class EDSSyncLog(ModelSQL, ModelView):
    'EDSSyncLog'
    __name__ = 'eds.sync.log'
    relation = fields.Many2One(
        'eds.relation', 'EDSRelation', ondelete='CASCADE',)
    timestamp = fields.DateTime('Timestamp', required=True)
    action = fields.Char('Action', required=True)

