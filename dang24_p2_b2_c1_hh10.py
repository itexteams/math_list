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


def bt_dang24_p2_b2_c1_hh10(self):
    # Khai báo biến và random số liệu
    v1 = random.randint(20, 30)
    v2 = random.randint(15, 25)
    angle_north_east = random.choice([30, 45, 60])
    total_hours = random.randint(5, 10)

    t1 = random.randint(2, 4)
    dist1 = v1 * t1
    dist1_false = dist1 + random.choice([-10, -5, 5, 10])

    angle_between = 90 - angle_north_east
    angle_between_false = angle_between + random.choice([-15, 15])

    t2 = 1
    d1_1h = v1 * t2
    d2_1h = v2 * t2
    dist_1h_sq = d1_1h**2 + d2_1h**2 - 2 * d1_1h * d2_1h * math.cos(math.radians(angle_between))
    dist_1h = round(math.sqrt(dist_1h_sq))
    dist_1h_false = dist_1h + random.choice([-5, -3, 3, 5])

    t3 = random.randint(3, 6)
    while t3 == t1 or t3 == t2:
        t3 = random.randint(3, 6)
    d1_t3 = v1 * t3
    d2_t3 = v2 * t3
    dist_t3_sq = d1_t3**2 + d2_t3**2 - 2 * d1_t3 * d2_t3 * math.cos(math.radians(angle_between))
    dist_t3 = round(math.sqrt(dist_t3_sq))
    compare_val = (dist_t3 // 10) * 10
    if dist_t3 > compare_val:
        str_compare = 'hơn %s' % compare_val
        is_true_vdc = True
    else:
        str_compare = 'ít hơn %s' % (compare_val + 10)
        is_true_vdc = True
        compare_val = compare_val + 10

    if is_true_vdc:
        str_compare_false = 'ít hơn %s' % compare_val if 'hơn' in str_compare else 'hơn %s' % compare_val


    # Nội dung câu hỏi
    noidungcauhoi = ('''\\immini{Hai tàu chở hàng cùng xuất phát từ một bến cảng nhưng đi theo hai hướng khác nhau. Chiếc thứ nhất di chuyển với tốc độ $%s$ hải lý/giờ theo hướng đông và chiếc thứ hai di chuyển theo hướng lệch so với hướng bắc $%s^\\circ$ về phía đông với tốc độ $%s$ hải lý/giờ. Giả sử chúng luôn di chuyển trên quãng đường thẳng trong suốt $%s$ giờ kể từ lúc xuất phát.}
                     {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                     			\\tikzset {_ip3ebfurw/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-91 }  \\pgftransformscale{2 }  }}}
                     		\\pgfdeclarehorizontalshading{_jimbqb8vq}{150bp}{rgb(0bp)=(0.6,0.85,1);
                     			rgb(37.5bp)=(0.6,0.85,1);
                     			rgb(43.01786150251116bp)=(1,1,1);
                     			rgb(100bp)=(1,1,1)}
                     		\\tikzset {_7hczxpox5/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-108 }  \\pgftransformscale{2 }  }}}
                     		\\pgfdeclarehorizontalshading{_22gahh306}{150bp}{rgb(0bp)=(0.31,0.89,0.76);
                     			rgb(37.5bp)=(0.31,0.89,0.76);
                     			rgb(62.5bp)=(0.29,0.56,0.89);
                     			rgb(100bp)=(0.29,0.56,0.89)}
                     		\\tikzset {_wgmadyh3u/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                     		\\pgfdeclarehorizontalshading{_r7b88j728}{150bp}{rgb(0bp)=(0,0,0);
                     			rgb(38.886904077870504bp)=(0,0,0);
                     			rgb(45.85118979215622bp)=(1,1,1);
                     			rgb(53.351195241723744bp)=(0,0,0);
                     			rgb(100bp)=(0,0,0)}
                     		\\tikzset {_hl4jla9rv/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                     		\\pgfdeclarehorizontalshading{_qga612ero}{150bp}{rgb(0bp)=(0.97,0.91,0.11);
                     			rgb(40.273813562733785bp)=(0.97,0.91,0.11);
                     			rgb(44.60714616945812bp)=(1,1,1);
                     			rgb(49.78571759802955bp)=(0.97,0.91,0.11);
                     			rgb(62.13095532996314bp)=(0.29,0.29,0.29);
                     			rgb(100bp)=(0.29,0.29,0.29)}
                     		\\tikzset {_29faidp92/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                     		\\pgfdeclarehorizontalshading{_gzn7ko24s}{150bp}{rgb(0bp)=(0.97,0.91,0.11);
                     			rgb(40.273813562733785bp)=(0.97,0.91,0.11);
                     			rgb(44.60714616945812bp)=(1,1,1);
                     			rgb(49.78571759802955bp)=(0.97,0.91,0.11);
                     			rgb(62.13095532996314bp)=(0.29,0.29,0.29);
                     			rgb(100bp)=(0.29,0.29,0.29)}
                     		\\tikzset {_u2pvpioj8/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                     		\\pgfdeclarehorizontalshading{_3k1mlecn5}{150bp}{rgb(0bp)=(0,0,0);
                     			rgb(38.886904077870504bp)=(0,0,0);
                     			rgb(45.85118979215622bp)=(1,1,1);
                     			rgb(53.351195241723744bp)=(0,0,0);
                     			rgb(100bp)=(0,0,0)}
                     		\\tikzset {_thh96inv4/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                     		\\pgfdeclarehorizontalshading{_wqn4jfg0t}{150bp}{rgb(0bp)=(0.97,0.91,0.11);
                     			rgb(40.273813562733785bp)=(0.97,0.91,0.11);
                     			rgb(44.60714616945812bp)=(1,1,1);
                     			rgb(49.78571759802955bp)=(0.97,0.91,0.11);
                     			rgb(62.13095532996314bp)=(0.29,0.29,0.29);
                     			rgb(100bp)=(0.29,0.29,0.29)}
                     		\\tikzset {_f2l1xeb7c/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                     		\\pgfdeclarehorizontalshading{_s0a5l2njn}{150bp}{rgb(0bp)=(0.97,0.91,0.11);
                     			rgb(40.273813562733785bp)=(0.97,0.91,0.11);
                     			rgb(44.60714616945812bp)=(1,1,1);
                     			rgb(49.78571759802955bp)=(0.97,0.91,0.11);
                     			rgb(62.13095532996314bp)=(0.29,0.29,0.29);
                     			rgb(100bp)=(0.29,0.29,0.29)}
                     		\\tikzset{every picture/.style={line width=0.75pt}} 
                     		\\draw  [draw opacity=0][shading=_jimbqb8vq,_ip3ebfurw] (10.1,7) -- (252.5,7) -- (252.5,159.9) -- (10.1,159.9) -- cycle ;
                     		\\draw  [draw opacity=0][shading=_22gahh306,_7hczxpox5] (10.1,40.4) -- (252.5,40.4) -- (252.5,159.9) -- (10.1,159.9) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.1 ] (47.69,49.5) .. controls (56.86,49.5) and (64.3,50.35) .. (64.3,51.4) .. controls (64.3,52.14) and (60.65,52.78) .. (55.3,53.1) .. controls (56.11,53.34) and (56.56,53.62) .. (56.56,53.92) .. controls (56.56,54.06) and (56.46,54.2) .. (56.27,54.33) .. controls (58.95,54.18) and (62.02,54.09) .. (65.29,54.09) .. controls (75.68,54.09) and (84.1,54.95) .. (84.1,56) .. controls (84.1,57.05) and (75.68,57.9) .. (65.29,57.9) .. controls (59.86,57.9) and (54.97,57.67) .. (51.54,57.3) .. controls (48.73,57.56) and (45.14,57.72) .. (41.22,57.72) .. controls (32.22,57.72) and (24.92,56.87) .. (24.92,55.82) .. controls (24.92,55.73) and (24.98,55.63) .. (25.1,55.54) .. controls (19.58,55.33) and (15.5,54.59) .. (15.5,53.7) .. controls (15.5,52.65) and (21.25,51.8) .. (28.33,51.8) .. controls (29.45,51.8) and (30.53,51.82) .. (31.56,51.86) .. controls (31.25,51.71) and (31.08,51.56) .. (31.08,51.4) .. controls (31.08,50.35) and (38.52,49.5) .. (47.69,49.5) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.1 ] (81.64,43.5) .. controls (86.92,43.5) and (91.2,44.5) .. (91.2,45.74) .. controls (91.2,46.61) and (89.1,47.36) .. (86.02,47.74) .. controls (86.48,48.03) and (86.75,48.36) .. (86.75,48.71) .. controls (86.75,48.87) and (86.69,49.03) .. (86.58,49.19) .. controls (88.12,49.01) and (89.89,48.91) .. (91.77,48.91) .. controls (97.75,48.91) and (102.6,49.92) .. (102.6,51.16) .. controls (102.6,52.4) and (97.75,53.4) .. (91.77,53.4) .. controls (88.64,53.4) and (85.83,53.13) .. (83.85,52.69) .. controls (82.23,53) and (80.16,53.19) .. (77.91,53.19) .. controls (72.73,53.19) and (68.53,52.19) .. (68.53,50.95) .. controls (68.53,50.84) and (68.56,50.73) .. (68.63,50.62) .. controls (65.45,50.37) and (63.1,49.49) .. (63.1,48.45) .. controls (63.1,47.21) and (66.41,46.21) .. (70.49,46.21) .. controls (71.13,46.21) and (71.75,46.23) .. (72.35,46.28) .. controls (72.17,46.11) and (72.07,45.93) .. (72.07,45.74) .. controls (72.07,44.5) and (76.35,43.5) .. (81.64,43.5) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.1 ] (173.9,45.5) .. controls (187.81,45.5) and (199.08,46.35) .. (199.08,47.4) .. controls (199.08,48.14) and (193.55,48.78) .. (185.44,49.1) .. controls (186.67,49.34) and (187.36,49.62) .. (187.36,49.92) .. controls (187.36,50.06) and (187.2,50.2) .. (186.91,50.33) .. controls (190.97,50.18) and (195.63,50.09) .. (200.58,50.09) .. controls (216.33,50.09) and (229.1,50.95) .. (229.1,52) .. controls (229.1,53.05) and (216.33,53.9) .. (200.58,53.9) .. controls (192.36,53.9) and (184.94,53.67) .. (179.73,53.3) .. controls (175.47,53.56) and (170.03,53.72) .. (164.09,53.72) .. controls (150.45,53.72) and (139.39,52.87) .. (139.39,51.82) .. controls (139.39,51.73) and (139.48,51.63) .. (139.65,51.54) .. controls (131.28,51.33) and (125.1,50.59) .. (125.1,49.7) .. controls (125.1,48.65) and (133.81,47.8) .. (144.55,47.8) .. controls (146.24,47.8) and (147.88,47.82) .. (149.45,47.86) .. controls (148.97,47.71) and (148.72,47.56) .. (148.72,47.4) .. controls (148.72,46.35) and (160,45.5) .. (173.9,45.5) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.1 ] (152.72,54.4) .. controls (140.22,54.4) and (130.09,55.47) .. (130.09,56.78) .. controls (130.09,57.7) and (135.06,58.5) .. (142.35,58.89) .. controls (141.25,59.21) and (140.63,59.55) .. (140.63,59.92) .. controls (140.63,60.1) and (140.77,60.27) .. (141.03,60.43) .. controls (137.38,60.25) and (133.19,60.14) .. (128.74,60.14) .. controls (114.58,60.14) and (103.1,61.21) .. (103.1,62.52) .. controls (103.1,63.83) and (114.58,64.9) .. (128.74,64.9) .. controls (136.14,64.9) and (142.8,64.61) .. (147.48,64.14) .. controls (151.31,64.48) and (156.21,64.68) .. (161.54,64.68) .. controls (173.81,64.68) and (183.76,63.62) .. (183.76,62.3) .. controls (183.76,62.18) and (183.68,62.07) .. (183.52,61.95) .. controls (191.04,61.69) and (196.6,60.76) .. (196.6,59.65) .. controls (196.6,58.34) and (188.77,57.27) .. (179.11,57.27) .. controls (177.59,57.27) and (176.12,57.3) .. (174.71,57.35) .. controls (175.14,57.16) and (175.36,56.97) .. (175.36,56.78) .. controls (175.36,55.47) and (165.23,54.4) .. (152.72,54.4) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.1 ] (62.72,63.5) .. controls (71.76,63.5) and (79.09,65.23) .. (79.09,67.36) .. controls (79.09,68.86) and (75.49,70.16) .. (70.22,70.8) .. controls (71.02,71.31) and (71.47,71.87) .. (71.47,72.47) .. controls (71.47,72.76) and (71.37,73.03) .. (71.18,73.3) .. controls (73.81,73) and (76.84,72.83) .. (80.07,72.83) .. controls (90.3,72.83) and (98.6,74.56) .. (98.6,76.69) .. controls (98.6,78.83) and (90.3,80.56) .. (80.07,80.56) .. controls (74.72,80.56) and (69.9,80.08) .. (66.51,79.33) .. controls (63.74,79.87) and (60.2,80.2) .. (56.35,80.2) .. controls (47.48,80.2) and (40.29,78.47) .. (40.29,76.34) .. controls (40.29,76.14) and (40.34,75.95) .. (40.46,75.77) .. controls (35.02,75.34) and (31,73.83) .. (31,72.03) .. controls (31,69.89) and (36.66,68.16) .. (43.65,68.16) .. controls (44.74,68.16) and (45.81,68.21) .. (46.82,68.29) .. controls (46.52,67.99) and (46.36,67.68) .. (46.36,67.36) .. controls (46.36,65.23) and (53.68,63.5) .. (62.72,63.5) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.1 ] (98.84,62) .. controls (105.2,62) and (110.36,63.22) .. (110.36,64.72) .. controls (110.36,65.77) and (107.83,66.69) .. (104.12,67.14) .. controls (104.68,67.5) and (104.99,67.9) .. (104.99,68.32) .. controls (104.99,68.52) and (104.92,68.71) .. (104.79,68.9) .. controls (106.65,68.69) and (108.78,68.57) .. (111.05,68.57) .. controls (118.26,68.57) and (124.1,69.79) .. (124.1,71.29) .. controls (124.1,72.79) and (118.26,74.01) .. (111.05,74.01) .. controls (107.28,74.01) and (103.89,73.68) .. (101.51,73.14) .. controls (99.56,73.53) and (97.06,73.76) .. (94.35,73.76) .. controls (88.1,73.76) and (83.04,72.54) .. (83.04,71.04) .. controls (83.04,70.9) and (83.08,70.77) .. (83.16,70.64) .. controls (79.33,70.33) and (76.5,69.27) .. (76.5,68) .. controls (76.5,66.5) and (80.49,65.28) .. (85.4,65.28) .. controls (86.18,65.28) and (86.93,65.31) .. (87.64,65.37) .. controls (87.43,65.16) and (87.31,64.94) .. (87.31,64.72) .. controls (87.31,63.22) and (92.47,62) .. (98.84,62) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.1 ] (125.7,69.33) .. controls (117.61,69.33) and (111.05,71.42) .. (111.05,74.01) .. controls (111.05,75.82) and (114.27,77.39) .. (118.98,78.17) .. controls (118.27,78.78) and (117.87,79.47) .. (117.87,80.2) .. controls (117.87,80.54) and (117.96,80.87) .. (118.13,81.2) .. controls (115.77,80.83) and (113.06,80.63) .. (110.18,80.63) .. controls (101.01,80.63) and (93.59,82.72) .. (93.59,85.31) .. controls (93.59,87.89) and (101.01,89.98) .. (110.18,89.98) .. controls (114.96,89.98) and (119.28,89.41) .. (122.3,88.5) .. controls (124.78,89.16) and (127.95,89.55) .. (131.4,89.55) .. controls (139.34,89.55) and (145.78,87.46) .. (145.78,84.87) .. controls (145.78,84.64) and (145.72,84.41) .. (145.62,84.19) .. controls (150.49,83.66) and (154.09,81.83) .. (154.09,79.66) .. controls (154.09,77.07) and (149.02,74.98) .. (142.77,74.98) .. controls (141.79,74.98) and (140.83,75.03) .. (139.92,75.13) .. controls (140.2,74.77) and (140.34,74.39) .. (140.34,74.01) .. controls (140.34,71.42) and (133.79,69.33) .. (125.7,69.33) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.1 ] (141.29,80.26) .. controls (135.77,80.26) and (131.3,81.69) .. (131.3,83.45) .. controls (131.3,84.69) and (133.5,85.76) .. (136.71,86.29) .. controls (136.22,86.7) and (135.95,87.17) .. (135.95,87.67) .. controls (135.95,87.9) and (136.01,88.13) .. (136.13,88.35) .. controls (134.52,88.1) and (132.67,87.96) .. (130.7,87.96) .. controls (124.46,87.96) and (119.39,89.39) .. (119.39,91.15) .. controls (119.39,92.92) and (124.46,94.34) .. (130.7,94.34) .. controls (133.97,94.34) and (136.91,93.95) .. (138.98,93.33) .. controls (140.67,93.78) and (142.83,94.05) .. (145.18,94.05) .. controls (150.59,94.05) and (154.98,92.62) .. (154.98,90.86) .. controls (154.98,90.7) and (154.95,90.54) .. (154.88,90.39) .. controls (158.2,90.03) and (160.65,88.79) .. (160.65,87.3) .. controls (160.65,85.54) and (157.19,84.11) .. (152.93,84.11) .. controls (152.26,84.11) and (151.61,84.15) .. (150.99,84.21) .. controls (151.18,83.97) and (151.28,83.71) .. (151.28,83.45) .. controls (151.28,81.69) and (146.81,80.26) .. (141.29,80.26) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.1 ] (177.2,82.75) .. controls (166.97,82.75) and (158.68,85.48) .. (158.68,88.86) .. controls (158.68,91.23) and (162.75,93.28) .. (168.71,94.29) .. controls (167.81,95.09) and (167.31,95.99) .. (167.31,96.94) .. controls (167.31,97.39) and (167.42,97.83) .. (167.64,98.25) .. controls (164.65,97.77) and (161.22,97.5) .. (157.58,97.5) .. controls (145.99,97.5) and (136.6,100.24) .. (136.6,103.61) .. controls (136.6,106.99) and (145.99,109.72) .. (157.58,109.72) .. controls (163.63,109.72) and (169.08,108.98) .. (172.91,107.78) .. controls (176.05,108.64) and (180.05,109.16) .. (184.42,109.16) .. controls (194.46,109.16) and (202.59,106.42) .. (202.59,103.05) .. controls (202.59,102.74) and (202.53,102.44) .. (202.4,102.15) .. controls (208.55,101.47) and (213.1,99.08) .. (213.1,96.24) .. controls (213.1,92.86) and (206.69,90.12) .. (198.79,90.12) .. controls (197.55,90.12) and (196.34,90.19) .. (195.19,90.32) .. controls (195.54,89.85) and (195.72,89.36) .. (195.72,88.86) .. controls (195.72,85.48) and (187.43,82.75) .. (177.2,82.75) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.1 ] (188.91,103.24) .. controls (183.5,103.24) and (179.11,104.65) .. (179.11,106.38) .. controls (179.11,107.59) and (181.26,108.64) .. (184.42,109.16) .. controls (183.94,109.57) and (183.67,110.03) .. (183.67,110.52) .. controls (183.67,110.75) and (183.73,110.97) .. (183.85,111.19) .. controls (182.27,110.94) and (180.45,110.8) .. (178.52,110.8) .. controls (172.39,110.8) and (167.42,112.21) .. (167.42,113.94) .. controls (167.42,115.67) and (172.39,117.07) .. (178.52,117.07) .. controls (181.73,117.07) and (184.61,116.69) .. (186.64,116.07) .. controls (188.3,116.52) and (190.42,116.78) .. (192.73,116.78) .. controls (198.04,116.78) and (202.35,115.38) .. (202.35,113.65) .. controls (202.35,113.49) and (202.32,113.34) .. (202.25,113.19) .. controls (205.51,112.84) and (207.91,111.61) .. (207.91,110.16) .. controls (207.91,108.43) and (204.52,107.02) .. (200.34,107.02) .. controls (199.68,107.02) and (199.04,107.06) .. (198.43,107.12) .. controls (198.62,106.88) and (198.71,106.63) .. (198.71,106.38) .. controls (198.71,104.65) and (194.33,103.24) .. (188.91,103.24) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.1 ] (60.48,89.83) .. controls (68.58,89.83) and (75.14,92.32) .. (75.14,95.4) .. controls (75.14,97.55) and (71.91,99.42) .. (67.2,100.35) .. controls (67.91,101.07) and (68.31,101.89) .. (68.31,102.75) .. controls (68.31,103.16) and (68.22,103.56) .. (68.05,103.95) .. controls (70.41,103.51) and (73.12,103.27) .. (76.01,103.27) .. controls (85.17,103.27) and (92.6,105.76) .. (92.6,108.83) .. controls (92.6,111.91) and (85.17,114.4) .. (76.01,114.4) .. controls (71.22,114.4) and (66.91,113.72) .. (63.88,112.63) .. controls (61.4,113.42) and (58.23,113.89) .. (54.78,113.89) .. controls (46.84,113.89) and (40.4,111.4) .. (40.4,108.32) .. controls (40.4,108.04) and (40.45,107.77) .. (40.55,107.5) .. controls (35.68,106.88) and (32.09,104.7) .. (32.09,102.11) .. controls (32.09,99.04) and (37.16,96.55) .. (43.41,96.55) .. controls (44.39,96.55) and (45.34,96.61) .. (46.25,96.73) .. controls (45.98,96.3) and (45.83,95.85) .. (45.83,95.4) .. controls (45.83,92.32) and (52.39,89.83) .. (60.48,89.83) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.1 ] (104.57,95.15) .. controls (108.61,95.15) and (111.88,96.29) .. (111.88,97.7) .. controls (111.88,98.69) and (110.27,99.54) .. (107.92,99.97) .. controls (108.28,100.3) and (108.48,100.67) .. (108.48,101.07) .. controls (108.48,101.26) and (108.43,101.44) .. (108.35,101.61) .. controls (109.52,101.42) and (110.88,101.3) .. (112.32,101.3) .. controls (116.89,101.3) and (120.6,102.44) .. (120.6,103.85) .. controls (120.6,105.26) and (116.89,106.4) .. (112.32,106.4) .. controls (109.93,106.4) and (107.77,106.09) .. (106.26,105.59) .. controls (105.02,105.95) and (103.44,106.17) .. (101.72,106.17) .. controls (97.76,106.17) and (94.54,105.02) .. (94.54,103.62) .. controls (94.54,103.49) and (94.57,103.36) .. (94.62,103.24) .. controls (92.19,102.96) and (90.39,101.96) .. (90.39,100.78) .. controls (90.39,99.37) and (92.92,98.23) .. (96.04,98.23) .. controls (96.53,98.23) and (97.01,98.26) .. (97.46,98.31) .. controls (97.33,98.11) and (97.25,97.91) .. (97.25,97.7) .. controls (97.25,96.29) and (100.53,95.15) .. (104.57,95.15) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.1 ] (73.16,112.83) .. controls (78.45,112.83) and (82.74,114.46) .. (82.74,116.47) .. controls (82.74,117.88) and (80.64,119.1) .. (77.55,119.71) .. controls (78.02,120.18) and (78.28,120.72) .. (78.28,121.28) .. controls (78.28,121.55) and (78.22,121.81) .. (78.11,122.06) .. controls (79.65,121.78) and (81.43,121.62) .. (83.31,121.62) .. controls (89.31,121.62) and (94.17,123.25) .. (94.17,125.26) .. controls (94.17,127.27) and (89.31,128.9) .. (83.31,128.9) .. controls (80.18,128.9) and (77.36,128.45) .. (75.38,127.74) .. controls (73.76,128.26) and (71.69,128.57) .. (69.43,128.57) .. controls (64.23,128.57) and (60.02,126.94) .. (60.02,124.92) .. controls (60.02,124.74) and (60.06,124.56) .. (60.12,124.39) .. controls (56.94,123.98) and (54.59,122.56) .. (54.59,120.86) .. controls (54.59,118.85) and (57.9,117.22) .. (61.99,117.22) .. controls (62.63,117.22) and (63.26,117.26) .. (63.85,117.34) .. controls (63.67,117.06) and (63.58,116.77) .. (63.58,116.47) .. controls (63.58,114.46) and (67.87,112.83) .. (73.16,112.83) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (187,118.88) -- (194.35,118.88) -- (194.35,121.82) -- (187,121.82) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (187.53,117.29) -- (193.81,117.29) -- (193.81,118.88) -- (187.53,118.88) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (187.53,116.4) -- (193.81,116.4) -- (193.81,117.29) -- (187.53,117.29) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (195.76,119.38) -- (199.4,119.38) -- (199.4,121.68) -- (195.76,121.68) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (199.4,119.38) -- (203.04,119.38) -- (203.04,121.68) -- (199.4,121.68) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (203.04,119.38) -- (206.68,119.38) -- (206.68,121.68) -- (203.04,121.68) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (206.68,119.38) -- (210.32,119.38) -- (210.32,121.68) -- (206.68,121.68) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (210.32,119.38) -- (213.95,119.38) -- (213.95,121.68) -- (210.32,121.68) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (213.95,119.38) -- (217.59,119.38) -- (217.59,121.68) -- (213.95,121.68) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (195.76,117) -- (199.4,117) -- (199.4,119.3) -- (195.76,119.3) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (199.4,117) -- (203.04,117) -- (203.04,119.3) -- (199.4,119.3) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (203.04,117) -- (206.68,117) -- (206.68,119.3) -- (203.04,119.3) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (206.68,117) -- (210.32,117) -- (210.32,119.3) -- (206.68,119.3) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (210.32,117) -- (213.95,117) -- (213.95,119.3) -- (210.32,119.3) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (213.95,117) -- (217.59,117) -- (217.59,119.3) -- (213.95,119.3) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 13; green, 74; blue, 145 }  ,fill opacity=1 ] (224.1,120.92) -- (220.69,123.9) -- (186.91,123.6) -- (186.1,121.12) -- (192.64,121.02) -- (192.64,121.82) -- (213.61,121.92) -- (216.93,121.12) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (222.4,122.41) -- (220.69,123.9) -- (186.91,123.6) -- (212.54,123.21) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (188,125.9) -- (195.35,125.9) -- (195.35,125.32) -- (188,125.32) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (188.53,126.22) -- (194.81,126.22) -- (194.81,125.9) -- (188.53,125.9) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (188.53,126.4) -- (194.81,126.4) -- (194.81,126.22) -- (188.53,126.22) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (196.76,125.8) -- (200.4,125.8) -- (200.4,125.34) -- (196.76,125.34) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (200.4,125.8) -- (204.04,125.8) -- (204.04,125.34) -- (200.4,125.34) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (204.04,125.8) -- (207.68,125.8) -- (207.68,125.34) -- (204.04,125.34) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (207.68,125.8) -- (211.32,125.8) -- (211.32,125.34) -- (207.68,125.34) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (211.32,125.8) -- (214.95,125.8) -- (214.95,125.34) -- (211.32,125.34) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (214.95,125.8) -- (218.59,125.8) -- (218.59,125.34) -- (214.95,125.34) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (196.76,126.28) -- (200.4,126.28) -- (200.4,125.82) -- (196.76,125.82) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (200.4,126.28) -- (204.04,126.28) -- (204.04,125.82) -- (200.4,125.82) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (204.04,126.28) -- (207.68,126.28) -- (207.68,125.82) -- (204.04,125.82) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (207.68,126.28) -- (211.32,126.28) -- (211.32,125.82) -- (207.68,125.82) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (211.32,126.28) -- (214.95,126.28) -- (214.95,125.82) -- (211.32,125.82) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (214.95,126.28) -- (218.59,126.28) -- (218.59,125.82) -- (214.95,125.82) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (225.1,125.5) -- (221.69,124.9) -- (187.91,124.96) -- (187.1,125.46) -- (193.64,125.48) -- (193.64,125.32) -- (214.61,125.3) -- (217.93,125.46) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.16 ] (223.4,125.2) -- (221.69,124.9) -- (187.91,124.96) -- (213.54,125.04) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 29; green, 89; blue, 159 }  ,fill opacity=1 ] (84.54,69.28) -- (84.09,72.44) -- (76.49,72.68) -- (75.86,69.69) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 16; green, 78; blue, 152 }  ,fill opacity=1 ] (84.09,72.44) -- (84.54,69.28) -- (99.25,56) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (98.3,53.99) -- (99.25,56) -- (84.54,69.28) -- (75.86,69.69) -- (93.56,55.79) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (91.5,56.18) -- (92.23,55.37) -- (94.18,55.28) -- (94.26,57.07) -- (93.53,57.87) -- (91.58,57.97) -- cycle ; \\draw   (94.18,55.28) -- (93.45,56.08) -- (91.5,56.18) ; \\draw   (93.45,56.08) -- (93.53,57.87) ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (93.53,56.08) -- (94.26,55.28) -- (96.21,55.18) -- (96.29,56.97) -- (95.56,57.78) -- (93.61,57.87) -- cycle ; \\draw   (96.21,55.18) -- (95.48,55.99) -- (93.53,56.08) ; \\draw   (95.48,55.99) -- (95.56,57.78) ;
                     		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (95.56,55.98) -- (96.29,55.18) -- (98.24,55.09) -- (98.32,56.87) -- (97.59,57.68) -- (95.64,57.77) -- cycle ; \\draw   (98.24,55.09) -- (97.51,55.89) -- (95.56,55.98) ; \\draw   (97.51,55.89) -- (97.59,57.68) ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (91.29,54.25) -- (92.01,53.45) -- (93.96,53.36) -- (94.05,55.15) -- (93.32,55.95) -- (91.37,56.04) -- cycle ; \\draw   (93.96,53.36) -- (93.23,54.16) -- (91.29,54.25) ; \\draw   (93.23,54.16) -- (93.32,55.95) ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (93.32,54.16) -- (94.04,53.35) -- (95.99,53.26) -- (96.08,55.05) -- (95.35,55.85) -- (93.4,55.95) -- cycle ; \\draw   (95.99,53.26) -- (95.26,54.06) -- (93.32,54.16) ; \\draw   (95.26,54.06) -- (95.35,55.85) ;
                     		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (95.34,54.06) -- (96.07,53.26) -- (98.02,53.16) -- (98.11,54.95) -- (97.38,55.75) -- (95.43,55.85) -- cycle ; \\draw   (98.02,53.16) -- (97.29,53.97) -- (95.34,54.06) ; \\draw   (97.29,53.97) -- (97.38,55.75) ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (89.17,57.98) -- (89.9,57.18) -- (91.85,57.08) -- (91.93,58.87) -- (91.2,59.68) -- (89.25,59.77) -- cycle ; \\draw   (91.85,57.08) -- (91.12,57.89) -- (89.17,57.98) ; \\draw   (91.12,57.89) -- (91.2,59.68) ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (91.2,57.88) -- (91.93,57.08) -- (93.88,56.99) -- (93.96,58.78) -- (93.23,59.58) -- (91.28,59.67) -- cycle ; \\draw   (93.88,56.99) -- (93.15,57.79) -- (91.2,57.88) ; \\draw   (93.15,57.79) -- (93.23,59.58) ;
                     		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (93.23,57.79) -- (93.96,56.98) -- (95.91,56.89) -- (95.99,58.68) -- (95.26,59.48) -- (93.31,59.57) -- cycle ; \\draw   (95.91,56.89) -- (95.18,57.69) -- (93.23,57.79) ; \\draw   (95.18,57.69) -- (95.26,59.48) ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (88.96,56.06) -- (89.69,55.25) -- (91.63,55.16) -- (91.72,56.95) -- (90.99,57.75) -- (89.04,57.85) -- cycle ; \\draw   (91.63,55.16) -- (90.9,55.96) -- (88.96,56.06) ; \\draw   (90.9,55.96) -- (90.99,57.75) ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (90.99,55.96) -- (91.71,55.16) -- (93.66,55.06) -- (93.75,56.85) -- (93.02,57.66) -- (91.07,57.75) -- cycle ; \\draw   (93.66,55.06) -- (92.93,55.87) -- (90.99,55.96) ; \\draw   (92.93,55.87) -- (93.02,57.66) ;
                     		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (93.01,55.86) -- (93.74,55.06) -- (95.69,54.97) -- (95.78,56.75) -- (95.05,57.56) -- (93.1,57.65) -- cycle ; \\draw   (95.69,54.97) -- (94.96,55.77) -- (93.01,55.86) ; \\draw   (94.96,55.77) -- (95.05,57.56) ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (86.97,60.02) -- (87.7,59.22) -- (89.65,59.12) -- (89.73,60.91) -- (89,61.71) -- (87.06,61.81) -- cycle ; \\draw   (89.65,59.12) -- (88.92,59.93) -- (86.97,60.02) ; \\draw   (88.92,59.93) -- (89,61.71) ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (89,59.92) -- (89.73,59.12) -- (91.68,59.02) -- (91.76,60.81) -- (91.03,61.62) -- (89.09,61.71) -- cycle ; \\draw   (91.68,59.02) -- (90.95,59.83) -- (89,59.92) ; \\draw   (90.95,59.83) -- (91.03,61.62) ;
                     		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (91.03,59.82) -- (91.76,59.02) -- (93.71,58.93) -- (93.79,60.72) -- (93.06,61.52) -- (91.12,61.61) -- cycle ; \\draw   (93.71,58.93) -- (92.98,59.73) -- (91.03,59.82) ; \\draw   (92.98,59.73) -- (93.06,61.52) ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (86.76,58.1) -- (87.49,57.29) -- (89.44,57.2) -- (89.52,58.99) -- (88.79,59.79) -- (86.84,59.89) -- cycle ; \\draw   (89.44,57.2) -- (88.71,58) -- (86.76,58.1) ; \\draw   (88.71,58) -- (88.79,59.79) ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (88.79,58) -- (89.52,57.2) -- (91.47,57.1) -- (91.55,58.89) -- (90.82,59.69) -- (88.87,59.79) -- cycle ; \\draw   (91.47,57.1) -- (90.74,57.91) -- (88.79,58) ; \\draw   (90.74,57.91) -- (90.82,59.69) ;
                     		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (90.82,57.9) -- (91.55,57.1) -- (93.5,57) -- (93.58,58.79) -- (92.85,59.6) -- (90.9,59.69) -- cycle ; \\draw   (93.5,57) -- (92.77,57.81) -- (90.82,57.9) ; \\draw   (92.77,57.81) -- (92.85,59.6) ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (84.65,61.94) -- (85.38,61.14) -- (87.32,61.05) -- (87.41,62.84) -- (86.68,63.64) -- (84.73,63.73) -- cycle ; \\draw   (87.32,61.05) -- (86.59,61.85) -- (84.65,61.94) ; \\draw   (86.59,61.85) -- (86.68,63.64) ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (86.68,61.85) -- (87.41,61.04) -- (89.35,60.95) -- (89.44,62.74) -- (88.71,63.54) -- (86.76,63.64) -- cycle ; \\draw   (89.35,60.95) -- (88.62,61.75) -- (86.68,61.85) ; \\draw   (88.62,61.75) -- (88.71,63.54) ;
                     		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (88.71,61.75) -- (89.44,60.95) -- (91.38,60.85) -- (91.47,62.64) -- (90.74,63.44) -- (88.79,63.54) -- cycle ; \\draw   (91.38,60.85) -- (90.65,61.66) -- (88.71,61.75) ; \\draw   (90.65,61.66) -- (90.74,63.44) ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (84.43,60.02) -- (85.16,59.22) -- (87.11,59.12) -- (87.2,60.91) -- (86.47,61.72) -- (84.52,61.81) -- cycle ; \\draw   (87.11,59.12) -- (86.38,59.93) -- (84.43,60.02) ; \\draw   (86.38,59.93) -- (86.47,61.72) ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (86.46,59.92) -- (87.19,59.12) -- (89.14,59.03) -- (89.23,60.81) -- (88.5,61.62) -- (86.55,61.71) -- cycle ; \\draw   (89.14,59.03) -- (88.41,59.83) -- (86.46,59.92) ; \\draw   (88.41,59.83) -- (88.5,61.62) ;
                     		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (88.49,59.83) -- (89.22,59.02) -- (91.17,58.93) -- (91.26,60.72) -- (90.53,61.52) -- (88.58,61.61) -- cycle ; \\draw   (91.17,58.93) -- (90.44,59.73) -- (88.49,59.83) ; \\draw   (90.44,59.73) -- (90.53,61.52) ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (82.44,63.86) -- (83.17,63.06) -- (85.12,62.96) -- (85.21,64.75) -- (84.48,65.56) -- (82.53,65.65) -- cycle ; \\draw   (85.12,62.96) -- (84.39,63.77) -- (82.44,63.86) ; \\draw   (84.39,63.77) -- (84.48,65.56) ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (84.47,63.76) -- (85.2,62.96) -- (87.15,62.87) -- (87.24,64.66) -- (86.51,65.46) -- (84.56,65.55) -- cycle ; \\draw   (87.15,62.87) -- (86.42,63.67) -- (84.47,63.76) ; \\draw   (86.42,63.67) -- (86.51,65.46) ;
                     		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (86.5,63.67) -- (87.23,62.86) -- (89.18,62.77) -- (89.27,64.56) -- (88.54,65.36) -- (86.59,65.46) -- cycle ; \\draw   (89.18,62.77) -- (88.45,63.57) -- (86.5,63.67) ; \\draw   (88.45,63.57) -- (88.54,65.36) ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (82.23,61.94) -- (82.96,61.14) -- (84.91,61.04) -- (84.99,62.83) -- (84.26,63.63) -- (82.32,63.73) -- cycle ; \\draw   (84.91,61.04) -- (84.18,61.85) -- (82.23,61.94) ; \\draw   (84.18,61.85) -- (84.26,63.63) ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (84.26,61.84) -- (84.99,61.04) -- (86.94,60.94) -- (87.02,62.73) -- (86.29,63.54) -- (84.35,63.63) -- cycle ; \\draw   (86.94,60.94) -- (86.21,61.75) -- (84.26,61.84) ; \\draw   (86.21,61.75) -- (86.29,63.54) ;
                     		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (86.29,61.74) -- (87.02,60.94) -- (88.97,60.85) -- (89.05,62.64) -- (88.32,63.44) -- (86.38,63.53) -- cycle ; \\draw   (88.97,60.85) -- (88.24,61.65) -- (86.29,61.74) ; \\draw   (88.24,61.65) -- (88.32,63.44) ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (80.35,65.53) -- (81.08,64.73) -- (83.03,64.64) -- (83.11,66.43) -- (82.38,67.23) -- (80.43,67.32) -- cycle ; \\draw   (83.03,64.64) -- (82.3,65.44) -- (80.35,65.53) ; \\draw   (82.3,65.44) -- (82.38,67.23) ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (82.38,65.44) -- (83.11,64.63) -- (85.06,64.54) -- (85.14,66.33) -- (84.41,67.13) -- (82.46,67.22) -- cycle ; \\draw   (85.06,64.54) -- (84.33,65.34) -- (82.38,65.44) ; \\draw   (84.33,65.34) -- (84.41,67.13) ;
                     		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (84.41,65.34) -- (85.14,64.53) -- (87.09,64.44) -- (87.17,66.23) -- (86.44,67.03) -- (84.49,67.13) -- cycle ; \\draw   (87.09,64.44) -- (86.36,65.24) -- (84.41,65.34) ; \\draw   (86.36,65.24) -- (86.44,67.03) ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (80.13,63.61) -- (80.86,62.81) -- (82.81,62.71) -- (82.9,64.5) -- (82.17,65.31) -- (80.22,65.4) -- cycle ; \\draw   (82.81,62.71) -- (82.08,63.52) -- (80.13,63.61) ; \\draw   (82.08,63.52) -- (82.17,65.31) ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (82.16,63.51) -- (82.89,62.71) -- (84.84,62.62) -- (84.93,64.4) -- (84.2,65.21) -- (82.25,65.3) -- cycle ; \\draw   (84.84,62.62) -- (84.11,63.42) -- (82.16,63.51) ; \\draw   (84.11,63.42) -- (84.2,65.21) ;
                     		\\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (84.19,63.42) -- (84.92,62.61) -- (86.87,62.52) -- (86.96,64.31) -- (86.23,65.11) -- (84.28,65.2) -- cycle ; \\draw   (86.87,62.52) -- (86.14,63.32) -- (84.19,63.42) ; \\draw   (86.14,63.32) -- (86.23,65.11) ;
                     		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (76.05,66.05) -- (77.53,64.42) -- (85.98,64.01) -- (86.15,67.64) -- (84.67,69.27) -- (76.22,69.68) -- cycle ; \\draw   (85.98,64.01) -- (84.5,65.64) -- (76.05,66.05) ; \\draw   (84.5,65.64) -- (84.67,69.27) ;
                     		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (76.8,64.07) -- (77.59,63.21) -- (85.08,62.85) -- (85.17,64.78) -- (84.38,65.65) -- (76.89,66.01) -- cycle ; \\draw   (85.08,62.85) -- (84.29,63.71) -- (76.8,64.07) ; \\draw   (84.29,63.71) -- (84.38,65.65) ;
                     		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (76.75,62.99) -- (77.19,62.5) -- (85.04,62.12) -- (85.09,63.21) -- (84.65,63.7) -- (76.8,64.07) -- cycle ; \\draw   (85.04,62.12) -- (84.6,62.61) -- (76.75,62.99) ; \\draw   (84.6,62.61) -- (84.65,63.7) ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.24 ] (99.25,56) -- (84.09,72.44) -- (76.49,72.68) -- (75.58,73.94) -- (85.6,73.7) -- cycle ;
                     		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (39.5,124) -- (183.91,123.61) ;
                     		\\draw [shift={(186.91,123.6)}, rotate = 179.85] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
                     		\\draw [color={rgb, 255:red, 20; green, 91; blue, 173 }  ,draw opacity=1 ]   (39.5,124) -- (78.2,75.18) ;
                     		\\draw [shift={(80.07,72.83)}, rotate = 128.4] [fill={rgb, 255:red, 20; green, 91; blue, 173 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
                     		\\draw  [dash pattern={on 4.5pt off 4.5pt}]  (39.5,124) -- (39.5,64.1) ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 208; green, 204; blue, 204 }  ,fill opacity=1 ] (25.1,125.6) -- (45.1,125.6) -- (10.1,159.9) -- (9.6,137.1) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (45.1,125.6) -- (42.1,133.1) -- (19.1,159.6) -- (10.1,159.9) -- cycle ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (22,128.5) -- (42.1,128.6) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (17,132.5) -- (37.1,132.6) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (9.6,137.1) -- (32.6,137.6) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (9.6,143.6) -- (25.6,143.75) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (10.6,153.1) -- (15.6,153.1) ;
                     		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (39,45) -- (39,24.1) ;
                     		\\draw [shift={(39,21.1)}, rotate = 90] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
                     		\\draw [shift={(39,48)}, rotate = 270] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
                     		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (48.8,34.55) -- (28.8,34.55) ;
                     		\\draw [shift={(25.8,34.55)}, rotate = 360] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
                     		\\draw [shift={(51.8,34.55)}, rotate = 180] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.22 ][fill={rgb, 255:red, 220; green, 213; blue, 213 }  ,fill opacity=1 ] (25.6,143.75) -- (45.8,159.9) -- (10.1,159.9) -- (9.6,143.6) -- cycle ;
                     		\\path  [shading=_r7b88j728,_wgmadyh3u] (15.34,135.8) -- (15.34,137.81) .. controls (15.34,138.37) and (16.68,138.82) .. (18.34,138.82) .. controls (19.99,138.82) and (21.33,138.37) .. (21.33,137.81) -- (21.33,135.8) .. controls (21.33,135.25) and (19.99,134.8) .. (18.34,134.8) .. controls (16.68,134.8) and (15.34,135.25) .. (15.34,135.8) .. controls (15.34,136.36) and (16.68,136.81) .. (18.34,136.81) .. controls (19.99,136.81) and (21.33,136.36) .. (21.33,135.8) ;  
                     		\\draw   (15.34,135.8) -- (15.34,137.81) .. controls (15.34,138.37) and (16.68,138.82) .. (18.34,138.82) .. controls (19.99,138.82) and (21.33,138.37) .. (21.33,137.81) -- (21.33,135.8) .. controls (21.33,135.25) and (19.99,134.8) .. (18.34,134.8) .. controls (16.68,134.8) and (15.34,135.25) .. (15.34,135.8) .. controls (15.34,136.36) and (16.68,136.81) .. (18.34,136.81) .. controls (19.99,136.81) and (21.33,136.36) .. (21.33,135.8) ;  
                     		\\path  [shading=_qga612ero,_hl4jla9rv] (17.21,121.97) -- (17.21,135.82) .. controls (17.21,136.01) and (17.73,136.17) .. (18.39,136.17) .. controls (19.04,136.17) and (19.56,136.01) .. (19.56,135.82) -- (19.56,121.97) .. controls (19.56,121.77) and (19.04,121.62) .. (18.39,121.62) .. controls (17.73,121.62) and (17.21,121.77) .. (17.21,121.97) .. controls (17.21,122.16) and (17.73,122.31) .. (18.39,122.31) .. controls (19.04,122.31) and (19.56,122.16) .. (19.56,121.97) ; 
                     		\\draw   (17.21,121.97) -- (17.21,135.82) .. controls (17.21,136.01) and (17.73,136.17) .. (18.39,136.17) .. controls (19.04,136.17) and (19.56,136.01) .. (19.56,135.82) -- (19.56,121.97) .. controls (19.56,121.77) and (19.04,121.62) .. (18.39,121.62) .. controls (17.73,121.62) and (17.21,121.77) .. (17.21,121.97) .. controls (17.21,122.16) and (17.73,122.31) .. (18.39,122.31) .. controls (19.04,122.31) and (19.56,122.16) .. (19.56,121.97) ; 
                     		\\path  [shading=_gzn7ko24s,_29faidp92] (16.83,119.65) -- (16.83,121.97) .. controls (16.83,122.22) and (17.52,122.42) .. (18.36,122.42) .. controls (19.21,122.42) and (19.89,122.22) .. (19.89,121.97) -- (19.89,119.65) .. controls (19.89,119.41) and (19.21,119.2) .. (18.36,119.2) .. controls (17.52,119.2) and (16.83,119.41) .. (16.83,119.65) .. controls (16.83,119.9) and (17.52,120.1) .. (18.36,120.1) .. controls (19.21,120.1) and (19.89,119.9) .. (19.89,119.65) ; 
                     		\\draw   (16.83,119.65) -- (16.83,121.97) .. controls (16.83,122.22) and (17.52,122.42) .. (18.36,122.42) .. controls (19.21,122.42) and (19.89,122.22) .. (19.89,121.97) -- (19.89,119.65) .. controls (19.89,119.41) and (19.21,119.2) .. (18.36,119.2) .. controls (17.52,119.2) and (16.83,119.41) .. (16.83,119.65) .. controls (16.83,119.9) and (17.52,120.1) .. (18.36,120.1) .. controls (19.21,120.1) and (19.89,119.9) .. (19.89,119.65) ; 
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (14.4,119.93) -- (15.46,119.13) -- (15.74,116.89) -- (13.46,116.53) -- (12.39,117.33) -- (12.12,119.56) -- cycle ; \\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ] (15.74,116.89) -- (14.67,117.7) -- (14.4,119.93) ; \\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ] (14.67,117.7) -- (12.39,117.33) ;
                     		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (29.78,122.01) -- (30.57,121.41) -- (30.78,119.75) -- (15.64,117.3) -- (14.84,117.9) -- (14.64,119.56) -- cycle ; \\draw   (30.78,119.75) -- (29.98,120.35) -- (29.78,122.01) ; \\draw   (29.98,120.35) -- (14.84,117.9) ;
                     		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (18.21,114.4) -- (18.3,117.64) -- (17.82,117.64) -- (17.91,114.4) -- cycle ;
                     		\\draw    (17.91,114.4) .. controls (16.98,115.14) and (17.18,116.89) .. (15.74,116.89) ;
                     		\\draw    (21.11,116.31) .. controls (22.21,118.31) and (25.74,117.74) .. (29.81,119.89) ;
                     		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (21.76,123.07) -- (21.56,122.05) -- (20.89,122.05) -- (20.69,123.07) -- (20.89,124.08) -- (21.56,124.08) -- cycle ;
                     		\\draw    (21.56,122.05) -- (21.55,120.76) ;
                     		\\draw    (20.89,122.05) -- (20.93,120.49) ;
                     		\\draw  [fill={rgb, 255:red, 140; green, 131; blue, 22 }  ,fill opacity=1 ] (30.07,120.36) -- (14.84,117.9) -- (14.64,119.56) -- (29.87,122.03) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (21.11,116.31) -- (18.65,115.91) -- (17.82,118) -- (17.77,120.36) -- (20.52,120.82) -- (20.57,118.46) -- (21.11,118.12) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (28.52,121.38) .. controls (28.52,121.16) and (28.7,120.98) .. (28.91,120.98) .. controls (29.13,120.98) and (29.3,121.16) .. (29.3,121.38) .. controls (29.3,121.6) and (29.13,121.77) .. (28.91,121.77) .. controls (28.7,121.77) and (28.52,121.6) .. (28.52,121.38) -- cycle ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (14.99,117.49) -- (12.59,117.1) ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (20.03,118.31) -- (20.58,116.68) ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (19.89,119.68) -- (20.03,118.31) ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (20.93,118.63) -- (29.87,120.14) ;
                     		\\path  [shading=_3k1mlecn5,_u2pvpioj8] (17,150.69) -- (17,153.11) .. controls (17,153.78) and (18.62,154.32) .. (20.61,154.32) .. controls (22.6,154.32) and (24.21,153.78) .. (24.21,153.11) -- (24.21,150.69) .. controls (24.21,150.02) and (22.6,149.47) .. (20.61,149.47) .. controls (18.62,149.47) and (17,150.02) .. (17,150.69) .. controls (17,151.35) and (18.62,151.9) .. (20.61,151.9) .. controls (22.6,151.9) and (24.21,151.35) .. (24.21,150.69) ; 
                     		\\draw   (17,150.69) -- (17,153.11) .. controls (17,153.78) and (18.62,154.32) .. (20.61,154.32) .. controls (22.6,154.32) and (24.21,153.78) .. (24.21,153.11) -- (24.21,150.69) .. controls (24.21,150.02) and (22.6,149.47) .. (20.61,149.47) .. controls (18.62,149.47) and (17,150.02) .. (17,150.69) .. controls (17,151.35) and (18.62,151.9) .. (20.61,151.9) .. controls (22.6,151.9) and (24.21,151.35) .. (24.21,150.69) ; 
                     		\\path  [shading=_wqn4jfg0t,_thh96inv4] (19.25,134.01) -- (19.25,150.71) .. controls (19.25,150.94) and (19.88,151.13) .. (20.67,151.13) .. controls (21.45,151.13) and (22.09,150.94) .. (22.09,150.71) -- (22.09,134.01) .. controls (22.09,133.78) and (21.45,133.6) .. (20.67,133.6) .. controls (19.88,133.6) and (19.25,133.78) .. (19.25,134.01) .. controls (19.25,134.24) and (19.88,134.43) .. (20.67,134.43) .. controls (21.45,134.43) and (22.09,134.24) .. (22.09,134.01) ; 
                     		\\draw   (19.25,134.01) -- (19.25,150.71) .. controls (19.25,150.94) and (19.88,151.13) .. (20.67,151.13) .. controls (21.45,151.13) and (22.09,150.94) .. (22.09,150.71) -- (22.09,134.01) .. controls (22.09,133.78) and (21.45,133.6) .. (20.67,133.6) .. controls (19.88,133.6) and (19.25,133.78) .. (19.25,134.01) .. controls (19.25,134.24) and (19.88,134.43) .. (20.67,134.43) .. controls (21.45,134.43) and (22.09,134.24) .. (22.09,134.01) ; 
                     		\\path  [shading=_s0a5l2njn,_f2l1xeb7c] (18.8,131.23) -- (18.8,134.02) .. controls (18.8,134.32) and (19.62,134.56) .. (20.64,134.56) .. controls (21.66,134.56) and (22.48,134.32) .. (22.48,134.02) -- (22.48,131.23) .. controls (22.48,130.93) and (21.66,130.69) .. (20.64,130.69) .. controls (19.62,130.69) and (18.8,130.93) .. (18.8,131.23) .. controls (18.8,131.53) and (19.62,131.77) .. (20.64,131.77) .. controls (21.66,131.77) and (22.48,131.53) .. (22.48,131.23) ; 
                     		\\draw   (18.8,131.23) -- (18.8,134.02) .. controls (18.8,134.32) and (19.62,134.56) .. (20.64,134.56) .. controls (21.66,134.56) and (22.48,134.32) .. (22.48,134.02) -- (22.48,131.23) .. controls (22.48,130.93) and (21.66,130.69) .. (20.64,130.69) .. controls (19.62,130.69) and (18.8,130.93) .. (18.8,131.23) .. controls (18.8,131.53) and (19.62,131.77) .. (20.64,131.77) .. controls (21.66,131.77) and (22.48,131.53) .. (22.48,131.23) ; 
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (15.86,131.56) -- (17.15,130.59) -- (17.48,127.91) -- (14.74,127.46) -- (13.45,128.43) -- (13.12,131.12) -- cycle ; \\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ] (17.48,127.91) -- (16.19,128.87) -- (15.86,131.56) ; \\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ] (16.19,128.87) -- (13.45,128.43) ;
                     		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (34.39,134.07) -- (35.35,133.35) -- (35.59,131.35) -- (17.36,128.39) -- (16.4,129.11) -- (16.16,131.12) -- cycle ; \\draw   (35.59,131.35) -- (34.64,132.07) -- (34.39,134.07) ; \\draw   (34.64,132.07) -- (16.4,129.11) ;
                     		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (20.46,124.9) -- (20.57,128.8) -- (19.99,128.8) -- (20.09,124.9) -- cycle ;
                     		\\draw    (20.09,124.9) .. controls (18.98,125.79) and (19.22,127.9) .. (17.48,127.91) ;
                     		\\draw    (23.95,127.2) .. controls (25.27,129.61) and (29.53,128.92) .. (34.43,131.52) ;
                     		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (24.74,135.34) -- (24.5,134.12) -- (23.69,134.12) -- (23.44,135.34) -- (23.69,136.57) -- (24.5,136.57) -- cycle ;
                     		\\draw    (24.5,134.12) -- (24.49,132.56) ;
                     		\\draw    (23.69,134.12) -- (23.73,132.23) ;
                     		\\draw  [fill={rgb, 255:red, 140; green, 131; blue, 22 }  ,fill opacity=1 ] (34.75,132.08) -- (16.4,129.11) -- (16.16,131.12) -- (34.5,134.09) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (23.95,127.2) -- (20.99,126.72) -- (19.99,129.24) -- (19.93,132.08) -- (23.24,132.63) -- (23.3,129.79) -- (23.95,129.38) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (32.88,133.31) .. controls (32.88,133.04) and (33.09,132.83) .. (33.35,132.83) .. controls (33.61,132.83) and (33.82,133.04) .. (33.82,133.31) .. controls (33.82,133.57) and (33.61,133.78) .. (33.35,133.78) .. controls (33.09,133.78) and (32.88,133.57) .. (32.88,133.31) -- cycle ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (16.57,128.62) -- (13.69,128.16) ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (22.65,129.61) -- (23.31,127.65) ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (22.48,131.26) -- (22.65,129.61) ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (23.74,129.99) -- (34.51,131.81) ;
                     		\\draw (33.5,9) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$N$};
                     		\\draw (33.5,48.5) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$S$};
                     		\\draw (51,28) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$E$};
                     		\\draw (14.5,28) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$W$};
                     		\\draw (28.1,113.6) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$O$};
                     		\\draw (178.5,125.5) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$A$};
                     		\\draw (65.5,69.5) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$B$};
                     		\\draw (31.07,148.38) node [anchor=north east][inner sep=0.75pt]  [rotate=-181.19,xscale=-1] [align=left] {?};
                     		\\draw (28.17,135.86) node [anchor=north east][inner sep=0.75pt]  [rotate=-181.19,xscale=-1] [align=left] {?};
                     	\\end{tikzpicture} }'''               
                     %(v1, angle_north_east, v2, total_hours))

    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Sau $%s$ giờ kể từ lúc xuất phát, chiếc tàu thứ nhất cách bến cảng $%s$ hải lý.' % (t1, dist1)
    nb_da_1_s = 'Sau $%s$ giờ kể từ lúc xuất phát, chiếc tàu thứ nhất cách bến cảng $%s$ hải lý.' % (t1, dist1_false)
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Quãng đường chiếc tàu thứ nhất đi được sau $%s$ giờ là: $s_1 = v_1 \\cdot t = %s \\cdot %s = %s$ (hải lý).'''
                    %(t1, v1, t1, dist1))

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
    th_da_1_d = '\\True Hai tàu di chuyển theo hai hướng tạo với nhau một góc $%s^\\circ$.' % (angle_between)  
    th_da_1_s = 'Hai tàu di chuyển theo hai hướng tạo với nhau một góc $%s^\\circ$.' % (angle_between_false)   
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)


    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Hướng đông tạo với hướng bắc một góc $90^\\circ$. \\\\
    Chiếc thứ hai đi theo hướng lệch so với hướng bắc $%s^\\circ$ về phía đông. \\\\
    Do đó, góc tạo bởi hai hướng đi của hai tàu là: $90^\\circ - %s^\\circ = %s^\\circ$.'''       
               %(angle_north_east, angle_north_east, angle_between))

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
    vd_da_1_d = '\\True Sau $1$ giờ kể từ lúc xuất phát, hai chiếc tàu cách nhau khoảng $%s$ hải lý.' % (dist_1h)  
    vd_da_1_s = 'Sau $1$ giờ kể từ lúc xuất phát, hai chiếc tàu cách nhau khoảng $%s$ hải lý.' % (dist_1h_false)  
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Sau $1$ giờ, tàu thứ nhất đi được đoạn đường $d_1 = %s \\cdot 1 = %s$ (hải lý). \\\\
    Tàu thứ hai đi được đoạn đường $d_2 = %s \\cdot 1 = %s$ (hải lý). \\\\
    Áp dụng định lý cosin, khoảng cách giữa hai tàu sau 1 giờ là $d$: \\\\
    $d^2 = d_1^2 + d_2^2 - 2d_1 d_2 \\cos %s^\\circ = %s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\cos %s^\\circ \\approx %s$. \\\\
    Suy ra $d \\approx %s$ (hải lý).'''  
               %(v1, d1_1h, v2, d2_1h, angle_between, d1_1h, d2_1h, d1_1h, d2_1h, angle_between, dist_1h_sq, dist_1h))

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
    vdc_da_1_d = '\\True Sau $%s$ giờ kể từ lúc xuất phát, khoảng cách giữa 2 tàu %s hải lý.' % (t3, str_compare) 
    vdc_da_1_s = 'Sau $%s$ giờ kể từ lúc xuất phát, khoảng cách giữa 2 tàu %s hải lý.' % (t3, str_compare_false) 
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Sau $%s$ giờ, quãng đường tàu thứ nhất đi được là: $s_1 = %s \\cdot %s = %s$ (hải lý). \\\\
    Quãng đường tàu thứ hai đi được là: $s_2 = %s \\cdot %s = %s$ (hải lý). \\\\
    Khoảng cách giữa hai tàu sau $%s$ giờ là $x$: \\\\
    $x = \\sqrt{s_1^2 + s_2^2 - 2s_1 s_2 \\cos %s^\\circ} = \\sqrt{%s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\cos %s^\\circ} \\approx %s$ (hải lý). \\\\
    Vì $x \\approx %s$ nên khoảng cách này %s hải lý.'''
               %(t3, v1, t3, d1_t3, v2, t3, d2_t3, t3, angle_between, d1_t3, d2_t3, d1_t3, d2_t3, angle_between, dist_t3, dist_t3, str_compare))

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
    str(noidungcauhoi)+ '\n'+
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
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

