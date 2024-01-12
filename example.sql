UPDATE student
SET group_id = 
    CASE 
        WHEN student_id BETWEEN 220 AND 233 THEN 14 -- Группа "Автоматизация технологических процессов"
        WHEN student_id BETWEEN 234 AND 247 THEN 15 -- Группа "Механика"
        WHEN student_id BETWEEN 248 AND 259 THEN 16 -- Группа "Компьютерные науки"
    END;
    
    ALTER TABLE grade
MODIFY COLUMN grade_name int;