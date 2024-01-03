SELECT AVG(CASE 
            WHEN grade_name = 'неуд' THEN 2
            WHEN grade_name = 'удовл' THEN 3
            WHEN grade_name = 'хорошо' THEN 4
            WHEN grade_name = 'отлично' THEN 5
          END) AS average_grade
FROM grade;
SELECT * FROM grade;