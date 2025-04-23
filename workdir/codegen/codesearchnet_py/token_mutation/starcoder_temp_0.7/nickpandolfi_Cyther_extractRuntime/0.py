def extractRuntime(runtime_dirs):
    """
    Used to find the company and company name to pass to gcc
    """
    company = ""
    company_name = ""
    for f in runtime_dirs:
        try:
            with open(f) as r:
                for line in r:
                    if line.startswith("CompanyName="):
                        company_name = line.split("=")[1].strip()
                    elif line.startswith("Company="):
                        company = line.split("=")[1].strip()
        except FileNotFoundError:
            pass
    return company, company_name


