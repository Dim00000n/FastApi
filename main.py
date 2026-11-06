from sqlalchemy import create_engine,Column,Integer,String,func,ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()
class TikTokUser(Base):
    __tablename__ = 'tiktok_user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    subscribers = Column(Integer,default=0)
    videos = relationship("TikTokVideo",back_populates="author_id")
class video(Base):
    __tablename__ = 'video'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    views = Column(Integer,default=0)
    creator_id = Column(Integer,ForeignKey("tiktok_user.id"))
    author_id = relationship("TikTokUser",back_populates="videos")
Base.metadata.create_all(engine)
sigmaboy = (TikTokUser(username="sigmaboy"))
video1 = video(title= "Sigma a")
video2 = video(title= "Sigma b")
sigmaboy.videos = [video1,video2]
session.add(sigmaboy)
session.commit()


user = session.query(TikTokUser)
for user in user:
    print(user.username)
    for videos in user.videos:
        print(videos.title)
