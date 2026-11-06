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


def bt_dang26_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1 & B3: Nghiên cứu và tạo thông số ngẫu nhiên
            # f(x) = (x - m) / (x^2 + n)
            m = random.randint(1, 3) 
            n = random.randint(2, 5)

            f = (x - m) / (x**2 + n)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=%s$.''' % (latex(f)))

            ########################################################################
            # Nhận biết 
            ########################################################################
            nb_da_1_d = '\\True Tập xác định của hàm số $y = f(x)$ là $\\mathbb{R}$'
            nb_da_1_s = 'Tập xác định của hàm số $y = f(x)$ là $\\mathbb{R} \\setminus \\{ %s \\}$' % (latex(n))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Tập xác định của hàm số $y = f(x)$ là $\\mathbb{R}$ vì $x^2 + %s > 0$ với mọi $x \\in \\mathbb{R}$.''' % (latex(n)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu
            ########################################################################
            # Tính toán giao điểm
            y_0 = -Rational(m, n) # f(0)
            x_int = m             # f(x)=0

            th_da_1_d = '\\True Đồ thị hàm số cắt trục hoành tại $x=%s$ và trục tung tại $y=%s$' % (latex(x_int), latex(y_0))
            th_da_1_s = 'Đồ thị hàm số cắt trục hoành tại $x=%s$ và trục tung tại $y=%s$' % (latex(y_0), latex(x_int))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Ta có $f(0)=%s$ và $f(x)=0 \\Leftrightarrow x-%s=0 \\Leftrightarrow x=%s$. Vậy nên đồ thị hàm số $y=f(x)$ cắt trục hoành, trục tung lần lượt tại $x=%s$ và $y=%s$.''' 
                            % (latex(y_0), latex(m), latex(x_int), latex(x_int), latex(y_0)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng
            ########################################################################
            # Xét tính nghịch biến trên khoảng (m, m+2) - Tương tự (1, 3) trong ảnh
            vd_da_1_d = '\\True Hàm số $y = f(x)$ nghịch biến trên khoảng $(%s; %s)$' % (m, m + 2)
            vd_da_1_s = '\\True Hàm số $y = f(x)$ đồng biến trên khoảng $(%s; %s)$' % (m, m + 2) # Để logic random True/False
            list_vd_da_1 = [vd_da_1_d, 'Hàm số $y = f(x)$ đồng biến trên khoảng $(%s; %s)$' % (m, m + 2)]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''$\\forall x_1, x_2 \\in (%s; %s), x_1 < x_2$, ta có: \\\\
            $f(x_1)-f(x_2) = \\frac{x_1-%s}{x_1^2+%s} - \\frac{x_2-%s}{x_2^2+%s} = \\frac{(x_2^2+%s)(x_1-%s)-(x_1^2+%s)(x_2-%s)}{(x_1^2+%s)(x_2^2+%s)}$ \\\\
            $= \\frac{x_1x_2(x_1-x_2) + (%s)(x_1^2-x_2^2) + %s(x_1-x_2)}{(x_1^2+%s)(x_2^2+%s)}$. \\\\
            Rõ ràng $\\forall x_1, x_2 \\in (%s; %s), x_1 < x_2$ thì $f(x_1)-f(x_2) < 0$. \\\\
            Vậy hàm số $y=f(x)$ nghịch biến trên khoảng $(%s; %s)$.''' 
                            % (m, m+2, m, n, m, n, n, m, n, m, n, n, m, n, n, n, m, m+2, m, m+2))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao
            ########################################################################
            # Tìm GTLN tương tự cách dùng Cauchy trong ảnh cho x > m
            # f(x) = (x-m)/(x^2+n). Xét 1/f(x) = (x^2+n)/(x-m) = (x-m) + (m^2+n)/(x-m) + 2m
            val_cauchy = 2*math.sqrt(m**2 + n)
            max_val_f = 1 / (val_cauchy + 2*m)
            x_max = m + math.sqrt(m**2 + n)

            vdc_da_1_d = '\\True Đồ thị hàm số $y=f(x)$ tiếp xúc với đường thẳng $y = \\frac{-%s + \\sqrt{%s}}{%s}$' % (m, m**2+n, 2*n) # Công thức rút gọn mẫu
            vdc_da_1_s = 'Hàm số $y=f(x)$ có giá trị lớn nhất bằng $1$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Xét $\\frac{x^2+%s}{x-%s} = x-%s + \\frac{%s}{x-%s} + %s \\ge 2\\sqrt{%s} + %s, \\forall x > %s$. \\\\
            Từ đó suy ra $f(x) = \\frac{x-%s}{x^2+%s} \\le \\frac{1}{2\\sqrt{%s} + %s}$. \\\\
            Dấu bằng xảy ra khi $x-%s = \\frac{%s}{x-%s} \\Leftrightarrow (x-%s)^2 = %s \\Leftrightarrow x = %s + \\sqrt{%s}$. \\\\
            Vậy đồ thị hàm số $y=f(x)$ tại $x = %s + \\sqrt{%s}$ tiếp xúc với đường thẳng $y = \\frac{1}{2\\sqrt{%s} + %s}$.''' 
                             % (n, m, m, m**2+n, m, 2*m, m**2+n, 2*m, m, m, n, m**2+n, 2*m, m, m**2+n, m, m, m**2+n, m, m**2+n, m, m**2+n, m**2+n, 2*m))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            # --- Phần logic chọn đáp án và in kết quả (Giữ nguyên mẫu) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)
                answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(ans_nb)+'}\n'
                '{'+str(ans_th)+'}\n'
                '{'+str(ans_vd)+'}\n'
                '{'+str(ans_vdc)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

