function getFullList(item) {
  return item.id;
}

export default function getListStudentIds(objArray) {
  if (objArray.constructor === Array) {
    return objArray.map(getFullList);
  }
  return [];
}
