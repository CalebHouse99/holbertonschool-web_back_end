export default function getListStudents() {
  const firstStudent = { firstName: 'Guillaume',  id: 1, location: 'San Francisco' };
  const secondStudent = { firstName: 'James', id: 2, location: 'Columbia' };
  const thirdStudent = { firstName: 'Serena', id: 5, location: 'San Francisco' };
  const arr = [firstStudent, secondStudent, thirdStudent];
  return arr;
}
