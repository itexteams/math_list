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


def bt_dang6_p3_b4_c4_ds10(self):
            # Khai báo biến
            # Hàm làm tròn theo kiểu Việt Nam (0.5 lên) và đổi dấu chấm thành phẩy
            def format_float(val):
                d = Decimal(str(float(val))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                return str(d).replace('.', ',')

            def format_val(val):
                return str(val).replace('.', ',')

            # --- B1 & B3: Nghiên cứu và tìm cách random bài toán ---
            # Các biến chính: BC, DC, BD. 
            # Điều kiện: Tam giác vuông tại A, D nằm trên tia AB nên AD = AB + BD.
            # Ta có: x^2 + AB^2 = BC^2 và x^2 + AD^2 = DC^2.
            # => AB = sqrt(BC^2 - x^2), AD = sqrt(DC^2 - x^2).
            # => sqrt(DC^2 - x^2) = sqrt(BC^2 - x^2) + BD.

            # Thử chọn các bộ số sao cho x thực và dương
            valid_params = False
            while not valid_params:
                bc = random.randint(5, 10)
                bd = random.randint(2, 5)
                # DC phải lớn hơn BC và thỏa mãn bất đẳng thức tam giác/hình học
                dc = bc + random.randint(2, 5)

                # Tính toán x^2 dựa trên phương trình: sqrt(dc^2 - x^2) = sqrt(bc^2 - x^2) + bd
                # Bình phương: dc^2 - x^2 = bc^2 - x^2 + 2*bd*sqrt(bc^2 - x^2) + bd^2
                # => dc^2 - bc^2 - bd^2 = 2*bd*sqrt(bc^2 - x^2)
                k_val = dc**2 - bc**2 - bd**2
                if k_val > 0:
                    rhs = k_val / (2 * bd)
                    if bc**2 > rhs**2:
                        x_sq = bc**2 - rhs**2
                        x_val = sqrt(x_sq)
                        valid_params = True

            # --- B2: Viết lại bài toán và tính toán ---
            x_rounded = Decimal(str(float(x_val))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            # Diện tích BCD = 1/2 * BD * AC (với AC = x)
            area_val = Decimal('0.5') * Decimal(str(bd)) * x_rounded
            area_rounded = area_val.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

            # Đáp án đúng
            da_final = format_float(area_rounded)

            # --- B4: Điều chỉnh phương án sai ---
            s = []
            while len(s) < 3:
                offset = random.choice([-2.1, -1.5, -0.8, 0.7, 1.2, 2.3, 3.1])
                wrong_ans = area_rounded + Decimal(str(offset))
                if wrong_ans > 0:
                    formatted_wrong = format_float(wrong_ans.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
                    if formatted_wrong != da_final and formatted_wrong not in s:
                        s.append(formatted_wrong)

            da_d = '\\True ' + '$' + da_final + '$'
            list_ans = [da_d, '$' + s[0] + '$', '$' + s[1] + '$', '$' + s[2] + '$']
            random.shuffle(list_ans)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tam giác $ABC$ vuông tại $A$ có $BC = %scm$. Điểm $D$ nằm trên tia $AB$ sao cho $DB = %scm, DC = %scm$. Đặt $AC = x$. Diện tích tam giác $BCD$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần mười).'''
                            % (latex(bc), latex(bd), latex(dc)))

            # Nội dung lời giải chi tiết
            loigiai = ('''Áp dụng định lí Pytago cho tam giác $ABC$ vuông tại $A$, ta được: $AC^2 + AB^2 = BC^2$. \\\\
            Suy ra $AB = \\sqrt{BC^2 - AC^2} = \\sqrt{%s^2 - x^2} = \\sqrt{%s - x^2} (cm)$. \\\\
            Áp dụng định lí Pytago cho tam giác $ACD$ vuông tại $A$, ta được: $AC^2 + AD^2 = CD^2$. \\\\
            Suy ra $AD = \\sqrt{CD^2 - AC^2} = \\sqrt{%s^2 - x^2} = \\sqrt{%s - x^2} (cm)$. \\\\
            Mà $AB + BD = AD$ nên $\\sqrt{%s - x^2} + %s = \\sqrt{%s - x^2}$ (1). \\\\
            Bình phương hai vế của phương trình (1), ta được: \\\\
            $%s - x^2 + %s\\sqrt{%s - x^2} + %s = %s - x^2 \\Rightarrow %s\\sqrt{%s - x^2} = %s \\Rightarrow x^2 = %s \\Rightarrow x \\approx %s$. \\\\
            Diện tích của tam giác $BCD$ là: $\\frac{1}{2} \\cdot %s \\cdot %s = %s \\approx %s (cm^2)$.'''
                      % (latex(bc), latex(bc**2), 
                         latex(dc), latex(dc**2),
                         latex(bc**2), latex(bd), latex(dc**2),
                         latex(bc**2), latex(2*bd), latex(bc**2), latex(bd**2), latex(dc**2), 
                         latex(2*bd), latex(bc**2), latex(dc**2 - bc**2 - bd**2), 
                         latex(Rational(bc**2 - (Rational(dc**2 - bc**2 - bd**2, 2*bd))**2)), 
                         format_float(x_rounded),
                         format_float(x_rounded), latex(bd), format_float(area_val), format_float(area_rounded)))
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(format_float(area_rounded))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

