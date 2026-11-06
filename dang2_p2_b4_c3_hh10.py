import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang2_p2_b4_c3_hh10(self):
            # Khai báo biến
            x=symbols('x')
            y=symbols('y')
            a=randint(2,15)
            b=randint(2,14)
            c=sqrt(a**2-b**2)
            t=b-1
            n=a+1
            d=randint(2,13)


            while a<=b or c==b or d>=b:
                x=symbols('x')
                y=symbols('y')
                a=randint(2,15)
                b=randint(2,14)
                c=sqrt(a**2-b**2)
                t=b-1
                n=a+1
                d=randint(2,13)
            ctb=sqrt(Rational((b**2*a**2-d**2*a**2),b**2))
            ctb1=sqrt(Rational((b**2*a**2-d**2*a**2+1),b**2))
            ctb2=sqrt(Rational((b**2*a**2-d**2*a**2-1),b**2))


            # Nội dung câu hỏi
            noidungcauhoi = ('Người ta muốn làm một hồ bơi có dạng hình elip với độ dài hai bán trục lần lượt là $%s$m và $%s$m. Xét hệ trục tọa độ $(Oxy)$ (đơn vị trên các trục là mét)'
                            ' có hai trục tọa độ chứa hai trục của elip, gốc $O$ là tâm của elip (hình vẽ).'
                            '\\begin{center} \n'
                            '''\\definecolor{qqccqq}{rgb}{0.,0.8,0.}
            \\definecolor{qqzzcc}{rgb}{0.,0.6,0.8}
            \\definecolor{wwccff}{rgb}{0.4,0.8,1.}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \\clip(-0.13381812920031844,-0.3516181434061261) rectangle (5.110031680458738,2.125648835639695);
                \\fill[line width=1.pt,color=wwccff,fill=wwccff,fill opacity=0.30000001192092896] (0.5156352642615678,1.1349660495613518) -- (0.682697800266148,1.2604780569788587) -- (0.8686925249120088,1.3564753342154319) -- (1.1266852074852995,1.452472611452005) -- (1.3786780602313045,1.518470739552149) -- (1.6546702322864528,1.5784690378250072) -- (1.9606615534780303,1.626467676443294) -- (2.2786525343241792,1.656466825579723) -- (2.668641473097759,1.6624666554070089) -- (3.010631773253051,1.656466825579723) -- (3.3886210523720584,1.6144680167887222) -- (3.6766128840817784,1.5664693781704357) -- (3.9286057368277834,1.4944714202430058) -- (4.126600121128216,1.422473462315576) -- (4.258596377328504,1.3684749938700036) -- (4.444591101974365,1.2544782271515729) -- (4.546588209038224,1.116482141123999) -- (4.600586677483797,0.9904857147509968) -- (4.600586677483797,0.8764889480325662) -- (4.552736275438784,0.7754981513058469) -- (4.456590761628937,0.678494563732134) -- (4.276595866810362,0.5584979671864175) -- (4.114600461473644,0.474500349604416) -- (3.83260845959121,0.38450290219512867) -- (3.4606190102994887,0.28850562495855553) -- (3.1786270084170543,0.2465068161675548) -- (2.7946378994707612,0.21050783720383984) -- (2.3206513431151805,0.18050868806741074) -- (1.942662063996173,0.18650851789469655) -- (1.4866749971224495,0.25250664599484063) -- (1.1146855478307278,0.34250409340412796) -- (0.8206938862937221,0.4565008601225586) -- (0.5867005230295746,0.6184962654592757) -- (0.45470426682928633,0.7984911602778504) -- (0.4326811338949127,0.9769581821962947) -- cycle;
                \\fill[line width=0.pt,color=qqzzcc,fill=qqzzcc,fill opacity=0.20000000298023224] (1.1146855478307278,0.34250409340412796) -- (0.8206938862937221,0.4565008601225586) -- (0.5867005230295746,0.6184962654592757) -- (0.45470426682928633,0.7984911602778504) -- (0.4326811338949127,0.9769581821962947) -- (0.5156352642615678,1.1349660495613518) -- (0.682697800266148,1.2604780569788587) -- (0.8686925249120088,1.3564753342154319) -- (1.1266852074852995,1.452472611452005) -- (1.3786780602313045,1.518470739552149) -- (1.6546702322864528,1.5784690378250072) -- (1.9606615534780303,1.626467676443294) -- (2.2786525343241792,1.656466825579723) -- (2.668641473097759,1.6624666554070089) -- (3.010631773253051,1.656466825579723) -- (3.3886210523720584,1.6144680167887222) -- (3.6766128840817784,1.5664693781704357) -- (3.9286057368277834,1.4944714202430058) -- (4.126600121128216,1.422473462315576) -- (4.258596377328504,1.3684749938700036) -- (4.444591101974365,1.2544782271515729) -- (4.546588209038224,1.116482141123999) -- (4.600586677483797,0.9904857147509968) -- (4.600586677483797,0.8764889480325662) -- (4.456590761628937,0.678494563732134) -- (4.4658319483880025,0.8663526750407547) -- (4.396592463356078,1.0084852042328543) -- (4.246596717673933,1.1284818007785706) -- (3.9886040351006415,1.248478397324287) -- (3.7486108420092084,1.3384758447335745) -- (3.334622583926486,1.4104738026610042) -- (2.878635517052763,1.4284732921428618) -- (2.500646237933755,1.386474483351861) -- (2.1946549167421776,1.3264761850790028) -- (1.7506675095230262,1.182480269224143) -- (1.4755330585042914,1.036211132458191) -- (1.262222437561464,0.8624024783566283) -- (1.1279157503011652,0.7004444143074448) -- (1.0906862285215846,0.5405906681264787) -- cycle;
                \\fill[line width=0.pt,color=qqccqq,fill=qqccqq,fill opacity=0.5] (0.12398241978776435,0.8034548228084794) -- (0.,0.8163937004656397) -- (0.,2.) -- (5.,2.) -- (5.007772797337614,-0.2586976403589206) -- (0.,-0.26601118689514214) -- (0.18821571829702263,0.6499790400830991) -- (0.26001761345928165,0.5446695938451195) -- (0.4,0.4) -- (0.6286006752922113,0.26224880620690133) -- (0.9541026000277856,0.14257898093646987) -- (1.265244145730908,0.04205632770930746) -- (1.6,0.) -- (2.083785750580661,-0.048892739496220444) -- (2.442795226391956,-0.0536795325070377) -- (2.82095187424652,-0.048892739496220444) -- (3.2517632452200744,0.003761983622769392) -- (3.6538538581287248,0.06599029276339374) -- (4.041584092004924,0.16651294599055616) -- (4.38144639577295,0.2861827712609876) -- (4.620786046313813,0.43457335459632257) -- (4.8,0.6) -- (4.899063097446748,0.7677512213269528) -- (4.911250510541688,0.993218363583341) -- (4.821831352768139,1.1430187201972768) -- (4.745242664595062,1.257901752456891) -- (4.608039029016554,1.3522268671883053) -- (4.460162464999528,1.4194762182110197) -- (4.282113295762114,1.4911904669316443) -- (4.131266082935973,1.5357027592409975) -- (3.9323146802039033,1.586763649189347) -- (3.656774262195837,1.6431996384199148) -- (3.3646350238258393,1.69299609950571) -- (3.012740032152887,1.712914683940028) -- (2.6641648045523207,1.7162344480124143) -- (2.2823919362278917,1.7062751557952553) -- (2.0483115777026244,1.6958939787073044) -- (1.7860975218103121,1.6740098890772446) -- (1.5584871888709466,1.636641028445408) -- (1.3214753878233605,1.5892386682358908) -- (1.0410114232503835,1.5102347345533622) -- (0.7801336010972534,1.4071139096132093) -- (0.5624845969353073,1.320309277980564) -- (0.36173560144800176,1.2055955662735325) -- (0.2342158182477585,1.0869121331341787) -- (0.15022846704014392,0.945183477971329) -- cycle;
                \\fill[line width=0.pt,color=qqccqq,fill=qqccqq,fill opacity=0.6000000238418579] (0.,0.8163937004656397) -- (0.12398241978776435,0.8034548228084794) -- (0.18821571829702263,0.6499790400830991) -- (0.,-0.26601118689514214) -- cycle;
                \\draw [line width=1.pt,color=wwccff] (0.5156352642615678,1.1349660495613518)-- (0.682697800266148,1.2604780569788587);
                \\draw [line width=1.pt,color=wwccff] (0.682697800266148,1.2604780569788587)-- (0.8686925249120088,1.3564753342154319);
                \\draw [line width=1.pt,color=wwccff] (0.8686925249120088,1.3564753342154319)-- (1.1266852074852995,1.452472611452005);
                \\draw [line width=1.pt,color=wwccff] (1.1266852074852995,1.452472611452005)-- (1.3786780602313045,1.518470739552149);
                \\draw [line width=1.pt,color=wwccff] (1.3786780602313045,1.518470739552149)-- (1.6546702322864528,1.5784690378250072);
                \\draw [line width=1.pt,color=wwccff] (1.6546702322864528,1.5784690378250072)-- (1.9606615534780303,1.626467676443294);
                \\draw [line width=1.pt,color=wwccff] (1.9606615534780303,1.626467676443294)-- (2.2786525343241792,1.656466825579723);
                \\draw [line width=1.pt,color=wwccff] (2.2786525343241792,1.656466825579723)-- (2.668641473097759,1.6624666554070089);
                \\draw [line width=1.pt,color=wwccff] (2.668641473097759,1.6624666554070089)-- (3.010631773253051,1.656466825579723);
                \\draw [line width=1.pt,color=wwccff] (3.010631773253051,1.656466825579723)-- (3.3886210523720584,1.6144680167887222);
                \\draw [line width=1.pt,color=wwccff] (3.3886210523720584,1.6144680167887222)-- (3.6766128840817784,1.5664693781704357);
                \\draw [line width=1.pt,color=wwccff] (3.6766128840817784,1.5664693781704357)-- (3.9286057368277834,1.4944714202430058);
                \\draw [line width=1.pt,color=wwccff] (3.9286057368277834,1.4944714202430058)-- (4.126600121128216,1.422473462315576);
                \\draw [line width=1.pt,color=wwccff] (4.126600121128216,1.422473462315576)-- (4.258596377328504,1.3684749938700036);
                \\draw [line width=1.pt,color=wwccff] (4.258596377328504,1.3684749938700036)-- (4.444591101974365,1.2544782271515729);
                \\draw [line width=1.pt,color=wwccff] (4.444591101974365,1.2544782271515729)-- (4.546588209038224,1.116482141123999);
                \\draw [line width=1.pt,color=wwccff] (4.546588209038224,1.116482141123999)-- (4.600586677483797,0.9904857147509968);
                \\draw [line width=1.pt,color=wwccff] (4.600586677483797,0.9904857147509968)-- (4.600586677483797,0.8764889480325662);
                \\draw [line width=1.pt,color=wwccff] (4.600586677483797,0.8764889480325662)-- (4.552736275438784,0.7754981513058469);
                \\draw [line width=1.pt,color=wwccff] (4.552736275438784,0.7754981513058469)-- (4.456590761628937,0.678494563732134);
                \\draw [line width=1.pt,color=wwccff] (4.456590761628937,0.678494563732134)-- (4.276595866810362,0.5584979671864175);
                \\draw [line width=1.pt,color=wwccff] (4.276595866810362,0.5584979671864175)-- (4.114600461473644,0.474500349604416);
                \\draw [line width=1.pt,color=wwccff] (4.114600461473644,0.474500349604416)-- (3.83260845959121,0.38450290219512867);
                \\draw [line width=1.pt,color=wwccff] (3.83260845959121,0.38450290219512867)-- (3.4606190102994887,0.28850562495855553);
                \\draw [line width=1.pt,color=wwccff] (3.4606190102994887,0.28850562495855553)-- (3.1786270084170543,0.2465068161675548);
                \\draw [line width=1.pt,color=wwccff] (3.1786270084170543,0.2465068161675548)-- (2.7946378994707612,0.21050783720383984);
                \\draw [line width=1.pt,color=wwccff] (2.7946378994707612,0.21050783720383984)-- (2.3206513431151805,0.18050868806741074);
                \\draw [line width=1.pt,color=wwccff] (2.3206513431151805,0.18050868806741074)-- (1.942662063996173,0.18650851789469655);
                \\draw [line width=1.pt,color=wwccff] (1.942662063996173,0.18650851789469655)-- (1.4866749971224495,0.25250664599484063);
                \\draw [line width=1.pt,color=wwccff] (1.4866749971224495,0.25250664599484063)-- (1.1146855478307278,0.34250409340412796);
                \\draw [line width=1.pt,color=wwccff] (1.1146855478307278,0.34250409340412796)-- (0.8206938862937221,0.4565008601225586);
                \\draw [line width=1.pt,color=wwccff] (0.8206938862937221,0.4565008601225586)-- (0.5867005230295746,0.6184962654592757);
                \\draw [line width=1.pt,color=wwccff] (0.5867005230295746,0.6184962654592757)-- (0.45470426682928633,0.7984911602778504);
                \\draw [line width=1.pt,color=wwccff] (0.45470426682928633,0.7984911602778504)-- (0.4326811338949127,0.9769581821962947);
                \\draw [line width=1.pt,color=wwccff] (0.4326811338949127,0.9769581821962947)-- (0.5156352642615678,1.1349660495613518);
                \\draw [line width=1.pt] (0.12398241978776435,0.8034548228084794)-- (0.15022846704014392,0.945183477971329);
                \\draw [line width=1.pt] (0.2342158182477585,1.0869121331341787)-- (0.36173560144800176,1.2055955662735325);
                \\draw [line width=1.pt] (0.5624845969353073,1.320309277980564)-- (0.7801336010972534,1.4071139096132093);
                \\draw [line width=1.pt] (0.5624845969353073,1.320309277980564)-- (0.36173560144800176,1.2055955662735325);
                \\draw [line width=1.pt] (0.2342158182477585,1.0869121331341787)-- (0.15022846704014392,0.945183477971329);
                \\draw [line width=1.pt] (0.7801336010972534,1.4071139096132093)-- (1.0410114232503835,1.5102347345533622);
                \\draw [line width=1.pt] (1.0410114232503835,1.5102347345533622)-- (1.3214753878233605,1.5892386682358908);
                \\draw [line width=1.pt] (1.3214753878233605,1.5892386682358908)-- (1.5584871888709466,1.636641028445408);
                \\draw [line width=1.pt] (1.5584871888709466,1.636641028445408)-- (1.7860975218103121,1.6740098890772446);
                \\draw [line width=1.pt] (1.7860975218103121,1.6740098890772446)-- (2.0483115777026244,1.6958939787073044);
                \\draw [line width=1.pt] (2.0483115777026244,1.6958939787073044)-- (2.2823919362278917,1.7062751557952553);
                \\draw [line width=1.pt] (2.2823919362278917,1.7062751557952553)-- (2.6641648045523207,1.7162344480124143);
                \\draw [line width=1.pt] (2.6641648045523207,1.7162344480124143)-- (3.012740032152887,1.712914683940028);
                \\draw [line width=1.pt] (3.012740032152887,1.712914683940028)-- (3.3646350238258393,1.69299609950571);
                \\draw [line width=1.pt] (3.3646350238258393,1.69299609950571)-- (3.656774262195837,1.6431996384199148);
                \\draw [line width=1.pt] (3.656774262195837,1.6431996384199148)-- (3.9323146802039033,1.586763649189347);
                \\draw [line width=1.pt] (3.9323146802039033,1.586763649189347)-- (4.131266082935973,1.5357027592409975);
                \\draw [line width=1.pt] (4.131266082935973,1.5357027592409975)-- (4.282113295762114,1.4911904669316443);
                \\draw [line width=1.pt] (4.282113295762114,1.4911904669316443)-- (4.460162464999528,1.4194762182110197);
                \\draw [line width=1.pt] (4.460162464999528,1.4194762182110197)-- (4.608039029016554,1.3522268671883053);
                \\draw [line width=1.pt] (0.12398241978776435,0.8034548228084794)-- (0.18821571829702263,0.6499790400830991);
                \\draw [line width=1.pt] (0.18821571829702263,0.6499790400830991)-- (0.26001761345928165,0.5446695938451195);
                \\draw [line width=1.pt] (0.26001761345928165,0.5446695938451195)-- (0.4,0.4);
                \\draw [line width=1.pt] (0.4,0.4)-- (0.6286006752922113,0.26224880620690133);
                \\draw [line width=1.pt] (0.6286006752922113,0.26224880620690133)-- (0.9541026000277856,0.14257898093646987);
                \\draw [line width=1.pt] (0.9541026000277856,0.14257898093646987)-- (1.265244145730908,0.04205632770930746);
                \\draw [line width=1.pt] (1.265244145730908,0.04205632770930746)-- (1.6,0.);
                \\draw [line width=1.pt] (1.6,0.)-- (2.083785750580661,-0.048892739496220444);
                \\draw [line width=1.pt] (2.083785750580661,-0.048892739496220444)-- (2.442795226391956,-0.0536795325070377);
                \\draw [line width=1.pt] (2.442795226391956,-0.0536795325070377)-- (2.82095187424652,-0.048892739496220444);
                \\draw [line width=1.pt] (2.82095187424652,-0.048892739496220444)-- (3.2517632452200744,0.003761983622769392);
                \\draw [line width=1.pt] (3.2517632452200744,0.003761983622769392)-- (3.6538538581287248,0.06599029276339374);
                \\draw [line width=1.pt] (3.6538538581287248,0.06599029276339374)-- (4.041584092004924,0.16651294599055616);
                \\draw [line width=1.pt] (4.041584092004924,0.16651294599055616)-- (4.38144639577295,0.2861827712609876);
                \\draw [line width=1.pt] (4.38144639577295,0.2861827712609876)-- (4.620786046313813,0.43457335459632257);
                \\draw [line width=1.pt] (4.620786046313813,0.43457335459632257)-- (4.8,0.6);
                \\draw [line width=1.pt] (4.8,0.6)-- (4.899063097446748,0.7677512213269528);
                \\draw [line width=1.pt] (4.899063097446748,0.7677512213269528)-- (4.911250510541688,0.993218363583341);
                \\draw [line width=1.pt] (4.911250510541688,0.993218363583341)-- (4.821831352768139,1.1430187201972768);
                \\draw [line width=1.pt] (4.821831352768139,1.1430187201972768)-- (4.745242664595062,1.257901752456891);
                \\draw [line width=1.pt] (4.745242664595062,1.257901752456891)-- (4.608039029016554,1.3522268671883053);
            \\end{tikzpicture}
            \\scalebox{0.6}{
                            \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                \\clip(-5.839179966992777,-2.923209967642699) rectangle (4.5,3.5);
                \\draw [rotate around={0.:(0.,0.)}] (0.,0.) ellipse (3.cm and 2.23606797749979cm);
                \\draw (3.8,-0.1) node[anchor=north west] {$x$};
                \\draw (-0.6,3.5) node[anchor=north west] {$y$};
                \\draw (-0.5,-0) node[anchor=north west] {$O$};
                \\draw (-0.7,2.8) node[anchor=north west] {$%s$};
                \\draw (3,0) node[anchor=north west] {$%s$};
                \\draw [->] (-4.,0.) -- (4.2,0.);
                \\draw [->] (0.,-4.) -- (0.,3.5);
            \\end{tikzpicture}}'''
                            '\\end{center} \n'
                            %(latex(a),latex(b),latex(b),latex(a),))



            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Phương trình chính tắc của elip là $\\dfrac{x^2}{%s}+\\dfrac{y^2}{%s}=1$'%(latex(a**2),latex(b**2))
            nb_da_1_s = 'Phương trình chính tắc của elip là $\\dfrac{x^2}{%s}+\\dfrac{y^2}{%s}=1$'%(latex(b**2),latex(a**2))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Phương trình chính tắc của elip là $\\dfrac{x^2}{%s}+\\dfrac{y^2}{%s}=1$'%(latex(a**2),latex(b**2))
            nb_da_2_s = 'Phương trình chính tắc của elip là $\\dfrac{x^2}{%s}-\\dfrac{y^2}{%s}=1$'%(latex(a**2),latex(b**2))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]

            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Elip có $a=%s;b=%s$ nên có phương trình chính tắc là $\\dfrac{x^2}{%s^2}+\\dfrac{y^2}{%s^2}=1\\Leftrightarrow \\dfrac{x^2}{%s}+\\dfrac{y^2}{%s}=1$.'

                            %(latex(a),latex(b),latex(a),latex(b),latex(a**2),latex(b**2),)
                        )
            loigiai_nb_2 =  ('Elip có $a=%s;b=%s$ nên có phương trình chính tắc là $\\dfrac{x^2}{%s^2}+\\dfrac{y^2}{%s^2}=1\\Leftrightarrow \\dfrac{x^2}{%s}+\\dfrac{y^2}{%s}=1$.'

                            %(latex(a),latex(b),latex(a),latex(b),latex(a**2),latex(b**2),)
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Xét các điểm $M,N$ cùng thuộc trục lớn của elip và cách đều $O$ một khoảng bằng $%s$m về hai phía của $O$. Khi đó tổng khoảng cách từ mọi điểm trên đường elip đến $M$ và $N$ luôn bằng $%s$m'%(latex(c),2*a)
            th_da_1_s = 'Xét các điểm $M,N$ cùng thuộc trục lớn của elip và cách đều $O$ một khoảng bằng $%s$m về hai phía của $O$. Khi đó tổng khoảng cách từ mọi điểm trên đường elip đến $M$ và $N$ luôn bằng $%s$m'%(latex(c),a)
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True Xét các điểm $M,N$ cùng thuộc trục lớn của elip và cách đều $O$ một khoảng bằng $%s$m về hai phía của $O$. Tổng khoảng cách từ mọi điểm trên đường elip đến $M$ và $N$ luôn bằng $%s$m'%(latex(c),2*a)
            th_da_2_s = 'Xét các điểm $M,N$ cùng thuộc trục lớn của elip và cách đều $O$ một khoảng bằng $%s$m về hai phía của $O$. Tổng khoảng cách từ mọi điểm trên đường elip đến $M$ và $N$ luôn bằng $%s$m'%(b,2*a)
            list_th_da_2=[th_da_2_d,th_da_2_s]

            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Ta có $a=%s;b=%s$ nên $c=\\sqrt{a^2-b^2}=\\sqrt{%s^2-%s^2}=%s$.\\\\ \n'
                            'Các tiêu điểm của elip có tọa độ là $(%s;0)$ và $(%s;0)$.\\\\ \n'
                            'Vậy $M$ và$ N$ chính là các tiêu điểm của elip. Vì vậy tổng khoảng khách từ mọi điểm trên đường elip đến $M$ và $N$ luôn bằng $2a=%s$m không đổi.'
                            %(latex(a),latex(b),latex(a),latex(b),latex(c),
                            latex(-c),latex(c),latex(2*a),)
                        )
            loigiai_th_2 = ('Ta có $a=%s;b=%s$ nên $c=\\sqrt{a^2-b^2}=\\sqrt{%s^2-%s^2}=%s$.\\\\ \n'
                            'Các tiêu điểm của elip có tọa độ là $(%s;0)$ và $(%s;0)$.\\\\ \n'
                            'Vậy $M$ và$ N$ chính là các tiêu điểm của elip. Vì vậy tổng khoảng khách từ mọi điểm trên đường elip đến $M$ và $N$ luôn bằng $2a=%s$m không đổi.'
                            %(latex(a),latex(b),latex(a),latex(b),latex(c),
                            latex(-c),latex(c),
                            latex(2*a),)
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Một người đứng ở vị trí $P$ cách $O$ một khoảng bằng $%s$m. Người đó đứng ở trong hồ '%(latex(t))
            vd_da_1_s = 'Một người đứng ở vị trí $P$ cách $O$ một khoảng bằng $%s$m. Người đó đứng ở ngoài hồ '%(latex(t))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Một người đứng ở vị trí $P$ cách $O$ một khoảng bằng $%s$m. Người đó đứng ở ngoài hồ '%(latex(n))
            vd_da_2_s = 'Một người đứng ở vị trí $P$ cách $O$ một khoảng bằng $%s$m. Người đó đứng ở trong hồ '%(latex(n))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]

            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('Gọi giao điểm của đường thẳng $OP$ và elip là $Q$. Vì độ dài bán trục bé là $%s$m nên $OQ\\ge %s$. \\\\ \n''Suy ra $OQ>OP=%s$m. Vậy $P$ ở vị trí trong hồ.'
                            %(latex(b),latex(b),latex(t))
                        )

            loigiai_vd_2 = ('Gọi giao điểm của đường thẳng $OP$ và elip là $Q$. Vì độ dài bán trục lớn là $%s$m nên $OQ\\le %s$.\\\\ \n'' Suy ra $OQ<OP=%s$m. Vậy $P$ ở vị trí ngoài hồ.'
                            %(latex(a),latex(a),latex(n))
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Xét vị trí $C$ trên mép hồ cách trục lớn một khoảng bằng $%s$m. Khi đó vị trí $C$ cách trục nhỏ một khoảng bằng $%s$m'%(latex(d),latex(ctb))
            vdc_da_1_s = 'Xét vị trí $C$ trên mép hồ cách trục lớn một khoảng bằng $%s$m. Khi đó vị trí $C$ cách trục nhỏ một khoảng bằng $%s$m'%(latex(d),latex(ctb1))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Xét vị trí $C$ trên mép hồ cách trục lớn một khoảng bằng $%s$m. Khi đó vị trí $C$ cách trục nhỏ một khoảng bằng $%s$m'%(latex(d),latex(ctb))
            vdc_da_2_s = 'Xét vị trí $C$ trên mép hồ cách trục lớn một khoảng bằng $%s$m. Khi đó vị trí $C$ cách trục nhỏ một khoảng bằng $%s$m'%(latex(d),latex(ctb2))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Giả sử $C(x_0;y_0)$. Ta có $\\heva{&\\dfrac{x_0^2}{%s}+\\dfrac{y_0^2}{%s}=1\\\\ &|y_0|=%s} \\Rightarrow \\heva{& \\dfrac{x_0^2}{%s}+\\dfrac{%s^2}{%s}=1\\\\ & |y_0|=%s }\\Rightarrow \\heva{&|x_0|=%s\\\\& |y_0|=%s}$.\\\\ \n'
                            'Vậy $C$ cách trục nhỏ một khoảng $%s$m.'
                            %(latex(a**2),latex(b**2),latex(d),latex(a**2),latex(d),latex(b**2),latex(d),latex(ctb),latex(d),
                            latex(ctb),)
                        )
            loigiai_vdc_2 = ('Giả sử $C(x_0;y_0)$. Ta có $\\heva{&\\dfrac{x_0^2}{%s}+\\dfrac{y_0^2}{%s}=1\\\\ &|y_0|=%s} \\Rightarrow \\heva{& \\dfrac{x_0^2}{%s}+\\dfrac{%s^2}{%s}=1\\\\ & |y_0|=%s }\\Rightarrow \\heva{&|x_0|=%s\\\\& |y_0|=%s}$.\\\\ \n'
                            'Vậy $C$ cách trục nhỏ một khoảng $%s$m.'
                            %(latex(a**2),latex(b**2),latex(d),latex(a**2),latex(d),latex(b**2),latex(d),latex(ctb),latex(d),
                            latex(ctb),)
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('- +','-').replace('+ -', '-').replace('- -', '+')
            return content   

