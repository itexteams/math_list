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


def bt_dang55_p1_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Cấu trúc: x + 2xf(x) = [f'(x)]^2 => sqrt(x) = f'(x)/sqrt(2f(x)+1)
            # Nguyên hàm: 2/3 * x^(3/2) + C = sqrt(2f(x)+1)
            # Tại x=1: 2/3 + C = sqrt(2f(1)+1). Đặt sqrt(2f(1)+1) = k
            # Chọn k sao cho f(1) đẹp. k nên là số hữu tỉ.

            # Chọn ngẫu nhiên các thông số
            # k = sqrt(2f(1)+1)
            k_vals = [Rational(2, 1), Rational(3, 1), Rational(5, 2)] 
            k = random.choice(k_vals)

            # f(1) = (k^2 - 1)/2
            f1 = (k**2 - 1) / 2

            # Cận trên b của tích phân (thường chọn số chính phương để sqrt(x) đẹp)
            b_vals = [4, 9]
            b = random.choice(b_vals)

            # Tính hằng số C
            C = k - Rational(2, 3)

            # Xác định hàm f(x)
            # sqrt(2f(x)+1) = 2/3 * x**(3/2) + C
            # f(x) = [(2/3 * x**(3/2) + C)^2 - 1] / 2
            expr_sqrt = Rational(2, 3) * x * sqrt(x) + C
            f_x = (expr_sqrt**2 - 1) / 2
            f_x_expanded = expand(f_x)

            # Tính tích phân I từ 1 đến b
            I_val = integrate(f_x, (x, 1, b))

            # B4: Điều chỉnh các phương án sai
            def generate_distractors(correct_val):
                distractors = set()
                while len(distractors) < 3:
                    # Tạo phương án sai bằng cách thay đổi tử số hoặc cộng trừ phân số
                    offset = random.choice([Rational(1, 1), Rational(2, 1), Rational(1, 45), Rational(10, 45)])
                    direction = random.choice([1, -1])
                    wrong = correct_val + direction * offset
                    if wrong != correct_val and wrong > 0:
                        distractors.add(wrong)
                return list(distractors)

            wrong_answers = generate_distractors(I_val)

            # Chuẩn bị nội dung hiển thị
            # Chuyển đổi sang LaTeX
            f1_latex = latex(f1)
            b_latex = latex(b)
            I_latex = latex(I_val)
            f_x_expanded_latex = latex(f_x_expanded)
            C_latex = latex(C)

            # B2: Viết lại bài toán theo mẫu code
            noidungcauhoi = (r'''Cho hàm số $f(x)$ có đạo hàm và đồng biến trên $[1; %s]$, thỏa mãn $x + 2xf(x) = [f'(x)]^2$ với mọi $x \in [1; %s]$. Biết $f(1) = %s$. Tích phân $I = \int_1^{%s} f(x) \text{d} x$ bằng'''
                             %(b_latex, b_latex, f1_latex, b_latex))

            # Các đáp án
            da_d = r'\True $%s$' % I_latex
            da_s1 = r'$%s$' % latex(wrong_answers[0])
            da_s2 = r'$%s$' % latex(wrong_answers[1])
            da_s3 = r'$%s$' % latex(wrong_answers[2])

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết
            # Tính toán các bước trung gian cho lời giải
            step_sqrt_fx = simplify(sqrt(2*f1 + 1))
            f_x_integrated = integrate(f_x, x)

            loigiai = (r'''Do $f(x)$ đồng biến trên $[1; %s]$ nên $f(x) \geq f(1) = %s > -\frac{1}{2}$, ngoài ra $f'(x) \geq 0, \forall x \in [1; %s]$. \\
            Khi đó ta có biến đổi sau:
            $$x + 2xf(x) = [f'(x)]^2 \Leftrightarrow \frac{f'(x)}{\sqrt{2f(x)+1}} = \sqrt{x}$$
            $$\Leftrightarrow \left(\sqrt{2f(x)+1}\right)' = \left(\frac{2}{3}\sqrt{x^3} + C\right)' \Leftrightarrow \sqrt{2f(x)+1} = \frac{2}{3}\sqrt{x^3} + C$$
            Mà $f(1) = %s \Rightarrow C = %s \Rightarrow f(x) = \frac{\left(\frac{2}{3}\sqrt{x^3} + %s\right)^2 - 1}{2} = %s.$ \\
            Vậy $I = \int_1^{%s} f(x) \text{d}x = \left( %s \right) \bigg|_1^{%s} = %s.$'''
                       %(b_latex, f1_latex, b_latex, f1_latex, C_latex, C_latex, f_x_expanded_latex, b_latex, latex(f_x_integrated), b_latex, I_latex))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

