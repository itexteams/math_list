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


def bt_dang8_p2_b3_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # B1-Nghiên cứu đề bài và B3-Suy nghĩ tìm cách random bài toán
            # Random số mũ n và hằng số c trong biểu thức (xy + c)^n
            n = random.randint(4, 6)
            c = random.choice([-2, -1, 1, 2])
            # Biểu thức hiển thị
            if c > 0:
                bt_hien_thi = "xy + %s" % latex(c)
            else:
                bt_hien_thi = "xy %s" % latex(c)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Khai triển $Q = \\left( %s \\right)^{%s}$.''' 
                             %(bt_hien_thi, latex(n)))

            # Hàm tính hệ số của x^m * y^m trong (xy + c)^n
            # Công thức tổng quát: C(n, k) * (xy)^(n-k) * c^k
            # Để có x^m * y^m thì n-k = m => k = n-m
            # Hệ số là: C(n, n-m) * c^(n-m)
            def get_coeff(n_val, c_val, m_val):
                return binomial(n_val, n_val - m_val) * (c_val**(n_val - m_val))

            ########################################################################
            # Nhận biết: Kiểm tra số hạng chứa x^2y^2
            m_nb = 2
            coeff_nb = get_coeff(n, c, m_nb)
            nb_da_1_d = '\\True Số hạng có chứa $x^2 y^2$ là $%s x^2 y^2$' % (latex(coeff_nb))
            nb_da_1_s = 'Số hạng có chứa $x^2 y^2$ là $%s x^2 y^2$' % (latex(-coeff_nb if coeff_nb !=0 else 10))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Số hạng tổng quát trong khai triển là $T_{k+1} = C_{%s}^{k} \\left( xy \\right)^{%s-k} \\left( %s \\right)^k$.\\\\
            Để có số hạng chứa $x^2 y^2$, ta chọn $%s-k = 2 \\Leftrightarrow k = %s$.\\\\
            Số hạng đó là: $C_{%s}^{%s} \\left( xy \\right)^2 \\left( %s \\right)^{%s} = %s x^2 y^2$.'''
                            % (latex(n), latex(n), latex(c), latex(n), latex(n-2), latex(n), latex(n-2), latex(c), latex(n-2), latex(coeff_nb)))

            ########################################################################
            # Thông hiểu: Hệ số của x^{n-1}y^{n-1}
            m_th = n - 1
            coeff_th = get_coeff(n, c, m_th)
            th_da_1_d = '\\True Hệ số của $x^{%s} y^{%s}$ trong khai triển là $%s$' % (latex(m_th), latex(m_th), latex(coeff_th))
            th_da_1_s = 'Hệ số của $x^{%s} y^{%s}$ trong khai triển là $%s$' % (latex(m_th), latex(m_th), latex(coeff_th + random.choice([-2, 2])))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Hệ số của $x^{%s} y^{%s}$ ứng với $%s-k = %s \\Leftrightarrow k = 1$.\\\\
            Hệ số cần tìm là: $C_{%s}^1 \\cdot \\left( %s \\right)^1 = %s$.'''
                            % (latex(m_th), latex(m_th), latex(n), latex(m_th), latex(n), latex(c), latex(coeff_th)))

            ########################################################################
            # Vận dụng: Hệ số của x^{n-2}y^{n-2}
            m_vd = n - 2
            coeff_vd = get_coeff(n, c, m_vd)
            vd_da_1_d = '\\True Hệ số của $x^{%s} y^{%s}$ trong khai triển là $%s$' % (latex(m_vd), latex(m_vd), latex(coeff_vd))
            vd_da_1_s = 'Hệ số của $x^{%s} y^{%s}$ trong khai triển là $%s$' % (latex(m_vd), latex(m_vd), latex(-coeff_vd if coeff_vd !=0 else 5))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Hệ số của $x^{%s} y^{%s}$ ứng với $%s-k = %s \\Leftrightarrow k = 2$.\\\\
            Hệ số cần tìm là: $C_{%s}^2 \\cdot \\left( %s \\right)^2 = %s$.'''
                            % (latex(m_vd), latex(m_vd), latex(n), latex(m_vd), latex(n), latex(c), latex(coeff_vd)))

            ########################################################################
            # Vận dụng cao: Hệ số của xy (tức x^1y^1)
            m_vdc = 1
            coeff_vdc = get_coeff(n, c, m_vdc)
            vdc_da_1_d = '\\True Hệ số của $xy$ trong khai triển là $%s$' % (latex(coeff_vdc))
            vdc_da_1_s = 'Hệ số của $xy$ trong khai triển là $%s$' % (latex(coeff_vdc * -1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Hệ số của $xy$ ứng với $%s-k = 1 \\Leftrightarrow k = %s$.\\\\
            Hệ số cần tìm là: $C_{%s}^{%s} \\cdot \\left( %s \\right)^{%s} = %s$.'''
                             % (latex(n), latex(n-1), latex(n), latex(n-1), latex(c), latex(n-1), latex(coeff_vdc)))

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

            # Gán lại vào list để xuất bản
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

