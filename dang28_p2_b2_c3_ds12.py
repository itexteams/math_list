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


def bt_dang28_p2_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến và tạo random
            while True:
                # Chọn T là tuổi thọ hữu ích (T = 4, 5, 6, 7)
                T = random.choice([4, 5, 6, 7])

                # Chọn N (hệ số của t^2 trong P'(t)). Đảm bảo (N * T^3) / 3 là số nguyên
                if T % 3 != 0:
                    N = random.choice([12, 15, 18, 21])
                else:
                    N = random.randint(10, 20)

                # Chọn M sao cho sqrt(M/N) xấp xỉ T nhưng nhỏ hơn T một chút 
                # (giống bài gốc sqrt(602/17) xấp xỉ 5.95 -> làm tròn T=6)
                offset = random.randint(2, 15)
                M = N * (T**2) - offset
                if M <= 0: 
                    continue

                # Sinh các hệ số a, b, c, d
                c = random.randint(30, 60)
                a = M + c
                b = random.randint(2, N - 2)
                d = N - b

                # Chọn năm khảo sát doanh thu (t1) sao cho R'(t1) > 0
                t1 = T + random.choice([2, 3, 4])
                if a > b * (t1**2):
                    break

            # Tính toán các kết quả cho đáp án
            cost_val = int(c * T + d * (T**3) / 3)
            profit_val = int(M * T - N * (T**3) / 3)


            hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.7,xscale=0.7]
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (198.7,200.9) -- (188.83,213.74) -- (139.75,214.02) -- (129.73,201.3) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (139.7,201.4) -- (168.2,151.07) -- (222.22,151.62) -- (249.69,202.51) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (289.83,78.2) -- (305.2,78.2) -- (305.2,194.85) -- (289.83,194.85) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (152.5,172) -- (253.3,172) -- (253.3,231.4) -- (152.5,231.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (161,181) -- (201.3,181) -- (201.3,221) -- (161,221) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (211.5,181) -- (244.3,181) -- (244.3,221) -- (211.5,221) -- cycle ;
            	\draw    (216.3,186.9) -- (240.3,186.9) ;
            	\draw    (216.3,191.4) -- (240.3,191.4) ;
            	\draw    (215.8,196.4) -- (239.8,196.4) ;
            	\draw    (215.9,201) -- (239.9,201) ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (253.8,131.5) -- (272.8,131.5) -- (272.8,172.4) -- (253.8,172.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (208,131.5) -- (253.8,131.5) -- (253.8,171.5) -- (208,171.5) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (214.5,137) -- (246.8,137) -- (246.8,155.1) -- (214.5,155.1) -- cycle ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (214.1,163.65) .. controls (214.1,161.74) and (215.64,160.2) .. (217.55,160.2) .. controls (219.46,160.2) and (221,161.74) .. (221,163.65) .. controls (221,165.56) and (219.46,167.1) .. (217.55,167.1) .. controls (215.64,167.1) and (214.1,165.56) .. (214.1,163.65) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (227.6,163.65) .. controls (227.6,161.74) and (229.14,160.2) .. (231.05,160.2) .. controls (232.96,160.2) and (234.5,161.74) .. (234.5,163.65) .. controls (234.5,165.56) and (232.96,167.1) .. (231.05,167.1) .. controls (229.14,167.1) and (227.6,165.56) .. (227.6,163.65) -- cycle ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (240.6,163.65) .. controls (240.6,161.74) and (242.14,160.2) .. (244.05,160.2) .. controls (245.96,160.2) and (247.5,161.74) .. (247.5,163.65) .. controls (247.5,165.56) and (245.96,167.1) .. (244.05,167.1) .. controls (242.14,167.1) and (240.6,165.56) .. (240.6,163.65) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (282.88,197.16) .. controls (282.88,194.62) and (284.94,192.56) .. (287.48,192.56) -- (307.17,192.56) .. controls (309.71,192.56) and (311.76,194.62) .. (311.76,197.16) -- (311.76,233.5) .. controls (311.76,236.04) and (309.71,238.1) .. (307.17,238.1) -- (287.48,238.1) .. controls (284.94,238.1) and (282.88,236.04) .. (282.88,233.5) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (311.82,184.16) .. controls (311.82,182.89) and (312.85,181.85) .. (314.12,181.85) -- (332.97,181.85) .. controls (334.24,181.85) and (335.28,182.89) .. (335.28,184.16) -- (335.28,192.74) .. controls (335.28,194.01) and (334.24,195.05) .. (332.97,195.05) -- (314.12,195.05) .. controls (312.85,195.05) and (311.82,194.01) .. (311.82,192.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (328.04,183.12) .. controls (328.04,182.42) and (328.61,181.85) .. (329.31,181.85) -- (334.01,181.85) .. controls (334.71,181.85) and (335.28,182.42) .. (335.28,183.12) -- (335.28,193.78) .. controls (335.28,194.48) and (334.71,195.05) .. (334.01,195.05) -- (329.31,195.05) .. controls (328.61,195.05) and (328.04,194.48) .. (328.04,193.78) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (251.2,171.9) -- (282.72,171.9) -- (282.72,232.13) -- (251.2,232.13) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (255.02,204.5) .. controls (255.02,194.47) and (261.57,186.33) .. (269.65,186.33) .. controls (277.73,186.33) and (284.27,194.47) .. (284.27,204.5) .. controls (284.27,214.54) and (277.73,222.67) .. (269.65,222.67) .. controls (261.57,222.67) and (255.02,214.54) .. (255.02,204.5) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (282.72,215.21) -- (270.22,215.46) .. controls (267.25,215.51) and (264.75,210.91) .. (264.63,205.17) .. controls (264.51,199.43) and (266.82,194.74) .. (269.78,194.68) -- (282.29,194.44) .. controls (285.25,194.38) and (287.75,198.98) .. (287.87,204.72) .. controls (287.99,210.46) and (285.68,215.16) .. (282.72,215.21) .. controls (279.75,215.27) and (277.25,210.67) .. (277.13,204.93) .. controls (277.01,199.19) and (279.32,194.49) .. (282.29,194.44) ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (304.13,206.77) -- (283.83,207.16) .. controls (283.02,207.18) and (282.33,205.92) .. (282.3,204.35) .. controls (282.27,202.77) and (282.9,201.49) .. (283.71,201.47) -- (304.02,201.08) .. controls (304.83,201.06) and (305.51,202.32) .. (305.54,203.89) .. controls (305.58,205.47) and (304.95,206.75) .. (304.13,206.77) .. controls (303.32,206.78) and (302.64,205.52) .. (302.6,203.95) .. controls (302.57,202.38) and (303.2,201.1) .. (304.02,201.08) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (338.14,219) -- (306.62,219.61) .. controls (302.36,219.69) and (298.77,213.08) .. (298.6,204.84) .. controls (298.42,196.6) and (301.74,189.85) .. (306,189.77) -- (337.52,189.16) .. controls (341.78,189.08) and (345.37,195.69) .. (345.54,203.93) .. controls (345.71,212.17) and (342.4,218.92) .. (338.14,219) .. controls (333.88,219.08) and (330.29,212.47) .. (330.12,204.23) .. controls (329.95,195.99) and (333.26,189.24) .. (337.52,189.16) ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (348.31,218.8) -- (336,219.04) .. controls (332.6,219.11) and (329.7,212.48) .. (329.53,204.24) .. controls (329.36,196) and (331.98,189.27) .. (335.38,189.2) -- (347.69,188.96) .. controls (351.09,188.9) and (353.99,195.52) .. (354.16,203.76) .. controls (354.33,212) and (351.71,218.74) .. (348.31,218.8) .. controls (344.91,218.87) and (342.02,212.24) .. (341.84,204) .. controls (341.67,195.76) and (344.29,189.03) .. (347.69,188.96) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (345.54,203.93) .. controls (345.54,201.99) and (346.48,200.42) .. (347.65,200.42) .. controls (348.81,200.42) and (349.75,201.99) .. (349.75,203.93) .. controls (349.75,205.87) and (348.81,207.44) .. (347.65,207.44) .. controls (346.48,207.44) and (345.54,205.87) .. (345.54,203.93) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (305.36,219.63) -- (336.31,219.63) -- (336.31,223.67) -- (305.36,223.67) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (336.31,219.63) -- (346.13,219.63) -- (346.13,223.67) -- (336.31,223.67) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (301.74,224.36) -- (332.69,224.36) -- (332.69,232.13) -- (301.74,232.13) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (332.69,224.36) -- (350.26,224.36) -- (350.26,232.13) -- (332.69,232.13) -- cycle ;
            	\draw    (256.99,179.37) -- (277.66,179.62) ;
            	\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (142,230) -- (319.1,230) -- (319.1,245.7) -- (142,245.7) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (319.1,230) -- (352.6,230) -- (352.6,245.7) -- (319.1,245.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (233.28,80.87) .. controls (233.27,80.66) and (233.26,80.45) .. (233.26,80.24) .. controls (232.71,60.92) and (248.35,44.8) .. (268.19,44.24) .. controls (288.02,43.68) and (304.55,58.89) .. (305.1,78.21) .. controls (305.11,78.54) and (305.11,78.86) .. (305.11,79.18) -- (289.83,79.2) .. controls (289.83,79.02) and (289.82,78.83) .. (289.82,78.65) .. controls (289.51,67.76) and (280.02,59.2) .. (268.62,59.52) .. controls (257.22,59.84) and (248.23,68.93) .. (248.54,79.81) .. controls (248.54,79.93) and (248.54,80.05) .. (248.55,80.17) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (221.7,98.4) -- (233.7,78.9) -- (248.55,78.9) -- (260.55,98.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (221.7,98.4) -- (260.55,98.4) -- (260.55,102.4) -- (221.7,102.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (163.88,122.5) -- (183.75,122.5) -- (183.75,171.9) -- (163.88,171.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (195.89,131.78) -- (183.78,150.6) -- (163.54,150.19) -- (152.2,130.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (215.26,73.21) -- (183.28,122.89) -- (164.17,122.5) -- (134.23,71.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (134.35,63.5) -- (215.26,63.5) -- (215.26,73.21) -- (134.35,73.21) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.35 ] (189.1,63.4) -- (214.7,63.5) -- (215.26,73.21) -- (183.28,122.89) -- (175.1,122.65) -- (188.2,71.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.25 ] (175.1,122.89) -- (183.28,122.89) -- (183.28,131.15) -- (175.1,131.15) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.25 ] (175.6,150.6) -- (183.78,150.6) -- (183.78,171.4) -- (175.6,171.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.35 ] (180.1,131.4) -- (195.89,131.78) -- (183.78,150.6) -- (175.6,150.6) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.35 ] (251.2,230.15) -- (319.1,230) -- (319.1,245.7) -- (142,245.7) -- cycle ;
            	\draw  [draw opacity=0] (247.63,78.98) .. controls (249.63,67.38) and (258.42,58.65) .. (268.95,58.65) .. controls (279.32,58.65) and (287.99,67.11) .. (290.17,78.43) -- (268.95,84.03) -- cycle ; \draw   (247.63,78.98) .. controls (249.63,67.38) and (258.42,58.65) .. (268.95,58.65) .. controls (279.32,58.65) and (287.99,67.11) .. (290.17,78.43) ;  
            	\draw  [draw opacity=0] (233.47,79.29) .. controls (233.46,78.87) and (233.45,78.45) .. (233.45,78.03) .. controls (233.45,59.45) and (249.51,44.4) .. (269.32,44.4) .. controls (289.14,44.4) and (305.2,59.45) .. (305.2,78.03) .. controls (305.2,78.38) and (305.19,78.73) .. (305.18,79.08) -- (269.32,78.03) -- cycle ; \draw   (233.47,79.29) .. controls (233.46,78.87) and (233.45,78.45) .. (233.45,78.03) .. controls (233.45,59.45) and (249.51,44.4) .. (269.32,44.4) .. controls (289.14,44.4) and (305.2,59.45) .. (305.2,78.03) .. controls (305.2,78.38) and (305.19,78.73) .. (305.18,79.08) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.25 ] (297.81,78.9) -- (306,78.9) -- (306,192.4) -- (297.81,192.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.17 ] (233.24,79.4) .. controls (233.17,60.46) and (248.64,44.8) .. (268.19,44.24) .. controls (288.02,43.68) and (304.55,58.89) .. (305.1,78.21) .. controls (305.11,78.73) and (305.11,79.24) .. (305.11,79.74) -- (298.45,79.65) .. controls (298.46,79.23) and (298.45,78.82) .. (298.44,78.4) .. controls (298,62.75) and (284.54,50.44) .. (268.37,50.9) .. controls (252.45,51.35) and (239.84,64.03) .. (239.9,79.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.35 ] (233.47,79.29) -- (239.9,79.37) -- (238.45,97.65) -- (223.2,97.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.35 ] (265.13,131.73) -- (272.8,131.5) -- (272.33,171.4) -- (253.8,171.5) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.25 ] (239.8,172.4) -- (251.2,171.9) -- (251.2,230.15) -- (175.47,229.73) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (293.9,80) -- (293.4,189.5) ;

            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (247.05,82.25) -- (254.9,96) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (141.4,65) -- (141.9,73) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (141.9,73) -- (166.9,122.5) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (166.9,122.5) -- (167.4,130.5) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (158.4,131) -- (168.2,151.07) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (168.4,171.5) -- (168.2,151.07) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.2 ] (175.6,171.4) -- (203.4,173) -- (165.4,228.5) -- (152.17,229.71) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (209.4,170) -- (208.9,133.5) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (153.17,229.71) -- (153.5,172) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (213.53,200.4) -- (213.5,182) ;
            	\draw  [draw opacity=0] (247.5,77.23) .. controls (249.65,64.27) and (259.23,54.5) .. (270.74,54.5) .. controls (282.97,54.5) and (293.04,65.55) .. (294.3,79.73) -- (270.74,82.73) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (247.5,77.23) .. controls (249.65,64.27) and (259.23,54.5) .. (270.74,54.5) .. controls (282.97,54.5) and (293.04,65.55) .. (294.3,79.73) ;  
            	\draw  [draw opacity=0] (343.43,217.16) .. controls (340.95,215.82) and (338.99,210.39) .. (338.84,203.84) .. controls (338.67,196.45) and (340.86,190.36) .. (343.78,189.98) -- (344.35,203.71) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (343.43,217.16) .. controls (340.95,215.82) and (338.99,210.39) .. (338.84,203.84) .. controls (338.67,196.45) and (340.86,190.36) .. (343.78,189.98) ;  
            	\draw    (298.6,204.84) -- (329.53,204.24) ;
            	\draw    (298.35,199.84) -- (329.28,199.24) ;
            	\draw    (300.6,194.34) -- (331.53,193.74) ;
            	\draw    (299.35,210.59) -- (330.28,209.99) ;
            	\draw    (301.35,216.09) -- (332.28,215.49) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] [dash pattern={on 0.84pt off 2.51pt}]  (217.5,139.8) -- (233.2,139.73) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] [dash pattern={on 0.84pt off 2.51pt}]  (217.5,143.47) -- (227.2,143.07) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] [dash pattern={on 0.84pt off 2.51pt}]  (217.83,147.47) -- (223.87,147.73) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (162.92,219.95) -- (162.88,201.55) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (144.2,243.07) -- (144.22,231.55) ;
            	\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (201.2,231.73) -- (144.22,231.55) ;
            \end{tikzpicture}'''

            # Nội dung câu hỏi
            noidungcauhoi = (r'''\immini{Giả sử rằng khi được $t$ năm tuổi, một máy công nghiệp A tạo ra doanh thu với tốc độ $R'(t) = %s - %st^2$ (triệu đồng/năm), thời điểm $t=0$ tính từ lúc máy A bắt đầu hoạt động. Biết rằng chi phí biên cho vận hành và bảo trì là $C'(t) = %s + %st^2$ (triệu đồng / năm), ở đây $C(t)$ là chi phí vận hành và bảo trì của máy A khi nó được $t$ năm tuổi.}{%s}''' % (a, b, c, d, hinhve))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Doanh thu sau %s năm của máy A là $\\int_0^{%s} \\left( %s - %st^2 \\right)\\text{d}t$ (triệu đồng)' % (t1, t1, a, b)
            nb_da_1_s = 'Doanh thu sau %s năm của máy A là $\\int_0^{%s} \\left( %s + %st^2 \\right)\\text{d}t$ (triệu đồng)' % (t1, t1, a, b)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Nhận xét rằng trên đoạn $[0;%s]$ hàm $R'(t)>0$, do đó doanh thu sau %s năm của máy công nghiệp A là \\\\ $\\int_0^{%s} \\left| %s - %st^2 \\right|\\text{d}t = \\int_0^{%s} \\left( %s - %st^2 \\right)\\text{d}t$.''' % (t1, t1, t1, a, b, t1, a, b))

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
            th_da_1_d = '\\True Tổng chi phí vận hành và bảo trì của máy A trong %s năm là %s (triệu đồng)' % (T, cost_val)
            th_da_1_s = 'Tổng chi phí vận hành và bảo trì của máy A trong %s năm là %s (triệu đồng)' % (T, cost_val + random.choice([20, 30, 45, 50]))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Tổng chi phí vận hành và bảo trì của máy A trong %s năm là \\\\ $\\int_0^{%s} \\left| %s + %st^2 \\right|\\text{d}t = \\int_0^{%s} \\left( %s + %st^2 \\right)\\text{d}t = %s$ (triệu đồng).''' % (T, T, c, d, T, c, d, cost_val))

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
            vd_da_1_d = '\\True Tuổi thọ hữu ích của một máy là số năm $T$ trước khi lợi nhuận (bằng doanh thu trừ chi phí) mà nó tạo ra bắt đầu giảm. Tuổi thọ hữu ích của máy A này là %s năm' % (T)
            vd_da_1_s = 'Tuổi thọ hữu ích của một máy là số năm $T$ trước khi lợi nhuận (bằng doanh thu trừ chi phí) mà nó tạo ra bắt đầu giảm. Tuổi thọ hữu ích của máy A này là %s năm' % (T + random.choice([1, 2]))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Lợi nhuận biên của máy A là $P'(t) = R'(t) - C'(t) = %s - %st^2$ (triệu đồng/năm). \\\\ Lợi nhuận bắt đầu giảm, có nghĩa là lợi nhuận biên âm. \\\\ Hay $P'(t) < 0 \\Leftrightarrow %s - %st^2 < 0 \\Rightarrow t > %s$ \\\\ Vậy tuổi thọ hữu ích của máy A là %s năm.''' % (M, N, M, N, T, T))

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
            vdc_da_1_d = '\\True Lợi nhuận do máy A tạo ra trong suốt thời gian tuổi thọ hữu ích của nó là %s (triệu đồng)' % (profit_val)
            vdc_da_1_s = 'Lợi nhuận do máy A tạo ra trong suốt thời gian tuổi thọ hữu ích của nó là %s (triệu đồng)' % (profit_val + random.choice([40, 52, 60]))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Lợi nhuận do máy A tạo ra trong suốt thời gian tuổi thọ hữu ích của nó là \\\\ $\\int_0^{%s} \\left| R'(t) - C'(t) \\right|\\text{d}t = \\int_0^{%s} \\left| %s - %st^2 \\right|\\text{d}t = %s$ (triệu đồng).''' % (T, T, M, N, profit_val))

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
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
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
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

