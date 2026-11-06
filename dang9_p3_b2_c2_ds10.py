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


def bt_dang9_p3_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                def fmt_num(num):
                    # Hàm xử lý số: nếu là số nguyên thì bỏ phần thập phân, nếu là số thập phân thì thay dấu chấm bằng dấu phẩy
                    if isinstance(num, (int, float)) and num == int(num):
                        return str(int(num))
                    return str(num).replace('.', ',')

                # Random thông số sao cho luôn đảm bảo hệ phương trình có nghiệm nguyên tối ưu
                while True:
                    x0 = random.randint(10, 20)  # Đáp án x (số tín chỉ A)
                    y0 = random.randint(5, 15)   # Số tín chỉ B
                    M = x0 + y0                  # Tổng số tín chỉ tối đa

                    ca_base = random.randint(1, 4)
                    cb_base = ca_base + random.randint(1, 2)
                    cA = ca_base * 10            # Giá tín chỉ A
                    cB = cb_base * 10            # Giá tín chỉ B

                    B = cA * x0 + cB * y0        # Tổng ngân sách

                    # Đảm bảo giao điểm trục tung là số nguyên
                    if B % cB != 0:
                        continue

                    rb = random.choice([2, 3, 4, 5]) # Lượng CO2 giảm từ B

                    # Để đỉnh (x0, y0) là giá trị lớn nhất duy nhất, hệ số góc phải thỏa mãn: cA/cB < rA/rB < 1
                    min_ra = rb * cA / cB
                    max_ra = rb
                    valid_ras = [val/2 for val in range(int(min_ra * 2) + 1, int(max_ra * 2))]

                    if valid_ras:
                        ra = random.choice(valid_ras) # Lượng CO2 giảm từ A
                        break

                yC = int(B / cB)

                # Tính các giá trị của F tại các đỉnh
                val_O = 0
                val_A = ra * M
                val_B = ra * x0 + rb * y0
                val_C = rb * yC

                # Format số liệu sang chuỗi chuẩn của Việt Nam
                str_cA = fmt_num(cA)
                str_cB = fmt_num(cB)
                str_rA = fmt_num(ra)
                str_rB = fmt_num(rb)
                str_M = fmt_num(M)
                str_B = fmt_num(B)
                str_x0 = fmt_num(x0)
                str_y0 = fmt_num(y0)
                str_yC = fmt_num(yC)

                str_valA = fmt_num(val_A)
                str_valB = fmt_num(val_B)
                str_valC = fmt_num(val_C)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (str_x0)]
                da = random.choice(du)

                # Tạo các đáp án sai không trùng với đáp án đúng và phải dương
                s_vals = [x0 + 1, x0 + 2, x0 + 3, x0 - 1, x0 - 2, x0 - 3]
                s_vals = [v for v in s_vals if v > 0]
                s = ['$%s$' % (v) for v in s_vals]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.9,xscale=0.9]
            	\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ,even odd rule] (131.2,185.25) .. controls (131.2,143.03) and (165.43,108.8) .. (207.65,108.8) .. controls (249.87,108.8) and (284.1,143.03) .. (284.1,185.25) .. controls (284.1,227.47) and (249.87,261.7) .. (207.65,261.7) .. controls (165.43,261.7) and (131.2,227.47) .. (131.2,185.25)(127.6,185.25) .. controls (127.6,141.04) and (163.44,105.2) .. (207.65,105.2) .. controls (251.86,105.2) and (287.7,141.04) .. (287.7,185.25) .. controls (287.7,229.46) and (251.86,265.3) .. (207.65,265.3) .. controls (163.44,265.3) and (127.6,229.46) .. (127.6,185.25) ;
            	\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (185.64,228.82) .. controls (185.64,240.24) and (180.39,250.44) .. (172.18,257.13) .. controls (163.52,250.46) and (157.94,239.99) .. (157.94,228.21) .. controls (157.94,216.79) and (163.19,206.59) .. (171.4,199.9) .. controls (180.06,206.57) and (185.64,217.05) .. (185.64,228.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (191.39,249.88) .. controls (186.2,255.27) and (179.09,257.7) .. (172.18,257.13) .. controls (171.12,250.05) and (173.24,242.57) .. (178.59,237.01) .. controls (183.77,231.62) and (190.88,229.19) .. (197.8,229.76) .. controls (198.85,236.84) and (196.73,244.32) .. (191.39,249.88) -- cycle ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (161.25,218.98) .. controls (170.08,231.18) and (173.69,245.15) .. (172.18,257.13) .. controls (159.98,255.1) and (147.35,247.2) .. (138.25,234.63) .. controls (129.42,222.43) and (125.81,208.45) .. (127.32,196.47) .. controls (139.52,198.5) and (152.15,206.41) .. (161.25,218.98) -- cycle ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (194.75,179.52) .. controls (190.02,188.09) and (180.89,193.9) .. (170.4,193.9) .. controls (155.05,193.9) and (142.6,181.45) .. (142.6,166.1) .. controls (142.6,150.75) and (155.05,138.3) .. (170.4,138.3) .. controls (181.53,138.3) and (191.14,144.85) .. (195.58,154.3) -- (186.06,158.76) .. controls (183.3,152.88) and (177.33,148.81) .. (170.4,148.81) .. controls (160.85,148.81) and (153.11,156.55) .. (153.11,166.1) .. controls (153.11,175.65) and (160.85,183.39) .. (170.4,183.39) .. controls (176.92,183.39) and (182.6,179.78) .. (185.55,174.45) -- cycle ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ,even odd rule] (208.61,165) .. controls (208.61,155.12) and (216.47,147.11) .. (226.15,147.11) .. controls (235.83,147.11) and (243.69,155.12) .. (243.69,165) .. controls (243.69,174.88) and (235.83,182.89) .. (226.15,182.89) .. controls (216.47,182.89) and (208.61,174.88) .. (208.61,165)(198.1,165) .. controls (198.1,149.32) and (210.66,136.6) .. (226.15,136.6) .. controls (241.64,136.6) and (254.2,149.32) .. (254.2,165) .. controls (254.2,180.68) and (241.64,193.4) .. (226.15,193.4) .. controls (210.66,193.4) and (198.1,180.68) .. (198.1,165) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (263.85,196.31) .. controls (268.6,191.95) and (258.04,185.55) .. (257.65,195.63) .. controls (253.39,195.82) and (254.16,195.92) .. (249.42,195.53) .. controls (246.41,176.93) and (281.29,179.35) .. (272.96,197.95) .. controls (269.66,202.89) and (262.88,204.25) .. (260.66,208.51) .. controls (269.08,209.09) and (272.18,208.42) .. (274.41,208.9) .. controls (274.51,212.39) and (274.22,211.71) .. (274.51,216.26) .. controls (253.58,216.46) and (262.88,216.26) .. (249.81,216.07) .. controls (246.71,205.51) and (258.52,199.5) .. (263.85,196.31) -- cycle ;
            \end{tikzpicture}'''

                # Nội dung câu hỏi
                noidungcauhoi = (r'''\immini{Tín chỉ carbon là một đơn vị thương mại đại diện cho quyền phát thải khí nhà kính, trong đó mỗi tín chỉ được tính toán định lượng tương đương với một tấn CO$_2$ (hoặc khí nhà kính khác quy đổi tương đương) đã được cắt giảm hoặc loại bỏ khỏi khí quyển. Về bản chất toán học, đây là một hệ thống kế toán sinh thái dựa trên nguyên tắc cân bằng: các tổ chức phát thải vượt hạn ngạch phải mua lại tín chỉ từ những dự án có chỉ số phát thải âm để triệt tiêu phần chênh lệch. Việc định giá và giao dịch các tín chỉ này tạo ra một cơ chế tài chính minh bạch, biến các nỗ lực bảo vệ môi trường thành tài sản số có giá trị kinh tế bền vững.}{%s}  Một doanh nghiệp cần đầu tư mua tín chỉ carbon từ hai dự án: Dự án A (trồng rừng) và Dự án B (năng lượng sạch). Mỗi tín chỉ dự án A giá $%s$ USD, dự án B giá $%s$ USD. Dự án A giúp giảm $%s$ tấn CO$_2$/tín chỉ, dự án B giảm $%s$ tấn CO$_2$/tín chỉ. Tổng số tín chỉ của hai dự án không quá $%s$. Doanh nghiệp cần mua $x$ tín chỉ từ dự án A và $y$ tín chỉ từ dự án B để lượng CO$_2$ giảm được là tối đa, biết rằng tổng ngân sách của doanh nghiệp không quá $%s$ USD. Giá trị của $x$ là bao nhiêu?'''
                                 % (hinhve,str_cA, str_cB, str_rA, str_rB, str_M, str_B))

                # Các phương án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $x$, $y$ $\\left( x, y \\ge 0 \\right)$ lần lượt là số tín chỉ carbon doanh nghiệp mua từ dự án A và dự án B. \\\\
            Theo giả thiết, ta có hệ bất phương trình:
            $$ \\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ x + y \\le %s \\\\ %s x + %s y \\le %s \\end{cases} $$
            Miền nghiệm của hệ bất phương trình là một tứ giác với các đỉnh $O \\left( 0; 0 \\right)$, $A \\left( %s; 0 \\right)$, $B \\left( %s; %s \\right)$ và $C \\left( 0; %s \\right)$. \\\\
            Lượng CO$_2$ giảm được là $F \\left( x, y \\right) = %s x + %s y$. \\\\
            Ta tính giá trị của $F$ tại các đỉnh: \\\\
            $F \\left( 0; 0 \\right) = 0$ \\\\
            $F \\left( %s; 0 \\right) = %s \\cdot %s = %s$ \\\\
            $F \\left( %s; %s \\right) = %s \\cdot %s + %s \\cdot %s = %s$ \\\\
            $F \\left( 0; %s \\right) = %s \\cdot %s = %s$ \\\\
            Ta thấy $F$ đạt giá trị lớn nhất bằng $%s$ khi $x = %s$, $y = %s$. \\\\
            Vậy giá trị của $x$ là $%s$.'''
                           % (str_M, str_cA, str_cB, str_B,
                              str_M, str_x0, str_y0, str_yC,
                              str_rA, str_rB,
                              str_M, str_rA, str_M, str_valA,
                              str_x0, str_y0, str_rA, str_x0, str_rB, str_y0, str_valB,
                              str_yC, str_rB, str_yC, str_valC,
                              str_valB, str_x0, str_y0,
                              str_x0))
                dapan='\\shortans[0]{$%s$}\n'%(str_x0)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

