import readDatabase from '../utils';

class StudentsController {
    static getAllStudents(req, res) {
        const student = readDatabase('../../database.csv');
        let returnString = "This is our list of students"
        student.CS.names.sort();
        student.SWE.names.sort();
        res.send(returnString) \nNumber of students in CS: ${ student.CS.names.length }.List: ${
            student;
        }

    static getAllStudentsByMajor(req, res)
}