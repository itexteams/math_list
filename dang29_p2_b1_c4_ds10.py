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


def bt_dang29_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            # B1 & B3: Nghiên cứu đề bài và thực hiện random hằng số k trong căn (x^2 + k)
            # Trong ảnh k = 2. Ta chọn ngẫu nhiên k trong khoảng [2, 10]
            k = random.randint(2, 10)
            f_x = sqrt(x**2 + k)

            # Nội dung câu hỏi
            noidungcauhoi = ('Cho hàm số $y = %s$.' % (latex(f_x)))

            ########################################################################
            # Nhận biết: Tập xác định
            nb_da_1_d = '\\True Tập xác định của hàm số là $\\mathscr{D}=\\mathbb{R}$'
            nb_da_1_s = 'Tập xác định của hàm số là $\\mathscr{D}=(0;+\\infty)$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('Điều kiện: $x^2 + %s \\ge 0, \\forall x \\in \\mathbb{R}$. Tập xác định $\\mathscr{D}=\\mathbb{R}$.' % (k))

            ########################################################################
            # Thông hiểu: Điểm thuộc đồ thị (Tính f(sqrt(k+c)))
            # Chọn một giá trị x_0 sao cho x_0^2 + k là số chính phương để đẹp bài toán
            # Hoặc đơn giản lấy x = sqrt(7) như đề bài
            x_val_tex = '\\sqrt{7}'
            y_val = sqrt(7 + k)
            nb_m_point = 'M\\left(\\sqrt{7}; %s\\right)' % (latex(y_val))

            th_da_1_d = '\\True Điểm $%s$ thuộc đồ thị hàm số' % (nb_m_point)
            th_da_1_s = 'Điểm $M\\left(\\sqrt{7}; %s\\right)$ thuộc đồ thị hàm số' % (latex(y_val + 1))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('Ta có $f(\\sqrt{7}) = \\sqrt{(\\sqrt{7})^2 + %s} = %s$ nên điểm $%s$ thuộc đồ thị hàm số.' % (k, latex(y_val), nb_m_point))

            ########################################################################
            # Vận dụng: Giao điểm với trục tung (f(0))
            y_0 = sqrt(k)
            vd_da_1_d = '\\True Hàm số cắt trục tung tại điểm $I(0; %s)$' % (latex(y_0))
            vd_da_1_s = '\\True Hàm số cắt trục hoành tại điểm $I(0; %s)$' % (latex(y_0)) # Sai vì (0; y) là trục tung
            # Lưu ý: Trong ảnh ghi "cắt trục hoành tại I(0; sqrt(2))" là sai kiến thức (phải là trục tung)
            # Ở đây ta giả định đáp án đúng là Trục Tung.

            list_vd_da_1 = [vd_da_1_d, 'Hàm số cắt trục hoành tại điểm $I(%s; 0)$' % (latex(y_0))]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('Ta có $f(0) = \\sqrt{0^2 + %s} = %s \\Rightarrow$ Hàm số cắt trục tung tại $I(0; %s)$.' % (k, latex(y_0), latex(y_0)))

            ########################################################################
            # Vận dụng cao: Tính đơn điệu
            vdc_da_1_d = '\\True Hàm số đồng biến trên khoảng $(0; +\\infty)$'
            vdc_da_1_s = 'Hàm số nghịch biến trên khoảng $(0; +\\infty)$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('Với mọi $x_1, x_2 \\in \\mathbb{R}$ và $x_1 < x_2$. Ta có:\\\\'
                             '$f(x_1) - f(x_2) = \\sqrt{x_1^2 + %s} - \\sqrt{x_2^2 + %s} = \\frac{x_1^2 - x_2^2}{\\sqrt{x_1^2 + %s} + \\sqrt{x_2^2 + %s}}$.\\\\'
                             'Suy ra $\\frac{f(x_1) - f(x_2)}{x_1 - x_2} = \\frac{x_1 + x_2}{\\sqrt{x_1^2 + %s} + \\sqrt{x_2^2 + %s}}$.\\\\'
                             'Nếu $0 < x_1 < x_2$ thì $x_1 + x_2 > 0 \\Rightarrow \\frac{f(x_1) - f(x_2)}{x_1 - x_2} > 0$.\\\\'
                             'Vậy hàm số đồng biến trên $(0; +\\infty)$.' % (k, k, k, k, k, k))

            ########################################################################
            # Xử lý trộn và kiểm tra số lượng câu đúng
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

            # Xuất nội dung theo mẫu yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

