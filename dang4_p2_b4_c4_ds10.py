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


def bt_dang4_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            def generate_question():
                while True:
                    # B3: Tìm cách random bài toán
                    # Chọn 2 nghiệm nguyên phân biệt x1, x2 cho phương trình sau khi bình phương
                    x1 = random.randint(-7, -1)
                    x2 = random.randint(-10, -8)

                    # Phương trình hệ quả: (x - x1)(x - x2) = x^2 - (x1+x2)x + x1*x2 = 0
                    # Gọi B = -(x1+x2), C = x1*x2 -> x^2 + Bx + C = 0
                    B = -(x1 + x2)
                    C = x1 * x2

                    # Thiết lập f(x) = x^2 + b1*x + c1
                    # Chọn b1, c1 sao cho f(x1) >= 0 và f(x2) >= 0
                    b1 = random.randint(-5, 5)
                    # f(x1) = x1^2 + b1*x1 + c1 >= 0 => c1 >= -x1^2 - b1*x1
                    c1_min = max(-x1**2 - b1*x1, -x2**2 - b1*x2)
                    c1 = random.randint(c1_min, c1_min + 10)

                    f_x = x**2 + b1*x + c1
                    # Để g(x) = 2x^2 + b2*x + c2 sao cho g(x) - f(x) = x^2 + Bx + C
                    # => b2 = b1 + B, c2 = c1 + C
                    b2 = b1 + B
                    c2 = c1 + C
                    g_x = 2*x**2 + b2*x + c2

                    # Kiểm tra điều kiện f(x) >= 0 tại các nghiệm
                    if f_x.subs(x, x1) >= 0 and f_x.subs(x, x2) >= 0:
                        return f_x, g_x, x1, x2, B, C

            f_x, g_x, x1, x2, B, C = generate_question()

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình $\\sqrt{%s} = \\sqrt{%s} \\quad (*)$.''' 
                             % (latex(f_x), latex(g_x)))

            ########################################################################
            # Nhận biết
            ########################################################################
            nb_da_1_d = '\\True Bình phương hai vế của phương trình (*), ta được $x^2 + %sx + %s = 0$' % (latex(B), latex(C))
            nb_da_1_s = 'Bình phương hai vế của phương trình (*), ta được $x^2 - %sx + %s = 0$' % (latex(B), latex(C))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Bình phương hai vế của phương trình (*), ta có:\\\\ 
                            $%s = %s \\\\
                            \\Leftrightarrow 2x^2 - x^2 + (%s)x - (%s)x + %s - %s = 0 \\\\
                            \\Leftrightarrow x^2 + %sx + %s = 0$.''' 
                            % (latex(f_x), latex(g_x), latex(f_x.coeff(x, 1) + B), latex(f_x.coeff(x, 1)), 
                               latex(f_x.subs(x, 0) + C), latex(f_x.subs(x, 0)), latex(B), latex(C)))

            ########################################################################
            # Thông hiểu
            ########################################################################
            th_da_1_d = '\\True $x = %s$ là một nghiệm của phương trình (*)' % (latex(x1))
            th_da_1_s = '$x = %s$ là một nghiệm của phương trình (*)' % (latex(abs(x1) + 2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Thay $x = %s$ vào phương trình (*):\\\\
                            Vế trái: $\\sqrt{%s} = \\sqrt{%s}$ (thỏa mãn).\\\\
                            Vậy $x = %s$ là nghiệm của phương trình.''' 
                            % (latex(x1), latex(f_x.subs(x, x1)), latex(f_x.subs(x, x1)), latex(x1)))

            ########################################################################
            # Vận dụng
            ########################################################################
            tong_nghiem = x1 + x2
            vd_da_1_d = '\\True Tổng các nghiệm của phương trình (*) bằng $%s$' % (latex(tong_nghiem))
            vd_da_1_s = 'Tổng các nghiệm của phương trình (*) bằng $%s$' % (latex(-tong_nghiem))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Giải phương trình $x^2 + %sx + %s = 0$, ta tìm được hai nghiệm là $x = %s$ và $x = %s$.\\\\
                            Thử lại cả hai giá trị vào điều kiện $f(x) \\ge 0$, ta thấy cả hai đều thỏa mãn.\\\\
                            Tổng các nghiệm là: $%s + (%s) = %s$.''' 
                            % (latex(B), latex(C), latex(x1), latex(x2), latex(x1), latex(x2), latex(tong_nghiem)))

            ########################################################################
            # Vận dụng cao
            ########################################################################
            vdc_da_1_d = '\\True Phương trình (*) có $2$ nghiệm phân biệt'
            vdc_da_1_s = 'Phương trình (*) có $1$ nghiệm duy nhất'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Sau khi giải phương trình hệ quả và thử lại vào phương trình ban đầu, ta xác định được tập nghiệm của phương trình là $S = \\{%s; %s\\}$.\\\\
                            Do đó phương trình có 2 nghiệm phân biệt.''' 
                             % (latex(x1), latex(x2)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Nội dung xuất bản
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

