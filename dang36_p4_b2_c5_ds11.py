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


def bt_dang36_p4_b2_c5_ds11(self):
            # Khai báo biến
            # --- BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM ---
            # Ta sẽ random 3 số nguyên dương A, B, C trong biểu thức P.
            A = random.randint(1900, 2100)
            B = random.randint(1900, 2100)
            C = random.randint(10, 100)

            kq_dung = A + B + C


            dap_an_sai = set()
            while len(dap_an_sai) < 3:
                # Tạo các phương án nhiễu bằng cách thay đổi giá trị tổng
                sai = kq_dung + random.choice([-100, -50, 1, 10, 20, 50, 100, -10, -20])
                if sai != kq_dung:
                    dap_an_sai.add(sai)

            list_sai = list(dap_an_sai)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho ba số thực dương $x, y, z$ theo thứ tự lập thành một cấp số nhân, đồng thời với mỗi số thực dương $a \, (a \neq 1)$ thì $\log_{a} x, \log_{\sqrt{a}} y, \log_{\sqrt[3]{a}} z$ theo thứ tự lập thành một cấp số cộng. Tính $P = \frac{%s x}{y} + \frac{%s y}{z} + \frac{%s z}{x}$.'''
                             % (latex(A), latex(B), latex(C)))

            # Các đáp án
            da_d = r'\True $%s$' % latex(kq_dung)
            da_s1 = r'$%s$' % latex(list_sai[0])
            da_s2 = r'$%s$' % latex(list_sai[1])
            da_s3 = r'$%s$' % latex(list_sai[2])

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = (r'''Ta có: $x, y, z$ là ba số thực dương, theo thứ tự lập thành một cấp số nhân thì $y^2 = x \cdot z \quad (1)$. \\
            Với mỗi số thực dương $a \, (a \neq 1)$, $\log_{a} x, \log_{\sqrt{a}} y, \log_{\sqrt[3]{a}} z$ theo thứ tự lập thành một cấp số cộng thì: \\
            $2\log_{\sqrt{a}} y = \log_{a} x + \log_{\sqrt[3]{a}} z \Leftrightarrow 4\log_{a} y = \log_{a} x + 3\log_{a} z \quad (2)$. \\
            Thay (1) vào (2), ta có $2\log_{a} y = \log_{a}(x \cdot z)$, do đó (2) trở thành: \\
            $2(2\log_{a} y) = 2\log_{a}(x \cdot z) \Leftrightarrow 2\log_{a} x + 2\log_{a} z = \log_{a} x + 3\log_{a} z$ \\
            $\Leftrightarrow \log_{a} x = \log_{a} z \Leftrightarrow x = z$. \\
            Từ (1) ta suy ra $y^2 = x^2 \Rightarrow y = x$ (vì $x, y > 0$). Vậy $x = y = z$. \\
            Thay vào biểu thức ta được: $P = %s + %s + %s = %s$.'''
                       % (latex(A), latex(B), latex(C), latex(kq_dung)))

            # Xuất kết quả theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

