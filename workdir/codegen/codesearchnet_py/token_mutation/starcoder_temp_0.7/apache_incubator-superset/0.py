def export_dashboards(print_stdout, dashboard_file):
    """Export ##ing to JSON"""
    dashboards = yaml.safe_load(dashboard_file)
    for dashboard in dashboards:
        dash_title = dashboard.pop("title")
        dash_filename = dash_title.lower().replace(" ", "_")
        dash_filename = re.sub("[^0-9a-zA-Z_-]", "", dash_filename)
        json_file = os.path.join(dashboard_dir, dash_filename + ".json")
        with open(json_file, "w") as f:
            json.dump(dashboard, f, indent=4)
        if print_stdout:
            print(json.dumps(dashboard, indent=4))


