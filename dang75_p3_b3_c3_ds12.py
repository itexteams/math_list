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


def bt_dang75_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Các bộ tham số (a^2, b^2, R, x_0) được lựa chọn để hoành độ giao điểm x_0 nguyên và R > b
            params = [
                (256, 48, 10, 8),    # Bài toán gốc trong ảnh
                (648, 72, 12, 9),
                (288, 50, 13, 12),
                (64, 12, 5, 4),
                (324, 72, 10, 6)
            ]

            # Random bài toán
            a2, b2, R, x0 = random.choice(params)

            R2 = R**2
            x02 = x0**2

            # Tính toán các giá trị cho lời giải bằng Sympy
            x = sp.Symbol('x')
            C_val = R2 - b2
            D_frac = sp.Rational(a2 - b2, a2)
            int_x2 = sp.Rational(1, 3) * (x0**3)
            term2 = D_frac * int_x2
            term1 = C_val * x0
            val_int = term1 - term2

            V_exact = 2 * sp.pi * val_int
            V_float = float(V_exact.evalf())
            V_round = int(Decimal(str(V_float)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

            # Các đáp án trắc nghiệm
            du = ['$%s$' % (V_round)]
            da = du[0]

            s = [
                '$%s$' % (V_round + 1),
                '$%s$' % (V_round + 2),
                '$%s$' % (V_round - 1),
                '$%s$' % (V_round - 2),
                '$%s$' % (V_round + 10),
                '$%s$' % (V_round - 10),
            ]

            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)

            # Tham số cho TikZ
            a_val = math.sqrt(a2)
            b_val = math.sqrt(b2)
            y0 = math.sqrt(R2 - x0**2)
            ang_c = math.degrees(math.acos(x0/R))
            ang_e = math.degrees(math.acos(x0/a_val))

            # Hình vẽ TikZ
            tikz_str = ('''\\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.3, line width=1pt]
            \\fill[yellow!50] (%s,%s) arc (%s:%s:%s) arc (%s:%s:%s and %s);
            \\draw[->] (-%s,0) -- (%s,0) node[below] {$x$};
            \\draw[->] (0,-2) -- (0,%s) node[left] {$y$};
            \\node[below left] at (0,0) {$O$};
            \\draw (-%s,0) arc (180:0:%s and %s);
            \\draw (%s,0) arc (0:180:%s);
            \\node[below] at (%s,0) {$%s$};
            \\node[below] at (-%s,0) {$-%s$};
            \\node[below] at (%s,0) {$%s$};
            \\node[below] at (-%s,0) {$-%s$};
            \\node at (0, %s) {$(H)$};
            \\end{tikzpicture}
            \\end{center}''' % (
                x0, round(y0, 2), round(ang_c, 2), round(180-ang_c, 2), R, round(180-ang_e, 2), round(ang_e, 2), round(a_val, 1), round(b_val, 2),
                round(a_val+2, 1), round(a_val+2, 1), round(R+2, 1),
                round(a_val, 1), round(a_val, 1), round(b_val, 2),
                R, R,
                R, R, R, R,
                round(a_val, 1), round(a_val, 1), round(a_val, 1), round(a_val, 1),
                round(y0+1.5, 1)
            ))

            # Câu hỏi
            noidungcauhoi = ('''Người ta cần tính thể tích của một vật thể được chế tác như sau. Trên mặt phẳng với hệ tọa độ $Oxy$ (một đơn vị độ dài trên mỗi trục tương ứng với một xăng-ti-mét trong thực tế), gọi $(H)$ là hình phẳng được tô đậm, giới hạn bởi đường elip $\\frac{x^2}{%s} + \\frac{y^2}{%s} = 1$ và đường tròn tâm $O$ có bán kính $%s$ (xem hình minh họa bên dưới). Vật thể có dạng khối tròn xoay được tạo thành khi quay hình phẳng $(H)$ quanh trục hoành. Thể tích của vật thể nói trên bằng bao nhiêu xăng-ti-mét khối (không làm tròn kết quả các phép tính trung gian, chỉ làm tròn kết quả phép tính cuối cùng đến hàng đơn vị)?\n%s'''
                             % (a2, b2, R, tikz_str))

            # Các đáp án
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ('''Phương trình đường tròn là $x^2 + y^2 = %s \\Rightarrow y^2 = %s - x^2$.\\\\
            Phương trình elip là $\\frac{x^2}{%s} + \\frac{y^2}{%s} = 1 \\Rightarrow y^2 = %s \\left( 1 - \\frac{x^2}{%s} \\right) = %s - %s x^2$.\\\\
            Hoành độ giao điểm của elip và đường tròn là nghiệm của phương trình:\\\\
            $ %s - x^2 = %s - %s x^2 \\Leftrightarrow %s x^2 = %s \\Leftrightarrow x^2 = %s \\Leftrightarrow x = \\pm %s. $\\\\
            Hình phẳng $(H)$ được giới hạn bởi nửa trên đường tròn và nửa trên elip trong khoảng $x \\in [-%s; %s]$.\\\\
            Thể tích khối tròn xoay tạo thành khi quay $(H)$ quanh trục hoành là:\\\\
            $ V = \\pi \\int_{-%s}^{%s} \\left[ \\left( %s - x^2 \\right) - \\left( %s - %s x^2 \\right) \\right] \\text{d}x $\\\\
            $ = \\pi \\int_{-%s}^{%s} \\left( %s - %s x^2 \\right) \\text{d}x = 2\\pi \\int_{0}^{%s} \\left( %s - %s x^2 \\right) \\text{d}x $\\\\
            $ = 2\\pi \\left( %s x - %s x^3 \\right) \\bigg|_{0}^{%s} = 2\\pi \\left( %s \\cdot %s - %s \\cdot %s \\right) $\\\\
            $ = 2\\pi \\left( %s - %s \\right) = 2\\pi \\cdot %s = %s \\pi \\approx %s \\text{ (cm}^3\\text{)}. $\\\\
            Làm tròn đến hàng đơn vị, ta được $%s$ cm$^3$.'''
                       % (R2, R2,
                          a2, b2, b2, a2, b2, sp.latex(sp.Rational(b2, a2)),
                          R2, b2, sp.latex(sp.Rational(b2, a2)), sp.latex(D_frac), C_val, x02, x0,
                          x0, x0,
                          x0, x0, R2, b2, sp.latex(sp.Rational(b2, a2)),
                          x0, x0, C_val, sp.latex(D_frac), x0, C_val, sp.latex(D_frac),
                          C_val, sp.latex(D_frac * sp.Rational(1, 3)), x0, C_val, x0, sp.latex(D_frac * sp.Rational(1, 3)), x0**3,
                          term1, sp.latex(term2), sp.latex(val_int), sp.latex(val_int * 2), str(round(V_float, 2)).replace('.', ','),
                          V_round))
            dapan='\\shortans[0]{$%s$}\n'%(latex(V_round))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex} \n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex} \n \\end{minipage} \n\n').replace('.0$','$')
            return content

