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


def bt_dang19_p2_b2_c3_ds12(self):
                # --- KHAI BÁO BIẾN NGẪU NHIÊN ---
                x = symbols('x')
                k_val = random.choice([2, 4]) # Chọn k chẵn để tích phân 0->pi bằng 0
                m_val = Rational(1, 2)
                f = sin(k_val * x)

                # Tính các giá trị tích phân/nguyên hàm cho các tầng độ nhận thức
                val_int_0_pi = integrate(f, (x, 0, pi)) # Thường = 0 với k chẵn

                # Tìm C sao cho F(0) = m_val => -1/k + C = m_val => C = m_val + 1/k
                C_val = m_val + Rational(1, k_val)
                F_x = - (1/Rational(k_val)) * cos(k_val * x) + C_val
                val_f_pi_2 = F_x.subs(x, pi/2)

                # Biểu thức cho Vận dụng
                expr_vd = cos(x) - f
                val_vd = integrate(expr_vd, (x, 0, pi/2))

                # Biểu thức cho Vận dụng cao
                val_vdc =2*k_val*integrate(f, (x, 0, pi/k_val))

                # Nội dung câu hỏi
                noidungcauhoi = (r"""Cho hàm số $f(x) = %s$ liên tục trên $\mathbb{R}$.""" % (latex(f)))

                ########################################################################
                # Nhận biết ############################################################
                nb_da_1_d = r'\True Giá trị của tích phân $\int_{0}^{\pi} f(x) \text{d}x = %s$' % (latex(val_int_0_pi))
                nb_da_1_s = r'Giá trị của tích phân $\int_{0}^{\pi} f(x) \text{d}x = 1$'
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
                nb_da_1 = random.choice(list_nb_da_1)
                list_nb_1 = [nb_da_1]

                loigiai_nb_1 = (r'Ta có $\int_{0}^{\pi} \sin %sx \text{d}x = \left( -\frac{1}{%s} \cos %sx \right) \Big|_{0}^{\pi} = -\frac{1}{%s}(\cos %s\pi - \cos 0) = %s$.' 
                                % (k_val, k_val, k_val, k_val, k_val, latex(val_int_0_pi)))
                list_nb_2 = [loigiai_nb_1]

                # Xáo trộn Nhận biết
                combined_nb = list(zip(list_nb_1, list_nb_2))
                random.shuffle(combined_nb)
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ########################################################################
                # Thông hiểu ###########################################################
                th_da_1_d = r'\True Gọi $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(0) = %s$, khi đó $F\left( \frac{\pi}{2} \right) = %s$' % (latex(m_val), latex(val_f_pi_2))
                th_da_1_s = r'Gọi $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(0) = %s$, khi đó $F\left( \frac{\pi}{2} \right) = 0$' % (latex(m_val))
                list_th_da_1 = [th_da_1_d, th_da_1_s]
                th_da_1 = random.choice(list_th_da_1)
                list_th_1 = [th_da_1]

                loigiai_th_1 = (r'Họ nguyên hàm $F(x) = \int \sin %sx \text{d}x = -\frac{1}{%s} \cos %sx + C$. \\ Vì $F(0) = %s \Rightarrow -\frac{1}{%s} + C = %s \Rightarrow C = %s$. \\ Vậy $F\left( \frac{\pi}{2} \right) = -\frac{1}{%s} \cos \left( \frac{%s\pi}{2} \right) + %s = %s$.' 
                                % (k_val, k_val, k_val, latex(m_val), k_val, latex(m_val), latex(C_val), k_val, k_val, latex(C_val), latex(val_f_pi_2)))
                list_th_2 = [loigiai_th_1]

                # Xáo trộn Thông hiểu
                combined_th = list(zip(list_th_1, list_th_2))
                random.shuffle(combined_th)
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ########################################################################
                # Vận dụng #############################################################
                vd_da_1_d = r'\True Tích phân $\int_{0}^{\frac{\pi}{2}} \left[ \cos x - f(x) \right] \text{d}x = %s$' % (latex(val_vd))
                vd_da_1_s = r'Tích phân $\int_{0}^{\frac{\pi}{2}} \left[ \cos x - f(x) \right] \text{d}x = \frac{1}{2}$'
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
                vd_da_1 = random.choice(list_vd_da_1)
                list_vd_1 = [vd_da_1]

                loigiai_vd_1 = (r'Ta có $\int_{0}^{\frac{\pi}{2}} (\cos x - \sin %sx) \text{d}x = \left( \sin x + \frac{1}{%s} \cos %sx \right) \Big|_{0}^{\frac{\pi}{2}} = %s$.' 
                                % (k_val, k_val, k_val, latex(val_vd)))
                list_vd_2 = [loigiai_vd_1]

                # Xáo trộn Vận dụng
                combined_vd = list(zip(list_vd_1, list_vd_2))
                random.shuffle(combined_vd)
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ########################################################################
                # Vận dụng cao #########################################################
                vdc_da_1_d = r'\True Tích phân $\int_{-\pi}^{\pi} |f(x)| \text{d}x = %s$' % (latex(val_vdc))
                vdc_da_1_s = r'Tích phân $\int_{-\pi}^{\pi} |f(x)| \text{d}x = 2$'
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
                vdc_da_1 = random.choice(list_vdc_da_1)
                list_vdc_1 = [vdc_da_1]

                loigiai_vdc_1 = (r'Ta có $\int_{-\pi}^{\pi} |\sin %s x| \text{d}x = %s$.' 
                                % (k_val,latex(val_vdc)))
                list_vdc_2 = [loigiai_vdc_1]

                # Xáo trộn Vận dụng cao
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))
                random.shuffle(combined_vdc)
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

                # --- KIỂM TRA SỐ LƯỢNG ĐÁP ÁN ĐÚNG (1-3) ---
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    nb_sel = random.choice(list_nb_da_1)
                    th_sel = random.choice(list_th_da_1)
                    vd_sel = random.choice(list_vd_da_1)
                    vdc_sel = random.choice(list_vdc_da_1)
                    if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                        shuffled_answers_nb = [nb_sel]
                        shuffled_answers_th = [th_sel]
                        shuffled_answers_vd = [vd_sel]
                        shuffled_answers_vdc = [vdc_sel]
                        break

                # --- XUẤT NỘI DUNG ---
                content = ('\\begin{minipage}{\\textwidth} \n'
                        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                        '\\choiceTFn \n'
                        '{' + str(shuffled_answers_nb[0]) + '}\n'
                        '{' + str(shuffled_answers_th[0]) + '}\n'
                        '{' + str(shuffled_answers_vd[0]) + '}\n'
                        '{' + str(shuffled_answers_vdc[0]) + '}\n'
                        '\\loigiai{ \n'
                        '\\begin{enumEX}[a)]{1} \n'
                        '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                        '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                        '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                        '\\end{enumEX}} \n'
                        '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+')

                return content

