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


def bt_dang28_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Bước 1: Random hóa các thông số của bài toán
            # Chiều rộng và chiều dài phần trong khung (đơn vị cm)
            w_in = random.randint(15, 20)  # Ví dụ: 17
            h_in = random.randint(22, 28)  # Ví dụ: 25

            # Tính toán các biểu thức liên quan
            # Kích thước cả khung: (w_in + 2x) và (h_in + 2x)
            # Diện tích f(x) = (w_in + 2x)(h_in + 2x) = 4x^2 + 2(w_in + h_in)x + w_in*h_in
            f_x = expand((w_in + 2*x) * (h_in + 2*x))
            coeff_x = 2 * (w_in + h_in)
            const_term = w_in * h_in

            # Tạo dữ liệu cho câu c (diện tích cụ thể)
            x_val_c = 2
            area_c = f_x.subs(x, x_val_c)

            # Tạo dữ liệu cho câu d (diện tích tối đa)
            x_val_d = 1
            area_d = f_x.subs(x, x_val_d)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Bạn Hà cần làm một khung ảnh hình chữ nhật sao cho phần trong của khung là hình chữ nhật có kích thước $%s cm \\times %s cm$, độ rộng viền xung quanh là $x$ cm.''' 
                             %(latex(w_in), latex(h_in)))

            ########################################################################
            # a) Nhận biết: Kích thước khung
            ########################################################################
            nb_da_1_d = '\\True Các kích thước của cả khung ảnh là $(%s+2x)cm, (%s+2x)cm$' % (latex(w_in), latex(h_in))
            nb_da_1_s = 'Các kích thước của cả khung ảnh là $(%s+x)cm, (%s+x)cm$' % (latex(w_in), latex(h_in))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Vì độ rộng viền là $x$ cm ở cả hai phía, nên chiều rộng mới là $%s + 2x$ (cm) và chiều dài mới là $%s + 2x$ (cm).''' % (latex(w_in), latex(h_in)))

            ########################################################################
            # b) Thông hiểu: Công thức diện tích
            ########################################################################
            th_da_1_d = '\\True Diện tích cả khung ảnh là $f(x) = 4x^2 + %sx + %s$ ($cm^2$)' % (latex(coeff_x), latex(const_term))
            th_da_1_s = 'Diện tích cả khung ảnh là $f(x) = x^2 + %sx + %s$ ($cm^2$)' % (latex(coeff_x), latex(const_term))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Diện tích cả khung ảnh là: $f(x) = (%s + 2x)(%s + 2x) = 4x^2 + %sx + %s$.''' % (latex(w_in), latex(h_in), latex(coeff_x), latex(const_term)))

            ########################################################################
            # c) Vận dụng: Tính x khi biết diện tích
            ########################################################################
            vd_da_1_d = '\\True Để diện tích của cả khung ảnh là $%scm^2$ thì bạn Hà cần làm độ rộng viền bằng $%scm$' % (latex(area_c), latex(x_val_c))
            vd_da_1_s = 'Để diện tích của cả khung ảnh là $%scm^2$ thì bạn Hà cần làm độ rộng viền bằng $1cm$' % (latex(area_c))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Giải phương trình $4x^2 + %sx + %s = %s \\Leftrightarrow 4x^2 + %sx - %s = 0$. Vì $x > 0$ nên ta chọn $x = %s$.''' 
                            % (latex(coeff_x), latex(const_term), latex(area_c), latex(coeff_x), latex(area_c - const_term), latex(x_val_c)))

            ########################################################################
            # d) Vận dụng cao: Bất phương trình diện tích
            ########################################################################
            vdc_da_1_d = '\\True Để diện tích của cả khung ảnh lớn nhất là $%scm^2$ thì bạn Hà cần làm độ rộng viền khung ảnh tối đa là $%scm$' % (latex(area_d), latex(x_val_d))
            vdc_da_1_s = 'Để diện tích của cả khung ảnh lớn nhất là $%scm^2$ thì bạn Hà cần làm độ rộng viền khung ảnh tối đa là $0.5cm$' % (latex(area_d))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Xét bất phương trình $f(x) \\le %s \\Leftrightarrow 4x^2 + %sx + %s \\le %s \\Leftrightarrow 4x^2 + %sx - %s \\le 0$. Kết hợp với điều kiện $x > 0$, ta được $0 < x \\le %s$. Vậy độ rộng tối đa là $%scm$.''' 
                             % (latex(area_d), latex(coeff_x), latex(const_term), latex(area_d), latex(coeff_x), latex(area_d - const_term), latex(x_val_d), latex(x_val_d)))

            # Hàm đếm số câu đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo số lượng đáp án đúng từ 1 đến 3
            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

