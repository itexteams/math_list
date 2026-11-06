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


def bt_dang10_p3_b1_c4_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                C = random.randint(2, 25) 
                L_ket_qua_random = C 
                # Chuẩn bị đáp án đúng: Thêm $ bao quanh biểu thức L = ...
                da_dung_tex_r = f'$L = {latex(L_ket_qua_random)}$' 
                da_d_r = ('\\True ' + str(da_dung_tex_r))
                so_sai_r = set()
                while len(so_sai_r) < 3:
                    # Chọn ngẫu nhiên một giá trị sai, ví dụ từ 1 đến 6 và đảm bảo nó khác C
                    sai_ngau_nhien = random.choice([1, 1, 2, 2.5, 3.5, 4.5, 5, 5.5, 6, 6.5]) 
                    if abs(sai_ngau_nhien - L_ket_qua_random) > 0.1: 
                        so_sai_r.add(sai_ngau_nhien)
                list_so_sai_r = [Rational(s) for s in list(so_sai_r)]
                # Chuyển đổi thành LaTeX: Thêm $ bao quanh biểu thức L = ...
                da_sai_1_tex_r = f'$L = {latex(list_so_sai_r[0])}$' 
                da_sai_2_tex_r = f'$L = {latex(list_so_sai_r[1])}$'
                da_sai_3_tex_r = f'$L = {latex(list_so_sai_r[2])}$'
                da_s1_r = str(da_sai_1_tex_r)
                da_s2_r = str(da_sai_2_tex_r)
                da_s3_r = str(da_sai_3_tex_r)
                # Đưa các đáp án vào 1 danh sách và random
                list_random_r = [da_d_r, da_s1_r, da_s2_r, da_s3_r]
                random.shuffle(list_random_r)
                # Câu hỏi
                noidungcauhoi = ('''Với $n$ là số nguyên dương, đặt $S_n = \\frac{%(C)s}{1\\sqrt{2} + 2\\sqrt{1}} + \\frac{%(C)s}{2\\sqrt{3} + 3\\sqrt{2}} + \\dots + \\frac{%(C)s}{n\\sqrt{n+1} + (n+1)\\sqrt{n}}$. Khi đó $\\lim_{n \\to +\\infty} S_n$ bằng bao nhiêu?'''
                                        %{'C': latex(C)})

                # Nội dung lời giải
                loigiai = ('''Ta có số hạng tổng quát $u_k = \\frac{%(C)s}{k\\sqrt{k+1} + (k+1)\\sqrt{k}}$. \\\\
                                  Biến đổi: $u_k = %(C)s \\cdot \\left( \\frac{1}{\\sqrt{k}} - \\frac{1}{\\sqrt{k+1}} \\right) = \\frac{%(C)s}{\\sqrt{k}} - \\frac{%(C)s}{\\sqrt{k+1}}$. \\\\
                                  Tổng rút gọn: $S_n = \\sum_{k=1}^{n} u_k = \\frac{%(C)s}{\\sqrt{1}} - \\frac{%(C)s}{\\sqrt{n+1}} = %(C)s - \\frac{%(C)s}{\\sqrt{n+1}}$. \\\\
                                  Suy ra $\\lim S_n = \\lim_{n \\to +\\infty} \\left( %(C)s - \\frac{%(C)s}{\\sqrt{n+1}} \\right) = %(C)s - 0 = %(C)s$.'''
                                        %{'C': latex(C)})


                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(C))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

