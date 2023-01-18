/* eslint-disable no-unused-vars */
function getFullList(item) {
  return item.location;
}

export default function getStudentsByLocation(students, loc) {
  const newStudents = [];
  for (let i = 0; i < students.length; i += 1) {
    if (students.map(getFullList)[i] === loc) {
      newStudents.push(students[i]);
    }
  }
  return newStudents;
}

const j = [1, 2, 3];
const k = j.filter((word) => word.length > 6);
