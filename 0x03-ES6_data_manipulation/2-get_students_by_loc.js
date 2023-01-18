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
