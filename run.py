# Load XML file to process
from xml.etree import ElementTree

with open('data\US20170000002A1-20170105.XML', 'rt') as f:
    tree = ElementTree.parse(f)

# get root element
root = tree.getroot()

flag_field_of_invention = False
flag_desc_related_art = False
flag_summary_of_invention = False
flag_detailed_desc_of_invention = False

field_of_invention = []
desc_related_art = []
summary_of_invention = []
detailed_desc_of_invention = []

for item in root.findall('./description'):
    for child in item:
        current_text = child.text

        subchild_text = ''
        for subchild in list(child):
            if subchild.tail:
                subchild_text += subchild.tail
        if subchild_text and current_text:
            current_text += subchild_text

        if current_text is not None and "field of the invention" in current_text.lower():
            print "processing Field of the Invention"
            flag_field_of_invention = True
            flag_desc_related_art = False
            flag_summary_of_invention = False
            flag_detailed_desc_of_invention = False
            continue
        elif current_text is not None and "description of the related art" in current_text.lower():
            print "processing Description of the related art"
            flag_field_of_invention = False
            flag_desc_related_art = True
            flag_summary_of_invention = False
            flag_detailed_desc_of_invention = False
            continue
        elif current_text is not None and "summary of the invention" in current_text.lower():
            print "processing Summary of the Invention"
            flag_field_of_invention = False
            flag_desc_related_art = False
            flag_summary_of_invention = True
            flag_detailed_desc_of_invention = False
            continue
        elif current_text is not None and "detailed description of the invention" in current_text.lower():
            print "processing Detailed Description of the Invention"
            flag_field_of_invention = False
            flag_desc_related_art = False
            flag_summary_of_invention = False
            flag_detailed_desc_of_invention = True
            continue

        if flag_field_of_invention:
            field_of_invention.append(current_text)
        elif flag_desc_related_art:
            desc_related_art.append(current_text)
        elif flag_summary_of_invention:
            summary_of_invention.append(current_text)
        elif flag_detailed_desc_of_invention:
            detailed_desc_of_invention.append(current_text)

print field_of_invention
print desc_related_art
print summary_of_invention
print detailed_desc_of_invention

# Extract required data
# Print raw data
# Perform key phrase extraction
# Perform topic modeling
# Perform text summarization
