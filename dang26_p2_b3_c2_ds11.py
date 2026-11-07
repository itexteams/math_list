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


def bt_dang26_p2_b3_c2_ds11(self):
    # Khai báo và random dữ liệu bài toán: Cấp số nhân (u_n)
    # u_1: số hạng đầu, q: công bội, n_end: số số hạng của dãy hữu hạn
    while True:
        u1 = random.randint(2, 5)
        q = random.randint(2, 4)
        n_end = random.randint(8, 11)  # Số số hạng của cấp số nhân hữu hạn
        # Giữ giá trị vừa phải để không bị tràn số quá lớn
        if u1 * (q ** (n_end - 1)) <= 1000000:
            break
    
    u2 = u1 * q
    u3 = u2 * q
    u_last = u1 * (q ** (n_end - 1))
    
    # Chọn số hạng thứ k để hỏi ở ý b (thường là n_end - 1 hoặc một số cụ thể)
    k = n_end - 1
    u_k = u1 * (q ** (k - 1))
    
    # Chọn m số hạng đầu để tính tổng ở ý c
    m = random.randint(5, 7)
    S_m = u1 * (q ** m - 1) // (q - 1)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho cấp số nhân $(u_n)$ gồm các số hạng $%s; %s; %s; \\ldots; %s$.''' % (latex(u1), latex(u2), latex(u3), latex(u_last)))
    
    ############################################################################## Nhận biết #################################################
    # Các đáp án ý a: Số hạng đầu và công bội
    # Mệnh đề đúng: u_1 = u1, q = q
    nb_da_1_d = '\\True Số hạng đầu và công bội của cấp số nhân lần lượt là $u_1 = %s$, $q = %s$' % (latex(u1), latex(q))
    # Mệnh đề sai: hoán đổi hoặc làm sai công bội
    q_wrong = q + 1 if random.choice([True, False]) else max(1, q - 1)
    nb_da_1_s = 'Số hạng đầu và công bội của cấp số nhân lần lượt là $u_1 = %s$, $q = %s$' % (latex(u1), latex(q_wrong))
    
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải ý a
    loigiai_nb_1 = ('''Số hạng đầu của cấp số nhân là $u_1 = %s$.\\\\ Công bội của cấp số nhân là $q = \\frac{u_2}{u_1} = \\frac{%s}{%s} = %s$.''' % (latex(u1), latex(u2), latex(u1), latex(q)))
    
    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################## Thông hiểu #################################################
    # Các đáp án ý b: Số hạng thứ k
    # Chuyển số k thành chữ tiếng Việt tương ứng
    doc_so = {7: 'bảy', 8: 'tám', 9: 'chín', 10: 'mười', 11: 'mười một'}
    k_str = doc_so.get(k, str(k))
    
    th_da_1_d = '\\True Số hạng thứ %s của cấp số nhân là $u_{%s} = %s$' % (k_str, latex(k), latex(u_k))
    u_k_wrong = u_k + random.choice([-q, q, 2 * q, -2 * q, 10])
    th_da_1_s = 'Số hạng thứ %s của cấp số nhân là $u_{%s} = %s$' % (k_str, latex(k), latex(u_k_wrong))
    
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải ý b
    loigiai_th_1 = ('''Số hạng thứ %s của cấp số nhân là:\\\\ $u_{%s} = u_1 \\cdot q^{%s-1} = %s \\cdot %s^{%s} = %s$.''' % (k_str, latex(k), latex(k), latex(u1), latex(q), latex(k - 1), latex(u_k)))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################## Vận dụng ###################################################
    # Các đáp án ý c: Tổng m số hạng đầu
    vd_da_1_d = '\\True Tổng của %s số hạng đầu của cấp số nhân là $S_{%s} = %s$' % (latex(m), latex(m), latex(S_m))
    S_m_wrong = S_m + random.choice([-1, 1, q, -q])
    vd_da_1_s = 'Tổng của %s số hạng đầu của cấp số nhân là $S_{%s} = %s$' % (latex(m), latex(m), latex(S_m_wrong))
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải ý c
    loigiai_vd_1 = ('''Tổng của %s số hạng đầu của cấp số nhân là:\\\\ $S_{%s} = \\frac{u_1(1 - q^{%s})}{1 - q} = \\frac{%s \\cdot (1 - %s^{%s})}{1 - %s} = %s$.''' % (latex(m), latex(m), latex(m), latex(u1), latex(q), latex(m), latex(q), latex(S_m)))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################## Vận dụng cao ###############################################
    # Các đáp án ý d: Số số hạng của cấp số nhân hữu hạn
    vdc_da_1_d = '\\True Cấp số nhân đã cho là dãy số hữu hạn gồm có %s số hạng' % (latex(n_end))
    n_wrong = n_end + random.choice([-1, 1, 2])
    vdc_da_1_s = 'Cấp số nhân đã cho là dãy số hữu hạn gồm có %s số hạng' % (latex(n_wrong))
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    # Tính số mũ của số hạng cuối để giải chi tiết
    power_val = u_last // u1
    
    loigiai_vdc_1 = ('''Gọi $n$ là số số hạng của cấp số nhân đã cho.\\\\ Số hạng cuối là $u_n = %s$.\\\\ Theo công thức số hạng tổng quát, ta có:\\\\ $u_n = u_1 \\cdot q^{n-1} \\Leftrightarrow %s \\cdot %s^{n-1} = %s \\Leftrightarrow %s^{n-1} = %s \\Leftrightarrow %s^{n-1} = %s^{%s} \\Leftrightarrow n - 1 = %s \\Leftrightarrow n = %s$.\\\\ Vậy cấp số nhân đã cho là dãy số hữu hạn gồm có %s số hạng.''' % (latex(u_last), latex(u1), latex(q), latex(u_last), latex(q), latex(power_val), latex(q), latex(q), latex(n_end - 1), latex(n_end - 1), latex(n_end), latex(n_end)))
    
    list_vdc_2 = [loigiai_vdc_1]
    
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    
    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
    
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
        
        if 1 <= true_count <= 3:
            break
    
    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
    '\\choiceTFn \n'
    '{' + str(shuffled_answers_nb[0]) + '}\n'
    '{' + str(shuffled_answers_th[0]) + '}\n'
    '{' + str(shuffled_answers_vd[0]) + '}\n'
    '{' + str(shuffled_answers_vdc[0]) + '}\n'
    '\\loigiai{ \n'
    '\\begin{enumEX}[a)]{1} \n'
    '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
    '\\item ' + str(shuffled_solutions_th[0]) + '\n'
    '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
    '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
    '\\end{enumEX}} \n'
    '\\end{ex}\n \\end{minipage}\n\n')
    
    print(content)