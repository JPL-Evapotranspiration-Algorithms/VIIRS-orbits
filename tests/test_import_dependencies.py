import pytest

# List of dependencies
dependencies = [
    "dateutil",
    "ephem",
    "geopandas",
    "numpy",
    "pyproj",
    "rasters",
    "shapely",
    "solar_apparent_time",
    "spacetrack"
]

# Generate individual test functions for each dependency
@pytest.mark.parametrize("dependency", dependencies)
def test_dependency_import(dependency):
    __import__(dependency)
