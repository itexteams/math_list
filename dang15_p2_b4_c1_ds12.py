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


def bt_dang15_p2_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các tham số k, d0, u để tạo hàm số f(x) = x^3 - 3k*x^2 + d0
            k = random.randint(1, 2)
            d0 = random.randint(4*k**3 + 1, 4*k**3 + 5) # Đảm bảo d0 > 4k^3 để y_CD * y_CT > 0

            f_expr = x**3 - 3*k*x**2 + d0
            f_prime = diff(f_expr, x)

            m_crit = 3*k**2

            # Bảng biến thiên cho f(x)
            x1_bbt = 0
            x2_bbt = 2*k
            y1_bbt = f_expr.subs(x, x1_bbt)
            y2_bbt = f_expr.subs(x, x2_bbt)

            x_inc = 2*k + random.randint(1, 2)

            # Xét cực trị và giao điểm với Ox của f(x)
            y_CD = y1_bbt
            y_CT = y2_bbt
            prod_CD_CT = y_CD * y_CT

            # Tham số m_val cho hàm g(x) = f(x) + m_val*x
            u = random.randint(1, 2)
            m_val = -3*u*(2*k + u)
            g_expr = f_expr + m_val*x
            g_prime = diff(g_expr, x)

            root1 = -u
            root2 = 2*k + u
            max_val = g_expr.subs(x, root1)
            max_val_s = max_val + random.choice([1, 2, 3])
            g_0 = g_expr.subs(x, 0)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=%s$ và hàm số $g(x)=f(x)+mx$ (với $m$ là tham số).'''
                             %(latex(f_expr)))

            ######################################################################## Nhận biết ############################################
            nb_da_1_d = '\\True Hàm số $g(x)$ đạt cực trị khi và chỉ khi $m < %s$' %(latex(m_crit))
            nb_da_1_s = 'Hàm số $g(x)$ đạt cực trị khi và chỉ khi $m > %s$' %(latex(m_crit))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Ta có $g(x) = %s + mx$. \\\\
            $g'(x) = %s + m$. \\\\
            Hàm số $g(x)$ đạt cực trị khi và chỉ khi phương trình $g'(x) = 0$ có $2$ nghiệm phân biệt. \\\\
            $\\Leftrightarrow \\Delta' = \\left(%s\\right)^2 - 3m > 0 \\Leftrightarrow %s - 3m > 0 \\Leftrightarrow m < %s$. \\\\
            Vậy hàm số $g(x)$ đạt cực trị khi và chỉ khi $m < %s$.'''
                            %(latex(x**3 - 3*k*x**2 + d0), latex(3*x**2 - 6*k*x), latex(-3*k), latex(9*k**2), latex(m_crit), latex(m_crit)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            th_da_1_d = '\\True Hàm số $f(x)$ đồng biến trên khoảng $\\left(%s; +\\infty\\right)$' %(latex(x_inc))
            th_da_1_s = 'Hàm số $f(x)$ nghịch biến trên khoảng $\\left(%s; +\\infty\\right)$' %(latex(x_inc))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Ta có $f'(x) = %s$. \\\\
            $f'(x) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow \\left[ \\begin{array}{l} x = %s \\\\ x = %s \\end{array} \\right.$. \\\\
            Bảng biến thiên: \\\\
            \\begin{tikzpicture}
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$x$/1,$f'(x)$/0.7,$f(x)$/2.1}
            {$-\\infty$,$%s$,$%s$,$+\\infty$}
            \\tkzTabLine{,+,0,-,0,+}
            \\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$}
            \\end{tikzpicture} \\\\
            Từ bảng biến thiên, hàm số $f(x)$ đồng biến trên các khoảng $\\left(-\\infty; %s\\right)$ và $\\left(%s; +\\infty\\right)$. \\\\
            Vì $\\left(%s; +\\infty\\right) \\subset \\left(%s; +\\infty\\right)$ nên hàm số $f(x)$ đồng biến trên khoảng $\\left(%s; +\\infty\\right)$.'''
                            %(latex(f_prime), latex(f_prime), latex(x1_bbt), latex(x2_bbt), latex(x1_bbt), latex(x2_bbt), latex(y1_bbt), latex(y2_bbt), latex(x1_bbt), latex(x2_bbt), latex(x_inc), latex(x2_bbt), latex(x_inc)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            vd_da_1_d = '\\True Đồ thị hàm số $f(x)$ cắt trục hoành tại $1$ điểm duy nhất'
            vd_da_1_s = 'Đồ thị hàm số $f(x)$ cắt trục hoành tại $3$ điểm phân biệt'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Từ bảng biến thiên, đồ thị hàm số $f(x)$ có điểm cực đại là $\\left(%s; %s\\right)$ và điểm cực tiểu là $\\left(%s; %s\\right)$. \\\\
            Ta có $y_{CĐ} \\cdot y_{CT} = %s \\cdot %s = %s > 0$. \\\\
            Do $y_{CĐ}$ và $y_{CT}$ cùng dấu nên đồ thị hàm số $f(x)$ cắt trục hoành tại $1$ điểm duy nhất.'''
                            %(latex(x1_bbt), latex(y1_bbt), latex(x2_bbt), latex(y2_bbt), latex(y1_bbt), latex(y2_bbt), latex(prod_CD_CT)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            vdc_da_1_d = '\\True Khi $m = %s$, giá trị lớn nhất của hàm $g(x)$ trên khoảng $\\left(-\\infty; 0\\right)$ bằng $%s$' %(latex(m_val), latex(max_val))
            vdc_da_1_s = 'Khi $m = %s$, giá trị lớn nhất của hàm $g(x)$ trên khoảng $\\left(-\\infty; 0\\right)$ bằng $%s$' %(latex(m_val), latex(max_val_s))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Khi $m = %s$, ta có $g(x) = %s$. \\\\
            $g'(x) = %s$. \\\\
            $g'(x) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow \\left[ \\begin{array}{l} x = %s \\\\ x = %s \\end{array} \\right.$. \\\\
            Trên khoảng $\\left(-\\infty; 0\\right)$, phương trình $g'(x) = 0$ có một nghiệm $x = %s$. \\\\
            Bảng biến thiên của $g(x)$ trên khoảng $\\left(-\\infty; 0\\right)$: \\\\
            \\begin{tikzpicture}
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$x$/1,$g'(x)$/0.7,$g(x)$/2.1}
            {$-\\infty$,$%s$,$0$}
            \\tkzTabLine{,+,0,-}
            \\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$}
            \\end{tikzpicture} \\\\
            Từ bảng biến thiên, giá trị lớn nhất của hàm số $g(x)$ trên khoảng $\\left(-\\infty; 0\\right)$ bằng $%s$ tại $x = %s$.'''
                             %(latex(m_val), latex(g_expr), latex(g_prime), latex(g_prime), latex(root1), latex(root2), latex(root1), latex(root1), latex(max_val), latex(g_0), latex(max_val), latex(root1)))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

