from django.test import TransactionTestCase
from django.utils.timezone import datetime
from .models import Department, Employee, SalaryGrade

class DatabaseTestCase(TransactionTestCase):

    @classmethod
    def setUpTestData(cls):
        cls.insert_test_data()

    @classmethod
    def insert_test_data(cls):
        Department.objects.all().delete()
        Employee.objects.all().delete()
        SalaryGrade.objects.all().delete()

        Department.objects.bulk_create([
            Department(deptno=10, dname='ACCOUNTING', loc='NEW YORK'),
            Department(deptno=20, dname='RESEARCH', loc='DALLAS'),
            Department(deptno=30, dname='SALES', loc='CHICAGO'),
            Department(deptno=40, dname='OPERATIONS', loc='BOSTON')
        ])

        Employee.objects.bulk_create([
            Employee(empno=7369, ename='SMITH', job='CLERK', mgr_id=7902, hiredate=datetime(1980, 12, 17), sal=800, comm=None, deptno_id=20),
            Employee(empno=7499, ename='ALLEN', job='SALESMAN', mgr_id=7698, hiredate=datetime(1981, 2, 20), sal=1600, comm=300, deptno_id=30),
            Employee(empno=7521, ename='WARD', job='SALESMAN', mgr_id=7698, hiredate=datetime(1981, 2, 22), sal=1250, comm=500, deptno_id=30),
            Employee(empno=7566, ename='JONES', job='MANAGER', mgr_id=7839, hiredate=datetime(1981, 4, 2), sal=2975, comm=None, deptno_id=20),
            Employee(empno=7654, ename='MARTIN', job='SALESMAN', mgr_id=7698, hiredate=datetime(1981, 9, 28), sal=1250, comm=1400, deptno_id=30),
            Employee(empno=7698, ename='BLAKE', job='MANAGER', mgr_id=7839, hiredate=datetime(1981, 5, 1), sal=2850, comm=None, deptno_id=30),
            Employee(empno=7782, ename='CLARK', job='MANAGER', mgr_id=7839, hiredate=datetime(1981, 6, 9), sal=2450, comm=None, deptno_id=10),
            Employee(empno=7788, ename='SCOTT', job='ANALYST', mgr_id=7566, hiredate=datetime(1987, 7, 13), sal=3000, comm=None, deptno_id=20),
            Employee(empno=7839, ename='KING', job='PRESIDENT', mgr=None, hiredate=datetime(1981, 11, 17), sal=5000, comm=None, deptno_id=10),
            Employee(empno=7844, ename='TURNER', job='SALESMAN', mgr_id=7698, hiredate=datetime(1981, 9, 8), sal=1500, comm=0, deptno_id=30),
            Employee(empno=7876, ename='ADAMS', job='CLERK', mgr_id=7788, hiredate=datetime(1987, 7, 13), sal=1100, comm=None, deptno_id=20),
            Employee(empno=7900, ename='JAMES', job='CLERK', mgr_id=7698, hiredate=datetime(1981, 12, 3), sal=950, comm=None, deptno_id=30),
            Employee(empno=7902, ename='FORD', job='ANALYST', mgr_id=7566, hiredate=datetime(1981, 12, 3), sal=3000, comm=None, deptno_id=20),
            Employee(empno=7934, ename='MILLER', job='CLERK', mgr_id=7782, hiredate=datetime(1982, 1, 23), sal=1300, comm=None, deptno_id=10)
        ])

        SalaryGrade.objects.bulk_create([
            SalaryGrade(grade=1, losal=700, hisal=1200),
            SalaryGrade(grade=2, losal=1201, hisal=1400),
            SalaryGrade(grade=3, losal=1401, hisal=2000),
            SalaryGrade(grade=4, losal=2001, hisal=3000),
            SalaryGrade(grade=5, losal=3001, hisal=9999)
        ])

    def test_departments_exist(self):
        self.assertEqual(Department.objects.count(), 4)

    def test_employees_exist(self):
        self.assertEqual(Employee.objects.count(), 14)

    def test_salary_grades_exist(self):
        self.assertEqual(SalaryGrade.objects.count(), 5)

    def test_employee_salary_range(self):
        for grade in SalaryGrade.objects.all():
            employees = Employee.objects.filter(sal__gte=grade.losal, sal__lte=grade.hisal)
            self.assertTrue(employees.exists())

#아래의 명령어 실행
# python manage.py shell

# from study_example.tests import DatabaseTestCase
# DatabaseTestCase.insert_test_data()