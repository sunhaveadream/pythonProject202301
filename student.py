# 对象、函数、函数调用关系
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import random
from faker import Faker
from sqlalchemy import text
import re
import csv


# 创建数据库连接
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test_db')

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 创建模型类
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    student_name = Column(String(200))
    student_sex= Column(String(8))
    student_hight= Column(Integer)
    student_weight= Column(Integer)
    student_number= Column(String(50))
    student_address= Column(String(200))
    student_email = Column(String(50))

# 创建表格
Base.metadata.create_all(engine)

# 数据库操作函数，插入数据库的函数
def insert_student(stu):
    print('insert_student')
    # INSERT INTO MYSQL
    session.add(stu)
    session.commit()
# 生成student对象函数；调用函数：随机生成各个字段函数，生成名字的函数以及生成地址的函数；返回值：一个student对象，包含每一个student对象的姓名等信息
def create_student():
    print('create_student')
    stu=Student()
    # stu.student_id递增
    stu.student_name = create_name()
    stu.student_email = create_email()
    stu.student_sex = create_sex()
    stu.student_hight = create_height()
    stu.student_weight = create_weight()
    stu.student_address = create_address()
    stu.student_number = create_number()
    return stu
# 插入数据到数据库；调用函数：生成student对象函数，插入数据库的函数，for循环；返回值：10w条student对象
def insert_student_list(nums):
    if nums > 0:
        for num in range(nums):
            st = create_student()
            insert_student(st)
    print('insert_student_list')
# 生成名字的函数（姓+名）；调用函数：随机函数；返回值：一个姓+名的组合名字
def create_name():
    with open('scoreCsv.csv', 'r') as file:
        csv_reader = csv.reader(file)
        # next(csv_reader) # 跳过标题行
        data = list(csv_reader)
        list1 = []
        for i in data:
            list1.extend(i)
    xingList = list1
    mingList = '搞清楚不同类型字段长度的意思数据库表的设计范式熟悉一下的对象数据类型'
    randomX = random.choice(xingList)[0]
    rangdomM = random.sample(mingList,1)[0]+random.sample(mingList,1)[0]
    xingming = randomX+rangdomM
    print('create_name')
    return xingming
# 生成地址的函数（省份+市+县+详细地址）；
def create_address():
    fake = Faker('zh_CN')
    # 随机生成中文地址
    address = fake.address()
    print('create_address')
    return address
# 生成性别的函数
def create_sex():
    fake = Faker()
    # 随机生成性别
    gender = fake.random_element(elements=('0', '1'))
    print('create_sex')
    return gender
# 生成年龄的函数
def create_age():
    fake = Faker()
    # 随机生成年龄
    age = fake.random_int(min=18, max=28)
    print('create_age')
    return age
# 生成邮箱的函数
def create_email():
    fake = Faker()
    # 随机生成QQ邮箱
    qq_email = fake.email(domain='qq.com')
    print('create_email')
    return qq_email
# 生成身高的函数
def create_height():
    fake = Faker(locale = 'zh_CN')
    # 随机生成身高
    height = fake.random_int(min=140, max=200)
    print('create_hight')
    return height
# 生成体重的函数
def create_weight():
    fake = Faker(locale = 'zh_CN')
    # 随机生成体重
    weight = fake.random_int(min=40, max=100)
    print('create_weight')
    return weight
# 生成电话的函数
def create_number():
    fake = Faker(locale = 'zh_CN')
    # 生成以1开头的11位数的电话号码
    phone_number = fake.phone_number()
    # while not re.match(r'^1\d{10}$', phone_number):
    #     phone_number = fake.phone_number()
    print('create_number')
    return phone_number
# 分页查询学生名字
def stearch_stuName(name,page,page_size):
    # data = session.query(Student).where(text('student_name="'+name+'"'))
    # 如何做到分页查询
    # 分页查询
    page = page  # 当前页码
    page_size = page_size  # 每页数据条数
    # 计算偏移量
    offset = (page - 1) * page_size
    # 查询数据
    data = session.query(Student).filter(Student.student_name == name).offset(offset).limit(page_size).all()
    # 打印查询结果
    for item in data:
        print(item.student_name,item.student_id)
# 更新学生姓名
def update_stuName(ID,newName):
    data = session.query(Student).filter_by(student_id=ID).first()
    data.student_name = newName
    session.commit()
    print(data .student_id,data.student_name)
# 删除单个学生信息
def delete_stuMessage(ID):
    stuData = session.query(Student).filter_by(student_id=ID).first()
    session.delete(stuData)
    session.commit()
    print(stuData.student_id, stuData.student_name)

if __name__=='__main__':
    # 批量插入学生
    insert_student_list(1000)#注意看加了索引后优化的查询性能
    # 生成姓名
    # print(create_name())
    # 分页查询学生信息('要查询的名字',查询的页数,每页展示几条数据)
    # stearch_stuName('赵象字',1,5)
    # 更新学生信息('要查询的学生ID','新的名字')
    # update_stuName(3,'新名字')
    # 删除学生信息(要查询的学生ID)
    # delete_stuMessage(3)
    # 测试随机生成地址
    # create_address()


