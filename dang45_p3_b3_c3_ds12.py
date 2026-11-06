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


def bt_dang45_p3_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random độ dài cạnh hình vuông (chọn các bội số của 3 để chia chẵn cho 3)
                a_val = random.choice([9, 12, 15, 18, 21, 24, 27, 30])
                a = Integer(a_val)

                # Tính bán kính các cung phần tư
                R_A = a
                R_E = Rational(2 * a, 3)
                R_F = Rational(a, 3)
                R_G = Rational(a, 3)

                # Tính toán diện tích phần tô đậm: S = S_A - S_E - S_F - S_G
                # S = 1/4 * pi * (R_A^2 - R_E^2 - R_F^2 - R_G^2)
                sum_sq = R_A**2 - R_E**2 - R_F**2 - R_G**2
                S_exact = Rational(1, 4) * pi * sum_sq
                S_coeff = Rational(sum_sq, 4)

                S_val = float(S_exact.evalf())
                kq_int = round(S_val)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq_int),
                      ]
                da= random.choice(du)
                s = ['$%s$'%(kq_int + 1),
                     '$%s$'%(kq_int + 2),
                     '$%s$'%(kq_int + 3),
                     '$%s$'%(kq_int - 1),
                     '$%s$'%(kq_int - 2),
                     '$%s$'%(kq_int - 3),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
            	\draw  [line width=1]  (29.64,51.24) -- (221.6,51.24) -- (221.6,243.2) -- (29.64,243.2) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1]  (156.5,116.01) .. controls (142.6,117.9) and (96.6,120.9) .. (92.3,179.6) .. controls (122.6,178.9) and (213.1,162.4) .. (221.69,51.8) .. controls (224.6,107.9) and (173.6,242.4) .. (29.64,242.39) .. controls (26.1,194.4) and (69.1,116.4) .. (156.5,116.01) -- cycle ;
            	\draw [line width=1]    (90.82,51.6) -- (92.02,243.2) ;
            	\draw [line width=1]    (155.92,51.1) -- (157.12,242.7) ;
            	\draw [line width=1]    (30.42,180.7) -- (221.62,180.7) ;
            	\draw [line width=1]    (30.22,116.2) -- (221.42,116.2) ;
            	\draw (10,35) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (221.5,35) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (221.6,243.2) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (12,241.5) node [anchor=north west][inner sep=0.75pt]    {$D$};
            	\draw (137.5,95) node [anchor=north west][inner sep=0.75pt]    {$G$};
            	\draw (140,182) node [anchor=north west][inner sep=0.75pt]    {$F$};
            \end{tikzpicture}'''

                # Câu hỏi
                noidungcauhoi = (r'''\immini{Từ bảng gỗ hình vuông $ABCD$ có độ dài cạnh $%s$ cm, bạn Anh chia hình vuông này thành $9$ hình vuông nhỏ bằng nhau rồi vẽ một hình càng cua được giới hạn bởi các cung phần tư của các đường tròn tâm $A, E, F, G$ (xem hình vẽ). Diện tích hình càng cua (phần tô đậm trong hình vẽ) theo đơn vị $\text{cm}^2$? (Kết quả làm tròn đến hàng đơn vị).}{%s}'''
                                 %(latex(a),hinhve))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Chia hình vuông cạnh $%s$ cm thành $9$ hình vuông nhỏ bằng nhau nên độ dài cạnh mỗi hình vuông nhỏ là $\\frac{%s}{3} = %s$ cm. \\\\
                            Bán kính của các cung phần tư tâm $A, E, F, G$ lần lượt là $R_A = %s$ cm, $R_E = 2 \\cdot %s = %s$ cm, $R_F = 1 \\cdot %s = %s$ cm, $R_G = 1 \\cdot %s = %s$ cm. \\\\
                            Diện tích hình càng cua là hiệu của diện tích cung phần tư tâm $A$ và tổng diện tích các cung phần tư tâm $E, F, G$: \\\\
                            $\\begin{aligned} S &= S_A - S_E - S_F - S_G \\\\ &= \\frac{1}{4}\\pi R_A^2 - \\frac{1}{4}\\pi R_E^2 - \\frac{1}{4}\\pi R_F^2 - \\frac{1}{4}\\pi R_G^2 \\\\ &= \\frac{1}{4}\\pi \\left( %s^2 - %s^2 - %s^2 - %s^2 \\right) \\\\ &= \\frac{1}{4}\\pi \\cdot %s = %s\\pi \\approx %s \\text{ (cm}^2\\text{)}. \\end{aligned}$'''
                         %(latex(a), latex(a), latex(R_F),
                           latex(R_A), latex(R_F), latex(R_E), latex(R_F), latex(R_F), latex(R_F), latex(R_G),
                           latex(R_A), latex(R_E), latex(R_F), latex(R_G),
                           latex(sum_sq), latex(S_coeff), kq_int
                         ))
                dapan='\\shortans[0]{$%s$}\n'%(kq_int)                                                                                                                        


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

