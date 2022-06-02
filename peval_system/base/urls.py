from django.contrib import admin
from django.urls import path, include 
from . import views
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve



app_name = 'base'

urlpatterns =[
    path("profile", views.view_profile, name='view_profile'),
    path("view_perf_info/", views.view_perf_info, name='view_perf_info'),
    
    path("add_educ_att", views.add_educ_att, name='add_educ_att'),
    path("add_workexp", views.add_workexp, name='add_workexp'),
    path("add_pub", views.add_pub, name='add_pub'),
    path("add_acc_events", views.add_acc_events, name='add_acc_events'),
    path("add_res_grants", views.add_res_grants, name='add_res_grants'),
    path("add_licexam", views.add_licexam, name='add_licexam'),
    path("add_trainsem", views.add_trainsem, name='add_trainsem'),
    path("add_confwork", views.add_confwork, name='add_confwork'),
    path("add_extserv", views.add_extserv, name='add_extserv'),
    path("add_facultyservrec", views.add_facultyservrec, name='add_facultyservrec'),

    path("edit_educ_att/<int:pk>/", views.edit_educ_att, name='edit_educ_att'),
    path("edit_workexp/<int:pk>/", views.edit_workexp, name='edit_workexp'),
    path("edit_acc_events/<int:pk>/", views.edit_acc_events, name='edit_acc_events'),
    path("edit_pub/<int:pk>/", views.edit_pub, name='edit_pub'),
    path("edit_res_grants/<int:pk>/", views.edit_res_grants, name='edit_res_grants'),
	path("edit_licexam/<int:pk>/", views.edit_licexam, name='edit_licexam'),
    path("edit_trainsem/<int:pk>/", views.edit_trainsem, name='edit_trainsem'),
    path("edit_confwork/<int:pk>/", views.edit_confwork, name='edit_confwork'),
    path("edit_extserv/<int:pk>/", views.edit_extserv, name='edit_extserv'),
    path("edit_facservrec/<int:pk>/", views.edit_facservrec, name='edit_facservrec'),
    
    path("delete_educ_att/<int:pk>/", views.delete_educ_att, name='delete_educ_att'),
    path("delete_workexp/<int:pk>/", views.delete_workexp, name='delete_workexp'),
    path("delete_acc_events/<int:pk>/", views.delete_acc_events, name='delete_acc_events'),
    path("delete_pub/<int:pk>/", views.delete_pub, name='delete_pub'),
    path("delete_res_grants/<int:pk>/", views.delete_res_grants, name='delete_res_grants'),
    path("delete_licexam/<int:pk>/", views.delete_licexam, name='delete_licexam'),
    path("delete_trainsem/<int:pk>/", views.delete_trainsem, name='delete_trainsem'),
    path("delete_confwork/<int:pk>/", views.delete_confwork, name='delete_confwork'),
    path("delete_extserv/<int:pk>/", views.delete_extserv, name='delete_extserv'),
    path("delete_facservrec/<int:pk>/", views.delete_facservrec, name='delete_facservrec'),

    path("admin_dash/", views.admin_dash, name='admin_dash'),
    path("edit_user/<int:pk>/", views.edit_user, name='edit_user'),
    path("edit_pers_info/<int:pk>/", views.edit_pers_info, name='edit_pers_info'),
    path("update_set/<int:pk>/", views.update_set, name='update_set'),
    path("add_facultyservrec_clerk/", views.add_facultyservrec_clerk, name='add_facultyservrec_clerk'),
    path("faculty_load/", views.faculty_load, name='faculty_load'),

    path("unithead_dashboard", views.unit_dash_view, name='unithead_dashboard'),
    path("unithead_dashboard_table", views.unit_table_view,name="unithead_dashboard_table"),
    path("unithead_faculty_list", views.unit_faculty_view, name='unithead_faculty_list'),
    path("unithead_role_assignment", views.unit_assignment_view, name='unithead_role_assignment'),
    path("unithead_pending_approvals", views.unithead_pending_approvals, name='unithead_pending_approvals'),

    path("accomView", views.accomView, name="accomView"),
    path("deptchair_dashboard", views.dept_dash_view, name='deptchair_dashboard'),
    path("deptchair_dashboard_table", views.dept_table_view,name="deptchair_dashboard_table"),
    path("deptchair_faculty_list", views.dept_faculty_view, name='deptchair_faculty_list'),
    path("deptchair_role_assignment", views.dept_assignment_view, name='deptchair_role_assignment'),
    path("deptchair_pending_approvals", views.deptchair_pending_approvals, name='deptchair_pending_approvals'),
    path("deptchair_add_clerk", views.dept_clerk_view, name='deptchair_add_clerk'),
    path("export_excel_accom", views.export_excel_accom, name="export_excel_accom"),

    path("approve_educ_att/<int:pk>", views.approve_educ_att, name="approve_educ_att"),
    path("approve_work_exp/<int:pk>", views.approve_work_exp, name="approve_work_exp"),
    path("approve_acc_events/<int:pk>", views.approve_acc_events, name="approve_acc_events"),
    path("approve_pub/<int:pk>", views.approve_pub, name="approve_pub"),
    path("approve_res_grant/<int:pk>", views.approve_res_grant, name="approve_res_grant"),
    path("approve_licexam/<int:pk>", views.approve_licexam, name="approve_licexam"),
    path("approve_trainsem/<int:pk>", views.approve_trainsem, name="approve_trainsem"),
    path("approve_confwork/<int:pk>", views.approve_confwork, name="approve_confwork"),
    path("approve_extserv/<int:pk>", views.approve_extserv, name="approve_extserv"),
    path("approve_facservrec/<int:pk>", views.approve_facservrec, name="approve_facservrec"),
    path("assign_deptchair/<int:pk>", views.assign_deptchair, name="assign_deptchair"),
    
    path("verify_educ_att/<int:pk>", views.verify_educ_att, name="verify_educ_att"),
    path("verify_work_exp/<int:pk>", views.verify_work_exp, name="verify_work_exp"),
    path("verify_acc_events/<int:pk>", views.verify_acc_events, name="verify_acc_events"),
    path("verify_pub/<int:pk>", views.verify_pub, name="verify_pub"),
    path("verify_res_grant/<int:pk>", views.verify_res_grant, name="verify_res_grant"),
    path("verify_licexam/<int:pk>", views.verify_licexam, name="verify_licexam"),
    path("verify_trainsem/<int:pk>", views.verify_trainsem, name="verify_trainsem"),
    path("verify_confwork/<int:pk>", views.verify_confwork, name="verify_confwork"),
    path("verify_extserv/<int:pk>", views.verify_extserv, name="verify_extserv"),
    path("verify_facservrec/<int:pk>", views.verify_facservrec, name="verify_facservrec"),
    path("assign_unithead/<int:pk>", views.assign_unithead, name="assign_unithead"),
    

]

urlpatterns += static(settings.UPLOAD_URL, document_root=settings.UPLOAD_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.)