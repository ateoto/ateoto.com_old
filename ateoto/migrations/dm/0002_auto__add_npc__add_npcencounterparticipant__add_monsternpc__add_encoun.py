# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NPC'
        db.create_table('dm_npc', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_alive', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('dm', ['NPC'])

        # Adding model 'NPCEncounterParticipant'
        db.create_table('dm_npcencounterparticipant', (
            ('encounterparticipant_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm.EncounterParticipant'], unique=True, primary_key=True)),
            ('npc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm.NPC'])),
        ))
        db.send_create_signal('dm', ['NPCEncounterParticipant'])

        # Adding model 'MonsterNPC'
        db.create_table('dm_monsternpc', (
            ('npc_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm.NPC'], unique=True, primary_key=True)),
            ('npc_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm.NPCType'])),
            ('hit_points', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('dm', ['MonsterNPC'])

        # Adding model 'Encounter'
        db.create_table('dm_encounter', (
            ('encountertemplate_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm.EncounterTemplate'], unique=True, primary_key=True)),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm.Party'])),
        ))
        db.send_create_signal('dm', ['Encounter'])

        # Adding model 'PCEncounterParticipant'
        db.create_table('dm_pcencounterparticipant', (
            ('encounterparticipant_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm.EncounterParticipant'], unique=True, primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Character'])),
        ))
        db.send_create_signal('dm', ['PCEncounterParticipant'])

        # Adding model 'EncounterInitiative'
        db.create_table('dm_encounterinitiative', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encounter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm.Encounter'])),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm.EncounterParticipant'])),
            ('initiative', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('dm', ['EncounterInitiative'])

        # Adding model 'NPCTypeAbility'
        db.create_table('dm_npctypeability', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('npc_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='abilities', to=orm['dm.NPCType'])),
            ('ability', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Ability'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('dm', ['NPCTypeAbility'])

        # Adding model 'BasicStoryNPC'
        db.create_table('dm_basicstorynpc', (
            ('npc_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm.NPC'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('dm', ['BasicStoryNPC'])

        # Adding model 'StoryNPC'
        db.create_table('dm_storynpc', (
            ('basicstorynpc_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm.BasicStoryNPC'], unique=True, primary_key=True)),
            ('npc_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm.NPCType'])),
            ('hit_points', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('dm', ['StoryNPC'])

        # Adding model 'EncounterTemplate'
        db.create_table('dm_encountertemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('dm', ['EncounterTemplate'])

        # Adding M2M table for field npcs on 'EncounterTemplate'
        db.create_table('dm_encountertemplate_npcs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('encountertemplate', models.ForeignKey(orm['dm.encountertemplate'], null=False)),
            ('npc', models.ForeignKey(orm['dm.npc'], null=False))
        ))
        db.create_unique('dm_encountertemplate_npcs', ['encountertemplate_id', 'npc_id'])

        # Adding model 'NPCTypeDefense'
        db.create_table('dm_npctypedefense', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('npc_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='defenses', to=orm['dm.NPCType'])),
            ('defense', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Defense'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('dm', ['NPCTypeDefense'])

        # Adding model 'NPCType'
        db.create_table('dm_npctype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Race'])),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('vision', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Vision'])),
            ('xp_reward', self.gf('django.db.models.fields.IntegerField')()),
            ('max_hit_points', self.gf('django.db.models.fields.IntegerField')()),
            ('alignment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Alignment'], blank=True)),
        ))
        db.send_create_signal('dm', ['NPCType'])

        # Adding M2M table for field roles on 'NPCType'
        db.create_table('dm_npctype_roles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('npctype', models.ForeignKey(orm['dm.npctype'], null=False)),
            ('role', models.ForeignKey(orm['character_builder.role'], null=False))
        ))
        db.create_unique('dm_npctype_roles', ['npctype_id', 'role_id'])

        # Adding model 'EncounterParticipant'
        db.create_table('dm_encounterparticipant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('dm', ['EncounterParticipant'])


    def backwards(self, orm):
        # Deleting model 'NPC'
        db.delete_table('dm_npc')

        # Deleting model 'NPCEncounterParticipant'
        db.delete_table('dm_npcencounterparticipant')

        # Deleting model 'MonsterNPC'
        db.delete_table('dm_monsternpc')

        # Deleting model 'Encounter'
        db.delete_table('dm_encounter')

        # Deleting model 'PCEncounterParticipant'
        db.delete_table('dm_pcencounterparticipant')

        # Deleting model 'EncounterInitiative'
        db.delete_table('dm_encounterinitiative')

        # Deleting model 'NPCTypeAbility'
        db.delete_table('dm_npctypeability')

        # Deleting model 'BasicStoryNPC'
        db.delete_table('dm_basicstorynpc')

        # Deleting model 'StoryNPC'
        db.delete_table('dm_storynpc')

        # Deleting model 'EncounterTemplate'
        db.delete_table('dm_encountertemplate')

        # Removing M2M table for field npcs on 'EncounterTemplate'
        db.delete_table('dm_encountertemplate_npcs')

        # Deleting model 'NPCTypeDefense'
        db.delete_table('dm_npctypedefense')

        # Deleting model 'NPCType'
        db.delete_table('dm_npctype')

        # Removing M2M table for field roles on 'NPCType'
        db.delete_table('dm_npctype_roles')

        # Deleting model 'EncounterParticipant'
        db.delete_table('dm_encounterparticipant')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'character_builder.ability': {
            'Meta': {'object_name': 'Ability'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'help_text': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.alignment': {
            'Meta': {'object_name': 'Alignment'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'character_builder.armorclass': {
            'Meta': {'object_name': 'ArmorClass'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.armortype': {
            'Meta': {'object_name': 'ArmorType'},
            'armor_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ArmorClass']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.character': {
            'Meta': {'object_name': 'Character'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'alignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Alignment']"}),
            'class_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ClassType']"}),
            'deity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Deity']"}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Gender']"}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hit_points': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_hit_points': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Race']"}),
            'slug_name': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['auth.User']"}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifiers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Modifier']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Role']"}),
            'role_flavor': ('django.db.models.fields.TextField', [], {}),
            'skill_choices': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Source']"}),
            'trained_skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['character_builder.Skill']", 'null': 'True', 'blank': 'True'}),
            'weapon_proficiencies': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.WeaponProficiencyGroup']", 'symmetrical': 'False'})
        },
        'character_builder.defense': {
            'Meta': {'object_name': 'Defense'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'abilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Ability']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'character_builder.deity': {
            'Meta': {'object_name': 'Deity'},
            'alignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Alignment']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'character_builder.gender': {
            'Meta': {'object_name': 'Gender'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'character_builder.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'script': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.modifier': {
            'Meta': {'object_name': 'Modifier'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.race': {
            'Meta': {'ordering': "['name']", 'object_name': 'Race'},
            'average_height_text': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'average_weight_text': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Language']", 'symmetrical': 'False'}),
            'modifiers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Modifier']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Size']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Source']"}),
            'speed': ('django.db.models.fields.IntegerField', [], {}),
            'vision': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Vision']"})
        },
        'character_builder.role': {
            'Meta': {'object_name': 'Role'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.size': {
            'Meta': {'object_name': 'Size'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'reach': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'space': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.skill': {
            'Meta': {'object_name': 'Skill'},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Ability']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.source': {
            'Meta': {'ordering': "['name']", 'object_name': 'Source'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.vision': {
            'Meta': {'object_name': 'Vision'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.weaponcategory': {
            'Meta': {'object_name': 'WeaponCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.weaponproficiencygroup': {
            'Meta': {'object_name': 'WeaponProficiencyGroup'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.WeaponCategory']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dm.basicstorynpc': {
            'Meta': {'object_name': 'BasicStoryNPC', '_ormbases': ['dm.NPC']},
            'description': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'npc_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm.NPC']", 'unique': 'True', 'primary_key': 'True'})
        },
        'dm.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'dm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.Party']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dm.encounter': {
            'Meta': {'object_name': 'Encounter', '_ormbases': ['dm.EncounterTemplate']},
            'encountertemplate_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm.EncounterTemplate']", 'unique': 'True', 'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.Party']"})
        },
        'dm.encounterinitiative': {
            'Meta': {'object_name': 'EncounterInitiative'},
            'encounter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.Encounter']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiative': ('django.db.models.fields.IntegerField', [], {}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.EncounterParticipant']"})
        },
        'dm.encounterparticipant': {
            'Meta': {'object_name': 'EncounterParticipant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dm.encountertemplate': {
            'Meta': {'object_name': 'EncounterTemplate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'npcs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dm.NPC']", 'symmetrical': 'False'})
        },
        'dm.historyline': {
            'Meta': {'object_name': 'HistoryLine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logged_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.Session']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'dm.monsternpc': {
            'Meta': {'object_name': 'MonsterNPC', '_ormbases': ['dm.NPC']},
            'hit_points': ('django.db.models.fields.IntegerField', [], {}),
            'npc_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm.NPC']", 'unique': 'True', 'primary_key': 'True'}),
            'npc_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.NPCType']"})
        },
        'dm.npc': {
            'Meta': {'object_name': 'NPC'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_alive': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'dm.npcencounterparticipant': {
            'Meta': {'object_name': 'NPCEncounterParticipant', '_ormbases': ['dm.EncounterParticipant']},
            'encounterparticipant_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm.EncounterParticipant']", 'unique': 'True', 'primary_key': 'True'}),
            'npc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.NPC']"})
        },
        'dm.npctype': {
            'Meta': {'object_name': 'NPCType'},
            'alignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Alignment']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'npc_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'abilities'", 'to': "orm['dm.NPCType']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'dm.npctypedefense': {
            'Meta': {'object_name': 'NPCTypeDefense'},
            'defense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Defense']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'npc_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'defenses'", 'to': "orm['dm.NPCType']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'dm.party': {
            'Meta': {'object_name': 'Party'},
            'background': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Character']", 'symmetrical': 'False'}),
            'formed_on': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dm.pcencounterparticipant': {
            'Meta': {'object_name': 'PCEncounterParticipant', '_ormbases': ['dm.EncounterParticipant']},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Character']"}),
            'encounterparticipant_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm.EncounterParticipant']", 'unique': 'True', 'primary_key': 'True'})
        },
        'dm.session': {
            'Meta': {'object_name': 'Session'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.Campaign']"}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        },
        'dm.storynpc': {
            'Meta': {'object_name': 'StoryNPC', '_ormbases': ['dm.BasicStoryNPC']},
            'basicstorynpc_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm.BasicStoryNPC']", 'unique': 'True', 'primary_key': 'True'}),
            'hit_points': ('django.db.models.fields.IntegerField', [], {}),
            'npc_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm.NPCType']"})
        }
    }

    complete_apps = ['dm']