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


def bt_dang10_p2_b2_c2_hh12(self):
            # Khai báo biến
            # Hàm phụ trợ để hiển thị dấu của tọa độ trong phương trình
            def fmt_num(val):
                if val < 0:
                    return "+%s" % (-val)
                elif val > 0:
                    return "-%s" % (val)
                else:
                    return ""

            # Chọn ngẫu nhiên cấu hình (t1, t2, c_coeff)
            configs = [
                (10, 20, 5), # Giống y hệt ảnh gốc
                (5, 15, 5),
                (10, 10, 10),
                (15, 5, 5),
                (20, 10, 5)
            ]
            t1, t2, c_coeff = random.choice(configs)

            # Tính toán tọa độ A, B
            xA = 10 + 3 * t1
            yA = -5 - t1
            zA = -5 + 2 * t1

            xB = -5 + 3 * t2
            yB = 10 - t2
            zB = 25 + 2 * t2

            c_val = "%s\\sqrt{6}" % (c_coeff)
            hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (197.54,247.26) -- (275.54,242.6) -- (182.87,228.6) -- (241.54,229.26) -- (152.87,209.93) -- (192.37,211.73) -- (135.03,196.4) -- (165.7,197.07) -- (114.37,183.07) -- (151.7,187.73) -- (55.7,152.4) -- (372.37,247.73) -- (362.61,265.65) -- (290.87,262.6) -- (312.87,254.6) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (214.54,253.93) -- (292.54,249.26) -- (199.87,235.26) -- (258.54,235.93) -- (169.87,216.6) -- (209.37,218.4) -- (152.03,203.07) -- (182.7,203.73) -- (131.37,189.73) -- (168.7,194.4) -- (72.7,159.07) -- (389.37,254.4) -- (379.61,272.32) -- (307.87,269.26) -- (329.87,261.26) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.54 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (150.85,124.87) .. controls (150.85,122.85) and (151.79,121.21) .. (152.95,121.21) .. controls (154.11,121.21) and (155.05,122.85) .. (155.05,124.87) .. controls (155.05,126.89) and (154.11,128.53) .. (152.95,128.53) .. controls (151.79,128.53) and (150.85,126.89) .. (150.85,124.87) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (146.3,102.07) -- (146.77,102.07) -- (146.77,144.07) -- (146.3,144.07) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (145.68,110.4) -- (147.25,110.4) -- (147.25,144.07) -- (145.68,144.07) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (145.2,115.46) -- (147.74,115.46) -- (147.74,143.24) -- (145.2,143.24) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (158,110.56) -- (157.99,111.4) -- (135.37,110.82) -- (135.38,109.99) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (159.1,118.98) -- (159.09,119.71) -- (134.03,119.07) -- (134.04,118.34) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (160.04,128.09) -- (160.05,127.06) -- (132.9,126.37) -- (132.88,127.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (147.74,104.03) -- (147.71,105.66) -- (145.03,105.59) -- (145.05,103.96) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (148.22,106.97) -- (148.21,107.68) -- (144.53,107.59) -- (144.54,106.87) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (143.75,108.6) -- (143.73,110.24) -- (141.04,110.17) -- (141.06,108.53) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (152.69,108.6) -- (152.66,110.24) -- (149.98,110.17) -- (150,108.53) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (147.27,109.11) -- (147.25,110.4) -- (145.29,110.35) -- (145.3,109.06) -- cycle ;
            	\draw    (155.95,107.95) -- (155.95,110.4) ;
            	\draw    (157.03,107.79) -- (157.03,110.24) ;
            	\draw    (149.06,106.48) -- (149.06,110.24) ;
            	\draw    (136.63,107.13) -- (136.63,109.58) ;
            	\draw    (137.47,107.13) -- (137.47,109.58) ;
            	\draw    (140.37,110.89) -- (145.32,114.48) ;
            	\draw    (147.49,114.48) -- (151.36,111.54) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (140.61,116.77) -- (140.59,118.41) -- (137.9,118.34) -- (137.92,116.7) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (153.17,117.1) -- (153.15,118.73) -- (150.46,118.66) -- (150.48,117.03) -- cycle ;
            	\draw    (134.82,115.63) -- (134.82,118.08) ;
            	\draw    (135.9,115.79) -- (135.9,118.24) ;
            	\draw    (158.12,116.28) -- (158.12,118.73) ;
            	\draw    (154.74,114.65) -- (154.86,118.73) ;
            	\draw    (148.82,114.48) -- (148.82,118.57) ;
            	\draw    (144.48,119.39) -- (144.48,139.97) ;
            	\draw    (152.81,119.71) -- (148.1,123.14) ;
            	\draw    (139.52,119.39) -- (145.2,122.82) ;
            	\draw    (139.26,115.1) -- (139.26,117.55) ;
            	\draw    (151.82,115.43) -- (151.82,117.88) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (138.44,124.45) -- (138.42,126.08) -- (135.73,126.02) -- (135.75,124.38) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (144.72,124.78) -- (144.69,126.41) -- (142.01,126.34) -- (142.03,124.71) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (153.53,124.94) -- (153.51,126.57) -- (150.82,126.51) -- (150.85,124.87) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (158.73,125.1) -- (158.7,126.74) -- (156.02,126.67) -- (156.04,125.04) -- cycle ;
            	\draw    (134.45,127.23) -- (144.48,139.97) ;
            	\draw    (136.87,127.88) -- (144.48,139.97) ;
            	\draw    (139.04,127.72) -- (145.2,141.44) ;
            	\draw    (142.18,127.55) -- (145.2,141.44) ;
            	\draw    (134.09,123.63) -- (134.09,126.08) ;
            	\draw    (140.97,122.65) -- (140.97,126.41) ;
            	\draw    (149.43,124.29) -- (149.43,126.74) ;
            	\draw    (158,122.82) -- (158,125.27) ;
            	\draw    (154.92,119.06) -- (155.46,126.08) ;
            	\draw    (156.07,119.55) -- (155.46,126.08) ;
            	\draw    (158.73,127.88) -- (155.22,137.52) ;
            	\draw    (160.04,128.09) -- (155.22,137.52) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (149.07,129.19) -- (151.6,129.19) -- (151.6,142.1) -- (149.07,142.1) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.54 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (176.44,106.91) .. controls (176.44,102.64) and (178.43,99.19) .. (180.87,99.19) .. controls (183.32,99.19) and (185.31,102.64) .. (185.31,106.91) .. controls (185.31,111.17) and (183.32,114.63) .. (180.87,114.63) .. controls (178.43,114.63) and (176.44,111.17) .. (176.44,106.91) -- cycle ;
            	\draw  [fill={rgb, 255:red, 101; green, 110; blue, 111 }  ,fill opacity=1 ] (367.77,175.2) -- (317.27,165.2) -- (316.97,160.4) -- (292.77,167.7) -- (367.77,186.7) -- cycle ;
            	\draw  [fill={rgb, 255:red, 101; green, 110; blue, 111 }  ,fill opacity=1 ] (444.27,202.7) -- (385.27,187.2) -- (384.47,180.4) -- (360.27,187.7) -- (435.27,206.7) -- cycle ;
            	\draw  [fill={rgb, 255:red, 98; green, 113; blue, 115 }  ,fill opacity=1 ] (369.97,184.4) -- (452.47,206.9) -- (352.67,216) -- (202.47,178.4) -- (104.47,144.9) -- (181.47,140.9) -- (316.97,160.4) -- (302.47,163.9) -- (384.47,180.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (352.67,216) -- (452.47,206.9) -- (449.97,218.4) -- (352.97,226.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (104.47,144.9) -- (202.47,178.4) -- (352.67,216) -- (352.97,226.9) -- (205.97,185.9) -- (105.47,149.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 106; green, 116; blue, 118 }  ,fill opacity=1 ] (350.17,226) .. controls (383.97,225.9) and (420.47,219.4) .. (449.97,218.4) .. controls (430.47,225.9) and (382.47,234.9) .. (378.97,270.4) .. controls (377.47,243.4) and (373.47,236.4) .. (350.17,226) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (105.47,149.4) .. controls (144.47,163.9) and (212.37,189.4) .. (352.97,226.9) .. controls (381.47,242.4) and (375.97,249.4) .. (378.97,270.4) .. controls (284.97,242.4) and (176.13,214.47) .. (146.47,188.8) .. controls (119.13,170.47) and (122.47,164.4) .. (105.47,149.4) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.68 ]   (265.57,154.5) -- (310.77,160.9) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (302.47,163.9) -- (310.77,160.9) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.68 ]   (302.47,163.9) -- (378.27,180.9) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.68 ]   (363.27,184.4) -- (378.27,180.9) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.68 ]   (363.27,184.4) -- (443.27,206.4) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.68 ]   (353.27,213.4) -- (443.27,206.4) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.68 ]   (169.27,142.4) -- (363.27,184.4) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.68 ]   (174.77,142.4) -- (369.97,184.4) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.68 ]   (135.77,144.4) -- (374.27,211.9) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.68 ]   (138.77,143.9) -- (379.77,211.4) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.68 ]   (386.27,203.4) -- (407.27,208.9) ;
            	\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (341.77,191.4) -- (386.27,203.4) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.68 ]   (313.27,183.4) -- (341.77,191.4) ;
            	\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (269.77,172.9) -- (313.27,183.4) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (250.77,168.4) -- (269.77,172.9) ;
            	\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (207.27,156.9) -- (250.77,168.4) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (188.27,152.4) -- (207.27,156.9) ;
            	\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (149.27,142.4) -- (188.27,152.4) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.68 ] [dash pattern={on 4.5pt off 4.5pt}]  (263.77,156.9) -- (302.47,163.9) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ]   (300.27,174.9) -- (402.77,201.4) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ]   (353.77,217.9) -- (450.27,209.4) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ]   (353.77,219.9) -- (450.27,211.4) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.54 ] (387.93,229.16) .. controls (388.93,228.19) and (390.88,227.66) .. (392.26,227.99) .. controls (393.65,228.31) and (393.96,229.36) .. (392.95,230.33) .. controls (391.94,231.3) and (390,231.82) .. (388.61,231.5) .. controls (387.22,231.18) and (386.92,230.13) .. (387.93,229.16) -- cycle ;
            	\draw   (398.61,226.69) .. controls (399.17,226.15) and (400.25,225.86) .. (401.02,226.04) .. controls (401.79,226.22) and (401.96,226.8) .. (401.4,227.34) .. controls (400.84,227.88) and (399.76,228.17) .. (398.99,227.99) .. controls (398.22,227.81) and (398.05,227.23) .. (398.61,226.69) -- cycle ;
            	\draw   (380.36,228.44) .. controls (380.92,227.9) and (382,227.61) .. (382.77,227.79) .. controls (383.54,227.97) and (383.71,228.55) .. (383.15,229.09) .. controls (382.59,229.63) and (381.51,229.92) .. (380.74,229.74) .. controls (379.97,229.56) and (379.8,228.98) .. (380.36,228.44) -- cycle ;
            	\draw   (385.81,228.66) .. controls (387.67,226.87) and (391.25,225.91) .. (393.8,226.51) .. controls (396.36,227.1) and (396.93,229.04) .. (395.07,230.83) .. controls (393.21,232.61) and (389.63,233.58) .. (387.07,232.98) .. controls (384.51,232.38) and (383.95,230.45) .. (385.81,228.66) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (197.93,177.47) -- (204.81,178.84) -- (204.93,183.5) -- (198.36,181.74) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (204.12,178.65) -- (202.91,180.81) -- (199.83,180.37) -- (199.27,177.95) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (204.6,179.8) -- (211.47,181.17) -- (211.6,185.83) -- (205.03,184.08) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (210.79,180.98) -- (209.57,183.14) -- (206.49,182.7) -- (205.94,180.29) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (211.6,181.8) -- (218.47,183.17) -- (218.6,187.83) -- (212.03,186.08) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (217.79,182.98) -- (216.57,185.14) -- (213.49,184.7) -- (212.94,182.29) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (218.93,183.47) -- (225.81,184.84) -- (225.93,189.5) -- (219.36,187.74) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (225.12,184.65) -- (223.91,186.81) -- (220.83,186.37) -- (220.27,183.95) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (226.6,185.8) -- (233.47,187.17) -- (233.6,191.83) -- (227.03,190.08) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (232.79,186.98) -- (231.57,189.14) -- (228.49,188.7) -- (227.94,186.29) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (234.6,188.13) -- (242.13,189.65) -- (242.27,194.8) -- (235.07,192.86) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (241.38,189.44) -- (240.04,191.83) -- (236.68,191.34) -- (236.06,188.67) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (242.93,190.8) -- (250.46,192.31) -- (250.6,197.47) -- (243.4,195.53) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (249.71,192.11) -- (248.37,194.5) -- (245.02,194.01) -- (244.4,191.34) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (250.27,191.8) -- (258.92,193.54) -- (259.08,199.47) -- (250.81,197.24) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (258.06,193.3) -- (256.52,196.05) -- (252.66,195.49) -- (251.95,192.42) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (258.27,193.47) -- (268.41,195.51) -- (268.6,202.45) -- (258.9,199.84) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (267.4,195.23) -- (265.6,198.45) -- (261.07,197.79) -- (260.24,194.19) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (267.6,196.13) -- (277.74,198.17) -- (277.93,205.12) -- (268.23,202.51) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (276.74,197.89) -- (274.93,201.12) -- (270.41,200.46) -- (269.57,196.86) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (276.6,198.47) -- (286.74,200.51) -- (286.93,207.45) -- (277.23,204.84) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (285.74,200.23) -- (283.93,203.45) -- (279.41,202.79) -- (278.57,199.19) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (286.93,201.13) -- (297.08,203.17) -- (297.27,210.12) -- (287.56,207.51) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (296.07,202.89) -- (294.27,206.12) -- (289.74,205.46) -- (288.91,201.86) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (296.27,203.47) -- (306.41,205.51) -- (306.6,212.45) -- (296.9,209.84) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (305.4,205.23) -- (303.6,208.45) -- (299.07,207.79) -- (298.24,204.19) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (304.27,205.47) -- (315.56,207.74) -- (315.77,215.47) -- (304.97,212.56) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (314.44,207.43) -- (312.43,211.01) -- (307.39,210.28) -- (306.46,206.27) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (314.6,208.13) -- (326.27,210.48) -- (326.48,218.47) -- (315.33,215.46) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (325.11,210.16) -- (323.03,213.86) -- (317.83,213.11) -- (316.87,208.97) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (326.6,211.13) -- (338.71,213.57) -- (338.93,221.86) -- (327.35,218.74) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (337.51,213.24) -- (335.35,217.08) -- (329.95,216.3) -- (328.95,212) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (338.27,214.47) -- (351.55,217.14) -- (351.8,226.23) -- (339.09,222.81) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (350.23,216.77) -- (347.87,220.99) -- (341.94,220.13) -- (340.85,215.41) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.52 ]   (313.27,219.8) .. controls (319.47,229.8) and (334.13,238.47) .. (338.13,254.8) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.52 ]   (270.93,207.13) .. controls (277.13,217.13) and (294.13,228.13) .. (298.13,244.47) ;
            	\draw   (192.8,185.47) -- (212.03,186.08) -- (235.07,192.86) -- (234.47,201.47) -- (217.13,198.8) -- (208.8,194.8) -- (192.8,188.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.53 ] (214.47,187.47) -- (233.6,191.83) -- (211.47,190.8) -- (197.13,186.8) -- cycle ;
            	\draw    (194.47,187.13) -- (210.47,192.8) ;
            	\draw    (210.47,192.8) -- (232.47,193.47) ;
            	\draw    (210.47,192.8) -- (208.8,194.8) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.52 ]   (231.47,205.47) .. controls (238.13,212.13) and (241.47,220.8) .. (244.8,231.27) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.68 ] [dash pattern={on 4.5pt off 4.5pt}]  (112.47,146.8) -- (207.47,177.23) ;
            	\draw  [color={rgb, 255:red, 176; green, 166; blue, 44 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.32 ] (174.3,155.88) -- (197.55,162.88) -- (175.55,165.88) -- (152.3,158.13) -- cycle ;
            	\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (125.8,144.13) -- (157.8,154.8) ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (104.85,148.56) -- (122.58,154.83) -- (121.14,167.38) -- (104.35,160.19) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (120.84,154.07) -- (116.76,159.4) -- (108.79,157.06) -- (108.21,150.36) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (116.18,154.89) -- (133.91,161.16) -- (132.47,173.71) -- (115.68,166.52) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (132.17,160.4) -- (128.1,165.74) -- (120.12,163.4) -- (119.55,156.7) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (131.51,158.22) -- (149.24,164.5) -- (147.8,177.04) -- (131.01,169.85) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (147.5,163.74) -- (143.43,169.07) -- (135.46,166.73) -- (134.88,160.03) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (147.51,167.22) -- (165.24,173.5) -- (163.8,186.04) -- (147.01,178.85) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (163.5,172.74) -- (159.43,178.07) -- (151.46,175.73) -- (150.88,169.03) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (159.85,167.89) -- (178.58,175.06) -- (176.8,190.13) -- (159.09,181.84) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.47 ] (176.75,174.19) -- (172,180.56) -- (164.18,178.11) -- (163.39,169.99) -- cycle ;
            	\draw    (186.13,180.47) -- (176.8,190.13) ;
            	\draw    (163.13,195.13) -- (139.13,178.8) ;
            	\draw  [fill={rgb, 255:red, 102; green, 113; blue, 115 }  ,fill opacity=1 ] (104.47,144.9) -- (173.07,168.47) -- (163.5,172.74) -- (92.07,145.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 102; green, 113; blue, 115 }  ,fill opacity=1 ] (93.44,145.2) -- (163.5,172.74) -- (163.4,176.13) -- (93.4,148.13) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (163.5,172.74) -- (173.07,168.47) -- (173.07,172.8) -- (163.4,176.13) -- cycle ;
            	\draw   (247.29,202.48) .. controls (246.56,201.41) and (246.54,200.76) .. (247.26,201.01) -- (252.44,202.82) .. controls (253.16,203.08) and (254.34,204.14) .. (255.07,205.21) -- (255.07,205.21) .. controls (255.81,206.27) and (255.82,206.93) .. (255.1,206.68) -- (249.92,204.86) .. controls (249.2,204.61) and (248.02,203.54) .. (247.29,202.48) -- cycle ;
            	\draw   (282.62,212.15) .. controls (281.89,211.08) and (281.88,210.42) .. (282.59,210.68) -- (287.78,212.49) .. controls (288.49,212.74) and (289.67,213.81) .. (290.41,214.87) -- (290.41,214.87) .. controls (291.14,215.94) and (291.15,216.6) .. (290.43,216.34) -- (285.25,214.53) .. controls (284.53,214.28) and (283.36,213.21) .. (282.62,212.15) -- cycle ;
            	\draw   (186.16,181.94) .. controls (185.43,180.87) and (185.41,180.21) .. (186.13,180.47) -- (191.31,182.28) .. controls (192.03,182.53) and (193.21,183.6) .. (193.94,184.67) -- (193.94,184.67) .. controls (194.68,185.73) and (194.69,186.39) .. (193.97,186.14) -- (188.79,184.32) .. controls (188.07,184.07) and (186.89,183) .. (186.16,181.94) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.21 ] (237.87,194.4) -- (351.8,226.23) -- (374.37,241.9) -- (378.97,270.4) -- (308.87,249.9) -- (246.87,222.9) -- (227.37,207.4) -- (224.87,214.4) -- (206.87,207.9) -- (192.87,194.4) -- (195.37,214.4) -- (176.87,206.4) -- (170.87,195.4) -- (158.37,195.9) -- (151.13,186.97) -- (138.37,181.4) -- (124.87,168.4) -- (176.8,190.13) -- (182.87,181.9) -- (215.28,199.16) -- (234.47,201.47) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (166.84,58.8) -- (167.85,58.8) -- (167.85,147.4) -- (166.84,147.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (165.55,76.38) -- (168.86,76.38) -- (168.86,147.4) -- (165.55,147.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (164.53,87.06) -- (169.88,87.06) -- (169.88,145.65) -- (164.53,145.65) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (191.54,76.72) -- (191.51,78.48) -- (143.79,77.27) -- (143.81,75.51) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (193.85,94.47) -- (193.83,96.02) -- (140.96,94.67) -- (140.99,93.12) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (195.84,113.7) -- (195.87,111.53) -- (138.58,110.07) -- (138.55,112.24) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (169.88,62.94) -- (169.83,66.38) -- (164.17,66.24) -- (164.21,62.79) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (170.9,69.14) -- (170.88,70.65) -- (163.13,70.45) -- (163.15,68.94) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (161.48,72.59) -- (161.43,76.03) -- (155.76,75.89) -- (155.81,72.44) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (180.33,72.59) -- (180.28,76.03) -- (174.61,75.89) -- (174.66,72.44) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (168.9,73.66) -- (168.86,76.38) -- (164.71,76.27) -- (164.75,73.55) -- cycle ;
            	\draw    (187.21,71.21) -- (187.21,76.38) ;
            	\draw    (189.5,70.86) -- (189.5,76.03) ;
            	\draw    (172.69,68.11) -- (172.69,76.03) ;
            	\draw    (146.45,69.48) -- (146.45,74.65) ;
            	\draw    (148.23,69.48) -- (148.23,74.65) ;
            	\draw    (154.34,77.41) -- (164.79,84.99) ;
            	\draw    (169.37,84.99) -- (177.53,78.79) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (154.85,89.82) -- (154.81,93.27) -- (149.14,93.12) -- (149.19,89.67) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (181.35,90.51) -- (181.3,93.96) -- (175.63,93.81) -- (175.68,90.36) -- cycle ;
            	\draw    (142.63,87.41) -- (142.63,92.58) ;
            	\draw    (144.92,87.75) -- (144.92,92.92) ;
            	\draw    (191.79,88.79) -- (191.79,93.96) ;
            	\draw    (184.66,85.34) -- (184.91,93.96) ;
            	\draw    (172.18,84.99) -- (172.18,93.61) ;
            	\draw    (163.01,95.33) -- (163.01,138.76) ;
            	\draw    (180.58,96.02) -- (170.65,103.26) ;
            	\draw    (152.56,95.33) -- (164.53,102.57) ;
            	\draw    (152,86.3) -- (152,91.47) ;
            	\draw    (178.49,86.99) -- (178.49,92.16) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (150.27,106.02) -- (150.22,109.47) -- (144.55,109.32) -- (144.6,105.87) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (163.51,106.71) -- (163.47,110.15) -- (157.8,110.01) -- (157.85,106.56) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (182.11,107.05) -- (182.06,110.5) -- (176.39,110.35) -- (176.44,106.91) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (193.06,107.4) -- (193.02,110.84) -- (187.35,110.7) -- (187.4,107.25) -- cycle ;
            	\draw    (141.86,111.88) -- (163.01,138.76) ;
            	\draw    (146.96,113.26) -- (163.01,138.76) ;
            	\draw    (151.54,112.91) -- (164.53,141.86) ;
            	\draw    (158.17,112.57) -- (164.53,141.86) ;
            	\draw    (141.1,104.29) -- (141.1,109.46) ;
            	\draw    (155.62,102.23) -- (155.62,110.15) ;
            	\draw    (173.45,105.67) -- (173.45,110.84) ;
            	\draw    (191.54,102.57) -- (191.54,107.74) ;
            	\draw    (185.04,94.64) -- (186.19,109.46) ;
            	\draw    (187.46,95.68) -- (186.19,109.46) ;
            	\draw    (193.06,113.26) -- (185.68,133.59) ;
            	\draw    (195.84,113.71) -- (185.68,133.59) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (172.7,116.01) -- (178.03,116.01) -- (178.03,143.24) -- (172.7,143.24) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (166.7,137.07) -- (195.87,137.07) -- (195.87,150.91) -- (166.7,150.91) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.44 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (148.53,136.4) -- (166.7,137.07) -- (166.7,150.91) -- (148.2,146.07) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (164.27,128.73) -- (198.93,128.73) -- (198.93,137.07) -- (164.27,137.07) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.44 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (153.6,129.07) -- (164.27,128.73) -- (164.27,137.07) -- (153.93,136.4) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.64 ]   (165.07,131.93) -- (198.13,131.87) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.64 ]   (165.27,134.4) -- (198.33,134.33) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.64 ]   (154.27,131.73) -- (165.07,131.93) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.64 ]   (153.93,134.4) -- (165.27,134.4) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.44 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (160.6,124.73) -- (203.27,124.07) -- (198.93,128.73) -- (164.27,128.73) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ] (170.17,143.4) -- (174.77,143.4) -- (174.77,150.33) -- (170.17,150.33) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ] (181.28,143.99) -- (185.88,143.99) -- (185.88,150.92) -- (181.28,150.92) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (188.93,140.57) .. controls (188.93,139.19) and (190.05,138.07) .. (191.43,138.07) .. controls (192.81,138.07) and (193.93,139.19) .. (193.93,140.57) .. controls (193.93,141.95) and (192.81,143.07) .. (191.43,143.07) .. controls (190.05,143.07) and (188.93,141.95) .. (188.93,140.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (196.43,139.57) .. controls (196.43,138.19) and (197.55,137.07) .. (198.93,137.07) .. controls (200.31,137.07) and (201.43,138.19) .. (201.43,139.57) .. controls (201.43,140.95) and (200.31,142.07) .. (198.93,142.07) .. controls (197.55,142.07) and (196.43,140.95) .. (196.43,139.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (161.77,139.57) .. controls (161.77,138.19) and (162.89,137.07) .. (164.27,137.07) .. controls (165.65,137.07) and (166.77,138.19) .. (166.77,139.57) .. controls (166.77,140.95) and (165.65,142.07) .. (164.27,142.07) .. controls (162.89,142.07) and (161.77,140.95) .. (161.77,139.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.55 ] (160.27,143.07) -- (160.93,149.73) -- (151.6,147.07) -- (152.6,141.73) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (377.52,78.66) -- (374.42,80.3) -- (361.96,83.41) -- (360.53,82.86) -- (360.9,81.4) -- (373.69,78.11) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (332.03,85.27) .. controls (342.99,79.79) and (363.6,76.83) .. (369.96,82.31) .. controls (362.32,92.18) and (336.41,91.61) .. (331.88,89.94) .. controls (330.73,88.03) and (330.65,86.44) .. (332.03,85.27) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (369.96,82.31) .. controls (361.96,90.17) and (349.9,91.81) .. (332.04,90.21) .. controls (329.43,87.24) and (333.09,84.14) .. (331.99,79.94) .. controls (341.74,78.69) and (348.99,78.15) .. (353.92,79.57) .. controls (350.99,87.98) and (362.69,85.42) .. (369.96,82.31) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (378.36,59.65) -- (380.67,59.65) -- (380.67,67.33) -- (378.36,67.33) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (403.47,53.26) -- (419.84,52.89) -- (400,56.18) -- cycle ;
            	\draw  [fill={rgb, 255:red, 98; green, 110; blue, 111 }  ,fill opacity=1 ] (299.39,88.16) -- (295.3,95.47) -- (285.62,95.28) -- (285.98,89.62) -- cycle ;
            	\draw  [fill={rgb, 255:red, 54; green, 59; blue, 60 }  ,fill opacity=1 ] (275.57,78.47) .. controls (273.01,82.49) and (275.28,86.77) .. (277.47,90.97) .. controls (269.9,93.09) and (263.51,83.96) .. (275.57,78.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (303.78,63.13) .. controls (316.93,59.11) and (320.95,56.91) .. (343.06,47.6) .. controls (351.65,47.41) and (364.99,47.05) .. (380.52,44.12) .. controls (386.47,45.43) and (403.91,49.42) .. (407.56,54.17) .. controls (402.63,60.2) and (375.95,66.41) .. (355.67,69.16) .. controls (350.74,68.97) and (346.72,67.22) .. (342.88,67.15) .. controls (338.13,67.15) and (336.67,67.51) .. (328.63,66.96) .. controls (317.12,69.16) and (317.12,70.43) .. (303.6,75.37) .. controls (283.68,77.74) and (278.2,71.71) .. (303.78,63.13) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (277.87,77.27) .. controls (303.23,79.79) and (309.63,70.65) .. (328.63,66.96) .. controls (332.28,67.4) and (337.22,67.58) .. (342.49,66.78) .. controls (347.96,68.1) and (355.02,68.88) .. (358.78,69.78) .. controls (354.76,71.24) and (356.12,74.2) .. (352.93,79.1) .. controls (348.47,82.09) and (335.68,85.93) .. (311.82,87.68) .. controls (296.56,88.6) and (293.36,91.52) .. (277.47,90.97) .. controls (272.9,87.32) and (271.99,80.74) .. (277.87,77.27) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (247.8,85.14) -- (279.59,81.43) -- (282.22,83.17) -- (271.69,84.48) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (245.75,70.43) -- (313.02,66.84) -- (306.78,69.7) -- (252.51,71.17) -- cycle ;
            	\draw [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ]   (313.02,66.84) -- (369.45,55.09) ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (306.78,69.7) -- (283.83,78.47) -- (240.63,72.63) -- (246.66,70.43) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (253.35,67.51) -- (249.77,69.7) -- (237.89,73.54) -- (236.47,72.99) -- (236.83,71.53) -- (249.51,67.51) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (293.18,60.2) -- (303.78,63.13) -- (289.89,68.24) -- (275.28,68.79) -- (275.09,66.23) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (277.47,38.28) -- (293.18,60.2) -- (276.04,65.87) -- (268.88,41.38) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (276.55,36.27) -- (277.47,38.28) -- (267.97,41.57) -- (267.24,39.92) -- cycle ;
            	\draw [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ]   (275.82,81.76) -- (283.83,78.47) ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (267.42,71.35) -- (266.51,74.82) -- (255.54,77.56) -- (256.09,73.91) -- cycle ;
            	\draw  [fill={rgb, 255:red, 147; green, 152; blue, 152 }  ,fill opacity=1 ] (343.06,47.6) .. controls (352.38,37.98) and (369.01,31.77) .. (380.52,44.12) .. controls (364.99,47.12) and (359.14,46.75) .. (343.06,47.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (342.49,66.78) .. controls (350.05,67.47) and (348.41,68.02) .. (358.28,69.48) .. controls (352.43,74.78) and (358.64,81) .. (344.75,78.62) .. controls (340.8,76.98) and (336.35,71.49) .. (342.49,66.78) -- cycle ;
            	\draw [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ]   (321.61,71.68) -- (341.46,66.82) ;
            	\draw [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ]   (328.56,69.85) -- (328.63,66.96) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.54 ] (343.36,68.02) .. controls (350.92,68.72) and (346.83,68.57) .. (356.69,70.03) .. controls (350.85,75.33) and (357.97,79.35) .. (345.73,77.71) .. controls (341.35,76.06) and (337.69,70.4) .. (343.36,68.02) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (277.47,38.28) -- (279.08,40.51) -- (269.57,43.98) -- (268.88,41.38) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (277.87,41.13) -- (289.86,61.52) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (272.15,42.83) -- (280.54,64.44) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 76; green, 86; blue, 87 }  ,fill opacity=1 ] (280.46,59.75) .. controls (280.36,59.41) and (280.55,59.05) .. (280.89,58.95) -- (285.77,57.5) .. controls (286.11,57.4) and (286.47,57.59) .. (286.57,57.93) -- (287.12,59.79) .. controls (287.22,60.13) and (287.03,60.49) .. (286.69,60.59) -- (281.81,62.04) .. controls (281.47,62.14) and (281.11,61.95) .. (281.01,61.61) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (276.58,49.83) -- (280.83,48.01) -- (281.87,50.44) -- (277.62,52.26) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 16; blue, 16 }  ,fill opacity=1 ] (276.73,50.13) -- (280.93,48.33) -- (281.05,48.59) -- (276.85,50.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 16; blue, 16 }  ,fill opacity=1 ] (277,50.71) -- (281.17,48.93) -- (281.27,49.17) -- (277.11,50.95) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 16; blue, 16 }  ,fill opacity=1 ] (277.19,51.23) -- (281.43,49.41) -- (281.55,49.68) -- (277.31,51.5) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 16; blue, 16 }  ,fill opacity=1 ] (277.41,51.76) -- (281.63,49.95) -- (281.74,50.21) -- (277.52,52.02) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 24; green, 81; blue, 149 }  ,fill opacity=1 ] (279.43,48.61) -- (280.83,48.01) -- (281.43,49.41) -- (280.03,50.01) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (289.86,61.52) -- (288.65,68.28) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (287.66,65.72) -- (283.72,67) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.53 ] (293.18,60.2) -- (303.78,63.13) -- (291.03,60.97) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (330.57,53.08) -- (327.75,58.78) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (327.75,58.78) -- (314.41,62.98) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (314.41,62.98) -- (311.31,67) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (326.83,60.97) .. controls (326.89,60.79) and (327.07,60.63) .. (327.25,60.61) -- (328.18,60.5) .. controls (328.35,60.48) and (328.45,60.61) .. (328.39,60.79) -- (327.83,62.58) .. controls (327.78,62.76) and (327.59,62.92) .. (327.42,62.94) -- (326.48,63.05) .. controls (326.31,63.07) and (326.21,62.94) .. (326.27,62.76) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (348.22,47.45) -- (346.75,50.56) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.41 ]   (346.75,50.56) -- (373.61,47.63) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.48 ]   (355.23,49.6) .. controls (355.52,53.11) and (353.7,55.67) .. (351.87,58.59) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (344.08,52.57) -- (346.78,52.14) -- (346.22,53.66) -- (344.3,55.5) -- (343.51,54.14) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.48 ]   (380.52,44.12) .. controls (367.77,47.27) and (368.31,63.89) .. (378.18,65.17) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.61 ] (373.08,52.72) .. controls (373.23,52.25) and (373.69,51.79) .. (374.1,51.7) -- (376.77,51.07) .. controls (377.18,50.98) and (377.4,51.28) .. (377.25,51.75) -- (377.25,51.75) .. controls (377.1,52.22) and (376.65,52.68) .. (376.23,52.78) -- (373.56,53.4) .. controls (373.15,53.5) and (372.94,53.19) .. (373.08,52.72) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (386.4,45.62) .. controls (378.91,45.62) and (373.61,59.14) .. (383.85,63.71) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.51 ] (374.53,47.59) .. controls (383.66,46.86) and (394.63,49.09) .. (405.3,54.17) .. controls (389.19,48.68) and (374.25,47.45) .. (372.2,50.74) .. controls (374.53,47.45) and (373.52,49.87) .. (374.53,47.59) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.27 ] (313.02,66.84) .. controls (326.25,63.89) and (356.58,57.68) .. (369.45,55.09) .. controls (361.6,57.78) and (350.26,60.75) .. (349.53,62.03) .. controls (350.81,64.59) and (381.63,62.34) .. (407.56,54.17) .. controls (402.45,59.87) and (377.6,65.9) .. (357.32,69.01) .. controls (351.29,68.83) and (349.09,66.63) .. (341.46,66.82) .. controls (333.36,68.86) and (320.15,73.58) .. (317.52,78.47) .. controls (309.37,75.4) and (290.11,78.86) .. (283.83,78.47) .. controls (275.59,78.58) and (266.94,74.67) .. (255.54,77.56) .. controls (253.53,77.29) and (256.93,75.42) .. (255.25,74.67) .. controls (252.52,73.46) and (244.87,73.25) .. (242.1,72.85) .. controls (242.72,71.85) and (244.19,70.99) .. (246.66,70.43) .. controls (247.47,69.97) and (304.07,69.92) .. (305.86,70.39) .. controls (308.84,68.89) and (311.78,67.43) .. (313.02,66.84) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (297.6,71.29) -- (305.28,79.84) -- (285.54,83.57) -- (284.23,75.04) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (279.59,81.43) .. controls (290.55,75.95) and (311.16,72.99) .. (317.52,78.47) .. controls (309.88,88.34) and (283.97,87.77) .. (279.44,86.11) .. controls (278.3,84.19) and (278.21,82.6) .. (279.59,81.43) -- cycle ;
            	\draw    (341.67,69.16) -- (355.93,70.98) ;
            	\draw    (343.03,69.34) .. controls (345.15,71.9) and (345.88,74.64) .. (346.97,77.56) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.32 ] (273.89,84.5) .. controls (277.92,84.23) and (277.1,83.18) .. (279.59,81.43) .. controls (280.37,80.88) and (283.33,80) .. (284.48,79.39) .. controls (285.73,77.98) and (282.83,75.96) .. (284.23,75.04) .. controls (291.06,73.54) and (294.72,71.9) .. (297.6,71.29) .. controls (298.37,72.39) and (298.53,74.16) .. (297.27,76.28) .. controls (296.29,77.94) and (295.84,78.13) .. (295.08,80.3) .. controls (293.06,86.12) and (304.4,82.68) .. (317.52,78.47) .. controls (322.19,79.18) and (336.97,75.26) .. (340.2,75.65) .. controls (341.31,75.78) and (343.76,80.78) .. (354.1,78.47) .. controls (345.15,83.96) and (329.8,86.88) .. (308.6,87.79) .. controls (287.59,91.08) and (290.33,90.9) .. (277.47,90.97) .. controls (274.98,88.71) and (275.17,87.98) .. (273.89,84.5) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (322.36,73.89) -- (329,72.54) -- (328.92,74.33) -- (322.28,75.68) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (323.87,74.47) .. controls (323.92,73.44) and (324.75,72.45) .. (325.72,72.25) .. controls (326.7,72.05) and (327.45,72.73) .. (327.41,73.75) .. controls (327.36,74.78) and (326.53,75.77) .. (325.55,75.97) .. controls (324.58,76.17) and (323.82,75.5) .. (323.87,74.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ,even odd rule] (325.15,74.21) .. controls (325.16,73.93) and (325.39,73.65) .. (325.66,73.59) .. controls (325.93,73.54) and (326.14,73.73) .. (326.13,74.01) .. controls (326.12,74.3) and (325.89,74.57) .. (325.62,74.63) .. controls (325.34,74.68) and (325.14,74.5) .. (325.15,74.21)(324.41,74.36) .. controls (324.45,73.65) and (325.02,72.96) .. (325.7,72.82) .. controls (326.38,72.68) and (326.9,73.15) .. (326.87,73.86) .. controls (326.83,74.57) and (326.26,75.26) .. (325.58,75.4) .. controls (324.9,75.54) and (324.38,75.07) .. (324.41,74.36) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.61 ] (332.7,72.09) .. controls (332.85,71.62) and (333.31,71.16) .. (333.72,71.06) -- (336.39,70.44) .. controls (336.8,70.35) and (337.02,70.65) .. (336.87,71.12) -- (336.87,71.12) .. controls (336.72,71.59) and (336.27,72.05) .. (335.85,72.15) -- (333.18,72.77) .. controls (332.77,72.86) and (332.56,72.56) .. (332.7,72.09) -- cycle ;
            	\draw    (351.25,41.02) .. controls (350.44,42.3) and (349.53,44.85) .. (350.26,47.05) ;
            	\draw    (352.45,40.83) .. controls (351.65,42.11) and (350.81,44.85) .. (351.54,47.05) ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (368.17,41.2) -- (379.75,43.58) -- (377.67,44.85) -- (364.88,46.32) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (357.97,41.28) .. controls (357.97,40.07) and (358.95,39.09) .. (360.16,39.09) .. controls (361.37,39.09) and (362.36,40.07) .. (362.36,41.28) .. controls (362.36,42.49) and (361.37,43.48) .. (360.16,43.48) .. controls (358.95,43.48) and (357.97,42.49) .. (357.97,41.28) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (357.41,45.1) .. controls (357.34,44.17) and (358.04,43.36) .. (358.97,43.3) -- (361.72,43.11) .. controls (362.65,43.04) and (363.46,43.74) .. (363.52,44.67) -- (363.64,46.35) .. controls (363.64,46.35) and (363.64,46.35) .. (363.64,46.35) -- (357.52,46.78) .. controls (357.52,46.78) and (357.52,46.78) .. (357.52,46.78) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (353.74,47.16) -- (354.86,42.99) -- (357.6,42.79) -- (359.31,46.75) -- cycle ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1.5]    (352.45,40.83) .. controls (357.17,38.68) and (357.7,42.66) .. (358.97,43.3) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.51 ] (361.99,38.13) .. controls (366.93,38.13) and (374.05,38.86) .. (378.8,43.79) .. controls (370.21,37.76) and (357.1,36.85) .. (355.05,40.14) .. controls (358.89,38.5) and (361.63,40.87) .. (361.99,38.13) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (118.18,101.71) -- (116.93,102.37) -- (111.92,103.62) -- (111.34,103.4) -- (111.49,102.81) -- (116.63,101.49) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (99.88,104.37) .. controls (104.29,102.16) and (112.58,100.97) .. (115.13,103.18) .. controls (112.06,107.14) and (101.65,106.92) .. (99.82,106.25) .. controls (99.37,105.48) and (99.33,104.84) .. (99.88,104.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (115.13,103.18) .. controls (111.92,106.34) and (107.07,107) .. (99.89,106.35) .. controls (98.84,105.16) and (100.31,103.91) .. (99.87,102.22) .. controls (103.79,101.72) and (106.7,101.51) .. (108.68,102.08) .. controls (107.51,105.45) and (112.21,104.43) .. (115.13,103.18) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (118.51,94.07) -- (119.44,94.07) -- (119.44,97.15) -- (118.51,97.15) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (128.61,91.5) -- (135.19,91.35) -- (127.21,92.67) -- cycle ;
            	\draw  [fill={rgb, 255:red, 98; green, 110; blue, 111 }  ,fill opacity=1 ] (86.77,105.53) -- (85.12,108.47) -- (81.23,108.39) -- (81.37,106.12) -- cycle ;
            	\draw  [fill={rgb, 255:red, 54; green, 59; blue, 60 }  ,fill opacity=1 ] (77.19,101.64) .. controls (76.16,103.25) and (77.07,104.97) .. (77.95,106.66) .. controls (74.91,107.51) and (72.34,103.84) .. (77.19,101.64) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (88.53,95.46) .. controls (93.82,93.85) and (95.43,92.97) .. (104.32,89.22) .. controls (107.77,89.15) and (113.14,89) .. (119.38,87.83) .. controls (121.77,88.35) and (128.78,89.96) .. (130.25,91.87) .. controls (128.27,94.29) and (117.54,96.79) .. (109.39,97.89) .. controls (107.41,97.82) and (105.79,97.11) .. (104.25,97.08) .. controls (102.34,97.08) and (101.75,97.23) .. (98.52,97.01) .. controls (93.89,97.89) and (93.89,98.4) .. (88.45,100.39) .. controls (80.45,101.34) and (78.24,98.92) .. (88.53,95.46) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (78.11,101.15) .. controls (88.31,102.16) and (90.88,98.49) .. (98.52,97.01) .. controls (99.99,97.18) and (101.97,97.26) .. (104.09,96.93) .. controls (106.29,97.47) and (109.13,97.78) .. (110.64,98.14) .. controls (109.02,98.73) and (109.57,99.92) .. (108.29,101.88) .. controls (106.5,103.09) and (101.35,104.63) .. (91.76,105.34) .. controls (85.63,105.71) and (84.34,106.88) .. (77.95,106.66) .. controls (76.11,105.19) and (75.75,102.55) .. (78.11,101.15) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (66.02,104.31) -- (78.8,102.83) -- (79.86,103.52) -- (75.63,104.05) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (65.2,98.4) -- (92.25,96.96) -- (89.73,98.11) -- (67.92,98.7) -- cycle ;
            	\draw [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ]   (92.25,96.96) -- (114.93,92.23) ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (89.73,98.11) -- (80.51,101.64) -- (63.14,99.28) -- (65.57,98.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (68.25,97.23) -- (66.81,98.11) -- (62.04,99.65) -- (61.47,99.43) -- (61.61,98.84) -- (66.71,97.23) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (84.27,94.29) -- (88.53,95.46) -- (82.95,97.52) -- (77.07,97.74) -- (77,96.71) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (77.95,85.47) -- (84.27,94.29) -- (77.38,96.57) -- (74.5,86.72) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (77.58,84.67) -- (77.95,85.47) -- (74.13,86.8) -- (73.84,86.14) -- cycle ;
            	\draw [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ]   (77.29,102.96) -- (80.51,101.64) ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (73.91,98.77) -- (73.54,100.17) -- (69.14,101.27) -- (69.36,99.8) -- cycle ;
            	\draw  [fill={rgb, 255:red, 147; green, 152; blue, 152 }  ,fill opacity=1 ] (104.32,89.22) .. controls (108.07,85.36) and (114.75,82.86) .. (119.38,87.83) .. controls (113.14,89.03) and (110.79,88.88) .. (104.32,89.22) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (104.09,96.93) .. controls (107.13,97.21) and (106.47,97.43) .. (110.44,98.02) .. controls (108.09,100.15) and (110.58,102.65) .. (105,101.69) .. controls (103.41,101.03) and (101.62,98.83) .. (104.09,96.93) -- cycle ;
            	\draw [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ]   (95.7,98.9) -- (103.67,96.95) ;
            	\draw [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ]   (98.49,98.17) -- (98.52,97.01) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.54 ] (104.44,97.43) .. controls (107.48,97.71) and (105.83,97.65) .. (109.8,98.24) .. controls (107.45,100.37) and (110.32,101.99) .. (105.39,101.33) .. controls (103.63,100.67) and (102.16,98.39) .. (104.44,97.43) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (77.95,85.47) -- (78.6,86.37) -- (74.78,87.77) -- (74.5,86.72) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (78.11,86.62) -- (82.93,94.82) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (75.81,87.3) -- (79.18,95.99) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 76; green, 86; blue, 87 }  ,fill opacity=1 ] (79.15,94.11) .. controls (79.11,93.97) and (79.19,93.83) .. (79.33,93.79) -- (81.29,93.2) .. controls (81.42,93.16) and (81.57,93.24) .. (81.61,93.38) -- (81.83,94.12) .. controls (81.87,94.26) and (81.79,94.41) .. (81.66,94.45) -- (79.7,95.03) .. controls (79.56,95.07) and (79.41,94.99) .. (79.37,94.85) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (77.59,90.12) -- (79.3,89.39) -- (79.72,90.37) -- (78.01,91.1) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 16; blue, 16 }  ,fill opacity=1 ] (77.65,90.24) -- (79.34,89.52) -- (79.39,89.62) -- (77.7,90.35) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 16; blue, 16 }  ,fill opacity=1 ] (77.76,90.47) -- (79.44,89.76) -- (79.48,89.85) -- (77.81,90.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 16; blue, 16 }  ,fill opacity=1 ] (77.84,90.68) -- (79.54,89.95) -- (79.59,90.06) -- (77.89,90.79) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 16; blue, 16 }  ,fill opacity=1 ] (77.93,90.9) -- (79.62,90.17) -- (79.67,90.27) -- (77.97,91) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 24; green, 81; blue, 149 }  ,fill opacity=1 ] (78.74,89.63) -- (79.3,89.39) -- (79.54,89.95) -- (78.98,90.19) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (82.93,94.82) -- (82.45,97.54) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (82.05,96.51) -- (80.46,97.02) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.53 ] (84.27,94.29) -- (88.53,95.46) -- (83.4,94.6) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (99.3,91.42) -- (98.17,93.72) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (98.17,93.72) -- (92.8,95.41) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (92.8,95.41) -- (91.55,97.02) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (97.8,94.6) .. controls (97.82,94.53) and (97.89,94.46) .. (97.96,94.45) -- (98.34,94.41) .. controls (98.41,94.4) and (98.45,94.45) .. (98.42,94.53) -- (98.2,95.24) .. controls (98.18,95.32) and (98.1,95.38) .. (98.03,95.39) -- (97.65,95.43) .. controls (97.59,95.44) and (97.55,95.39) .. (97.57,95.32) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ]   (106.39,89.16) -- (105.81,90.41) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.41 ]   (105.81,90.41) -- (116.6,89.24) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.48 ]   (109.21,90.03) .. controls (109.33,91.44) and (108.6,92.47) .. (107.86,93.64) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (104.73,91.22) -- (105.82,91.05) -- (105.59,91.66) -- (104.82,92.4) -- (104.5,91.85) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.48 ]   (119.38,87.83) .. controls (114.25,89.09) and (114.47,95.77) .. (118.44,96.29) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.61 ] (116.39,91.28) .. controls (116.45,91.09) and (116.63,90.91) .. (116.8,90.87) -- (117.87,90.62) .. controls (118.04,90.58) and (118.13,90.7) .. (118.07,90.89) -- (118.07,90.89) .. controls (118.01,91.08) and (117.82,91.27) .. (117.66,91.3) -- (116.58,91.55) .. controls (116.42,91.59) and (116.33,91.47) .. (116.39,91.28) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (121.75,88.43) .. controls (118.73,88.43) and (116.6,93.86) .. (120.72,95.7) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.51 ] (116.97,89.22) .. controls (120.64,88.92) and (125.05,89.82) .. (129.34,91.87) .. controls (122.87,89.66) and (116.86,89.16) .. (116.03,90.48) .. controls (116.97,89.16) and (116.57,90.14) .. (116.97,89.22) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.27 ] (92.25,96.96) .. controls (97.56,95.77) and (109.76,93.28) .. (114.93,92.23) .. controls (111.77,93.32) and (107.21,94.51) .. (106.92,95.02) .. controls (107.44,96.05) and (119.82,95.15) .. (130.25,91.87) .. controls (128.19,94.16) and (118.2,96.58) .. (110.05,97.83) .. controls (107.63,97.76) and (106.75,96.88) .. (103.67,96.95) .. controls (100.42,97.77) and (95.11,99.67) .. (94.05,101.64) .. controls (90.78,100.4) and (83.03,101.79) .. (80.51,101.64) .. controls (77.19,101.68) and (73.72,100.11) .. (69.14,101.27) .. controls (68.33,101.16) and (69.69,100.41) .. (69.02,100.11) .. controls (67.92,99.62) and (64.85,99.53) .. (63.73,99.37) .. controls (63.98,98.97) and (64.57,98.63) .. (65.57,98.4) .. controls (65.89,98.22) and (88.65,98.2) .. (89.36,98.38) .. controls (90.56,97.78) and (91.75,97.2) .. (92.25,96.96) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (86.05,98.75) -- (89.13,102.18) -- (81.2,103.68) -- (80.67,100.25) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 153; blue, 155 }  ,fill opacity=1 ] (78.8,102.83) .. controls (83.21,100.62) and (91.5,99.43) .. (94.05,101.64) .. controls (90.98,105.6) and (80.57,105.37) .. (78.74,104.7) .. controls (78.28,103.93) and (78.25,103.3) .. (78.8,102.83) -- cycle ;
            	\draw    (103.76,97.89) -- (109.49,98.62) ;
            	\draw    (104.31,97.96) .. controls (105.16,98.99) and (105.45,100.09) .. (105.89,101.27) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.32 ] (76.51,104.06) .. controls (78.13,103.95) and (77.8,103.53) .. (78.8,102.83) .. controls (79.12,102.6) and (80.31,102.25) .. (80.77,102) .. controls (81.27,101.44) and (80.11,100.63) .. (80.67,100.25) .. controls (83.42,99.65) and (84.88,98.99) .. (86.05,98.75) .. controls (86.35,99.19) and (86.42,99.9) .. (85.91,100.75) .. controls (85.52,101.42) and (85.33,101.5) .. (85.03,102.37) .. controls (84.22,104.71) and (88.78,103.32) .. (94.05,101.64) .. controls (95.93,101.92) and (101.87,100.34) .. (103.17,100.5) .. controls (103.62,100.55) and (104.6,102.56) .. (108.76,101.64) .. controls (105.16,103.84) and (98.99,105.01) .. (90.47,105.38) .. controls (82.02,106.7) and (83.12,106.63) .. (77.95,106.66) .. controls (76.95,105.75) and (77.02,105.45) .. (76.51,104.06) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (96,99.79) -- (98.67,99.25) -- (98.63,99.97) -- (95.97,100.51) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (96.61,100.03) .. controls (96.63,99.61) and (96.96,99.21) .. (97.35,99.13) .. controls (97.74,99.05) and (98.05,99.32) .. (98.03,99.74) .. controls (98.01,100.15) and (97.67,100.55) .. (97.28,100.63) .. controls (96.89,100.71) and (96.59,100.44) .. (96.61,100.03) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ,even odd rule] (97.12,99.92) .. controls (97.12,99.81) and (97.22,99.7) .. (97.33,99.67) .. controls (97.43,99.65) and (97.52,99.73) .. (97.51,99.84) .. controls (97.51,99.96) and (97.42,100.07) .. (97.31,100.09) .. controls (97.2,100.11) and (97.11,100.04) .. (97.12,99.92)(96.82,99.98) .. controls (96.84,99.69) and (97.07,99.42) .. (97.34,99.36) .. controls (97.61,99.31) and (97.82,99.49) .. (97.81,99.78) .. controls (97.8,100.07) and (97.56,100.34) .. (97.29,100.4) .. controls (97.02,100.45) and (96.81,100.27) .. (96.82,99.98) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.61 ] (100.16,99.07) .. controls (100.22,98.88) and (100.4,98.69) .. (100.57,98.66) -- (101.64,98.41) .. controls (101.8,98.37) and (101.89,98.49) .. (101.83,98.68) -- (101.83,98.68) .. controls (101.77,98.87) and (101.59,99.05) .. (101.42,99.09) -- (100.35,99.34) .. controls (100.18,99.38) and (100.1,99.26) .. (100.16,99.07) -- cycle ;
            	\draw    (107.61,86.58) .. controls (107.29,87.09) and (106.92,88.12) .. (107.22,89) ;
            	\draw    (108.1,86.5) .. controls (107.77,87.02) and (107.44,88.12) .. (107.73,89) ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (114.41,86.65) -- (119.07,87.6) -- (118.23,88.12) -- (113.09,88.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (110.31,86.68) .. controls (110.31,86.2) and (110.71,85.8) .. (111.2,85.8) .. controls (111.68,85.8) and (112.08,86.2) .. (112.08,86.68) .. controls (112.08,87.17) and (111.68,87.56) .. (111.2,87.56) .. controls (110.71,87.56) and (110.31,87.17) .. (110.31,86.68) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (110.09,88.22) .. controls (110.06,87.84) and (110.34,87.52) .. (110.72,87.49) -- (111.82,87.42) .. controls (112.2,87.39) and (112.52,87.67) .. (112.55,88.05) -- (112.59,88.72) .. controls (112.59,88.72) and (112.59,88.72) .. (112.59,88.72) -- (110.13,88.89) .. controls (110.13,88.89) and (110.13,88.89) .. (110.13,88.89) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (108.62,89.05) -- (109.06,87.37) -- (110.16,87.29) -- (110.85,88.88) -- cycle ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1.5]    (108.1,86.5) .. controls (109.99,85.64) and (110.21,87.24) .. (110.72,87.49) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.51 ] (111.93,85.42) .. controls (113.91,85.42) and (116.78,85.71) .. (118.69,87.69) .. controls (115.24,85.27) and (109.97,84.9) .. (109.14,86.22) .. controls (110.68,85.56) and (111.78,86.52) .. (111.93,85.42) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (175.37,129.63) -- (192.53,149.33) -- (166.7,150.91) -- (148.2,146.07) -- (164.27,128.73) -- cycle ;
            \end{tikzpicture}'''
            # Nội dung câu hỏi
            noidungcauhoi = (r'''\immini{Trong không gian $Oxyz$ cho trước, đơn vị trên mỗi trục là $1$ mét, có hai chiếc chiến đấu cơ từ hai vị trí $A(%s; %s; %s), B(%s; %s; %s)$ cần đáp xuống hai vị trí thuộc tàu sân bay hải quân để nạp nhiên liệu. Bề mặt chứa các đường băng trên tàu là mặt phẳng $(P): 3x - y + 2z - 25 = 0$.}{%s}''' 
                             % (xA, yA, zA, xB, yB, zB, hinhve))

            ######################################################################## Nhận biết ############################################
            # Phương trình qua A vuông góc P: VTCP là (3; -1; 2)
            eq_d = "\\frac{x%s}{3} = \\frac{y%s}{-1} = \\frac{z%s}{2}" % (fmt_num(xA), fmt_num(yA), fmt_num(zA))
            eq_s = "\\frac{x%s}{3} = \\frac{y%s}{1} = \\frac{z%s}{-2}" % (fmt_num(xA), fmt_num(yA), fmt_num(zA))

            # Các đáp án
            nb_da_1_d = '\\True Đường thẳng qua $A$ và vuông góc với mặt phẳng $(P)$ có phương trình chính tắc là $%s$' % (eq_d)
            nb_da_1_s = 'Đường thẳng qua $A$ và vuông góc với mặt phẳng $(P)$ có phương trình chính tắc là $%s$' % (eq_s)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Mặt phẳng $(P): 3x - y + 2z - 25 = 0$ có vectơ pháp tuyến $\\vec{n} = (3; -1; 2)$. \\\\
            Đường thẳng đi qua $A(%s; %s; %s)$ và vuông góc với $(P)$ nhận $\\vec{n} = (3; -1; 2)$ làm vectơ chỉ phương. \\\\
            Phương trình chính tắc của đường thẳng là $%s$.''' % (xA, yA, zA, eq_d))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Tính tổng khoảng cách
            sum_dist_exact = (t1 + t2) * math.sqrt(14)
            sum_dist_round = round(sum_dist_exact)
            sum_dist_fake = sum_dist_round - 2

            # Các đáp án
            th_da_1_d = '\\True Tổng khoảng cách từ hai vị trí chiến đấu cơ đến mặt phẳng chứa đường băng là $%sm$ (làm tròn đến hàng đơn vị mét)' % (sum_dist_round)
            th_da_1_s = 'Tổng khoảng cách từ hai vị trí chiến đấu cơ đến mặt phẳng chứa đường băng là $%sm$ (làm tròn đến hàng đơn vị mét)' % (sum_dist_fake)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            sum_dist_exact_str = str(round(sum_dist_exact, 2)).replace('.', ',')
            loigiai_th_1 = ('''Khoảng cách từ $A$ đến $(P)$ là $d(A, (P)) = \\frac{|3(%s) - (%s) + 2(%s) - 25|}{\\sqrt{3^2 + (-1)^2 + 2^2}} = %s\\sqrt{14}$. \\\\
            Khoảng cách từ $B$ đến $(P)$ là $d(B, (P)) = \\frac{|3(%s) - (%s) + 2(%s) - 25|}{\\sqrt{14}} = %s\\sqrt{14}$. \\\\
            Tổng khoảng cách là $d(A, (P)) + d(B, (P)) = %s\\sqrt{14} \\approx %sm \\approx %sm$.''' 
                            % (xA, yA, zA, t1, xB, yB, zB, t2, t1 + t2, sum_dist_exact_str, sum_dist_round))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Tọa độ A' đối xứng với A qua (P)
            # Do A được tạo từ H(10, -5, -5) với tham số t1, nên A' có tham số -t1
            xAp = 20 - xA
            yAp = -10 - yA
            zAp = -10 - zA

            # Các đáp án
            vd_da_1_d = '\\True Tọa độ điểm $A\'$ đối xứng với điểm $A$ qua mặt phẳng $(P)$ là $A\'(%s; %s; %s)$' % (xAp, yAp, zAp)
            vd_da_1_s = 'Tọa độ điểm $A\'$ đối xứng với điểm $A$ qua mặt phẳng $(P)$ là $A\'(%s; %s; %s)$' % (-xAp, yAp, zAp)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Gọi $H$ là hình chiếu vuông góc của $A$ lên $(P)$. \\\\
            Đường thẳng $AH$ có phương trình tham số $\\begin{cases} x = %s + 3t \\\\ y = %s - t \\\\ z = %s + 2t \\end{cases}$. \\\\
            Thay vào phương trình $(P)$ ta được $3(%s + 3t) - (%s - t) + 2(%s + 2t) - 25 = 0 \\Leftrightarrow 14t + %s = 0 \\Leftrightarrow t = -%s$. \\\\
            Suy ra $H(10; -5; -5)$. \\\\
            Điểm $A\'$ đối xứng với $A$ qua $(P)$ suy ra $H$ là trung điểm của đoạn $AA\'$. \\\\
            Tọa độ $A\'$ là $\\begin{cases} x_{A\'} = 2x_H - x_A = 20 - %s = %s \\\\ y_{A\'} = 2y_H - y_A = -10 - (%s) = %s \\\\ z_{A\'} = 2z_H - z_A = -10 - %s = %s \\end{cases}$. \\\\
            Vậy $A\'(%s; %s; %s)$.''' 
                            % (xA, yA, zA, xA, yA, zA, 14 * t1, t1, xA, xAp, yA, yAp, zA, zAp, xAp, yAp, zAp))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Tính tổng đường bay ngắn nhất
            HK_sq = 15**2 + 15**2 + 30**2 # HK = 15*sqrt(6)
            MN_coeff = c_coeff
            min_dist_exact = math.sqrt(14 * (t1 + t2)**2 + 6 * (15 - MN_coeff)**2)
            ans_vdc = round(min_dist_exact)
            ans_vdc_fake = ans_vdc + 5

            vdc_da_1_d = '\\True Người chỉ huy ở tàu sân bay phát tín hiệu để hai chiến đấu cơ đáp xuống các vị trí $M, N$ cách nhau $%sm$. Tổng đường bay ngắn nhất $AM + BN$ bằng $%sm$ (làm tròn đến hàng đơn vị)' % (c_val, ans_vdc)
            vdc_da_1_s = 'Người chỉ huy ở tàu sân bay phát tín hiệu để hai chiến đấu cơ đáp xuống các vị trí $M, N$ cách nhau $%sm$. Tổng đường bay ngắn nhất $AM + BN$ bằng $%sm$ (làm tròn đến hàng đơn vị)' % (c_val, ans_vdc_fake)

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            min_dist_exact_str = str(round(min_dist_exact, 2)).replace('.', ',')
            loigiai_vdc_1 = ('''Gọi $H(10; -5; -5)$ và $K(-5; 10; 25)$ lần lượt là hình chiếu vuông góc của $A$ và $B$ lên mặt phẳng $(P)$. \\\\
            Ta dễ dàng kiểm tra được $A, B$ nằm cùng phía so với mặt phẳng $(P)$. Điểm $A\'$ đối xứng với $A$ qua $(P)$. \\\\
            Ta có $AM + BN = A\'M + BN$. \\\\
            Tịnh tiến điểm $A\'$ theo vectơ $\\vec{MN}$ được điểm $A_1$, ta có $A\'M = A_1N$. \\\\
            Khi đó $AM + BN = A_1N + BN \\ge A_1B$. \\\\
            Dấu bằng xảy ra khi $N$ là giao điểm của $A_1B$ và mặt phẳng $(P)$. \\\\
            Khoảng cách hình chiếu: $HK = \\sqrt{(-5-10)^2 + (10 - (-5))^2 + (25 - (-5))^2} = 15\\sqrt{6}$. \\\\
            Khoảng cách nhỏ nhất $A_1B = \\sqrt{ (d(A, (P)) + d(B, (P)))^2 + (HK - MN)^2 } = \\sqrt{ (%s\\sqrt{14})^2 + (15\\sqrt{6} - %s\\sqrt{6})^2 }$. \\\\
            Suy ra $A_1B = \\sqrt{ %s + %s } \\approx %s \\approx %sm$.''' 
                             % (t1 + t2, MN_coeff, 14 * (t1 + t2)**2, 6 * (15 - MN_coeff)**2, min_dist_exact_str, ans_vdc))

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
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content 

