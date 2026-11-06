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


def bt_dang43_p1_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random vị trí n_target cần tìm (chọn n từ 3 đến 8)
                n_target = random.randint(3, 8)

                # Giá trị số hạng u_n = (n - 1) / (n^2 + 1)
                val = sp.Rational(n_target - 1, n_target**2 + 1)
                num = val.p  # tử số
                den = val.q  # mẫu số

                # Giải phương trình để lấy nghiệm còn lại làm lời giải chi tiết
                n_var = sp.Symbol('n')
                eq = sp.Eq(num * (n_var**2 + 1), den * (n_var - 1))
                roots = sp.solve(eq, n_var)

                other_root = None
                for r in roots:
                    if r != n_target:
                        other_root = r
                        break

                if other_root is not None:
                    if other_root.is_rational and other_root > 0 and other_root.is_integer:
                        str_other = 'n = %s \\text{ (thỏa mãn)}' % (sp.latex(other_root))
                    else:
                        str_other = 'n = %s \\text{ (loại do } n \\notin \\mathbb{N}^*)' % (sp.latex(other_root))
                    loigiai_nghiem = ('\\Leftrightarrow \\hoac{& n = %s \\text{ (thỏa mãn)} \\\\ & %s }.' % (n_target, str_other))
                else:
                    loigiai_nghiem = ('\\Leftrightarrow n = %s \\text{ (thỏa mãn)}' % (n_target))

                # Tạo danh sách các phương án sai
                candidates = [n_target - 2, n_target - 1, n_target + 1, n_target + 2, n_target + 3]
                valid_candidates = [c for c in candidates if c > 0 and c != n_target]
                random.shuffle(valid_candidates)
                distractors = valid_candidates[:3]
                distractors.sort()

                # Câu hỏi
                noidungcauhoi = ('Cho dãy số $(u_n)$, biết $u_n = \\frac{n-1}{n^2+1}$. Số $\\frac{%s}{%s}$ là số hạng thứ mấy của dãy số?' % (num, den))

                # Các đáp án
                da_d = ('\\True $%s$' % (n_target))
                da_s1 = ('$%s$' % (distractors[0]))
                da_s2 = ('$%s$' % (distractors[1]))
                da_s3 = ('$%s$' % (distractors[2]))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                pt_bien_doi = '%s(n^2+1) = %s(n-1)' % (num, den) if num != 1 else 'n^2+1 = %s(n-1)' % (den)
                pt_bac_2 = '%sn^2 - %sn + %s = 0' % (num if num != 1 else '', den, num + den)

                loigiai = ('Xét phương trình $u_n = \\frac{%s}{%s}$: \\\\ '
                           '$\\Leftrightarrow \\frac{n-1}{n^2+1} = \\frac{%s}{%s}$ \\\\ '
                           '$\\Leftrightarrow %s$ \\\\ '
                           '$\\Leftrightarrow %s$ \\\\ '
                           '$%s$ \\\\ '
                           'Vậy $\\frac{%s}{%s}$ là số hạng thứ $%s$ của dãy số.' 
                           % (num, den, num, den, pt_bien_doi, pt_bac_2, loigiai_nghiem, num, den, n_target))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

