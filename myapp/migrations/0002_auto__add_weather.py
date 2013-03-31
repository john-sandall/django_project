# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Weather'
        db.create_table(u'myapp_weather', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('nzmax', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nzmin', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('ukmax', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('ukmin', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nzhistmax', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nzhistmin', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('ukhistmax', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('ukhistmin', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'myapp', ['Weather'])


    def backwards(self, orm):
        # Deleting model 'Weather'
        db.delete_table(u'myapp_weather')


    models = {
        u'myapp.weather': {
            'Meta': {'object_name': 'Weather'},
            'date': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nzhistmax': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'nzhistmin': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'nzmax': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'nzmin': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ukhistmax': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ukhistmin': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ukmax': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ukmin': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['myapp']