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


def bt_dang25_p2_b3_c3_ds12(self):
                # Khai báo biến
                x = symbols('x')

                # Bước 1: Random thông số bài toán
                # f(x) = (1/a)*x^3 - x^2. Nghiệm là x=0 và x=a.
                a_val = random.randint(2, 6) 
                f_x = Rational(1, a_val)*x**3 - x**2

                # Nội dung câu hỏi
                noidungcauhoi = r'''Cho hình phẳng $(H)$ giới hạn bởi đường cong $y = f(x) = %s$ và trục hoành.''' % (latex(f_x))

                ########################################################################
                # Nhận biết: Hoành độ giao điểm
                ########################################################################
                nb_da_1_d = r'\True Đồ thị hàm số $y=f(x)$ cắt trục hoành tại hai điểm phân biệt có hoành độ $x=0, x=%s$' % (a_val)
                nb_da_1_s = r'Đồ thị hàm số $y=f(x)$ cắt trục hoành tại ba điểm phân biệt'
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

                loigiai_nb_1 = r'''Phương trình hoành độ giao điểm: $%s = 0 \Leftrightarrow x^2\left(\frac{x}{%s}-1\right)=0 \Leftrightarrow x=0$ hoặc $x=%s$. Vậy đồ thị cắt trục hoành tại 2 điểm.''' % (latex(f_x), a_val, a_val)

                ########################################################################
                # Thông hiểu: Nguyên hàm cơ bản
                ########################################################################
                nguyen_ham = integrate(f_x, x)
                th_da_1_d = r'\True $\int f(x) \text{d}x = %s + C$' % (latex(nguyen_ham))
                th_da_1_s = r'$\int f(x) \text{d}x = \frac{1}{%s}x^4 - x^3 + C$' % (a_val * 2)
                list_th_da_1 = [th_da_1_d, th_da_1_s]

                loigiai_th_1 = r'''Áp dụng công thức nguyên hàm cơ bản: $\int \left( \frac{x^3}{%s} - x^2 \right) \text{d}x = \frac{x^4}{%s} - \frac{x^3}{3} + C$.''' % (a_val, 4*a_val)

                ########################################################################
                # Vận dụng: Diện tích hình phẳng (S = a^3/12)
                ########################################################################
                dien_tich_val = Rational(a_val**3, 12)
                vd_da_1_d = r'\True Diện tích hình phẳng $(H)$ là $S = %s$' % (latex(dien_tich_val))
                vd_da_1_s = r'Diện tích hình phẳng $(H)$ là $S = \frac{%s}{3}$' % (a_val**2)
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

                loigiai_vd_1 = r'''Diện tích hình phẳng là $S = \int_{0}^{%s} |f(x)| \text{d}x = \int_{0}^{%s} (x^2 - \frac{x^3}{%s}) \text{d}x = \left( \frac{x^3}{3} - \frac{x^4}{%s} \right) \bigg|_0^{%s} = %s$.''' % (a_val, a_val, a_val, 4*a_val, a_val, latex(dien_tich_val))

                ########################################################################
                # Vận dụng cao: Thể tích khối tròn xoay (V = pi * a^5 / 105)
                ########################################################################
                the_tich_val = Rational(a_val**5, 105)
                vdc_da_1_d = r'\True Thể tích khối tròn xoay khi quay $(H)$ quanh trục $Ox$ là $V = %s\pi$' % (latex(the_tich_val))
                vdc_da_1_s = r'Thể tích khối tròn xoay khi quay $(H)$ quanh trục $Ox$ là $V = %s$' % (latex(the_tich_val))
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

                loigiai_vdc_1 = r'''Thể tích khối tròn xoay là $V = \pi \int_{0}^{%s} f^2(x) \text{d}x = \pi \int_{0}^{%s} \left( \frac{x^3}{%s} - x^2 \right)^2 \text{d}x = %s\pi$.''' % (a_val, a_val, a_val, latex(the_tich_val))

                # --- Logic chọn bộ đáp án thỏa mãn 1-3 câu đúng ---
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

                # Xuất nội dung theo định dạng mẫu dang24
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                    '\\choiceTFn \n'
                    '{' + ans_nb + '}\n'
                    '{' + ans_th + '}\n'
                    '{' + ans_vd + '}\n'
                    '{' + ans_vdc + '}\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item ' + loigiai_nb_1 + '\n'
                    '\\item ' + loigiai_th_1 + '\n'
                    '\\item ' + loigiai_vd_1 + '\n'
                    '\\item ' + loigiai_vdc_1 + '\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n\\end{minipage}\n\n')
                return content

