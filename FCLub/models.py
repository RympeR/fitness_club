from sqlalchemy import Column, Integer, String, Date, Numeric, Boolean, Time, ForeignKey

from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class position(db.Model):
    __tablename__ = 'position'
    position_name = Column(String(50), primary_key=True)

    def __init__(self, position_name):
        self.position_name = position_name

    def __repr__(self):
        return "<position '%s'>" % self.position_name


class client(db.Model):
    __tablename__ = 'client'
    card_number_client = Column(Integer, primary_key=True)
    name_client = Column(String(30), nullable=False)
    surname_client = Column(String(80), nullable=False)
    patronomyc_client = Column(String(50), nullable=False)
    mobile_telephone_client = Column(String(12), nullable=False, unique=True)
    review = Column(String(300), nullable=True)

    abonements = relationship('abonement', order_by='abonement.id_abonement', backref='client')

    def __init__(self, card_number_client, name_client, surname_client, patronomyc_client, mobile_telephone_client,
                 review):
        self.card_number_client = card_number_client
        self.name_client = name_client
        self.surname_client = surname_client
        self.patronomyc_client = patronomyc_client
        self.mobile_telephone_client = mobile_telephone_client
        self.review = review

    def __repr__(self):
        return "<client ('%s','%s','%s','%s','%s','%s'>" % (self.card_number_client,self.name_client,self.surname_client,self.patronomyc_client,self.mobile_telephone_client,self.review)


class service(db.Model):
    __tablename__ = 'service'
    id_service = Column(Integer, primary_key=True)
    specialization_service = Column(String(30), nullable=False)
    type_service = Column(String(40), nullable=False)

    servstaff = relationship('staff', order_by='staff.id_staff', backref='service')
    abonements = relationship('abonement', order_by='abonement.id_abonement', backref='service')

    def __init__(self, id_service, specialization_service, type_service):
        self.id_service = id_service
        self.specialization_service = specialization_service
        self.type_service = type_service

    def __repr__(self):
        return "<service '%s','%s','%s'>" % (self.id_service,self.specialization_service,self.type_service)


class roles(db.Model):
    __tablename__ = 'roles'
    id_role = Column(Integer, primary_key=True)
    name_of_role = Column(String(20), nullable=False)

    users = relationship('staff', backref='role')

    def __init__(self, id_role, name_of_role):
        self.id_role = id_role
        self.name_of_role = name_of_role

    def __repr__(self):
        return "<roles '%s','%s'>" % (self.id_role, self.name_of_role)


class staff(db.Model):
    __tablename__ = 'staff'
    id_staff = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey('service.id_service'), nullable=False)
    name_staff = Column(String(30), nullable=False)
    surname_staff = Column(String(80), nullable=False)
    patronomyc_staff = Column(String(50), nullable=False)
    mobile_telephone_staff = Column(String(12), nullable=False, unique=True)
    position_staff = Column(String(50), nullable=False)
    salary_ = Column(Numeric, nullable=False)
    login = Column(String(20), unique=True, nullable=False)
    passw = Column(String(20), nullable=False)
    role_to_login = Column(Integer, ForeignKey('roles.id_role'), nullable=False)

    vacations = relationship('vacation', order_by='vacation.begin_date_vacation', backref='staff')
    workshifts = relationship('workshift', order_by='workshift.date_workshift', backref='staff')

    def __init__(self, id_staff, service_id, name_staff, surname_staff, patronomyc_staff, mobile_telephone_staff, position_staff, salary_, login, passw, role_to_login):
        self.id_staff = id_staff
        self.service_id = service_id
        self.name_staff = name_staff
        self.surname_staff = surname_staff
        self.patronomyc_staff = patronomyc_staff
        self.mobile_telephone_staff = mobile_telephone_staff
        self.position_staff = position_staff
        self.salary_ = salary_
        self.login = login
        self.passw = passw
        self.role_to_login = role_to_login

    def __repr__(self):
        return "<staff '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'>" % (self.id_staff, self.service_id, self.name_staff, self.surname_staff, self.patronomyc_staff, self.mobile_telephone_staff, self.position_staff, self.salary_, self.login, self.passw, self.role_to_login)


