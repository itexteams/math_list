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


def bt_dang11_p1_b1_c2_hh10(self):
            # Khai báo biến
            d = ['$\\overrightarrow{HA}=\\overrightarrow{CD}$',
                '$\\overrightarrow{AD}=\\overrightarrow{HC}$',
                '$\\overrightarrow{DA}=\\overrightarrow{CH}$',
                '$\\overrightarrow{AH}=\\overrightarrow{DC}$',
                ]
            da= random.choice(d)
            s = ['$\\overrightarrow{HA}=\\overrightarrow{DC}$',
                '$\\overrightarrow{AD}=\\overrightarrow{CH}$',
                '$\\overrightarrow{OB}=\\overrightarrow{OC}$',
                '$\\overrightarrow{HB}=\\overrightarrow{AC}$',
                '$\\overrightarrow{HC}=\\overrightarrow{AB}$',
                '$\\overrightarrow{HO}=\\overrightarrow{BC}$',
                '$\\overrightarrow{AB}=\\overrightarrow{CH}$',
                '$\\overrightarrow{BC}=\\overrightarrow{HA}$',
                '$\\overrightarrow{AC}=\\overrightarrow{HB}$',
                '$\\overrightarrow{OH}=\\overrightarrow{CA}$',
                ]
            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)

            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Câu hỏi
                noidungcauhoi='''Cho tam giác $ABC$ có trực tâm $H$. $D$ là điểm đối xứng với $B$ qua tâm $O$ của đường tròn ngoại tiếp tam giác $ABC$. Khẳng định nào sau đây đúng? \n'''
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        '\\begin{center} \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1.5]   \n'
                        '\\clip(-1.909973675373131,-1.7754926904268369) rectangle (1.8042258770284245,1.8608410432660853); \n'
                        '\\draw(0.,0.) circle (1.5cm); \n'
                        '\\draw (-0.6039720408234261,1.3730323280620838)-- (-1.3629529666281197,-0.6263858321830145); \n'
                        '\\draw (-0.6039720408234261,1.3730323280620838)-- (1.3623987014414416,-0.6275904542858135); \n'
                        '\\draw (1.3623987014414416,-0.6275904542858135)-- (-1.3629529666281197,-0.6263858321830145); \n'
                        '\\draw (-0.6039720408234261,1.3730323280620838)-- (-0.6048559439856518,-0.6267209157027821); \n'
                        '\\draw (-1.3629529666281197,-0.6263858321830145)-- (0.02265027767971544,0.7354949301647232); \n'
                        '\\draw (1.3623987014414416,-0.6275904542858135)-- (-1.0200997437842922,0.2768080910710037); \n'
                        '\\draw (0.6039720408234261,-1.3730323280620838)-- (-0.6039720408234261,1.3730323280620838); \n'
                        '\\draw (-1.3629529666281197,-0.6263858321830145)-- (0.6039720408234261,-1.3730323280620838); \n'
                        '\\draw (0.6039720408234261,-1.3730323280620838)-- (1.3623987014414416,-0.6275904542858135); \n'
                        '\\draw (-1.776376219247247,-0.4362006086384373) node[anchor=north west] {$A$}; \n'
                        '\\draw (-0.7964924678397505,1.767402060815732) node[anchor=north west] {$B$}; \n'
                        '\\draw (1.4304699472270102,-0.4751335179927512) node[anchor=north west] {$C$}; \n'
                        '\\draw (0.581732523302965,-1.2849380325624813) node[anchor=north west] {$D$}; \n'
                        '\\draw (0.00003153795515743,0.217872268514037) node[anchor=north west] {$O$}; \n'
                        '\\draw (-0.6329742485516318,0.05336619541799746) node[anchor=north west] {$H$}; \n'
        	            '\\end{tikzpicture} \n'
                        '\\end{center} \n'

                        '$BD$ là đường kính nên $\\overrightarrow{OB}=\\overrightarrow{DO}$. \\\\ \n'
                        '$AH \\bot BC, DC \\bot BC \\Rightarrow AH // DC$. \\\\ \n'
                        'Và $CH \\bot AB, DA \\bot AB \\Rightarrow CH // DA$. \\\\ \n'
                        'Suy ra tứ giác $HADC$ là hình bình hành $\\Rightarrow \\overrightarrow{HA}=\\overrightarrow{CD}$ và $\\overrightarrow{AD}=\\overrightarrow{HC}$.'

                        )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

