"""Handles the installation of downloaded modules."""
import os
import shutil
import tempfile
import zipfile

from _cloud import utils


def install(zipfile, metadata):
    """Install a module once it has been downloaded locally.

    Takes the GitHub repo zipped up in a BytesIO, as well as all the metadata
    about the package.
    """
    # Initial extraction (to a temporary directory)
    zipfile = zipfile.ZipFile(zipfile)
    extract_to = tempfile.gettempdir()
    zipfile.extractall(extract_to)
    # Moving of the main module to a site-packages dir
    extracted = os.path.join(extract_to, zipfile.namelist()[0])
    source = os.path.join(extracted, metadata["entry_point"])
    destination = os.path.join(
        utils.pick_site_dir(metadata["py_versions"]),
        os.path.basename(metadata["entry_point"])
    )
    shutil.move(source, destination)
