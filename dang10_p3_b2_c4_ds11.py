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


def bt_dang10_p3_b2_c4_ds11(self):
            # Khai báo biến
            # BƯỚC 1 & 2: Thiết lập bài toán với x tiến tới vô cực
            x = symbols('x')

            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập hướng tiến tới của x: +oo hoặc -oo
                huong_tien = random.choice([sp.oo, -sp.oo])
                str_huong = "+\\infty" if huong_tien == sp.oo else "-\\infty"

                # Random hệ số của mẫu số (ax^2 + bx + c)
                mau_a = random.choice([2, 3, 4, 5]) 
                mau_b = random.randint(1, 10)
                mau_c = random.randint(-5, 5)

                # Random giá trị giới hạn mong muốn (L)
                L = random.randint(-10, 10)
                while L == 0: L = random.randint(-10, 10)

                # Tính m: m / mau_a = L => m = L * mau_a
                # Lưu ý: Với hàm phân thức bậc tử = bậc mẫu, giới hạn tại +oo và -oo là như nhau
                m_val = L * mau_a

                # Random các hệ số nhiễu
                tu_d = random.randint(-10, 10)
                tu_e = random.randint(-10, 10)

                # Các đáp án trắc nghiệm
                da_dung = '$m = %s$' % (latex(m_val))

                # Tạo danh sách đáp án nhiễu
                s = [
                    '$m = %s$' % (latex(m_val + random.randint(1, 3))),
                    '$m = %s$' % (latex(m_val - random.randint(1, 3))),
                    '$m = %s$' % (latex(L)), 
                    '$m = %s$' % (latex(-m_val)),
                ]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = (r'Giá trị thực của tham số $m$ thỏa mãn $\lim_{x \to %s} \frac{m x^2 %s x %s}{%s x^2 + %s x %s} = %s$ bằng bao nhiêu?'
                                 % (str_huong,
                                    ('+' + str(tu_d) if tu_d >= 0 else str(tu_d)), 
                                    ('+' + str(tu_e) if tu_e >= 0 else str(tu_e)),
                                    latex(mau_a), 
                                    ('+' + str(mau_b) if mau_b >= 0 else str(mau_b)),
                                    (str(mau_c) if mau_c <= 0 else '+' + str(mau_c)),
                                    latex(L)))

                # Các đáp án
                da_d = r'\True ' + da_dung
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Ta có:
                            $\lim_{x \to %s} \frac{m x^2 %s x %s}{%s x^2 + %s x %s} = %s$ 
                            $\Leftrightarrow \lim_{x \to %s} \frac{m %s \frac{1}{x} %s \frac{1}{x^2}}{%s %s \frac{1}{x} %s \frac{1}{x^2}} = %s$
                            $\Leftrightarrow \frac{m}{%s} = %s \Rightarrow m = %s$.'''
                           %(str_huong,
                             ('+' + str(tu_d) if tu_d >= 0 else str(tu_d)), 
                             ('+' + str(tu_e) if tu_e >= 0 else str(tu_e)),
                             latex(mau_a), 
                             ('+' + str(mau_b) if mau_b >= 0 else str(mau_b)),
                             (str(mau_c) if mau_c <= 0 else '+' + str(mau_c)),
                             latex(L),
                             str_huong,
                             ('+' + str(tu_d) if tu_d >= 0 else str(tu_d)),
                             ('+' + str(tu_e) if tu_e >= 0 else str(tu_e)),
                             latex(mau_a),
                             ('+' + str(mau_b) if mau_b >= 0 else str(mau_b)),
                             (str(mau_c) if mau_c <= 0 else '+' + str(mau_c)),
                             latex(L),
                             latex(mau_a),
                             latex(L),
                             latex(m_val)))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(m_val))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

