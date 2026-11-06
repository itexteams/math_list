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


def bt_dang49_p3_b1_c5_ds10(self):
            # Chọn ngẫu nhiên 5 chữ số khác nhau từ 1 đến 9
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. Randomize dữ liệu
                foods_list = ["Mật ong", "Phấn hoa", "Sữa ong chúa", "Nước", "Sáp ong", "Keo ong"]
                m = random.randint(4, 6) # Số loại thức ăn (tương đương số màu)
                selected = random.sample(foods_list, m)

                # Tạo chuỗi danh sách thức ăn
                food_str = ""
                for i in range(m - 1):
                    food_str += selected[i] + ", "
                food_str += "và " + selected[-1]

                # 2. Tính toán
                # Ô trung tâm có m cách chọn
                # 6 ô xung quanh tạo thành đồ thị vòng C6, phải tô bằng m-1 màu còn lại
                k = m - 1 
                k_minus_1 = k - 1

                # Công thức đa thức sắc số cho đồ thị vòng C_n: (k-1)^n + (-1)^n(k-1)
                # Với n = 6: số cách = (k-1)^6 + (k-1)
                kq_vong = (k_minus_1)**6 + k_minus_1
                kq = m * kq_vong

                # Các đáp án sai (sai do dùng nhầm công thức)
                sai1 = m * ((k_minus_1)**6 - k_minus_1) # Sai dấu trong đa thức
                sai2 = m * k * ((k_minus_1)**5)         # Lỗi coi vòng tròn là đường thẳng (path)
                sai3 = m * (k**6)                       # Lỗi không trừ đi các trường hợp trùng lặp ở 2 đầu chu trình

                # Lọc đáp án để đảm bảo không bị trùng nhau
                s = set([sai1, sai2, sai3, kq + 12, kq - 12, kq + 24])
                if kq in s:
                    s.remove(kq)
                s_list = list(s)
                random.shuffle(s_list)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Các đáp án trắc nghiệm định dạng LaTeX
                da = '$%s$' % (kq)
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 207; green, 237; blue, 230 }  ,fill opacity=1 ] (490.67,163.98) .. controls (493.26,148.35) and (496.14,133.21) .. (506.74,131.08) .. controls (511.69,130.13) and (511.39,142.74) .. (507.8,149.92) .. controls (512.33,160.26) and (493.96,169.09) .. (490.67,163.98) -- cycle ;
            	\draw    (490.67,163.98) .. controls (495.98,152.62) and (503.23,148.58) .. (507.8,149.92) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (490.67,163.98) -- (500.17,156.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (500.17,156.9) -- (507.8,149.92) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (499.09,158.71) -- (505.67,159.19) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (497.72,154.16) -- (503.24,153.41) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (490.67,163.98) -- (502.59,140.24) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (497.64,149.71) -- (504.31,148.77) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (500.26,144.7) -- (499.05,137.39) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (502.59,140.24) -- (509.8,134.5) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (500.26,144.7) -- (506.27,142.34) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (504.31,148.77) -- (506.27,142.34) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (506.27,142.34) -- (509.94,139.61) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (502.59,140.24) -- (504.23,132.58) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (497.64,149.71) -- (495.46,144.57) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (527.1,190.55) -- (516.55,182.75) -- (520.05,179) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (500.18,171.58) .. controls (497.25,174.5) and (494.41,188.08) .. (497.35,186.65) .. controls (499.61,185.73) and (501.79,171.92) .. (500.18,171.58) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (489.13,166.62) .. controls (487.37,168.72) and (484.91,178.39) .. (486.57,177.35) .. controls (487.84,176.67) and (489.97,166.85) .. (489.13,166.62) -- cycle ;
            	\draw    (474.8,154.3) -- (479.3,160.55) ;
            	\draw  [fill={rgb, 255:red, 245; green, 208; blue, 35 }  ,fill opacity=1 ] (500.69,166.66) .. controls (504.64,162.61) and (512.1,163.46) .. (517.35,168.58) .. controls (522.61,173.69) and (523.67,181.13) .. (519.72,185.18) .. controls (515.77,189.24) and (508.31,188.39) .. (503.05,183.27) .. controls (497.8,178.16) and (496.74,170.72) .. (500.69,166.66) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.48 ] (503.74,165.73) .. controls (505.98,163.42) and (511.56,165.21) .. (516.2,169.72) .. controls (520.83,174.23) and (522.77,179.76) .. (520.53,182.07) .. controls (518.28,184.37) and (512.7,182.59) .. (508.07,178.07) .. controls (503.43,173.56) and (501.49,168.03) .. (503.74,165.73) -- cycle ;
            	\draw  [color={rgb, 255:red, 180; green, 117; blue, 13 }  ,draw opacity=1 ][fill={rgb, 255:red, 249; green, 194; blue, 103 }  ,fill opacity=1 ] (457.54,94.13) -- (430.7,111.87) -- (401.92,97.5) -- (399.97,65.39) -- (426.81,47.65) -- (455.59,62.02) -- cycle ;
            	\draw  [color={rgb, 255:red, 200; green, 132; blue, 18 }  ,draw opacity=1 ][fill={rgb, 255:red, 245; green, 200; blue, 123 }  ,fill opacity=1 ] (453.73,92.23) -- (430.44,107.63) -- (405.46,95.16) -- (403.77,67.29) -- (427.06,51.89) -- (452.04,64.36) -- cycle ;
            	\draw  [color={rgb, 255:red, 178; green, 117; blue, 15 }  ,draw opacity=1 ][fill={rgb, 255:red, 237; green, 219; blue, 109 }  ,fill opacity=1 ] (449.24,95.6) -- (430.44,108.03) -- (410.28,97.96) -- (408.92,75.47) -- (427.71,63.04) -- (447.88,73.11) -- cycle ;
            	\draw [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ]   (403.77,67.29) -- (408.92,75.07) ;
            	\draw [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ]   (427.06,51.89) -- (427.71,62.64) ;
            	\draw [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ]   (452.04,64.36) -- (447.88,72.71) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 145; blue, 19 }  ,fill opacity=1 ] (427.06,51.89) -- (427.71,62.64) -- (408.92,75.07) -- (410.28,97.56) -- (405.46,95.16) -- (403.77,67.29) -- cycle ;
            	\draw  [color={rgb, 255:red, 180; green, 117; blue, 13 }  ,draw opacity=1 ][fill={rgb, 255:red, 249; green, 194; blue, 103 }  ,fill opacity=1 ] (431.54,144.13) -- (404.7,161.87) -- (375.92,147.5) -- (373.97,115.39) -- (400.81,97.65) -- (429.59,112.02) -- cycle ;
            	\draw  [color={rgb, 255:red, 200; green, 132; blue, 18 }  ,draw opacity=1 ][fill={rgb, 255:red, 245; green, 200; blue, 123 }  ,fill opacity=1 ] (427.73,142.23) -- (404.44,157.63) -- (379.46,145.16) -- (377.77,117.29) -- (401.06,101.89) -- (426.04,114.36) -- cycle ;
            	\draw  [color={rgb, 255:red, 178; green, 117; blue, 15 }  ,draw opacity=1 ][fill={rgb, 255:red, 237; green, 219; blue, 109 }  ,fill opacity=1 ] (423.24,145.6) -- (404.44,158.03) -- (384.28,147.96) -- (382.92,125.47) -- (401.71,113.04) -- (421.88,123.11) -- cycle ;
            	\draw [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ]   (377.77,117.29) -- (382.92,125.07) ;
            	\draw [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ]   (401.06,101.89) -- (401.71,112.64) ;
            	\draw [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ]   (426.04,114.36) -- (421.88,122.71) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 145; blue, 19 }  ,fill opacity=1 ] (401.06,101.89) -- (401.71,112.64) -- (382.92,125.07) -- (384.28,147.56) -- (379.46,145.16) -- (377.77,117.29) -- cycle ;
            	\draw  [color={rgb, 255:red, 180; green, 117; blue, 13 }  ,draw opacity=1 ][fill={rgb, 255:red, 249; green, 194; blue, 103 }  ,fill opacity=1 ] (462.54,191.13) -- (435.7,208.87) -- (406.92,194.5) -- (404.97,162.39) -- (431.81,144.65) -- (460.59,159.02) -- cycle ;
            	\draw  [color={rgb, 255:red, 200; green, 132; blue, 18 }  ,draw opacity=1 ][fill={rgb, 255:red, 245; green, 200; blue, 123 }  ,fill opacity=1 ] (458.73,189.23) -- (435.44,204.63) -- (410.46,192.16) -- (408.77,164.29) -- (432.06,148.89) -- (457.04,161.36) -- cycle ;
            	\draw [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ]   (408.77,164.29) -- (413.92,172.07) ;
            	\draw [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ]   (432.06,148.89) -- (432.71,159.64) ;
            	\draw [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ]   (457.04,161.36) -- (452.88,169.71) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 220; green, 145; blue, 19 }  ,fill opacity=1 ] (432.06,148.89) -- (432.71,159.64) -- (413.92,172.07) -- (415.28,194.56) -- (410.46,192.16) -- (408.77,164.29) -- cycle ;
            	\draw  [color={rgb, 255:red, 178; green, 117; blue, 15 }  ,draw opacity=1 ][fill={rgb, 255:red, 237; green, 219; blue, 109 }  ,fill opacity=1 ] (455.86,191.53) -- (435.44,205.03) -- (413.54,194.09) -- (412.06,169.66) -- (432.48,156.16) -- (454.38,167.09) -- cycle ;
            	\draw  [color={rgb, 255:red, 180; green, 117; blue, 13 }  ,draw opacity=1 ][fill={rgb, 255:red, 249; green, 194; blue, 103 }  ,fill opacity=1 ] (406.04,194.63) -- (379.2,212.37) -- (350.42,198) -- (348.47,165.89) -- (375.31,148.15) -- (404.09,162.52) -- cycle ;
            	\draw  [color={rgb, 255:red, 200; green, 132; blue, 18 }  ,draw opacity=1 ][fill={rgb, 255:red, 222; green, 146; blue, 17 }  ,fill opacity=1 ] (402.23,192.73) -- (378.94,208.13) -- (353.96,195.66) -- (352.27,167.79) -- (375.56,152.39) -- (400.54,164.86) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 186; blue, 84 }  ,fill opacity=1 ] (353.25,180.26) .. controls (353.25,167.75) and (364,157.62) .. (377.25,157.62) .. controls (390.51,157.62) and (401.25,167.75) .. (401.25,180.26) .. controls (401.25,192.76) and (390.51,202.9) .. (377.25,202.9) .. controls (364,202.9) and (353.25,192.76) .. (353.25,180.26) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.21 ] (363.75,184.7) .. controls (363.75,176.86) and (371.29,170.5) .. (380.58,170.5) .. controls (389.88,170.5) and (397.42,176.86) .. (397.42,184.7) .. controls (397.42,192.54) and (389.88,198.9) .. (380.58,198.9) .. controls (371.29,198.9) and (363.75,192.54) .. (363.75,184.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.42 ] (359.4,165.4) .. controls (378.4,153.9) and (387.4,154.9) .. (392.4,167.9) .. controls (383.4,173.9) and (375.4,155.4) .. (359.9,181.9) .. controls (356.4,176.9) and (354.4,174.4) .. (359.4,165.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.66 ] (368.45,160.8) .. controls (370.26,160.13) and (375.04,158.9) .. (376.57,160.8) .. controls (378.09,162.69) and (377.78,163.49) .. (373.45,165.62) .. controls (369.12,167.76) and (364.97,169.52) .. (363.17,167.52) .. controls (361.37,165.52) and (366.65,161.46) .. (368.45,160.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.68 ] (398.03,181.32) .. controls (398.05,190.13) and (390.47,202.76) .. (376.11,197.32) .. controls (390.02,195.63) and (393.54,191.27) .. (398.03,181.32) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.37 ] (372.4,187.29) .. controls (372.4,183.21) and (376.88,179.9) .. (382.4,179.9) .. controls (387.93,179.9) and (392.41,183.21) .. (392.41,187.29) .. controls (392.41,191.37) and (387.93,194.68) .. (382.4,194.68) .. controls (376.88,194.68) and (372.4,191.37) .. (372.4,187.29) -- cycle ;
            	\draw  [color={rgb, 255:red, 180; green, 117; blue, 13 }  ,draw opacity=1 ][fill={rgb, 255:red, 249; green, 194; blue, 103 }  ,fill opacity=1 ] (488.54,141.63) -- (461.7,159.37) -- (432.92,145) -- (430.97,112.89) -- (457.81,95.15) -- (486.59,109.52) -- cycle ;
            	\draw  [color={rgb, 255:red, 200; green, 132; blue, 18 }  ,draw opacity=1 ][fill={rgb, 255:red, 222; green, 146; blue, 17 }  ,fill opacity=1 ] (484.73,139.73) -- (461.44,155.13) -- (436.46,142.66) -- (434.77,114.79) -- (458.06,99.39) -- (483.04,111.86) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 186; blue, 84 }  ,fill opacity=1 ] (435.75,127.26) .. controls (435.75,114.75) and (446.5,104.62) .. (459.75,104.62) .. controls (473.01,104.62) and (483.75,114.75) .. (483.75,127.26) .. controls (483.75,139.76) and (473.01,149.9) .. (459.75,149.9) .. controls (446.5,149.9) and (435.75,139.76) .. (435.75,127.26) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.21 ] (446.25,131.7) .. controls (446.25,123.86) and (453.79,117.5) .. (463.08,117.5) .. controls (472.38,117.5) and (479.92,123.86) .. (479.92,131.7) .. controls (479.92,139.54) and (472.38,145.9) .. (463.08,145.9) .. controls (453.79,145.9) and (446.25,139.54) .. (446.25,131.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.42 ] (441.9,112.4) .. controls (460.9,100.9) and (469.9,101.9) .. (474.9,114.9) .. controls (465.9,120.9) and (457.9,102.4) .. (442.4,128.9) .. controls (438.9,123.9) and (436.9,121.4) .. (441.9,112.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.66 ] (450.95,107.8) .. controls (452.76,107.13) and (457.54,105.9) .. (459.07,107.8) .. controls (460.59,109.69) and (460.28,110.49) .. (455.95,112.62) .. controls (451.62,114.76) and (447.47,116.52) .. (445.67,114.52) .. controls (443.87,112.52) and (449.15,108.46) .. (450.95,107.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.68 ] (480.53,128.32) .. controls (480.55,137.13) and (472.97,149.76) .. (458.61,144.32) .. controls (472.52,142.63) and (476.04,138.27) .. (480.53,128.32) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.37 ] (454.9,134.29) .. controls (454.9,130.21) and (459.38,126.9) .. (464.9,126.9) .. controls (470.43,126.9) and (474.91,130.21) .. (474.91,134.29) .. controls (474.91,138.37) and (470.43,141.68) .. (464.9,141.68) .. controls (459.38,141.68) and (454.9,138.37) .. (454.9,134.29) -- cycle ;
            	\draw  [color={rgb, 255:red, 180; green, 117; blue, 13 }  ,draw opacity=1 ][fill={rgb, 255:red, 249; green, 194; blue, 103 }  ,fill opacity=1 ] (375.54,146.63) -- (348.7,164.37) -- (319.92,150) -- (317.97,117.89) -- (344.81,100.15) -- (373.59,114.52) -- cycle ;
            	\draw  [color={rgb, 255:red, 200; green, 132; blue, 18 }  ,draw opacity=1 ][fill={rgb, 255:red, 222; green, 146; blue, 17 }  ,fill opacity=1 ] (371.73,144.73) -- (348.44,160.13) -- (323.46,147.66) -- (321.77,119.79) -- (345.06,104.39) -- (370.04,116.86) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 186; blue, 84 }  ,fill opacity=1 ] (322.75,132.26) .. controls (322.75,119.75) and (333.5,109.62) .. (346.75,109.62) .. controls (360.01,109.62) and (370.75,119.75) .. (370.75,132.26) .. controls (370.75,144.76) and (360.01,154.9) .. (346.75,154.9) .. controls (333.5,154.9) and (322.75,144.76) .. (322.75,132.26) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.21 ] (333.25,136.7) .. controls (333.25,128.86) and (340.79,122.5) .. (350.08,122.5) .. controls (359.38,122.5) and (366.92,128.86) .. (366.92,136.7) .. controls (366.92,144.54) and (359.38,150.9) .. (350.08,150.9) .. controls (340.79,150.9) and (333.25,144.54) .. (333.25,136.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.42 ] (328.9,117.4) .. controls (347.9,105.9) and (356.9,106.9) .. (361.9,119.9) .. controls (352.9,125.9) and (344.9,107.4) .. (329.4,133.9) .. controls (325.9,128.9) and (323.9,126.4) .. (328.9,117.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.66 ] (337.95,112.8) .. controls (339.76,112.13) and (344.54,110.9) .. (346.07,112.8) .. controls (347.59,114.69) and (347.28,115.49) .. (342.95,117.62) .. controls (338.62,119.76) and (334.47,121.52) .. (332.67,119.52) .. controls (330.87,117.52) and (336.15,113.46) .. (337.95,112.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.68 ] (367.53,133.32) .. controls (367.55,142.13) and (359.97,154.76) .. (345.61,149.32) .. controls (359.52,147.63) and (363.04,143.27) .. (367.53,133.32) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.37 ] (341.9,139.29) .. controls (341.9,135.21) and (346.38,131.9) .. (351.9,131.9) .. controls (357.43,131.9) and (361.91,135.21) .. (361.91,139.29) .. controls (361.91,143.37) and (357.43,146.68) .. (351.9,146.68) .. controls (346.38,146.68) and (341.9,143.37) .. (341.9,139.29) -- cycle ;
            	\draw  [color={rgb, 255:red, 180; green, 117; blue, 13 }  ,draw opacity=1 ][fill={rgb, 255:red, 249; green, 194; blue, 103 }  ,fill opacity=1 ] (401.04,96.63) -- (374.2,114.37) -- (345.42,100) -- (343.47,67.89) -- (370.31,50.15) -- (399.09,64.52) -- cycle ;
            	\draw  [color={rgb, 255:red, 200; green, 132; blue, 18 }  ,draw opacity=1 ][fill={rgb, 255:red, 222; green, 146; blue, 17 }  ,fill opacity=1 ] (397.23,94.73) -- (373.94,110.13) -- (348.96,97.66) -- (347.27,69.79) -- (370.56,54.39) -- (395.54,66.86) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 186; blue, 84 }  ,fill opacity=1 ] (348.25,82.26) .. controls (348.25,69.75) and (359,59.62) .. (372.25,59.62) .. controls (385.51,59.62) and (396.25,69.75) .. (396.25,82.26) .. controls (396.25,94.76) and (385.51,104.9) .. (372.25,104.9) .. controls (359,104.9) and (348.25,94.76) .. (348.25,82.26) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.21 ] (358.75,86.7) .. controls (358.75,78.86) and (366.29,72.5) .. (375.58,72.5) .. controls (384.88,72.5) and (392.42,78.86) .. (392.42,86.7) .. controls (392.42,94.54) and (384.88,100.9) .. (375.58,100.9) .. controls (366.29,100.9) and (358.75,94.54) .. (358.75,86.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.42 ] (354.4,67.4) .. controls (373.4,55.9) and (382.4,56.9) .. (387.4,69.9) .. controls (378.4,75.9) and (370.4,57.4) .. (354.9,83.9) .. controls (351.4,78.9) and (349.4,76.4) .. (354.4,67.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.66 ] (363.45,62.8) .. controls (365.26,62.13) and (370.04,60.9) .. (371.57,62.8) .. controls (373.09,64.69) and (372.78,65.49) .. (368.45,67.62) .. controls (364.12,69.76) and (359.97,71.52) .. (358.17,69.52) .. controls (356.37,67.52) and (361.65,63.46) .. (363.45,62.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.68 ] (393.03,83.32) .. controls (393.05,92.13) and (385.47,104.76) .. (371.11,99.32) .. controls (385.02,97.63) and (388.54,93.27) .. (393.03,83.32) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.37 ] (367.4,89.29) .. controls (367.4,85.21) and (371.88,81.9) .. (377.4,81.9) .. controls (382.93,81.9) and (387.41,85.21) .. (387.41,89.29) .. controls (387.41,93.37) and (382.93,96.68) .. (377.4,96.68) .. controls (371.88,96.68) and (367.4,93.37) .. (367.4,89.29) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (461.24,120.2) .. controls (461.24,118.71) and (462.44,117.5) .. (463.93,117.5) .. controls (465.43,117.5) and (466.63,118.71) .. (466.63,120.2) .. controls (466.63,121.69) and (465.43,122.9) .. (463.93,122.9) .. controls (462.44,122.9) and (461.24,121.69) .. (461.24,120.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (463.94,137.67) .. controls (463.94,136.57) and (464.82,135.69) .. (465.92,135.69) .. controls (467.01,135.69) and (467.9,136.57) .. (467.9,137.67) .. controls (467.9,138.76) and (467.01,139.65) .. (465.92,139.65) .. controls (464.82,139.65) and (463.94,138.76) .. (463.94,137.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (443.94,127.17) .. controls (443.94,126.07) and (444.82,125.19) .. (445.92,125.19) .. controls (447.01,125.19) and (447.9,126.07) .. (447.9,127.17) .. controls (447.9,128.26) and (447.01,129.15) .. (445.92,129.15) .. controls (444.82,129.15) and (443.94,128.26) .. (443.94,127.17) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (450.94,134.29) .. controls (450.94,133.19) and (451.82,132.31) .. (452.92,132.31) .. controls (454.01,132.31) and (454.9,133.19) .. (454.9,134.29) .. controls (454.9,135.38) and (454.01,136.27) .. (452.92,136.27) .. controls (451.82,136.27) and (450.94,135.38) .. (450.94,134.29) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (452.94,119.42) .. controls (452.94,118.32) and (453.82,117.44) .. (454.92,117.44) .. controls (456.01,117.44) and (456.9,118.32) .. (456.9,119.42) .. controls (456.9,120.51) and (456.01,121.4) .. (454.92,121.4) .. controls (453.82,121.4) and (452.94,120.51) .. (452.94,119.42) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (473.19,128.67) .. controls (473.19,127.57) and (474.07,126.69) .. (475.17,126.69) .. controls (476.26,126.69) and (477.15,127.57) .. (477.15,128.67) .. controls (477.15,129.76) and (476.26,130.65) .. (475.17,130.65) .. controls (474.07,130.65) and (473.19,129.76) .. (473.19,128.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (461.1,129.72) .. controls (461.1,128.63) and (461.99,127.74) .. (463.08,127.74) .. controls (464.18,127.74) and (465.07,128.63) .. (465.07,129.72) .. controls (465.07,130.81) and (464.18,131.7) .. (463.08,131.7) .. controls (461.99,131.7) and (461.1,130.81) .. (461.1,129.72) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (467.69,112.84) .. controls (467.69,111.74) and (468.57,110.85) .. (469.67,110.85) .. controls (470.76,110.85) and (471.65,111.74) .. (471.65,112.84) .. controls (471.65,113.93) and (470.76,114.82) .. (469.67,114.82) .. controls (468.57,114.82) and (467.69,113.93) .. (467.69,112.84) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (452.92,136.27) .. controls (452.92,135.17) and (453.81,134.29) .. (454.9,134.29) .. controls (455.99,134.29) and (456.88,135.17) .. (456.88,136.27) .. controls (456.88,137.36) and (455.99,138.25) .. (454.9,138.25) .. controls (453.81,138.25) and (452.92,137.36) .. (452.92,136.27) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (360.52,126.72) .. controls (360.52,125.62) and (361.41,124.74) .. (362.5,124.74) .. controls (363.59,124.74) and (364.48,125.62) .. (364.48,126.72) .. controls (364.48,127.81) and (363.59,128.7) .. (362.5,128.7) .. controls (361.41,128.7) and (360.52,127.81) .. (360.52,126.72) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (346.12,136.7) .. controls (346.12,135.61) and (347.01,134.72) .. (348.1,134.72) .. controls (349.2,134.72) and (350.08,135.61) .. (350.08,136.7) .. controls (350.08,137.79) and (349.2,138.68) .. (348.1,138.68) .. controls (347.01,138.68) and (346.12,137.79) .. (346.12,136.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (350.08,136.7) .. controls (350.08,135.61) and (350.97,134.72) .. (352.07,134.72) .. controls (353.16,134.72) and (354.05,135.61) .. (354.05,136.7) .. controls (354.05,137.79) and (353.16,138.68) .. (352.07,138.68) .. controls (350.97,138.68) and (350.08,137.79) .. (350.08,136.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (359.93,139.29) .. controls (359.93,138.19) and (360.81,137.31) .. (361.91,137.31) .. controls (363,137.31) and (363.89,138.19) .. (363.89,139.29) .. controls (363.89,140.38) and (363,141.27) .. (361.91,141.27) .. controls (360.81,141.27) and (359.93,140.38) .. (359.93,139.29) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (387.41,89.29) .. controls (387.41,88.19) and (388.29,87.31) .. (389.39,87.31) .. controls (390.48,87.31) and (391.37,88.19) .. (391.37,89.29) .. controls (391.37,90.38) and (390.48,91.27) .. (389.39,91.27) .. controls (388.29,91.27) and (387.41,90.38) .. (387.41,89.29) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (344.77,130.28) .. controls (344.77,129.18) and (345.66,128.3) .. (346.75,128.3) .. controls (347.85,128.3) and (348.73,129.18) .. (348.73,130.28) .. controls (348.73,131.37) and (347.85,132.26) .. (346.75,132.26) .. controls (345.66,132.26) and (344.77,131.37) .. (344.77,130.28) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (355.69,131.72) .. controls (355.69,130.62) and (356.57,129.74) .. (357.67,129.74) .. controls (358.76,129.74) and (359.65,130.62) .. (359.65,131.72) .. controls (359.65,132.81) and (358.76,133.7) .. (357.67,133.7) .. controls (356.57,133.7) and (355.69,132.81) .. (355.69,131.72) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (344.19,145.22) .. controls (344.19,144.12) and (345.07,143.24) .. (346.17,143.24) .. controls (347.26,143.24) and (348.15,144.12) .. (348.15,145.22) .. controls (348.15,146.31) and (347.26,147.2) .. (346.17,147.2) .. controls (345.07,147.2) and (344.19,146.31) .. (344.19,145.22) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (327.42,131.92) .. controls (327.42,130.82) and (328.31,129.94) .. (329.4,129.94) .. controls (330.49,129.94) and (331.38,130.82) .. (331.38,131.92) .. controls (331.38,133.01) and (330.49,133.9) .. (329.4,133.9) .. controls (328.31,133.9) and (327.42,133.01) .. (327.42,131.92) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (335.69,122.97) .. controls (335.69,121.87) and (336.57,120.99) .. (337.67,120.99) .. controls (338.76,120.99) and (339.65,121.87) .. (339.65,122.97) .. controls (339.65,124.06) and (338.76,124.95) .. (337.67,124.95) .. controls (336.57,124.95) and (335.69,124.06) .. (335.69,122.97) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (354.69,121.47) .. controls (354.69,120.37) and (355.57,119.49) .. (356.67,119.49) .. controls (357.76,119.49) and (358.65,120.37) .. (358.65,121.47) .. controls (358.65,122.56) and (357.76,123.45) .. (356.67,123.45) .. controls (355.57,123.45) and (354.69,122.56) .. (354.69,121.47) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (338.19,136.97) .. controls (338.19,135.87) and (339.07,134.99) .. (340.17,134.99) .. controls (341.26,134.99) and (342.15,135.87) .. (342.15,136.97) .. controls (342.15,138.06) and (341.26,138.95) .. (340.17,138.95) .. controls (339.07,138.95) and (338.19,138.06) .. (338.19,136.97) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (368.44,71.72) .. controls (368.44,70.62) and (369.32,69.74) .. (370.42,69.74) .. controls (371.51,69.74) and (372.4,70.62) .. (372.4,71.72) .. controls (372.4,72.81) and (371.51,73.7) .. (370.42,73.7) .. controls (369.32,73.7) and (368.44,72.81) .. (368.44,71.72) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (377.94,86.22) .. controls (377.94,85.12) and (378.82,84.24) .. (379.92,84.24) .. controls (381.01,84.24) and (381.9,85.12) .. (381.9,86.22) .. controls (381.9,87.31) and (381.01,88.2) .. (379.92,88.2) .. controls (378.82,88.2) and (377.94,87.31) .. (377.94,86.22) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (356.77,88.68) .. controls (356.77,87.59) and (357.66,86.7) .. (358.75,86.7) .. controls (359.85,86.7) and (360.73,87.59) .. (360.73,88.68) .. controls (360.73,89.78) and (359.85,90.66) .. (358.75,90.66) .. controls (357.66,90.66) and (356.77,89.78) .. (356.77,88.68) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (385.77,76.18) .. controls (385.77,75.09) and (386.66,74.2) .. (387.75,74.2) .. controls (388.85,74.2) and (389.73,75.09) .. (389.73,76.18) .. controls (389.73,77.28) and (388.85,78.16) .. (387.75,78.16) .. controls (386.66,78.16) and (385.77,77.28) .. (385.77,76.18) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (367.02,96.93) .. controls (367.02,95.84) and (367.91,94.95) .. (369,94.95) .. controls (370.1,94.95) and (370.98,95.84) .. (370.98,96.93) .. controls (370.98,98.03) and (370.1,98.91) .. (369,98.91) .. controls (367.91,98.91) and (367.02,98.03) .. (367.02,96.93) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (368.29,82.26) .. controls (368.29,81.16) and (369.18,80.28) .. (370.27,80.28) .. controls (371.37,80.28) and (372.25,81.16) .. (372.25,82.26) .. controls (372.25,83.35) and (371.37,84.24) .. (370.27,84.24) .. controls (369.18,84.24) and (368.29,83.35) .. (368.29,82.26) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (358.04,76.26) .. controls (358.04,75.16) and (358.93,74.28) .. (360.02,74.28) .. controls (361.12,74.28) and (362,75.16) .. (362,76.26) .. controls (362,77.35) and (361.12,78.24) .. (360.02,78.24) .. controls (358.93,78.24) and (358.04,77.35) .. (358.04,76.26) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (378.04,96.26) .. controls (378.04,95.16) and (378.93,94.28) .. (380.02,94.28) .. controls (381.12,94.28) and (382,95.16) .. (382,96.26) .. controls (382,97.35) and (381.12,98.24) .. (380.02,98.24) .. controls (378.93,98.24) and (378.04,97.35) .. (378.04,96.26) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (375.54,75.51) .. controls (375.54,74.41) and (376.43,73.53) .. (377.52,73.53) .. controls (378.62,73.53) and (379.5,74.41) .. (379.5,75.51) .. controls (379.5,76.6) and (378.62,77.49) .. (377.52,77.49) .. controls (376.43,77.49) and (375.54,76.6) .. (375.54,75.51) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (365.42,87.31) .. controls (365.42,86.21) and (366.31,85.33) .. (367.4,85.33) .. controls (368.49,85.33) and (369.38,86.21) .. (369.38,87.31) .. controls (369.38,88.4) and (368.49,89.29) .. (367.4,89.29) .. controls (366.31,89.29) and (365.42,88.4) .. (365.42,87.31) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (453.81,125.99) .. controls (453.81,125.07) and (454.55,124.33) .. (455.47,124.33) .. controls (456.39,124.33) and (457.13,125.07) .. (457.13,125.99) .. controls (457.13,126.91) and (456.39,127.65) .. (455.47,127.65) .. controls (454.55,127.65) and (453.81,126.91) .. (453.81,125.99) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (455.56,141.99) .. controls (455.56,141.07) and (456.3,140.33) .. (457.22,140.33) .. controls (458.14,140.33) and (458.88,141.07) .. (458.88,141.99) .. controls (458.88,142.91) and (458.14,143.65) .. (457.22,143.65) .. controls (456.3,143.65) and (455.56,142.91) .. (455.56,141.99) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (469.56,123.24) .. controls (469.56,122.32) and (470.3,121.58) .. (471.22,121.58) .. controls (472.14,121.58) and (472.88,122.32) .. (472.88,123.24) .. controls (472.88,124.16) and (472.14,124.9) .. (471.22,124.9) .. controls (470.3,124.9) and (469.56,124.16) .. (469.56,123.24) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (467.81,132.74) .. controls (467.81,131.82) and (468.55,131.08) .. (469.47,131.08) .. controls (470.39,131.08) and (471.13,131.82) .. (471.13,132.74) .. controls (471.13,133.66) and (470.39,134.4) .. (469.47,134.4) .. controls (468.55,134.4) and (467.81,133.66) .. (467.81,132.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (463.93,117.5) .. controls (463.93,116.58) and (464.68,115.84) .. (465.6,115.84) .. controls (466.52,115.84) and (467.26,116.58) .. (467.26,117.5) .. controls (467.26,118.42) and (466.52,119.16) .. (465.6,119.16) .. controls (464.68,119.16) and (463.93,118.42) .. (463.93,117.5) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (380.93,82.78) .. controls (380.93,81.86) and (381.67,81.11) .. (382.59,81.11) .. controls (383.51,81.11) and (384.25,81.86) .. (384.25,82.78) .. controls (384.25,83.69) and (383.51,84.44) .. (382.59,84.44) .. controls (381.67,84.44) and (380.93,83.69) .. (380.93,82.78) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (451.26,130.64) .. controls (451.26,129.73) and (452,128.98) .. (452.92,128.98) .. controls (453.84,128.98) and (454.58,129.73) .. (454.58,130.64) .. controls (454.58,131.56) and (453.84,132.31) .. (452.92,132.31) .. controls (452,132.31) and (451.26,131.56) .. (451.26,130.64) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (446.72,121.4) .. controls (446.72,120.49) and (447.47,119.74) .. (448.39,119.74) .. controls (449.3,119.74) and (450.05,120.49) .. (450.05,121.4) .. controls (450.05,122.32) and (449.3,123.07) .. (448.39,123.07) .. controls (447.47,123.07) and (446.72,122.32) .. (446.72,121.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (352.06,140.74) .. controls (352.06,139.82) and (352.8,139.08) .. (353.72,139.08) .. controls (354.64,139.08) and (355.38,139.82) .. (355.38,140.74) .. controls (355.38,141.66) and (354.64,142.4) .. (353.72,142.4) .. controls (352.8,142.4) and (352.06,141.66) .. (352.06,140.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (346.76,122.5) .. controls (346.76,121.58) and (347.5,120.84) .. (348.42,120.84) .. controls (349.34,120.84) and (350.08,121.58) .. (350.08,122.5) .. controls (350.08,123.42) and (349.34,124.16) .. (348.42,124.16) .. controls (347.5,124.16) and (346.76,123.42) .. (346.76,122.5) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (335.51,130.25) .. controls (335.51,129.33) and (336.25,128.59) .. (337.17,128.59) .. controls (338.09,128.59) and (338.83,129.33) .. (338.83,130.25) .. controls (338.83,131.17) and (338.09,131.91) .. (337.17,131.91) .. controls (336.25,131.91) and (335.51,131.17) .. (335.51,130.25) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=0.47 ] (333.26,142.25) .. controls (333.26,141.33) and (334,140.59) .. (334.92,140.59) .. controls (335.84,140.59) and (336.58,141.33) .. (336.58,142.25) .. controls (336.58,143.17) and (335.84,143.91) .. (334.92,143.91) .. controls (334,143.91) and (333.26,143.17) .. (333.26,142.25) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (365.01,78.5) .. controls (365.01,77.58) and (365.75,76.84) .. (366.67,76.84) .. controls (367.59,76.84) and (368.33,77.58) .. (368.33,78.5) .. controls (368.33,79.42) and (367.59,80.16) .. (366.67,80.16) .. controls (365.75,80.16) and (365.01,79.42) .. (365.01,78.5) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (372.01,89.5) .. controls (372.01,88.58) and (372.75,87.84) .. (373.67,87.84) .. controls (374.59,87.84) and (375.33,88.58) .. (375.33,89.5) .. controls (375.33,90.42) and (374.59,91.16) .. (373.67,91.16) .. controls (372.75,91.16) and (372.01,90.42) .. (372.01,89.5) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (458.26,135.25) .. controls (458.26,134.33) and (459,133.59) .. (459.92,133.59) .. controls (460.84,133.59) and (461.58,134.33) .. (461.58,135.25) .. controls (461.58,136.17) and (460.84,136.91) .. (459.92,136.91) .. controls (459,136.91) and (458.26,136.17) .. (458.26,135.25) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (444.59,133.36) .. controls (444.59,132.44) and (445.33,131.7) .. (446.25,131.7) .. controls (447.17,131.7) and (447.91,132.44) .. (447.91,133.36) .. controls (447.91,134.28) and (447.17,135.03) .. (446.25,135.03) .. controls (445.33,135.03) and (444.59,134.28) .. (444.59,133.36) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (345.84,137.61) .. controls (345.84,136.69) and (346.58,135.95) .. (347.5,135.95) .. controls (348.42,135.95) and (349.16,136.69) .. (349.16,137.61) .. controls (349.16,138.53) and (348.42,139.28) .. (347.5,139.28) .. controls (346.58,139.28) and (345.84,138.53) .. (345.84,137.61) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (349.59,127.36) .. controls (349.59,126.44) and (350.33,125.7) .. (351.25,125.7) .. controls (352.17,125.7) and (352.91,126.44) .. (352.91,127.36) .. controls (352.91,128.28) and (352.17,129.03) .. (351.25,129.03) .. controls (350.33,129.03) and (349.59,128.28) .. (349.59,127.36) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (382.59,81.11) .. controls (382.59,80.19) and (383.33,79.45) .. (384.25,79.45) .. controls (385.17,79.45) and (385.91,80.19) .. (385.91,81.11) .. controls (385.91,82.03) and (385.17,82.78) .. (384.25,82.78) .. controls (383.33,82.78) and (382.59,82.03) .. (382.59,81.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (367.34,93.29) .. controls (367.34,92.37) and (368.08,91.63) .. (369,91.63) .. controls (369.92,91.63) and (370.66,92.37) .. (370.66,93.29) .. controls (370.66,94.21) and (369.92,94.95) .. (369,94.95) .. controls (368.08,94.95) and (367.34,94.21) .. (367.34,93.29) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 208; blue, 35 }  ,fill opacity=1 ] (485.42,161.29) .. controls (488.16,157.32) and (493.72,156.4) .. (497.83,159.25) .. controls (501.95,162.09) and (503.06,167.61) .. (500.32,171.58) .. controls (497.58,175.56) and (492.02,176.47) .. (487.9,173.63) .. controls (483.79,170.79) and (482.67,165.26) .. (485.42,161.29) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.45 ] (483.99,164.48) .. controls (483.99,161.18) and (487.75,158.5) .. (492.4,158.5) .. controls (497.04,158.5) and (500.8,161.18) .. (500.8,164.48) .. controls (500.8,167.77) and (497.04,170.45) .. (492.4,170.45) .. controls (487.75,170.45) and (483.99,167.77) .. (483.99,164.48) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (473.73,161.73) .. controls (474.8,160.18) and (476.49,159.5) .. (477.5,160.19) .. controls (478.51,160.89) and (478.47,162.71) .. (477.4,164.26) .. controls (476.33,165.81) and (474.64,166.5) .. (473.63,165.8) .. controls (472.62,165.1) and (472.67,163.28) .. (473.73,161.73) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 208; blue, 35 }  ,fill opacity=1 ] (476.08,161.84) .. controls (479.38,157.07) and (484.79,155.09) .. (488.17,157.43) .. controls (491.54,159.76) and (491.61,165.52) .. (488.32,170.29) .. controls (485.02,175.06) and (479.61,177.04) .. (476.23,174.71) .. controls (472.86,172.37) and (472.79,166.61) .. (476.08,161.84) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (482.23,163.23) .. controls (483.3,161.68) and (484.99,161) .. (486,161.69) .. controls (487.01,162.39) and (486.97,164.21) .. (485.9,165.76) .. controls (484.83,167.31) and (483.14,168) .. (482.13,167.3) .. controls (481.12,166.6) and (481.17,164.78) .. (482.23,163.23) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (483.07,163.57) .. controls (483.07,163.06) and (483.48,162.65) .. (483.99,162.65) .. controls (484.5,162.65) and (484.92,163.06) .. (484.92,163.57) .. controls (484.92,164.08) and (484.5,164.5) .. (483.99,164.5) .. controls (483.48,164.5) and (483.07,164.08) .. (483.07,163.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (474.07,161.57) .. controls (474.07,161.06) and (474.48,160.65) .. (474.99,160.65) .. controls (475.5,160.65) and (475.92,161.06) .. (475.92,161.57) .. controls (475.92,162.08) and (475.5,162.5) .. (474.99,162.5) .. controls (474.48,162.5) and (474.07,162.08) .. (474.07,161.57) -- cycle ;
            	\draw    (476.06,172.02) .. controls (477.95,173.78) and (480.8,174.45) .. (482.8,170.75) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (479.85,151.12) .. controls (478.36,148.82) and (469.82,143.65) .. (470.34,145.54) .. controls (470.62,146.95) and (479.39,151.85) .. (479.85,151.12) -- cycle ;
            	\draw    (479.85,151.12) -- (483.05,159.8) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (474.8,154.3) .. controls (472.14,153.65) and (462.38,155.73) .. (464.05,156.75) .. controls (465.22,157.59) and (474.97,155.15) .. (474.8,154.3) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (493.9,170.95) .. controls (492.03,172.96) and (489.1,182.5) .. (490.81,181.53) .. controls (492.11,180.92) and (494.72,171.22) .. (493.9,170.95) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (490.81,181.53) .. controls (488.11,181.08) and (478.53,183.87) .. (480.27,184.77) .. controls (481.5,185.52) and (491.04,182.37) .. (490.81,181.53) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (486.57,177.35) .. controls (484.43,176.94) and (476.14,178.09) .. (477.42,178.72) .. controls (478.31,179.22) and (486.62,177.85) .. (486.57,177.35) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (496.62,171.6) .. controls (495.89,173.45) and (498.11,178.59) .. (499.24,177.2) .. controls (500.16,176.17) and (497.54,171.18) .. (496.62,171.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (504.98,173.41) .. controls (503.31,173.65) and (498.07,177.01) .. (499.24,177.2) .. controls (500.09,177.4) and (505.25,173.84) .. (504.98,173.41) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (504.98,173.41) .. controls (502.88,176.96) and (503.52,190.83) .. (506,188.71) .. controls (507.96,187.24) and (506.63,173.33) .. (504.98,173.41) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (506,188.71) .. controls (506.48,191.4) and (512.32,199.49) .. (512.58,197.55) .. controls (512.88,196.14) and (506.71,188.21) .. (506,188.71) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (497.35,186.65) .. controls (497.34,189.39) and (501.64,198.39) .. (502.25,196.53) .. controls (502.79,195.19) and (498.13,186.29) .. (497.35,186.65) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (512.58,197.55) .. controls (511.35,195.13) and (510.57,198.23) .. (509.64,200.12) .. controls (512.38,201.66) and (512.83,199.35) .. (512.58,197.55) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (502.25,196.53) .. controls (501.01,194.11) and (500.23,197.21) .. (499.31,199.1) .. controls (502.04,200.63) and (502.5,198.33) .. (502.25,196.53) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (476.6,188.81) .. controls (479.32,189.29) and (479.48,186.72) .. (480.27,184.77) .. controls (475.55,186.08) and (475.61,187.9) .. (476.6,188.81) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (473.76,182.75) .. controls (476.47,183.23) and (476.63,180.66) .. (477.42,178.72) .. controls (472.7,180.03) and (472.77,181.84) .. (473.76,182.75) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (507.76,163.76) .. controls (509.9,164.1) and (510.5,164.3) .. (511.42,167.4) .. controls (510.52,173.82) and (509.32,176.78) .. (504.23,181.96) .. controls (502.13,181.97) and (502.36,182.11) .. (499.9,179.91) .. controls (504.22,175.8) and (507.73,171.36) .. (507.76,163.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (514.51,167.27) .. controls (516.66,167.58) and (517.26,167.78) .. (518.1,171.09) .. controls (517.04,177.99) and (515.76,181.2) .. (510.52,186.88) .. controls (508.39,186.93) and (508.62,187.08) .. (506.2,184.77) .. controls (510.65,180.27) and (514.29,175.42) .. (514.51,167.27) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (520.2,173.43) .. controls (521.66,173.7) and (521.48,178.25) .. (522.1,180.68) .. controls (521.49,185.71) and (523.18,181.12) .. (519.72,185.18) .. controls (518.28,185.19) and (516.52,187.82) .. (514.85,186.09) .. controls (517.79,182.87) and (520.18,179.39) .. (520.2,173.43) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.59 ] (503.89,167.78) .. controls (504.8,165.81) and (505.15,165.29) .. (508.39,165.25) .. controls (514.32,167.86) and (516.85,169.82) .. (520.45,176.12) .. controls (519.89,178.15) and (520.09,177.97) .. (517.3,179.73) .. controls (514.52,174.46) and (511.2,169.88) .. (503.89,167.78) -- cycle ;
            	\draw  [fill={rgb, 255:red, 207; green, 237; blue, 230 }  ,fill opacity=1 ] (495.1,160.78) .. controls (505.54,148.05) and (516.03,135.88) .. (528.36,138.31) .. controls (534.09,139.5) and (527.58,150.49) .. (520.23,155.36) .. controls (519.97,166.31) and (496.1,166.62) .. (495.1,160.78) -- cycle ;
            	\draw    (495.1,160.78) .. controls (506.33,152.92) and (516.03,152.31) .. (520.23,155.36) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (495.1,160.78) -- (508.69,158.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (508.69,158.4) -- (520.23,155.36) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (506.64,159.56) -- (513.41,162.66) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (507.43,154.99) -- (513.67,156.58) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (495.1,160.78) -- (519.44,144.7) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (509.53,151.04) -- (517.08,152.92) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (514.77,147.69) -- (517.08,140.75) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (519.44,144.7) -- (529.94,142.57) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (514.77,147.69) -- (522.33,148.05) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (517.08,152.92) -- (522.33,148.05) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (522.33,148.05) -- (527.58,147.14) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (519.44,144.7) -- (524.95,138.62) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.25 ]   (509.53,151.04) -- (509.74,145.62) ;
            \end{tikzpicture}'''
                # 3. Câu hỏi
                noidungcauhoi = (r'''\immini{Trong một tổ ong, ong chúa muốn phân chia khu vực lưu trữ thức ăn ở một cụm gồm 7 ô lục giác liền kề nhau. Ong chúa yêu cầu phân loại cụm này thành các khu vực khác nhau để lưu trữ: %s. Để dễ phân biệt, mỗi loại thức ăn sẽ được quy định bằng một màu sắc riêng (ví dụ: vàng cho mật, đỏ cho phấn hoa...). Quy tắc an toàn là: "Không được đặt hai khu vực chứa cùng một loại thức ăn ngay cạnh nhau (chung cạnh)". Hỏi ban quản lý tổ ong có bao nhiêu phương án khác nhau để sắp xếp các khu vực lưu trữ thức ăn trong cụm 7 ô này?}{%s}'''
                                 % (food_str, hinhve))

                # 4. Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = '$%s$' % (das1)
                da_s2 = '$%s$' % (das2)
                da_s3 = '$%s$' % (das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # 5. Nội dung lời giải
                loigiai = ('''Mô hình hóa cụm 7 ô lục giác liền kề: Cụm này gồm 1 ô ở trung tâm và 6 ô xung quanh tạo thành một vòng khép kín. Hai ô được gọi là "kề nhau" nếu chúng có chung một cạnh. \\\\
                Số loại thức ăn cần phân bổ (tương ứng với số màu cần tô) là $m = %s$.\\\\
                \\textbf{Bước 1:} Chọn loại thức ăn cho ô trung tâm. Có $%s$ cách chọn. Ô trung tâm này kề với cả 6 ô xung quanh.\\\\
                \\textbf{Bước 2:} Phân bổ thức ăn cho 6 ô xung quanh. Do 6 ô này đều kề với ô trung tâm nên chúng chỉ được chọn các loại thức ăn khác với ô trung tâm (còn $%s - 1 = %s$ loại). Đồng thời 6 ô xung quanh tạo thành một vòng tuần hoàn (đồ thị chu trình $C_6$) và 2 ô kề nhau trên vòng không được trùng loại thức ăn.\\\\
                Bài toán trở thành bài toán tô màu đồ thị vòng $C_6$ với $k = %s$ màu.\\\\
                Số cách tô màu đồ thị vòng $C_n$ với $k$ màu được tính theo công thức đa thức sắc số:\\\\ $P_n = \\left(k-1\\right)^n + \\left(-1\\right)^n\\left(k-1\\right)$.\\\\
                Áp dụng với $n=6$ và $k=%s$: Số cách phân bổ cho 6 ô xung quanh là:\\\\
                $\\left(%s-1\\right)^6 + \\left(-1\\right)^6\\left(%s-1\\right) = %s^6 + %s = %s$ (cách).\\\\
                Vậy tổng số phương án sắp xếp là: $%s \\cdot %s = %s$ (phương án).'''
                           % (m, m, m, k, k, k, k, k, k_minus_1, k_minus_1, kq_vong, m, kq_vong, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

