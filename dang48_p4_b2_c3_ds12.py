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


def bt_dang48_p4_b2_c3_ds12(self):
            # Khai báo biến
            # --- KHAI BÁO BIẾN ---
            x = symbols('x')

            # Tọa độ các điểm để bài toán luôn đẹp (số nguyên)
            # A(-1, yA), B(xB, yA), C(xC, yC)
            xA = -1
            yA = random.randint(1, 2)
            xB = random.randint(1, 3)
            xC = random.randint(5, 7)
            yC = random.randint(-2, 0)

            # Giá trị F(xA) = F_start
            F_start = random.randint(-2, 2)

            # Xác định hàm số f(x) trên từng khoảng
            # Khoảng 1: [-1, xB] -> f(x) = yA
            f1 = yA
            # Khoảng 2: [xB, xC] -> Đường thẳng qua B(xB, yA) và C(xC, yC)
            # Hệ số góc m = (yC - yA) / (xC - xB)
            m = Rational(yC - yA, xC - xB)
            f2 = m * (x - xB) + yA

            # Tìm nguyên hàm F(x)
            # F1 = yA*x + C1. Vì F(xA) = F_start => yA*xA + C1 = F_start
            C1 = F_start - yA * xA
            F1 = yA * x + C1

            # F2 = nguyên hàm f2 + C2. 
            # Tính liên tục tại xB: F1(xB) = F2(xB)
            F2_temp = sp.integrate(f2, x)
            C2 = F1.subs(x, xB) - F2_temp.subs(x, xB)
            F2 = F2_temp + C2

            # Tính giá trị cần tìm: F(x1) + F(x2)
            # Ở đây ta chọn x1 = điểm giữa xB và xC, x2 = xC (giống đề mẫu 4 và 6)
            x1 = xB + 2
            x2 = xC
            val_F_x1 = F2.subs(x, x1)
            val_F_x2 = F2.subs(x, x2)
            kq_dung = val_F_x1 + val_F_x2

            # --- TẠO CÁC ĐÁP ÁN ---
            da_dung = '$%s$' % latex(kq_dung)
            # Tạo các đáp án nhiễu
            s = []
            for i in [-2, -1, 1, 2, 3]:
                sai = kq_dung + i
                if sai != kq_dung:
                    s.append('$%s$' % latex(sai))

            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # --- VẼ HÌNH TIKZ ---
            tikz_code = r'''\begin{center}
            \begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \draw[->] (%(xmin)s,0) -- (%(xmax)s,0) node[below] {$x$};
                \draw[->] (0,%(ymin)s) -- (0,%(ymax)s) node[left] {$y$};
                \draw[dotted] (%(xA)s,0) node[below]{$%(xA)s$} -- (%(xA)s,%(yA)s) node[above left]{$A$} -- (0,%(yA)s) node[left]{$%(yA)s$};
                \draw[dotted] (%(xB)s,0) node[below]{$%(xB)s$} -- (%(xB)s,%(yA)s) node[above]{$B$};
                \draw[dotted] (%(xC)s,0) node[above]{$%(xC)s$} -- (%(xC)s,%(yC)s) node[below right]{$C$} -- (0,%(yC)s) node[left]{$%(yC)s$};
                \draw[thick, blue] (%(xA)s,%(yA)s) -- (%(xB)s,%(yA)s) -- (%(xC)s,%(yC)s);
                \node[below left] at (0,0) {$O$};
            \end{tikzpicture}
            \end{center}''' % {
                'xA': xA, 'xB': xB, 'xC': xC, 'yA': yA, 'yC': yC,
                'xmin': xA - 1, 'xmax': xC + 1, 'ymin': min(yC, 0) - 1, 'ymax': yA + 1
            }

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (r'''Cho hàm số $y = f(x)$ liên tục trên $[%s; %s]$ và có đồ thị đường gấp khúc $ABC$ như hình bên.
            Biết $F$ là một nguyên hàm của $f$ thỏa mãn $F(%s) = %s$. Tính $F(%s) + F(%s)$.
            ''' % (latex(xA), latex(xC), latex(xA), latex(F_start), latex(x1), latex(x2)) 
            + tikz_code)

            # --- NỘI DUNG LỜI GIẢI ---
            loigiai = (r'''Dựa vào đồ thị ta có hàm số $f(x) = \begin{cases} %s & \text{khi } %s \le x \le %s \\ %s & \text{khi } %s < x \le %s \end{cases}$. \\
            Nguyên hàm $F(x)$ có dạng: $F(x) = \begin{cases} %s + C_1 & \text{khi } %s \le x \le %s \\ %s + C_2 & \text{khi } %s < x \le %s \end{cases}$. \\
            Vì $F(%s) = %s \Rightarrow %s + C_1 = %s \Rightarrow C_1 = %s$. \\
            Do $F(x)$ liên tục tại $x = %s$, ta có: \\
            $\lim_{x \to %s^-} F(x) = F(%s) = %s$. \\
            $\lim_{x \to %s^+} F(x) = %s + C_2$. \\
            $\Rightarrow %s + C_2 = %s \Rightarrow C_2 = %s$. \\
            Khi đó: \\
            $F(%s) = %s$. \\
            $F(%s) = %s$. \\
            Vậy $F(%s) + F(%s) = %s + %s = %s$.'''
            % (latex(f1), latex(xA), latex(xB), latex(f2), latex(xB), latex(xC),
               latex(sp.integrate(f1, x)), latex(xA), latex(xB), latex(F2_temp), latex(xB), latex(xC),
               latex(xA), latex(F_start), latex(f1*xA), latex(F_start), latex(C1),
               latex(xB), latex(xB), latex(xB), latex(F1.subs(x, xB)),
               latex(xB), latex(F2_temp.subs(x, xB)),
               latex(F2_temp.subs(x, xB)), latex(F1.subs(x, xB)), latex(C2),
               latex(x1), latex(val_F_x1),
               latex(x2), latex(val_F_x2),
               latex(x1), latex(x2), latex(val_F_x1), latex(val_F_x2), latex(kq_dung)
            ))

            # --- XUẤT CÂU TRẮC NGHIỆM ---
            list_1 = ['\\True ' + da_dung, das1, das2, das3]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

