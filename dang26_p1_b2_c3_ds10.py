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


def bt_dang26_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B1, B2, B3: Phân tích, thiết kế và sinh tham số ngẫu nhiên
                while True:
                    # Chọn ngẫu nhiên x (nghiệm) và các hệ số b, c cho biểu thức bx^2 + c
                    x_val = random.randint(2, 5)
                    b = random.choice([2, 4]) 
                    c = random.choice([-5, -3, -1, 1, 3, 5]) 

                    expr_val = b * (x_val**2) + c

                    # Đảm bảo giá trị biểu thức đủ lớn để chèn các số nhỏ hơn vào trước nó
                    if expr_val > 10:
                        break

                # Tính toán phần tử đứng trước biểu thức (vị trí thứ 5)
                # k chẵn để tổng của 2 số ở giữa (vị trí 5 và 6) chia hết cho 2 -> trung vị nguyên
                k = random.choice([0, 2, 4])
                a = expr_val - k

                # Tính số trung vị
                M_e = (a + expr_val) // 2

                # Sinh ngẫu nhiên các phần tử râu ria để tạo thành dãy 10 số liên tiếp tăng dần
                left_nums = sorted(random.sample(range(1, a), 4))
                right_nums = sorted(random.sample(range(expr_val + 1, expr_val + 20), 4))

                # Hàm hỗ trợ định dạng biểu thức bậc 2 tránh trường hợp "1x^2" hoặc "+ -1"
                def format_term(coeff, constant):
                    coeff_str = "x^2" if coeff == 1 else f"{coeff}x^2"
                    if constant > 0:
                        return f"{coeff_str} + {constant}"
                    elif constant < 0:
                        return f"{coeff_str} - {abs(constant)}"
                    else:
                        return coeff_str

                term6_str = format_term(b, c)

                # Chuỗi dữ liệu hiển thị (gắn LaTeX chung cho cả dòng)
                data_list = left_nums + [a, term6_str] + right_nums
                data_str_latex = "$" + " \\quad ".join(map(str, data_list)) + "$"

                # Chuẩn bị tham số cho chuỗi lời giải
                num1_str = f"{term6_str} + {a}"
                num2_str = format_term(b, a + c)

                A = b // 2
                B = (a + c) // 2
                simplified_str = format_term(A, B)

                # Lời giải chi tiết tính trung vị
                loigiai_calc = f"Số trung vị trong mẫu số liệu trên là $\\frac{{{num1_str}}}{{2}} = \\frac{{{num2_str}}}{{2}} = {simplified_str}$"

                # Ma trận nghiệm
                matrix_str = f"\\left[\\begin{{array}}{{ll}} x = {x_val} & (\\text{{thỏa mãn}}) \\\\\\\\ x = {-x_val} & (\\text{{loại}}) \\end{{array}}\\right."

                # Phương trình tìm x
                step2 = f"x^2 = {(M_e - B)//A}"

                # Đáp án đúng
                da = f"$x = {x_val}$"

                # Sinh các đáp án nhiễu (Dựa vào sai lầm phổ biến)
                distractors = set()
                distractors.add(f"$x = {M_e}$")
                distractors.add(f"$x = {M_e - 1}$")
                distractors.add(f"$x = {x_val + random.randint(5, 10)}$")
                while len(distractors) < 3:
                    distractors.add(f"$x = {random.randint(10, 20)}$")

                distractors = list(distractors)
                das1 = distractors[0]
                das2 = distractors[1]
                das3 = distractors[2]

                # Câu hỏi
                noidungcauhoi = (f"Biết rằng số trung vị trong mẫu số liệu sau (đã sắp xếp theo thứ tự) bằng ${M_e}$. "
                                 f"\\begin{{center}}\n{data_str_latex}\n\\end{{center}}"
                                 f"Số nguyên dương $x$ bằng")

                # Trộn đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (f"{loigiai_calc}.\n\n"
                           f"Từ giả thiết suy ra ${simplified_str} = {M_e} \\Leftrightarrow {step2} \\Leftrightarrow {matrix_str}$.\\\\\n"
                           f"Vậy $x = {x_val}$.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

