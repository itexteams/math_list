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


def bt_dang36_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Tỉ lệ nữ (ví dụ từ 30% đến 60%)
            nu_pct = random.randint(30, 60)
            nam_pct = 100 - nu_pct

            # Tỉ lệ mua bảo hiểm của nữ (ví dụ từ 5% đến 15%)
            nu_ins_pct = random.randint(5, 15)
            # Tỉ lệ mua bảo hiểm của nam (ví dụ từ 4% đến 12%, đảm bảo khác nữ)
            nam_ins_pct = random.randint(4, 12)
            while nam_ins_pct == nu_ins_pct:
                nam_ins_pct = random.randint(4, 12)

            # Chuyển sang số hữu tỉ để tính toán chính xác
            P_A = Rational(nu_pct, 100)        # P(A): Nhân viên là nữ
            P_notA = Rational(nam_pct, 100)    # P(not A): Nhân viên là nam
            P_B_A = Rational(nu_ins_pct, 100)  # P(B|A): Nữ mua bảo hiểm
            P_B_notA = Rational(nam_ins_pct, 100) # P(B|not A): Nam mua bảo hiểm

            # Xác suất tổng quát P(B): Nhân viên có mua bảo hiểm
            P_B = P_A * P_B_A + P_notA * P_B_notA

            # Xác suất hậu nghiệm (Bayes)
            P_A_B = (P_A * P_B_A) / P_B        # P(Nữ | Mua bảo hiểm)
            P_notA_B = (P_notA * P_B_notA) / P_B # P(Nam | Mua bảo hiểm)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một doanh nghiệp có $%s\\%%$ nhân viên là nữ. Tỉ lệ nhân viên nữ và tỉ lệ nhân viên nam mua bảo hiểm nhân thọ lần lượt là $%s\\%%$ và $%s\\%%$. Chọn ngẫu nhiên một nhân viên của doanh nghiệp.''' 
                             % (latex(nu_pct), latex(nu_ins_pct), latex(nam_ins_pct)))

            ########################################################################
            # Nhận biết: Tính P(B)
            ########################################################################
            P_B_val = float(P_B)
            nb_da_1_d = '\\True Xác suất nhân viên được chọn có mua bảo hiểm nhân thọ là $%s$' % (latex(P_B_val))
            nb_da_1_s = 'Xác suất nhân viên được chọn có mua bảo hiểm nhân thọ là $%s$' % (latex(round(P_B_val + 0.002, 3)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Gọi $A$ là biến cố: "Nhân viên được chọn là nữ", $B$ là biến cố: "Nhân viên được chọn có mua bảo hiểm nhân thọ".\\\\ Theo đề bài: $P(A)=%s; P(\\bar{A})=%s; P(B|A)=%s; P(B|\\bar{A})=%s$.\\\\ Xác suất nhân viên có mua bảo hiểm là:\\\\ $P(B) = P(A).P(B|A) + P(\\bar{A}).P(B|\\bar{A}) = %s.%s + %s.%s = %s$.'''
                            % (latex(P_A), latex(P_notA), latex(P_B_A), latex(P_B_notA), latex(P_A), latex(P_B_A), latex(P_notA), latex(P_B_notA), latex(P_B_val)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Tính P(A|B) - Nữ biết đã mua BH
            ########################################################################
            th_da_1_d = '\\True Biết rằng nhân viên được chọn có mua bảo hiểm nhân thọ. Xác suất nhân viên đó là nữ là $%s$' % (latex(P_A_B))
            th_da_1_s = 'Biết rằng nhân viên được chọn có mua bảo hiểm nhân thọ. Xác suất nhân viên đó là nữ là $%s$' % (latex(P_A_B * Rational(9, 10)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Xác suất nhân viên là nữ khi biết người đó mua bảo hiểm:\\\\ $P(A|B) = \\frac{P(AB)}{P(B)} = \\frac{P(A).P(B|A)}{P(B)} = \\frac{%s.%s}{%s} = %s$.'''
                            % (latex(P_A), latex(P_B_A), latex(P_B_val), latex(P_A_B)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Tính P(not A|B) - Nam biết đã mua BH
            ########################################################################
            vd_da_1_d = '\\True Biết rằng nhân viên được chọn có mua bảo hiểm nhân thọ. Xác suất nhân viên đó là nam là $%s$' % (latex(P_notA_B))
            vd_da_1_s = 'Biết rằng nhân viên được chọn có mua bảo hiểm nhân thọ. Xác suất nhân viên đó là nam là $%s$' % (latex(P_notA_B + Rational(1, 50)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Xác suất nhân viên là nam khi biết người đó mua bảo hiểm:\\\\ $P(\\bar{A}|B) = \\frac{P(\\bar{A}B)}{P(B)} = \\frac{P(\\bar{A}).P(B|\\bar{A})}{P(B)} = \\frac{%s.%s}{%s} = %s$.'''
                            % (latex(P_notA), latex(P_B_notA), latex(P_B_val), latex(P_notA_B)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: So sánh
            ########################################################################
            if P_A_B > P_notA_B:
                so_sanh_text = "nữ nhiều hơn là nam"
                nguoc_lai_text = "nam nhiều hơn là nữ"
            else:
                so_sanh_text = "nam nhiều hơn là nữ"
                nguoc_lai_text = "nữ nhiều hơn là nam"

            vdc_da_1_d = '\\True Biết rằng nhân viên được chọn có mua bảo hiểm nhân thọ. Khi đó nhân viên đó là %s' % (so_sanh_text)
            vdc_da_1_s = 'Biết rằng nhân viên được chọn có mua bảo hiểm nhân thọ. Khi đó nhân viên đó là %s' % (nguoc_lai_text)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''So sánh hai xác suất hậu nghiệm: Ta có $P(A|B) = %s$ và $P(\\bar{A}|B) = %s$. \\\\ Vì $%s %s %s$ nên nếu nhân viên được chọn có mua bảo hiểm nhân thọ thì khả năng nhân viên đó là %s cao hơn.'''
                             % (latex(P_A_B), latex(P_notA_B), latex(P_A_B), ">" if P_A_B > P_notA_B else "<", latex(P_notA_B), "nữ" if P_A_B > P_notA_B else "nam"))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Logic chọn số câu đúng từ 1 đến 3
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán lại và trộn (để đảm bảo tính ngẫu nhiên như mẫu)
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
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

