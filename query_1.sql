SELECT student, AVG(CAST(grade_name AS SIGNED)) AS average_grade
FROM grade
GROUP BY student
ORDER BY average_grade DESC
LIMIT 5;
