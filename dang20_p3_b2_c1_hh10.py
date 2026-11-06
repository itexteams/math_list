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


def bt_dang20_p3_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random khoảng cách d (PQ)
                d = random.choice([200, 250, 300, 350, 400, 450, 500])

                # Random góc nhìn từ P (nhỏ hơn) và Q (lớn hơn)
                alpha = random.randint(10, 20)
                beta = random.randint(35, 50)

                # Tính toán kết quả
                rad_a = math.radians(alpha)
                rad_b = math.radians(beta)
                cot_a = 1 / math.tan(rad_a)
                cot_b = 1 / math.tan(rad_b)

                h = d / (cot_a - cot_b)
                kq_num = round(h)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(latex(kq_num))]
                da = random.choice(du)

                s = ['$%s$'%(latex(kq_num + 10)),
                     '$%s$'%(latex(kq_num + 5)),
                     '$%s$'%(latex(kq_num + 2)),
                     '$%s$'%(latex(kq_num + 1)),
                     '$%s$'%(latex(kq_num - 1)),
                     '$%s$'%(latex(kq_num - 2)),
                     '$%s$'%(latex(kq_num - 5)),
                     '$%s$'%(latex(kq_num - 10))
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\scalebox{0.6}{ \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\tikzset {_sir5s7obj/.code = {\pgfsetadditionalshadetransform{ 
            	\pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-271 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_k183i7izw}{150bp}{rgb(0bp)=(0.99,0.99,0.66);
            rgb(37.5bp)=(0.99,0.99,0.66);
            rgb(62.5bp)=(0.67,0.94,0.94);
            rgb(100bp)=(0.67,0.94,0.94)}
            \tikzset {_zucviyb05/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_3deztv9r7}{150bp}{rgb(0bp)=(0.68,0.96,0.9);
            rgb(37.5bp)=(0.68,0.96,0.9);
            rgb(62.5bp)=(0.33,0.77,0.77);
            rgb(100bp)=(0.33,0.77,0.77)}
            \tikzset{every picture/.style={line width=0.75pt}} 
            	\draw  [draw opacity=0][shading=_k183i7izw,_sir5s7obj] (56.7,19.23) -- (455.84,19.23) -- (455.84,271.67) -- (56.7,271.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.8 ] (107.35,101.71) .. controls (124.18,101.71) and (138.5,112.07) .. (143.87,126.55) .. controls (145.09,126.38) and (146.34,126.3) .. (147.61,126.3) .. controls (160.47,126.3) and (171.26,134.87) .. (174.2,146.43) .. controls (178.36,140.87) and (185.12,137.25) .. (192.76,137.25) .. controls (205.4,137.25) and (215.65,147.15) .. (215.65,159.37) .. controls (215.65,161.58) and (215.31,163.72) .. (214.68,165.74) -- (215.66,165.74) .. controls (217.47,161.89) and (221.49,159.22) .. (226.15,159.22) .. controls (230.81,159.22) and (234.82,161.89) .. (236.63,165.74) -- (249.3,165.74) .. controls (253.75,165.74) and (257.37,169.23) .. (257.37,173.54) .. controls (257.37,177.84) and (253.75,181.34) .. (249.3,181.34) -- (228.04,181.34) .. controls (227.42,181.43) and (226.79,181.49) .. (226.15,181.49) .. controls (225.5,181.49) and (224.87,181.43) .. (224.25,181.34) -- (195.44,181.34) .. controls (194.56,181.43) and (193.67,181.49) .. (192.76,181.49) .. controls (191.86,181.49) and (190.96,181.43) .. (190.09,181.34) -- (59.95,181.34) .. controls (59.04,181.43) and (58.11,181.49) .. (57.17,181.49) .. controls (56.84,181.49) and (56.52,181.48) .. (56.2,181.47) -- (56.2,133.97) .. controls (56.52,133.96) and (56.84,133.95) .. (57.17,133.95) .. controls (61.32,133.95) and (65.23,134.94) .. (68.66,136.7) .. controls (69.99,117.16) and (86.8,101.71) .. (107.35,101.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (145.78,40.84) .. controls (151.8,40.84) and (156.92,44) .. (158.84,48.41) .. controls (159.27,48.36) and (159.72,48.33) .. (160.17,48.33) .. controls (164.77,48.33) and (168.63,50.94) .. (169.68,54.46) .. controls (171.17,52.77) and (173.59,51.67) .. (176.32,51.67) .. controls (180.84,51.67) and (184.5,54.68) .. (184.5,58.4) .. controls (184.5,59.08) and (184.38,59.73) .. (184.15,60.34) -- (184.5,60.34) .. controls (185.15,59.17) and (186.59,58.36) .. (188.25,58.36) .. controls (189.92,58.36) and (191.35,59.17) .. (192,60.34) -- (196.53,60.34) .. controls (198.12,60.34) and (199.42,61.41) .. (199.42,62.72) .. controls (199.42,64.03) and (198.12,65.09) .. (196.53,65.09) -- (188.93,65.09) .. controls (188.71,65.12) and (188.48,65.14) .. (188.25,65.14) .. controls (188.02,65.14) and (187.8,65.12) .. (187.58,65.09) -- (177.28,65.09) .. controls (176.96,65.12) and (176.64,65.14) .. (176.32,65.14) .. controls (175.99,65.14) and (175.67,65.12) .. (175.36,65.09) -- (128.83,65.09) .. controls (128.5,65.12) and (128.17,65.14) .. (127.84,65.14) .. controls (127.5,65.14) and (127.17,65.12) .. (126.84,65.09) -- (117.8,65.09) .. controls (117.26,65.27) and (116.67,65.37) .. (116.05,65.37) .. controls (115.43,65.37) and (114.84,65.27) .. (114.3,65.09) -- (114.16,65.09) .. controls (112.57,65.09) and (111.28,64.03) .. (111.28,62.72) .. controls (111.28,62.52) and (111.31,62.34) .. (111.36,62.16) .. controls (111.31,61.93) and (111.28,61.68) .. (111.28,61.44) .. controls (111.28,59.27) and (113.42,57.51) .. (116.05,57.51) .. controls (117.19,57.51) and (118.24,57.84) .. (119.07,58.4) .. controls (119.05,58.23) and (119.05,58.07) .. (119.05,57.9) .. controls (119.05,53.9) and (122.98,50.66) .. (127.84,50.66) .. controls (129.32,50.66) and (130.72,50.96) .. (131.94,51.5) .. controls (132.42,45.55) and (138.43,40.84) .. (145.78,40.84) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (330.02,68.87) .. controls (323.23,68.87) and (317.45,72.02) .. (315.28,76.43) .. controls (314.79,76.38) and (314.28,76.36) .. (313.77,76.36) .. controls (308.58,76.36) and (304.23,78.97) .. (303.04,82.49) .. controls (301.36,80.79) and (298.63,79.69) .. (295.55,79.69) .. controls (290.45,79.69) and (286.31,82.71) .. (286.31,86.43) .. controls (286.31,87.1) and (286.45,87.75) .. (286.7,88.37) -- (286.31,88.37) .. controls (285.58,87.19) and (283.96,86.38) .. (282.08,86.38) .. controls (280.2,86.38) and (278.58,87.19) .. (277.84,88.37) -- (272.73,88.37) .. controls (270.93,88.37) and (269.48,89.43) .. (269.48,90.74) .. controls (269.48,92.05) and (270.93,93.12) .. (272.73,93.12) -- (281.31,93.12) .. controls (281.56,93.15) and (281.82,93.16) .. (282.08,93.16) .. controls (282.34,93.16) and (282.59,93.15) .. (282.84,93.12) -- (294.47,93.12) .. controls (294.82,93.15) and (295.18,93.16) .. (295.55,93.16) .. controls (295.91,93.16) and (296.27,93.15) .. (296.63,93.12) -- (349.15,93.12) .. controls (349.52,93.15) and (349.89,93.16) .. (350.27,93.16) .. controls (350.65,93.16) and (351.03,93.15) .. (351.39,93.12) -- (361.6,93.12) .. controls (362.21,93.29) and (362.88,93.39) .. (363.58,93.39) .. controls (364.28,93.39) and (364.94,93.29) .. (365.56,93.12) -- (365.71,93.12) .. controls (367.5,93.12) and (368.96,92.05) .. (368.96,90.74) .. controls (368.96,90.55) and (368.93,90.36) .. (368.87,90.18) .. controls (368.93,89.95) and (368.96,89.71) .. (368.96,89.46) .. controls (368.96,87.29) and (366.55,85.54) .. (363.58,85.54) .. controls (362.29,85.54) and (361.1,85.87) .. (360.17,86.42) .. controls (360.19,86.26) and (360.2,86.09) .. (360.2,85.92) .. controls (360.2,81.93) and (355.75,78.69) .. (350.27,78.69) .. controls (348.6,78.69) and (347.02,78.99) .. (345.64,79.52) .. controls (345.1,73.57) and (338.31,68.87) .. (330.02,68.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.8 ] (412.37,108.71) .. controls (398.07,108.71) and (385.9,119.07) .. (381.33,133.55) .. controls (380.29,133.39) and (379.23,133.31) .. (378.16,133.31) .. controls (367.23,133.31) and (358.06,141.88) .. (355.56,153.44) .. controls (352.03,147.87) and (346.28,144.25) .. (339.79,144.25) .. controls (329.05,144.25) and (320.34,154.16) .. (320.34,166.37) .. controls (320.34,168.59) and (320.63,170.73) .. (321.16,172.75) -- (320.33,172.75) .. controls (318.79,168.9) and (315.38,166.22) .. (311.42,166.22) .. controls (307.46,166.22) and (304.05,168.9) .. (302.51,172.75) -- (291.74,172.75) .. controls (287.96,172.75) and (284.89,176.24) .. (284.89,180.54) .. controls (284.89,184.85) and (287.96,188.34) .. (291.74,188.34) -- (309.81,188.34) .. controls (310.33,188.44) and (310.87,188.49) .. (311.42,188.49) .. controls (311.97,188.49) and (312.51,188.44) .. (313.03,188.34) -- (337.51,188.34) .. controls (338.26,188.44) and (339.02,188.49) .. (339.79,188.49) .. controls (340.56,188.49) and (341.32,188.44) .. (342.06,188.34) -- (452.65,188.34) .. controls (453.43,188.44) and (454.21,188.49) .. (455.01,188.49) .. controls (455.29,188.49) and (455.56,188.49) .. (455.84,188.47) -- (455.84,140.97) .. controls (455.56,140.96) and (455.29,140.96) .. (455.01,140.96) .. controls (451.49,140.96) and (448.16,141.95) .. (445.25,143.7) .. controls (444.12,124.16) and (429.83,108.71) .. (412.37,108.71) -- cycle ;
            	\draw  [draw opacity=0][shading=_3deztv9r7,_zucviyb05] (56.2,169.75) -- (455.84,169.75) -- (455.84,271.67) -- (56.2,271.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.61 ] (311.65,230.43) .. controls (339.68,216.42) and (465.78,202.4) .. (437.76,230.43) .. controls (430.2,237.99) and (345.56,279.61) .. (351.26,255.14) .. controls (342.12,256.29) and (335.11,256.44) .. (332.25,255.09) .. controls (327.35,238.97) and (347.76,243.77) .. (336.45,242.48) .. controls (313.35,239.83) and (311.77,236.55) .. (311.65,230.43) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.26 ][fill={rgb, 255:red, 198; green, 197; blue, 179 }  ,fill opacity=1 ] (299.6,157.14) .. controls (304.56,154.67) and (312.3,164.46) .. (323.42,161.35) .. controls (327.42,160.75) and (342.84,149.2) .. (360.55,144.53) .. controls (368.31,142.49) and (383.6,159.61) .. (392.08,157.84) .. controls (402.07,155.77) and (415.61,139.92) .. (424.31,136.83) .. controls (438.32,140.33) and (445.33,141.73) .. (455.01,140.96) .. controls (456.54,172.56) and (455.14,169.05) .. (454.43,208.29) .. controls (436.92,201.17) and (404.64,192.06) .. (392.78,184.47) .. controls (388.45,181.7) and (409.12,177.62) .. (402.59,176.06) .. controls (361.93,166.35) and (299.69,170.63) .. (255.46,169.05) .. controls (261.77,159.25) and (271.58,171.16) .. (299.6,157.14) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.26 ][fill={rgb, 255:red, 142; green, 141; blue, 129 }  ,fill opacity=1 ] (305.91,162.05) .. controls (310.86,159.57) and (318.6,167.96) .. (329.73,164.85) .. controls (333.73,164.25) and (347.12,159.23) .. (360.55,144.53) .. controls (368.31,142.49) and (382.2,164.51) .. (390.68,162.75) .. controls (400.67,160.68) and (398.8,172.15) .. (407.49,169.05) .. controls (421.51,172.56) and (444.85,152.24) .. (454.53,151.47) .. controls (454.53,182.99) and (453.03,171.16) .. (454.43,208.29) .. controls (436.92,201.17) and (405.47,192.07) .. (393.61,184.49) .. controls (389.28,181.72) and (409.94,177.64) .. (403.41,176.08) .. controls (362.75,166.37) and (300.51,170.65) .. (256.29,169.07) .. controls (262.59,159.26) and (277.88,176.06) .. (305.91,162.05) -- cycle ;
            	\draw  [fill={rgb, 255:red, 111; green, 109; blue, 83 }  ,fill opacity=1 ] (399.1,204.11) -- (349.77,243.88) -- (335.05,237.57) -- (318.24,234.07) -- (325.94,220.76) -- (326.65,209.55) -- (329.29,199.66) -- (345.15,201.31) -- (363.36,199.91) -- (380.18,202.01) -- cycle ;
            	\draw  [fill={rgb, 255:red, 111; green, 109; blue, 83 }  ,fill opacity=1 ] (423.33,220.2) -- (368.68,263.64) -- (355.37,253.69) -- (343.46,251.59) -- (337.15,248.78) -- (346.96,234.35) -- (353.27,227.34) -- (353.53,215.74) -- (369.38,217.4) -- (387.6,215.99) -- (404.41,218.1) -- cycle ;
            	\draw  [fill={rgb, 255:red, 111; green, 109; blue, 83 }  ,fill opacity=1 ] (454.86,236.31) -- (454.43,270.97) -- (321.74,269.94) -- (360.97,260.13) -- (372.88,246.12) -- (379.89,243.32) -- (385.05,231.86) -- (400.91,233.51) -- (419.12,232.11) -- (435.94,234.21) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 150; green, 149; blue, 130 }  ,fill opacity=1 ] (383.39,270.64) -- (374.29,269.24) -- (400.21,253.13) -- (383.56,256.69) -- (388.3,246.12) -- (368.68,263.64) -- (321.74,269.94) -- (360.97,260.13) -- (372.88,246.12) -- (379.89,243.32) -- (385.05,231.86) -- (400.91,233.51) -- (419.12,232.11) -- (401.61,259.43) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 150; green, 149; blue, 130 }  ,fill opacity=1 ] (445.05,248.22) -- (435.94,265.04) -- (439.44,248.22) -- (435.94,234.21) -- (447.15,234.91) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 150; green, 149; blue, 130 }  ,fill opacity=1 ] (353.27,248.08) -- (343.46,251.59) -- (337.15,248.78) -- (353.27,227.34) -- (353.53,215.74) -- (363.78,216.7) -- (372.14,224.55) -- (365.18,243.18) -- (360.97,235.47) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 150; green, 149; blue, 130 }  ,fill opacity=1 ] (329.04,232) -- (321.74,234.77) -- (329.04,211.26) -- (328.05,206.05) -- (336.45,210.25) -- (347.66,217.26) -- (336.45,231.27) -- (336.74,219.39) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ][fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (355.37,188.67) .. controls (370.78,187.97) and (373.59,188.67) .. (395.31,182.13) .. controls (405.57,182.33) and (415.12,180.61) .. (422.63,174.58) .. controls (433.5,174.89) and (444.56,174.19) .. (455.56,171.58) .. controls (455.56,205.49) and (455.56,211.79) .. (454.86,236.31) .. controls (437.34,234.91) and (445.75,237.01) .. (419.12,232.11) .. controls (407.21,235.61) and (392.97,232.51) .. (385.05,231.86) .. controls (387.77,228.82) and (394.31,226.26) .. (406.05,224.56) .. controls (395.39,221.4) and (383.87,220.71) .. (372.14,224.55) .. controls (369.18,221.94) and (366.38,219.32) .. (363.78,216.7) .. controls (353.97,216.7) and (343.82,215.49) .. (341.36,211.79) .. controls (328.75,203.38) and (333.65,212.49) .. (329.29,199.66) .. controls (337.15,195.68) and (347.66,194.28) .. (355.37,188.67) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.62 ]   (348.36,260.69) .. controls (350.41,257.96) and (314.74,265.6) .. (327.4,253.1) .. controls (340.06,240.6) and (287.41,243.88) .. (314.03,227.06) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (105.35,133.93) .. controls (108.67,133.41) and (110.27,133.67) .. (110.01,137.78) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (109.99,136.34) .. controls (113.3,135.82) and (114.91,136.08) .. (114.64,140.19) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (143.96,144.45) .. controls (146.81,142.67) and (148.38,142.28) .. (149.75,146.16) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (149.17,144.85) .. controls (152.02,143.07) and (153.59,142.67) .. (154.96,146.56) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (97.03,154.69) .. controls (97.8,152.16) and (98.55,151.19) .. (101.46,153.39) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (100.4,152.7) .. controls (101.18,150.17) and (101.92,149.2) .. (104.83,151.4) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (122.93,123.12) .. controls (124.2,121.85) and (124.92,121.58) .. (125.58,124.43) ;
            	\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ]   (125.3,123.46) .. controls (126.58,122.19) and (127.29,121.92) .. (127.95,124.78) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.24 ] (365.47,202.99) .. controls (365.47,200.29) and (380.52,198.11) .. (399.1,198.11) .. controls (417.67,198.11) and (432.72,200.29) .. (432.72,202.99) .. controls (432.72,205.68) and (417.67,207.87) .. (399.1,207.87) .. controls (380.52,207.87) and (365.47,205.68) .. (365.47,202.99) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (361.96,207.5) -- (366.95,95.41) -- (386.94,95.41) -- (391.94,207.5) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (363.08,184.86) -- (364.48,161.82) -- (389.14,161.82) -- (390.54,184.86) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (364.76,138.9) -- (366.16,115.86) -- (387.46,115.86) -- (388.86,138.9) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ] (368.4,64.58) -- (385.5,64.58) -- (385.5,81.96) -- (368.4,81.96) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (377.88,47.77) -- (388.3,61.78) -- (365.6,61.78) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (365.6,61.78) -- (388.3,61.78) -- (388.3,64.58) -- (365.6,64.58) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (375.24,46.95) .. controls (375.24,47.4) and (375.61,47.77) .. (376.06,47.77) -- (378.51,47.77) .. controls (378.96,47.77) and (379.33,47.4) .. (379.33,46.95) -- (379.33,44.42) .. controls (379.33,43.97) and (378.96,43.6) .. (378.51,43.6) -- (376.06,43.6) .. controls (375.61,43.6) and (375.24,43.97) .. (375.24,44.42) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ]   (377.46,43.6) -- (377.46,34.26) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ]   (372.32,64.92) -- (372.6,81.68) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ]   (381.57,64.36) -- (381.85,81.11) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (366.95,76.07) -- (386.94,76.07) -- (386.94,95.41) -- (366.95,95.41) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (390.26,92.88) -- (387.68,99.33) -- (366.64,99.33) -- (364.06,92.88) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (364.06,89.24) -- (390.26,89.24) -- (390.26,92.88) -- (364.06,92.88) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ] (364.06,89.24) -- (390.82,89.24) -- (390.82,81.11) -- (364.06,81.11) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ] (371.34,89.24) -- (383.53,89.24) -- (383.53,81.11) -- (371.34,81.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (387.68,99.33) -- (391.94,207.5) -- (385.08,207.17) -- (385.08,207.17) -- (382.97,103.48) -- (372.46,99.27) -- (364.98,87.64) -- (383.53,89.24) -- (381.57,76.15) -- (386.94,76.07) -- (390.26,89.24) -- (390.26,89.24) -- (390.26,92.88) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (368.68,197.45) .. controls (368.68,195.85) and (369.98,194.56) .. (371.58,194.56) -- (371.67,194.56) .. controls (373.27,194.56) and (374.57,195.85) .. (374.57,197.45) -- (374.57,205.07) .. controls (374.57,205.07) and (374.57,205.07) .. (374.57,205.07) -- (368.68,205.07) .. controls (368.68,205.07) and (368.68,205.07) .. (368.68,205.07) -- cycle ;
            	\draw  [dash pattern={on 4.5pt off 4.5pt}]  (117.87,208.57) -- (361.96,207.5) ;
            	\draw  [dash pattern={on 4.5pt off 4.5pt}]  (117.87,208.57) -- (365.6,61.78) ;
            	\draw  [dash pattern={on 4.5pt off 4.5pt}]  (252.38,207.87) -- (365.6,61.78) ;
            	\draw    (402.31,66.54) -- (402.31,203.61) ;
            	\draw [shift={(402.31,206.61)}, rotate = 270] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            	\draw [shift={(402.31,63.54)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            	\draw    (397.41,63.68) -- (407.91,63.54) ;
            	\draw    (397.41,205.91) -- (407.91,205.77) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (100.55,194.88) -- (110.15,194.88) -- (110.15,207) -- (100.55,207) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (78.24,204.85) .. controls (78.24,203.53) and (79.31,202.45) .. (80.64,202.45) -- (88.44,202.45) -- (88.44,207.25) -- (78.24,207.25) -- cycle ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (77.48,209.07) -- (110.9,209.27) -- (113.93,205.73) -- (97.53,207) -- (76.57,207) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (76.57,207) -- (97.53,207) -- (113.93,205.73) -- (117.21,200.43) -- (99.8,203.72) -- (74.81,205.23) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (99.8,195.13) -- (110.9,195.13) -- (110.9,192.86) -- (99.8,192.86) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (103.84,199.68) -- (108.63,199.68) -- (108.63,197.91) -- (103.84,197.91) -- cycle ;
            	\draw [line width=1.5]    (96.92,204.02) -- (96.26,174.94) ;
            	\draw [line width=1.5]    (96.92,204.02) -- (78.09,187.81) ;
            	\draw    (96.92,178.02) -- (117.21,200.43) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (107.65,205.51) .. controls (107.65,204.69) and (108.31,204.02) .. (109.14,204.02) .. controls (109.96,204.02) and (110.63,204.69) .. (110.63,205.51) .. controls (110.63,206.33) and (109.96,207) .. (109.14,207) .. controls (108.31,207) and (107.65,206.33) .. (107.65,205.51) -- cycle ;
            	\draw    (96.92,178.02) -- (99.8,203.72) ;
            	\draw    (96.92,178.02) -- (93.49,204.22) ;
            	\draw    (79.76,189.13) -- (76.57,204.98) ;
            	\draw    (79.76,189.13) -- (78.24,204.85) ;
            	\draw    (96.92,178.02) -- (79.76,189.13) ;
            	\draw    (96.92,178.02) -- (80.61,190.59) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (236.57,196.17) -- (245.28,196.17) -- (245.28,207.17) -- (236.57,207.17) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (216.32,205.22) .. controls (216.32,204.02) and (217.29,203.05) .. (218.49,203.05) -- (225.57,203.05) -- (225.57,207.4) -- (216.32,207.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (215.63,209.05) -- (245.97,209.23) -- (248.72,206.02) -- (233.82,207.17) -- (214.8,207.17) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (214.8,207.17) -- (233.82,207.17) -- (248.72,206.02) -- (251.7,201.21) -- (235.89,204.19) -- (213.2,205.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (235.89,196.4) -- (245.97,196.4) -- (245.97,194.34) -- (235.89,194.34) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (239.55,200.52) -- (243.91,200.52) -- (243.91,198.92) -- (239.55,198.92) -- cycle ;
            	\draw [line width=1.5]    (233.27,204.47) -- (232.68,178.07) ;
            	\draw [line width=1.5]    (233.27,204.47) -- (216.18,189.75) ;
            	\draw    (233.27,180.86) -- (251.7,201.21) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (243.01,205.82) .. controls (243.01,205.07) and (243.62,204.47) .. (244.37,204.47) .. controls (245.11,204.47) and (245.72,205.07) .. (245.72,205.82) .. controls (245.72,206.57) and (245.11,207.17) .. (244.37,207.17) .. controls (243.62,207.17) and (243.01,206.57) .. (243.01,205.82) -- cycle ;
            	\draw    (233.27,180.86) -- (235.89,204.19) ;
            	\draw    (233.27,180.86) -- (230.16,204.65) ;
            	\draw    (217.69,190.95) -- (214.8,205.34) ;
            	\draw    (217.69,190.95) -- (216.32,205.22) ;
            	\draw    (233.27,180.86) -- (217.69,190.95) ;
            	\draw    (233.27,180.86) -- (218.47,192.27) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.23 ] (56.2,169.75) .. controls (77.87,171.47) and (205.87,166.8) .. (231.87,171.47) .. controls (267.2,182.8) and (185.82,176.5) .. (169.2,182.13) .. controls (152.58,187.76) and (213.65,182.38) .. (209.2,193.47) .. controls (204.75,204.56) and (173.35,196.69) .. (161.2,203.47) .. controls (149.05,210.24) and (303.2,209.47) .. (307.2,214.13) .. controls (311.2,218.8) and (326.54,225.37) .. (275.87,232.8) .. controls (225.19,240.23) and (301.75,249.37) .. (274.53,250.8) .. controls (247.31,252.23) and (149.46,260.11) .. (99.2,256.13) .. controls (48.94,252.16) and (143.12,237.35) .. (139.2,231.47) .. controls (135.28,225.58) and (70.77,235.05) .. (56.2,220.71) .. controls (55.87,206.13) and (56.53,187.47) .. (56.2,169.75) -- cycle ;
            	\draw [color={rgb, 255:red, 62; green, 137; blue, 120 }  ,draw opacity=0.67 ]   (83.35,211.01) .. controls (92.03,204.51) and (96.36,217.52) .. (105.04,211.01) ;
            	\draw [color={rgb, 255:red, 62; green, 137; blue, 120 }  ,draw opacity=0.67 ]   (88.84,211.16) .. controls (97.52,204.65) and (101.86,217.67) .. (110.53,211.16) ;
            	\draw [color={rgb, 255:red, 62; green, 137; blue, 120 }  ,draw opacity=0.67 ]   (78,211.45) .. controls (86.68,204.94) and (91.01,217.96) .. (99.69,211.45) ;
            	\draw [color={rgb, 255:red, 62; green, 137; blue, 120 }  ,draw opacity=0.67 ]   (219.68,211.35) .. controls (228.36,204.84) and (232.7,217.85) .. (241.37,211.35) ;
            	\draw [color={rgb, 255:red, 62; green, 137; blue, 120 }  ,draw opacity=0.67 ]   (225.18,211.49) .. controls (233.85,204.99) and (238.19,218) .. (246.87,211.49) ;
            	\draw [color={rgb, 255:red, 62; green, 137; blue, 120 }  ,draw opacity=0.67 ]   (214.33,211.78) .. controls (223.01,205.28) and (227.35,218.29) .. (236.02,211.78) ;
            	\draw (348,42.67) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (365.47,205) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (109.14,211) node [anchor=north west][inner sep=0.75pt]    {$P$};
            	\draw (244.37,211) node [anchor=north west][inner sep=0.75pt]    {$Q$};
            	\draw (403.33,119.33) node [anchor=north west][inner sep=0.75pt]    {$h$};
            \end{tikzpicture} }'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Hai con thuyền ở hai vị trí $P$ và $Q$ cách nhau $%s$ m và thẳng hàng với chân $B$ của tháp hải đăng trên bờ biển. Từ $P$ và $Q$, người ta nhìn thấy ngọn của tháp hải đăng lần lượt dưới $\widehat{BPA} = %s^\circ$ và $\widehat{BQA} = %s^\circ$. Chiều cao của tháp hải đăng là bao nhiêu mét? (Kết quả làm tròn đến hàng đơn vị).}{%s}'''
                                 %(latex(d), latex(alpha), latex(beta),hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $A$ là ngọn tháp hải đăng, $B$ là chân tháp hải đăng. Chiều cao của tháp là $h = AB$. \\\\
                            Xét tam giác vuông $ABP$ vuông tại $B$, ta có: $PB = \\frac{AB}{\\tan \\widehat{BPA}} = h \\cdot \\cot %s^\\circ$. \\\\
                            Xét tam giác vuông $ABQ$ vuông tại $B$, ta có: $QB = \\frac{AB}{\\tan \\widehat{BQA}} = h \\cdot \\cot %s^\\circ$. \\\\
                            Do $\\widehat{BPA} < \\widehat{BQA}$ nên $PB > QB$, do đó điểm $Q$ nằm giữa $B$ và $P$. \\\\
                            Ta có khoảng cách giữa hai con thuyền là $PQ = PB - QB$. \\\\
                            Suy ra $PQ = h \\cdot \\cot %s^\\circ - h \\cdot \\cot %s^\\circ = h (\\cot %s^\\circ - \\cot %s^\\circ)$. \\\\
                            $\\Rightarrow h = \\frac{PQ}{\\cot %s^\\circ - \\cot %s^\\circ} = \\frac{%s}{\\cot %s^\\circ - \\cot %s^\\circ} \\approx %s$ (m).'''
                           %(latex(alpha), latex(beta), latex(alpha), latex(beta), latex(alpha), latex(beta), latex(alpha), latex(beta), latex(d), latex(alpha), latex(beta), latex(kq_num)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

