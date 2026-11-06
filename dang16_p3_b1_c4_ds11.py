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


def bt_dang16_p3_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến danh sách dạng (chỉ có 1 dạng bài này)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':

                a = randint(1, 5) 
                b = randint(2, 9) # Hệ số của n
                c = randint(1, 20) # Hệ số tự do

                kq_fraction = Rational(1, 3 * a)
                h1=kq_fraction
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq1=str(kq).replace('.', ',')

                # Tạo các bước giải chi tiết cho LaTeX
                # Bước phân tích mẫu số trong giới hạn: a + b/n^2 + c/n^3
                mau_so_limit_str = f"{a} + \\frac{{{b}}}{{n^2}} + \\frac{{{c}}}{{n^3}}"
                if a == 1: # Nếu a=1 thì không cần viết số 1, nhưng trong biểu thức 1 + ... thì cần
                    mau_so_limit_str = f"1 + \\frac{{{b}}}{{n^2}} + \\frac{{{c}}}{{n^3}}"

                # --- TẠO CÁC ĐÁP ÁN NHIỄU (DISTRACTORS) ---
                # Tạo danh sách các đáp án sai dựa trên các lỗi sai thường gặp
                wrong_1 = Rational(1, a)       # Sai vì quên chia 3
                wrong_2 = Rational(1, 6 * a)   # Sai vì tính nhầm hệ số
                wrong_3 = Rational(2, 3 * a)   # Sai ngẫu nhiên
                wrong_4 = Rational(a, 3)       # Nghịch đảo

                # Đảm bảo các đáp án sai không trùng với đáp án đúng
                set_answers = {kq_fraction}
                list_wrong = []

                for w in [wrong_1, wrong_2, wrong_3, wrong_4, 0]:
                    if w not in set_answers and w > 0:
                        set_answers.add(w)
                        list_wrong.append(w)
                        if len(list_wrong) >= 3:
                            break

                # Định dạng LaTeX cho các đáp án
                da = '$%s$' % latex(kq_fraction)
                s = ['$%s$' % latex(w) for w in list_wrong]

                # Chọn ngẫu nhiên vị trí đáp án
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- NỘI DUNG CÂU HỎI ---
                # Xây dựng đa thức mẫu số để hiển thị
                # Nếu a=1 thì viết n^3, ngược lại viết an^3
                poly_mau = f"{'' if a==1 else a}n^3 + {b}n + {c}"

                noidungcauhoi = (
                    'Giới hạn $\\lim_{n\\to+\\infty} \\dfrac{1^2 + 2^2 + 3^2 + 4^2 + ... + n^2}{%s}$ có giá trị bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).' 
                    % poly_mau
                )

                # --- NỘI DUNG LỜI GIẢI ---
                loigiai = (
                    'Ta có kết quả quen thuộc $1^2 + 2^2 + 3^2 + ... + n^2 = \\dfrac{n(n+1)(2n+1)}{6}$. \\\\\n'
                    'Do đó: \n'
                    '$$\\begin{aligned}'
                    '\\lim_{n\\to+\\infty} \\dfrac{1^2 + ... + n^2}{%s} &= \\lim_{n\\to+\\infty} \\dfrac{n(n+1)(2n+1)}{6(%s)} \\\\'
                    '&= \\lim_{n\\to+\\infty} \\dfrac{\\left(1+\\frac{1}{n}\\right)\\left(2+\\frac{1}{n}\\right)}{6\\left(%s\\right)} \\\\'
                    '&= \\dfrac{1.2}{6.%s} = %s \\approx %s.'
                    '\\end{aligned}$$'
                    % (poly_mau, poly_mau, mau_so_limit_str, a, latex(kq_fraction),str(kq1))
                )

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kq1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

