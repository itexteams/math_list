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


def bt_dang44_p2_b3_c4_ds10(self):
            # Khai báo biến
            Q = symbols('Q')
            # c: Chi phí cố định
            P = random.choice([1100, 1200, 1300, 1400, 1500])
            b = random.choice([150, 180, 200, 220])
            c = random.choice([120000, 130000, 140000, 150000])

            # Hàm tổng chi phí: C = Q^2 + b*Q + c
            # Doanh thu: R = P*Q
            # Hàm lợi nhuận: L = R - C = -Q^2 + (P-b)*Q - c
            coeff_Q = P - b
            delta = coeff_Q**2 - 4*c

            # Đảm bảo delta > 0 để bài toán có nghiệm (có điểm hòa vốn)
            while delta <= 0:
                P = random.randint(1200, 1600)
                coeff_Q = P - b
                delta = coeff_Q**2 - 4*c

            # Tính toán các giá trị chính xác
            Q1 = (coeff_Q - math.sqrt(delta)) / 2
            Q2 = (coeff_Q + math.sqrt(delta)) / 2
            Q_hoa_von = round(Q1)
            min_Q = math.ceil(Q1)
            max_Q = math.floor(Q2)
            max_profit = -(coeff_Q/2)**2 + coeff_Q*(coeff_Q/2) - c
            k_limit = int((max_profit // 10000 + 1) * 10000) # Một ngưỡng lợi nhuận không thể đạt tới

            # Nội dung câu hỏi
            noidungcauhoi = ('''Bộ phận nghiên cứu thị trường của một xí nghiệp xác định tổng chi phí để sản xuất $Q$ sản phẩm là $Q^2 + %sQ + %s$ (nghìn đồng). Giả sử giá mỗi sản phẩm bán ra thị trường là $%s$ nghìn đồng. Lợi nhuận là hiệu của doanh thu trừ đi tổng chi phí để sản xuất.''' 
                             %(latex(b), latex(c), latex(P)))

            ########################################################################
            # a) Nhận biết: Công thức hàm lợi nhuận
            ########################################################################
            correct_L = -Q**2 + coeff_Q*Q - c
            wrong_L = -Q**2 + (coeff_Q - 20)*Q - c

            nb_da_1_d = '\\True Lợi nhuận của xí nghiệp thu được sau khi bán hết $Q$ sản phẩm là $%s$' % (latex(correct_L))
            nb_da_1_s = 'Lợi nhuận của xí nghiệp thu được sau khi bán hết $Q$ sản phẩm là $%s$' % (latex(wrong_L))

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = ('''Doanh thu thu được khi bán $Q$ sản phẩm là $R(Q) = %sQ$. \\\\ Lợi nhuận là: $L(Q) = R(Q) - C(Q) = %sQ - (Q^2 + %sQ + %s) = %s$.''' 
                            % (latex(P), latex(P), latex(b), latex(c), latex(correct_L)))

            ########################################################################
            # b) Thông hiểu: Điểm hòa vốn
            ########################################################################
            th_da_1_d = '\\True Xí nghiệp sản xuất khoảng $%s$ sản phẩm là hòa vốn' % (latex(Q_hoa_von))
            th_da_1_s = 'Xí nghiệp sản xuất khoảng $%s$ sản phẩm là hòa vốn' % (latex(Q_hoa_von + 50))

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = ('''Để hòa vốn thì lợi nhuận bằng $0$, tức là: $-Q^2 + %sQ - %s = 0$. \\\\ Giải phương trình ta được $Q \\approx %s$ hoặc $Q \\approx %s$. Vậy sản xuất khoảng $%s$ sản phẩm thì hòa vốn.''' 
                            % (latex(coeff_Q), latex(c), round(Q1, 2), round(Q2, 2), latex(Q_hoa_von)))

            ########################################################################
            # c) Vận dụng: Điều kiện không bị lỗ
            ########################################################################
            vd_da_1_d = '\\True Điều kiện của số lượng sản phẩm để xí nghiệp không bị lỗ là $%s \\le Q \\le %s$' % (latex(min_Q), latex(max_Q))
            vd_da_1_s = 'Điều kiện của số lượng sản phẩm để xí nghiệp không bị lỗ là $%s \\le Q \\le %s$' % (latex(min_Q - 10), latex(max_Q + 10))

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = ('''Xí nghiệp không bị lỗ khi $L(Q) \\ge 0 \\Leftrightarrow -Q^2 + %sQ - %s \\ge 0$. \\\\ Nghiệm của bất phương trình là $%s \\le Q \\le %s$. \\\\ Vì $Q$ nguyên nên $%s \\le Q \\le %s$.''' 
                            % (latex(coeff_Q), latex(c), round(Q1, 2), round(Q2, 2), latex(min_Q), latex(max_Q)))

            ########################################################################
            # d) Vận dụng cao: Lợi nhuận tối đa
            ########################################################################
            vdc_da_1_d = '\\True Lợi nhuận của xí nghiệp không thể đạt $%s$ (nghìn đồng)' % (latex(k_limit))
            vdc_da_1_s = 'Lợi nhuận của xí nghiệp có thể đạt trên $%s$ (nghìn đồng)' % (latex(k_limit))

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = ('''Xét hàm số $L(Q) = -Q^2 + %sQ - %s$. \\\\ Đỉnh của parabol là $Q_0 = \\frac{-(%s)}{2(-1)} = %s$. \\\\ Lợi nhuận tối đa là $L(%s) = %s$ (nghìn đồng). \\\\ Vì $%s < %s$ nên lợi nhuận không thể đạt $%s$ nghìn đồng.''' 
                             % (latex(coeff_Q), latex(c), latex(coeff_Q), latex(coeff_Q/2), latex(coeff_Q/2), latex(max_profit), latex(max_profit), latex(k_limit), latex(k_limit)))

            # --- BƯỚC 2: XỬ LÝ ĐÁP ÁN ĐÚNG/SAI THEO MẪU ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Gán vào list để shuffle (tương ứng với cấu trúc mẫu)
            shuffled_answers = [ans_a, ans_b, ans_c, ans_d]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # --- BƯỚC 3: XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
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

