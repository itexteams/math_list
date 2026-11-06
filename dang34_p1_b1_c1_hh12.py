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


def bt_dang34_p1_b1_c1_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. Định nghĩa các nhóm vectơ bằng nhau trên hình lập phương
                # Nhóm 1: Các cạnh ngang (trước - sau)
                g1_pos = ['\\overrightarrow{AB}', '\\overrightarrow{DC}', '\\overrightarrow{A\'B\'}', '\\overrightarrow{D\'C\'}']
                g1_neg = ['\\overrightarrow{BA}', '\\overrightarrow{CD}', '\\overrightarrow{B\'A\'}', '\\overrightarrow{C\'D\'}']

                # Nhóm 2: Các cạnh dọc (trái - phải)
                g2_pos = ['\\overrightarrow{AD}', '\\overrightarrow{BC}', '\\overrightarrow{A\'D\'}', '\\overrightarrow{B\'C\'}']
                g2_neg = ['\\overrightarrow{DA}', '\\overrightarrow{CB}', '\\overrightarrow{D\'A\'}', '\\overrightarrow{C\'B\'}']

                # Nhóm 3: Các cạnh đứng (trên - dưới)
                g3_pos = ['\\overrightarrow{AA\'}', '\\overrightarrow{BB\'}', '\\overrightarrow{CC\'}', '\\overrightarrow{DD\'}']
                g3_neg = ['\\overrightarrow{A\'A}', '\\overrightarrow{B\'B}', '\\overrightarrow{C\'C}', '\\overrightarrow{D\'D}']

                # Gộp tất cả thành 6 nhóm để dễ dàng chọn ngẫu nhiên
                groups = [g1_pos, g1_neg, g2_pos, g2_neg, g3_pos, g3_neg]

                # 2. Chọn ngẫu nhiên một nhóm làm nhóm chứa vectơ câu hỏi và đáp án đúng
                g_idx = random.randint(0, 5)
                target_group = groups[g_idx]

                # Rút ngẫu nhiên 2 vectơ khác nhau từ nhóm mục tiêu (1 cho câu hỏi, 1 cho đáp án)
                vec_q, vec_ans = random.sample(target_group, 2)
                da = f"${vec_ans}$"

                # 3. Tạo các đáp án nhiễu
                # Nhiễu 1: Lấy vectơ đối (cùng phương nhưng ngược hướng) -> lỗi học sinh hay mắc
                opp_idx = g_idx + 1 if g_idx % 2 == 0 else g_idx - 1
                opp_group = groups[opp_idx]
                distractor1 = random.choice(opp_group)

                # Nhiễu 2 & 3: Lấy vectơ ở các phương hoàn toàn khác
                other_indices = [i for i in range(6) if i != g_idx and i != opp_idx]
                other_g1, other_g2 = random.sample(other_indices, 2)

                distractor2 = random.choice(groups[other_g1])
                distractor3 = random.choice(groups[other_g2])

                das1 = f"${distractor1}$"
                das2 = f"${distractor2}$"
                das3 = f"${distractor3}$"

                # 4. Vẽ hình lập phương bằng TikZ để nhúng trực tiếp vào LaTeX
                str_tkz = '''\\begin{center}
