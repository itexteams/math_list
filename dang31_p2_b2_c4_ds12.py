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


def bt_dang31_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Tổng số học sinh (N)
            N = random.choice([800, 1000, 1200])
            # Số học sinh tham gia CLB Thể thao (nA)
            nA = random.randint(35, 55) * N // 100 
            n_notA = N - nA
            # Số học sinh tham gia CLB và biết bơi (nAB)
            nAB = random.randint(nA // 3, nA // 2)
            # Số học sinh KHÔNG tham gia CLB nhưng biết bơi (n_notAB)
            n_notAB = random.randint(n_notA // 4, n_notA // 3)

            # Tính toán các xác suất dạng Rational
            pA = Rational(nA, N)
            pB_given_notA = Rational(n_notAB, n_notA)
            total_B = nAB + n_notAB
            pB = Rational(total_B, N)
            pB_given_A = Rational(nAB, nA)
            pA_given_B = Rational(nAB, total_B)

            # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Trường THPT X có %s học sinh, trong đó có %s học sinh tham gia câu lạc bộ thể thao. Trong số các học sinh tham gia câu lạc bộ thể thao của trường có %s học sinh biết bơi. Trong số các học sinh của trường không tham gia câu lạc bộ thể thao có %s học sinh biết bơi. Chọn ngẫu nhiên một học sinh của trường THPT X.\\\\
            Gọi $A$ là biến cố: "Chọn được học sinh thuộc câu lạc bộ thể thao".\\\\
            Gọi $B$ là biến cố: "Chọn được học sinh biết bơi".''' 
            %(N, nA, nAB, n_notAB))

            ########################################################################
            # Nhận biết (Xác suất P(A))
            ########################################################################
            nb_da_1_d = '\\True Xác suất $P(A)=%s$' % (latex(pA))
            nb_da_1_s = 'Xác suất $P(A)=%s$' % (latex(pA + Rational(1, 100)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Xác suất $P(A) = \\frac{%s}{%s} = %s$.''' 
                            % (nA, N, latex(pA)))

            ########################################################################
            # Thông hiểu (Xác suất điều kiện P(B|not A))
            ########################################################################
            th_da_1_d = '\\True Xác suất có điều kiện $P(B | \\bar{A}) = %s$' % (latex(pB_given_notA))
            th_da_1_s = 'Xác suất có điều kiện $P(B | \\bar{A}) = %s$' % (latex(pB_given_notA + Rational(1, 20)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Số học sinh không tham gia câu lạc bộ là: $%s - %s = %s$. \\\\
            Xác suất có điều kiện $P(B | \\bar{A}) = \\frac{%s}{%s} = %s$.''' 
                            % (N, nA, n_notA, n_notAB, n_notA, latex(pB_given_notA)))

            ########################################################################
            # Vận dụng (Xác suất P(B))
            ########################################################################
            vd_da_1_d = '\\True Xác suất $P(B) = %s$' % (latex(pB))
            vd_da_1_s = 'Xác suất $P(B) = %s$' % (latex(pB - Rational(1, 50)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Số học sinh biết bơi là: $%s + %s = %s$. \\\\
            Xác suất $P(B) = \\frac{%s}{%s} = %s$.''' 
                            % (nAB, n_notAB, total_B, total_B, N, latex(pB)))

            ########################################################################
            # Vận dụng cao (Xác suất Bayes P(A|B))
            ########################################################################
            # Tính giá trị xấp xỉ để giữ lại câu chữ về làm tròn nếu cần, nhưng đáp án vẫn là Rational
            approx_val = round(float(pA_given_B), 2)
            approx_str = str(approx_val).replace('.', ',')

            vdc_da_1_d = '\\True Xác suất chọn được học sinh thuộc câu lạc bộ thể thao mà học sinh đó biết bơi bằng $%s$' % (latex(pA_given_B))
            vdc_da_1_s = 'Xác suất chọn được học sinh thuộc câu lạc bộ thể thao mà học sinh đó biết bơi bằng $%s$' % (latex(pA_given_B + Rational(1, 100)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Ta có $P(B|A) = \\frac{%s}{%s} = %s$. \\\\
            Áp dụng công thức Bayes, xác suất chọn được học sinh thuộc câu lạc bộ thể thao mà học sinh đó biết bơi là: \\\\
            $P(A|B) = \\frac{P(A) \\cdot P(B|A)}{P(B)} = \\frac{%s \\cdot %s}{%s} = %s$.''' 
                             % (nAB, nA, latex(pB_given_A), latex(pA), latex(pB_given_A), latex(pB), latex(pA_given_B)))

            # --- BƯỚC 3: KIỂM TRA ĐIỀU KIỆN ĐÁP ÁN ĐÚNG ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_da_1, th_da_1, vd_da_1, vdc_da_1]) <= 3:
                    break

            # --- BƯỚC 4: XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

