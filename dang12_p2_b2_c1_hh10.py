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


def bt_dang12_p2_b2_c1_hh10(self):
    # Khai báo biến và ngẫu nhiên hóa độ cao h
    h = random.choice([6, 9, 12, 15, 18, 24])

    # Tính toán các đại lượng hình học theo SymPy
    AM_expr = sp.Rational(2 * h, 3) * sp.sqrt(3)
    BM_expr = 2 * h
    AB_expr = sp.Rational(2 * h, 3) * sp.sqrt(3)

    # Mã TikZ vẽ hình đài quan sát và 2 vận động viên

    # Nội dung câu hỏi
    noidungcauhoi = ('''Một người đứng trên đài quan sát đặt ở cuối một đường đua thẳng. Ở độ cao $%s\\text{ m}$ so với mặt đường đua, tại một thời điểm người đó nhìn thấy hai vận động viên A và B dưới các góc tương ứng là $60^\\circ$ và $30^\\circ$, so với phương nằm ngang như hình vẽ.
    \\begin{center}
    	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.2,xscale=1.2]
    		\\tikzset {_f4g8le2b8/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-90 }  \\pgftransformscale{2 }  }}}
    		\\pgfdeclarehorizontalshading{_rdkt2f3kz}{150bp}{rgb(0bp)=(0.6,0.85,1);
    			rgb(37.5bp)=(0.6,0.85,1);
    			rgb(62.5bp)=(1,1,1);
    			rgb(100bp)=(1,1,1)}
    		\\tikzset{every picture/.style={line width=0.75pt}}  
    		\\draw  [draw opacity=0][shading=_rdkt2f3kz,_f4g8le2b8] (41.6,25.4) -- (308.5,25.4) -- (308.5,165.9) -- (41.6,165.9) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (71.41,63.71) .. controls (71.41,62.63) and (72.58,61.76) .. (74.02,61.76) .. controls (75.47,61.76) and (76.64,62.63) .. (76.64,63.71) .. controls (76.64,64.79) and (75.47,65.66) .. (74.02,65.66) .. controls (72.58,65.66) and (71.41,64.79) .. (71.41,63.71) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (70.52,65.3) -- (76.16,66.56) -- (75.15,73.48) -- (69.92,72.47) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (69.92,72.47) -- (75.15,73.48) -- (75.33,77.99) -- (74.48,84.13) -- (72.22,85.4) -- (71.94,76.13) -- (71.65,83.92) -- (69.1,84.13) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 240; green, 226; blue, 201 }  ,fill opacity=1 ] (76.16,66.56) -- (78.35,68.57) -- (78.73,65.93) -- (78.73,65.93) -- (77.51,69.83) -- (75.15,67.82) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 240; green, 226; blue, 201 }  ,fill opacity=1 ] (76.64,63.71) -- (75.29,65.29) -- (74.02,65.66) -- (72.76,65.29) -- (73.14,63.62) -- (75.62,63.02) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (76.86,64.41) -- (80.6,64.41) -- (80.6,65.93) -- (76.86,65.93) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (303.6,166.4) -- (307.1,161.9) -- (56.6,161.4) -- (41.6,165.9) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.4 ][fill={rgb, 255:red, 144; green, 174; blue, 208 }  ,fill opacity=1 ] (57.31,83.98) -- (60.41,84.04) -- (58.79,164.42) -- (55.69,164.36) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.4 ][fill={rgb, 255:red, 144; green, 174; blue, 208 }  ,fill opacity=1 ] (72.54,83.62) -- (75.63,83.47) -- (79.56,163.78) -- (76.47,163.93) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.47 ][fill={rgb, 255:red, 144; green, 174; blue, 208 }  ,fill opacity=1 ] (52.6,83.5) -- (80.1,83.5) -- (80.1,86.4) -- (52.6,86.4) -- cycle ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (59.6,145.9) -- (75.6,145.4) ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (59.1,120.9) -- (74.6,120.9) ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (59.6,145.9) -- (67.6,161.4) ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (67.6,161.4) -- (75.6,145.4) ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (59.1,120.9) -- (75.6,145.4) ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (59.6,145.9) -- (74.6,120.9) ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (59.1,120.9) -- (72.6,86.4) ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (74.6,120.9) -- (61.1,87.4) ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.47 ][fill={rgb, 255:red, 144; green, 174; blue, 208 }  ,fill opacity=1 ] (52.6,62.4) -- (54.6,62.4) -- (54.6,83.5) -- (52.6,83.5) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.47 ][fill={rgb, 255:red, 144; green, 174; blue, 208 }  ,fill opacity=1 ] (78.1,62.4) -- (80.1,62.4) -- (80.1,83.5) -- (78.1,83.5) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.42 ][fill={rgb, 255:red, 144; green, 174; blue, 208 }  ,fill opacity=1 ] (66.6,46.4) -- (86.1,62) -- (47.5,62) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.26 ] (66.6,46.4) -- (72.6,62.4) -- (47.5,62) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (66.6,46.4) -- (80.1,62.4) -- (75.1,61.9) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.47 ][fill={rgb, 255:red, 144; green, 174; blue, 208 }  ,fill opacity=1 ] (54.6,71.5) -- (78.1,71.5) -- (78.1,72.95) -- (54.6,72.95) -- cycle ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (66.6,72.95) -- (66.35,83.5) ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (60.11,72.46) -- (59.86,83.01) ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (72.6,72.95) -- (72.35,83.5) ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (75.6,72.95) -- (75.35,83.5) ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (69.6,72.95) -- (69.35,83.5) ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (63.6,72.95) -- (63.35,83.5) ;
    		\\draw [color={rgb, 255:red, 81; green, 102; blue, 127 }  ,draw opacity=1 ]   (57.6,72.95) -- (57.35,83.5) ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 240; green, 226; blue, 201 }  ,fill opacity=1 ] (174.65,144.78) -- (171.67,145.6) -- (169.7,149.17) -- (169.31,147.87) -- (171.06,144.16) -- (174.13,143.19) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (175.16,142.19) .. controls (175.16,141.01) and (176.12,140.05) .. (177.3,140.05) .. controls (178.48,140.05) and (179.44,141.01) .. (179.44,142.19) .. controls (179.44,143.37) and (178.48,144.33) .. (177.3,144.33) .. controls (176.12,144.33) and (175.16,143.37) .. (175.16,142.19) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (174.19,143.23) -- (178.2,146.4) -- (175.44,151.51) -- (171.16,150.4) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (171.16,150.4) -- (175.44,151.51) -- (178.47,153.3) -- (175.57,156.2) -- (172.81,154.41) -- (170.33,156.62) -- (167.84,154.13) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 240; green, 226; blue, 201 }  ,fill opacity=1 ] (178.47,153.3) -- (181.1,155.79) -- (176.26,162.41) -- (175.02,161.31) -- (176.54,157.86) -- (177.78,156.62) -- (175.57,156.2) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 240; green, 226; blue, 201 }  ,fill opacity=1 ] (167.84,154.13) -- (170.33,156.62) -- (167.01,158.69) -- (161.63,160.9) -- (161.08,159.65) -- (164.67,157.31) -- (166.88,156.62) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (174.58,161.61) -- (176.54,162.41) -- (177.78,164.9) -- (175.85,164.21) -- (174.06,162.69) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (161.08,159.65) -- (161.05,161.77) -- (159.19,163.84) -- (159.13,161.78) -- (159.88,159.56) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 240; green, 226; blue, 201 }  ,fill opacity=1 ] (178.2,146.4) -- (179.99,148.61) -- (183.17,148.33) -- (182.48,149.44) -- (179.3,149.99) -- (177.37,147.78) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 240; green, 226; blue, 201 }  ,fill opacity=1 ] (179.44,142.19) -- (178.34,143.92) -- (177.3,144.33) -- (176.26,143.92) -- (176.58,142.09) -- (178.61,141.43) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 239; green, 224; blue, 201 }  ,fill opacity=1 ] (183.17,148.33) -- (185.1,148.2) -- (185.1,149.85) -- (183.86,150.4) -- (182.64,149.41) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 239; green, 224; blue, 201 }  ,fill opacity=1 ] (168.53,148.33) -- (169.91,148.2) -- (169.91,149.85) -- (168.67,150.4) -- (167.98,149.44) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 240; green, 226; blue, 201 }  ,fill opacity=1 ] (269.59,145.25) -- (266.53,146.1) -- (264.51,149.76) -- (264.11,148.42) -- (265.9,144.62) -- (269.06,143.62) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (270.11,142.6) .. controls (270.11,141.38) and (271.1,140.4) .. (272.31,140.4) .. controls (273.52,140.4) and (274.5,141.38) .. (274.5,142.6) .. controls (274.5,143.81) and (273.52,144.79) .. (272.31,144.79) .. controls (271.1,144.79) and (270.11,143.81) .. (270.11,142.6) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (269.12,143.66) -- (273.23,146.92) -- (270.4,152.16) -- (266,151.02) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (266,151.02) -- (270.4,152.16) -- (273.51,154) -- (270.54,156.97) -- (267.7,155.13) -- (265.15,157.4) -- (262.6,154.85) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 240; green, 226; blue, 201 }  ,fill opacity=1 ] (273.51,154) -- (276.2,156.55) -- (271.25,163.35) -- (269.97,162.22) -- (271.53,158.67) -- (272.8,157.4) -- (270.54,156.97) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 240; green, 226; blue, 201 }  ,fill opacity=1 ] (262.6,154.85) -- (265.15,157.4) -- (261.75,159.52) -- (256.23,161.79) -- (255.66,160.52) -- (259.35,158.11) -- (261.61,157.4) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (269.52,162.53) -- (271.53,163.35) -- (272.8,165.9) -- (270.82,165.19) -- (268.98,163.63) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (255.66,160.52) -- (255.63,162.69) -- (253.72,164.81) -- (253.66,162.7) -- (254.44,160.42) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 240; green, 226; blue, 201 }  ,fill opacity=1 ] (273.23,146.92) -- (275.07,149.18) -- (278.33,148.9) -- (277.62,150.03) -- (274.36,150.6) -- (272.38,148.33) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 240; green, 226; blue, 201 }  ,fill opacity=1 ] (274.5,142.6) -- (273.37,144.37) -- (272.31,144.79) -- (271.25,144.37) -- (271.57,142.49) -- (273.65,141.82) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 239; green, 224; blue, 201 }  ,fill opacity=1 ] (278.33,148.9) -- (280.31,148.76) -- (280.31,150.46) -- (279.04,151.02) -- (277.79,150) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 239; green, 224; blue, 201 }  ,fill opacity=1 ] (263.31,148.9) -- (264.73,148.76) -- (264.73,150.46) -- (263.45,151.02) -- (262.75,150.03) -- cycle ;
    		\\draw  [dash pattern={on 4.5pt off 4.5pt}]  (80.6,64.41) -- (171.06,144.16) ;
    		\\draw  [dash pattern={on 4.5pt off 4.5pt}]  (80.6,64.41) -- (265.9,144.62) ;
    		\\draw  [dash pattern={on 4.5pt off 4.5pt}]  (80.6,64.41) -- (258.6,64.41) ;
    		\\draw    (84.02,74.5) -- (84.48,159.9) ;
    		\\draw [shift={(84.5,162.9)}, rotate = 269.69] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
    		\\draw [shift={(84,71.5)}, rotate = 89.69] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
    		\\draw    (103,74.4) .. controls (110,73.9) and (113.5,68.4) .. (111.5,64) ;
    		\\draw    (91,73.9) .. controls (98,73.4) and (101.5,67.9) .. (99.5,63.5) ;
    		\\draw (68,166.5) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$O$};
    		\\draw (167,165.5) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$A$};
    		\\draw (264.5,166.5) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$B$};
    		\\draw (79.5,43.5) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$M$};
    		\\draw (106.5,53) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$30^{o}$};
    		\\draw (91,52.5) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$60^{o}$};
    		\\draw (86,109) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$%s$m};
    	\\end{tikzpicture}
    \\end{center}''' %(latex(h),latex(h)))

    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Độ dài $AB^2 = BM^2 + AM^2 - 2BM \\cdot AM \\cdot \\cos 30^\\circ$'
    nb_da_1_s = 'Độ dài $AB^2 = BM^2 + AM^2 + 2BM \\cdot AM \\cdot \\cos 30^\\circ$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Góc giữa hai tia quan sát là $\\widehat{AMB} = 60^\\circ - 30^\\circ = 30^\\circ$. \\\\
    Theo định lý côsin trong tam giác $ABM$, ta có $AB^2 = BM^2 + AM^2 - 2BM \\cdot AM \\cdot \\cos 30^\\circ$.'''
                )

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ######################################################################## Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Diện tích tam giác $ABM$ được tính theo công thức $S_{\\Delta ABM} = \\frac{1}{2} \\cdot AM \\cdot AB \\cdot \\sin 60^\\circ$'
    th_da_1_s = 'Diện tích tam giác $ABM$ được tính theo công thức $S_{\\Delta ABM} = \\frac{1}{2} \\cdot AM \\cdot AB \\cdot \\cos 60^\\circ$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Ta có góc $\\widehat{MAB} = 180^\\circ - 60^\\circ = 120^\\circ$. \\\\
    Diện tích tam giác $ABM$ là $S_{\\Delta ABM} = \\frac{1}{2} \\cdot AM \\cdot AB \\cdot \\sin 120^\\circ$. \\\\
    Do $\\sin 120^\\circ = \\sin 60^\\circ$ nên $S_{\\Delta ABM} = \\frac{1}{2} \\cdot AM \\cdot AB \\cdot \\sin 60^\\circ$.'''
                )

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Độ dài cạnh $AM$ là $%s\\text{ (m)}$' %(latex(AM_expr))
    vd_da_1_s = 'Độ dài cạnh $AM$ là $%s\\text{ (m)}$' %(latex(AM_expr + 2))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Xét tam giác vuông $MHA$ tại chân đường cao $H$, ta có: \\\\
    $AM = \\frac{MH}{\\sin 60^\\circ} = \\frac{%s}{\\frac{\\sqrt{3}}{2}} = %s\\text{ (m)}$.'''
                %(latex(h), latex(AM_expr)
                    ))

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Khoảng cách giữa hai vận động viên A và B tại thời điểm đó là $%s\\text{ (m)}$' %(latex(AB_expr))
    vdc_da_1_s = 'Khoảng cách giữa hai vận động viên A và B tại thời điểm đó là $%s\\text{ (m)}$' %(latex(h))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Xét tam giác vuông $MHB$ tại $H$, ta có $BM = \\frac{MH}{\\sin 30^\\circ} = \\frac{%s}{\\frac{1}{2}} = %s\\text{ (m)}$. \\\\
    Áp dụng định lý côsin trong tam giác $ABM$: \\\\
    $AB = \\sqrt{AM^2 + BM^2 - 2 \\cdot AM \\cdot BM \\cdot \\cos 30^\\circ} = %s\\text{ (m)}$.'''
                %(latex(h), latex(BM_expr), latex(AB_expr)
                    ))

    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vdc)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+
    str(noidungcauhoi)+ 
        '\n\\choiceTFn \n'
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
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

