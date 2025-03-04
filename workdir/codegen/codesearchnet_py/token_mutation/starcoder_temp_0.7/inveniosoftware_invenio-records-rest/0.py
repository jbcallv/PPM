def transform_record(self, pid, record, links_factory=None, **kwargs):
        """Transform abstract into an it representation."""
        record = dict(record)
        links = links_factory(pid, record, **kwargs) if links_factory else {}
        return {
            "pid": pid,
            "title": record.get("title"),
            "authors": record.get("authors", []),
            "abstract": record.get("abstract"),
            "description": record.get("description"),
            "links": links,
        }

    def get_pid_by_object_type(self, object_type):
        """Return pid by object type."""
        return f"{object_type.lower()}-1"

    def get_pid_by_object_type_and_field(self, object_type, field):
        """Return pid by object type and field."""
        return f"{object_type.lower()}-{field.lower()}"

    def get_object_type_by_pid(self, pid):
        """Return object type by pid."""
        return pid.split("-")[0].capitalize()

    def get_field_by_pid(self, pid):
        """Return field by pid."""
        return pid.split("-")[-1].capitalize()

    def get_pid_by_record(self, record):
        """Return pid by record."""
        return record.get("pid")

