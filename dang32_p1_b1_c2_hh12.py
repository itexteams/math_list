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


def bt_dang32_p1_b1_c2_hh12(self):
            def vecto(p1, p2):
                return Matrix([p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2]])

            # Random tọa độ điểm A, B
            A = [randint(-5, 5) for _ in range(3)]
            B = [randint(-5, 5) for _ in range(3)]

            # Random pháp tuyến nQ, đảm bảo không phải vecto không
            nq_coeff = [randint(-5, 5) for _ in range(3)]
            while sum(c**2 for c in nq_coeff) == 0:
                nq_coeff = [randint(-5, 5) for _ in range(3)]

            AB = vecto(A, B)
            nq = Matrix(nq_coeff)
            np = AB.cross(nq)

            # Kiểm tra nP không là vecto không (AB không cùng phương nQ)
            while np == Matrix([0, 0, 0]):
                A = [randint(-5, 5) for _ in range(3)]
                B = [randint(-5, 5) for _ in range(3)]
                nq_coeff = [randint(-5, 5) for _ in range(3)]
                while sum(c**2 for c in nq_coeff) == 0:
                    nq_coeff = [randint(-5, 5) for _ in range(3)]
                AB = vecto(A, B)
                nq = Matrix(nq_coeff)
                np = AB.cross(nq)

            # --- PHẦN SỬA LỖI HIỂN THỊ PHƯƠNG TRÌNH (Q) ---
            def format_plane_eq(coeffs, constant):
                vars = ['x', 'y', 'z']
                parts = []
                for i in range(3):
                    c = coeffs[i]
                    if c == 0: continue

                    # Xử lý dấu và hệ số
                    if c == 1:
                        term = vars[i]
                    elif c == -1:
                        term = "-" + vars[i]
                    else:
                        term = f"{c}{vars[i]}"

                    # Thêm dấu nối nếu không phải số hạng đầu tiên
                    if parts and c > 0:
                        parts.append("+" + term)
                    else:
                        parts.append(term)

                eq = "".join(parts)
                if constant > 0:
                    eq += f"+{constant}"
                elif constant < 0:
                    eq += f"{constant}"
                return eq + "=0"

            d = randint(-5, 5)
            q_eq = format_plane_eq(nq_coeff, d)
            # ----------------------------------------------

            # Format hiển thị tọa độ
            A_latex = "(%s;%s;%s)" % (latex(A[0]), latex(A[1]), latex(A[2]))
            B_latex = "(%s;%s;%s)" % (latex(B[0]), latex(B[1]), latex(B[2]))
            nq_latex = "(%s;%s;%s)" % (latex(nq[0]), latex(nq[1]), latex(nq[2]))
            np_latex = "(%s;%s;%s)" % (latex(np[0]), latex(np[1]), latex(np[2]))
            AB_latex = "(%s;%s;%s)" % (latex(AB[0]), latex(AB[1]), latex(AB[2]))

            # Đáp án đúng và sai
            kq_np_latex = "$%s$" % (np_latex)
            s = []
            while len(s) < 3:
                err = np + Matrix([randint(-3, 3) for _ in range(3)])
                if err != np and err.tolist() not in [x.tolist() for x in s]:
                    s.append(err)

            das = ["$(%s;%s;%s)$" % (latex(v[0]), latex(v[1]), latex(v[2])) for v in s]

            noidungcauhoi = ('''Trong không gian $Oxyz$, cho mặt phẳng $(P)$ đi qua hai điểm $A%s$, $B%s$ và vuông góc với mặt phẳng $(Q): %s$. Khi đó mặt phẳng $(P)$ có một vectơ pháp tuyến là'''
                            %(A_latex, B_latex, q_eq))

            da_d = ('\\True ' + str(kq_np_latex))
            list_1 = [da_d, das[0], das[1], das[2]]
            random.shuffle(list_1)

            loigiai=('''Mặt phẳng $(Q)$ có vectơ pháp tuyến là $\\vec{n}_Q = %s$. \\\\
