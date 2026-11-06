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


def bt_dang10_p2_b2_c2_hh10(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên
            m = random.randint(20, 30) # Cân nặng em nhỏ
            m1 = random.randint(31, 40) # Cân nặng chị
            d = round(random.uniform(3.0, 5.0), 1) # Chiều dài cầu trượt
            g = 9.8 # Gia tốc trọng trường
            alpha = 30 # Góc nghiêng
            beta = 90 - alpha # Góc giữa P và d

            # Tính toán các giá trị
            P = round(m * g, 1)
            A = round(P * d * math.cos(math.radians(beta)), 1)
            P1 = round(m1 * g, 1)
            A1 = round(P1 * d * math.cos(math.radians(beta)), 1)
            A_total = round(A + A1, 1)

            # Làm tròn kết quả nếu là số nguyên
            if P.is_integer(): P = int(P)
            if A.is_integer(): A = int(A)
            if P1.is_integer(): P1 = int(P1)
            if A1.is_integer(): A1 = int(A1)
            if A_total.is_integer(): A_total = int(A_total)

            A_total_false = round(A_total + random.choice([0.2, 0.5, -0.2, -0.5, 1.5, -1.5]), 1)
            if A_total_false.is_integer(): A_total_false = int(A_total_false)

            # Định dạng hiển thị số thập phân bằng dấu phẩy
            str_d = str(d).replace('.', ',')
            str_g = str(g).replace('.', ',')
            str_P = str(P).replace('.', ',')
            str_A = str(A).replace('.', ',')
            str_P1 = str(P1).replace('.', ',')
            str_A1 = str(A1).replace('.', ',')
            str_A_total = str(A_total).replace('.', ',')
            str_A_total_false = str(A_total_false).replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một em nhỏ có cân nặng $m = %s$ kg trượt trên cầu trượt dài $%s$ m. Biết rằng, cầu trượt có góc nghiêng so với phương nằm ngang là $30^\\circ$.
                             \\begin{center} \\scalebox{0.7}{ 
                             	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                             		\\tikzset {_3nh4gf34u/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-90 }  \\pgftransformscale{2 }  }}}
                             		\\pgfdeclarehorizontalshading{_orgnzx2cx}{150bp}{rgb(0bp)=(0.6,0.85,1);
                             			rgb(37.5bp)=(0.6,0.85,1);
                             			rgb(62.5bp)=(1,1,1);
                             			rgb(100bp)=(1,1,1)}
                             		\\tikzset{every picture/.style={line width=0.75pt}} 
                             		\\draw  [draw opacity=0][shading=_orgnzx2cx,_3nh4gf34u] (45.87,31.47) -- (493.87,31.47) -- (493.87,238.47) -- (45.87,238.47) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 103; green, 183; blue, 16 }  ,fill opacity=1 ] (86.78,162.04) .. controls (86.35,158.26) and (87.76,154.51) .. (90.42,152.4) .. controls (93.07,150.28) and (96.51,150.16) .. (99.27,152.09) .. controls (100.24,149.89) and (102.03,148.38) .. (104.08,148) .. controls (106.14,147.62) and (108.23,148.42) .. (109.71,150.17) .. controls (110.54,148.18) and (112.17,146.84) .. (114.03,146.63) .. controls (115.88,146.42) and (117.7,147.37) .. (118.83,149.14) .. controls (120.33,147.03) and (122.72,146.14) .. (124.96,146.86) .. controls (127.21,147.57) and (128.9,149.77) .. (129.31,152.5) .. controls (131.15,153.1) and (132.68,154.62) .. (133.51,156.68) .. controls (134.34,158.74) and (134.39,161.12) .. (133.64,163.22) .. controls (135.45,166.04) and (135.87,169.8) .. (134.75,173.09) .. controls (133.63,176.38) and (131.13,178.71) .. (128.18,179.22) .. controls (128.16,182.31) and (126.74,185.14) .. (124.48,186.63) .. controls (122.21,188.12) and (119.44,188.02) .. (117.25,186.39) .. controls (116.31,190.09) and (113.68,192.81) .. (110.49,193.38) .. controls (107.3,193.95) and (104.12,192.26) .. (102.32,189.05) .. controls (100.13,190.63) and (97.49,191.09) .. (95.01,190.31) .. controls (92.52,189.54) and (90.41,187.6) .. (89.13,184.93) .. controls (86.89,185.24) and (84.71,183.85) .. (83.69,181.45) .. controls (82.67,179.04) and (83.02,176.13) .. (84.57,174.17) .. controls (82.57,172.76) and (81.54,169.96) .. (82.03,167.23) .. controls (82.53,164.51) and (84.42,162.47) .. (86.73,162.18) ; \\draw  [draw opacity=0] (84.57,174.17) .. controls (85.52,174.83) and (86.61,175.13) .. (87.7,175.03)(89.13,184.93) .. controls (89.6,184.87) and (90.06,184.73) .. (90.5,184.52)(102.32,189.05) .. controls (101.99,188.46) and (101.72,187.82) .. (101.5,187.16)(117.25,186.39) .. controls (117.42,185.71) and (117.53,185.02) .. (117.58,184.32)(128.18,179.22) .. controls (128.2,175.93) and (126.64,172.92) .. (124.16,171.47)(133.64,163.22) .. controls (133.24,164.34) and (132.62,165.33) .. (131.85,166.12)(129.31,152.5) .. controls (129.38,152.95) and (129.41,153.41) .. (129.41,153.87)(118.83,149.14) .. controls (118.45,149.67) and (118.14,150.26) .. (117.91,150.89)(109.71,150.17) .. controls (109.51,150.65) and (109.36,151.16) .. (109.26,151.68)(99.27,152.09) .. controls (99.85,152.5) and (100.39,152.99) .. (100.87,153.55)(86.78,162.04) .. controls (86.84,162.56) and (86.93,163.07) .. (87.06,163.58) ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 103; green, 183; blue, 16 }  ,fill opacity=1 ] (58.05,186.17) .. controls (57.55,182.48) and (59.17,178.82) .. (62.2,176.75) .. controls (65.24,174.69) and (69.17,174.57) .. (72.32,176.45) .. controls (73.43,174.31) and (75.47,172.82) .. (77.83,172.45) .. controls (80.18,172.08) and (82.56,172.87) .. (84.25,174.58) .. controls (85.2,172.63) and (87.07,171.32) .. (89.19,171.12) .. controls (91.31,170.91) and (93.38,171.84) .. (94.67,173.57) .. controls (96.39,171.51) and (99.12,170.64) .. (101.68,171.34) .. controls (104.25,172.04) and (106.18,174.19) .. (106.66,176.85) .. controls (108.76,177.44) and (110.51,178.93) .. (111.46,180.94) .. controls (112.41,182.95) and (112.46,185.28) .. (111.6,187.33) .. controls (113.67,190.09) and (114.16,193.76) .. (112.87,196.97) .. controls (111.59,200.19) and (108.73,202.47) .. (105.37,202.96) .. controls (105.34,205.98) and (103.72,208.75) .. (101.13,210.2) .. controls (98.54,211.66) and (95.38,211.57) .. (92.87,209.97) .. controls (91.8,213.59) and (88.79,216.25) .. (85.14,216.8) .. controls (81.5,217.36) and (77.86,215.71) .. (75.81,212.57) .. controls (73.3,214.12) and (70.29,214.56) .. (67.45,213.81) .. controls (64.61,213.05) and (62.19,211.15) .. (60.74,208.55) .. controls (58.17,208.85) and (55.69,207.49) .. (54.52,205.14) .. controls (53.36,202.79) and (53.76,199.95) .. (55.52,198.03) .. controls (53.23,196.65) and (52.06,193.92) .. (52.63,191.25) .. controls (53.19,188.59) and (55.35,186.6) .. (57.99,186.32) ; \\draw  [draw opacity=0] (55.52,198.03) .. controls (56.6,198.68) and (57.85,198.97) .. (59.1,198.87)(60.74,208.55) .. controls (61.27,208.48) and (61.8,208.35) .. (62.3,208.14)(75.81,212.57) .. controls (75.43,211.99) and (75.12,211.37) .. (74.87,210.72)(92.87,209.97) .. controls (93.06,209.31) and (93.19,208.63) .. (93.25,207.94)(105.36,202.96) .. controls (105.39,199.75) and (103.6,196.8) .. (100.77,195.4)(111.6,187.33) .. controls (111.14,188.42) and (110.44,189.4) .. (109.55,190.17)(106.66,176.85) .. controls (106.73,177.29) and (106.77,177.74) .. (106.76,178.19)(94.67,173.57) .. controls (94.24,174.09) and (93.89,174.66) .. (93.62,175.28)(84.25,174.58) .. controls (84.02,175.05) and (83.85,175.54) .. (83.75,176.05)(72.32,176.45) .. controls (72.98,176.85) and (73.6,177.33) .. (74.15,177.88)(58.05,186.17) .. controls (58.11,186.68) and (58.22,187.19) .. (58.37,187.68) ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 103; green, 183; blue, 16 }  ,fill opacity=1 ] (105.39,184.65) .. controls (104.9,180.95) and (106.52,177.3) .. (109.55,175.23) .. controls (112.59,173.16) and (116.52,173.04) .. (119.66,174.93) .. controls (120.78,172.78) and (122.82,171.3) .. (125.17,170.93) .. controls (127.52,170.56) and (129.91,171.34) .. (131.6,173.05) .. controls (132.55,171.1) and (134.42,169.79) .. (136.54,169.59) .. controls (138.66,169.38) and (140.73,170.31) .. (142.02,172.04) .. controls (143.74,169.98) and (146.47,169.11) .. (149.03,169.81) .. controls (151.6,170.51) and (153.53,172.66) .. (154,175.32) .. controls (156.11,175.91) and (157.86,177.4) .. (158.81,179.41) .. controls (159.76,181.42) and (159.81,183.75) .. (158.95,185.8) .. controls (161.02,188.56) and (161.5,192.23) .. (160.22,195.45) .. controls (158.94,198.66) and (156.08,200.94) .. (152.71,201.43) .. controls (152.69,204.45) and (151.07,207.22) .. (148.48,208.68) .. controls (145.88,210.13) and (142.72,210.04) .. (140.22,208.44) .. controls (139.15,212.06) and (136.14,214.72) .. (132.49,215.27) .. controls (128.84,215.83) and (125.21,214.18) .. (123.16,211.04) .. controls (120.65,212.59) and (117.63,213.03) .. (114.8,212.28) .. controls (111.96,211.52) and (109.54,209.63) .. (108.08,207.02) .. controls (105.52,207.32) and (103.03,205.97) .. (101.87,203.61) .. controls (100.7,201.26) and (101.1,198.42) .. (102.87,196.5) .. controls (100.58,195.12) and (99.41,192.39) .. (99.97,189.72) .. controls (100.54,187.06) and (102.7,185.07) .. (105.34,184.79) ; \\draw  [draw opacity=0] (102.87,196.5) .. controls (103.95,197.15) and (105.2,197.44) .. (106.45,197.34)(108.08,207.02) .. controls (108.62,206.95) and (109.15,206.82) .. (109.65,206.61)(123.16,211.04) .. controls (122.78,210.46) and (122.47,209.84) .. (122.22,209.2)(140.22,208.44) .. controls (140.41,207.78) and (140.54,207.1) .. (140.59,206.42)(152.71,201.43) .. controls (152.74,198.22) and (150.95,195.28) .. (148.12,193.87)(158.95,185.8) .. controls (158.49,186.9) and (157.79,187.87) .. (156.9,188.64)(154,175.32) .. controls (154.08,175.77) and (154.12,176.21) .. (154.11,176.66)(142.02,172.04) .. controls (141.59,172.56) and (141.24,173.13) .. (140.97,173.75)(131.6,173.05) .. controls (131.37,173.52) and (131.2,174.01) .. (131.09,174.52)(119.66,174.93) .. controls (120.33,175.33) and (120.95,175.81) .. (121.5,176.36)(105.39,184.65) .. controls (105.46,185.16) and (105.57,185.66) .. (105.71,186.15) ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 103; green, 183; blue, 16 }  ,fill opacity=1 ] (151.96,201.53) .. controls (151.76,200.04) and (152.41,198.58) .. (153.63,197.75) .. controls (154.84,196.92) and (156.42,196.87) .. (157.68,197.63) .. controls (158.13,196.77) and (158.95,196.17) .. (159.89,196.02) .. controls (160.83,195.87) and (161.79,196.19) .. (162.47,196.87) .. controls (162.85,196.09) and (163.6,195.57) .. (164.45,195.49) .. controls (165.3,195.4) and (166.13,195.78) .. (166.65,196.47) .. controls (167.34,195.64) and (168.43,195.29) .. (169.46,195.58) .. controls (170.49,195.86) and (171.27,196.72) .. (171.45,197.79) .. controls (172.3,198.02) and (173,198.62) .. (173.38,199.43) .. controls (173.76,200.23) and (173.78,201.17) .. (173.44,201.99) .. controls (174.27,203.09) and (174.46,204.57) .. (173.95,205.86) .. controls (173.43,207.15) and (172.29,208.06) .. (170.94,208.26) .. controls (170.93,209.47) and (170.28,210.58) .. (169.24,211.16) .. controls (168.2,211.75) and (166.93,211.71) .. (165.92,211.07) .. controls (165.5,212.52) and (164.29,213.59) .. (162.83,213.81) .. controls (161.36,214.03) and (159.91,213.37) .. (159.08,212.11) .. controls (158.08,212.73) and (156.87,212.91) .. (155.73,212.61) .. controls (154.59,212.31) and (153.62,211.55) .. (153.04,210.5) .. controls (152.01,210.62) and (151.01,210.08) .. (150.54,209.13) .. controls (150.08,208.19) and (150.24,207.05) .. (150.94,206.28) .. controls (150.03,205.73) and (149.56,204.63) .. (149.78,203.56) .. controls (150.01,202.49) and (150.88,201.7) .. (151.94,201.58) ; \\draw  [draw opacity=0] (150.94,206.28) .. controls (151.38,206.54) and (151.88,206.66) .. (152.38,206.62)(153.04,210.5) .. controls (153.25,210.47) and (153.46,210.42) .. (153.66,210.34)(159.08,212.11) .. controls (158.93,211.88) and (158.8,211.63) .. (158.71,211.37)(165.92,211.07) .. controls (166,210.81) and (166.05,210.53) .. (166.08,210.26)(170.94,208.26) .. controls (170.95,206.97) and (170.23,205.79) .. (169.1,205.23)(173.44,201.99) .. controls (173.25,202.43) and (172.97,202.82) .. (172.62,203.13)(171.45,197.79) .. controls (171.49,197.96) and (171.5,198.14) .. (171.5,198.32)(166.65,196.47) .. controls (166.48,196.68) and (166.33,196.91) .. (166.23,197.16)(162.47,196.87) .. controls (162.38,197.06) and (162.31,197.26) .. (162.27,197.47)(157.68,197.63) .. controls (157.95,197.79) and (158.2,197.98) .. (158.42,198.2)(151.96,201.53) .. controls (151.98,201.73) and (152.03,201.93) .. (152.09,202.13) ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 103; green, 183; blue, 16 }  ,fill opacity=1 ] (37.89,204.21) .. controls (37.6,202.07) and (38.54,199.95) .. (40.29,198.75) .. controls (42.05,197.56) and (44.32,197.49) .. (46.15,198.58) .. controls (46.79,197.34) and (47.97,196.48) .. (49.34,196.27) .. controls (50.7,196.05) and (52.08,196.51) .. (53.06,197.5) .. controls (53.61,196.37) and (54.69,195.61) .. (55.91,195.49) .. controls (57.14,195.37) and (58.34,195.91) .. (59.09,196.91) .. controls (60.08,195.72) and (61.66,195.21) .. (63.15,195.62) .. controls (64.63,196.03) and (65.75,197.27) .. (66.02,198.81) .. controls (67.24,199.15) and (68.26,200.01) .. (68.81,201.18) .. controls (69.35,202.34) and (69.38,203.69) .. (68.89,204.88) .. controls (70.09,206.47) and (70.37,208.6) .. (69.62,210.46) .. controls (68.88,212.32) and (67.23,213.64) .. (65.28,213.93) .. controls (65.26,215.67) and (64.33,217.28) .. (62.83,218.12) .. controls (61.33,218.96) and (59.5,218.91) .. (58.04,217.98) .. controls (57.43,220.08) and (55.68,221.62) .. (53.57,221.94) .. controls (51.46,222.26) and (49.36,221.31) .. (48.17,219.49) .. controls (46.72,220.38) and (44.97,220.64) .. (43.33,220.2) .. controls (41.69,219.77) and (40.29,218.67) .. (39.44,217.16) .. controls (37.96,217.34) and (36.52,216.55) .. (35.84,215.19) .. controls (35.17,213.83) and (35.4,212.18) .. (36.42,211.07) .. controls (35.1,210.27) and (34.42,208.69) .. (34.75,207.15) .. controls (35.07,205.61) and (36.33,204.45) .. (37.85,204.29) ; \\draw  [draw opacity=0] (36.42,211.07) .. controls (37.05,211.45) and (37.77,211.62) .. (38.5,211.56)(39.44,217.16) .. controls (39.75,217.12) and (40.06,217.04) .. (40.35,216.92)(48.17,219.49) .. controls (47.95,219.15) and (47.77,218.79) .. (47.62,218.42)(58.04,217.98) .. controls (58.16,217.6) and (58.23,217.21) .. (58.26,216.81)(65.28,213.93) .. controls (65.29,212.07) and (64.26,210.36) .. (62.62,209.55)(68.89,204.88) .. controls (68.62,205.51) and (68.22,206.07) .. (67.7,206.52)(66.02,198.81) .. controls (66.07,199.07) and (66.09,199.33) .. (66.09,199.59)(59.09,196.91) .. controls (58.84,197.21) and (58.64,197.54) .. (58.48,197.9)(53.06,197.5) .. controls (52.92,197.77) and (52.83,198.05) .. (52.76,198.35)(46.15,198.58) .. controls (46.53,198.81) and (46.89,199.09) .. (47.21,199.41)(37.89,204.21) .. controls (37.92,204.5) and (37.99,204.79) .. (38.07,205.08) ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 244; green, 215; blue, 166 }  ,fill opacity=1 ] (49.33,215) .. controls (67.47,202.73) and (103.15,191.5) .. (167.87,190.6) .. controls (232.58,189.7) and (206.52,210.55) .. (263.2,215.27) .. controls (319.88,219.98) and (479.21,215.92) .. (471.2,223.93) .. controls (463.19,231.95) and (567.2,241.27) .. (444.53,257.27) .. controls (321.87,273.27) and (97.87,277.93) .. (60.53,261.93) .. controls (23.2,245.93) and (31.2,227.27) .. (49.33,215) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=0.68 ] (49.33,215) .. controls (67.47,202.73) and (103.15,191.5) .. (167.87,190.6) .. controls (232.58,189.7) and (206.52,210.55) .. (263.2,215.27) .. controls (319.88,219.98) and (479.21,215.92) .. (471.2,223.93) .. controls (463.19,231.95) and (527.2,232.6) .. (404.53,248.6) .. controls (320.65,245.95) and (246.56,218.08) .. (149.2,235.27) .. controls (129.87,253.93) and (87.15,251.21) .. (60.53,261.93) .. controls (19.2,250.6) and (31.2,227.27) .. (49.33,215) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.13 ] (65.33,230.33) .. controls (83.47,218.07) and (103.2,203.13) .. (145.87,217.13) .. controls (188.53,231.13) and (222.52,225.89) .. (279.2,230.6) .. controls (335.88,235.31) and (385.21,228.45) .. (377.2,236.47) .. controls (369.19,244.48) and (422.53,243.8) .. (357.2,247.8) .. controls (291.87,251.8) and (240.75,245.43) .. (199.2,245.13) .. controls (157.65,244.84) and (146.53,248.47) .. (105.87,253.8) .. controls (65.2,259.13) and (47.2,242.6) .. (65.33,230.33) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (148.27,102.4) -- (172.27,102.4) .. controls (174.53,102.4) and (176.37,104.24) .. (176.37,106.5) -- (176.37,122.9) -- (174.16,122.9) -- (174.16,107.22) .. controls (174.16,105.94) and (173.13,104.91) .. (171.85,104.91) -- (148.68,104.91) .. controls (147.41,104.91) and (146.37,105.94) .. (146.37,107.22) -- (146.37,122.9) -- (144.17,122.9) -- (144.17,106.5) .. controls (144.17,104.24) and (146,102.4) .. (148.27,102.4) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (141.37,121.9) -- (134.87,135.9) -- (166.87,136.9) -- (362.87,236.4) -- (424.37,236.4) -- (420.87,221.4) -- (371.87,221.9) -- (176.37,121.9) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (143.07,129.15) .. controls (143.07,127.36) and (144.53,125.9) .. (146.32,125.9) .. controls (148.12,125.9) and (149.57,127.36) .. (149.57,129.15) .. controls (149.57,130.94) and (148.12,132.4) .. (146.32,132.4) .. controls (144.53,132.4) and (143.07,130.94) .. (143.07,129.15) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (153.07,129.15) .. controls (153.07,127.36) and (154.53,125.9) .. (156.32,125.9) .. controls (158.12,125.9) and (159.57,127.36) .. (159.57,129.15) .. controls (159.57,130.94) and (158.12,132.4) .. (156.32,132.4) .. controls (154.53,132.4) and (153.07,130.94) .. (153.07,129.15) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (163.07,129.15) .. controls (163.07,127.36) and (164.53,125.9) .. (166.32,125.9) .. controls (168.12,125.9) and (169.57,127.36) .. (169.57,129.15) .. controls (169.57,130.94) and (168.12,132.4) .. (166.32,132.4) .. controls (164.53,132.4) and (163.07,130.94) .. (163.07,129.15) -- cycle ;
                             		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (141.37,122.9) -- (176.37,122.9) ;
                             		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (176.37,122.9) -- (371.87,222.9) ;
                             		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (371.87,222.9) -- (420.87,222.4) ;
                             		\\draw  [color={rgb, 255:red, 29; green, 81; blue, 144 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (370.77,235.9) -- (424.37,236.4) -- (402.37,243.4) -- (340.87,243.4) -- (153.27,138.4) -- (172.77,136.4) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 249; green, 212; blue, 184 }  ,fill opacity=1 ] (201.9,133.67) .. controls (205.64,133.55) and (205.07,134.62) .. (207.02,135.81) .. controls (206.56,136.54) and (206.2,137.48) .. (205.99,138.68) .. controls (206.4,140.67) and (207.42,143.39) .. (209.17,146.98) .. controls (209.97,147.43) and (211.11,148.01) .. (212.64,148.74) .. controls (212.35,149.59) and (212.15,150.57) .. (212.05,151.71) .. controls (211.66,151.27) and (211.32,150.78) .. (211.04,150.25) .. controls (210.14,151.04) and (209.61,152.17) .. (209.57,153.71) .. controls (206.57,153.27) and (204.67,152.56) .. (204.72,151.28) .. controls (204.84,148.23) and (202.18,144.95) .. (199.97,139.13) .. controls (200.53,137.24) and (201.22,135.43) .. (201.9,133.67) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 16; green, 150; blue, 120 }  ,fill opacity=1 ] (185.71,147.68) .. controls (194.71,141.07) and (200.19,143.15) .. (210.2,147.3) .. controls (208.86,148.34) and (207.95,149.34) .. (207.4,150.32) .. controls (206.17,149.62) and (205.16,149.06) .. (204.34,148.63) .. controls (200.22,150.58) and (199.19,152.63) .. (200.18,154.79) .. controls (201.31,154.49) and (202.66,154.57) .. (204.18,154.94) .. controls (202.08,157.13) and (202.46,154.29) .. (200.94,159.02) .. controls (193.39,154.86) and (189.42,156.18) .. (185.71,147.68) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 248; green, 197; blue, 28 }  ,fill opacity=1 ] (195.96,123.49) .. controls (207.29,117.83) and (202.49,120.85) .. (204.38,125.01) .. controls (201.84,125.31) and (206.84,128.6) .. (207.02,135.81) .. controls (205.54,135.63) and (204.41,135.61) .. (203.85,135.89) .. controls (203.01,137.56) and (202.93,140.16) .. (204,144.09) .. controls (200.41,146.55) and (196.07,143.15) .. (190.78,145.6) .. controls (185.49,142.01) and (186.45,137.34) .. (191.91,135.78) .. controls (191.45,133.67) and (185.38,133.32) .. (185.68,131.62) .. controls (187.57,127.65) and (190.16,124.63) .. (195.96,123.49) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 249; green, 212; blue, 184 }  ,fill opacity=1 ] (217.31,114.24) .. controls (216.36,115.17) and (215.24,116.64) .. (214.24,118.56) .. controls (215.42,125.2) and (207.67,127.84) .. (201.25,124.44) .. controls (205.21,127.46) and (198.03,130.11) .. (195.96,123.49) .. controls (196.33,122.17) and (197,121.52) .. (196.52,119.9) .. controls (180.08,104.79) and (216.62,96.79) .. (217.31,114.24) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (192.44,100.82) .. controls (190.48,97.8) and (192.46,99.61) .. (194.82,98.55) .. controls (196.02,96.93) and (198.36,95.64) .. (201.4,94.66) .. controls (203.23,94.07) and (196.35,97.79) .. (198.6,97.42) .. controls (215.56,94.65) and (216.55,104.98) .. (221.65,107.62) .. controls (221.65,109.56) and (220.03,107.88) .. (219.57,108.76) .. controls (218.66,110.52) and (218.19,112.4) .. (218.25,114.05) .. controls (216.21,110.66) and (214.7,108.37) .. (212.28,106.74) .. controls (207.83,103.73) and (213.25,108.51) .. (214.66,110.84) .. controls (215.49,112.19) and (207.95,104.56) .. (209.94,107.81) .. controls (210.48,108.7) and (209.62,108.76) .. (208.62,108.8) .. controls (207.22,108.86) and (204.99,103.22) .. (206.73,105.54) .. controls (207.28,106.29) and (205.99,108.16) .. (204.58,110.22) .. controls (204.1,110.92) and (203.13,111.26) .. (202,111.42) .. controls (199.05,111.83) and (200.1,113.45) .. (200.87,114.43) .. controls (195.58,105.17) and (192.18,115.75) .. (197.25,116.94) .. controls (197.15,117.94) and (196.93,118.95) .. (196.52,119.9) .. controls (186.7,115.75) and (190.48,106.68) .. (187.43,111.01) .. controls (187.57,106.6) and (189.32,103.2) .. (192.44,100.82) -- cycle ;
                             		\\draw    (207.86,112.04) .. controls (207.99,111.54) and (210.41,110.31) .. (211.83,112.35) ;
                             		\\draw    (214.59,114.32) .. controls (214.89,113.7) and (216.94,112.62) .. (216.93,115.56) ;
                             		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (207.75,115.24) .. controls (207.99,114.21) and (208.74,113.5) .. (209.43,113.66) .. controls (210.12,113.82) and (210.48,114.79) .. (210.24,115.83) .. controls (210,116.86) and (209.24,117.57) .. (208.55,117.41) .. controls (207.87,117.25) and (207.5,116.28) .. (207.75,115.24) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (208.47,114.79) .. controls (208.56,114.4) and (208.9,114.15) .. (209.22,114.23) .. controls (209.55,114.3) and (209.74,114.68) .. (209.65,115.06) .. controls (209.56,115.45) and (209.22,115.7) .. (208.9,115.62) .. controls (208.57,115.55) and (208.38,115.17) .. (208.47,114.79) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (213.58,116.76) .. controls (213.73,115.99) and (214.22,115.46) .. (214.66,115.58) .. controls (215.1,115.7) and (215.34,116.42) .. (215.18,117.2) .. controls (215.02,117.98) and (214.54,118.51) .. (214.1,118.39) .. controls (213.65,118.27) and (213.42,117.54) .. (213.58,116.76) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (214.04,116.42) .. controls (214.1,116.13) and (214.32,115.95) .. (214.53,116) .. controls (214.73,116.06) and (214.86,116.34) .. (214.8,116.63) .. controls (214.74,116.92) and (214.52,117.1) .. (214.32,117.05) .. controls (214.11,116.99) and (213.99,116.71) .. (214.04,116.42) -- cycle ;
                             		\\draw    (212.57,118.74) .. controls (213.39,118.41) and (216.02,118.82) .. (213.3,121.29) ;
                             		\\draw [fill={rgb, 255:red, 143; green, 48; blue, 60 }  ,fill opacity=1 ]   (206.08,120.28) .. controls (206.25,124.53) and (209.5,124.46) .. (211.52,121.95) ;
                             		\\draw [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (206.73,120.55) .. controls (208.15,122.5) and (210.13,122.55) .. (210.9,121.8) ;
                             		\\draw [color={rgb, 255:red, 152; green, 108; blue, 34 }  ,draw opacity=1 ]   (191.91,135.78) -- (193.88,130.86) ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.36 ]   (190.17,126.33) .. controls (192.93,124.25) and (195.5,127.08) .. (194.18,129.16) ;
                             		\\draw    (198.49,145.41) -- (204.34,148.63) ;
                             		\\draw    (204,144.09) -- (202.27,146.92) ;
                             		\\draw  [fill={rgb, 255:red, 249; green, 212; blue, 184 }  ,fill opacity=1 ] (185.68,131.62) .. controls (189.38,132.19) and (189.61,133.51) .. (191.31,135.04) .. controls (190.72,135.66) and (190.2,136.53) .. (189.77,137.67) .. controls (189.82,139.7) and (190.32,142.56) .. (191.39,146.41) .. controls (192.1,147) and (193.12,147.78) .. (194.48,148.77) .. controls (194.05,149.55) and (193.68,150.48) .. (193.37,151.58) .. controls (193.06,151.08) and (192.82,150.54) .. (192.64,149.96) .. controls (191.61,150.57) and (190.89,151.59) .. (190.57,153.1) .. controls (187.7,152.12) and (185.96,151.08) .. (186.24,149.83) .. controls (186.91,146.85) and (184.88,143.15) .. (183.77,137.01) .. controls (184.66,135.26) and (184.69,133.23) .. (185.68,131.62) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 249; green, 212; blue, 184 }  ,fill opacity=1 ] (210.2,147.3) .. controls (212.22,147.81) and (215.11,148.91) .. (218.17,150.45) .. controls (225.38,161.34) and (228.9,162.9) .. (230.61,165.44) .. controls (231.67,167.02) and (229.47,165.44) .. (227.77,169.41) .. controls (222.26,161.14) and (215.69,162.01) .. (213.56,157.15) .. controls (212.85,155.51) and (210.84,154.01) .. (206.05,154.1) .. controls (207.28,150.72) and (207.56,148.96) .. (210.2,147.3) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 249; green, 212; blue, 184 }  ,fill opacity=1 ] (203.1,149) .. controls (205.11,149.51) and (208,150.61) .. (211.07,152.15) .. controls (218.28,163.04) and (221.8,164.6) .. (223.5,167.14) .. controls (224.56,168.72) and (222.37,167.14) .. (220.67,171.11) .. controls (215.15,162.84) and (208.59,163.71) .. (206.46,158.85) .. controls (205.74,157.21) and (203.74,155.71) .. (198.94,155.8) .. controls (200.17,152.42) and (200.45,150.66) .. (203.1,149) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (220.86,164.31) -- (223.5,167.14) -- (220.67,171.11) -- (217.08,166.95) -- (218.78,164.87) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (227.96,162.61) -- (230.61,165.44) -- (227.77,169.41) -- (224.18,165.25) -- (225.88,163.17) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (231.74,164.12) .. controls (233.11,163.35) and (235.01,162.59) .. (237.3,161.87) .. controls (238.92,161.13) and (241.91,162.33) .. (240.42,163.68) .. controls (236.78,169.38) and (233.39,173.66) .. (230.9,173.36) .. controls (228.17,171.52) and (226.55,169.73) .. (226.96,167.91) .. controls (228.38,167.9) and (229.78,167.51) .. (228.69,165.28) .. controls (229.94,163.3) and (230.68,164.02) .. (231.74,164.12) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 210; green, 203; blue, 203 }  ,fill opacity=1 ] (239.38,163.4) .. controls (240.62,162.46) and (240.95,162.9) .. (241.28,163.4) .. controls (238.13,168.39) and (235.32,171.74) .. (231.58,173.3) .. controls (230.8,173.39) and (231.25,173) .. (230.56,172.83) .. controls (235.48,170.73) and (236.75,165.67) .. (239.38,163.4) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (236.67,166.17) .. controls (236.63,166.14) and (236.6,166.11) .. (236.57,166.07) .. controls (235.58,165.07) and (235.59,163.45) .. (236.59,162.47) .. controls (237.59,161.48) and (239.2,161.49) .. (240.19,162.5) .. controls (240.23,162.54) and (240.27,162.58) .. (240.3,162.62) -- cycle ;
                             		\\draw    (230.95,165.73) -- (234.1,163.94) ;
                             		\\draw    (233.45,165.34) -- (233.32,163.32) ;
                             		\\draw    (232.67,165.81) -- (232.54,163.79) ;
                             		\\draw    (231.87,166.15) -- (231.74,164.12) ;
                             		\\draw    (232.82,170.94) -- (236.67,166.17) ;
                             		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (224.56,166.01) .. controls (225.93,165.24) and (227.83,164.48) .. (230.12,163.76) .. controls (231.74,163.02) and (234.73,164.22) .. (233.24,165.57) .. controls (229.6,171.27) and (226.21,175.55) .. (223.72,175.25) .. controls (220.99,173.41) and (219.37,171.62) .. (219.78,169.8) .. controls (221.2,169.79) and (222.6,169.4) .. (221.51,167.17) .. controls (222.76,165.19) and (223.5,165.91) .. (224.56,166.01) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 210; green, 203; blue, 203 }  ,fill opacity=1 ] (232.2,165.28) .. controls (233.44,164.35) and (233.77,164.79) .. (234.1,165.28) .. controls (230.95,170.28) and (228.14,173.63) .. (224.4,175.19) .. controls (223.62,175.28) and (224.07,174.89) .. (223.38,174.72) .. controls (228.3,172.62) and (229.57,167.56) .. (232.2,165.28) -- cycle ;
                             		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (229.49,168.06) .. controls (229.45,168.03) and (229.42,167.99) .. (229.39,167.96) .. controls (228.4,166.96) and (228.41,165.34) .. (229.41,164.36) .. controls (230.41,163.37) and (232.02,163.38) .. (233.01,164.39) .. controls (233.05,164.43) and (233.09,164.47) .. (233.12,164.51) -- cycle ;
                             		\\draw    (223.77,167.62) -- (226.92,165.83) ;
                             		\\draw    (226.27,167.23) -- (226.14,165.21) ;
                             		\\draw    (225.49,167.7) -- (225.36,165.67) ;
                             		\\draw    (224.69,168.04) -- (224.56,166.01) ;
                             		\\draw    (225.64,172.83) -- (229.49,168.06) ;
                             		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (152.37,139.4) -- (105.27,242.4) -- (95.77,242.4) -- (142.57,139.15) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (126.27,109.4) -- (150.27,109.4) .. controls (152.53,109.4) and (154.37,111.24) .. (154.37,113.5) -- (154.37,129.9) -- (152.16,129.9) -- (152.16,114.22) .. controls (152.16,112.94) and (151.13,111.91) .. (149.85,111.91) -- (126.68,111.91) .. controls (125.41,111.91) and (124.37,112.94) .. (124.37,114.22) -- (124.37,129.9) -- (122.17,129.9) -- (122.17,113.5) .. controls (122.17,111.24) and (124,109.4) .. (126.27,109.4) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (119.37,129.9) -- (112.87,142.9) -- (144.87,143.9) -- (340.87,243.4) -- (402.37,243.4) -- (398.87,228.4) -- (349.87,228.9) -- (154.37,128.9) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (131.07,136.15) .. controls (131.07,134.36) and (132.53,132.9) .. (134.32,132.9) .. controls (136.12,132.9) and (137.57,134.36) .. (137.57,136.15) .. controls (137.57,137.94) and (136.12,139.4) .. (134.32,139.4) .. controls (132.53,139.4) and (131.07,137.94) .. (131.07,136.15) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (141.07,136.15) .. controls (141.07,134.36) and (142.53,132.9) .. (144.32,132.9) .. controls (146.12,132.9) and (147.57,134.36) .. (147.57,136.15) .. controls (147.57,137.94) and (146.12,139.4) .. (144.32,139.4) .. controls (142.53,139.4) and (141.07,137.94) .. (141.07,136.15) -- cycle ;
                             		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (119.37,129.9) -- (154.37,129.9) ;
                             		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (154.37,129.9) -- (349.87,229.9) ;
                             		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (349.87,229.9) -- (398.87,229.4) ;
                             		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (111.65,158.36) -- (137.29,156.9) .. controls (137.67,156.88) and (138.03,157.88) .. (138.1,159.13) .. controls (138.17,160.39) and (137.93,161.42) .. (137.55,161.44) -- (111.91,162.9) .. controls (111.53,162.92) and (111.17,161.92) .. (111.1,160.67) .. controls (111.02,159.42) and (111.27,158.38) .. (111.65,158.36) .. controls (112.02,158.34) and (112.39,159.34) .. (112.46,160.59) .. controls (112.53,161.85) and (112.28,162.88) .. (111.91,162.9) ;
                             		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (103.15,175.86) -- (128.79,174.4) .. controls (129.17,174.38) and (129.53,175.38) .. (129.6,176.63) .. controls (129.67,177.89) and (129.43,178.92) .. (129.05,178.94) -- (103.41,180.4) .. controls (103.03,180.42) and (102.67,179.42) .. (102.6,178.17) .. controls (102.52,176.92) and (102.77,175.88) .. (103.15,175.86) .. controls (103.52,175.84) and (103.89,176.84) .. (103.96,178.09) .. controls (104.03,179.35) and (103.78,180.38) .. (103.41,180.4) ;
                             		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (94.65,194.86) -- (120.29,193.4) .. controls (120.67,193.38) and (121.03,194.38) .. (121.1,195.63) .. controls (121.17,196.89) and (120.93,197.92) .. (120.55,197.94) -- (94.91,199.4) .. controls (94.53,199.42) and (94.17,198.42) .. (94.1,197.17) .. controls (94.02,195.92) and (94.27,194.88) .. (94.65,194.86) .. controls (95.02,194.84) and (95.39,195.84) .. (95.46,197.09) .. controls (95.53,198.35) and (95.28,199.38) .. (94.91,199.4) ;
                             		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (86.65,213.86) -- (112.29,212.4) .. controls (112.67,212.38) and (113.03,213.38) .. (113.1,214.63) .. controls (113.17,215.89) and (112.93,216.92) .. (112.55,216.94) -- (86.91,218.4) .. controls (86.53,218.42) and (86.17,217.42) .. (86.1,216.17) .. controls (86.02,214.92) and (86.27,213.88) .. (86.65,213.86) .. controls (87.02,213.84) and (87.39,214.84) .. (87.46,216.09) .. controls (87.53,217.35) and (87.28,218.38) .. (86.91,218.4) ;
                             		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (78.15,232.36) -- (103.79,230.9) .. controls (104.17,230.88) and (104.53,231.88) .. (104.6,233.13) .. controls (104.67,234.39) and (104.43,235.42) .. (104.05,235.44) -- (78.41,236.9) .. controls (78.03,236.92) and (77.67,235.92) .. (77.6,234.67) .. controls (77.52,233.42) and (77.77,232.38) .. (78.15,232.36) .. controls (78.52,232.34) and (78.89,233.34) .. (78.96,234.59) .. controls (79.03,235.85) and (78.78,236.88) .. (78.41,236.9) ;
                             		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (126.87,133.4) -- (75.97,244.4) -- (66.97,244.4) -- (117.37,133.4) -- cycle ;
                             		\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (119.62,135.9) .. controls (119.62,134.11) and (121.07,132.65) .. (122.87,132.65) .. controls (124.66,132.65) and (126.12,134.11) .. (126.12,135.9) .. controls (126.12,137.69) and (124.66,139.15) .. (122.87,139.15) .. controls (121.07,139.15) and (119.62,137.69) .. (119.62,135.9) -- cycle ;
                             		\\draw [color={rgb, 255:red, 84; green, 111; blue, 146 }  ,draw opacity=1 ]   (146.17,147.5) -- (103.87,239.9) ;
                             		\\draw [color={rgb, 255:red, 84; green, 111; blue, 146 }  ,draw opacity=1 ]   (121.45,139.96) -- (73.87,244.9) ;
                             		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (153.47,134.12) -- (353.57,237) ;
                             		\\draw  [dash pattern={on 4.5pt off 4.5pt}]  (153.47,134.12) -- (153.47,237) ;
                             		\\draw  [dash pattern={on 4.5pt off 4.5pt}]  (154.47,237) -- (353.57,237) ;
                             		\\draw    (200.94,159.02) -- (200.94,189) ;
                             		\\draw [shift={(200.94,192)}, rotate = 270] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
                             		\\draw (150.87,136.4) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$A$};
                             		\\draw (352.37,229.4) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$B$};
                             		\\draw (185.2,173.5) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$\\vec{P}$};
                             	\\end{tikzpicture} }
                             \\end{center}''' % (m, str_d))


            ######################################################################## Nhận biết ############################################

            # Các đáp án
            nb_da_1_d = '\\True Công thức tính độ lớn của trọng lực là $P = mg$, với $g = %s$ m/s$^2$' % (str_g)
            nb_da_1_s = 'Công thức tính độ lớn của trọng lực là $P = \\frac{m}{g}$, với $g = %s$ m/s$^2$' % (str_g)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Công thức tính độ lớn của trọng lực là $P = mg$, với $g = %s$ m/s$^2$.''' % (str_g))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Độ lớn của trọng lực là $%s$ N' % (str_P)
            th_da_1_s = 'Độ lớn của trọng lực là $%s$ N' % (str(round(P + 10, 1)).replace('.', ','))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Độ lớn của trọng lực của em nhỏ tạo ra khi chơi cầu trượt là:\\\\
            $P = mg = %s \\cdot %s = %s$ N.''' % (m, str_g, str_P))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)


            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Góc tạo bởi trọng lực $\\vec{P}$ và độ dịch chuyển $\\vec{d}$ là $%s^\\circ$' % (beta)
            vd_da_1_s = 'Góc tạo bởi trọng lực $\\vec{P}$ và độ dịch chuyển $\\vec{d}$ là $30^\\circ$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Trọng lực $\\vec{P}$ có phương thẳng đứng, hướng xuống. Độ dịch chuyển $\\vec{d}$ dọc theo mặt phẳng nghiêng góc $30^\\circ$ so với phương ngang. Do đó, góc tạo bởi trọng lực $\\vec{P}$ và độ dịch chuyển $\\vec{d}$ là $90^\\circ - 30^\\circ = 60^\\circ$.''')

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)


            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Công sinh bởi trọng lực $\\vec{P}$ khi em nhỏ và chị của em trượt hết chiều dài cầu trượt có tổng bằng $%s$ J. Biết chị của em nhỏ nặng $%s$ kg' % (str_A_total, m1)
            vdc_da_1_s = 'Công sinh bởi trọng lực $\\vec{P}$ khi em nhỏ và chị của em trượt hết chiều dài cầu trượt có tổng bằng $%s$ J. Biết chị của em nhỏ nặng $%s$ kg' % (str_A_total_false, m1)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Công sinh ra khi em nhỏ trượt hết chiều dài cầu trượt là:\\\\
            $A = P \\cdot d \\cdot \\cos(\\vec{P}, \\vec{d}) = %s \\cdot %s \\cdot \\cos 60^\\circ = %s$ J.\\\\
            Độ lớn trọng lực của chị em nhỏ tạo ra khi chơi cầu trượt là:\\\\
            $P_1 = m_1 \\cdot g = %s \\cdot %s = %s$ N.\\\\
            Công sinh ra khi chị của em nhỏ trượt hết chiều dài cầu trượt là:\\\\
            $A_1 = P_1 \\cdot d \\cdot \\cos(\\vec{P}_1, \\vec{d}) = %s \\cdot %s \\cdot \\cos 60^\\circ = %s$ J.\\\\
            Tổng công sinh ra: $A + A_1 = %s + %s = %s$ J.''' % (str_P, str_d, str_A, m1, str_g, str_P1, str_P1, str_d, str_A1, str_A, str_A1, str_A_total))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
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

