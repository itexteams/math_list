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


def bt_dang29_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- ĐÁP ÁN ĐÚNG (Hàm số chứa căn bậc hai luôn xác định trên R) ---
                # Chọn ngẫu nhiên giữa sin x hoặc cos x
                ham_dung = random.choice(['\\cos x', '\\sin x'])
                b = random.randint(1, 3)
                a = b + random.randint(0, 2) # Đảm bảo a >= b để biểu thức luôn >= 0

                chuoi_da_dung = f"y = \\sqrt{{{a} + {b}{ham_dung}}}" if b != 1 else f"y = \\sqrt{{{a} + {ham_dung}}}"
                pt_trong_can = f"{a} + {b}{ham_dung} \\ge 0" if b != 1 else f"{a} + {ham_dung} \\ge 0"

                if a == b:
                    he_qua = f"{ham_dung} \\ge -1"
                else:
                    # Nếu a > b, rút ra điều kiện dạng phân số hoặc số cụ thể
                    he_qua = f"{ham_dung} \\ge -\\frac{{{a}}}{{{b}}}" if b > 1 else f"{ham_dung} \\ge -{a}"

                # --- CÁC PHƯƠNG ÁN SAI (Nhiễu) ---
                # Phương án sai 1: Dạng phân thức chứa cot^2(x) hoặc tan^2(x) dưới mẫu (Không xác định tại điểm cot/tan không xác định)
                m1 = random.randint(1, 4)
                chuoi_sai_1 = f"y = \\frac{{\\cos^2 x + {m1}}}{{\\cot^2 x + 1}}"

                # Phương án sai 2: Dạng chứa cot hoặc tan có chứa hệ số nhân góc
                k1 = random.randint(2, 4)
                chuoi_sai_2 = f"y = \\cot {k1}x - \\tan x"

                # Phương án sai 3: Hàm số chứa căn ở góc nhưng biểu thức góc có điều kiện x >= -m2
                m2 = random.randint(1, 5)
                chuoi_sai_3 = f"y = \\sin \\sqrt{{x + {m2}}}"

                # Đóng gói chuỗi đưa vào hệ thống trắc nghiệm
                da = f"${chuoi_da_dung}$"
                das1 = f"${chuoi_sai_1}$"
                das2 = f"${chuoi_sai_2}$"
                das3 = f"${chuoi_sai_3}$"

                # Câu hỏi
                noidungcauhoi = ('''Hàm số nào có tập xác định là $\\mathbb{R}$?''')

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo các bước như hình mẫu
                loigiai = ('''$%s$ được xác định $\\Leftrightarrow %s \\Leftrightarrow %s$ (luôn đúng với $\\forall x \\in \\mathbb{{R}}$). \\\\ Vậy tập xác định của hàm số $%s$ là $\\mathbb{{R}}$.'''
                           % (chuoi_da_dung, pt_trong_can, he_qua, chuoi_da_dung))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

