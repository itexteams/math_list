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


def bt_dang7_p2_b1_c1_ds10(self):
    # Khai báo biến
    x = symbols('x')

    # B3: Random bài toán
    # Random hằng số c trong biểu thức x > c/x để tạo biến thể
    c = random.choice([1, 2, 3, 4]) 

    # Nội dung câu hỏi
    noidungcauhoi = '''Cho mệnh đề chứa biến $P(x):$ "$x > \\frac{%s}{x}$". Xét tính đúng sai của các câu sau:''' % (latex(c))

    def check_p(val, c_val):
        """Hàm kiểm tra tính đúng sai của mệnh đề P(val)"""
        if val == 0: return False
        return val > (c_val / val)

    ######################################################################## Nhận biết (Câu a) ############################################
    val_a = random.choice([1, 2, 3, 4,5,6]) 
    is_a_true = check_p(val_a, c)
    # Tạo đáp án
    nb_da_1_d = r'\True P($%s$)' % latex(val_a)
    nb_da_1_s = r'P($%s$)' % latex(val_a)
    list_nb_da_1 = [nb_da_1_d if is_a_true else nb_da_1_s]
    # Lời giải
    loigiai_nb_1 = r'Ta có $P(%s): %s > \frac{%s}{%s}$ là mệnh đề %s.' % (
        latex(val_a), latex(val_a), latex(c), latex(val_a), "đúng" if is_a_true else "sai"
    )
    list_nb_2 = [loigiai_nb_1]

    ######################################################################## Thông hiểu (Câu b) ############################################
    val_b = -Rational(1, 3)
    is_b_true = check_p(val_b, c)
    # Tạo đáp án
    th_da_1_d = r'\True P$\left( %s \right)$' % latex(val_b)
    th_da_1_s = r'P$\left( %s \right)$' % latex(val_b)
    list_th_da_1 = [th_da_1_d if is_b_true else th_da_1_s]
    # Lời giải
    loigiai_th_1 = r'Ta có $P\left( %s \right): %s > %s$ là mệnh đề %s.' % (
        latex(val_b), latex(val_b), latex(c/val_b), "đúng" if is_b_true else "sai"
    )
    list_th_2 = [loigiai_th_1]

    ######################################################################## Vận dụng (Câu c) ############################################
    # Kiểm tra ∀x ∈ N, P(x) (Trong N* thường xét từ 1, 2, 3...)
    # Với x > c/x, nếu c >= 1 thì x=1 luôn làm mệnh đề sai hoặc cần kiểm tra kỹ
    is_c_true = all(check_p(n, c) for n in range(1, 11))
    vd_da_1_d = r'\True $\forall x \in \mathbb{N}, P(x)$'
    vd_da_1_s = r'$\forall x \in \mathbb{N}, P(x)$'
    list_vd_da_1 = [vd_da_1_d if is_c_true else vd_da_1_s]
    # Lời giải
    loigiai_vd_1 = r'Mệnh đề $\forall x \in \mathbb{N}, P(x)$ là %s.' % ("đúng" if is_c_true else "sai")
    if not is_c_true:
        loigiai_vd_1 += r' Vì với $x=1$, $P(1)$ là mệnh đề sai.'
    list_vd_2 = [loigiai_vd_1]

    ######################################################################## Vận dụng cao (Câu d) ############################################
    # Kiểm tra ∃x ∈ N, P(x)
    is_d_true = any(check_p(n, c) for n in range(1, 11))
    vdc_da_1_d = r'\True $\exists x \in \mathbb{N}, P(x)$'
    vdc_da_1_s = r'$\exists x \in \mathbb{N}, P(x)$'
    list_vdc_da_1 = [vdc_da_1_d if is_d_true else vdc_da_1_s]
    # Lời giải
    loigiai_vdc_1 = r'Mệnh đề $\exists x \in \mathbb{N}, P(x)$ là %s.' % ("đúng" if is_d_true else "sai")
    if is_d_true:
        # Tìm một ví dụ x thỏa mãn để đưa vào lời giải
        example_x = next(n for n in range(1, 11) if check_p(n, c))
        loigiai_vdc_1 += r' Vì với $x=%s$, $%s > \frac{%s}{%s}$ là mệnh đề đúng.' % (example_x, example_x, c, example_x)
    list_vdc_2 = [loigiai_vdc_1]

    # --- Hậu xử lý và xuất bản (Giữ nguyên cấu trúc mẫu của bạn) ---
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        ans_a = random.choice([r'\True ' + list_nb_da_1[0].replace('\\True ', ''), list_nb_da_1[0].replace('\\True ', '')])
        ans_b = random.choice([r'\True ' + list_th_da_1[0].replace('\\True ', ''), list_th_da_1[0].replace('\\True ', '')])
        ans_c = random.choice([r'\True ' + list_vd_da_1[0].replace('\\True ', ''), list_vd_da_1[0].replace('\\True ', '')])
        ans_d = random.choice([r'\True ' + list_vdc_da_1[0].replace('\\True ', ''), list_vdc_da_1[0].replace('\\True ', '')])

        # Logic kiểm tra: Chỉ dấu \True khi mệnh đề thực sự đúng
        # Để đơn giản và đúng yêu cầu random trắc nghiệm đúng sai:
        temp_ans = [
            (r'\True ' if is_a_true else '') + list_nb_da_1[0].replace('\\True ', ''),
            (r'\True ' if is_b_true else '') + list_th_da_1[0].replace('\\True ', ''),
            (r'\True ' if is_c_true else '') + list_vd_da_1[0].replace('\\True ', ''),
            (r'\True ' if is_d_true else '') + list_vdc_da_1[0].replace('\\True ', '')
        ]
        # Lưu ý: Trong trắc nghiệm Đúng/Sai mẫu mới, ta thường giữ nguyên phát biểu và 
        # học sinh chọn Đúng/Sai. Ở đây code tạo ra trạng thái Đúng (\True) cố định theo toán học.
        break

    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' +
        str(noidungcauhoi) + '\n' +
        '\\choiceTFn \n'
        '{' + str(temp_ans[0]) + '}\n'
        '{' + str(temp_ans[1]) + '}\n'
        '{' + str(temp_ans[2]) + '}\n'
        '{' + str(temp_ans[3]) + '}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item ' + str(list_nb_2[0]) + '\n'
        '\\item ' + str(list_th_2[0]) + '\n'
        '\\item ' + str(list_vd_2[0]) + '\n'
        '\\item ' + str(list_vdc_2[0]) + '\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage}\n')
    return content

