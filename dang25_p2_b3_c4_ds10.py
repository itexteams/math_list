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


def bt_dang25_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Tạo tham số ngẫu nhiên cho tam thức bậc hai có 2 nghiệm phân biệt
            # Ở đây ta giữ nguyên cấu trúc (x^2 + m) (x^2 - sx + p)
            m = random.randint(1, 5) # Luôn dương để x^2 + m vô nghiệm
            x1 = random.randint(-4, -1) # Nghiệm âm
            x2 = random.randint(1, 5)   # Nghiệm dương
            # x^2 - (x1+x2)x + x1*x2
            s = x1 + x2
            p = x1 * x2

            f_x = (x**2 + m) * (x**2 - s*x + p)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho đa thức $f(x)=(x^2+%s)(x^2-%sx%s)$.''' 
                             %(latex(m), latex(s) if s != 1 else "", latex(p) if p < 0 else "+" + str(p)))

            ########################################################################
            # Nhận biết
            ########################################################################
            nb_da_1_d = '\\True Đa thức đã cho không phải tam thức bậc hai'
            nb_da_1_s = 'Đa thức đã cho là một tam thức bậc hai'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Đa thức $f(x)$ sau khi khai triển có bậc cao nhất là $x^4$, do đó đây là đa thức bậc bốn, không phải tam thức bậc hai.''')

            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu
            ########################################################################
            # Tính toán nghiệm: x^2 + m = 0 (vô nghiệm), x^2 - sx + p = 0 có nghiệm x1, x2
            nghiem_duong = [v for v in [x1, x2] if v > 0]
            so_nghiem_duong = len(nghiem_duong)

            th_da_1_d = '\\True Đa thức đã cho có %s nghiệm dương' % (so_nghiem_duong)
            th_da_1_s = 'Đa thức đã cho có %s nghiệm dương' % (so_nghiem_duong + 1)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Ta có $f(x)=0 \\Leftrightarrow (x^2+%s)(x^2-%sx%s)=0$. Vì $x^2+%s > 0$ với mọi $x$, nên phương trình tương đương $x^2-%sx%s=0 \\Leftrightarrow x=%s$ hoặc $x=%s$. Vậy đa thức có %s nghiệm dương là $x=%s$.''' 
                            % (latex(m), latex(s), latex(p), latex(m), latex(s), latex(p), latex(x1), latex(x2), so_nghiem_duong, latex(x2)))

            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng
            ########################################################################
            # Tìm các giá trị nguyên của x để f(x) < 0
            # f(x) < 0 <=> x1 < x < x2
            cac_gia_tri_nguyen = [v for v in range(x1 + 1, x2)]
            so_luong_nguyen = len(cac_gia_tri_nguyen)

            vd_da_1_d = '\\True Có %s giá trị nguyên của $x$ để $f(x) < 0$' % (so_luong_nguyen)
            vd_da_1_s = 'Có %s giá trị nguyên của $x$ để $f(x) < 0$' % (so_luong_nguyen + 2)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Vì $x^2+%s > 0$ nên $f(x) < 0 \\Leftrightarrow x^2-%sx%s < 0 \\Leftrightarrow %s < x < %s$. Các giá trị nguyên thỏa mãn là: $%s$. Vậy có %s giá trị.''' 
                            % (latex(m), latex(s), latex(p), latex(x1), latex(x2), ", ".join(map(str, cac_gia_tri_nguyen)), so_luong_nguyen))

            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao
            ########################################################################
            # Xét f(x+k) < 0. Ở đây mẫu là f(x+3) < 0. Ta chọn k ngẫu nhiên.
            k = random.randint(1, 4)
            # f(x+k) < 0 <=> x1 < x+k < x2 <=> x1-k < x < x2-k
            low = x1 - k
            high = x2 - k

            vdc_da_1_d = '\\True $f(x+%s) < 0 \\Leftrightarrow %s < x < %s$' % (k, latex(low), latex(high))
            vdc_da_1_s = '$f(x+%s) < 0 \\Leftrightarrow %s < x < %s$' % (k, latex(low - 1), latex(high))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Đặt $t = x+%s$, khi đó bất phương trình trở thành $f(t) < 0$. Theo kết quả trên ta có $%s < t < %s$, hay $%s < x+%s < %s \\Leftrightarrow %s < x < %s$.''' 
                             % (k, latex(x1), latex(x2), latex(x1), k, latex(x2), latex(low), latex(high)))

            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                current_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Gán lại để xuất
            final_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
            final_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(final_answers[0]) + '}\n'
                '{' + str(final_answers[1]) + '}\n'
                '{' + str(final_answers[2]) + '}\n'
                '{' + str(final_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(final_solutions[0]) + '\n'
                '\\item ' + str(final_solutions[1]) + '\n'
                '\\item ' + str(final_solutions[2]) + '\n'
                '\\item ' + str(final_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','+')
            return content

