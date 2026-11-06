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


def bt_dang5_p2_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            n = symbols('n')

            # 1. TẠO THÔNG SỐ NGẪU NHIÊN
            # u_n = (a1*n^2 + b1*n + c1) / (d1*n^2 + e1*n + f1)
            a1 = random.randint(1, 5)
            d1 = random.randint(2, 6) * a1 # Để rút gọn ra phân số đẹp
            b1 = random.randint(-5, 5)
            c1 = random.randint(1, 10)
            e1 = random.randint(1, 5)
            f1 = random.randint(1, 5)

            # v_n = sqrt(a2*n^2 + c2) / (d2*n)
            # Chọn a2 là số chính phương để khai căn đẹp
            list_cp = [4, 9, 16, 25]
            a2 = random.choice(list_cp)
            d2 = random.randint(2, 8)
            c2 = random.randint(1, 10)

            # Định nghĩa biểu thức
            u_n_expr = (a1*n**2 + b1*n + c1) / (d1*n**2 + e1*n + f1)
            v_n_expr = sqrt(a2*n**2 + c2) / (d2*n)

            # Tính các giới hạn thực tế
            L_u = Rational(a1, d1)
            L_v = Rational(int(sqrt(a2)), d2)

            # Nội dung câu hỏi gốc
            noidungcauhoi = (r"Cho hai dãy số $(u_n)$ và $(v_n)$ với $u_n = %s, v_n = %s$." 
                             % (latex(u_n_expr), latex(v_n_expr)))

            ########################################################################
            # NHẬN BIẾT: Giới hạn u_n
            ########################################################################
            L_u_sai = L_u + random.choice([Rational(1, 2), 1])
            nb_da_1_d = r'\True $\lim_{n \to +\infty} u_n = %s$' % (latex(L_u))
            nb_da_1_s = r'$\lim_{n \to +\infty} u_n = %s$' % (latex(L_u_sai))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r"Ta có $\lim_{n \to +\infty} u_n = \lim_{n \to +\infty} \frac{%s n^2 %s n + %s}{%s n^2 + %s n + %s} = \frac{%s}{%s} = %s$." 
                            % (a1, '+'+str(b1) if b1>=0 else b1, c1, d1, e1, f1, a1, d1, latex(L_u)))

            ########################################################################
            # THÔNG HIỂU: Giới hạn v_n
            ########################################################################
            L_v_sai = Rational(a2, d2) # Quên khai căn
            th_da_1_d = r'\True $\lim_{n \to +\infty} v_n = %s \Rightarrow \lim_{n \to +\infty} \left( v_n - %s \right) = 0$' % (latex(L_v), latex(L_v))
            th_da_1_s = r'$\lim_{n \to +\infty} v_n = %s \Rightarrow \lim_{n \to +\infty} \left( v_n - %s \right) = 0$' % (latex(L_v_sai), latex(L_v_sai))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r"Ta có $\lim_{n \to +\infty} v_n = \lim_{n \to +\infty} \frac{\sqrt{%s n^2 + %s}}{%s n} = \frac{\sqrt{%s}}{%s} = %s$. Suy ra $\lim_{n \to +\infty} \left(v_n - %s\right) = 0$."
                            % (a2, c2, d2, a2, d2, latex(L_v), latex(L_v)))

            ########################################################################
            # VẬN DỤNG: Giới hạn 4*u_n - v_n
            ########################################################################
            coeff_vd = 4
            val_vd = coeff_vd * L_u - L_v
            val_vd_sai = coeff_vd * L_u + L_v
            vd_da_1_d = r'\True $\lim_{n \to +\infty} (%d u_n - v_n) = %s$' % (coeff_vd, latex(val_vd))
            vd_da_1_s = r'$\lim_{n \to +\infty} (%d u_n - v_n) = %s$' % (coeff_vd, latex(val_vd_sai))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r"$\lim_{n \to +\infty} (%d u_n - v_n) = %d \lim_{n \to +\infty} u_n - \lim_{n \to +\infty} v_n = %d \cdot %s - %s = %s$."
                            % (coeff_vd, coeff_vd, coeff_vd, latex(L_u), latex(L_v), latex(val_vd)))

            ########################################################################
            # VẬN DỤNG CAO: Giới hạn thương u_n / 2v_n
            ########################################################################
            coeff_vdc = 2
            val_vdc = L_u / (coeff_vdc * L_v)
            val_vdc_sai = L_u / L_v # Quên số 2 ở mẫu
            vdc_da_1_d = r'\True $\lim_{n \to +\infty} \frac{u_n}{%d v_n} = %s$' % (coeff_vdc, latex(val_vdc))
            vdc_da_1_s = r'$\lim_{n \to +\infty} \frac{u_n}{%d v_n} = %s$' % (coeff_vdc, latex(val_vdc_sai))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r"$\lim_{n \to +\infty} \frac{u_n}{%d v_n} = \frac{\lim_{n \to +\infty} u_n}{%d \cdot \lim_{n \to +\infty} v_n} = \frac{%s}{%d \cdot %s} = %s$."
                             % (coeff_vdc, coeff_vdc, latex(L_u), coeff_vdc, latex(L_v), latex(val_vdc)))

            # --- PHẦN LOGIC CHỌN ĐÁP ÁN (GIỮ NGUYÊN MẪU CỦA BẠN) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            # Xuất kết quả theo định dạng LaTeX mong muốn
            content = (r'\begin{minipage}{\textwidth}' + '\n'
                r'\begin{ex}' + '\n' + str(noidungcauhoi) + '\n'
                r'\choiceTFn' + '\n'
                '{' + ans_nb + '}\n'
                '{' + ans_th + '}\n'
                '{' + ans_vd + '}\n'
                '{' + ans_vdc + '}\n'
                r'\loigiai{' + '\n'
                r'\begin{enumEX}[a)]{1}' + '\n'
                r'\item ' + loigiai_nb_1 + '\n'
                r'\item ' + loigiai_th_1 + '\n'
                r'\item ' + loigiai_vd_1 + '\n'
                r'\item ' + loigiai_vdc_1 + '\n'
                r'\end{enumEX}}' + '\n'
                r'\end{ex}' + '\n' + r'\end{minipage}' + '\n\n')
            return content

