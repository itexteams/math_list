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


def bt_dang35_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo và random số liệu
                u1 = 1
                d = random.randint(2, 5)  # Công sai d
                N = 2 * random.randint(35, 60)  # Số lượng số hạng N (chẵn)
                k = random.randint(35, 65)  # Số hạng cuối của tổng S

                # Tính toán các giá trị phụ thuộc
                N_half = N // 2
                N_minus_1 = N - 1
                S_N = N_half * (2 * u1 + N_minus_1 * d)

                k_minus_1 = k - 1
                u_k = u1 + k_minus_1 * d

                num_sd = k_minus_1 * d
                den_sd = u_k

                a = k_minus_1
                b = u_k
                kq = b - 2 * a  # Giá trị b - 2a cần tìm

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq))]
                da = random.choice(du)

                s = [
                    '$%s$' % (latex(kq + 1)),
                    '$%s$' % (latex(kq + 2)),
                    '$%s$' % (latex(kq + 3)),
                    '$%s$' % (latex(kq - 1)),
                    '$%s$' % (latex(kq - 2)),
                    '$%s$' % (latex(kq - 3)),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Nội dung câu hỏi
                noidungcauhoi = (
                    '''Cho cấp số cộng $(u_n)$ có số hạng đầu bằng $%s$ và tổng $%s$ số hạng đầu bằng $%s$. Biết tổng $\\frac{1}{u_1u_2} + \\frac{1}{u_2u_3} + \\dots + \\frac{1}{u_{%s}u_{%s}} = \\frac{a}{b}, a;b \\in \\mathbb{N}, \\frac{a}{b}$ là phân số tối giản. Giá trị $b - 2a$ bằng bao nhiêu?'''
                    % (latex(u1), latex(N), latex(S_N), latex(k_minus_1), latex(k))
                )

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (
                    '''Gọi $d$ là công sai của cấp số cộng. Ta có $S_{%s} = %s(2u_1 + %sd) = %s$ với $u_1 = %s \\Rightarrow d = %s$\\\\
            Đặt $S = \\frac{1}{u_1u_2} + \\frac{1}{u_2u_3} + \\dots + \\frac{1}{u_{%s}u_{%s}}$.\\\\
            Ta có $S \\cdot d = \\frac{d}{u_1u_2} + \\frac{d}{u_2u_3} + \\dots + \\frac{d}{u_{%s}u_{%s}} = \\frac{u_2 - u_1}{u_1u_2} + \\frac{u_3 - u_2}{u_2u_3} + \\dots + \\frac{u_{%s} - u_{%s}}{u_{%s}u_{%s}} = \\frac{1}{u_1} - \\frac{1}{u_{%s}}$\\\\
            $= %s - \\frac{1}{%s + %s \\cdot %s} = \\frac{%s}{%s}$.\\\\
            Với $d = %s$ nên $S = \\frac{%s}{%s} \\longrightarrow a = %s; b = %s$.\\\\
            Vậy $b - 2a = %s$.'''
                    % (
                        latex(N),
                        latex(N_half),
                        latex(N_minus_1),
                        latex(S_N),
                        latex(u1),
                        latex(d),
                        latex(k_minus_1),
                        latex(k),
                        latex(k_minus_1),
                        latex(k),
                        latex(k),
                        latex(k_minus_1),
                        latex(k_minus_1),
                        latex(k),
                        latex(k),
                        latex(u1),
                        latex(u1),
                        latex(k_minus_1),
                        latex(d),
                        latex(num_sd),
                        latex(den_sd),
                        latex(d),
                        latex(a),
                        latex(b),
                        latex(a),
                        latex(b),
                        latex(kq),
                    )
                )
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

