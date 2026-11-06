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


def bt_dang12_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            def generate_data():
                while True:
                    m = random.randint(3, 6) # Giá trị chặn trên của điều kiện
                    x1 = random.randint(0, m - 1) # Nghiệm đúng
                    x2 = random.randint(m + 1, m + 6) # Nghiệm loại

                    a = x1 + x2 - 2*m
                    b = m**2 - x1*x2

                    # Kiểm tra hệ số để biểu thức không quá xấu hoặc a = 0
                    if a != 0 and b != 0:
                        c1 = a - 2*m
                        c2 = m**2 + b
                        return m, x1, x2, a, b, c1, c2

            m, x1, x2, a, b, c1, c2 = generate_data()

            # Biểu thức trong và ngoài căn
            bt_trong_can = a*x + b
            bt_ngoai_can = x - m

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình $x^2 %s x + %s + 2(x - %s)\\sqrt{%s} = 0$.''' 
                            % (('+' + latex(c1) if c1 > 0 else latex(c1)), latex(c2), latex(m), latex(bt_trong_can)))

            ########################################################################
            # Nhận biết
            ########################################################################
            nb_da_1_d = '\\True Điều kiện để phương trình có nghiệm là $x \\le %s$' % (latex(m))
            nb_da_1_s = 'Điều kiện để phương trình có nghiệm là $x \\ge %s$' % (latex(m))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Phương trình tương đương $((x-%s) + \\sqrt{%s})^2 = 0 \\Leftrightarrow \\sqrt{%s} = %s - x$. \\\\ 
                            Điều kiện để phương trình có nghiệm là $%s - x \\ge 0 \\Leftrightarrow x \\le %s$.''' 
                            % (latex(m), latex(bt_trong_can), latex(bt_trong_can), latex(m), latex(m), latex(m)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu
            ########################################################################
            th_da_1_d = '\\True Phương trình có duy nhất $1$ nghiệm'
            th_da_1_s = 'Phương trình có $2$ nghiệm phân biệt'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Với điều kiện $x \\le %s$, phương trình trở thành: \\\\
                            $%s = ( %s - x )^2 \\Leftrightarrow %s = x^2 - %s x + %s$ \\\\
                            $\\Leftrightarrow x^2 - %s x + %s = 0 \\Leftrightarrow \\left[ \\begin{aligned} & x = %s \\text{ (thỏa mãn)} \\\\ & x = %s \\text{ (loại)} \\end{aligned} \\right.$ \\\\
                            Vậy phương trình có duy nhất một nghiệm $x = %s$.''' 
                            %(latex(m), latex(bt_trong_can), latex(m), latex(bt_trong_can), latex(2*m), latex(m**2), latex(a+2*m), latex(m**2-b), latex(x1), latex(x2), latex(x1)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng
            ########################################################################
            vd_da_1_d = '\\True Nghiệm của phương trình nhỏ hơn %s' % (latex(x1 + 1))
            vd_da_1_s = 'Nghiệm của phương trình lớn hơn %s' % (latex(x1 + 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Vì nghiệm của phương trình là $x = %s$, mà $%s < %s$ nên nghiệm của phương trình nhỏ hơn %s.''' 
                            % (latex(x1), latex(x1), latex(x1+1), latex(x1+1)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao
            ########################################################################
            parity = "số lẻ" if x1 % 2 != 0 else "số chẵn"
            anti_parity = "số chẵn" if x1 % 2 != 0 else "số lẻ"

            vdc_da_1_d = '\\True Nghiệm của phương trình là một %s' % (parity)
            vdc_da_1_s = 'Nghiệm của phương trình là một %s' % (anti_parity)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Nghiệm của phương trình tìm được là $x = %s$, đây là một %s.''' % (latex(x1), parity))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Logic chọn số câu đúng/sai
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

            # Gán kết quả cuối cùng
            shuffled_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

