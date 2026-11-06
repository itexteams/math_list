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


def bt_dang15_p2_b2_c1_hh10(self):
    # Hàm hỗ trợ định dạng số thập phân sử dụng dấu phẩy
    def format_num(num):
        return str(num).replace('.', ',')

    # Khai báo biến ngẫu nhiên
    d = random.randint(20, 40)
    alpha = random.randint(55, 75)
    beta = random.randint(35, alpha - 10)

    angle_ADB_true = alpha - beta
    angle_ADB_false = angle_ADB_true + random.choice([-2, -1, 1, 2])

    angle_CDA_true = 90 - alpha
    angle_CDA_false = angle_CDA_true + random.choice([-2, -1, 1, 2])

    # Tính toán các cạnh và làm tròn 1 chữ số thập phân
    AD_exact = d * math.sin(math.radians(beta)) / math.sin(math.radians(angle_ADB_true))
    AD_true = round(AD_exact, 1)
    AD_false = round(AD_exact + random.choice([-2.5, -1.2, 1.3, 2.4]), 1)

    h_exact = AD_exact * math.sin(math.radians(alpha))
    h_true = round(h_exact, 1)
    h_false = round(h_exact + random.choice([-2.1, -1.4, 1.5, 2.2]), 1)

    # Nội dung câu hỏi
    noidungcauhoi = ('''Giả sử $CD = h$ là chiều cao của tháp trong đó $C$ là chân tháp. Chọn hai điểm $A$; $B$ trên mặt đất sao cho ba điểm $A$; $B$; $C$ thẳng hàng. Ta đo được $AB = %s m$; $\\widehat{CAD} = %s^\\circ$; $\\widehat{CBD} = %s^\\circ$. Các kết quả làm tròn đến hàng phần chục.
                     \\begin{center}
                     	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                     		\\tikzset {_nv9rokvg2/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-89 }  \\pgftransformscale{2 }  }}}
                     		\\pgfdeclarehorizontalshading{_20u0upqc9}{150bp}{rgb(0bp)=(0.6,0.85,1);
                     			rgb(37.5bp)=(0.6,0.85,1);
                     			rgb(62.5bp)=(1,1,1);
                     			rgb(100bp)=(1,1,1)}
                     		\\tikzset{every picture/.style={line width=0.75pt}} 
                     		\\draw  [draw opacity=0][shading=_20u0upqc9,_nv9rokvg2] (50.5,38.1) -- (369.2,38.1) -- (369.2,184.5) -- (50.5,184.5) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.28 ][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (74.12,178.37) .. controls (73.74,175.73) and (75,173.12) .. (77.36,171.65) .. controls (79.72,170.17) and (82.77,170.09) .. (85.22,171.43) .. controls (86.09,169.9) and (87.68,168.84) .. (89.51,168.58) .. controls (91.33,168.31) and (93.19,168.87) .. (94.5,170.09) .. controls (95.24,168.7) and (96.69,167.77) .. (98.34,167.62) .. controls (99.99,167.47) and (101.6,168.14) .. (102.61,169.37) .. controls (103.94,167.9) and (106.07,167.28) .. (108.06,167.78) .. controls (110.05,168.28) and (111.56,169.81) .. (111.93,171.72) .. controls (113.56,172.13) and (114.92,173.2) .. (115.66,174.63) .. controls (116.4,176.07) and (116.44,177.73) .. (115.77,179.2) .. controls (117.38,181.17) and (117.76,183.79) .. (116.76,186.08) .. controls (115.76,188.38) and (113.54,190.01) .. (110.92,190.36) .. controls (110.9,192.52) and (109.64,194.49) .. (107.63,195.53) .. controls (105.61,196.57) and (103.15,196.51) .. (101.2,195.36) .. controls (100.37,197.95) and (98.03,199.85) .. (95.2,200.24) .. controls (92.36,200.64) and (89.53,199.46) .. (87.94,197.22) .. controls (85.99,198.33) and (83.64,198.64) .. (81.44,198.1) .. controls (79.23,197.56) and (77.35,196.21) .. (76.22,194.35) .. controls (74.22,194.57) and (72.29,193.6) .. (71.38,191.92) .. controls (70.48,190.24) and (70.79,188.21) .. (72.16,186.84) .. controls (70.38,185.85) and (69.47,183.9) .. (69.91,182) .. controls (70.35,180.1) and (72.03,178.67) .. (74.08,178.47) ; \\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.28 ] (72.16,186.84) .. controls (73,187.3) and (73.97,187.51) .. (74.94,187.44)(76.22,194.35) .. controls (76.63,194.3) and (77.04,194.2) .. (77.43,194.06)(87.94,197.22) .. controls (87.65,196.81) and (87.4,196.36) .. (87.21,195.9)(101.2,195.36) .. controls (101.35,194.89) and (101.45,194.41) .. (101.5,193.92)(110.92,190.36) .. controls (110.94,188.06) and (109.55,185.96) .. (107.35,184.96)(115.77,179.2) .. controls (115.41,179.98) and (114.87,180.67) .. (114.18,181.22)(111.93,171.72) .. controls (111.99,172.03) and (112.01,172.35) .. (112.01,172.67)(102.61,169.37) .. controls (102.27,169.74) and (102,170.15) .. (101.79,170.59)(94.5,170.09) .. controls (94.33,170.43) and (94.19,170.78) .. (94.11,171.14)(85.22,171.43) .. controls (85.74,171.72) and (86.22,172.06) .. (86.65,172.45)(74.12,178.37) .. controls (74.18,178.74) and (74.26,179.1) .. (74.37,179.45) ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.28 ][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (104.43,181.92) .. controls (104.17,180.36) and (105,178.82) .. (106.56,177.95) .. controls (108.12,177.08) and (110.13,177.03) .. (111.75,177.82) .. controls (112.32,176.92) and (113.37,176.29) .. (114.58,176.14) .. controls (115.78,175.98) and (117.01,176.31) .. (117.88,177.03) .. controls (118.36,176.21) and (119.32,175.66) .. (120.41,175.57) .. controls (121.5,175.49) and (122.56,175.88) .. (123.22,176.61) .. controls (124.11,175.74) and (125.51,175.37) .. (126.82,175.67) .. controls (128.14,175.96) and (129.13,176.87) .. (129.37,177.99) .. controls (130.45,178.24) and (131.35,178.86) .. (131.84,179.71) .. controls (132.33,180.56) and (132.35,181.54) .. (131.91,182.4) .. controls (132.98,183.57) and (133.22,185.11) .. (132.57,186.47) .. controls (131.91,187.82) and (130.44,188.78) .. (128.71,188.99) .. controls (128.7,190.26) and (127.87,191.43) .. (126.54,192.04) .. controls (125.21,192.65) and (123.59,192.62) .. (122.3,191.94) .. controls (121.75,193.47) and (120.21,194.59) .. (118.33,194.82) .. controls (116.46,195.06) and (114.6,194.36) .. (113.54,193.04) .. controls (112.26,193.69) and (110.71,193.88) .. (109.25,193.56) .. controls (107.8,193.24) and (106.55,192.44) .. (105.81,191.34) .. controls (104.49,191.47) and (103.21,190.9) .. (102.62,189.91) .. controls (102.02,188.92) and (102.22,187.72) .. (103.13,186.91) .. controls (101.96,186.33) and (101.36,185.18) .. (101.64,184.06) .. controls (101.93,182.93) and (103.04,182.1) .. (104.4,181.98) ; \\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.28 ] (103.13,186.91) .. controls (103.69,187.18) and (104.33,187.31) .. (104.97,187.27)(105.81,191.34) .. controls (106.08,191.32) and (106.35,191.26) .. (106.61,191.17)(113.54,193.04) .. controls (113.35,192.79) and (113.19,192.53) .. (113.06,192.26)(122.3,191.94) .. controls (122.4,191.66) and (122.46,191.38) .. (122.49,191.09)(128.71,188.99) .. controls (128.73,187.64) and (127.81,186.4) .. (126.36,185.8)(131.91,182.4) .. controls (131.68,182.87) and (131.32,183.27) .. (130.86,183.6)(129.37,177.99) .. controls (129.42,178.18) and (129.43,178.36) .. (129.43,178.55)(123.22,176.61) .. controls (123,176.82) and (122.82,177.07) .. (122.69,177.33)(117.88,177.03) .. controls (117.76,177.23) and (117.67,177.44) .. (117.62,177.65)(111.75,177.82) .. controls (112.09,177.99) and (112.41,178.19) .. (112.69,178.42)(104.43,181.92) .. controls (104.46,182.13) and (104.52,182.34) .. (104.59,182.55) ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.28 ][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (120.73,188.53) .. controls (120.4,186.49) and (121.48,184.47) .. (123.51,183.33) .. controls (125.54,182.18) and (128.17,182.12) .. (130.28,183.16) .. controls (131.02,181.97) and (132.39,181.16) .. (133.96,180.95) .. controls (135.53,180.75) and (137.12,181.18) .. (138.26,182.12) .. controls (138.89,181.05) and (140.14,180.33) .. (141.56,180.21) .. controls (142.98,180.1) and (144.36,180.61) .. (145.23,181.57) .. controls (146.37,180.43) and (148.2,179.95) .. (149.92,180.33) .. controls (151.63,180.72) and (152.93,181.91) .. (153.24,183.38) .. controls (154.65,183.7) and (155.82,184.53) .. (156.45,185.64) .. controls (157.09,186.75) and (157.12,188.03) .. (156.55,189.17) .. controls (157.93,190.69) and (158.26,192.71) .. (157.4,194.49) .. controls (156.54,196.27) and (154.63,197.53) .. (152.38,197.8) .. controls (152.36,199.46) and (151.28,201) .. (149.54,201.8) .. controls (147.81,202.6) and (145.7,202.55) .. (144.02,201.67) .. controls (143.31,203.66) and (141.29,205.13) .. (138.85,205.44) .. controls (136.41,205.75) and (133.98,204.84) .. (132.61,203.1) .. controls (130.93,203.96) and (128.92,204.2) .. (127.02,203.79) .. controls (125.12,203.37) and (123.51,202.32) .. (122.53,200.88) .. controls (120.81,201.05) and (119.15,200.3) .. (118.37,199) .. controls (117.59,197.7) and (117.86,196.13) .. (119.04,195.07) .. controls (117.51,194.31) and (116.73,192.8) .. (117.11,191.33) .. controls (117.48,189.86) and (118.93,188.76) .. (120.7,188.61) ; \\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.28 ] (119.04,195.07) .. controls (119.77,195.43) and (120.6,195.59) .. (121.44,195.54)(122.53,200.88) .. controls (122.89,200.85) and (123.24,200.77) .. (123.58,200.66)(132.61,203.1) .. controls (132.36,202.78) and (132.15,202.44) .. (131.98,202.08)(144.02,201.67) .. controls (144.15,201.3) and (144.23,200.93) .. (144.27,200.55)(152.38,197.8) .. controls (152.39,196.02) and (151.2,194.4) .. (149.31,193.62)(156.55,189.17) .. controls (156.24,189.77) and (155.77,190.31) .. (155.18,190.73)(153.24,183.38) .. controls (153.29,183.62) and (153.32,183.87) .. (153.31,184.12)(145.23,181.57) .. controls (144.94,181.85) and (144.7,182.17) .. (144.53,182.51)(138.26,182.12) .. controls (138.11,182.38) and (137.99,182.66) .. (137.92,182.94)(130.28,183.16) .. controls (130.72,183.38) and (131.13,183.65) .. (131.5,183.95)(120.73,188.53) .. controls (120.78,188.81) and (120.85,189.09) .. (120.95,189.36) ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (369.8,173.1) -- (369.2,184.5) -- (310.8,185.6) -- (317.3,180.6) -- (329.8,179.6) -- (330.8,176.1) -- (344.8,175.1) -- (349.3,170.1) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (50.5,184.5) -- (370.7,184.5) -- (370.7,205.6) -- (50.5,205.6) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.46 ] (87.57,185.79) .. controls (101.51,183.09) and (132.18,186.87) .. (118.24,192.28) .. controls (104.3,197.68) and (193.85,186.47) .. (207.79,194.57) .. controls (221.73,202.67) and (71.55,203.21) .. (57.61,195.11) .. controls (43.67,187.01) and (73.64,188.49) .. (87.57,185.79) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.36 ][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (92.25,74.63) .. controls (92.25,72.98) and (93.58,71.65) .. (95.22,71.65) -- (95.22,71.65) .. controls (96.87,71.65) and (98.2,72.98) .. (98.2,74.63) -- (98.2,82) .. controls (98.2,82) and (98.2,82) .. (98.2,82) -- (92.25,82) .. controls (92.25,82) and (92.25,82) .. (92.25,82) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 244; green, 229; blue, 205 }  ,fill opacity=1 ] (101.7,84.57) -- (106.2,156.32) -- (107.45,156.57) -- (107.95,158.57) -- (106.95,159.57) -- (108.5,178.62) -- (84.2,178.3) -- (84.7,159.57) -- (83.45,159.32) -- (83.95,156.07) -- (85.7,155.32) -- (89.45,96.32) -- (89.7,85.07) -- (89.2,78.9) -- (93.2,77.4) -- (97.95,77.65) -- (102.2,78.9) -- cycle ;
                     		\\draw    (85.7,155.32) .. controls (93.8,153.9) and (101.4,154.3) .. (106.2,156.32) ;
                     		\\draw    (88.2,158.3) .. controls (96.3,156.88) and (102.15,157.55) .. (106.95,159.57) ;
                     		\\draw    (89.45,97.32) .. controls (97.55,95.9) and (97.8,96.28) .. (102.6,98.3) ;
                     		\\draw    (89.45,99.32) .. controls (97.55,97.9) and (97.8,98.28) .. (102.6,100.3) ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (101.7,84.57) -- (102.6,98.3) -- (102.6,98.3) -- (99,97.9) -- (98.6,84.7) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (102.6,100.3) -- (106.2,156.32) -- (87.8,154.7) -- (89.8,147.5) -- (97.8,149.9) -- (101.4,140.7) -- (100.6,113.1) -- (96.6,99.1) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (106.95,159.57) -- (107.85,173.3) -- (108.5,178.62) -- (84.2,178.3) -- (85.4,161.5) -- (89.8,167.9) -- (103.85,159.7) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.42 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (96.77,127.72) .. controls (96.77,126.86) and (97.46,126.17) .. (98.32,126.17) -- (98.52,126.17) .. controls (99.38,126.17) and (100.08,126.86) .. (100.08,127.72) -- (100.08,137.03) .. controls (100.08,137.03) and (100.08,137.03) .. (100.08,137.03) -- (96.77,137.03) .. controls (96.77,137.03) and (96.77,137.03) .. (96.77,137.03) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.42 ] (96.38,127.45) .. controls (96.38,126.37) and (97.25,125.5) .. (98.32,125.5) -- (98.52,125.5) .. controls (99.59,125.5) and (100.46,126.37) .. (100.46,127.45) -- (100.46,137.03) .. controls (100.46,137.03) and (100.46,137.03) .. (100.46,137.03) -- (96.38,137.03) .. controls (96.38,137.03) and (96.38,137.03) .. (96.38,137.03) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.42 ][fill={rgb, 255:red, 235; green, 232; blue, 196 }  ,fill opacity=1 ] (95.6,136.9) -- (102.8,136.9) -- (102.8,137.9) -- (95.6,137.9) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.42 ] (96.86,131) -- (99.98,131) -- (99.98,131.27) -- (96.86,131.27) -- cycle ;
                     		\\draw    (86.6,90.1) .. controls (90.45,87.4) and (98.45,86.4) .. (105.2,89.9) ;
                     		\\draw    (86.6,91.85) .. controls (90.45,89.15) and (98.45,88.15) .. (105.2,91.65) ;
                     		\\draw    (102.45,94.9) -- (105.2,89.9) ;
                     		\\draw    (89.45,94.9) -- (86.6,90.1) ;
                     		\\draw    (95.7,93.9) -- (95.95,89.15) ;
                     		\\draw    (99.2,94.15) -- (100.95,89.9) ;
                     		\\draw    (92.2,93.65) -- (91.2,90.15) ;
                     		\\draw    (97.45,93.9) -- (98.45,88.9) ;
                     		\\draw    (101.2,93.9) -- (102.95,90.65) ;
                     		\\draw    (93.95,93.65) -- (93.7,89.65) ;
                     		\\draw    (90.7,94.4) -- (88.95,90.4) ;
                     		\\draw    (86.35,85.35) .. controls (90.2,82.65) and (98.2,81.65) .. (104.95,85.15) ;
                     		\\draw    (104.95,85.15) -- (105.2,89.9) ;
                     		\\draw    (86.35,85.35) -- (86.6,90.1) ;
                     		\\draw    (95.2,82.65) -- (95.45,87.4) ;
                     		\\draw    (92.2,82.9) -- (92.45,87.65) ;
                     		\\draw    (99.2,82.9) -- (99.45,87.65) ;
                     		\\draw    (87.7,84.65) -- (87.95,89.4) ;
                     		\\draw    (103.95,85.15) -- (104.2,89.9) ;
                     		\\draw    (90.45,78.15) -- (90.39,74.95) -- (90,68.59) ;
                     		\\draw    (100.95,78.65) -- (101.2,69.4) ;
                     		\\draw    (95.22,76.83) -- (95.22,65.33) ;
                     		\\draw    (90.2,80.07) .. controls (98.3,78.65) and (97.15,78.88) .. (101.95,80.9) ;
                     		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (89.7,69.45) .. controls (89.78,66.79) and (92.44,64.65) .. (95.7,64.65) .. controls (99.01,64.65) and (101.7,66.85) .. (101.7,69.57) .. controls (101.7,69.6) and (101.7,69.63) .. (101.7,69.66) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (108.5,178.62) -- (114.5,190.62) -- (68.8,189.72) -- (71,182.62) -- (77,179.62) -- (80,172.62) -- (86,172.62) -- (101,172.12) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.2 ] (96.7,182.4) -- (105.2,189.9) -- (68.8,189.72) -- (71,182.62) -- (77,179.62) -- (87.2,184.4) -- (89.2,179.9) -- (96.35,178.46) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.46 ] (199.42,183.13) .. controls (217.77,180.43) and (258.15,184.21) .. (239.8,189.61) .. controls (221.44,195.02) and (339.37,183.81) .. (357.73,191.91) .. controls (376.08,200.01) and (178.31,200.55) .. (159.95,192.45) .. controls (141.6,184.35) and (181.06,185.83) .. (199.42,183.13) -- cycle ;
                     		\\draw    (96.2,189.79) -- (341.2,190.1) ;
                     		\\draw    (96.2,189.79) -- (95.22,65.33) ;
                     		\\draw    (95.22,65.33) -- (341.2,190.1) ;
                     		\\draw    (95.22,65.33) -- (239.8,189.61) ;
                     		\\draw  [dash pattern={on 4.5pt off 4.5pt}]  (95.22,65.33) -- (59,65.33) ;
                     		\\draw    (65.5,69) -- (65.5,185.1) ;
                     		\\draw [shift={(65.5,188.1)}, rotate = 270] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
                     		\\draw [shift={(65.5,66)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
                     		\\draw    (210,189.6) .. controls (207.5,182.6) and (209,176.1) .. (219.5,173) ;
                     		\\draw    (298,189.6) .. controls (295.5,182.6) and (297,176.1) .. (307.5,173) ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.2 ] (366.8,177.1) -- (368.4,183.04) -- (332,182.86) -- (337.8,179.6) -- (341.3,177.6) -- (350.4,177.54) -- (352.4,173.04) -- (359.8,177.1) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (323.44,50.77) .. controls (326.67,50.77) and (329.65,51.13) .. (332.01,51.72) .. controls (332.79,49.91) and (335.18,48.6) .. (338.01,48.6) .. controls (341.48,48.6) and (344.29,50.58) .. (344.29,53.02) .. controls (344.29,53.41) and (344.22,53.78) .. (344.08,54.14) .. controls (351.3,54.29) and (357,56.2) .. (357,58.55) .. controls (357,60.99) and (350.81,62.97) .. (343.18,62.97) .. controls (342.4,62.97) and (341.64,62.95) .. (340.89,62.91) .. controls (338.36,63.91) and (334.49,64.55) .. (330.15,64.55) .. controls (325.67,64.55) and (321.69,63.87) .. (319.17,62.81) .. controls (316.69,63.57) and (313.32,64.04) .. (309.62,64.04) .. controls (301.99,64.04) and (295.8,62.06) .. (295.8,59.62) .. controls (295.8,57.17) and (301.99,55.19) .. (309.62,55.19) .. controls (309.62,52.75) and (315.81,50.77) .. (323.44,50.77) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (131.11,131.17) .. controls (132.96,131.17) and (134.66,131.37) .. (136.01,131.72) .. controls (136.46,130.68) and (137.82,129.93) .. (139.44,129.93) .. controls (141.42,129.93) and (143.03,131.06) .. (143.03,132.46) .. controls (143.03,132.68) and (142.99,132.89) .. (142.91,133.1) .. controls (147.04,133.18) and (150.3,134.28) .. (150.3,135.62) .. controls (150.3,137.02) and (146.76,138.15) .. (142.4,138.15) .. controls (141.95,138.15) and (141.51,138.14) .. (141.09,138.11) .. controls (139.64,138.69) and (137.43,139.05) .. (134.95,139.05) .. controls (132.38,139.05) and (130.11,138.66) .. (128.66,138.06) .. controls (127.24,138.49) and (125.32,138.76) .. (123.2,138.76) .. controls (118.84,138.76) and (115.3,137.63) .. (115.3,136.23) .. controls (115.3,134.83) and (118.84,133.7) .. (123.2,133.7) .. controls (123.2,132.3) and (126.74,131.17) .. (131.11,131.17) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (280.07,114.19) .. controls (282.51,114.19) and (284.74,114.46) .. (286.51,114.91) .. controls (287.11,113.55) and (288.9,112.56) .. (291.03,112.56) .. controls (293.63,112.56) and (295.74,114.05) .. (295.74,115.89) .. controls (295.74,116.18) and (295.69,116.46) .. (295.59,116.72) .. controls (301.01,116.84) and (305.3,118.28) .. (305.3,120.04) .. controls (305.3,121.88) and (300.65,123.36) .. (294.91,123.36) .. controls (294.33,123.36) and (293.75,123.35) .. (293.19,123.32) .. controls (291.29,124.07) and (288.38,124.55) .. (285.12,124.55) .. controls (281.75,124.55) and (278.76,124.04) .. (276.86,123.24) .. controls (275,123.82) and (272.47,124.17) .. (269.69,124.17) .. controls (263.95,124.17) and (259.3,122.68) .. (259.3,120.84) .. controls (259.3,119.01) and (263.95,117.52) .. (269.69,117.52) .. controls (269.69,115.68) and (274.34,114.19) .. (280.07,114.19) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (137.06,59.77) .. controls (134.86,59.77) and (132.85,60.13) .. (131.25,60.72) .. controls (130.71,58.91) and (129.09,57.6) .. (127.18,57.6) .. controls (124.83,57.6) and (122.92,59.58) .. (122.92,62.02) .. controls (122.92,62.41) and (122.97,62.78) .. (123.06,63.14) .. controls (118.17,63.29) and (114.3,65.2) .. (114.3,67.55) .. controls (114.3,69.99) and (118.5,71.97) .. (123.67,71.97) .. controls (124.2,71.97) and (124.72,71.95) .. (125.22,71.91) .. controls (126.94,72.91) and (129.57,73.55) .. (132.51,73.55) .. controls (135.54,73.55) and (138.24,72.87) .. (139.95,71.81) .. controls (141.64,72.57) and (143.92,73.04) .. (146.43,73.04) .. controls (151.6,73.04) and (155.8,71.06) .. (155.8,68.62) .. controls (155.8,66.17) and (151.6,64.19) .. (146.43,64.19) .. controls (146.43,61.75) and (142.23,59.77) .. (137.06,59.77) -- cycle ;
                     		\\draw (88,50) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$D$};
                     		\\draw (88,189.81) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$C$};
                     		\\draw (231,190.81) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$A$};
                     		\\draw (334,189.81) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$B$};
                     		\\draw (190,164.5) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$\\alpha $};
                     		\\draw (284,168) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$\\beta $};
                     		\\draw (53.5,116.5) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$h$};
                     	\\end{tikzpicture}
                     \\end{center}'''              
                     %(d, alpha, beta))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án (Không có dấu chấm ở cuối)
    nb_da_1_d = '\\True $\\widehat{ADB} = %s^\\circ$' % (angle_ADB_true)
    nb_da_1_s = '$\\widehat{ADB} = %s^\\circ$' % (angle_ADB_false)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có góc ngoài của tam giác bằng tổng hai góc trong không kề với nó, do đó xét $\\triangle ABD$ ta có: \\\\
    $\\widehat{CAD} = \\widehat{ADB} + \\widehat{ABD} \\Rightarrow \\widehat{ADB} = \\widehat{CAD} - \\widehat{ABD} = %s^\\circ - %s^\\circ = %s^\\circ$.'''
                %(alpha, beta, angle_ADB_true))

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True $\\widehat{CDA} = %s^\\circ$' %(angle_CDA_true)  
    th_da_1_s = '$\\widehat{CDA} = %s^\\circ$' %(angle_CDA_false)   
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Xét tam giác vuông $ACD$ vuông tại $C$, ta có: \\\\
    $\\widehat{CDA} = 90^\\circ - \\widehat{CAD} = 90^\\circ - %s^\\circ = %s^\\circ$.'''       
               %(alpha, angle_CDA_true))

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## 
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True $AD = %s m$' %(format_num(AD_true))  
    vd_da_1_s = '$AD = %s m$' %(format_num(AD_false))  
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Áp dụng định lý sin cho $\\triangle ABD$, ta có: \\\\
    $\\frac{AD}{\\sin \\widehat{ABD}} = \\frac{AB}{\\sin \\widehat{ADB}} \\Rightarrow AD = \\frac{AB \\cdot \\sin \\widehat{ABD}}{\\sin \\widehat{ADB}} = \\frac{%s \\cdot \\sin %s^\\circ}{\\sin %s^\\circ} \\approx %s m$.'''  
               %(d, beta, angle_ADB_true, format_num(AD_true)))

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## 
    # Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True $h = %s m$' %(format_num(h_true)) 
    vdc_da_1_s = '$h = %s m$' %(format_num(h_false)) 
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Xét tam giác vuông $ACD$ vuông tại $C$, ta có: \\\\
    $\\sin \\widehat{CAD} = \\frac{CD}{AD} \\Rightarrow h = CD = AD \\cdot \\sin \\widehat{CAD} \\approx %s \\cdot \\sin %s^\\circ \\approx %s m$.'''
               %(format_num(AD_true), alpha, format_num(h_true)))

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
        '\\end{ex}\n\\end{minipage}\n\n')
    return content

