str='''
1. 在MySQL中，服务器处理语句的结束标志为:
A、GO
B、@@
C、$$ 
D、分号
2. “abc”属于：
A、 字符串型
B、 整型 
C、 数字型 
D、 日期和时间类型 
3. 查看表的结构，使用：
A、 find
B、 select
C、 alter
D、 Desc
4. 在SQL语言中，用来插入和更新数据的命令是： 
A、 INSERT,UPDATE
B、 UPDATE,INSERT 
C、 DELETE,UPDATE
D、 INSERT,SELECT
5. 创建数据库的语法格式是：
A、 SHOW DATABASE；
B、 USE 数据库名；
C、 CREATE DATABASE 数据库名；
D、 DROP DATABASE 数据库名；
6. 查询tb数据表中id=1的记录，语法格式是：
A、 select * into tb where id=1；
B、 select * where tb where id=1；
C、 select * delete tb where id=1；
D、 select * from tb where id=1；
7. 查询book表中price字段的最大值，查询语句是： 
A、 select max(price) from book；
B、 select min(price) from book；
C、 select price from min book；
D、 select price from max book；
8. 查询xs数据表中的所有数据，并按学号降序排列，语法格式是： 
A、 select * from xs group by 学号desc；
B、 select * from xs order by 学号 asc；
C、 select * from xs order by 学号 desc；
D、 select * from xs 学号 order by；
9. 如下哪一个不可以用来作为MySQL的字符串截取函数：
A、 substr
B、 mid
C、 lpad
D、 Reverse
10. 以下语句错误的是( )
A、select sal+1 from emp；
B、select sal*10,sal*deptno from emp；
C、不能使用运算符号
D、select sal*10,deptno*10 from emp；
11. SQL语言允许使用通配符进行字符串匹配的操作，其中‘%’可以表示： 
A、 0个字符 
B、 1个字符 
C、 多个字符 
D、 以上都可以 
12. 关系数据库中关系实质上是一个二维表，表中每一条记录（行）在关系模式中被称为：
A、元组
B、属性
C、行
D、列
13. 在SQL语言中，子查询是：。
A、选取单表中字段子集的查询语句
B、选取多表中字段子集的查询语句
C、返回单表中数据子集的查询语言
D、嵌入到另一个查询语句之中的查询语句
14. 向数据表中插入一-条记录用以下哪一项(
A、 CREATE
B、 INSERT
C、 SAVE
D、 UPDATE
15. 以下哪项是用来分组的：
A、ORDER BY
B、ORDERED BY
C、GROUP BY
D、GROUPED BY
16. 以下聚合函数求平均数的是(
A、 COUNT
B、 MAX
C、 AVG
D、 SUM
17. 从GROUP BY分组的结果集中再次用条件表达式进行筛选的子句是：
A、FROM
B、ORDER BY
C、HAVING
D、WHERE
18. 数据库备份，只备份数据表，不备份数据库的命令是：
A、mysqldump  -u  username  -p  password  dbName  >  name.sql存放路径
B、mysqldump  -u  username  -p  password  -B  dbName  >  name.sql路径
C、source  name.sql存放路径
D、mysql  -uusername  -ppassword  [dbname]  <  name.sql路径
19. 授予zhangsan在mysql_test数据库中的customers表上拥有对列cust_id和列cust_name的select权限
A、grant  select,update  on  mysql_test.customers  to 'zhangsan'@'localhost'identified by'123';
B、grant  select(cust_id,cust_name)  on  mysql_test.customers  to'zhangsan'@'localhost’;
C、grant  all  on mysql_test.*  to'zhangsan'@'localhost';
D、grant  create  user  on *.*  to'zhangsan'@'localhost';
20. 执行SELECT SUBSTRING('foobarbar' FROM -4 FOR 2)语句后的输入为：
A、'bar'
B、'barbar'
C、'rb'
D、'ba'
21. 以下语句不正确的是：
A、select * from emp;
B、select ename,hiredate,sal from emp;
C、select  *  from emp order deptno;
D、select  *  from emp where deptno=1 and sal<300;
22. delete from employee语句的作用是：
A、删除当前数据库中整个employee表，包括表结构
B、删除当前数据库中employee表内的所有行
C、由于没有where 子句，因此不删除任何数据
D、删除当前数据库中employee表内的当前行
23. 条件“BETWEEN 20 AND 30表示年龄在20到30之间，且:
A、包括20岁不包括30岁
B、不包括20岁包括30岁
C、不包括20岁和30岁
D、包括20岁和30岁
24. 以下表示可变长度字符串的数据类型是(
A、TEXT
B、CHAR
C、VARCHAR
D、EMUM
25. 拼接字段的函数是(
A、SUBSTRING()
B、TRIM()
C、SUM()
D、CONCAT()
26. 关系数据库中，主键是：
A、创建唯一的索引，允许空值
B、只允许以表中第一字段建立
C、主键值可以重复
D、为标识表中唯一的实体
27. 返回字符串长度的函数是(
A、len()
B、length()
C、left()
D、reverse()
28. 在SELECT语句中，使用关键字（）可以把重复行屏蔽。
A、TOP
B、ALL
C、UNION
D、DISTINCT
29. 若要在基本表S中增加一列CN (课程名)，可用：
A、ADD TABLE S ALTER(CN CHAR( 8 ))
B、ALTER TABLE S ADD(CN CHAR (8 ))
C、ADD TABLE S(CN CHAR( 8 ))
D、ALTER TABLE S (ADD CN CHAR( 8 ))
30. 以下不属于中间件的是 
A、Jboss
B、Apache
C、Tomcat
D、Phpstudy
31. 中间件Weblogic和ApacheTomcat默认端口是（）。
7001、80
B、 7001、8080
C、 7002、80
D、 7002、8080
33. 下面对union的描述正确的是：（不定项）
A、union 只连接结果集完全一样的查询语句
B、union 可以连接结果集中数据类型个数相同的多个结果集
C、union是筛选关键词，对结果集再进行操作
D、任何查询语句都可以用union 来连接

'''
str=str.replace(' ','')
str=str.replace('\t','')
str=str.replace('\nA.','\t')
str=str.replace('\nB.','\t')
str=str.replace('\nC.','\t')
str=str.replace('\nD.','\t')
str=str.replace('\nA、','\t')
str=str.replace('\nB、','\t')
str=str.replace('\nC、','\t')
str=str.replace('\nD、','\t')
str=str.replace('A、','\t')
str=str.replace('B、','\t')
str=str.replace('C、','\t')
str=str.replace('D、','\t')
str=str.replace('A.','\t')
str=str.replace('B.','\t')
str=str.replace('C.','\t')
str=str.replace('D.','\t')
print(str)