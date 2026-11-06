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


def bt_dang15_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B1: Random các thông số cho hàm số y = ax^2 + bx + c
                # Ở đây ảnh mẫu là y = x^2 - 3mx + m^2 + 1 với m = 1
                # Ta sẽ random m và một vài biến thể để bài toán phong phú
                m_val = random.randint(1, 5)

                # Hàm số cụ thể khi đã thay m: y = x^2 - (3*m)x + (m^2 + 1)
                # y = ax^2 + bx + c
                a = 1
                b = -3 * m_val
                c = m_val**2 + 1

                x_sym = symbols('x')
                f_x = a*x_sym**2 + b*x_sym + c

                # B2: Tính toán các thông số kỹ thuật
                # Hoành độ đỉnh x_I = -b / 2a
                x_I = Rational(-b, 2*a)
                # Tung độ đỉnh y_I
                y_I = f_x.subs(x_sym, x_I)

                # Khoảng đồng biến của hàm số bậc hai (a > 0) là (x_I; +oo)
                kq_dung = '(%s; +\\infty)' % (latex(x_I))

                # B3: Tạo các phương án sai (không trùng đáp án đúng)
                s = [
                    '(-\\infty; %s)' % (latex(x_I)),
                    '(%s; +\\infty)' % (latex(-x_I)),
                    '(-\\infty; %s)' % (latex(-x_I)),
                    '(%s; +\\infty)' % (latex(x_I + 1)),
                    '(%s; +\\infty)' % (latex(x_I - 1)),
                    '(%s; +\\infty)' % (latex(Rational(b, 2*a)))
                ]
                # Lọc bỏ phương án nếu lỡ trùng với đáp án đúng
                s = [i for i in s if i != kq_dung]

                list_sai = random.sample(s, 3)
                da_d = '\\True $' + kq_dung + '$'
                da_s1 = '$' + list_sai[0] + '$'
                da_s2 = '$' + list_sai[1] + '$'
                da_s3 = '$' + list_sai[2] + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # B4: Soạn nội dung câu hỏi
                noidungcauhoi = (r'''Cho hàm số $y = x^2 - 3mx + m^2 + 1$ (1), $m$ là tham số. Khi $m = %s$ tìm khoảng đồng biến của hàm số.'''
                                 % (latex(m_val)))

                # B5: Tạo mã TikZ cho bảng biến thiên
                # Tính toán hướng mũi tên: a > 0 nên giảm rồi tăng
                tikz_bbt = r''' \begin{center}
            \begin{tikzpicture}
                \tkzTabInit[lgt=1.2,espcl=2.5]{$x$/1, $y$/2}{$-\infty$, $%s$, $+\infty$}
                \tkzTabVar{+/ $+\infty$, -/ $%s$, +/ $+\infty$}
            \end{tikzpicture}
            \end{center}''' % (latex(x_I), latex(y_I))

                # B6: Soạn lời giải
                loigiai = (r'''Khi $m = %s$, hàm số trở thành $y = %s$. \\
                            Tập xác định: $D = \mathbb{R}$. \\
                            Đỉnh $I\left( %s ; %s \right)$. \\
                            Bảng biến thiên: 
                            %s
                            Dựa vào bảng biến thiên, hàm số đồng biến trên khoảng $\left( %s; +\infty \right)$.'''
                           % (latex(m_val), latex(f_x), latex(x_I), latex(y_I), tikz_bbt, latex(x_I)))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n' +
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

