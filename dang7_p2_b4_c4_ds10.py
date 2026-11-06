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


def bt_dang7_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # 1. THIẾT LẬP BÀI TOÁN (Có thể thay đổi các tham số này để tạo bài toán mới)
            # Phương trình: (x + k)*(sqrt(x + a) - sqrt(-x^2 + bx + c)) = 0
            k = randint(1,5)
            a = randint(4,9)
            b = randint(4,9)
            c = randint(15,20)

            f1 = x + k
            f2 = sqrt(x + a)
            f3 = sqrt(-x**2 + b*x + c)
            pt = f1 * (f2 - f3)

            # Tìm điều kiện xác định
            cond1 = x + a >= 0
            cond2 = -x**2 + b*x + c >= 0
            sol_cond1 = solve(cond1, x)
            sol_cond2 = solve(cond2, x)
            domain = sol_cond1.as_set() & sol_cond2.as_set()

            # Giải phương trình
            # Nghiệm từ x + k = 0
            sol1 = solve(f1, x)
            # Nghiệm từ sqrt(x + a) = sqrt(-x^2 + bx + c)
            sol2 = solve(f2 - f3, x)

            all_candidates = list(set(sol1 + sol2))
            valid_solutions = [s for s in all_candidates if domain.contains(s)]
            valid_solutions.sort()

            # Các thông số để làm đáp án
            num_sol = len(valid_solutions)
            sum_sol = sum(valid_solutions)
            max_sol = max(valid_solutions)

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho phương trình $(x+%s)\left(\sqrt{x+%s}-\sqrt{-x^2+%sx+%s}\right)=0 \quad (*)$.''' % (latex(k), latex(a), latex(b), latex(c))

            ########################################################################
            # a) Điều kiện xác định
            ########################################################################
            cond_correct = r'\True Điều kiện xác định của phương trình là $%s$' % latex(domain)
            cond_wrong = r'Điều kiện: $x \ge %s$' % latex(max_sol - 1)
            list_a = [cond_correct, cond_wrong]
            da_a = random.choice(list_a)

            loigiai_a = r'''Điều kiện xác định: $\begin{cases} x+%s \ge 0 \\ -x^2+%sx+%s \ge 0 \end{cases} \Leftrightarrow %s$.''' % (latex(a), latex(b), latex(c), latex(domain))

            ########################################################################
            # b) Số lượng nghiệm
            ########################################################################
            sol_count_correct = r'\True Phương trình $(*)$ có %s nghiệm phân biệt' % num_sol
            sol_count_wrong = r'Phương trình $(*)$ có %s nghiệm phân biệt' % (num_sol - 1)
            list_b = [sol_count_correct, sol_count_wrong]
            da_b = random.choice(list_b)

            loigiai_b = r'''Phương trình $(*) \Leftrightarrow \left[\begin{aligned} & x+%s=0 \\ & \sqrt{x+%s}=\sqrt{-x^2+%sx+%s} \end{aligned}\right. \Leftrightarrow \left[\begin{aligned} & x=%s \\ & x^2-%sx-%s=0 \end{aligned}\right. \Leftrightarrow x \in \{%s\}$. Đối chiếu điều kiện, phương trình có %s nghiệm.''' % (latex(k), latex(a), latex(b), latex(c), latex(-k), latex(b-1), latex(c-a), ", ".join([latex(s) for s in all_candidates]), num_sol)

            ########################################################################
            # c) Tính chất nghiệm (nhỏ hơn 5)
            ########################################################################
            prop_correct = r'\True Các nghiệm của phương trình $(*)$ đều thuộc đoạn $[%s; %s]$ ' % (latex(min(valid_solutions)), latex(max_sol))
            prop_wrong = r'Các nghiệm của phương trình $(*)$ nhỏ hơn $%s$' % latex(max_sol)
            list_c = [prop_correct, prop_wrong]
            da_c = random.choice(list_c)

            loigiai_c = r'''Các nghiệm của phương trình là $x \in \{%s\}$. Như vậy các nghiệm đều $\le %s$.''' % (", ".join([latex(s) for s in valid_solutions]), latex(max_sol))

            ########################################################################
            # d) Tổng các nghiệm
            ########################################################################
            sum_correct = r'\True Tổng các nghiệm của phương trình $(*)$ bằng $%s$' % latex(sum_sol)
            sum_wrong = r'Tổng các nghiệm của phương trình $(*)$ bằng $%s$' % latex(sum_sol + 1)
            list_d = [sum_correct, sum_wrong]
            da_d = random.choice(list_d)

            loigiai_d = r'''Tổng các nghiệm là: $%s = %s$.''' % (" + ".join(["(" + latex(s) + ")" if s < 0 else latex(s) for s in valid_solutions]), latex(sum_sol))

            # ----------------------------------------------------------------------
            # XỬ LÝ KẾT QUẢ ĐỂ XUẤT RA THEO MẪU
            # ----------------------------------------------------------------------

            # Đưa vào list để shuffle (tùy chọn) hoặc giữ nguyên thứ tự a, b, c, d
            choices = [da_a, da_b, da_c, da_d]
            solutions = [loigiai_a, loigiai_b, loigiai_c, loigiai_d]

            # Hàm đếm số câu True để đảm bảo logic (từ 1 đến 3 câu đúng)
            def count_true(list_ans):
                return sum('\\True' in s for s in list_ans)

            # Chạy loop cho đến khi đạt yêu cầu số câu True (Ví dụ từ 1 đến 4)
            while True:
                c1 = random.choice(list_a)
                c2 = random.choice(list_b)
                c3 = random.choice(list_c)
                c4 = random.choice(list_d)
                if 1 <= count_true([c1, c2, c3, c4]) <= 3:
                    shuffled_answers = [c1, c2, c3, c4]
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(solutions[0]) + '\n'
                '\\item ' + str(solutions[1]) + '\n'
                '\\item ' + str(solutions[2]) + '\n'
                '\\item ' + str(solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

