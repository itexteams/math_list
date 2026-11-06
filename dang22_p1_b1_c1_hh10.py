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


def bt_dang22_p1_b1_c1_hh10(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng chuỗi LaTeX cho hàm lượng giác và góc
            def fmt(func, ang):
                return f"\\{func} {ang}^\\circ"

            # ==============================================================================
            # NGÂN HÀNG CÁC TÍNH CHẤT LƯỢNG GIÁC (Mở rộng các góc và các hàm)
            # Mỗi hàm trả về: (Mệnh đề ĐÚNG, Mệnh đề SAI, Lời giải chi tiết)
            # ==============================================================================

            def gen_sin_0_90():
                a = random.randint(10, 80)
                b = random.randint(a + 1, 89)
                # Sin đồng biến trên (0, 90)
                return f"{fmt('sin', a)} < {fmt('sin', b)}", f"{fmt('sin', a)} > {fmt('sin', b)}", f"Trong khoảng $(0^\\circ, 90^\\circ)$, hàm số $\\sin$ đồng biến. Vì $0^\\circ < {a}^\\circ < {b}^\\circ < 90^\\circ$ nên $\\sin {a}^\\circ < \\sin {b}^\\circ$."

            def gen_sin_90_180():
                a = random.randint(91, 170)
                b = random.randint(a + 1, 179)
                # Sin nghịch biến trên (90, 180)
                return f"{fmt('sin', a)} > {fmt('sin', b)}", f"{fmt('sin', a)} < {fmt('sin', b)}", f"Trong khoảng $(90^\\circ, 180^\\circ)$, hàm số $\\sin$ nghịch biến. Vì $90^\\circ < {a}^\\circ < {b}^\\circ < 180^\\circ$ nên $\\sin {a}^\\circ > \\sin {b}^\\circ$."

            def gen_cos_0_180():
                a = random.randint(10, 170)
                b = random.randint(a + 1, 179)
                # Cos nghịch biến trên (0, 180)
                return f"{fmt('cos', a)} > {fmt('cos', b)}", f"{fmt('cos', a)} < {fmt('cos', b)}", f"Trong khoảng $(0^\\circ, 180^\\circ)$, hàm số $\\cos$ nghịch biến. Vì $0^\\circ < {a}^\\circ < {b}^\\circ < 180^\\circ$ nên $\\cos {a}^\\circ > \\cos {b}^\\circ$."

            def gen_tan_0_90():
                a = random.randint(10, 80)
                b = random.randint(a + 1, 89)
                # Tan đồng biến trên (0, 90)
                return f"{fmt('tan', a)} < {fmt('tan', b)}", f"{fmt('tan', a)} > {fmt('tan', b)}", f"Trong khoảng $(0^\\circ, 90^\\circ)$, hàm số $\\tan$ đồng biến. Vì $0^\\circ < {a}^\\circ < {b}^\\circ < 90^\\circ$ nên $\\tan {a}^\\circ < \\tan {b}^\\circ$."

            def gen_tan_90_180():
                a = random.randint(91, 170)
                b = random.randint(a + 1, 179)
                # Tan đồng biến trên (90, 180)
                return f"{fmt('tan', a)} < {fmt('tan', b)}", f"{fmt('tan', a)} > {fmt('tan', b)}", f"Trong khoảng $(90^\\circ, 180^\\circ)$, hàm số $\\tan$ đồng biến. Vì $90^\\circ < {a}^\\circ < {b}^\\circ < 180^\\circ$ nên $\\tan {a}^\\circ < \\tan {b}^\\circ$."

            def gen_cot_0_180():
                a = random.randint(10, 80)
                b = random.randint(91, 179) # Chọn 1 góc nhọn, 1 góc tù để đa dạng
                # Cot nghịch biến trên (0, 180)
                return f"{fmt('cot', a)} > {fmt('cot', b)}", f"{fmt('cot', a)} < {fmt('cot', b)}", f"Trong khoảng $(0^\\circ, 180^\\circ)$, hàm số $\\cot$ nghịch biến. Vì $0^\\circ < {a}^\\circ < {b}^\\circ < 180^\\circ$ nên $\\cot {a}^\\circ > \\cot {b}^\\circ$."

            def gen_cross_sign_tan():
                a = random.randint(10, 89)
                b = random.randint(91, 179)
                # Tan góc nhọn dương, tan góc tù âm
                return f"{fmt('tan', a)} > {fmt('tan', b)}", f"{fmt('tan', a)} < {fmt('tan', b)}", f"Góc ${a}^\\circ$ là góc nhọn nên $\\tan {a}^\\circ > 0$. Góc ${b}^\\circ$ là góc tù nên $\\tan {b}^\\circ < 0$. Do đó $\\tan {a}^\\circ > \\tan {b}^\\circ$."

            def gen_sin_cos_cross():
                a = random.randint(91, 179)
                # Góc tù: sin > 0, cos < 0
                return f"{fmt('sin', a)} > {fmt('cos', a)}", f"{fmt('sin', a)} < {fmt('cos', a)}", f"Với góc tù ${a}^\\circ$ (từ $90^\\circ$ đến $180^\\circ$), ta có $\\sin {a}^\\circ > 0$ và $\\cos {a}^\\circ < 0$. Do đó $\\sin {a}^\\circ > \\cos {a}^\\circ$."

            # ==============================================================================

            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':

                # Đưa tất cả các trường hợp vào 1 danh sách và xáo trộn
                generators = [gen_sin_0_90, gen_sin_90_180, gen_cos_0_180, gen_tan_0_90, 
                              gen_tan_90_180, gen_cot_0_180, gen_cross_sign_tan, gen_sin_cos_cross]
                random.shuffle(generators)

                # 1. Chọn generators[0] làm ĐÁP ÁN ĐÚNG
                true_stmt, _, loigiai_text = generators[0]()
                da = true_stmt
                loigiai = loigiai_text

                # 2. Chọn generators[1], [2], [3] làm ĐÁP ÁN SAI (Lấy mệnh đề sai của chúng)
                _, false_stmt_1, _ = generators[1]()
                _, false_stmt_2, _ = generators[2]()
                _, false_stmt_3, _ = generators[3]()

                das1 = false_stmt_1
                das2 = false_stmt_2
                das3 = false_stmt_3

                # Câu hỏi
                noidungcauhoi = "Khẳng định nào sau đây đúng?"

                # Các đáp án
                da_d = ('\\True $'+str(da) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm (Đảm bảo cấu trúc cố định ở cuối file)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

