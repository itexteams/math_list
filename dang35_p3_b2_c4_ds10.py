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


def bt_dang35_p3_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các số liệu bài toán
                w2 = random.choice([100, 150, 200, 250, 300]) # Nửa khoảng cách giữa 2 tháp (tọa độ x của tháp)
                w = 2 * w2 # Khoảng cách giữa 2 tháp
                h = random.choice([50, 80, 100, 120, 150, 200]) # Chiều cao tháp

                # Khoảng cách từ H đến O phải nhỏ hơn khoảng cách từ tháp đến O
                d_choices = [30, 40, 50, 60, 80, 90, 100, 120, 150]
                d = random.choice([x for x in d_choices if x < w2]) 

                # Tính hệ số a = h / w2^2
                a_val = Rational(h, w2**2)
                if a_val.q == 1:
                    a_str = str(a_val.p)
                else:
                    a_str = "\\frac{%s}{%s}" % (a_val.p, a_val.q)

                # Tính kết quả CH = a * d^2
                kq_val = Rational(h * d**2, w2**2)
                kq_float = float(kq_val)

                # Định dạng kết quả, dùng dấu phẩy cho số thập phân
                if kq_float.is_integer():
                    kq = str(int(kq_float))
                    kq_num = int(kq_float)
                else:
                    kq = str(round(kq_float, 2)).replace('.', ',')
                    kq_num = round(kq_float, 2)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai khác nhau và khác đáp án đúng
                s_vals = []
                for offset in [5, 10, -5, -10, 2, -2, 1, -1]:
                    fake_val = kq_num + offset
                    if fake_val > 0:
                        if isinstance(fake_val, int) or fake_val.is_integer():
                            s_vals.append('$%s$' % str(int(fake_val)))
                        else:
                            s_vals.append('$%s$' % str(round(fake_val, 2)).replace('.', ','))

                s_vals = list(set(s_vals))
                if da in s_vals:
                    s_vals.remove(da)

                das1 = random.choice(s_vals)
                s_vals.remove(das1)
                das2 = random.choice(s_vals)
                s_vals.remove(das2)
                das3 = random.choice(s_vals)

                # Câu hỏi (kèm hình vẽ TikZ theo đúng hình dạng mẫu)
                noidungcauhoi = ('''\\immini{Một cây cầu treo có trụ tháp đôi cao $%s$ m so với mặt của cây cầu và cách nhau $%s$ m. Các dây cáp có dạng đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) như hình vẽ và được treo trên các đỉnh tháp. Chiều cao $CH$ của dây cáp bằng bao nhiêu mét? Biết điểm $H$ cách tâm $O$ của cây cầu $%s$ m (giả sử mặt của cây cầu là bằng phẳng).}
            {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\\tikzset {_5wg2p3svj/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-90 }  \\pgftransformscale{2 }  }}}
            	\\pgfdeclarehorizontalshading{_fsr5a9hke}{150bp}{rgb(0bp)=(0.6,0.85,1);
            		rgb(37.5bp)=(0.6,0.85,1);
            		rgb(62.5bp)=(0.88,0.93,0.93);
            		rgb(100bp)=(0.88,0.93,0.93)}
            	\\tikzset {_lxpstl94e/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
            	\\pgfdeclarehorizontalshading{_ugytdajx7}{150bp}{rgb(0bp)=(0.6,0.85,1);
            		rgb(37.5bp)=(0.6,0.85,1);
            		rgb(62.5bp)=(0,0.5,0.5);
            		rgb(100bp)=(0,0.5,0.5)}
            	\\tikzset{every picture/.style={line width=0.75pt}}
            	\\draw  [draw opacity=0][shading=_fsr5a9hke,_5wg2p3svj] (5.3,18.67) -- (284.4,18.67) -- (284.4,199.07) -- (5.3,199.07) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 147; green, 144; blue, 101 }  ,fill opacity=1 ] (78.4,157.5) -- (96.4,163) -- (118.9,164.5) -- (129.9,163.5) -- (140.4,166) -- (153.9,170.5) -- (29.3,170.4) -- (37.4,163) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (18.9,158.5) -- (29.4,155.5) -- (39.9,158.5) -- (63.4,161) -- (83.4,164.5) -- (143.3,170.9) -- (5.8,169.9) -- (5.4,152.5) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 147; green, 144; blue, 101 }  ,fill opacity=1 ] (206.4,164.5) -- (217.4,160) -- (238.8,159.2) -- (259.9,155.5) -- (284.8,155.2) -- (284.8,172.7) -- (167.8,171.4) -- (185.4,167) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (212.8,163.2) -- (234.9,161) -- (259.9,162) -- (284.8,155.2) -- (284.8,172.7) -- (189.4,169.5) -- (203.4,167.5) -- cycle ;
            	\\draw  [draw opacity=0][shading=_ugytdajx7,_lxpstl94e] (5.55,170.2) -- (284.3,170.2) -- (284.3,196.9) -- (5.55,196.9) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=0.3 ] (23.93,185.96) -- (41.43,188.36) -- (59.43,179.45) -- (90.43,179.79) -- (144.93,170.2) -- (5.8,169.9) -- (5.8,187.2) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=0.49 ] (206.24,176.92) -- (230.09,181.89) -- (256.66,180.24) -- (284.3,183.55) -- (284.3,170.2) -- (168.3,170.29) -- (188.9,175.26) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.08 ] (122.87,172) -- (171.27,172) .. controls (177.24,172) and (182.07,173.96) .. (182.07,176.39) .. controls (182.07,176.62) and (182.03,176.85) .. (181.94,177.08) -- (232.57,177.08) .. controls (238.54,177.08) and (243.37,179.04) .. (243.37,181.47) .. controls (243.37,183.89) and (238.54,185.85) .. (232.57,185.85) -- (192.4,185.85) .. controls (192.71,186.22) and (192.87,186.62) .. (192.87,187.03) .. controls (192.87,189.05) and (188.85,190.69) .. (183.87,190.69) -- (92.57,190.69) .. controls (87.6,190.69) and (83.57,189.05) .. (83.57,187.03) .. controls (83.57,185.01) and (87.6,183.37) .. (92.57,183.37) -- (135.15,183.37) .. controls (134.46,182.8) and (134.07,182.15) .. (134.07,181.47) .. controls (134.07,181.23) and (134.12,181) .. (134.21,180.77) -- (122.87,180.77) .. controls (116.91,180.77) and (112.07,178.81) .. (112.07,176.39) .. controls (112.07,173.96) and (116.91,172) .. (122.87,172) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 205; green, 202; blue, 202 }  ,fill opacity=1 ] (68.3,172.7) -- (54.8,181.2) -- (32.3,181.2) -- (44.8,173.2) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 152; green, 148; blue, 148 }  ,fill opacity=1 ] (54.8,181.2) -- (54.3,189.2) -- (31.3,189.2) -- (31.3,181.7) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 205; green, 202; blue, 202 }  ,fill opacity=1 ] (68.3,172.7) -- (67.8,180.7) -- (54.3,189.2) -- (54.3,181.7) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 157; green, 152; blue, 152 }  ,fill opacity=1 ] (59.8,55.2) -- (59.8,176.2) -- (52.8,176.2) -- (56.3,54.7) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 201; green, 197; blue, 197 }  ,fill opacity=1 ] (61.6,55.07) -- (62.27,173.4) -- (59.8,176.2) -- (59.8,55.2) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 205; green, 202; blue, 202 }  ,fill opacity=1 ] (59.3,64.37) -- (58.93,70.73) -- (53.6,68.4) -- (53.93,61.73) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 205; green, 202; blue, 202 }  ,fill opacity=1 ] (58.97,89.37) -- (58.6,95.73) -- (53.27,93.4) -- (53.6,86.73) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 205; green, 202; blue, 202 }  ,fill opacity=1 ] (58.63,149.37) -- (58.27,155.73) -- (52.6,155.4) -- (52.93,148.73) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 150; green, 148; blue, 148 }  ,fill opacity=1 ] (58.97,71.03) -- (56.93,72.07) -- (52.93,70.4) -- (53.6,68.4) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 150; green, 148; blue, 148 }  ,fill opacity=1 ] (58.63,96.03) -- (56.6,97.07) -- (52.6,95.4) -- (53.27,93.4) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 205; green, 202; blue, 202 }  ,fill opacity=1 ] (217.3,172.37) -- (229.72,180.87) -- (250.41,180.87) -- (238.92,172.87) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 152; green, 148; blue, 148 }  ,fill opacity=1 ] (229.72,180.87) -- (230.18,188.87) -- (251.33,188.87) -- (251.33,181.37) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 205; green, 202; blue, 202 }  ,fill opacity=1 ] (217.3,172.37) -- (217.76,180.37) -- (230.18,188.87) -- (230.18,181.37) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 157; green, 152; blue, 152 }  ,fill opacity=1 ] (225.12,54.87) -- (225.12,175.87) -- (231.56,175.87) -- (228.34,54.37) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 201; green, 197; blue, 197 }  ,fill opacity=1 ] (223.46,54.73) -- (222.85,173.07) -- (225.12,175.87) -- (225.12,54.87) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 205; green, 202; blue, 202 }  ,fill opacity=1 ] (225.58,64.03) -- (225.92,70.4) -- (230.82,68.07) -- (230.51,61.4) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 205; green, 202; blue, 202 }  ,fill opacity=1 ] (225.88,89.03) -- (226.22,95.4) -- (231.13,93.07) -- (230.82,86.4) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 205; green, 202; blue, 202 }  ,fill opacity=1 ] (226.19,149.03) -- (226.53,155.4) -- (231.74,155.07) -- (231.43,148.4) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 150; green, 148; blue, 148 }  ,fill opacity=1 ] (225.88,70.7) -- (227.76,71.73) -- (231.43,70.07) -- (230.82,68.07) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 150; green, 148; blue, 148 }  ,fill opacity=1 ] (226.19,95.7) -- (228.06,96.73) -- (231.74,95.07) -- (231.13,93.07) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 205; green, 202; blue, 202 }  ,fill opacity=1 ] (283.47,139.4) -- (283.47,142.07) -- (5.3,143.9) -- (5.47,139.73) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 159; green, 154; blue, 154 }  ,fill opacity=1 ] (283.47,142.07) -- (282.8,144.4) -- (5.8,144.4) -- (5.47,142.07) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 157; green, 152; blue, 152 }  ,fill opacity=1 ] (52.13,50.07) -- (49.13,179.07) -- (40.47,179.07) -- (48.13,50.07) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 201; green, 197; blue, 197 }  ,fill opacity=1 ] (54.13,50.4) -- (52.13,178.07) -- (49.13,179.07) -- (52.13,50.07) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 201; green, 197; blue, 197 }  ,fill opacity=1 ] (233.47,49.07) -- (234.13,178.73) -- (230.8,177.4) -- (230.47,49.07) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 157; green, 152; blue, 152 }  ,fill opacity=1 ] (237.13,49.07) -- (242.8,178.73) -- (234.13,178.73) -- (233.47,49.07) -- cycle ;
            	\\draw    (47,57) .. controls (41.9,72.5) and (24.9,91.5) .. (5.4,99) ;
            	\\draw    (46.5,73) .. controls (41.4,88.5) and (24.9,106.5) .. (5.4,114) ;
            	\\draw    (238,58.5) .. controls (242.4,78) and (262.4,94) .. (283.4,99) ;
            	\\draw    (238,74) .. controls (242.4,93.5) and (262.4,109.5) .. (283.4,114.5) ;
            	\\draw    (54.5,58) .. controls (131.4,177) and (159.4,154.5) .. (230.9,58) ;
            	\\draw [color={rgb, 255:red, 152; green, 149; blue, 149 }  ,draw opacity=1 ]   (66,75.5) -- (65.9,140.5) ;
            	\\draw [color={rgb, 255:red, 152; green, 149; blue, 149 }  ,draw opacity=1 ]   (219,74) -- (218.9,139) ;
            	\\draw [color={rgb, 255:red, 152; green, 149; blue, 149 }  ,draw opacity=1 ]   (75.9,90) -- (75.9,140) ;
            	\\draw [color={rgb, 255:red, 152; green, 149; blue, 149 }  ,draw opacity=1 ]   (208.9,87.5) -- (208.9,139) ;
            	\\draw [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ]   (86.4,103) -- (86.4,139.5) ;
            	\\draw [color={rgb, 255:red, 152; green, 149; blue, 149 }  ,draw opacity=1 ]   (198.4,100) -- (198.4,138.5) ;
            	\\draw [color={rgb, 255:red, 152; green, 149; blue, 149 }  ,draw opacity=1 ]   (97.4,116) -- (97.4,139.5) ;
            	\\draw [color={rgb, 255:red, 152; green, 149; blue, 149 }  ,draw opacity=1 ]   (187.4,112) -- (187.4,138.5) ;
            	\\draw [color={rgb, 255:red, 152; green, 149; blue, 149 }  ,draw opacity=1 ]   (108.9,126) -- (108.9,139.5) ;
            	\\draw [color={rgb, 255:red, 152; green, 149; blue, 149 }  ,draw opacity=1 ]   (174.9,124) -- (174.9,139) ;
            	\\draw [color={rgb, 255:red, 152; green, 149; blue, 149 }  ,draw opacity=1 ]   (120.4,133) -- (120.4,139.5) ;
            	\\draw [color={rgb, 255:red, 152; green, 149; blue, 149 }  ,draw opacity=1 ]   (162.4,132) -- (162.4,139) ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 101; green, 121; blue, 80 }  ,fill opacity=1 ] (15.4,161) -- (27.4,166.5) -- (32.9,175.5) -- (41.9,184) -- (55.4,197) -- (5.8,196.55) -- (5.55,156.9) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 101; green, 121; blue, 80 }  ,fill opacity=1 ] (273.9,164.5) -- (261.4,169.5) -- (253.86,175.85) -- (244.4,186.5) -- (219.9,197) -- (284.3,196.9) -- (284.8,155.2) -- cycle ;
            	\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (5.47,139.73) -- (280.47,139.4) ;
            	\\draw [shift={(283.47,139.4)}, rotate = 179.93] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            	\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (140.4,161) -- (140.4,47.5) ;
            	\\draw [shift={(140.4,44.5)}, rotate = 90] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            	\\draw    (245.51,60.5) -- (248.29,134.5) ;
            	\\draw [shift={(248.4,137.5)}, rotate = 267.85] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            	\\draw [shift={(245.4,57.5)}, rotate = 87.85] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            	\\draw    (48.9,181.5) -- (232.4,181.5) ;
            	\\draw [shift={(235.4,181.5)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            	\\draw [shift={(45.9,181.5)}, rotate = 0] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            	\\draw    (89.9,161) -- (137.4,161) ;
            	\\draw [shift={(140.4,161)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            	\\draw [shift={(86.9,161)}, rotate = 0] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            	\\draw (123.5,145) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$O$};
            	\\draw (26.5,145) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$A$};
            	\\draw (239,145) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$B$};
            	\\draw (80.5,85) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$C$};
            	\\draw (78,145) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$H$};
            	\\draw (162.5,71) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$y=ax^{2}$};
            	\\draw (270,130) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$x$};
            	\\draw (126,42) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$y$};
            	\\draw (248,108.5) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$%s$m};
            	\\draw (128,185) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$%s$m};
            	\\draw (100.5,161.5) node [anchor=north west][inner sep=0.75pt]  [font=\\tiny]  {$%s$m};
            \\end{tikzpicture}}'''
                                 % (latex(h), latex(w), latex(d), latex(d), latex(w), latex(h)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Chọn hệ trục tọa độ $Oxy$ như hình vẽ, với gốc tọa độ $O$ là điểm thấp nhất của dây cáp. \\\\
            Khi đó, phương trình của parabol có dạng $y = ax^2$. \\\\
            Do hai trụ tháp cách nhau $%s$ m và cao $%s$ m so với mặt cầu, nên parabol đi qua điểm có tọa độ $\\left(\\frac{%s}{2}; %s\\right) = (%s; %s)$. \\\\
            Thay tọa độ điểm này vào phương trình parabol, ta được: \\\\
            $%s = a \\cdot %s^2 \\Rightarrow a = \\frac{%s}{%s} = %s$. \\\\
            Vậy phương trình của parabol là $y = %s x^2$. \\\\
            Điểm $H$ cách tâm $O$ một khoảng $%s$ m nên điểm $H$ có hoành độ $x = -%s$ (hoặc $x = %s$). \\\\
            Thay $x = -%s$ vào phương trình parabol, ta tính được tung độ của điểm $C$: \\\\
            $y_C = %s \\cdot (-%s)^2 = %s$. \\\\
            Vậy chiều cao $CH$ của dây cáp là $%s$ m.'''
                           % (latex(w), latex(h), latex(w), latex(h), latex(w2), latex(h),
                              latex(h), latex(w2), latex(h), latex(w2**2), a_str,
                              a_str,
                              latex(d), latex(d), latex(d),
                              latex(d),
                              a_str, latex(d), kq,
                              kq))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

