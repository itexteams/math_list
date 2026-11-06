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


def bt_dang33_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1 & B2: Thiết lập bài toán gốc và random tham số
            # Chọn m_val ngẫu nhiên để tạo các câu hỏi cụ thể (ví dụ a, b)
            m_a = random.randint(2, 5)
            m_b = random.randint(-5, -2)

            # Hàm số gốc: y = (m^2 - 1)x + (m - 1)
            noidungcauhoi = ('''Cho hàm số $y = (m^2 - 1)x + (m - 1)$.''')

            ########################################################################
            # Nhận biết: Kiểm tra với m cụ thể
            f_a_val = (m_a**2 - 1)
            g_a_val = (m_a - 1)
            nb_da_1_d = '\\True Khi $m = ' + str(m_a) + '$ hàm số trở thành $y = ' + str(f_a_val) + 'x + ' + str(g_a_val) + '$ đồng biến trên $\\mathbb{R}$'
            nb_da_1_s = 'Khi $m = ' + str(m_a) + '$ hàm số trở thành $y = ' + str(f_a_val) + 'x + ' + str(g_a_val) + '$ nghịch biến trên $\\mathbb{R}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Khi $m = ''' + str(m_a) + '''$ ta có $y = (''' + str(m_a) + '''^2 - 1)x + (''' + str(m_a) + ''' - 1) = ''' + str(f_a_val) + '''x + ''' + str(g_a_val) + '''$. Vì $''' + str(f_a_val) + ''' > 0$ nên hàm số đồng biến trên $\\mathbb{R}$.''')

            ########################################################################
            # Thông hiểu: Kiểm tra tính biến thiên và đồ thị
            f_b_val = (m_b**2 - 1)
            g_b_val = (m_b - 1)
            th_da_1_d = '\\True Khi $m = ' + str(m_b) + '$ đồ thị hàm số là đường thẳng đi lên từ trái qua phải'
            th_da_1_s = 'Khi $m = ' + str(m_b) + '$ đồ thị hàm số là đường thẳng đi xuống từ trái qua phải'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Khi $m = ''' + str(m_b) + '''$ ta có $y = ''' + str(f_b_val) + '''x + ''' + str(g_b_val) + '''$. Do $''' + str(f_b_val) + ''' > 0$ nên hàm số đồng biến, đồ thị là đường thẳng đi lên từ trái qua phải.''')

            ########################################################################
            # Vận dụng: Điều kiện nghịch biến
            vd_da_1_d = '\\True Hàm số nghịch biến trên $\\mathbb{R}$ khi $-1 < m < 1$'
            vd_da_1_s = 'Hàm số nghịch biến trên $\\mathbb{R}$ khi $m > 1$ hoặc $m < -1$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Hàm số nghịch biến trên $\\mathbb{R}$ khi hệ số góc $a < 0 \\Leftrightarrow m^2 - 1 < 0 \\Leftrightarrow -1 < m < 1$. Nếu $m$ nhận giá trị nguyên thì $m = 0$.''')

            ########################################################################
            # Vận dụng cao: Điều kiện đồng biến
            vdc_da_1_d = '\\True Hàm số đồng biến trên $\\mathbb{R}$ khi $m \\in (-\\infty; -1) \\cup (1; +\\infty)$'
            vdc_da_1_s = 'Hàm số đồng biến trên $\\mathbb{R}$ khi $m \\in (-1; 1)$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Hàm số đồng biến trên $\\mathbb{R}$ khi hệ số góc $a > 0 \\Leftrightarrow m^2 - 1 > 0 \\Leftrightarrow \\left[\\begin{aligned} & m < -1 \\\\ & m > 1 \\end{aligned}\\right. \\Leftrightarrow m \\in (-\\infty; -1) \\cup (1; +\\infty)$.''')

            # Các bước xử lý xáo trộn và kiểm tra true_count (giữ nguyên logic mẫu)
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                current_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    shuffled_answers = current_answers
                    break

            # Map lại lời giải tương ứng (đơn giản hóa vì mỗi mục chỉ có 1 lời giải logic)
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
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

