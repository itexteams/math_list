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


def bt_dang25_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo các biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random tử số và mẫu số của xác suất ra mặt 6 của con xúc xắc lệch (k/m)
                # k/m thường > 1/6. Ví dụ chọn k=2, m=3 hoặc k=3, m=4
                k = random.choice([2, 3, 2, 4])
                m = random.choice([3, 5, 7])
                while k >= m or Rational(k, m) <= Rational(1, 6):
                    k = randint(2, 5)
                    m = randint(3, 8)

                p6_biased = Rational(k, m)
                # Các mặt còn lại bằng nhau => (1 - k/m) / 5
                p_rest_biased = (1 - p6_biased) / 5

                p6_fair = Rational(1, 6)
                p1_fair = Rational(1, 6)

                # Tính P(B): Xác suất 2 lần đầu ra mặt 6
                # P(B) = P(A)*P(B|A) + P(not A)*P(B|not A)
                # P(B) = 1/2 * (1/6 * 1/6) + 1/2 * (k/m * k/m)
                pb_fair = p6_fair**2
                pb_biased = p6_biased**2
                pb = Rational(1, 2) * pb_fair + Rational(1, 2) * pb_biased

                # Tính P(CB): Xác suất 2 lần đầu ra mặt 6 và lần 3 ra mặt 1
                pcb_fair = p6_fair**2 * p1_fair
                pcb_biased = p6_biased**2 * p_rest_biased
                pcb = Rational(1, 2) * pcb_fair + Rational(1, 2) * pcb_biased

                # Tính P(C|B) = P(CB) / P(B)
                res_prob = pcb / pb

                p_val = res_prob.p # Tử số
                q_val = res_prob.q # Mẫu số
                while p_val + q_val>9999:
                    k = random.choice([2, 3, 2, 4])
                    m = random.choice([3, 5, 7])
                    while k >= m or Rational(k, m) <= Rational(1, 6):
                        k = randint(2, 5)
                        m = randint(3, 8)

                    p6_biased = Rational(k, m)
                    # Các mặt còn lại bằng nhau => (1 - k/m) / 5
                    p_rest_biased = (1 - p6_biased) / 5

                    p6_fair = Rational(1, 6)
                    p1_fair = Rational(1, 6)

                    # Tính P(B): Xác suất 2 lần đầu ra mặt 6
                    # P(B) = P(A)*P(B|A) + P(not A)*P(B|not A)
                    # P(B) = 1/2 * (1/6 * 1/6) + 1/2 * (k/m * k/m)
                    pb_fair = p6_fair**2
                    pb_biased = p6_biased**2
                    pb = Rational(1, 2) * pb_fair + Rational(1, 2) * pb_biased

                    # Tính P(CB): Xác suất 2 lần đầu ra mặt 6 và lần 3 ra mặt 1
                    pcb_fair = p6_fair**2 * p1_fair
                    pcb_biased = p6_biased**2 * p_rest_biased
                    pcb = Rational(1, 2) * pcb_fair + Rational(1, 2) * pcb_biased

                    # Tính P(C|B) = P(CB) / P(B)
                    res_prob = pcb / pb

                    p_val = res_prob.p # Tử số
                    q_val = res_prob.q # Mẫu số
                final_ans = p_val + q_val

                # Tạo các đáp án nhiễu
                s = []
                offsets = [-10, -5, 5, 10, 20, -20, 15, -15]
                while len(s) < 3:
                    off = random.choice(offsets)
                    fake = final_ans + off
                    if fake > 0 and fake != final_ans and fake not in s:
                        s.append(fake)

                da_d = '\\True $' + str(final_ans) + '$'
                da_s1 = '$' + str(s[0]) + '$'
                da_s2 = '$' + str(s[1]) + '$'
                da_s3 = '$' + str(s[2]) + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Bạn $A$ có hai quân xúc xắc $6$ mặt. Một xúc xắc cân đối có xác suất ra các mặt đều như nhau. Xúc xắc còn lại có xác suất ra mặt $6$ là $%s$ và xác suất ra các mặt còn lại bằng nhau. Bạn $A$ chọn ngẫu nhiên một trong hai xúc xắc và tung nó ba lần. Xác suất để lần thứ ba ra mặt $1$ khi biết cả hai lần trước đó đều ra mặt $6$ là $\\frac{p}{q}$ với $p, q$ là các số nguyên dương và số nguyên tố cùng nhau. Tổng $p+q$ bằng bao nhiêu?'''
                                 % (latex(p6_biased)))

                # Nội dung lời giải chi tiết
                loigiai = ('''Gọi $A$ là biến cố chọn được con xúc xắc cân đối. \\\\
                             $\\overline{A}$ là biến cố chọn được con xúc xắc còn lại. \\\\
                             Gọi $B$ là biến cố hai lần trước đều ra mặt $6$. \\\\
                             $C$ là biến cố lần thứ ba ra mặt $1$. \\\\
                             Ta có $P(A) = P(\\overline{A}) = \\frac{1}{2}$. \\\\
                             Xác suất ra mặt $6$ của xúc xắc cân đối là $\\frac{1}{6}$, xác suất ra mặt $6$ của xúc xắc lệch là $%s$. \\\\
                             Xác suất để hai lần đầu ra mặt $6$ là: \\\\
                             $P(B) = \\frac{1}{2} \\cdot \\left(\\frac{1}{6}\\right)^2 + \\frac{1}{2} \\cdot \\left(%s\\right)^2 = %s$. \\\\
                             Xác suất để hai lần đầu ra mặt $6$ và lần thứ ba ra mặt $1$ là: \\\\
                             (Lưu ý: Ở xúc xắc lệch, xác suất ra mặt $1$ là $(1 - %s) : 5 = %s$) \\\\
                             $P(CB) = \\frac{1}{2} \\cdot \\left(\\frac{1}{6}\\right)^2 \\cdot \\frac{1}{6} + \\frac{1}{2} \\cdot \\left(%s\\right)^2 \\cdot %s = %s$. \\\\
                             Xác suất cần tìm là xác suất có điều kiện: \\\\
                             $P(C|B) = \\frac{P(CB)}{P(B)} = \\frac{%s}{%s} = \\frac{%s}{%s}$. \\\\
                             Suy ra $p = %s, q = %s$. \\\\
                             Vậy $p + q = %s + %s = %s$.'''
                           % (latex(p6_biased), latex(p6_biased), latex(pb), 
                              latex(p6_biased), latex(p_rest_biased), 
                              latex(p6_biased), latex(p_rest_biased), latex(pcb),
                              latex(pcb), latex(pb), latex(p_val), latex(q_val),
                              latex(p_val), latex(q_val), latex(p_val), latex(q_val), latex(final_ans)))
                dapan=' \\shortans[0]{$%s$} '%(latex(final_ans))
            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

