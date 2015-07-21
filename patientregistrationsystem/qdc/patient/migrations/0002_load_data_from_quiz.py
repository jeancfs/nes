# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

        for old in orm['quiz.AlcoholFrequency'].objects.all():
            new = orm.AlcoholFrequency(id=old.id,
                                       name=old.name)
            new.save()

        for old in orm['quiz.AlcoholPeriod'].objects.all():
            new = orm.AlcoholPeriod(id=old.id,
                                    name=old.name)
            new.save()

        for old in orm['quiz.AmountCigarettes'].objects.all():
            new = orm.AmountCigarettes(id=old.id,
                                       name=old.name)
            new.save()

        for old in orm['quiz.Fleshtone'].objects.all():
            new = orm.Fleshtone(id=old.id,
                                name=old.name)
            new.save()

        for old in orm['quiz.Gender'].objects.all():
            new = orm.Gender(id=old.id,
                             name=old.name)
            new.save()

        for old in orm['quiz.MaritalStatus'].objects.all():
            new = orm.MaritalStatus(id=old.id,
                                    name=old.name)
            new.save()

        for old in orm['quiz.Payment'].objects.all():
            new = orm.Payment(id=old.id,
                              name=old.name)
            new.save()

        for old in orm['quiz.Religion'].objects.all():
            new = orm.Religion(id=old.id,
                               name=old.name)
            new.save()

        for old in orm['quiz.Schooling'].objects.all():
            new = orm.Schooling(id=old.id,
                                name=old.name)
            new.save()

        for old in orm['quiz.ClassificationOfDiseases'].objects.all():
            new = orm.ClassificationOfDiseases(id=old.id,
                                               code=old.code,
                                               description=old.description,
                                               abbreviated_description=old.abbreviated_description,
                                               parent_id=old.parent_id)
            new.save()

        for old in orm['quiz.Patient'].objects.all():
            new = orm.Patient(id=old.id,
                              cpf=old.cpf,
                              rg=old.rg,
                              name=old.name,
                              medical_record=old.medical_record,
                              natural_of=old.natural_of,
                              citizenship=old.citizenship,
                              street=old.street,
                              address_number=old.address_number,
                              district=old.district,
                              address_complement=old.address_complement,
                              zipcode=old.zipcode,
                              country=old.country,
                              state=old.state,
                              city=old.city,
                              phone=old.phone,
                              cellphone=old.cellphone,
                              email=old.email,
                              date_birth=old.date_birth,
                              gender_id=old.gender_id,
                              marital_status_id=old.marital_status_id,
                              removed=old.removed,
                              changed_by_id=old.changed_by_id)
            new.save()

        for old in orm['quiz.SocialDemographicData'].objects.all():
            new = orm.SocialDemographicData(id=old.id,
                                            patient_id=old.patient_id,
                                            religion_id=old.religion_id,
                                            profession=old.profession,
                                            occupation=old.occupation,
                                            benefit_government=old.benefit_government,
                                            payment_id=old.payment_id,
                                            flesh_tone_id=old.flesh_tone_id,
                                            schooling_id=old.schooling_id,
                                            tv=old.tv,
                                            dvd=old.dvd,
                                            radio=old.radio,
                                            bath=old.bath,
                                            automobile=old.automobile,
                                            wash_machine=old.wash_machine,
                                            refrigerator=old.refrigerator,
                                            freezer=old.freezer,
                                            house_maid=old.house_maid,
                                            social_class=old.social_class,
                                            changed_by_id=old.changed_by_id)
            new.save()

        for old in orm['quiz.HistoricalPatient'].objects.all():
            new = orm.HistoricalPatient(id=old.id,
                                        cpf=old.cpf,
                                        rg=old.rg,
                                        name=old.name,
                                        medical_record=old.medical_record,
                                        natural_of=old.natural_of,
                                        citizenship=old.citizenship,
                                        street=old.street,
                                        address_number=old.address_number,
                                        district=old.district,
                                        address_complement=old.address_complement,
                                        zipcode=old.zipcode,
                                        country=old.country,
                                        state=old.state,
                                        city=old.city,
                                        phone=old.phone,
                                        cellphone=old.cellphone,
                                        email=old.email,
                                        date_birth=old.date_birth,
                                        gender_id=old.gender_id,
                                        marital_status_id=old.marital_status_id,
                                        removed=old.removed,
                                        changed_by_id=old.changed_by_id,
                                        history_id=old.history_id,
                                        history_date=old.history_date,
                                        history_user_id=old.history_user_id,
                                        history_type=old.history_type)
            new.save()

        for old in orm['quiz.HistoricalSocialDemographicData'].objects.all():
            new = orm.HistoricalSocialDemographicData(id=old.id,
                                                      patient_id=old.patient_id,
                                                      religion_id=old.religion_id,
                                                      profession=old.profession,
                                                      occupation=old.occupation,
                                                      benefit_government=old.benefit_government,
                                                      payment_id=old.payment_id,
                                                      flesh_tone_id=old.flesh_tone_id,
                                                      schooling_id=old.schooling_id,
                                                      tv=old.tv,
                                                      dvd=old.dvd,
                                                      radio=old.radio,
                                                      bath=old.bath,
                                                      automobile=old.automobile,
                                                      wash_machine=old.wash_machine,
                                                      refrigerator=old.refrigerator,
                                                      freezer=old.freezer,
                                                      house_maid=old.house_maid,
                                                      social_class=old.social_class,
                                                      changed_by_id=old.changed_by_id,
                                                      history_id=old.history_id,
                                                      history_date=old.history_date,
                                                      history_user_id=old.history_user_id,
                                                      history_type=old.history_type)
            new.save()

        for old in orm['quiz.HistoricalSocialHistoryData'].objects.all():
            new = orm.HistoricalSocialHistoryData(id=old.id,
                                                  patient_id=old.patient_id,
                                                  smoker=old.smoker,
                                                  amount_cigarettes_id=old.amount_cigarettes_id,
                                                  ex_smoker=old.ex_smoker,
                                                  alcoholic=old.alcoholic,
                                                  alcohol_frequency_id=old.alcohol_frequency_id,
                                                  alcohol_period_id=old.alcohol_period_id,
                                                  drugs=old.drugs,
                                                  changed_by_id=old.changed_by_id,
                                                  history_id=old.history_id,
                                                  history_date=old.history_date,
                                                  history_user_id=old.history_user_id,
                                                  history_type=old.history_type)
            new.save()

        for old in orm['quiz.SocialHistoryData'].objects.all():
            new = orm.SocialHistoryData(id=old.id,
                                        patient_id=old.patient_id,
                                        smoker=old.smoker,
                                        amount_cigarettes_id=old.amount_cigarettes_id,
                                        ex_smoker=old.ex_smoker,
                                        alcoholic=old.alcoholic,
                                        alcohol_frequency_id=old.alcohol_frequency_id,
                                        alcohol_period_id=old.alcohol_period_id,
                                        drugs=old.drugs,
                                        changed_by_id=old.changed_by_id)
            new.save()

        for old in orm['quiz.MedicalRecordData'].objects.all():
            new = orm.MedicalRecordData(id=old.id,
                                        patient_id=old.patient_id,
                                        record_date=old.record_date,
                                        record_responsible_id=old.record_responsible_id)
            new.save()

        for old in orm['quiz.Diagnosis'].objects.all():
            new = orm.Diagnosis(id=old.id,
                                medical_record_data_id=old.medical_record_data_id,
                                classification_of_diseases_id=old.classification_of_diseases_id,
                                date=old.date,
                                description=old.description)
            new.save()


        for old in orm['quiz.ComplementaryExam'].objects.all():
            new = orm.ComplementaryExam(id=old.id,
                                        diagnosis_id=old.diagnosis_id,
                                        date=old.date,
                                        description=old.description,
                                        doctor=old.doctor,
                                        doctor_register=old.doctor_register,
                                        exam_site=old.exam_site)
            new.save()


        for old in orm['quiz.ExamFile'].objects.all():
            new = orm.ExamFile(id=old.id,
                               exam_id=old.exam_id,
                               content=old.content)
            new.save()

    def backwards(self, orm):
        "Write your backwards methods here."

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
        u'patient.alcoholfrequency': {
            'Meta': {'object_name': 'AlcoholFrequency'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'patient.alcoholperiod': {
            'Meta': {'object_name': 'AlcoholPeriod'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'patient.amountcigarettes': {
            'Meta': {'object_name': 'AmountCigarettes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'patient.classificationofdiseases': {
            'Meta': {'object_name': 'ClassificationOfDiseases'},
            'abbreviated_description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'children'", 'null': 'True', 'to': u"orm['patient.ClassificationOfDiseases']"})
        },
        u'patient.complementaryexam': {
            'Meta': {'object_name': 'ComplementaryExam'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Diagnosis']"}),
            'doctor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'doctor_register': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'exam_site': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'patient.diagnosis': {
            'Meta': {'unique_together': "((u'medical_record_data', u'classification_of_diseases'),)", 'object_name': 'Diagnosis'},
            'classification_of_diseases': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.ClassificationOfDiseases']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medical_record_data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.MedicalRecordData']"})
        },
        u'patient.examfile': {
            'Meta': {'object_name': 'ExamFile'},
            'content': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'exam': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.ComplementaryExam']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'patient.fleshtone': {
            'Meta': {'object_name': 'FleshTone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'patient.gender': {
            'Meta': {'object_name': 'Gender'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'patient.historicalpatient': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalPatient'},
            'address_complement': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'address_number': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'cellphone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'changed_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'citizenship': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cpf': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'date_birth': ('django.db.models.fields.DateField', [], {}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'gender_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'marital_status_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'medical_record': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'natural_of': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'removed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'})
        },
        u'patient.historicalsocialdemographicdata': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalSocialDemographicData'},
            'automobile': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bath': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'benefit_government': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'changed_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'dvd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'flesh_tone_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'freezer': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'house_maid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'patient_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'payment_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'radio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'refrigerator': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'religion_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'schooling_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'social_class': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tv': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wash_machine': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'patient.historicalsocialhistorydata': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalSocialHistoryData'},
            'alcohol_frequency_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'alcohol_period_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'alcoholic': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'amount_cigarettes_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'changed_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'drugs': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'ex_smoker': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'patient_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'smoker': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'patient.maritalstatus': {
            'Meta': {'object_name': 'MaritalStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'patient.medicalrecorddata': {
            'Meta': {'object_name': 'MedicalRecordData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Patient']"}),
            'record_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'record_responsible': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'patient.patient': {
            'Meta': {'object_name': 'Patient'},
            'address_complement': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'address_number': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'cellphone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'citizenship': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'date_birth': ('django.db.models.fields.DateField', [], {}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Gender']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marital_status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.MaritalStatus']", 'null': 'True', 'blank': 'True'}),
            'medical_record': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'natural_of': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'removed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'})
        },
        u'patient.payment': {
            'Meta': {'object_name': 'Payment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'patient.religion': {
            'Meta': {'object_name': 'Religion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'patient.schooling': {
            'Meta': {'object_name': 'Schooling'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'patient.socialdemographicdata': {
            'Meta': {'object_name': 'SocialDemographicData'},
            'automobile': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bath': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'benefit_government': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'dvd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'flesh_tone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.FleshTone']", 'null': 'True', 'blank': 'True'}),
            'freezer': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'house_maid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Patient']"}),
            'payment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Payment']", 'null': 'True', 'blank': 'True'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'radio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'refrigerator': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'religion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Religion']", 'null': 'True', 'blank': 'True'}),
            'schooling': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Schooling']", 'null': 'True', 'blank': 'True'}),
            'social_class': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tv': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wash_machine': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'patient.socialhistorydata': {
            'Meta': {'object_name': 'SocialHistoryData'},
            'alcohol_frequency': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['patient.AlcoholFrequency']", 'null': 'True', 'blank': 'True'}),
            'alcohol_period': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['patient.AlcoholPeriod']", 'null': 'True', 'blank': 'True'}),
            'alcoholic': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'amount_cigarettes': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['patient.AmountCigarettes']", 'null': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'drugs': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'ex_smoker': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Patient']"}),
            'smoker': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'quiz.alcoholfrequency': {
            'Meta': {'object_name': 'AlcoholFrequency'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'quiz.alcoholperiod': {
            'Meta': {'object_name': 'AlcoholPeriod'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'quiz.amountcigarettes': {
            'Meta': {'object_name': 'AmountCigarettes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'quiz.classificationofdiseases': {
            'Meta': {'object_name': 'ClassificationOfDiseases'},
            'abbreviated_description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'children'", 'null': 'True', 'to': u"orm['quiz.ClassificationOfDiseases']"})
        },
        u'quiz.complementaryexam': {
            'Meta': {'object_name': 'ComplementaryExam'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Diagnosis']"}),
            'doctor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'doctor_register': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'exam_site': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'quiz.diagnosis': {
            'Meta': {'unique_together': "((u'medical_record_data', u'classification_of_diseases'),)", 'object_name': 'Diagnosis'},
            'classification_of_diseases': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.ClassificationOfDiseases']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medical_record_data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.MedicalRecordData']"})
        },
        u'quiz.examfile': {
            'Meta': {'object_name': 'ExamFile'},
            'content': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'exam': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.ComplementaryExam']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'quiz.fleshtone': {
            'Meta': {'object_name': 'FleshTone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'quiz.gender': {
            'Meta': {'object_name': 'Gender'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'quiz.historicalpatient': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalPatient'},
            'address_complement': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'address_number': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'cellphone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'changed_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'citizenship': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cpf': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'date_birth': ('django.db.models.fields.DateField', [], {}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'gender_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'marital_status_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'medical_record': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'natural_of': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'removed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'})
        },
        u'quiz.historicalsocialdemographicdata': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalSocialDemographicData'},
            'automobile': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bath': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'benefit_government': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'changed_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'dvd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'flesh_tone_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'freezer': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'house_maid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'patient_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'payment_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'radio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'refrigerator': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'religion_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'schooling_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'social_class': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tv': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wash_machine': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'quiz.historicalsocialhistorydata': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalSocialHistoryData'},
            'alcohol_frequency_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'alcohol_period_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'alcoholic': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'amount_cigarettes_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'changed_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'drugs': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'ex_smoker': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'patient_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'smoker': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'quiz.maritalstatus': {
            'Meta': {'object_name': 'MaritalStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'quiz.medicalrecorddata': {
            'Meta': {'object_name': 'MedicalRecordData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Patient']"}),
            'record_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'record_responsible': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'quiz.patient': {
            'Meta': {'object_name': 'Patient'},
            'address_complement': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'address_number': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'cellphone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'citizenship': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'date_birth': ('django.db.models.fields.DateField', [], {}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Gender']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marital_status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.MaritalStatus']", 'null': 'True', 'blank': 'True'}),
            'medical_record': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'natural_of': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'removed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'})
        },
        u'quiz.payment': {
            'Meta': {'object_name': 'Payment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'quiz.religion': {
            'Meta': {'object_name': 'Religion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'quiz.schooling': {
            'Meta': {'object_name': 'Schooling'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'quiz.socialdemographicdata': {
            'Meta': {'object_name': 'SocialDemographicData'},
            'automobile': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bath': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'benefit_government': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'dvd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'flesh_tone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.FleshTone']", 'null': 'True', 'blank': 'True'}),
            'freezer': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'house_maid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Patient']"}),
            'payment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Payment']", 'null': 'True', 'blank': 'True'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'radio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'refrigerator': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'religion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Religion']", 'null': 'True', 'blank': 'True'}),
            'schooling': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Schooling']", 'null': 'True', 'blank': 'True'}),
            'social_class': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tv': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wash_machine': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'quiz.socialhistorydata': {
            'Meta': {'object_name': 'SocialHistoryData'},
            'alcohol_frequency': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['quiz.AlcoholFrequency']", 'null': 'True', 'blank': 'True'}),
            'alcohol_period': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['quiz.AlcoholPeriod']", 'null': 'True', 'blank': 'True'}),
            'alcoholic': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'amount_cigarettes': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['quiz.AmountCigarettes']", 'null': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'drugs': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'ex_smoker': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Patient']"}),
            'smoker': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['patient']
    symmetrical = True
