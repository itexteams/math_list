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


def bt_dang11_p1_b2_c2_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='4':
                # Khai báo biến
                a1=randint(1,9)
                h=randint(1,9)
                a2=a1+h
                a3=a2+h
                a4=a3+h
                a5=a4+h
                a6=a5+h

                m11=randint(1,9)
                m12=randint(1,9)
                m13=randint(1,9)
                m14=randint(1,9)
                m15=randint(1,9)

                n1=m11+m12+m13+m14+m15

                k=randint(2,5)
                m21=k*m11
                m22=k*m12
                m23=k*m13
                m24=k*m14
                m25=k*m15-1

                n2=m21+m22+m23+m24+m25

                x1=Rational(a1+a2,2)
                x2=Rational(a2+a3,2)
                x3=Rational(a3+a4,2)
                x4=Rational(a4+a5,2)
                x5=Rational(a5+a6,2)

                xtb1=Rational(m11*x1+m12*x2+m13*x3+m14*x4+m15*x5,n1)
                ps1=Rational(m11*x1**2+m12*x2**2+m13*x3**2+m14*x4**2+m15*x5**2,n1)-xtb1**2
                dolech1=sqrt(ps1)
                dl1=round(dolech1,4)

                xtb2=Rational(m21*x1+m22*x2+m23*x3+m24*x4+m25*x5,n2)
                ps2=Rational(m21*x1**2+m22*x2**2+m23*x3**2+m24*x4**2+m25*x5**2,n2)-xtb2**2
                dolech2=sqrt(ps2)
                dl2=round(dolech2,4)

                sosanh=dolech1/dolech2

                du = ['$s_1>s_2$',
                    ]
                da= random.choice(du)
                s = ['$s_1<s_2$',
                    '$s_1=s_2$',
                    '$2s_1=s_2$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Hai mẫu số liệu ghép nhóm $M_1, M_2$ có bảng tần số ghép nhóm như sau  \n'
                                '\\begin{center}  \n'
                                    '$M_1$ \\hspace*{1cm}  \n'
                                    '\\begin{tabular}{|c|c|c|c|c|c|}  \n'
                                        '\\hline   \n'
                                        'Nhóm & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\  \n'
                                        '\\hline  \n'
                                        'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\  \n'
                                        '\\hline  \n'
                                    '\\end{tabular} \\\\  \n'
                                    '\\vspace*{0.5cm}  \n'
                                    '$M_2$ \\hspace*{1cm}  \n'
                                    '\\begin{tabular}{|c|c|c|c|c|c|}  \n'
                                        '\\hline  \n'
                                        'Nhóm & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\  \n'
                                        '\\hline  \n'
                                        'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\  \n'
                                        '\\hline  \n'
                                    '\\end{tabular}  \n'
                                '\\end{center}  \n'
                                'Gọi $s_1, s_2$ lần lượt là độ lệch chuẩn của mẫu số liệu ghép nhóm $M_1, M_2$. Phát biểu nào sau đây đúng?'
                                %(latex(a1),latex(a2),latex(a2),latex(a3),latex(a3),latex(a4),latex(a4),latex(a5),latex(a5),latex(a6),
                                latex(m11),latex(m12),latex(m13),latex(m14),latex(m15),
                                latex(a1),latex(a2),latex(a2),latex(a3),latex(a3),latex(a4),latex(a4),latex(a5),latex(a5),latex(a6),
                                latex(m21),latex(m22),latex(m23),latex(m24),latex(m25),
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s; x_2=%s; x_3=%s; x_4=%s; x_5=%s$. \\\\ \n'
                        'Xét mẫu số liệu ghép nhóm $M_1$. \\\\ \n'
                        '\\hspace*{1cm} Cỡ mẫu $n_1=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        '\\hspace*{1cm} Số trung bình $\\bar{x}_1=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Phương sai $s_1^2=\\dfrac{%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2}{%s}-\\left(%s\\right)^2=%s$. \\\\ \n'
                        '\\hspace*{1cm} Độ lệch chuẩn $s_1=\\sqrt{s_1^2}=%s \\approx %s$. \\hspace*{1cm} (1). \\\\ \n'

                        'Xét mẫu số liệu ghép nhóm $M_2$. \\\\ \n'
                        '\\hspace*{1cm} Cỡ mẫu $n_2=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        '\\hspace*{1cm} Số trung bình $\\bar{x}_2=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Phương sai $s_2^2=\\dfrac{%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2}{%s}-\\left(%s\\right)^2=%s$. \\\\ \n'
                        '\\hspace*{1cm} Độ lệch chuẩn $s_2=\\sqrt{s_2^2}=%s \\approx %s$. \\hspace*{1cm} (2). \\\\ \n'
                        'Từ (1) và (2) ta thấy $s_1>s_2$.'
                        %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(m11),latex(m12),latex(m13),latex(m14),latex(m15),latex(n1),
                        latex(m11),latex(x1),latex(m12),latex(x2),latex(m13),latex(x3),latex(m14),latex(x4),latex(m15),latex(x5),latex(n1),latex(xtb1),
                        latex(m11),latex(x1),latex(m12),latex(x2),latex(m13),latex(x3),latex(m14),latex(x4),latex(m15),latex(x5),latex(n1),latex(xtb1),latex(ps1),
                        latex(dolech1),latex(dl1),

                        latex(m21),latex(m22),latex(m23),latex(m24),latex(m25),latex(n2),
                        latex(m21),latex(x1),latex(m22),latex(x2),latex(m23),latex(x3),latex(m24),latex(x4),latex(m25),latex(x5),latex(n2),latex(xtb2),
                        latex(m21),latex(x1),latex(m22),latex(x2),latex(m23),latex(x3),latex(m24),latex(x4),latex(m25),latex(x5),latex(n2),latex(xtb2),latex(ps2),
                        latex(dolech2),latex(dl2),
                        ))

            if dang=='3':
                # Khai báo biến
                a1=randint(1,9)
                h=randint(1,9)
                a2=a1+h
                a3=a2+h
                a4=a3+h
                a5=a4+h
                a6=a5+h

                m11=randint(1,9)
                m12=randint(1,9)
                m13=randint(1,9)
                m14=randint(1,9)
                m15=randint(1,9)

                n1=m11+m12+m13+m14+m15

                k=randint(2,5)
                m21=k*m11
                m22=k*m12
                m23=k*m13
                m24=k*m14
                m25=k*m15+1

                n2=m21+m22+m23+m24+m25

                x1=Rational(a1+a2,2)
                x2=Rational(a2+a3,2)
                x3=Rational(a3+a4,2)
                x4=Rational(a4+a5,2)
                x5=Rational(a5+a6,2)

                xtb1=Rational(m11*x1+m12*x2+m13*x3+m14*x4+m15*x5,n1)
                ps1=Rational(m11*x1**2+m12*x2**2+m13*x3**2+m14*x4**2+m15*x5**2,n1)-xtb1**2
                dolech1=sqrt(ps1)
                dl1=round(dolech1,4)

                xtb2=Rational(m21*x1+m22*x2+m23*x3+m24*x4+m25*x5,n2)
                ps2=Rational(m21*x1**2+m22*x2**2+m23*x3**2+m24*x4**2+m25*x5**2,n2)-xtb2**2
                dolech2=sqrt(ps2)
                dl2=round(dolech2,4)

                sosanh=dolech1/dolech2

                du = ['$s_1<s_2$',
                    ]
                da= random.choice(du)
                s = ['$s_1>s_2$',
                    '$s_1=s_2$',
                    '$2s_1=s_2$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Hai mẫu số liệu ghép nhóm $M_1, M_2$ có bảng tần số ghép nhóm như sau  \n'
                                '\\begin{center}  \n'
                                    '$M_1$ \\hspace*{1cm}  \n'
                                    '\\begin{tabular}{|c|c|c|c|c|c|}  \n'
                                        '\\hline   \n'
                                        'Nhóm & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\  \n'
                                        '\\hline  \n'
                                        'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\  \n'
                                        '\\hline  \n'
                                    '\\end{tabular} \\\\  \n'
                                    '\\vspace*{0.5cm}  \n'
                                    '$M_2$ \\hspace*{1cm}  \n'
                                    '\\begin{tabular}{|c|c|c|c|c|c|}  \n'
                                        '\\hline  \n'
                                        'Nhóm & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\  \n'
                                        '\\hline  \n'
                                        'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\  \n'
                                        '\\hline  \n'
                                    '\\end{tabular}  \n'
                                '\\end{center}  \n'
                                'Gọi $s_1, s_2$ lần lượt là độ lệch chuẩn của mẫu số liệu ghép nhóm $M_1, M_2$. Phát biểu nào sau đây đúng?'
                                %(latex(a1),latex(a2),latex(a2),latex(a3),latex(a3),latex(a4),latex(a4),latex(a5),latex(a5),latex(a6),
                                latex(m11),latex(m12),latex(m13),latex(m14),latex(m15),
                                latex(a1),latex(a2),latex(a2),latex(a3),latex(a3),latex(a4),latex(a4),latex(a5),latex(a5),latex(a6),
                                latex(m21),latex(m22),latex(m23),latex(m24),latex(m25),
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s; x_2=%s; x_3=%s; x_4=%s; x_5=%s$. \\\\ \n'
                        'Xét mẫu số liệu ghép nhóm $M_1$. \\\\ \n'
                        '\\hspace*{1cm} Cỡ mẫu $n_1=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        '\\hspace*{1cm} Số trung bình $\\bar{x}_1=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Phương sai $s_1^2=\\dfrac{%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2}{%s}-\\left(%s\\right)^2=%s$. \\\\ \n'
                        '\\hspace*{1cm} Độ lệch chuẩn $s_1=\\sqrt{s_1^2}=%s \\approx %s$. \\hspace*{1cm} (1). \\\\ \n'

                        'Xét mẫu số liệu ghép nhóm $M_2$. \\\\ \n'
                        '\\hspace*{1cm} Cỡ mẫu $n_2=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        '\\hspace*{1cm} Số trung bình $\\bar{x}_2=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Phương sai $s_2^2=\\dfrac{%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2}{%s}-\\left(%s\\right)^2=%s$. \\\\ \n'
                        '\\hspace*{1cm} Độ lệch chuẩn $s_2=\\sqrt{s_2^2}=%s \\approx %s$. \\hspace*{1cm} (2). \\\\ \n'
                        'Từ (1) và (2) ta thấy $s_1<s_2$.'
                        %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(m11),latex(m12),latex(m13),latex(m14),latex(m15),latex(n1),
                        latex(m11),latex(x1),latex(m12),latex(x2),latex(m13),latex(x3),latex(m14),latex(x4),latex(m15),latex(x5),latex(n1),latex(xtb1),
                        latex(m11),latex(x1),latex(m12),latex(x2),latex(m13),latex(x3),latex(m14),latex(x4),latex(m15),latex(x5),latex(n1),latex(xtb1),latex(ps1),
                        latex(dolech1),latex(dl1),

                        latex(m21),latex(m22),latex(m23),latex(m24),latex(m25),latex(n2),
                        latex(m21),latex(x1),latex(m22),latex(x2),latex(m23),latex(x3),latex(m24),latex(x4),latex(m25),latex(x5),latex(n2),latex(xtb2),
                        latex(m21),latex(x1),latex(m22),latex(x2),latex(m23),latex(x3),latex(m24),latex(x4),latex(m25),latex(x5),latex(n2),latex(xtb2),latex(ps2),
                        latex(dolech2),latex(dl2),
                        ))

            if dang=='2':
                # Khai báo biến
                a1=randint(1,9)
                h=randint(1,9)
                a2=a1+h
                a3=a2+h
                a4=a3+h
                a5=a4+h
                a6=a5+h

                m11=randint(1,9)
                m12=randint(1,9)
                m13=randint(1,9)
                m14=randint(1,9)
                m15=randint(1,9)

                n1=m11+m12+m13+m14+m15

                k=randint(2,5)
                m21=k*m11
                m22=k*m12
                m23=k*m13
                m24=k*m14
                m25=k*m15

                n2=m21+m22+m23+m24+m25

                x1=Rational(a1+a2,2)
                x2=Rational(a2+a3,2)
                x3=Rational(a3+a4,2)
                x4=Rational(a4+a5,2)
                x5=Rational(a5+a6,2)

                xtb1=Rational(m11*x1+m12*x2+m13*x3+m14*x4+m15*x5,n1)
                ps1=Rational(m11*x1**2+m12*x2**2+m13*x3**2+m14*x4**2+m15*x5**2,n1)-xtb1**2
                dolech1=sqrt(ps1)

                xtb2=Rational(m21*x1+m22*x2+m23*x3+m24*x4+m25*x5,n2)
                ps2=Rational(m21*x1**2+m22*x2**2+m23*x3**2+m24*x4**2+m25*x5**2,n2)-xtb2**2
                dolech2=sqrt(ps2)

                sosanh=dolech1/dolech2

                du = ['$\\dfrac{s_1}{s_2}=%s$'%(latex(sosanh)),
                    ]
                da= random.choice(du)
                s = ['$\\dfrac{s_1}{s_2}=2$',
                    '$\\dfrac{s_1}{s_2}=3$',
                    '$\\dfrac{s_1}{s_2}=4$',
                    '$\\dfrac{s_1}{s_2}=\\dfrac{1}{2}$',
                    '$\\dfrac{s_1}{s_2}=\\dfrac{1}{3}$',
                    '$\\dfrac{s_1}{s_2}=\\dfrac{1}{4}$',
                    '$\\dfrac{s_1}{s_2}=\\dfrac{3}{2}$',
                    '$\\dfrac{s_1}{s_2}=\\dfrac{2}{3}$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Hai mẫu số liệu ghép nhóm $M_1, M_2$ có bảng tần số ghép nhóm như sau  \n'
                                '\\begin{center}  \n'
                                    '$M_1$ \\hspace*{1cm}  \n'
                                    '\\begin{tabular}{|c|c|c|c|c|c|}  \n'
                                        '\\hline   \n'
                                        'Nhóm & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\  \n'
                                        '\\hline  \n'
                                        'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\  \n'
                                        '\\hline  \n'
                                    '\\end{tabular} \\\\  \n'
                                    '\\vspace*{0.5cm}  \n'
                                    '$M_2$ \\hspace*{1cm}  \n'
                                    '\\begin{tabular}{|c|c|c|c|c|c|}  \n'
                                        '\\hline  \n'
                                        'Nhóm & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\  \n'
                                        '\\hline  \n'
                                        'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\  \n'
                                        '\\hline  \n'
                                    '\\end{tabular}  \n'
                                '\\end{center}  \n'
                                'Gọi $s_1, s_2$ lần lượt là độ lệch chuẩn của mẫu số liệu ghép nhóm $M_1, M_2$. Phát biểu nào sau đây đúng?'
                                %(latex(a1),latex(a2),latex(a2),latex(a3),latex(a3),latex(a4),latex(a4),latex(a5),latex(a5),latex(a6),
                                latex(m11),latex(m12),latex(m13),latex(m14),latex(m15),
                                latex(a1),latex(a2),latex(a2),latex(a3),latex(a3),latex(a4),latex(a4),latex(a5),latex(a5),latex(a6),
                                latex(m21),latex(m22),latex(m23),latex(m24),latex(m25),
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s; x_2=%s; x_3=%s; x_4=%s; x_5=%s$. \\\\ \n'
                        'Xét mẫu số liệu ghép nhóm $M_1$. \\\\ \n'
                        '\\hspace*{1cm} Cỡ mẫu $n_1=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        '\\hspace*{1cm} Số trung bình $\\bar{x}_1=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Phương sai $s_1^2=\\dfrac{%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2}{%s}-\\left(%s\\right)^2=%s$. \\\\ \n'
                        '\\hspace*{1cm} Độ lệch chuẩn $s_1=\\sqrt{s_1^2}=%s$. \\hspace*{1cm} (1). \\\\ \n'

                        'Xét mẫu số liệu ghép nhóm $M_2$. \\\\ \n'
                        '\\hspace*{1cm} Cỡ mẫu $n_2=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        '\\hspace*{1cm} Số trung bình $\\bar{x}_2=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Phương sai $s_2^2=\\dfrac{%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2}{%s}-\\left(%s\\right)^2=%s$. \\\\ \n'
                        '\\hspace*{1cm} Độ lệch chuẩn $s_2=\\sqrt{s_2^2}=%s$. \\hspace*{1cm} (2). \\\\ \n'
                        'Từ (1) và (2) ta thấy $\\dfrac{s_1}{s_2}=%s$.'
                        %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(m11),latex(m12),latex(m13),latex(m14),latex(m15),latex(n1),
                        latex(m11),latex(x1),latex(m12),latex(x2),latex(m13),latex(x3),latex(m14),latex(x4),latex(m15),latex(x5),latex(n1),latex(xtb1),
                        latex(m11),latex(x1),latex(m12),latex(x2),latex(m13),latex(x3),latex(m14),latex(x4),latex(m15),latex(x5),latex(n1),latex(xtb1),latex(ps1),
                        latex(dolech1),

                        latex(m21),latex(m22),latex(m23),latex(m24),latex(m25),latex(n2),
                        latex(m21),latex(x1),latex(m22),latex(x2),latex(m23),latex(x3),latex(m24),latex(x4),latex(m25),latex(x5),latex(n2),latex(xtb2),
                        latex(m21),latex(x1),latex(m22),latex(x2),latex(m23),latex(x3),latex(m24),latex(x4),latex(m25),latex(x5),latex(n2),latex(xtb2),latex(ps2),
                        latex(dolech2),
                        latex(sosanh)
                        ))

            if dang=='1':
                # Khai báo biến
                a1=randint(1,9)
                h=randint(1,9)
                a2=a1+h
                a3=a2+h
                a4=a3+h
                a5=a4+h
                a6=a5+h

                m11=randint(1,9)
                m12=randint(1,9)
                m13=randint(1,9)
                m14=randint(1,9)
                m15=randint(1,9)

                n1=m11+m12+m13+m14+m15

                k=randint(2,5)
                m21=k*m11
                m22=k*m12
                m23=k*m13
                m24=k*m14
                m25=k*m15

                n2=m21+m22+m23+m24+m25

                x1=Rational(a1+a2,2)
                x2=Rational(a2+a3,2)
                x3=Rational(a3+a4,2)
                x4=Rational(a4+a5,2)
                x5=Rational(a5+a6,2)

                xtb1=Rational(m11*x1+m12*x2+m13*x3+m14*x4+m15*x5,n1)
                ps1=Rational(m11*x1**2+m12*x2**2+m13*x3**2+m14*x4**2+m15*x5**2,n1)-xtb1**2
                dolech1=sqrt(ps1)

                xtb2=Rational(m21*x1+m22*x2+m23*x3+m24*x4+m25*x5,n2)
                ps2=Rational(m21*x1**2+m22*x2**2+m23*x3**2+m24*x4**2+m25*x5**2,n2)-xtb2**2
                dolech2=sqrt(ps2)

                sosanh=dolech1/dolech2

                du = ['$s_1=%s s_2$'%(latex(sosanh)),
                    ]
                da= random.choice(du)
                s = ['$s_1=2s_2$',
                    '$2s_1=s_2$',
                    '$s_1=3s_2$',
                    '$3s_1=s_2$',
                    '$s_1=4s_2$',
                    '$4s_1=s_2$',
                    '$s_1>s_2$',
                    '$s_1<s_2$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Hai mẫu số liệu ghép nhóm $M_1, M_2$ có bảng tần số ghép nhóm như sau  \n'
                                '\\begin{center}  \n'
                                    '$M_1$ \\hspace*{1cm}  \n'
                                    '\\begin{tabular}{|c|c|c|c|c|c|}  \n'
                                        '\\hline   \n'
                                        'Nhóm & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\  \n'
                                        '\\hline  \n'
                                        'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\  \n'
                                        '\\hline  \n'
                                    '\\end{tabular} \\\\  \n'
                                    '\\vspace*{0.5cm}  \n'
                                    '$M_2$ \\hspace*{1cm}  \n'
                                    '\\begin{tabular}{|c|c|c|c|c|c|}  \n'
                                        '\\hline  \n'
                                        'Nhóm & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\  \n'
                                        '\\hline  \n'
                                        'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\  \n'
                                        '\\hline  \n'
                                    '\\end{tabular}  \n'
                                '\\end{center}  \n'
                                'Gọi $s_1, s_2$ lần lượt là độ lệch chuẩn của mẫu số liệu ghép nhóm $M_1, M_2$. Phát biểu nào sau đây đúng?'
                                %(latex(a1),latex(a2),latex(a2),latex(a3),latex(a3),latex(a4),latex(a4),latex(a5),latex(a5),latex(a6),
                                latex(m11),latex(m12),latex(m13),latex(m14),latex(m15),
                                latex(a1),latex(a2),latex(a2),latex(a3),latex(a3),latex(a4),latex(a4),latex(a5),latex(a5),latex(a6),
                                latex(m21),latex(m22),latex(m23),latex(m24),latex(m25),
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s; x_2=%s; x_3=%s; x_4=%s; x_5=%s$. \\\\ \n'
                        'Xét mẫu số liệu ghép nhóm $M_1$. \\\\ \n'
                        '\\hspace*{1cm} Cỡ mẫu $n_1=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        '\\hspace*{1cm} Số trung bình $\\bar{x}_1=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Phương sai $s_1^2=\\dfrac{%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2}{%s}-\\left(%s\\right)^2=%s$. \\\\ \n'
                        '\\hspace*{1cm} Độ lệch chuẩn $s_1=\\sqrt{s_1^2}=%s$. \\hspace*{1cm} (1). \\\\ \n'

                        'Xét mẫu số liệu ghép nhóm $M_2$. \\\\ \n'
                        '\\hspace*{1cm} Cỡ mẫu $n_2=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        '\\hspace*{1cm} Số trung bình $\\bar{x}_2=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Phương sai $s_2^2=\\dfrac{%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2+%s \\cdot \\left(%s\\right)^2}{%s}-\\left(%s\\right)^2=%s$. \\\\ \n'
                        '\\hspace*{1cm} Độ lệch chuẩn $s_2=\\sqrt{s_2^2}=%s$. \\hspace*{1cm} (2). \\\\ \n'
                        'Từ (1) và (2) ta thấy $s_1=%s s_2$.'
                        %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(m11),latex(m12),latex(m13),latex(m14),latex(m15),latex(n1),
                        latex(m11),latex(x1),latex(m12),latex(x2),latex(m13),latex(x3),latex(m14),latex(x4),latex(m15),latex(x5),latex(n1),latex(xtb1),
                        latex(m11),latex(x1),latex(m12),latex(x2),latex(m13),latex(x3),latex(m14),latex(x4),latex(m15),latex(x5),latex(n1),latex(xtb1),latex(ps1),
                        latex(dolech1),

                        latex(m21),latex(m22),latex(m23),latex(m24),latex(m25),latex(n2),
                        latex(m21),latex(x1),latex(m22),latex(x2),latex(m23),latex(x3),latex(m24),latex(x4),latex(m25),latex(x5),latex(n2),latex(xtb2),
                        latex(m21),latex(x1),latex(m22),latex(x2),latex(m23),latex(x3),latex(m24),latex(x4),latex(m25),latex(x5),latex(n2),latex(xtb2),latex(ps2),
                        latex(dolech2),
                        latex(sosanh)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('=1 s_2', '=s_2')
            return content

