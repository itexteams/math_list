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


def bt_dang32_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            t = symbols('t')

            # B3: Tìm cách random bài toán
            # Random các hệ số a và b để tạo ra các bài toán khác nhau
            # Ở bài gốc: a = 2/3, b = 6
            val_a = random.choice([Rational(1, 3), Rational(2, 3), 1, Rational(4, 3), 2])
            val_b = random.choice([3, 4, 5, 6, 8, 10])

            # Hàm h'(t) = 6at^2 + 2bt
            f_derivative = 6*val_a*t**2 + 2*val_b*t
            # Nguyên hàm h(t) = 2at^3 + bt^2 (do h(0) = 0)
            h_t = 2*val_a*t**3 + val_b*t**2

            # Tính các giá trị cụ thể để làm đáp án
            vol_3 = h_t.subs(t, 3)
            vol_6 = h_t.subs(t, 6)
            vol_9 = h_t.subs(t, 9)
            vol_3_to_6 = vol_6 - vol_3

            # Nội dung câu hỏi gốc
            noidungcauhoi = r'''Một máy bơm nước vào bể chứa nước. Gọi $h(t)$ là thể tích nước bơm được sau $t$ giây. Cho $h'(t) = 6at^2 + 2bt$ và ban đầu bể không có nước.'''

            ########################################################################
            # Nhận biết: Công thức tính thể tích tại thời điểm t
            ########################################################################
            nb_da_1_d = r'\True Sau 3 giây thì thể tích nước trong bể là $h(3) = \int_0^3 (6at^2 + 2bt) \text{d}t$'
            nb_da_1_s = r'Sau 3 giây thì thể tích nước trong bể là $h(3) = \int_0^3 (6at^2 + 2bt)^2 \text{d}t$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = r'''Thể tích nước bơm được sau $t$ giây là $h(t) = \int_0^t h'(u) \text{d}u$. \\ Vậy sau 3 giây thể tích là $h(3) = \int_0^3 (6at^2 + 2bt) \text{d}t$.'''

            ########################################################################
            # Thông hiểu: Tính toán biểu thức h(6) theo a, b
            ########################################################################
            expr_6 = 432*val_a + 36*val_b
            th_da_1_d = r'\True Sau 6 giây thể tích nước trong bể là $432a + 36b$'
            th_da_1_s = r'Sau 6 giây thể tích nước trong bể là $216a + 36b$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = r'''Ta có $h(6) = \int_0^6 (6at^2 + 2bt) \text{d}t = (2at^3 + bt^2) \Big|_0^6 = 2a \cdot 6^3 + b \cdot 6^2 = 432a + 36b$.'''

            ########################################################################
            # Vận dụng: Tính lượng nước bơm được trong một khoảng thời gian
            ########################################################################
            # Giả sử đề bài cho vol_3 và vol_6 cụ thể
            vd_da_1_d = r'\True Nếu thể tích nước sau 3 giây là $%s m^3$ và sau 6 giây là $%s m^3$ thì lượng nước bơm được từ giây thứ 3 đến giây thứ 6 là $%s m^3$' % (latex(vol_3), latex(vol_6), latex(vol_3_to_6))
            vd_da_1_s = r'Nếu thể tích nước sau 3 giây là $%s m^3$ và sau 6 giây là $%s m^3$ thì lượng nước bơm được từ giây thứ 3 đến giây thứ 6 là $%s m^3$' % (latex(vol_3), latex(vol_6), latex(vol_6))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = r'''Lượng nước bơm được từ giây thứ 3 đến giây thứ 6 là \\ $V = h(6) - h(3) = %s - %s = %s (m^3)$.''' % (latex(vol_6), latex(vol_3), latex(vol_3_to_6))

            ########################################################################
            # Vận dụng cao: Tìm a, b và tính h(9)
            ########################################################################
            vdc_da_1_d = r'\True Giả sử sau 3 giây thể tích là $%s m^3$ và sau 6 giây là $%s m^3$. Khi đó sau 9 giây thể tích nước là $%s m^3$' % (latex(vol_3), latex(vol_6), latex(vol_9))
            vdc_da_1_s = r'Giả sử sau 3 giây thể tích là $%s m^3$ và sau 6 giây là $%s m^3$. Khi đó sau 9 giây thể tích nước là $%s m^3$' % (latex(vol_3), latex(vol_6), latex(vol_6 + vol_3))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = r'''Từ giả thiết ta có hệ phương trình: $\begin{cases} 54a + 9b = %s \\ 432a + 36b = %s \end{cases} \Rightarrow \begin{cases} a = %s \\ b = %s \end{cases}$. \\ Khi đó sau 9 giây thể tích là: $h(9) = 2 \cdot %s \cdot 9^3 + %s \cdot 9^2 = %s (m^3)$.''' % (latex(vol_3), latex(vol_6), latex(val_a), latex(val_b), latex(val_a), latex(val_b), latex(vol_9))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp xáo trộn cho đến khi số đáp án đúng hợp lý (1 đến 3)
            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                current_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

