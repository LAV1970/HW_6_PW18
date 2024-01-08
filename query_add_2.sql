SELECT s.name AS student_name, g.grade_name
FROM student s
JOIN grade g ON s.name = g.student
JOIN groupps gp ON s.group_id = gp.group_id
WHERE gp.name_group = 'Механика' AND g.subject_id = 7
      AND g.data = (SELECT MAX(data) FROM grade WHERE student = s.name AND subject_id = 7);