import sys
import os
import requests as req
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QVBoxLayout, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from tqdm import tqdm
import webbrowser
import ctypes

def hide_console():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

class Dwn:
    def __init__(self, dwn_name, dwn_description, dwn_executable, dwn_url_part1, dwn_url_part2=""):
        self.dwn_name = dwn_name
        self.dwn_description = dwn_description
        self.dwn_executable = dwn_executable
        self.dwn_url_part1 = dwn_url_part1
        self.dwn_url_part2 = dwn_url_part2

class Tool:
    def __init__(self, name, code, command, got_latest, latestfn, info, downloads):
        self.name = name
        self.code = code
        self.command = command
        self.got_latest = got_latest
        self.latestfn = latestfn
        self.info = info
        self.downloads = downloads

tools = {
    "1" : Tool(
        "EchoX", "d1-1", 1, True,
        lambda: "",
        r"https://github.com/UnLovedCookie/EchoX",
        [
            Dwn(
                "EchoX", "", "EchoX.bat",
                r"https://github.com/UnLovedCookie/EchoX/releases/latest/download/EchoX.bat"
            )
        ]
    ),

    "2" : Tool(
        "Hone", "d2-1", 1, True,
        lambda: "",
        r"https://hone.gg",
        [
            Dwn(
                "Hone", "", "HoneInstaller.exe",
                r"https://download.overwolf.com/installer/prod/cfbc7eeb79ab95eb3f553c4344a186ee/Hone%20-%20Installer.exe"
            )
        ]
    ),

    "3" : Tool(
        "ShutUp10++", "d3-1", 1, True,
        lambda: "",
        r"https://www.oo-software.com/shutup10",
        [
            Dwn(
                "ShutUp10++", "", "ShutUp10.exe",
                r"https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe"
            )
        ]
    ),

    "4" : Tool(
        "Optimizer", "d4-1", 1, False,
        lambda: str(("hellzerg/optimizer")),
        r"https://github.com/hellzerg/optimizer",
        [
            Dwn(
                "Optimizer", "", "Optimizer.exe",
                r"https://github.com/hellzerg/optimizer/releases/download/16.2/Optimizer-16.2.exe",
                
            )
        ]
    ),

    "5" : Tool(
        "PyDebloatX", "d5-1", 1, True,
        lambda: "",
        r"https://github.com/Teraskull/PyDebloatX",
        [
            Dwn(
                "PyDebloatX", "", "PyDebloatX-Portable.exe",
                r"https://github.com/Teraskull/PyDebloatX/releases/latest/download/PyDebloatX_portable.exe"
            )
        ]
    ),

    "6" : Tool(
        "QuickBoost", "d6-1", 1, True,
        lambda: "",
        r"https://github.com/SanGraphic/QuickBoost",
        [
            Dwn(
                "QuickBoost", "", "QuickBoost.exe",
                r"https://github.com/SanGraphic/QuickBoost/releases/latest/download/QuickBoost.exe"
            )
        ]
    ),


    "7" : Tool(
        "WindowsSpyBlocker", "d7-1", 1, True,
        lambda: "",
        r"https://github.com/crazy-max/WindowsSpyBlocker",
        [
            Dwn(
                "WindowsSpyBlocker", "", "WindowsSpyBlocker.exe",
                r"https://github.com/crazy-max/WindowsSpyBlocker/releases/latest/download/WindowsSpyBlocker.exe"
            )
        ]
    ),

    "8" : Tool(
        "PrivateZilla", "d8-1", 1, True,
        lambda: "",
        r"https://github.com/builtbybel/privatezilla",
        [
            Dwn(
                "PrivateZilla", "", "PrivateZilla.zip",
                r"https://github.com/builtbybel/privatezilla/releases/latest/download/privatezilla.zip"
            )
        ]
    ),

    "9" : Tool(
        "ZusierAIO", "d9-1", 1, True,
        lambda: "",
        r"https://github.com/Zusier/Zusiers-optimization-Batch",
        [
            Dwn(
                "ZusierAIO", "", "ZusierAIO.bat",
                r"https://raw.githubusercontent.com/Zusier/Zusiers-optimization-Batch/master/Zusier%20AIO.bat"
            )
        ]
    ),

    "10" : Tool(
        "CoutX", "d10-1", 1, True,
        lambda: "",
        r"https://github.com/UnLovedCookie/CoutX",
        [
            Dwn(
                "CoutX", "", "CoutX-Setup.exe",
                r"https://github.com/UnLovedCookie/CoutX/releases/latest/download/CoutX-Setup.exe"
            )
        ]
    ),

    "11" : Tool(
        "InsiderEnroller", "t1-1", 1, False,
        lambda: str(("Jathurshan-2019/Insider-Enroller")),
        r"https://github.com/Jathurshan-2019/Insider-Enroller",
        [
            Dwn(
                "InsiderEnroller", "", "InsiderEnroller.zip",
                r"https://github.com/Jathurshan-2019/Insider-Enroller/releases/latest/download/Insider_Enrollerv",
                r".zip"
            )
        ]
    ),

    "12" : Tool(
        "Windows11Fixer", "t2-1", 1, False,
        lambda: str(("99natmar99/Windows-11-Fixer")),
        r"https://github.com/99natmar99/Windows-11-Fixer",
        [
            Dwn(
                "Windows11Fixer", "", "Windows11Fixer.zip",
                r"https://github.com/99natmar99/Windows-11-Fixer/releases/latest/download/Windows.11.Fixer.v",
                r".Portable.zip"
            )
        ]
    ),

    "13" : Tool(
        "DisableRoundedCorners", "t3-1", 1, True,
        lambda: "",
        r"https://github.com/valinet/Win11DisableRoundedCorners",
        [
            Dwn(
                "AntiRoundCorners", "", "AntiRoundCorners.exe",
                r"https://github.com/valinet/Win11DisableRoundedCorners/releases/latest/download/Win11DisableOrRestoreRoundedCorners.exe"
            )
        ]
    ),

    "14" : Tool(
        "Fix Drag&Drop", "t4-1", 1, True,
        lambda: "",
        r"https://github.com/HerMajestyDrMona/Windows11DragAndDropToTaskbarFix",
        [
            Dwn(
                "Fix Drag&Drop", "", "FixDragAndDrop.exe",
                r"https://github.com/HerMajestyDrMona/Windows11DragAndDropToTaskbarFix/releases/latest/download/Windows11DragAndDropToTaskbarFix.exe"
            )
        ]
    ),

    "15" : Tool(
        "Winaero Tweaker", "t5-1", 1, True,
        lambda: "",
        r"https://winaero.com/winaero-tweaker/",
        [
            Dwn(
                "Winaero Tweaker", "", "WinaeroTweaker.zip",
                r"https://winaerotweaker.com/download/winaerotweaker.zip"
            )
        ]
    ),

    "16" : Tool(
        "Process Hacker", "y6-1", 1, True,
        lambda: "",
        r"https://sourceforge.net/projects/processhacker/",
        [
            Dwn(
                "Process Hacker", "", "Process Hacker.exe",
                r"https://deac-fra.dl.sourceforge.net/project/processhacker/processhacker2/processhacker-2.39-setup.exe"
            )
        ]
    ),

    "17" : Tool(
        "REAL", "t7-1", 1, True,
        lambda: "",
        r"https://github.com/miniant-git/REAL",
        [
            Dwn(
                "REAL", "", "REAL.exe",
                r"https://github.com/miniant-git/REAL/releases/latest/download/REAL.exe"
            )
        ]
    ),

    "18" : Tool(
        "NVCleanstall", "t8-1", 1, True,
        lambda: "",
        r"",
        [
            Dwn(
                "NVCleanstall", "", "NVCleanstall.exe",
                r"https://us1-dl.techpowerup.com/files/mK8aMPQXCfeeBXjGJiCZEA/1703064607/NVCleanstall_1.16.0.exe"
            )
        ]
    ),

    "19" : Tool(
        "SophiApp", "t9-1", 1, True,
        lambda: str(("Sophia-Community/SophiApp")),
        r"https://github.com/Sophia-Community/SophiApp",
        [
            Dwn(
                "SophiApp", "", "SophiApp.zip",
                r"https://github.com/Sophia-Community/SophiApp/releases/download/1.0.97/SophiApp.zip",
            )
        ]
    ),

    "20" : Tool(
        "Choco", "a1-1", 1, True,
        lambda: "",
        r"https://github.com/xemulat/XToolbox/blob/main/files/choco.bat",
        [
            Dwn(
                "Choco", "", "choco.bat",
                r"https://raw.githubusercontent.com/xemulat/Windows-Toolkit/main/files/choco.bat"
            )
        ]
    ),
    "21" : Tool(
        "AutoRun", "a1-1", 1, True,
        lambda: "",
        r"https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns",
        [
            Dwn(
                "AutoRun", "", "AutoRun.zip",
                r"https://download.sysinternals.com/files/Autoruns.zip"
            )
        ]
    ),
    "22" : Tool(
        "Wise_Game_Booster", "a1-1", 1, True,
        lambda: "",
        r"https://www.wisecleaner.com/wise-game-booster.html",
        [
            Dwn(
                "Wise Game Booster", "", "Wise Game Booster.exe",
                r"https://downloads.wisecleaner.com/soft/WGBSetup_1.5.7.81.exe"
            )
        ]
    ),
    "23" : Tool(
        "DriverMax", "a1-1", 1, True,
        lambda: "",
        r"https://www.drivermax.com/",
        [
            Dwn(
                "DriverMax", "", "DriverMax.exe",
                r"https://www.drivermax.com/soft/dmx/drivermax.exe"
            )
        ]
    ),
    "24" : Tool(
        "cpu-z", "a1-1", 1, True,
        lambda: "",
        r"https://www.cpuid.com/softwares/cpu-z.html",
        [
            Dwn(
                "cpu-z", "", "cpu-z.exe",
                r"https://download.cpuid.com/cpu-z/cpu-z_2.08-en.exe"
            )
        ]
    ),
    "25" : Tool(
        "ADW Cleaner", "a1-1", 1, True,
        lambda: "",
        r"https://www.malwarebytes.com/adwcleaner",
        [
            Dwn(
                "ADW Cleaner", "", "ADW Cleaner.exe",
                r"https://adwcleaner.malwarebytes.com/adwcleaner?channel=release"
            )
        ]
    ),
    "26" : Tool(
        "Process Lasso", "a1-1", 1, True,
        lambda: "",
        r"https://bitsum.com/",
        [
            Dwn(
                "Process Lasso", "", "Process Lasso.exe",
                r"https://dl.bitsum.com/files/processlassosetup64.exe"
            )
        ]
    ),
    "27" : Tool(
        "Revo Uninstaller", "a1-1", 1, True,
        lambda: "",
        r"https://www.revouninstaller.com/products/revo-uninstaller-free/",
        [
            Dwn(
                "Revo Uninstaller", "", "Revo Uninstaller.exe",
                r"https://download.revouninstaller.com/download/revosetup.exe"
            )
        ]
    ),
    
}
names = {
    "1": "EchoX",
    "2": "Hone",
    "3": "ShutUp10++",
    "4": "Optimizer",
    "5": "PyDebloatX",
    "6": "QuickBoost",
    "7": "WindowsSpyBlocker",
    "8": "PrivateZilla",
    "9": "ZusierAIO",
    "10": "CoutX",
    "11": "InsiderEnroller",
    "12": "Windows11Fixer",
    "13": "DisableRoundedCorners",
    "14": "Fix Drag&Drop",
    "15": "Winaero Tweaker",
    "16": "Process Hacker",
    "17": "REAL",
    "18": "NVCleanstall",
    "19": "SophiApp",
    "20": "Choco",
    "21": "AutoRuns",
    "22": "Wise Game Booster",
    "23": "Drivermax",
    "24": "cpu-z",
    "25": "ADW Cleaner",
    "26": "Process Lasso",
    "27": "Revo Uninstaller",
}



