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


def bt_dang26_p2_b1_c3_ds12(self):
                # Khai báo biến ký hiệu
                x = symbols('x')

                # --- BƯỚC 1: RANDOM CÁC GIÁ TRỊ ---
                k_val = random.randint(1, 5) # Tham số k trong |x - k|

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Cho hàm số $f(x)=|x-%s|$.''' % (latex(k_val)))

                ########################################################################
                # Nhận biết: Kiểm tra nguyên hàm trên khoảng (k; +inf)
                ########################################################################
                c_nb = random.randint(1, 5)
                F_nb_dung = Rational(1, 2)*x**2 - k_val*x + c_nb

                nb_da_1_d = r'\True Trên khoảng $(%s; +\infty)$, $F(x) = %s$ là một nguyên hàm của hàm số đã cho' % (latex(k_val), latex(F_nb_dung))
                nb_da_1_s = r'Trên khoảng $(%s; +\infty)$, $F(x) = %s$ là một nguyên hàm của hàm số đã cho' % (latex(k_val), latex(F_nb_dung + x))
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

                loigiai_nb_1 = (r'''Trên khoảng $(%s; +\infty)$, $f(x) = x - %s$. Ta có $F'(x) = \left( %s \right)' = x - %s = f(x)$.''' 
                                % (latex(k_val), latex(k_val), latex(F_nb_dung), latex(k_val)))

                ########################################################################
                # Thông hiểu: Kiểm tra nguyên hàm trên khoảng (-inf; k)
                ########################################################################
                c_th = random.randint(1, 5)
                G_th_sai = Rational(1, 2)*x**2 - k_val*x - c_th 

                th_da_1_d = r'\True Hàm số $G(x) = %s$ không phải là nguyên hàm của hàm số trên khoảng $(-\infty; %s)$' % (latex(G_th_sai), latex(k_val))
                th_da_1_s = r'Hàm số $G(x) = %s$ là một nguyên hàm của hàm số trên khoảng $(-\infty; %s)$' % (latex(G_th_sai), latex(k_val))
                list_th_da_1 = [th_da_1_d, th_da_1_s]

                loigiai_th_1 = (r'''Trên khoảng $(-\infty; %s)$, $f(x) = -x + %s$. Mà $G'(x) = \left( %s \right)' = x - %s \neq f(x)$.''' 
                                % (latex(k_val), latex(k_val), latex(G_th_sai), latex(k_val)))

                ########################################################################
                # Vận dụng: Tìm C trên khoảng (k; +inf)
                ########################################################################
                x_vd = k_val + 1
                c_vd_val = random.randint(2, 6)
                C_constant_vd = c_vd_val - (Rational(1, 2)*x_vd**2 - k_val*x_vd)
                x_calc_vd = k_val + 3
                val_final_vd = Rational(1, 2)*x_calc_vd**2 - k_val*x_calc_vd + C_constant_vd

                vd_da_1_d = r'\True Gọi $F(x)$ là một nguyên hàm của $f(x)$ trên $(%s; +\infty)$. Nếu $F(%s) = %s$ thì $F(%s) = %s$' % (latex(k_val), latex(x_vd), latex(c_vd_val), latex(x_calc_vd), latex(val_final_vd))
                vd_da_1_s = r'Gọi $F(x)$ là một nguyên hàm của $f(x)$ trên $(%s; +\infty)$. Nếu $F(%s) = %s$ thì $F(%s) = %s$' % (latex(k_val), latex(x_vd), latex(c_vd_val), latex(x_calc_vd), latex(val_final_vd + 1))
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

                loigiai_vd_1 = (r'''Trên $(%s; +\infty)$, $F(x) = \int (x-%s)\text{d}x = \frac{x^2}{2}-%sx+C$. Vì $F(%s)=%s \Rightarrow C=%s$. Khi đó $F(%s)=%s$.''' 
                                % (latex(k_val), latex(k_val), latex(k_val), latex(x_vd), latex(c_vd_val), latex(C_constant_vd), latex(x_calc_vd), latex(val_final_vd)))

                ########################################################################
                # Vận dụng cao: Nguyên hàm liên tục trên R
                ########################################################################
                x_low = k_val - 1
                y_low = random.randint(1, 3)
                C2_vdc = y_low - (-Rational(1, 2)*x_low**2 + k_val*x_low)
                C1_vdc = k_val**2 + C2_vdc
                x_vdc_1 = k_val - 2
                x_vdc_2 = k_val + 3
                val_1 = -Rational(1, 2)*x_vdc_1**2 + k_val*x_vdc_1 + C2_vdc
                val_2 = Rational(1, 2)*x_vdc_2**2 - k_val*x_vdc_2 + C1_vdc
                tong_vdc = val_1 + val_2

                vdc_da_1_d = r'\True Giả sử $F(x)$ là nguyên hàm của $f(x)$ trên $\mathbb{R}$ và $F(%s)=%s$. Khi đó $F(%s)+F(%s)=%s$' % (latex(x_low), latex(y_low), latex(x_vdc_1), latex(x_vdc_2), latex(tong_vdc))
                vdc_da_1_s = r'Giả sử $F(x)$ là nguyên hàm của $f(x)$ trên $\mathbb{R}$ và $F(%s)=%s$. Khi đó $F(%s)+F(%s)=%s$' % (latex(x_low), latex(y_low), latex(x_vdc_1), latex(x_vdc_2), latex(tong_vdc - 1))
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

                loigiai_vdc_1 = (r'''$F(x) = \begin{cases} \frac{x^2}{2}-%sx+C_1 & \text{khi } x \ge %s \\ -\frac{x^2}{2}+%sx+C_2 & \text{khi } x < %s \end{cases}$. Từ $F(%s)=%s \Rightarrow C_2=%s$. Do $F(x)$ liên tục tại $x=%s$ nên $\lim_{x \to %s^+} F(x) = \lim_{x \to %s^-} F(x) \Rightarrow C_1=%s$. Vậy $F(%s)+F(%s)=%s$.''' 
                                 % (latex(k_val), latex(k_val), latex(k_val), latex(k_val), latex(x_low), latex(y_low), latex(C2_vdc), latex(k_val), latex(k_val), latex(k_val), latex(C1_vdc), latex(x_vdc_1), latex(x_vdc_2), latex(tong_vdc)))

                # --- LOGIC CHỌN ĐÁP ÁN ĐÚNG/SAI ---
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    choice_nb = random.choice(list_nb_da_1)
                    choice_th = random.choice(list_th_da_1)
                    choice_vd = random.choice(list_vd_da_1)
                    choice_vdc = random.choice(list_vdc_da_1)

                    current_answers = [choice_nb, choice_th, choice_vd, choice_vdc]
                    if 1 <= count_true_answers(current_answers) <= 3:
                        break

                # Xuất nội dung theo định dạng LaTeX (đồng bộ 100% với dang22)
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                    '\\choiceTFn \n'
                    '{' + str(choice_nb) + '}\n'
                    '{' + str(choice_th) + '}\n'
                    '{' + str(choice_vd) + '}\n'
                    '{' + str(choice_vdc) + '}\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item ' + str(loigiai_nb_1) + '\n'
                    '\\item ' + str(loigiai_th_1) + '\n'
                    '\\item ' + str(loigiai_vd_1) + '\n'
                    '\\item ' + str(loigiai_vdc_1) + '\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n \\end{minipage} \n\n')
                return content

