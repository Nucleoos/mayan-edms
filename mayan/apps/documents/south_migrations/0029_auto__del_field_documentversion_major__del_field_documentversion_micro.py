# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'DocumentVersion', fields ['document', 'major', 'minor', 'micro']
        db.delete_unique(u'documents_documentversion', ['document_id', 'major', 'minor', 'micro'])

        # Deleting field 'DocumentVersion.major'
        db.delete_column(u'documents_documentversion', 'major')

        # Deleting field 'DocumentVersion.micro'
        db.delete_column(u'documents_documentversion', 'micro')

        # Deleting field 'DocumentVersion.minor'
        db.delete_column(u'documents_documentversion', 'minor')

    def backwards(self, orm):
        # Adding field 'DocumentVersion.major'
        db.add_column(u'documents_documentversion', 'major',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DocumentVersion.micro'
        db.add_column(u'documents_documentversion', 'micro',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DocumentVersion.minor'
        db.add_column(u'documents_documentversion', 'minor',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding unique constraint on 'DocumentVersion', fields ['document', 'major', 'minor', 'micro']
        db.create_unique(u'documents_documentversion', ['document_id', 'major', 'minor', 'micro'])

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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'documents.document': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Document'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'document_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documents'", 'to': u"orm['documents.DocumentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "u'Uninitialized document'", 'max_length': '255', 'db_index': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "u'eng'", 'max_length': '8'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "u'840ee754-cd01-4a28-b17c-e432e32356bb'", 'max_length': '48'})
        },
        u'documents.documentpage': {
            'Meta': {'ordering': "['page_number']", 'object_name': 'DocumentPage'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'document_version': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pages'", 'to': u"orm['documents.DocumentVersion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_label': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'page_number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'})
        },
        u'documents.documentpagetransformation': {
            'Meta': {'ordering': "('order',)", 'object_name': 'DocumentPageTransformation'},
            'arguments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'document_page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['documents.DocumentPage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'transformation': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'documents.documenttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'DocumentType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'ocr': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'documents.documenttypefilename': {
            'Meta': {'ordering': "['filename']", 'object_name': 'DocumentTypeFilename'},
            'document_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'filenames'", 'to': u"orm['documents.DocumentType']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'documents.documentversion': {
            'Meta': {'object_name': 'DocumentVersion'},
            'checksum': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'versions'", 'to': u"orm['documents.Document']"}),
            'encoding': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mimetype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'documents.recentdocument': {
            'Meta': {'ordering': "('-datetime_accessed',)", 'object_name': 'RecentDocument'},
            'datetime_accessed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['documents.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['documents']