class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PixelToolBox 1.1v')
        self.setGeometry(515, 300, 340, 165)
        self.setWindowIcon(QIcon('C:\\Users\\Administrator\\Desktop\\1111.jpg'))

        self.setStyleSheet("""
            QWidget {
                background-color: #28004d;
            }
            QLabel {
                color: #e6e6e6;
            }
            QLineEdit {
                background-color: #4d004d;
                color: #e6e6e6;
                border: 2px solid #e6e6e6;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton {
                background-color: #4d004d;
                color: #e6e6e6;
                border-radius: 4px;
                padding: 5px 10px;
            }
        """)

        title_label = QLabel('Ptox Tool\n')
        title_label.setStyleSheet("font-size: 22px; font-weight: bold;")
        title_label.setAlignment(QtCore.Qt.AlignCenter)

        launch_button_tools = QPushButton('Tools')
        launch_button_tools.clicked.connect(self.show_tools)

        button1 = QPushButton('Discord')
        button2 = QPushButton('Web Site')
        button1.clicked.connect(self.Discord)
        button2.clicked.connect(self.Help)

        vbox = QVBoxLayout()
        vbox.addWidget(title_label)
        vbox.addWidget(launch_button_tools)
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addStretch()

        self.setLayout(vbox)

    def show_tools(self):
        tools_window = DownloaderApp()
        tools_window.show()

    def Discord(self):
        DiscordUrl = "https://discord.gg/83Hyg3DKar"
        webbrowser.open(DiscordUrl)

    def Help(self):
        PixelWebsite = "https://shorturl.at/owIM3"
        webbrowser.open(PixelWebsite)

class DownloaderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ptox-Tools')
        self.setGeometry(450, 235, 450, 150)
        self.setWindowIcon(QIcon('C:\\Users\\Administrator\\Desktop\\1111.jpg'))

        self.setStyleSheet("""
            QWidget {
                background-color: #28004d;
            }
            QLabel {
                color: #e6e6e6;
            }
            QLineEdit {
                background-color: #4d004d;
                color: #e6e6e6;
                border: 2px solid #e6e6e6;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton {
                background-color: #4d004d;
                color: #e6e6e6;
                border-radius: 4px;
                padding: 5px 10px;
            }
        """)

        self.tools_layout = QGridLayout()
        title_label_1 = QLabel('Tools\n')
        title_label_1.setStyleSheet("font-size: 20px; font-weight: bold;")
        title_label_1.setAlignment(QtCore.Qt.AlignCenter)
        
        row, col = 0, 0
        for code, tool in tools.items():
            button = QPushButton(names[code])
            button.clicked.connect(lambda _, c=code: self.download_tool(c))
            self.tools_layout.addWidget(button, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

        back_button = QPushButton('Back')
        back_button.clicked.connect(self.close)

        vbox = QVBoxLayout()
        vbox.addWidget(title_label_1)
        vbox.addLayout(self.tools_layout)
        vbox.addWidget(back_button)

        self.setLayout(vbox)

    def download_tool(self, code):
        tool = tools[code]

        if tool.got_latest:
            latest_version = tool.latestfn()
            QMessageBox.information(self, 'Latest Version', f'Latest version for {tool.name}: {latest_version}')

        for download in tool.downloads:
            self.download_file(download)

    def download_file(self, download):
        url = download.dwn_url_part1 + download.dwn_url_part2
        response = req.get(url, stream=True)

        file_size = int(response.headers.get('Content-Length', 0))
        chunk_size = 1024
        num_bars = file_size // chunk_size

        progress = tqdm(total=file_size, unit='B', unit_scale=True)

        with open(download.dwn_executable, 'wb') as file, progress:
            for data in response.iter_content(chunk_size=chunk_size):
                progress.update(len(data))
                file.write(data)

        QMessageBox.information(self, 'Download Complete', f'Download of {download.dwn_name} complete.')

if __name__ == '__main__':
    hide_console()
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
