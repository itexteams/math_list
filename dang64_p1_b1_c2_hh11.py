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


def bt_dang64_p1_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hóa hệ số k trong AA' = sqrt(k)*a
                # k = 2 => cos = 1/2 => 60 độ
                # k = 0.5 => cos = 0 => 90 độ
                # Để giữ bài toán đẹp như mẫu, ta chọn k sao cho ra góc 60 hoặc 90
                list_k = [2, Rational(1, 2)]
                k_val = random.choice(list_k)

                # Tính toán các thành phần để đưa vào lời giải
                # AB.BC = a*a*cos(120) = -a^2/2
                dot_base = Rational(-1, 2)
                # BB'.CC' = (sqrt(k)a)^2 = k*a^2
                dot_height = k_val
                # Tổng tích vô hướng = (k - 0.5)a^2
                dot_total = dot_height + dot_base

                # Độ dài AB' và BC' = sqrt(a^2 + k*a^2) = a*sqrt(1+k)
                mag_sq = 1 + k_val
                mag_val = sqrt(mag_sq)

                # Tính cos alpha = dot_total / (mag_sq)
                cos_alpha = dot_total / mag_sq

                # Xác định góc kết quả
                if cos_alpha == Rational(1, 2):
                    kq_goc = "60^\\circ"
                    ds_dung = "60^\\circ"
                    s = ["30^\\circ", "45^\\circ", "90^\\circ", "120^\\circ"]
                elif cos_alpha == 0:
                    kq_goc = "90^\\circ"
                    ds_dung = "90^\\circ"
                    s = ["30^\\circ", "45^\\circ", "60^\\circ", "120^\\circ"]
                else:
                    # Trường hợp dự phòng nếu mở rộng k
                    angle = int(deg(acos(cos_alpha)).evalf())
                    kq_goc = str(angle) + "^\\circ"
                    ds_dung = kq_goc
                    s = ["30^\\circ", "45^\\circ", "60^\\circ", "90^\\circ"]

                # Thiết lập nội dung câu hỏi
                # Hệ số căn của AA'
                if k_val == 2:
                    h_latex = "\\sqrt{2}a"
                else:
                    h_latex = "\\frac{\\sqrt{2}}{2}a"

                noidungcauhoi = ("Cho hình lăng trụ tam giác đều $ABC.A'B'C'$ có $AB = a$ và $AA' = %s$. Góc giữa hai đường thẳng $AB'$ và $BC'$ bằng" 
                                 % (h_latex))

                # Các đáp án
                da_d = ("\\True $" + ds_dung+'$')
                random.shuffle(s)
                da_s1 = '$'+ s[0] +'$'
                da_s2 = '$'+ s[1] +'$'
                da_s3 = '$'+ s[2] +'$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Hình vẽ TikZ
                hinh_ve = ("\\begin{center}\n"
                           "\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
                           "\\coordinate (A') at (0,0);\n"
                           "\\coordinate (B') at (1.2,-1.2);\n"
                           "\\coordinate (C') at (3.5,0);\n"
                           "\\coordinate (A) at (0,4);\n"
                           "\\coordinate (B) at (1.2,2.8);\n"
                           "\\coordinate (C) at (3.5,4);\n"
                           "\\draw (A)--(A') (A)--(B)--(C)--(A) (B)--(B') (C)--(C') (A')--(B')--(C');\n"
                           "\\draw[dashed]  (A')--(C');\n"
                           "\\draw (A)--(B') (B)--(C');\n"
                           "\\foreach \\p/\\pos in {A/left, B/left, C/right, A'/left, B'/below, C'/right} \\fill (\\p) node[\\pos]{\\p};\n"
                           "\\end{tikzpicture}\n"
                           "\\end{center}")

                # Lời giải chi tiết
                loigiai = (hinh_ve + "\n"
                           "Ta có $\\vec{AB'} \\cdot \\vec{BC'} = (\\vec{AB} + \\vec{BB'})(\\vec{BC} + \\vec{CC'}) = \\vec{AB} \\cdot \\vec{BC} + \\vec{AB} \\cdot \\vec{CC'} + \\vec{BB'} \\cdot \\vec{BC} + \\vec{BB'} \\cdot \\vec{CC'}$. \\\\\n"
                           "Vì lăng trụ đứng và đáy là tam giác đều cạnh $a$ nên: \\\\\n"
                           "$\\vec{AB} \\cdot \\vec{BC} = a \\cdot a \\cdot \\cos 120^\\circ = -\\frac{a^2}{2}$; \\\\\n"
                           "$\\vec{AB} \\cdot \\vec{CC'} = 0$ (do $CC' \\perp (ABC)$); \\\\\n"
                           "$\\vec{BB'} \\cdot \\vec{BC} = 0$ (do $BB' \\perp (ABC)$); \\\\\n"
                           "$\\vec{BB'} \\cdot \\vec{CC'} = AA'^2 = (%s)^2 = %s a^2$. \\\\\n"
                           "Suy ra $\\vec{AB'} \\cdot \\vec{BC'} = -\\frac{a^2}{2} + 0 + 0 + %s a^2 = %s a^2$. \\\\\n"
                           "Độ dài các đoạn thẳng: $AB' = BC' = \\sqrt{a^2 + AA'^2} = \\sqrt{a^2 + %s a^2} = a\\sqrt{%s}$. \\\\\n"
                           "Suy ra $\\cos(AB', BC') = \\frac{|\\vec{AB'} \\cdot \\vec{BC'}|}{|\\vec{AB'}| \\cdot |\\vec{BC'}|} = \\frac{%s a^2}{a\\sqrt{%s} \\cdot a\\sqrt{%s}} = %s$. \\\\\n"
                           "Vậy $(AB', BC') = %s$."
                           % (h_latex, latex(k_val), latex(k_val), latex(dot_total), latex(k_val), latex(mag_sq), 
                              latex(abs(dot_total)), latex(mag_sq), latex(mag_sq), latex(cos_alpha), kq_goc))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

