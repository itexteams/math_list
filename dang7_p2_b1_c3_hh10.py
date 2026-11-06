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


def bt_dang7_p2_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            def generate_problem():
                while True:
                    # Random tọa độ các điểm M, N và trực tâm H để tạo ra các đường thẳng đẹp
                    xm, ym = random.randint(-3, 3), random.randint(-3, 3)
                    xn, yn = random.randint(-3, 3), random.randint(-3, 3)
                    xh, yh = random.randint(-3, 3), random.randint(-3, 3)

                    # Đảm bảo các điểm không trùng nhau và không thẳng hàng
                    if (xm, ym) != (xn, yn) and (xm, ym) != (xh, yh) and (xn, yn) != (xh, yh):
                        # Phương trình MN đi qua M và N
                        # (yn-ym)x - (xn-xm)y + ym(xn-xm) - xm(yn-ym) = 0
                        a1, b1 = yn - ym, -(xn - xm)
                        c1 = -a1 * xm - b1 * ym

                        # Phương trình MK đi qua M và H
                        a2, b2 = yh - ym, -(xh - xm)
                        c2 = -a2 * xm - b2 * ym

                        # Phương trình NQ đi qua N và H
                        a3, b3 = yh - yn, -(xh - xn)
                        c3 = -a3 * xn - b3 * yn

                        # Kiểm tra tính hợp lệ (các đường thẳng không trùng hoặc song song)
                        if a1*b2 != a2*b1 and a1*b3 != a3*b1 and a2*b3 != a3*b2:
                            return (a1, b1, c1), (a2, b2, c2), (a3, b3, c3), (xm, ym), (xn, yn)

            # Khởi tạo dữ liệu bài toán
            (a1, b1, c1), (a2, b2, c2), (a3, b3, c3), (xm, ym), (xn, yn) = generate_problem()

            # Phương trình các đường thẳng dưới dạng biểu thức Sympy
            pt_MN = a1*x + b1*y + c1
            pt_MK = a2*x + b2*y + c2
            pt_NQ = a3*x + b3*y + c3

            # Tính toán các giá trị đúng
            # NP đi qua N(xn, yn) và vuông góc với MK(a2, b2) => VTPT là (b2, -a2)
            a_np, b_np = b2, -a2
            c_np = -a_np * xn - b_np * yn
            pt_NP_dung = a_np*x + b_np*y + c_np

            # MP đi qua M(xm, ym) và vuông góc với NQ(a3, b3) => VTPT là (b3, -a3)
            a_mp, b_mp = b3, -a3
            c_mp = -a_mp * xm - b_mp * ym
            pt_MP_dung = a_mp*x + b_mp*y + c_mp

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tam giác $MNP$ có phương trình đường thẳng chứa cạnh $MN$ là $%s=0$, phương trình đường cao $MK (K \\in NP)$ là $%s=0$, phương trình đường cao $NQ (Q \\in MP)$ là $%s=0$.''' 
                             % (latex(pt_MN), latex(pt_MK), latex(pt_NQ)))

            ########################################################################
            # a) Tọa độ điểm M
            m_da_d = '\\True Điểm $M$ có tọa độ là $(%s; %s)$' % (xm, ym)
            m_da_s = 'Điểm $M$ có tọa độ là $(%s; %s)$' % (xm + 1, ym - 1)
            list_m = [m_da_d, m_da_s]

            loigiai_m = ('''Điểm $M$ là giao điểm của đường thẳng $MN$ và đường cao $MK$. Tọa độ điểm $M$ là nghiệm của hệ phương trình: \\\\
            $\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$. Vậy $M(%s; %s)$.''' 
                         % (latex(pt_MN), latex(pt_MK), xm, ym, xm, ym))

            ########################################################################
            # b) Tọa độ điểm N
            n_da_d = '\\True Điểm $N$ có tọa độ là $(%s; %s)$' % (xn, yn)
            n_da_s = 'Điểm $N$ có tọa độ là $(%s; %s)$' % (xn - 2, yn + 1)
            list_n = [n_da_d, n_da_s]

            loigiai_n = ('''Điểm $N$ là giao điểm của đường thẳng $MN$ và đường cao $NQ$. Tọa độ điểm $N$ là nghiệm của hệ phương trình: \\\\
            $\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$. Vậy $N(%s; %s)$.''' 
                         % (latex(pt_MN), latex(pt_NQ), xn, yn, xn, yn))

            ########################################################################
            # c) Phương trình cạnh NP
            np_da_d = '\\True Phương trình đường thẳng $NP$ là $%s = 0$' % (latex(pt_NP_dung))
            np_da_s = 'Phương trình đường thẳng $NP$ là $%s = 0$' % (latex(pt_NP_dung + random.randint(1, 5)))
            list_np = [np_da_d, np_da_s]

            loigiai_np = ('''Đường thẳng $NP$ đi qua điểm $N(%s; %s)$ và vuông góc với đường cao $MK: %s = 0$. \\\\
            Đường thẳng $MK$ có vectơ pháp tuyến $\\vec{n}_{MK} = (%s; %s)$ nên có vectơ chỉ phương $\\vec{u}_{MK} = (%s; %s)$. \\\\
            Vì $NP \\perp MK$ nên đường thẳng $NP$ nhận $\\vec{u}_{MK} = (%s; %s)$ làm vectơ pháp tuyến. \\\\
            Phương trình đường thẳng $NP$ là: $%s(x - (%s)) + (%s)(y - (%s)) = 0 \\Leftrightarrow %s = 0$.''' 
                          % (xn, yn, latex(pt_MK), a2, b2, b2, -a2, b2, -a2, b2, xn, -a2, yn, latex(pt_NP_dung)))

            ########################################################################
            # d) Phương trình cạnh MP
            mp_da_d = '\\True Phương trình đường thẳng $MP$ là $%s = 0$' % (latex(pt_MP_dung))
            mp_da_s = 'Phương trình đường thẳng $MP$ là $%s = 0$' % (latex(pt_MP_dung + random.randint(1, 5)))
            list_mp = [mp_da_d, mp_da_s]

            loigiai_mp = ('''Đường thẳng $MP$ đi qua điểm $M(%s; %s)$ và vuông góc với đường cao $NQ: %s = 0$. \\\\
            Đường thẳng $NQ$ có vectơ pháp tuyến $\\vec{n}_{NQ} = (%s; %s)$ nên có vectơ chỉ phương $\\vec{u}_{NQ} = (%s; %s)$. \\\\
            Vì $MP \\perp NQ$ nên đường thẳng $MP$ nhận $\\vec{u}_{NQ} = (%s; %s)$ làm vectơ pháp tuyến. \\\\
            Phương trình đường thẳng $MP$ là: $%s(x - (%s)) + (%s)(y - (%s)) = 0 \\Leftrightarrow %s = 0$.''' 
                          % (xm, ym, latex(pt_NQ), a3, b3, b3, -a3, b3, -a3, b3, xm, -a3, ym, latex(pt_MP_dung)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp chọn đáp án ngẫu nhiên đảm bảo có 1-3 câu đúng
            while True:
                da_a = random.choice(list_m)
                da_b = random.choice(list_n)
                da_c = random.choice(list_np)
                da_d = random.choice(list_mp)

                if 1 <= count_true_answers([da_a, da_b, da_c, da_d]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(da_a) + '}\n'
                '{' + str(da_b) + '}\n'
                '{' + str(da_c) + '}\n'
                '{' + str(da_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_m) + '\n'
                '\\item ' + str(loigiai_n) + '\n'
                '\\item ' + str(loigiai_np) + '\n'
                '\\item ' + str(loigiai_mp) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   

