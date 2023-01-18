export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((data) => data.location === city)
    .map((data) => {
      const newData = data;
      newData.grade = 'N/A';
      for (const prop of newGrades) {
        if (newData.id === prop.studentId) newData.grade = prop.grade;
      }
      return newData;
    });
}
