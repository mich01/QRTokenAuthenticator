from DBConnect import db
class JsonModel(object):
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Members(db.Model):
    __tablename__ = 'tbl_members'
    ID = db.Column(db.Integer, autoincrement=True)
    MemberID = db.Column(db.String(50), primary_key=True, nullable=False)
    Image = db.Column(db.String(50))
    SurName = db.Column(db.String(100), nullable=False)
    OtherNames = db.Column(db.String(500), nullable=False)
    Gender = db.Column(db.String(1), nullable=False)
    NationalID = db.Column(db.String(10), nullable=False)

    def __init__(self, Image, MemberID,CertID, SurName, OtherNames,Gender,NationalID):
        self.MemberID = MemberID
        self.SurName = SurName
        self.OtherNames = OtherNames
        self.Image = Image
        self.Gender =Gender
        self.CertID =CertID
        self.NationalID = NationalID

class Certs(db.Model):
    __tablename__ = 'tbl_certs'
    ID = db.Column(db.Integer,  autoincrement=True)
    CertID = db.Column(db.String(20), primary_key=True,nullable=False)
    MemberID = db.Column(db.String(20), nullable=False)
    Issued = db.Column(db.Date(),nullable=False)
    Expires = db.Column(db.Date(), nullable=True)
    Description = db.Column(db.String(500), nullable=False)

    def __init__(self, MemberID,CertID,Issued, Expires, Description):
        self.MemberID = MemberID
        self.CertID = CertID
        self.Issued = Issued
        self.Expires = Expires
        self.Description = Description