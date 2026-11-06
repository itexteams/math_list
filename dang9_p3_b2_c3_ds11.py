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


def bt_dang9_p3_b2_c3_ds11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        x_val = random.choice([10, 12, 14, 16, 18, 20, 22, 24])
        n1 = 10
        n3 = 20
        n4 = 10

        n_total = n1 + x_val + n3 + n4  # 40 + x_val
        half_n = Rational(n_total, 2)

        # Me = 30 + (n/2 - (n1 + x)) / n3 * 10
        # = 30 + ((40 + x)/2 - (10 + x)) / 20 * 10 = 30 + (20 - x/2) / 2 = 40 - x/4
        me_val = 30 + Rational(half_n - (n1 + x_val), n3) * 10

        # Định dạng số trung vị
        me_dec = Decimal(str(float(me_val))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        me_str = str(me_dec).replace('.', ',')

        quarter_n = Rational(n_total, 4)
        q1_val = 20 + Rational(quarter_n - n1, x_val) * 10
        # Chú ý: (n/4 - 10)/x * 10 = (x/4)/x * 10 = 2.5 => Q1 = 22.5 luôn là hằng số đẹp!

        number = Decimal(str(float(q1_val)))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Để nghiên cứu thói quen tự học trực tuyến của học sinh chuyên, một trường THPT tiến hành khảo sát thời gian sử dụng máy tính để học bài mỗi ngày (tính bằng phút) của một nhóm học sinh và thu được bảng tần số ghép nhóm sau:
    \\begin{center}
    \\begin{tabular}{|c|c|c|c|c|}
    \\hline
    \\textbf{Thời gian (phút)} & $[10;20)$ & $[20;30)$ & $[30;40)$ & $[40;50)$ \\\\ \\hline
    \\textbf{Số học sinh} & $%s$ & $x$ & $%s$ & $%s$ \\\\ \\hline
    \\end{tabular}
    \\end{center}
    Biết trung vị của mẫu số liệu ghép nhóm này bằng $%s$ phút. Tứ phân vị thứ nhất $Q_1$ của mẫu số liệu đó bằng bao nhiêu?'''
                         % (latex(n1), latex(n3), latex(n4), me_str))

        # Nội dung lời giải
        loigiai = ('''Cỡ mẫu của mẫu số liệu ghép nhóm là: \\\\
    $n = %s + x + %s + %s = %s + x$. \\\\
    Vì trung vị $M_e = %s \\in [30;40)$ nên nhóm chứa trung vị là $[30;40)$. \\\\
    Ta có công thức tính trung vị: \\\\
    $M_e = 30 + \\dfrac{\\dfrac{n}{2} - (%s + x)}{%s} \\cdot 10 = 30 + \\dfrac{\\dfrac{%s + x}{2} - %s - x}{2} = 30 + \\dfrac{%s - x}{4}$. \\\\
    Theo giả thiết: \\\\
    $30 + \\dfrac{%s - x}{4} = %s \\Leftrightarrow \\dfrac{%s - x}{4} = %s \\Leftrightarrow %s - x = %s \\Leftrightarrow x = %s$. \\\\
    Với $x = %s$, cỡ mẫu là $n = %s + %s = %s$. \\\\
    Ta có $\\dfrac{n}{4} = \\dfrac{%s}{4} = %s$. \\\\
    Vì $%s < %s \\le %s + %s = %s$ nên nhóm chứa tứ phân vị thứ nhất $Q_1$ là $[20;30)$. \\\\
    Áp dụng công thức tính tứ phân vị thứ nhất: \\\\
    $Q_1 = 20 + \\dfrac{\\dfrac{n}{4} - %s}{x} \\cdot (30 - 20) = 20 + \\dfrac{%s - %s}{%s} \\cdot 10 = %s$. \\\\
    Vậy tứ phân vị thứ nhất của mẫu số liệu là $Q_1 = %s$.'''
                   % (latex(n1), latex(n3), latex(n4), latex(n1 + n3 + n4),
                      me_str,
                      latex(n1), latex(n3),
                      latex(n1 + n3 + n4), latex(n1),
                      latex(n3 + n4 - n1),
                      latex(n3 + n4 - n1), me_str,
                      latex(n3 + n4 - n1), str(me_dec - 30).replace('.', ','),
                      latex(n3 + n4 - n1), str((me_dec - 30) * 4).replace('.', ','),
                      latex(x_val),
                      latex(x_val), latex(n1 + n3 + n4), latex(x_val), latex(n_total),
                      latex(n_total), str(Decimal(str(float(quarter_n))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                      latex(n1), str(Decimal(str(float(quarter_n))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                      latex(n1), latex(x_val), latex(n1 + x_val),
                      latex(n1),
                      str(Decimal(str(float(quarter_n))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                      latex(n1), latex(x_val),
                      kq_str,
                      kq_str))

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

