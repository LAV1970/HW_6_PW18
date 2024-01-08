SELECT groupps.name_group, AVG(grade.grade_name) AS average_grade
FROM groupps
JOIN student ON groupps.group_id = student.group_id
JOIN grade ON student.name = grade.student AND groupps.subject = grade.subject_id
WHERE grade.subject_id = 7 AND grade.grade_name IS NOT NULL
GROUP BY groupps.name_group
ORDER BY average_grade DESC
LIMIT 0, 1000;