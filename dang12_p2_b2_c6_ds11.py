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


def bt_dang12_p2_b2_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            A, B = symbols('A B')

            # B3: Suy nghĩ tìm cách random bài toán
            # Thiết lập thông số ngẫu nhiên sao cho thỏa mãn các quy tắc xác suất
            # P(A) + P(B) - P(A giao B) <= 1 và P(A giao B) <= min(P(A), P(B))
            while True:
                pa_val = random.randint(55, 75)   # % người mua sách A
                pb_val = random.randint(60, 80)   # % người mua sách B
                pab_val = random.randint(40, min(pa_val, pb_val) - 5) # % mua cả hai

                if (pa_val + pb_val - pab_val) <= 95: # Đảm bảo tổng không vượt quá 100% (chừa chỗ cho người không mua gì)
                    break

            # Chuyển sang số thập phân dạng chuỗi có dấu phẩy
            def format_prob(val):
                return str(round(val / 100, 2)).replace('.', ',')

            s_pa = format_prob(pa_val)
            s_pb = format_prob(pb_val)
            s_pab = format_prob(pab_val)
            s_union = format_prob(pa_val + pb_val - pab_val)
            s_not_both = format_prob(100 - pab_val)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một nhà xuất bản phát hành hai cuốn sách $A$ và $B$. Thống kê cho thấy có $%s\\%%$ người mua sách $A$; $%s\\%%$ người mua sách $B$; $%s\\%%$ người mua cả sách $A$ và sách $B$. Chọn ngẫu nhiên một người mua. Gọi $A$ là biến cố: "người đó mua quyển sách $A$", $B$ là biến cố: "người đó mua quyển sách $B$".''' 
                             %(pa_val, pb_val, pab_val))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $P\\left(A\\right)=%s; P\\left(B\\right)=%s$' % (s_pa, s_pb)
            nb_da_1_s = '$P\\left(A\\right)=%s; P\\left(B\\right)=%s$' % (s_pb, s_pa)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = ('''Từ giả thiết, ta có xác suất người đó mua sách $A$ là $P\\left(A\\right)=\\frac{%s}{100}=%s$ và xác suất người đó mua sách $B$ là $P\\left(B\\right)=\\frac{%s}{100}=%s$.''' 
                            % (pa_val, s_pa, pb_val, s_pb))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Biến cố: "người mua đó mua cả sách $A$ và sách $B$" là biến cố $A \\cap B$.'
            th_da_1_s = 'Biến cố: "người mua đó mua cả sách $A$ và sách $B$" là biến cố $A \\cup B$.'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]
            loigiai_th_1 = ('''Biến cố mua cả hai cuốn sách $A$ và $B$ là giao của hai biến cố $A$ và $B$, ký hiệu là $A \\cap B$. Ta có $P\\left(A \\cap B\\right)=\\frac{%s}{100}=%s$.''' 
                            % (pab_val, s_pab))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Xác suất để người mua đó mua ít nhất một trong hai sách $A$ hoặc $B$ là: %s.' % (s_union)
            vd_da_1_s = 'Xác suất để người mua đó mua ít nhất một trong hai sách $A$ hoặc $B$ là: %s.' % (format_prob(pa_val + pb_val))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = ('''Biến cố "người mua đó mua ít nhất một trong hai sách" là biến cố hợp $A \\cup B$. \\\\
                            Ta có $P\\left(A \\cup B\\right) = P\\left(A\\right) + P\\left(B\\right) - P\\left(A \\cap B\\right) = %s + %s - %s = %s$.''' 
                            % (s_pa, s_pb, s_pab, s_union))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Xác suất để người mua đó không mua cả sách $A$ và sách $B$ là: %s.' % (s_not_both)
            vdc_da_1_s = 'Xác suất để người mua đó không mua cả sách $A$ và sách $B$ là: %s.' % (format_prob(100 - (pa_val + pb_val - pab_val)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = ('''Biến cố "không mua cả sách $A$ và sách $B$" là biến cố đối của biến cố "mua cả hai sách $A$ và $B$". \\\\
                            Xác suất cần tìm là $P\\left(\\overline{A \\cap B}\\right) = 1 - P\\left(A \\cap B\\right) = 1 - %s = %s$.''' 
                            % (s_pab, s_not_both))
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    # Cập nhật lại các biến đã chọn để dùng cho content
                    final_nb_ans, final_nb_sol = (nb_sel, loigiai_nb_1)
                    final_th_ans, final_th_sol = (th_sel, loigiai_th_1)
                    final_vd_ans, final_vd_sol = (vd_sel, loigiai_vd_1)
                    final_vdc_ans, final_vdc_sol = (vdc_sel, loigiai_vdc_1)
                    break

            # Xuất câu hỏi với đáp án và lời giải
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(final_nb_ans)+'}\n'
                '{'+str(final_th_ans)+'}\n'
                '{'+str(final_vd_ans)+'}\n'
                '{'+str(final_vdc_ans)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(final_nb_sol)+'\n'
                '\\item '+str(final_th_sol)+'\n'
                '\\item '+str(final_vd_sol)+'\n'
                '\\item '+str(final_vdc_sol)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

