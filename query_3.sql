SELECT g.name_group, AVG(CASE WHEN grade.subject_id = 5 THEN grade.grade_name END) AS average_grade
FROM groupps g
JOIN student s ON g.group_id = s.group_id
JOIN grade ON s.student_id = grade.student_id
WHERE g.fach = 'Механика'
GROUP BY g.name_group
ORDER BY average_grade DESC
LIMIT 0, 1000;