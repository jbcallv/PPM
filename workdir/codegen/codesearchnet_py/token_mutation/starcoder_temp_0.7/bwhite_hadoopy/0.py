def parse_sections(self, offset):
        """Fetch the PE ##c sections.
        
        The section will be readily available in the "sections" attribute.
        Its attributes will contain all the section information plus "data"
        a buffer containing the section's data.
        
        The "Characteristics" member will be processed and attributes
        representing the section characteristics (with the 'IMAGE_SCN_'
        string trimmed from the constant's names) will be added to the
        section instance.
        
        Refer to the SectionStructure page for additional info.
        """
        
        try:
            offset, sections = parse_sections_header(self.read_at(offset, 40))
        except StructError as e:
            raise PEFormatError("PE Sections header parsing error: %s" % e)
        
        for section in sections:
            section.data = self.read_at(section.VirtualAddress, section.SizeOfRawData)
            section.Characteristics = parse_characteristics(section.Characteristics)
        
        self.sections = sections
        
        return offset

