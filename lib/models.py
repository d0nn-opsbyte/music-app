from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, validates
from datetime import datetime


engine = create_engine('sqlite:///music_app.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    playlists = relationship("Playlist", back_populates="user", cascade="all, delete-orphan")

    @validates('name', 'email')
    def validate_fields(self, key, value):
        if not value or len(value.strip()) == 0:
            raise ValueError(f"{key} cannot be empty")
        if key == 'email' and '@' not in value:
            raise ValueError("Email must be valid")
        return value.strip()

    def __repr__(self):
        return f"User {self.id}: {self.name} ({self.email})"

class Playlist(Base):
    __tablename__ = 'playlists'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="playlists")
    songs = relationship("Song", back_populates="playlist", cascade="all, delete-orphan")

    @validates('title')
    def validate_title(self, key, title):
        if not title or len(title.strip()) == 0:
            raise ValueError("Playlist title cannot be empty")
        return title.strip()

    def __repr__(self):
        return f"Playlist {self.id}: {self.title}"

class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    artist = Column(String(100), nullable=False)
    album = Column(String(100))
    playlist_id = Column(Integer, ForeignKey('playlists.id'))

    playlist = relationship("Playlist", back_populates="songs")

    @validates('title', 'artist')
    def validate_fields(self, key, value):
        if not value or len(value.strip()) == 0:
            raise ValueError(f"{key} cannot be empty")
        return value.strip()

    def __repr__(self):
        return f"Song {self.id}: '{self.title}' by {self.artist}"

# Create all tables
Base.metadata.create_all(engine)