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


def bt_dang76_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random độ dài trục lớn 2a và trục bé 2b
                a = random.randint(12, 18)
                L_a = 2 * a

                # Trục bé phải nhỏ hơn trục lớn
                L_b = random.randint(18, L_a - 1)
                b_val = L_b / 2.0

                # Random thông số giá bán
                v0 = 1000
                p0 = random.choice([15000, 20000, 25000, 30000])
                p0_k = int(p0 / 1000)

                # Xử lý chuỗi hiển thị dấu phẩy cho số thập phân
                b_str = str(b_val).replace('.0', '').replace('.', ',')

                # Tính toán chính xác phân số của thể tích
                vol_frac = frac(4 * a, 3) * frac(str(b_val))**2
                if vol_frac.denominator == 1:
                    vol_str = str(vol_frac.numerator)
                else:
                    vol_str = "\\frac{%s}{%s}" % (vol_frac.numerator, vol_frac.denominator)

                # Tính thể tích xấp xỉ
                v_approx = float(vol_frac) * math.pi
                v_approx_rounded = round(v_approx, 2)
                v_approx_str = str(v_approx_rounded).replace('.', ',')

                # Tính doanh thu theo giá trị xấp xỉ (như trong ảnh mẫu)
                revenue = round((v_approx_rounded / v0) * p0)
                rev_exact_str = "{:,}".format(revenue).replace(',', '.')

                # Làm tròn đến hàng nghìn
                revenue_rounded = round(revenue / 1000) * 1000
                kq_k = int(revenue_rounded / 1000)

                # Các đáp án trắc nghiệm
                du = ['$%s.000$' % (kq_k)]
                da = random.choice(du)

                # Tạo các phương án sai lệch nhau
                s = [
                     '$%s.000$' % (kq_k + 1),
                     '$%s.000$' % (kq_k - 1),
                     '$%s.000$' % (kq_k + 2),
                     '$%s.000$' % (kq_k - 2),
                     '$%s.000$' % (kq_k + 3),
                     '$%s.000$' % (kq_k - 3),
                     '$%s.000$' % (kq_k + 5),
                     '$%s.000$' % (kq_k - 5),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''\\immini{Khi bổ dọc một quả dưa hấu hình Elip tròn xoay qua trục lớn, ta thu được mặt cắt thiết diện qua tâm là một hình Elip có độ dài trục lớn là $%s$ cm và độ dài trục bé là $%s$ cm. Người ta ép toàn bộ quả dưa hấu này để làm nước sinh tố giải khát, biết rằng cứ mỗi $%s$ cm$^3$ thể tích dưa hấu sẽ làm được các cốc sinh tố trị giá tổng cộng $%s.000$ đồng. Hỏi quả dưa hấu trên có thể đem lại tối đa bao nhiêu tiền bán sinh tố? (làm tròn kết quả đến hàng nghìn, giả sử vỏ quả dưa mỏng không đáng kể).}
                                 {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.14 ] (175.6,133.45) .. controls (175.6,124.75) and (203.58,117.7) .. (238.1,117.7) .. controls (272.62,117.7) and (300.6,124.75) .. (300.6,133.45) .. controls (300.6,142.15) and (272.62,149.2) .. (238.1,149.2) .. controls (203.58,149.2) and (175.6,142.15) .. (175.6,133.45) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (167,97.96) .. controls (167,71.75) and (204.18,50.5) .. (250.05,50.5) .. controls (295.92,50.5) and (333.1,71.75) .. (333.1,97.96) .. controls (333.1,124.17) and (295.92,145.41) .. (250.05,145.41) .. controls (204.18,145.41) and (167,124.17) .. (167,97.96) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (168,94) .. controls (173.6,90.7) and (329.1,89.2) .. (332.6,94.7) .. controls (326.1,101.7) and (177.6,102.2) .. (168,94) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (168,94) .. controls (201.6,120.7) and (311.1,113.7) .. (332.6,94.7) .. controls (329.6,124.2) and (181.6,128.2) .. (168,94) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (168,94) .. controls (184.6,138.7) and (307.6,144.7) .. (332.6,94.7) .. controls (334.1,140.2) and (181.6,158.2) .. (168,94) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (168,95.35) .. controls (201.6,70.64) and (311.1,77.12) .. (332.6,94.7) .. controls (329.6,67.4) and (181.6,63.7) .. (168,95.35) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (168,94) .. controls (184.6,56.2) and (307.6,51.12) .. (332.6,93.41) .. controls (334.1,54.93) and (181.6,39.71) .. (168,94) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.14 ] (167,97.7) .. controls (167,76.44) and (189.97,59.2) .. (218.3,59.2) .. controls (246.63,59.2) and (269.6,76.44) .. (269.6,97.7) .. controls (269.6,118.96) and (246.63,136.2) .. (218.3,136.2) .. controls (189.97,136.2) and (167,118.96) .. (167,97.7) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.14 ] (167,98.45) .. controls (167,74.01) and (198.92,54.2) .. (238.3,54.2) .. controls (277.68,54.2) and (309.6,74.01) .. (309.6,98.45) .. controls (309.6,122.89) and (277.68,142.7) .. (238.3,142.7) .. controls (198.92,142.7) and (167,122.89) .. (167,98.45) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.14 ] (234.1,159.45) .. controls (234.1,150.75) and (262.08,143.7) .. (296.6,143.7) .. controls (331.12,143.7) and (359.1,150.75) .. (359.1,159.45) .. controls (359.1,168.15) and (331.12,175.2) .. (296.6,175.2) .. controls (262.08,175.2) and (234.1,168.15) .. (234.1,159.45) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (391.6,123.96) .. controls (391.6,150.17) and (354.42,171.41) .. (308.55,171.41) .. controls (262.68,171.41) and (225.5,150.17) .. (225.5,123.96) .. controls (225.5,123.37) and (225.52,122.78) .. (225.56,122.2) -- (391.54,122.2) .. controls (391.58,122.78) and (391.6,123.37) .. (391.6,123.96) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (226.5,120) .. controls (232.1,116.7) and (387.6,115.2) .. (391.1,120.7) .. controls (384.6,127.7) and (236.1,128.2) .. (226.5,120) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (226.5,120) .. controls (260.1,146.7) and (369.6,139.7) .. (391.1,120.7) .. controls (388.1,150.2) and (240.1,154.2) .. (226.5,120) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (226.5,120) .. controls (243.1,164.7) and (366.1,170.7) .. (391.1,120.7) .. controls (392.6,166.2) and (240.1,184.2) .. (226.5,120) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (226.5,121.35) .. controls (260.1,96.64) and (369.6,103.12) .. (391.1,120.7) .. controls (388.1,93.4) and (240.1,89.7) .. (226.5,121.35) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (225.6,122.2) .. controls (225.6,108.95) and (262.65,98.2) .. (308.35,98.2) .. controls (354.05,98.2) and (391.1,108.95) .. (391.1,122.2) .. controls (391.1,135.45) and (354.05,146.2) .. (308.35,146.2) .. controls (262.65,146.2) and (225.6,135.45) .. (225.6,122.2) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.17 ] (248.6,122.2) .. controls (248.6,114.19) and (275.35,107.7) .. (308.35,107.7) .. controls (341.35,107.7) and (368.1,114.19) .. (368.1,122.2) .. controls (368.1,130.21) and (341.35,136.7) .. (308.35,136.7) .. controls (275.35,136.7) and (248.6,130.21) .. (248.6,122.2) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (248.6,122.2) .. controls (248.6,121.78) and (250,121.43) .. (251.73,121.43) .. controls (253.46,121.43) and (254.87,121.78) .. (254.87,122.2) .. controls (254.87,122.62) and (253.46,122.97) .. (251.73,122.97) .. controls (250,122.97) and (248.6,122.62) .. (248.6,122.2) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (361.83,122.2) .. controls (361.83,121.78) and (363.24,121.43) .. (364.97,121.43) .. controls (366.7,121.43) and (368.1,121.78) .. (368.1,122.2) .. controls (368.1,122.62) and (366.7,122.97) .. (364.97,122.97) .. controls (363.24,122.97) and (361.83,122.62) .. (361.83,122.2) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (254.92,129.12) .. controls (254.82,128.7) and (256.11,128.05) .. (257.79,127.65) .. controls (259.48,127.26) and (260.92,127.27) .. (261.02,127.68) .. controls (261.11,128.1) and (259.83,128.75) .. (258.14,129.15) .. controls (256.46,129.54) and (255.01,129.53) .. (254.92,129.12) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (351.92,116.12) .. controls (351.82,115.7) and (353.11,115.05) .. (354.79,114.65) .. controls (356.48,114.26) and (357.92,114.27) .. (358.02,114.68) .. controls (358.11,115.1) and (356.83,115.75) .. (355.14,116.15) .. controls (353.46,116.54) and (352.01,116.53) .. (351.92,116.12) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (266.02,132.81) .. controls (265.88,132.41) and (267.08,131.61) .. (268.7,131.01) .. controls (270.33,130.42) and (271.76,130.26) .. (271.91,130.65) .. controls (272.05,131.05) and (270.86,131.86) .. (269.23,132.45) .. controls (267.61,133.05) and (266.17,133.21) .. (266.02,132.81) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (342.02,112.81) .. controls (341.88,112.41) and (343.08,111.61) .. (344.7,111.01) .. controls (346.33,110.42) and (347.76,110.26) .. (347.91,110.65) .. controls (348.05,111.05) and (346.86,111.86) .. (345.23,112.45) .. controls (343.61,113.05) and (342.17,113.21) .. (342.02,112.81) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (277.56,135.41) .. controls (277.29,135.08) and (278.15,133.92) .. (279.48,132.81) .. controls (280.8,131.7) and (282.1,131.07) .. (282.37,131.39) .. controls (282.64,131.72) and (281.79,132.88) .. (280.46,133.99) .. controls (279.13,135.1) and (277.83,135.73) .. (277.56,135.41) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (330.23,111.07) .. controls (329.96,110.75) and (330.81,109.59) .. (332.14,108.48) .. controls (333.47,107.37) and (334.77,106.73) .. (335.04,107.06) .. controls (335.31,107.38) and (334.45,108.55) .. (333.12,109.66) .. controls (331.8,110.76) and (330.5,111.4) .. (330.23,111.07) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (288.7,137.76) .. controls (288.33,137.54) and (288.76,136.16) .. (289.64,134.67) .. controls (290.53,133.19) and (291.54,132.16) .. (291.9,132.37) .. controls (292.27,132.59) and (291.84,133.97) .. (290.96,135.46) .. controls (290.07,136.95) and (289.06,137.98) .. (288.7,137.76) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (318.7,110.09) .. controls (318.33,109.87) and (318.76,108.49) .. (319.64,107.01) .. controls (320.53,105.52) and (321.54,104.49) .. (321.9,104.71) .. controls (322.27,104.93) and (321.84,106.31) .. (320.96,107.79) .. controls (320.07,109.28) and (319.06,110.31) .. (318.7,110.09) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (301,138.2) .. controls (300.57,138.2) and (300.22,136.8) .. (300.2,135.07) .. controls (300.18,133.34) and (300.51,131.94) .. (300.94,131.93) .. controls (301.36,131.93) and (301.72,133.33) .. (301.73,135.06) .. controls (301.75,136.79) and (301.42,138.2) .. (301,138.2) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (307.61,110.84) .. controls (307.19,110.84) and (306.83,109.44) .. (306.82,107.71) .. controls (306.8,105.98) and (307.13,104.58) .. (307.55,104.57) .. controls (307.98,104.57) and (308.33,105.97) .. (308.35,107.7) .. controls (308.37,109.43) and (308.04,110.84) .. (307.61,110.84) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (314.11,138.09) .. controls (313.7,138.2) and (313.01,136.94) .. (312.56,135.26) .. controls (312.11,133.59) and (312.08,132.15) .. (312.49,132.04) .. controls (312.9,131.93) and (313.59,133.2) .. (314.04,134.87) .. controls (314.49,136.54) and (314.52,137.99) .. (314.11,138.09) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (298.11,111.76) .. controls (297.7,111.87) and (297.01,110.6) .. (296.56,108.93) .. controls (296.11,107.26) and (296.08,105.81) .. (296.49,105.71) .. controls (296.9,105.6) and (297.59,106.86) .. (298.04,108.54) .. controls (298.49,110.21) and (298.52,111.65) .. (298.11,111.76) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (329.24,135.23) .. controls (328.94,135.53) and (327.69,134.82) .. (326.44,133.62) .. controls (325.18,132.43) and (324.41,131.21) .. (324.7,130.91) .. controls (324.99,130.6) and (326.24,131.32) .. (327.5,132.51) .. controls (328.75,133.71) and (329.53,134.92) .. (329.24,135.23) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (287.9,110.89) .. controls (287.61,111.2) and (286.36,110.48) .. (285.1,109.29) .. controls (283.85,108.09) and (283.07,106.88) .. (283.36,106.57) .. controls (283.66,106.27) and (284.91,106.98) .. (286.16,108.18) .. controls (287.42,109.37) and (288.19,110.59) .. (287.9,110.89) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (343.38,132.91) .. controls (343.18,133.28) and (341.78,132.9) .. (340.26,132.07) .. controls (338.75,131.24) and (337.68,130.27) .. (337.89,129.89) .. controls (338.09,129.52) and (339.48,129.9) .. (341,130.73) .. controls (342.52,131.56) and (343.58,132.53) .. (343.38,132.91) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (277.05,111.57) .. controls (276.84,111.94) and (275.45,111.57) .. (273.93,110.74) .. controls (272.41,109.91) and (271.35,108.93) .. (271.55,108.56) .. controls (271.76,108.19) and (273.15,108.56) .. (274.67,109.39) .. controls (276.19,110.23) and (277.25,111.2) .. (277.05,111.57) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (358.16,130.02) .. controls (357.98,130.41) and (356.56,130.14) .. (354.98,129.43) .. controls (353.41,128.72) and (352.27,127.83) .. (352.44,127.44) .. controls (352.62,127.06) and (354.04,127.32) .. (355.62,128.03) .. controls (357.19,128.75) and (358.33,129.64) .. (358.16,130.02) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (264.49,115.69) .. controls (264.31,116.08) and (262.89,115.81) .. (261.32,115.1) .. controls (259.74,114.39) and (258.6,113.5) .. (258.78,113.11) .. controls (258.95,112.72) and (260.37,112.99) .. (261.95,113.7) .. controls (263.53,114.41) and (264.66,115.3) .. (264.49,115.69) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.08 ] (272.5,122.35) .. controls (272.5,119.45) and (287.27,117.1) .. (305.5,117.1) .. controls (323.73,117.1) and (338.5,119.45) .. (338.5,122.35) .. controls (338.5,125.25) and (323.73,127.6) .. (305.5,127.6) .. controls (287.27,127.6) and (272.5,125.25) .. (272.5,122.35) -- cycle ;
                                 	\\draw  [color={rgb, 255:red, 61; green, 117; blue, 5 }  ,draw opacity=0.52 ][line width=2.25]  (226.5,122.1) .. controls (226.5,110.23) and (262.76,100.6) .. (307.5,100.6) .. controls (352.24,100.6) and (388.5,110.23) .. (388.5,122.1) .. controls (388.5,133.97) and (352.24,143.6) .. (307.5,143.6) .. controls (262.76,143.6) and (226.5,133.97) .. (226.5,122.1) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (115.02,159.49) .. controls (115.02,156.5) and (123.8,154.07) .. (134.64,154.07) .. controls (145.48,154.07) and (154.26,156.5) .. (154.26,159.49) .. controls (154.26,162.48) and (145.48,164.91) .. (134.64,164.91) .. controls (123.8,164.91) and (115.02,162.48) .. (115.02,159.49) -- cycle ;
                                 	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.71 ] (117.29,99.02) .. controls (117.29,94.55) and (127.52,90.92) .. (140.15,90.92) .. controls (152.77,90.92) and (163,94.55) .. (163,99.02) .. controls (163,103.49) and (152.77,107.11) .. (140.15,107.11) .. controls (127.52,107.11) and (117.29,103.49) .. (117.29,99.02) -- cycle ;
                                 	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.71 ]   (117.29,99.02) -- (125.78,158.01) ;
                                 	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.71 ]   (163,99.02) -- (154.51,158.01) ;
                                 	\\draw  [draw opacity=0] (154.29,157.84) .. controls (154.44,158.11) and (154.51,158.39) .. (154.51,158.67) .. controls (154.51,161.28) and (148.08,163.4) .. (140.15,163.4) .. controls (132.21,163.4) and (125.78,161.28) .. (125.78,158.67) .. controls (125.78,158.5) and (125.81,158.33) .. (125.86,158.17) -- (140.15,158.67) -- cycle ; \\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.71 ] (154.29,157.84) .. controls (154.44,158.11) and (154.51,158.39) .. (154.51,158.67) .. controls (154.51,161.28) and (148.08,163.4) .. (140.15,163.4) .. controls (132.21,163.4) and (125.78,161.28) .. (125.78,158.67) .. controls (125.78,158.5) and (125.81,158.33) .. (125.86,158.17) ;  
                                 	\\draw  [draw opacity=0] (154.26,159.49) .. controls (154.43,159.22) and (154.51,158.95) .. (154.51,158.67) .. controls (154.51,156.23) and (148.08,154.26) .. (140.15,154.26) .. controls (132.21,154.26) and (125.78,156.23) .. (125.78,158.67) .. controls (125.78,158.84) and (125.81,159) .. (125.87,159.17) -- (140.15,158.67) -- cycle ; \\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.71 ] (154.26,159.49) .. controls (154.43,159.22) and (154.51,158.95) .. (154.51,158.67) .. controls (154.51,156.23) and (148.08,154.26) .. (140.15,154.26) .. controls (132.21,154.26) and (125.78,156.23) .. (125.78,158.67) .. controls (125.78,158.84) and (125.81,159) .. (125.87,159.17) ;  
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (159.45,114.73) -- (153.14,159.13) -- (127.24,158.92) -- (120.93,114.73) -- cycle ;
                                 	\\draw  [color={rgb, 255:red, 214; green, 54; blue, 73 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (128.07,158.18) .. controls (128.07,156.37) and (133.55,154.91) .. (140.31,154.91) .. controls (147.07,154.91) and (152.55,156.37) .. (152.55,158.18) .. controls (152.55,159.98) and (147.07,161.44) .. (140.31,161.44) .. controls (133.55,161.44) and (128.07,159.98) .. (128.07,158.18) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (120.93,114.75) .. controls (120.93,111.64) and (129.55,109.12) .. (140.19,109.12) .. controls (150.83,109.12) and (159.45,111.64) .. (159.45,114.75) .. controls (159.45,117.86) and (150.83,120.39) .. (140.19,120.39) .. controls (129.55,120.39) and (120.93,117.86) .. (120.93,114.75) -- cycle ;
                                 	\\draw  [draw opacity=0] (159.22,114.99) .. controls (159.23,115.05) and (159.23,115.12) .. (159.23,115.18) .. controls (159.23,118.19) and (150.63,120.64) .. (140.02,120.64) .. controls (129.42,120.64) and (120.81,118.19) .. (120.81,115.18) .. controls (120.81,114.96) and (120.86,114.73) .. (120.96,114.52) -- (140.02,115.18) -- cycle ; \\draw  [color={rgb, 255:red, 236; green, 203; blue, 203 }  ,draw opacity=0.71 ] (159.22,114.99) .. controls (159.23,115.05) and (159.23,115.12) .. (159.23,115.18) .. controls (159.23,118.19) and (150.63,120.64) .. (140.02,120.64) .. controls (129.42,120.64) and (120.81,118.19) .. (120.81,115.18) .. controls (120.81,114.96) and (120.86,114.73) .. (120.96,114.52) ;  
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.29 ] (129.85,106.68) -- (133.55,162.62) -- (131.16,161.09) -- (124.19,105.16) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.29 ] (153.36,106.46) -- (148.57,160.88) -- (147.05,160.44) -- (150.09,107.33) -- cycle ;
                                 	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.54 ] (118.88,99.02) .. controls (118.88,95.32) and (128.4,92.31) .. (140.15,92.31) .. controls (151.89,92.31) and (161.41,95.32) .. (161.41,99.02) .. controls (161.41,102.72) and (151.89,105.72) .. (140.15,105.72) .. controls (128.4,105.72) and (118.88,102.72) .. (118.88,99.02) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.06 ] (143.13,107.33) -- (140.52,163.27) -- (138.12,163.05) -- (134.86,107.11) -- cycle ;
                                 	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (123.71,105.59) -- (131.16,161.09) ;
                                 	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (124.98,73.57) -- (132.28,104.02) .. controls (132.31,104.16) and (131.96,104.36) .. (131.49,104.47) .. controls (131.02,104.59) and (130.61,104.56) .. (130.58,104.42) -- (123.27,73.98) .. controls (123.24,73.84) and (123.59,73.63) .. (124.06,73.52) .. controls (124.53,73.41) and (124.94,73.43) .. (124.98,73.57) .. controls (125.01,73.71) and (124.66,73.92) .. (124.19,74.03) .. controls (123.72,74.14) and (123.31,74.12) .. (123.27,73.98) ;
                                 	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.36 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.55 ] (132.52,104.52) -- (136.32,120.34) .. controls (136.35,120.49) and (135.97,120.71) .. (135.47,120.83) .. controls (134.97,120.95) and (134.54,120.92) .. (134.5,120.77) -- (130.7,104.95) .. controls (130.67,104.8) and (131.05,104.58) .. (131.55,104.46) .. controls (132.05,104.34) and (132.48,104.36) .. (132.52,104.52) .. controls (132.56,104.67) and (132.18,104.88) .. (131.68,105.01) .. controls (131.18,105.13) and (130.74,105.1) .. (130.7,104.95) ;
                                 	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.36 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.26 ] (136.72,120.81) -- (146.41,157.15) .. controls (146.46,157.32) and (146.05,157.57) .. (145.51,157.71) .. controls (144.96,157.86) and (144.49,157.84) .. (144.44,157.68) -- (134.75,121.34) .. controls (134.71,121.17) and (135.12,120.92) .. (135.66,120.78) .. controls (136.2,120.63) and (136.68,120.65) .. (136.72,120.81) .. controls (136.77,120.97) and (136.36,121.22) .. (135.82,121.37) .. controls (135.27,121.51) and (134.8,121.5) .. (134.75,121.34) ;
                                 \\end{tikzpicture}}'''
                                 % (L_a, L_b, v0, p0_k))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                		\\draw  [line width=1]  (58.5,208.55) .. controls (58.5,184.22) and (97.7,164.5) .. (146.05,164.5) .. controls (194.4,164.5) and (233.6,184.22) .. (233.6,208.55) .. controls (233.6,232.88) and (194.4,252.6) .. (146.05,252.6) .. controls (97.7,252.6) and (58.5,232.88) .. (58.5,208.55) -- cycle ;
                		\\draw [line width=1]    (25.6,208.55) -- (266.6,208.55) ;
                		\\draw [shift={(270.6,208.55)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                		\\draw [line width=1]    (146.05,270) -- (146.05,142) ;
                		\\draw [shift={(146.05,138)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                		\\draw (127,211) node [anchor=north west][inner sep=0.75pt]    {$O$};
                		\\draw (254.5,211) node [anchor=north west][inner sep=0.75pt]    {$x$};
                		\\draw (129,139) node [anchor=north west][inner sep=0.75pt]    {$y$};
                	\\end{tikzpicture}
                \\end{center} Chọn hệ trục tọa độ $Oxy$ có gốc $O$ trùng tâm Elip đối xứng của dưa hấu. Trục lớn trùng với $Ox$. \\\\
                             Elip thiết diện có phương trình: 
                             $$\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1.$$
                             Với $a = %s$ cm, $b = %s$ cm. \\\\
                             Nửa nhánh trên Elip: $y^2 = b^2\\left(1 - \\frac{x^2}{a^2}\\right)$. \\\\
                             Khi xoay elip này quanh trục $Ox$ ta được thể tích quả dưa hấu:
                             $$V = \\pi \\int_{-%s}^{%s} y^2 \\mathrm{\\,d}x = \\pi \\int_{-%s}^{%s} %s^2 \\left(1 - \\frac{x^2}{%s^2}\\right) \\mathrm{\\,d}x = \\frac{4}{3}\\pi a b^2 = \\frac{4}{3}\\pi \\cdot %s \\cdot (%s)^2 = %s \\pi \\approx %s \\text{ (cm}^3\\text{)}.$$ \\\\
                             Tổng số tiền thu hoạch bán sinh tố:
                             $$T = \\frac{%s}{%s} \\times %s.000 \\approx %s \\text{ đồng} \\approx %s.000 \\text{ đồng}.$$'''
                             % (a, b_str,
                                a, a, a, a, b_str, a,
                                a, b_str, vol_str, v_approx_str,
                                v_approx_str, v0, p0_k, rev_exact_str, kq_k))
            dapan='\\shortans[0]{$%s$}\n'%(kq_k)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

