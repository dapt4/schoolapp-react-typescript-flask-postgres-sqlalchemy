from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

class Base(DeclarativeBase):
    pass

class SchoolClass(Base):
    __tablename__ = 'school_class'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    belongs_to: Mapped[int] = relationship('BelongsTo', cascade='all, delete')
    
    def __repr__(self):
        return f'<SchoolClass(id={self.id}, name={self.name})>'

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class Student(Base):
    __tablename__ = 'student'
    dni: Mapped[str] = mapped_column(String(30), primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    belongs_to: Mapped[int] = relationship('BelongsTo', cascade='all, delete')

    def __repr__(self):
        return f'<Student(dni={self.dni}, name={self.name})'

    def to_dict(self):
        return {'dni': self.dni, 'name': self.name}

class BelongsTo(Base):
    __tablename__ = 'belongs_to'
    id: Mapped[int] = mapped_column(primary_key=True)
    class_id: Mapped[int] = mapped_column(ForeignKey('school_class.id'))
    student_dni: Mapped[str] = mapped_column(ForeignKey('student.dni'))
