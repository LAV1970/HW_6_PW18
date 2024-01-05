SELECT student.name AS student_name, groupps.name_group
FROM student
JOIN groupps ON student.group_id = groupps.group_id
WHERE groupps.name_group = '14';
    