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


def bt_dang16_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Hàm tính tổ hợp C(n, k)
            def nCr(n, k):
                if k < 0 or k > n:
                    return 0
                return math.comb(n, k)

            # Khai báo các biến ngẫu nhiên
            # nR: số bi đỏ, nY: số bi vàng, nB: số bi xanh
            # Để đảm bảo logic 4 trường hợp như hình:
            # k=4 (chọn 4 bi), r > y và b >= 1
            nR = random.randint(5, 7)
            nY = random.randint(3, 4)
            nB = random.randint(4, 6)
            n_total = nR + nY + nB
            k_select = 4

            # 1. Tính không gian mẫu
            n_omega = nCr(n_total, k_select)

            # 2. Tính các trường hợp thuận lợi cho biến cố A (Số đỏ > Số vàng và có mặt bi xanh)
            # Các bộ (đỏ, vàng, xanh) thỏa mãn r + y + b = 4, r > y, b >= 1:
            # TH1: (1, 0, 3) -> 1 đỏ, 0 vàng, 3 xanh
            # TH2: (2, 0, 2) -> 2 đỏ, 0 vàng, 2 xanh
            # TH3: (3, 0, 1) -> 3 đỏ, 0 vàng, 1 xanh
            # TH4: (2, 1, 1) -> 2 đỏ, 1 vàng, 1 xanh

            th1_val = nCr(nR, 1) * nCr(nB, 3)
            th2_val = nCr(nR, 2) * nCr(nB, 2)
            th3_val = nCr(nR, 3) * nCr(nB, 1)
            th4_val = nCr(nR, 2) * nCr(nY, 1) * nCr(nB, 1)

            n_A = th1_val + th2_val + th3_val + th4_val

            # 3. Tính xác suất và tối giản phân số
            res_frac = Rational(n_A, n_omega)
            kq_latex = latex(res_frac)

            # 4. Tạo các phương án sai
            def generate_wrong_answers(correct_frac):
                wrong = set()
                num, den = correct_frac.p, correct_frac.q
                while len(wrong) < 3:
                    # Tạo ngẫu nhiên bằng cách thay đổi tử hoặc mẫu
                    w_num = max(1, num + random.randint(-10, 10))
                    w_den = max(den // 2, den + random.randint(-20, 20))
                    w_frac = Rational(w_num, w_den)
                    if w_frac != correct_frac:
                        wrong.add('$%s$' % latex(w_frac))
                return list(wrong)

            wrong_answers = generate_wrong_answers(res_frac)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một hộp có $%s$ viên bi đỏ, $%s$ viên bi vàng và $%s$ viên bi xanh. Chọn ngẫu nhiên $%s$ viên bi trong hộp, xác suất để $%s$ viên bi được chọn có số bi đỏ lớn hơn số bi vàng và nhất thiết phải có mặt bi xanh bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                             %(latex(nR), latex(nY), latex(nB), latex(k_select), latex(k_select)))

            # Đáp án
            da_d = '\\True $%s$' % kq_latex
            list_1 = [da_d] + wrong_answers
            random.shuffle(list_1)

            h1=res_frac
            number = Decimal(float(h1))  # Số cần làm tròn
            kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kqz=str(kq1).replace('.', ',')
            # Nội dung lời giải chi tiết
            loigiai = ('''Không gian mẫu là số cách chọn ngẫu nhiên $%s$ viên bi từ hộp chứa $%s$ viên bi. \\\\
            Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^{%s} = %s$. \\\\
            Gọi $A$ là biến cố ‘$%s$ viên bi được chọn có số bi đỏ lớn hơn số bi vàng và nhất thiết phải có mặt bi xanh’. Ta có các trường hợp thuận lợi cho biến cố $A$ như sau: \\\\
            \\textbf{TH1:} Chọn $1$ bi đỏ, $3$ bi xanh nên có $C_{%s}^{1}C_{%s}^{3} = %s$ cách. \\\\
            \\textbf{TH2:} Chọn $2$ bi đỏ, $2$ bi xanh nên có $C_{%s}^{2}C_{%s}^{2} = %s$ cách. \\\\
            \\textbf{TH3:} Chọn $3$ bi đỏ, $1$ bi xanh nên có $C_{%s}^{3}C_{%s}^{1} = %s$ cách. \\\\
            \\textbf{TH4:} Chọn $2$ bi đỏ, $1$ bi vàng và $1$ bi xanh nên có $C_{%s}^{2}C_{%s}^{1}C_{%s}^{1} = %s$ cách. \\\\
            Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = %s + %s + %s + %s = %s$. \\\\
            Vậy xác suất cần tính $P\\left(A\\right) = \\frac{%s}{%s} = %s \\approx %s$.'''
                       %(latex(k_select), latex(n_total), latex(n_total), latex(k_select), latex(n_omega),
                         latex(k_select),
                         latex(nR), latex(nB), latex(th1_val),
                         latex(nR), latex(nB), latex(th2_val),
                         latex(nR), latex(nB), latex(th3_val),
                         latex(nR), latex(nY), latex(nB), latex(th4_val),
                         latex(th1_val), latex(th2_val), latex(th3_val), latex(th4_val), latex(n_A),
                         latex(n_A), latex(n_omega), kq_latex, kqz))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

