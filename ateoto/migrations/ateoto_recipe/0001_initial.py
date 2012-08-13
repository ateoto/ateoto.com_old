# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ingredient'
        db.create_table('ateoto_recipe_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('ateoto_recipe', ['Ingredient'])

        # Adding model 'IngredientLine'
        db.create_table('ateoto_recipe_ingredientline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ateoto_recipe.Ingredient'])),
            ('quantity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('preparation', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('ateoto_recipe', ['IngredientLine'])


    def backwards(self, orm):
        # Deleting model 'Ingredient'
        db.delete_table('ateoto_recipe_ingredient')

        # Deleting model 'IngredientLine'
        db.delete_table('ateoto_recipe_ingredientline')


    models = {
        'ateoto_recipe.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'ateoto_recipe.ingredientline': {
            'Meta': {'object_name': 'IngredientLine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ateoto_recipe.Ingredient']"}),
            'preparation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'quantity': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['ateoto_recipe']