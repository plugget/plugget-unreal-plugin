from pathlib import Path
import subprocess
import unreal
import importlib


# def project_plugins_dir():
#     project_path = unreal.Paths.project_plugins_dir()
#     project_path = unreal.Paths.convert_relative_path_to_full(project_path)
#     return Path(project_path)


def project_site_dir():
    content_path = unreal.Paths.project_content_dir()  # '../../../Users/USER/MyProject/Content/'
    content_path = unreal.Paths.convert_relative_path_to_full(content_path)  # 'C:/Users/USER/MyProject/Content/'
    return Path(content_path) / r"Python\Lib\site-packages"  # 'C:/Users/USER/MyProject/Content/Python/Lib/site-packages'


def pip_install(names):
    cmd = ['pip', 'install', *names, '-t', str(project_site_dir())]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    importlib.invalidate_caches()  # refresh modules
    out, err = proc.communicate()

    # print output
    out = out.decode().splitlines()
    err = err.decode().splitlines()
    for line in out:
        unreal.log(line)
    for line in err:
        unreal.log_error(line)


def setup():
    # install unreal-qt -> pyside & stylesheet
    # install plugget qt -> plugget
    # todo install from requirements.txt
    # get path current file
    file_path = Path(__file__).parent

    # todo upload unreal-qt to pypi
    # todo upload plugget-qt to pypi

    # core requires
    # - plugget
    pip_install(['git+https://github.com/hannesdelbeke/plugget-qt-search'])

    # for UI: =============================================================================================
    # - unreal-qt (optional)
    # - plugget-qt
    # - pyside2
    # - unrealstylesheet (optional)

    # todo add toml to repos
    # repo_urls = [
    # # "git+https://github.com/hannesdelbeke/plugget-unreal",
    # "git+https://github.com/hannesdelbeke/plugget-qt-search",
    # "git+https://github.com/hannesdelbeke/unreal_qt"
    # ]
    # pip_install(repo_urls)

    # add UI to menu Windows/Tools-section: Plugget Manager
    # import unimenu
    # menu = unimenu.Node(label="my menu")
    # item = unimenu.Node(label="hi", command='print("hi")')

    # for now just run it on startup, todo fix hack
    # import plugget_search_widget  # currently import creates the widget & shows it  # noqa

setup()
