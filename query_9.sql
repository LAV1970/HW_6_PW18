SELECT DISTINCT groupps.name_group, groupps.subject
FROM student
JOIN groupps ON student.group_id = groupps.group_id
WHERE student.name = 'Denise Pace';