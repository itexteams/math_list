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


def bt_dang19_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM
            # Hàm số có dạng y = ax^2 + bx + c. 
            # Để giống bài mẫu y = -x^2 + 6x - 5:
            # Chọn a âm để có giá trị lớn nhất.
            a_val = -1 
            # Chọn b chẵn để đỉnh và nghiệm đẹp (hoành độ đỉnh -b/2a)
            b_val = random.randint(2, 5) * 2 
            # Chọn c ngẫu nhiên
            c_val = random.randint(-7, -2)

            f = a_val*x**2 + b_val*x + c_val
            # Tọa độ đỉnh I(x_i, y_i)
            x_i = Rational(-b_val, 2*a_val)
            y_i = f.subs(x, x_i)
            # Trục tung
            y_tung = f.subs(x, 0)
            # Biến m cho câu d
            m_val = random.randint(1, 10)

            # Nội dung câu hỏi
            noidungcauhoi = ('Cho hàm số $y = ' + latex(f) + '$.')

            ########################################################################
            # a) Giao điểm với trục tung
            nb_da_1_d = '\\True Tọa độ giao điểm của đồ thị hàm số với trục tung là $A(0; ' + str(y_tung) + ')$.'
            nb_da_1_s = 'Tọa độ giao điểm của đồ thị hàm số với trục tung là $A(' + str(y_tung) + '; 0)$.'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('Tọa độ giao điểm của đồ thị hàm số với trục tung tại điểm $A(0;' + str(y_tung) + ')$.')

            ########################################################################
            # b) Tọa độ đỉnh
            th_da_1_d = '\\True Đỉnh của đồ thị hàm số là điểm $I(' + latex(x_i) + '; ' + latex(y_i) + ')$.'
            th_da_1_s = 'Đỉnh của đồ thị hàm số là điểm $I(' + latex(-x_i) + '; ' + latex(y_i) + ')$.'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('Đỉnh của đồ thị hàm số là điểm $I\\left(\\frac{-b}{2a}; \\frac{-\\Delta}{4a}\\right) = I(' + latex(x_i) + ';' + latex(y_i) + ')$.')

            ########################################################################
            # c) Giá trị lớn nhất
            vd_da_1_d = '\\True Giá trị lớn nhất của hàm số là ' + latex(y_i) + '.'
            vd_da_1_s = 'Giá trị lớn nhất của hàm số là ' + latex(x_i) + '.'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('Xét hàm số $y = f(x) = ' + latex(f) + '$, có $a < 0$ nên giá trị lớn nhất của hàm số là $y = f\\left(-\\frac{b}{2a}\\right) = f(' + latex(x_i) + ') = ' + latex(y_i) + '$.')

            ########################################################################
            # d) Tương giao (Tìm m để có 2 nghiệm phân biệt)
            # Phương trình: ax^2 + bx + c = 4x - m <=> ax^2 + (b-4)x + c + m = 0
            # delta' = ((b-4)/2)^2 - a*(c+m) > 0
            b_new = b_val - 4
            delta_half = Rational(b_new, 2)
            # Biểu thức delta' > 0: delta_half**2 - a_val*(c_val + m) > 0
            # 1*(c_val + m) > -delta_half**2 => m > -delta_half**2 - c_val
            m_threshold = - (delta_half**2) - c_val

            vdc_da_1_d = '\\True Đường thẳng $d: y = 4x - m$ cắt đồ thị $(P)$ tại $2$ điểm phân biệt khi $m > ' + latex(m_threshold) + '$.'
            vdc_da_1_s = 'Đường thẳng $d: y = 4x - m$ cắt đồ thị $(P)$ tại $2$ điểm phân biệt khi $m < ' + latex(m_threshold) + '$.'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('Xét phương trình hoành độ giao điểm của đường thẳng $d$ và đồ thị $(P)$ là: \\\\ $' + 
                             latex(f) + ' = 4x - m \\Leftrightarrow x^2 - ' + str(b_new) + 'x + ' + str(-c_val) + ' - m = 0 \\quad (1) $ \\\\ ' +
                             'Đường thẳng $d$ cắt đồ thị $(P)$ tại $2$ điểm phân biệt khi và chỉ khi phương trình (1) có $2$ nghiệm phân biệt \\\\ ' +
                             '$\\Leftrightarrow \\Delta\' = ' + latex(delta_half**2) + ' - (' + str(-c_val) + ' - m) > 0 \\Leftrightarrow m > ' + latex(m_threshold) + '$.')

            ########################################################################
            # Xử lý chọn đáp án Đúng/Sai ngẫu nhiên (1-3 câu đúng)
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_da, th_da, vd_da, vdc_da]) <= 3:
                    break

            # Xuất nội dung
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

