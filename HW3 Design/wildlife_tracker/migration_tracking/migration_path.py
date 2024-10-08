from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat



class MigrationPath:
    def __init__(self,
                path_id: int,
                start_location: Habitat,
                duration: Optional[int] = None
                 ) -> None:
                self.duration = duration
                self.path_id = path_id
                self.start_location = start_location
    
    def remove_migration_path(path_id: int) -> None:
        pass

    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass