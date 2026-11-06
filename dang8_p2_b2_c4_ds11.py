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


def bt_dang8_p2_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # BƯỚC 1: NGẪU NHIÊN HÓA CÁC THÔNG SỐ CỦA ĐỀ BÀI
            # x0: điểm giới hạn (trong ảnh là 3)
            x_0 = randint(1, 6)
            # L: giới hạn của f(x) (trong ảnh là -2)
            L = random.choice([i for i in range(-9, 10) if i != 0])
            # n: số mũ của g(x) (trong ảnh là mũ 3 - chọn số lẻ để giống tính chất trong ảnh)
            n = random.choice([1, 3, 5])

            # Hàm g(x)
            g_expr = (x - x_0)**n

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $f(x)$ có $\lim_{x \to %s} f(x) = %s$ và $g(x) = (x - %s)^{%s}$.''' 
                             % (latex(x_0), latex(L), latex(x_0), latex(n)))

            ########################################################################
            # NHẬN BIẾT: Giới hạn của g(x)
            ########################################################################
            nb_da_1_d = r'\True $\lim_{x \to %s^-} g(x) = 0$' % (latex(x_0))
            nb_da_1_s = r'$\lim_{x \to %s^-} g(x) = %s$' % (latex(x_0), latex(L))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r'''Ta có $\lim_{x \to %s^-} g(x) = \lim_{x \to %s^-} (x - %s)^{%s} = 0$.''' 
                            % (latex(x_0), latex(x_0), latex(x_0), latex(n)))

            ########################################################################
            # THÔNG HIỂU: Giới hạn của 1/g(x)
            ########################################################################
            # Vì n lẻ và x -> x0+, g(x) luôn > 0 nên 1/g(x) -> +vô cùng
            th_da_1_d = r'\True $\lim_{x \to %s^+} \frac{1}{g(x)} = +\infty$' % (latex(x_0))
            th_da_1_s = r'$\lim_{x \to %s^+} \frac{1}{g(x)} = -\infty$' % (latex(x_0))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''Ta có: $\lim_{x \to %s^+} g(x) = 0$ và với mọi $x > %s$ thì $g(x) > 0$ (do $n=%s$ lẻ). 
                            Do đó $\lim_{x \to %s^+} \frac{1}{g(x)} = +\infty$.''' 
                            % (latex(x_0), latex(x_0), latex(n), latex(x_0)))

            ########################################################################
            # VẬN DỤNG: Giới hạn f(x)/g(x)
            ########################################################################
            # Kết quả phụ thuộc vào dấu của L
            kq_vd = "+\\infty" if L > 0 else "-\\infty"
            kq_vd_sai = "-\\infty" if L > 0 else "+\\infty"

            vd_da_1_d = r'\True $\lim_{x \to %s^+} \frac{f(x)}{g(x)} = %s$' % (latex(x_0), kq_vd)
            vd_da_1_s = r'$\lim_{x \to %s^+} \frac{f(x)}{g(x)} = %s$' % (latex(x_0), kq_vd_sai)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r'''Ta có: $\lim_{x \to %s^+} \frac{f(x)}{g(x)} = \lim_{x \to %s^+} f(x) \cdot \frac{1}{g(x)}$. 
                            Vì $\lim_{x \to %s^+} f(x) = %s$ và $\lim_{x \to %s^+} \frac{1}{g(x)} = +\infty$ nên giới hạn bằng $%s$.''' 
                            % (latex(x_0), latex(x_0), latex(x_0), latex(L), latex(x_0), kq_vd))

            ########################################################################
            # VẬN DỤNG CAO: Giới hạn 1/[f(x).g(x)]
            ########################################################################
            # Giới hạn này cũng phụ thuộc vào dấu của L
            kq_vdc = "+\\infty" if L > 0 else "-\\infty"
            kq_vdc_sai = "0"

            vdc_da_1_d = r'\True $\lim_{x \to %s^+} \frac{1}{f(x) \cdot g(x)} = %s$' % (latex(x_0), kq_vdc)
            vdc_da_1_s = r'$\lim_{x \to %s^+} \frac{1}{f(x) \cdot g(x)} = %s$' % (latex(x_0), kq_vdc_sai)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''Ta có $\lim_{x \to %s^+} \frac{1}{f(x) \cdot g(x)} = \lim_{x \to %s^+} \frac{1}{f(x)} \cdot \frac{1}{g(x)}$. 
                            Do $\lim_{x \to %s^+} \frac{1}{f(x)} = \frac{1}{%s}$ và $\lim_{x \to %s^+} \frac{1}{g(x)} = +\infty$ 
                            nên $\lim_{x \to %s^+} \frac{1}{f(x) \cdot g(x)} = %s$.''' 
                            % (latex(x_0), latex(x_0), latex(x_0), latex(L), latex(x_0), latex(x_0), kq_vdc))

            # Hàm đếm số câu đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp chọn đáp án đến khi có từ 1 đến 3 câu đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Xuất nội dung theo mẫu LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + nb_sel + '}\n'
                '{' + th_sel + '}\n'
                '{' + vd_sel + '}\n'
                '{' + vdc_sel + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_nb_1 + '\n'
                '\\item ' + loigiai_th_1 + '\n'
                '\\item ' + loigiai_vd_1 + '\n'
                '\\item ' + loigiai_vdc_1 + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

