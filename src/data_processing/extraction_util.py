from xml.etree import ElementTree

FIELD_OF_THE_INVENTION = "field of the invention"
DESC_OF_THE_RELATED_ART = "description of the related art"
SUMMARY_OF_THE_INVENTION = "summary of the invention"
DETAILED_DESC_OF_THE_INVENTION = "detailed description of the invention"


def extract_application_data(full_file_path):
    with open(full_file_path, 'rt') as f:
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

            if current_text is not None and FIELD_OF_THE_INVENTION in current_text.lower():
                # print "processing " + FIELD_OF_THE_INVENTION
                flag_field_of_invention = True
                flag_desc_related_art = False
                flag_summary_of_invention = False
                flag_detailed_desc_of_invention = False
                continue
            elif current_text is not None and DESC_OF_THE_RELATED_ART in current_text.lower():
                # print "processing " + DESC_OF_THE_RELATED_ART
                flag_field_of_invention = False
                flag_desc_related_art = True
                flag_summary_of_invention = False
                flag_detailed_desc_of_invention = False
                continue
            elif current_text is not None and SUMMARY_OF_THE_INVENTION in current_text.lower():
                # print "processing " + SUMMARY_OF_THE_INVENTION
                flag_field_of_invention = False
                flag_desc_related_art = False
                flag_summary_of_invention = True
                flag_detailed_desc_of_invention = False
                continue
            elif current_text is not None and DETAILED_DESC_OF_THE_INVENTION in current_text.lower():
                # print "processing " + DETAILED_DESC_OF_THE_INVENTION
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

    # print field_of_invention
    # print desc_related_art
    # print summary_of_invention
    # print detailed_desc_of_invention

    extracton_results = {FIELD_OF_THE_INVENTION: field_of_invention,
                        DESC_OF_THE_RELATED_ART: desc_related_art,
                        SUMMARY_OF_THE_INVENTION: summary_of_invention,
                        DETAILED_DESC_OF_THE_INVENTION: detailed_desc_of_invention}

    return extracton_results
