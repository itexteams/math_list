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


def bt_dang79_p3_b2_c1_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        params = [
            (2, 36, 3, 18, 2, 1),      # t=3, x=2, y=1
            (2, 288, 6, 72, 4, 2),     # t=6, x=4, y=2
            (3, 96, 4, 36, 3, 1),      # t=4, x=3, y=1
            (1, 16, 2, 12, 1, 1),      # t=2, x=1, y=1
            (1, 128, 4, 48, 2, 2)      # t=4, x=2, y=2
        ]
        val_a, val_K, val_t, min_val, val_x0, val_y0 = random.choice(params)

        coef_t2 = Rational(val_a, val_a + 1)
        two_c = 2 * coef_t2

        number = Decimal(str(min_val))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Biểu thức G(x, y)
        if val_a == 1:
            str_G = 'x^2 + y^2'
            str_cs_left = 'x^2 + y^2'
            str_cs_split = '\\dfrac{x^2}{1} + \\dfrac{y^2}{1}'
            str_cs_denom = '1 + 1'
        else:
            str_G = 'x^2 + %sy^2' % (latex(val_a))
            str_cs_left = 'x^2 + %sy^2' % (latex(val_a))
            str_cs_split = '\\dfrac{x^2}{1} + \\dfrac{y^2}{\\frac{1}{%s}}' % (latex(val_a))
            str_cs_denom = '1 + \\dfrac{1}{%s}' % (latex(val_a))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một doanh nghiệp sản xuất hai loại sản phẩm A và B. Để sản xuất $x$ tấn sản phẩm A và $y$ tấn sản phẩm B ($x > 0, y > 0$), chi phí sản xuất (tính bằng tỷ đồng) được xác định bởi công thức:
    \\[ G(x, y) = %s. \\]
    Ngoài ra, doanh nghiệp phải trả chi phí vận chuyển và lưu kho bảo quản (tính bằng tỷ đồng) tỷ lệ nghịch với tổng khối lượng sản phẩm sản xuất được, cụ thể là $H(x, y) = \\dfrac{%s}{x + y}$. Tổng chi phí vận hành của doanh nghiệp là $T(x, y) = G(x, y) + H(x, y)$ (tỷ đồng). Biết rằng doanh nghiệp luôn muốn tối thiểu hóa tổng chi phí vận hành này. Giá trị nhỏ nhất của tổng chi phí vận hành đó bằng bao nhiêu? (tính bằng tỷ đồng).'''
                         % (str_G, latex(val_K)))

        # Nội dung lời giải bằng khảo sát hàm số và bảng biến thiên
        loigiai = ('''Tổng chi phí vận hành của doanh nghiệp là: \\\\
    $T(x, y) = %s + \\dfrac{%s}{x + y}$. \\\\
    Áp dụng bất đẳng thức Bunhiacopxki (Cauchy-Schwarz) dạng phân thức cho hai số dương $x, y$: \\\\
    $%s = %s \\ge \\dfrac{(x + y)^2}{%s} = %s(x + y)^2$. \\\\
    Dấu bằng xảy ra khi $\\dfrac{x}{1} = \\dfrac{y}{\\frac{1}{%s}} \\Leftrightarrow x = %sy$. \\\\
    Đặt $t = x + y$ ($t > 0$). Khi đó: \\\\
    $T(x, y) \\ge f(t) = %st^2 + \\dfrac{%s}{t}$. \\\\
    Xét hàm số $f(t) = %st^2 + \\dfrac{%s}{t}$ trên khoảng $(0; +\\infty)$. \\\\
    Ta có đạo hàm: \\\\
    $f'(t) = %st - \\dfrac{%s}{t^2} = \\dfrac{%st^3 - %s}{t^2}$. \\\\
    Cho $f'(t) = 0 \\Leftrightarrow %st^3 - %s = 0 \\Leftrightarrow t^3 = %s \\Leftrightarrow t = %s$. \\\\
    Bảng biến thiên của hàm số $f(t)$ trên khoảng $(0; +\\infty)$:
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\tkzTabInit[lgt=1.5,espcl=2.5]{$t$/0.8, $f'(t)$/0.8, $f(t)$/2}{$0$, $%s$, $+\\infty$}
    \\tkzTabLine{d, -, 0, +, }
    \\tkzTabVar{+D+/ $+\\infty$, -/ $%s$, +/ $+\\infty$}
    \\end{tikzpicture}
    \\end{center}
    Từ bảng biến thiên, ta suy ra $\\min_{(0; +\\infty)} f(t) = f(%s) = %s$. \\\\
    Đẳng thức xảy ra khi và chỉ khi: \\\\
    $\\begin{cases} x = %sy \\\\ x + y = %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$ (thỏa mãn $x > 0, y > 0$). \\\\
    Vậy giá trị nhỏ nhất của tổng chi phí vận hành là $%s$ tỷ đồng.'''
                   % (str_G, latex(val_K),
                      str_cs_left, str_cs_split, str_cs_denom, latex(coef_t2),
                      latex(val_a), latex(val_a),
                      latex(coef_t2), latex(val_K),
                      latex(coef_t2), latex(val_K),
                      latex(two_c), latex(val_K), latex(two_c), latex(val_K),
                      latex(two_c), latex(val_K), latex(val_t**3), latex(val_t),
                      latex(val_t),
                      latex(min_val),
                      latex(val_t), latex(min_val),
                      latex(val_a), latex(val_t),
                      latex(val_x0), latex(val_y0),
                      str(kq_str)))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n' +
               '\\end{minipage} \n\n')
    return content

