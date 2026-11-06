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


def bt_dang13_p2_b1_c4_ds12(self):
            # Khai báo biến
            # x1, y1: bi xanh, đỏ hộp 1. x2, y2: bi xanh, đỏ hộp 2.
            x1 = random.randint(3, 5)
            y1 = random.randint(7, 10)
            x2 = random.randint(5, 8)
            y2 = random.randint(6, 9)

            # Tổng số bi
            n1 = x1 + y1
            n2 = x2 + y2
            n2_sau = n2 + 1 # Tổng bi hộp 2 sau khi chuyển

            # Tính toán các giá trị xác suất
            pa = Rational(x1, n1)
            pa_not = Rational(y1, n1)

            # P(B|A): Hộp 2 có (x2+1) xanh, y2 đỏ. Lấy 2 xanh.
            pb_a = Rational(math.comb(x2 + 1, 2), math.comb(n2_sau, 2))

            # P(B|A_not): Hộp 2 có x2 xanh, (y2+1) đỏ. Lấy 2 xanh.
            pb_a_not = Rational(math.comb(x2, 2), math.comb(n2_sau, 2))

            # Xác suất đầy đủ P(B)
            pb = pa * pb_a + pa_not * pb_a_not

            # Xác suất hậu nghiệm (Bayes)
            p_a_b = (pa * pb_a) / pb
            p_a_not_b = 1 - p_a_b

            # Nội dung câu hỏi
            noidungcauhoi = ('''Có hai hộp đựng các viên bi cùng kích thước và khối lượng. Hộp thứ nhất chứa %s viên bi xanh và %s viên bi đỏ, hộp thứ hai chứa %s viên bi xanh và %s viên bi đỏ. Lấy ngẫu nhiên 1 viên bi từ hộp thứ nhất chuyển sang hộp thứ hai, sau đó lấy ngẫu nhiên 2 viên bi từ hộp thứ hai. Gọi $A$ là biến cố "Viên bi được lấy ra từ hộp thứ nhất là xanh", $B$ là biến cố "Hai viên bi được lấy ra từ hộp thứ hai là xanh".''' 
                             %(latex(x1), latex(y1), latex(x2), latex(y2)))

            ########################################################################
            # Nhận biết 
            ########################################################################
            nb_da_1_d = '\\True Xác suất của biến cố $A$ là $%s$' %(latex(pa))
            nb_da_1_s = 'Xác suất của biến cố $A$ là $%s$' %(latex(pa_not))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Số cách lấy 1 viên bi bất kì từ hộp thứ nhất là %s và số cách lấy được 1 viên bi xanh từ hộp thứ nhất là %s. Vậy xác suất biến cố $A$ là $P(A) = \\frac{%s}{%s} = %s$.''' 
                            %(latex(n1), latex(x1), latex(x1), latex(n1), latex(pa)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu
            ########################################################################
            th_da_1_d = '\\True Xác suất của biến cố $B$ là $%s$' %(latex(pb))
            th_da_1_s = 'Xác suất của biến cố $B$ là $%s$' %(latex(pb_a))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Ta có $P(A) = %s \\Rightarrow P(\\overline{A}) = %s$. \\\\
            Xác suất lấy 2 bi xanh từ hộp 2 khi biết bi chuyển sang là xanh: $P(B|A) = \\frac{C_{%s}^2}{C_{%s}^2} = %s$. \\\\
            Xác suất lấy 2 bi xanh từ hộp 2 khi biết bi chuyển sang là đỏ: $P(B|\\overline{A}) = \\frac{C_{%s}^2}{C_{%s}^2} = %s$. \\\\
            Xác suất của biến cố $B$ là: $P(B) = P(A).P(B|A) + P(\\overline{A}).P(B|\\overline{A}) = %s.%s + %s.%s = %s$.''' 
                            %(latex(pa), latex(pa_not), latex(x2+1), latex(n2_sau), latex(pb_a), latex(x2), latex(n2_sau), latex(pb_a_not), latex(pa), latex(pb_a), latex(pa_not), latex(pb_a_not), latex(pb)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng
            ########################################################################
            vd_da_1_d = '\\True Giả sử 2 viên bi lấy ra từ hộp thứ hai là 2 viên bi xanh thì xác suất lấy được viên bi xanh ở hộp thứ nhất là $%s$' %(latex(p_a_b))
            vd_da_1_s = 'Giả sử 2 viên bi lấy ra từ hộp thứ hai là 2 viên bi xanh thì xác suất lấy được viên bi xanh ở hộp thứ nhất là $%s$' %(latex(pb))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta cần tính xác suất có điều kiện $P(A|B)$. \\\\
            Ta có $P(A|B) = \\frac{P(A).P(B|A)}{P(B)} = \\frac{%s . %s}{%s} = %s$.''' 
                            %(latex(pa), latex(pb_a), latex(pb), latex(p_a_b)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao
            ########################################################################
            vdc_da_1_d = '\\True Giả sử 2 viên bi lấy ra từ hộp thứ hai là 2 viên bi xanh thì xác suất lấy được viên bi đỏ ở hộp thứ nhất là $%s$' %(latex(p_a_not_b))
            vdc_da_1_s = 'Giả sử 2 viên bi lấy ra từ hộp thứ hai là 2 viên bi xanh thì xác suất lấy được viên bi đỏ ở hộp thứ nhất là $%s$' %(latex(p_a_b))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Ta cần tính xác suất có điều kiện $P(\\overline{A}|B)$. \\\\
            Ta có $P(\\overline{A}|B) = 1 - P(A|B) = 1 - %s = %s$.''' 
                             %(latex(p_a_b), latex(p_a_not_b)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo số lượng đáp án đúng từ 1 đến 3
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    shuffled_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                    shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]
                    break

            # Xuất nội dung theo cấu trúc yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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

