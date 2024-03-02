import xmltodict
import yaml

# Чтение XML файла
input = open('xml.input.xml', encoding= 'utf8')
xml_file = input.read()

# Конвертация XML в словарь
file_convert = xmltodict.parse(xml_file)

# Конвертация словаря в YAML
yaml_file = yaml.dump(file_convert)

# Запись YAML данных в файл
output = open('output_add1.yaml', 'w')
output.write(yaml_file)
#print(yaml_file.encode('utf8'))
