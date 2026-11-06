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


def bt_dang26_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo danh sách dạng (ở đây chỉ có 1 dạng bài Bayes)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # p_pt: Phần trăm học sinh chọn khối D (Ví dụ: 60%)
                p_pt = random.choice([40, 50, 60, 70, 75])
                pa_val = Rational(p_pt, 100)
                pna_val = 1 - pa_val

                # p1: Xác suất đỗ nếu chọn khối D (Ví dụ: 0,7)
                # p2: Xác suất đỗ nếu không chọn khối D (Ví dụ: 0,8)
                p1_num = random.randint(5, 8)
                p2_num = random.randint(5, 9)
                # Đảm bảo p1 và p2 không quá gần nhau để bài toán hay hơn
                if p1_num == p2_num:
                    p2_num = p1_num + 1 if p1_num < 9 else p1_num - 1

                pba_val = Rational(p1_num, 10)
                pbna_val = Rational(p2_num, 10)

                # Tính toán theo công thức Bayes: P(A|B) = [P(A)*P(B|A)] / [P(A)*P(B|A) + P(not A)*P(B|not A)]
                tu_so = pa_val * pba_val
                mau_so = pa_val * pba_val + pna_val * pbna_val
                p_final = simplify(tu_so / mau_so)

                m = p_final.p # Tử số phân số tối giản
                n = p_final.q # Mẫu số phân số tối giản
                ket_qua_dung = m + n

                # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = ket_qua_dung + random.choice([-10, -5, 5, 10, 12, -8, 15, 20])
                    if sai > 0 and sai != ket_qua_dung:
                        s.add(f'${sai}$')

                list_sai = list(s)
                da_d = '\\True $%s$' % (ket_qua_dung)
                da_s1 = list_sai[0]
                da_s2 = list_sai[1]
                da_s3 = list_sai[2]

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # B2: Viết lại nội dung câu hỏi
                noidungcauhoi = (
                    "Trong kì thi tốt nghiệp trung học phổ thông, trường THPT A có $%s \\%%$ học sinh lựa chọn khối D để xét tuyển đại học. "
                    "Biết rằng, nếu một học sinh lựa chọn khối D thì xác suất để học sinh đó đỗ đại học là $%s$ còn nếu học sinh không lựa chọn khối D "
                    "thì xác suất để học sinh đó đỗ đại học là $%s$. Chọn ngẫu nhiên một học sinh của trường THPT A đã tốt nghiệp trong kì thi trên. "
                    "Giả sử xác suất để học sinh đó chọn khối D biết học sinh này đã đỗ đại học là $\\frac{m}{n}$ với $n$ là số nguyên dương và "
                    "$\\frac{m}{n}$ là phân số tối giản. Tổng $m+n$ bằng bao nhiêu?"
                    % (latex(p_pt), latex(float(pba_val)).replace('.', ','), latex(float(pbna_val)).replace('.', ','))
                )

                # Nội dung lời giải chi tiết theo mẫu ảnh
                loigiai = (
                    "Gọi A là biến cố: \"Học sinh đó chọn khối D\" \\\\ "
                    "B là biến cố: \"Học sinh đó đỗ đại học\" \\\\ "
                    "Ta có: $P(A) = %s$; $P(\\overline{A}) = 1 - %s = %s$; $P(B|A) = %s$ và $P(B|\\overline{A}) = %s$ \\\\ "
                    "Áp dụng công thức Bayes, ta có: \\\\ "
                    "$$P(A|B) = \\frac{P(A).P(B|A)}{P(A).P(B|A) + P(\\overline{A}).P(B|\\overline{A})} = "
                    "\\frac{%s . %s}{%s . %s + %s . %s} = \\frac{%s}{%s}$$ \\\\ "
                    "Vì $\\frac{%s}{%s}$ là phân số tối giản nên $m = %s, n = %s$. \\\\ "
                    "Vậy $m + n = %s$."
                    % (
                        latex(float(pa_val)).replace('.', ','), 
                        latex(float(pa_val)).replace('.', ','), 
                        latex(float(pna_val)).replace('.', ','), 
                        latex(float(pba_val)).replace('.', ','), 
                        latex(float(pbna_val)).replace('.', ','),
                        latex(float(pa_val)).replace('.', ','), latex(float(pba_val)).replace('.', ','),
                        latex(float(pa_val)).replace('.', ','), latex(float(pba_val)).replace('.', ','),
                        latex(float(pna_val)).replace('.', ','), latex(float(pbna_val)).replace('.', ','),
                        latex(m), latex(n), latex(m), latex(n), latex(m), latex(n), latex(ket_qua_dung)
                    )
                )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(ket_qua_dung))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu (không dùng tiền tố r)
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

