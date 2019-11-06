
import xml.etree.ElementTree as ET
import os

path = 'C:/Users/Administrator/Desktop/Project/images/test'
print(path)
for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename)
    print(fullname)
    '''tree = ET.parse(fullname)
    print(fullname)
    print(tree)'''
    with open(filename) as f:
      tree = ET.parse(f)
      root = tree.getroot()


      for elem in root.getiterator():
        try:
          elem.text = elem.text.replace('C:/Users/Administrator/Desktop/Project', '/content/Project')
        except AttributeError:
          pass

    #tree.write('image (346).xml', encoding="utf8")
    # Adding the xml_declaration and method helped keep the header info at the top of the file.
    tree.write(filename, method='xml')

