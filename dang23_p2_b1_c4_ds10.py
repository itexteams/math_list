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


def bt_dang23_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            m_val = random.choice([i for i in range(-5, 6) if i != 0]) # Random tham số m khác 0
            # Trong hình m = 1 -> f(x) = x/(x-1)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=\\frac{x}{x-%s}$.''' % (latex(m_val)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Tập xác định của hàm số là $\\mathscr{D}=\\mathbb{R} \\setminus \\{%s\\}$' % (latex(m_val))
            nb_da_1_s = 'Tập xác định của hàm số là $\\mathscr{D}=\\mathbb{R}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Nội dung lời giải
            loigiai_nb_1 = ('''Hàm số xác định khi $x-%s \\neq 0 \\Leftrightarrow x \\neq %s$. \\ Vậy tập xác định là $\\mathscr{D}=\\mathbb{R} \\setminus \\{%s\\}$.''' 
                            % (latex(m_val), latex(m_val), latex(m_val)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip([nb_da_1], list_nb_2))

            ########################################################################
            # Thông hiểu ############################################
            # Đạo hàm f'(x) = -m / (x-m)^2. Vì x/(x-m) có đạo hàm là (1*(x-m) - 1*x)/(x-m)^2 = -m/(x-m)^2
            tu_so_dao_ham = -m_val
            dau_db = "đồng biến" if tu_so_dao_ham > 0 else "nghịch biến"
            dau_db_s = "nghịch biến" if tu_so_dao_ham > 0 else "đồng biến"

            th_da_1_d = '\\True Hàm số %s trên khoảng $(%s; +\\infty)$' % (dau_db, latex(m_val))
            th_da_1_s = 'Hàm số %s trên khoảng $(%s; +\\infty)$' % (dau_db_s, latex(m_val))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Với mọi $x_1, x_2 \\in (%s; +\\infty)$ và $x_1 < x_2$, ta có $f(x_1)-f(x_2) = \\frac{x_1}{x_1-%s} - \\frac{x_2}{x_2-%s} = \\frac{%s(x_2-x_1)}{(x_1-%s)(x_2-%s)}$. \\ Vì $x_1, x_2 > %s$ nên mẫu số dương. Nếu $x_2-x_1 > 0$, dấu của hiệu phụ thuộc vào tử số. Suy ra hàm số %s trên các khoảng xác định.''' 
                            % (latex(m_val), latex(m_val), latex(m_val), latex(m_val), latex(m_val), latex(m_val), latex(m_val), dau_db))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip([th_da_1], list_th_2))

            ########################################################################
            # Vận dụng ############################################
            x1_vd = m_val + 1
            x2_vd = m_val + 2
            # Nếu nghịch biến (m>0), f(x1) > f(x2). Nếu đồng biến (m<0), f(x1) < f(x2).
            if m_val > 0:
                vd_da_1_d = '\\True $f(%s) > f(%s)$' % (latex(x1_vd), latex(x2_vd))
                vd_da_1_s = '$f(%s) < f(%s)$' % (latex(x1_vd), latex(x2_vd))
            else:
                vd_da_1_d = '\\True $f(%s) < f(%s)$' % (latex(x1_vd), latex(x2_vd))
                vd_da_1_s = '$f(%s) > f(%s)$' % (latex(x1_vd), latex(x2_vd))

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Vì hàm số %s trên khoảng $(%s; +\\infty)$ và $%s < %s$ nên ta có so sánh tương ứng giữa $f(%s)$ và $f(%s)$.''' 
                            % (dau_db, latex(m_val), latex(x1_vd), latex(x2_vd), latex(x1_vd), latex(x2_vd)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip([vd_da_1], list_vd_2))

            ########################################################################
            # Vận dụng cao ############################################
            # Bài toán: Tìm m để hàm số y = x / (x - (2m-1)) xác định trên (0;1]
            # Điều kiện: 2m-1 không thuộc (0;1] => 2m-1 <= 0 hoặc 2m-1 > 1
            vdc_da_1_d = '\\True Giá trị của $m$ để hàm số xác định trên $(0;1]$ là $m \\le \\frac{1}{2}$ hoặc $m > 1$'
            vdc_da_1_s = 'Giá trị của $m$ để hàm số xác định trên $(0;1]$ là $0 < m \\le 1$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Hàm số xác định khi $x \\neq 2m-1$. Để hàm số xác định trên $(0;1]$ thì $2m-1 \\notin (0;1]$. \\\\ Suy ra $\\left[\\begin{aligned} & 2m-1 \\le 0 \\\\ & 2m-1 > 1 \\end{aligned} \\right. \\Leftrightarrow \\left[\\begin{aligned} & m \\le \\frac{1}{2} \\\\ & m > 1 \\end{aligned} \\right. $.''' )

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))

            ########################################################################
            # Logic kiểm tra số câu Đúng/Sai
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

