import xml.etree.ElementTree as ET
tree=ET.parse("student.xml")
root=tree.getroot()

for student in root.findall("student"):
    id=student.find("id").text
    name = student.find("name").text
    marks = student.find("marks").text
    print(id,name,marks)

root=ET.Element("employee")
emp1=ET.SubElement(root,"emp")
ET.SubElement(emp1,"id").text="101"
ET.SubElement(emp1,"Name").text="Rama"
ET.SubElement(emp1,"Salary").text="100000"
emp2=ET.SubElement(root,"emp")
ET.SubElement(emp2,"id").text="102"
ET.SubElement(emp2,"Name").text="pavi"
ET.SubElement(emp2,"Salary").text="200000"

tree=ET.ElementTree(root)
tree.write("employee.xml")
print("xml file written successfully")
