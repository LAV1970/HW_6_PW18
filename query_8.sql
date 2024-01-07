SELECT AVG(grade.grade_name) AS average_grade
FROM grade
JOIN student ON grade.student = student.name
JOIN professor_subject ON grade.subject_id = professor_subject.subject_id
WHERE professor_subject.professor_id = 2;
