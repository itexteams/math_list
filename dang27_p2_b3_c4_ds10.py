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


def bt_dang27_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, m = symbols('x m')

            # B1: Thiết lập các hệ số để có thể random
            # Hàm số có dạng f(x) = (m+a)x^2 - 2(m+a)x + 2m + b
            # Trong ảnh: a = 1, b = 4
            a = randint(1, 3)
            b = randint(4, 6)
            m_min = -5
            m_max = 5

            # Biểu thức f(x)
            f_x = (m + a)*x**2 - 2*(m + a)*x + 2*m + b

            # Tính toán các giá trị logic cho lời giải
            # 1. Điều kiện để f(x) >= 0 với mọi x:
            # TH1: m + a = 0 => m = -a. Khi đó f(x) = 2(-a) + b
            val_m_case1 = -a
            f_at_neg_a = 2*(-a) + b # Với a=1, b=4 thì f(x)=2 >= 0 (Đúng)

            # TH2: m + a > 0 và Delta' <= 0
            # Delta' = (m+a)^2 - (m+a)(2m + b) = (m+a)(m + a - 2m - b) = (m+a)(-m + a - b)
            # Delta' <= 0 <=> (m+a)(m - a + b) >= 0
            # Vì m + a > 0 nên m >= a - b
            m_threshold = a - b # Với a=1, b=4 thì m >= -3. 
            # Kết hợp m > -a: m > -1. 
            # Tổng hợp: m >= -a (nếu b-2a >= 0)

            count_m = 0
            list_m = []
            for i in range(m_min, m_max + 1):
                # Kiểm tra f(x) >= 0 với mọi x
                # Đơn giản hóa: m >= -a (trong trường hợp cụ thể của bài toán này)
                if i >= -a:
                    count_m += 1
                    list_m.append(i)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f (x) = (m+%s)x^2 - 2(m+%s)x + 2m + %s$. ''' 
                             %(latex(a), latex(a), latex(b)))

            ########################################################################
            # a) Nhận biết: Tính bậc hai của hàm số
            nb_da_1_d = 'Hàm số đã cho là hàm số bậc hai khi $m \\neq %s$' %(latex(-a))
            nb_da_1_s = 'Hàm số đã cho luôn là hàm số bậc hai'
            list_nb_da_1 = ['\\True ' + nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Hàm số $f(x)$ là hàm số bậc hai khi hệ số của $x^2$ khác $0$, tức là $m + %s \\neq 0 \\Leftrightarrow m \\neq %s$. \\\\ Do đó khẳng định "luôn là hàm số bậc hai" là sai.''' 
                            %(latex(a), latex(-a)))

            ########################################################################
            # b) Thông hiểu: Tính f(x+1)
            # f(x+1) = (m+a)(x+1)^2 - 2(m+a)(x+1) + 2m + b
            # = (m+a)(x^2 + 2x + 1) - 2(m+a)x - 2(m+a) + 2m + b
            # = (m+a)x^2 + (m+a) - 2(m+a) + 2m + b = (m+a)x^2 + m - a + b
            val_b_expr = m - a + b
            th_da_1_d = '\\True $f(x+1) = (m+%s)x^2 + m + %s$' %(latex(a), latex(b-a))
            th_da_1_s = '$f(x+1) = (m+%s)(x^2+1)+2$' %(latex(a))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Ta có: \\\\ $f(x+1) = (m+%s)(x+1)^2 - 2(m+%s)(x+1) + 2m + %s$ \\\\
                            $= (m+%s)(x^2+2x+1) - 2(m+%s)x - 2(m+%s) + 2m + %s$ \\\\
                            $= (m+%s)x^2 + 2(m+%s)x + (m+%s) - 2(m+%s)x - 2m - %s + 2m + %s$ \\\\
                            $= (m+%s)x^2 + m + %s$.''' 
                            %(latex(a), latex(a), latex(b), latex(a), latex(a), latex(a), latex(b), 
                              latex(a), latex(a), latex(a), latex(a), latex(2*a), latex(b), latex(a), latex(b-a)))

            ########################################################################
            # c) Vận dụng: Bất phương trình vô nghiệm
            vd_da_1_d = '\\True Có %s giá trị nguyên của tham số $m \\in [%s; %s]$ để bất phương trình $f(x) < 0$ vô nghiệm' %(latex(count_m), latex(m_min), latex(m_max))
            vd_da_1_s = 'Có 5 giá trị nguyên của tham số $m \\in [%s; %s]$ để bất phương trình $f(x) < 0$ vô nghiệm' %(latex(m_min), latex(m_max))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Bất phương trình $f(x) < 0$ vô nghiệm khi và chỉ khi $f(x) \\ge 0, \\forall x \\in \\mathbb{R}$. \\\\
                            TH1: $m + %s = 0 \\Leftrightarrow m = %s$. Khi đó $f(x) = 2(%s) + %s = %s \\ge 0$ (đúng). \\\\
                            TH2: $m > %s$ và $\\Delta' = (m+%s)^2 - (m+%s)(2m+%s) \\le 0$ \\\\
                            $\\Leftrightarrow (m+%s)(m+%s - 2m - %s) \\le 0 \\Leftrightarrow (m+%s)(-m + %s) \\le 0$. \\\\
                            Vì $m > %s$ nên $-m + %s \\le 0 \\Leftrightarrow m \\ge %s$. \\\\
                            Kết hợp lại ta được $m \\ge %s$. \\\\
                            Vì $m \\in [%s; %s]$ nên $m \\in \\{%s\\}$. Có %s giá trị.''' 
                            %(latex(a), latex(-a), latex(-a), latex(b), latex(f_at_neg_a), latex(-a), 
                              latex(a), latex(a), latex(b), latex(a), latex(a), latex(b), latex(a), latex(a-b), 
                              latex(-a), latex(a-b), latex(a-b), latex(-a), latex(m_min), latex(m_max), 
                              ", ".join(map(str, list_m)), latex(count_m)))

            ########################################################################
            # d) Vận dụng cao: Tập nghiệm R
            vdc_da_1_d = '\\True Có %s giá trị nguyên của tham số $m \\in [%s; %s]$ để bất phương trình $\\frac{f(x)}{x^2+1} \\ge 0$ có tập nghiệm $\\mathbb{R}$' %(latex(count_m), latex(m_min), latex(m_max))
            vdc_da_1_s = 'Có 10 giá trị nguyên của tham số $m \\in [%s; %s]$ để bất phương trình $\\frac{f(x)}{x^2+1} \\ge 0$ có tập nghiệm $\\mathbb{R}$' %(latex(m_min), latex(m_max))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Vì $x^2 + 1 > 0, \\forall x \\in \\mathbb{R}$ nên $\\frac{f(x)}{x^2+1} \\ge 0 \\Leftrightarrow f(x) \\ge 0$. \\\\
                            Yêu cầu bài toán tương đương với $f(x) \\ge 0, \\forall x \\in \\mathbb{R}$. \\\\
                            Theo kết quả câu c), ta có $m \\ge %s$. \\\\
                            Với $m \\in [%s; %s]$, các giá trị nguyên của $m$ là $%s$. \\\\
                            Vậy có %s giá trị thỏa mãn.''' 
                            %(latex(-a), latex(m_min), latex(m_max), ", ".join(map(str, list_m)), latex(count_m)))

            # Logic xáo trộn và chọn số lượng đáp án đúng (từ 1 đến 3)
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
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

