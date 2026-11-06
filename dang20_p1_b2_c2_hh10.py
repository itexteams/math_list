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


def bt_dang20_p1_b2_c2_hh10(self):
            # Khai báo biến
            # Random độ dài cạnh của hình vuông
            a = random.randint(1, 45)

            # Tính toán kết quả chính xác và làm tròn đến hàng phần mười
            kq_val = 1.5 * a * math.sqrt(2)
            kq_round = round(kq_val, 1)

            # Định dạng kết quả hiển thị (chuyển dấu . thành dấu ,)
            kq_str = f"{kq_round:.1f}".replace('.', ',')

            # Tạo các đáp án nhiễu (dao động quanh đáp án đúng)
            s = [
                round(kq_val + 0.1, 1),
                round(kq_val - 0.1, 1),
                round(kq_val + 0.2, 1),
                round(kq_val - 0.2, 1),
                round(kq_val + 1.0, 1)
            ]
            random.shuffle(s)

            # Khởi tạo danh sách đáp án
            dapan_dung = f'${kq_str}$'
            dapan_sai = [f'${f"{x:.1f}".replace(".", ",")}$' for x in s[:3]]

            list_1 = ['\\True ' + dapan_dung] + dapan_sai
            random.shuffle(list_1) # Trộn ngẫu nhiên vị trí đáp án đúng

            # ==========================================
            # Tạo nội dung Câu hỏi và Lời giải
            # ==========================================

            noidungcauhoi = (f"Cho hình vuông $ABCD$ có tâm là $O$ và cạnh ${a}$. Tính $|\\overrightarrow{{OA}} - \\overrightarrow{{CB}}| + |\\overrightarrow{{CD}} - \\overrightarrow{{DA}}|$. Kết quả làm tròn đến hàng phần mười.")

            # Code vẽ hình bằng TikZ tự động chèn vào lời giải
            tikz_code = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                '\\coordinate (A) at (0,3);\n'
                '\\coordinate (B) at (3,3);\n'
                '\\coordinate (C) at (3,0);\n'
                '\\coordinate (D) at (0,0);\n'
                '\\coordinate (O) at (1.5,1.5);\n'
                '\\draw (A)--(B)--(C)--(D)--cycle;\n'
                '\\draw (A)--(C) (B)--(D);\n'
                '\\foreach \\p/\\pos in {A/above left, B/above right, C/below right, D/below left, O/above}\n'
                '\\fill (\\p) circle (1.5pt) node[\\pos] {$\\p$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
            )

            # Lời giải chi tiết
            loigiai = (
                f"{tikz_code}"
                f"+ Vì $O$ là tâm của hình vuông nên $\\overrightarrow{{OA}} = \\overrightarrow{{CO}}$ suy ra $\\overrightarrow{{OA}} - \\overrightarrow{{CB}} = \\overrightarrow{{CO}} - \\overrightarrow{{CB}} = \\overrightarrow{{BO}}$. \\\\\n"
                f"Vậy $|\\overrightarrow{{OA}} - \\overrightarrow{{CB}}| = |\\overrightarrow{{BO}}| = \\frac{{{a}\\sqrt{{2}}}}{{2}}$. \\\\\n"
                f"+ Do $ABCD$ là hình vuông nên $\\overrightarrow{{CD}} = \\overrightarrow{{BA}}$ suy ra $\\overrightarrow{{CD}} - \\overrightarrow{{DA}} = \\overrightarrow{{BA}} + \\overrightarrow{{AD}} = \\overrightarrow{{BD}}$. \\\\\n"
                f"Mà $|\\overrightarrow{{BD}}| = BD = \\sqrt{{AB^2 + AD^2}} = {a}\\sqrt{{2}}$ suy ra $|\\overrightarrow{{CD}} - \\overrightarrow{{DA}}| = {a}\\sqrt{{2}}$. \\\\\n"
                f"Khi đó $|\\overrightarrow{{OA}} - \\overrightarrow{{CB}}| + |\\overrightarrow{{CD}} - \\overrightarrow{{DA}}| = \\frac{{{a}\\sqrt{{2}}}}{{2}} + {a}\\sqrt{{2}} = \\frac{{3 \\cdot {a}\\sqrt{{2}}}}{{2}} \\approx {kq_str}$."
            )

            # ==========================================
            # Xuất câu trắc nghiệm theo đúng form yêu cầu
            # ==========================================

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{\n' + str(loigiai) + '\n}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

