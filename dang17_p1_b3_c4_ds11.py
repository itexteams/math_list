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


def bt_dang17_p1_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # 1. Random tham số
            a = random.randint(1, 5)
            c = random.randint(1, 5)
            d = random.randint(1, 3)
            e = random.randint(1, 5)
            n = random.randint(2, 4)

            # 2. Định nghĩa các hàm nhánh
            # Nhánh 1: x < 0
            f1 = -a * x * cos(x)
            # Nhánh 2: 0 <= x < 1
            f2 = (c * x**2) / (d + x)
            # Nhánh 3: x >= 1
            f3 = e * x**n

            # 3. Tính giới hạn và giá trị hàm số
            # Tại x = 0
            lim_0_trai = limit(f1, x, 0, dir='-')
            lim_0_phai = limit(f2, x, 0, dir='+')
            f_0 = f2.subs(x, 0)

            # Tại x = 1
            lim_1_trai = limit(f2, x, 1, dir='-')
            lim_1_phai = limit(f3, x, 1, dir='+')
            f_1 = f3.subs(x, 1)

            # 4. Xác định tính liên tục để tạo đáp án đúng
            is_cont_0 = (lim_0_trai == lim_0_phai == f_0)
            is_cont_1 = (lim_1_trai == lim_1_phai) # Thực tế cần so với f(1) nữa nhưng f(1) thuộc nhánh f3

            def get_status(status_0, status_1):
                txt0 = "liên tục" if status_0 else "gián đoạn"
                txt1 = "liên tục" if status_1 else "gián đoạn"
                return f"Hàm số {txt0} tại $x=0$ và {txt1} tại $x=1$"

            da_dung = get_status(is_cont_0, is_cont_1)

            # Tạo danh sách các khẳng định sai
            all_cases = [
                get_status(True, True),
                get_status(True, False),
                get_status(False, True),
                get_status(False, False)
            ]
            list_da_sai = [case for case in all_cases if case != da_dung]
            random.shuffle(list_da_sai)

            # 5. Soạn nội dung câu hỏi
            noidungcauhoi = r'''Cho hàm số $f(x) = \begin{cases} %s, & x < 0 \\ %s, & 0 \le x < 1 \\ %s, & x \ge 1 \end{cases}$. Khẳng định nào sau đây đúng?''' % (
                latex(f1), latex(f2), latex(f3)
            )

            # 6. Soạn lời giải chi tiết
            loigiai = r'''$f(x)$ liên tục tại $x \neq 0$ và $x \neq 1$. \\
            Tại $x = 0$: \\
            $\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} (%s) = %s$. \\
            $\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \frac{%s}{%s} = %s$. \\
            $f(0) = %s$. \\
            Suy ra %s tại $x=0$. \\
            Tại $x = 1$: \\
            $\lim_{x \to 1^-} f(x) = \lim_{x \to 1^-} \frac{%s}{%s} = %s$. \\
            $\lim_{x \to 1^+} f(x) = \lim_{x \to 1^+} (%s) = %s$. \\
            Suy ra %s tại $x=1$.''' % (
                latex(f1), latex(lim_0_trai), 
                latex(c*x**2), latex(d+x), latex(lim_0_phai), 
                latex(f_0), 
                "$\\lim_{x \\to 0^-} f(x) = \\lim_{x \\to 0^+} f(x) = f(0)$ nên hàm số liên tục" if is_cont_0 else "giới hạn hai bên không bằng nhau hoặc khác f(0) nên hàm số gián đoạn",
                latex(c*x**2), latex(d+x), latex(lim_1_trai),
                latex(f3), latex(lim_1_phai),
                "$\\lim_{x \\to 1^-} f(x) = \\lim_{x \\to 1^+} f(x)$ nên hàm số liên tục" if is_cont_1 else r"$\\lim_{x \\to 1^-} f(x) \\neq \\lim_{x \\to 1^+} f(x)$ nên hàm số gián đoạn"
            )

            # 7. Đưa vào cấu trúc EX
            list_1 = ['\\True ' + da_dung] + list_da_sai
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

