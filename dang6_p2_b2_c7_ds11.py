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


def bt_dang6_p2_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3 - Suy nghĩ tìm cách random bài toán
            # Random hệ số cho hàm số f(x) = ax^3 + bx^2 + cx
            a_coeff = random.choice([-2, -1, 1, 2])
            b_coeff = randint(-5, 5)
            c_coeff = randint(-2, 5)

            f_x = a_coeff*x**3 + b_coeff*x**2 + c_coeff*x
            df_x = diff(f_x, x)

            # Điểm thử cho các câu hỏi
            x_b = randint(1, 4)
            val_df_xb = df_x.subs(x, x_b)

            x_c1 = randint(1, 3)
            x_c2 = x_c1 + randint(1, 2)
            val_df_xc1 = df_x.subs(x, x_c1)
            val_df_xc2 = df_x.subs(x, x_c2)

            x_d1 = randint(-3, -1)
            x_d2 = randint(1, 3)
            val_sum_d = df_x.subs(x, x_d1) + df_x.subs(x, x_d2)

            # B1 & B2 - Nghiên cứu và viết lại bài toán
            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f\\left( x \\right) = %s$.''' % (latex(f_x)))

            ########################################################################
            # Nhận biết: Về công thức đạo hàm
            nb_da_1_d = '\\True Hàm số có đạo hàm là $f\'\\left( x \\right) = %s$' % (latex(df_x))
            nb_da_1_s = 'Hàm số có đạo hàm là $f\'\\left( x \\right) = %s$' % (latex(diff(f_x, x) + randint(1, 3)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = ('''Áp dụng công thức đạo hàm hàm đa thức, ta có:\\\\
            $f'\\left( x \\right) = \\left( %s \\right)' = %s$.''' % (latex(f_x), latex(df_x)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Tính giá trị đạo hàm tại 1 điểm
            th_da_1_d = '\\True $f\'\\left( %s \\right) = %s$' % (latex(x_b), latex(val_df_xb))
            th_da_1_s = '$f\'\\left( %s \\right) = %s$' % (latex(x_b), latex(val_df_xb + randint(1, 5)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]
            loigiai_th_1 = ('''Thay $x = %s$ vào biểu thức đạo hàm ta được:\\\\
            $f'\\left( %s \\right) = %s$.''' % (latex(x_b), latex(x_b), latex(val_df_xb)))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: So sánh giá trị đạo hàm
            if val_df_xc1 < val_df_xc2:
                vd_da_1_d = '\\True $f\'\\left( %s \\right) < f\'\\left( %s \\right)$' % (latex(x_c1), latex(x_c2))
                vd_da_1_s = '$f\'\\left( %s \\right) > f\'\\left( %s \\right)$' % (latex(x_c1), latex(x_c2))
            else:
                vd_da_1_d = '\\True $f\'\\left( %s \\right) \\ge f\'\\left( %s \\right)$' % (latex(x_c1), latex(x_c2))
                vd_da_1_s = '$f\'\\left( %s \\right) < f\'\\left( %s \\right)$' % (latex(x_c1), latex(x_c2))

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = ('''Ta tính các giá trị:\\\\
            $f'\\left( %s \\right) = %s$\\\\
            $f'\\left( %s \\right) = %s$\\\\
            So sánh ta thấy khẳng định trên là đúng.''' % (latex(x_c1), latex(val_df_xc1), latex(x_c2), latex(val_df_xc2)))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Biểu thức tổng đạo hàm
            vdc_da_1_d = '\\True $f\'\\left( %s \\right) + f\'\\left( %s \\right) = %s$' % (latex(x_d1), latex(x_d2), latex(val_sum_d))
            vdc_da_1_s = '$f\'\\left( %s \\right) + f\'\\left( %s \\right) = 0$' % (latex(x_d1), latex(x_d2)) if val_sum_d != 0 else '$f\'\\left( %s \\right) + f\'\\left( %s \\right) = 1$' % (latex(x_d1), latex(x_d2))

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = ('''Tính từng giá trị đạo hàm:\\\\
            $f'\\left( %s \\right) = %s$\\\\
            $f'\\left( %s \\right) = %s$\\\\
            Suy ra $f'\\left( %s \\right) + f'\\left( %s \\right) = %s + \\left( %s \\right) = %s$.''' 
                            % (latex(x_d1), latex(df_x.subs(x, x_d1)), latex(x_d2), latex(df_x.subs(x, x_d2)), 
                               latex(x_d1), latex(x_d2), latex(df_x.subs(x, x_d1)), latex(df_x.subs(x, x_d2)), latex(val_sum_d)))
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Gán kết quả cuối cùng để xuất LaTeX
            ans_final = [nb_sel, th_sel, vd_sel, vdc_sel]
            sol_final = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_final[0]) + '}\n'
                '{' + str(ans_final[1]) + '}\n'
                '{' + str(ans_final[2]) + '}\n'
                '{' + str(ans_final[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(sol_final[0]) + '\n'
                '\\item ' + str(sol_final[1]) + '\n'
                '\\item ' + str(sol_final[2]) + '\n'
                '\\item ' + str(sol_final[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

