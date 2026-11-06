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


def bt_dang53_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Bước 1 & 3: Nghiên cứu đề bài và thiết lập các biến số để random
            # Giả sử CD = x, AD = x, AB = 2x. SA = h.
            # Trong hình mẫu: x = 1, h = 3.
            x = random.randint(1, 20)
            h = random.randint(2, 20)

            ab_val = 2 * x
            ad_val = x
            cd_val = x
            sa_val = h

            # Kết quả: Diện tích tam giác SIB (hình chiếu của SBC lên (SAB))
            # S_SIB = 1/2 * SA * IB. Vì I là trung điểm AB nên IB = x.
            # S_SIB = 1/2 * h * x
            kq_val = Rational(h * x, 2)
            kq_float = float(kq_val)
            kq_str = str(kq_float).replace('.', ',')

            # Bước 4: Tạo các phương án sai không trùng với đáp án đúng
            def generate_distractors(correct_val):
                options = set()
                while len(options) < 3:
                    # Tạo các giá trị sai quanh kết quả đúng
                    offset = random.choice([Rational(1, 2), 1, Rational(3, 2), 2])
                    case = random.randint(1, 4)
                    if case == 1:
                        val = correct_val + offset
                    elif case == 2:
                        val = abs(correct_val - offset)
                    elif case == 3:
                        val = correct_val * 2
                    else:
                        val = correct_val / 2

                    if val != correct_val and val > 0:
                        s_val = str(float(val)).replace('.', ',')
                        options.add('$%s$' % s_val)
                return list(options)

            distractors = generate_distractors(kq_val)
            da_d = '\\True $%s$' % kq_str
            list_ans = [da_d] + distractors
            random.shuffle(list_ans)

            # Bước 2: Viết nội dung câu hỏi và lời giải chi tiết
            # Không dùng tiền tố r, sử dụng \\ cho các lệnh LaTeX
            noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy là hình thang vuông tại $A$ và $D$, $AB = 2AD = 2CD = %s$. '
                             'Biết $SA \\perp \\left( ABCD \\right)$, $SA = %s$. Diện tích hình chiếu vuông góc của tam giác $SBC$ '
                             'lên mặt phẳng $\\left( SAB \\right)$ là bao nhiêu? (làm tròn kết quả đến hàng phần chục).' 
                             % (latex(ab_val), latex(sa_val)))

            # Tạo mã TikZ cho hình vẽ giống 100% hình mẫu
            tikz_code = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[line width=1pt, scale=0.8, font=\\footnotesize]\n'
                '\\coordinate (A) at (0,0);\n'
                '\\coordinate (B) at (4,0);\n'
                '\\coordinate (D) at (-1.2,-1.2);\n'
                '\\coordinate (C) at (1.8,-1.2);\n'
                '\\coordinate (I) at (2,0);\n'
                '\\coordinate (S) at (0,3.5);\n'
                '\\draw[dashed] (S)--(A) (A)--(D) (A)--(I) (A)--(C) (S)--(I) (I)--(B);\n'
                '\\draw (S)--(D) (D)--(C) (C)--(B) (B)--(S) (S)--(C) ;\n'
                '\\node[left] at (A) {$A$};\n'
                '\\node[right] at (B) {$B$};\n'
                '\\node[below left] at (D) {$D$};\n'
                '\\node[below right] at (C) {$C$};\n'
                '\\node[above right] at (I) {$I$};\n'
                '\\node[above] at (S) {$S$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )

            loigiai = ('Gọi $I$ là trung điểm $AB$. \\\\\n'
                       'Dễ dàng chứng minh $AICD$ là hình vuông $\\Rightarrow CI = \\frac{1}{2} AB \\Rightarrow \\Delta ABC$ vuông tại $C$. \\\\\n'
                       'Ta có: $\\begin{cases} CI \\perp AB \\\\ CI \\perp SA \\end{cases} \\Rightarrow CI \\perp \\left( SAB \\right)$. \\\\\n'
                       'Hình chiếu của $\\Delta SBC$ trên $\\left( SAB \\right)$ là $\\Delta SIB$. \\\\\n'
                       'Vì $SA \\perp AB$ và $I$ thuộc $AB$ nên $SA \\perp IB$. Tam giác $SIB$ vuông tại $A$. \\\\\n'
                       '$S_{\\Delta SIB} = \\frac{1}{2} S_{\\Delta SAB} = \\frac{1}{2} \\cdot \\frac{1}{2} \\cdot SA \\cdot AB = \\frac{1}{4} \\cdot %s \\cdot %s = %s$.'
                       % (latex(sa_val), latex(ab_val), kq_str))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm theo đúng cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'  + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + tikz_code + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

