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


def bt_dang40_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu cho Sympy
            x = symbols('x')


            lis_k = [2, 3, 4, 5,6,7,8,9]
            k_val = random.choice(lis_k)

            a = 3 * k_val
            b = 4 * k_val
            f_prime_0 = k_val
            f_0 = 0

            # Tính toán các biểu thức để đưa vào lời giải
            expr_rhs = (a*x + b)*exp(2*x)
            integral_1 = integrate((a*x + b)*exp(x), x) 
            # integral_1 = (3kx + k)e^x
            expr_f_prime_plus_f = (a*x + k_val)*exp(2*x)
            integral_2 = integrate((a*x + k_val)*exp(3*x), x)
            # integral_2 = k*x*e^{3x}

            # Đáp án đúng
            kq_val = k_val # Hệ số của e^2
            da_dung = f"${latex(kq_val)}e^2$"

            # Bước 4: Điều chỉnh các phương án sai không trùng với đáp án đúng
            s = [
                f"${latex(kq_val + 1)}e^2$",
                f"${latex(kq_val + 2)}e^2$",
                f"$e^{{{latex(kq_val + 1)}}}$",
                f"${latex(kq_val)}e$",
                f"${latex(2*kq_val)}e^2$",
                f"${latex(kq_val)}e^3$"
            ]

            # Loại bỏ đáp án đúng nếu lỡ có trong danh sách nhiễu
            if da_dung in s:
                s.remove(da_dung)

            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Bước 2: Viết lại bài toán theo mẫu code
            # Câu hỏi
            noidungcauhoi = (
                f"Cho hàm số $f(x)$ có đạo hàm cấp hai liên tục trên $\\mathbb{{R}}$ và thoả mãn "
                f"$f(0)={f_0}, f'(0)={f_prime_0}, f''(x) = f(x) + ({a}x + {b})e^{{2x}}$ với mọi $x \\in \\mathbb{{R}}$. "
                f"Tính $f(1)$."
            )

            # Các đáp án
            da_d = '\\True ' + da_dung
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = (
                f"Ta có: \n"
                f"$$f''(x) - f(x) = ({a}x + {b})e^{{2x}} \\iff \\frac{{f''(x) - f(x)}}{{e^x}} = ({a}x + {b})e^x$$\n"
                f"$$\\iff \\frac{{f''(x)e^x - f'(x)e^x}}{{e^{{2x}}}} + \\frac{{f'(x)e^x - f(x)e^x}}{{e^{{2x}}}} = ({a}x + {b})e^x$$\n"
                f"$$\\iff \\left( \\frac{{f'(x)}}{{e^x}} \\right)' + \\left( \\frac{{f(x)}}{{e^x}} \\right)' = ({a}x + {b})e^x$$\n"
                f"Lấy nguyên hàm hai vế ta được:\n"
                f"$$\\frac{{f'(x)}}{{e^x}} + \\frac{{f(x)}}{{e^x}} = \\int ({a}x + {b})e^x dx = ({a}x + {k_val})e^x + C$$\n"
                f"Khi $x = 0 \\Rightarrow \\frac{{{f_prime_0}}}{{1}} + \\frac{{{f_0}}}{{1}} = (0 + {k_val}) + C \\Rightarrow C = 0$.\n"
                f"Suy ra: $\\frac{{f'(x) + f(x)}}{{e^x}} = ({a}x + {k_val})e^x \\iff f'(x) + f(x) = ({a}x + {k_val})e^{{2x}}$\n"
                f"$\\iff f'(x)e^x + f(x)e^x = ({a}x + {k_val})e^{{3x}} \\iff [f(x)e^x]' = ({a}x + {k_val})e^{{3x}}$\n"
                f"$\\Rightarrow f(x)e^x = \\int ({a}x + {k_val})e^{{3x}} dx = {latex(k_val)}xe^{{3x}} + C_1$\n"
                f"Lại có $x = 0 \\Rightarrow 0 = 0 + C_1 \\Rightarrow C_1 = 0$.\n"
                f"Vậy: $f(x) = {latex(k_val)}xe^{{2x}} \\Rightarrow f(1) = {latex(kq_val)}e^2$."
            )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

