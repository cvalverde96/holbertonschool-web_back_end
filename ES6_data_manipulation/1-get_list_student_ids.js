export default function getListStudentIds(object) {
  if (!Array.isArray(object)) {
    return [];
  }

  return object.map((item) => item.id);
}
