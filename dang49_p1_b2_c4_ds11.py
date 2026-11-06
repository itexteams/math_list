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


def bt_dang49_p1_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3- Tư duy Random
            # Chọn a là số chẵn để đảm bảo các số b, c là số nguyên đẹp
            list_a = [4, 6, 8]  
            a = random.choice(list_a)
            c = int((a**2 - 2) / 2)
            b = Rational(c**2 - 1, a**2) # Dùng Rational để tránh sai số dấu phẩy động
            # Nghiệm còn lại của tử thức (x-k), chọn k khác 1
            k = random.randint(2, 5) 

            # Biểu thức
            tu = (x - 1) * (x - k)
            mau = a * sqrt(x + b) - (x + c)
            f = tu / mau

            # Tính toán các thành phần cho lời giải
            lien_hop = a * sqrt(x + b) + (x + c)

            # Tính giới hạn
            kq_limit = limit(f, x, 1, dir='+')
            if kq_limit == S.Infinity:
                kq_tex = "+\\infty"
            elif kq_limit == S.NegativeInfinity:
                kq_tex = "-\\infty"
            else:
                kq_tex = latex(kq_limit)

            # --- Phần xuất nội dung theo mẫu ---

            # Câu hỏi
            noidungcauhoi = (r'''Giá trị của giới hạn $\displaystyle \lim_{x \to 1^+} \frac{%s}{%s}$ bằng''' 
                            %(latex(tu), latex(mau)))

            # Đáp án
            da_d = r'\True $%s$' % kq_tex
            # Danh sách các đáp án nhiễu tiềm năng
            list_ans_pool = ['$-\\infty$', '$+\\infty$', '$0$', '$1$', '$-1$', '$2$']

            # Loại bỏ đáp án đúng ra khỏi danh sách nhiễu để không bị trùng
            clean_ans_pool = [ans for ans in list_ans_pool if kq_tex not in ans]
            da_s = random.sample(clean_ans_pool, 3)

            # Gộp lại và xáo trộn (Dùng list_final thống nhất)
            list_final = [da_d] + da_s
            random.shuffle(list_final)

            # Lời giải chi tiết
            # Tính toán giá trị tử số sau khi khử dạng vô định để đưa vào lời giải
            tu_so_rut_gon = (1 - k) * (2 * (1 + c))

            loigiai = (r'''Ta có:
            $$\lim_{x \to 1^+} \frac{%s}{%s} = \lim_{x \to 1^+} \frac{(x-1)(x-%s)(%s)}{-(x-1)^2} = \lim_{x \to 1^+} \frac{(x-%s)(%s)}{-(x-1)}$$
            Ta có $\displaystyle \lim_{x \to 1^+} (x-%s)(%s) = %s$. \\
            Và $\displaystyle \lim_{x \to 1^+} [-(x-1)] = 0$ và $-(x-1) < 0$ với mọi $x > 1$. \\
            Vậy giới hạn đã cho bằng $%s$.''' 
                      %(latex(tu), latex(mau), k, latex(lien_hop), k, latex(lien_hop), 
                        k, latex(lien_hop), tu_so_rut_gon, kq_tex))

            # Xuất kết quả theo format mẫu (Sửa list_1 thành list_final)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_final[0])+'}\n'
                '{'+str(list_final[1])+'}\n'
                '{'+str(list_final[2])+'}\n'
                '{'+str(list_final[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

