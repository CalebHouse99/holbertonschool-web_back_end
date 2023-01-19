export default function cleanSet(set, startString) {
  let newString = '';
  set.forEach((value) => {
    if (value.startsWith(startString)) {
      newString += `${value.slice(startString.length)}-`;
    }
  });
  return newString.slice(0, -1);
}
