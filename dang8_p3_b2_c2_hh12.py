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


def bt_dang8_p3_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thông số đề bài gốc
                # Điểm A(xA, yA, zA)
                xA, yA, zA = randint(-3,3), randint(-3,3), randint(1,4)
                # Đường thẳng Delta: x=x0+at, y=y0+bt, z=z0+ct
                # Điểm M0(x0, y0, z0) thuộc Delta
                x0, y0, z0 = randint(-3,-1), randint(1,3), randint(-3,-1) # x=0+t, y=1+2t, z=-1+t
                # vectơ chỉ phương u(a, b, c) của Delta
                a, b, c = randint(1,3), randint(1,3), randint(1,3)

                # 1. Tính toán
                # vectơ M0A: (xA-x0, yA-y0, zA-z0)
                M0A_x, M0A_y, M0A_z = xA - x0, yA - y0, zA - z0 # (1, 0, 2)
                # vectơ u: (1, 2, 1)

                # Công thức khoảng cách: d(A, Delta) = |[M0A, u]| / |u|

                # a. Tích có hướng [M0A, u]
                tich_co_huong_x = M0A_y * c - M0A_z * b # 0*1 - 2*2 = -4
                tich_co_huong_y = M0A_z * a - M0A_x * c # 2*1 - 1*1 = 1
                tich_co_huong_z = M0A_x * b - M0A_y * a # 1*2 - 0*1 = 2

                # b. Độ lớn |[M0A, u]|
                tu_so_binh_phuong = tich_co_huong_x**2 + tich_co_huong_y**2 + tich_co_huong_z**2 # 16 + 1 + 4 = 21
                tu_so = sqrt(tu_so_binh_phuong) # sqrt(21)

                # c. Độ lớn |u|
                mau_so_binh_phuong = a**2 + b**2 + c**2 # 1 + 4 + 1 = 6
                mau_so = sqrt(mau_so_binh_phuong) # sqrt(6)

                # d. Kết quả d(A, Delta)
                kq_chinh_xac = tu_so / mau_so # sqrt(21)/sqrt(6) = sqrt(7/2)

                # Kết quả làm tròn đến hàng phần mười (như lời giải gốc: sqrt(14)/2 ~ 1.87 -> 1.9)
                # Lời giải gốc dùng: AH = sqrt(14)/2. Lỗi in ấn trong lời giải gốc?
                # Ta tính theo công thức vectơ: d = sqrt(21)/sqrt(6) = sqrt(126)/6 ≈ 1.87

                kq_lam_tron = Decimal(float(kq_chinh_xac)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Vì lời giải gốc dùng sqrt(14)/2 ≈ 1.9, ta dùng kết quả này để giữ đúng đề bài
                # Ta tính lại theo lời giải gốc: H(1/2; 2; -1/2). AH^2 = (1/2)^2 + (1)^2 + (3/2)^2 = 1/4 + 1 + 9/4 = 14/4 = 7/2
                # AH = sqrt(7/2) = sqrt(14)/2 ≈ 1.87. Lời giải ghi sqrt(14)/2, làm tròn 1.9
                # Ta dùng kết quả chính xác: 1.87 -> 1.9

                kq_str = str(kq_lam_tron).replace('.', ',') # 1,9

                # 2. Các đáp án trắc nghiệm
                du = ['$%s$'%(kq_str)]
                da= random.choice(du)

                # Các đáp án sai được chọn xung quanh giá trị đúng
                kq_float = float(kq_lam_tron)
                s = [f'${kq_float+0.1:.1f}'.replace('.', ',') + '$', 
                     f'${kq_float-0.1:.1f}'.replace('.', ',') + '$', 
                     f'${kq_float+0.2:.1f}'.replace('.', ',') + '$',
                     f'${kq_float-0.2:.1f}'.replace('.', ',') + '$',
                     f'${kq_float+0.3:.1f}'.replace('.', ',') + '$',
                     f'${kq_float-0.3:.1f}'.replace('.', ',') + '$']

                # Lọc bỏ đáp án trùng và chọn ngẫu nhiên 3 đáp án sai
                s = list(set([x for x in s if x != da]))
                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # 3. Câu hỏi
                pt_delta = '\\begin{cases} x = t \\\\ y = 1+2t \\\\ z = -1+t \\end{cases}'

                noidungcauhoi = ('''Trong không gian $Oxyz$, khoảng cách từ điểm $A(%s;%s;%s)$ đến đường thẳng $\\Delta:\\begin{cases} x = t \\\\ y = 1+2t \\\\ z = -1+t \\end{cases}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần mười).'''
                                  %(latex(xA),latex(yA),latex(zA)
                                  ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # 4. Nội dung lời giải (theo phương pháp hình chiếu H)

                # Giá trị t trong lời giải gốc: t=1/2
                t_hinh_chieu = Rational(1, 2)
                # Tọa độ H: x=1/2, y=1+2(1/2)=2, z=-1+1/2 = -1/2
                H_x, H_y, H_z = Rational(1, 2), 2, Rational(-1, 2)
                # vectơ AH: (1/2-1, 2-1, -1/2-1) = (-1/2, 1, -3/2)
                AH_vectơ = f"\\left(-\\frac{1}{2}; 1; -\\frac{3}{2}\\right)"

                loigiai=('''Đường thẳng $\\Delta$ có vectơ chỉ phương $\\vec{u}(%s;%s;%s)$. Điểm $M_0(%s;%s;%s)$ thuộc $\\Delta$.\\\\
                            Gọi $H$ là hình chiếu vuông góc của $A$ lên $\\Delta$. $H \\in \\Delta \\Rightarrow  H(t; 1+2t; -1+t)$.\\\\
                            vectơ $\\vec{AH}$ có tọa độ: $\\vec{AH} = (t-%s; 1+2t-%s; -1+t-%s) = (t-1; 2t; t-2)$.\\\\
                            Vì $H$ là hình chiếu nên $\\vec{AH} \\perp \\vec{u} \\Leftrightarrow \\vec{AH} \\cdot \\vec{u} = 0$ hay 
                            $$(t-1) \\cdot 1 + (2t) \\cdot 2 + (t-2) \\cdot 1 = 0 \\Leftrightarrow t - 1 + 4t + t - 2 = 0 \\Leftrightarrow 6t - 3 = 0 \\Leftrightarrow t = \\frac{1}{2}.$$\\\\
                            Do đó, hình chiếu $H$ có tọa độ: $H\\left(%s;%s;%s\\right)$.\\\\
                            Khoảng cách cần tìm là $d(A, \\Delta) = AH$.
                            $$\\vec{AH} = \\left(%s - %s; %s - %s; %s - %s\\right) = %s.$$
                            $$AH = |\\vec{AH}| = \\sqrt{\\left(-\\frac{1}{2}\\right)^2 + 1^2 + \\left(-\\frac{3}{2}\\right)^2} = \\sqrt{\\frac{1}{4} + 1 + \\frac{9}{4}} = \\sqrt{\\frac{14}{4}} = \\frac{\\sqrt{14}}{2} \\approx %s \\text{ (km)}.$$
                            Làm tròn kết quả đến hàng phần mười, ta được $d(A, \\Delta) \\approx %s$.'''
                        %(latex(a),latex(b),latex(c), latex(x0),latex(y0),latex(z0),
                          latex(xA),latex(yA),latex(zA),
                          latex(H_x),latex(H_y),latex(H_z),
                          latex(H_x),latex(xA),latex(H_y),latex(yA),latex(H_z),latex(zA), AH_vectơ,
                          str(Decimal(float(kq_chinh_xac)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','), # 1.87
                          kq_str
                        ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_str))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content    

