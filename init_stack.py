import os
import shutil
import subprocess


INIT_IN_DEMO_FOLDER = True


def init_in_folder(project_name):
    project_name = "demo" if INIT_IN_DEMO_FOLDER else project_name
    os.mkdir(project_name) if not os.path.isdir(project_name) else None
    os.chdir(project_name)
    reset_demo_folder(project_name) if project_name == "demo" else None


def reset_demo_folder(project_name):
    shutil.rmtree(project_name) if os.path.isdir(project_name) else None


def installation_exists(cli_command):
    try:
        subprocess.run(cli_command, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False
    except:
        return False


def react_native(project_name):
    if not installation_exists(["npm", "--version"]):
        return

    # Init project folder
    init_in_folder(project_name)

    # Init and nstall React.js and React DOM
    os.system("npm init -y")
    os.system("npm install react react-dom")

    # Create the public folder
    os.mkdir("public")

    # Create the index.html file in the public folder
    index_html = '''\
<!DOCTYPE html>
<html>
    <head>
        <title>{project_name}</title>
    </head>
    <body>
        <div id="root"></div>
        <script src="./index.js"></script>
    </body>
</html>'''.format(project_name=project_name)
    with open("public/index.html", "w") as f:
        f.write(index_html)

    # Create the src folder
    os.makedirs("src")

    # Create the index.js file in the src folder
    index_js = '''\
import React from "react";
import ReactDOM from "react-dom";

const App = () => {{
    return (
        <div>
        <h1>Hello, {0}!</h1>
        </div>
    );
}};

ReactDOM.render(<App />, document.getElementById("root"));'''.format(project_name)
    with open("src/index.js", "w") as f:
        f.write(index_js)

    # Create the .gitignore file
    gitignore = '''\
node_modules
dist'''

    with open(".gitignore", "w") as f:
        f.write(gitignore)


if __name__ == "__main__":
    react_native("my-app")
