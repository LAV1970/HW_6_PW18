SELECT s.name AS student_name, AVG(g.grade_name) AS average_grade
FROM student s
JOIN grade g ON s.name = g.student
JOIN groupps gp ON s.group_id = gp.group_id
WHERE g.subject_id = 7 AND gp.name_group = 'Механика'
GROUP BY s.name;