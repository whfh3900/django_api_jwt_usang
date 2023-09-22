# serializers.py
from rest_framework import serializers
from .models import UsangData

class UsangDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsangData
        fields = '__all__'
        fields = ["cst_cnt", "pst_cnt", "cst_iss_val", "pst_iss_val", \
                "pre_cst_val", "pre_pst_val", "pre_cst_val_dt", \
                "pre_pst_val_dt", "all_bs_dt", "new_asn_cnt", "emp_bgn_dt", \
                "emp_end_dt", "sh_bgn_dt", "sh_end_dt", "pym_dt", "prc_pln", \
                "lst_pln_dt", "chf_agn", "nst_gv_yn", "fip_cm", "nst_rm", \
                "nst_sch_dt", "notes", "recei_dt",]


