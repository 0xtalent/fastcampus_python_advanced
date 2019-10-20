# Chapter01-1
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 일반적인 코딩으로 작성해볼게요

# 학생1
student_name_1 = 'Kim'
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
    {'gender': 'Male'},
    {'score1': 95},
    {'score2': 88}
]

# 학생2
student_name_2 = 'Lee'
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [
    {'gender': 'Female'},
    {'score1': 77},
    {'score2': 92}
]

# 학생3
student_name_3 = 'Park'
student_number_3 = 3
student_grade_3 = 4
student_detail_3 = [
    {'gender': 'Male'},
    {'score1': 99},
    {'score2': 100}
]

# 리스트 구조로 바꿔볼게요
# 관리하기 힘들어요
# 데이터의 정확한 위치(인덱스)를 매핑해서 사용 해야되요
student_names_list = ['Kim', 'Lee', 'Park']
student_numbers_list = [1, 2, 3]
student_grades_list = [1, 2, 4]
student_details_list = [
    {'gender': 'Male', 'score1': 95, 'score2': 88},
    {'gender': 'Female', 'score1': 77, 'score2': 92},
    {'gender': 'Male', 'score1': 99, 'score2': 100}
]

# 학생 삭제
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)

# 오늘의 실수 , 빼먹었고, s 빼먹었다ㅋㅋ

print()
print()

# 딕셔너리 구조로 바꿔볼게요
# 코드 반복 지속되고, 중첩 문제가 발행해요
students_dicts = [
    {'student_name': 'Kim', 'student_number': 1, 'student_grade': 1, 'student_detail': {'gender': 'Male', 'score1': 95, 'score2': 88}},
    {'student_name': 'Lee', 'student_number': 2, 'student_grade': 2, 'student_detail': {'gender': 'Female', 'score1': 77, 'score2': 92}},
    {'student_name': 'Kim', 'student_number': 3, 'student_grade': 4, 'student_detail': {'gender': 'Male', 'score1': 99, 'score2': 100}}
]

del students_dicts[1]
print(students_dicts)
print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화가 되며, 이번에는 메소드를 활용해서 강력한 코드를 작성해보자

class Student():
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._name, self._number)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._name, self._number)

student1 = Student('kim', 1, 1, {'gender': 'Male', 'score1' : 95, 'score2' : 88})
student2 = Student('Lee', 2, 2, {'gender': 'Female', 'score1' : 77, 'score2' : 92})
student3 = Student('Park', 3, 4, {'gender': 'Male', 'score1' : 99, 'score2' : 100})

print(student1.__dict__)

# 리스트 선언
students_list = []

students_list.append(student1)
students_list.append(student2)
students_list.append(student3)

print()

print(students_list)

# 반복(__str__)
for x in students_list:
    print(x)

# 객체지향의 정의는 실제 세계에 존재하는 학생을 직접 모델링했죠. Class로
# 모델링을 해서, 모델링을 했다는 것은 그 학생이라는 객체, 삶, 실제 세계에 있는 학생을
# 어떤 가진 속성들을 이렇게 모델링해서 프로그램을 개발하는 과정을 객체지향 프로그래밍이라 한다.
# 어렵다...더 공부해야겠다!
