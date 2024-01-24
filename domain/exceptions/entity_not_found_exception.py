class EntityNotFoundException(Exception):
    """Exception raised when an entity is not found in the repository."""

    def __init__(self, entity_name, entity_id):
        self.entity_name = entity_name
        self.entity_id = entity_id
        message = f"{entity_name} with ID {entity_id} was not found."
        super().__init__(message)