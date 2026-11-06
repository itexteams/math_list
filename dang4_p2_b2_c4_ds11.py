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


def bt_dang4_p2_b2_c4_ds11(self):
            # Khai báo biến
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Để bài toán có ý nghĩa như mẫu: 
            # f(x) nên có 2 nghiệm phân biệt x1, x2.
            # g(x) nên là một nhị thức bậc nhất có nghiệm trùng với một trong hai nghiệm của f(x).
            x1 = random.randint(1, 3)
            x2 = random.randint(4, 9)
            k = random.choice([-3, -2, 2, 3])

            f_expr = (x - x1) * (x - x2) # f(x) = x^2 - (x1+x2)x + x1*x2
            g_expr = k * (x2 - x)       # g(x) = k*x2 - k*x (Dạng giống 10 - 2x)

            f_expand = simplify(f_expr)
            g_expand = simplify(g_expr)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho $f(x) = %s$ và $g(x) = %s$.''' 
                             % (latex(f_expand), latex(g_expand)))

            ########################################################################
            # Nhận biết: Giới hạn tại nghiệm x1
            val_a = 0
            nb_da_1_d = r'\True $\lim_{x \to %s} f(x) = %s$' % (latex(x1), latex(val_a))
            nb_da_1_s = r'$\lim_{x \to %s} f(x) = %s$' % (latex(x1), latex(x1 + x2))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r'''$\lim_{x \to %s} f(x) = \lim_{x \to %s} \left[%s \right] = %s$.''' 
                            % (latex(x1), latex(x1), latex(f_expand), latex(val_a)))

            ########################################################################
            # Thông hiểu: Giới hạn tổ hợp tại điểm x=2 (hoặc x1+1)
            x_val_b = x1 + 1
            res_b = 2 * f_expand.subs(x, x_val_b) - g_expand.subs(x, x_val_b)
            th_da_1_d = r'\True $\lim_{x \to %s} [2f(x) - g(x)] = %s$' % (latex(x_val_b), latex(res_b))
            th_da_1_s = r'$\lim_{x \to %s} [2f(x) - g(x)] = %s$' % (latex(x_val_b), latex(res_b + 5))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''$\lim_{x \to %s} [2f(x) - g(x)] = 2f(%s) - g(%s) = 2(%s) - (%s) = %s$.''' 
                            % (latex(x_val_b), latex(x_val_b), latex(x_val_b), 
                               latex(f_expand.subs(x, x_val_b)), latex(g_expand.subs(x, x_val_b)), latex(res_b)))

            ########################################################################
            # Vận dụng: Giới hạn f(x)/g(x) tại x -> x2 (Dạng 0/0)
            res_c = limit(f_expr / g_expr, x, x2)
            vd_da_1_d = r'\True $\lim_{x \to %s} \frac{f(x)}{g(x)} = %s$' % (latex(x2), latex(res_c))
            vd_da_1_s = r'$\lim_{x \to %s} \frac{f(x)}{g(x)} = %s$' % (latex(x2), latex(-res_c))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r'''$\lim_{x \to %s} \frac{f(x)}{g(x)} = \lim_{x \to %s} \frac{(x-%s)(x-%s)}{%s(x-%s)} = \lim_{x \to %s} \frac{x-%s}{%s} = %s$.''' 
                            % (latex(x2), latex(x2), latex(x1), latex(x2), latex(-k), latex(x2), 
                               latex(x2), latex(x1), latex(-k), latex(res_c)))

            ########################################################################
            # Vận dụng cao: Giới hạn [f(x)]^2/g(x) tại x -> x2
            res_d = 0
            vdc_da_1_d = r'\True $\lim_{x \to %s} \frac{[f(x)]^2}{g(x)} = %s$' % (latex(x2), latex(res_d))
            vdc_da_1_s = r'$\lim_{x \to %s} \frac{[f(x)]^2}{g(x)} = 1$' % (latex(x2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''$\lim_{x \to %s} \frac{[f(x)]^2}{g(x)} = \lim_{x \to %s} \frac{(x-%s)^2(x-%s)^2}{%s(x-%s)} = \lim_{x \to %s} \frac{(x-%s)^2(x-%s)}{%s} = 0$.''' 
                             % (latex(x2), latex(x2), latex(x1), latex(x2), latex(-k), latex(x2), 
                                latex(x2), latex(x1), latex(x2), latex(-k)))

            # Hàm đếm số đáp án đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp xáo trộn đáp án đúng/sai
            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)

                answers = [nb_da, th_da, vd_da, vdc_da]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung theo mẫu LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da) + '}\n'
                '{' + str(th_da) + '}\n'
                '{' + str(vd_da) + '}\n'
                '{' + str(vdc_da) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

