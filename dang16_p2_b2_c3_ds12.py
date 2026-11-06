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


def bt_dang16_p2_b2_c3_ds12(self):
            # Khai báo biến
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Random hệ số k của sqrt(x), ví dụ k chạy từ 2 đến 6. Trong ảnh mẫu k = 3.
            k = random.randint(2, 6)
            # Cận tích phân cố định là 1 và 4 để đảm bảo khai căn đẹp như đề bài
            c_duoi = 1
            c_tren = 4

            # Định nghĩa hàm số f(x)
            f = (1 - k*sqrt(x))/x

            # Tính toán các giá trị để làm đáp án đúng
            # a) Tích phân f'(x)
            val_a = f.subs(x, c_tren) - f.subs(x, c_duoi)

            # b) Tích phân f(x)
            # Tích phân của 1/x - k*x**(-1/2) là ln(x) - 2*k*sqrt(x)
            integ_f = ln(x) - 2*k*sqrt(x)
            val_b = integ_f.subs(x, c_tren) - integ_f.subs(x, c_duoi)

            # c) Tích phân x*f(x)
            xf = x * f # Kết quả là 1 - k*sqrt(x)
            integ_xf = integrate(xf, x)
            val_c = integ_xf.subs(x, c_tren) - integ_xf.subs(x, c_duoi)

            # d) Tích phân [f'(x) + 2x.f(x)]
            val_d = val_a + 2 * val_c

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Trên khoảng $(0;+\infty)$, cho hàm số $f(x) = \dfrac{%s}{x}$.''' 
                             % (latex(1 - k*sqrt(x))))

            ########################################################################
            # Nhận biết (Câu a) ############################################
            nb_da_1_d = r'''\True $\int_{%s}^{%s} f'(x) \text{d}x = %s$''' % (c_duoi, c_tren, latex(val_a))
            nb_da_1_s = r'''$\int_{%s}^{%s} f'(x) \text{d}x = %s$''' % (c_duoi, c_tren, latex(-val_a))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r'''Ta có $\int_{%s}^{%s} f'(x) \text{d}x = f(x) \Big|_{%s}^{%s} = f(%s) - f(%s) = %s$.''' 
                            % (c_duoi, c_tren, c_duoi, c_tren, c_tren, c_duoi, latex(val_a)))

            ########################################################################
            # Thông hiểu (Câu b) ############################################
            th_da_1_d = r'\True $\int_{%s}^{%s} f(x) \text{d}x = \ln %s - %s$' % (c_duoi, c_tren, c_tren, latex(2*k*(sqrt(c_tren)-sqrt(c_duoi))))
            th_da_1_s = r'$\int_{%s}^{%s} f(x) \text{d}x = \ln %s + %s$' % (c_duoi, c_tren, c_tren, latex(2*k))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''Ta có $\int_{%s}^{%s} f(x) \text{d}x = \int_{%s}^{%s} \left( \frac{1}{x} - %s x^{-\frac{1}{2}} \right) \text{d}x = \left( \ln x - %s\sqrt{x} \right) \Big|_{%s}^{%s} = %s$.''' 
                            % (c_duoi, c_tren, c_duoi, c_tren, k, 2*k, c_duoi, c_tren, latex(val_b)))

            ########################################################################
            # Vận dụng (Câu c) ############################################
            vd_da_1_d = r'\True $\int_{%s}^{%s} x f(x) \text{d}x = %s$' % (c_duoi, c_tren, latex(val_c))
            vd_da_1_s = r'$\int_{%s}^{%s} x f(x) \text{d}x = %s$' % (c_duoi, c_tren, latex(val_c + 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r'''Ta có $\int_{%s}^{%s} x f(x) \text{d}x = \int_{%s}^{%s} (1 - %s\sqrt{x}) \text{d}x = \left( x - %s x^{\frac{3}{2}} \right) \Big|_{%s}^{%s} = %s$.''' 
                            % (c_duoi, c_tren, c_duoi, c_tren, k, latex(Rational(2*k, 3)), c_duoi, c_tren, latex(val_c)))

            ########################################################################
            # Vận dụng cao (Câu d) ############################################
            vdc_da_1_d = r'''\True $\int_{%s}^{%s} [f'(x) + 2x.f(x)] \text{d}x = %s$''' % (c_duoi, c_tren, latex(val_d))
            vdc_da_1_s = r'''$\int_{%s}^{%s} [f'(x) + 2x.f(x)] \text{d}x = %s$''' % (c_duoi, c_tren, latex(val_d - 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''Ta có $\int_{1}^{4} [f'(x) + 2x.f(x)] \text{d}x = \int_{1}^{4} f'(x) \text{d}x + 2\int_{1}^{4} xf(x) \text{d}x = %s + 2(%s) = %s$.''' 
                             % (latex(val_a), latex(val_c), latex(val_d)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp chọn đáp án ngẫu nhiên
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán lời giải tương ứng (do lời giải ở trên là cố định cho đáp án đúng, 
            # trong thực tế bạn có thể tùy biến thêm nếu muốn lời giải thay đổi theo đáp án sai)
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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

