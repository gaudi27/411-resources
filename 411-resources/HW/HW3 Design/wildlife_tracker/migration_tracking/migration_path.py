from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration import MigrationPath


class MigrationPath:
    def __init__(self,
                migration_path: MigrationPath,
                path_id: int,
                start_location: Habitat,
                paths: dict[int, MigrationPath] = {},
                duration: Optional[int] = None
                 ) -> None:
                self.duration = duration
                self.path_id = path_id
                self.migration_path = migration_path
                self.start_location = start_location
                self.paths = paths
        
    
    def remove_migration_path(path_id: int) -> None:
        pass

    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    def get_migration_path_by_id(path_id: int) -> MigrationPath:
        pass

    def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:
        pass