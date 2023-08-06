from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# 创建数据库连接
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test_db')

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 创建模型类/ORM基类
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))

# 创建表格
Base.metadata.create_all(engine)

# 插入数据
user = User(name='John Doe', email='john@example.com')
session.add(user)
session.commit()

# 分页查询
page = 1 # 当前页码
page_size = 2 # 每页数据条数

# 计算偏移量
offset = (page - 1)* page_size

# 查询数据
# users = session.query(User).all()
users = session.query(User).offset(offset).limit(page_size).all()
# 打印查询结果
for user in users:
    print(user.id,user.name, user.email)

# 关闭数据库连接
session.close()