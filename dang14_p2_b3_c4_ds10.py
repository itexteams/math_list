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


def bt_dang14_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1: Random số liệu mới
            # Chọn 2 nghiệm nguyên phân biệt x1 < x2 trong khoảng từ -5 đến 5
            x1 = random.randint(-3, 1)
            x2 = x1 + random.randint(2, 4)

            # Hệ số của f(x) = x^2 - ax + b
            # f(x) = (x - x1)(x - x2) = x^2 - (x1 + x2)x + x1*x2
            # Suy ra: a = x1 + x2 và b = x1 * x2
            a_val = x1 + x2
            b_val = x1 * x2

            f_x = x**2 - a_val*x + b_val

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Tam thức bậc hai $f(x) = x^2 - ax + b$ có bảng xét dấu như sau:
            \begin{center}
            \begin{tabular}{|c|ccccccc|}
            \hline
            $x$ & $-\infty$ & & %s & & %s & & $+\infty$ \\ \hline
            $f(x)$ & & $+$ & $0$ & $-$ & $0$ & $+$ & \\ \hline
            \end{tabular}
            \end{center}''' % (latex(x1), latex(x2)))

            ########################################################################
            # a) Xét f(x) < 0
            da_a_d = r'\True $f(x) < 0 \Leftrightarrow %s < x < %s$' % (latex(x1), latex(x2))
            da_a_s = r'$f(x) < 0 \Leftrightarrow x < %s$ hoặc $x > %s$' % (latex(x1), latex(x2))
            list_da_a = [da_a_d, da_a_s]

            loigiai_a = (r'''Dựa vào bảng xét dấu, ta thấy $f(x)$ mang dấu âm ($-$) khi $x$ nằm trong khoảng giữa hai nghiệm. Do đó $f(x) < 0 \Leftrightarrow %s < x < %s$.''' 
                         % (latex(x1), latex(x2)))

            ########################################################################
            # b) Tính a + b
            tong_ab = a_val + b_val
            da_b_d = r'\True $a + b = %s$' % (latex(tong_ab))
            da_b_s = r'$a + b = %s$' % (latex(tong_ab + random.choice([-2, -1, 1, 2])))
            list_da_b = [da_b_d, da_b_s]

            loigiai_b = (r'''Từ bảng xét dấu, $f(x)$ có hai nghiệm $x_1 = %s, x_2 = %s$. Theo định lý Vi-ét cho tam thức $x^2 - ax + b$:
            Ta có $x_1 + x_2 = a \Rightarrow a = %s + %s = %s$.
            Ta có $x_1 \cdot x_2 = b \Rightarrow b = %s \cdot %s = %s$.
            Vậy $a + b = %s + %s = %s$.''' 
                         % (latex(x1), latex(x2), latex(x1), latex(x2), latex(a_val), 
                            latex(x1), latex(x2), latex(b_val), latex(a_val), latex(b_val), latex(tong_ab)))

            ########################################################################
            # c) Tính f(x_2 + 1)
            x_test = x2 + 1
            f_val_test = x_test**2 - a_val*x_test + b_val
            da_c_d = r'\True $f(%s) = %s$' % (latex(x_test), latex(f_val_test))
            da_c_s = r'$f(%s) = %s$' % (latex(x_test), latex(f_val_test - 2))
            list_da_c = [da_c_d, da_c_s]

            loigiai_c = (r'''Ta có hàm số là $f(x) = x^2 - %sx + %s$. 
            Thay $x = %s$ vào biểu thức ta được $f(%s) = (%s)^2 - %s \cdot (%s) + %s = %s$.''' 
                         % (latex(a_val), latex(b_val), latex(x_test), latex(x_test), 
                            latex(x_test), latex(a_val), latex(x_test), latex(b_val), latex(f_val_test)))

            ########################################################################
            # d) Đa thức g(x) - tạo một đa thức có nghiệm trùng x1
            x3 = x2 - 1 # Tạo thêm 1 nghiệm khác
            h_x = (x - x1)*(x - x3)
            h_x_expand = expand(h_x)

            da_d_d = r'\True Đa thức $g(x) = (%s)f(x)$ có bảng xét dấu không đổi dấu khi đi qua $x = %s$' % (latex(h_x_expand), latex(x1))
            da_d_s = r'Đa thức $g(x) = (%s)f(x)$ đổi dấu khi đi qua tất cả các nghiệm' % (latex(h_x_expand))
            list_da_d = [da_d_d, da_d_s]

            loigiai_d = (r'''Ta có $g(x) = (%s)f(x) = (x-%s)(x-%s) \cdot (x-%s)(x-%s) = (x-%s)^2(x-%s)(x-%s)$.
            Vì $x = %s$ là nghiệm bội chẵn (bậc 2) nên $g(x)$ không đổi dấu khi đi qua $x = %s$.''' 
                         % (latex(h_x_expand), latex(x1), latex(x3), latex(x1), latex(x2), latex(x1), latex(x3), latex(x2), latex(x1), latex(x1)))

            ########################################################################
            # Lặp chọn đáp án đảm bảo có 1-3 câu đúng
            def count_true(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_da_a)
                ans_b = random.choice(list_da_b)
                ans_c = random.choice(list_da_c)
                ans_d = random.choice(list_da_d)
                if 1 <= count_true([ans_a, ans_b, ans_c, ans_d]) <= 3:
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
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

