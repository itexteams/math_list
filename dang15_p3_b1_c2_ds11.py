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


def bt_dang15_p3_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Sinh ngẫu nhiên tham số k và các số hạng ban đầu
                k = randint(0, 5)
                u1_val = randint(1, 5)
                diff = randint(1, 5)
                u2_val = u1_val + diff
                v1_val = diff

                # Định dạng hệ thức truy hồi và các bước biến đổi theo k
                if k == 0:
                    rec_tex = "a u_{n+1} + (1 - a) u_n"
                    step1_tex = "u_{n+2} - u_{n+1} = (a - 1) u_{n+1} + (1 - a) u_n"
                    step2_tex = "u_{n+2} - u_{n+1} = (a - 1) (u_{n+1} - u_n)"
                    q_tex = "a - 1"
                    cond_tex = "a - 1 > 0 \\Leftrightarrow a > 1"
                    h_val = 1
                else:
                    kp1 = k + 1
                    rec_tex = "(a - %s) u_{n+1} + (%s - a) u_n" % (latex(k), latex(kp1))
                    step1_tex = "u_{n+2} - u_{n+1} = (a - %s) u_{n+1} + (%s - a) u_n" % (latex(kp1), latex(kp1))
                    step2_tex = "u_{n+2} - u_{n+1} = (a - %s) (u_{n+1} - u_n)" % (latex(kp1))
                    q_tex = "a - %s" % (latex(kp1))
                    cond_tex = "a - %s > 0 \\Leftrightarrow a > %s" % (latex(kp1), latex(kp1))
                    h_val = kp1

                # Đáp án đúng
                kq = h_val
                da = "$%s$" % (latex(kq))

                # Tạo danh sách các phương án sai
                s_candidates = [
                    kq + 1,
                    kq - 1 if kq - 1 > 0 else kq + 4,
                    kq + 2,
                    kq + 3,
                    2 * kq + 1,
                    kq + 4
                ]

                s = []
                for cand in s_candidates:
                    cand_str = "$%s$" % (latex(cand))
                    if cand != kq and cand_str not in s and cand > 0:
                        s.append(cand_str)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Cho dãy số $(u_n)$ biết $\\begin{cases} u_1 = %s; u_2 = %s \\\\ u_{n+2} = %s, \\forall n \\in \\mathbb{N}^* \\end{cases}$. Gọi $S$ là tập hợp tất cả các giá trị của $a$ để dãy số $(u_n)$ tăng. Biết $S = (h; +\\infty)$. Giá trị $h$ bằng bao nhiêu?'''
                                 % (latex(u1_val), latex(u2_val), rec_tex))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có: $u_{n+2} = %s$\\\\
            $\\Leftrightarrow %s$\\\\
            $\\Leftrightarrow %s$ với mọi $n \\ge 1$.\\\\
            Đặt $v_n = u_{n+1} - u_n$ với mọi $n \\ge 1$.\\\\
            Ta có $v_1 = u_2 - u_1 = %s - %s = %s > 0$.\\\\
            Suy ra $v_{n+1} = (%s) v_n$ với mọi $n \\ge 1$.\\\\
            Do đó, $(v_n)$ là một cấp số nhân với số hạng đầu $v_1 = %s$ và công bội $q = %s$.\\\\
            Số hạng tổng quát của $(v_n)$ là $v_n = v_1 \\cdot q^{n-1} = %s \\cdot (%s)^{n-1}$.\\\\
            Dãy số $(u_n)$ là dãy số tăng khi và chỉ khi $u_{n+1} > u_n$ với mọi $n \\ge 1$, tức là $v_n > 0$ với mọi $n \\ge 1$.\\\\
            Vì $v_1 = %s > 0$ nên $v_n > 0$ với mọi $n \\ge 1 \\Leftrightarrow %s$.\\\\
            Do đó $S = (%s; +\\infty)$, suy ra $h = %s$.\\\\
            Vậy $h = %s$.'''
                           % (rec_tex, step1_tex, step2_tex,
                              latex(u2_val), latex(u1_val), latex(v1_val),
                              q_tex,
                              latex(v1_val), q_tex,
                              latex(v1_val), q_tex,
                              latex(v1_val), cond_tex,
                              latex(h_val), latex(h_val), latex(h_val)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(h_val))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

