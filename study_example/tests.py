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


  # annotate @, aggregate
    def test_annotate(self):
        # 🎯 annotate() 정리
        # ✔ annotate()는 개별 객체(레코드)에 대해 추가 필드를 생성하여 값을 포함한 QuerySet 반환
        # ✔ GROUP BY를 자동으로 처리하여 집계 함수(Aggregate Functions) 적용 가능
        # ✔ Count, Sum, Avg, Min, Max, Length 등 다양한 집계 연산을 활용 가능
        # ✔ Case-When을 사용하여 조건부 필드 추가 가능
        # 🔹 즉, annotate()는 개별 항목에 대해 추가 정보를 붙이는 강력한 기능! 🚀

        from django.db.models.functions import Length

        # 각 질문별 content의 길이 구하기
        # SELECT id, subject, LENGTH(content) AS content_length FROM pybo_question;
        # questions = Question.objects.annotate(content_length=Length("content"))
        # for q in questions:
        #    print(q.subject, q.content_length)

        # 4️⃣ 각 질문별 최신 답변의 날짜 가져오기from django.db.models import Max

        questions = Question.objects.annotate(
            latest_answer_date=Max("answers__create_date")
        )
        # for q in questions:
        #    print(q.subject, q.latest_answer_date)

        # 4️⃣ 각 문제별, 대답들 갯수
        questions = Question.objects.annotate(answer_count=Count("answers"))
        # SELECT q.id, q.subject, COUNT(a.id) AS answer_count
        # FROM Question q
        # LEFT JOIN Answer a ON q.id = a.question_id
        # GROUP BY q.id, q.subject;

        # for q in questions:
        #    print(f"질문: {q.subject}, 답변 개수: {q.answer_count}")

    def test_aggregate(self):
        # SELECT COUNT(id) AS total_answers FROM Answer;
        answer = Answer.objects.aggregate(total_answers=Count("id"))  # 전체 갯수 또는 *
        print(answer)  # {'total_answers': 5}

        # 2. 전체 질문 개수 구하기
        result = Question.objects.aggregate(total_questions=Count("id"))
        print(result)

        # 3. 전체 답변의 평균 길이 구하기
        # SELECT AVG(LENGTH(content)) AS avg_content_length FROM Answer;
        result = Answer.objects.aggregate(avg_content_length=Avg(Length("content")))
        # print(result)

        # 4. 가장 오래된 질문 날짜 구하기
        # SELECT MIN(create_date) AS oldest_question FROM Question;
        result = Question.objects.aggregate(oldest_question=Min("create_date"))
        # print(result)

        # 5. 전체 답변 글자 수 합계 구하기
        result = Answer.objects.aggregate(total_content_length=Sum(Length("content")))
        # print(result)

        # 6. 가장 긴 질문 길이 구하기
        result = Question.objects.aggregate(longest_question=Max(Length("content")))
        # print(result)

    def test_raw(self):
        from django.db import connection

        questions = Question.objects.raw("SELECT * FROM pybo_question")
        for question in questions:
            print(question.id, question.subject)

        # 2. 특정 질문 가져오기 (id=1)
        # SELECT * FROM pybo_question WHERE id = 1;
        question = Question.objects.raw(
            "SELECT * FROM pybo_question WHERE id = %s", [1]
        )
        for q in question:
            print(q.subject, q.content)
        # 3. 특정 키워드가 포함된 질문 검색
        keyword = "%Django%"
        questions = Question.objects.raw(
            "SELECT * FROM pybo_question WHERE content LIKE %s", [keyword]
        )
        for q in questions:
            print(q.subject)

        # 4. 답변이 가장 많은 질문 가져오기
        questions = Question.objects.raw(
            """
            SELECT q.id, q.subject, COUNT(a.id) AS answer_count
            FROM pybo_question q
            LEFT JOIN pybo_answer a ON q.id = a.question_id
            GROUP BY q.id
            ORDER BY answer_count DESC
            LIMIT 1
        """
        )
        for q in questions:
            print(q.subject, q.answer_count)

        # 5. 질문 ID와 해당하는 답변 개수 가져오기

        questions = Question.objects.raw(
            """
            SELECT q.id, q.subject, COUNT(a.id) AS num_answers
            FROM pybo_question q
            LEFT JOIN pybo_answer a ON q.id = a.question_id
            GROUP BY q.id
        """
        )
        for q in questions:
            print(q.subject, q.num_answers)


# def test_sum_answer_ids(self):
#     """
#     Test for Sum aggregation on answer ids
#     """
#     result = Answer.objects.aggregate(Sum("id"))
#     # SQL 쿼리:
#     # SELECT SUM(id) FROM Answer;
#     print(result)
#     self.assertEqual(result["id__sum"], 15)
