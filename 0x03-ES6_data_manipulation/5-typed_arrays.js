export default function createInt8TypedArray(length, position, value) {
  if (position > length) throw new Error('Position outside range');
  const viewData = new DataView(new ArrayBuffer(length));
  viewData.setInt8(position, value);
  return viewData;
}
