/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2021/10/18 23:01:35                          */
/*==============================================================*/


/*==============================================================*/
/* Table: course                                                */
/*==============================================================*/
create table course
(
   c_id                 char(10) not null,
   lab_id               char(10),
   c_name               char(16),
   c_teacher            char(16),
   c_hours              float,
   c_credit             float,
   c_numbers            int,
   primary key (c_id)
);

/*==============================================================*/
/* Table: lab                                                   */
/*==============================================================*/
create table lab
(
   lab_id               char(10) not null,
   m_id                 char(10),
   lab_name             char(16) not null,
   lab_address          char(10) not null,
   lab_area             float not null,
   lab_numbers          int not null,
   lab_computer         char(40) not null,
   primary key (lab_id)
);

/*==============================================================*/
/* Table: manager                                               */
/*==============================================================*/
create table manager
(
   m_id                 char(10) not null,
   m_name               char(16),
   primary key (m_id)
);

/*==============================================================*/
/* Table: software                                              */
/*==============================================================*/
create table software
(
   s_id                 char(10) not null,
   t_id                 char(10),
   s_name               char(16) not null,
   s_version            char(30),
   s_volume             float,
   primary key (s_id)
);

/*==============================================================*/
/* Table: software_lab                                          */
/*==============================================================*/
create table software_lab
(
   lab_id               char(10) not null,
   s_id                 char(10) not null,
   primary key (lab_id, s_id)
);

/*==============================================================*/
/* Table: student                                               */
/*==============================================================*/
create table student
(
   t_id                 char(10) not null,
   t_name               char(10),
   primary key (t_id)
);

/*==============================================================*/
/* Table: student_course                                        */
/*==============================================================*/
create table student_course
(
   c_id                 char(10) not null,
   t_id                 char(10) not null,
   primary key (c_id, t_id)
);

/*==============================================================*/
/* Table: teacher                                               */
/*==============================================================*/
create table teacher
(
   t_id                 char(10) not null,
   t_name               char(16),
   primary key (t_id)
);

/*==============================================================*/
/* Table: teacher_course                                        */
/*==============================================================*/
create table teacher_course
(
   c_id                 char(10) not null,
   t_id                 char(10) not null,
   primary key (c_id, t_id)
);

/*==============================================================*/
/* Table: type                                                  */
/*==============================================================*/
create table type
(
   t_id                 char(10) not null,
   t_name               char(16),
   primary key (t_id)
);

/*==============================================================*/
/* Table: user                                                  */
/*==============================================================*/
create table user
(
   u_id                 char(10) not null,
   t_id                 char(10),
   u_name               char(16),
   u_lab                char(16),
   u_time               datetime,
   primary key (u_id)
);

/*==============================================================*/
/* Index: use_time                                              */
/*==============================================================*/
create index use_time on user
(
   u_time
);

/*==============================================================*/
/* View: ViewLabManager                                         */
/*==============================================================*/
create  VIEW      ViewLabManager
  as
select
   lab.lab_id,
   lab.lab_name,
   manager.m_id,
   manager.m_name,
   user.u_lab,
   user.u_time
from
   lab,
   manager,
   user
where 
   manager.m_id = lab.m_id and user.t_id = manager.m_id;

alter table course add constraint FK_course_lab foreign key (lab_id)
      references lab (lab_id) on delete restrict on update restrict;

alter table lab add constraint FK_manager_lab foreign key (m_id)
      references manager (m_id) on delete restrict on update restrict;

alter table software add constraint FK_software_type foreign key (t_id)
      references type (t_id) on delete restrict on update restrict;

alter table software_lab add constraint FK_software_lab foreign key (lab_id)
      references lab (lab_id) on delete restrict on update restrict;

alter table software_lab add constraint FK1_software_lab foreign key (s_id)
      references software (s_id) on delete restrict on update restrict;

alter table student_course add constraint FK_student_course foreign key (c_id)
      references course (c_id) on delete restrict on update restrict;

alter table student_course add constraint FK1_student_course foreign key (t_id)
      references student (t_id) on delete restrict on update restrict;

alter table teacher_course add constraint FK2_teacher_course foreign key (c_id)
      references course (c_id) on delete restrict on update restrict;

alter table teacher_course add constraint FK3_teacher_course foreign key (t_id)
      references teacher (t_id) on delete restrict on update restrict;

alter table user add constraint FK_manager_user foreign key (t_id)
      references manager (m_id) on delete restrict on update restrict;

alter table user add constraint FK_student_user foreign key (t_id)
      references student (t_id) on delete restrict on update restrict;

alter table user add constraint FK_teacher_user foreign key (t_id)
      references teacher (t_id) on delete restrict on update restrict;
      
DELIMITER ;;

CREATE TRIGGER manager_before_delete
    BEFORE DELETE ON manager
    FOR EACH ROW
BEGIN
    DELETE FROM lab
    WHERE lab.m_id = manager.m_id;
END;;

DELIMITER ;


