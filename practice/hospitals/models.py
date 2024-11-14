from django.db import models

# M
# Doctor 모델에서 Patient에 접근하려면 역참조
# patient_set
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

# N
# Patient 모델에서 Doctor에 접근하려면 참조
# doctors 속성
class Patient(models.Model):
    # ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
    
# ORM 코드
doctor1 = Doctor.objects.create(name='allie')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='duke')
# 1번 patient1에 doctor1 추가
patient1.doctors.add(doctor1)
# 2번 doctor1에 patient2 추가
doctor1.patient_set.add(patient2)
# 3번 doctor1에 patient1 추가
doctor1.patient_set.remove(patient1
                           )
