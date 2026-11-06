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


def bt_dang65_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo dạng
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Danh sách các bộ thông số (h, L, v1, v2) hợp lệ để cho ra kết quả đẹp
                # h: khoảng cách từ AB đến đường nhựa (km)
                # L: khoảng cách AB (km)
                # v1: vận tốc trên sa mạc (km/h)
                # v2: vận tốc trên đường nhựa (km/h)
                param_list = [
                    (10, 70, 30, 50),
                    (10, 80, 30, 50),
                    (15, 70, 30, 50),
                    (15, 90, 30, 50),
                    (20, 80, 30, 50),
                    (20, 100, 30, 50),
                    (12, 70, 30, 50),
                    (16, 80, 30, 50)
                ]

                h, L, v1, v2 = random.choice(param_list)

                # Tính toán giá trị x tối ưu: T'(x) = 0 => x = (v1 / sqrt(v2^2 - v1^2)) * h = (3/4) * h
                x_val = Rational(3, 4) * h
                ac_val = sqrt(h**2 + x_val**2) # = (5/4) * h
                cd_val = L - 2 * x_val

                # Thời gian tối thiểu (giờ)
                t_hours = (2 * ac_val) / v1 + cd_val / v2

                # Thời gian tối thiểu (phút)
                t_minutes = int(t_hours * 60)
                kq = str(t_minutes)

                # Tạo phương án sai không trùng đáp án đúng
                t_direct = int((L / v1) * 60) # Đi thẳng sa mạc A -> B
                t_perp = int(((2 * h) / v1 + L / v2) * 60) # Đi vuông góc xuống đường nhựa
                t_mid = int((2 * math.sqrt(h**2 + (L / 2)**2) / v1) * 60) # Đi đến trung điểm đường nhựa

                s_set = set()
                for candidate in [t_direct, t_perp, t_mid, t_minutes + 8, t_minutes - 8, t_minutes + 12, t_minutes - 12, t_minutes + 15]:
                    if candidate != t_minutes and candidate > 0:
                        s_set.add(str(candidate))

                s = list(s_set)
                random.shuffle(s)

                da = '$%s$ phút' % (kq)
                das1 = '$%s$ phút' % (s[0])
                das2 = '$%s$ phút' % (s[1])
                das3 = '$%s$ phút' % (s[2])

                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Một nhà địa chất học đang ở tại điểm $A$ trên sa mạc. Anh ta muốn đến điểm $B$ và cách $A$ một đoạn là $%s$ km. Trong sa mạc thì xe anh ta chỉ có thể di chuyển với vận tốc là $%s$ km/h. May mắn thay, có một con đường nhựa song song với đường nối $A$ và $B$ và cách $AB$ một đoạn $%s$ km. Trên đường nhựa đó thì xe nhà địa chất này có thể di chuyển với vận tốc $%s$ km/h. Xe có thể đi từ $A$ đến một điểm $C$ bất kỳ trên đường nhựa, chạy trên đường đến $D$, rồi đi từ $D$ đến $B$. Thời gian ngắn nhất để nhà địa chất di chuyển từ $A$ đến $B$ là bao nhiêu phút?}
                                 {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                                 			\\tikzset {_mfcyd03iw/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{18.48 bp } { -5.94 bp }  }  \\pgftransformrotate{-91 }  \\pgftransformscale{2.64 }  }}}
                                 		\\pgfdeclarehorizontalshading{_lwnil18u6}{150bp}{rgb(0bp)=(0.96,0.65,0.14);
                                 			rgb(37.5bp)=(0.96,0.65,0.14);
                                 			rgb(50bp)=(0.95,0.95,0.56);
                                 			rgb(62.5bp)=(0.96,0.65,0.14);
                                 			rgb(100bp)=(0.96,0.65,0.14)}
                                 		\\tikzset{every picture/.style={line width=0.75pt}} 
                                 		\\draw  [draw opacity=0][shading=_lwnil18u6,_mfcyd03iw] (12.5,22) -- (315.62,22) -- (315.62,227.9) -- (12.5,227.9) -- cycle ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (12.5,155.95) -- (316.45,155.95) -- (316.45,180.67) -- (12.5,180.67) -- cycle ;
                                 		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (12.5,157.33) -- (316.45,157.33) ;
                                 		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (12.5,179.29) -- (316.45,179.29) ;
                                 		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ] [dash pattern={on 4.5pt off 4.5pt}]  (12.5,168.31) -- (316.45,168.31) ;
                                 		\\draw  [line width=1.5]  (266.73,72.96) -- (223.92,157.33) -- (107.1,157.33) -- (64.29,72.96) -- cycle ;
                                 		\\draw [line width=1.5]  [dash pattern={on 5.63pt off 4.5pt}]  (64.29,72.96) -- (64.29,156.5) ;
                                 		\\draw [line width=1.5]  [dash pattern={on 5.63pt off 4.5pt}]  (266.73,72.96) -- (266.73,156.5) ;
                                 		\\draw [line width=1.5]  [dash pattern={on 5.63pt off 4.5pt}]  (266.73,157.5) -- (64.29,157.5) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (46.12,171.99) -- (46.57,196.14) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (58.9,188.44) -- (46.57,196.14) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (58.58,183.81) -- (46.57,196.14) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (56.34,178.22) -- (46.57,196.14) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (51.39,175.34) -- (46.57,196.14) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (46.57,196.14) -- (35.42,190.01) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (36.54,185.69) -- (46.57,196.14) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (39.1,180.9) -- (46.57,196.14) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (42.45,177.07) -- (46.57,196.14) ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (39.41,195.6) .. controls (39.41,193.62) and (42.62,192.02) .. (46.57,192.02) .. controls (50.52,192.02) and (53.73,193.62) .. (53.73,195.6) .. controls (53.73,197.57) and (50.52,199.18) .. (46.57,199.18) .. controls (42.62,199.18) and (39.41,197.57) .. (39.41,195.6) -- cycle ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (224.27,175.44) -- (224.71,199.59) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (237.04,191.89) -- (224.71,199.59) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (236.72,187.26) -- (224.71,199.59) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (234.49,181.67) -- (224.71,199.59) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (229.54,178.8) -- (224.71,199.59) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (224.71,199.59) -- (213.57,193.46) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (214.68,189.15) -- (224.71,199.59) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (217.24,184.35) -- (224.71,199.59) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (220.59,180.52) -- (224.71,199.59) ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (217.56,199.05) .. controls (217.56,197.07) and (220.76,195.47) .. (224.71,195.47) .. controls (228.67,195.47) and (231.87,197.07) .. (231.87,199.05) .. controls (231.87,201.03) and (228.67,202.63) .. (224.71,202.63) .. controls (220.76,202.63) and (217.56,201.03) .. (217.56,199.05) -- cycle ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (73.79,194.12) -- (74.07,209.04) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (81.69,204.28) -- (74.07,209.04) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (81.49,201.42) -- (74.07,209.04) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (80.11,197.97) -- (74.07,209.04) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (77.05,196.19) -- (74.07,209.04) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (74.07,209.04) -- (67.19,205.25) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (67.88,202.59) -- (74.07,209.04) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (69.45,199.63) -- (74.07,209.04) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (71.53,197.26) -- (74.07,209.04) ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (69.65,208.7) .. controls (69.65,207.48) and (71.63,206.49) .. (74.07,206.49) .. controls (76.51,206.49) and (78.49,207.48) .. (78.49,208.7) .. controls (78.49,209.92) and (76.51,210.91) .. (74.07,210.91) .. controls (71.63,210.91) and (69.65,209.92) .. (69.65,208.7) -- cycle ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (291.29,201.72) -- (291.57,216.63) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (299.19,211.88) -- (291.57,216.63) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (298.99,209.02) -- (291.57,216.63) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (297.61,205.57) -- (291.57,216.63) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (294.55,203.79) -- (291.57,216.63) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (291.57,216.63) -- (284.69,212.85) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (285.38,210.18) -- (291.57,216.63) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (286.95,207.22) -- (291.57,216.63) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (289.03,204.86) -- (291.57,216.63) ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (287.15,216.3) .. controls (287.15,215.08) and (289.13,214.09) .. (291.57,214.09) .. controls (294.01,214.09) and (295.99,215.08) .. (295.99,216.3) .. controls (295.99,217.52) and (294.01,218.51) .. (291.57,218.51) .. controls (289.13,218.51) and (287.15,217.52) .. (287.15,216.3) -- cycle ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (289.22,120.24) -- (289.5,135.16) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (297.11,130.4) -- (289.5,135.16) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (296.92,127.54) -- (289.5,135.16) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (295.54,124.09) -- (289.5,135.16) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (292.48,122.31) -- (289.5,135.16) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (289.5,135.16) -- (282.61,131.37) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (283.3,128.71) -- (289.5,135.16) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (284.88,125.75) -- (289.5,135.16) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (286.95,123.38) -- (289.5,135.16) ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (285.08,134.82) .. controls (285.08,133.6) and (287.06,132.61) .. (289.5,132.61) .. controls (291.94,132.61) and (293.92,133.6) .. (293.92,134.82) .. controls (293.92,136.04) and (291.94,137.03) .. (289.5,137.03) .. controls (287.06,137.03) and (285.08,136.04) .. (285.08,134.82) -- cycle ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (276.6,104.22) -- (276.81,115.58) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (282.61,111.96) -- (276.81,115.58) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (282.46,109.78) -- (276.81,115.58) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (281.41,107.15) -- (276.81,115.58) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (279.08,105.79) -- (276.81,115.58) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (276.81,115.58) -- (271.57,112.69) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (272.09,110.66) -- (276.81,115.58) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (273.3,108.41) -- (276.81,115.58) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (274.87,106.61) -- (276.81,115.58) ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (273.44,115.33) .. controls (273.44,114.4) and (274.95,113.64) .. (276.81,113.64) .. controls (278.67,113.64) and (280.18,114.4) .. (280.18,115.33) .. controls (280.18,116.26) and (278.67,117.01) .. (276.81,117.01) .. controls (274.95,117.01) and (273.44,116.26) .. (273.44,115.33) -- cycle ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (304.22,77.98) -- (304.43,89.34) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (310.23,85.72) -- (304.43,89.34) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (310.08,83.54) -- (304.43,89.34) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (309.03,80.91) -- (304.43,89.34) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (306.7,79.56) -- (304.43,89.34) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (304.43,89.34) -- (299.19,86.46) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (299.71,84.43) -- (304.43,89.34) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (300.91,82.17) -- (304.43,89.34) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (302.49,80.37) -- (304.43,89.34) ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (301.06,89.09) .. controls (301.06,88.16) and (302.57,87.4) .. (304.43,87.4) .. controls (306.29,87.4) and (307.8,88.16) .. (307.8,89.09) .. controls (307.8,90.02) and (306.29,90.77) .. (304.43,90.77) .. controls (302.57,90.77) and (301.06,90.02) .. (301.06,89.09) -- cycle ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (204.1,200.19) -- (204.31,211.56) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (210.11,207.93) -- (204.31,211.56) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (209.96,205.75) -- (204.31,211.56) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (208.91,203.12) -- (204.31,211.56) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (206.58,201.77) -- (204.31,211.56) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (204.31,211.56) -- (199.07,208.67) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (199.59,206.64) -- (204.31,211.56) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (200.8,204.39) -- (204.31,211.56) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (202.37,202.58) -- (204.31,211.56) ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (200.94,211.3) .. controls (200.94,210.37) and (202.45,209.62) .. (204.31,209.62) .. controls (206.17,209.62) and (207.68,210.37) .. (207.68,211.3) .. controls (207.68,212.23) and (206.17,212.99) .. (204.31,212.99) .. controls (202.45,212.99) and (200.94,212.23) .. (200.94,211.3) -- cycle ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (174.41,207.1) -- (174.62,218.46) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (180.42,214.84) -- (174.62,218.46) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (180.27,212.66) -- (174.62,218.46) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (179.22,210.03) -- (174.62,218.46) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (176.89,208.68) -- (174.62,218.46) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (174.62,218.46) -- (169.38,215.57) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (169.9,213.55) -- (174.62,218.46) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (171.1,211.29) -- (174.62,218.46) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (172.68,209.49) -- (174.62,218.46) ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (171.25,218.21) .. controls (171.25,217.28) and (172.76,216.52) .. (174.62,216.52) .. controls (176.48,216.52) and (177.99,217.28) .. (177.99,218.21) .. controls (177.99,219.14) and (176.48,219.89) .. (174.62,219.89) .. controls (172.76,219.89) and (171.25,219.14) .. (171.25,218.21) -- cycle ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (48.74,112.5) -- (48.96,123.87) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (54.76,120.24) -- (48.96,123.87) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (54.61,118.06) -- (48.96,123.87) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (53.55,115.43) -- (48.96,123.87) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (51.22,114.08) -- (48.96,123.87) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (48.96,123.87) -- (43.71,120.98) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (44.24,118.95) -- (48.96,123.87) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (45.44,116.7) -- (48.96,123.87) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (47.02,114.89) -- (48.96,123.87) ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (45.59,123.61) .. controls (45.59,122.68) and (47.1,121.93) .. (48.96,121.93) .. controls (50.82,121.93) and (52.32,122.68) .. (52.32,123.61) .. controls (52.32,124.54) and (50.82,125.3) .. (48.96,125.3) .. controls (47.1,125.3) and (45.59,124.54) .. (45.59,123.61) -- cycle ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (31.51,52.1) -- (31.63,58.85) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (35.08,56.7) -- (31.63,58.85) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (34.99,55.41) -- (31.63,58.85) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (34.36,53.84) -- (31.63,58.85) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (32.98,53.04) -- (31.63,58.85) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (31.63,58.85) -- (28.52,57.14) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (28.83,55.93) -- (31.63,58.85) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (29.55,54.59) -- (31.63,58.85) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (30.48,53.52) -- (31.63,58.85) ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (29.63,58.7) .. controls (29.63,58.15) and (30.53,57.7) .. (31.63,57.7) .. controls (32.74,57.7) and (33.63,58.15) .. (33.63,58.7) .. controls (33.63,59.25) and (32.74,59.7) .. (31.63,59.7) .. controls (30.53,59.7) and (29.63,59.25) .. (29.63,58.7) -- cycle ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (32.86,124.93) -- (33.07,136.29) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (38.88,132.67) -- (33.07,136.29) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (38.73,130.49) -- (33.07,136.29) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (37.67,127.86) -- (33.07,136.29) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (35.34,126.51) -- (33.07,136.29) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (33.07,136.29) -- (27.83,133.41) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (28.35,131.38) -- (33.07,136.29) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (29.56,129.12) -- (33.07,136.29) ;
                                 		\\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (31.14,127.32) -- (33.07,136.29) ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (29.71,136.04) .. controls (29.71,135.11) and (31.21,134.36) .. (33.07,134.36) .. controls (34.93,134.36) and (36.44,135.11) .. (36.44,136.04) .. controls (36.44,136.97) and (34.93,137.72) .. (33.07,137.72) .. controls (31.21,137.72) and (29.71,136.97) .. (29.71,136.04) -- cycle ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.1 ] (91.45,113.91) .. controls (117.68,113.91) and (138.95,119.96) .. (138.95,127.42) .. controls (138.95,127.48) and (138.95,127.55) .. (138.95,127.61) .. controls (143.9,127.49) and (149,127.42) .. (154.2,127.42) .. controls (204.04,127.42) and (244.45,133.47) .. (244.45,140.93) .. controls (244.45,147.02) and (217.49,152.18) .. (180.45,153.86) .. controls (182.73,155.11) and (183.95,156.44) .. (183.95,157.82) .. controls (183.95,159.93) and (181.06,161.94) .. (175.9,163.72) .. controls (231.17,164.73) and (273.45,170.32) .. (273.45,177.07) .. controls (273.45,184.53) and (221.74,190.58) .. (157.95,190.58) .. controls (94.16,190.58) and (42.45,184.53) .. (42.45,177.07) .. controls (42.45,174.23) and (49.92,171.6) .. (62.67,169.43) .. controls (39.18,167.07) and (23.45,162.76) .. (23.45,157.82) .. controls (23.45,152.42) and (42.27,147.76) .. (69.47,145.59) .. controls (65.9,144.14) and (63.95,142.57) .. (63.95,140.93) .. controls (63.95,140.16) and (64.38,139.41) .. (65.2,138.68) .. controls (52.39,136.26) and (43.95,132.12) .. (43.95,127.42) .. controls (43.95,119.96) and (65.22,113.91) .. (91.45,113.91) -- cycle ;
                                 		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.33 ] (267.74,70.11) .. controls (251.34,70.11) and (238.05,73.19) .. (238.05,76.98) .. controls (238.05,77.01) and (238.05,77.04) .. (238.06,77.07) .. controls (234.96,77.01) and (231.77,76.98) .. (228.52,76.98) .. controls (197.37,76.98) and (172.12,80.05) .. (172.12,83.84) .. controls (172.12,86.94) and (188.97,89.55) .. (212.12,90.41) .. controls (210.7,91.05) and (209.93,91.72) .. (209.93,92.42) .. controls (209.93,93.5) and (211.74,94.51) .. (214.96,95.42) .. controls (180.43,95.93) and (154,98.77) .. (154,102.2) .. controls (154,105.99) and (186.32,109.07) .. (226.18,109.07) .. controls (266.04,109.07) and (298.36,105.99) .. (298.36,102.2) .. controls (298.36,100.76) and (293.69,99.42) .. (285.72,98.32) .. controls (300.4,97.12) and (310.23,94.93) .. (310.23,92.42) .. controls (310.23,89.68) and (298.47,87.31) .. (281.47,86.21) .. controls (283.7,85.47) and (284.92,84.67) .. (284.92,83.84) .. controls (284.92,83.45) and (284.66,83.07) .. (284.15,82.7) .. controls (292.15,81.47) and (297.42,79.36) .. (297.42,76.98) .. controls (297.42,73.19) and (284.13,70.11) .. (267.74,70.11) -- cycle ;
                                 		\\draw (43.55,52.43) node [anchor=north west][inner sep=0.75pt]    {$A$};
                                 		\\draw (271.02,53.12) node [anchor=north west][inner sep=0.75pt]    {$B$};
                                 		\\draw (97.26,156.07) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ]  {$C$};
                                 		\\draw (216.62,155.95) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ]  {$D$};
                                 	\\end{tikzpicture} }'''
                                 % (latex(L), latex(v1), latex(h), latex(v2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuyển đổi dấu chấm thành dấu phẩy cho số thập phân
                x_str = str(float(x_val)).replace('.', ',') if isinstance(x_val, Float) or x_val % 1 != 0 else str(x_val)
                ac_str = str(float(ac_val)).replace('.', ',') if ac_val % 1 != 0 else str(ac_val)
                cd_str = str(float(cd_val)).replace('.', ',') if cd_val % 1 != 0 else str(cd_val)

                v1_half = v1 // 2
                v2_half = v2 // 2
                h2 = h**2

                # Nội dung lời giải
                loigiai = ('''Gọi $A', B'$ lần lượt là hình chiếu vuông góc của $A, B$ trên con đường nhựa. \\\\
            Đường thẳng $AB$ song song với con đường nhựa nên $A'B' = AB = %s$ km và $AA' = BB' = %s$ km. \\\\
            Đặt $A'C = x$ km (với $0 \\le x \\le %s$). Theo tính chất đối xứng, ta có $B'D = x$ km. \\\\
            Độ dài đoạn đường nhựa $CD$ là $CD = %s - 2x$ (km). \\\\
            Độ dài quãng đường đi trên sa mạc là $AC = BD = \\sqrt{%s^2 + x^2} = \\sqrt{%s + x^2}$ (km). \\\\
            Thời gian di chuyển tổng cộng (tính theo giờ) là: \\\\
            $T(x) = \\frac{AC + BD}{%s} + \\frac{CD}{%s} = \\frac{2\\sqrt{%s + x^2}}{%s} + \\frac{%s - 2x}{%s} = \\frac{\\sqrt{%s + x^2}}{%s} + \\frac{%s - 2x}{%s}$. \\\\
            Xét hàm số $T(x)$ trên đoạn $[0; %s]$: \\\\
            $T'(x) = \\frac{x}{%s\\sqrt{%s + x^2}} - \\frac{2}{%s} = \\frac{x}{%s\\sqrt{%s + x^2}} - \\frac{1}{%s}$. \\\\
            Cho $T'(x) = 0 \\Leftrightarrow  \\frac{x}{%s\\sqrt{%s + x^2}} = \\frac{1}{%s} \\Leftrightarrow  %s x = %s \\sqrt{%s + x^2} \\Leftrightarrow  x = %s$. \\\\
            Thay $x = %s$ vào biểu thức $T(x)$, ta được thời gian ngắn nhất là: \\\\
            $T(%s) = \\frac{\\sqrt{%s + %s^2}}{%s} + \\frac{%s - 2 \\cdot %s}{%s} = \\frac{%s}{60}$ giờ. \\\\
            Đổi sang đơn vị phút: $\\frac{%s}{60} \\cdot 60 = %s$ phút.'''
                           % (latex(L), latex(h), latex(L // 2),
                              latex(L), latex(h), latex(h2),
                              latex(v1), latex(v2), latex(h2), latex(v1), latex(L), latex(v2), latex(h2), latex(v1_half), latex(L), latex(v2),
                              latex(L // 2),
                              latex(v1_half), latex(h2), latex(v2), latex(v1_half), latex(h2), latex(v2_half),
                              latex(v1_half), latex(h2), latex(v2_half), latex(v2_half), latex(v1_half), latex(h2), x_str,
                              x_str,
                              x_str, latex(h2), x_str, latex(v1_half), latex(L), x_str, latex(v2), latex(kq),
                              latex(kq), latex(kq)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

