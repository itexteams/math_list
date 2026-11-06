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


def bt_dang18_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1 & 3: Thiết lập các bộ số ngẫu nhiên (m: AB, n: AD, p: SA^2)
                # Chọn bộ số để kết quả gọn đẹp
                sets = [
                    {'m': 2, 'n': 1, 'p': 3}, # Bài gốc: AB=2a, AD=a, SA=a*sqrt(3) -> cos = sqrt(10)/4
                    {'m': 1, 'n': 1, 'p': 2}, # AB=a, AD=a, SA=a*sqrt(2) -> cos = sqrt(2)/2
                    {'m': 3, 'n': 4, 'p': 11},# AB=3a, AD=4a, SA=a*sqrt(11) -> cos = 5/6
                    {'m': 2, 'n': 2, 'p': 1}, # AB=2a, AD=2a, SA=a -> cos = 2*sqrt(2)/3
                    {'m': 1, 'n': 2, 'p': 5}  # AB=a, AD=2a, SA=a*sqrt(5) -> cos = sqrt(2)/2
                ]
                data = random.choice(sets)
                m, n, p = data['m'], data['n'], data['p']

                # Khai báo ký hiệu
                a = symbols('a')

                # Tính toán các cạnh
                AB = m*a
                AD = n*a
                SA = sqrt(p)*a

                AC_sq = m**2 + n**2
                AC = sqrt(AC_sq)*a

                SC_sq = AC_sq + p
                SC = sqrt(SC_sq)*a

                # Cosin(SCA) = AC / SC
                cos_val = sqrt(AC_sq) / sqrt(SC_sq)

                # Chuyển sang tex
                AB_tex = latex(m) + 'a' if m != 1 else 'a'
                AD_tex = latex(n) + 'a' if n != 1 else 'a'
                SA_tex = 'a\\sqrt{' + str(p) + '}' if p != 1 else 'a'
                AC_tex = latex(sqrt(AC_sq)) + 'a'
                SC_tex = latex(sqrt(SC_sq)) + 'a'
                kq_tex = latex(cos_val).replace('.', ',')

                # Bước 4: Tạo các phương án sai không trùng đáp án đúng
                du = ['$%s$' % (kq_tex)]
                da = random.choice(du)

                # Danh sách phương án sai dựa trên các sai lầm phổ biến (nhầm Sin, nhầm cạnh)
                s = [
                    '$%s$' % (latex(sqrt(p)/sqrt(SC_sq))).replace('.', ','), # Sin thay vì Cos
                    '$%s$' % (latex(sqrt(p)/sqrt(AC_sq))).replace('.', ','), # Tan thay vì Cos
                    '$%s$' % (latex(Rational(1, 2))).replace('.', ','),
                    '$%s$' % (latex(sqrt(2)/2)).replace('.', ','),
                    '$%s$' % (latex(sqrt(3)/2)).replace('.', ','),
                    '$%s$' % (latex(sqrt(6)/4)).replace('.', ',')
                ]

                # Lọc bỏ nếu trùng đáp án đúng
                s = [item for item in s if item != da]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Dựng hình TikZ
                hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[line cap=round,line join=round,scale=0.7, line width=1pt]
            \\coordinate (A) at (0,3);
            \\coordinate (B) at (-1.5,0.5);
            \\coordinate (C) at (2.5,0.5);
            \\coordinate (D) at (4,3);
            \\coordinate (S) at (0,6.5);
            \\draw [dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C);
            \\draw (S)--(B)--(C)--(D)--cycle (S)--(C);
            \\draw (0,3.3)--(0.3,3.3)--(0.3,3);
            \\draw (A) node[left] {$A$} (B) node[below left] {$B$} (C) node[below right] {$C$} (D) node[right] {$D$} (S) node[above] {$S$};
            \\end{tikzpicture}
            \\end{center}''')

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật, $AB = %s$, $AD = %s$. Cạnh bên $SA$ vuông góc với mặt phẳng đáy và $SA = %s$. Cosin của góc giữa đường thẳng $SC$ và mặt phẳng đáy bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 % ( AB_tex, AD_tex, SA_tex))

                # Đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)
                h1=cos_val
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.', ',')
                # Bước 2: Nội dung lời giải chi tiết
                loigiai = ('''%s Hình chiếu vuông góc của đường thẳng $SC$ lên mặt phẳng $\\left( ABCD \\right)$ là đường thẳng $AC$. \\\\
                             Do đó $\\left( SC, \\left( ABCD \\right) \\right) = \\widehat{SCA}$. \\\\
                             Xét tam giác $ABC$ vuông tại $B$, ta có $AC = \\sqrt{AB^2 + BC^2} = \\sqrt{\\left( %s \\right)^2 + \\left( %s \\right)^2} = %s$. \\\\
                             Vì $SA \\perp \\left( ABCD \\right)$ nên $SA \\perp AC$, suy ra tam giác $SAC$ vuông tại $A$. \\\\
                             Ta có $SC = \\sqrt{SA^2 + AC^2} = \\sqrt{\\left( %s \\right)^2 + \\left( %s \\right)^2} = %s$. \\\\
                             Trong tam giác vuông $SAC$, ta có $\\cos \\widehat{SCA} = \\frac{AC}{SC} = \\frac{%s}{%s} = %s \\approx %s$.'''
                           % (hinh_ve, AB_tex, AD_tex, AC_tex, SA_tex, AC_tex, SC_tex, AC_tex, SC_tex, kq_tex, kqz))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

