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


def bt_dang64_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Danh sách các bộ cấu hình ngẫu nhiên (D, v1_str, t_nghi, v2_str, D_km_str, R_km_str, k1_str, k2_str, t4_str, C_str, f0_str, f_pi6_expr, f_pi6_val, f_pi2_val)
                configs = [
                    (200, '3', 5, '6', '0,2', '0,1', '4', '2', '2', '7', '11', '2\\sqrt{3} + \\frac{\\pi}{3} + 7', '11,5', '10,1'),
                    (300, '4,5', 10, '9', '0,3', '0,15', '4', '2', '2', '12', '16', '2\\sqrt{3} + \\frac{\\pi}{3} + 12', '16,5', '15,1'),
                    (400, '6', 8, '12', '0,4', '0,2', '4', '2', '2', '10', '14', '2\\sqrt{3} + \\frac{\\pi}{3} + 10', '14,5', '13,1'),
                    (150, '3', 5, '6', '0,15', '0,075', '3', '1,5', '1,5', '6,5', '9,5', '1,5\\sqrt{3} + \\frac{\\pi}{4} + 6,5', '9,9', '8,9'),
                    (250, '2,5', 10, '5', '0,25', '0,125', '6', '3', '3', '13', '19', '3\\sqrt{3} + \\frac{\\pi}{2} + 13', '19,8', '17,7')
                ]

                (D, v1_str, t_nghi, v2_str, D_km_str, R_km_str, k1_str, k2_str, t4_str, C_str, f0_str, f_pi6_expr, f_pi6_val, f_pi2_val) = random.choice(configs)

                t_nghi_str = str(t_nghi)

                # Tạo đáp án đúng
                du = ['$%s$' % (f_pi6_val)]
                da = random.choice(du)

                # Tạo các phương án sai ngẫu nhiên không trùng với đáp án đúng
                val = float(f_pi6_val.replace(',', '.'))
                s_vals = [val + 0.5, val - 0.5, val + 1.0, val - 1.0, val + 1.5, val - 1.5, val + 2.0, val - 2.0]
                s_strs = [str(Decimal(str(v)).quantize(Decimal('0.1'))).replace('.', ',') for v in s_vals]
                s_strs = [x for x in s_strs if x != f_pi6_val]

                das1_val = random.choice(s_strs)
                s_strs.remove(das1_val)
                das2_val = random.choice(s_strs)
                s_strs.remove(das2_val)
                das3_val = random.choice(s_strs)

                da_d = ('\\True ' + str(da))
                da_s1 = '$%s$' % (das1_val)
                da_s2 = '$%s$' % (das2_val)
                da_s3 = '$%s$' % (das3_val)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung câu hỏi có hình vẽ TikZ
                noidungcauhoi = ('''Một hồ nước hình bán nguyệt có đường kính $AB = %s$ m. Một người chèo thuyền theo một đường thẳng với vận tốc $%s\\text{ km/h}$ từ vị trí $A$ đến vị trí $C$ bất kỳ trên cung $AB$. Tại vị trí $C$, người đó nghỉ $%s$ phút rồi tiếp tục chạy bộ dọc theo cung nhỏ $CB$ đến $B$, sau đó chạy theo đường thẳng $BA$ để quay về $A$ với vận tốc $%s\\text{ km/h}$ (tham khảo hình vẽ). Hỏi người đó mất nhiều nhất bao nhiêu phút để về đến vị trí $A$ (kết quả quy tròn đến hàng phần chục)?\\\\
            \\begin{center}   
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (50.5,32) -- (331.1,32) -- (331.1,203.6) -- (50.5,203.6) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 154; green, 197; blue, 247 }  ,fill opacity=1 ] (189.8,59.5) .. controls (268.6,59.4) and (299.1,135.4) .. (295,164.7) .. controls (248.6,165.4) and (126.1,164.9) .. (84.6,164.7) .. controls (82.6,124.4) and (116.1,61.9) .. (189.8,59.5) -- cycle ;
            		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=3]    (84.6,164.7) .. controls (92.1,22.4) and (293.6,28.9) .. (295,164.7) ;
            		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (83.6,164.7) -- (297.1,164.7) -- (297.1,179.4) -- (83.6,179.4) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (167.1,164.7) -- (213.6,164.7) -- (213.6,179.4) -- (167.1,179.4) -- cycle ;
            		\\draw    (167.1,172.05) -- (213.6,172.05) ;
            		\\draw    (167.1,168.55) -- (213.6,168.55) ;
            		\\draw    (167.1,176.05) -- (213.6,176.05) ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 120; green, 174; blue, 235 }  ,fill opacity=1 ] (189.81,70.9) .. controls (262.44,70.81) and (290.55,137.78) .. (286.77,163.6) .. controls (244,164.22) and (131.1,163.78) .. (92.85,163.6) .. controls (91.01,128.09) and (121.89,73.01) .. (189.81,70.9) -- cycle ;
            		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.25 ][line width=0.75]    (96.5,164.7) .. controls (103.15,43.64) and (281.86,49.17) .. (283.1,164.7) ;
            		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75]    (83,164.7) .. controls (90.61,21.17) and (295.18,27.73) .. (296.6,164.7) ;
            		\\draw  [fill={rgb, 255:red, 109; green, 171; blue, 38 }  ,fill opacity=1 ] (64.15,55.96) .. controls (63.87,53.13) and (64.78,50.32) .. (66.5,48.74) .. controls (68.22,47.16) and (70.45,47.07) .. (72.23,48.51) .. controls (72.86,46.86) and (74.02,45.73) .. (75.35,45.45) .. controls (76.68,45.16) and (78.03,45.77) .. (78.99,47.07) .. controls (79.53,45.58) and (80.59,44.58) .. (81.79,44.42) .. controls (82.99,44.26) and (84.16,44.98) .. (84.89,46.3) .. controls (85.86,44.72) and (87.41,44.05) .. (88.86,44.59) .. controls (90.32,45.13) and (91.41,46.77) .. (91.68,48.81) .. controls (92.87,49.26) and (93.86,50.41) .. (94.4,51.94) .. controls (94.94,53.48) and (94.96,55.27) .. (94.48,56.84) .. controls (95.65,58.95) and (95.93,61.76) .. (95.2,64.23) .. controls (94.47,66.69) and (92.85,68.44) .. (90.95,68.82) .. controls (90.93,71.13) and (90.02,73.25) .. (88.55,74.36) .. controls (87.08,75.48) and (85.29,75.41) .. (83.87,74.18) .. controls (83.27,76.95) and (81.56,78.99) .. (79.5,79.42) .. controls (77.43,79.84) and (75.37,78.58) .. (74.21,76.17) .. controls (72.79,77.36) and (71.08,77.7) .. (69.47,77.12) .. controls (67.87,76.54) and (66.5,75.09) .. (65.67,73.09) .. controls (64.22,73.33) and (62.81,72.29) .. (62.15,70.49) .. controls (61.49,68.69) and (61.72,66.51) .. (62.72,65.04) .. controls (61.42,63.98) and (60.76,61.89) .. (61.08,59.85) .. controls (61.4,57.81) and (62.62,56.28) .. (64.12,56.07) ; \\draw   (62.72,65.03) .. controls (63.33,65.53) and (64.04,65.76) .. (64.75,65.68)(65.67,73.09) .. controls (65.98,73.04) and (66.27,72.94) .. (66.56,72.78)(74.21,76.17) .. controls (74,75.73) and (73.82,75.26) .. (73.68,74.76)(83.87,74.18) .. controls (83.98,73.68) and (84.05,73.16) .. (84.08,72.63)(90.95,68.82) .. controls (90.96,66.35) and (89.95,64.1) .. (88.35,63.02)(94.48,56.84) .. controls (94.22,57.68) and (93.82,58.42) .. (93.32,59.01)(91.68,48.81) .. controls (91.72,49.15) and (91.74,49.5) .. (91.74,49.84)(84.89,46.3) .. controls (84.65,46.7) and (84.45,47.14) .. (84.3,47.61)(78.99,47.07) .. controls (78.86,47.43) and (78.77,47.81) .. (78.7,48.2)(72.23,48.51) .. controls (72.61,48.82) and (72.96,49.18) .. (73.27,49.61)(64.15,55.96) .. controls (64.19,56.35) and (64.25,56.73) .. (64.33,57.11) ;
            		\\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (68.2,57.94) .. controls (67.99,55.83) and (68.67,53.75) .. (69.95,52.57) .. controls (71.23,51.39) and (72.89,51.32) .. (74.21,52.4) .. controls (74.69,51.17) and (75.55,50.33) .. (76.54,50.12) .. controls (77.53,49.91) and (78.53,50.35) .. (79.25,51.33) .. controls (79.65,50.22) and (80.43,49.47) .. (81.33,49.35) .. controls (82.22,49.24) and (83.09,49.77) .. (83.64,50.75) .. controls (84.36,49.58) and (85.51,49.08) .. (86.59,49.48) .. controls (87.67,49.88) and (88.49,51.1) .. (88.69,52.62) .. controls (89.58,52.96) and (90.31,53.81) .. (90.71,54.95) .. controls (91.11,56.1) and (91.13,57.43) .. (90.77,58.6) .. controls (91.65,60.17) and (91.85,62.26) .. (91.31,64.09) .. controls (90.77,65.93) and (89.56,67.23) .. (88.14,67.51) .. controls (88.13,69.23) and (87.45,70.81) .. (86.36,71.64) .. controls (85.27,72.47) and (83.93,72.42) .. (82.88,71.5) .. controls (82.43,73.57) and (81.16,75.08) .. (79.62,75.4) .. controls (78.08,75.72) and (76.55,74.78) .. (75.69,72.99) .. controls (74.63,73.87) and (73.36,74.12) .. (72.16,73.69) .. controls (70.97,73.26) and (69.95,72.18) .. (69.33,70.69) .. controls (68.25,70.87) and (67.21,70.09) .. (66.71,68.75) .. controls (66.22,67.41) and (66.39,65.79) .. (67.14,64.7) .. controls (66.17,63.91) and (65.68,62.35) .. (65.91,60.83) .. controls (66.15,59.31) and (67.06,58.18) .. (68.18,58.02) ; \\draw   (67.14,64.69) .. controls (67.59,65.07) and (68.12,65.23) .. (68.64,65.18)(69.33,70.69) .. controls (69.56,70.66) and (69.78,70.58) .. (69.99,70.46)(75.69,72.99) .. controls (75.53,72.66) and (75.4,72.3) .. (75.29,71.93)(82.88,71.5) .. controls (82.96,71.13) and (83.01,70.74) .. (83.04,70.35)(88.14,67.51) .. controls (88.15,65.68) and (87.4,64) .. (86.21,63.2)(90.77,58.6) .. controls (90.58,59.22) and (90.28,59.77) .. (89.91,60.21)(88.69,52.62) .. controls (88.72,52.87) and (88.74,53.13) .. (88.73,53.39)(83.64,50.75) .. controls (83.46,51.05) and (83.31,51.37) .. (83.2,51.73)(79.25,51.33) .. controls (79.15,51.59) and (79.08,51.88) .. (79.03,52.17)(74.21,52.4) .. controls (74.5,52.62) and (74.76,52.9) .. (74.99,53.21)(68.2,57.94) .. controls (68.23,58.23) and (68.27,58.52) .. (68.33,58.8) ;
            		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (72.27,59.84) .. controls (72.15,58.64) and (72.54,57.44) .. (73.27,56.77) .. controls (74,56.09) and (74.95,56.05) .. (75.71,56.67) .. controls (75.98,55.97) and (76.47,55.48) .. (77.04,55.36) .. controls (77.61,55.24) and (78.19,55.5) .. (78.59,56.05) .. controls (78.82,55.42) and (79.27,54.99) .. (79.79,54.92) .. controls (80.3,54.86) and (80.8,55.16) .. (81.11,55.73) .. controls (81.53,55.05) and (82.19,54.77) .. (82.8,55) .. controls (83.42,55.23) and (83.89,55.93) .. (84.01,56.8) .. controls (84.51,56.99) and (84.94,57.48) .. (85.17,58.13) .. controls (85.39,58.79) and (85.41,59.55) .. (85.2,60.22) .. controls (85.7,61.12) and (85.82,62.32) .. (85.51,63.37) .. controls (85.2,64.42) and (84.51,65.17) .. (83.69,65.33) .. controls (83.69,66.31) and (83.3,67.22) .. (82.67,67.69) .. controls (82.04,68.17) and (81.28,68.14) .. (80.68,67.62) .. controls (80.42,68.8) and (79.69,69.67) .. (78.81,69.85) .. controls (77.93,70.03) and (77.05,69.49) .. (76.56,68.46) .. controls (75.95,68.97) and (75.22,69.12) .. (74.54,68.87) .. controls (73.85,68.62) and (73.27,68) .. (72.92,67.15) .. controls (72.3,67.25) and (71.7,66.81) .. (71.41,66.04) .. controls (71.13,65.27) and (71.23,64.34) .. (71.66,63.71) .. controls (71.1,63.26) and (70.82,62.37) .. (70.96,61.5) .. controls (71.09,60.63) and (71.62,59.98) .. (72.25,59.89) ; \\draw   (71.66,63.71) .. controls (71.92,63.93) and (72.22,64.02) .. (72.52,63.99)(72.92,67.15) .. controls (73.04,67.13) and (73.17,67.09) .. (73.29,67.02)(76.56,68.46) .. controls (76.47,68.28) and (76.39,68.07) .. (76.33,67.86)(80.68,67.62) .. controls (80.72,67.4) and (80.75,67.18) .. (80.77,66.95)(83.69,65.33) .. controls (83.7,64.28) and (83.27,63.32) .. (82.58,62.86)(85.2,60.22) .. controls (85.09,60.58) and (84.92,60.9) .. (84.71,61.15)(84.01,56.8) .. controls (84.02,56.94) and (84.03,57.09) .. (84.03,57.24)(81.11,55.73) .. controls (81.01,55.89) and (80.92,56.08) .. (80.86,56.28)(78.59,56.05) .. controls (78.54,56.21) and (78.5,56.37) .. (78.47,56.54)(75.71,56.67) .. controls (75.87,56.8) and (76.02,56.96) .. (76.16,57.13)(72.27,59.84) .. controls (72.28,60.01) and (72.31,60.17) .. (72.34,60.33) ;
            		\\draw  [fill={rgb, 255:red, 109; green, 171; blue, 38 }  ,fill opacity=1 ] (89.25,62.16) .. controls (89.05,60.14) and (89.71,58.14) .. (90.94,57) .. controls (92.17,55.87) and (93.76,55.81) .. (95.03,56.84) .. controls (95.48,55.66) and (96.31,54.85) .. (97.26,54.65) .. controls (98.21,54.45) and (99.18,54.88) .. (99.87,55.81) .. controls (100.25,54.74) and (101.01,54.03) .. (101.86,53.92) .. controls (102.72,53.8) and (103.56,54.31) .. (104.08,55.26) .. controls (104.78,54.13) and (105.89,53.65) .. (106.93,54.04) .. controls (107.96,54.42) and (108.75,55.6) .. (108.94,57.06) .. controls (109.79,57.38) and (110.5,58.19) .. (110.88,59.3) .. controls (111.27,60.4) and (111.29,61.67) .. (110.94,62.8) .. controls (111.78,64.31) and (111.98,66.32) .. (111.46,68.08) .. controls (110.94,69.84) and (109.78,71.09) .. (108.42,71.36) .. controls (108.41,73.01) and (107.75,74.53) .. (106.7,75.33) .. controls (105.65,76.12) and (104.37,76.07) .. (103.35,75.2) .. controls (102.92,77.18) and (101.7,78.64) .. (100.23,78.94) .. controls (98.75,79.25) and (97.28,78.34) .. (96.45,76.62) .. controls (95.43,77.47) and (94.21,77.71) .. (93.06,77.3) .. controls (91.91,76.89) and (90.93,75.85) .. (90.34,74.42) .. controls (89.3,74.59) and (88.3,73.84) .. (87.82,72.55) .. controls (87.35,71.27) and (87.51,69.71) .. (88.23,68.66) .. controls (87.3,67.9) and (86.83,66.4) .. (87.06,64.95) .. controls (87.28,63.49) and (88.16,62.4) .. (89.23,62.24) ; \\draw   (88.23,68.66) .. controls (88.67,69.01) and (89.17,69.17) .. (89.68,69.12)(90.34,74.42) .. controls (90.56,74.38) and (90.77,74.31) .. (90.98,74.2)(96.45,76.62) .. controls (96.29,76.31) and (96.17,75.97) .. (96.07,75.61)(103.35,75.2) .. controls (103.43,74.84) and (103.48,74.47) .. (103.51,74.09)(108.42,71.36) .. controls (108.43,69.6) and (107.7,67.99) .. (106.56,67.22)(110.94,62.8) .. controls (110.75,63.4) and (110.47,63.93) .. (110.11,64.35)(108.94,57.06) .. controls (108.97,57.3) and (108.98,57.54) .. (108.98,57.79)(104.08,55.26) .. controls (103.91,55.54) and (103.77,55.86) .. (103.66,56.2)(99.87,55.81) .. controls (99.77,56.07) and (99.7,56.34) .. (99.66,56.62)(95.03,56.84) .. controls (95.3,57.06) and (95.55,57.32) .. (95.77,57.62)(89.25,62.16) .. controls (89.28,62.44) and (89.32,62.72) .. (89.38,62.99) ;
            		\\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (92.15,63.58) .. controls (92,62.07) and (92.49,60.58) .. (93.4,59.74) .. controls (94.32,58.9) and (95.5,58.85) .. (96.45,59.62) .. controls (96.79,58.74) and (97.4,58.14) .. (98.11,57.99) .. controls (98.82,57.84) and (99.54,58.16) .. (100.05,58.85) .. controls (100.33,58.06) and (100.9,57.53) .. (101.54,57.44) .. controls (102.17,57.36) and (102.8,57.74) .. (103.19,58.44) .. controls (103.71,57.6) and (104.53,57.25) .. (105.3,57.53) .. controls (106.07,57.82) and (106.66,58.69) .. (106.8,59.78) .. controls (107.43,60.02) and (107.96,60.63) .. (108.25,61.45) .. controls (108.53,62.27) and (108.55,63.22) .. (108.29,64.05) .. controls (108.91,65.18) and (109.06,66.67) .. (108.67,67.98) .. controls (108.29,69.29) and (107.43,70.22) .. (106.41,70.43) .. controls (106.4,71.66) and (105.92,72.79) .. (105.13,73.38) .. controls (104.35,73.97) and (103.4,73.93) .. (102.64,73.28) .. controls (102.32,74.76) and (101.42,75.84) .. (100.32,76.07) .. controls (99.22,76.29) and (98.12,75.62) .. (97.5,74.34) .. controls (96.75,74.97) and (95.84,75.15) .. (94.98,74.85) .. controls (94.13,74.54) and (93.4,73.76) .. (92.96,72.7) .. controls (92.19,72.83) and (91.44,72.27) .. (91.09,71.31) .. controls (90.73,70.36) and (90.86,69.2) .. (91.39,68.41) .. controls (90.7,67.85) and (90.35,66.74) .. (90.51,65.65) .. controls (90.68,64.57) and (91.34,63.75) .. (92.13,63.64) ; \\draw   (91.39,68.41) .. controls (91.71,68.68) and (92.09,68.8) .. (92.47,68.76)(92.96,72.7) .. controls (93.12,72.68) and (93.28,72.62) .. (93.43,72.54)(97.5,74.34) .. controls (97.39,74.11) and (97.29,73.85) .. (97.22,73.59)(102.64,73.28) .. controls (102.7,73.01) and (102.74,72.74) .. (102.76,72.46)(106.41,70.43) .. controls (106.42,69.11) and (105.88,67.91) .. (105.03,67.34)(108.29,64.05) .. controls (108.15,64.5) and (107.94,64.89) .. (107.67,65.21)(106.8,59.78) .. controls (106.82,59.96) and (106.83,60.14) .. (106.83,60.33)(103.19,58.44) .. controls (103.06,58.65) and (102.95,58.89) .. (102.87,59.14)(100.05,58.85) .. controls (99.98,59.04) and (99.93,59.25) .. (99.89,59.45)(96.45,59.62) .. controls (96.65,59.78) and (96.84,59.98) .. (97,60.2)(92.15,63.58) .. controls (92.17,63.79) and (92.2,63.99) .. (92.24,64.19) ;
            		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (95.06,64.94) .. controls (94.97,64.08) and (95.25,63.23) .. (95.77,62.74) .. controls (96.3,62.26) and (96.98,62.23) .. (97.52,62.67) .. controls (97.71,62.17) and (98.07,61.82) .. (98.47,61.74) .. controls (98.88,61.65) and (99.29,61.84) .. (99.58,62.23) .. controls (99.75,61.78) and (100.07,61.47) .. (100.43,61.43) .. controls (100.8,61.38) and (101.16,61.59) .. (101.38,62) .. controls (101.68,61.52) and (102.15,61.31) .. (102.59,61.48) .. controls (103.04,61.64) and (103.37,62.14) .. (103.45,62.77) .. controls (103.81,62.9) and (104.12,63.25) .. (104.28,63.72) .. controls (104.44,64.19) and (104.45,64.73) .. (104.3,65.21) .. controls (104.66,65.86) and (104.75,66.71) .. (104.52,67.47) .. controls (104.3,68.22) and (103.81,68.75) .. (103.23,68.86) .. controls (103.22,69.57) and (102.94,70.22) .. (102.5,70.56) .. controls (102.05,70.9) and (101.5,70.88) .. (101.07,70.5) .. controls (100.89,71.35) and (100.37,71.97) .. (99.74,72.1) .. controls (99.11,72.23) and (98.48,71.84) .. (98.12,71.11) .. controls (97.69,71.47) and (97.17,71.57) .. (96.68,71.4) .. controls (96.19,71.22) and (95.77,70.78) .. (95.52,70.17) .. controls (95.08,70.24) and (94.65,69.92) .. (94.45,69.37) .. controls (94.25,68.82) and (94.32,68.16) .. (94.62,67.71) .. controls (94.22,67.39) and (94.02,66.75) .. (94.12,66.13) .. controls (94.22,65.51) and (94.59,65.04) .. (95.05,64.98) ; \\draw   (94.62,67.71) .. controls (94.81,67.86) and (95.02,67.93) .. (95.24,67.91)(95.52,70.17) .. controls (95.61,70.15) and (95.7,70.12) .. (95.79,70.07)(98.12,71.11) .. controls (98.06,70.97) and (98,70.83) .. (97.96,70.68)(101.07,70.5) .. controls (101.1,70.35) and (101.13,70.19) .. (101.13,70.03)(103.23,68.86) .. controls (103.23,68.11) and (102.92,67.43) .. (102.43,67.1)(104.3,65.21) .. controls (104.23,65.47) and (104.1,65.7) .. (103.95,65.88)(103.45,62.77) .. controls (103.46,62.87) and (103.47,62.97) .. (103.47,63.08)(101.38,62) .. controls (101.31,62.12) and (101.25,62.25) .. (101.2,62.4)(99.58,62.23) .. controls (99.54,62.34) and (99.51,62.46) .. (99.49,62.58)(97.52,62.67) .. controls (97.64,62.77) and (97.74,62.88) .. (97.84,63.01)(95.06,64.94) .. controls (95.07,65.06) and (95.09,65.18) .. (95.11,65.29) ;
            		\\draw  [fill={rgb, 255:red, 109; green, 171; blue, 38 }  ,fill opacity=1 ] (72.25,88.3) .. controls (72.05,86.24) and (72.71,84.2) .. (73.96,83.05) .. controls (75.21,81.9) and (76.83,81.84) .. (78.12,82.89) .. controls (78.58,81.69) and (79.42,80.87) .. (80.39,80.66) .. controls (81.36,80.45) and (82.34,80.89) .. (83.03,81.84) .. controls (83.42,80.76) and (84.19,80.03) .. (85.06,79.92) .. controls (85.94,79.8) and (86.79,80.32) .. (87.32,81.28) .. controls (88.03,80.13) and (89.15,79.65) .. (90.21,80.04) .. controls (91.26,80.43) and (92.06,81.62) .. (92.25,83.11) .. controls (93.12,83.43) and (93.84,84.26) .. (94.23,85.38) .. controls (94.62,86.5) and (94.64,87.8) .. (94.29,88.94) .. controls (95.14,90.47) and (95.34,92.51) .. (94.81,94.31) .. controls (94.28,96.1) and (93.11,97.36) .. (91.72,97.64) .. controls (91.71,99.32) and (91.04,100.86) .. (89.98,101.67) .. controls (88.91,102.48) and (87.61,102.43) .. (86.58,101.54) .. controls (86.14,103.55) and (84.9,105.03) .. (83.4,105.34) .. controls (81.9,105.65) and (80.4,104.73) .. (79.56,102.98) .. controls (78.53,103.85) and (77.29,104.09) .. (76.12,103.67) .. controls (74.95,103.25) and (73.96,102.2) .. (73.36,100.75) .. controls (72.3,100.92) and (71.28,100.16) .. (70.8,98.85) .. controls (70.32,97.54) and (70.49,95.96) .. (71.21,94.89) .. controls (70.27,94.12) and (69.79,92.6) .. (70.02,91.12) .. controls (70.25,89.64) and (71.14,88.53) .. (72.23,88.38) ; \\draw   (71.21,94.89) .. controls (71.66,95.25) and (72.17,95.42) .. (72.68,95.36)(73.36,100.75) .. controls (73.58,100.71) and (73.8,100.63) .. (74,100.52)(79.56,102.98) .. controls (79.41,102.66) and (79.28,102.32) .. (79.17,101.96)(86.58,101.54) .. controls (86.66,101.17) and (86.71,100.79) .. (86.73,100.41)(91.72,97.64) .. controls (91.73,95.85) and (91,94.21) .. (89.83,93.43)(94.29,88.94) .. controls (94.1,89.55) and (93.81,90.09) .. (93.44,90.52)(92.25,83.11) .. controls (92.28,83.35) and (92.3,83.6) .. (92.3,83.85)(87.32,81.28) .. controls (87.14,81.57) and (87,81.89) .. (86.89,82.23)(83.03,81.84) .. controls (82.94,82.1) and (82.87,82.38) .. (82.82,82.66)(78.12,82.89) .. controls (78.4,83.11) and (78.65,83.38) .. (78.88,83.68)(72.25,88.3) .. controls (72.28,88.58) and (72.32,88.86) .. (72.38,89.13) ;
            		\\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (75.19,89.74) .. controls (75.04,88.21) and (75.54,86.69) .. (76.47,85.83) .. controls (77.4,84.98) and (78.6,84.93) .. (79.56,85.71) .. controls (79.91,84.82) and (80.53,84.21) .. (81.25,84.05) .. controls (81.97,83.9) and (82.7,84.23) .. (83.22,84.93) .. controls (83.51,84.13) and (84.08,83.58) .. (84.73,83.5) .. controls (85.38,83.41) and (86.01,83.8) .. (86.41,84.51) .. controls (86.93,83.66) and (87.77,83.3) .. (88.56,83.59) .. controls (89.34,83.88) and (89.93,84.77) .. (90.08,85.87) .. controls (90.72,86.12) and (91.26,86.73) .. (91.55,87.57) .. controls (91.84,88.4) and (91.86,89.36) .. (91.59,90.21) .. controls (92.23,91.36) and (92.38,92.88) .. (91.98,94.21) .. controls (91.59,95.54) and (90.71,96.48) .. (89.68,96.69) .. controls (89.68,97.94) and (89.18,99.09) .. (88.39,99.69) .. controls (87.59,100.29) and (86.63,100.25) .. (85.86,99.59) .. controls (85.53,101.09) and (84.61,102.19) .. (83.49,102.42) .. controls (82.37,102.65) and (81.26,101.97) .. (80.63,100.67) .. controls (79.87,101.31) and (78.94,101.49) .. (78.07,101.18) .. controls (77.2,100.87) and (76.46,100.08) .. (76.02,99) .. controls (75.23,99.13) and (74.47,98.57) .. (74.11,97.59) .. controls (73.76,96.62) and (73.88,95.44) .. (74.42,94.64) .. controls (73.72,94.07) and (73.36,92.94) .. (73.53,91.84) .. controls (73.71,90.74) and (74.37,89.91) .. (75.18,89.79) ; \\draw   (74.42,94.64) .. controls (74.75,94.91) and (75.13,95.04) .. (75.52,94.99)(76.02,99) .. controls (76.18,98.97) and (76.34,98.92) .. (76.5,98.83)(80.63,100.67) .. controls (80.52,100.43) and (80.42,100.17) .. (80.35,99.9)(85.86,99.59) .. controls (85.92,99.32) and (85.96,99.04) .. (85.97,98.75)(89.68,96.69) .. controls (89.69,95.36) and (89.14,94.14) .. (88.28,93.55)(91.59,90.21) .. controls (91.45,90.67) and (91.24,91.07) .. (90.97,91.39)(90.08,85.87) .. controls (90.1,86.06) and (90.11,86.24) .. (90.11,86.43)(86.41,84.51) .. controls (86.28,84.73) and (86.17,84.97) .. (86.09,85.22)(83.22,84.93) .. controls (83.15,85.13) and (83.1,85.33) .. (83.06,85.54)(79.56,85.71) .. controls (79.77,85.87) and (79.96,86.07) .. (80.13,86.3)(75.19,89.74) .. controls (75.21,89.95) and (75.25,90.15) .. (75.29,90.36) ;
            		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (78.15,91.12) .. controls (78.06,90.24) and (78.34,89.37) .. (78.88,88.88) .. controls (79.41,88.39) and (80.1,88.37) .. (80.65,88.81) .. controls (80.85,88.3) and (81.21,87.95) .. (81.62,87.86) .. controls (82.03,87.78) and (82.45,87.96) .. (82.75,88.37) .. controls (82.91,87.91) and (83.24,87.59) .. (83.61,87.55) .. controls (83.98,87.5) and (84.35,87.72) .. (84.57,88.13) .. controls (84.87,87.64) and (85.35,87.43) .. (85.8,87.6) .. controls (86.25,87.76) and (86.59,88.27) .. (86.68,88.91) .. controls (87.05,89.05) and (87.35,89.4) .. (87.52,89.88) .. controls (87.69,90.35) and (87.69,90.91) .. (87.54,91.39) .. controls (87.91,92.05) and (87.99,92.92) .. (87.77,93.68) .. controls (87.54,94.45) and (87.04,94.99) .. (86.45,95.1) .. controls (86.45,95.82) and (86.16,96.48) .. (85.71,96.82) .. controls (85.25,97.17) and (84.7,97.15) .. (84.26,96.77) .. controls (84.07,97.62) and (83.54,98.26) .. (82.9,98.39) .. controls (82.26,98.52) and (81.62,98.13) .. (81.26,97.38) .. controls (80.82,97.75) and (80.3,97.86) .. (79.8,97.68) .. controls (79.3,97.5) and (78.88,97.05) .. (78.62,96.43) .. controls (78.17,96.5) and (77.73,96.18) .. (77.53,95.62) .. controls (77.32,95.06) and (77.39,94.39) .. (77.7,93.93) .. controls (77.3,93.6) and (77.1,92.96) .. (77.2,92.32) .. controls (77.3,91.69) and (77.68,91.22) .. (78.14,91.15) ; \\draw   (77.7,93.93) .. controls (77.89,94.09) and (78.11,94.16) .. (78.33,94.13)(78.62,96.43) .. controls (78.71,96.41) and (78.81,96.38) .. (78.89,96.33)(81.26,97.38) .. controls (81.2,97.25) and (81.14,97.1) .. (81.1,96.94)(84.26,96.77) .. controls (84.29,96.61) and (84.31,96.45) .. (84.32,96.29)(86.45,95.1) .. controls (86.45,94.34) and (86.14,93.64) .. (85.64,93.31)(87.54,91.39) .. controls (87.46,91.65) and (87.34,91.88) .. (87.18,92.07)(86.68,88.91) .. controls (86.69,89.01) and (86.7,89.12) .. (86.7,89.22)(84.57,88.13) .. controls (84.5,88.25) and (84.44,88.39) .. (84.39,88.53)(82.75,88.37) .. controls (82.71,88.48) and (82.68,88.6) .. (82.66,88.72)(80.65,88.81) .. controls (80.77,88.91) and (80.88,89.02) .. (80.97,89.15)(78.15,91.12) .. controls (78.16,91.24) and (78.18,91.36) .. (78.2,91.48) ;
            		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.05 ] (50.5,32) -- (237.1,32.9) -- (80.6,203.9) -- (50.5,203.6) -- cycle ;
            		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (385.5,164.2) .. controls (393.11,20.67) and (597.68,27.23) .. (599.1,164.2) ;
            		\\draw [line width=1]    (385.5,164.2) -- (599.1,164.2) ;
            		\\draw [line width=1]    (385.5,164.2) -- (547.7,72.9) ;
            		\\draw (65.5,148) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\\draw (366.5,150) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\\draw (298.5,150.5) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\\draw (602.5,152.5) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\\draw (549.5,55) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\\end{tikzpicture}
            \\end{center}'''
                                 % (latex(D), v1_str, latex(t_nghi), v2_str))

                # Nội dung lời giải chi tiết và bảng biến thiên dạng tkzTab (đã bọc ngoặc nhọn để tránh lỗi phẩy)
                loigiai = ('''Đổi $AB = %s\\text{ m} = %s$ km.\\\\
            Gọi $x = \\widehat{CAB}$ với $0 \\le x \\le \\frac{\\pi}{2}$ (rad).\\\\
            Trong tam giác vuông $ABC$, ta có: $AC = AB \\cdot \\cos x = %s \\cos x$ (km).\\\\
            Thời gian chèo thuyền từ $A$ đến $C$ là: $t_1 = \\frac{%s \\cos x}{%s} \\text{ (giờ)} = \\frac{%s \\cos x \\cdot 60}{%s} = %s \\cos x$ (phút).\\\\
            Góc ở tâm $\\widehat{COB} = 2x$ (rad). Độ dài cung nhỏ $CB$ là: $l_{CB} = R \\cdot 2x = %s \\cdot 2x = %s x$ (km).\\\\
            Thời gian chạy bộ từ $C$ đến $B$ dọc theo cung $CB$ là: $t_3 = \\frac{%s x}{%s} \\text{ (giờ)} = \\frac{%s x \\cdot 60}{%s} = %s x$ (phút).\\\\
            Thời gian chạy bộ từ $B$ về $A$ dọc theo đường thẳng $BA$ là: $t_4 = \\frac{%s}{%s} \\text{ (giờ)} = \\frac{%s \\cdot 60}{%s} = %s$ (phút).\\\\
            Thời gian nghỉ tại $C$ là: $t_2 = %s$ phút.\\\\
            Tổng thời gian người đó di chuyển và nghỉ ngơi là:\\\\
            $f(x) = t_1 + t_2 + t_3 + t_4 = %s \\cos x + %s + %s x + %s = %s \\cos x + %s x + %s$ (phút).\\\\
            Xét hàm số $f(x) = %s \\cos x + %s x + %s$ trên đoạn $\\left[0; \\frac{\\pi}{2}\\right]$.\\\\
            Ta có: $f'(x) = -%s \\sin x + %s$.\\\\
            Cho $f'(x) = 0 \\iff -%s \\sin x + %s = 0 \\iff \\sin x = \\frac{1}{2} \\iff x = \\frac{\\pi}{6}$ (vì $x \\in \\left[0; \\frac{\\pi}{2}\\right]$).\\\\
            Bảng biến thiên của hàm số $f(x)$ trên $\\left[0; \\frac{\\pi}{2}\\right]$:\\\\
            \\begin{center}
            \\begin{tikzpicture} 
            \\tkzTabInit[espcl=2.5,lgt=1.5]  
            {$x$/0.7,$f'(x)$/0.7,$f(x)$/2.1} 
            {$0$,$\\frac{\\pi}{6}$,$\\frac{\\pi}{2}$}  
            \\tkzTabLine{,+,0,-,}  
            \\tkzTabVar{-/{$%s$}, +/{$%s$}, -/{$%s$}} 
            \\end{tikzpicture}
            \\end{center}
            Tính giá trị của $f(x)$ tại các điểm biên và điểm cực trị:\\\\
            $f(0) = %s \\cos 0 + %s \\cdot 0 + %s = %s$ (phút).\\\\
            $f\\left(\\frac{\\pi}{6}\\right) = %s \\cos\\left(\\frac{\\pi}{6}\\right) + %s \\cdot \\frac{\\pi}{6} + %s = %s \\approx %s$ (phút).\\\\
            $f\\left(\\frac{\\pi}{2}\\right) = %s \\cos\\left(\\frac{\\pi}{2}\\right) + %s \\cdot \\frac{\\pi}{2} + %s \\approx %s$ (phút).\\\\
            Căn cứ vào bảng biến thiên, thời gian nhiều nhất để người đó về đến vị trí $A$ là khoảng $%s$ phút.'''
                           % (latex(D), D_km_str,
                              D_km_str,
                              D_km_str, v1_str, D_km_str, v1_str, k1_str,
                              R_km_str, D_km_str,
                              D_km_str, v2_str, D_km_str, v2_str, k2_str,
                              D_km_str, v2_str, D_km_str, v2_str, t4_str,
                              t_nghi_str,
                              k1_str, t_nghi_str, k2_str, t4_str, k1_str, k2_str, C_str,
                              k1_str, k2_str, C_str,
                              k1_str, k2_str,
                              k1_str, k2_str,
                              f0_str, f_pi6_val, f_pi2_val,
                              k1_str, k2_str, C_str, f0_str,
                              k1_str, k2_str, C_str, f_pi6_expr, f_pi6_val,
                              k1_str, k2_str, C_str, f_pi2_val,
                              f_pi6_val))
            dapan='\\shortans[0]{$%s$}\n'%(f_pi6_val)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

