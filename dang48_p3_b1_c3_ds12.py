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


def bt_dang48_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Cấu trúc: f(x) - x*f'(x) = -m*x^3 - n*x^2
            # Để kết quả đẹp, ta chọn m là số chẵn
            m = random.randint(1, 5) * 2  # m thuộc {2, 4, 6, 8, 10}
            n = random.randint(1, 6)
            x0 = 1
            # Chọn f(1) sao cho C là số nguyên hoặc phân số đẹp
            # f(1)/1 = (m/2)*1^2 + n*1 + C => C = f(1) - (m/2 + n)
            C_val = random.randint(-5, 5)
            f_x0 = int(m/2 + n + C_val)

            # Tính giá trị cần tìm f(x1)
            x1 = random.randint(2, 3)

            # Tính toán hàm f(x) để tìm đáp án đúng
            # [f(x)/x]' = m*x + n
            # f(x)/x = (m/2)*x^2 + n*x + C
            term1 = Rational(m, 2)
            C = f_x0 - (term1 * x0**2 + n * x0)
            f_func = (term1 * x**2 + n * x + C) * x
            ans_val = f_func.subs(x, x1)

            # B4: Điều chỉnh các phương án sai không được trùng đáp án đúng
            da_dung = f"${ans_val}$"
            s = set()
            while len(s) < 3:
                sai = ans_val + random.choice([-10, -5, -2, 2, 5, 10, 12, 15])
                if sai != ans_val:
                    s.add(f"${sai}$")

            list_sai = list(s)

            # Nội dung câu hỏi
            noidungcauhoi = (
                f"Cho hàm số $f(x)$ thỏa mãn $f({x0}) = {f_x0}$ và "
                f"$f(x) = x f'(x) - {m}x^3 - {n}x^2$ với mọi $x > 0$. "
                f"Giá trị của $f({x1})$ bằng bao nhiêu?"
            )

            # Nội dung lời giải (B2: Viết lại y hệt cấu trúc bài mẫu)
            loigiai = (
                f"Ta có: $f(x) - x f'(x) = -{m}x^3 - {n}x^2 \\Leftrightarrow  \\frac{{f(x) - x f'(x)}}{{x^2}} = \\frac{{-{m}x^3 - {n}x^2}}{{x^2}}$ \\\\\n"
                f"$\\Leftrightarrow -\\left[ \\frac{{f(x)}}{{x}} \\right]' = -{m}x - {n} \\Leftrightarrow  \\left[ \\frac{{f(x)}}{{x}} \\right]' = {m}x + {n}$. \\\\\n"
                f"Suy ra $\\frac{{f(x)}}{{x}}$ là một nguyên hàm của hàm số $g(x) = {m}x + {n}$. \\\\\n"
                f"Ta có $\\int ({m}x + {n}) \\text{{d}}x = {latex(simplify(term1*x**2 + n*x))} + C$. \\\\\n"
                f"Do đó, $\\frac{{f(x)}}{{x}} = {latex(simplify(term1*x**2 + n*x))} + C \\quad (1)$. \\\\\n"
                f"Vì $f({x0}) = {f_x0}$ nên thay $x = {x0}$ vào (1) ta được: "
                f"$\\frac{{{f_x0}}}{{{x0}}} = {term1 * x0**2 + n * x0} + C \\Leftrightarrow  C = {C}$. \\\\\n"
                f"Từ đó $f(x) = x({latex(simplify(term1*x**2 + n*x + C))}) = {latex(expand(f_func))}$. \\\\\n"
                f"Vậy $f({x1}) = {ans_val}$.")
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(ans_val)) 

            # Đưa các đáp án vào danh sách và trộn
            list_ans = [f"\\True {da_dung}", list_sai[0], list_sai[1], list_sai[2]]
            random.shuffle(list_ans)

            # Xuất kết quả theo định dạng yêu cầu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + str(dapan)+
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n')
            return content  

