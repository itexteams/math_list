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


def bt_dang22_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            # Random hằng số a trong căn (x + a) để làm mới bài toán
            a_val = random.randint(1, 5) 

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = f(x) = \\sqrt{x + %s}$.''' % (latex(a_val)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Tập xác định của hàm số là $\\mathscr{D} = [%s; +\\infty)$' % (latex(-a_val))
            nb_da_1_s = 'Tập xác định của hàm số là $\\mathscr{D} = (%s; +\\infty)$' % (latex(-a_val))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Hàm số xác định $\\Leftrightarrow x + %s \\geq 0 \\Leftrightarrow x \\geq %s$. Vậy tập xác định $\\mathscr{D} = [%s; +\\infty)$.''' 
                            % (latex(a_val), latex(-a_val), latex(-a_val)))

            ########################################################################
            # Thông hiểu ############################################
            y0_val = sqrt(0 + a_val)
            th_da_1_d = '\\True Vì $0 \\in \\mathscr{D}$ và $%s = \\sqrt{0 + %s}$ nên $M(0; %s)$ thuộc đồ thị hàm số' % (latex(y0_val), latex(a_val), latex(y0_val))
            th_da_1_s = 'Vì $0 \\in \\mathscr{D}$ nên $M(0; 0)$ thuộc đồ thị hàm số'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Vì $0 \\in \\mathscr{D}$ và $%s = \\sqrt{0 + %s}$ nên $M(0; %s)$ thuộc đồ thị hàm số.''' 
                            % (latex(y0_val), latex(a_val), latex(y0_val)))

            ########################################################################
            # Vận dụng ############################################
            f1 = sqrt(1 + a_val)
            f3 = sqrt(3 + a_val)
            tong_f = f1 + f3
            gia_tri_gia = 5 # Giá trị gây nhiễu trong ảnh

            vd_da_1_d = '\\True Vì $f(1) + f(3) = %s + %s \\neq %s$' % (latex(f1), latex(f3), latex(gia_tri_gia))
            vd_da_1_s = 'Vì $f(1) + f(3) = %s$' % (latex(gia_tri_gia))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Vì $f(1) + f(3) = \\sqrt{1 + %s} + \\sqrt{3 + %s} = %s + %s \\neq %s$.''' 
                            % (latex(a_val), latex(a_val), latex(f1), latex(f3), latex(gia_tri_gia)))

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Hàm số đồng biến trên khoảng $(0; +\\infty)$'
            vdc_da_1_s = 'Hàm số nghịch biến trên khoảng $(0; +\\infty)$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Xét hàm số $y = f(x) = \\sqrt{x + %s}$ trên khoảng $(0; +\\infty)$. \\\\
            $\\forall x_1, x_2 \\in (0; +\\infty)$, $x_1 < x_2$, ta có: \\\\
            $f(x_1) - f(x_2) = \\sqrt{x_1 + %s} - \\sqrt{x_2 + %s} = \\frac{x_1 + %s - (x_2 + %s)}{\\sqrt{x_1 + %s} + \\sqrt{x_2 + %s}} = \\frac{x_1 - x_2}{\\sqrt{x_1 + %s} + \\sqrt{x_2 + %s}} < 0$. \\\\
            Suy ra $f(x_1) < f(x_2)$. \\\\
            Vậy hàm số đồng biến trên khoảng $(0; +\\infty)$.''' 
                            % (latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val)))

            # --- Logic kiểm tra số câu True (1-3 câu) ---
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

            # Xuất nội dung theo mẫu yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

