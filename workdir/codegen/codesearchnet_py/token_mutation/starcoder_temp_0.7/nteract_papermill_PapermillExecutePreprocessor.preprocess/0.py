def preprocess(self, nb_man, resources, km=None):
        """
        ##age the parent " process changes slightly
        """
        #print("Preprocessing")
        for cell in nb_man.cells:
            cell.source = re.sub(r'\s+','', cell.source)
            if cell.cell_type == "code":
                if "age_parent" in cell.source:
                    cell.source = re.sub(r"age_parent\(.*", "age_parent(km)", cell.source)
        return nb_man, resources

