SELECT DISTINCT groupps.name_group, groupps.subject
FROM student
JOIN groupps ON student.group_id = groupps.group_id
JOIN professor_subject ON groupps.subject = professor_subject.subject_id
WHERE student.name = 'Denise Pace' AND professor_subject.professor_id = 2;