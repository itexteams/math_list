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


def bt_dang16_p3_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo danh sách các số nguyên tố để làm cơ số
            primes = [2, 3, 5, 7, 11]

            # B1: Ngẫu nhiên các tham số
            # Chọn 3 số nguyên tố khác nhau x, y, z
            x, y, z = random.sample(primes, 3)
            # Chọn số mũ k (trong hình là 2 vì 45 = 3^2 * 5)
            k = random.randint(2, 5)

            # Tính toán các giá trị hiển thị trong đề bài
            base_log = x * y
            val_log = (y**k) * z

            # Các giá trị m, n, p theo công thức biến đổi
            m = 1
            n = k
            p = 1
            kq_dung = m + n + p

            # B2: Tạo các phương án nhiễu (không trùng đáp án đúng)
            s = set()
            while len(s) < 3:
                fake = kq_dung + random.choice([-3, -2, -1, 1, 2, 3])
                if fake != kq_dung and fake > 0:
                    s.add(fake)

            list_options = list(s)
            da_s1 = f"${list_options[0]}$"
            da_s2 = f"${list_options[1]}$"
            da_s3 = f"${list_options[2]}$"
            da_d = f"\\True ${kq_dung}$"

            # Trộn đáp án
            list_all = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_all)

            # B3: Viết nội dung câu hỏi
            noidungcauhoi = (
                f"Đặt $a = \\log_{{{x}}} {y}$; $b = \\log_{{{z}}} {y}$. "
                f"Nếu biểu diễn $\\log_{{{base_log}}} {val_log} = \\frac{{a(m+nb)}}{{b(a+p)}}$ thì $m+n+p$ bằng bao nhiêu?"
            )

            # B4: Viết nội dung lời giải
            loigiai = (
                f"Ta có: $\\log_{{{base_log}}} {val_log} = \\frac{{\\log_{{{y}}} {val_log}}}{{\\log_{{{y}}} {base_log}}} "
                f"= \\frac{{\\log_{{{y}}} {y}^{{{k}}} + \\log_{{{y}}} {z}}}{{\\log_{{{y}}} {x} + \\log_{{{y}}} {y}}} "
                f"= \\frac{{{k} + \\frac{{1}}{{b}}}}{{\\frac{{1}}{{a}} + 1}} = \\frac{{\\frac{{{k}b+1}}{{b}}}}{{\\frac{{1+a}}{{a}}}} "
                f"= \\frac{{a({k}b+1)}}{{b(a+1)}}$.\\\\\n"
                f"Đối chiếu với giả thiết $\\frac{{a(m+nb)}}{{b(a+p)}}$, ta suy ra: "
                f"$m={m}, n={n}, p={p}$.\\\\\n"
                f"Vậy $m+n+p = {m} + {n} + {p} = {kq_dung}$."
            )
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq_dung))

            # Xuất câu trắc nghiệm theo mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

