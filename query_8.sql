SELECT AVG(grade.grade_name) AS average_grade
FROM grade
JOIN student ON grade.student_id = student.student_id
JOIN subject ON grade.subject_id = subject.subject_id;
