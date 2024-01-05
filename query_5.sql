SELECT professor.name AS professor_name, groupps.subject
FROM professor
JOIN professor_subject ON professor.professor_id = professor_subject.professor_id
JOIN groupps ON professor_subject.subject_id = groupps.fach
WHERE professor.name = 'Andrew Carter';
