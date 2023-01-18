/* eslint-disable no-unused-vars */
function getFullList(item) {
  return item.id;
}

export default function getListStudentIds(objArray) {
  if (objArray == null) {
    return [];
  }
  if (objArray.constructor === Array) {
    const arr = objArray.map(getFullList);
    let sum = 0;
    for (let i = 0; i < arr.length; i += 1) {
      sum += arr[i];
    }
    return sum;
  }
  return [];
}

const a = [1, 2, 3].reduce((partialSum, a) => partialSum + a, 0);
