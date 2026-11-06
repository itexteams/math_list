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


def bt_dang7_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # BƯỚC 1: RANDOM BÀI TOÁN (Random 2 nghiệm nguyên để bảng xét dấu đẹp)
            x1 = random.randint(-2, 2)
            x2 = x1 + random.randint(1, 4) # Đảm bảo x2 > x1
            f_sym = (x - x1) * (x - x2)
            f_expand = f_sym.expand()

            # Lấy các hệ số để dùng cho tính toán
            a_val = 1
            b_val = - (x1 + x2)
            c_val = x1 * x2
            delta = b_val**2 - 4*a_val*c_val

            # Nội dung câu hỏi
            noidungcauhoi = "Cho tam thức bậc hai $f(x) = %s$." % (latex(f_expand))

            ########################################################################
            # NHẬN BIẾT: Về số nghiệm
            nb_da_1_d = r'\True Tam thức bậc hai có $2$ nghiệm phân biệt'
            nb_da_1_s = r'Tam thức bậc hai vô nghiệm'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = "Ta có $\\Delta = (%s)^2 - 4 \\cdot 1 \\cdot %s = %s > 0$. Do đó phương trình $f(x)=0$ có $2$ nghiệm phân biệt $x=%s, x=%s$." % (b_val, c_val, delta, x1, x2)

            ########################################################################
            # THÔNG HIỂU: Về dấu của tam thức
            th_da_1_d = r'Tam thức bậc hai $f(x)$ luôn dương với mọi $x \in \mathbb{R}$'
            th_da_1_s = r'\True Tam thức bậc hai $f(x)$ nhận giá trị âm khi $x \in (%s; %s)$' % (x1, x2)
            # Đổi lại logic để khớp với đề bài gốc (Câu b thường sai)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = "Vì $a=1 > 0$ và tam thức có hai nghiệm phân biệt nên $f(x) < 0$ khi $x$ nằm trong khoảng hai nghiệm $(%s; %s)$ và $f(x) > 0$ khi $x \\in (-\\infty; %s) \\cup (%s; +\\infty)$." % (x1, x2, x1, x2)

            ########################################################################
            # VẬN DỤNG: Bảng xét dấu
            # Tạo bảng xét dấu bằng tabular
            bang_xet_dau = r"""\begin{tabular}{|c|ccccccc|}
            \hline
            $x$ & $-\infty$ & & %s & & %s & & $+\infty$ \\ \hline
            $f(x)$ & & $+$ & $0$ & $-$ & $0$ & $+$ & \\ \hline
            \end{tabular}""" % (x1, x2)

            bang_xet_dau_sai = r"""\begin{tabular}{|c|ccccccc|}
            \hline
            $x$ & $-\infty$ & & %s & & %s & & $+\infty$ \\ \hline
            $f(x)$ & & $-$ & $0$ & $+$ & $0$ & $-$ & \\ \hline
            \end{tabular}""" % (x1, x2)

            vd_da_1_d = r'\True Tam thức bậc hai $f(x)$ có bảng xét dấu là \\ %s' %(bang_xet_dau)
            vd_da_1_s = r'Tam thức bậc hai $f(x)$ có bảng xét dấu là \\ %s' %(bang_xet_dau_sai)
            # Chỗ này trong ảnh gốc là bảng xét dấu cụ thể, ta sẽ đưa vào lời giải
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = "Dựa vào quy tắc xét dấu tam thức bậc hai: 'Trong trái, ngoài cùng'. Hệ số $a=1 > 0$ nên trong khoảng $(%s; %s)$ mang dấu âm, ngoài khoảng mang dấu dương. \\\\ %s" % (x1, x2, bang_xet_dau)

            ########################################################################
            # VẬN DỤNG CAO: Số nguyên thỏa mãn f(x) < 0
            so_nguyen = [i for i in range(x1 + 1, x2)]
            count_nguyen = len(so_nguyen)

            vdc_da_1_d = r'\True Có duy nhất %s số nguyên thỏa mãn $f(x) < 0$' % (count_nguyen)
            vdc_da_1_s = r'Có %s số nguyên thỏa mãn $f(x) < 0$' % (count_nguyen + 1)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            if count_nguyen == 0:
                loigiai_vdc_1 = "Bất phương trình $f(x) < 0 \\Leftrightarrow %s < x < %s$. Trong khoảng này không có số nguyên nào." % (x1, x2)
            else:
                loigiai_vdc_1 = "Bất phương trình $f(x) < 0 \\Leftrightarrow %s < x < %s$. Các số nguyên thỏa mãn là: %s. Vậy có %s số." % (x1, x2, ", ".join(map(str, so_nguyen)), count_nguyen)

            ########################################################################
            # XỬ LÝ ĐẦU RA
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    break

            # Gán vào list cuối cùng
            shuffled_answers = [d1, d2, d3, d4]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

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

