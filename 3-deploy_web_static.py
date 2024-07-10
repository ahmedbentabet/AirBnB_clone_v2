#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
using the functions do_pack and do_deploy.
"""

from fabric.api import local, env, put, run
from datetime import datetime
import os

# Define the servers where the commands will be executed
env.hosts = ['100.25.200.111', '100.27.4.15']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns the archive path if successful, otherwise returns None.
    """
    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate a timestamp for the archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"

    # Print message about packing
    print(f"Packing web_static to {archive_name}")

    # Create the .tgz archive
    result = local(f"tar -cvzf {archive_name} web_static", capture=True)

    # Check if the archive was created successfully
    if result.succeeded:
        return archive_name
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    Args:
        archive_path (str): The path to the archive to be distributed.
    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    if not os.path.exists(archive_path):
        return False

    # Get the archive file name without extension
    archive_name = os.path.basename(archive_path)
    no_ext = archive_name.split(".")[0]
    release_folder = f"/data/web_static/releases/{no_ext}/"

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, f"/tmp/{archive_name}")

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        run(f"mkdir -p {release_folder}")
        run(f"tar -xzf /tmp/{archive_name} -C {release_folder}")

        # Delete the archive from the web server
        run(f"rm /tmp/{archive_name}")

        # Move files to the correct location
        run(f"mv {release_folder}web_static/* {release_folder}")
        run(f"rm -rf {release_folder}web_static")

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        # linked to the new version of your code
        run(f"ln -s {release_folder} /data/web_static/current")

        return True
    except Exception:
        return False


def deploy():
    """
    Creates and distributes an archive to web servers.
    Returns the return value of do_deploy.
    """
    # Call the do_pack() function and store the path of the created archive
    archive_path = do_pack()

    # Return False if no archive has been created
    if archive_path is None:
        return False

    # Call the do_deploy(archive_path) using the new path of the new archive
    result = do_deploy(archive_path)

    # Return the return value of do_deploy
    return result
