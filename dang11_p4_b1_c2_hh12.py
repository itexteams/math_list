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


def bt_dang11_p4_b1_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                z1=randint(2,5)
                y1=randint(1,6)
                x1=randint(1,7)
                h1=randint(1,5)
                h=h1*10
                z2=nsimplify(h1/10)
                y2=randint(1,6)
                x2=randint(1,5)
                while x1-x2==0 or y1-y2==0:
                    z1=randint(2,5)
                    y1=randint(1,6)
                    x1=randint(1,7)
                    h1=randint(1,5)
                    h=h1*10
                    z2=nsimplify(h1/10)
                    y2=randint(1,6)
                    x2=randint(1,5)
                x3=nsimplify(x2+((x1-x2)*z2)/(z1+z2))
                y3=nsimplify(y2+((y1-y2)*z2)/(z1+z2))






                # Nội dung câu hỏi
                noidungcauhoi =  ('\\immini{'
                                    'Với hệ trục tọa độ $Oxyz$ sao cho $O$ nằm trên mặt nước, mặt phẳng $(Oxy)$ là mặt nước, trục $Oz$ hướng lên trên (đơn vị đo: mét), một con chim bói cá đang ở vị trí '
                                    'cách mặt nước $%s$m, cách mặt phẳng $(Oxz), (Oyz)$ lần lượt là $%s$m và $%s$m phóng thẳng xuống vị trí con cá, biết con cá cách mặt nước $%s$cm, cách mặt phẳng $(Oxz), (Oyz)$ lần lượt là $%s$m và $%s$m. Tìm tọa độ điểm $B$ lúc chim bói cá vừa tiếp xúc với mặt nước.'
                                '}{'
                        '\\scalebox{0.6}{ '
                        '\\definecolor{qqffff}{rgb}{0.,1.,1.}\n'
                        '\\definecolor{ffqqqq}{rgb}{1.,0.,0.}\n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                    '\\clip(-3.8061494221595087,-3.190085788516386) rectangle (7.038644215693838,5.018129579583585);\n'
                    '\\draw [->,line width=1.pt] (0.,0.) -- (6.,0.);\n'
                    '\\draw [->,line width=1.pt] (0.,0.) -- (0.,4.);\n'
                    '\\draw [->,line width=1.pt] (0.,0.) -- (-3.,-2.);\n'
                    '\\draw [line width=1.pt] (1.,-1.)-- (3.,2.);\n'
                    '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,-1.)-- (0.3349996723485401,-2.020049504363662);\n'
                    '\\draw [line width=1.pt] (2.2369775162661636,2.0127378334441315)-- (2.6686827670892934,2.3005413339928844);\n'
                    '\\draw [shift={(2.7744319472096115,1.8761827067841346)},line width=1.pt]  plot[domain=0.9833168057371772:1.8150197110908495,variable=\\t]({1.*0.43733640779451943*cos(\\t r)+0.*0.43733640779451943*sin(\\t r)},{0.*0.43733640779451943*cos(\\t r)+1.*0.43733640779451943*sin(\\t r)});\n'
                    '\\draw [shift={(3.3796845636588397,2.9253938148476766)},line width=1.pt]  plot[domain=4.225375398135158:5.2244012606729475,variable=\\t]({1.*0.7753442328274344*cos(\\t r)+0.*0.7753442328274344*sin(\\t r)},{0.*0.7753442328274344*cos(\\t r)+1.*0.7753442328274344*sin(\\t r)});\n'
                    '\\draw [shift={(2.67171791566828,3.0113017159312157)},line width=1.pt]  plot[domain=4.935876582262372:5.622359813554018,variable=\\t]({1.*0.7193667485807793*cos(\\t r)+0.*0.7193667485807793*sin(\\t r)},{0.*0.7193667485807793*cos(\\t r)+1.*0.7193667485807793*sin(\\t r)});\n'
                    '\\draw [line width=1.pt] (2.2369775162661636,2.0127378334441315)-- (2.6036948798686073,2.342319261491897);\n'
                    '\\draw [shift={(2.83467439445201,2.4135003203862437)},line width=1.pt]  plot[domain=2.1105439676999125:3.440528307784841,variable=\\t]({1.*0.24169873665889274*cos(\\t r)+0.*0.24169873665889274*sin(\\t r)},{0.*0.24169873665889274*cos(\\t r)+1.*0.24169873665889274*sin(\\t r)});\n'
                    '\\draw [shift={(3.087782039788708,2.1830835378279407)},line width=1.pt]  plot[domain=1.22912185447372:2.2821848631529544,variable=\\t]({1.*0.5779282377380419*cos(\\t r)+0.*0.5779282377380419*sin(\\t r)},{0.*0.5779282377380419*cos(\\t r)+1.*0.5779282377380419*sin(\\t r)});\n'
                    '\\draw [shift={(3.5129618390429576,1.9796658304595889)},line width=1.pt]  plot[domain=0.683085600269301:1.5240176217437904,variable=\\t]({1.*0.7069341672498356*cos(\\t r)+0.*0.7069341672498356*sin(\\t r)},{0.*0.7069341672498356*cos(\\t r)+1.*0.7069341672498356*sin(\\t r)});\n'
                    '\\draw [shift={(3.8576964717574844,2.4278547466182885)},line width=1.pt]  plot[domain=4.209377193467227:6.27346170946145,variable=\\t]({1.*0.20359350327155848*cos(\\t r)+0.*0.20359350327155848*sin(\\t r)},{0.*0.20359350327155848*cos(\\t r)+1.*0.20359350327155848*sin(\\t r)});\n'
                    '\\draw [shift={(4.584082525315954,-0.7832645609773279)},line width=1.pt]  plot[domain=1.4930879130337666:1.7322880307478843,variable=\\t]({1.*3.251445768208692*cos(\\t r)+0.*3.251445768208692*sin(\\t r)},{0.*3.251445768208692*cos(\\t r)+1.*3.251445768208692*sin(\\t r)});\n'
                    '\\draw [shift={(4.331631857806438,2.3564638064523256)},line width=1.pt]  plot[domain=3.326466390847806:4.36875861400753,variable=\\t]({1.*0.5819985484612398*cos(\\t r)+0.*0.5819985484612398*sin(\\t r)},{0.*0.5819985484612398*cos(\\t r)+1.*0.5819985484612398*sin(\\t r)});\n'
                    '\\draw [shift={(3.9158431720106703,2.3283932856588923)},line width=1.pt]  plot[domain=-2.6740231383929136:0.5904914269624169,variable=\\t]({1.*0.17508478002678138*cos(\\t r)+0.*0.17508478002678138*sin(\\t r)},{0.*0.17508478002678138*cos(\\t r)+1.*0.17508478002678138*sin(\\t r)});\n'
                    '\\draw [shift={(4.429809196450003,2.470404999036663)},line width=1.pt]  plot[domain=3.7268473227490304:4.832950931139623,variable=\\t]({1.*0.5638841065235283*cos(\\t r)+0.*0.5638841065235283*sin(\\t r)},{0.*0.5638841065235283*cos(\\t r)+1.*0.5638841065235283*sin(\\t r)});\n'
                    '\\draw [shift={(4.565658249487715,2.9937336706681523)},line width=1.pt]  plot[domain=4.1281806838802275:4.8773175851407276,variable=\\t]({1.*0.9144915516712032*cos(\\t r)+0.*0.9144915516712032*sin(\\t r)},{0.*0.9144915516712032*cos(\\t r)+1.*0.9144915516712032*sin(\\t r)});\n'
                    '\\draw [shift={(4.560249956905031,2.3460651374853465)},line width=1.pt]  plot[domain=-1.0220283748968377:0.38613179219425264,variable=\\t]({1.*0.2981985793179025*cos(\\t r)+0.*0.2981985793179025*sin(\\t r)},{0.*0.2981985793179025*cos(\\t r)+1.*0.2981985793179025*sin(\\t r)});\n'
                    '\\draw [shift={(4.5229302541652325,2.102103495509938)},line width=1.pt]  plot[domain=4.5810140182669965:6.229047628920983,variable=\\t]({1.*0.19315394756210627*cos(\\t r)+0.*0.19315394756210627*sin(\\t r)},{0.*0.19315394756210627*cos(\\t r)+1.*0.19315394756210627*sin(\\t r)});\n'
                    '\\draw [shift={(4.232270566812936,2.1585024883803805)},line width=1.pt]  plot[domain=4.442788169668575:5.531809474062147,variable=\\t]({1.*0.36312952071187793*cos(\\t r)+0.*0.36312952071187793*sin(\\t r)},{0.*0.36312952071187793*cos(\\t r)+1.*0.36312952071187793*sin(\\t r)});\n'
                    '\\draw [shift={(2.9885876925113406,3.3721566302873955)},line width=1.pt]  plot[domain=-1.1443491021056786:0.21238099541087593,variable=\\t]({1.*0.7079558105969419*cos(\\t r)+0.*0.7079558105969419*sin(\\t r)},{0.*0.7079558105969419*cos(\\t r)+1.*0.7079558105969419*sin(\\t r)});\n'
                    '\\draw [shift={(3.0462028884373447,3.798903138752004)},line width=1.pt]  plot[domain=-0.41234825291832244:0.9258955729604488,variable=\\t]({1.*0.6924758866715544*cos(\\t r)+0.*0.6924758866715544*sin(\\t r)},{0.*0.6924758866715544*cos(\\t r)+1.*0.6924758866715544*sin(\\t r)});\n'
                    '\\draw [shift={(3.1803462813768095,2.9248013412307126)},line width=1.pt]  plot[domain=-0.453481106084233:0.872962329472444,variable=\\t]({1.*0.7785904783413403*cos(\\t r)+0.*0.7785904783413403*sin(\\t r)},{0.*0.7785904783413403*cos(\\t r)+1.*0.7785904783413403*sin(\\t r)});\n'
                    '\\draw [shift={(3.276297235566787,3.4774361491435055)},line width=1.pt]  plot[domain=-0.32986721038033373:0.7821069952994816,variable=\\t]({1.*0.6353827672449396*cos(\\t r)+0.*0.6353827672449396*sin(\\t r)},{0.*0.6353827672449396*cos(\\t r)+1.*0.6353827672449396*sin(\\t r)});\n'
                    '\\draw [shift={(2.7851617688995605,3.891690468632666)},line width=1.pt]  plot[domain=-0.09560735959193423:0.6986081016843847,variable=\\t]({1.*1.048185234652956*cos(\\t r)+0.*1.048185234652956*sin(\\t r)},{0.*1.048185234652956*cos(\\t r)+1.*1.048185234652956*sin(\\t r)});\n'
                    '\\draw [shift={(2.2862777698808445,3.776718357271352)},line width=1.pt]  plot[domain=-0.36448371601700025:0.5639461853763033,variable=\\t]({1.*1.7541891350474748*cos(\\t r)+0.*1.7541891350474748*sin(\\t r)},{0.*1.7541891350474748*cos(\\t r)+1.*1.7541891350474748*sin(\\t r)});\n'
                    '\\draw [shift={(2.554690482676841,3.936612144518547)},line width=1.pt]  plot[domain=-0.5695346432766266:0.3865606095336108,variable=\\t]({1.*1.6566867407667132*cos(\\t r)+0.*1.6566867407667132*sin(\\t r)},{0.*1.6566867407667132*cos(\\t r)+1.*1.6566867407667132*sin(\\t r)});\n'
                    '\\draw [shift={(3.258000933876638,3.8516357463076947)},line width=1.pt]  plot[domain=-0.9080405340497251:0.24238447063129787,variable=\\t]({1.*1.138282695609434*cos(\\t r)+0.*1.138282695609434*sin(\\t r)},{0.*1.138282695609434*cos(\\t r)+1.*1.138282695609434*sin(\\t r)});\n'
                    '\\draw [shift={(3.7042518957763186,3.62140740327906)},line width=1.pt]  plot[domain=5.079615963082772:6.222958143322791,variable=\\t]({1.*0.8134184802850544*cos(\\t r)+0.*0.8134184802850544*sin(\\t r)},{0.*0.8134184802850544*cos(\\t r)+1.*0.8134184802850544*sin(\\t r)});\n'
                    '\\draw [shift={(3.9409646253658335,3.2276420384548743)},line width=1.pt]  plot[domain=4.703155846730432:5.736500739496487,variable=\\t]({1.*0.48861791888606293*cos(\\t r)+0.*0.48861791888606293*sin(\\t r)},{0.*0.48861791888606293*cos(\\t r)+1.*0.48861791888606293*sin(\\t r)});\n'
                    '\\draw [shift={(3.956734618773825,2.776379145909976)},line width=1.pt]  plot[domain=-1.948711411647741:0.07829017170705069,variable=\\t]({1.*0.20730455112608312*cos(\\t r)+0.*0.20730455112608312*sin(\\t r)},{0.*0.20730455112608312*cos(\\t r)+1.*0.20730455112608312*sin(\\t r)});\n'
                    '\\draw [shift={(3.5388947393411723,4.354054694683316)},line width=1.pt]  plot[domain=0.6447187166086181:3.164523218783006,variable=\\t]({1.*0.07645144838933202*cos(\\t r)+0.*0.07645144838933202*sin(\\t r)},{0.*0.07645144838933202*cos(\\t r)+1.*0.07645144838933202*sin(\\t r)});\n'
                    '\\draw [shift={(3.7039570242338167,4.491015336314938)},line width=1.pt]  plot[domain=2.5693792558959396:3.8607110051871993,variable=\\t]({1.*0.13816965778372434*cos(\\t r)+0.*0.13816965778372434*sin(\\t r)},{0.*0.13816965778372434*cos(\\t r)+1.*0.13816965778372434*sin(\\t r)});\n'
                    '\\draw [shift={(3.568345548943492,4.299082624846891)},line width=1.pt]  plot[domain=0.529891542899658:1.498004579297181,variable=\\t]({1.*0.26745904956798394*cos(\\t r)+0.*0.26745904956798394*sin(\\t r)},{0.*0.26745904956798394*cos(\\t r)+1.*0.26745904956798394*sin(\\t r)});\n'
                    '\\draw [shift={(4.044268365699954,4.602469476202521)},line width=1.pt]  plot[domain=2.7556700762484105:3.7429566703969694,variable=\\t]({1.*0.29729941736747273*cos(\\t r)+0.*0.29729941736747273*sin(\\t r)},{0.*0.29729941736747273*cos(\\t r)+1.*0.29729941736747273*sin(\\t r)});\n'
                    '\\draw [shift={(3.7952193123463225,4.539657755346624)},line width=1.pt]  plot[domain=0.13415526271837647:1.720674347183885,variable=\\t]({1.*0.17670032420416842*cos(\\t r)+0.*0.17670032420416842*sin(\\t r)},{0.*0.17670032420416842*cos(\\t r)+1.*0.17670032420416842*sin(\\t r)});\n'
                    '\\draw [shift={(4.029485341325628,4.548285228949479)},line width=1.pt]  plot[domain=0.21309117085725895:2.8931419737351445,variable=\\t]({1.*0.061027284524720685*cos(\\t r)+0.*0.061027284524720685*sin(\\t r)},{0.*0.061027284524720685*cos(\\t r)+1.*0.061027284524720685*sin(\\t r)});\n'
                    '\\draw [shift={(4.278367835686626,4.12418098565742)},line width=1.pt]  plot[domain=0.0078349868686811:2.8366120897419824,variable=\\t]({1.*0.0846445891110624*cos(\\t r)+0.*0.0846445891110624*sin(\\t r)},{0.*0.0846445891110624*cos(\\t r)+1.*0.0846445891110624*sin(\\t r)});\n'
                    '\\draw [shift={(4.414753518583797,3.557373392493117)},line width=1.pt]  plot[domain=0.14751513806299615:1.9279487042537355,variable=\\t]({1.*0.10255586487592194*cos(\\t r)+0.*0.10255586487592194*sin(\\t r)},{0.*0.10255586487592194*cos(\\t r)+1.*0.10255586487592194*sin(\\t r)});\n'
                    '\\draw [shift={(4.27437216382878,3.1060912389691318)},line width=1.pt]  plot[domain=-1.0056686061365028:0.6419091635826633,variable=\\t]({1.*0.1568477243042297*cos(\\t r)+0.*0.1568477243042297*sin(\\t r)},{0.*0.1568477243042297*cos(\\t r)+1.*0.1568477243042297*sin(\\t r)});\n'
                    '\\draw [shift={(2.7222320204091965,3.7887956340698308)},line width=1.pt]  plot[domain=0.05852581120017343:0.6082495659170867,variable=\\t]({1.*1.0696015159520962*cos(\\t r)+0.*1.0696015159520962*sin(\\t r)},{0.*1.0696015159520962*cos(\\t r)+1.*1.0696015159520962*sin(\\t r)});\n'
                    '\\draw [shift={(2.282293079559452,3.748158732236787)},line width=1.pt]  plot[domain=-0.29030321293530026:0.42478953686598736,variable=\\t]({1.*1.6647900934724795*cos(\\t r)+0.*1.6647900934724795*sin(\\t r)},{0.*1.6647900934724795*cos(\\t r)+1.*1.6647900934724795*sin(\\t r)});\n'
                    '\\draw [shift={(2.607389682669848,3.9001675110001384)},line width=1.pt]  plot[domain=-0.5166873429449987:0.45282088958841205,variable=\\t]({1.*1.5156997179504064*cos(\\t r)+0.*1.5156997179504064*sin(\\t r)},{0.*1.5156997179504064*cos(\\t r)+1.*1.5156997179504064*sin(\\t r)});\n'
                    '\\draw [shift={(2.984718388557175,3.8945952111767643)},line width=1.pt]  plot[domain=-0.7426950109432502:0.23995538359635074,variable=\\t]({1.*1.3170294378190273*cos(\\t r)+0.*1.3170294378190273*sin(\\t r)},{0.*1.3170294378190273*cos(\\t r)+1.*1.3170294378190273*sin(\\t r)});\n'
                    '\\draw [shift={(3.5925864235910243,3.701339672529063)},line width=1.pt]  plot[domain=5.141690736797607:6.217652445092772,variable=\\t]({1.*0.8793340073978424*cos(\\t r)+0.*0.8793340073978424*sin(\\t r)},{0.*0.8793340073978424*cos(\\t r)+1.*0.8793340073978424*sin(\\t r)});\n'
                    '\\draw [shift={(3.8275404742614043,3.5503924116513295)},line width=1.pt]  plot[domain=4.881888028931043:5.6666991708919285,variable=\\t]({1.*0.7387217525674371*cos(\\t r)+0.*0.7387217525674371*sin(\\t r)},{0.*0.7387217525674371*cos(\\t r)+1.*0.7387217525674371*sin(\\t r)});\n'
                    '\\draw [shift={(3.382284498720038,3.6082740684110046)},line width=1.pt]  plot[domain=3.588048295881636:4.598360640790577,variable=\\t]({1.*0.8864260948726851*cos(\\t r)+0.*0.8864260948726851*sin(\\t r)},{0.*0.8864260948726851*cos(\\t r)+1.*0.8864260948726851*sin(\\t r)});\n'
                    '\\draw [shift={(2.729251182569387,3.265598277084533)},line width=1.pt]  plot[domain=1.0862539101069986:3.4084850734309886,variable=\\t]({1.*0.15188554338868543*cos(\\t r)+0.*0.15188554338868543*sin(\\t r)},{0.*0.15188554338868543*cos(\\t r)+1.*0.15188554338868543*sin(\\t r)});\n'
                    '\\draw [shift={(2.989213033553751,3.7947724642874894)},line width=1.pt]  plot[domain=4.265440982768235:4.821257068865862,variable=\\t]({1.*0.43777490863025714*cos(\\t r)+0.*0.43777490863025714*sin(\\t r)},{0.*0.43777490863025714*cos(\\t r)+1.*0.43777490863025714*sin(\\t r)});\n'
                    '\\draw [shift={(3.2969698567901755,2.812906643511953)},line width=1.pt]  plot[domain=0.865038441612789:2.0150158877302817,variable=\\t]({1.*0.6054431363003027*cos(\\t r)+0.*0.6054431363003027*sin(\\t r)},{0.*0.6054431363003027*cos(\\t r)+1.*0.6054431363003027*sin(\\t r)});\n'
                    '\\draw [shift={(3.309597232057085,4.268593801162885)},line width=1.pt]  plot[domain=3.643725379075529:4.10377858472943,variable=\\t]({1.*1.271328683594854*cos(\\t r)+0.*1.271328683594854*sin(\\t r)},{0.*1.271328683594854*cos(\\t r)+1.*1.271328683594854*sin(\\t r)});\n'
                    '\\draw [shift={(3.4311115735194604,4.134692284929772)},line width=1.pt]  plot[domain=3.3135680820013866:3.9033007358029814,variable=\\t]({1.*1.1544068459752244*cos(\\t r)+0.*1.1544068459752244*sin(\\t r)},{0.*1.1544068459752244*cos(\\t r)+1.*1.1544068459752244*sin(\\t r)});\n'
                    '\\draw [shift={(4.047578622780057,4.300299692105459)},line width=1.pt]  plot[domain=3.2023231819249056:3.722965576442845,variable=\\t]({1.*1.6128126994622642*cos(\\t r)+0.*1.6128126994622642*sin(\\t r)},{0.*1.6128126994622642*cos(\\t r)+1.*1.6128126994622642*sin(\\t r)});\n'
                    '\\draw [shift={(4.310045594590383,4.064505308533864)},line width=1.pt]  plot[domain=3.064817299026706:3.5561468237765816,variable=\\t]({1.*1.6497893813488766*cos(\\t r)+0.*1.6497893813488766*sin(\\t r)},{0.*1.6497893813488766*cos(\\t r)+1.*1.6497893813488766*sin(\\t r)});\n'
                    '\\draw [shift={(4.320214350833691,3.789198960880193)},line width=1.pt]  plot[domain=2.9498134896830885:3.4436892493528553,variable=\\t]({1.*1.4439568126815658*cos(\\t r)+0.*1.4439568126815658*sin(\\t r)},{0.*1.4439568126815658*cos(\\t r)+1.*1.4439568126815658*sin(\\t r)});\n'
                    '\\draw [shift={(3.8360557295063544,3.555608662488587)},line width=1.pt]  plot[domain=2.709680081249772:3.3820918097562074,variable=\\t]({1.*0.822962587665556*cos(\\t r)+0.*0.822962587665556*sin(\\t r)},{0.*0.822962587665556*cos(\\t r)+1.*0.822962587665556*sin(\\t r)});\n'
                    '\\draw [shift={(3.5132549243189435,3.5090548233037406)},line width=1.pt]  plot[domain=2.321589901147342:3.4331692734473505,variable=\\t]({1.*0.37516493273615303*cos(\\t r)+0.*0.37516493273615303*sin(\\t r)},{0.*0.37516493273615303*cos(\\t r)+1.*0.37516493273615303*sin(\\t r)});\n'
                    '\\draw [shift={(3.610830819807858,3.436157207259836)},line width=1.pt]  plot[domain=2.214659638167577:3.195727452413375,variable=\\t]({1.*0.33679643047667723*cos(\\t r)+0.*0.33679643047667723*sin(\\t r)},{0.*0.33679643047667723*cos(\\t r)+1.*0.33679643047667723*sin(\\t r)});\n'
                    '\\draw [shift={(3.596338906192932,3.435000195349916)},line width=1.pt]  plot[domain=1.5486114934725446:3.339710506473977,variable=\\t]({1.*0.16504041669370084*cos(\\t r)+0.*0.16504041669370084*sin(\\t r)},{0.*0.16504041669370084*cos(\\t r)+1.*0.16504041669370084*sin(\\t r)});\n'
                    '\\draw [shift={(3.707501922321099,3.329927732088821)},line width=1.pt]  plot[domain=1.9710762445107193:2.914433365291615,variable=\\t]({1.*0.17812946899023888*cos(\\t r)+0.*0.17812946899023888*sin(\\t r)},{0.*0.17812946899023888*cos(\\t r)+1.*0.17812946899023888*sin(\\t r)});\n'
                    '\\draw [shift={(2.236628858691885,3.6816064240560715)},line width=1.pt]  plot[domain=0.25979533011387707:3.682777004741871,variable=\\t]({1.*0.04833170205054342*cos(\\t r)+0.*0.04833170205054342*sin(\\t r)},{0.*0.04833170205054342*cos(\\t r)+1.*0.04833170205054342*sin(\\t r)});\n'
                    '\\draw [shift={(2.525114554715511,3.8054654019570258)},line width=1.pt]  plot[domain=2.6242179098678644:3.573504298004649,variable=\\t]({1.*0.2662239801615606*cos(\\t r)+0.*0.2662239801615606*sin(\\t r)},{0.*0.2662239801615606*cos(\\t r)+1.*0.2662239801615606*sin(\\t r)});\n'
                    '\\draw [shift={(2.3109798608324654,3.841437673548228)},line width=1.pt]  plot[domain=0.061251985307523314:1.7490883409110725,variable=\\t]({1.*0.09724365988412792*cos(\\t r)+0.*0.09724365988412792*sin(\\t r)},{0.*0.09724365988412792*cos(\\t r)+1.*0.09724365988412792*sin(\\t r)});\n'
                    '\\draw [shift={(2.719817453474918,3.9822349819949907)},line width=1.pt]  plot[domain=2.4788206303805453:3.314406281404417,variable=\\t]({1.*0.35783581302261264*cos(\\t r)+0.*0.35783581302261264*sin(\\t r)},{0.*0.35783581302261264*cos(\\t r)+1.*0.35783581302261264*sin(\\t r)});\n'
                    '\\draw [shift={(2.391290052324773,4.043619383417844)},line width=1.pt]  plot[domain=0.020222169441366518:1.2862225982988025,variable=\\t]({1.*0.16544760685484555*cos(\\t r)+0.*0.16544760685484555*sin(\\t r)},{0.*0.16544760685484555*cos(\\t r)+1.*0.16544760685484555*sin(\\t r)});\n'
                    '\\draw [shift={(2.6849974916169344,4.063257375377653)},line width=1.pt]  plot[domain=1.7251413144377372:3.267910374856852,variable=\\t]({1.*0.12932404688359386*cos(\\t r)+0.*0.12932404688359386*sin(\\t r)},{0.*0.12932404688359386*cos(\\t r)+1.*0.12932404688359386*sin(\\t r)});\n'
                    '\\draw [shift={(2.6682603789157966,4.074745158527126)},line width=1.pt]  plot[domain=-0.2591787343880103:1.5978256685045296,variable=\\t]({1.*0.11634141240364815*cos(\\t r)+0.*0.11634141240364815*sin(\\t r)},{0.*0.11634141240364815*cos(\\t r)+1.*0.11634141240364815*sin(\\t r)});\n'
                    '\\draw [shift={(2.849950356109876,4.003189925247187)},line width=1.pt]  plot[domain=0.8594262162669916:2.599074045478431,variable=\\t]({1.*0.08084234360485305*cos(\\t r)+0.*0.08084234360485305*sin(\\t r)},{0.*0.08084234360485305*cos(\\t r)+1.*0.08084234360485305*sin(\\t r)});\n'
                    '\\draw [shift={(2.759113281685979,3.907466328843323)},line width=1.pt]  plot[domain=-0.33655937397561786:0.829758160450246,variable=\\t]({1.*0.21274853595644347*cos(\\t r)+0.*0.21274853595644347*sin(\\t r)},{0.*0.21274853595644347*cos(\\t r)+1.*0.21274853595644347*sin(\\t r)});\n'
                    '\\draw [shift={(3.0583710165363938,3.7989159638013446)},line width=1.pt]  plot[domain=1.2798847813296592:2.7706329179938316,variable=\\t]({1.*0.1056301140702481*cos(\\t r)+0.*0.1056301140702481*sin(\\t r)},{0.*0.1056301140702481*cos(\\t r)+1.*0.1056301140702481*sin(\\t r)});\n'
                    '\\draw [shift={(2.9927421837002757,3.7928514036189123)},line width=1.pt]  plot[domain=-0.473471899452937:0.8411038067957285,variable=\\t]({1.*0.14389503157621572*cos(\\t r)+0.*0.14389503157621572*sin(\\t r)},{0.*0.14389503157621572*cos(\\t r)+1.*0.14389503157621572*sin(\\t r)});\n'
                    '\\draw [shift={(3.232694161834193,3.649156402602717)},line width=1.pt]  plot[domain=1.3893841267037847:2.5323007956513006,variable=\\t]({1.*0.13643837038307602*cos(\\t r)+0.*0.13643837038307602*sin(\\t r)},{0.*0.13643837038307602*cos(\\t r)+1.*0.13643837038307602*sin(\\t r)});\n'
                    '\\draw [shift={(3.20573404397613,3.712289439525548)},line width=1.pt]  plot[domain=-0.7585365971052616:0.9429990294424664,variable=\\t]({1.*0.08780961575219914*cos(\\t r)+0.*0.08780961575219914*sin(\\t r)},{0.*0.08780961575219914*cos(\\t r)+1.*0.08780961575219914*sin(\\t r)});\n'
                    '\\draw [shift={(3.4238092581475623,3.4587731898780087)},line width=1.pt]  plot[domain=1.6321336754750588:2.2450532330062574,variable=\\t]({1.*0.24721284596636464*cos(\\t r)+0.*0.24721284596636464*sin(\\t r)},{0.*0.24721284596636464*cos(\\t r)+1.*0.24721284596636464*sin(\\t r)});\n'
                    '\\draw [shift={(3.388858218534611,3.6433404314716937)},line width=1.pt]  plot[domain=-0.4110038839257921:1.2625625544486287,variable=\\t]({1.*0.06525617501035724*cos(\\t r)+0.*0.06525617501035724*sin(\\t r)},{0.*0.06525617501035724*cos(\\t r)+1.*0.06525617501035724*sin(\\t r)});\n'
                    '\\draw [shift={(3.5161381222223205,3.536764201479325)},line width=1.pt]  plot[domain=0.6460861702835697:2.26824974369592,variable=\\t]({1.*0.10503133227254616*cos(\\t r)+0.*0.10503133227254616*sin(\\t r)},{0.*0.10503133227254616*cos(\\t r)+1.*0.10503133227254616*sin(\\t r)});\n'
                    '\\draw [shift={(3.512917755802809,3.5816673139304083)},line width=1.pt]  plot[domain=-0.9489412642556729:0.2074916303955437,variable=\\t]({1.*0.08899103681239709*cos(\\t r)+0.*0.08899103681239709*sin(\\t r)},{0.*0.08899103681239709*cos(\\t r)+1.*0.08899103681239709*sin(\\t r)});\n'
                    '\\draw [shift={(3.593671345479584,3.464641571110086)},line width=1.pt]  plot[domain=0.5836727013575925:2.144987867422474,variable=\\t]({1.*0.05323036213448792*cos(\\t r)+0.*0.05323036213448792*sin(\\t r)},{0.*0.05323036213448792*cos(\\t r)+1.*0.05323036213448792*sin(\\t r)});\n'
                    '\\draw [shift={(3.9393034373639595,4.587035267688649)},line width=1.pt]  plot[domain=3.6361610895286214:3.904169321570757,variable=\\t]({1.*1.8814069170601395*cos(\\t r)+0.*1.8814069170601395*sin(\\t r)},{0.*1.8814069170601395*cos(\\t r)+1.*1.8814069170601395*sin(\\t r)});\n'
                    '\\draw [shift={(3.4508169272396287,4.1059604584075515)},line width=1.pt]  plot[domain=3.3846535244784772:3.866948514984606,variable=\\t]({1.*1.0743555383533774*cos(\\t r)+0.*1.0743555383533774*sin(\\t r)},{0.*1.0743555383533774*cos(\\t r)+1.*1.0743555383533774*sin(\\t r)});\n'
                    '\\draw [shift={(4.877576542451782,4.393078148573635)},line width=1.pt]  plot[domain=3.289632284586858:3.570695933818807,variable=\\t]({1.*2.3465388437406194*cos(\\t r)+0.*2.3465388437406194*sin(\\t r)},{0.*2.3465388437406194*cos(\\t r)+1.*2.3465388437406194*sin(\\t r)});\n'
                    '\\draw [shift={(3.9849575827548778,3.859005723781642)},line width=1.pt]  plot[domain=2.9884122426109667:3.5505904590580784,variable=\\t]({1.*1.218509268084527*cos(\\t r)+0.*1.218509268084527*sin(\\t r)},{0.*1.218509268084527*cos(\\t r)+1.*1.218509268084527*sin(\\t r)});\n'
                    '\\draw [shift={(3.865352435531914,3.6711196234838237)},line width=1.pt]  plot[domain=2.960173026655225:3.4785421597298263,variable=\\t]({1.*0.9205338568221048*cos(\\t r)+0.*0.9205338568221048*sin(\\t r)},{0.*0.9205338568221048*cos(\\t r)+1.*0.9205338568221048*sin(\\t r)});\n'
                    '\\draw [shift={(3.585386975922342,3.509138752000421)},line width=1.pt]  plot[domain=2.702677657986858:3.393391830357546,variable=\\t]({1.*0.5132266472148284*cos(\\t r)+0.*0.5132266472148284*sin(\\t r)},{0.*0.5132266472148284*cos(\\t r)+1.*0.5132266472148284*sin(\\t r)});\n'
                    '\\draw [shift={(3.639598574435278,3.411585068530775)},line width=1.pt]  plot[domain=2.565749184587302:3.1446033259108876,variable=\\t]({1.*0.44129463055594154*cos(\\t r)+0.*0.44129463055594154*sin(\\t r)},{0.*0.44129463055594154*cos(\\t r)+1.*0.44129463055594154*sin(\\t r)});\n'
                    '\\draw [shift={(3.624413532205944,3.4096032194777237)},line width=1.pt]  plot[domain=2.2731002938718725:3.1188001089976423,variable=\\t]({1.*0.2720427315568967*cos(\\t r)+0.*0.2720427315568967*sin(\\t r)},{0.*0.2720427315568967*cos(\\t r)+1.*0.2720427315568967*sin(\\t r)});\n'
                    '\\draw [shift={(3.6144476106524093,3.3879507386411905)},line width=1.pt]  plot[domain=1.9593357322653537:3.1338412830163738,variable=\\t]({1.*0.1311610325310385*cos(\\t r)+0.*0.1311610325310385*sin(\\t r)},{0.*0.1311610325310385*cos(\\t r)+1.*0.1311610325310385*sin(\\t r)});\n'
                    '\\draw [shift={(3.5232278097992697,3.2789142329296266)},line width=1.pt]  plot[domain=-0.031188031755802648:1.3041869900061174,variable=\\t]({1.*0.16652001867168958*cos(\\t r)+0.*0.16652001867168958*sin(\\t r)},{0.*0.16652001867168958*cos(\\t r)+1.*0.16652001867168958*sin(\\t r)});\n'
                    '\\draw [line width=1.pt] (2.7406238806506913,2.4299645487358803) circle (0.05122642160706963cm);\n'
                    '\\draw [shift={(2.968562207488225,2.188669190416078)},line width=1.pt]  plot[domain=1.511710873294993:2.7430196387398578,variable=\\t]({1.*0.39589962251293664*cos(\\t r)+0.*0.39589962251293664*sin(\\t r)},{0.*0.39589962251293664*cos(\\t r)+1.*0.39589962251293664*sin(\\t r)});\n'
                    '\\draw [shift={(2.889000813866025,3.1546074326549225)},line width=1.pt]  plot[domain=4.890835562781653:5.455614482447706,variable=\\t]({1.*0.5799385479313439*cos(\\t r)+0.*0.5799385479313439*sin(\\t r)},{0.*0.5799385479313439*cos(\\t r)+1.*0.5799385479313439*sin(\\t r)});\n'
                    '\\draw [shift={(2.4811768136069126,3.0553594465859857)},line width=1.pt]  plot[domain=4.955872593187596:5.518636391530917,variable=\\t]({1.*0.7777588737455513*cos(\\t r)+0.*0.7777588737455513*sin(\\t r)},{0.*0.7777588737455513*cos(\\t r)+1.*0.7777588737455513*sin(\\t r)});\n'
                    '\\draw [shift={(2.6043327169953328,4.547991805168573)},line width=1.pt]  plot[domain=4.924862597943186:5.02313994766684,variable=\\t]({1.*2.0777294258473633*cos(\\t r)+0.*2.0777294258473633*sin(\\t r)},{0.*2.0777294258473633*cos(\\t r)+1.*2.0777294258473633*sin(\\t r)});\n'
                    '\\draw [shift={(3.238848804018088,3.147802761563134)},line width=1.pt]  plot[domain=-1.2743903506007843:0.2723705904652487,variable=\\t]({1.*0.468073150323666*cos(\\t r)+0.*0.468073150323666*sin(\\t r)},{0.*0.468073150323666*cos(\\t r)+1.*0.468073150323666*sin(\\t r)});\n'
                    '\\draw [shift={(0.14047921405243602,-3.784491722320432)},line width=1.pt]  plot[domain=1.0585772481313829:2.0619635513949595,variable=\\t]({1.*1.574902674290679*cos(\\t r)+0.*1.574902674290679*sin(\\t r)},{0.*1.574902674290679*cos(\\t r)+1.*1.574902674290679*sin(\\t r)});\n'
                    '\\draw [shift={(-0.09976439796373848,-2.046274264313491)},line width=1.pt]  plot[domain=3.749237438436322:4.755517857093409,variable=\\t]({1.*0.6121448157987234*cos(\\t r)+0.*0.6121448157987234*sin(\\t r)},{0.*0.6121448157987234*cos(\\t r)+1.*0.6121448157987234*sin(\\t r)});\n'
                    '\\draw [shift={(0.1369037681699048,-0.7734143103341096)},line width=1.pt]  plot[domain=4.601263415461584:5.089968048588553,variable=\\t]({1.*1.896131047731787*cos(\\t r)+0.*1.896131047731787*sin(\\t r)},{0.*1.896131047731787*cos(\\t r)+1.*1.896131047731787*sin(\\t r)});\n'
                    '\\draw [shift={(1.3969808654997784,-2.735035313913904)},line width=1.pt]  plot[domain=1.7264815219769407:2.8006468024070963,variable=\\t]({1.*0.5952941166607018*cos(\\t r)+0.*0.5952941166607018*sin(\\t r)},{0.*0.5952941166607018*cos(\\t r)+1.*0.5952941166607018*sin(\\t r)});\n'
                    '\\draw [shift={(1.4892707555757307,-2.0116559163038192)},line width=1.pt]  plot[domain=3.8178914348674446:4.47871908380262,variable=\\t]({1.*0.8377005022146958*cos(\\t r)+0.*0.8377005022146958*sin(\\t r)},{0.*0.8377005022146958*cos(\\t r)+1.*0.8377005022146958*sin(\\t r)});\n'
                    '\\draw [shift={(1.024037913379634,-2.255283681993995)},line width=1.pt]  plot[domain=-0.7745204001983108:0.3684299656913801,variable=\\t]({1.*0.30082562735741214*cos(\\t r)+0.*0.30082562735741214*sin(\\t r)},{0.*0.30082562735741214*cos(\\t r)+1.*0.30082562735741214*sin(\\t r)});\n'
                    '\\draw [shift={(0.5909892878576943,-2.751511874280071)},line width=1.pt]  plot[domain=-0.10619725422767257:0.4153983450900745,variable=\\t]({1.*0.7083028739339026*cos(\\t r)+0.*0.7083028739339026*sin(\\t r)},{0.*0.7083028739339026*cos(\\t r)+1.*0.7083028739339026*sin(\\t r)});\n'
                    '\\draw [shift={(-0.3342819546720046,-2.4401627418378182)},line width=1.pt]  plot[domain=-2.0921424182724984:1.6540278431883009,variable=\\t]({1.*0.15374144997552536*cos(\\t r)+0.*0.15374144997552536*sin(\\t r)},{0.*0.15374144997552536*cos(\\t r)+1.*0.15374144997552536*sin(\\t r)});\n'
                    '\\draw [shift={(0.006938878315867114,-2.765149438311124)},line width=1.pt]  plot[domain=2.2133164049966862:4.025431771529465,variable=\\t]({1.*0.13402594589831457*cos(\\t r)+0.*0.13402594589831457*sin(\\t r)},{0.*0.13402594589831457*cos(\\t r)+1.*0.13402594589831457*sin(\\t r)});\n'
                    '\\draw [shift={(-0.13971612581434004,-2.8814194916305147)},line width=1.pt]  plot[domain=0.15533767146089186:1.2823223277823514,variable=\\t]({1.*0.23320592177052343*cos(\\t r)+0.*0.23320592177052343*sin(\\t r)},{0.*0.23320592177052343*cos(\\t r)+1.*0.23320592177052343*sin(\\t r)});\n'
                    '\\draw [shift={(-0.09863995787804523,-2.101406420071274)},line width=1.pt]  plot[domain=4.739203096111904:4.961586911972514,variable=\\t]({1.*0.7676450547528741*cos(\\t r)+0.*0.7676450547528741*sin(\\t r)},{0.*0.7676450547528741*cos(\\t r)+1.*0.7676450547528741*sin(\\t r)});\n'
                    '\\draw [shift={(0.5366889326766869,-2.6707025183060766)},line width=1.pt]  plot[domain=2.9552550009742427:4.483006624515626,variable=\\t]({1.*0.1199773641524334*cos(\\t r)+0.*0.1199773641524334*sin(\\t r)},{0.*0.1199773641524334*cos(\\t r)+1.*0.1199773641524334*sin(\\t r)});\n'
                    '\\draw [shift={(0.7001064039528003,-2.737863856739453)},line width=1.pt]  plot[domain=2.7619345367890964:3.3964131503985717,variable=\\t]({1.*0.19706083484669762*cos(\\t r)+0.*0.19706083484669762*sin(\\t r)},{0.*0.19706083484669762*cos(\\t r)+1.*0.19706083484669762*sin(\\t r)});\n'
                    '\\draw [shift={(0.5014592864694217,-2.4551971807150723)},line width=1.pt]  plot[domain=4.308208498544725:4.7867557655106925,variable=\\t]({1.*0.21021637316222552*cos(\\t r)+0.*0.21021637316222552*sin(\\t r)},{0.*0.21021637316222552*cos(\\t r)+1.*0.21021637316222552*sin(\\t r)});\n'
                    '\\draw [shift={(0.3237729443936342,-2.2854966257646505)},line width=1.pt]  plot[domain=2.3115054583632646:2.931391874733615,variable=\\t]({1.*0.33291987616369506*cos(\\t r)+0.*0.33291987616369506*sin(\\t r)},{0.*0.33291987616369506*cos(\\t r)+1.*0.33291987616369506*sin(\\t r)});\n'
                    '\\draw [shift={(5.771085343798003,9.021339856817654)},line width=1.pt]  plot[domain=4.238567096893147:4.280906686110154,variable=\\t]({1.*12.430614449301062*cos(\\t r)+0.*12.430614449301062*sin(\\t r)},{0.*12.430614449301062*cos(\\t r)+1.*12.430614449301062*sin(\\t r)});\n'
                    '\\draw [shift={(-0.4678871324947543,-2.1959483547826664)},line width=1.pt]  plot[domain=4.120133412199771:4.582544747405041,variable=\\t]({1.*0.24084007075611924*cos(\\t r)+0.*0.24084007075611924*sin(\\t r)},{0.*0.24084007075611924*cos(\\t r)+1.*0.24084007075611924*sin(\\t r)});\n'
                    '\\draw [line width=1.pt] (-0.3430512574680169,-2.3684127538495976) circle (0.042095441474894274cm);\n'
                    '\\draw [line width=1.pt] (-0.3430512574680169,-2.3684127538495976) circle (0.029685191456151637cm);\n'
                    '\\draw [shift={(1.1841073022491329,-0.48330921312444697)},line width=1.pt]  plot[domain=4.557614595880568:4.740100153259883,variable=\\t]({1.*1.9831252795095862*cos(\\t r)+0.*1.9831252795095862*sin(\\t r)},{0.*1.9831252795095862*cos(\\t r)+1.*1.9831252795095862*sin(\\t r)});\n'
                    '\\draw [shift={(1.1798800555069817,-2.027679160741207)},line width=1.pt]  plot[domain=4.084173761036954:4.8789483359361,variable=\\t]({1.*0.5129911642564668*cos(\\t r)+0.*0.5129911642564668*sin(\\t r)},{0.*0.5129911642564668*cos(\\t r)+1.*0.5129911642564668*sin(\\t r)});\n'
                    '\\draw [shift={(1.3149432472302658,-1.9201486907231966)},line width=1.pt]  plot[domain=4.028517773893087:4.678448665160368,variable=\\t]({1.*0.7204875015110846*cos(\\t r)+0.*0.7204875015110846*sin(\\t r)},{0.*0.7204875015110846*cos(\\t r)+1.*0.7204875015110846*sin(\\t r)});\n'
                    '\\draw [shift={(1.3639328040120728,-2.811406091656812)},line width=1.pt]  plot[domain=1.641361752428561:2.4170650986938003,variable=\\t]({1.*0.6030530433825446*cos(\\t r)+0.*0.6030530433825446*sin(\\t r)},{0.*0.6030530433825446*cos(\\t r)+1.*0.6030530433825446*sin(\\t r)});\n'
                    '\\draw [shift={(1.344338404688765,-3.028681982582927)},line width=1.pt]  plot[domain=1.5994476246827993:2.194316267469439,variable=\\t]({1.*0.7412177584602251*cos(\\t r)+0.*0.7412177584602251*sin(\\t r)},{0.*0.7412177584602251*cos(\\t r)+1.*0.7412177584602251*sin(\\t r)});\n'
                    '\\draw [shift={(1.3036422959437286,-3.47824203984787)},line width=1.pt]  plot[domain=1.5712470824485323:1.9097873744471063,variable=\\t]({1.*1.1107213453375828*cos(\\t r)+0.*1.1107213453375828*sin(\\t r)},{0.*1.1107213453375828*cos(\\t r)+1.*1.1107213453375828*sin(\\t r)});\n'
                    '\\draw [shift={(1.4332568463025692,-7.533829086131709)},line width=1.pt]  plot[domain=1.6013407077987116:1.6626775902550677,variable=\\t]({1.*5.118052922132519*cos(\\t r)+0.*5.118052922132519*sin(\\t r)},{0.*5.118052922132519*cos(\\t r)+1.*5.118052922132519*sin(\\t r)});\n'
                    '\\draw [shift={(1.2092324953083609,-2.0168823902997373)},line width=1.pt]  plot[domain=4.15065200540739:4.832754264088777,variable=\\t]({1.*0.5606535984180864*cos(\\t r)+0.*0.5606535984180864*sin(\\t r)},{0.*0.5606535984180864*cos(\\t r)+1.*0.5606535984180864*sin(\\t r)});\n'
                    '\\draw [shift={(1.430270065322212,-1.9072945310312273)},line width=1.pt]  plot[domain=3.9894497760223815:4.555007125697114,variable=\\t]({1.*0.8370561065266718*cos(\\t r)+0.*0.8370561065266718*sin(\\t r)},{0.*0.8370561065266718*cos(\\t r)+1.*0.8370561065266718*sin(\\t r)});\n'
                    '\\draw [shift={(-0.301718345938588,-2.447412370770491)},line width=1.pt]  plot[domain=-2.284324903482838:1.84621032839864,variable=\\t]({1.*0.16674295828193045*cos(\\t r)+0.*0.16674295828193045*sin(\\t r)},{0.*0.16674295828193045*cos(\\t r)+1.*0.16674295828193045*sin(\\t r)});\n'
                    '\\draw [shift={(0.34446411872555155,-2.2472216706326367)},line width=1.pt]  plot[domain=2.408341206651285:2.947379856752916,variable=\\t]({1.*0.283308079128508*cos(\\t r)+0.*0.283308079128508*sin(\\t r)},{0.*0.283308079128508*cos(\\t r)+1.*0.283308079128508*sin(\\t r)});\n'
                    '\\draw [shift={(0.32058845840175537,-2.2392265464130676)},line width=1.pt]  plot[domain=2.3302908715327932:2.93869742686212,variable=\\t]({1.*0.21276053200436484*cos(\\t r)+0.*0.21276053200436484*sin(\\t r)},{0.*0.21276053200436484*cos(\\t r)+1.*0.21276053200436484*sin(\\t r)});\n'
                    '\\draw [shift={(0.30693875637679857,-2.2241246983685827)},line width=1.pt]  plot[domain=2.1884658120784537:2.9573707074269415,variable=\\t]({1.*0.15160181157461833*cos(\\t r)+0.*0.15160181157461833*sin(\\t r)},{0.*0.15160181157461833*cos(\\t r)+1.*0.15160181157461833*sin(\\t r)});\n'
                    '\\draw [shift={(0.3380476800879533,-2.2348560403314117)},line width=1.pt]  plot[domain=2.218939429643336:2.8824097831715667,variable=\\t]({1.*0.13908086763895344*cos(\\t r)+0.*0.13908086763895344*sin(\\t r)},{0.*0.13908086763895344*cos(\\t r)+1.*0.13908086763895344*sin(\\t r)});\n'
                    '\\draw [shift={(0.35002297728802423,-2.212017756645346)},line width=1.pt]  plot[domain=2.203711685363977:3.0144654252119083,variable=\\t]({1.*0.07847919001835474*cos(\\t r)+0.*0.07847919001835474*sin(\\t r)},{0.*0.07847919001835474*cos(\\t r)+1.*0.07847919001835474*sin(\\t r)});\n'
                    '\\draw [shift={(0.3578906058004947,-2.207447056591407)},line width=1.pt]  plot[domain=2.1372482105251:3.1829313883737793,variable=\\t]({1.*0.04662761218009192*cos(\\t r)+0.*0.04662761218009192*sin(\\t r)},{0.*0.04662761218009192*cos(\\t r)+1.*0.04662761218009192*sin(\\t r)});\n'
                    '\\draw [shift={(0.38134312559031514,-2.210667487414817)},line width=1.pt]  plot[domain=2.1382500318753346:3.249895324989884,variable=\\t]({1.*0.029312015218738607*cos(\\t r)+0.*0.029312015218738607*sin(\\t r)},{0.*0.029312015218738607*cos(\\t r)+1.*0.029312015218738607*sin(\\t r)});\n'
                    '\\draw [shift={(0.07558005127800108,-2.7469396783546762)},line width=1.pt]  plot[domain=2.602561819326099:3.8128280443046836,variable=\\t]({1.*0.1735613798219292*cos(\\t r)+0.*0.1735613798219292*sin(\\t r)},{0.*0.1735613798219292*cos(\\t r)+1.*0.1735613798219292*sin(\\t r)});\n'
                    '\\draw [shift={(0.23479559093462216,-2.6901596591003165)},line width=1.pt]  plot[domain=3.0371291759824355:3.6904264903574178,variable=\\t]({1.*0.30985618885967225*cos(\\t r)+0.*0.30985618885967225*sin(\\t r)},{0.*0.30985618885967225*cos(\\t r)+1.*0.30985618885967225*sin(\\t r)});\n'
                    '\\draw [shift={(1.465706657593817,-2.149892328528027)},line width=1.pt]  plot[domain=3.4603763857837246:3.5831955659321664,variable=\\t]({1.*1.6207351109994779*cos(\\t r)+0.*1.6207351109994779*sin(\\t r)},{0.*1.6207351109994779*cos(\\t r)+1.*1.6207351109994779*sin(\\t r)});\n'
                    '\\draw [shift={(-0.38576101798841783,-2.951451948555383)},line width=1.pt]  plot[domain=0.24195847382454244:0.754405273268819,variable=\\t]({1.*0.4287066945756778*cos(\\t r)+0.*0.4287066945756778*sin(\\t r)},{0.*0.4287066945756778*cos(\\t r)+1.*0.4287066945756778*sin(\\t r)});\n'
                    '\\draw [shift={(-0.2798178003596934,-2.9592423615947223)},line width=1.pt]  plot[domain=0.32949449340021975:0.9702255997382151,variable=\\t]({1.*0.36531840925842024*cos(\\t r)+0.*0.36531840925842024*sin(\\t r)},{0.*0.36531840925842024*cos(\\t r)+1.*0.36531840925842024*sin(\\t r)});\n'
                    '\\draw [shift={(0.5064106229683653,-2.592588109418518)},line width=1.pt]  plot[domain=3.7093585078367837:4.581521131899287,variable=\\t]({1.*0.10392800077492993*cos(\\t r)+0.*0.10392800077492993*sin(\\t r)},{0.*0.10392800077492993*cos(\\t r)+1.*0.10392800077492993*sin(\\t r)});\n'
                    '\\draw [shift={(0.5332108358464673,-2.6177029535572776)},line width=1.pt]  plot[domain=3.404313483273165:4.3370188011205695,variable=\\t]({1.*0.11848806630057174*cos(\\t r)+0.*0.11848806630057174*sin(\\t r)},{0.*0.11848806630057174*cos(\\t r)+1.*0.11848806630057174*sin(\\t r)});\n'
                    '\\draw [shift={(0.567741896372487,-2.630352893889358)},line width=1.pt]  plot[domain=3.2626629797767017:4.22334550806811,variable=\\t]({1.*0.15005182641986628*cos(\\t r)+0.*0.15005182641986628*sin(\\t r)},{0.*0.15005182641986628*cos(\\t r)+1.*0.15005182641986628*sin(\\t r)});\n'
                    '\\draw [shift={(1.0101254517944265,-0.3015843753729407)},line width=1.pt,color=qqffff]  plot[domain=4.071350162706313:5.330956833547141,variable=\\t]({1.*1.0632497653033235*cos(\\t r)+0.*1.0632497653033235*sin(\\t r)},{0.*1.0632497653033235*cos(\\t r)+1.*1.0632497653033235*sin(\\t r)});\n'
                    '\\draw [shift={(0.9860523620842628,-0.7817971485300839)},line width=1.pt,color=qqffff]  plot[domain=4.062621401552663:5.323451714385806,variable=\\t]({1.*0.4595040039812063*cos(\\t r)+0.*0.4595040039812063*sin(\\t r)},{0.*0.4595040039812063*cos(\\t r)+1.*0.4595040039812063*sin(\\t r)});\n'
                    '\\draw [shift={(1.1008505367714987,-1.5519709945898161)},line width=1.pt,color=qqffff]  plot[domain=1.06011712415332:1.8182992465206331,variable=\\t]({1.*0.6476853913778554*cos(\\t r)+0.*0.6476853913778554*sin(\\t r)},{0.*0.6476853913778554*cos(\\t r)+1.*0.6476853913778554*sin(\\t r)});\n'
                    '\\draw [shift={(0.783473107943988,-1.3911102604455592)},line width=1.pt,color=qqffff]  plot[domain=1.391829726001232:2.2192081525589527,variable=\\t]({1.*0.6167148388465494*cos(\\t r)+0.*0.6167148388465494*sin(\\t r)},{0.*0.6167148388465494*cos(\\t r)+1.*0.6167148388465494*sin(\\t r)});\n'
                    '\\draw [shift={(0.3688295130668951,-1.0390750759931675)},line width=1.pt,color=qqffff]  plot[domain=1.8072990694887392:3.884246700612849,variable=\\t]({1.*0.22258702098197036*cos(\\t r)+0.*0.22258702098197036*sin(\\t r)},{0.*0.22258702098197036*cos(\\t r)+1.*0.22258702098197036*sin(\\t r)});\n'
                    '\\draw [shift={(1.66342183139273,-1.1136215279834247)},line width=1.pt,color=qqffff]  plot[domain=-0.20305700639731494:1.8966039974198499,variable=\\t]({1.*0.25545427870449616*cos(\\t r)+0.*0.25545427870449616*sin(\\t r)},{0.*0.25545427870449616*cos(\\t r)+1.*0.25545427870449616*sin(\\t r)});\n'
                    '\\draw [shift={(1.3586864787117865,-0.899158235491216)},line width=1.pt,color=qqffff]  plot[domain=4.787879642374751:5.564193536396235,variable=\\t]({1.*0.5470913290064053*cos(\\t r)+0.*0.5470913290064053*sin(\\t r)},{0.*0.5470913290064053*cos(\\t r)+1.*0.5470913290064053*sin(\\t r)});\n'
                    '\\draw (-0.3114395457411715,-1.3992024354763921) node[anchor=north west] {$A$};\n'
                    '\\draw (0.42232516140716264,-0.41670392929472905) node[anchor=north west] {$B$};\n'
                    '\\draw (2.9469732215954987,2.2571844103135943) node[anchor=north west] {$C$};\n'
                    '\\draw (-0.6099201045811719,0.6031046467419339) node[anchor=north west] {$O$};\n'
                    '\\draw (-2.8360876059295075,-1.8) node[anchor=north west] {$x$};\n'
                    '\\draw (5.533804731542168,-0.1) node[anchor=north west] {$y$};\n'
                    '\\draw (-0.5,4) node[anchor=north west] {$z$};\n'
                    '\\begin{scriptsize}\n'
                        '\\draw [fill=ffqqqq] (0.9590319257008675,-1.0628412681105723) circle (1.5pt);\n'
                        '\\draw [fill=ffqqqq] (2.9923853653107155,1.9885780479660733) circle (1.5pt);\n'
                        '\\draw [fill=ffqqqq] (0.3349996723485401,-2.020049504363662) circle (1.5pt);\n'
                    '\\end{scriptsize}\n'
                    '\\end{tikzpicture}}}\n'



                    %(latex(z1),latex(y1),latex(x1),latex(h),latex(y2),latex(x2)))

                # Nội dung lời giải
                loigiai = ('Ta có $A\\left(%s;%s;-%s\\right),C\\left(%s;%s;%s\\right)$ và $\\vec{AC}=\\left(%s;%s;%s\\right)$.\\\\ \n'
                        'Vì $B \\in (Oxy)$ nên $B(x;y;0)$. Suy ra $\\vec{AB}=\\left(x-%s;y-%s;%s\\right)$.\\\\ \n'
                        'Vì ba điểm $A,B,C$ thẳng hàng nên hai vectơ $\\vec{AB}$ và $\\vec{AC}$ cùng phương\\\\ \n'
                        'Do đó $\\dfrac{x-%s}{%s}=\\dfrac{y-%s}{%s}=\\dfrac{%s}{%s}\\Rightarrow \\heva{x=%s\\\\y=%s}$.\\\\ \n'
                        'Vậy $B\\left(%s;%s;0\\right)$.'
                        %(latex(x2),latex(y2),latex(z2),
                            latex(x1),latex(y1),latex(z1),
                            latex(x1-x2),latex(y1-y2),latex(z1+z2),
                            latex(x2),latex(y2),latex(z2),
                            latex(x2),latex(x1-x2),latex(y2),latex(y1-y2),latex(z2),latex(z1+z2),
                            latex(x3),latex(y3),latex(x3),latex(y3),

                            )
                        )
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content 

