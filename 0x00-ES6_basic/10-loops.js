export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  for (const iter of array) {
    const newVal = `${appendString}${iter}`;
    newArray.push(newVal);
  }

  return newArray;
}
