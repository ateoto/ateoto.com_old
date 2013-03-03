# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Condition'
        db.create_table(u'character_builder_condition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('effect', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('character_builder', ['Condition'])

        # Adding field 'Character.notes'
        db.add_column(u'character_builder_character', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding M2M table for field conditions on 'Character'
        db.create_table(u'character_builder_character_conditions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('character', models.ForeignKey(orm['character_builder.character'], null=False)),
            ('condition', models.ForeignKey(orm['character_builder.condition'], null=False))
        ))
        db.create_unique(u'character_builder_character_conditions', ['character_id', 'condition_id'])


    def backwards(self, orm):
        # Deleting model 'Condition'
        db.delete_table(u'character_builder_condition')

        # Deleting field 'Character.notes'
        db.delete_column(u'character_builder_character', 'notes')

        # Removing M2M table for field conditions on 'Character'
        db.delete_table('character_builder_character_conditions')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'character_builder.ability': {
            'Meta': {'object_name': 'Ability'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'help_text': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.abilitymod': {
            'Meta': {'object_name': 'AbilityMod', '_ormbases': ['character_builder.Modifier']},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Ability']"}),
            u'modifier_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.Modifier']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.actiontype': {
            'Meta': {'object_name': 'ActionType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.alignment': {
            'Meta': {'object_name': 'Alignment'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'character_builder.armorclass': {
            'Meta': {'object_name': 'ArmorClass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.armoritem': {
            'Meta': {'object_name': 'ArmorItem', '_ormbases': ['character_builder.Item']},
            'armor_modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['character_builder.DefenseMod']"}),
            'armor_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ArmorType']"}),
            u'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'penalties': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Modifier']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'character_builder.armortype': {
            'Meta': {'object_name': 'ArmorType'},
            'armor_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ArmorClass']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.character': {
            'Meta': {'object_name': 'Character'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'alignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Alignment']"}),
            'class_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ClassType']"}),
            'conditions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Condition']", 'symmetrical': 'False', 'blank': 'True'}),
            'deity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Deity']"}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Gender']"}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hit_points': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_hit_points': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Race']"}),
            'slug_name': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'xp': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'character_builder.characterability': {
            'Meta': {'object_name': 'CharacterAbility'},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Ability']"}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'abilities'", 'to': "orm['character_builder.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.characterarmortype': {
            'Meta': {'object_name': 'CharacterArmorType'},
            'armor_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ArmorType']"}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'armor_types'", 'to': "orm['character_builder.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.characterclassfeature': {
            'Meta': {'object_name': 'CharacterClassFeature'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'class_features'", 'to': "orm['character_builder.Character']"}),
            'choice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ClassFeatureChoice']", 'null': 'True', 'blank': 'True'}),
            'class_feature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ClassFeature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.charactercurrency': {
            'Meta': {'object_name': 'CharacterCurrency'},
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wealth'", 'to': "orm['character_builder.Character']"}),
            'currency_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Currency']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.characterequipment': {
            'Meta': {'object_name': 'CharacterEquipment'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equipment'", 'to': "orm['character_builder.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_equipped': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Item']"})
        },
        'character_builder.characterfeat': {
            'Meta': {'object_name': 'CharacterFeat'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feats'", 'to': "orm['character_builder.Character']"}),
            'choice_result': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'feat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Feat']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'required_choice': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'character_builder.characterpower': {
            'Meta': {'object_name': 'CharacterPower'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'powers'", 'to': "orm['character_builder.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'power': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Power']"})
        },
        'character_builder.characterracefeature': {
            'Meta': {'object_name': 'CharacterRaceFeature'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'race_features'", 'to': "orm['character_builder.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race_feature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.RaceFeature']"})
        },
        'character_builder.characterskill': {
            'Meta': {'object_name': 'CharacterSkill'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'to': "orm['character_builder.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_trained': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Skill']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.classfeature': {
            'Meta': {'object_name': 'ClassFeature'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'choices': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.ClassFeatureChoice']", 'symmetrical': 'False', 'blank': 'True'}),
            'class_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.ClassType']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'passive_effects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Modifier']", 'symmetrical': 'False', 'blank': 'True'}),
            'requires_choice': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'character_builder.classfeaturechoice': {
            'Meta': {'object_name': 'ClassFeatureChoice'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'character_builder.classpower': {
            'Meta': {'object_name': 'ClassPower', '_ormbases': ['character_builder.Power']},
            'class_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ClassType']"}),
            u'power_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.Power']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.classskill': {
            'Meta': {'object_name': 'ClassSkill'},
            'class_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'class_skills'", 'to': "orm['character_builder.ClassType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Skill']"})
        },
        'character_builder.classtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ClassType'},
            'armor_proficiencies': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.ArmorType']", 'symmetrical': 'False'}),
            'base_hit_points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'favored_abilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Ability']", 'symmetrical': 'False'}),
            'hit_points_per_level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifiers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Modifier']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Role']"}),
            'role_flavor': ('django.db.models.fields.TextField', [], {}),
            'skill_choices': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Source']"}),
            'trained_skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['character_builder.Skill']", 'null': 'True', 'blank': 'True'}),
            'weapon_proficiencies': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.WeaponProficiencyGroup']", 'symmetrical': 'False'})
        },
        'character_builder.classtypedefmod': {
            'Meta': {'object_name': 'ClassTypeDefMod'},
            'bonus': ('django.db.models.fields.IntegerField', [], {}),
            'class_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ClassType']"}),
            'defense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Defense']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.condition': {
            'Meta': {'object_name': 'Condition'},
            'effect': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'character_builder.currency': {
            'Meta': {'object_name': 'Currency'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'})
        },
        'character_builder.currencyexchange': {
            'Meta': {'object_name': 'CurrencyExchange'},
            'currency_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['character_builder.Currency']"}),
            'currency_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['character_builder.Currency']"}),
            'exchange_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '9'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.defense': {
            'Meta': {'object_name': 'Defense'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'abilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Ability']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'character_builder.defensemod': {
            'Meta': {'object_name': 'DefenseMod', '_ormbases': ['character_builder.Modifier']},
            'defense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Defense']"}),
            u'modifier_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.Modifier']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.deity': {
            'Meta': {'object_name': 'Deity'},
            'alignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Alignment']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'character_builder.feat': {
            'Meta': {'object_name': 'Feat'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'can_retake': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'choices': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.FeatChoice']", 'symmetrical': 'False', 'blank': 'True'}),
            'has_passive_effects': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'passive_effects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Modifier']", 'symmetrical': 'False', 'blank': 'True'}),
            'requires_choice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'special': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'character_builder.featabilityprereq': {
            'Meta': {'object_name': 'FeatAbilityPrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Ability']"}),
            u'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.featarmororarmorprereq': {
            'Meta': {'object_name': 'FeatArmorOrArmorPrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'allowed_armors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.ArmorType']", 'symmetrical': 'False'}),
            u'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.featarmortypeprereq': {
            'Meta': {'object_name': 'FeatArmorTypePrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'armor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ArmorType']"}),
            u'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.featchoice': {
            'Meta': {'object_name': 'FeatChoice'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.featclassfeatureprereq': {
            'Meta': {'object_name': 'FeatClassFeaturePrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'classfeature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ClassFeature']"}),
            u'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.featclasstypeprereq': {
            'Meta': {'object_name': 'FeatClassTypePrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'class_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ClassType']"}),
            u'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.featdeityprereq': {
            'Meta': {'object_name': 'FeatDeityPrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'deity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Deity']"}),
            u'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.featfeatprereq': {
            'Meta': {'object_name': 'FeatFeatPrereq', '_ormbases': ['character_builder.FeatPrereq']},
            u'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'}),
            'pre_feat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Feat']"})
        },
        'character_builder.featpower': {
            'Meta': {'object_name': 'FeatPower', '_ormbases': ['character_builder.Power']},
            'feat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Feat']"}),
            u'power_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.Power']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.featprereq': {
            'Meta': {'object_name': 'FeatPrereq'},
            'feat': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prereqs'", 'to': "orm['character_builder.Feat']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.featraceprereq': {
            'Meta': {'object_name': 'FeatRacePrereq', '_ormbases': ['character_builder.FeatPrereq']},
            u'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Race']"})
        },
        'character_builder.featskillorskillprereq': {
            'Meta': {'object_name': 'FeatSkillOrSkillPrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'allowed_skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Skill']", 'symmetrical': 'False'}),
            u'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.featskillprereq': {
            'Meta': {'object_name': 'FeatSkillPrereq', '_ormbases': ['character_builder.FeatPrereq']},
            u'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Skill']"})
        },
        'character_builder.gender': {
            'Meta': {'object_name': 'Gender'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'character_builder.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Price']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Source']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'script': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.level': {
            'Meta': {'object_name': 'Level'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'xp_required': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.modifier': {
            'Meta': {'object_name': 'Modifier'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.power': {
            'Meta': {'object_name': 'Power'},
            'action_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ActionType']"}),
            'attack': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'effect': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'flavor': ('django.db.models.fields.TextField', [], {}),
            'hit': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hit_modifier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Ability']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.PowerKeyword']", 'symmetrical': 'False'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'miss': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'power_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.PowerType']"}),
            'range_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'range_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.PowerRange']"}),
            'requirement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'secondary_attack': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'secondary_hit': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'secondary_hit_modifier': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'secondary_hit_modifier'", 'null': 'True', 'to': "orm['character_builder.Ability']"}),
            'secondary_target': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'special': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sustain': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sustain_action': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sustain_action'", 'null': 'True', 'to': "orm['character_builder.ActionType']"}),
            'target': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'usage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.PowerUsage']"})
        },
        'character_builder.powerkeyword': {
            'Meta': {'object_name': 'PowerKeyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.powerrange': {
            'Meta': {'object_name': 'PowerRange'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.powertype': {
            'Meta': {'object_name': 'PowerType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.powerusage': {
            'Meta': {'object_name': 'PowerUsage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.price': {
            'Meta': {'object_name': 'Price'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Currency']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.race': {
            'Meta': {'ordering': "['name']", 'object_name': 'Race'},
            'average_height_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'average_weight_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Language']", 'symmetrical': 'False'}),
            'modifiers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Modifier']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'playable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Size']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Source']"}),
            'speed': ('django.db.models.fields.IntegerField', [], {}),
            'vision': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Vision']"})
        },
        'character_builder.raceabilitymod': {
            'Meta': {'object_name': 'RaceAbilityMod'},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Ability']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.IntegerField', [], {}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ability_mods'", 'to': "orm['character_builder.Race']"})
        },
        'character_builder.racefeature': {
            'Meta': {'object_name': 'RaceFeature'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'choices': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.RaceFeatureChoice']", 'symmetrical': 'False', 'blank': 'True'}),
            'has_passive_effects': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'passive_effects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Modifier']", 'symmetrical': 'False', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Race']"}),
            'requires_choice': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'character_builder.racefeaturechoice': {
            'Meta': {'object_name': 'RaceFeatureChoice'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'character_builder.raceskillmod': {
            'Meta': {'object_name': 'RaceSkillMod'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.IntegerField', [], {}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skill_mods'", 'to': "orm['character_builder.Race']"}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Skill']"})
        },
        'character_builder.racialpower': {
            'Meta': {'object_name': 'RacialPower', '_ormbases': ['character_builder.Power']},
            u'power_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.Power']", 'unique': 'True', 'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Race']"})
        },
        'character_builder.role': {
            'Meta': {'object_name': 'Role'},
            'flavor': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.size': {
            'Meta': {'object_name': 'Size'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'reach': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'space': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.skill': {
            'Meta': {'object_name': 'Skill'},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Ability']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.skillmod': {
            'Meta': {'object_name': 'SkillMod', '_ormbases': ['character_builder.Modifier']},
            u'modifier_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.Modifier']", 'unique': 'True', 'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Skill']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.source': {
            'Meta': {'ordering': "['name']", 'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.speedmod': {
            'Meta': {'object_name': 'SpeedMod', '_ormbases': ['character_builder.Modifier']},
            u'modifier_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.Modifier']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.vision': {
            'Meta': {'object_name': 'Vision'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.weaponcategory': {
            'Meta': {'object_name': 'WeaponCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.weapongroup': {
            'Meta': {'object_name': 'WeaponGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.weaponproficiencygroup': {
            'Meta': {'object_name': 'WeaponProficiencyGroup'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.WeaponCategory']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.weapontype': {
            'Meta': {'object_name': 'WeaponType'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.WeaponCategory']"}),
            'damage': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.WeaponGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'proficiency': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'properties': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'weapon_range': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['character_builder']