class vacation(db.Model):
    __tablename__ = 'vacation'
    id_vacation = Column(Integer, primary_key=True)
    vacation_staff = Column(Integer, ForeignKey('staff.id_staff'), nullable=False)
    begin_date_vacation = Column(Date, nullable=False)
    end_date_vacation = Column(Date, nullable=False)
    paid = Column(Boolean, nullable=False)

    def __init__(self, id_vacation, vacation_staff, begin_date_vacation, end_date_vacation, paid):
        self.id_vacation = id_vacation
        self.vacation_staff = vacation_staff
        self.begin_date_vacation = begin_date_vacation
        self.end_date_vacation = end_date_vacation
        self.paid = paid

    def __repr__(self):
        return "<vacation '%s','%s','%s','%s','%s'>" % (self.id_vacation,self.vacation_staff, self.begin_date_vacation, self.end_date_vacation, self.paid)


class workshift(db.Model):
    __tablename__ = 'workshift'
    id_workshift = Column(Integer, primary_key=True)
    workshift_staff = Column(Integer, ForeignKey('staff.id_staff'), nullable=False)
    date_workshift = Column(String(15), nullable=False)
    begin_time_workshift = Column(Time, nullable=False)
    end_time_workshift = Column(Time, nullable=False)

    def __init__(self, id_workshift, workshift_staff, date_workshift, begin_time_workshift, end_time_workshift):
        self.id_workshift = id_workshift
        self.workshift_staff = workshift_staff
        self.date_workshift = date_workshift
        self.begin_time_workshift = begin_time_workshift
        self.end_time_workshift = end_time_workshift

    def __repr__(self):
        return "<workshift '%s','%s','%s','%s','%s'>" % (self.id_workshift, self.workshift_staff, self.date_workshift, self.begin_time_workshift, self.end_time_workshift)


class abonement(db.Model):
    __tablename__ = 'abonement'
    id_abonement = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey('service.id_service'), nullable=False)
    cardnumber_abonement = Column(Integer, ForeignKey('client.card_number_client'), nullable=False)
    begindate_abonement = Column(Date, nullable=False)
    enddate_abonement = Column(Date, nullable=False)
    isactive_abonement = Column(Boolean, nullable=False)
    cost_abonement_ = Column(Numeric, nullable=False)

    def __init__(self, id_abonement, service_id, cardnumber_abonement, begindate_abonement, enddate_abonement, isactive_abonement,cost_abonement_):
        self.id_abonement = id_abonement
        self.service_id = service_id
        self.cardnumber_abonement = cardnumber_abonement
        self.begindate_abonement = begindate_abonement
        self.enddate_abonement = enddate_abonement
        self.isactive_abonement = isactive_abonement
        self.cost_abonement_ = cost_abonement_

    def __repr__(self):
        return "<abonement '%s','%s','%s','%s','%s','%s','%s'>" % (self.id_abonement, self.service_id, 
                self.cardnumber_abonement, self.begindate_abonement, self.enddate_abonement, self.isactive_abonement,self.cost_abonement_)

class cost_ab(db.Model):
    __tablename__ = 'cost_ab'
    id_ca = Column(Integer, primary_key=True)
    durationmonths = Column(Integer, nullable=False)
    serv_id = Column(Integer, ForeignKey('service.id_service'), nullable=False)
    cost_ = Column(Numeric, nullable=False)

    def __init_(self, id_ca, durationmonths, serv_id, cost_):
        self.id_ca = id_ca
        self.durationmonths = durationmonths
        self.serv_id = serv_id
        self.cost_ = cost_      

    def __repr__(self):
        return "<cost_ab '%s','%s','%s','%s'>" % (self.id_ca, self.durationmonths, self.serv_id, self.cost_)


class record(db.Model):
    __tablename__ = "record"
    id_record = Column(Integer, primary_key=True)
    day_record = Column(String(15), nullable=False)
    cardnumber_client_record = Column(Integer, ForeignKey('client.card_number_client'), nullable=False)
    time_beginrecord = Column(Time, nullable=False)
    time_endrecord = Column(Time, nullable=False)
    id_staff_record = Column(Integer, ForeignKey('staff.id_staff'), nullable=False)

    def __init__ (self, id_record, day_record, cardnumber_client_record, time_beginrecord, time_endrecord, id_staff_record):
        self.id_record = id_record
        self.day_record = day_record
        self.cardnumber_client_record = cardnumber_client_record
        self.time_beginrecord = time_beginrecord
        self.time_endrecord = time_endrecord
        self.id_staff_record = id_staff_record

    def __repr__(self):
        return "<record '%s','%s','%s','%s','%s','%s'>" % (self.id_record, self.day_record, self.cardnumber_client_record, self.time_beginrecord, self.time_endrecord, self.id_staff_record)
