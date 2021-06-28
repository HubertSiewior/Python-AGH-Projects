import xml.etree.ElementTree as ET


def indent(elem, level=0):
    # Function for better view of xml file
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def export_to_xml_H1_H2(file_name, files_array):
    project = ET.Element("Project", Xml_structure="simple")
    # Making needed subtrees
    models = ET.SubElement(project, "Models")
    diagrams = ET.SubElement(project, "Diagrams")
    class_diagram = ET.SubElement(diagrams, "ClassDiagram", name=file_name)
    shapes = ET.SubElement(class_diagram, "Shapes")
    connectors = ET.SubElement(class_diagram, "Connectors")
    model_relationship_container = ET.SubElement(models, "ModelRelationshipContainer")
    model_children = ET.SubElement(model_relationship_container, "ModelChildren")
    model_package = ET.SubElement(models, "Package", name=file_name)
    model_package_children = ET.SubElement(model_package, "ModelChildren")

    for file_index, python_file in enumerate(files_array):
        # Class model
        Class = ET.SubElement(model_package_children, "Class", Id=str("ID" + python_file[0]), Name=python_file[0])
        model_children_class = ET.SubElement(Class, "ModelChildren")
        # Class attributes
        ET.SubElement(model_children_class, "Attribute", Name="Size", InitialValue=str(python_file[1]),
                      Id=str("IDAtrr" + python_file[0]), Type=str(type(python_file[1]).__name__))
        # Class shape in Class Diagram
        ET.SubElement(shapes, "Class", Id=str("IDShape" + python_file[0]), Model=str("ID" + python_file[0]),
                      Name=str(python_file[0]))

        for dependence_index, dependence in enumerate(python_file[2]):
            if file_index != dependence_index and dependence != 0:
                # Usage model
                ET.SubElement(model_children, "Usage",
                              From=str("ID" + python_file[0]),
                              Id=str("ID" + python_file[0] + "To" + files_array[dependence_index][0]),
                              To=str("ID" + files_array[dependence_index][0]), Name=str(dependence)
                              )
                # Usage in Connectors in Class Diagram
                ET.SubElement(connectors, "Usage",
                              From=str("IDShape" + python_file[0]),
                              Model=str("ID" + python_file[0] + "To" + files_array[dependence_index][0]),
                              To=str("IDShape" + files_array[dependence_index][0]))

    indent(project)
    tree = ET.ElementTree(project)
    # Writing xml tree to file
    tree.write(file_name + ".xml", encoding="utf-8", xml_declaration=True)


def export_to_xml_H3(file_name, files_array):
    Project = ET.Element("Project", Xml_structure="simple")
    # Making needed subtrees
    models = ET.SubElement(Project, "Models")
    diagrams = ET.SubElement(Project, "Diagrams")
    class_diagram = ET.SubElement(diagrams, "ClassDiagram", name=file_name)
    shapes = ET.SubElement(class_diagram, "Shapes")
    connectors = ET.SubElement(class_diagram, "Connectors")
    model_relationship_container = ET.SubElement(models, "ModelRelationshipContainer")
    model_children = ET.SubElement(model_relationship_container, "ModelChildren")
    model_package = ET.SubElement(models, "Package", name=file_name)
    model_package_children = ET.SubElement(model_package, "ModelChildren")
    for module_index, module in enumerate(files_array):
        # Package in which all of the module classes will be
        package = ET.SubElement(model_package_children, "Package", Name=module[0][2], Id="ID" + module[0][2])
        model_children_package = ET.SubElement(package, "ModelChildren")
        # Package shape in Class Diagram
        package_shapes = ET.SubElement(shapes, "Package", Name=module[0][2],
                                       Model=str("ID" + module[0][2]), Id="IDShape" + module[0][2])
        diagram_element_children = ET.SubElement(package_shapes, "DiagramElementChildren")

        for file_index, python_file in enumerate(module):
            # Class model
            Class = ET.SubElement(model_children_package, "Class", Id=str("ID" + python_file[0]),
                                  Name=str(python_file[0]))
            model_children_class = ET.SubElement(Class, "ModelChildren")
            # Class attributes
            ET.SubElement(model_children_class, "Attribute", Name="Size", InitialValue=str(python_file[1]),
                          Id=str("IDAtrr" + python_file[0]), Type=str(type(python_file[1]).__name__))
            # Class shape in Class Diagram
            ET.SubElement(diagram_element_children, "Class", Id=str("IDShape" + python_file[0]),
                          Model=str("ID" + python_file[0]), Name=str(python_file[0]))

            for dependence_module_index, dependence_module_array in enumerate(python_file[3]):
                for dependence_index, dependence in enumerate(dependence_module_array):
                    if (module_index != dependence_module_index or file_index != dependence_index) and dependence != 0:
                        # Usage model
                        ET.SubElement(model_children, "Usage",
                                      From=str("ID" + python_file[0]),
                                      Id=str("ID" + python_file[0] + "To" +
                                             files_array[dependence_module_index][dependence_index][0]),
                                      To=str("ID" + files_array[dependence_module_index][dependence_index][0]),
                                      Name=str(dependence)
                                      )
                        # Usage in Connectors in Class Diagram
                        ET.SubElement(connectors, "Usage",
                                      From=str("IDShape" + python_file[0]),
                                      Model=str("ID" + python_file[0] + "To" +
                                                files_array[dependence_module_index][dependence_index][0]),
                                      To=str("IDShape" + files_array[dependence_module_index][dependence_index][0]))
    indent(Project)
    tree = ET.ElementTree(Project)
    # Writing xml tree to file
    tree.write(file_name + ".xml", encoding="utf-8", xml_declaration=True)


def main(file_name, data, story_number: int):
    if story_number == 1 or story_number == 2:
        export_to_xml_H1_H2(file_name, data)
    elif story_number == 3:
        export_to_xml_H3(file_name, data)


if __name__ == '__main__':
    # example data for tests
    module_dataH1 = [
        ["get_dependencies.py", 10024, [None, 20, 35]],
        ["draw_graphH3.py", 4048, [12, None, 38]],
        ["os.py", 10000, [32, -1, None]],

    ]
    module_dataH3 = [
        [["jeden.py", 1000, "modul1", [[None, 20, 35], [12, 1], [1]]],
         ["dwa.py", 2000, "modul1", [[0, None, 35], [12, 0], [2]]],
         ["trzy.py", 3000, "modul1", [[0, 200, None], [12, 2], [0]]]],

        [["cztery.py", 1000, "modul2", [[0, 20, 35], [None, 9], [0]]],
         ["piec.py", 2000, "modul2", [[2, 8, 35], [12, None], [2]]]],

        [["szesc.py", 1000, "modul3", [[0, 20, 35], [12, 0], [None]]]]
    ]
    main("testH1", module_dataH1, 1)
    main("testH3", module_dataH3, 3)
