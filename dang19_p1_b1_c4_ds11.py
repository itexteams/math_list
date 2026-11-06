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


def bt_dang19_p1_b1_c4_ds11(self):
            # Khai báo biến
            k = randint(1, 10) 

            kq_chuan = Rational(3 * k, 4)


            lis_phuongan = []

            # Đáp án đúng
            da_dung = kq_chuan 
            lis_phuongan.append(da_dung)

            # Đáp án sai 1: Cộng thêm 1/4
            da_sai1 = kq_chuan + Rational(1, 4)
            lis_phuongan.append(da_sai1)

            # Đáp án sai 2: Trừ đi 1/4 (nếu âm hoặc bằng 0 thì cộng 1/2)
            da_sai2 = kq_chuan - Rational(1, 4)
            if da_sai2 <= 0: 
                da_sai2 = kq_chuan + Rational(1, 2)
            lis_phuongan.append(da_sai2)

            # Đáp án sai 3: Kết quả = k (bẫy học sinh quên nhân 3/4) hoặc k/2
            da_sai3 = Rational(k, 2)
            if da_sai3 in lis_phuongan: # Tránh trùng
                da_sai3 = Rational(5 * k, 4)
            lis_phuongan.append(da_sai3)

            # Xáo trộn đáp án để hiển thị ngẫu nhiên
            # Lưu lại text hiển thị
            choices_text = [f"${latex(x)}$" for x in lis_phuongan]
            random.shuffle(choices_text)

            # Tìm vị trí đáp án đúng sau khi shuffle để đánh dấu \True
            final_choices = []
            for item in choices_text:
                if item == f"${latex(da_dung)}$":
                    final_choices.append(f"\\True {item}")
                else:
                    final_choices.append(item)

            # --- Xây dựng nội dung lời giải (LaTeX) ---

            # Xử lý hiển thị tử số trong chuỗi LaTeX
            tu_so = str(k) if k > 1 else "1" # Nếu k=1 thì hiển thị số 1, không cần ẩn
            k_factor = f"{k} \\cdot" if k > 1 else "" # Dùng cho lời giải đoạn tách k ra ngoài
            k_frac = f"\\frac{{{k}}}{{2}}" if k > 1 else "\\frac{1}{2}"

            # Nội dung câu hỏi
            noidungcauhoi = (
                f"Cho dãy số $(u_n)$ biết $u_n = \\frac{{{tu_so}}}{{2^2 - 1}} + \\frac{{{tu_so}}}{{3^2 - 1}} + \\dots + \\frac{{{tu_so}}}{{n^2 - 1}}$. Giới hạn của dãy số là"
            )

            # Nội dung lời giải
            loigiai = (
                "Ta có: \n"
                f"$$u_n = \\frac{{{tu_so}}}{{2^2 - 1}} + \\frac{{{tu_so}}}{{3^2 - 1}} + \\dots + \\frac{{{tu_so}}}{{n^2 - 1}}$$\n"
                f"$$= \\frac{{{tu_so}}}{{1 \\cdot 3}} + \\frac{{{tu_so}}}{{2 \\cdot 4}} + \\frac{{{tu_so}}}{{3 \\cdot 5}} + \\dots + \\frac{{{tu_so}}}{{(n-1)(n+1)}}$$\n"
                f"$$= {k_frac} \\left( 1 - \\frac{{1}}{{3}} + \\frac{{1}}{{2}} - \\frac{{1}}{{4}} + \\frac{{1}}{{3}} - \\frac{{1}}{{5}} + \\dots + \\frac{{1}}{{n-1}} - \\frac{{1}}{{n+1}} \\right)$$\n"
                f"$$= {k_frac} \\left( 1 + \\frac{{1}}{{2}} - \\frac{{1}}{{n}} - \\frac{{1}}{{n+1}} \\right) = {k_frac} \\left( \\frac{{3}}{{2}} - \\frac{{1}}{{n}} - \\frac{{1}}{{n+1}} \\right)$$\n"
                f"$$= \\frac{{{latex(Rational(3*k, 4))}}}{{1}} - \\frac{{{latex(Rational(k, 2))}}}{{n}} - \\frac{{{latex(Rational(k, 2))}}}{{n+1}}.$$\n"
                "Suy ra: \n"
                f"$$\\lim_{{n\\to +\\infty}} u_n = \\lim_{{n\\to +\\infty}} \\left[ \\frac{{{latex(Rational(3*k, 4))}}}{{1}} - \\frac{{{latex(Rational(k, 2))}}}{{n}} - \\frac{{{latex(Rational(k, 2))}}}{{n+1}} \\right] = {latex(kq_chuan)}.$$"
            )

            # --- Xuất kết quả theo định dạng yêu cầu ---
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\choice \n'
                '{' + final_choices[0] + '}\n'
                '{' + final_choices[1] + '}\n'
                '{' + final_choices[2] + '}\n'
                '{' + final_choices[3] + '}\n'
                '\\loigiai{\n' + loigiai + '\n}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

