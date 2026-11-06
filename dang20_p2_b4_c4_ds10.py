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


def bt_dang20_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1: Nghiên cứu đề bài và random tham số
            # Phương trình gốc: x^2 + sqrt(x+k) = k. Trong ảnh k = 5.
            # Chọn k ngẫu nhiên để bài toán đa dạng
            k = random.choice([3, 4, 5, 6, 7])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình $x^2 + \\sqrt{x+%s} = %s$.''' % (latex(k), latex(k)))

            # Tính toán các giá trị để phục vụ lời giải và đáp án
            # Điều kiện: x >= -k
            # Biến đổi: (x^2 - (x+k)) + (x + sqrt(x+k)) = 0 
            # <=> (x - sqrt(x+k))(x + sqrt(x+k)) + (x + sqrt(x+k)) = 0
            # <=> (x + sqrt(x+k))(x - sqrt(x+k) + 1) = 0

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Điều kiện xác định của phương trình là $x \\geq -%s$' % (latex(k))
            nb_da_1_s = 'Điều kiện xác định của phương trình là $x \\geq %s$' % (latex(k))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Điều kiện xác định: $x + %s \\geq 0 \\Leftrightarrow x \\geq -%s$.''' % (latex(k), latex(k)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Phương trình đã cho tương đương với $(x + \\sqrt{x+%s})(x - \\sqrt{x+%s} + 1) = 0$' % (latex(k), latex(k))
            th_da_1_s = 'Phương trình đã cho tương đương với $(x + \\sqrt{x+%s})(x + \\sqrt{x+%s} + 1) = 0$' % (latex(k), latex(k))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Biến đổi phương trình: \\\\
            $x^2 + \\sqrt{x+%s} = %s \\Leftrightarrow x^2 - (x+%s) + x + \\sqrt{x+%s} = 0$ \\\\
            $\\Leftrightarrow (x - \\sqrt{x+%s})(x + \\sqrt{x+%s}) + (x + \\sqrt{x+%s}) = 0$ \\\\
            $\\Leftrightarrow (x + \\sqrt{x+%s})(x - \\sqrt{x+%s} + 1) = 0$.''' % (latex(k), latex(k), latex(k), latex(k), latex(k), latex(k), latex(k), latex(k), latex(k)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))

            ########################################################################
            # Vận dụng ############################################
            # Giải phương trình để đếm số nghiệm
            # TH1: sqrt(x+k) = -x (x <= 0) => x+k = x^2 => x^2 - x - k = 0
            # TH2: sqrt(x+k) = x + 1 (x >= -1) => x+k = x^2 + 2x + 1 => x^2 + x + 1 - k = 0
            vd_da_1_d = '\\True Phương trình đã cho có 2 nghiệm phân biệt'
            vd_da_1_s = 'Phương trình đã cho vô nghiệm'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Giải hai trường hợp: \\\\
            + Trường hợp 1: $\\sqrt{x+%s} = -x \\Leftrightarrow \\begin{cases} x \\leq 0 \\\\ x^2 - x - %s = 0 \\end{cases} \\Rightarrow x = \\frac{1-\\sqrt{%s}}{2}$ (thỏa mãn). \\\\
            + Trường hợp 2: $\\sqrt{x+%s} = x + 1 \\Leftrightarrow \\begin{cases} x \\geq -1 \\\\ x^2 + x + 1 - %s = 0 \\end{cases} \\Rightarrow x = \\frac{-1+\\sqrt{%s}}{2}$ (thỏa mãn). \\\\
            Vậy phương trình có 2 nghiệm phân biệt.''' % (latex(k), latex(k), latex(1+4*k), latex(k), latex(k), latex(4*k-3)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))

            ########################################################################
            # Vận dụng cao ############################################
            # Tích hai nghiệm: x1 = (1-sqrt(1+4k))/2 (<0) và x2 = (-1+sqrt(4k-3))/2 (>0)
            # Tích luôn âm
            vdc_da_1_d = '\\True Tích các nghiệm của phương trình là một số âm'
            vdc_da_1_s = 'Tích các nghiệm của phương trình là một số dương'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Dựa vào kết quả ở trên, ta có hai nghiệm là $x_1 = \\frac{1-\\sqrt{%s}}{2} < 0$ và $x_2 = \\frac{-1+\\sqrt{%s}}{2} > 0$ (do $k \\geq %s$). \\\\
            Do đó tích hai nghiệm $x_1 \\cdot x_2 < 0$ là một số âm.''' % (latex(1+4*k), latex(4*k-3), latex(k)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            ########################################################################
            # Xử lý Logic và Xuất nội dung ############################################

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                random.shuffle(combined_nb)
                random.shuffle(combined_th)
                random.shuffle(combined_vd)
                random.shuffle(combined_vdc)

                shuffled_answers = [combined_nb[0][0], combined_th[0][0], combined_vd[0][0], combined_vdc[0][0]]
                if 1 <= count_true_answers(shuffled_answers) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(combined_nb[0][0]) + '}\n'
                '{' + str(combined_th[0][0]) + '}\n'
                '{' + str(combined_vd[0][0]) + '}\n'
                '{' + str(combined_vdc[0][0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(combined_nb[0][1]) + '\n'
                '\\item ' + str(combined_th[0][1]) + '\n'
                '\\item ' + str(combined_vd[0][1]) + '\n'
                '\\item ' + str(combined_vdc[0][1]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

