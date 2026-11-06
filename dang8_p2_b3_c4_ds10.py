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


def bt_dang8_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1: Nghiên cứu đề bài và thiết lập thông số ngẫu nhiên
            # Giả sử f(x) = x - (m+n)*sqrt(x) + m*n = (sqrt(x)-m)(sqrt(x)-n)
            # Với m, n là các số nguyên dương, m < n
            m = random.randint(1, 2)
            n = random.randint(m + 1, m + 4)

            sum_mn = m + n
            prod_mn = m * n
            m_sq = m**2
            n_sq = n**2

            # Hàm số f(x)
            f_expr = x - sum_mn*sqrt(x) + prod_mn

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=%s$.''' 
                             % (latex(f_expr)))

            ########################################################################
            # Nhận biết: Kiểm tra f(m^2) = 0
            ########################################################################
            f_m_sq = m_sq - sum_mn * m + prod_mn # Luôn bằng 0

            nb_da_1_d = '\\True $f(%s)=0$' % (latex(m_sq))
            nb_da_1_s = '$f(%s)=%s$' % (latex(m_sq), random.randint(1, 5))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Ta có $f(%s) = %s - %s\\sqrt{%s} + %s = %s - %s \\cdot %s + %s = 0$.''' 
                            % (latex(m_sq), latex(m_sq), latex(sum_mn), latex(m_sq), latex(prod_mn), latex(m_sq), latex(sum_mn), latex(m), latex(prod_mn)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Số điểm cắt trục hoành
            ########################################################################
            # Phương trình f(x)=0 <=> x - (m+n)sqrt(x) + mn = 0 <=> sqrt(x)=m hoặc sqrt(x)=n 
            # <=> x=m^2 hoặc x=n^2 (2 điểm phân biệt)

            th_da_1_d = '\\True Đồ thị hàm số cắt trục hoành tại $2$ điểm phân biệt'
            th_da_1_s = 'Đồ thị hàm số cắt trục hoành tại $1$ điểm duy nhất'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Phương trình hoành độ giao điểm: $x - %s\\sqrt{x} + %s = 0$. \\\\
                            Đặt $t = \\sqrt{x}$ ($t \\ge 0$), ta có: $t^2 - %st + %s = 0 \\Leftrightarrow \\left[ \\begin{aligned} & t = %s \\\\ & t = %s \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned} \\right.$. \\\\
                            Vậy đồ thị hàm số cắt trục hoành tại $2$ điểm phân biệt có hoành độ $x = %s$ và $x = %s$.'''
                            % (latex(sum_mn), latex(prod_mn), latex(sum_mn), latex(prod_mn), latex(m), latex(n), latex(m_sq), latex(n_sq), latex(m_sq), latex(n_sq)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Số điểm nguyên nằm dưới trục hoành
            ########################################################################
            # f(x) < 0 <=> m < sqrt(x) < n <=> m^2 < x < n^2
            # Số giá trị nguyên: (n^2 - 1) - (m^2 + 1) + 1 = n^2 - m^2 - 1
            count_pts = n_sq - m_sq - 1

            vd_da_1_d = '\\True Có %s điểm thuộc đồ thị hàm số (với hoành độ nguyên) nằm hoàn toàn phía dưới trục hoành' % (count_pts)
            vd_da_1_s = 'Có %s điểm thuộc đồ thị hàm số (với hoành độ nguyên) nằm hoàn toàn phía dưới trục hoành' % (count_pts + random.choice([-2, 2]))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Điểm nằm phía dưới trục hoành khi $f(x) < 0 \\Leftrightarrow x - %s\\sqrt{x} + %s < 0$. \\\\
                            Đặt $t = \\sqrt{x}$ ($t \\ge 0$), ta có: $t^2 - %st + %s < 0 \\Leftrightarrow %s < t < %s$. \\\\
                            Suy ra $%s < \\sqrt{x} < %s \\Leftrightarrow %s < x < %s$. \\\\
                            Vì $x$ nguyên nên $x \\in \\{%s; \\dots; %s\\}$. \\\\
                            Số giá trị nguyên của $x$ là: %s - %s - 1 = %s điểm.'''
                            %(latex(sum_mn), latex(prod_mn), latex(sum_mn), latex(prod_mn), latex(m), latex(n), latex(m), latex(n), latex(m_sq), latex(n_sq), latex(m_sq + 1), latex(n_sq - 1), latex(n_sq), latex(m_sq), count_pts))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Bất phương trình (x^2 + k)f(x) <= 0
            ########################################################################
            # Vì x^2 + k > 0 nên bpt <=> f(x) <= 0 <=> m^2 <= x <= n^2
            k = random.randint(1, 5)
            vdc_da_1_d = '\\True Bất phương trình $(x^2 + %s)f(x) \\le 0$ có tập nghiệm $S = [%s; %s]$' % (k, m_sq, n_sq)
            vdc_da_1_s = 'Bất phương trình $(x^2 + %s)f(x) \\le 0$ có tập nghiệm $S = [%s; %s]$' % (k, m, n)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Vì $x^2 + %s > 0$ với mọi $x \\in \\mathbb{R}$, nên bất phương trình $(x^2 + %s)f(x) \\le 0$ tương đương với: \\\\
                             $f(x) \\le 0 \\Leftrightarrow x - %s\\sqrt{x} + %s \\le 0$. \\\\
                             Đặt $t = \\sqrt{x}$ ($t \\ge 0$), ta có: $t^2 - %st + %s \\le 0 \\Leftrightarrow %s \\le t \\le %s$. \\\\
                             Suy ra $%s \\le \\sqrt{x} \\le %s \\Leftrightarrow %s \\le x \\le %s$. \\\\
                             Vậy tập nghiệm của bất phương trình là $S = [%s; %s]$.'''
                             % (k, k, latex(sum_mn), latex(prod_mn), latex(sum_mn), latex(prod_mn), m, n, m, n, m_sq, n_sq, m_sq, n_sq))

            list_vdc_2 = [loigiai_vdc_1]

            # Hàm đếm số câu đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp để đảm bảo có 1-3 câu đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Xuất nội dung theo mẫu yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(nb_sel) + '}\n'
                '{' + str(th_sel) + '}\n'
                '{' + str(vd_sel) + '}\n'
                '{' + str(vdc_sel) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

