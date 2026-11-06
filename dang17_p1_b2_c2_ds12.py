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


def bt_dang17_p1_b2_c2_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random khoảng chiều cao bắt đầu
                start_val = random.choice([145, 150, 155, 160])

                # Phân bố tần số đối xứng để đảm bảo số trung bình luôn đẹp
                n1 = random.randint(2, 5)
                n2 = random.randint(5, 8)
                n3 = random.randint(8, 12)
                n4 = n2
                n5 = n1
                N = 2*n1 + 2*n2 + n3

                # Random thông tin phụ
                class_name = "12A" + str(random.randint(1, 9))
                year = random.choice([2024, 2025, 2026])
                year_str = f"{year} - {year+1}"

                # Tính các trung điểm đại diện
                x1 = start_val + 2.5
                x2 = start_val + 7.5
                x3 = start_val + 12.5
                x4 = start_val + 17.5
                x5 = start_val + 22.5

                # Do tính đối xứng, giá trị trung bình chính là x3
                x_bar = x3

                # Tử số của phương sai 
                var_num = n1 * (x1 - x_bar)**2 + n2 * (x2 - x_bar)**2 + n3 * (x3 - x_bar)**2 + n4 * (x4 - x_bar)**2 + n5 * (x5 - x_bar)**2
                var_num = int(var_num)

                # Hàm hỗ trợ định dạng số sang dạng có dấu phẩy thay cho dấu thập phân
                def fmt_num(num):
                    if num == int(num):
                        return str(int(num))
                    return str(num).replace('.', ',')

                x1_str = fmt_num(x1)
                x2_str = fmt_num(x2)
                x5_str = fmt_num(x5)
                x_bar_str = fmt_num(x_bar)

                # Sử dụng Sympy để rút gọn độ lệch chuẩn dưới dạng LaTeX
                s_sym = sqrt(Rational(var_num, N))
                latex_s = latex(s_sym)

                # Giá trị xấp xỉ của độ lệch chuẩn
                s_val = math.sqrt(var_num / N)
                s_approx_str = "{:.2f}".format(s_val).replace('.', ',')

                # Tạo đáp án nhiễu bám sát vào hình dạng của đáp án đúng
                num_frac, den_frac = Rational(var_num, N).as_numer_denom()
                val_inside = num_frac * den_frac

                distractors = set()
                for offset in [1, 2, 3, -1, -2, -3]:
                    fake_val = val_inside + offset
                    if fake_val > 0:
                        fake_expr = latex(sqrt(fake_val) / den_frac)
                        distractors.add('$%s$' % fake_expr)

                distractors.discard('$%s$' % latex_s)
                wrong_choices = random.sample(list(distractors), 3)

                ans_correct = '$%s$' % latex_s

                # Xây dựng bảng
                table_str = ('''\\begin{center}
                \\begin{tabular}{|c|c|c|c|c|c|}
                \\hline
                \\textbf{Chiều cao} & $[%s;%s)$ & $[%s;%s)$ & $[%s;%s)$ & $[%s;%s)$ & $[%s;%s)$ \\\\
                \\hline
                \\textbf{Tần số} & %s & %s & %s & %s & %s \\\\
                \\hline
                \\end{tabular}
                \\end{center}''' % (start_val, start_val+5, start_val+5, start_val+10, start_val+10, start_val+15, start_val+15, start_val+20, start_val+20, start_val+25, n1, n2, n3, n4, n5))

                # Câu hỏi
                noidungcauhoi = ('''Bảng số liệu ghép nhóm về chiều cao đo được của $%s$ học sinh nam lớp $%s$ đầu năm học $%s$ của một trường THPT được cho như sau:
                %s
                Độ lệch chuẩn của mẫu số liệu ghép nhóm trên là''' % (N, class_name, year_str, table_str))

                # Lời giải trình bày chuẩn format
                loigiai = ('''Giá trị trung bình mẫu số liệu ghép nhóm là $\\overline{x} = \\frac{%s.%s + %s.%s + \\dots + %s.%s}{%s} = %s$.\\\\
                Độ lệch chuẩn mẫu số liệu ghép nhóm là: \\\\
                $s = \\sqrt{s^2} = \\sqrt{\\frac{%s.(%s - \\overline{x})^2 + \\dots + %s.(%s - \\overline{x})^2}{%s}} = %s \\approx %s$.'''
                % (x1_str, n1, x2_str, n2, x5_str, n5, N, x_bar_str, 
                   n1, x1_str, n5, x5_str, N, latex_s, s_approx_str))

                # Xử lý các đáp án
                da_d = ('\\True ' + ans_correct)
                da_s1 = str(wrong_choices[0])
                da_s2 = str(wrong_choices[1]) 
                da_s3 = str(wrong_choices[2]) 

                # Trộn đều các đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content



