# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EncounterParticipant.notes'
        db.add_column(u'dm_encounterparticipant', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'Encounter.party'
        db.delete_column(u'dm_encounter', 'party_id')

        # Adding field 'Encounter.campaign'
        db.add_column(u'dm_encounter', 'campaign',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['dm.Campaign']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EncounterParticipant.notes'
        db.delete_column(u'dm_encounterparticipant', 'notes')

        # Adding field 'Encounter.party'
        db.add_column(u'dm_encounter', 'party',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['dm.Party']),
                      keep_default=False)

        # Deleting field 'Encounter.campaign'
        db.delete_column(u'dm_encounter', 'campaign_id')


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
        'character_builder.condition': {
            'Meta': {'object_name': 'Condition'},
            'effect': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'character_builder.defense': {
            'Meta': {'object_name': 'Defense'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'abilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Ability']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'character_builder.deity': {
            'Meta': {'object_name': 'Deity'},
            'alignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Alignment']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'character_builder.gender': {
            'Meta': {'object_name': 'Gender'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'character_builder.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'script': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.modifier': {
            'Meta': {'object_name': 'Modifier'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
        'character_builder.powerusage': {
            'Meta': {'object_name': 'PowerUsage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        'character_builder.source': {
            'Meta': {'ordering': "['name']", 'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        'character_builder.weaponproficiencygroup': {
            'Meta': {'object_name': 'WeaponProficiencyGroup'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.WeaponCategory']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dm.basicstorynpc': {
            'Meta': {'object_name': 'BasicStoryNPC', '_ormbases': ['dm.NPC']},
            'description': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'npc_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm.NPC']", 'unique': 'True', 'primary_key': 'True'})
        },
        'dm.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'dm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.Party']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dm.encounter': {
            'Meta': {'object_name': 'Encounter'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.Campaign']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.EncounterTemplate']"})
        },
        'dm.encounterparticipant': {
            'Meta': {'object_name': 'EncounterParticipant'},
            'encounter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.Encounter']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiative': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'})
        },
        'dm.encountertemplate': {
            'Meta': {'object_name': 'EncounterTemplate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'npcs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dm.NPC']", 'symmetrical': 'False'}),
            'setup': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tactics': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'dm.historyline': {
            'Meta': {'object_name': 'HistoryLine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logged_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.Session']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'dm.monsternpc': {
            'Meta': {'object_name': 'MonsterNPC', '_ormbases': ['dm.NPC']},
            'hit_points': ('django.db.models.fields.IntegerField', [], {}),
            u'npc_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm.NPC']", 'unique': 'True', 'primary_key': 'True'}),
            'npc_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.NPCType']"})
        },
        'dm.npc': {
            'Meta': {'object_name': 'NPC'},
            'conditions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Condition']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_alive': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'dm.npcencounterparticipant': {
            'Meta': {'object_name': 'NPCEncounterParticipant', '_ormbases': ['dm.EncounterParticipant']},
            u'encounterparticipant_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm.EncounterParticipant']", 'unique': 'True', 'primary_key': 'True'}),
            'npc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.NPC']"})
        },
        'dm.npctype': {
            'Meta': {'object_name': 'NPCType'},
            'alignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Alignment']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'max_hit_points': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Race']"}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Role']", 'symmetrical': 'False'}),
            'vision': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Vision']"}),
            'xp_reward': ('django.db.models.fields.IntegerField', [], {})
        },
        'dm.npctypeability': {
            'Meta': {'object_name': 'NPCTypeAbility'},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Ability']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'npc_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'abilities'", 'to': "orm['dm.NPCType']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'dm.npctypedefense': {
            'Meta': {'object_name': 'NPCTypeDefense'},
            'defense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Defense']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'npc_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'defenses'", 'to': "orm['dm.NPCType']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'dm.npctypepower': {
            'Meta': {'object_name': 'NPCTypePower'},
            'action_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ActionType']", 'null': 'True', 'blank': 'True'}),
            'attack_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.PowerRange']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['character_builder.PowerKeyword']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'npc_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'powers'", 'to': "orm['dm.NPCType']"}),
            'recharge_text': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'usage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.PowerUsage']", 'null': 'True', 'blank': 'True'})
        },
        'dm.npctypeskill': {
            'Meta': {'object_name': 'NPCTypeSkill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'npc_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'to': "orm['dm.NPCType']"}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Skill']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'dm.party': {
            'Meta': {'object_name': 'Party'},
            'background': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Character']", 'symmetrical': 'False'}),
            'formed_on': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dm.pcencounterparticipant': {
            'Meta': {'object_name': 'PCEncounterParticipant', '_ormbases': ['dm.EncounterParticipant']},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Character']"}),
            u'encounterparticipant_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm.EncounterParticipant']", 'unique': 'True', 'primary_key': 'True'})
        },
        'dm.session': {
            'Meta': {'object_name': 'Session'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.Campaign']"}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        },
        'dm.storynpc': {
            'Meta': {'object_name': 'StoryNPC', '_ormbases': ['dm.BasicStoryNPC']},
            u'basicstorynpc_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm.BasicStoryNPC']", 'unique': 'True', 'primary_key': 'True'}),
            'hit_points': ('django.db.models.fields.IntegerField', [], {}),
            'npc_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.NPCType']"})
        }
    }

    complete_apps = ['dm']