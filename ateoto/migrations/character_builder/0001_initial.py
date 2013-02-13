# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ability'
        db.create_table('character_builder_ability', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('help_text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('character_builder', ['Ability'])

        # Adding model 'Skill'
        db.create_table('character_builder_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ability', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Ability'])),
        ))
        db.send_create_signal('character_builder', ['Skill'])

        # Adding model 'Defense'
        db.create_table('character_builder_defense', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('character_builder', ['Defense'])

        # Adding M2M table for field abilities on 'Defense'
        db.create_table('character_builder_defense_abilities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('defense', models.ForeignKey(orm['character_builder.defense'], null=False)),
            ('ability', models.ForeignKey(orm['character_builder.ability'], null=False))
        ))
        db.create_unique('character_builder_defense_abilities', ['defense_id', 'ability_id'])

        # Adding model 'Modifier'
        db.create_table('character_builder_modifier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('character_builder', ['Modifier'])

        # Adding model 'AbilityMod'
        db.create_table('character_builder_abilitymod', (
            ('modifier_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.Modifier'], unique=True, primary_key=True)),
            ('ability', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Ability'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('character_builder', ['AbilityMod'])

        # Adding model 'SkillMod'
        db.create_table('character_builder_skillmod', (
            ('modifier_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.Modifier'], unique=True, primary_key=True)),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Skill'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('character_builder', ['SkillMod'])

        # Adding model 'DefenseMod'
        db.create_table('character_builder_defensemod', (
            ('modifier_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.Modifier'], unique=True, primary_key=True)),
            ('defense', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Defense'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('character_builder', ['DefenseMod'])

        # Adding model 'Role'
        db.create_table('character_builder_role', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('character_builder', ['Role'])

        # Adding model 'Alignment'
        db.create_table('character_builder_alignment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('character_builder', ['Alignment'])

        # Adding model 'Level'
        db.create_table('character_builder_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('xp_required', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('character_builder', ['Level'])

        # Adding model 'Deity'
        db.create_table('character_builder_deity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('alignment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Alignment'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('character_builder', ['Deity'])

        # Adding model 'Source'
        db.create_table('character_builder_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('character_builder', ['Source'])

        # Adding model 'Size'
        db.create_table('character_builder_size', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('space', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('reach', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('character_builder', ['Size'])

        # Adding model 'Gender'
        db.create_table('character_builder_gender', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal('character_builder', ['Gender'])

        # Adding model 'Language'
        db.create_table('character_builder_language', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('script', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('character_builder', ['Language'])

        # Adding model 'Vision'
        db.create_table('character_builder_vision', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('character_builder', ['Vision'])

        # Adding model 'Race'
        db.create_table('character_builder_race', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Source'])),
            ('average_height_text', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('average_weight_text', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('size', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Size'])),
            ('speed', self.gf('django.db.models.fields.IntegerField')()),
            ('vision', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Vision'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('character_builder', ['Race'])

        # Adding M2M table for field languages on 'Race'
        db.create_table('character_builder_race_languages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('race', models.ForeignKey(orm['character_builder.race'], null=False)),
            ('language', models.ForeignKey(orm['character_builder.language'], null=False))
        ))
        db.create_unique('character_builder_race_languages', ['race_id', 'language_id'])

        # Adding M2M table for field modifiers on 'Race'
        db.create_table('character_builder_race_modifiers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('race', models.ForeignKey(orm['character_builder.race'], null=False)),
            ('modifier', models.ForeignKey(orm['character_builder.modifier'], null=False))
        ))
        db.create_unique('character_builder_race_modifiers', ['race_id', 'modifier_id'])

        # Adding model 'RaceFeatureChoice'
        db.create_table('character_builder_racefeaturechoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('benefit', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('character_builder', ['RaceFeatureChoice'])

        # Adding model 'RaceFeature'
        db.create_table('character_builder_racefeature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('benefit', self.gf('django.db.models.fields.TextField')()),
            ('requires_choice', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Race'])),
            ('has_passive_effects', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('character_builder', ['RaceFeature'])

        # Adding M2M table for field choices on 'RaceFeature'
        db.create_table('character_builder_racefeature_choices', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('racefeature', models.ForeignKey(orm['character_builder.racefeature'], null=False)),
            ('racefeaturechoice', models.ForeignKey(orm['character_builder.racefeaturechoice'], null=False))
        ))
        db.create_unique('character_builder_racefeature_choices', ['racefeature_id', 'racefeaturechoice_id'])

        # Adding M2M table for field passive_effects on 'RaceFeature'
        db.create_table('character_builder_racefeature_passive_effects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('racefeature', models.ForeignKey(orm['character_builder.racefeature'], null=False)),
            ('modifier', models.ForeignKey(orm['character_builder.modifier'], null=False))
        ))
        db.create_unique('character_builder_racefeature_passive_effects', ['racefeature_id', 'modifier_id'])

        # Adding model 'RaceAbilityMod'
        db.create_table('character_builder_raceabilitymod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ability_mods', to=orm['character_builder.Race'])),
            ('ability', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Ability'])),
            ('modifier', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('character_builder', ['RaceAbilityMod'])

        # Adding model 'RaceSkillMod'
        db.create_table('character_builder_raceskillmod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skill_mods', to=orm['character_builder.Race'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Skill'])),
            ('modifier', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('character_builder', ['RaceSkillMod'])

        # Adding model 'WeaponCategory'
        db.create_table('character_builder_weaponcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('character_builder', ['WeaponCategory'])

        # Adding model 'WeaponGroup'
        db.create_table('character_builder_weapongroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('character_builder', ['WeaponGroup'])

        # Adding model 'WeaponProficiencyGroup'
        db.create_table('character_builder_weaponproficiencygroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('character_builder', ['WeaponProficiencyGroup'])

        # Adding M2M table for field categories on 'WeaponProficiencyGroup'
        db.create_table('character_builder_weaponproficiencygroup_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('weaponproficiencygroup', models.ForeignKey(orm['character_builder.weaponproficiencygroup'], null=False)),
            ('weaponcategory', models.ForeignKey(orm['character_builder.weaponcategory'], null=False))
        ))
        db.create_unique('character_builder_weaponproficiencygroup_categories', ['weaponproficiencygroup_id', 'weaponcategory_id'])

        # Adding model 'WeaponType'
        db.create_table('character_builder_weapontype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.WeaponCategory'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.WeaponGroup'])),
            ('proficiency', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('damage', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('weapon_range', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('properties', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('character_builder', ['WeaponType'])

        # Adding model 'ArmorClass'
        db.create_table('character_builder_armorclass', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('character_builder', ['ArmorClass'])

        # Adding model 'ArmorType'
        db.create_table('character_builder_armortype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('armor_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.ArmorClass'])),
        ))
        db.send_create_signal('character_builder', ['ArmorType'])

        # Adding model 'Currency'
        db.create_table('character_builder_currency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
        ))
        db.send_create_signal('character_builder', ['Currency'])

        # Adding model 'CurrencyExchange'
        db.create_table('character_builder_currencyexchange', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('currency_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['character_builder.Currency'])),
            ('currency_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['character_builder.Currency'])),
            ('exchange_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=18, decimal_places=9)),
        ))
        db.send_create_signal('character_builder', ['CurrencyExchange'])

        # Adding model 'Item'
        db.create_table('character_builder_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Source'])),
        ))
        db.send_create_signal('character_builder', ['Item'])

        # Adding model 'ClassType'
        db.create_table('character_builder_classtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Role'])),
            ('role_flavor', self.gf('django.db.models.fields.TextField')()),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Source'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('skill_choices', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('base_hit_points', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hit_points_per_level', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('character_builder', ['ClassType'])

        # Adding M2M table for field favored_abilities on 'ClassType'
        db.create_table('character_builder_classtype_favored_abilities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('classtype', models.ForeignKey(orm['character_builder.classtype'], null=False)),
            ('ability', models.ForeignKey(orm['character_builder.ability'], null=False))
        ))
        db.create_unique('character_builder_classtype_favored_abilities', ['classtype_id', 'ability_id'])

        # Adding M2M table for field modifiers on 'ClassType'
        db.create_table('character_builder_classtype_modifiers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('classtype', models.ForeignKey(orm['character_builder.classtype'], null=False)),
            ('modifier', models.ForeignKey(orm['character_builder.modifier'], null=False))
        ))
        db.create_unique('character_builder_classtype_modifiers', ['classtype_id', 'modifier_id'])

        # Adding M2M table for field weapon_proficiencies on 'ClassType'
        db.create_table('character_builder_classtype_weapon_proficiencies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('classtype', models.ForeignKey(orm['character_builder.classtype'], null=False)),
            ('weaponproficiencygroup', models.ForeignKey(orm['character_builder.weaponproficiencygroup'], null=False))
        ))
        db.create_unique('character_builder_classtype_weapon_proficiencies', ['classtype_id', 'weaponproficiencygroup_id'])

        # Adding M2M table for field armor_proficiencies on 'ClassType'
        db.create_table('character_builder_classtype_armor_proficiencies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('classtype', models.ForeignKey(orm['character_builder.classtype'], null=False)),
            ('armortype', models.ForeignKey(orm['character_builder.armortype'], null=False))
        ))
        db.create_unique('character_builder_classtype_armor_proficiencies', ['classtype_id', 'armortype_id'])

        # Adding M2M table for field trained_skills on 'ClassType'
        db.create_table('character_builder_classtype_trained_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('classtype', models.ForeignKey(orm['character_builder.classtype'], null=False)),
            ('skill', models.ForeignKey(orm['character_builder.skill'], null=False))
        ))
        db.create_unique('character_builder_classtype_trained_skills', ['classtype_id', 'skill_id'])

        # Adding model 'ClassFeatureChoice'
        db.create_table('character_builder_classfeaturechoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('benefit', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('character_builder', ['ClassFeatureChoice'])

        # Adding model 'ClassFeature'
        db.create_table('character_builder_classfeature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('benefit', self.gf('django.db.models.fields.TextField')()),
            ('requires_choice', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('character_builder', ['ClassFeature'])

        # Adding M2M table for field choices on 'ClassFeature'
        db.create_table('character_builder_classfeature_choices', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('classfeature', models.ForeignKey(orm['character_builder.classfeature'], null=False)),
            ('classfeaturechoice', models.ForeignKey(orm['character_builder.classfeaturechoice'], null=False))
        ))
        db.create_unique('character_builder_classfeature_choices', ['classfeature_id', 'classfeaturechoice_id'])

        # Adding M2M table for field class_type on 'ClassFeature'
        db.create_table('character_builder_classfeature_class_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('classfeature', models.ForeignKey(orm['character_builder.classfeature'], null=False)),
            ('classtype', models.ForeignKey(orm['character_builder.classtype'], null=False))
        ))
        db.create_unique('character_builder_classfeature_class_type', ['classfeature_id', 'classtype_id'])

        # Adding M2M table for field passive_effects on 'ClassFeature'
        db.create_table('character_builder_classfeature_passive_effects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('classfeature', models.ForeignKey(orm['character_builder.classfeature'], null=False)),
            ('modifier', models.ForeignKey(orm['character_builder.modifier'], null=False))
        ))
        db.create_unique('character_builder_classfeature_passive_effects', ['classfeature_id', 'modifier_id'])

        # Adding model 'ClassTypeDefMod'
        db.create_table('character_builder_classtypedefmod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('class_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.ClassType'])),
            ('defense', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Defense'])),
            ('bonus', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('character_builder', ['ClassTypeDefMod'])

        # Adding model 'ClassSkill'
        db.create_table('character_builder_classskill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('class_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='class_skills', to=orm['character_builder.ClassType'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Skill'])),
        ))
        db.send_create_signal('character_builder', ['ClassSkill'])

        # Adding model 'FeatChoice'
        db.create_table('character_builder_featchoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('benefit', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('character_builder', ['FeatChoice'])

        # Adding model 'Feat'
        db.create_table('character_builder_feat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('benefit', self.gf('django.db.models.fields.TextField')()),
            ('special', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('has_passive_effects', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_retake', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('requires_choice', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('character_builder', ['Feat'])

        # Adding M2M table for field passive_effects on 'Feat'
        db.create_table('character_builder_feat_passive_effects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('feat', models.ForeignKey(orm['character_builder.feat'], null=False)),
            ('modifier', models.ForeignKey(orm['character_builder.modifier'], null=False))
        ))
        db.create_unique('character_builder_feat_passive_effects', ['feat_id', 'modifier_id'])

        # Adding M2M table for field choices on 'Feat'
        db.create_table('character_builder_feat_choices', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('feat', models.ForeignKey(orm['character_builder.feat'], null=False)),
            ('featchoice', models.ForeignKey(orm['character_builder.featchoice'], null=False))
        ))
        db.create_unique('character_builder_feat_choices', ['feat_id', 'featchoice_id'])

        # Adding model 'FeatPrereq'
        db.create_table('character_builder_featprereq', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feat', self.gf('django.db.models.fields.related.ForeignKey')(related_name='prereqs', to=orm['character_builder.Feat'])),
        ))
        db.send_create_signal('character_builder', ['FeatPrereq'])

        # Adding model 'FeatRacePrereq'
        db.create_table('character_builder_featraceprereq', (
            ('featprereq_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.FeatPrereq'], unique=True, primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Race'])),
        ))
        db.send_create_signal('character_builder', ['FeatRacePrereq'])

        # Adding model 'FeatClassTypePrereq'
        db.create_table('character_builder_featclasstypeprereq', (
            ('featprereq_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.FeatPrereq'], unique=True, primary_key=True)),
            ('class_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.ClassType'])),
        ))
        db.send_create_signal('character_builder', ['FeatClassTypePrereq'])

        # Adding model 'FeatClassFeaturePrereq'
        db.create_table('character_builder_featclassfeatureprereq', (
            ('featprereq_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.FeatPrereq'], unique=True, primary_key=True)),
            ('classfeature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.ClassFeature'])),
        ))
        db.send_create_signal('character_builder', ['FeatClassFeaturePrereq'])

        # Adding model 'FeatAbilityPrereq'
        db.create_table('character_builder_featabilityprereq', (
            ('featprereq_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.FeatPrereq'], unique=True, primary_key=True)),
            ('ability', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Ability'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('character_builder', ['FeatAbilityPrereq'])

        # Adding model 'FeatSkillPrereq'
        db.create_table('character_builder_featskillprereq', (
            ('featprereq_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.FeatPrereq'], unique=True, primary_key=True)),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Skill'])),
        ))
        db.send_create_signal('character_builder', ['FeatSkillPrereq'])

        # Adding model 'FeatSkillOrSkillPrereq'
        db.create_table('character_builder_featskillorskillprereq', (
            ('featprereq_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.FeatPrereq'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('character_builder', ['FeatSkillOrSkillPrereq'])

        # Adding M2M table for field allowed_skills on 'FeatSkillOrSkillPrereq'
        db.create_table('character_builder_featskillorskillprereq_allowed_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('featskillorskillprereq', models.ForeignKey(orm['character_builder.featskillorskillprereq'], null=False)),
            ('skill', models.ForeignKey(orm['character_builder.skill'], null=False))
        ))
        db.create_unique('character_builder_featskillorskillprereq_allowed_skills', ['featskillorskillprereq_id', 'skill_id'])

        # Adding model 'FeatFeatPrereq'
        db.create_table('character_builder_featfeatprereq', (
            ('featprereq_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.FeatPrereq'], unique=True, primary_key=True)),
            ('pre_feat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Feat'])),
        ))
        db.send_create_signal('character_builder', ['FeatFeatPrereq'])

        # Adding model 'FeatDeityPrereq'
        db.create_table('character_builder_featdeityprereq', (
            ('featprereq_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.FeatPrereq'], unique=True, primary_key=True)),
            ('deity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Deity'])),
        ))
        db.send_create_signal('character_builder', ['FeatDeityPrereq'])

        # Adding model 'FeatArmorTypePrereq'
        db.create_table('character_builder_featarmortypeprereq', (
            ('featprereq_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.FeatPrereq'], unique=True, primary_key=True)),
            ('armor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.ArmorType'])),
        ))
        db.send_create_signal('character_builder', ['FeatArmorTypePrereq'])

        # Adding model 'FeatArmorOrArmorPrereq'
        db.create_table('character_builder_featarmororarmorprereq', (
            ('featprereq_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.FeatPrereq'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('character_builder', ['FeatArmorOrArmorPrereq'])

        # Adding M2M table for field allowed_armors on 'FeatArmorOrArmorPrereq'
        db.create_table('character_builder_featarmororarmorprereq_allowed_armors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('featarmororarmorprereq', models.ForeignKey(orm['character_builder.featarmororarmorprereq'], null=False)),
            ('armortype', models.ForeignKey(orm['character_builder.armortype'], null=False))
        ))
        db.create_unique('character_builder_featarmororarmorprereq_allowed_armors', ['featarmororarmorprereq_id', 'armortype_id'])

        # Adding model 'PowerType'
        db.create_table('character_builder_powertype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('character_builder', ['PowerType'])

        # Adding model 'PowerKeyword'
        db.create_table('character_builder_powerkeyword', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('character_builder', ['PowerKeyword'])

        # Adding model 'Power'
        db.create_table('character_builder_power', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('power_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.PowerType'])),
            ('flavor', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('target', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('attack', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('hit', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('miss', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('effect', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('special', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('character_builder', ['Power'])

        # Adding model 'ClassPower'
        db.create_table('character_builder_classpower', (
            ('power_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.Power'], unique=True, primary_key=True)),
            ('class_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.ClassType'])),
        ))
        db.send_create_signal('character_builder', ['ClassPower'])

        # Adding model 'RacialPower'
        db.create_table('character_builder_racialpower', (
            ('power_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.Power'], unique=True, primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Race'])),
        ))
        db.send_create_signal('character_builder', ['RacialPower'])

        # Adding model 'FeatPower'
        db.create_table('character_builder_featpower', (
            ('power_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['character_builder.Power'], unique=True, primary_key=True)),
            ('feat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Feat'])),
        ))
        db.send_create_signal('character_builder', ['FeatPower'])

        # Adding model 'Character'
        db.create_table('character_builder_character', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug_name', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('class_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.ClassType'])),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Race'])),
            ('gender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Gender'])),
            ('xp', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('max_hit_points', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('hit_points', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('alignment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Alignment'])),
            ('deity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Deity'])),
        ))
        db.send_create_signal('character_builder', ['Character'])

        # Adding model 'CharacterCurrency'
        db.create_table('character_builder_charactercurrency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wealth', to=orm['character_builder.Character'])),
            ('currency_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Currency'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('character_builder', ['CharacterCurrency'])

        # Adding model 'CharacterRaceFeature'
        db.create_table('character_builder_characterracefeature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(related_name='race_features', to=orm['character_builder.Character'])),
            ('race_feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.RaceFeature'])),
            ('benefit', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('character_builder', ['CharacterRaceFeature'])

        # Adding model 'CharacterClassFeature'
        db.create_table('character_builder_characterclassfeature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(related_name='class_features', to=orm['character_builder.Character'])),
            ('class_feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.ClassFeature'])),
            ('choice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.ClassFeatureChoice'], null=True, blank=True)),
        ))
        db.send_create_signal('character_builder', ['CharacterClassFeature'])

        # Adding model 'CharacterAbility'
        db.create_table('character_builder_characterability', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(related_name='abilities', to=orm['character_builder.Character'])),
            ('ability', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Ability'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('character_builder', ['CharacterAbility'])

        # Adding model 'CharacterArmorType'
        db.create_table('character_builder_characterarmortype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(related_name='armor_types', to=orm['character_builder.Character'])),
            ('armor_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.ArmorType'])),
        ))
        db.send_create_signal('character_builder', ['CharacterArmorType'])

        # Adding model 'CharacterSkill'
        db.create_table('character_builder_characterskill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skills', to=orm['character_builder.Character'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Skill'])),
            ('is_trained', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('character_builder', ['CharacterSkill'])

        # Adding model 'CharacterFeat'
        db.create_table('character_builder_characterfeat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(related_name='feats', to=orm['character_builder.Character'])),
            ('feat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Feat'])),
            ('required_choice', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('choice_result', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('character_builder', ['CharacterFeat'])

        # Adding model 'CharacterPower'
        db.create_table('character_builder_characterpower', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(related_name='powers', to=orm['character_builder.Character'])),
            ('power', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['character_builder.Power'])),
        ))
        db.send_create_signal('character_builder', ['CharacterPower'])


    def backwards(self, orm):
        # Deleting model 'Ability'
        db.delete_table('character_builder_ability')

        # Deleting model 'Skill'
        db.delete_table('character_builder_skill')

        # Deleting model 'Defense'
        db.delete_table('character_builder_defense')

        # Removing M2M table for field abilities on 'Defense'
        db.delete_table('character_builder_defense_abilities')

        # Deleting model 'Modifier'
        db.delete_table('character_builder_modifier')

        # Deleting model 'AbilityMod'
        db.delete_table('character_builder_abilitymod')

        # Deleting model 'SkillMod'
        db.delete_table('character_builder_skillmod')

        # Deleting model 'DefenseMod'
        db.delete_table('character_builder_defensemod')

        # Deleting model 'Role'
        db.delete_table('character_builder_role')

        # Deleting model 'Alignment'
        db.delete_table('character_builder_alignment')

        # Deleting model 'Level'
        db.delete_table('character_builder_level')

        # Deleting model 'Deity'
        db.delete_table('character_builder_deity')

        # Deleting model 'Source'
        db.delete_table('character_builder_source')

        # Deleting model 'Size'
        db.delete_table('character_builder_size')

        # Deleting model 'Gender'
        db.delete_table('character_builder_gender')

        # Deleting model 'Language'
        db.delete_table('character_builder_language')

        # Deleting model 'Vision'
        db.delete_table('character_builder_vision')

        # Deleting model 'Race'
        db.delete_table('character_builder_race')

        # Removing M2M table for field languages on 'Race'
        db.delete_table('character_builder_race_languages')

        # Removing M2M table for field modifiers on 'Race'
        db.delete_table('character_builder_race_modifiers')

        # Deleting model 'RaceFeatureChoice'
        db.delete_table('character_builder_racefeaturechoice')

        # Deleting model 'RaceFeature'
        db.delete_table('character_builder_racefeature')

        # Removing M2M table for field choices on 'RaceFeature'
        db.delete_table('character_builder_racefeature_choices')

        # Removing M2M table for field passive_effects on 'RaceFeature'
        db.delete_table('character_builder_racefeature_passive_effects')

        # Deleting model 'RaceAbilityMod'
        db.delete_table('character_builder_raceabilitymod')

        # Deleting model 'RaceSkillMod'
        db.delete_table('character_builder_raceskillmod')

        # Deleting model 'WeaponCategory'
        db.delete_table('character_builder_weaponcategory')

        # Deleting model 'WeaponGroup'
        db.delete_table('character_builder_weapongroup')

        # Deleting model 'WeaponProficiencyGroup'
        db.delete_table('character_builder_weaponproficiencygroup')

        # Removing M2M table for field categories on 'WeaponProficiencyGroup'
        db.delete_table('character_builder_weaponproficiencygroup_categories')

        # Deleting model 'WeaponType'
        db.delete_table('character_builder_weapontype')

        # Deleting model 'ArmorClass'
        db.delete_table('character_builder_armorclass')

        # Deleting model 'ArmorType'
        db.delete_table('character_builder_armortype')

        # Deleting model 'Currency'
        db.delete_table('character_builder_currency')

        # Deleting model 'CurrencyExchange'
        db.delete_table('character_builder_currencyexchange')

        # Deleting model 'Item'
        db.delete_table('character_builder_item')

        # Deleting model 'ClassType'
        db.delete_table('character_builder_classtype')

        # Removing M2M table for field favored_abilities on 'ClassType'
        db.delete_table('character_builder_classtype_favored_abilities')

        # Removing M2M table for field modifiers on 'ClassType'
        db.delete_table('character_builder_classtype_modifiers')

        # Removing M2M table for field weapon_proficiencies on 'ClassType'
        db.delete_table('character_builder_classtype_weapon_proficiencies')

        # Removing M2M table for field armor_proficiencies on 'ClassType'
        db.delete_table('character_builder_classtype_armor_proficiencies')

        # Removing M2M table for field trained_skills on 'ClassType'
        db.delete_table('character_builder_classtype_trained_skills')

        # Deleting model 'ClassFeatureChoice'
        db.delete_table('character_builder_classfeaturechoice')

        # Deleting model 'ClassFeature'
        db.delete_table('character_builder_classfeature')

        # Removing M2M table for field choices on 'ClassFeature'
        db.delete_table('character_builder_classfeature_choices')

        # Removing M2M table for field class_type on 'ClassFeature'
        db.delete_table('character_builder_classfeature_class_type')

        # Removing M2M table for field passive_effects on 'ClassFeature'
        db.delete_table('character_builder_classfeature_passive_effects')

        # Deleting model 'ClassTypeDefMod'
        db.delete_table('character_builder_classtypedefmod')

        # Deleting model 'ClassSkill'
        db.delete_table('character_builder_classskill')

        # Deleting model 'FeatChoice'
        db.delete_table('character_builder_featchoice')

        # Deleting model 'Feat'
        db.delete_table('character_builder_feat')

        # Removing M2M table for field passive_effects on 'Feat'
        db.delete_table('character_builder_feat_passive_effects')

        # Removing M2M table for field choices on 'Feat'
        db.delete_table('character_builder_feat_choices')

        # Deleting model 'FeatPrereq'
        db.delete_table('character_builder_featprereq')

        # Deleting model 'FeatRacePrereq'
        db.delete_table('character_builder_featraceprereq')

        # Deleting model 'FeatClassTypePrereq'
        db.delete_table('character_builder_featclasstypeprereq')

        # Deleting model 'FeatClassFeaturePrereq'
        db.delete_table('character_builder_featclassfeatureprereq')

        # Deleting model 'FeatAbilityPrereq'
        db.delete_table('character_builder_featabilityprereq')

        # Deleting model 'FeatSkillPrereq'
        db.delete_table('character_builder_featskillprereq')

        # Deleting model 'FeatSkillOrSkillPrereq'
        db.delete_table('character_builder_featskillorskillprereq')

        # Removing M2M table for field allowed_skills on 'FeatSkillOrSkillPrereq'
        db.delete_table('character_builder_featskillorskillprereq_allowed_skills')

        # Deleting model 'FeatFeatPrereq'
        db.delete_table('character_builder_featfeatprereq')

        # Deleting model 'FeatDeityPrereq'
        db.delete_table('character_builder_featdeityprereq')

        # Deleting model 'FeatArmorTypePrereq'
        db.delete_table('character_builder_featarmortypeprereq')

        # Deleting model 'FeatArmorOrArmorPrereq'
        db.delete_table('character_builder_featarmororarmorprereq')

        # Removing M2M table for field allowed_armors on 'FeatArmorOrArmorPrereq'
        db.delete_table('character_builder_featarmororarmorprereq_allowed_armors')

        # Deleting model 'PowerType'
        db.delete_table('character_builder_powertype')

        # Deleting model 'PowerKeyword'
        db.delete_table('character_builder_powerkeyword')

        # Deleting model 'Power'
        db.delete_table('character_builder_power')

        # Deleting model 'ClassPower'
        db.delete_table('character_builder_classpower')

        # Deleting model 'RacialPower'
        db.delete_table('character_builder_racialpower')

        # Deleting model 'FeatPower'
        db.delete_table('character_builder_featpower')

        # Deleting model 'Character'
        db.delete_table('character_builder_character')

        # Deleting model 'CharacterCurrency'
        db.delete_table('character_builder_charactercurrency')

        # Deleting model 'CharacterRaceFeature'
        db.delete_table('character_builder_characterracefeature')

        # Deleting model 'CharacterClassFeature'
        db.delete_table('character_builder_characterclassfeature')

        # Deleting model 'CharacterAbility'
        db.delete_table('character_builder_characterability')

        # Deleting model 'CharacterArmorType'
        db.delete_table('character_builder_characterarmortype')

        # Deleting model 'CharacterSkill'
        db.delete_table('character_builder_characterskill')

        # Deleting model 'CharacterFeat'
        db.delete_table('character_builder_characterfeat')

        # Deleting model 'CharacterPower'
        db.delete_table('character_builder_characterpower')


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
        'character_builder.abilitymod': {
            'Meta': {'object_name': 'AbilityMod', '_ormbases': ['character_builder.Modifier']},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Ability']"}),
            'modifier_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.Modifier']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
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
        'character_builder.characterability': {
            'Meta': {'object_name': 'CharacterAbility'},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Ability']"}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'abilities'", 'to': "orm['character_builder.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.characterarmortype': {
            'Meta': {'object_name': 'CharacterArmorType'},
            'armor_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ArmorType']"}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'armor_types'", 'to': "orm['character_builder.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.characterclassfeature': {
            'Meta': {'object_name': 'CharacterClassFeature'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'class_features'", 'to': "orm['character_builder.Character']"}),
            'choice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ClassFeatureChoice']", 'null': 'True', 'blank': 'True'}),
            'class_feature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ClassFeature']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.charactercurrency': {
            'Meta': {'object_name': 'CharacterCurrency'},
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wealth'", 'to': "orm['character_builder.Character']"}),
            'currency_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.characterfeat': {
            'Meta': {'object_name': 'CharacterFeat'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feats'", 'to': "orm['character_builder.Character']"}),
            'choice_result': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'feat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Feat']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'required_choice': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'character_builder.characterpower': {
            'Meta': {'object_name': 'CharacterPower'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'powers'", 'to': "orm['character_builder.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'power': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Power']"})
        },
        'character_builder.characterracefeature': {
            'Meta': {'object_name': 'CharacterRaceFeature'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'race_features'", 'to': "orm['character_builder.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race_feature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.RaceFeature']"})
        },
        'character_builder.characterskill': {
            'Meta': {'object_name': 'CharacterSkill'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'to': "orm['character_builder.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_trained': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Skill']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.classfeature': {
            'Meta': {'object_name': 'ClassFeature'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'choices': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.ClassFeatureChoice']", 'symmetrical': 'False', 'blank': 'True'}),
            'class_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.ClassType']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'passive_effects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Modifier']", 'symmetrical': 'False', 'blank': 'True'}),
            'requires_choice': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'character_builder.classfeaturechoice': {
            'Meta': {'object_name': 'ClassFeatureChoice'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'character_builder.classpower': {
            'Meta': {'object_name': 'ClassPower', '_ormbases': ['character_builder.Power']},
            'class_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ClassType']"}),
            'power_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.Power']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.classskill': {
            'Meta': {'object_name': 'ClassSkill'},
            'class_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'class_skills'", 'to': "orm['character_builder.ClassType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Skill']"})
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
        'character_builder.classtypedefmod': {
            'Meta': {'object_name': 'ClassTypeDefMod'},
            'bonus': ('django.db.models.fields.IntegerField', [], {}),
            'class_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ClassType']"}),
            'defense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Defense']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.currency': {
            'Meta': {'object_name': 'Currency'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'})
        },
        'character_builder.currencyexchange': {
            'Meta': {'object_name': 'CurrencyExchange'},
            'currency_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['character_builder.Currency']"}),
            'currency_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['character_builder.Currency']"}),
            'exchange_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '9'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.defense': {
            'Meta': {'object_name': 'Defense'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'abilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Ability']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'character_builder.defensemod': {
            'Meta': {'object_name': 'DefenseMod', '_ormbases': ['character_builder.Modifier']},
            'defense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Defense']"}),
            'modifier_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.Modifier']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.deity': {
            'Meta': {'object_name': 'Deity'},
            'alignment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Alignment']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'character_builder.feat': {
            'Meta': {'object_name': 'Feat'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'can_retake': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'choices': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.FeatChoice']", 'symmetrical': 'False', 'blank': 'True'}),
            'has_passive_effects': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'passive_effects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Modifier']", 'symmetrical': 'False', 'blank': 'True'}),
            'requires_choice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'special': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'character_builder.featabilityprereq': {
            'Meta': {'object_name': 'FeatAbilityPrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Ability']"}),
            'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.featarmororarmorprereq': {
            'Meta': {'object_name': 'FeatArmorOrArmorPrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'allowed_armors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.ArmorType']", 'symmetrical': 'False'}),
            'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.featarmortypeprereq': {
            'Meta': {'object_name': 'FeatArmorTypePrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'armor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ArmorType']"}),
            'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.featchoice': {
            'Meta': {'object_name': 'FeatChoice'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.featclassfeatureprereq': {
            'Meta': {'object_name': 'FeatClassFeaturePrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'classfeature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ClassFeature']"}),
            'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.featclasstypeprereq': {
            'Meta': {'object_name': 'FeatClassTypePrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'class_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.ClassType']"}),
            'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.featdeityprereq': {
            'Meta': {'object_name': 'FeatDeityPrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'deity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Deity']"}),
            'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.featfeatprereq': {
            'Meta': {'object_name': 'FeatFeatPrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'}),
            'pre_feat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Feat']"})
        },
        'character_builder.featpower': {
            'Meta': {'object_name': 'FeatPower', '_ormbases': ['character_builder.Power']},
            'feat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Feat']"}),
            'power_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.Power']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.featprereq': {
            'Meta': {'object_name': 'FeatPrereq'},
            'feat': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prereqs'", 'to': "orm['character_builder.Feat']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.featraceprereq': {
            'Meta': {'object_name': 'FeatRacePrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Race']"})
        },
        'character_builder.featskillorskillprereq': {
            'Meta': {'object_name': 'FeatSkillOrSkillPrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'allowed_skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Skill']", 'symmetrical': 'False'}),
            'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'})
        },
        'character_builder.featskillprereq': {
            'Meta': {'object_name': 'FeatSkillPrereq', '_ormbases': ['character_builder.FeatPrereq']},
            'featprereq_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.FeatPrereq']", 'unique': 'True', 'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Skill']"})
        },
        'character_builder.gender': {
            'Meta': {'object_name': 'Gender'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'character_builder.item': {
            'Meta': {'object_name': 'Item'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Source']"})
        },
        'character_builder.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'script': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.level': {
            'Meta': {'object_name': 'Level'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'xp_required': ('django.db.models.fields.IntegerField', [], {})
        },
        'character_builder.modifier': {
            'Meta': {'object_name': 'Modifier'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'character_builder.power': {
            'Meta': {'object_name': 'Power'},
            'attack': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'flavor': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hit': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'miss': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'power_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.PowerType']"}),
            'special': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'target': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'character_builder.powerkeyword': {
            'Meta': {'object_name': 'PowerKeyword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.powertype': {
            'Meta': {'object_name': 'PowerType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        'character_builder.raceabilitymod': {
            'Meta': {'object_name': 'RaceAbilityMod'},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Ability']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.IntegerField', [], {}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ability_mods'", 'to': "orm['character_builder.Race']"})
        },
        'character_builder.racefeature': {
            'Meta': {'object_name': 'RaceFeature'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'choices': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.RaceFeatureChoice']", 'symmetrical': 'False', 'blank': 'True'}),
            'has_passive_effects': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'passive_effects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.Modifier']", 'symmetrical': 'False', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Race']"}),
            'requires_choice': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'character_builder.racefeaturechoice': {
            'Meta': {'object_name': 'RaceFeatureChoice'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'character_builder.raceskillmod': {
            'Meta': {'object_name': 'RaceSkillMod'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifier': ('django.db.models.fields.IntegerField', [], {}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skill_mods'", 'to': "orm['character_builder.Race']"}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Skill']"})
        },
        'character_builder.racialpower': {
            'Meta': {'object_name': 'RacialPower', '_ormbases': ['character_builder.Power']},
            'power_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.Power']", 'unique': 'True', 'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Race']"})
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
        'character_builder.skillmod': {
            'Meta': {'object_name': 'SkillMod', '_ormbases': ['character_builder.Modifier']},
            'modifier_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['character_builder.Modifier']", 'unique': 'True', 'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.Skill']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
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
        'character_builder.weapongroup': {
            'Meta': {'object_name': 'WeaponGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.weaponproficiencygroup': {
            'Meta': {'object_name': 'WeaponProficiencyGroup'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['character_builder.WeaponCategory']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'character_builder.weapontype': {
            'Meta': {'object_name': 'WeaponType'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.WeaponCategory']"}),
            'damage': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['character_builder.WeaponGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'proficiency': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'properties': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'weapon_range': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['character_builder']