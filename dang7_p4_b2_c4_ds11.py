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


def bt_dang7_p4_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            a_sym = symbols('a')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Random điểm giới hạn x0 (tránh số 0 để không lỗi phép chia khi tìm a)
                x0 = random.randint(-3, 4)
                if x0 == 0: x0 = 5 

                # 2. Tạo hàm không chứa tham số a (f_fixed = m*x^2 + n*x + p)
                m = random.randint(1, 2)
                n = random.randint(-3, 3)
                p = random.randint(-2, 5)
                f_fixed = m*x**2 + n*x + p
                val_fixed = f_fixed.subs(x, x0)

                # 3. Tạo hàm chứa tham số a (f_var = q*x^2 + a*x + k)
                q = random.randint(1, 2)
                k = random.randint(-3, 3)

                # Giải phương trình: q*x0^2 + a*x0 + k = val_fixed để tìm a
                # a*x0 = val_fixed - q*x0^2 - k
                tu_so = val_fixed - q*x0**2 - k
                a_val = Rational(tu_so, x0)

                # 4. Ngẫu nhiên vị trí của nhánh chứa a (nhánh trên hoặc nhánh dưới)
                is_a_on_top = random.choice([True, False])

                if is_a_on_top:
                    f_tren = q*x**2 + a_sym*x + k
                    f_duoi = f_fixed
                    lim_phai_tex = latex(q*x0**2 + a_sym*x0 + k)
                    lim_trai_tex = latex(val_fixed)
                else:
                    f_tren = f_fixed
                    f_duoi = q*x**2 + a_sym*x + k
                    lim_phai_tex = latex(val_fixed)
                    lim_trai_tex = latex(q*x0**2 + a_sym*x0 + k)

                # --- Câu hỏi ---
                noidungcauhoi = (r'''Tính giá trị của $a$ để hàm số $f(x) = \begin{cases} %s & \text{khi } x > %s \\ %s & \text{khi } x \le %s \end{cases}$ có giới hạn tại $x = %s$.''' 
                                 % (latex(f_tren), latex(x0), latex(f_duoi), latex(x0), latex(x0)))

                # --- Các đáp án ---
                da_d = r'\True $a = %s$' % (latex(a_val))
                # Tạo các đáp án sai ngẫu nhiên
                s1 = r'$a = %s$' % (latex(a_val + 1))
                s2 = r'$a = %s$' % (latex(a_val - 1))
                s3 = r'$a = %s$' % (latex(a_val + 2))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, s1, s2, s3]
                random.shuffle(list_1)

                # --- Nội dung lời giải ---
                loigiai = (r'''TXĐ: $D = \mathbb{R}$. \\
                           Xét: $\lim_{x \to %s^+} f(x) = \lim_{x \to %s^+} (%s) = %s$. \\
                           $\lim_{x \to %s^-} f(x) = \lim_{x \to %s^-} (%s) = %s$. \\
                           Hàm số $y = f(x)$ có giới hạn tại $x = %s$ khi và chỉ khi \\
                           $\lim_{x \to %s^+} f(x) = \lim_{x \to %s^-} f(x) \Leftrightarrow %s = %s \Leftrightarrow a = %s$.''' 
                           % (latex(x0), latex(x0), latex(f_tren), lim_phai_tex,
                              latex(x0), latex(x0), latex(f_duoi), lim_trai_tex,
                              latex(x0), latex(x0), latex(x0), lim_phai_tex, lim_trai_tex, latex(a_val)))

            # Xuất câu trắc nghiệm theo định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content       

