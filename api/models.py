from django.db import models

# Create your models here.
class UsangData(models.Model):
    id = models.IntegerField(primary_key=True)
    cst_cnt = models.CharField(max_length=255)
    pst_cnt = models.CharField(max_length=255)
    cst_iss_val = models.CharField(max_length=255)
    pst_iss_val = models.CharField(max_length=255)
    pre_cst_val = models.CharField(max_length=255)
    pre_pst_val = models.CharField(max_length=255)
    pre_cst_val_dt = models.DateField()
    pre_pst_val_dt = models.DateField()
    all_bs_dt = models.DateField()
    new_asn_cnt = models.CharField(max_length=255)
    emp_bgn_dt = models.DateField()
    emp_end_dt = models.DateField()
    sh_bgn_dt = models.DateField()
    sh_end_dt = models.DateField()
    pym_dt = models.DateField()
    prc_pln = models.TextField()
    lst_pln_dt = models.DateField()
    chf_agn = models.CharField(max_length=255)
    nst_gv_yn = models.CharField(max_length=255)
    fip_cm = models.TextField()
    nst_rm = models.TextField()
    nst_sch_dt = models.CharField(max_length=255)
    ci_mth = models.CharField(max_length=255)
    notes = models.TextField()
    recei_dt = models.DateField()
    pub_ann_dt = models.CharField()
    
    class Meta:
        app_label = 'myapp'
        db_table = 'usang_data'
        # using = "default"
