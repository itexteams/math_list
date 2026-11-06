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


def bt_dang19_p3_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các giả thiết: khoảng cách CD, chiều cao giác kế OC, góc ngắm AOB
                cd = random.randint(30, 90)
                oc = random.randint(1, 2)
                angle = random.choice([30, 45, 60])

                # Tính toán giá trị lượng giác chính xác để hiển thị vào lời giải bằng sympy
                if angle == 30:
                    tan_val_tex = r"\frac{\sqrt{3}}{3}"
                    ab_sym = cd * sp.sqrt(3) / 3
                elif angle == 45:
                    tan_val_tex = "1"
                    ab_sym = cd * 1
                else: # 60
                    tan_val_tex = r"\sqrt{3}"
                    ab_sym = cd * sp.sqrt(3)

                ab_tex = latex(ab_sym)

                # Tính toán kết quả gần đúng
                ab_float = cd * math.tan(math.radians(angle))
                h_float = ab_float + oc

                # Làm tròn đến hàng đơn vị theo yêu cầu đề bài
                kq_dec = Decimal(float(h_float)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq_int = int(kq_dec)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq_int)]
                da = random.choice(du)

                # Sinh các đáp án sai lệch nhau ngẫu nhiên
                s = [
                    '$%s$' % (kq_int + random.randint(1, 3)),
                    '$%s$' % (kq_int + random.randint(4, 7)),
                    '$%s$' % (kq_int + random.randint(8, 12)),
                    '$%s$' % (kq_int - random.randint(1, 3)),
                    '$%s$' % (kq_int - random.randint(4, 7)),
                    '$%s$' % (kq_int - random.randint(8, 12))
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{center} \scalebox{0.7}{ 
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\tikzset {_6hjavha3n/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_v0vxn52ee}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            			rgb(45.42857033865792bp)=(0.61,0.61,0.61);
            			rgb(50bp)=(1,1,1);
            			rgb(55.96428462437221bp)=(0.5,0.5,0.5);
            			rgb(100bp)=(0.5,0.5,0.5)}
            		\tikzset {_pyep8eg47/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_4r0wjynlz}{150bp}{rgb(0bp)=(0,0.5,0);
            			rgb(37.5bp)=(0,0.5,0);
            			rgb(37.5bp)=(0.82,0.01,0.11);
            			rgb(46.4810289655413bp)=(1,1,1);
            			rgb(62.5bp)=(0.82,0.01,0.11);
            			rgb(100bp)=(0.82,0.01,0.11)}
            		\tikzset {_jn48095e6/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_eckqezn65}{150bp}{rgb(0bp)=(0,0.5,0);
            			rgb(37.5bp)=(0,0.5,0);
            			rgb(37.5bp)=(0.82,0.01,0.11);
            			rgb(46.4810289655413bp)=(1,1,1);
            			rgb(62.5bp)=(0.82,0.01,0.11);
            			rgb(100bp)=(0.82,0.01,0.11)}
            		\tikzset {_in8s4ht11/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_sl1y1bh3r}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            			rgb(43.981023515973774bp)=(0.61,0.61,0.61);
            			rgb(49.33816637311663bp)=(1,1,1);
            			rgb(55.69642748151507bp)=(0.5,0.5,0.5);
            			rgb(100bp)=(0.5,0.5,0.5)}
            		\tikzset {_za1spe3ho/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_i7iu5kxob}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            			rgb(43.981023515973774bp)=(0.61,0.61,0.61);
            			rgb(49.33816637311663bp)=(1,1,1);
            			rgb(55.69642748151507bp)=(0.5,0.5,0.5);
            			rgb(100bp)=(0.5,0.5,0.5)}
            		\tikzset {_u6ti8hlvc/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_a95fcgctk}{150bp}{rgb(0bp)=(0.82,0.01,0.11);
            			rgb(37.571427481515066bp)=(0.82,0.01,0.11);
            			rgb(45.517856052943635bp)=(0.93,0.9,0.9);
            			rgb(62.5bp)=(0.82,0.01,0.11);
            			rgb(100bp)=(0.82,0.01,0.11)}
            		\tikzset {_qep3w0bv7/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-42 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_zl76pi2s0}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            			rgb(46.729910714285715bp)=(0.61,0.61,0.61);
            			rgb(49.33816637311663bp)=(1,1,1);
            			rgb(50.49888065883091bp)=(0.5,0.5,0.5);
            			rgb(100bp)=(0.5,0.5,0.5)}
            		\tikzset {_hi1rvrb2b/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-138 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_hiu89ra55}{150bp}{rgb(0bp)=(0.61,0.61,0.61);
            			rgb(46.729910714285715bp)=(0.61,0.61,0.61);
            			rgb(49.33816637311663bp)=(1,1,1);
            			rgb(50.49888065883091bp)=(0.5,0.5,0.5);
            			rgb(100bp)=(0.5,0.5,0.5)}
            		\tikzset {_xegrypfxy/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_sh2nemfy7}{150bp}{rgb(0bp)=(0.82,0.01,0.11);
            			rgb(45.42857033865792bp)=(0.82,0.01,0.11);
            			rgb(50bp)=(1,1,1);
            			rgb(56.12388610839844bp)=(0.82,0.01,0.11);
            			rgb(100bp)=(0.82,0.01,0.11)}
            		\tikzset{every picture/.style={line width=0.75pt}} 
            		\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (238.17,276.1) .. controls (237.86,274.51) and (238.88,272.93) .. (240.8,272.04) .. controls (242.71,271.15) and (245.19,271.1) .. (247.17,271.91) .. controls (247.88,270.99) and (249.17,270.35) .. (250.65,270.19) .. controls (252.13,270.03) and (253.63,270.37) .. (254.7,271.1) .. controls (255.3,270.26) and (256.48,269.7) .. (257.82,269.61) .. controls (259.15,269.52) and (260.46,269.92) .. (261.27,270.67) .. controls (262.36,269.78) and (264.08,269.4) .. (265.7,269.71) .. controls (267.31,270.01) and (268.54,270.93) .. (268.83,272.08) .. controls (270.16,272.33) and (271.26,272.98) .. (271.86,273.84) .. controls (272.46,274.71) and (272.49,275.71) .. (271.95,276.59) .. controls (273.26,277.78) and (273.56,279.36) .. (272.75,280.75) .. controls (271.94,282.13) and (270.14,283.11) .. (268.02,283.33) .. controls (268,284.63) and (266.98,285.82) .. (265.35,286.45) .. controls (263.71,287.07) and (261.72,287.03) .. (260.14,286.34) .. controls (259.46,287.9) and (257.57,289.05) .. (255.26,289.29) .. controls (252.96,289.53) and (250.67,288.82) .. (249.38,287.46) .. controls (247.8,288.13) and (245.89,288.32) .. (244.1,288) .. controls (242.32,287.67) and (240.79,286.85) .. (239.87,285.73) .. controls (238.25,285.86) and (236.69,285.28) .. (235.95,284.27) .. controls (235.22,283.25) and (235.47,282.03) .. (236.58,281.2) .. controls (235.14,280.61) and (234.4,279.43) .. (234.75,278.28) .. controls (235.11,277.14) and (236.48,276.28) .. (238.14,276.16) ; \draw  [draw opacity=0] (236.58,281.2) .. controls (237.26,281.48) and (238.05,281.61) .. (238.84,281.56)(239.87,285.73) .. controls (240.21,285.7) and (240.54,285.65) .. (240.86,285.56)(249.38,287.46) .. controls (249.14,287.21) and (248.94,286.95) .. (248.78,286.67)(260.14,286.34) .. controls (260.26,286.06) and (260.34,285.77) .. (260.37,285.47)(268.02,283.33) .. controls (268.03,281.94) and (266.91,280.67) .. (265.12,280.07)(271.95,276.59) .. controls (271.66,277.07) and (271.22,277.48) .. (270.66,277.82)(268.83,272.08) .. controls (268.88,272.27) and (268.9,272.47) .. (268.9,272.66)(261.27,270.67) .. controls (261,270.89) and (260.78,271.14) .. (260.61,271.4)(254.7,271.1) .. controls (254.56,271.3) and (254.45,271.52) .. (254.38,271.74)(247.17,271.91) .. controls (247.59,272.08) and (247.98,272.29) .. (248.33,272.53)(238.17,276.1) .. controls (238.22,276.32) and (238.28,276.53) .. (238.38,276.74) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (198.11,271.87) .. controls (197.74,270.17) and (198.97,268.49) .. (201.29,267.54) .. controls (203.61,266.59) and (206.61,266.53) .. (209.01,267.4) .. controls (209.87,266.41) and (211.43,265.73) .. (213.22,265.56) .. controls (215.02,265.39) and (216.84,265.75) .. (218.13,266.54) .. controls (218.86,265.64) and (220.28,265.04) .. (221.9,264.95) .. controls (223.52,264.85) and (225.1,265.28) .. (226.09,266.07) .. controls (227.4,265.13) and (229.49,264.73) .. (231.45,265.05) .. controls (233.41,265.37) and (234.88,266.36) .. (235.24,267.58) .. controls (236.85,267.85) and (238.19,268.54) .. (238.91,269.46) .. controls (239.64,270.39) and (239.68,271.46) .. (239.02,272.4) .. controls (240.6,273.67) and (240.97,275.36) .. (239.99,276.83) .. controls (239.01,278.31) and (236.83,279.36) .. (234.26,279.59) .. controls (234.24,280.98) and (233,282.25) .. (231.02,282.92) .. controls (229.04,283.59) and (226.63,283.54) .. (224.71,282.81) .. controls (223.9,284.47) and (221.6,285.7) .. (218.81,285.95) .. controls (216.03,286.21) and (213.25,285.45) .. (211.69,284) .. controls (209.77,284.72) and (207.46,284.92) .. (205.3,284.57) .. controls (203.13,284.23) and (201.28,283.35) .. (200.17,282.15) .. controls (198.21,282.3) and (196.31,281.67) .. (195.42,280.59) .. controls (194.53,279.51) and (194.84,278.2) .. (196.19,277.32) .. controls (194.44,276.68) and (193.54,275.43) .. (193.97,274.2) .. controls (194.4,272.98) and (196.06,272.06) .. (198.07,271.93) ; \draw  [draw opacity=0] (196.19,277.32) .. controls (197.01,277.62) and (197.97,277.75) .. (198.92,277.71)(200.17,282.15) .. controls (200.58,282.13) and (200.98,282.06) .. (201.36,281.97)(211.69,284) .. controls (211.4,283.74) and (211.15,283.45) .. (210.96,283.16)(224.71,282.81) .. controls (224.86,282.51) and (224.96,282.19) .. (225,281.88)(234.26,279.59) .. controls (234.28,278.11) and (232.91,276.76) .. (230.75,276.11)(239.02,272.4) .. controls (238.67,272.9) and (238.14,273.35) .. (237.46,273.7)(235.24,267.58) .. controls (235.3,267.79) and (235.33,267.99) .. (235.33,268.2)(226.09,266.07) .. controls (225.76,266.31) and (225.49,266.58) .. (225.29,266.86)(218.13,266.54) .. controls (217.96,266.75) and (217.83,266.98) .. (217.74,267.22)(209.01,267.4) .. controls (209.52,267.58) and (209.99,267.8) .. (210.42,268.06)(198.11,271.87) .. controls (198.16,272.1) and (198.25,272.33) .. (198.36,272.56) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (100.93,274.27) .. controls (100.52,272.62) and (101.86,270.99) .. (104.37,270.06) .. controls (106.88,269.14) and (110.13,269.09) .. (112.74,269.93) .. controls (113.66,268.97) and (115.35,268.31) .. (117.29,268.14) .. controls (119.24,267.98) and (121.21,268.33) .. (122.61,269.09) .. controls (123.4,268.22) and (124.94,267.64) .. (126.69,267.55) .. controls (128.45,267.45) and (130.16,267.87) .. (131.23,268.64) .. controls (132.65,267.72) and (134.91,267.33) .. (137.03,267.64) .. controls (139.15,267.96) and (140.75,268.92) .. (141.14,270.11) .. controls (142.88,270.37) and (144.33,271.04) .. (145.11,271.93) .. controls (145.9,272.83) and (145.94,273.87) .. (145.23,274.79) .. controls (146.94,276.02) and (147.34,277.66) .. (146.28,279.1) .. controls (145.22,280.53) and (142.86,281.55) .. (140.07,281.77) .. controls (140.05,283.12) and (138.71,284.36) .. (136.57,285.01) .. controls (134.42,285.65) and (131.81,285.61) .. (129.74,284.9) .. controls (128.85,286.52) and (126.36,287.7) .. (123.35,287.95) .. controls (120.33,288.2) and (117.32,287.46) .. (115.63,286.06) .. controls (113.55,286.75) and (111.06,286.95) .. (108.71,286.61) .. controls (106.36,286.28) and (104.36,285.43) .. (103.16,284.26) .. controls (101.03,284.4) and (98.98,283.79) .. (98.02,282.74) .. controls (97.05,281.69) and (97.38,280.42) .. (98.84,279.57) .. controls (96.95,278.95) and (95.98,277.73) .. (96.45,276.54) .. controls (96.91,275.35) and (98.71,274.46) .. (100.89,274.34) ; \draw  [draw opacity=0] (98.85,279.57) .. controls (99.74,279.86) and (100.77,279.99) .. (101.8,279.94)(103.16,284.26) .. controls (103.6,284.24) and (104.04,284.17) .. (104.45,284.08)(115.63,286.06) .. controls (115.32,285.8) and (115.05,285.53) .. (114.85,285.24)(129.74,284.9) .. controls (129.9,284.61) and (130,284.3) .. (130.05,284)(140.07,281.77) .. controls (140.09,280.33) and (138.62,279.02) .. (136.27,278.39)(145.23,274.79) .. controls (144.85,275.28) and (144.27,275.71) .. (143.54,276.06)(141.14,270.11) .. controls (141.2,270.3) and (141.23,270.51) .. (141.23,270.71)(131.23,268.64) .. controls (130.87,268.87) and (130.58,269.13) .. (130.36,269.4)(122.61,269.09) .. controls (122.42,269.3) and (122.28,269.52) .. (122.19,269.75)(112.74,269.93) .. controls (113.29,270.11) and (113.8,270.32) .. (114.25,270.57)(100.93,274.27) .. controls (100.99,274.5) and (101.08,274.72) .. (101.2,274.94) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (55.93,274.41) .. controls (55.52,272.75) and (56.86,271.12) .. (59.37,270.2) .. controls (61.88,269.27) and (65.13,269.22) .. (67.74,270.06) .. controls (68.66,269.1) and (70.35,268.44) .. (72.29,268.28) .. controls (74.24,268.11) and (76.21,268.46) .. (77.61,269.23) .. controls (78.4,268.36) and (79.94,267.77) .. (81.69,267.68) .. controls (83.45,267.59) and (85.16,268) .. (86.23,268.78) .. controls (87.65,267.85) and (89.91,267.46) .. (92.03,267.78) .. controls (94.15,268.09) and (95.75,269.05) .. (96.14,270.24) .. controls (97.88,270.5) and (99.33,271.17) .. (100.11,272.07) .. controls (100.9,272.96) and (100.94,274.01) .. (100.23,274.92) .. controls (101.94,276.15) and (102.34,277.79) .. (101.28,279.23) .. controls (100.22,280.67) and (97.86,281.68) .. (95.07,281.9) .. controls (95.05,283.25) and (93.71,284.49) .. (91.57,285.14) .. controls (89.42,285.79) and (86.81,285.75) .. (84.74,285.03) .. controls (83.85,286.65) and (81.36,287.84) .. (78.35,288.09) .. controls (75.33,288.33) and (72.32,287.6) .. (70.63,286.19) .. controls (68.55,286.89) and (66.06,287.09) .. (63.71,286.75) .. controls (61.36,286.41) and (59.36,285.56) .. (58.16,284.4) .. controls (56.03,284.53) and (53.98,283.93) .. (53.02,282.88) .. controls (52.05,281.83) and (52.38,280.56) .. (53.84,279.7) .. controls (51.95,279.08) and (50.98,277.86) .. (51.45,276.67) .. controls (51.91,275.48) and (53.71,274.59) .. (55.89,274.47) ; \draw  [draw opacity=0] (53.85,279.7) .. controls (54.74,279.99) and (55.77,280.12) .. (56.8,280.08)(58.16,284.4) .. controls (58.6,284.37) and (59.04,284.31) .. (59.45,284.22)(70.63,286.19) .. controls (70.32,285.94) and (70.05,285.66) .. (69.85,285.37)(84.74,285.03) .. controls (84.9,284.74) and (85,284.44) .. (85.05,284.13)(95.07,281.9) .. controls (95.09,280.47) and (93.62,279.15) .. (91.27,278.52)(100.23,274.92) .. controls (99.85,275.41) and (99.27,275.84) .. (98.54,276.19)(96.14,270.24) .. controls (96.2,270.44) and (96.23,270.64) .. (96.23,270.84)(86.23,268.78) .. controls (85.87,269.01) and (85.58,269.26) .. (85.36,269.54)(77.61,269.23) .. controls (77.42,269.43) and (77.28,269.66) .. (77.19,269.88)(67.74,270.06) .. controls (68.29,270.24) and (68.8,270.46) .. (69.25,270.7)(55.93,274.41) .. controls (55.99,274.63) and (56.08,274.86) .. (56.2,275.08) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 225; green, 202; blue, 162 }  ,fill opacity=1 ] (50.03,272.87) -- (567.87,272.87) -- (567.87,295.8) -- (50.03,295.8) -- cycle ;
            		\path  [shading=_v0vxn52ee,_6hjavha3n] (150.6,70.96) -- (153.6,56.53) -- (157.6,56.53) -- (160.6,70.96) -- cycle ; 
            		\draw   (150.6,70.96) -- (153.6,56.53) -- (157.6,56.53) -- (160.6,70.96) -- cycle ; 
            		\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (148.5,70.96) .. controls (148.5,68.85) and (150.21,67.13) .. (152.33,67.13) -- (160.27,67.13) .. controls (162.39,67.13) and (164.1,68.85) .. (164.1,70.96) -- (164.1,75.93) .. controls (164.1,75.93) and (164.1,75.93) .. (164.1,75.93) -- (148.5,75.93) .. controls (148.5,75.93) and (148.5,75.93) .. (148.5,75.93) -- cycle ;
            		\path  [shading=_4r0wjynlz,_pyep8eg47] (143.5,79.52) -- (143.5,72.94) .. controls (143.5,72.16) and (149.23,71.53) .. (156.3,71.53) .. controls (163.37,71.53) and (169.1,72.16) .. (169.1,72.94) -- (169.1,79.52) .. controls (169.1,80.3) and (163.37,80.93) .. (156.3,80.93) .. controls (149.23,80.93) and (143.5,80.3) .. (143.5,79.52) .. controls (143.5,78.74) and (149.23,78.11) .. (156.3,78.11) .. controls (163.37,78.11) and (169.1,78.74) .. (169.1,79.52) ; 
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ] (143.5,79.52) -- (143.5,72.94) .. controls (143.5,72.16) and (149.23,71.53) .. (156.3,71.53) .. controls (163.37,71.53) and (169.1,72.16) .. (169.1,72.94) -- (169.1,79.52) .. controls (169.1,80.3) and (163.37,80.93) .. (156.3,80.93) .. controls (149.23,80.93) and (143.5,80.3) .. (143.5,79.52) .. controls (143.5,78.74) and (149.23,78.11) .. (156.3,78.11) .. controls (163.37,78.11) and (169.1,78.74) .. (169.1,79.52) ; 
            		\path  [shading=_eckqezn65,_jn48095e6] (145,79.61) .. controls (145,78.88) and (150.06,78.29) .. (156.3,78.29) .. controls (162.54,78.29) and (167.6,78.88) .. (167.6,79.61) .. controls (167.6,80.34) and (162.54,80.93) .. (156.3,80.93) .. controls (150.06,80.93) and (145,80.34) .. (145,79.61) -- cycle ; 
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.55 ] (145,79.61) .. controls (145,78.88) and (150.06,78.29) .. (156.3,78.29) .. controls (162.54,78.29) and (167.6,78.88) .. (167.6,79.61) .. controls (167.6,80.34) and (162.54,80.93) .. (156.3,80.93) .. controls (150.06,80.93) and (145,80.34) .. (145,79.61) -- cycle ; 
            		\path  [shading=_sl1y1bh3r,_in8s4ht11] (154.1,80.53) -- (158.1,80.53) -- (158.1,199.83) -- (154.1,199.83) -- cycle ; 
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.49 ] (154.1,80.53) -- (158.1,80.53) -- (158.1,199.83) -- (154.1,199.83) -- cycle ; 
            		\draw [color={rgb, 255:red, 200; green, 192; blue, 192 }  ,draw opacity=1 ][line width=2.25]    (141.1,178.53) -- (139.23,194.56) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=2.25]    (142.6,161.53) -- (141.1,178.53) ;
            		\draw [color={rgb, 255:red, 200; green, 192; blue, 192 }  ,draw opacity=1 ][line width=2.25]    (145.1,127.53) -- (142.6,161.53) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=2.25]    (148.6,80.53) -- (145.1,127.53) ;
            		\draw [color={rgb, 255:red, 200; green, 192; blue, 192 }  ,draw opacity=1 ][line width=2.25]    (172.52,177.92) -- (173.36,194.04) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=2.25]    (171.14,160.91) -- (172.52,177.92) ;
            		\draw [color={rgb, 255:red, 200; green, 192; blue, 192 }  ,draw opacity=1 ][line width=2.25]    (167.9,126.98) -- (171.14,160.91) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=2.25]    (163.47,80.06) -- (167.9,126.98) ;
            		\draw [color={rgb, 255:red, 200; green, 192; blue, 192 }  ,draw opacity=1 ][line width=2.25]    (172.52,177.92) -- (139.23,194.56) ;
            		\draw [color={rgb, 255:red, 200; green, 192; blue, 192 }  ,draw opacity=1 ][line width=2.25]    (141.1,178.53) -- (173.36,194.04) ;
            		\draw [color={rgb, 255:red, 200; green, 192; blue, 192 }  ,draw opacity=1 ][line width=2.25]    (171.14,160.91) -- (142.6,161.53) ;
            		\draw [color={rgb, 255:red, 200; green, 192; blue, 192 }  ,draw opacity=1 ][line width=2.25]    (145.72,128.5) -- (167.9,126.98) ;
            		\draw [color={rgb, 255:red, 200; green, 192; blue, 192 }  ,draw opacity=1 ][line width=2.25]    (169.52,143.94) -- (142.6,161.53) ;
            		\draw [color={rgb, 255:red, 200; green, 192; blue, 192 }  ,draw opacity=1 ][line width=2.25]    (145.72,128.5) -- (169.52,143.94) ;
            		\draw [color={rgb, 255:red, 200; green, 192; blue, 192 }  ,draw opacity=1 ][line width=2.25]    (167.9,126.98) -- (143.85,144.53) ;
            		\draw [color={rgb, 255:red, 200; green, 192; blue, 192 }  ,draw opacity=1 ][line width=2.25]    (144.6,142.03) -- (171.14,160.91) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=2.25]    (142.6,161.53) -- (172.52,177.92) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=2.25]    (171.14,160.91) -- (141.1,178.53) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=2.25]    (172.52,177.92) -- (141.1,178.53) ;
            		\path  [shading=_i7iu5kxob,_za1spe3ho] (151.6,208.93) -- (161,208.93) -- (161,245.83) -- (151.6,245.83) -- cycle ; 
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.49 ] (151.6,208.93) -- (161,208.93) -- (161,245.83) -- (151.6,245.83) -- cycle ; 
            		\path  [shading=_a95fcgctk,_u6ti8hlvc] (134.5,206.74) -- (134.5,196.52) .. controls (134.5,195.31) and (144.26,194.33) .. (156.3,194.33) .. controls (168.34,194.33) and (178.1,195.31) .. (178.1,196.52) -- (178.1,206.74) .. controls (178.1,207.95) and (168.34,208.93) .. (156.3,208.93) .. controls (144.26,208.93) and (134.5,207.95) .. (134.5,206.74) .. controls (134.5,205.53) and (144.26,204.55) .. (156.3,204.55) .. controls (168.34,204.55) and (178.1,205.53) .. (178.1,206.74) ; 
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ] (134.5,206.74) -- (134.5,196.52) .. controls (134.5,195.31) and (144.26,194.33) .. (156.3,194.33) .. controls (168.34,194.33) and (178.1,195.31) .. (178.1,196.52) -- (178.1,206.74) .. controls (178.1,207.95) and (168.34,208.93) .. (156.3,208.93) .. controls (144.26,208.93) and (134.5,207.95) .. (134.5,206.74) .. controls (134.5,205.53) and (144.26,204.55) .. (156.3,204.55) .. controls (168.34,204.55) and (178.1,205.53) .. (178.1,206.74) ; 
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.55 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (137.05,206.88) .. controls (137.05,205.75) and (145.67,204.83) .. (156.3,204.83) .. controls (166.93,204.83) and (175.55,205.75) .. (175.55,206.88) .. controls (175.55,208.02) and (166.93,208.93) .. (156.3,208.93) .. controls (145.67,208.93) and (137.05,208.02) .. (137.05,206.88) -- cycle ;
            		\path  [shading=_zl76pi2s0,_qep3w0bv7] (141.1,206.83) -- (143.99,208.13) -- (126.6,246.83) -- (123.71,245.54) -- cycle ; 
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.49 ] (141.1,206.83) -- (143.99,208.13) -- (126.6,246.83) -- (123.71,245.54) -- cycle ; 
            		\path  [shading=_hiu89ra55,_hi1rvrb2b] (190.72,245.12) -- (187.88,246.53) -- (168.98,208.54) -- (171.82,207.13) -- cycle ; 
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.49 ] (190.72,245.12) -- (187.88,246.53) -- (168.98,208.54) -- (171.82,207.13) -- cycle ; 
            		\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=1.5]    (135.29,227.48) -- (178.43,227.54) ;
            		\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=1.5]    (126.6,246.83) -- (156.86,227.51) ;
            		\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=1.5]    (156.86,227.51) -- (189.3,245.83) ;
            		\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=1.5]    (143.99,208.13) -- (156.3,227.38) ;
            		\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=1.5]    (156.86,227.51) -- (170.4,207.84) ;
            		\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=1.5]    (135.29,227.48) -- (168.98,208.54) ;
            		\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=1.5]    (143.99,208.13) -- (178.43,227.54) ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.53 ][fill={rgb, 255:red, 174; green, 171; blue, 136 }  ,fill opacity=1 ] (113,245.93) -- (201.1,245.93) -- (201.1,272.83) -- (113,272.83) -- cycle ;
            		\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 150; green, 147; blue, 106 }  ,fill opacity=1 ] (135,259.38) -- (179.1,259.38) -- (179.1,272.83) -- (135,272.83) -- cycle ;
            		\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 121; green, 119; blue, 88 }  ,fill opacity=1 ] (144.5,259.38) -- (169.6,259.38) -- (169.6,272.83) -- (144.5,272.83) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.48 ]   (129.5,246.93) -- (124.1,273.33) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.48 ]   (183.1,245.33) -- (187.6,272.33) ;
            		\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (182.1,245.33) -- (186.6,272.33) ;
            		\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (130.5,246.93) -- (125.1,273.33) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (132.65,256.98) -- (180.9,256.98) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (132.65,271.98) -- (132.65,256.98) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (180.9,271.98) -- (180.9,256.98) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (141.65,271.98) -- (141.65,259.73) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (172.15,272.48) -- (172.15,260.23) ;
            		\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (147.5,266.11) -- (166.6,266.11) -- (166.6,272.83) -- (147.5,272.83) -- cycle ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=2.25]    (165.6,108.03) -- (145.1,127.53) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=2.25]    (167.9,126.98) -- (146.6,107.53) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=2.25]    (165.6,108.03) -- (146.6,107.53) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=2.25]    (164.1,82.53) -- (146.6,107.53) ;
            		\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=2.25]    (165.6,108.03) -- (148.6,80.53) ;
            		\path  [shading=_sh2nemfy7,_xegrypfxy] (153.6,56.53) -- (154.8,27.03) -- (156.4,27.03) -- (157.6,56.53) -- cycle ; 
            		\draw   (153.6,56.53) -- (154.8,27.03) -- (156.4,27.03) -- (157.6,56.53) -- cycle ; 
            		\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (149.6,43.68) .. controls (149.6,43.05) and (152.29,42.53) .. (155.6,42.53) .. controls (158.91,42.53) and (161.6,43.05) .. (161.6,43.68) .. controls (161.6,44.32) and (158.91,44.83) .. (155.6,44.83) .. controls (152.29,44.83) and (149.6,44.32) .. (149.6,43.68) -- cycle ;
            		\draw    (567.87,272.87) -- (49.87,272.87) ;
            		\draw  [dash pattern={on 4.5pt off 4.5pt}]  (85.87,27.03) -- (297.87,27.03) ;
            		\draw    (89.33,30) -- (89.33,268.8) ;
            		\draw [shift={(89.33,270.8)}, rotate = 270] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (12,-3) -- (0,0) -- (12,3) -- cycle    ;
            		\draw [shift={(89.33,28)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (12,-3) -- (0,0) -- (12,3) -- cycle    ;
            		\draw  [dash pattern={on 4.5pt off 4.5pt}]  (156.1,199.83) -- (156.53,287.47) ;
            		\draw  [dash pattern={on 4.5pt off 4.5pt}]  (444.53,198.93) -- (444.97,286.57) ;
            		\draw    (442.97,287.47) -- (158.53,287.47) ;
            		\draw [shift={(156.53,287.47)}, rotate = 360] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (12,-3) -- (0,0) -- (12,3) -- cycle    ;
            		\draw [shift={(444.97,287.47)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (12,-3) -- (0,0) -- (12,3) -- cycle    ;
            		\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (440.93,198.93) .. controls (440.93,196.95) and (442.55,195.33) .. (444.53,195.33) .. controls (446.52,195.33) and (448.13,196.95) .. (448.13,198.93) .. controls (448.13,200.92) and (446.52,202.53) .. (444.53,202.53) .. controls (442.55,202.53) and (440.93,200.92) .. (440.93,198.93) -- cycle ;
            		\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (442.84,202.53) -- (446.22,202.53) -- (446.22,211.25) -- (442.84,211.25) -- cycle ;
            		\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (450.93,211.88) -- (450.93,214.83) .. controls (450.93,215.18) and (448.07,215.47) .. (444.53,215.47) .. controls (441,215.47) and (438.13,215.18) .. (438.13,214.83) -- (438.13,211.88) .. controls (438.13,211.53) and (441,211.25) .. (444.53,211.25) .. controls (448.07,211.25) and (450.93,211.53) .. (450.93,211.88) .. controls (450.93,212.23) and (448.07,212.51) .. (444.53,212.51) .. controls (441,212.51) and (438.13,212.23) .. (438.13,211.88) ;
            		\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (441.13,215.47) -- (447.93,215.47) -- (447.93,217.47) -- (441.13,217.47) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (438.8,217.47) -- (450.27,217.47) -- (450.27,221.13) -- (438.8,221.13) -- cycle ;
            		\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (441.6,220.8) -- (438.8,221.13) -- (414.93,272.47) -- (416.93,272.8) -- cycle ;
            		\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (450.27,221.13) -- (447.6,221.13) -- (473.93,272.67) -- (475.93,273) -- cycle ;
            		\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (446.6,222.13) -- (443.53,222.13) -- (443.27,273) -- (445.27,273.33) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (430.93,238.13) -- (432.93,239.13) -- (431.6,242.47) -- (428.93,241.8) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (442.93,239.8) -- (446.27,239.8) -- (446.27,243.8) -- (442.93,243.8) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (456.93,239.8) -- (459.93,239.47) -- (461.93,243.47) -- (458.6,244.13) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (443.6,270.13) -- (446.27,270.13) -- (446.6,273) -- (443.27,273) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (415.27,269.6) -- (417.93,269.6) -- (418.27,272.47) -- (414.93,272.47) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (474.27,269.8) -- (476.93,269.8) -- (477.27,272.67) -- (473.93,272.67) -- cycle ;
            		\draw   (436.57,198.93) .. controls (436.57,194.54) and (440.14,190.97) .. (444.53,190.97) .. controls (448.93,190.97) and (452.49,194.54) .. (452.49,198.93) .. controls (452.49,203.33) and (448.93,206.89) .. (444.53,206.89) .. controls (440.14,206.89) and (436.57,203.33) .. (436.57,198.93) -- cycle ;
            		\draw  [dash pattern={on 4.5pt off 4.5pt}]  (156.4,27.03) -- (444.53,198.93) ;
            		\draw  [dash pattern={on 4.5pt off 4.5pt}]  (158.1,199.83) -- (448.53,198.93) ;
            		\draw (146,3) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (139.33,184.33) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (135,272.83) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\draw (446.6,273) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (454,188) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\draw (71.33,137) node [anchor=north west][inner sep=0.75pt]    {$h$};
            	\end{tikzpicture} }
            \end{center}'''
                # Câu hỏi
                noidungcauhoi = (r'''Xác định chiều cao của một tháp truyền hình mà không cần lên đỉnh của tháp. Đặt kế giác thẳng đứng cách chân tháp một khoảng $CD=%sm$, biết chiều cao của giác kế là $OC=%sm$. Quay thanh giác kế sao cho khi ngắm theo thanh ta nhìn thấy đỉnh $A$ của tháp. Đọc trên giác kế số đo của góc $\widehat{AOB}=%s^\circ$. Chiều cao của ngọn tháp bằng bao nhiêu mét? (Kết quả làm tròn đến hàng đơn vị). %s''' 
                                 % (cd, oc, angle, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Tam giác $OAB$ vuông tại $B$, có $\\tan \\widehat{AOB} = \\frac{AB}{OB} \\Rightarrow AB = \\tan %s^\\circ \\cdot OB = %s \\cdot %s = %s m$. \\\\
            Vậy chiều cao của ngọn tháp là $h = AB + OC = %s + %s \\approx %s$ m.'''
                           % (angle, tan_val_tex, cd, ab_tex, ab_tex, oc, kq_int))
                dapan='\\shortans[0]{$%s$}\n'%(kq_int)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

