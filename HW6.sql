1.
a)
SELECT STUDENT.Name
FROM STUDENT
WHERE
    STUDENT.Class = 4
    AND
    STUDENT.Major = 'CS';

b)
SELECT COURSE.Course_name
FROM COURSE
NATURAL JOIN SECTION
WHERE
    SECTION.Year IN ('07','08')
    AND
    SECTION.Instructor = 'King';

c)
SELECT S.Course_number, S.Semester, S.Year, COUNT(G.Student_number)
FROM SECTION AS S
NATURAL JOIN GRADE_REPORT
WHERE S.Instructor = 'King';

d)
SELECT Sd.Name, 
    C.Course_number, 
    C.Course_number, 
    C.Credit_hours, 
    Sn.Semester, 
    Sn.Year, 
    G.Grade
FROM STUDENT AS Sd
NATURAL JOIN GRADE_REPORT
NATURAL JOIN SECTION
NATURAL JOIN COURSE
WHERE
    Sd.Class = 4
    AND
    Sd.Major = 'CS';

2.
a)
INSERT INTO STUDENT(Name,Student_number,Class,Major)
VALUES ('Johnson',25,1,'Math');

b)
UPDATE STUDENT
SET Class = 2
WHERE Name = 'Smith';

c)
INSERT INTO COURSE(Course_name,Course_number,Credit_hours,Department)
VALUES ('Knowledge Engineering','cs4390',3,'CS');

d)
DELETE FROM STUDENT
WHERE Name = 'Smith' AND Student_number = 17;

3.
a)
SELECT E.Fname
FROM EMPLOYEE AS E
WHERE E.Ssn IN
    (SELECT M.Ssn, MAX(M.Salary)
    FROM EMPLOYEE AS M
    JOIN DEPARTMENT AS D ON M.Dno = D.Dnumber
    GROUP BY D.Dnumber);

b)
SELECT E.Fname, E.Lname
FROM EMPLOYEE AS E
WHERE Super_ssn = '88866555';

c)
SELECT E.Fname, E.Lname
FROM EMPLOYEE AS E
HAVING E.Salary - 10000 >= MIN(E.Salary);